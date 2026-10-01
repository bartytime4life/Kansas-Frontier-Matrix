import type { Feature, FeatureCollection, Geometry, GeoJsonProperties } from "geojson";

export const FEMA_DECLARATION_LIMIT = 250;
type Row = Record<string, unknown>;
const record = (value: unknown): value is Row => Boolean(value) && typeof value === "object" && !Array.isArray(value);
const string = (value: unknown, max = 120) => typeof value === "string" && value.length <= max ? value.trim() : null;
const utc = (value: unknown) => {
  const text = string(value, 40);
  if (!text || !/^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(?:\.\d+)?Z$/.test(text)) return null;
  const parsed = Date.parse(text);
  return Number.isFinite(parsed) ? new Date(parsed).toISOString() : null;
};

/** County designation geometry is a 2020 locator, never a disaster footprint. */
export function parseFemaDeclarations(payload: unknown, counties: FeatureCollection, retrievedAt: string) {
  if (!record(payload) || !Array.isArray(payload.DisasterDeclarationsSummaries)
    || counties.type !== "FeatureCollection" || counties.features.length !== 105) throw new Error("FEMA_RESPONSE_SHAPE");
  const countyByGeoid = new Map(counties.features.map(feature => [feature.properties?.geoid, feature]));
  const features: Feature<Geometry, GeoJsonProperties>[] = [];
  const seen = new Set<string>();
  let skipped = 0;
  let newest: string | null = null;
  for (const candidate of payload.DisasterDeclarationsSummaries) {
    if (features.length >= FEMA_DECLARATION_LIMIT) break;
    if (!record(candidate)) { skipped += 1; continue; }
    const id = string(candidate.id, 100);
    const state = string(candidate.state, 2);
    const stateFips = string(candidate.fipsStateCode, 2);
    const countyFips = string(candidate.fipsCountyCode, 3);
    const declarationAt = utc(candidate.declarationDate);
    const disasterNumber = candidate.disasterNumber;
    const county = countyFips ? countyByGeoid.get(`20${countyFips}`) : null;
    if (!id || !/^[A-Za-z0-9-]+$/.test(id) || seen.has(id) || state !== "KS" || stateFips !== "20"
      || !countyFips || !/^\d{3}$/.test(countyFips) || !county || !declarationAt
      || typeOfDisasterNumber(disasterNumber) === null
      || !county.geometry || !["Polygon", "MultiPolygon"].includes(county.geometry.type)) {
      skipped += 1;
      continue;
    }
    seen.add(id);
    const incidentBeginAt = utc(candidate.incidentBeginDate);
    const incidentEndAt = utc(candidate.incidentEndDate);
    const featureId = `fema-${id}`;
    features.push({ type: "Feature", id: featureId, geometry: county.geometry, properties: {
      featureId, name: `${string(candidate.designatedArea) || county.properties?.name || "Kansas county"} · FEMA ${disasterNumber}`,
      disasterNumber, declarationType: string(candidate.declarationType, 12),
      incidentType: string(candidate.incidentType, 80), designatedArea: string(candidate.designatedArea),
      countyGeoid: `20${countyFips}`, countyName: county.properties?.name,
      declarationAt, incidentBeginAt, incidentEndAt, retrievedAt,
      geometryRole: "2020 Census county locator, not disaster footprint",
      evidenceRole: "EXTERNAL_CONTEXT_ONLY", providerRecordId: id,
    } });
    if (!newest || declarationAt > newest) newest = declarationAt;
  }
  const truncated = payload.DisasterDeclarationsSummaries.length > FEMA_DECLARATION_LIMIT;
  return { data: { type: "FeatureCollection" as const, features }, skipped, truncated,
    upstreamUpdatedAt: newest, partial: skipped > 0 || truncated };
}

function typeOfDisasterNumber(value: unknown): number | null {
  return typeof value === "number" && Number.isInteger(value) && value > 0 && value < 100_000 ? value : null;
}
