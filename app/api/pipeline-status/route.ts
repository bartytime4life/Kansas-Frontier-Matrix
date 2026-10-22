import { getPipelineStore } from '../../../server/pipeline-store.mjs';
export const dynamic = 'force-dynamic';
export async function GET() {
  const headers = { 'Cache-Control': 'no-store', 'X-Content-Type-Options': 'nosniff' };
  if (process.env.KFM_PIPELINE_ENABLED !== 'true') return Response.json({ configured: false, state: 'setup-pending' }, { headers });
  try {
    const state = await (await getPipelineStore()).status();
    return Response.json({ ...state, workerHealth: state.workerSeen && Date.now() - state.workerSeen < 900000 ? 'online' : 'missing' }, { headers });
  } catch { return Response.json({ configured: false, state: 'storage-unavailable' }, { status: 503, headers }); }
}
