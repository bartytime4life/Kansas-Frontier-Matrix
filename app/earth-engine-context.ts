// Reviewed visual context only. This schema is deliberately separate from KFM evidence and source admission.
export const EARTH_ENGINE_CONTEXT_PREFIX = "earth-engine-context/v1";
export const EARTH_ENGINE_CONTEXT_ACTIVE_KEY = `${EARTH_ENGINE_CONTEXT_PREFIX}/active.json`;
export const EARTH_ENGINE_CONTEXT_LAYERS = [
  { id: "ee-cdl", title: "2024 crop classes", source: "USDA/NASS/CDL", period: "2024 harvest year", attribution: "USDA NASS Cropland Data Layer", legend: "Crop classes; consult the USDA class table" },
  { id: "ee-chirps", title: "2024 rainfall", source: "UCSB-CHG/CHIRPS/DAILY", period: "2024 calendar year", attribution: "UCSB Climate Hazards Center · CHIRPS", legend: "Annual precipitation · mm" },
  { id: "ee-terraclimate", title: "2024 drought index", source: "IDAHO_EPSCOR/TERRACLIMATE", period: "2024 calendar year", attribution: "University of Idaho / UC Merced · TerraClimate", legend: "Annual mean PDSI · unitless" },
  { id: "ee-sentinel2", title: "2024 satellite composite", source: "COPERNICUS/S2_SR_HARMONIZED", period: "2024 calendar year", attribution: "Contains modified Copernicus Sentinel data 2024 · European Union / ESA", legend: "Natural color · quality screened annual median" },
  { id: "ee-3dep", title: "Elevation mosaic", source: "USGS/3DEP/10m_collection", period: "Mixed acquisition dates · source mosaic", attribution: "USGS 3D Elevation Program", legend: "Elevation · meters" },
] as const;

export type EarthEngineContextLayerId = typeof EARTH_ENGINE_CONTEXT_LAYERS[number]["id"];
export type EarthEngineTileIndex = { sha256: string; count: number; minX: number; maxX: number; minY: number; maxY: number };
export type EarthEngineContextLayer = {
  id: EarthEngineContextLayerId;
  status: "approved" | "held";
  source: string;
  period: string;
  resolutionMeters: number;
  attribution: string;
  limits: string;
  legend: string;
  geotiffSha256: string;
  reviewSha256: string;
  tileIndexes: Record<string, EarthEngineTileIndex>;
};
export type EarthEngineContextManifest = {
  schema: "kfm-earth-engine-context/v1";
  setId: string;
  boundary: "Kansas · TIGER/2018/States · STATEFP 20";
  approvedAt: string;
  reviewState: "APPROVED_VISUAL_CONTEXT";
  admission: "NOT_ADMITTED";
  evidence: "NOT_CLAIM_EVIDENCE";
  layers: EarthEngineContextLayer[];
};
export type EarthEngineContextPointer = { schema: "kfm-earth-engine-context-pointer/v1"; setId: string; manifestSha256: string };

const hash = (value: unknown): value is string => typeof value === "string" && /^[0-9a-f]{64}$/.test(value);
const setId = (value: unknown): value is string => typeof value === "string" && /^ks-(?:2024|terrain)-[a-z0-9-]{6,64}$/.test(value);
const plain = (value: unknown): value is Record<string, unknown> => Boolean(value && typeof value === "object" && !Array.isArray(value));
const text = (value: unknown, max = 1000): value is string => typeof value === "string" && value.length > 0 && value.length <= max;
const coord = (value: unknown) => Number.isInteger(value) && Number(value) >= 0 && Number(value) <= 1_073_741_823;

export function parseEarthEnginePointer(value: unknown): EarthEngineContextPointer | null {
  if (!plain(value) || value.schema !== "kfm-earth-engine-context-pointer/v1" || !setId(value.setId) || !hash(value.manifestSha256)) return null;
  return value as EarthEngineContextPointer;
}

