/**
 * FAA UAS Facility Map (UASFM) grid ceilings and the FAA temporary flight
 * restriction (TFR) list. UASFM cells give the maximum altitude, 0–400 ft AGL,
 * that LAANC can authorize near an airport; they do not authorize a flight.
 * TFR boundaries and altitude limits come from each NOTAM's XNOTAM detail file.
 */
export const UASFM_API_PATH = "/api/aviation/uas-grid";
export const TFR_API_PATH = "/api/aviation/tfrs";
export const UASFM_SERVICE = "https://services6.arcgis.com/ssFJjBXIUyZDrSYZ/arcgis/rest/services/FAA_UAS_FacilityMap_Data/FeatureServer/0";
export const UASFM_PAGE_SIZE = 2000;
export const UASFM_MAX_PAGES = 15;
export const UASFM_MAX_CELLS = 30000;
export const TFR_LIST_URL = "https://tfr.faa.gov/tfrapi/exportTfrList";
export const TFR_HOME = "https://tfr.faa.gov/";
// Subrequest budget: one list read plus at most this many detail files per refresh.
export const TFR_MAX_DETAILS = 30;
// Kansas plus the four neighbouring states: a border TFR can reach into Kansas airspace.
const TFR_REGION_STATES = new Set(["KS", "NE", "MO", "OK", "CO"]);
const TFR_REGION_TEXT = /\b(KANSAS|NEBRASKA|MISSOURI|OKLAHOMA|COLORADO)\b|,\s*(KS|NE|MO|OK|CO)\b/i;
// Same envelope as the airspace product: Kansas plus ~15 NM.
const TFR_REGION_BBOX = [-102.3, 36.7, -94.3, 40.3] as const;

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
export function parseTfrList(value: unknown): Readonly<{ kansas: readonly TfrEntry[]; regional: readonly TfrEntry[]; total: number }> {
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
  // Detail candidates: Kansas first, then neighbouring states, whose boundaries are checked against the region.
  const regional = [...kansas, ...entries.filter(entry => !kansas.includes(entry) && ((entry.state !== null && TFR_REGION_STATES.has(entry.state)) || TFR_REGION_TEXT.test(entry.description)))];
  return Object.freeze({ kansas: Object.freeze(kansas), regional: Object.freeze(regional.slice(0, TFR_MAX_DETAILS)), total: entries.length });
}

/** Detail file for one NOTAM id ("6/1234" -> detail_6_1234.xml); anything else is refused, never interpolated. */
export function tfrDetailUrl(notam: string): string {
  if (!/^\d\/\d{1,5}$/.test(notam)) throw new Error("Unexpected NOTAM id.");
  return `${TFR_HOME}download/detail_${notam.replace("/", "_")}.xml`;
}

export type TfrLimit = Readonly<{ valueFt: number; reference: "SFC" | "AGL" | "MSL" | "FL" | "UNL" }>;
export type TfrShape = Readonly<{ notam: string; type: string | null; name: string | null; floor: TfrLimit; ceiling: TfrLimit;
  effective: string | null; expires: string | null; ring: readonly (readonly [number, number])[]; bbox: readonly [number, number, number, number] }>;

const decodeXml = (value: string) => value.replace(/&(amp|lt|gt|quot|apos|#\d{1,6}|#x[0-9a-f]{1,6});/gi, (_, entity: string) => {
  const named: Record<string, string> = { amp: "&", lt: "<", gt: ">", quot: "\"", apos: "'" };
  if (entity[0] !== "#") return named[entity.toLowerCase()];
  const code = entity[1] === "x" || entity[1] === "X" ? parseInt(entity.slice(2), 16) : parseInt(entity.slice(1), 10);
  return code > 0 && code <= 0x10ffff ? String.fromCodePoint(code) : "";
});
// XNOTAM elements used here are leaf text or non-nesting groups, so a bounded tag scan is exact for them.
const blocks = (xml: string, tag: string): string[] => [...xml.matchAll(new RegExp(`<${tag}(?:\\s[^>]*)?>([\\s\\S]*?)</${tag}>`, "g"))].map(match => match[1]);
const leaf = (xml: string, tag: string, max = 400): string | null => {
  const value = blocks(xml, tag)[0];
  return value === undefined ? null : text(decodeXml(value), max);
};

