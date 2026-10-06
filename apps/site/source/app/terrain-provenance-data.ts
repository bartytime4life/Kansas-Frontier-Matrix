/** Public EPT discovery metadata only; never reads point payloads or activates a source. */
export type TerrainExtent = readonly [number, number, number, number];
export type TerrainWorkUnit = Readonly<{
  id: string;
  sourceUrl: string;
  metadataSha256: string;
  metadataBytes: number;
  pointCount: number | null;
  nativeBounds: readonly number[] | null;
  horizontalCrs: string | null;
  verticalCrs: string | null;
  geographicExtent: TerrainExtent | null;
  acquisitionStart: string | null;
  acquisitionEnd: string | null;
  acquisitionReason: string;
}>;

export type TerrainDiscovery = Readonly<{
  capturedAt: string;
  declaredProjectCount: number;
  completeForPrefix: boolean;
  completeForState: boolean;
  metadataBytes: number | null;
  rejectedProjects: number;
  projects: readonly TerrainWorkUnit[];
}>;

// Matches the existing Kansas reference study bounds. This is a study rectangle,
// not the legal state boundary or a surveyed acquisition footprint.
export const TERRAIN_STUDY_BOUNDS: TerrainExtent = [-102.06, 36.99, -94.58, 40.01];
export const TERRAIN_PROVENANCE_LINKS = {
  catalog: "https://registry.opendata.aws/usgs-lidar/",
  program: "https://www.usgs.gov/3d-elevation-program",
} as const;

function record(value: unknown): value is Record<string, unknown> {
  return Boolean(value) && typeof value === "object" && !Array.isArray(value);
}

function count(value: unknown): number | null {
  return typeof value === "number" && Number.isSafeInteger(value) && value >= 0 ? value : null;
}

function reportedCode(value: unknown): string | null {
  const text = typeof value === "number" && Number.isSafeInteger(value) ? String(value) : value;
  return typeof text === "string" && /^[1-9][0-9]{0,7}$/.test(text) ? text : null;
}

function date(value: unknown): string | null {
  if (typeof value !== "string" || !/^\d{4}-\d{2}-\d{2}(?:T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2}))?$/.test(value)) return null;
  const time = Date.parse(value);
  return Number.isFinite(time) && new Date(time).toISOString().slice(0, 10) === value.slice(0, 10) ? value : null;
}

function bounds(value: unknown): readonly number[] | null {
  if (!Array.isArray(value) || value.length !== 6 || !value.every(n => typeof n === "number" && Number.isFinite(n))) return null;
  return value[0] < value[3] && value[1] < value[4] && value[2] <= value[5] ? [...value] : null;
}

/** Derive only rectangular horizontal extents for explicitly reported EPSG CRS. */
export function terrainGeographicExtent(nativeBounds: readonly number[] | null, authority: unknown, horizontal: unknown): TerrainExtent | null {
  if (!nativeBounds || authority !== "EPSG") return null;
  const code = reportedCode(horizontal);
  let extent: number[];
  if (code === "3857") {
    const radius = 6378137;
    const world = Math.PI * radius;
    if ([nativeBounds[0], nativeBounds[1], nativeBounds[3], nativeBounds[4]].some(n => Math.abs(n) > world)) return null;
    const longitude = (x: number) => x / radius * 180 / Math.PI;
    const latitude = (y: number) => Math.atan(Math.sinh(y / radius)) * 180 / Math.PI;
    extent = [longitude(nativeBounds[0]), latitude(nativeBounds[1]), longitude(nativeBounds[3]), latitude(nativeBounds[4])];
  } else if (code === "4326") {
    extent = [nativeBounds[0], nativeBounds[1], nativeBounds[3], nativeBounds[4]];
  } else return null;
  const [west, south, east, north] = extent;
  if (![west, south, east, north].every(Number.isFinite) || west < -180 || east > 180 || south < -90 || north > 90 || west >= east || south >= north) return null;
  return [west, south, east, north];
}

