import { boundedFetch } from "./api/event-atlas/upstream";
import type { FeatureCollection, Geometry } from "geojson";

export const COUNTY_EDITIONS = { "2010": 100, "2020": 82 } as const;
export type CountyEdition = keyof typeof COUNTY_EDITIONS;
const number = (value: unknown) => value !== null && value !== undefined && String(value).trim() !== "" && Number.isFinite(Number(value)) && Number(value) >= 0 ? Number(value) : null;

async function readCountyBaseline(edition: CountyEdition, fetcher: typeof boundedFetch, timeoutMs: number) {
  const url = new URL(`https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/tigerWMS_Census${edition}/MapServer/${COUNTY_EDITIONS[edition]}/query`);
  url.search = new URLSearchParams({ where: "STATE='20'", outFields: "GEOID,NAME,BASENAME,STATE,COUNTY,AREALAND,AREAWATER,POP100,HU100", returnGeometry: "true", outSR: "4326", geometryPrecision: "5", maxAllowableOffset: "0.001", f: "geojson" }).toString();
  const raw = JSON.parse((await fetcher(url.toString(), 6 * 1024 * 1024, { timeoutMs })).text());
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

export type CountyBaseline = Awaited<ReturnType<typeof readCountyBaseline>>;
/** A decennial baseline does not change. One good answer is kept for a day, the lifetime the feed already
 * tells caches, so Census is not asked again on every request that reaches the server. */
export const COUNTY_BASELINE_FRESH_MS = 24 * 60 * 60 * 1000;
/** If Census cannot be reached when that day is up, the kept answer still serves for one more day,
 * the feed's stale-while-revalidate window. After that the failure is reported. */
export const COUNTY_BASELINE_STALE_MS = 2 * COUNTY_BASELINE_FRESH_MS;
/** Census sometimes leaves a request hanging and answers the next one at once. Two attempts fit
 * inside the 18 seconds a single attempt used to be given. */
export const COUNTY_BASELINE_ATTEMPT_TIMEOUTS_MS = Object.freeze([7_000, 11_000]);

export function createCountyBaseline(fetcher: typeof boundedFetch = boundedFetch, now: () => number = Date.now) {
  const kept = new Map<CountyEdition, { baseline: CountyBaseline; at: number }>();
  const pending = new Map<CountyEdition, Promise<CountyBaseline>>();
  return async function countyBaseline(edition: CountyEdition): Promise<CountyBaseline> {
    const held = kept.get(edition);
    if (held && now() - held.at < COUNTY_BASELINE_FRESH_MS) return held.baseline;
    // Requests that arrive together (the county layer and the FEMA feed on a cold start) share one read.
    let request = pending.get(edition);
    if (!request) {
      request = (async () => {
        let failure: unknown;
        for (const timeoutMs of COUNTY_BASELINE_ATTEMPT_TIMEOUTS_MS) {
          try {
            const baseline = await readCountyBaseline(edition, fetcher, timeoutMs);
            kept.set(edition, { baseline, at: now() });
            return baseline;
          } catch (error) { failure = error; }
        }
        throw failure;
      })().finally(() => pending.delete(edition));
      pending.set(edition, request);
    }
    try { return await request; }
    catch (error) {
      if (held && now() - held.at < COUNTY_BASELINE_STALE_MS) return held.baseline;
      throw error;
    }
  };
}
/** The Census county baseline for an edition: the same official answer, kept and retried as described above. */
export const countyBaseline = createCountyBaseline();
