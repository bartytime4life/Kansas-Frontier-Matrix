import { basemapCacheRequest } from "./basemap-cache";
import { loadMapLibre, type Map as GLMap } from "./maplibre-seam";
import { canUpdateSurfaceCapture, sameSurfaceContent, surfaceRasterSampling, type SurfaceBounds, type SurfaceCapture } from "./selected-surface";

export type SurfaceDetailFrame = { image: HTMLCanvasElement; bounds: SurfaceBounds; zoom: number };
const mercator = (lat: number) => Math.log(Math.tan(Math.PI / 4 + lat * Math.PI / 360));
const latitude = (y: number) => (2 * Math.atan(Math.exp(y)) - Math.PI / 2) * 180 / Math.PI;

/** The requested pixels cover real geographic bounds, never an enlarged locator screenshot. */
export function surfaceRenderFrame(bounds: SurfaceBounds, pixels = 2048) {
  const x = (bounds[2] - bounds[0]) / 360, y = (mercator(bounds[3]) - mercator(bounds[1])) / (2 * Math.PI);
  const width = Math.max(64, Math.round(pixels * Math.min(1, x / y))), height = Math.max(64, Math.round(pixels * Math.min(1, y / x)));
  return { width, height, center: [(bounds[0] + bounds[2]) / 2, latitude((mercator(bounds[1]) + mercator(bounds[3])) / 2)] as [number, number], zoom: Math.min(22, Math.log2(Math.min(width / x, height / y) / 512)) };
}

/** Map surface coordinates are linear in Web Mercator, as is the recorded cutaway. */
export function detailBoundsFromSurface(area: SurfaceBounds, points: readonly { x: number; z: number }[]): SurfaceBounds | null {
  if (!points.length) return null;
  const span = (area[2] - area[0]) * Math.PI / 180, mid = (mercator(area[1]) + mercator(area[3])) / 2;
  const west = Math.max(area[0], area[0] + (Math.min(...points.map(p => p.x)) / 6 + .5) * (area[2] - area[0]));
  const east = Math.min(area[2], area[0] + (Math.max(...points.map(p => p.x)) / 6 + .5) * (area[2] - area[0]));
  const south = Math.max(area[1], latitude(mid - Math.max(...points.map(p => p.z)) / 6 * span));
  const north = Math.min(area[3], latitude(mid - Math.min(...points.map(p => p.z)) / 6 * span));
  return east > west && north > south ? [west, south, east, north] : null;
}

