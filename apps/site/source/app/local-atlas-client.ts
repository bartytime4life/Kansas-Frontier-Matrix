import { readBoundedJson } from "./bounded-json";
import { INTAKE_DESK_ORIGIN } from "./intake-desk-client";

export type AtlasBounds = [number, number, number, number];
export type AtlasGroup = { id: string; title: string; variable: string; resolution: string; period: string; series: string; units: string; frameCount: number; start: string; end: string };
export type AtlasFrame = { id: string; label: string; key: string; units: string; processedAt: string | null };
export type AtlasItem = { id: string; name: string; family: string; kind: string; domain: string; status: string; bbox_wgs84: AtlasBounds | null; time_start: string | null; time_end: string | null; size_bytes: number; preview: "vector" | "raster" | "unsupported"; reason: string | null };
export type AtlasRaster = { imageDataUrl: string; coordinates: [[number, number], [number, number], [number, number], [number, number]]; width: number; height: number; min: number | null; max: number | null; band: number; nodata: number | null; paletteType?: "continuous" | "categorical"; colorMap?: { value: number; color: string }[]; colors?: string[]; units?: string | null };
export type AtlasPreview = { schema: "kfm-local-atlas-preview/v1"; id: string; kind: "vector" | "raster"; title: string;
  source: { role: string; attribution: string; sourceUrl: string | null; sha256: string | null };
  time: { kind: string; label: string; start: string | null; end: string | null; processedAt: string | null }; units: string | null;
  bounds: AtlasBounds | null; limitations: string[]; displayedCount: number; totalCount: number | null; truncated: boolean;
  authority: { admission: false; evidence: false; release: false }; numericFields: string[]; valueField: string | null;
  data: GeoJSON.FeatureCollection | AtlasRaster };
export type AtlasCoverage = GeoJSON.FeatureCollection & { total: number; offset: number; limit: number; displayedCount: number; scannedCount: number; nextOffset: number | null; note: string };
export type AtlasCatalog = { total: number; offset: number; limit: number; items: AtlasItem[] };
export type AtlasFrames = { group: AtlasGroup; total: number; offset: number; limit: number; frames: AtlasFrame[] };
const object = (v: unknown): v is Record<string, unknown> => Boolean(v && typeof v === "object" && !Array.isArray(v));
const count = (v: unknown): v is number => Number.isSafeInteger(v) && Number(v) >= 0;
const string = (v: unknown): v is string => typeof v === "string" && v.length <= 4000;
const nullableString = (v: unknown) => v === null || string(v);
const finite = (v: unknown): v is number => typeof v === "number" && Number.isFinite(v);
const strings = (v: unknown): v is string[] => Array.isArray(v) && v.length <= 200 && v.every(string);
export const atlasBounds = (v: unknown): v is AtlasBounds => Array.isArray(v) && v.length === 4 && v.every(finite) && v[0] >= -180 && v[2] <= 180 && v[1] >= -90 && v[3] <= 90 && v[0] <= v[2] && v[1] <= v[3];

