/** Reviewed display carrier for one official Kansas USGS historical scan. */
export type TopoOverlayManifest = Readonly<{
  version: 1;
  packageId: string;
  sheet: { id: number; scanId: number; name: string; year: number; scale: number; state: "KS" };
  geotiff: { url: string; sha256: string; bytes: number; crs: string; transform: number[]; width: number; height: number };
  bounds: [number, number, number, number];
  minZoom: number;
  maxZoom: number;
  sourceRetrievedAt: string;
  tiles: Record<string, { sha256: string; bytes: number }>;
  evidenceRole: "EXTERNAL_CONTEXT_ONLY";
}>;

const digest = (value: unknown): value is string => typeof value === "string" && /^[0-9a-f]{64}$/.test(value);
const integer = (value: unknown, min: number, max: number): value is number => Number.isInteger(value) && (value as number) >= min && (value as number) <= max;
const coordinate = (value: unknown, min: number, max: number): value is number => typeof value === "number" && Number.isFinite(value) && value >= min && value <= max;
export const topoOverlayPrefix = "historical-topo/v1";
export const topoRequestKey = (scanId: number) => `${topoOverlayPrefix}/requests/${scanId}.json`;
export const topoCandidateKey = (scanId: number) => `${topoOverlayPrefix}/candidates/${scanId}.json`;
export const topoActiveKey = (scanId: number) => `${topoOverlayPrefix}/active/${scanId}.json`;
export const topoManifestKey = (scanId: number, packageId: string) => `${topoOverlayPrefix}/packages/${scanId}/${packageId}/manifest.json`;
export const topoTileKey = (scanId: number, packageId: string, address: string) => `${topoOverlayPrefix}/packages/${scanId}/${packageId}/tiles/${address}.png`;

export function parseTopoOverlayManifest(value: unknown): TopoOverlayManifest | null {
  if (!value || typeof value !== "object") return null;
  const m = value as Partial<TopoOverlayManifest>;
  const s = m.sheet, g = m.geotiff, b = m.bounds;
  if (m.version !== 1 || m.evidenceRole !== "EXTERNAL_CONTEXT_ONLY" || !s || !g || !b || !m.tiles
    || !integer(s.id, 1, 1e10) || !integer(s.scanId, 1, 1e10) || s.state !== "KS"
    || typeof s.name !== "string" || !/^[\p{L}\p{N} .'-]{1,120}$/u.test(s.name)
    || !integer(s.year, 1800, 2100) || !integer(s.scale, 1, 1e7)
    || !digest(g.sha256) || m.packageId !== g.sha256.slice(0, 24)
    || !integer(g.bytes, 1024, 500_000_000) || !integer(g.width, 1, 30000) || !integer(g.height, 1, 30000)
    || typeof g.crs !== "string" || g.crs.length < 3 || g.crs.length > 1000
    || !Array.isArray(g.transform) || g.transform.length !== 6 || g.transform.some((n) => typeof n !== "number" || !Number.isFinite(n))
    || !Array.isArray(b) || b.length !== 4 || !coordinate(b[0], -125, -66) || !coordinate(b[1], 24, 50)
    || !coordinate(b[2], -125, -66) || !coordinate(b[3], 24, 50) || b[0] >= b[2] || b[1] >= b[3]
    || b[2] < -102.1 || b[0] > -94.5 || b[3] < 37 || b[1] > 40.1
    || !integer(m.minZoom, 0, 16) || !integer(m.maxZoom, m.minZoom, 16)
    || typeof m.sourceRetrievedAt !== "string" || !Number.isFinite(Date.parse(m.sourceRetrievedAt))) return null;
  let url: URL;
  try { url = new URL(g.url ?? ""); } catch { return null; }
  if (url.protocol !== "https:" || url.hostname !== "prd-tnm.s3.amazonaws.com"
    || !url.pathname.startsWith("/StagedProducts/Maps/HistoricalTopo/GeoTIFF/KS/KS_")
    || !url.pathname.endsWith(`_${s.scanId}_${s.year}_${s.scale}_geo.tif`)
    || url.search || url.hash) return null;
  const entries = Object.entries(m.tiles);
  if (!entries.length || entries.length > 5000) return null;
  let totalBytes = 0;
  for (const [address, tile] of entries) {
    const parts = /^(\d{1,2})\/(\d{1,8})\/(\d{1,8})$/.exec(address);
    if (!parts || !tile || !digest(tile.sha256) || !integer(tile.bytes, 24, 2_000_000)) return null;
    const [z, x, y] = parts.slice(1).map(Number);
    if (z < m.minZoom || z > m.maxZoom || x >= 2 ** z || y >= 2 ** z) return null;
    totalBytes += tile.bytes;
  }
  if (totalBytes > 500_000_000) return null;
  return m as TopoOverlayManifest;
}

export type TopoActivePointer = { scanId: number; packageId: string; manifestSha256: string; reviewedAt: string; reviewedBy: string; note: string; previousPackageId: string | null; previousManifestSha256: string | null };
export function parseTopoActivePointer(value: unknown): TopoActivePointer | null {
  if (!value || typeof value !== "object") return null;
  const p = value as Partial<TopoActivePointer>;
  if (!integer(p.scanId, 1, 1e10) || typeof p.packageId !== "string" || !/^[0-9a-f]{24}$/.test(p.packageId)
    || !digest(p.manifestSha256) || typeof p.reviewedAt !== "string" || !Number.isFinite(Date.parse(p.reviewedAt))
    || typeof p.reviewedBy !== "string" || !/^[0-9a-f]{64}$/.test(p.reviewedBy)
    || typeof p.note !== "string" || p.note.length < 10 || p.note.length > 1000
    || !(p.previousPackageId === null && p.previousManifestSha256 === null
      || typeof p.previousPackageId === "string" && /^[0-9a-f]{24}$/.test(p.previousPackageId) && digest(p.previousManifestSha256))) return null;
  return p as TopoActivePointer;
}
