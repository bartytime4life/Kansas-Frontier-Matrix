import type { GeoJSONSource, LayerSpecification, Map as MapLibreMap } from "./maplibre-seam";
import type { FeatureCollection } from "geojson";
import { TERRAIN_SOURCE_ID, terrainPresentationSourceMatches, unexaggeratedTerrainElevation } from "./map-runtime";
import { effectiveSceneLight } from "./scene-effects";
import { terrainSourceFor } from "./terrain-sources";
import { orderedOverlayIds } from "./map-layer-composition";
import {
  TERRAIN_DRAWING_INITIAL_STATUS, TERRAIN_DRAWING_MIN_ZOOM,
  terrainDrawingCoordinate, terrainDrawingFootprint, terrainDrawingGeometryBatches,
  type TerrainDrawingConfig, type TerrainDrawingGeometry, type TerrainDrawingGrid, type TerrainDrawingStatus,
} from "./terrain-drawing";
import { terrainSurfaceGeometryBatches, terrainSurfaceCellAt, terrainSurfaceOpacity, type TerrainSurfaceGeometry, type TerrainSurfaceProbe } from "./terrain-surface";

export const TERRAIN_DRAWING_SOURCE_ID = "scene-terrain-drawing";
export const TERRAIN_DRAWING_LAYER_IDS = ["scene-terrain-grid-casing", "scene-terrain-grid", "scene-terrain-contour-casing", "scene-terrain-contours", "scene-terrain-index"] as const;
export const TERRAIN_SURFACE_LAYER_ID = "scene-terrain-surface";
const SAMPLE_BATCH = 128;
const RESAMPLE_THROTTLE_MS = 700;
type Camera = { center: [number, number]; zoom: number };
const sameCamera = (a: Camera, b: Camera) => Math.abs(a.zoom - b.zoom) < 1e-7 && a.center.every((value, index) => Math.abs(value - b.center[index]) < 1e-7);
const palettes = {
  clear: { minor: "#b9e1ce", major: "#fff0bb", grid: "#89c6b3", casing: "#183c35" },
  dusk: { minor: "#ffc98f", major: "#fff1c6", grid: "#a0d1ce", casing: "#493329" },
  night: { minor: "#91d2eb", major: "#e3f8ff", grid: "#78afc9", casing: "#142a3a" },
};

/** A display-only derivative of the already-loaded terrain. No request path,
 * extra DEM source, render loop, worker, export or persistent storage is added. */
