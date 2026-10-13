// Fail closed until the real merchant, identity, pricing and private delivery
// adapters are configured. A client role or success redirect is never payment.
export async function POST() {
  return Response.json(
    { code: "REPORT_SERVICE_NOT_CONFIGURED", error: "Report checkout is being configured. Your map and draft are preserved." },
    { status: 503, headers: { "Cache-Control": "private, no-store", "X-Content-Type-Options": "nosniff" } },
  );
}
