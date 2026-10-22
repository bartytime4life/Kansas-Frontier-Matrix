import type { ResearchContext, ResearchRecord } from "./research-context";
import type { OfficialContextPayload, OfficialContextState } from "./live-context";

type County = NonNullable<ResearchContext["county"]>;
type Point = readonly [number, number];
// Bounded Kansas display geometry, not a cadastral or historical boundary test.
function validRing(value: unknown): value is Point[] {
  return Array.isArray(value) && value.length >= 4 && value.length <= 10000
    && value.every(p => Array.isArray(p) && p.length >= 2 && Number.isFinite(p[0]) && Number.isFinite(p[1])
      && p[0] >= -103 && p[0] <= -94 && p[1] >= 36 && p[1] <= 41)
    && value[0][0] === value.at(-1)[0] && value[0][1] === value.at(-1)[1];
}
function ringLocation(point: Point, ring: readonly (readonly number[])[]): "edge" | "inside" | "outside" {
  let inside = false;
  for (let i = 0, j = ring.length - 1; i < ring.length; j = i++) {
    const a = ring[j], b = ring[i];
    const cross = (point[0] - a[0]) * (b[1] - a[1]) - (point[1] - a[1]) * (b[0] - a[0]);
    if (Math.abs(cross) < 1e-12 && point[0] >= Math.min(a[0], b[0]) && point[0] <= Math.max(a[0], b[0])
      && point[1] >= Math.min(a[1], b[1]) && point[1] <= Math.max(a[1], b[1])) return "edge";
    if ((a[1] > point[1]) !== (b[1] > point[1]) && point[0] < (b[0] - a[0]) * (point[1] - a[1]) / (b[1] - a[1]) + a[0]) inside = !inside;
  }
  return inside ? "inside" : "outside";
}
function inventory(payload: OfficialContextPayload | undefined, state: OfficialContextState) {
  return ["ready", "partial"].includes(state) && payload?.feed === "census-counties" && ["ready", "partial"].includes(payload.state)
    && Array.isArray(payload.data?.features) && payload.data.features.length <= 105 ? payload.data.features : [];
}
export function researchCounties(payload: OfficialContextPayload | undefined, state: OfficialContextState): County[] {
  const rows = inventory(payload, state).flatMap(feature => {
    const p = feature?.properties;
    return p && typeof p.geoid === "string" && /^20\d{3}$/.test(p.geoid) && p.featureId === `us-census-county-${p.geoid}`
      && typeof p.name === "string" && p.name.length > 0 && p.name.length <= 100 && !/[\x00-\x1f\x7f]/.test(p.name)
      && ["2010", "2020"].includes(p.vintage)
      ? [{ geoid: p.geoid, title: /county$/i.test(p.name) ? p.name : `${p.name} County`, edition: p.vintage as County["edition"], state: "ready" as const }] : [];
  });
  // Ambiguous duplicate identity must not select an arbitrary boundary.
  return rows.filter(row => rows.filter(other => other.geoid === row.geoid).length === 1).sort((a, b) => a.title.localeCompare(b.title));
}
export function countyResearch(selected: County | null, records: readonly ResearchRecord[], payload: OfficialContextPayload | undefined, state: OfficialContextState): { county?: County; records: readonly ResearchRecord[] } {
  if (!selected) return { records };
  const available = researchCounties(payload, state).find(row => row.geoid === selected.geoid && row.edition === selected.edition);
  const feature = available && inventory(payload, state).find(row => row?.properties?.geoid === selected.geoid);
  const geometry = feature?.geometry;
  const polygons = geometry?.type === "Polygon" ? [geometry.coordinates] : geometry?.type === "MultiPolygon" ? geometry.coordinates : [];
  if (!available || !Array.isArray(polygons) || !polygons.length || polygons.length > 100 || !polygons.every(p => Array.isArray(p) && p.length > 0 && p.length <= 100 && p.every(validRing))) {
    return { county: { ...selected, state: "unavailable" }, records: [] };
  }
  return { county: available, records: records.filter(row => polygons.some(polygon => {
    const outer = ringLocation(row.coordinates, polygon[0]);
    return outer !== "outside" && !polygon.slice(1).some(hole => ringLocation(row.coordinates, hole) !== "outside");
  })) };
}
