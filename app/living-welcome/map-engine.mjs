// The welcome's background map: one non-interactive MapLibre map that shows
// the real map each topic opens with. Loaded after the welcome has painted.
import { loadMapLibre } from '../maplibre-seam';
import { BASEMAPS } from '../map-runtime';
import { basemapCacheRequest } from '../basemap-cache';
import { browserRenderBudget } from '../map-performance';
import { webgl2Available } from '../webgl-support';
import { applyOfficialContextState, clearNoaaSatelliteFrame, defaultOfficialContextOpacity, OFFICIAL_CONTEXT_BY_ID, OFFICIAL_CONTEXT_SOURCES, setNoaaRadarObservationTime, setNoaaSatelliteFrame } from '../live-context';
import { isNoaaRadarManifest, NOAA_RADAR_FRAME_API_PATH, noaaRadarManifestIsFresh } from '../noaa-radar';
import { isNoaaSatelliteManifest, NOAA_SATELLITE_FRAMES_PATH, NOAA_SATELLITE_FRESH_AGE_MS } from '../noaa-satellite';
import { setPopulationPrisms } from '../population-prisms';
import { WELCOME_IDLE_VIEW, welcomeDriftLeg, welcomeStyle, welcomeView } from '../welcome-map-view';

const WORKER_URL = '/maplibre/maplibre-gl-worker.mjs';
// Pointer sweeps across the cards should not restyle the map for every card passed.
export const SETTLE_MS = 220;

// A style document by URL (the standard OpenFreeMap style) or as given.
const styleDocuments = new Map();
function resolveStyle(style) {
  if (typeof style !== 'string') return Promise.resolve(style);
  if (!styleDocuments.has(style)) styleDocuments.set(style, fetch(style, { signal: AbortSignal.timeout(15_000) }).then(response => {
    if (!response.ok) throw new Error('Style unavailable');
    return response.json();
  }).catch(error => { styleDocuments.delete(style); throw error; }));
  return styleDocuments.get(style);
}

// Starter data the Explorer reads as GeoJSON comes from the same fixed
// adapters; the payload is shared between previews for a few minutes.
const PAYLOAD_TTL_MS = 5 * 60_000;
const payloads = new Map();
function loadPayload(feed) {
  const cached = payloads.get(feed);
  if (cached && Date.now() - cached.at < PAYLOAD_TTL_MS) return cached.promise;
  const promise = fetch(OFFICIAL_CONTEXT_BY_ID[feed].apiPath, { signal: AbortSignal.timeout(12_000) }).then(response => response.ok ? response.json() : Promise.reject(new Error('Feed unavailable')))
    .then(body => {
      if (body?.feed !== feed || body.data?.type !== 'FeatureCollection' || !Array.isArray(body.data.features)) throw new Error('Unexpected feed payload');
      return body;
    });
  payloads.set(feed, { at: Date.now(), promise });
  promise.catch(() => { if (payloads.get(feed)?.promise === promise) payloads.delete(feed); });
  return promise;
}
// Radar shows its newest advertised scan, and only while that scan is current
// (the Explorer's own freshness rule); otherwise the preview shows no radar.
// The rule is applied again on every draw, and a selected radar preview is
// re-checked every minute (a new frame list every two), so a scan that ages
// past the rule leaves the map and the caption.
const RADAR_TTL_MS = 2 * 60_000;
export const RADAR_RECHECK_MS = 60_000;
const radarCurrent = at => Boolean(at) && noaaRadarManifestIsFresh({ frames: [at] }, Date.now());
let radarFrame = null;
function loadRadarFrame() {
  if (radarFrame && Date.now() - radarFrame.at < RADAR_TTL_MS) return radarFrame.promise;
  const promise = fetch(NOAA_RADAR_FRAME_API_PATH, { signal: AbortSignal.timeout(12_000) }).then(response => response.ok ? response.json() : null)
    .then(manifest => isNoaaRadarManifest(manifest) && noaaRadarManifestIsFresh(manifest, Date.now()) ? manifest.frames.at(-1) : null, () => null);
  radarFrame = { at: Date.now(), promise };
  return promise;
}
const readsPayload = id => { const source = OFFICIAL_CONTEXT_BY_ID[id]; return Boolean(source?.apiPath && source.kind.endsWith('GEOJSON')); };
const satelliteCurrent = frame => {
  const age = Date.now() - Date.parse(frame?.observedAt);
  return Number.isFinite(age) && age >= -5 * 60_000 && age <= NOAA_SATELLITE_FRESH_AGE_MS;
};
let satelliteFrame = null;
function loadSatelliteFrame() {
  if (satelliteFrame && Date.now() - satelliteFrame.at < RADAR_TTL_MS) return satelliteFrame.promise;
  const promise = fetch(NOAA_SATELLITE_FRAMES_PATH, { signal: AbortSignal.timeout(12_000) }).then(response => response.ok ? response.json() : null)
    .then(manifest => isNoaaSatelliteManifest(manifest) && satelliteCurrent(manifest.frames.at(-1)) ? manifest.frames.at(-1) : null, () => null);
  satelliteFrame = { at: Date.now(), promise };
  return promise;
}

