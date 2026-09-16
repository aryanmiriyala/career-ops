"""Export the latest configured scan batch from cached employer directories."""
import csv
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from workspace_app.core import discovery


def board_url(source, token):
    if source == 'workday':
        tenant, instance, site = token.split('|', 2)
        return f'https://{tenant}.{instance}.myworkdayjobs.com/{site}'
    bases = {'greenhouse': 'https://boards.greenhouse.io/', 'lever': 'https://jobs.lever.co/',
             'ashby': 'https://jobs.ashbyhq.com/', 'smartrecruiters': 'https://jobs.smartrecruiters.com/'}
    return bases[source] + token


def main():
    state = json.loads((ROOT / '.local-workspace/scan.json').read_text())
    rows = []
    targets = discovery.load_json(discovery.DIRECT_ATS_TARGETS_PATH)['targets']
    batches = [('direct', targets)]
    for coverage in state.get('coverage', []):
        if coverage['layer'] != 'broad-ats':
            continue
        source = coverage['source']
        cache = discovery.BROAD_ATS_CACHE_DIR
        if not (cache / f'{source}.json').exists():
            raise SystemExit(f'Missing cached directory: {source}')
        entries = discovery.load_broad_ats_company_entries(source, cache)
        batches.append(('broad', discovery.company_batch(entries, state['company_limit'], state.get('company_offset', 0))))
    for layer, entries in batches:
        for entry in entries:
            rows.append([layer, entry['source'], entry['company'], board_url(entry['source'], entry['token'])])
    rows.extend([['public-feed', 'arbeitnow', '', 'https://www.arbeitnow.com/api/job-board-api'],
                 ['public-feed', 'remoteok', '', 'https://remoteok.com/api']])
    output = ROOT / state['results_dir'] / 'source-inventory.csv'
    with output.open('w', newline='') as handle:
        writer = csv.writer(handle)
        writer.writerow(['layer', 'source', 'company', 'url'])
        writer.writerows(rows)
    print(f'{len(rows)} targets/feed entries: {output}')
    print('Reconstructed from current caches and scan offset; not a per-request success log.')


if __name__ == '__main__':
    main()
