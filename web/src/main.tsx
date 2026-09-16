import React, { useEffect, useState } from 'react';
import { createRoot } from 'react-dom/client';
import { ArrowRight, BriefcaseBusiness, Check, ChevronLeft, ChevronRight, CircleAlert, Clock3, ExternalLink, FileText, KeyRound, LoaderCircle, LogOut, MapPin, Plus, RefreshCw, Search, ShieldCheck, Square, X } from 'lucide-react';
import './app.css';
import { authConfig, authorization, initializeAuth, supabase } from './auth';
import { Button } from './components/ui/button';
import { Dialog, DialogTitle } from './components/ui/dialog';

type Session = { authenticated: boolean; local_only?: boolean; setup_required?: boolean; email?: string };
type Job = { id: string; company: string; title: string; location: string; url: string; source: string; posted_at: string | null; first_seen_at: string | null; status: string; flags: string[]; score: number | null; notes: string; report: string; screening: { bucket: string; label: string; reason: string } };
type Board = { jobs: Job[]; total: number; stored: number; undated: number; sources: string[]; issues: string[]; last_seen_at: string | null };
type Scan = { status: string; message?: string; stage?: string; started_at?: string; finished_at?: string; company_limit?: number; results_dir?: string; source_errors?: number; fetched_jobs?: number; coverage?: { layer: string; source: string; fetched: number; errors: number; scanned?: number; available?: number }[] };
type Evidence = { id: string; source: string; line: number; heading: string; text: string };
type Intake = { id: string; company: string; title: string; status: string; mode: string; created_at: string; flags: string[]; jd?: string; brief?: { evidence: Evidence[]; unmatched_terms: string[]; characters: number; estimated_tokens: number; notice: string } };
type Provider = { id: string; name: string; configured: boolean; variables: string[]; check_kind: string };
type CheckResult = { status: string; message: string; latency_ms?: number; usage?: { total_tokens?: number } };

async function api<T>(path: string, body?: unknown): Promise<T> {
  const response = await fetch('/api' + path, { credentials: 'same-origin', headers: { ...await authorization(), ...(body !== undefined ? { 'Content-Type': 'application/json' } : {}) }, ...(body !== undefined ? { method: 'POST', body: JSON.stringify(body) } : {}) });
  const data = await response.json();
  if (!response.ok) {
    if (response.status === 401 && !path.startsWith('/auth/')) window.dispatchEvent(new Event('session-expired'));
    throw new Error(typeof data.detail === 'string' ? data.detail : 'Request failed.');
  }
  return data;
}
const date = (value?: string | null) => value ? new Date(value).toLocaleString([], { month: 'short', day: 'numeric', hour: 'numeric', minute: '2-digit' }) : 'Unknown';
const label = (value: string) => value.replaceAll('_', ' ');
function Busy() { return <LoaderCircle size={16} className="spin" aria-label="Loading"/>; }
function Notice({ children }: { children: React.ReactNode }) { return <div className="notice" role="status"><CircleAlert size={16}/><span>{children}</span></div>; }
function Badge({ value }: { value: string }) { return <span className={'badge ' + (value.includes('blocked') || value === 'failed' ? 'bad' : ['shortlist', 'verified', 'completed'].includes(value) ? 'good' : '')}>{label(value)}</span>; }

