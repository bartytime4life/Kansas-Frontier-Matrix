// The welcome's background map: one non-interactive MapLibre map that shows
// the real map each topic opens with. Loaded after the welcome has painted.
import { loadMapLibre } from '../maplibre-seam';
import { BASEMAPS } from '../map-runtime';
import { basemapCacheRequest } from '../basemap-cache';
import { browserRenderBudget } from '../map-performance';
import { webgl2Available } from '../webgl-support';
import { WELCOME_IDLE_VIEW, welcomeDriftLeg, welcomeStyle, welcomeView } from '../welcome-map-view';

const WORKER_URL = '/maplibre/maplibre-gl-worker.mjs';
// Pointer sweeps across the cards should not restyle the map for every card passed.
export const SETTLE_MS = 220;

// A style document by URL (the standard OpenFreeMap style) or as given.
const styleDocuments = new Map();
function resolveStyle(style) {
  if (typeof style !== 'string') return Promise.resolve(style);
  if (!styleDocuments.has(style)) styleDocuments.set(style, fetch(style).then(response => {
    if (!response.ok) throw new Error('Style unavailable');
    return response.json();
  }).catch(error => { styleDocuments.delete(style); throw error; }));
  return styleDocuments.get(style);
}

export async function createWelcomeMap(container, { onReady, onError } = {}) {
  if (!webgl2Available()) { onError?.(); return null; }
  const lib = await loadMapLibre();
  lib.setWorkerUrl(WORKER_URL);
  const budget = browserRenderBudget();
  let map;
  try {
    map = new lib.Map({
      container, interactive: false, transformRequest: basemapCacheRequest, attributionControl: { compact: true },
      style: { version: 8, sources: {}, layers: [] }, center: WELCOME_IDLE_VIEW.camera.center, zoom: WELCOME_IDLE_VIEW.camera.zoom,
      pixelRatio: budget.pixelRatio, maxTileCacheSize: budget.tileCache, maxPitch: 72, renderWorldCopies: false, fadeDuration: 200,
    });
  } catch { onError?.(); return null; }
  map.getCanvas().setAttribute('aria-hidden', 'true');
  map.getCanvas().tabIndex = -1;
  let view = null, basemap = null, paused = true, reduced = false, leg = 0, settle = 0, disposed = false, ready = false, applying = false;
  const drift = () => {
    if (disposed || paused || reduced || applying || !view) return;
    const next = welcomeDriftLeg(view, leg++);
    map.easeTo({ bearing: next.bearing, zoom: next.zoom, duration: next.duration, easing: t => t * t * (3 - 2 * t), essential: true });
  };
  map.on('moveend', event => { if (!event.originalEvent && !paused) drift(); });
  map.on('idle', () => { if (!ready && !disposed) { ready = true; onReady?.(); } });
  const apply = next => {
    if (disposed) return;
    const restyle = next.basemap !== basemap || next.scene !== view?.scene;
    view = next; leg = 0;
    const { center, zoom, pitch, bearing } = next.camera;
    const camera = { center: [center[0], center[1]], zoom, pitch, bearing };
    // Stopping the last drift ends a move; it must not start one for the new view.
    applying = true; map.stop(); applying = false;
    if (restyle) {
      basemap = next.basemap;
      // Styles are resolved here rather than through setStyle's transformStyle,
      // which waits for the previous style to load and so stalls after one fails.
      void resolveStyle(BASEMAPS[next.basemap].style).then(style => {
        if (disposed || view !== next) return;
        map.setStyle(welcomeStyle(style, next), { diff: false });
        // Jumping ends a move, which starts the drift for this view.
        map.once('style.load', () => { if (view === next) map.jumpTo(camera); });
      }, () => { if (view === next) basemap = null; });
    } else if (reduced || paused) map.jumpTo(camera);
    else map.flyTo({ ...camera, duration: 2200, essential: true });
  };
  return {
    get view() { return view; },
    show(topic) {
      clearTimeout(settle);
      const next = welcomeView(topic);
      if (view && next.topic === view.topic) return;
      // The first view applies at once; later ones wait for the pointer to settle.
      if (!view) apply(next); else settle = setTimeout(() => apply(next), SETTLE_MS);
    },
    setPaused(value) { if (paused === value) return; paused = value; if (paused) map.stop(); else drift(); },
    setReduced(value) { if (reduced === value) return; reduced = value; if (reduced) map.stop(); else drift(); },
    dispose() { disposed = true; clearTimeout(settle); try { map.remove(); } catch { /* Already removed. */ } },
  };
}
