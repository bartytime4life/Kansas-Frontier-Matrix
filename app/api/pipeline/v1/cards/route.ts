import { getCardPipelineSnapshot } from '../../../../card-pipeline-server';
export const dynamic = 'force-dynamic';
export async function GET(request: Request) {
  const headers = { 'Cache-Control': 'no-store', 'X-Content-Type-Options': 'nosniff', 'Referrer-Policy': 'no-referrer' };
  if (new URL(request.url).search) return Response.json({ error: 'INVALID_QUERY' }, { status: 400, headers });
  return Response.json(await getCardPipelineSnapshot(), { headers });
}
