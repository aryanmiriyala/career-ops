"""Single-provider requests, persisted usage, and metadata-only Langfuse telemetry."""
import json
import time
from contextlib import contextmanager

import httpx

from .core import now_iso, write_json
from .providers import PROVIDERS, credentials

BASES = {
    'zai': 'https://api.z.ai/api/paas/v4',
    'openrouter': 'https://openrouter.ai/api/v1',
    'groq': 'https://api.groq.com/openai/v1',
    'gemini': 'https://generativelanguage.googleapis.com/v1beta/openai',
    'opencode': 'https://opencode.ai/zen/v1',
    'mistral': 'https://api.mistral.ai/v1',
    'featherless': 'https://api.featherless.ai/v1',
    'cerebras': 'https://api.cerebras.ai/v1',
    'deepseek': 'https://api.deepseek.com/v1',
    'together': 'https://api.together.xyz/v1',
    'cloudflare': 'https://api.cloudflare.com/client/v4/accounts/{account_id}/ai',
    'huggingface': 'https://api-inference.huggingface.co',
    'ollama': 'http://localhost:11434/v1',
    'lmstudio': 'http://localhost:1234/v1',
    'local_openai': 'custom',
}


def get_base_url(provider, values):
    """Get the base URL for a provider, substituting env vars where needed."""
    base = BASES[provider]
    if provider == 'cloudflare':
        account_id = values.get('CLOUDFLARE_ACCOUNT_ID')
        if not account_id:
            raise ValueError('CLOUDFLARE_ACCOUNT_ID required for Cloudflare provider')
        base = base.format(account_id=account_id)
    elif provider == 'local_openai':
        custom_base = values.get('LOCAL_OPENAI_COMPATIBLE_BASE_URL')
        if not custom_base:
            raise ValueError('LOCAL_OPENAI_COMPATIBLE_BASE_URL required for local_openai provider')
        base = custom_base.rstrip('/')
    elif provider in ('ollama', 'lmstudio'):
        # Allow override via env vars
        if provider == 'ollama':
            override = values.get('OLLAMA_BASE_URL')
        else:
            override = values.get('LM_STUDIO_BASE_URL')
        if override:
            base = override.rstrip('/v1').rstrip('/') + '/v1'
    return base


# Providers that are free/local and don't require allow_paid
FREE_PROVIDERS = {
    'zai': 'glm-4.7-flash',
    'ollama': None,  # any model
    'lmstudio': None,
    'local_openai': None,
}


def allowed_route(provider, model, allow_paid):
    if provider not in BASES:
        raise ValueError('Unsupported provider')
    # Free/local providers don't require allow_paid
    if provider in FREE_PROVIDERS:
        free_model = FREE_PROVIDERS[provider]
        if free_model is None or model == free_model:
            return
    # Do not infer free quota from the existence of a key or a model name.
    if not allow_paid:
        raise ValueError('This route requires explicit paid/quota usage approval; no fallback was made')


class Telemetry:
    def __init__(self, root):
        self.client = None
        self.status = 'not_configured'
        values = credentials(root)
        if values.get('LANGFUSE_PUBLIC_KEY') and values.get('LANGFUSE_SECRET_KEY'):
            try:
                from langfuse import Langfuse
                self.client = Langfuse(public_key=values['LANGFUSE_PUBLIC_KEY'],
                                      secret_key=values['LANGFUSE_SECRET_KEY'],
                                      base_url=values.get('LANGFUSE_BASE_URL') or values.get('LANGFUSE_HOST'),
                                      timeout=5)
                self.status = 'enabled_metadata_only'
            except Exception:
                self.status = 'unavailable_local_usage_retained'

    @contextmanager
    def generation(self, name, model, run_id):
        span = None
        if self.client:
            try:
                span = self.client.start_observation(name=name, as_type='generation', model=model,
                                                      metadata={'run_id': run_id, 'content_redacted': True})
            except Exception:
                self.status = 'unavailable_local_usage_retained'
        try:
            yield span
        finally:
            if span:
                try:
                    span.end()
                except Exception:
                    self.status = 'unavailable_local_usage_retained'

    def flush(self):
        if self.client:
            try:
                self.client.flush()
            except Exception:
                self.status = 'unavailable_local_usage_retained'