/** One bounded, disposable renderer. It refreshes visible detail during camera movement without starving tile requests. */
export function startCutawaySurfaceDetail(options: {
  capture: SurfaceCapture; pixels: number; onFrame: (frame: SurfaceDetailFrame) => void; onStatus: (status: string) => void;
}) {
  let disposed = false, map: GLMap | null = null, timer: ReturnType<typeof setTimeout> | undefined, timeout: ReturnType<typeof setTimeout> | undefined, previewTimer: ReturnType<typeof setTimeout> | undefined;
  let requested = options.capture.bounds, key = "", pending = true, partial = false, ready = false, displayedFrameComplete = false, refreshing = false;
  let capture = options.capture;
  const container = document.createElement("div");
  container.setAttribute("aria-hidden", "true"); container.style.cssText = "position:fixed;left:-10000px;top:0;pointer-events:none;contain:strict;";
  document.body.append(container);
  const apply = () => {
    if (disposed || !map || !ready) return;
    const next = requested.map(n => n.toFixed(6)).join(","); if (next === key) return; key = next;
    const frame = surfaceRenderFrame(requested, options.pixels);
    container.style.width = `${frame.width}px`; container.style.height = `${frame.height}px`;
    pending = true; clearTimeout(timeout);
    options.onStatus(`Loading surface detail · ${frame.width} × ${frame.height} pixels…${refreshing ? " Previous surface remains visible until a replacement is drawn." : ""}`);
    map.resize(); map.jumpTo({ center: frame.center, zoom: frame.zoom, bearing: 0, pitch: 0 }); map.triggerRepaint();
    timeout = setTimeout(() => { if (!disposed && pending) options.onStatus(refreshing ? "Surface refresh is incomplete. The previous surface remains visible; missing new tiles are unknown." : "Surface detail is incomplete. Missing tiles are unknown; move or retry the surface."); }, 12000);
  };
  options.onStatus("Preparing high-detail surface tiles…");
  timeout = setTimeout(() => { if (!disposed && pending) options.onStatus("Surface tiles are taking longer to load. Coverage is unconfirmed; retry or choose another basemap."); }, 12000);
  loadMapLibre().then(lib => {
    if (disposed) return;
    lib.setWorkerUrl("/maplibre/maplibre-gl-worker.mjs");
    const frame = surfaceRenderFrame(requested, options.pixels);
    container.style.width = `${frame.width}px`; container.style.height = `${frame.height}px`;
    const style = detailStyle();
    map = new lib.Map({ transformRequest: basemapCacheRequest, container, style, center: frame.center, zoom: frame.zoom, interactive: false, attributionControl: false,
      pixelRatio: 1, maxTileCacheSize: 96, fadeDuration: 0, renderWorldCopies: false, canvasContextAttributes: { preserveDrawingBuffer: true } });
    const view = map;
    view.on("styleimagemissing", event => { const image = capture.images.find(i => i.id === event.id); if (image && !view.hasImage(image.id)) view.addImage(image.id, image.data, { pixelRatio: image.pixelRatio, sdf: image.sdf }); });
    const styleReady = () => { if (disposed || ready) return; ready = true; for (const sample of surfaceRasterSampling(capture.style, false)) view.setPaintProperty(sample.id, "raster-resampling", sample.value); apply(); };
    view.on("style.load", styleReady); view.on("load", styleReady);
    view.on("error", () => { partial = true; if (!disposed) options.onStatus(refreshing ? "New surface tiles are unavailable. The previous surface remains visible; new blank patches are unknown." : "Some surface tiles are unavailable. Blank patches are unknown, not clear conditions."); });
    const copyFrame = (settled: boolean) => {
      if (disposed || !ready || !pending) return;
      if (refreshing && (!settled || partial)) {
        if (settled && partial) {
          pending = false; clearTimeout(timeout); clearTimeout(previewTimer); previewTimer = undefined;
          options.onStatus("New surface tiles are incomplete. The previous complete surface remains visible; retry the refresh.");
        }
        return;
      }
      try {
        const canvas = view.getCanvas(), image = document.createElement("canvas"); image.width = canvas.width; image.height = canvas.height;
        const context = image.getContext("2d"); if (!context) throw new Error("Surface copy unavailable");
        context.drawImage(canvas, 0, 0); context.getImageData(0, 0, 1, 1);
        const b = view.getBounds();
        if (settled) { pending = false; clearTimeout(timeout); clearTimeout(previewTimer); previewTimer = undefined; }
        options.onFrame({ image, bounds: [b.getWest(), b.getSouth(), b.getEast(), b.getNorth()], zoom: view.getZoom() });
        // A render preview or a settled frame with tile errors is visible, but
        // neither can be promised as a complete fallback for the next refresh.
        displayedFrameComplete = settled && !partial; refreshing = false;
        options.onStatus(`${!settled ? "Loading surface detail · partial preview" : partial ? "Partial surface detail" : "Surface detail ready"} · ${image.width} × ${image.height} pixels · map zoom ${view.getZoom().toFixed(1)}. Provider resolution and dates still apply.${!settled ? " Unfinished tiles are unknown." : ""}`);
      } catch { pending = false; options.onStatus("Surface detail could not be drawn. The selector preview and source records remain available."); }
    };
    // A slow optional overlay must not hold back already rendered basemap tiles.
    // Copy at most once per second during active loading; idle publishes the final frame.
    view.on("render", () => {
      if (!disposed && ready && pending && previewTimer === undefined) {
        // Capture in the render event: canvas pixels and geographic bounds share this frame.
        copyFrame(false); previewTimer = setTimeout(() => { previewTimer = undefined; }, 1000);
      }
    });
    view.on("idle", () => { if (view.areTilesLoaded()) copyFrame(true); });
  }).catch(() => { if (!disposed) options.onStatus("Surface detail is unavailable. Retry the surface or use the Surface map view."); });
  function detailStyle() {
    const style = JSON.parse(JSON.stringify(capture.style));
    for (const layer of style.layers) if (layer.type === "raster") layer.paint = { ...layer.paint, "raster-fade-duration": 0, "raster-resampling": "nearest" };
    return style;
  }
  return {
    updateCapture(next: SurfaceCapture) {
      if (disposed || !map || !ready) return false;
      if (sameSurfaceContent(capture, next)) return true;
      if (!canUpdateSurfaceCapture(capture, next)) return false;
      capture = next;
      // Errors describe one attempt; a later exact capture may recover. Keep
      // the last complete pixels until this attempt settles without new errors.
      pending = true; partial = false; refreshing = displayedFrameComplete; clearTimeout(timeout);
      options.onStatus("Updating surface layers… Loaded basemap tiles are retained; coverage is pending.");
      timeout = setTimeout(() => { if (!disposed && pending) options.onStatus("Surface layer update is incomplete. Existing pixels may show the prior layers; retry the surface."); }, 12000);
      // Diff applies exact paint, layer order, additions/removals and GeoJSON data.
      // Raster/vector sources, source clocks and image bytes must match first.
      try { map.setStyle(detailStyle(), { diff: true }); map.triggerRepaint(); }
      catch { return false; }
      return true;
    },
    refresh() {
      if (disposed || !map) return false;
      if (!ready) { options.onStatus("Surface tiles are already preparing. The current cutaway remains available."); return true; }
      clearTimeout(timer); timer = undefined; clearTimeout(timeout); clearTimeout(previewTimer); previewTimer = undefined;
      key = ""; pending = true; partial = false; ready = false; refreshing = displayedFrameComplete;
      options.onStatus(refreshing ? "Refreshing surface tiles… Previous surface remains visible until a replacement is drawn." : "Refreshing surface tiles… Existing preview may be incomplete; missing tiles are unknown.");
      timeout = setTimeout(() => { if (!disposed && pending) options.onStatus(refreshing ? "Surface refresh is taking longer. The previous surface remains visible; new coverage is unconfirmed." : "Surface tiles are taking longer to load. Coverage is unconfirmed; retry or choose another basemap."); }, 12000);
      try { map.setStyle(detailStyle(), { diff: false }); }
      catch {
        ready = true; pending = false; clearTimeout(timeout);
        options.onStatus(displayedFrameComplete ? "Surface refresh unavailable. The previous surface remains visible; retry or choose another basemap." : "Surface refresh unavailable. Existing preview may be incomplete; retry or choose another basemap.");
      }
      return true;
    },
    update(bounds: SurfaceBounds) { if(bounds.map(n=>n.toFixed(6)).join(",")===requested.map(n=>n.toFixed(6)).join(","))return; requested = bounds; if (timer === undefined) timer = setTimeout(() => { timer = undefined; apply(); }, 200); },
    dispose() { disposed = true; clearTimeout(timer); clearTimeout(timeout); clearTimeout(previewTimer); map?.remove(); container.remove(); },
  };
}