export function parseEarthEngineManifest(value: unknown): EarthEngineContextManifest | null {
  if (!plain(value) || value.schema !== "kfm-earth-engine-context/v1" || !setId(value.setId)
    || value.boundary !== "Kansas · TIGER/2018/States · STATEFP 20"
    || value.reviewState !== "APPROVED_VISUAL_CONTEXT" || value.admission !== "NOT_ADMITTED"
    || value.evidence !== "NOT_CLAIM_EVIDENCE" || !text(value.approvedAt, 40)
    || !Array.isArray(value.layers) || value.layers.length < 1 || value.layers.length > 5) return null;
  const seen = new Set<string>();
  for (const layer of value.layers) {
    const descriptor = EARTH_ENGINE_CONTEXT_LAYERS.find((d) => d.id === layer?.id);
    const resolution = layer?.id === "ee-chirps" ? 5566 : layer?.id === "ee-terraclimate" ? 4638 : 30;
    if (!plain(layer) || !descriptor || descriptor.source !== layer.source || descriptor.period !== layer.period
      || descriptor.attribution !== layer.attribution || layer.resolutionMeters !== resolution
      || seen.has(String(layer.id)) || !["approved", "held"].includes(String(layer.status))
      || !text(layer.period, 100) || !Number.isFinite(layer.resolutionMeters) || Number(layer.resolutionMeters) <= 0
      || !text(layer.attribution) || !text(layer.limits, 3000) || !text(layer.legend)
      || !hash(layer.geotiffSha256) || !hash(layer.reviewSha256) || !plain(layer.tileIndexes)) return null;
    seen.add(String(layer.id));
    for (const [zText, entry] of Object.entries(layer.tileIndexes)) {
      const z = Number(zText);
      if (!/^(0|[1-9]\d?)$/.test(zText) || z > 18 || !plain(entry) || !hash(entry.sha256)
        || !Number.isInteger(entry.count) || Number(entry.count) < 1 || Number(entry.count) > 10_000_000
        || !coord(entry.minX) || !coord(entry.maxX) || !coord(entry.minY) || !coord(entry.maxY)
        || Number(entry.minX) > Number(entry.maxX) || Number(entry.minY) > Number(entry.maxY)
        || Number(entry.maxX) >= 2 ** z || Number(entry.maxY) >= 2 ** z) return null;
    }
    if (layer.status === "approved" && Object.keys(layer.tileIndexes).length === 0) return null;
  }
  return value as EarthEngineContextManifest;
}

export function parseEarthEngineTileIndex(value: unknown, expected: EarthEngineTileIndex, z: number): Record<string, string> | null {
  if (!plain(value) || !plain(value.tiles)) return null;
  const entries = Object.entries(value.tiles);
  if (entries.length !== expected.count) return null;
  const tiles: Record<string, string> = Object.create(null);
  for (const [key, digest] of entries) {
    const match = /^(0|[1-9]\d*)\/(0|[1-9]\d*)$/.exec(key);
    if (!match || !hash(digest)) return null;
    const x = Number(match[1]), y = Number(match[2]);
    if (x < expected.minX || x > expected.maxX || y < expected.minY || y > expected.maxY || x >= 2 ** z || y >= 2 ** z) return null;
    tiles[key] = digest;
  }
  return tiles;
}

export const earthEngineManifestKey = (id: string) => `${EARTH_ENGINE_CONTEXT_PREFIX}/sets/${id}/manifest.json`;
export const earthEngineIndexKey = (id: string, layer: string, z: number) => `${EARTH_ENGINE_CONTEXT_PREFIX}/sets/${id}/indexes/${layer}/${z}.json`;
export const earthEngineTileKey = (id: string, layer: string, z: number, x: number, y: number) => `${EARTH_ENGINE_CONTEXT_PREFIX}/sets/${id}/tiles/${layer}/${z}/${x}/${y}.png`;
export const earthEngineTileVisibleAtYear = (layer: EarthEngineContextLayerId, year: number) => layer === "ee-3dep" || year === 2024;
