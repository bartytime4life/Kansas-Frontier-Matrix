import { parseTileRequest, soilAvailability, soilTileBytes, SoilSourceError } from "../../../soil-moisture-server";
export const dynamic = "force-dynamic";
export async function GET(request: Request) {
  try {
    const { view, day, z, x, y } = parseTileRequest(request.url);
    const { value } = await soilAvailability();
    if (!value.availableDays.includes(day)) throw new SoilSourceError("DAY_UNAVAILABLE", 404);
    const bytes = await soilTileBytes(view, day, z, x, y);
    return new Response(bytes as BodyInit, { headers: { "Content-Type": "image/png", "Cache-Control": "private, max-age=900", "X-Content-Type-Options": "nosniff", "X-Soil-Source-Day": day } });
  } catch (error) {
    const code = error instanceof SoilSourceError ? error.code : "NASA_TILE_ERROR";
    return Response.json({ state: "error", code, message: "Exact-day NASA tile unavailable; no substituted image was used." }, { status: error instanceof SoilSourceError ? error.httpStatus : 502, headers: { "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff" } });
  }
}