function Login({ session, onLogin }: { session: Session; onLogin: (s: Session) => void }) {
  const [error, setError] = useState(''); const [busy, setBusy] = useState(false);
  const setup = session.setup_required;
  const remote = authConfig.mode === 'supabase';
  return <div className="login-page"><div className="brand"><span className="brand-icon"><BriefcaseBusiness size={21}/></span>Career Ops</div><main className="login-main">
    <div className="eyebrow">LOCAL WORKSPACE</div><h1>{setup ? 'Create your account' : 'Welcome back'}</h1>
    <p className="muted">{setup ? 'Your private career workspace.' : 'Sign in to your career workspace.'}</p>
    {remote && !authConfig.configured && <Notice>{authConfig.message}</Notice>}
    <form onSubmit={async e => { e.preventDefault(); setBusy(true); setError(''); const data = new FormData(e.currentTarget); try { if (remote) { if (!supabase) throw new Error('Supabase is not configured.'); const { error } = await supabase.auth.signInWithPassword({ email: String(data.get('email')), password: String(data.get('password')) }); if (error) throw new Error('Sign-in failed. Check your credentials and email confirmation.'); const session = await api<Session>('/auth/session'); if (!session.authenticated) { await supabase.auth.signOut(); throw new Error('This account is not authorized for this workspace.'); } onLogin(session); } else { onLogin(await api<Session>('/auth/' + (setup ? 'setup' : 'login'), Object.fromEntries(data))); } } catch (e) { setError((e as Error).message); } finally { setBusy(false); } }}>
      <label>Email<input required name="email" type="email" autoComplete="username" autoFocus/></label>
      <label>Password<input required name="password" type="password" minLength={remote ? 1 : 12} maxLength={200} autoComplete={setup ? 'new-password' : 'current-password'}/></label>
      {setup && <span className="field-note">At least 12 characters</span>}
      {error && <Notice>{error}</Notice>}
      <Button variant="primary" className="w-full" disabled={busy || (remote && !authConfig.configured)}>{busy ? <Busy/> : <ArrowRight size={17}/>} {setup ? 'Create account' : 'Sign in'}</Button>
    </form><div className="login-foot"><ShieldCheck size={16}/>{remote ? 'Secured by Supabase Auth' : 'Single-owner local instance'}</div>
  </main><footer>Career Ops <span>Local development</span></footer></div>;
}

function IntakeForm({ job, onClose, onSave }: { job?: Job; onClose: () => void; onSave: (v: Intake) => void }) {
  const [mode, setMode] = useState('balanced'); const [busy, setBusy] = useState(false); const [error, setError] = useState('');
  const descriptions: Record<string, string> = { faithful: 'Verified facts. Light rephrasing.', balanced: 'Verified facts. Natural role alignment.', aggressive: 'Verified facts. Stronger project selection and emphasis.' };
  return <Dialog onClose={onClose}><DialogTitle className="mb-6 pr-8 text-[22px] font-semibold leading-7">New application intake</DialogTitle>
    <form onSubmit={async e => { e.preventDefault(); const data = new FormData(e.currentTarget); setBusy(true); setError(''); try { onSave(await api<Intake>('/intakes', { ...Object.fromEntries(data), mode })); } catch (e) { setError((e as Error).message); } finally { setBusy(false); } }}>
      <div className="grid min-w-0 grid-cols-1 gap-x-3 sm:grid-cols-2"><label>Company<input name="company" defaultValue={job?.company} maxLength={150} required autoFocus/></label><label>Role<input name="title" defaultValue={job?.title} maxLength={200} required/></label></div>
      <label>Posting URL<input name="url" type="url" defaultValue={job?.url} maxLength={2000}/></label>
      <label>Full job description<textarea name="jd" required minLength={100} maxLength={80000} rows={9}/></label>
      <fieldset className="min-w-0"><legend className="mb-2 text-xs font-medium">Tailoring mode</legend><div className="grid grid-cols-3 gap-1 rounded-[5px] border border-line bg-soft p-1">{['faithful', 'balanced', 'aggressive'].map(m => <Button type="button" variant="ghost" aria-pressed={m === mode} className={'min-w-0 px-1 text-xs ' + (m === mode ? 'bg-white text-accent shadow-sm' : '')} key={m} onClick={() => setMode(m)}>{m[0].toUpperCase() + m.slice(1)}</Button>)}</div></fieldset>
      <p className="field-note">{descriptions[mode]}</p>
      {error && <Notice>{error}</Notice>}
      <div className="mt-5 flex flex-wrap items-center justify-between gap-3 border-t border-line pt-4 text-xs"><span className="muted">0 model calls</span><Button variant="primary" disabled={busy}>{busy ? <Busy/> : <FileText size={16}/>}Save & review evidence</Button></div>
    </form></Dialog>;
}