function project(value: unknown): TerrainWorkUnit | null {
  if (!record(value) || typeof value.provider_work_unit !== "string" || !/^KS_[A-Za-z0-9_.-]{1,220}$/.test(value.provider_work_unit)) return null;
  const id = value.provider_work_unit;
  if (typeof value.source_url !== "string") return null;
  let url: URL;
  try { url = new URL(value.source_url); } catch { return null; }
  if (url.protocol !== "https:" || url.hostname !== "usgs-lidar-public.s3.amazonaws.com" || url.port || url.username || url.password || url.search || url.hash || url.pathname !== `/${id}/ept.json`) return null;
  if (typeof value.metadata_sha256 !== "string" || !/^[a-f0-9]{64}$/.test(value.metadata_sha256)) return null;
  const metadataBytes = count(value.metadata_bytes);
  if (metadataBytes === null) return null;
  const nativeBounds = bounds(value.bounds);
  const srs = record(value.srs) ? value.srs : {};
  const authority = typeof srs.authority === "string" && /^[A-Za-z0-9_-]{1,20}$/.test(srs.authority) ? srs.authority : null;
  const horizontal = reportedCode(srs.horizontal), vertical = reportedCode(srs.vertical);
  const start = date(value.temporal_start), end = date(value.temporal_end);
  const validPeriod = start !== null && end !== null && Date.parse(start) <= Date.parse(end);
  return {
    id, sourceUrl: url.href, metadataSha256: value.metadata_sha256, metadataBytes,
    pointCount: count(value.point_count), nativeBounds,
    horizontalCrs: authority && horizontal ? `${authority}:${horizontal}` : null,
    verticalCrs: authority && vertical ? `${authority}:${vertical}` : null,
    geographicExtent: terrainGeographicExtent(nativeBounds, authority, horizontal),
    acquisitionStart: validPeriod ? start : null, acquisitionEnd: validPeriod ? end : null,
    acquisitionReason: typeof value.temporal_reason === "string" && value.temporal_reason.length <= 500 ? value.temporal_reason : "Acquisition dates are not established by this metadata snapshot.",
  };
}

export function parseTerrainDiscovery(value: unknown): TerrainDiscovery | null {
  if (!record(value) || value.schema_version !== "kfm-3dep-discovery-v1" || value.selection !== "KS_ provider prefix" || !Array.isArray(value.projects) || value.projects.length > 1000) return null;
  const capturedAt = date(value.captured_at), declaredProjectCount = count(value.project_count);
  if (!capturedAt || declaredProjectCount === null) return null;
  const seen = new Set<string>();
  const projects = value.projects.flatMap(row => {
    const item = project(row);
    if (!item || seen.has(item.id)) return [];
    seen.add(item.id);
    return [item];
  }).sort((a, b) => a.id.localeCompare(b.id));
  const rejectedProjects = value.projects.length - projects.length;
  return {
    capturedAt, declaredProjectCount, projects, rejectedProjects,
    completeForPrefix: value.complete_for_prefix === true && rejectedProjects === 0 && declaredProjectCount === projects.length,
    // A provider-name prefix cannot establish spatial state completeness.
    completeForState: false,
    metadataBytes: count(value.metadata_bytes_captured),
  };
}

export function filterTerrainWorkUnits(projects: readonly TerrainWorkUnit[], query: string): readonly TerrainWorkUnit[] {
  const needle = query.trim().toLowerCase();
  return needle ? projects.filter(item => item.id.toLowerCase().includes(needle)) : projects;
}

export function terrainDiagramBounds(projects: readonly TerrainWorkUnit[]): TerrainExtent {
  const extents = [TERRAIN_STUDY_BOUNDS, ...projects.flatMap(item => item.geographicExtent ? [item.geographicExtent] : [])];
  const west = Math.min(...extents.map(extent => extent[0])), south = Math.min(...extents.map(extent => extent[1]));
  const east = Math.max(...extents.map(extent => extent[2])), north = Math.max(...extents.map(extent => extent[3]));
  const longitudePad = (east - west) * .06, latitudePad = (north - south) * .1;
  return [west - longitudePad, south - latitudePad, east + longitudePad, north + latitudePad];
}
