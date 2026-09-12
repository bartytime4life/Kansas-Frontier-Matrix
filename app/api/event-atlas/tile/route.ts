import { boundedFetch } from "../upstream";
import { imageryTiles } from "../../../event-atlas";
export const dynamic = "force-dynamic";
// A source-confirmed HTTP 204 means an empty aggregate tile, not an error.
const EMPTY_PNG = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAAC0lEQVR4nGNgAAIAAAUAAXpeqz8AAAAASUVORK5CYII=";
export async function GET(request: Request) {
  try {
    const p = new URL(request.url).searchParams;
    if ([...p.keys()].some((key) => !["kind","date","z","x","y"].includes(key) || p.getAll(key).length !== 1)) throw new Error("Invalid tile query.");
    const kind = p.get("kind"), date = p.get("date") ?? "", z = Number(p.get("z")), x = Number(p.get("x")), y = Number(p.get("y"));
    if (["kind","date","z","x","y"].some((key) => !p.has(key)) || ["z","x","y"].some((key) => !/^\d+$/.test(p.get(key) ?? ""))) throw new Error("A complete tile address is required.");
    if (!["satellite","flora","fauna"].includes(kind ?? "") || !/^\d{4}-\d{2}-\d{2}$/.test(date) || !Number.isFinite(Date.parse(date)) || new Date(date).toISOString().slice(0,10) !== date || date < "1995-01-01" || date > new Date().toISOString().slice(0,10) || ![z,x,y].every(Number.isInteger) || z < 0 || z > (kind === "satellite" ? 9 : 6) || x < 0 || y < 0 || x >= 2**z || y >= 2**z) throw new Error("Tile outside the date or coarse spatial budget.");
    const upstream = kind === "satellite" ? imageryTiles(date).replace("{z}",String(z)).replace("{x}",String(x)).replace("{y}",String(y)) : `https://api.gbif.org/v2/map/occurrence/density/${z}/${x}/${y}@1x.png?taxonKey=${kind === "flora" ? 6 : 1}&country=US&year=${date.slice(0,4)},${date.slice(0,4)}&bin=hex&hexPerTile=20&style=${kind === "flora" ? "green.poly" : "purpleYellow.poly"}`;
    const tile = await boundedFetch(upstream, 2 * 1024 * 1024);
    if (kind === "satellite" && tile.headers.get("layer-time-actual")?.slice(0,10) !== date) throw new Error("Satellite date was not confirmed; nearest-date substitution refused.");
    const empty = tile.bytes.length === 0;
    if (empty && kind === "satellite") throw new Error("Satellite coverage unavailable.");
    if (!empty && (kind === "satellite" ? !tile.headers.get("content-type")?.includes("image/jpeg") : !tile.headers.get("content-type")?.includes("image/png"))) throw new Error("Unexpected tile response.");
    const bytes = empty ? Uint8Array.from(atob(EMPTY_PNG), (char) => char.charCodeAt(0)) : tile.bytes;
    return new Response(bytes, { headers: { "Content-Type": empty ? "image/png" : tile.headers.get("content-type")!, "Cache-Control": "public, max-age=1200", "X-Content-Type-Options": "nosniff", "X-Temporal-Support": kind === "satellite" ? date : date.slice(0,4), "X-Aggregate-State": empty ? "no-records" : "source-image" } });
  } catch { return Response.json({ message: "The exact-date tile is unavailable. No substituted date was used." }, { status: 502, headers: { "Cache-Control": "no-store" } }); }
}
