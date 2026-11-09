export const PR_URL = 'https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5751';
export const MERGE = '205e344ea8d05077414d3a0f8606512b66272be5';
export const SOURCE_ROOT = `https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/${MERGE}/`;
export const STORAGE_KEY = 'kfm-recovery-workspace-v1';
export const FEEDS = [
  { id: 'iem', name: 'IEM Wind', short: 'IEM', description: 'Iowa Environmental Mesonet', source: 'iem-wind', failures: 3, reason: 'HTTP_429', duration: 'within 3 seconds', shape: 'Monthly windows · 16 stations per batch', wait: '5s between batches · 12 months / run', file: 'sql_feed_sources.py', color: 'olive', cursor: 'obs_backfill_next / obs_backfill_month / obs_backfill_batch', tables: 'iem-wind-observations → kfm_wind_observations; iem-wind-daily → kfm_wind_daily', note: '67 stations in PR; runbook lists 68. Confirm the catalog used by the run.' },
  { id: 'usgs', name: 'USGS daily observations', short: 'USGS', description: 'United States Geological Survey', source: 'usgs-daily', failures: 5, reason: 'USGS_RATE_LIMITED', duration: 'after ~5 minutes per series', shape: '25-year spans · from year before period_begin', wait: '5s between series · EARLIEST fallback', file: 'sql_feed_water.py', color: 'sage', cursor: 'Existing per-series backfill state', tables: 'usgs-daily-record / usgs-daily-modified → kfm_usgs_daily_values; kfm_usgs_series and kfm_usgs_sites retained', note: 'Source identity per time_series_id / time is preserved in merged code. Local tables have not been inspected.' },
  { id: 'wikidata', name: 'Wikidata Kansas', short: 'WD', description: 'Kansas entity queries', source: 'wikidata-kansas', failures: 3, reason: 'WIKIDATA_RATE_LIMITED', duration: 'after 221 seconds', shape: 'Existing cycle / items / ranges resume', wait: '2s between queries · 400-query cap', file: 'sql_feed_wikidata_plss.py', color: 'clay', cursor: 'Existing cycle / items / ranges', tables: 'wikidata-places / wikidata-places-box → kfm_wikidata_places; wikidata-people → kfm_wikidata_people; wikidata-events → kfm_wikidata_events', note: 'Repeated queries count against the 400-query cap. Installed resume behavior remains unverified.' },
] as const;
export type FeedId = typeof FEEDS[number]['id'];
export const EVIDENCE_TYPES = ['release identity', 'database preservation', 'read-only status', 'journal', 'provider response', 'backfill receipt', 'targeted test', 'source', 'reviewer/retest'] as const;
export type EvidenceType = typeof EVIDENCE_TYPES[number];
export type Evidence = { id: string; type: EvidenceType; title: string; observedAt: string; reference: string; excerpt: string; sha256: string; scope: string; limitations: string; createdAt: string; imported?: boolean };
export const PHASES = ['before #5751', 'after #5751', 'unknown'] as const;
export const OUTCOMES = ['not executed', 'waiting', 'stopped', 'completed', 'failed', 'partial'] as const;
export const NUMERIC_FIELDS = ['attempts', 'waitedSeconds', 'rowsRetained', 'rowsLoaded', 'rowsUnchanged', 'rowsPending'] as const;
export type RunRecord = {
  runId: string; feed: FeedId; phase: typeof PHASES[number]; observedAt: string; release: string; commit: string; catalogIdentity: string;
  readOnly: 'unknown' | 'confirmed read-only' | 'not read-only'; journal: string; providerResponse: string; retryAfter: string;
  attempts: string; actualWaits: string; waitedSeconds: string; outcome: typeof OUTCOMES[number]; cursorBefore: string; cursorAfter: string;
  rowsRetained: string; rowsLoaded: string; rowsUnchanged: string; rowsPending: string; receipt: string; retest: string; gaps: string; evidenceIds: string[];
};
export type Revision = { revision: number; savedAt: string; record: RunRecord };
export type Run = { id: string; revisions: Revision[]; imported?: boolean };
export type Decision = { id: string; runId: string; revision: number; reviewer: string; decision: 'needs evidence' | 'accepted for stated scope' | 'rejected'; scope: string; rationale: string; evidenceIds: string[]; retest: string; createdAt: string };
export type Workspace = { version: 1; evidence: Evidence[]; runs: Run[]; decisions: Decision[]; importHistory: { at: string; note: string }[]; seedProvenance: { pr: string; merge: string; verifiedOn: string; boundary: string } };
export const newWorkspace = (): Workspace => ({ version: 1, evidence: [], runs: [], decisions: [], importHistory: [], seedProvenance: { pr: PR_URL, merge: MERGE, verifiedOn: '2026-11-08', boundary: 'Merged source confirmed via GitHub. Historical journals and tests are author-reported; installed machine and feed executions not inspected.' } });
export const blankRun = (feed: FeedId = 'iem'): RunRecord => ({ runId: '', feed, phase: 'after #5751', observedAt: '', release: '', commit: '', catalogIdentity: '', readOnly: 'unknown', journal: '', providerResponse: '', retryAfter: '', attempts: '', actualWaits: '', waitedSeconds: '', outcome: 'not executed', cursorBefore: '', cursorAfter: '', rowsRetained: '', rowsLoaded: '', rowsUnchanged: '', rowsPending: '', receipt: '', retest: '', gaps: '', evidenceIds: [] });
export const latest = (run: Run): Revision => run.revisions[run.revisions.length - 1];
export const isTimestamp = (value: unknown): value is string => typeof value === 'string' && /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{1,3})?Z$/.test(value) && Number.isFinite(Date.parse(value)) && new Date(value).toISOString().slice(0, 19) === value.slice(0, 19);
export const validReference = (value: string) => !/^[a-z][a-z\d+.-]*:/i.test(value) || /^https?:\/\//i.test(value);
export const safeUrl = (value: string): string | undefined => { try { const u = new URL(value); return ['http:', 'https:'].includes(u.protocol) ? u.href : undefined; } catch { return undefined; } };
export function validateRecord(record: RunRecord): string[] {
  const errors: string[] = [];
  if (!record.runId.trim()) errors.push('A run identifier is required.');
  if (!FEEDS.some(f => f.id === record.feed)) errors.push('Choose a known feed.');
  if (!isTimestamp(record.observedAt)) errors.push('Enter a valid UTC timestamp, for example 2026-11-08T19:30:00Z.');
  if (!PHASES.includes(record.phase) || !OUTCOMES.includes(record.outcome)) errors.push('Choose a valid phase and outcome.');
  if (!['unknown', 'confirmed read-only', 'not read-only'].includes(record.readOnly)) errors.push('Choose a valid read-only status.');
  for (const key of NUMERIC_FIELDS) if (record[key] !== '' && (!Number.isFinite(Number(record[key])) || Number(record[key]) < 0 || !/^\d+(?:\.\d+)?$/.test(record[key]) || (key !== 'waitedSeconds' && !Number.isInteger(Number(record[key]))))) errors.push(`${key} must be a finite, nonnegative ${key === 'waitedSeconds' ? 'number' : 'whole number'}, or blank.`);
  if (record.actualWaits.trim() && record.actualWaits.split(',').some(v => !/^\s*\d+(?:\.\d+)?\s*$/.test(v) || !Number.isFinite(Number(v)))) errors.push('Actual waits must be a comma-separated list of nonnegative seconds.');
  if (record.actualWaits.trim() && record.waitedSeconds !== '' && record.actualWaits.split(',').every(v => /^\s*\d+(?:\.\d+)?\s*$/.test(v) && Number.isFinite(Number(v)))) { const sum = record.actualWaits.split(',').reduce((n,v) => n + Number(v), 0); if (Math.abs(sum - Number(record.waitedSeconds)) > 0.000001) errors.push('Recorded total waiting seconds must equal the sum of actual waits, or leave the total unknown.'); }
  if (record.commit && !/^[a-f0-9]{7,40}$/i.test(record.commit)) errors.push('Use a 7–40 character hexadecimal commit, or leave it unknown.');
  return errors;
}
export function decisionFor(workspace: Workspace, run: Run): Decision | undefined { return [...workspace.decisions].reverse().find(d => d.runId === run.id && d.revision === latest(run).revision); }
export function gapsFor(workspace: Workspace, run: Run): string[] {
  const r = latest(run).record;
  const refs = workspace.evidence.filter(e => r.evidenceIds.includes(e.id));
  const has = (type: EvidenceType) => refs.some(e => e.type === type);
  const gaps: string[] = [];
  if (r.phase !== 'after #5751') gaps.push('An after-#5751 run');
  if (!r.release || !r.commit || !has('release identity')) gaps.push('Installed release + commit evidence');
  if (!r.catalogIdentity || !has('database preservation')) gaps.push('Database, source identity + provenance preservation');
  if (r.readOnly !== 'confirmed read-only' || !has('read-only status')) gaps.push('Read-only status evidence');
  if (!r.journal || !has('journal')) gaps.push('Read-only journal capture');
  if (!r.providerResponse || !has('provider response') || r.outcome === 'not executed') gaps.push('Actual provider execution evidence');
  if (!r.attempts || Number(r.attempts) < 1 || !r.actualWaits.trim() || r.waitedSeconds === '') gaps.push('Observed attempts and bounded-wait evidence (record zero waits explicitly)');
  if (r.waitedSeconds !== '' && Number(r.waitedSeconds) > 2700) gaps.push('Observed waiting exceeds the 2,700-second source budget; investigate the discrepancy');
  if ((!r.cursorBefore && !r.cursorAfter && !r.receipt) || !has('backfill receipt')) gaps.push('Resumable backfill evidence');
  return gaps;
}
export function isSupported(workspace: Workspace, run: Run) {
  const d = decisionFor(workspace, run);
  const r = latest(run).record;
  return gapsFor(workspace, run).length === 0 && r.outcome === 'completed' && !!r.retest.trim() && d?.decision === 'accepted for stated scope' && d.scope === 'Recovery assessment' && !!d.retest.trim();
}
const requireText = (x: unknown, label: string, max = 20000) => { if (typeof x !== 'string' || x.length > max) throw Error(`Invalid ${label}: expected text under ${max} characters.`); return x; };
function validateRefs(value: unknown, evidenceIds: Set<string>, label: string): string[] { if (!Array.isArray(value) || value.length > 200 || value.some(id => typeof id !== 'string' || !evidenceIds.has(id))) throw Error(`${label} contains missing or invalid evidence references.`); return value; }
export function parseWorkspace(raw: string): Workspace {
  if (raw.length > 5_000_000) throw Error('Backup exceeds the 5 MB import limit.');
  const w = JSON.parse(raw) as Workspace;
  if (!w || w.version !== 1 || !Array.isArray(w.evidence) || !Array.isArray(w.runs) || !Array.isArray(w.decisions) || !Array.isArray(w.importHistory) || w.evidence.length > 1000 || w.runs.length > 1000 || w.decisions.length > 4000 || w.importHistory.length > 1000) throw Error('Unsupported or oversized workspace backup.');
  const ids = new Set<string>();
  for (const e of w.evidence) {
    if (!e || !EVIDENCE_TYPES.includes(e.type)) throw Error('Invalid evidence type.');
    for (const k of ['id', 'title', 'observedAt', 'reference', 'excerpt', 'sha256', 'scope', 'limitations', 'createdAt'] as const) requireText(e[k], `evidence ${k}`);
    if (!e.id.trim() || !e.title.trim() || !e.scope.trim() || !e.reference.trim() || ids.has(e.id)) throw Error('Evidence IDs must be unique and evidence needs a title and scope.');
    if (!isTimestamp(e.observedAt) || !isTimestamp(e.createdAt) || !validReference(e.reference) || (e.sha256 && !/^[a-f0-9]{64}$/i.test(e.sha256))) throw Error(`Invalid timestamp, reference or SHA-256 in ${e.id}.`);
    ids.add(e.id);
  }
  const runIds = new Set<string>();
  for (const run of w.runs) {
    requireText(run?.id, 'run ID', 200);
    if (!run.id || runIds.has(run.id) || !Array.isArray(run.revisions) || !run.revisions.length || run.revisions.length > 200) throw Error('Run IDs must be unique with 1–200 valid revisions.');
    runIds.add(run.id);
    run.revisions.forEach((rev, index) => {
      if (!rev || rev.revision !== index + 1 || !isTimestamp(rev.savedAt) || !rev.record) throw Error(`Invalid revision history in ${run.id}.`);
      const template = blankRun();
      for (const key of Object.keys(template) as (keyof RunRecord)[]) if (key !== 'evidenceIds') requireText(rev.record[key], `run ${key}`);
      const errors = validateRecord(rev.record); if (errors.length) throw Error(errors.join(' '));
      if (rev.record.runId !== run.id) throw Error('Run identifiers cannot change between revisions.');
      validateRefs(rev.record.evidenceIds, ids, 'Run');
    });
  }
  const decisionIds = new Set<string>();
  for (const d of w.decisions) {
    if (!d || !['needs evidence', 'accepted for stated scope', 'rejected'].includes(d.decision)) throw Error('Invalid reviewer decision.');
    for (const key of ['id', 'runId', 'reviewer', 'scope', 'rationale', 'retest', 'createdAt'] as const) requireText(d[key], `decision ${key}`);
    const run = w.runs.find(r => r.id === d.runId);
    if (!d.id || decisionIds.has(d.id) || !run || !Number.isInteger(d.revision) || !run.revisions.some(r => r.revision === d.revision) || !isTimestamp(d.createdAt) || !d.reviewer.trim() || !d.scope.trim() || !d.rationale.trim()) throw Error('Invalid reviewer identity, revision or rationale.');
    decisionIds.add(d.id); validateRefs(d.evidenceIds, ids, 'Decision');
    if (!d.evidenceIds.length) throw Error('Decisions need evidence references.');
  }
  for (const h of w.importHistory) if (!h || !isTimestamp(h.at) || typeof h.note !== 'string' || h.note.length > 100000) throw Error('Invalid import history.');
  return { ...newWorkspace(), evidence: w.evidence, runs: w.runs, decisions: w.decisions, importHistory: w.importHistory };
}
export function mergeImport(current: Workspace, incoming: Workspace): Workspace {
  const collisions = incoming.evidence.filter(e => current.evidence.some(x => x.id === e.id)).map(e => e.id).concat(incoming.runs.filter(r => current.runs.some(x => x.id === r.id)).map(r => r.id));
  if (collisions.length) throw Error(`Nothing imported. Existing IDs conflict: ${collisions.slice(0, 8).join(', ')}. Import into an empty browser profile or use unique IDs; existing notes are never overwritten.`);
  const at = new Date().toISOString();
  return { ...current, evidence: [...current.evidence, ...incoming.evidence.map(e => ({ ...e, imported: true }))], runs: [...current.runs, ...incoming.runs.map(r => ({ ...r, imported: true }))], importHistory: [...current.importHistory, { at, note: `Imported ${incoming.runs.length} runs and ${incoming.evidence.length} evidence notes. All imported runs require local review. Historical decisions (not active): ${JSON.stringify(incoming.decisions)}. Prior import attestations: ${JSON.stringify(incoming.importHistory)}` }] };
}

