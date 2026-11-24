import { loadMapLibre, type Map as GLMap, type StyleSpecification, type MapMouseEvent } from "../maplibre-seam";
import { browserRenderBudget } from "../map-performance";
import { webgl2Available } from "../webgl-support";
import { readNeonLidarPilot } from "../neon-lidar-pilot-client";
import { createNeonScienceDataset, type NeonScienceDataset } from "../neon-lidar-science";
import { neonLidarProbe, type NeonLidarMode } from "../neon-lidar-preview";
import { applyNeonMapOverlay, buildNeon3DMapData, buildNeonMapData, neonMapBounds, NEON_LOCAL_FILL, NEON_LOCAL_GROUND, NEON_LOCAL_SOURCE, type NeonMapData, type Neon3DMetadata } from "../neon-lidar-map";
import { buildNeonStoryStops, type NeonStoryStop } from "../neon-lidar-story";

type Probe = ReturnType<typeof neonLidarProbe>;
export type TerrainState = {
  phase: "loading" | "rendering" | "ready" | "error" | "unsupported";
  message: string; dataset: NeonScienceDataset | null; mode: NeonLidarMode;
  scale: number; representation: "columns" | "flat"; metadata: Neon3DMetadata | null;
  row: string; column: string; probe: Probe; stops: NeonStoryStop[]; activeStop: string | null;
};
export const initialTerrainState = (): TerrainState => ({ phase: "loading", message: "Loading the Konza Prairie landscape…", dataset: null, mode: "dtm", scale: 3, representation: "columns", metadata: null, row: "", column: "", probe: null, stops: [], activeStop: null });
export const TERRAIN_LOCAL_STYLE: StyleSpecification = {
  version: 8, projection: { type: "mercator" }, sources: {},
  light: { anchor: "map", position: [1.5, 235, 45], color: "#fff4d6", intensity: 0.6 },
  layers: [{ id: "terrain-background", type: "background", paint: { "background-color": "#102a35" } }],
};
function observe(container: HTMLElement, resize: () => void) {
  const observer = new ResizeObserver(resize); observer.observe(container);
  return () => observer.disconnect();
}
const defaultRuntime = { loadMap: loadMapLibre, readPilot: readNeonLidarPilot, webgl: webgl2Available, budget: browserRenderBudget, observe, defer: queueMicrotask };
const draftNumber = (value: string, limit: number) => /^\d+$/.test(value) && Number.isInteger(Number(value)) && Number(value) >= 1 && Number(value) <= limit ? Number(value) - 1 : null;

