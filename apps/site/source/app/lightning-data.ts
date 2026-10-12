/** Fixed provider contracts for display-only lightning density and climatology. */
export const NOAA_LIGHTNING_LAYER = "ldn_lightning_strike_density";
export const NOAA_LIGHTNING_STYLE = "lightning_density";
export const NOAA_LIGHTNING_CAPABILITIES_URL = "https://nowcoast.noaa.gov/geoserver/observations/lightning_detection/ows?service=WMS&version=1.3.0&request=GetCapabilities";
export const NOAA_LIGHTNING_LEGEND_URL = "https://nowcoast.noaa.gov/geoserver/observations/lightning_detection/ows?service=WMS&version=1.3.0&request=GetLegendGraphic&format=image%2Fpng&width=292&height=46&layer=ldn_lightning_strike_density";
export const NOAA_LIGHTNING_WMS_URL = "https://nowcoast.noaa.gov/geoserver/observations/lightning_detection/ows";
export const NASA_LIGHTNING_METADATA_URL = "https://gibs.earthdata.nasa.gov/layer-metadata/v1.0/LIS_High_Resolution_Full_Climatology_Combined_Flash_Rate_Climatology.json";
export const NASA_LIGHTNING_TILES = "https://gibs.earthdata.nasa.gov/wmts/epsg3857/best/LIS_High_Resolution_Full_Climatology_Combined_Flash_Rate_Climatology/default/1995-05-04/GoogleMapsCompatible_Level6/{z}/{y}/{x}.png";
export const LIGHTNING_MAX_FRAMES = 32;

export type LightningManifest = Readonly<{
  layer: typeof NOAA_LIGHTNING_LAYER;
  frames: readonly string[];
  latest: string;
  retrievedAt: string;
  intervalMinutes: 15;
  evidenceRole: "EXTERNAL_CONTEXT_ONLY";
}>;

export const canonicalLightningTime = (value: string): string | null => {
  if (!/^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{3})?Z$/.test(value)) return null;
  const milliseconds = Date.parse(value);
  if (!Number.isFinite(milliseconds)) return null;
  const canonical = new Date(milliseconds).toISOString();
  return canonical.slice(0, 19) === value.slice(0, 19) ? canonical : null;
};

export function parseLightningCapabilities(xml: string, retrievedAt = new Date().toISOString()): LightningManifest {
  const marker = `<Name>${NOAA_LIGHTNING_LAYER}</Name>`;
  const start = xml.indexOf(marker);
  const end = xml.indexOf("</Layer>", start);
  if (start < 0 || end < 0) throw new Error("The fixed NOAA lightning density layer is missing.");
  const layerXml = xml.slice(start, end);
  const dimension = layerXml.match(/<Dimension\b([^>]*)\bname=["']time["']([^>]*)>([\s\S]*?)<\/Dimension>/i);
  if (!dimension) throw new Error("NOAA lightning has no explicit time dimension.");
  const raw = dimension[3].split(",").map((entry) => entry.trim()).filter(Boolean);
  if (!raw.length || raw.length > 4096 || raw.some((entry) => entry.includes("/"))) throw new Error("NOAA lightning time list is unsupported.");
  const parsed = raw.map(canonicalLightningTime);
  if (parsed.some((entry) => !entry)) throw new Error("NOAA lightning advertised an invalid UTC time.");
  if (parsed.some((entry) => {
    const date = new Date(entry!);
    return date.getUTCMinutes() % 15 !== 0 || date.getUTCSeconds() !== 0 || date.getUTCMilliseconds() !== 0;
  })) throw new Error("NOAA lightning frames no longer follow the declared 15-minute clock.");
  const frames = [...new Set(parsed as string[])].sort().slice(-LIGHTNING_MAX_FRAMES);
  const latest = frames.at(-1);
  if (!latest || !Number.isFinite(Date.parse(retrievedAt))) throw new Error("NOAA lightning times are unavailable.");
  return { layer: NOAA_LIGHTNING_LAYER, frames, latest, retrievedAt, intervalMinutes: 15, evidenceRole: "EXTERNAL_CONTEXT_ONLY" };
}

export function lightningTileCoordinates(z: number, x: number, y: number): { z: number; x: number; y: number; bbox: string } {
  if (![z, x, y].every(Number.isSafeInteger) || z < 0 || z > 13 || x < 0 || y < 0 || x >= 2 ** z || y >= 2 ** z) throw new Error("Invalid lightning tile coordinates.");
  const extent = 20037508.342789244;
  const tileWidth = 2 * extent / 2 ** z;
  const west = -extent + x * tileWidth;
  const east = west + tileWidth;
  const north = extent - y * tileWidth;
  const south = north - tileWidth;
  return { z, x, y, bbox: [west, south, east, north].join(",") };
}

export function lightningWmsUrl(frame: string, z: number, x: number, y: number): string {
  const canonical = canonicalLightningTime(frame);
  if (!canonical || canonical !== frame) throw new Error("Lightning tiles require an advertised UTC frame.");
  const { bbox } = lightningTileCoordinates(z, x, y);
  const params = new URLSearchParams({ SERVICE: "WMS", VERSION: "1.1.1", REQUEST: "GetMap", LAYERS: NOAA_LIGHTNING_LAYER, STYLES: NOAA_LIGHTNING_STYLE, FORMAT: "image/png", TRANSPARENT: "TRUE", SRS: "EPSG:3857", BBOX: bbox, WIDTH: "256", HEIGHT: "256", TIME: frame });
  return `${NOAA_LIGHTNING_WMS_URL}?${params}`;
}

export function lightningTilePath(frame: string): string {
  const canonical = canonicalLightningTime(frame);
  if (!canonical || canonical !== frame) throw new Error("Invalid lightning frame.");
  return `/api/lightning/tiles/${encodeURIComponent(frame)}/{z}/{x}/{y}`;
}