export function appendRunRevision(workspace: Workspace, record: RunRecord, originalId?: string): Workspace {
  const errors = validateRecord(record);
  if (errors.length) throw Error(errors.join(' '));
  if (record.evidenceIds.some(id => !workspace.evidence.some(e => e.id === id))) throw Error('Unknown evidence reference.');
  const existing = originalId ? workspace.runs.find(r => r.id === originalId) : undefined;
  if (originalId && (!existing || record.runId !== originalId)) throw Error('Existing run identity must be preserved.');
  if (!originalId && workspace.runs.some(r => r.id === record.runId)) throw Error('This run identifier already exists. Edit it to preserve history.');
  const revision: Revision = { revision: existing ? latest(existing).revision + 1 : 1, savedAt: new Date().toISOString(), record: { ...record, evidenceIds: [...record.evidenceIds] } };
  return { ...workspace, runs: existing ? workspace.runs.map(r => r.id === originalId ? { ...r, revisions: [...r.revisions, revision] } : r) : [...workspace.runs, { id: record.runId, revisions: [revision] }] };
}

export function latestAfterRun(workspace: Workspace, feed: FeedId): Run | undefined {
  return workspace.runs.filter(run => latest(run).record.feed === feed && latest(run).record.phase === 'after #5751').sort((a,b) => Date.parse(latest(b).record.observedAt) - Date.parse(latest(a).record.observedAt) || Date.parse(latest(b).savedAt) - Date.parse(latest(a).savedAt))[0];
}
export function supportedFeedCount(workspace: Workspace): number {
  return FEEDS.filter(feed => { const run = latestAfterRun(workspace, feed.id); return run && isSupported(workspace, run); }).length;
}