function Jobs({ onIntake }: { onIntake: (job: Job) => void }) {
  const [board, setBoard] = useState<Board>(); const [scan, setScan] = useState<Scan>({ status: 'idle' });
  const [q, setQ] = useState(''); const [hours, setHours] = useState('48'); const [basis, setBasis] = useState('posted'); const [scope, setScope] = useState('all'); const [source, setSource] = useState(''); const [page, setPage] = useState(1);
  const [selected, setSelected] = useState<Job>(); const [error, setError] = useState(''); const [loading, setLoading] = useState(false); const [revision, setRevision] = useState(0); const [limit, setLimit] = useState('100');
  const running = ['running', 'cancelling'].includes(scan.status);
  useEffect(() => { let live = true; const poll = async () => { try { const s = await api<Scan>('/scans/current'); if (live) setScan(old => { if (old.status !== s.status) setRevision(v => v + 1); return s; }); } catch (e) { if (live) setError((e as Error).message); } }; void poll(); const id = setInterval(poll, 3000); return () => { live = false; clearInterval(id); }; }, []);
  useEffect(() => { let live = true; setLoading(true); const id = setTimeout(async () => { try { const b = await api<Board>('/jobs?' + new URLSearchParams({ q, hours, basis, scope, source, page: String(page) })); if (live) { setBoard(b); setError(''); } } catch (e) { if (live) setError((e as Error).message); } finally { if (live) setLoading(false); } }, 180); return () => { live = false; clearTimeout(id); }; }, [q, hours, basis, scope, source, page, revision]);
  return <><header className="page-heading"><div><div className="eyebrow">DISCOVERY</div><h1>Job board</h1><p className="muted">Last seen {date(board?.last_seen_at)}</p></div><div className="scan-actions"><label className="sr-only" htmlFor="scan-limit">Scan scope</label><select id="scan-limit" value={limit} disabled={running} onChange={e => setLimit(e.target.value)}><option value="100">100 boards / source</option><option value="250">250 boards / source</option><option value="20">20 boards / source</option><option value="0">All boards</option></select><button className="primary" disabled={running} onClick={async () => { try { setScan(await api<Scan>('/scans', { company_limit: Number(limit) })); } catch (e) { setError((e as Error).message); } }}>{running ? <Busy/> : <RefreshCw size={16}/>}Refresh postings</button></div></header>
    <div className="metrics"><div><span>U.S. postings in this view</span><strong>{board?.total ?? '—'}</strong></div><div><span>Stored U.S. postings</span><strong>{board?.stored ?? '—'}</strong></div><div><span>Unknown posted date</span><strong>{board?.undated ?? '—'}</strong></div><div><span>Discovery model calls</span><strong>0<span className="metric-unit"> / scan</span></strong></div></div>
    {scan.status !== 'idle' && <div className="scan-strip"><span>{running && <Busy/>}<Badge value={scan.status}/>{scan.company_limit === 0 ? 'Full scan' : `${scan.company_limit ?? ''} broad boards per source`}<span className="muted">{date(scan.started_at)}</span></span>{running && <button className="quiet" onClick={async () => setScan(await api<Scan>('/scans/cancel', {}))}><Square size={13}/>Cancel scan</button>}</div>}
    {error && <Notice>{error}</Notice>}
    {!!board?.issues.length && <Notice>{board.issues.length} report files could not be loaded.</Notice>}
    {!!scan.source_errors && <Notice>{scan.source_errors} source requests failed. {scan.fetched_jobs ?? 0} postings were fetched before filtering. Results may be incomplete.</Notice>}
    {running && scan.stage && <p className="text-xs text-subtle" role="status">Scanning: {label(scan.stage)}</p>}
    {!!scan.coverage?.length && <details className="mb-5"><summary>Source coverage · {date(scan.finished_at)}</summary><div className="overflow-x-auto"><table className="mt-3 w-full"><thead><tr><th>Source</th><th>Layer</th><th>Boards scanned</th><th>Fetched</th><th>Failures</th></tr></thead><tbody>{scan.coverage.map(s => <tr key={s.layer + s.source}><td>{s.source}</td><td>{s.layer}</td><td>{s.scanned == null ? 'Not recorded' : `${s.scanned} / ${s.available}`}</td><td>{s.fetched}</td><td>{s.errors}</td></tr>)}</tbody></table></div></details>}
    <div className="filters"><div className="search-box"><Search size={17}/><input aria-label="Search jobs" placeholder="Search role, company, location" value={q} onChange={e => { setQ(e.target.value); setPage(1); }}/></div>
      <select aria-label="Date basis" value={basis} onChange={e => { setBasis(e.target.value); setPage(1); }}><option value="posted">Posted date</option><option value="discovered">First discovered</option></select>
      <select aria-label="Time window" value={hours} onChange={e => { setHours(e.target.value); setPage(1); }}><option value="6">Last 6 hours</option><option value="12">Last 12 hours</option><option value="24">Last 24 hours</option><option value="48">Last 48 hours</option><option value="168">Last 7 days</option><option value="0">All stored dates</option></select>
      <select aria-label="Source" value={source} onChange={e => { setSource(e.target.value); setPage(1); }}><option value="">All sources</option>{board?.sources.map(s => <option key={s}>{s}</option>)}</select>
    </div>
    <div className="view-tabs">{['all', 'shortlist', 'review', 'blocked', 'unassessed'].map(s => <button key={s} className={scope === s ? 'active' : ''} onClick={() => { setScope(s); setPage(1); }}>{{ all: 'All postings', shortlist: 'Rule matches', review: 'Check fit', blocked: 'Eligibility flags', unassessed: 'Not assessed' }[s]}</button>)}{loading && <Busy/>}</div>
    <div className="board-content"><div className="table-wrap"><table><thead><tr><th>Company / role</th><th>Location</th><th>{basis === 'posted' ? 'Posted' : 'First discovered'}</th><th>Discovery filter</th><th><span className="sr-only">Details</span></th></tr></thead><tbody>{board?.jobs.map(job => <tr key={job.id} className={selected?.id === job.id ? 'selected-row' : ''}><td><div className="mb-1 text-[15px] font-semibold text-ink">{job.company}</div><button className="job-title" onClick={() => setSelected(job)}>{job.title}</button><div className="mt-1 text-xs text-subtle">{job.source}</div></td><td>{job.location}</td><td className="date-cell">{date(basis === 'posted' ? job.posted_at : job.first_seen_at)}</td><td><span title={job.screening.reason}><Badge value={job.screening.label}/></span></td><td><button className="icon" title="View job" aria-label={'View ' + job.title} onClick={() => setSelected(job)}><ChevronRight size={18}/></button></td></tr>)}</tbody></table>
      {!loading && board?.total === 0 && <div className="empty"><Search size={27}/><h3>No postings in this view</h3><p>{hours !== '0' ? 'Refresh sources or choose another time window.' : 'Try another search or refresh sources.'}</p>{hours !== '0' && <button className="quiet" onClick={() => { setHours('0'); setPage(1); }}>View all stored dates<ArrowRight size={15}/></button>}</div>}
    </div></div>
    <div className="pagination"><span>{board?.total ?? 0} matches · {basis === 'posted' ? 'Unknown posting dates excluded from timed windows' : 'Discovery time is not publication time'}</span><div><button className="icon" title="Previous page" aria-label="Previous page" disabled={page === 1} onClick={() => setPage(v => v - 1)}><ChevronLeft size={18}/></button><span>Page {page}</span><button className="icon" title="Next page" aria-label="Next page" disabled={page * 30 >= (board?.total ?? 0)} onClick={() => setPage(v => v + 1)}><ChevronRight size={18}/></button></div></div>
    {selected && <Dialog sheet onClose={() => setSelected(undefined)}><div className="mb-6 pr-9"><Badge value={selected.screening.label}/></div><div className="mb-2 text-base font-semibold">{selected.company}</div><DialogTitle className="mb-4 text-[22px] font-semibold leading-7">{selected.title}</DialogTitle><p className="location"><MapPin size={16}/>{selected.location}</p><dl><dt>Posted</dt><dd>{date(selected.posted_at)}</dd><dt>First discovered</dt><dd>{date(selected.first_seen_at)}</dd><dt>Source</dt><dd>{selected.source}</dd><dt>Discovery filter</dt><dd>{selected.screening.reason}</dd><dt>Keyword heuristic (not resume alignment)</dt><dd>{selected.score == null ? 'Not recorded' : `${selected.score}/100`}</dd></dl><div className="flag-list">{selected.flags.map(f => <Badge key={f} value={f}/>)}</div>{selected.notes && <p className="muted">{selected.notes}</p>}<div className="drawer-actions"><Button asChild><a href={selected.url} target="_blank" rel="noopener noreferrer">Open posting<ExternalLink size={16}/></a></Button><Button variant="primary" onClick={() => { onIntake(selected); setSelected(undefined); }}><FileText size={16}/>Review evidence</Button></div></Dialog>}
  </>;
}

