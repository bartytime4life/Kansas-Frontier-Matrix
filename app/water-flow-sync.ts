import type { FeatureCollection } from "geojson";
import type { GeoJSONSource, Map as MapLibreMap } from "./maplibre-seam";
import { createSettledMapCommit, uploadedGeoJSON } from "./map-performance";
import { effectiveSceneLight, sceneEffectsFor, type SceneLightPreset } from "./scene-effects";
import { createWaterFlowLayer, WATER_FLOW_PALETTES, type WaterFlowLayer } from "./water-flow-layer";
import {
  buildFlowGeometry, flowCellSelectionForView, flowDetailForZoom, flowRequestKey, parseFlowRequestKey, FLOW_PROFILES, FLOW_MIN_ZOOM, gaugeCue, parseFlowlinePayload,
  type FlowDetail, type FlowlineCellPayload, type FlowReach, type GaugeCue,
} from "./water-flow-motion";

/**
 * Keeps the flowing-water layer in step with the map: fetches 3DHP cells
 * around the view, follows the USGS gauge layer's current readings (live,
 * playback or a saved day), and shows the layer only where it applies.
 */

export const WATER_FLOW_LAYER_ID = "scene-water-flow";
const CACHE_LIMIT = 36;
const RETRY_AFTER_MS = 60_000;

export type WaterFlowStatus = Readonly<{
  state: "off" | "zoom" | "loading" | "ready" | "partial" | "unavailable";
  reaches: number;
  gaugedReaches: number;
  cells: number;
  failedCells: number;
  truncatedCells: number;
  availableReaches: number;
  drawingLimited: boolean;
  detail?: FlowDetail;
  viewLimited?: boolean;
}>;
const OFF: WaterFlowStatus = Object.freeze({ state: "off", reaches: 0, gaugedReaches: 0, cells: 0, failedCells: 0, truncatedCells: 0, availableReaches: 0, drawingLimited: false });

type CellState = { state: "loading"; controller: AbortController } | { state: "ready"; payload: FlowlineCellPayload } | { state: "failed"; at: number };
type FlowState = {
  cache: Map<string, CellState>;
  wanted: string[];
  detail: FlowDetail;
  viewLimited: boolean;
  preset: SceneLightPreset;
  efficient: boolean;
  gaugeSourceId: string;
  gaugeLayerId: string;
  geometryKey: string;
  status: WaterFlowStatus;
  listening: boolean;
  rebuildFrame: number;
  layer: WaterFlowLayer | null;
};
const states = new WeakMap<object, FlowState>();
const listeners = new Set<(status: WaterFlowStatus) => void>();

const fetchDefault = async (key: string, signal: AbortSignal): Promise<FlowlineCellPayload> => {
  const request = parseFlowRequestKey(key);
  if (!request) throw new Error("Invalid flowline request.");
  const suffix = request.detail === "local" ? "" : "&detail=" + request.detail;
  const response = await fetch("/api/hydrology/flowlines?cell=" + encodeURIComponent(request.cell.map(v => v.toFixed(2)).join(",")) + suffix, { signal, headers: { Accept: "application/json" } });
  if (!response.ok) throw new Error("Flowline cell unavailable.");
  const payload = parseFlowlinePayload(await response.json());
  if (flowRequestKey(payload.cell, payload.detail ?? "local") !== key) throw new Error("Flowline response identity mismatch.");
  return payload;
};
let fetchCell = fetchDefault;
/** Test seam: replaces how cells are fetched; omission restores production transport. */
export const setWaterFlowFetcher = (fetcher: typeof fetchCell = fetchDefault): void => { fetchCell = fetcher; };

/** The Scene panel follows the most recently updated map. */
export const subscribeWaterFlowStatus = (listener: (status: WaterFlowStatus) => void): (() => void) => {
  listeners.add(listener);
  return () => { listeners.delete(listener); };
};
export const waterFlowStatus = (map: object): WaterFlowStatus => states.get(map)?.status ?? OFF;

