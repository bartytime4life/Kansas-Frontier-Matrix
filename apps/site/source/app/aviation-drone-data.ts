/**
 * FAA UAS Facility Map (UASFM) grid ceilings and the FAA temporary flight
 * restriction (TFR) list. UASFM cells give the maximum altitude, 0–400 ft AGL,
 * that LAANC can authorize near an airport; they do not authorize a flight.
 * The TFR list has no geometry here: each entry is shown as text with its NOTAM.
 */
export const UASFM_API_PATH = "/api/aviation/uas-grid";
export const TFR_API_PATH = "/api/aviation/tfrs";
export const UASFM_SERVICE = "https://services6.arcgis.com/ssFJjBXIUyZDrSYZ/arcgis/rest/services/FAA_UAS_FacilityMap_Data/FeatureServer/0";
export const UASFM_PAGE_SIZE = 2000;
export const UASFM_MAX_PAGES = 15;
export const UASFM_MAX_CELLS = 30000;
export const TFR_LIST_URL = "https://tfr.faa.gov/tfrapi/exportTfrList";
export const TFR_HOME = "https://tfr.faa.gov/";

// Fixed query: Kansas region envelope, three fields, stable order, paged by offset.
export const uasfmPageUrl = (page: number): string => {
  if (!Number.isInteger(page) || page < 0 || page >= UASFM_MAX_PAGES) throw new Error("UASFM page out of range.");
  const params = new URLSearchParams({ where: "1=1", geometry: "-102.3,36.7,-94.3,40.3", geometryType: "esriGeometryEnvelope", inSR: "4326",
    spatialRel: "esriSpatialRelIntersects", outFields: "CEILING,APT1_FAAID,APT1_NAME", returnGeometry: "true", outSR: "4326", geometryPrecision: "5",
    orderByFields: "OBJECTID", resultRecordCount: String(UASFM_PAGE_SIZE), resultOffset: String(page * UASFM_PAGE_SIZE), f: "geojson" });
  return `${UASFM_SERVICE}/query?${params.toString()}`;
};

export type UasCell = Readonly<{ ceilingFt: number; airport: string | null; airportName: string | null; bbox: readonly [number, number, number, number];
  ring: readonly (readonly [number, number])[] }>;

const isObject = (value: unknown): value is Record<string, unknown> => Boolean(value) && typeof value === "object" && !Array.isArray(value);
const position = (value: unknown): value is [number, number] => Array.isArray(value) && value.length >= 2
  && typeof value[0] === "number" && Number.isFinite(value[0]) && Math.abs(value[0]) <= 180 && typeof value[1] === "number" && Number.isFinite(value[1]) && Math.abs(value[1]) <= 90;
const text = (value: unknown, max: number): string | null => typeof value === "string" && value.trim() && value.length <= max ? value.trim() : null;

/** One ArcGIS GeoJSON page. An `error` body or missing CEILING fails the whole page, never a guess. */
export function parseUasfmPage(value: unknown): Readonly<{ cells: readonly UasCell[]; more: boolean }> {
  if (!isObject(value) || value.type !== "FeatureCollection" || !Array.isArray(value.features)) throw new Error("UASFM page was not a FeatureCollection.");
  const cells = value.features.flatMap((feature): UasCell[] => {
    if (!isObject(feature) || !isObject(feature.properties) || !isObject(feature.geometry)) throw new Error("UASFM feature shape changed.");
    const properties = feature.properties, ceiling = properties.CEILING;
    if (typeof ceiling !== "number" || !Number.isInteger(ceiling) || ceiling < 0 || ceiling > 400) throw new Error("UASFM CEILING missing or out of range.");
    const polygons = feature.geometry.type === "Polygon" ? [feature.geometry.coordinates] : feature.geometry.type === "MultiPolygon" ? feature.geometry.coordinates : null;
    if (!Array.isArray(polygons)) throw new Error("UASFM geometry type changed.");
    return polygons.flatMap((polygon): UasCell[] => {
      const outer = Array.isArray(polygon) ? polygon[0] : null;
      if (!Array.isArray(outer) || outer.length < 4 || !outer.every(position)) return [];
      const ring = Object.freeze(outer.map(point => Object.freeze([point[0], point[1]] as const)));
      const xs = ring.map(point => point[0]), ys = ring.map(point => point[1]);
      return [Object.freeze({ ceilingFt: ceiling, airport: text(properties.APT1_FAAID, 8), airportName: text(properties.APT1_NAME, 120),
        bbox: Object.freeze([Math.min(...xs), Math.min(...ys), Math.max(...xs), Math.max(...ys)] as [number, number, number, number]), ring })];
    });
  });
  const more = value.exceededTransferLimit === true || (isObject(value.properties) && value.properties.exceededTransferLimit === true) || value.features.length >= UASFM_PAGE_SIZE;
  return Object.freeze({ cells: Object.freeze(cells), more });
}

