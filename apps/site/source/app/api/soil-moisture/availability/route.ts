import { soilAvailability, SoilSourceError } from "../../../soil-moisture-server";
import { SOIL_GLOBAL_BOUNDS_WGS84, SOIL_PRODUCT_FIRST_DAY, SOIL_PRODUCT_METADATA } from "../../../soil-moisture";
export const dynamic = "force-dynamic";
export async function GET(request: Request) {
  const started = Date.now();
  try {
    const params = new URL(request.url).searchParams;
    if ([...params.keys()].some(k => k !== "retry" || params.getAll(k).length !== 1) || (params.has("retry") && params.get("retry") !== "1")) return Response.json({ state: "error", code: "INVALID_REQUEST" }, { status: 400 });
    const { value, cache } = await soilAvailability(params.get("retry") === "1");
    return Response.json({ state: value.latestCommonDay ? "available" : "unavailable", ...SOIL_PRODUCT_METADATA, coverageBoundsWgs84: SOIL_GLOBAL_BOUNDS_WGS84, firstProductDay: SOIL_PRODUCT_FIRST_DAY, snapshotUtc: SOIL_PRODUCT_METADATA.displayFrameTimeUtc, scaleKmApprox: SOIL_PRODUCT_METADATA.approximateResolutionKm, ...value, backend: { state: "ok", durationMs: Date.now() - started, cache } }, { headers: { "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff" } });
  } catch (error) {
    const code = error instanceof SoilSourceError ? error.code : "NASA_AVAILABILITY_ERROR";
    return Response.json({ state: "error", ...SOIL_PRODUCT_METADATA, coverageBoundsWgs84: SOIL_GLOBAL_BOUNDS_WGS84, firstProductDay: SOIL_PRODUCT_FIRST_DAY, availableDays: [], latestCommonDay: null, backend: { state: "error", code, durationMs: Date.now() - started, cache: "none" } }, { status: error instanceof SoilSourceError ? error.httpStatus : 502, headers: { "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff" } });
  }
}
