import { createClient, type SupabaseClient } from '@supabase/supabase-js';

export type AuthConfig = { mode: 'local' | 'supabase'; configured?: boolean; url?: string; publishable_key?: string; message?: string };
export let authConfig: AuthConfig = { mode: 'local' };
export let supabase: SupabaseClient | null = null;

export async function initializeAuth() {
  const response = await fetch('/api/auth/config');
  if (!response.ok) throw new Error('Unable to load sign-in configuration.');
  authConfig = await response.json();
  if (authConfig.mode === 'supabase' && authConfig.configured && !supabase) {
    supabase = createClient(authConfig.url!, authConfig.publishable_key!, { auth: { flowType: 'pkce' } });
  }
}

export async function authorization(): Promise<Record<string, string>> {
  if (!supabase) return {};
  const { data } = await supabase.auth.getSession();
  return data.session ? { Authorization: `Bearer ${data.session.access_token}` } : {};
}
