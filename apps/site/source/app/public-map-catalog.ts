/** Provider discovery metadata, distinct from verified LocalMapSheet file identities. */
export type PublicMapAsset = {
  id: string; title: string; format: string; url: string; expectedBytes: number | null;
  kind: "download" | "service" | "request";
  availability: "verified" | "unverified" | "request-only"; checkedAt: string | null;
};
export type PublicMapRecord = {
  id: string; sourceId: string; publisher: string; title: string; counties: string[];
  mapYear: number | null; digitalYear: number | null; scale: string | null; scaleUnit: string | null;
  crs?: string | null; spatialAccuracy?: string | null;
  metadataUrl: string; rights: { status: string; text: string; url: string | null };
  description: string; geometryRole: string; bbox: [number, number, number, number] | null;
  point: [number, number] | null; assets: PublicMapAsset[];
};
export type PublicMapCoverage = {
  sourceId: string; title: string; state: "seed" | "partial" | "complete" | "unavailable";
  recordCount: number; expectedCount: number | null; discoveredCount?: number; seedReferenceCount?: number; reason: string; checkedAt: string | null;
};
export type PublicMapCatalog = {
  schema: "kfm-public-map-catalog/v1"; generatedAt: string;
  records: PublicMapRecord[]; coverage: PublicMapCoverage[]; sourceUrls?: string[];
};
export type PublicMapFilter = { text: string; publisher: string; county: string; year: string; format: string };
export const PUBLIC_MAP_PAGE_SIZE = 20;
export const PUBLIC_MAP_MAX_BYTES = 32 * 1024 * 1024;
export const PUBLIC_MAP_DOWNLOAD_LIMIT = 500_000_000_000;
const object = (value: unknown): value is Record<string, unknown> => !!value && typeof value === "object" && !Array.isArray(value);
export const publicMapText = (value: unknown, max = 2000): value is string => typeof value === "string" && value.length <= max && !/[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]/.test(value);
export const publicMapCount = (value: unknown): value is number => Number.isSafeInteger(value) && Number(value) >= 0;
export const publicMapStamp = (value: unknown): value is string => publicMapText(value, 40) && /^\d{4}-\d{2}-\d{2}(?:T|$)/.test(value) && Number.isFinite(Date.parse(value));
const year = (value: unknown) => value === null || Number.isInteger(value) && Number(value) >= 1500 && Number(value) <= 2200;
const nonempty = (value: unknown, max = 2000): value is string => publicMapText(value, max) && value.trim().length > 0;
export function publicMapHttps(value: unknown): value is string {
  if (!nonempty(value, 6000) || /[\s\\]/.test(value)) return false;
  try { const url = new URL(value); return url.protocol === "https:" && !url.username && !url.password && !url.port && !["localhost", "127.0.0.1", "[::1]"].includes(url.hostname); }
  catch { return false; }
}
const position = (value: unknown): value is [number, number] => Array.isArray(value) && value.length === 2 && value.every(n => typeof n === "number" && Number.isFinite(n)) && Math.abs(value[0]) <= 180 && Math.abs(value[1]) <= 90;
export function parsePublicMapCatalog(value: unknown): PublicMapCatalog | null {
  if (!object(value) || value.schema !== "kfm-public-map-catalog/v1" || !publicMapStamp(value.generatedAt)
    || !Array.isArray(value.records) || value.records.length > 50_000 || !Array.isArray(value.coverage) || value.coverage.length > 32
    || value.sourceUrls !== undefined && (!Array.isArray(value.sourceUrls) || value.sourceUrls.length > 32 || !value.sourceUrls.every(publicMapHttps))) return null;
  const records = new Set<string>(), assets = new Set<string>(), sources = new Set<string>();
  for (const row of value.coverage) {
    if (!object(row) || !nonempty(row.sourceId, 160) || sources.has(row.sourceId) || !nonempty(row.title, 500)
      || !["seed", "partial", "complete", "unavailable"].includes(String(row.state)) || !publicMapCount(row.recordCount)
      || row.seedReferenceCount !== undefined && !publicMapCount(row.seedReferenceCount)
      || row.discoveredCount !== undefined && (!publicMapCount(row.discoveredCount) || row.discoveredCount + Number(row.seedReferenceCount ?? 0) !== row.recordCount)
      || !(row.expectedCount === null || publicMapCount(row.expectedCount)) || !publicMapText(row.reason, 6000) || !(row.checkedAt === null || publicMapStamp(row.checkedAt))
      || row.state === "complete" && row.expectedCount !== null && (row.discoveredCount ?? row.recordCount) !== row.expectedCount) return null;
    sources.add(row.sourceId);
  }
  const counts = new Map<string, number>();
  for (const row of value.records) {
    if (!object(row) || !nonempty(row.id, 300) || records.has(row.id) || !nonempty(row.sourceId, 160) || !sources.has(row.sourceId)
      || !nonempty(row.publisher, 500) || !nonempty(row.title, 2000) || !Array.isArray(row.counties) || row.counties.length > 105 || !row.counties.every(v => nonempty(v, 100))
      || !year(row.mapYear) || !year(row.digitalYear) || !(row.scale === null || nonempty(row.scale, 200))
      || !(row.crs === undefined || row.crs === null || nonempty(row.crs, 1000)) || !(row.spatialAccuracy === undefined || row.spatialAccuracy === null || nonempty(row.spatialAccuracy, 4000))
      || !(row.scaleUnit === null || publicMapText(row.scaleUnit, 100)) || !publicMapHttps(row.metadataUrl)
      || !object(row.rights) || !nonempty(row.rights.status, 100) || !publicMapText(row.rights.text, 12_000) || !(row.rights.url === null || publicMapHttps(row.rights.url))
      || !publicMapText(row.description, 20_000) || !publicMapText(row.geometryRole, 500)
      || !(row.point === null || position(row.point)) || !Array.isArray(row.assets) || row.assets.length > 100) return null;
    if (row.bbox !== null && (!Array.isArray(row.bbox) || row.bbox.length !== 4 || !position(row.bbox.slice(0, 2)) || !position(row.bbox.slice(2)) || row.bbox[0] >= row.bbox[2] || row.bbox[1] >= row.bbox[3])) return null;
    records.add(row.id); counts.set(row.sourceId, (counts.get(row.sourceId) ?? 0) + 1);
    for (const asset of row.assets) {
      if (!object(asset) || !nonempty(asset.id, 500) || assets.has(asset.id) || !nonempty(asset.title, 2000) || !nonempty(asset.format, 100)
        || !publicMapHttps(asset.url) || !(asset.expectedBytes === null || publicMapCount(asset.expectedBytes) && asset.expectedBytes > 0)
        || !["download", "service", "request"].includes(String(asset.kind)) || !["verified", "unverified", "request-only"].includes(String(asset.availability)) || !(asset.checkedAt === null || publicMapStamp(asset.checkedAt))) return null;
      assets.add(asset.id);
    }
  }
  if (value.coverage.some(row => row.recordCount !== (counts.get(row.sourceId) ?? 0))) return null;
  return value as unknown as PublicMapCatalog;
}
/** Verified public files only. Metadata, shops, services and archive requests are not downloads. */
export const canDownloadPublicMap = (asset: PublicMapAsset) => asset.kind === "download" && asset.availability === "verified";
export function filterPublicMaps(records: readonly PublicMapRecord[], filter: PublicMapFilter) {
  const words = filter.text.trim().toLocaleLowerCase("en-US").split(/\s+/).filter(Boolean);
  return records.filter(row => row.assets.some(canDownloadPublicMap)
    && !["paid", "purchase-required", "request-only"].includes(row.rights.status)
    && (filter.publisher === "all" || row.publisher === filter.publisher)
    && (filter.county === "all" || (filter.county === "unknown" ? row.counties.length === 0 : row.counties.includes(filter.county)))
    && (filter.year === "all" || (filter.year === "unknown" ? row.mapYear === null : row.mapYear === Number(filter.year)))
    && words.every(word => `${row.title} ${row.id} ${row.publisher} ${row.counties.join(" ")} ${row.description}`.toLocaleLowerCase("en-US").includes(word))
    && (filter.format === "all" || row.assets.some(asset => canDownloadPublicMap(asset) && asset.format === filter.format)));
}
/** Explicit MiB limit; a known asset size is a lower bound, never automatic permission. */
export function publicMapSelectedLimit(input: string, asset: PublicMapAsset, ceiling = PUBLIC_MAP_DOWNLOAD_LIMIT): number | null {
  if (!/^\d+(?:\.\d{1,3})?$/.test(input)) return null;
  const bytes = Math.floor(Number(input) * 1024 * 1024);
  return Number.isSafeInteger(bytes) && bytes > 0 && bytes <= ceiling && (asset.expectedBytes === null || bytes >= asset.expectedBytes) ? bytes : null;
}
