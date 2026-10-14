/** Local diagnostic records; never release, deployment, or source-admission evidence. */
export type FrameSummary = { frames: number; fps: number; p95Ms: number; maxMs: number; over25ms: number };
export type PacingRecord = {
  format: 'kfm-frame-pacing-v2';
  workload: Record<string, unknown>;
  browser: FrameSummary; map: FrameSummary;
  dataUnchanged: boolean; workloadUnchanged: boolean;
  readiness: { before: boolean; after: boolean };
  visibility: { visible: boolean; focused: boolean; interrupted: boolean };
  moving: boolean; interrupted: boolean; steps: number; elapsedMs: number;
};
const stable = (value: unknown): string => JSON.stringify(value, (_key, item) =>
  item && typeof item === 'object' && !Array.isArray(item)
    ? Object.fromEntries(Object.entries(item).sort(([a], [b]) => a.localeCompare(b))) : item);
export const samePacingWorkload = (a: unknown, b: unknown) => stable(a) === stable(b);

/** Reject incomplete/unequal records before discussing a performance difference. */
export function comparePacingRecords(before: PacingRecord, after: PacingRecord, target = 60) {
  const holds: string[] = [];
  if (!(target > 0 && Number.isFinite(target))) holds.push('Invalid frame-rate target');
  for (const [name, record] of [['published', before], ['candidate', after]] as const) {
    if (record?.format !== 'kfm-frame-pacing-v2' || !record.workload || typeof record.workload !== 'object'
      || !Object.keys(record.workload).length) { holds.push(`${name}: missing workload identity`); continue; }
    for (const field of ['camera','viewport','canvas','sourceDigest','visibleFeatureDigest']) {
      if (record.workload[field] === undefined) holds.push(`${name}: missing ${field}`);
    }
    if (!record.dataUnchanged || !record.workloadUnchanged) holds.push(`${name}: data or selection changed`);
    if (!record.readiness?.before || !record.readiness?.after) holds.push(`${name}: sources or tiles not ready`);
    if (!record.visibility?.visible || !record.visibility?.focused || record.visibility?.interrupted) holds.push(`${name}: foreground interrupted`);
    if (!(record.elapsedMs >= 11900 && record.elapsedMs <= 12500)) holds.push(`${name}: sample duration differs from 12 seconds`);
    if (!record.moving) holds.push(`${name}: idle redraw cadence is not navigation acceptance`);
    if (record.interrupted && record.steps !== 48) holds.push(`${name}: interrupted input sequence incomplete`);
    for (const summary of [record.browser, record.map]) {
      if (!summary || !Number.isInteger(summary.frames) || summary.frames <= 0
        || ![summary.fps, summary.p95Ms, summary.maxMs, summary.over25ms].every(Number.isFinite)
        || summary.fps <= 0 || summary.p95Ms <= 0 || summary.maxMs < summary.p95Ms
        || !Number.isInteger(summary.over25ms) || summary.over25ms < 0 || summary.over25ms > summary.frames
        || Math.abs(summary.fps - summary.frames * 1000 / record.elapsedMs) > .05) holds.push(`${name}: invalid frame statistics`);
    }
  }
  if (!samePacingWorkload(before?.workload, after?.workload)
    || before?.moving !== after?.moving || before?.interrupted !== after?.interrupted) holds.push('Workloads differ');
  if (holds.length) return { status: 'INCONCLUSIVE' as const, holds };
  // One missing presentation frame at each edge and timer rounding are allowed.
  const smooth = [after.browser, after.map].every(s => s.fps >= target * .98 && s.p95Ms <= 1000 / target * 1.2 && s.over25ms / s.frames <= .01);
  return { status: smooth ? 'PASS' as const : 'HOLD' as const, holds: smooth ? [] : ['Candidate misses navigation frame-pacing budget'],
    difference: { browserFps: after.browser.fps - before.browser.fps, mapFps: after.map.fps - before.map.fps } };
}
