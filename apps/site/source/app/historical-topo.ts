import type { Feature, Polygon } from "geojson";

export const TOPO_CATALOG_URL = "https://ngmdb.usgs.gov/arcgis/rest/services/topoview/ustOverlay/MapServer/0/query";
export const TOPO_PAGE_SIZE = 24;
export type TopoSearch = { lng: number; lat: number; from: number; through: number; scale: "all" | "24000" | "62500" | "125000" | "250000"; name: string; offset: number };
export type TopoSheet = { id: number; scanId: number; name: string; state: string; year: number; imprintYear: number | null; scale: number; series: string; datum: string; footprint: Feature<Polygon>; viewerHref: string };

const integer = (value: unknown, min: number, max: number) => typeof value === "number" && Number.isInteger(value) && value >= min && value <= max;
const text = (value: unknown, max = 120) => typeof value === "string" && value.length > 0 && value.length <= max ? value : null;

export function parseTopoSearch(url: string): TopoSearch {
  const params = new URL(url).searchParams;
  const allowed = new Set(["lng", "lat", "from", "through", "scale", "name", "offset"]);
  if ([...params.keys()].some((key) => !allowed.has(key) || params.getAll(key).length !== 1)) throw new Error("Invalid historical map search.");
  const lng = Number(params.get("lng"));
  const lat = Number(params.get("lat"));
  const from = Number(params.get("from") ?? 1930);
  const through = Number(params.get("through") ?? 1960);
  const offset = Number(params.get("offset") ?? 0);
  const scale = params.get("scale") ?? "all";
  const name = (params.get("name") ?? "").trim();
  if (!Number.isFinite(lng) || lng < -125 || lng > -66 || !Number.isFinite(lat) || lat < 24 || lat > 50
    || !integer(from, 1800, 2100) || !integer(through, 1800, 2100) || from > through
    || !integer(offset, 0, 240) || offset % TOPO_PAGE_SIZE !== 0
    || !["all", "24000", "62500", "125000", "250000"].includes(scale)
    || (name.length > 40 || (name && !/^[\p{L}\p{N} .'-]+$/u.test(name)))) throw new Error("Choose a valid U.S. map center, year range, scale, and sheet name.");
  return { lng, lat, from, through, scale: scale as TopoSearch["scale"], name, offset };
}

export function topoProviderUrl(search: TopoSearch): string {
  const where = ["primary_state = 'KS'", `date_on_map >= ${search.from}`, `date_on_map <= ${search.through}`];
  if (search.scale !== "all") where.push(`map_scale = ${search.scale}`);
  if (search.name) where.push(`map_name LIKE '%${search.name.replaceAll("'", "''")}%'`);
  const query = new URL(TOPO_CATALOG_URL);
  query.search = new URLSearchParams({
    where: where.join(" AND "),
    geometry: `${Math.max(-180, search.lng - 0.65)},${Math.max(-90, search.lat - 0.45)},${Math.min(180, search.lng + 0.65)},${Math.min(90, search.lat + 0.45)}`,
    geometryType: "esriGeometryEnvelope", inSR: "4326", outSR: "4326", spatialRel: "esriSpatialRelIntersects",
    outFields: "OBJECTID,map_scale,map_name,primary_state,date_on_map,imprint_year,scan_id,series,datum",
    returnGeometry: "true", resultRecordCount: String(TOPO_PAGE_SIZE), resultOffset: String(search.offset),
    orderByFields: "date_on_map DESC,map_name ASC,OBJECTID ASC", f: "json",
  }).toString();
  return query.toString();
}

export function topoViewerHref(lng: number, lat: number): string {
  return `https://ngmdb.usgs.gov/topoview/viewer/#12/${lat.toFixed(5)}/${lng.toFixed(5)}`;
}

export function parseTopoCatalog(payload: unknown): { sheets: TopoSheet[]; more: boolean } {
  if (!payload || typeof payload !== "object") throw new Error("USGS catalog response is unavailable.");
  const body = payload as { error?: unknown; features?: unknown; exceededTransferLimit?: unknown };
  if (body.error || !Array.isArray(body.features)) throw new Error("USGS catalog response is unavailable.");
  const sheets = body.features.flatMap((raw: unknown) => {
    if (!raw || typeof raw !== "object") return [];
    const entry = raw as { attributes?: Record<string, unknown>; geometry?: { rings?: unknown } };
    const a = entry.attributes;
    const rings = entry.geometry?.rings;
    // The USGS primary-state label is the catalog's jurisdiction for a sheet.
    // Keep this check even if the upstream WHERE clause is ignored or changes.
    if (!a || a.primary_state !== "KS" || !integer(a.OBJECTID, 1, 1e10) || !integer(a.scan_id, 1, 1e10)
      || !integer(a.date_on_map, 1800, 2100) || !integer(a.map_scale, 1, 1e7)
      || !text(a.map_name) || !text(a.primary_state, 3) || !Array.isArray(rings) || rings.length < 1 || rings.length > 8) return [];
    const coordinates: number[][][] = [];
    for (const rawRing of rings) {
      if (!Array.isArray(rawRing) || rawRing.length < 4 || rawRing.length > 500) return [];
      const ring: number[][] = [];
      for (const point of rawRing) {
        if (!Array.isArray(point) || point.length < 2 || !Number.isFinite(point[0]) || !Number.isFinite(point[1]) || Math.abs(point[0]) > 180 || Math.abs(point[1]) > 90) return [];
        ring.push([point[0], point[1]]);
      }
      if (ring[0][0] !== ring.at(-1)?.[0] || ring[0][1] !== ring.at(-1)?.[1]) return [];
      coordinates.push(ring);
    }
    const outer = coordinates[0];
    const lng = (Math.min(...outer.map((point) => point[0])) + Math.max(...outer.map((point) => point[0]))) / 2;
    const lat = (Math.min(...outer.map((point) => point[1])) + Math.max(...outer.map((point) => point[1]))) / 2;
    const footprint: Feature<Polygon> = { type: "Feature", properties: { scanId: a.scan_id }, geometry: { type: "Polygon", coordinates } };
    return [{ id: a.OBJECTID as number, scanId: a.scan_id as number, name: a.map_name as string, state: a.primary_state as string, year: a.date_on_map as number,
      imprintYear: integer(a.imprint_year, 1800, 2100) ? a.imprint_year as number : null, scale: a.map_scale as number,
      series: text(a.series, 30) ?? "USGS catalog", datum: text(a.datum, 30) ?? "unspecified", footprint, viewerHref: topoViewerHref(lng, lat) }];
  });
  return { sheets, more: body.exceededTransferLimit === true && body.features.length === TOPO_PAGE_SIZE };
}