/** One route session owns one bounded receipt and one local renderer. No external basemap or DEM. */
export function createTerrainController(container: HTMLElement, onChange: (state: TerrainState) => void, reducedMotion = false, runtime = defaultRuntime) {
  let state = initialTerrainState(), disposed = false, failed = false, map: GLMap | null = null;
  let motionHeld = reducedMotion;
  let styleReady = false, framed = false, renderPending = false, fittedZoom = 15;
  let data: NeonMapData | null = null, unobserve: (() => void) | null = null;
  let styleTimer: ReturnType<typeof setTimeout> | null = null, renderTimer: ReturnType<typeof setTimeout> | null = null;
  const request = new AbortController();
  const publish = (patch: Partial<TerrainState>) => { if (!disposed && (!failed || patch.phase === "error")) { state = { ...state, ...patch }; onChange(state); } };
  const clearTimers = () => { if (styleTimer) clearTimeout(styleTimer); if (renderTimer) clearTimeout(renderTimer); styleTimer = renderTimer = null; };
  const teardown = () => {
    unobserve?.(); unobserve = null;
    if (map) { const old = map; map = null; old.off("style.load", onStyle); old.off("render", onRender); old.off("error", onError); old.off("click", onPick); old.getCanvas().removeEventListener("webglcontextlost", onContextLost); try { old.remove(); } catch { /* Terminal cleanup cannot restore a failed renderer. */ } }
  };
  function fail(message: string) {
    if (disposed || failed) return;
    failed = true; request.abort(); clearTimers(); teardown(); publish({ phase: "error", message });
  }
  function frame(initial = false) {
    if (!map || !state.dataset || !styleReady || failed || disposed) return;
    const bounds = neonMapBounds(state.dataset.receipt.preview);
    if (!bounds) throw new Error("No georeferencing");
    const size = container.getBoundingClientRect();
    if (size.width < 120 || size.height < 160) throw new Error("Map host too small");
    map.resize();
    map.fitBounds(bounds, { padding: { top: 45, left: 35, right: 35, bottom: 45 }, maxZoom: 15.5,
      pitch: state.representation === "columns" ? 60 : 0, bearing: state.representation === "columns" ? -25 : 0,
      linear: true, duration: initial || motionHeld ? 0 : 650 });
    fittedZoom = Math.min(15.5, map.getZoom()); framed = true;
  }
  function apply(initial = false) {
    if (!map || !data || !state.dataset || !styleReady || failed || disposed) return;
    try {
      const metadata = buildNeon3DMapData(data, state.mode, state.scale).metadata;
      if (!metadata.eligible_cells && state.representation === "columns") throw new Error("No eligible columns");
      const activeMap = map;
      applyNeonMapOverlay(activeMap, data, state.mode, 1, { representation: state.representation, verticalExaggeration: state.scale });
      if (failed || disposed || map !== activeMap) return;
      if (!framed) frame(true);
      if (failed || disposed || map !== activeMap) return;
      renderPending = true;
      publish({ metadata, phase: "rendering", message: initial ? "Drawing the raised ground at 3×…" : "Updating the sampled landscape…" });
      if (renderTimer) clearTimeout(renderTimer);
      renderTimer = setTimeout(() => fail("The landscape did not finish drawing. Retry 3D or use the 2D Science inspector."), 20_000);
      map.triggerRepaint();
    } catch { fail("The 3D landscape could not be drawn. Retry, or inspect the same data in Terrain Science."); }
  }
  function onStyle() {
    if (!map || disposed || failed) return;
    try { map.setProjection({ type: "mercator" }); styleReady = true; framed = false; if (styleTimer) clearTimeout(styleTimer); styleTimer = null; apply(true); }
    catch { fail("The local map style could not start. Retry 3D or use Terrain Science."); }
  }
  function onRender() {
    if (!map || !renderPending || !framed || disposed || failed) return;
    try {
      const layer = map.getLayer(NEON_LOCAL_FILL);
      if (layer?.type !== (state.representation === "columns" ? "fill-extrusion" : "fill") || !map.isSourceLoaded(NEON_LOCAL_SOURCE)) return;
      // A loaded source alone is insufficient: at least one owned sample must be
      // present in the viewport after the pitched/framed camera has rendered.
      if (!map.queryRenderedFeatures({ layers: [NEON_LOCAL_FILL] }).some(feature => feature.source === NEON_LOCAL_SOURCE)) return;
      renderPending = false; if (renderTimer) clearTimeout(renderTimer); renderTimer = null;
      publish({ phase: "ready", message: state.representation === "columns" ? `3D sampled landscape · ${state.scale}× relative heights` : "2D sample footprints · source values unchanged" });
    } catch { fail("The rendered landscape could not be verified. Retry or open the Science inspector."); }
  }
  function onError() { fail("The local 3D renderer reported an error. Retry, or open the 2D Science inspector."); }
  function onContextLost(event: Event) { event.preventDefault(); fail("The 3D graphics context was lost. Retry 3D, or use the 2D Science inspector."); }
  function select(row: number, column: number, activeStop: string | null = null) {
    if (!state.dataset || disposed || failed) return;
    const probe = neonLidarProbe(state.dataset.receipt.preview, row, column);
    if (!probe) return;
    publish({ row: String(row + 1), column: String(column + 1), probe, activeStop });
  }
  function onPick(event: MapMouseEvent) {
    if (!map || state.phase !== "ready") return;
    try {
      const layers = [NEON_LOCAL_FILL, NEON_LOCAL_GROUND].filter(id => map?.getLayer(id));
      if (!layers.length) return;
      const feature = map.queryRenderedFeatures(event.point, { layers }).find(hit => hit.source === NEON_LOCAL_SOURCE);
      if (typeof feature?.properties?.row === "number" && typeof feature.properties.column === "number") select(feature.properties.row, feature.properties.column);
    } catch { fail("Sample picking is unavailable. Retry, or use the row and column inspector in Science."); }
  }
  async function start() {
    if (disposed) return;
    if (!runtime.webgl()) { publish({ phase: "unsupported", message: "This browser cannot start WebGL2. Use the 2D raster and data tools in Terrain Science." }); return; }
    // Both operations start once per live route attempt. A deferred start lets
    // a retired Strict Mode mount cancel before it acquires any resources.
    void runtime.readPilot(request.signal).then(receipt => {
      if (disposed || failed) return;
      const dataset = createNeonScienceDataset(receipt);
      if (!dataset) throw new Error("Invalid pilot receipt");
      data = buildNeonMapData(dataset.receipt.preview);
      if (!data || !neonMapBounds(dataset.receipt.preview)) throw new Error("Missing map georeferencing");
      const stops = buildNeonStoryStops(dataset.receipt.preview), first = stops.find(stop => stop.id === "high-ground") || stops[0];
      publish({ dataset, stops, row: first ? String(first.row + 1) : "", column: first ? String(first.column + 1) : "", probe: first?.probe ?? null, activeStop: first?.id ?? null });
      apply(true);
    }).catch(() => { if (!disposed && !failed) fail("The Konza Prairie dataset could not be loaded or validated. Retry, or open Terrain Science."); });
    styleTimer = setTimeout(() => fail("The local 3D map did not start. Retry, or use the 2D Science inspector."), 20_000);
    try {
      const lib = await runtime.loadMap();
      if (disposed || failed) return;
      lib.setWorkerUrl("/maplibre/maplibre-gl-worker.mjs");
      const budget = runtime.budget();
      map = new lib.Map({ container, style: TERRAIN_LOCAL_STYLE, center: [-98.3, 38.5], zoom: 5, pitch: 60, bearing: -25,
        maxPitch: 60, minZoom: 10, maxZoom: 18, renderWorldCopies: false, attributionControl: { compact: true },
        pixelRatio: budget.pixelRatio, maxTileCacheSize: Math.min(32, budget.tileCache) });
      map.on("style.load", onStyle); map.on("render", onRender); map.on("error", onError); map.on("click", onPick);
      map.getCanvas().setAttribute("aria-label", "Konza sampled terrain. Arrow keys pan; plus and minus zoom. Use visible surface, scale, story and sample controls for a keyboard alternative.");
      map.getCanvas().addEventListener("webglcontextlost", onContextLost);
      unobserve = runtime.observe(container, () => { if (!disposed && !failed) { try { map?.resize(); } catch { fail("The map could not resize. Retry 3D."); } } });
    } catch { fail("The 3D map could not start. Retry, or use the 2D Science inspector."); }
  }
  runtime.defer(() => { void start(); });
  return {
    getState: () => state,
    setReducedMotion(value: boolean) { motionHeld = value; },
    setMode(mode: NeonLidarMode) { if (!["dtm", "dsm", "chm"].includes(mode) || failed || disposed) return; publish({ mode, activeStop: null }); apply(); },
    setScale(scale: number) { if (!Number.isFinite(scale) || scale < 1 || scale > 5 || failed || disposed) return; publish({ scale }); apply(); },
    fit() { try { frame(); } catch { fail("The tile could not be framed. Enlarge the view and retry 3D."); } },
    show3D() { if (failed || disposed) return; publish({ representation: "columns" }); framed = false; apply(); },
    show2D() { if (failed || disposed) return; publish({ representation: "flat" }); framed = false; apply(); },
    turn(direction: number) { if (!map || failed || disposed || !Number.isFinite(direction)) return; try { map.easeTo({ bearing: map.getBearing() + Math.max(-45, Math.min(45, direction)), duration: motionHeld ? 0 : 250 }); } catch { fail("The map camera could not rotate. Retry 3D."); } },
    focus(id: string) {
      const stop = state.stops.find(item => item.id === id);
      if (!map || !stop || failed || disposed) return;
      publish({ mode: stop.mode }); select(stop.row, stop.column, stop.id); apply();
      if (stop.display_center) try { map.easeTo({ center: stop.display_center, zoom: Math.min(fittedZoom, map.getZoom()), pitch: state.representation === "columns" ? 60 : 0, duration: motionHeld ? 0 : 450 }); } catch { fail("The sampled location could not be framed. Retry 3D."); }
    },
    setCoordinate(axis: "row" | "column", value: string) {
      if (!state.dataset || failed || disposed || state[axis] === value) return;
      const drafts = { row: state.row, column: state.column, [axis]: value }, grid = state.dataset.receipt.preview.grid;
      const row = draftNumber(drafts.row, grid.height), column = draftNumber(drafts.column, grid.width);
      publish({ ...drafts, probe: row === null || column === null ? null : neonLidarProbe(state.dataset.receipt.preview, row, column), activeStop: null });
    },
    dispose() { if (disposed) return; disposed = true; request.abort(); clearTimers(); teardown(); },
  };
}
export type TerrainController = ReturnType<typeof createTerrainController>;