class Transport:
    def __init__(self, root, telemetry=None, client_factory=httpx.Client):
        self.root, self.telemetry, self.client_factory = root, telemetry or Telemetry(root), client_factory

    def complete(self, directory, run_id, stage, schema, system, payload, config, review=False):
        provider = config.review_provider if review else config.provider
        model = config.review_model if review else config.model
        allowed_route(provider, model, config.allow_paid)
        values = credentials(self.root)
        key = next((values.get(a) for a in PROVIDERS[provider][1] if values.get(a)), None)
        if not key and provider not in ('ollama', 'lmstudio', 'local_openai'):
            raise ValueError('No configured key for selected provider')
        messages = [{'role': 'system', 'content': system + '\nReturn only JSON matching this schema:\n' + json.dumps(schema.model_json_schema())},
                    {'role': 'user', 'content': json.dumps(payload, ensure_ascii=True)}]
        # UTF-8 bytes plus framing is a conservative input reservation, not measured tokens.
        reservation = len(json.dumps(messages).encode()) + 1024 + config.max_output_tokens
        ledger_path = directory / 'usage.json'
        ledger = json.loads(ledger_path.read_text()) if ledger_path.exists() else []
        used = sum(item['reserved_tokens'] for item in ledger)
        if used + reservation > config.token_budget:
            raise ValueError('Run token reservation budget exhausted; no request was sent')
        record = {'stage': stage, 'provider': provider, 'requested_model': model, 'started_at': now_iso(),
                  'reserved_tokens': reservation, 'status': 'request_started', 'usage': None, 'cost': None}
        ledger.append(record)
        write_json(ledger_path, ledger)
        body = {'model': model, 'messages': messages, 'max_tokens': config.max_output_tokens,
                'response_format': {'type': 'json_object'}}
        if provider == 'zai':
            body['thinking'] = {'type': 'disabled'}
        start = time.monotonic()
        try:
            with self.telemetry.generation(stage, model, run_id) as span:
                with self.client_factory(timeout=180, follow_redirects=False) as client:
                    base_url = get_base_url(provider, values)
                    headers = self._build_headers(provider, key, values)
                    response = client.post(base_url + '/chat/completions', headers=headers, json=body)
                if response.status_code != 200:
                    record['http_status'] = response.status_code
                    raise ValueError(f'Provider returned HTTP {response.status_code}; no automatic retry or fallback')
                data = response.json()
                usage = data.get('usage', {})
                record.update(usage={k: v for k, v in usage.items() if k in {'prompt_tokens', 'completion_tokens', 'total_tokens', 'prompt_tokens_details', 'completion_tokens_details', 'cost'}},
                              served_model=data.get('model', model), cost=usage.get('cost'), status='response_received')
                write_json(ledger_path, ledger)
                if span:
                    try:
                        span.update(usage_details={k: v for k, v in {'input': usage.get('prompt_tokens'), 'output': usage.get('completion_tokens')}.items() if isinstance(v, int)})
                    except Exception:
                        self.telemetry.status = 'unavailable_local_usage_retained'
                choice = data['choices'][0]
                if choice.get('finish_reason') not in {'stop', None}:
                    raise ValueError('Provider output was incomplete; draft not accepted')
                result = schema.model_validate_json(choice['message']['content'])
                record['status'] = 'validated'
                return result
        except Exception as exc:
            record['status'] = 'failed_or_billing_uncertain'
            if isinstance(exc, ValueError) and not hasattr(exc, 'errors'):
                raise
            raise ValueError('Provider response or schema validation failed; usage retained, no automatic retry') from None
        finally:
            record['latency_ms'] = round((time.monotonic() - start) * 1000)
            record['finished_at'] = now_iso()
            write_json(ledger_path, ledger)

    def _build_headers(self, provider, key, values):
        if provider == 'gemini':
            return {'x-goog-api-key': key}
        elif provider == 'cloudflare':
            return {'Authorization': f'Bearer {key}', 'Content-Type': 'application/json'}
        elif provider in ('ollama', 'lmstudio', 'local_openai'):
            # Local providers may not need auth, but include if key exists
            if key:
                return {'Authorization': f'Bearer {key}', 'Content-Type': 'application/json'}
            return {'Content-Type': 'application/json'}
        else:
            return {'Authorization': f'Bearer {key}', 'Content-Type': 'application/json'}