function Applications({ current, onSelect, onNew }: { current?: Intake; onSelect: (i: Intake) => void; onNew: () => void }) {
  const [items, setItems] = useState<Intake[]>([]); const [error, setError] = useState('');
  useEffect(() => { api<Intake[]>('/intakes').then(setItems).catch(e => setError(e.message)); }, [current]);
  return <><header className="page-heading"><div><div className="eyebrow">APPLICATIONS</div><h1>Evidence workspace</h1><p className="muted">{items.length} saved intakes</p></div><button className="primary" onClick={onNew}><Plus size={17}/>New intake</button></header>{error && <Notice>{error}</Notice>}
    <div className="application-layout"><div className="intake-list">{items.map(item => <button key={item.id} className={'intake-item ' + (current?.id === item.id ? 'selected' : '')} onClick={async () => { try { onSelect(await api<Intake>('/intakes/' + item.id)); } catch (e) { setError((e as Error).message); } }}><span className="muted">{item.company}</span><strong>{item.title}</strong><Badge value={item.status}/><small>{date(item.created_at)}</small></button>)}{items.length === 0 && <p className="muted">No saved intakes yet.</p>}</div>
    <section className="evidence-panel">{current ? <><div className="panel-heading"><div><div className="eyebrow">{current.company}</div><h2>{current.title}</h2></div><Badge value={current.mode}/></div><Notice>{current.status === 'eligibility_blocked' ? 'Explicit work-authorization blocker detected. This intake is blocked.' : 'Drafting and submission validation are not enabled in this build. Evidence selection needs review.'}</Notice><div className="brief-stats"><span><strong>{current.brief?.evidence.length ?? 0}</strong> source excerpts</span><span><strong>{current.brief?.estimated_tokens ?? 0}</strong> estimated evidence tokens</span><span><strong>0</strong> model calls</span></div><h3>Evidence candidates</h3>{current.brief?.evidence.map(e => <article className="evidence-item" key={e.id}><h4>{e.heading || e.source}</h4><p>{e.text}</p><div className="evidence-source">{e.source}:{e.line}<code>{e.id}</code></div></article>)}{!current.brief?.evidence.length && <p className="muted">No lexical evidence matches. Source review is required.</p>}<details><summary>Unmatched terms ({current.brief?.unmatched_terms.length ?? 0})</summary><p>{current.brief?.unmatched_terms.join(', ')}</p><p className="muted">{current.brief?.notice}</p></details><details><summary>Saved job description</summary><pre className="jd-text">{current.jd}</pre></details></> : <div className="empty"><FileText size={28}/><h3>Select an intake</h3><p>Job descriptions and evidence candidates appear here.</p></div>}</section></div>
  </>;
}

