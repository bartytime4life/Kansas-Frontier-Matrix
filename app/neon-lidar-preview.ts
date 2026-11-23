/** Bounded local preview contract. Original GeoTIFF checks belong to the offline preparer. */
export const NEON_LIDAR_MAX_BYTES = 2 * 1024 * 1024;
export const NEON_LIDAR_SCHEMA = "kfm-neon-lidar-preview-v1";
export type NeonLidarMode = "dtm" | "dsm" | "chm";
export type NeonLidarGeoreferencing = {
  method: "rasterio-warp-transform"; target_crs: "EPSG:4326"; source_crs: string;
  coordinate_epoch: null; height_values_transformed: false; horizontal_accuracy_m: null;
  corner_width: number; corners: [number, number][];
};
export type NeonLidarPreview = {
  schema_version: typeof NEON_LIDAR_SCHEMA;
  data_kind: "provider-files" | "synthetic-test";
  generated_at: string;
  source: {
    site: "KONZ" | "KONA" | "UKFS"; month: string; acquisition_run: string; release: string; tile: string;
    attribution: string; horizontal_crs: string; vertical_reference: string; vertical_reference_basis: string;
    canopy_floor_m: null | 0.7 | 2; canopy_floor_basis: string;
    files: { kind: NeonLidarMode; name: string; product: string; sha256: string; bytes: number }[];
  };
  grid: {
    width: number; height: number; bounds: [number, number, number, number];
    source_resolution_m: 1; preview_resolution_m: number; sampling: "nearest-neighbor";
    dtm: (number | null)[]; dsm: (number | null)[]; chm: (number | null)[];
  };
  georeferencing?: NeonLidarGeoreferencing;
  lifecycle: "local-preview-only"; source_admitted: false; released: false;
};
const record = (value: unknown): value is Record<string, unknown> => !!value && typeof value === "object" && !Array.isArray(value);
const finite = (value: unknown): value is number => typeof value === "number" && Number.isFinite(value);
const text = (value: unknown, max: number): value is string => typeof value === "string" && value.trim().length > 0 && value.length <= max && !/[\u0000-\u0008\u000b\u000c\u000e-\u001f\u007f]/.test(value);
function utcDate(value: unknown): value is string {
  if (typeof value !== "string" || !/^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{1,6})?Z$/.test(value)) return false;
  const time = Date.parse(value);
  return Number.isFinite(time) && new Date(time).toISOString().slice(0, 19) === value.slice(0, 19);
}