export async function createWelcomeMap(container, { onReady, onError, onRadar, onSources } = {}) {
  if (!webgl2Available()) { onError?.(); return null; }
  const lib = await loadMapLibre();
  lib.setWorkerUrl(WORKER_URL);
  const budget = browserRenderBudget();
  let map;
  try {
    map = new lib.Map({
      container, interactive: false, transformRequest: basemapCacheRequest, attributionControl: { compact: true },
      style: { version: 8, sources: {}, layers: [] }, center: WELCOME_IDLE_VIEW.camera.center, zoom: WELCOME_IDLE_VIEW.camera.zoom,
      // A hover preview needs fewer retained tiles than an investigation map.
      // Keep the chosen pixel density so cartographic labels remain readable.
      pixelRatio: budget.pixelRatio, maxTileCacheSize: Math.min(budget.tileCache, budget.efficient ? 24 : budget.coarsePointer ? 32 : 48), maxPitch: 72, renderWorldCopies: false, fadeDuration: 200,
    });
  } catch { onError?.(); return null; }
  map.getCanvas().setAttribute('aria-hidden', 'true');
  map.getCanvas().tabIndex = -1;
  // `styleKey` names the style applied or still pending (basemap and view); it
  // is tracked apart from the selected topic, because topics that share a
  // style (Science and Sky, or Evidence and the default map) take turns while
  // it loads, and the loaded style serves whichever of them is selected then.
  let view = null, styleKey = null, styleEpoch = 0, styleLoaded = false, contextLost = false, paused = true, reduced = false, leg = 0, settle = 0, disposed = false, ready = false, applying = false, transitioning = false;
  const cameraOf = ({ camera: { center, zoom, pitch, bearing } }) => ({ center: [center[0], center[1]], zoom, pitch, bearing });
  const drift = () => {
    if (disposed || paused || reduced || budget.efficient || applying || !view?.topic) return;
    const next = welcomeDriftLeg(view, leg++);
    map.easeTo({ bearing: next.bearing, zoom: next.zoom, duration: next.duration, easing: t => t * t * (3 - 2 * t), essential: true });
  };
  map.on('moveend', event => { transitioning = false; if (!event.originalEvent && !paused) drift(); });
  const suspend = () => {
    const finishTransition = transitioning;
    transitioning = false;
    map.stop();
    // Pausing a flight must still leave the selected category's intended view.
    // Drift can resume bearing/zoom, but cannot repair an interrupted center.
    if (finishTransition && styleLoaded && view) map.jumpTo(cameraOf(view));
  };
  // Reveal the first frame of the installed style. `loaded()` also waits for
  // optional provider/terrain sources, so one stalled source can hide an
  // otherwise usable map forever (especially in a still, reduced-motion view).
  // Renderer readiness does not attest to tile or observation availability;
  // those retain their independent source states below.
  map.on('render', () => { if (!ready && !disposed && styleLoaded) { contextLost = false; ready = true; onReady?.(); reportSources(); } });
  map.on('webglcontextlost', () => { if (!disposed) { contextLost = true; ready = false; onError?.(); reportSources(); } });
  // The selected topic's starter layers, drawn by the Explorer's own context
  // renderer with every other provider layer hidden. Re-run after each style
  // load (a new style drops them) and as each GeoJSON payload arrives.
  const opacity = defaultOfficialContextOpacity();
  let loaded = {}, radarAt = null, radarShown = null, satellite = null, layersVisible = true;
  const pending = new Set(), failures = new Set();
  const reportSources = () => onSources?.({ topic: view?.topic, mapState: contextLost ? 'unavailable' : styleLoaded ? 'ready' : 'loading', sources: (view?.starters ?? []).map(id => {
    const source = OFFICIAL_CONTEXT_BY_ID[id], count = loaded[id]?.data.features.length;
    const frame = id === 'nws-radar' ? radarCurrent(radarAt) && { observedAt: radarAt, kind: 'radar' }
      : id === 'noaa-goes-geocolor' ? satelliteCurrent(satellite) && satellite : null;
    const state = !layersVisible ? 'hidden' : (source?.minDisplayZoom ?? 0) > view.camera.zoom ? 'zoom-in' : pending.has(id) ? 'loading'
      : failures.has(id) ? 'unavailable' : id === 'nws-radar' || id === 'noaa-goes-geocolor' ? frame ? 'dated-frame' : 'unavailable'
      : readsPayload(id) ? count === undefined ? 'loading' : count ? 'records' : 'empty' : 'map-layer';
    return { id, label: source?.shortTitle ?? id, state, count, observedAt: frame?.observedAt ?? null, product: frame?.kind ?? null };
  }) });
  const drawData = () => {
    if (disposed || !styleLoaded || !view) return;
    const shown = new Set(layersVisible ? view.starters : []);
    const visibility = Object.fromEntries(OFFICIAL_CONTEXT_SOURCES.map(source => [source.id, shown.has(source.id)]));
    const radar = shown.has('nws-radar') && radarCurrent(radarAt) ? radarAt : null;
    visibility['nws-radar'] = Boolean(radar);
    // The generic renderer must never request an undated satellite raster.
    visibility['noaa-goes-geocolor'] = false;
    try {
      if (radar) setNoaaRadarObservationTime(map, radar);
      setPopulationPrisms(map, layersVisible && view.prisms);
      applyOfficialContextState(map, visibility, opacity, loaded);
      if (shown.has('noaa-goes-geocolor') && satelliteCurrent(satellite)) setNoaaSatelliteFrame(map, satellite, true, opacity['noaa-goes-geocolor']);
      else clearNoaaSatelliteFrame(map);
    } catch { /* Preview data is optional; the map stays. */ }
    // The caption names the radar scan only while one is drawn.
    if (radar !== radarShown) { radarShown = radar; onRadar?.(radar); }
    reportSources();
  };
  const refreshRadar = () => {
    if (pending.has('nws-radar')) return;
    pending.add('nws-radar');
    return loadRadarFrame().then(at => { if (disposed) return; pending.delete('nws-radar'); radarAt = at; if (view?.starters.includes('nws-radar')) drawData(); });
  };
  const refreshSatellite = () => {
    if (pending.has('noaa-goes-geocolor')) return;
    pending.add('noaa-goes-geocolor');
    return loadSatelliteFrame().then(frame => { if (disposed) return; pending.delete('noaa-goes-geocolor'); satellite = frame; if (view?.starters.includes('noaa-goes-geocolor')) drawData(); });
  };
  const radarTimer = setInterval(() => {
    if (disposed || !view) return;
    // Expire old frames even while held, but never poll a hidden/paused welcome.
    if (view.starters.some(id => id === 'nws-radar' || id === 'noaa-goes-geocolor')) drawData();
    if (layersVisible && !paused && !reduced) {
      if (view.starters.includes('nws-radar')) refreshRadar();
      if (view.starters.includes('noaa-goes-geocolor')) refreshSatellite();
    }
  }, RADAR_RECHECK_MS);
  const requestData = next => {
    if (!layersVisible) return;
    if (next.starters.includes('nws-radar')) refreshRadar();
    if (next.starters.includes('noaa-goes-geocolor')) refreshSatellite();
    for (const feed of next.starters.filter(readsPayload)) {
      if (loaded[feed] || pending.has(feed)) continue;
      pending.add(feed); failures.delete(feed);
      loadPayload(feed).then(payload => {
        if (disposed) return; pending.delete(feed); loaded = { ...loaded, [feed]: payload }; if (view?.starters.includes(feed)) drawData();
      }, () => { if (disposed) return; pending.delete(feed); failures.add(feed); if (view?.starters.includes(feed)) drawData(); });
    }
  };
  const apply = next => {
    if (disposed) return;
    view = next; leg = 0;
    requestData(next);
    const key = `${next.basemap}|${next.scene}`;
    // Stopping the last drift ends a move; it must not start one for the new view.
    applying = true; map.stop(); applying = false;
    if (key !== styleKey) {
      // A → B → A may reuse A's pending style promise. Only the latest
      // application owns it; otherwise both A callbacks rebuild the GPU style.
      const epoch = ++styleEpoch;
      styleKey = key; styleLoaded = false; ready = false;
      onSources?.({ topic: next.topic, mapState: 'loading', sources: [] });
      const failed = () => {
        if (disposed || styleEpoch !== epoch) return;
        styleKey = null; styleLoaded = false;
        onSources?.({ topic: view.topic, mapState: 'unavailable', sources: [] });
      };
      // Styles are resolved here rather than through setStyle's transformStyle,
      // which waits for the previous style to load and so stalls after one fails.
      const requestedStyle = BASEMAPS[next.basemap].style;
      void resolveStyle(requestedStyle).then(style => {
        if (disposed || styleEpoch !== epoch) return;
        try {
          map.setStyle(welcomeStyle(style, view), { diff: false });
          // Jumping ends a move, which starts the drift for the view selected now.
          map.once('style.load', () => { if (disposed || styleEpoch !== epoch) return; styleLoaded = true; drawData(); map.jumpTo(cameraOf(view)); });
        } catch {
          // A fetched document can parse as JSON yet be rejected by MapLibre.
          // A deliberate retry must re-read it rather than reuse that document.
          if (typeof requestedStyle === 'string') styleDocuments.delete(requestedStyle);
          failed();
        }
      }, failed);
    } else if (!styleLoaded) {
      // The pending style jumps to this view, and draws its data, when it loads.
    } else {
      drawData();
      if (paused || reduced || budget.efficient) map.jumpTo(cameraOf(next));
      else { transitioning = true; map.flyTo({ ...cameraOf(next), duration: 2200, essential: true }); }
    }
  };
  return {
    get view() { return view; },
    show(topic) {
      clearTimeout(settle);
      const next = welcomeView(topic);
      if (view && next.topic === view.topic && styleKey !== null) return;
      // The first view applies at once; later ones wait for the pointer to settle.
      if (!view) apply(next); else settle = setTimeout(() => apply(next), SETTLE_MS);
    },
    setPaused(value) { if (paused === value) return; paused = value; if (paused) suspend(); else drift(); },
    setReduced(value) { if (reduced === value) return; reduced = value; if (reduced) suspend(); else drift(); },
    setLayersVisible(value) {
      if (layersVisible === value) return;
      layersVisible = value;
      if (value && view) requestData(view);
      drawData();
    },
    dispose() { disposed = true; clearTimeout(settle); clearInterval(radarTimer); try { map.remove(); } catch { /* Already removed. */ } },
  };
}