function Providers() {
  const [data, setData] = useState<{ providers: Provider[]; langfuse_configured: boolean }>(); const [checks, setChecks] = useState<Record<string, CheckResult>>({}); const [busy, setBusy] = useState(''); const [error, setError] = useState('');
  useEffect(() => { api<typeof data>('/providers').then(setData).catch(e => setError(e.message)); }, []);
  return <><header className="page-heading"><div><div className="eyebrow">SETTINGS</div><h1>Model providers</h1><p className="muted">Local credentials · generation disabled</p></div><span className="pill"><ShieldCheck size={15}/>Keys stay server-side</span></header>{error && <Notice>{error}</Notice>}
    <div className="provider-list">{data?.providers.map(p => <section className="provider-row" key={p.id}><div className="provider-icon"><KeyRound size={20}/></div><div className="provider-info"><h3>{p.name}<span className={'dot ' + (p.configured ? 'configured' : '')}/></h3><code>{p.variables.join(' / ')}</code>{checks[p.id] && <p className={checks[p.id].status === 'failed' ? 'error-text' : 'muted'}>{checks[p.id].message}{checks[p.id].latency_ms != null && ` · ${checks[p.id].latency_ms} ms`}{checks[p.id].usage?.total_tokens != null && ` · ${checks[p.id].usage?.total_tokens} tokens`}</p>}</div><span className="muted">{p.configured ? 'Configured' : 'Not set'}</span><button disabled={!p.configured || !!busy} onClick={async () => { setBusy(p.id); try { const result = await api<CheckResult>('/providers/' + p.id + '/check', {}); setChecks(v => ({ ...v, [p.id]: result })); } catch (e) { setError((e as Error).message); } finally { setBusy(''); } }}>{busy === p.id ? <Busy/> : <Check size={15}/>} {p.id === 'zai' ? 'Test free model' : 'Check connection'}</button></section>)}</div>
    <section className="settings-note"><h3>Observability</h3><p>Langfuse credentials: {data?.langfuse_configured ? 'configured' : 'not set'}. Trace integration is pending.</p><h3>Provider checks</h3><p>Z.ai runs a short, synthetic GLM-4.7-Flash completion. Other checks request account or model metadata without generating text. Connection success does not establish free quota.</p></section>
  </>;
}