/** Only finite WGS84 geometry enters the renderer; the response is bounded before parsing. */
export function atlasCollection(value: unknown): value is GeoJSON.FeatureCollection {
  if (!object(value) || value.type !== "FeatureCollection" || !Array.isArray(value.features) || value.features.length > 5000) return false;
  let vertices = 0;
  const coordinates = (v: unknown, depth: number): boolean => {
    if (!Array.isArray(v) || depth > 5) return false;
    if (typeof v[0] === "number") return ++vertices <= 180000 && v.length >= 2 && v.length <= 3 && v.every(finite) && Math.abs(v[0]) <= 180 && Math.abs(v[1]) <= 90;
    return v.every(x => coordinates(x, depth + 1));
  };
  const geometry = (v: unknown, depth = 0): boolean => {
    if (v === null) return true;
    if (!object(v) || depth > 4) return false;
    if (v.type === "GeometryCollection") return Array.isArray(v.geometries) && v.geometries.length <= 5000 && v.geometries.every(g => geometry(g, depth + 1));
    return ["Point", "MultiPoint", "LineString", "MultiLineString", "Polygon", "MultiPolygon"].includes(String(v.type)) && coordinates(v.coordinates, 0);
  };
  const properties = (v: unknown, depth = 0): boolean => {
    if (depth > 12) return false;
    if (typeof v === "number") return finite(v);
    if (Array.isArray(v)) return v.every(p => properties(p, depth + 1));
    if (object(v)) return Object.values(v).every(p => properties(p, depth + 1));
    return v === null || typeof v === "string" || typeof v === "boolean";
  };
  return value.features.every(f => object(f) && f.type === "Feature" && (f.properties === null || object(f.properties) && properties(f.properties)) && geometry(f.geometry));
}
export function parseAtlasPreview(v: unknown): AtlasPreview | null {
  if (!object(v) || v.schema !== "kfm-local-atlas-preview/v1" || !string(v.id) || !string(v.title) || !["vector", "raster"].includes(String(v.kind))
    || !object(v.authority) || [v.authority.admission, v.authority.evidence, v.authority.release].some(x => x !== false)
    || !object(v.source) || !string(v.source.role) || !string(v.source.attribution) || !nullableString(v.source.sourceUrl) || !nullableString(v.source.sha256)
    || !object(v.time) || !string(v.time.kind) || !string(v.time.label) || ![v.time.start, v.time.end, v.time.processedAt].every(nullableString)
    || !nullableString(v.units) || !(v.bounds === null || atlasBounds(v.bounds)) || !strings(v.limitations) || !count(v.displayedCount)
    || !(v.totalCount === null || count(v.totalCount)) || typeof v.truncated !== "boolean" || !strings(v.numericFields) || !nullableString(v.valueField)) return null;
  if (v.kind === "vector") { if (!atlasCollection(v.data) || v.displayedCount !== v.data.features.length) return null; }
  else {
    const d = v.data;
    if (object(d) && ((d.paletteType !== undefined && !["continuous", "categorical"].includes(String(d.paletteType)))
      || (d.colors !== undefined && (!Array.isArray(d.colors) || d.colors.length < 2 || d.colors.length > 12 || !d.colors.every(c => typeof c === "string" && /^#[a-fA-F0-9]{6}$/.test(c))))
      || (d.colorMap !== undefined && (!Array.isArray(d.colorMap) || d.colorMap.length > 256 || !d.colorMap.every(c => object(c) && finite(c.value) && typeof c.color === "string" && /^#[a-fA-F0-9]{6}$/.test(c.color)))))) return null;
    if (!object(d) || typeof d.imageDataUrl !== "string" || d.imageDataUrl.length > 2_800_000 || !/^data:image\/png;base64,[A-Za-z0-9+/]+=*$/.test(d.imageDataUrl)
      || !count(d.width) || !count(d.height) || d.width < 1 || d.height < 1 || d.width > 2048 || d.height > 2048 || !count(d.band) || d.band < 1
      || ![d.min, d.max, d.nodata].every(x => x === null || finite(x)) || !Array.isArray(d.coordinates) || d.coordinates.length !== 4
      || !d.coordinates.every(c => Array.isArray(c) && c.length === 2 && c.every(finite) && Math.abs(c[0]) <= 180 && Math.abs(c[1]) <= 90)) return null;
  }
  return v as AtlasPreview;
}
const groupValid = (v: unknown): v is AtlasGroup => object(v) && [v.id, v.title, v.variable, v.resolution, v.period, v.series, v.units, v.start, v.end].every(string) && count(v.frameCount);
export function parseAtlasGroups(v: unknown): AtlasGroup[] | null {
  return object(v) && v.schema === "kfm-local-atlas-prism-groups/v1" && Array.isArray(v.groups) && v.groups.length <= 1000 && v.groups.every(groupValid) ? v.groups : null;
}
export function parseAtlasFrames(v: unknown): AtlasFrames | null {
  return object(v) && v.schema === "kfm-local-atlas-prism-frames/v1" && groupValid(v.group) && [v.total, v.offset, v.limit].every(count) && Array.isArray(v.frames) && v.frames.length <= 366
    && v.frames.every(f => object(f) && [f.id, f.label, f.key, f.units].every(string) && nullableString(f.processedAt)) ? v as AtlasFrames : null;
}
export function parseAtlasCatalog(v: unknown): AtlasCatalog | null {
  return object(v) && v.schema === "kfm-local-atlas-catalog/v1" && [v.total, v.offset, v.limit].every(count) && Array.isArray(v.items) && v.items.length <= 500
    && v.items.every(i => object(i) && [i.id, i.name, i.family, i.kind, i.domain, i.status].every(string) && count(i.size_bytes)
      && (i.bbox_wgs84 === null || atlasBounds(i.bbox_wgs84)) && [i.time_start, i.time_end, i.reason].every(nullableString)
      && ["vector", "raster", "unsupported"].includes(String(i.preview))) ? v as AtlasCatalog : null;
}
export function parseAtlasCoverage(v: unknown): AtlasCoverage | null {
  return atlasCollection(v) && object(v) && [v.total, v.offset, v.limit, v.displayedCount, v.scannedCount].every(count)
    && (v.nextOffset === null || count(v.nextOffset)) && string(v.note) && v.displayedCount === v.features.length ? v as unknown as AtlasCoverage : null;
}

export async function atlasRequest<T>(path: string, signal: AbortSignal, parse: (v: unknown) => T | null, body?: unknown, token?: string): Promise<T> {
  const combined = AbortSignal.any([signal, AbortSignal.timeout(body ? 30_000 : 15_000)]);
  const response = await fetch(`${INTAKE_DESK_ORIGIN}${path}`, { signal: combined, credentials: "omit", cache: "no-store", redirect: "error",
    ...(body ? { method: "POST", headers: { "Content-Type": "application/json", "X-KFM-Session": token ?? "" }, body: JSON.stringify(body) } : {}) });
  const value = await readBoundedJson(response, 12 * 1024 * 1024, combined);
  combined.throwIfAborted();
  if (!response.ok) throw new Error(object(value) && string(value.error) ? value.error : "The local companion could not prepare this view.");
  const result = parse(value);
  if (result === null) throw new Error("The local companion returned an unsupported response. Update the Intake Desk and reconnect.");
  return result;
}
export const atlasSession = (v: unknown) => object(v) && typeof v.sessionToken === "string" && /^[A-Za-z0-9_-]{16,256}$/.test(v.sessionToken) ? v.sessionToken : null;
/** Each selection owns its response. Clear/unmount invalidates requests even if transport ignores cancellation. */
export class AtlasRequestGate {
  private current = 0;
  private controller: AbortController | null = null;
  clear() { this.current++; this.controller?.abort(); this.controller = null; }
  begin() { this.clear(); const id = this.current; this.controller = new AbortController(); return { signal: this.controller.signal, current: () => id === this.current && !this.controller?.signal.aborted }; }
}

/** Translate expected local preparation failures into a useful next action. */
export function atlasErrorMessage(error: unknown): string {
  const message = error instanceof Error ? error.message : "";
  const code = message.match(/^ATLAS_[A-Z0-9_]+/)?.[0];
  if (error instanceof Error && error.name === "TimeoutError" || code === "ATLAS_PREVIEW_TIMEOUT") return "The local preview took too long. Try a smaller file or another period.";
  const messages: Record<string, string> = {
    ATLAS_CSV_COORDINATES_REQUIRED: "This table needs latitude and longitude columns before it can be mapped. Review its fields in Intake Desk or choose a spatial file.",
    ATLAS_SPATIAL_RUNTIME_UNAVAILABLE: "The local spatial reader is unavailable. Start or update the Intake Desk with its spatial tools, then reconnect.",
    ATLAS_SPATIAL_READER_FAILED: "The local reader could not prepare this file. Review the source in Intake Desk or choose a prepared spatial copy.",
    ATLAS_GEOJSON_CRS_UNSUPPORTED: "This geometry uses an unsupported coordinate system. Prepare a WGS84 longitude/latitude copy before previewing it.",
    ATLAS_COORDINATES_NOT_WGS84: "These coordinates are not valid WGS84 longitude and latitude. Review the coordinate system in Intake Desk.",
    ATLAS_FORMAT_NEEDS_SPATIAL_DERIVATIVE: "This format needs a prepared spatial copy. Use the historical-map tools for PDF sheets, or review preparation options in Intake Desk.",
    ATLAS_ARCHIVE_SELECT_SINGLE_RASTER: "This archive needs exactly one supported GeoTIFF. Prepare a single-raster file or archive for the layer you want to map.",
    ATLAS_ARCHIVE_SELECT_SINGLE_VECTOR: "This archive needs exactly one supported shapefile with its companion files. Prepare a single-layer archive for the layer you want to map.",
    ATLAS_SOURCE_CHANGED: "This source changed after it was indexed. Run analysis in Intake Desk, then reconnect and select it again.",
    ATLAS_SOURCE_CHANGED_REANALYZE: "This source changed after it was indexed. Run analysis in Intake Desk, then reconnect and select it again.",
    ATLAS_FRAME_CHANGED_REFRESH: "This climate frame changed during preparation. Reconnect to refresh the catalog, then select the period again.",
    ATLAS_BAND_INVALID: "That raster band is unavailable. Choose a valid band number, starting with band 1.",
    ATLAS_RASTER_CRS_OR_BAND_INVALID: "The raster band or coordinate system is unavailable. Try band 1, or review the raster metadata in Intake Desk.",
    ATLAS_PREVIEW_BUSY: "The Intake Desk is preparing another preview. Wait for it to finish, then try again.",
    ATLAS_RASTER_OUTSIDE_KANSAS: "This raster does not overlap the Kansas preview area. Choose a Kansas source to display here.",
    ATLAS_RESPONSE_LIMIT: "This file exceeds the bounded preview size. Choose a smaller spatial subset or a prepared overview.",
    ATLAS_VERTEX_LIMIT: "This geometry is too detailed for a bounded preview. Prepare a simplified or smaller spatial subset.",
    ATLAS_NO_DISPLAYABLE_FEATURES: "No map-ready features were found. Review the geometry or coordinate columns in Intake Desk.",
    ATLAS_PRISM_NOT_AVAILABLE: "Processed PRISM climate data is not available on this PC yet. Check local curation in Intake Desk, or explore Local files.",
    ATLAS_DIFFERENCE_INCOMPATIBLE: "These periods cannot be compared. Choose both from the same climate collection, with matching variable, units, resolution, and cadence.",
    ATLAS_DIFFERENCE_REQUIRES_PRISM: "Period differences are available for PRISM county means. Choose a climate collection and two compatible periods.",
    ATLAS_ITEM_HELD: "This file is held for intake review. Open Intake Desk to inspect its status before preparing a map view.",
    ATLAS_FRAME_NOT_FOUND: "This climate period is no longer in the current catalog. Reconnect and select an available frame.",
    ATLAS_GROUP_NOT_FOUND: "This climate collection is no longer in the current catalog. Reconnect and choose an available collection.",
    ATLAS_YEAR_INVALID: "Enter a four-digit year, or clear the year filter to browse all available periods.",
    ATLAS_GEOJSON_INVALID: "This file does not contain valid GeoJSON. Review or repair it in Intake Desk before mapping it.",
    ATLAS_GEOMETRY_INVALID: "This geometry could not be drawn safely. Review or repair the source coordinates before mapping it.",
    ATLAS_GEOMETRY_UNSUPPORTED: "This geometry type is not supported by the local preview. Prepare a point, line, or polygon copy.",
    ATLAS_COUNTY_GEOMETRY_INVALID: "The local county reference could not be read. Check the prepared county geometry in Intake Desk before mapping climate data.",
    ATLAS_PRISM_CATALOG_LIMIT: "The climate catalog exceeds the local reader limit. Check the PRISM curation status in Intake Desk.",
    ATLAS_ARCHIVE_UNSAFE: "This archive cannot be opened by the local preview. Review its contents and prepare a supported spatial file in Intake Desk.",
    ATLAS_SHAPEFILE_MEMBER_MISSING_OR_LIMIT: "This shapefile is incomplete or exceeds the preview limit. Keep its required companion files together, or prepare a smaller spatial subset.",
  };
  if (code && messages[code]) return messages[code];
  if (code && /(?:MEMBER_LIMIT|RASTER_LIMIT|IMAGE_LIMIT|ROW_LIMIT|FIELD_LIMIT)$/.test(code)) return "This source exceeds the local preview limits. Prepare a smaller single-layer subset or an overview in Intake Desk.";
  if (code) return "The local preview could not be prepared. Review the source in Intake Desk, then reconnect or choose another file.";
  if (error instanceof TypeError || /fetch|network|connection/i.test(message)) return "The local Intake Desk could not be reached. Start it on this PC, then reconnect.";
  if (message === "The local companion returned an unsupported response. Update the Intake Desk and reconnect.") return message;
  return "The local preview is unavailable. Reconnect to Intake Desk and try another file or period.";
}
