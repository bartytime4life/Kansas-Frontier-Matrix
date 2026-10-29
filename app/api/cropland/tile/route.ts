import { boundedFetch } from "../../event-atlas/upstream";
import { CDL_MAX_ZOOM, CDL_MIN_ZOOM, cdlTileProviderUrl, isCdlYear, tileBounds, tileInRegion } from "../../../cropland";

export const dynamic = "force-dynamic";
const MAX_BYTES = 2 * 1024 * 1024;

/**
 * One Web Mercator tile of the Cropland Data Layer for a year. CropScape draws
 * in longitude and latitude, so the tile's corners are asked for in EPSG:4326;
 * at field zoom (8 and up) the two agree to under a pixel. A year's CDL does
 * not change, so tiles are kept a week.
 */
export async function GET(request: Request) {
  const params = new URL(request.url).searchParams;
  const [year, z, x, y] = ["year", "z", "x", "y"].map(key => Number(params.get(key)));
  const noStore = { "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff" };
  if (["year", "z", "x", "y"].some(key => !params.get(key)) || !isCdlYear(year) || !Number.isInteger(z) || z < CDL_MIN_ZOOM || z > CDL_MAX_ZOOM
    || !Number.isInteger(x) || !Number.isInteger(y) || x < 0 || y < 0 || x >= 2 ** z || y >= 2 ** z)
    return Response.json({ state: "error", message: "Ask for a CDL year and a tile at zoom 8–13." }, { status: 400, headers: noStore });
  // Outside Kansas and its margin there is nothing to draw.
  if (!tileInRegion(tileBounds(z, x, y))) return new Response(null, { status: 204, headers: { "Cache-Control": "public, max-age=604800", "X-Content-Type-Options": "nosniff" } });
  try {
    const response = await boundedFetch(cdlTileProviderUrl(year, z, x, y), MAX_BYTES, { timeoutMs: 20_000 });
    const type = response.headers.get("content-type") ?? "";
    if (!type.startsWith("image/png")) throw new Error("CropScape answered without a PNG.");
    return new Response(response.bytes, { headers: { "Content-Type": "image/png", "Cache-Control": "public, max-age=86400, s-maxage=604800", "X-Content-Type-Options": "nosniff" } });
  } catch {
    return new Response(null, { status: 502, headers: noStore });
  }
}
