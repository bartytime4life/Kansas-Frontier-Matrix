import type { Feature, Geometry } from "geojson";
import type { OfficialContextPayload, OfficialContextState } from "./live-context";

export type CountySearchItem = Readonly<{
  id: string;
  kind: "county";
  title: string;
  subtitle: string;
  featureId: string;
}>;

// The county feed is asynchronous; an absent county row is not a completed
// global no-match while that feed or the current query is still unsettled.
export function globalSearchStatus(
  query: string,
  settledQuery: string,
  countyState: OfficialContextState,
  resultCount: number,
): Readonly<{ message: string; busy: boolean }> {
  const term = query.trim();
  if (!term) return { message: "", busy: false };
  if (term.toLocaleLowerCase("en-US") !== settledQuery.trim().toLocaleLowerCase("en-US")) {
    return { message: "Updating search…", busy: true };
  }
  if (countyState === "idle") return { message: "County search is not ready. Available layers, features, and official sources can still be searched.", busy: false };
  if (countyState === "loading") return { message: "Loading county matches…", busy: true };
  if (countyState === "empty") return { message: "No counties are available to search.", busy: false };
  if (countyState === "partial") return { message: "County search has limited coverage.", busy: false };
  if (countyState === "ready") return {
    message: resultCount ? "" : `No matches for “${term}”. Try a county, layer, feature, or official source name.`, busy: false,
  };
  // Errors and unexpected runtime states cannot establish complete coverage.
  return {
    message: resultCount ? "County search is unavailable. Showing available matches."
      : "County search is unavailable. You can still search available layers, features, and official sources.",
    busy: false,
  };
}

// Search only the county baseline already returned by the bounded adapter.
// This is a display index, not a gazetteer, source registry or evidence release.
export function countySearchResults(
  payload: OfficialContextPayload | undefined,
  state: OfficialContextState,
  query: string,
): CountySearchItem[] {
  const term = query.trim().toLocaleLowerCase("en-US");
  if (!term || !["ready", "partial"].includes(state) || payload?.feed !== "census-counties" || !Array.isArray(payload.data?.features)) return [];
  return payload.data.features.flatMap(feature => {
    const p = feature.properties;
    if (!p || !/^us-census-county-20\d{3}$/.test(p.featureId ?? "") ||
        typeof p.name !== "string" || !p.name.trim() || p.name.length > 100 ||
        !["2010", "2020"].includes(String(p.vintage))) return [];
    const title = /\bcounty$/i.test(p.name.trim()) ? p.name.trim() : `${p.name.trim()} County`;
    if (!`${title} Kansas ${p.geoid ?? ""}`.toLocaleLowerCase("en-US").includes(term)) return [];
    return [{ id: `county:${p.featureId}`, kind: "county" as const, title,
      subtitle: `${p.vintage} U.S. Census baseline · source context, not KFM evidence`, featureId: p.featureId }];
  }).sort((a, b) => a.title.localeCompare(b.title, "en-US")).slice(0, 7);
}

export function countySearchGeometry(feature: Feature<Geometry>) {
  if (!["Polygon", "MultiPolygon"].includes(feature.geometry?.type) ||
      !("coordinates" in feature.geometry) || !Array.isArray(feature.geometry.coordinates)) return null;
  const rings = feature.geometry.type === "Polygon" ? feature.geometry.coordinates
    : feature.geometry.type === "MultiPolygon" ? feature.geometry.coordinates.flat() : [];
  let west = Infinity, east = -Infinity, south = Infinity, north = -Infinity, count = 0;
  for (const ring of rings) {
   if (!Array.isArray(ring)) return null;
   for (const point of ring) {
    if (!Array.isArray(point) || point.length < 2) return null;
    const [lng, lat] = point;
    if (!Number.isFinite(lng) || !Number.isFinite(lat) || lng < -180 || lng > 180 || lat < -90 || lat > 90) return null;
    west = Math.min(west, lng); east = Math.max(east, lng);
    south = Math.min(south, lat); north = Math.max(north, lat); count++;
   }
  }
  if (!count || west >= east || south >= north) return null;
  return { bounds: [[west, south], [east, north]] as [[number, number], [number, number]],
    focus: [(west + east) / 2, (south + north) / 2] as [number, number] };
}