function App() {
  const [session, setSession] = useState<Session>(); const [error, setError] = useState(''); const [view, setView] = useState('jobs'); const [modal, setModal] = useState<{ job?: Job }>(); const [current, setCurrent] = useState<Intake>();
  useEffect(() => { initializeAuth().then(() => api<Session>('/auth/session')).then(setSession).catch(e => setError(e.message)); const expire = () => setSession({ authenticated: false }); window.addEventListener('session-expired', expire); return () => window.removeEventListener('session-expired', expire); }, []);
  useEffect(() => { const close = (e: KeyboardEvent) => { if (e.key === 'Escape') setModal(undefined); }; window.addEventListener('keydown', close); return () => window.removeEventListener('keydown', close); }, []);
  if (!session) return <div className="initial">{error ? <Notice>{error}</Notice> : <Busy/>}</div>;
  if (!session.authenticated) return <Login session={session} onLogin={setSession}/>;
  return <div className="shell"><aside className="sidebar"><div className="brand"><span className="brand-icon"><BriefcaseBusiness size={21}/></span>Career Ops</div><div className="sidebar-label">WORKSPACE</div><nav>{[{ id: 'jobs', title: 'Job board', icon: Search }, { id: 'applications', title: 'Evidence', icon: FileText }, { id: 'providers', title: 'Providers', icon: KeyRound }].map(({ id, title, icon: Icon }) => <button key={id} className={view === id ? 'active' : ''} onClick={() => setView(id)}><Icon size={18}/>{title}{view === id && <ChevronRight size={14}/>}</button>)}</nav><div className="sidebar-bottom"><div className="local-indicator"><span className="dot configured"/>Local instance</div><div className="account" style={session.local_only ? { display: "none" } : undefined}><span title={session.email}>{session.email}</span><button className="icon" title="Sign out" aria-label="Sign out" onClick={async () => { try { await api('/auth/logout', {}); } finally { await supabase?.auth.signOut(); setSession({ authenticated: false }); } }}><LogOut size={17}/></button></div></div></aside>
    <main className="main"><div className="topbar"><span><BriefcaseBusiness size={14}/>Personal workspace<ChevronRight size={13}/>{view === 'jobs' ? 'Job board' : view === 'applications' ? 'Evidence' : 'Providers'}</span><span><Clock3 size={13}/>{new Date().toLocaleDateString([], { month: 'short', day: 'numeric', year: 'numeric' })}</span></div><div className="page">{view === 'jobs' ? <Jobs onIntake={job => setModal({ job })}/> : view === 'applications' ? <Applications current={current} onSelect={setCurrent} onNew={() => setModal({})}/> : <Providers/>}</div></main>
    {modal && <IntakeForm job={modal.job} onClose={() => setModal(undefined)} onSave={intake => { setCurrent(intake); setModal(undefined); setView('applications'); }}/>}</div>;
}
createRoot(document.getElementById('root')!).render(<App/>);
