import { soilAvailability, SoilSourceError } from "../../../soil-moisture-server";
export const dynamic = "force-dynamic";
export async function GET(request: Request) {
  const started = Date.now();
  try {
    const params = new URL(request.url).searchParams;
    if ([...params.keys()].some(k => k !== "retry" || params.getAll(k).length !== 1) || (params.has("retry") && params.get("retry") !== "1")) return Response.json({ state: "error", code: "INVALID_REQUEST" }, { status: 400 });
    const { value, cache } = await soilAvailability(params.get("retry") === "1");
    return Response.json({ state: value.latestCommonDay ? "available" : "unavailable", product: "SPL4SMAU", version: "008", snapshotUtc: "12:00", scaleKmApprox: 9, ...value, backend: { state: "ok", durationMs: Date.now() - started, cache } }, { headers: { "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff" } });
  } catch (error) {
    const code = error instanceof SoilSourceError ? error.code : "NASA_AVAILABILITY_ERROR";
    return Response.json({ state: "error", product: "SPL4SMAU", version: "008", availableDays: [], latestCommonDay: null, backend: { state: "error", code, durationMs: Date.now() - started, cache: "none" } }, { status: error instanceof SoilSourceError ? error.httpStatus : 502, headers: { "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff" } });
  }
}
