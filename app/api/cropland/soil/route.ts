import { readBoundedJson } from "../../../bounded-json";
import { inCdlRegion } from "../../../cropland";

export const dynamic = "force-dynamic";
const SDA_URL = "https://sdmdataaccess.sc.egov.usda.gov/Tabular/post.rest";
const MAX_COMPONENTS = 8;
/** The columns the query selects, in order. The response is read by position. */
const COLUMNS = ["mukey", "muname", "compname", "comppct_r", "majcompflag", "drainagecl", "hydgrp", "nirrcapcl", "aws0150wta"] as const;
/** SDA sends its numbers as text; a blank cell is null. */
const numeric = (cell: string | number | null) => {
  if (cell === null || cell === "") return null;
  const value = Number(cell);
  if (!Number.isFinite(value)) throw new Error("Unrecognized USDA number");
  return value;
};
const text = (cell: string | number | null) => cell === null ? null : String(cell);
const noStore = { "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff" };
const headers = { "Cache-Control": "public, max-age=86400, s-maxage=604800", "X-Content-Type-Options": "nosniff" };

/**
 * The SSURGO soil-map unit at a point in or near Kansas, from USDA Soil Data Access: its components with their
 * drainage, hydrologic group and non-irrigated capability class, and the map unit's water storage to 150 cm. Map components are
 * alternatives within the mapped area, not the soil at the point.
 */
export async function GET(request: Request) {
  const params = new URL(request.url).searchParams;
  const lon = Number(params.get("lon")), lat = Number(params.get("lat"));
  if ([...params.keys()].some(key => key !== "lon" && key !== "lat") || params.get("lon") === null || params.get("lat") === null || !inCdlRegion(lon, lat))
    return Response.json({ state: "error", message: "Choose a point in or near Kansas." }, { status: 400, headers: noStore });
  const query = `SELECT TOP 20 mu.mukey,mu.muname,c.compname,c.comppct_r,c.majcompflag,c.drainagecl,c.hydgrp,c.nirrcapcl,ma.aws0150wta FROM mapunit mu JOIN component c ON c.mukey=mu.mukey LEFT JOIN muaggatt ma ON ma.mukey=mu.mukey WHERE mu.mukey IN (SELECT mukey FROM SDA_Get_Mukey_from_intersection_with_WktWgs84('POINT(${lon.toFixed(5)} ${lat.toFixed(5)})')) ORDER BY c.comppct_r DESC`;
  const controller = new AbortController(), timer = setTimeout(() => controller.abort(), 15_000);
  const cancel = () => controller.abort(); request.signal.addEventListener("abort", cancel, { once: true });
  try {
    const response = await fetch(SDA_URL, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ format: "JSON+COLUMNNAME", query }), signal: controller.signal });
    if (!response.ok) throw new Error("USDA unavailable");
    const data = await readBoundedJson(response, 64 * 1024, controller.signal);
    const table = data && typeof data === "object" && "Table" in data ? (data as { Table: unknown }).Table : null;
    if (!Array.isArray(table) || !Array.isArray(table[0]) || table[0].length !== COLUMNS.length) throw new Error("Unrecognized USDA response");
    const rows = table.slice(1).map(row => {
      if (!Array.isArray(row) || row.length !== COLUMNS.length || row.some(cell => cell !== null && typeof cell !== "string" && typeof cell !== "number")) throw new Error("Unrecognized USDA row");
      return Object.fromEntries(COLUMNS.map((name, i) => [name, row[i]])) as Record<(typeof COLUMNS)[number], string | number | null>;
    });
    const dominant = rows[0];
    const body = {
      lon, lat, retrievedAt: new Date().toISOString(),
      state: dominant ? "ready" : "none",
      // The water storage is a weighted average over every component of the map unit, so it belongs to the unit, not to each component.
      mapUnit: dominant ? { key: String(dominant.mukey), name: String(dominant.muname), waterStorageCm: numeric(dominant.aws0150wta) } : null,
      components: rows.filter(row => row.mukey === dominant?.mukey).slice(0, MAX_COMPONENTS).map(row => ({
        name: String(row.compname ?? "Unnamed component"), percent: numeric(row.comppct_r), major: row.majcompflag === "Yes", drainage: text(row.drainagecl),
        hydrologicGroup: text(row.hydgrp), capability: numeric(row.nirrcapcl),
      })),
    };
    return Response.json(body, { headers });
  } catch {
    return Response.json({ state: "unavailable", message: "USDA Soil Data Access did not answer for this point. No soil is inferred." }, { status: 502, headers: noStore });
  } finally { clearTimeout(timer); request.signal.removeEventListener("abort", cancel); }
}
