/** Browser-local inspection only. No network, persistence, evidence or release. */
import { readBoundedJson } from "./bounded-json";

export const SEISMIC_PREVIEW_MAX_BYTES = 8 * 1024 * 1024;
export const SEISMIC_PREVIEW_MAX_EVENTS = 10000;
export const KANSAS_SEISMIC_PREVIEW_BOUNDS = Object.freeze([-102.1, 36.9, -94.5, 40.1] as const);
export type SeismicPreviewScope = Readonly<{ startMs: number; endMs: number }>;
export type SeismicPreviewEvent = Readonly<{
  id: string; originMs: number; updatedMs: number | null;
  longitude: number; latitude: number; depthKm: number | null;
  magnitude: number | null; magnitudeType: string | null; reviewStatus: string | null;
}>;
export type SeismicPreview = Readonly<{
  scope: SeismicPreviewScope; events: readonly SeismicPreviewEvent[];
  suppliedCount: number; excludedCount: number; generatedMs: number | null;
  inspectedAt: string; sha256: string;
  origin: "UNVERIFIED_LOCAL_FILE"; admission: "NOT_ADMITTED";
}>;

type RecordValue = Record<string, unknown>;
const record = (value: unknown): value is RecordValue => !!value && typeof value === "object" && !Array.isArray(value);
const idPattern = /^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$/;
function fail(): never { throw new Error("SEISMIC_PREVIEW_INVALID"); }
const number = (value: unknown): number => typeof value === "number" && Number.isFinite(value) ? value : fail();
const epoch = (value: unknown): number => {
  const n = number(value);
  return Number.isSafeInteger(n) && Math.abs(n) <= 8640000000000000 ? n : fail();
};
const optionalNumber = (value: unknown): number | null => value == null ? null : number(value);
const optionalText = (value: unknown): string | null => value == null ? null
  : typeof value === "string" && value.length > 0 && value.length <= 256 && !/[\u0000-\u001f]/.test(value) ? value : fail();

export function previewScope(startMs: number, endMs: number): SeismicPreviewScope {
  epoch(startMs); epoch(endMs);
  if (startMs >= endMs) fail();
  return Object.freeze({ startMs, endMs });
}