export function parseNeonLidarPreview(value: unknown): NeonLidarPreview | null {
  if (!record(value) || value.schema_version !== NEON_LIDAR_SCHEMA || !utcDate(value.generated_at)
    || (value.data_kind !== "provider-files" && value.data_kind !== "synthetic-test")
    || value.lifecycle !== "local-preview-only" || value.source_admitted !== false || value.released !== false) return null;
  const s = value.source, g = value.grid;
  if (!record(s) || !record(g) || !["KONZ", "KONA", "UKFS"].includes(String(s.site))
    || typeof s.month !== "string" || !/^\d{4}-(?:0[1-9]|1[0-2])$/.test(s.month) || s.month.startsWith("0000")
    || typeof s.release !== "string" || !/^RELEASE-\d{4}$/.test(s.release) || s.release === "RELEASE-0000"
    || typeof s.tile !== "string" || !text(s.attribution, 500)
    || !text(s.horizontal_crs, 12000) || !/^\s*(?:PROJCS|PROJCRS)\s*\[/.test(s.horizontal_crs)
    || !text(s.vertical_reference, 500) || !text(s.vertical_reference_basis, 500) || !text(s.canopy_floor_basis, 500)
    || (s.canopy_floor_m !== null && s.canopy_floor_m !== 0.7 && s.canopy_floor_m !== 2)) return null;
  const tile = /^NEON_D06_(KONZ|KONA|UKFS)_DP3_(\d{6})_(\d{7})$/.exec(s.tile);
  if (!tile || tile[1] !== s.site) return null;
  if (!text(s.acquisition_run, 100)) return null;
  const run = /^(\d{4})_(KONZ|KONA|UKFS)_([1-9]\d*)$/.exec(s.acquisition_run);
  if (!run || run[1] !== s.month.slice(0, 4) || run[2] !== s.site) return null;
  const west = Number(tile[2]), south = Number(tile[3]);
  if (west < 100000 || west > 900000 || west % 1000 !== 0 || south % 1000 !== 0) return null;
  if (!Array.isArray(s.files) || s.files.length !== 3) return null;
  const kinds = new Set<string>();
  for (const file of s.files) {
    if (!record(file) || typeof file.kind !== "string" || !["dtm", "dsm", "chm"].includes(file.kind) || kinds.has(file.kind)
      || file.name !== `${s.tile}_${file.kind.toUpperCase()}.tif`
      || file.product !== (file.kind === "chm" ? "DP3.30015.001" : "DP3.30024.001")
      || typeof file.sha256 !== "string" || !/^[a-f0-9]{64}$/.test(file.sha256)
      || !Number.isSafeInteger(file.bytes) || (file.bytes as number) <= 0) return null;
    kinds.add(file.kind);
  }
  if (!Number.isInteger(g.width) || (g.width as number) < 8 || (g.width as number) > 128 || g.height !== g.width
    || g.source_resolution_m !== 1 || g.sampling !== "nearest-neighbor"
    || !finite(g.preview_resolution_m) || Math.abs(g.preview_resolution_m - 1000 / (g.width as number)) > 1e-9
    || !Array.isArray(g.bounds) || g.bounds.length !== 4 || !g.bounds.every(finite)
    || g.bounds[0] !== west || g.bounds[1] !== south || g.bounds[2] !== west + 1000 || g.bounds[3] !== south + 1000) return null;
  const cells = (g.width as number) ** 2;
  for (const kind of ["dtm", "dsm", "chm"] as const) {
    const samples = g[kind];
    if (!Array.isArray(samples) || samples.length !== cells) return null;
    for (const sample of samples) if (sample !== null && (!finite(sample) || (kind === "chm" && sample < 0))) return null;
  }
  // Older local lab previews remain readable, but cannot be placed on a map.
  if (value.georeferencing !== undefined) {
    const geo = value.georeferencing, width = (g.width as number) + 1;
    if (!record(geo) || geo.method !== "rasterio-warp-transform" || geo.target_crs !== "EPSG:4326"
      || geo.source_crs !== s.horizontal_crs || geo.coordinate_epoch !== null
      || geo.height_values_transformed !== false || geo.horizontal_accuracy_m !== null
      || geo.corner_width !== width || !Array.isArray(geo.corners) || geo.corners.length !== width ** 2) return null;
    for (let index = 0; index < geo.corners.length; index++) {
      const point = geo.corners[index];
      if (!Array.isArray(point) || point.length !== 2 || !point.every(finite)
        || point[0] < -103 || point[0] > -94 || point[1] < 36 || point[1] > 41) return null;
      // A north-up metric UTM grid must preserve local west/east and north/south
      // ordering in this bounded region. Reject folded or reversed cell grids.
      if (index % width && point[0] <= (geo.corners[index - 1] as number[])[0]) return null;
      if (index >= width && point[1] >= (geo.corners[index - width] as number[])[1]) return null;
    }
  }
  // Also enforce the budget for direct callers, including unrecognized extra fields.
  try { if (new TextEncoder().encode(JSON.stringify(value)).byteLength > NEON_LIDAR_MAX_BYTES) return null; }
  catch { return null; }
  return value as NeonLidarPreview;
}

export async function readNeonLidarLocalJson(file: Pick<File, "size" | "text">, signal: AbortSignal): Promise<unknown> {
  signal.throwIfAborted();
  if (!Number.isSafeInteger(file.size) || file.size < 1 || file.size > NEON_LIDAR_MAX_BYTES) throw new Error("Choose a nonempty preview JSON no larger than 2 MiB.");
  const raw = await file.text();
  signal.throwIfAborted();
  if (raw.length > NEON_LIDAR_MAX_BYTES || new TextEncoder().encode(raw).byteLength > NEON_LIDAR_MAX_BYTES) throw new Error("The preview exceeds the 2 MiB local limit.");
  return JSON.parse(raw);
}

export function neonElevationDomain(preview: NeonLidarPreview): [number, number] | null {
  let min = Infinity, max = -Infinity;
  for (const samples of [preview.grid.dtm, preview.grid.dsm]) for (const value of samples) {
    if (value !== null) { min = Math.min(min, value); max = Math.max(max, value); }
  }
  return min === Infinity ? null : [min, max];
}

export function neonLidarProbe(preview: NeonLidarPreview, row: number, column: number) {
  const { grid } = preview;
  if (!Number.isInteger(row) || !Number.isInteger(column) || row < 0 || column < 0 || row >= grid.height || column >= grid.width) return null;
  const index = row * grid.width + column, dtm = grid.dtm[index], dsm = grid.dsm[index];
  const difference = dtm === null || dsm === null ? null : dsm - dtm;
  return {
    row, column, dtm, dsm, chm: grid.chm[index],
    // Nearest source pixel to the preview cell center; row zero is north.
    easting: grid.bounds[0] + Math.floor((column + 0.5) * 1000 / grid.width) + 0.5,
    northing: grid.bounds[3] - Math.floor((row + 0.5) * 1000 / grid.height) - 0.5,
    surfaceAboveGround: difference !== null && Number.isFinite(difference) ? difference : null,
    differenceIssue: difference === null ? "missing" : !Number.isFinite(difference) ? "nonfinite" : difference < 0 ? "negative" : null,
  };
}

export function neonSampleColor(value: number, domain: [number, number]): string {
  const [min, max] = domain, span = max - min;
  const fraction = min === max ? 0.5 : Number.isFinite(span) ? (value - min) / span : (value / 2 - min / 2) / (max / 2 - min / 2);
  const t = Math.max(0, Math.min(1, fraction));
  const stops = [[27, 59, 68], [79, 132, 115], [205, 205, 122], [248, 235, 195]];
  const part = Math.min(2, Math.floor(t * 3)), mix = t * 3 - part;
  return `rgb(${stops[part].map((component, channel) => Math.round(component + (stops[part + 1][channel] - component) * mix)).join(", ")})`;
}
