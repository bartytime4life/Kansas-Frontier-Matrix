import { boundedFetch } from "../../event-atlas/upstream";
import { cdlValueProviderUrl, inCdlRegion, isCdlYear, parseCdlValue } from "../../../cropland";

export const dynamic = "force-dynamic";
const MAX_BYTES = 64 * 1024;

/** The Cropland Data Layer class of the 30 m cell at a point in or near Kansas for a year, from CropScape's GetCDLValue. Kept a day. */
export async function GET(request: Request) {
  const params = new URL(request.url).searchParams;
  const year = Number(params.get("year")), lon = Number(params.get("lon")), lat = Number(params.get("lat"));
  const noStore = { "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff" };
  if (!isCdlYear(year) || params.get("lon") === null || params.get("lat") === null || !inCdlRegion(lon, lat))
    return Response.json({ state: "error", message: "Choose a CDL year and a point in or near Kansas." }, { status: 400, headers: noStore });
  try {
    const response = await boundedFetch(cdlValueProviderUrl(year, lon, lat), MAX_BYTES, { timeoutMs: 15_000 });
    return Response.json({ year, lon, lat, crop: parseCdlValue(response.text()) },
      { headers: { "Cache-Control": "public, max-age=86400, s-maxage=604800", "X-Content-Type-Options": "nosniff" } });
  } catch {
    return Response.json({ state: "unavailable", message: "CropScape did not answer for this point." }, { status: 502, headers: noStore });
  }
}
