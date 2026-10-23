import { checkDatabaseConnection } from '../../../server/database-connection.mjs';

export const dynamic = 'force-dynamic';
export async function GET(request: Request) {
  const headers = { 'Cache-Control': 'no-store', 'X-Content-Type-Options': 'nosniff' };
  if (new URL(request.url).search) return Response.json({ error: 'QUERY_NOT_ALLOWED' }, { status: 400, headers });
  const result = await checkDatabaseConnection();
  return Response.json(result, { status: result.connected ? 200 : 503, headers });
}
