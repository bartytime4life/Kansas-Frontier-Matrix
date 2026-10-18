import identity from '../../build-info.generated.json';

// Public application identity only. No host environment or private stores.
export function GET() {
  return Response.json(identity, { headers: { 'Cache-Control': 'no-store', 'X-Content-Type-Options': 'nosniff' } });
}