const inside = (lon: number, lat: number, ring: UasCell["ring"]) => {
  let crosses = false;
  for (let i = 0, j = ring.length - 1; i < ring.length; j = i++) {
    const [xi, yi] = ring[i], [xj, yj] = ring[j];
    if ((yi > lat) !== (yj > lat) && lon < (xj - xi) * (lat - yi) / (yj - yi) + xi) crosses = !crosses;
  }
  return crosses;
};

/** Lowest ceiling among cells containing the point (cells should not overlap; the lowest is the safe reading). */
export function uasCeilingAt(cells: readonly UasCell[], lon: number, lat: number): UasCell | null {
  let best: UasCell | null = null;
  for (const cell of cells) {
    if (lon < cell.bbox[0] || lon > cell.bbox[2] || lat < cell.bbox[1] || lat > cell.bbox[3] || !inside(lon, lat, cell.ring)) continue;
    if (!best || cell.ceilingFt < best.ceilingFt) best = cell;
  }
  return best;
}

export const UAS_CEILING_COLORS: readonly (readonly [number, string])[] = Object.freeze([
  [0, "#c0392b"], [50, "#e0662a"], [100, "#e8952c"], [200, "#e3c33a"], [300, "#9cc94a"], [400, "#3d9a5b"],
]);
export const uasCeilingColor = (feet: number) => [...UAS_CEILING_COLORS].reverse().find(([floor]) => feet >= floor)?.[1] ?? UAS_CEILING_COLORS[0][1];

/** Each cell is extruded from the ground to its LAANC ceiling; a 0 ft cell is a flat red tile. */
export function uasFeatures(cells: readonly UasCell[], exaggeration: number): GeoJSON.FeatureCollection {
  return { type: "FeatureCollection", features: cells.map((cell, index) => ({ type: "Feature", id: index,
    geometry: { type: "Polygon", coordinates: [cell.ring.map(point => [point[0], point[1]])] },
    properties: { ceiling: cell.ceilingFt, color: uasCeilingColor(cell.ceilingFt), base: 0, top: Math.max(2, cell.ceilingFt * 0.3048 * exaggeration),
      label: `${cell.ceilingFt} ft` } })) };
}

export type TfrEntry = Readonly<{ notam: string; type: string | null; state: string | null; facility: string | null; description: string; created: string | null }>;

const pick = (item: Record<string, unknown>, keys: readonly string[], max: number) => {
  for (const key of keys) { const value = text(item[key], max); if (value) return value; }
  return null;
};

/**
 * The FAA list's field names have changed before, so several spellings are
 * accepted. Kansas entries are those with state KS or "KANSAS"/", KS" in the text.
 */
export function parseTfrList(value: unknown): Readonly<{ kansas: readonly TfrEntry[]; total: number }> {
  const list = Array.isArray(value) ? value : isObject(value) && Array.isArray(value.tfrs) ? value.tfrs : isObject(value) && Array.isArray(value.data) ? value.data : null;
  if (!list) throw new Error("The TFR list was not an array.");
  const entries = list.slice(0, 5000).filter(isObject).flatMap((item): TfrEntry[] => {
    const notam = pick(item, ["notam_id", "notamId", "NOTAM_ID", "notam", "NOTAM"], 32);
    const description = pick(item, ["description", "desc", "DESCRIPTION", "name", "title"], 600);
    if (!notam || !description) return [];
    return [Object.freeze({ notam, description, type: pick(item, ["type", "TYPE", "legal", "tfr_type"], 64), state: pick(item, ["state", "STATE"], 32),
      facility: pick(item, ["facility", "FACILITY", "artcc", "ARTCC"], 16), created: pick(item, ["creation_date", "creationDate", "date", "mod_date"], 40) })];
  });
  const kansas = entries.filter(entry => entry.state === "KS" || /\bKANSAS\b|,\s*KS\b/i.test(entry.description));
  return Object.freeze({ kansas: Object.freeze(kansas), total: entries.length });
}
