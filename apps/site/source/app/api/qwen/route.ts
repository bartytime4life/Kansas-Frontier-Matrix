export const dynamic = "force-dynamic";

const reply = (body: Record<string, unknown>, status: number) =>
  Response.json(body, { status, headers: { "cache-control": "no-store", "x-content-type-options": "nosniff" } });

/**
 * Hosted inference is deliberately dormant in the owner-local release.
 * Legacy endpoint/model environment variables are not activation authority.
 * A future hosted mode requires a separately reviewed governed contract.
 */
export async function POST(request: Request) {
  const origin = request.headers.get("origin");
  if (origin && origin !== new URL(request.url).origin) {
    return reply({ status: "disabled", message: "Hosted Qwen is not available from this origin." }, 403);
  }
  return reply({
    status: "disabled",
    message: "Hosted Qwen is disabled. Use the governed owner-local companion.",
  }, 503);
}