let motionStartedAt: number | null = null;
/** One flow clock for the page; null holds the water still (reduced motion, ambient motion off, Battery saver). */
export const setWaterFlowMotion = (active: boolean): void => {
  motionStartedAt = active ? (motionStartedAt ?? performance.now()) : null;
};
const flowClock = (): number | null => motionStartedAt === null ? null : (performance.now() - motionStartedAt) / 1000;

export const waterFlowShouldShow = (enabled: boolean, efficient: boolean, zoom: number): boolean =>
  enabled && !efficient && Number.isFinite(zoom) && zoom >= FLOW_MIN_ZOOM;

/** The layer instance this module added, while the style still holds it. */
const layerOf = (map: MapLibreMap): WaterFlowLayer | undefined =>
  map.getLayer(WATER_FLOW_LAYER_ID) ? states.get(map)?.layer ?? undefined : undefined;
export const waterFlowIsAnimating = (map: MapLibreMap): boolean =>
  Boolean(map.getLayer(WATER_FLOW_LAYER_ID)) && map.getLayoutProperty(WATER_FLOW_LAYER_ID, "visibility") === "visible"
  && (layerOf(map)?.segmentCount ?? 0) > 0;

const setStatus = (state: FlowState, status: WaterFlowStatus) => {
  if (JSON.stringify(state.status) === JSON.stringify(status)) return;
  state.status = status;
  for (const listener of listeners) { try { listener(status); } catch { /* listener only */ } }
};

const gaugeCues = (map: MapLibreMap, state: FlowState): GaugeCue[] => {
  if (!map.getLayer(state.gaugeLayerId) || map.getLayoutProperty(state.gaugeLayerId, "visibility") === "none") return [];
  const data: FeatureCollection | undefined = uploadedGeoJSON(map.getSource(state.gaugeSourceId) as GeoJSONSource | undefined);
  return (data?.features ?? []).flatMap((feature) => {
    const cue = feature.geometry?.type === "Point" ? gaugeCue(feature.properties as Record<string, unknown> | null, feature.geometry.coordinates) : null;
    return cue ? [cue] : [];
  });
};

/** Rebuilds geometry when the ready cells or gauge readings changed. */
const rebuild = (map: MapLibreMap, state: FlowState) => {
  const layer = layerOf(map);
  const visible = waterFlowShouldShow(sceneEffectsFor(map).waterFlow, state.efficient, map.getZoom());
  if (!layer || !visible) {
    setStatus(state, { ...OFF, state: sceneEffectsFor(map).waterFlow && !state.efficient ? "zoom" : "off" });
    return;
  }
  const ready = state.wanted.flatMap((key) => { const cell = state.cache.get(key); return cell?.state === "ready" ? [cell.payload] : []; });
  const cues = state.detail === "local" ? gaugeCues(map, state) : [];
  const key = JSON.stringify([state.detail, ready.map((payload) => flowRequestKey(payload.cell, payload.detail ?? "local")), cues]);
  let metrics = state.status;
  if (key !== state.geometryKey) {
    state.geometryKey = key;
    const reaches: FlowReach[] = ready.flatMap((payload) => payload.reaches);
    const geometry = buildFlowGeometry(reaches, cues);
    layer.setGeometry(geometry.count ? geometry : null);
    metrics = { ...state.status, reaches: geometry.reaches, gaugedReaches: geometry.gauged,
      availableReaches: geometry.availableReaches, drawingLimited: geometry.truncated };
  }
  const failed = state.wanted.filter((cellKey) => state.cache.get(cellKey)?.state === "failed").length;
  const loading = state.wanted.filter((cellKey) => state.cache.get(cellKey)?.state === "loading").length;
  setStatus(state, {
    state: loading ? "loading" : failed === state.wanted.length && failed > 0 ? "unavailable" : failed || state.viewLimited || metrics.drawingLimited || ready.some((payload) => payload.truncated) ? "partial" : "ready",
    reaches: metrics.reaches, gaugedReaches: metrics.gaugedReaches,
    cells: ready.length, failedCells: failed, truncatedCells: ready.filter((payload) => payload.truncated).length,
    availableReaches: metrics.availableReaches, drawingLimited: metrics.drawingLimited, detail: state.detail, viewLimited: state.viewLimited,
  });
};