/** Ported from OpenSectional's XNOTAM reader: FL is hundreds of feet, HEI is above ground, 99999 or more is unlimited, otherwise MSL. */
function tfrLimit(code: string | null, value: string | null, unit: string | null): TfrLimit {
  const feet = value !== null && /^\d{1,6}$/.test(value) ? Number(value) : null;
  if (feet === null) throw new Error("TFR altitude missing or malformed.");
  if (unit === "FL") return Object.freeze({ valueFt: feet * 100, reference: "FL" as const });
  if (code === "HEI") return Object.freeze({ valueFt: feet, reference: feet === 0 ? "SFC" as const : "AGL" as const });
  if (feet >= 99999) return Object.freeze({ valueFt: 99999, reference: "UNL" as const });
  return Object.freeze({ valueFt: feet, reference: "MSL" as const });
}

const coordinate = (value: string | null, positive: string, negative: string, limit: number): number | null => {
  const match = value ? /^(\d{1,3}(?:\.\d+)?)([A-Z])$/.exec(value) : null;
  if (!match || (match[2] !== positive && match[2] !== negative)) return null;
  // Five decimals (~1 m) keeps a 30-TFR response small without moving a boundary visibly.
  const degrees = Math.round(Number(match[1]) * 1e5) / 1e5 * (match[2] === negative ? -1 : 1);
  return Math.abs(degrees) <= limit ? degrees : null;
};

// Bounds that reject, never truncate: a shortened boundary would draw and test the wrong area.
const TFR_MAX_AREAS = 50;
const TFR_MAX_VERTICES = 20_000;

/**
 * Areas of one XNOTAM detail file that reach the Kansas region. Geometry is the
 * FAA's pre-traced `abdMergedArea` boundary (circles and arcs already
 * polygonised); the alternate `aseShapes` description is ignored. An area whose
 * boundary or limits cannot be read whole is counted in `unreadable`, never
 * dropped silently or shortened, so the map can say a restriction is missing.
 * Only areas wholly outside the region are left out without a count.
 */
export function parseTfrDetail(xml: string, notam: string): Readonly<{ shapes: readonly TfrShape[]; unreadable: number }> {
  if (!/<XNOTAM-Update[\s>]/.test(xml)) throw new Error("Not an XNOTAM document.");
  const not = blocks(xml, "Not")[0];
  const tfr = not === undefined ? undefined : blocks(not, "TfrNot")[0];
  const groups = tfr === undefined ? [] : blocks(tfr, "TFRAreaGroup");
  if (not === undefined || tfr === undefined || !groups.length) return Object.freeze({ shapes: Object.freeze([]), unreadable: 1 });
  const type = leaf(tfr, "codeType", 64), notEffective = leaf(not, "dateEffective", 40), notExpires = leaf(not, "dateExpire", 40);
  let unreadable = Math.max(0, groups.length - TFR_MAX_AREAS);
  const shapes = groups.slice(0, TFR_MAX_AREAS).flatMap((group): TfrShape[] => {
    const area = blocks(group, "aseTFRArea")[0], merged = blocks(group, "abdMergedArea")[0];
    const vertices = merged === undefined ? [] : blocks(merged, "Avx");
    if (area === undefined || vertices.length < 3 || vertices.length > TFR_MAX_VERTICES) { unreadable++; return []; }
    const points = vertices.map(vertex => [coordinate(leaf(vertex, "geoLong", 24), "E", "W", 180), coordinate(leaf(vertex, "geoLat", 24), "N", "S", 90)] as const);
    if (points.some(([lon, lat]) => lon === null || lat === null)) { unreadable++; return []; }
    const ring = (points as (readonly [number, number])[]).map(point => Object.freeze([point[0], point[1]] as const));
    const [first, last] = [ring[0], ring[ring.length - 1]];
    if (first[0] !== last[0] || first[1] !== last[1]) ring.push(first);
    const xs = ring.map(point => point[0]), ys = ring.map(point => point[1]);
    const bbox = Object.freeze([Math.min(...xs), Math.min(...ys), Math.max(...xs), Math.max(...ys)] as [number, number, number, number]);
    if (bbox[2] < TFR_REGION_BBOX[0] || bbox[0] > TFR_REGION_BBOX[2] || bbox[3] < TFR_REGION_BBOX[1] || bbox[1] > TFR_REGION_BBOX[3]) return [];
    let floor: TfrLimit, ceiling: TfrLimit;
    try {
      floor = tfrLimit(leaf(area, "codeDistVerLower", 8), leaf(area, "valDistVerLower", 8), leaf(area, "uomDistVerLower", 8));
      ceiling = tfrLimit(leaf(area, "codeDistVerUpper", 8), leaf(area, "valDistVerUpper", 8), leaf(area, "uomDistVerUpper", 8));
    } catch { unreadable++; return []; }
    const schedule = blocks(area, "ScheduleGroup")[0];
    return [Object.freeze({ notam, type, name: leaf(area, "txtName", 200), floor, ceiling, ring: Object.freeze(ring), bbox,
      effective: (schedule !== undefined ? leaf(schedule, "dateEffective", 40) : null) ?? notEffective,
      expires: (schedule !== undefined ? leaf(schedule, "dateExpire", 40) : null) ?? notExpires })];
  });
  return Object.freeze({ shapes: Object.freeze(shapes), unreadable });
}

