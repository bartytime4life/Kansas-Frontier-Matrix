import identity from "../../build-info.generated.json";

/** Build-only metadata; never reads environment, user identity, DB or R2. */
export function GET() {
  return Response.json(identity, { headers: { "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff" } });
}