export function createTerrainDrawing(map: MapLibreMap, onStatus: (status: TerrainDrawingStatus) => void, onProbe?: (probe: TerrainSurfaceProbe | null) => void) {
  let config: TerrainDrawingConfig = { mode: "off", enabled: false, provider: "mapzen", efficient: false, detail: false, light: "clear", azimuth: 210 };
  let status = TERRAIN_DRAWING_INITIAL_STATUS;
  let destroyed = false, mutating = false, moving = false, sampling = false, generation = 0;
  let timer: ReturnType<typeof setTimeout> | undefined;
  let activeSource: object | undefined;
  let samplingCamera: Camera | undefined;
  let lastStarted = -Infinity;
  let contentPending = false;
  let cache: { geometry: TerrainDrawingGeometry; surface: TerrainSurfaceGeometry; footprint: Omit<TerrainDrawingGrid, "heights">; camera: Camera; source: object } | undefined;
  let probeId: number | undefined;
  const active = (value = config) => value.mode !== "off" || (value.surface ?? "off") !== "off";
  const surfaceOn = () => (config.surface ?? "off") !== "off";

  const report = (next: TerrainDrawingStatus) => {
    if (destroyed || JSON.stringify(next) === JSON.stringify(status)) return;
    status = next;
    onStatus(next);
  };
  const camera = (): Camera => {
    const center = map.getCenter();
    return { center: [center.lng, center.lat], zoom: map.getZoom() };
  };
  const source = (): object | undefined => {
    try {
      if (!config.enabled || !active() || map.getProjection()?.type !== "mercator" || map.getTerrain()?.source !== TERRAIN_SOURCE_ID || !terrainPresentationSourceMatches(map, terrainSourceFor(config.provider))) return;
      return map.getSource(TERRAIN_SOURCE_ID);
    } catch { return; }
  };
  const cancel = () => {
    generation += 1;
    if (timer !== undefined) clearTimeout(timer);
    timer = undefined;
    samplingCamera = undefined;
    sampling = false;
  };
  const remove = () => {
    mutating = true;
    try {
      for (const id of [...TERRAIN_DRAWING_LAYER_IDS, TERRAIN_SURFACE_LAYER_ID]) if (map.getLayer(id)) map.removeLayer(id);
      if (map.getSource(TERRAIN_DRAWING_SOURCE_ID)) map.removeSource(TERRAIN_DRAWING_SOURCE_ID);
    } catch { /* A replacing style owns disposal of the previous layers. */ }
    finally { mutating = false; }
  };
  const clearProbe = () => {
    if (probeId === undefined) return;
    try { if (map.getSource(TERRAIN_DRAWING_SOURCE_ID)) map.setFeatureState({ source: TERRAIN_DRAWING_SOURCE_ID, id: probeId }, { probed: false }); } catch { /* A removed style has no feature state to clear. */ }
    probeId = undefined;
    onProbe?.(null);
  };
  const clear = () => { cancel(); clearProbe(); cache = undefined; remove(); };
  const unavailable = (message: string) => report({ ...TERRAIN_DRAWING_INITIAL_STATUS, state: "unavailable", message });
  const waiting = () => report({ ...TERRAIN_DRAWING_INITIAL_STATUS, state: "loading", message: "Settling the view · drawing follows loaded terrain" });
  const readyStatus = () => {
    if (!cache) return;
    const { geometry, footprint, surface } = cache;
    const coverage = Math.round(geometry.coverage * 100);
    report({
      state: geometry.coverage > 0 ? "ready" : "loading",
      message: geometry.coverage === 0 ? "Waiting for loaded elevation tiles in the centered patch"
        : `${coverage}% sampled coverage · centered patch${geometry.clipped ? " · drawing detail capped" : geometry.intervalMeters === null ? " · no contour crossings" : ""}`,
      intervalMeters: geometry.intervalMeters, spacingMeters: footprint.spacingMeters,
      coverage: geometry.coverage, sampleCount: geometry.sampleCount,
      validCellCount: surface.cells.size, totalCellCount: surface.totalCellCount,
    });
  };
  const beforeEvidence = () => {
    const layers = map.getStyle().layers ?? [];
    const overlays = new Set(orderedOverlayIds(layers));
    return layers.find(layer => layer.type === "symbol" || overlays.has(layer.id))?.id;
  };
  const orderDrawing = () => {
    // The optional native height tint can be added after our fill. Reestablish
    // the drawing group above it, with derivative fill below all line casings.
    const layers = map.getStyle().layers ?? [];
    const order = layers.map(layer => layer.id);
    if (!order.includes(TERRAIN_SURFACE_LAYER_ID)) return;
    const group = [TERRAIN_SURFACE_LAYER_ID, ...TERRAIN_DRAWING_LAYER_IDS].filter(id => order.includes(id));
    const before = beforeEvidence();
    const other = order.filter(id => !group.includes(id));
    const insertion = before ? other.indexOf(before) : other.length;
    const desired = [...other.slice(0, insertion), ...group, ...other.slice(insertion)];
    if (desired.some((id, index) => order[index] !== id)) for (const id of group) map.moveLayer(id, before);
    // A late-added tint can be above the evidence anchor. Move only that owned
    // presentation layer beneath our group; moving the group alone would never
    // satisfy the ordering and could repeat on every styledata event.
    const settled = (map.getStyle().layers ?? []).map(layer => layer.id);
    if (settled.indexOf("kfm-terrain-color-relief") > settled.indexOf(TERRAIN_SURFACE_LAYER_ID)) map.moveLayer("kfm-terrain-color-relief", TERRAIN_SURFACE_LAYER_ID);
  };
  const paint = () => {
    if (destroyed || !cache) return;
    mutating = true;
    try {
      const palette = palettes[effectiveSceneLight(map, config.light, config.azimuth).preset];
      if (map.getLayer(TERRAIN_SURFACE_LAYER_ID)) {
        map.setLayoutProperty(TERRAIN_SURFACE_LAYER_ID, "visibility", surfaceOn() ? "visible" : "none");
        map.setPaintProperty(TERRAIN_SURFACE_LAYER_ID, "fill-color", ["get", config.surface === "aspect" ? "aspectColor" : "slopeColor"]);
        map.setPaintProperty(TERRAIN_SURFACE_LAYER_ID, "fill-opacity", terrainSurfaceOpacity(config.surfaceOpacity));
      }
      const contour = config.mode === "contours" || config.mode === "both";
      const grid = config.mode === "grid" || config.mode === "both";
      const styles = [
        { visible: grid, color: palette.casing, opacity: contour ? 0.35 : 0.63 },
        { visible: grid, color: palette.grid, opacity: contour ? 0.34 : 0.66 },
        { visible: contour, color: palette.casing, opacity: 0.85 },
        { visible: contour, color: palette.minor, opacity: 0.9 },
        { visible: contour, color: palette.major, opacity: 1 },
      ];
      for (const [index, id] of TERRAIN_DRAWING_LAYER_IDS.entries()) {
        if (!map.getLayer(id)) continue;
        map.setLayoutProperty(id, "visibility", styles[index].visible ? "visible" : "none");
        map.setPaintProperty(id, "line-color", styles[index].color);
        map.setPaintProperty(id, "line-opacity", styles[index].opacity);
      }
      orderDrawing();
    } catch { /* Style replacement will retrigger sampling once ready. */ }
    finally { mutating = false; }
  };
  const publish = (geometry: TerrainDrawingGeometry, surface: TerrainSurfaceGeometry, footprint: Omit<TerrainDrawingGrid, "heights">, sampledCamera: Camera, sampledSource: object, token: number) => {
    if (destroyed || token !== generation || source() !== sampledSource || !sameCamera(camera(), sampledCamera)) return;
    mutating = true;
    try {
      clearProbe();
      const data: FeatureCollection = { type: "FeatureCollection", features: [...surface.data.features, ...geometry.data.features] };
      const attached = map.getSource(TERRAIN_DRAWING_SOURCE_ID) as GeoJSONSource | undefined;
      if (attached) attached.setData(data);
      else map.addSource(TERRAIN_DRAWING_SOURCE_ID, { type: "geojson", data, attribution: "KFM terrain drawing · loaded display DEM · approximate display derivatives" });
      const before = beforeEvidence();
      if (!map.getLayer(TERRAIN_SURFACE_LAYER_ID)) map.addLayer({
        id: TERRAIN_SURFACE_LAYER_ID, type: "fill", source: TERRAIN_DRAWING_SOURCE_ID,
        filter: ["==", ["get", "role"], "surface"],
        paint: { "fill-color": ["get", "slopeColor"], "fill-opacity": 0.55,
          "fill-outline-color": ["case", ["boolean", ["feature-state", "probed"], false], "#fff8d9", "rgba(0,0,0,0)"] },
      }, TERRAIN_DRAWING_LAYER_IDS.find(id => map.getLayer(id)) ?? before);
      // Two-tone strokes remain legible on both pale cartography and dark
      // imagery. Index contours carry a clearly heavier casing and core;
      // the lattice stays behind them and softens in the combined view.
      const layers: LayerSpecification[] = [
        { id: TERRAIN_DRAWING_LAYER_IDS[0], type: "line", source: TERRAIN_DRAWING_SOURCE_ID, filter: ["==", ["get", "role"], "grid"], paint: { "line-width": 1.75 } },
        { id: TERRAIN_DRAWING_LAYER_IDS[1], type: "line", source: TERRAIN_DRAWING_SOURCE_ID, filter: ["==", ["get", "role"], "grid"], paint: { "line-width": 0.7 } },
        { id: TERRAIN_DRAWING_LAYER_IDS[2], type: "line", source: TERRAIN_DRAWING_SOURCE_ID, filter: ["==", ["get", "role"], "contour"], paint: { "line-width": ["case", ["==", ["get", "index"], true], 4.1, 2.5] } },
        { id: TERRAIN_DRAWING_LAYER_IDS[3], type: "line", source: TERRAIN_DRAWING_SOURCE_ID, filter: ["all", ["==", ["get", "role"], "contour"], ["==", ["get", "index"], false]], paint: { "line-width": 0.95 } },
        { id: TERRAIN_DRAWING_LAYER_IDS[4], type: "line", source: TERRAIN_DRAWING_SOURCE_ID, filter: ["all", ["==", ["get", "role"], "contour"], ["==", ["get", "index"], true]], paint: { "line-width": 2.1 } },
      ];
      for (const layer of layers) if (!map.getLayer(layer.id)) map.addLayer(layer, before);
      cache = { geometry, surface, footprint, camera: sampledCamera, source: sampledSource };
      samplingCamera = undefined;
      sampling = false;
    } catch {
      clear();
      unavailable("Terrain drawing is waiting for the map style");
      return;
    } finally { mutating = false; }
    paint();
    readyStatus();
    if (contentPending) schedule();
  };
  const begin = () => {
    timer = undefined;
    if (destroyed || moving) return;
    if (!active()) { clear(); report(TERRAIN_DRAWING_INITIAL_STATUS); return; }
    const sampledSource = source();
    if (!sampledSource) { clear(); activeSource = undefined; unavailable("Choose Terrain 3D to draw the loaded elevation surface"); return; }
    const sampledCamera = camera();
    const footprint = terrainDrawingFootprint(sampledCamera.center, sampledCamera.zoom, config.efficient, config.detail);
    if (!footprint) {
      clear();
      unavailable(sampledCamera.zoom < TERRAIN_DRAWING_MIN_ZOOM ? `Zoom to ${TERRAIN_DRAWING_MIN_ZOOM} or choose a landscape below` : "Center the view within Kansas to draw terrain");
      return;
    }
    activeSource = sampledSource;
    samplingCamera = sampledCamera;
    sampling = true;
    contentPending = false;
    lastStarted = Date.now();
    const token = generation;
    const heights: (number | null)[] = new Array(footprint.size ** 2);
    let offset = 0;
    report({ ...TERRAIN_DRAWING_INITIAL_STATUS, state: "loading", message: "Tracing the loaded elevation surface…", spacingMeters: footprint.spacingMeters });
    const current = () => !destroyed && token === generation && source() === sampledSource && !moving && sameCamera(camera(), sampledCamera);
    const failClosed = () => { if (!destroyed && token === generation) { clear(); unavailable("Terrain changed · waiting for loaded elevation"); } };
    const sampleBatch = () => {
      timer = undefined;
      if (!current()) { failClosed(); return; }
      const until = Math.min(heights.length, offset + SAMPLE_BATCH);
      try {
        for (; offset < until; offset += 1) heights[offset] = unexaggeratedTerrainElevation(map, terrainDrawingCoordinate(footprint, offset));
      } catch { failClosed(); return; }
      if (offset < heights.length) { timer = setTimeout(sampleBatch, 0); return; }
      const sampledGrid = { ...footprint, heights };
      const geometry = terrainDrawingGeometryBatches(sampledGrid);
      const drawBatch = () => {
        timer = undefined;
        if (!current()) { failClosed(); return; }
        const batch = geometry.next();
        if (batch.done) {
          const surface = terrainSurfaceGeometryBatches(sampledGrid);
          const surfaceBatch = () => {
            timer = undefined;
            if (!current()) { failClosed(); return; }
            const cells = surface.next();
            if (cells.done) publish(batch.value, cells.value, footprint, sampledCamera, sampledSource, token);
            else timer = setTimeout(surfaceBatch, 0);
          };
          timer = setTimeout(surfaceBatch, 0);
        }
        else timer = setTimeout(drawBatch, 0);
      };
      timer = setTimeout(drawBatch, 0);
    };
    timer = setTimeout(sampleBatch, 0);
  };
  // The first content event schedules a pass; subsequent events don't reset
  // the timer. This coalesces bursts without starving slow/late tile arrivals.
  function schedule() {
    if (destroyed || moving || sampling || !active() || timer !== undefined) return;
    timer = setTimeout(begin, Math.max(100, lastStarted + RESAMPLE_THROTTLE_MS - Date.now()));
  }
  const onMoveStart = () => {
    moving = true;
    cancel();
    clearProbe();
    if (active() && !cache) waiting();
  };
  const onMove = () => {
    if (destroyed || !active()) return;
    const previous = cache?.camera ?? samplingCamera;
    if (previous && !sameCamera(previous, camera())) { clear(); waiting(); }
  };
  const onMoveEnd = () => {
    moving = false;
    if (!active()) return;
    if (cache && source() === cache.source && sameCamera(cache.camera, camera()) && !contentPending) { paint(); readyStatus(); }
    else { if (cache && (!sameCamera(cache.camera, camera()) || source() !== cache.source)) clear(); schedule(); }
  };
  const onSourceData = (event: { sourceId?: string; sourceDataType?: string }) => {
    if (destroyed || mutating || !active() || event.sourceId !== TERRAIN_SOURCE_ID || (event.sourceDataType && event.sourceDataType !== "content")) return;
    if (activeSource && source() !== activeSource) clear();
    contentPending = true;
    // A pass in progress finishes against its captured identity, then processes
    // one coalesced trailing update. Overlay setData never reaches this branch.
    schedule();
  };
  const onStyleData = () => {
    if (destroyed || mutating || !active()) return;
    const attached = source();
    if (activeSource && activeSource !== attached) { clear(); activeSource = attached; unavailable("Terrain changed · waiting for loaded elevation"); schedule(); }
    else if (cache) { mutating = true; try { orderDrawing(); } catch { /* A replacing style will reload. */ } finally { mutating = false; } }
  };
  const onStyleLoad = () => { if (!destroyed && active()) { clear(); activeSource = undefined; schedule(); } };
  const probeAt = (coordinate: [number, number]) => {
    if (destroyed || moving || !surfaceOn() || config.probeEnabled === false || !cache || source() !== cache.source || !sameCamera(camera(), cache.camera)) { clearProbe(); return null; }
    const cell = terrainSurfaceCellAt(cache.footprint, cache.surface.cells, coordinate);
    if (!cell) { clearProbe(); return null; }
    const probe: TerrainSurfaceProbe = { slopeDegrees: cell.slopeDegrees, aspectDegrees: cell.aspectDegrees, elevationMeters: cell.elevationMeters, center: cell.center, spacingMeters: cell.spacingMeters };
    if (probeId !== cell.id) {
      clearProbe();
      probeId = cell.id;
      try { map.setFeatureState({ source: TERRAIN_DRAWING_SOURCE_ID, id: cell.id }, { probed: true }); } catch { /* Probe text remains useful without an outline. */ }
      onProbe?.(probe);
    }
    return probe;
  };
  const onPointer = (event: { lngLat: { lng: number; lat: number } }) => probeAt([event.lngLat.lng, event.lngLat.lat]);
  map.on("movestart", onMoveStart);
  map.on("move", onMove);
  map.on("moveend", onMoveEnd);
  map.on("sourcedata", onSourceData);
  map.on("styledata", onStyleData);
  map.on("style.load", onStyleLoad);
  map.on("mousemove", onPointer);
  map.on("click", onPointer);
  map.on("mouseout", clearProbe);

  return {
    update(next: TerrainDrawingConfig) {
      if (destroyed) return;
      const previous = config;
      config = { ...next };
      if (!active()) { clear(); activeSource = undefined; contentPending = false; report(TERRAIN_DRAWING_INITIAL_STATUS); return; }
      if (!surfaceOn() || config.probeEnabled === false || previous.surface !== config.surface) clearProbe();
      const changed = previous.enabled !== config.enabled || previous.provider !== config.provider || previous.efficient !== config.efficient || previous.detail !== config.detail;
      if (changed || !active(previous)) {
        clear(); activeSource = undefined; contentPending = false;
        if (!config.enabled) unavailable("Choose Terrain 3D to draw the loaded elevation surface");
        else { waiting(); schedule(); }
        return;
      }
      // Modes and scene light only affect styling of the same sampled surface.
      if (cache) paint();
      else if (config.enabled) schedule();
    },
    probeCenter() {
      if (destroyed) return null;
      try { return probeAt(camera().center); } catch { clearProbe(); return null; }
    },
    destroy() {
      if (destroyed) return;
      clearProbe();
      destroyed = true;
      cancel();
      map.off("movestart", onMoveStart);
      map.off("move", onMove);
      map.off("moveend", onMoveEnd);
      map.off("sourcedata", onSourceData);
      map.off("styledata", onStyleData);
      map.off("style.load", onStyleLoad);
      map.off("mousemove", onPointer);
      map.off("click", onPointer);
      map.off("mouseout", clearProbe);
      remove();
      cache = undefined;
    },
  };
}
