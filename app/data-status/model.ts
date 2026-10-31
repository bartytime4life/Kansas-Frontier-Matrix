export const HOLD_LABELS: Record<string, string> = {
  CAPTURE_REQUIRED: 'Capture the original file before review.', FORMAT_UNRECOGNIZED: 'File format needs identification.',
  DOMAIN_UNRESOLVED: 'Choose the source domain.', RIGHTS_UNKNOWN: 'Confirm source reuse rights.',
  RIGHTS_RESTRICTED: 'Source reuse is restricted.', RIGHTS_DENIED: 'Source reuse is not permitted.',
  SENSITIVITY_UNKNOWN: 'Review sensitivity before sharing.', SENSITIVITY_SENSITIVE: 'Sensitive material needs review.',
  SENSITIVITY_RESTRICTED: 'Restricted material must remain private.', REVIEW_FLAGS: 'Resolve source or quality review flags.',
  GITHUB_BUDGET_EXCEEDED: 'The GitHub data budget is exceeded; keep bulk data local.',
  OUTSIDE_KANSAS: 'Check whether the source belongs in the Kansas collection.',
  REVIEWED_LOCAL_ONLY: 'Local review is complete; sharing is still held.', OTHER: 'Further details are available in the local Intake Desk.',
};
export const INTAKE_LABELS = { reviewed: 'Reviewed locally', ready: 'Ready for routing review', review: 'Needs review', blocked: 'Blocked', other: 'Other intake states' };
export type Capacity = { format: 'kfm-database-capacity-v1'; scope: 'visible-hosted-sql-tables'; checkedAt: string;
  state: 'measured' | 'unavailable'; targetBytes: number; tables: number | null; usedBytes: number | null; estimatedRows: number | null };
export type LocalReport = { format: 'kfm-local-data-status-v1'; scope: 'selected-local-catalogs'; checkedAt: string;
  sql: { state: 'measured' | 'unavailable'; targetBytes: number; catalogCount: number | null; usedBytes: number | null; journalBytes: number | null };
  intake: { state: 'measured' | 'unavailable'; files: number | null; counts: Record<keyof typeof INTAKE_LABELS, number> | null; holds: { code: string; files: number }[] } };
const record = (v: unknown): v is Record<string, unknown> => Boolean(v) && typeof v === 'object' && !Array.isArray(v);
const count = (v: unknown): v is number => typeof v === 'number' && Number.isSafeInteger(v) && v >= 0;
const nullable = (v: unknown) => v === null || count(v);
const stamp = (v: unknown): v is string => typeof v === 'string' && v.length <= 32 && /^\d{4}-\d{2}-\d{2}T/.test(v) && Number.isFinite(Date.parse(v));
export function parseCapacity(v: unknown): Capacity {
  if (!record(v) || v.format !== 'kfm-database-capacity-v1' || v.scope !== 'visible-hosted-sql-tables' || !stamp(v.checkedAt)
    || !['measured', 'unavailable'].includes(String(v.state)) || !count(v.targetBytes) || v.targetBytes === 0
    || ![v.tables, v.usedBytes, v.estimatedRows].every(nullable)
    || (v.state === 'unavailable' ? [v.tables, v.usedBytes, v.estimatedRows].some(x => x !== null) : !count(v.tables))) throw new Error('Invalid database status');
  return { format: v.format, scope: v.scope, checkedAt: v.checkedAt, state: v.state as Capacity['state'],
    targetBytes: v.targetBytes, tables: v.tables as number | null, usedBytes: v.usedBytes as number | null, estimatedRows: v.estimatedRows as number | null };
}
export function parseLocalReport(v: unknown): LocalReport {
  if (!record(v) || v.format !== 'kfm-local-data-status-v1' || v.scope !== 'selected-local-catalogs' || !stamp(v.checkedAt)
    || !record(v.sql) || !record(v.intake)) throw new Error('Invalid local report');
  const s = v.sql, i = v.intake;
  if (!['measured', 'unavailable'].includes(String(s.state)) || !count(s.targetBytes) || s.targetBytes === 0
    || ![s.catalogCount, s.usedBytes, s.journalBytes].every(nullable)
    || (s.state === 'measured' ? !count(s.catalogCount) || s.catalogCount < 1 || s.catalogCount > 32 || !count(s.usedBytes) || !count(s.journalBytes) || s.journalBytes > s.usedBytes
      : [s.catalogCount, s.usedBytes, s.journalBytes].some(x => x !== null))) throw new Error('Invalid local SQL status');
  if (!['measured', 'unavailable'].includes(String(i.state)) || !nullable(i.files) || !Array.isArray(i.holds) || i.holds.length > Object.keys(HOLD_LABELS).length) throw new Error('Invalid intake status');
  const keys = Object.keys(INTAKE_LABELS);
  if (i.state === 'measured' ? !count(i.files) || !record(i.counts) || !keys.every(k => count((i.counts as Record<string, unknown>)[k]))
    || keys.reduce((total, k) => total + Number((i.counts as Record<string, unknown>)[k]), 0) !== i.files
    : i.files !== null || i.counts !== null || i.holds.length !== 0) throw new Error('Invalid intake counts');
  const seen = new Set();
  const holds = i.holds.map(h => {
    if (!record(h) || typeof h.code !== 'string' || !Object.hasOwn(HOLD_LABELS, h.code) || seen.has(h.code) || !count(h.files) || h.files > Number(i.files)) throw new Error('Invalid intake holds');
    seen.add(h.code); return { code: h.code, files: h.files };
  });
  return { format: v.format, scope: v.scope, checkedAt: v.checkedAt,
    sql: { state: s.state as LocalReport['sql']['state'], targetBytes: s.targetBytes, catalogCount: s.catalogCount as number | null, usedBytes: s.usedBytes as number | null, journalBytes: s.journalBytes as number | null },
    intake: { state: i.state as LocalReport['intake']['state'], files: i.files as number | null,
      counts: i.counts === null ? null : Object.fromEntries(keys.map(k => [k, (i.counts as Record<string, number>)[k]])) as NonNullable<LocalReport['intake']['counts']>, holds } };
}
export const gigabytes = (value: number | null) => value === null ? 'Unknown' : `${(value / 1e9).toFixed(2)} GB`;
