import type { Map as MapLibreMap } from "./maplibre-seam";
import { basemapSourceIdentity, basemapTileKey } from "./basemap-health";

// Explicit browser-local opt-in, consistent with stormPerf. No transport,
// persistent storage, raw coordinates, URLs, exception text or stacks.
type TraceEvent = { event: string; at: number; generation: number; basemap: string; source: string | null;
  sourceInstance: number | null; sourceRelation: "current" | "different" | "unknown";
  tile: number | null; tileState: string | null; status: number | null; cancelled: boolean;
  viewport: [number, number]; hidden: boolean };
type Trace = { snapshot: () => { startedAtEpochMs: number; events: TraceEvent[]; firstFailure: TraceEvent | null; droppedEvents: number; uncorrelatedTiles: number; collectorErrors: number; boundary: string } };

export function installBasemapDiagnostics(map: MapLibreMap, readState: () => { generation: number; basemap: string }): () => void {
  if (new URLSearchParams(window.location.search).get("basemapTrace") !== "1") return () => {};
  const host = window as Window & { __kfmBasemapTrace?: Trace };
  const events: TraceEvent[] = [], instances = new WeakMap<object, number>(), tiles = new Map<string, number>();
  let sequence = 0, droppedEvents = 0, uncorrelatedTiles = 0, collectorErrors = 0, firstFailure: TraceEvent | null = null;
  const started = performance.now();
  const startedAtEpochMs = Number.isFinite(performance.timeOrigin) ? performance.timeOrigin + started : Date.now();
  const capture = (name: string, value?: unknown) => {
    const event = value as { sourceId?: string; source?: unknown; tile?: { state?: string }; error?: { status?: number; name?: string } } | undefined;
    const state = readState();
    const styleSources = map.getStyle()?.sources ?? {};
    // Only finite, renderer-registered IDs; unknown/untrusted IDs are omitted.
    const publicIds = ["openmaptiles", "ne2_shaded", "basemap-relief-dem", "orientation-kansas", "esri-imagery", "kansas-ng911-2024", "photoreal-openmaptiles", "osm-context", "usgs-topo-context"];
    const id = event?.sourceId && publicIds.includes(event.sourceId) && Object.hasOwn(styleSources, event.sourceId) ? event.sourceId : null;
    const source = id ? map.getSource(id) : undefined;
    if (source && !instances.has(source)) instances.set(source, ++sequence);
    const currentIdentity = source ? basemapSourceIdentity(source.serialize()) : null;
    const originIdentity = basemapSourceIdentity(event?.source);
    const key = basemapTileKey(value);
    const scopedKey = key && id ? `${state.generation}:${id}:${instances.get(source!) ?? 0}:${key}` : null;
    if (scopedKey && !tiles.has(scopedKey)) { if (tiles.size < 2048) tiles.set(scopedKey, tiles.size + 1); else uncorrelatedTiles++; }
    const row: TraceEvent = { event: name, at: Math.round(performance.now() - started), ...state, source: id,
      sourceInstance: source ? instances.get(source)! : null,
      sourceRelation: currentIdentity && originIdentity ? currentIdentity === originIdentity ? "current" : "different" : "unknown",
      tile: scopedKey ? tiles.get(scopedKey) ?? null : null,
      tileState: ["loaded", "errored", "loading", "reloading", "expired", "unloaded"].includes(event?.tile?.state ?? "") ? event!.tile!.state! : null,
      status: typeof event?.error?.status === "number" && Number.isInteger(event.error.status) && event.error.status >= 100 && event.error.status <= 599 ? event.error.status : null,
      cancelled: event?.error?.name === "AbortError", viewport: [window.innerWidth, window.innerHeight], hidden: document.hidden };
    if (name === "error" && !firstFailure) firstFailure = row;
    if (events.length === 512) { events.shift(); droppedEvents++; }
    events.push(row);
  };
  const record = (name: string, value?: unknown) => { try { capture(name, value); } catch { collectorErrors++; } };
  const bindings = ["styledataloading", "styledata", "style.load", "sourcedataloading", "sourcedata", "sourcedataabort", "error", "idle", "resize", "movestart", "moveend", "zoomstart", "zoomend", "rotateend", "pitchend"] as const;
  const listeners = bindings.map(name => { const fn = (event: unknown) => record(name, event); map.on(name, fn); return { name, fn }; });
  const visibility = () => record("visibilitychange"), navigation = () => record("navigation");
  document.addEventListener("visibilitychange", visibility);
  for (const name of ["pagehide", "pageshow", "popstate"]) window.addEventListener(name, navigation);
  const copy = (row: TraceEvent): TraceEvent => ({ ...row, viewport: [...row.viewport] });
  const probe: Trace = { snapshot: () => ({ startedAtEpochMs, events: events.map(copy), firstFailure: firstFailure ? copy(firstFailure) : null,
    droppedEvents, uncorrelatedTiles, collectorErrors,
    boundary: "Attached immediately after Map construction; constructor-synchronous events and pre-navigation network are not captured. Tile tokens omit coordinates. Settlement is not successful coverage. No provider root cause inferred." }) };
  host.__kfmBasemapTrace = probe;
  record("attached");
  return () => {
    for (const { name, fn } of listeners) map.off(name, fn);
    document.removeEventListener("visibilitychange", visibility);
    for (const name of ["pagehide", "pageshow", "popstate"]) window.removeEventListener(name, navigation);
    if (host.__kfmBasemapTrace === probe) delete host.__kfmBasemapTrace;
  };
}