export const formatTfrLimit = (limit: TfrLimit): string => limit.reference === "SFC" ? "SFC" : limit.reference === "UNL" ? "UNL"
  : limit.reference === "FL" ? `FL${String(Math.round(limit.valueFt / 100)).padStart(3, "0")}` : `${Math.round(limit.valueFt).toLocaleString("en-US")} ${limit.reference}`;

/** Height above the local ground reference, in feet; unlimited ceilings are drawn to FL600 like the Class A cap. */
export const tfrLimitAboveGround = (limit: TfrLimit, groundFt: number): number =>
  limit.reference === "SFC" ? 0 : limit.reference === "AGL" ? limit.valueFt : Math.max(0, (limit.reference === "UNL" ? 60000 : limit.valueFt) - groundFt);

export const TFR_COLOR = "#d0021b";

/** TFR areas whose boundary contains the point. */
export const tfrsAtPoint = (shapes: readonly TfrShape[], lon: number, lat: number): readonly TfrShape[] =>
  shapes.filter(shape => lon >= shape.bbox[0] && lon <= shape.bbox[2] && lat >= shape.bbox[1] && lat <= shape.bbox[3] && inside(lon, lat, shape.ring));

/** Each TFR area extruded from its floor to its ceiling above an approximate ground reference. */
export function tfrFeatures(shapes: readonly TfrShape[], groundFtAt: (lon: number, lat: number) => number, exaggeration: number): GeoJSON.FeatureCollection {
  return { type: "FeatureCollection", features: shapes.map((shape, index) => {
    const ground = groundFtAt((shape.bbox[0] + shape.bbox[2]) / 2, (shape.bbox[1] + shape.bbox[3]) / 2);
    const base = tfrLimitAboveGround(shape.floor, ground) * 0.3048 * exaggeration;
    const top = Math.max(base + 30, tfrLimitAboveGround(shape.ceiling, ground) * 0.3048 * exaggeration);
    return { type: "Feature", id: index, geometry: { type: "Polygon", coordinates: [shape.ring.map(point => [point[0], point[1]])] },
      properties: { notam: shape.notam, base, top, color: TFR_COLOR,
        label: `TFR ${shape.notam}${shape.type ? ` ${shape.type}` : ""} · ${formatTfrLimit(shape.floor)}–${formatTfrLimit(shape.ceiling)}` } };
  }) };
}