/** USGS-shaped bytes do not prove they came from USGS. Original fields are not rendered as HTML. */
export async function inspectSeismicSnapshot(
  bytes: ArrayBuffer, scope: SeismicPreviewScope, inspectedAt: string,
): Promise<SeismicPreview> {
  const boundScope = previewScope(scope.startMs, scope.endMs);
  if (!(bytes instanceof ArrayBuffer) || bytes.byteLength > SEISMIC_PREVIEW_MAX_BYTES) fail();
  if (typeof inspectedAt !== "string" || !/^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z$/.test(inspectedAt)
    || !Number.isFinite(Date.parse(inspectedAt)) || new Date(inspectedAt).toISOString() !== inspectedAt) fail();
  // Copy once: a caller cannot change the bytes between parsing and hashing.
  const original = bytes.slice(0);
  const payload = await readBoundedJson(new Response(original), SEISMIC_PREVIEW_MAX_BYTES);
  if (!record(payload) || payload.type !== "FeatureCollection" || !Array.isArray(payload.features)
    || payload.features.length > SEISMIC_PREVIEW_MAX_EVENTS || !record(payload.metadata)
    || payload.metadata.count !== payload.features.length || payload.metadata.status !== 200) fail();
  const generatedMs = payload.metadata.generated == null ? null : epoch(payload.metadata.generated);
  const seen = new Set<string>();
  const events: SeismicPreviewEvent[] = [];
  for (const feature of payload.features) {
    if (!record(feature) || feature.type !== "Feature" || typeof feature.id !== "string" || !idPattern.test(feature.id)
      || !record(feature.properties) || !record(feature.geometry) || feature.geometry.type !== "Point"
      || !Array.isArray(feature.geometry.coordinates) || feature.geometry.coordinates.length !== 3) fail();
    const p = feature.properties;
    const longitude = number(feature.geometry.coordinates[0]);
    const latitude = number(feature.geometry.coordinates[1]);
    if (longitude < -180 || longitude > 180 || latitude < -90 || latitude > 90) fail();
    const event: SeismicPreviewEvent = Object.freeze({ id: feature.id, originMs: epoch(p.time),
      updatedMs: p.updated == null ? null : epoch(p.updated), longitude, latitude,
      depthKm: optionalNumber(feature.geometry.coordinates[2]), magnitude: optionalNumber(p.mag),
      magnitudeType: optionalText(p.magType), reviewStatus: optionalText(p.status) });
    const aliases = new Set([event.id]);
    if (p.ids != null) {
      if (typeof p.ids !== "string" || p.ids.length > 2048) fail();
      const parts = p.ids.split(",").filter(Boolean);
      if (parts.length > 128 || parts.some((id) => !idPattern.test(id))) fail();
      parts.forEach((id) => aliases.add(id));
    }
    for (const alias of aliases) {
      if (seen.has(alias)) fail();
      seen.add(alias);
    }
    const eventType = optionalText(p.type);
    const [west, south, east, north] = KANSAS_SEISMIC_PREVIEW_BOUNDS;
    if (eventType === "earthquake" && boundScope.startMs <= event.originMs && event.originMs < boundScope.endMs
      && west <= longitude && longitude <= east && south <= latitude && latitude <= north) events.push(event);
  }
  const hash = await crypto.subtle.digest("SHA-256", original);
  const sha256 = "sha256:" + Array.from(new Uint8Array(hash), (n) => n.toString(16).padStart(2, "0")).join("");
  return Object.freeze({ scope: boundScope, events: Object.freeze(events), suppliedCount: payload.features.length,
    excludedCount: payload.features.length - events.length, generatedMs, inspectedAt, sha256,
    origin: "UNVERIFIED_LOCAL_FILE", admission: "NOT_ADMITTED" });
}

export type PreviewSessionState = Readonly<{
  phase: "IDLE" | "PROCESSING" | "PREVIEW" | "STALE_PREVIEW" | "ERROR";
  preview: SeismicPreview | null; selectedId: string | null;
}>;

/** Generational tokens prevent a late import from restoring cleared data or selection. */
export class SeismicPreviewSession {
  private generation = 0;
  private active: number | null = null;
  private scopeKey = "";
  private value: PreviewSessionState = Object.freeze({ phase: "IDLE", preview: null, selectedId: null });
  get state(): PreviewSessionState { return this.value; }
  begin(scope: SeismicPreviewScope): number {
    const { startMs, endMs } = previewScope(scope.startMs, scope.endMs);
    const key = JSON.stringify([startMs, endMs]);
    if (key !== this.scopeKey) this.clear();
    this.scopeKey = key;
    this.active = ++this.generation;
    this.value = Object.freeze({ ...this.value, phase: "PROCESSING" });
    return this.active;
  }
  accept(ticket: number, preview: SeismicPreview): boolean {
    if (ticket !== this.active || JSON.stringify([preview.scope.startMs, preview.scope.endMs]) !== this.scopeKey) return false;
    this.active = null;
    this.value = Object.freeze({ phase: "PREVIEW", preview, selectedId: null });
    return true;
  }
  fail(ticket: number): boolean {
    if (ticket !== this.active) return false;
    this.active = null;
    this.value = Object.freeze({ ...this.value, phase: this.value.preview ? "STALE_PREVIEW" : "ERROR" });
    return true;
  }
  select(id: string): boolean {
    if (!this.value.preview?.events.some((event) => event.id === id)) return false;
    this.value = Object.freeze({ ...this.value, selectedId: id });
    return true;
  }
  clear(): void {
    this.generation += 1;
    this.active = null;
    this.scopeKey = "";
    this.value = Object.freeze({ phase: "IDLE", preview: null, selectedId: null });
  }
}