const cancelRebuild = (state: FlowState) => {
  if (state.rebuildFrame) cancelAnimationFrame(state.rebuildFrame);
  state.rebuildFrame = 0;
};

/** Coalesce cell completions and gauge playback before the next visible frame. */
const scheduleRebuild = (map: MapLibreMap, state: FlowState) => {
  if (states.get(map) !== state || state.rebuildFrame || !state.wanted.length) return;
  state.rebuildFrame = requestAnimationFrame(() => {
    state.rebuildFrame = 0;
    if (states.get(map) !== state) return;
    try { rebuild(map, state); } catch { /* decorative */ }
  });
};

const clearPendingWork = (state: FlowState) => {
  cancelRebuild(state);
  for (const cell of state.cache.values()) if (cell.state === "loading") cell.controller.abort();
  state.cache.clear(); state.wanted = []; state.geometryKey = "";
  setStatus(state, OFF);
};

const requestCells = (map: MapLibreMap, state: FlowState) => {
  const bounds = map.getBounds();
  const center = map.getCenter();
  const visible = waterFlowShouldShow(sceneEffectsFor(map).waterFlow, state.efficient, map.getZoom());
  const selection = visible
    ? flowCellSelectionForView({ west: bounds.getWest(), south: bounds.getSouth(), east: bounds.getEast(), north: bounds.getNorth() }, [center.lng, center.lat], map.getZoom())
    : { cells: [], limited: false };
  state.detail = flowDetailForZoom(map.getZoom());
  state.viewLimited = selection.limited;
  const wanted = selection.cells.map(cell => flowRequestKey(cell, state.detail));
  state.wanted = wanted;
  // Cancel requests the view no longer needs.
  for (const [key, cell] of state.cache) {
    if (cell.state === "loading" && !wanted.includes(key)) { cell.controller.abort(); state.cache.delete(key); }
  }
  const now = Date.now();
  for (const key of wanted) {
    const cell = state.cache.get(key);
    if (cell && (cell.state !== "failed" || now - cell.at < RETRY_AFTER_MS)) {
      // Refresh recency for the cache order.
      state.cache.delete(key); state.cache.set(key, cell);
      continue;
    }
    const controller = new AbortController();
    const request = { state: "loading" as const, controller };
    state.cache.set(key, request);
    void fetchCell(key, controller.signal).then(
      (payload) => {
        // Abort is advisory: a resolved old request must not replace a new one
        // for the same cell after a rapid pan or off/on toggle.
        if (!controller.signal.aborted && state.cache.get(key) === request) {
          state.cache.set(key, { state: "ready", payload }); scheduleRebuild(map, state);
        }
      },
      () => {
        if (!controller.signal.aborted && state.cache.get(key) === request) {
          state.cache.set(key, { state: "failed", at: Date.now() }); scheduleRebuild(map, state);
        }
      },
    );
  }
  while (state.cache.size > CACHE_LIMIT) {
    const oldest = [...state.cache.keys()].find((key) => !wanted.includes(key));
    if (!oldest) break;
    state.cache.delete(oldest);
  }
  rebuild(map, state);
};

export type WaterFlowSyncOptions = Readonly<{
  light: SceneLightPreset;
  azimuth: number;
  efficient: boolean;
  /** The official USGS streamflow source and point layer. */
  gaugeSourceId: string;
  gaugeLayerId: string;
}>;

/**
 * Adds (or removes) the flowing-water layer above the basemap and below data
 * overlays and labels, and brings it up to date. Safe on every style load.
 */
