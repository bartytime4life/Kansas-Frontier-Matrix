import { boundedFetch } from "./api/event-atlas/upstream";
import type { FeatureCollection, Geometry } from "geojson";

export const COUNTY_EDITIONS = { "2010": 100, "2020": 82 } as const;
export type CountyEdition = keyof typeof COUNTY_EDITIONS;
const number = (value: unknown) => value !== null && value !== undefined && String(value).trim() !== "" && Number.isFinite(Number(value)) && Number(value) >= 0 ? Number(value) : null;

export async function countyBaseline(edition: CountyEdition) {
  const url = new URL(`https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/tigerWMS_Census${edition}/MapServer/${COUNTY_EDITIONS[edition]}/query`);
  url.search = new URLSearchParams({ where: "STATE='20'", outFields: "GEOID,NAME,BASENAME,STATE,COUNTY,AREALAND,AREAWATER,POP100,HU100", returnGeometry: "true", outSR: "4326", geometryPrecision: "5", maxAllowableOffset: "0.001", f: "geojson" }).toString();
  const raw = JSON.parse((await boundedFetch(url.toString(), 6 * 1024 * 1024)).text());
  if (raw.type !== "FeatureCollection" || !Array.isArray(raw.features) || raw.features.length !== 105 || raw.exceededTransferLimit) throw new Error("Census did not return all 105 Kansas counties.");
  const ids = new Set<string>();
  const data: FeatureCollection = { type: "FeatureCollection", features: raw.features.map((feature: { geometry: Geometry; properties: Record<string, unknown> }) => {
    const p = feature.properties;
    if (!p || typeof p.GEOID !== "string" || !/^20\d{3}$/.test(p.GEOID) || ids.has(p.GEOID) || !["Polygon", "MultiPolygon"].includes(feature.geometry?.type)) throw new Error("Census county identity or geometry was invalid.");
    ids.add(p.GEOID);
    return { type: "Feature", id: p.GEOID, geometry: feature.geometry, properties: {
      featureId: `us-census-county-${p.GEOID}`, geoid: p.GEOID, name: p.BASENAME ?? p.NAME, stateFips: "20", countyFips: p.GEOID.slice(2),
      population: number(p.POP100), housingUnits: number(p.HU100), landSquareMiles: number(p.AREALAND) === null ? null : Number(p.AREALAND) / 2589988.110336, waterSquareMiles: number(p.AREAWATER) === null ? null : Number(p.AREAWATER) / 2589988.110336,
      populationEstimate: number(p.POP100), populationEstimateYear: Number(edition), populationEstimateProduct: `${edition} decennial census count`, vintage: edition, sourceOrganization: "U.S. Census Bureau", evidenceRole: "EXTERNAL_CONTEXT_ONLY",
    } };
  }) };
  return { data, edition, source: url.toString(), retrievedAt: new Date().toISOString(), limitation: `${edition} Census geography, population and housing counts for all 105 Kansas counties. Land/water area is in square miles. This is a pinned baseline, not a reconstruction of county boundaries or population at the event date.` };
}
