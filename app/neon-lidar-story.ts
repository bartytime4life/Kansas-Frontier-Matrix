/** Actual sampled locations for a user-directed map story; no inferred native extrema. */
import { neonLidarProbe, type NeonLidarMode, type NeonLidarPreview } from "./neon-lidar-preview";

export type NeonStoryStop = {
  id: "low-ground" | "high-ground" | "high-canopy" | "surface-gap";
  label: string; mode: NeonLidarMode; row: number; column: number; value_m: number;
  /** Center of the transformed display footprint, not a native sample position. */
  display_center: [number, number] | null;
  probe: NonNullable<ReturnType<typeof neonLidarProbe>>;
};
const finite = (value: unknown): value is number => typeof value === "number" && Number.isFinite(value);

function displayCenter(preview: NeonLidarPreview, row: number, column: number): [number, number] | null {
  const geo = preview.georeferencing;
  if (!geo || geo.corner_width !== preview.grid.width + 1 || geo.corners.length !== geo.corner_width ** 2) return null;
  const nw = row * geo.corner_width + column;
  const corners = [geo.corners[nw], geo.corners[nw + 1], geo.corners[nw + geo.corner_width], geo.corners[nw + geo.corner_width + 1]];
  if (corners.some(point => !Array.isArray(point) || point.length !== 2 || !point.every(finite))) return null;
  // Average display corners only to frame the cell. Probes retain the actual
  // nearest 1 m sample's native coordinate and original measurement values.
  return [corners.reduce((sum, point) => sum + point[0] / 4, 0), corners.reduce((sum, point) => sum + point[1] / 4, 0)];
}

export function buildNeonStoryStops(preview: NeonLidarPreview): NeonStoryStop[] {
  const { width, height } = preview.grid;
  if (!Number.isInteger(width) || !Number.isInteger(height) || width < 1 || height < 1 || width * height > 128 ** 2) return [];
  const stops = new Map<NeonStoryStop["id"], NeonStoryStop>();
  function consider(id: NeonStoryStop["id"], label: string, mode: NeonLidarMode, probe: NeonStoryStop["probe"], value: number | null, lower = false) {
    if (!finite(value)) return;
    const previous = stops.get(id);
    // Strict comparison keeps the first row-major sample when values tie.
    if (previous && (lower ? value >= previous.value_m : value <= previous.value_m)) return;
    stops.set(id, { id, label, mode, row: probe.row, column: probe.column, value_m: value,
      display_center: displayCenter(preview, probe.row, probe.column), probe });
  }
  for (let row = 0; row < height; row++) for (let column = 0; column < width; column++) {
    const probe = neonLidarProbe(preview, row, column);
    if (!probe) continue;
    consider("low-ground", "Lowest sampled ground", "dtm", probe, probe.dtm, true);
    consider("high-ground", "Highest sampled ground", "dtm", probe, probe.dtm);
    consider("high-canopy", "Highest sampled canopy", "chm", probe, probe.chm);
    consider("surface-gap", "Largest sampled DSM − DTM", "dsm", probe, probe.surfaceAboveGround);
  }
  return ["low-ground", "high-ground", "high-canopy", "surface-gap"].flatMap(id => {
    const stop = stops.get(id as NeonStoryStop["id"]);
    return stop ? [stop] : [];
  });
}
