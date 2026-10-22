import { getPipelineStore } from '../../../../../server/pipeline-store.mjs';
import { publicHistory } from '../../../../../server/pipeline-handler.mjs';
export const dynamic = 'force-dynamic';
export async function GET(request: Request) {
  const headers = { 'Cache-Control': 'no-store', 'X-Content-Type-Options': 'nosniff' };
  if (process.env.KFM_PIPELINE_ENABLED !== 'true') return Response.json({ items: [], state: 'setup-pending' }, { headers });
  try {
    const url = new URL(request.url); if (url.search) return Response.json({ error: 'INVALID_QUERY' }, { status: 400, headers });
    return Response.json(await publicHistory(url.pathname.split('/').at(-2)!, { store: await getPipelineStore() }), { headers });
  } catch { return Response.json({ state: 'withheld', reason: 'HISTORY_UNAVAILABLE' }, { status: 503, headers }); }
}