export function syncWaterFlow(map: MapLibreMap, options: WaterFlowSyncOptions): boolean {
  let state = states.get(map);
  if (!sceneEffectsFor(map).waterFlow) {
    if (map.getLayer(WATER_FLOW_LAYER_ID)) map.removeLayer(WATER_FLOW_LAYER_ID);
    if (state) clearPendingWork(state);
    return true;
  }
  if (!state) {
    state = { cache: new Map(), wanted: [], detail: "local", viewLimited: false, preset: options.light, efficient: options.efficient, gaugeSourceId: options.gaugeSourceId, gaugeLayerId: options.gaugeLayerId, geometryKey: "", status: OFF, listening: false, rebuildFrame: 0, layer: null };
    states.set(map, state);
  }
  const current = state;
  current.preset = effectiveSceneLight(map, options.light, options.azimuth).preset;
  current.efficient = options.efficient;
  current.gaugeSourceId = options.gaugeSourceId;
  current.gaugeLayerId = options.gaugeLayerId;
  if (!current.listening) {
    current.listening = true;
    const settledMove = createSettledMapCommit(() => {
      if (states.get(map) !== current || !sceneEffectsFor(map).waterFlow) return;
      try { requestCells(map, current); syncWaterFlowVisibility(map, current.efficient); } catch { /* decorative */ }
    }, () => map.isMoving());
    const move = () => settledMove.schedule();
    const start = () => settledMove.cancel();
    const source = (event: { sourceId?: string }) => {
      if (event.sourceId === current.gaugeSourceId) scheduleRebuild(map, current);
    };
    const remove = () => {
      states.delete(map);
      settledMove.cancel();
      clearPendingWork(current);
      current.layer = null;
      map.off("moveend", move); map.off("movestart", start); map.off("sourcedata", source); map.off("remove", remove);
    };
    map.on("moveend", move);
    map.on("movestart", start);
    map.on("sourcedata", source);
    map.on("remove", remove);
  }
  // Decorative: a GPU or shader failure removes the layer and never degrades the map.
  try {
    if (!map.getLayer(WATER_FLOW_LAYER_ID)) {
      const beforeId = map.getStyle().layers?.find((layer) => layer.type === "symbol"
        || (layer.id.startsWith("kfm-") && layer.id !== "kfm-background") || layer.id.startsWith("external-"))?.id;
      const layer = createWaterFlowLayer({ id: WATER_FLOW_LAYER_ID, clock: flowClock, palette: () => WATER_FLOW_PALETTES[current.preset] });
      map.addLayer(layer, beforeId);
      current.layer = layer;
      current.geometryKey = "";
    }
    syncWaterFlowVisibility(map, current.efficient);
    requestCells(map, current);
    return true;
  } catch {
    try { if (map.getLayer(WATER_FLOW_LAYER_ID)) map.removeLayer(WATER_FLOW_LAYER_ID); } catch { /* already gone */ }
    return false;
  }
}

export function syncWaterFlowVisibility(map: MapLibreMap, efficient: boolean): void {
  if (!map.getLayer(WATER_FLOW_LAYER_ID)) return;
  const visibility = waterFlowShouldShow(sceneEffectsFor(map).waterFlow, efficient, map.getZoom()) ? "visible" : "none";
  if (map.getLayoutProperty(WATER_FLOW_LAYER_ID, "visibility") !== visibility) map.setLayoutProperty(WATER_FLOW_LAYER_ID, "visibility", visibility);
}

/** A short reading for the Scene panel. */
export function waterFlowReading(status: WaterFlowStatus): string | null {
  switch (status.state) {
    case "off": return null;
    case "zoom": return `Zoom to ${FLOW_MIN_ZOOM} or closer to see rivers flow`;
    case "loading": return (status.detail ? FLOW_PROFILES[status.detail].label + " · " : "") + "Loading USGS 3DHP river directions…" + (status.reaches ? " · " + status.reaches.toLocaleString("en-US") + " reaches already visible" : "");
    case "unavailable": return (status.detail ? FLOW_PROFILES[status.detail].label + " · " : "") + "USGS 3DHP river directions are unavailable right now";
    default: {
      const tier = status.detail ? FLOW_PROFILES[status.detail].label + " · " : "";
      const reaches = `${status.reaches.toLocaleString("en-US")} reach${status.reaches === 1 ? "" : "es"} with a USGS flow direction`;
      const gauged = status.gaugedReaches ? ` · ${status.gaugedReaches} lit by a gauge reading` : "";
      const partial = status.drawingLimited
        ? ` · drawing limit: ${status.availableReaches.toLocaleString("en-US")} loaded reaches; some geometry omitted`
        : status.state === "partial" ? " · some areas incomplete" : "";
      return status.reaches ? tier + `${reaches}${gauged}${partial}` : `No mapped flow direction in view${partial}`;
    }
  }
}
