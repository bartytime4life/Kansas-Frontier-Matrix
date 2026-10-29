import type { Feature, Polygon } from "geojson";
import type { OfficialContextPayload, OfficialContextSource } from "./live-context";

export const DEFLOCK_ID = "deflock-alpr" as const;
export const DEFLOCK_GRID_DEGREES = 0.05;
export const DEFLOCK_MAX_RECORDS = 5000;
export const DEFLOCK_COLOR = "#9b72cf";
export const DEFLOCK_LICENSE = "https://opendatacommons.org/licenses/odbl/1-0/";
export const DEFLOCK_LIMITATION = "Community-reported ALPR nodes from OpenStreetMap using DeFlock's tagging convention. Counts describe mapped reports, not verified cameras or current operation. Locations are generalized to 0.05° cells (about 4.3 × 5.6 km in Kansas); cells are not camera coverage or jurisdiction boundaries. Exact locations and identifying tags are withheld pending sensitivity review. Missing reports never establish that an area is camera-free. Database time is not installation, observation or verification time. External context only; no KFM evidence release.";

export const DEFLOCK_SOURCE: OfficialContextSource = Object.freeze({
  id: DEFLOCK_ID, title: "DeFlock · community-reported ALPR areas", shortTitle: "DeFlock · reported ALPR areas",
  organization: "OpenStreetMap contributors · DeFlock tagging", domain: "Roads, rail & movement", kind: "OPERATIONAL_GEOJSON",
  sourceId: "external-deflock-alpr", layerIds: ["external-deflock-alpr-fill", "external-deflock-alpr-line", "external-deflock-alpr-count"],
  interactiveLayerIds: ["external-deflock-alpr-fill"], apiPath: "/api/live-context?feed=deflock-alpr",
  endpointLabel: "Kansas OSM ALPR nodes · 0.05° generalized report cells",
  sourceUrl: "https://deflock.org/", serviceUrl: "https://overpass-api.de/",
  cadence: "On selection or refresh; shared server cache up to one hour",
  freshness: "OSM database snapshot; each report's observation date and current operation are unknown",
  defaultVisibility: false, defaultOpacity: 0.35, color: DEFLOCK_COLOR,
  attribution: 'DeFlock tagging · © <a href="https://www.openstreetmap.org/copyright">OpenStreetMap contributors</a> · <a href="https://opendatacommons.org/licenses/odbl/1-0/">ODbL</a>',
  evidenceRole: "EXTERNAL_CONTEXT_ONLY", boundary: DEFLOCK_LIMITATION,
  legend: "Violet grid cells contain mapped ALPR reports; numbers count reports per cell, not verified devices. Every cell is 0.05°; not a surveillance footprint.",
  legendUrl: "https://www.openstreetmap.org/copyright",
  fallback: "Unavailable, malformed or over-budget source responses leave the layer unavailable; no substitute locations or camera-free inference.",
});

const record = (value: unknown): value is Record<string, unknown> => Boolean(value) && typeof value === "object" && !Array.isArray(value);

/** Raw positions and all OSM tags stop here. Only generalized, deterministic cell counts leave the adapter. */
export function parseDeflock(raw: unknown, now = new Date()): OfficialContextPayload {
  if (!record(raw) || raw.remark || !Array.isArray(raw.elements) || raw.elements.length > DEFLOCK_MAX_RECORDS + 1
    || !record(raw.osm3s) || typeof raw.osm3s.timestamp_osm_base !== "string") throw new Error("Invalid or incomplete OSM response.");
  const sourceTime = Date.parse(raw.osm3s.timestamp_osm_base);
  if (!Number.isFinite(sourceTime) || sourceTime < Date.UTC(2004, 0, 1) || sourceTime > now.getTime() + 300_000) throw new Error("Invalid OSM database time.");
  // Echoing the area object makes missing/ambiguous area selection different from zero matching nodes.
  const areas = raw.elements.filter(e => record(e) && e.type === "area");
  if (areas.length !== 1 || !Number.isSafeInteger(areas[0].id) || areas[0].id <= 0) throw new Error("Kansas source area unavailable.");
  const cells = new Map<string, { x: number; y: number; count: number }>(), ids = new Set<number>();
  let omitted = 0, accepted = 0;
  for (const e of raw.elements) {
    if (e === areas[0]) continue;
    if (!record(e) || e.type !== "node" || !Number.isSafeInteger(e.id) || (e.id as number) <= 0
      || typeof e.lon !== "number" || typeof e.lat !== "number" || !Number.isFinite(e.lon) || !Number.isFinite(e.lat)
      || e.lon < -102.06 || e.lon > -94.58 || e.lat < 36.99 || e.lat > 40.01
      || !record(e.tags) || e.tags.man_made !== "surveillance" || e.tags["surveillance:type"] !== "ALPR"
      || ["disused", "abandoned", "removed", "demolished"].some(key => (e.tags as Record<string, unknown>)[key] === "yes")
      || e.tags.operational_status === "removed") { omitted++; continue; }
    if (ids.has(e.id as number)) throw new Error("Duplicate OSM identity.");
    ids.add(e.id as number);
    const x = Math.floor(e.lon * 20), y = Math.floor(e.lat * 20), id = `deflock-grid-${x}-${y}`;
    const cell = cells.get(id) ?? { x, y, count: 0 }; cell.count++; cells.set(id, cell); accepted++;
  }
  const retrievedAt = now.toISOString(), upstreamUpdatedAt = new Date(sourceTime).toISOString();
  const features: Feature<Polygon>[] = [...cells].sort(([a], [b]) => a.localeCompare(b)).map(([id, cell]) => {
    const west = cell.x / 20, east = (cell.x + 1) / 20, south = cell.y / 20, north = (cell.y + 1) / 20;
    return { type: "Feature", id, geometry: { type: "Polygon", coordinates: [[[west, south], [east, south], [east, north], [west, north], [west, south]]] },
      properties: { featureId: id, name: `${cell.count} community-reported ALPR ${cell.count === 1 ? "node" : "nodes"} · generalized area`, reportCount: cell.count,
        gridDegrees: DEFLOCK_GRID_DEGREES, retrievedAt, upstreamUpdatedAt, evidenceRole: "EXTERNAL_CONTEXT_ONLY", locationPrecision: "generalized-grid", license: DEFLOCK_LICENSE } };
  });
  return { feed: DEFLOCK_ID, state: omitted ? "partial" : features.length ? "ready" : "empty", retrievedAt, upstreamUpdatedAt,
    featureCount: features.length, data: { type: "FeatureCollection", features }, source: "© OpenStreetMap contributors · ODbL 1.0 · DeFlock ALPR tagging · fixed Kansas Overpass query",
    limitation: `${accepted} mapped reports in ${features.length} generalized cells; ${omitted} invalid, out-of-scope or inactive-tagged records withheld. ${DEFLOCK_LIMITATION} Data license: ${DEFLOCK_LICENSE}`,
    truncated: false };
}
