import { boundedFetch } from "../../event-atlas/upstream";
import { inLandCoverRegion, landCoverPointProviderUrl, parseLandCoverPoint } from "../../../land-cover";

export const dynamic = "force-dynamic";
const MAX_BYTES = 64 * 1024;

/** The NLCD 2021 class of the 30 m cell at a point in or near Kansas. NLCD is a fixed product, so answers are kept a week. */
export async function GET(request: Request) {
  const params = new URL(request.url).searchParams;
  const lon = Number(params.get("lon")), lat = Number(params.get("lat"));
  const noStore = { "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff" };
  if (params.get("lon") === null || params.get("lat") === null || !inLandCoverRegion(lon, lat))
    return Response.json({ state: "error", message: "Choose a point in or near Kansas." }, { status: 400, headers: noStore });
  try {
    const response = await boundedFetch(landCoverPointProviderUrl(lon, lat), MAX_BYTES, { timeoutMs: 12_000 });
    const code = parseLandCoverPoint(JSON.parse(response.text()) as unknown);
    return Response.json({ lon, lat, code }, { headers: { "Cache-Control": "public, max-age=86400, s-maxage=604800", "X-Content-Type-Options": "nosniff" } });
  } catch {
    return Response.json({ state: "unavailable", message: "MRLC did not answer for this point." }, { status: 502, headers: noStore });
  }
}
