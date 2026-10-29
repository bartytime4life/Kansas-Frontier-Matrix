import type { Feature, Polygon, MultiPolygon } from "geojson";
import type { OfficialContextPayload, OfficialContextSource } from "./live-context";

export const CIVIC_ID = "census-congress-119" as const;
export const CIVIC_SERVICE = "https://tigerweb.geo.census.gov/arcgis/rest/services/Generalized_ACS2025/Legislative/MapServer/5";
export const CIVIC_OFFICIAL_MAPS = "https://www.sos.ks.gov/elections/district-maps.html";
export const CIVIC_LIMITATION = "U.S. Census Bureau generalized 1:500,000 congressional district geography, January 1, 2025 vintage, for the 119th Congress (2025–2027). Colors identify districts, not parties or election results. Boundaries are display reference, not an address-level voting determination. No officeholders, polling places or current ballot eligibility are inferred. Confirm election geography with Kansas election officials. External context only; no KFM evidence release.";
export const CIVIC_SOURCE: OfficialContextSource = Object.freeze({
  id: CIVIC_ID, title: "Kansas U.S. House districts through time", shortTitle: "U.S. House district history",
  organization: "U.S. Census Bureau · Lewis, DeVine, Pitcher and Martis", domain: "Government & civic", kind: "SNAPSHOT_GEOJSON",
  sourceId: "external-census-congress-119", layerIds: ["external-census-congress-119-fill", "external-census-congress-119-line", "external-census-congress-119-label", "external-census-congress-119-at-large"],
  interactiveLayerIds: ["external-census-congress-119-fill", "external-census-congress-119-at-large"], apiPath: "/api/live-context?feed=census-congress-119",
  sourceUrl: CIVIC_SERVICE, serviceUrl: CIVIC_SERVICE, endpointLabel: "Kansas · Congresses 36–119 · Census and pinned historical plans",
  cadence: "On selection or refresh; shared server cache up to 24 hours", freshness: "1861 statehood through the 119th Congress · exact selected Congress and source edition shown on each record",
  defaultVisibility: false, defaultOpacity: 0.32, color: "#397f7a",
  attribution: '<a href="https://www.census.gov/">U.S. Census Bureau</a> · ACS 2025 generalized districts · <a href="https://cdmaps.polisci.ucla.edu/">Lewis et al. historical districts</a> · <a href="/civic-history-license.txt">MIT license</a>',
  evidenceRole: "EXTERNAL_CONTEXT_ONLY", boundary: "Kansas congressional history from statehood, with Census geometry for the 119th Congress and scholarly reconstructed earlier plans. Dates select Congress terms, not election dates. At-large constituencies may overlap numbered districts and elect multiple representatives. External context only; inspect each record for source and limitations.",
  legend: "Colors identify district numbers, not parties. At-large boundaries use a dashed outline when numbered districts coexist.", legendUrl: CIVIC_OFFICIAL_MAPS,
  fallback: "Missing, incomplete or changed-edition responses leave the layer unavailable. No boundaries are invented or replaced with another Congress.",
});

const object = (v: unknown): v is Record<string, unknown> => Boolean(v) && typeof v === "object" && !Array.isArray(v);
const position = (p: unknown): p is [number, number] => Array.isArray(p) && p.length === 2 && typeof p[0] === "number" && typeof p[1] === "number"
  && Number.isFinite(p[0]) && Number.isFinite(p[1]) && p[0] >= -102.1 && p[0] <= -94.5 && p[1] >= 36.9 && p[1] <= 40.1;

export function validateCivicGeometry(value: unknown, budget: { vertices: number }): Polygon | MultiPolygon {
  if (!object(value)) throw new Error("Invalid district geometry.");
  const g = value;
    const polygons = g.type === "Polygon" ? [g.coordinates] : g.type === "MultiPolygon" ? g.coordinates : null;
    if (!Array.isArray(polygons) || !polygons.length || polygons.length > 1000) throw new Error("Invalid district geometry.");
    for (const polygon of polygons) {
      if (!Array.isArray(polygon) || !polygon.length) throw new Error("Missing district ring.");
      for (const ring of polygon) {
        if (!Array.isArray(ring) || ring.length < 4 || (budget.vertices += ring.length) > 50_000 || !ring.every(position)
          || ring[0][0] !== ring[ring.length - 1][0] || ring[0][1] !== ring[ring.length - 1][1]) throw new Error("Invalid or oversized district ring.");
        let twiceArea = 0; for (let i = 1; i < ring.length; i++) twiceArea += ring[i - 1][0] * ring[i][1] - ring[i][0] * ring[i - 1][1];
        if (Math.abs(twiceArea) < 1e-10) throw new Error("Degenerate district ring.");
      }
    }
  return { type: g.type, coordinates: g.coordinates } as Polygon | MultiPolygon;
}

/** Validate the complete four-district edition; never fill a missing district from a different vintage. */
export function parseCivicDistricts(raw: unknown, now = new Date()): OfficialContextPayload {
  if (!object(raw) || raw.error || raw.exceededTransferLimit || raw.type !== "FeatureCollection" || !Array.isArray(raw.features) || raw.features.length !== 4) throw new Error("Incomplete congressional geography.");
  const ids = new Set<string>(), budget = { vertices: 0 };
  const retrievedAt = now.toISOString();
  const features: Feature<Polygon | MultiPolygon>[] = raw.features.map(row => {
    if (!object(row) || row.type !== "Feature" || !object(row.properties) || !object(row.geometry)) throw new Error("Invalid district feature.");
    const p = row.properties, g = row.geometry;
    if (p.STATE !== "20" || p.CDSESSN !== "119" || typeof p.GEOID !== "string" || !/^200[1-4]$/.test(p.GEOID) || ids.has(p.GEOID)) throw new Error("District identity or Congress changed.");
    ids.add(p.GEOID);
    const geometry = validateCivicGeometry(g, budget);
    const district = Number(p.GEOID.slice(2)), id = `census-119-${p.GEOID}`;
    return { type: "Feature", id, geometry,
      properties: { featureId: id, geoid: p.GEOID, district, name: `Kansas U.S. House District ${district}`, congress: "119th Congress · 2025–2027", vintage: "2025-01-01",
        displayScale: "1:500,000 generalized", congressNumber: 119, termStart: "2025-01-03", termEndExclusive: "2027-01-03", sourceOrganization: "U.S. Census Bureau", sourceUrl: CIVIC_SERVICE, basis: "Census generalized geography", limitation: CIVIC_LIMITATION, retrievedAt, evidenceRole: "EXTERNAL_CONTEXT_ONLY", officialMapsUrl: CIVIC_OFFICIAL_MAPS } };
  });
  features.sort((a, b) => a.properties!.district - b.properties!.district);
  return { feed: CIVIC_ID, state: "ready", featureCount: 4, retrievedAt, upstreamUpdatedAt: null,
    data: { type: "FeatureCollection", features }, source: "U.S. Census Bureau · Generalized ACS 2025 · 119th Congressional Districts 500K · Kansas",
    limitation: CIVIC_LIMITATION, truncated: false };
}
