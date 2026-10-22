import { getPipelineStore } from '../server/pipeline-store.mjs';
import { handlePipeline } from '../server/pipeline-handler.mjs';
import { canonical, sha, verifyProfile, PipelineError } from '../server/pipeline-contract.mjs';
import { parseWaterPackage, projectWater } from './governed-water';
import { parseWeatherPackage, projectWeather } from './governed-weather';

export async function validateGoverned(family: string, payload: { snapshot: unknown; decision: Record<string, unknown> }, at: number) {
  const text = canonical(payload.snapshot);
  const result = family === 'water'
    ? await projectWater(await parseWaterPackage(text), payload.decision, 'layers', new Date(at).toISOString())
    : await projectWeather(await parseWeatherPackage(text), payload.decision, 'layers', new Date(at).toISOString());
  if (result.envelope.outcome !== 'ANSWER') throw new PipelineError('GOVERNED_RELEASE_WITHHELD', 403);
  return result;
}
export async function pipelineRequest(request: Request) {
  if (process.env.KFM_PIPELINE_ENABLED !== 'true') return Response.json({ error: 'PIPELINE_DISABLED' }, { status: 404, headers: { 'Cache-Control': 'no-store' } });
  try { return await handlePipeline(request, { store: await getPipelineStore(), validateGoverned }); }
  catch { return Response.json({ error: 'PIPELINE_UNAVAILABLE' }, { status: 503, headers: { 'Cache-Control': 'no-store' } }); }
}
export async function governedPipelineSnapshot(family: 'water' | 'weather') {
  const row = await (await getPipelineStore()).active(family);
  if (!row || row.state !== 'COMMITTED' || !row.projection) return null;
  if ((process.env.KFM_PIPELINE_REVOKED_PROFILES ?? '').split(',').includes(row.manifest.approval.profile.id)) throw new Error('APPROVAL_REVOKED');
  verifyProfile(row.manifest.approval, process.env.KFM_PIPELINE_APPROVER_PUBLIC_KEY, { sourceId: family, recipe: row.manifest.recipeSha256 });
  if (sha(canonical(row.projection)) !== row.manifest.payloadSha256) throw new Error('PROJECTION_INTEGRITY_FAILED');
  return row.projection as { snapshot: unknown; decision: Record<string, unknown> };
}
