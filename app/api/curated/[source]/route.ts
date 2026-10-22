import { getPipelineStore } from '../../../../server/pipeline-store.mjs';
import { publicContext, publicArtifact } from '../../../../server/pipeline-handler.mjs';
import { PipelineError } from '../../../../server/pipeline-contract.mjs';
export const dynamic = 'force-dynamic';
export async function GET(request: Request) {
  const headers = { 'Cache-Control': 'no-store', 'X-Content-Type-Options': 'nosniff' };
  try {
    if (process.env.KFM_PIPELINE_ENABLED !== 'true') return Response.json({ state: 'withheld', reason: 'PIPELINE_NOT_CONFIGURED' }, { headers });
    const url = new URL(request.url), id = url.pathname.split('/').at(-1)!;
    if ([...url.searchParams.keys()].some(k => !['release','download'].includes(k)) || [...url.searchParams].length > 2 || url.searchParams.getAll('release').length > 1 || url.searchParams.getAll('download').length > 1
      || url.searchParams.has('download') && (url.searchParams.get('download') !== '1' || !url.searchParams.get('release'))) return Response.json({ error: 'INVALID_QUERY' }, { status: 400, headers });
    if (url.searchParams.get('download') === '1') {
      const releaseId = url.searchParams.get('release')!;
      const bytes = await publicArtifact(id, { store: await getPipelineStore() }, releaseId);
      return new Response(new Uint8Array(bytes), { headers: { ...headers, 'Content-Type': 'application/json', 'Content-Disposition': `attachment; filename="${id}-${releaseId}.json"` } });
    }
    return Response.json(await publicContext(id, { store: await getPipelineStore() }, url.searchParams.get('release')), { headers });
  } catch (e) {
    return Response.json({ state: 'withheld', reason: e instanceof PipelineError ? e.message : 'RELEASE_STORE_UNAVAILABLE' }, { status: e instanceof PipelineError && e.status === 400 ? 400 : 503, headers });
  }
}
