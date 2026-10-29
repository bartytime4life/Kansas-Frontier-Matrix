import { AIRSPACE_GROUPS, AVIATION_CONTEXT_ASSET, airspaceFeatures, aviationEditionStatus, parseAviationContext, type AirspaceGroup, type AviationContext } from '../aviation-airspace';
import { ALL_ALTITUDES, sliceCollection } from '../aviation-chart';
import type { Map as MapLibreMap } from '../maplibre-seam';

/** One optional, same-origin NASR snapshot. No weather, traffic, TFR or grid polling. */
export async function readWelcomeAviation(signal: AbortSignal): Promise<AviationContext> {
  const response = await fetch(AVIATION_CONTEXT_ASSET.url, { signal, cache: 'force-cache', redirect: 'error' });
  if (!response.ok || !response.body) throw new Error('Aviation reference unavailable');
  const declared = Number(response.headers.get('content-length'));
  if (Number.isFinite(declared) && declared > AVIATION_CONTEXT_ASSET.maxBytes) {
    await response.body.cancel(); throw new Error('Aviation reference exceeded its bound');
  }
  const reader = response.body.getReader(), chunks: Uint8Array[] = [];
  let size = 0;
  const abort = () => { void reader.cancel().catch(() => undefined); };
  signal.addEventListener('abort', abort, { once: true });
  try {
    while (true) {
      signal.throwIfAborted();
      const chunk = await reader.read();
      signal.throwIfAborted();
      if (chunk.done) break;
      size += chunk.value.byteLength;
      if (size > AVIATION_CONTEXT_ASSET.maxBytes) throw new Error('Aviation reference exceeded its bound');
      chunks.push(chunk.value);
    }
    const bytes = new Uint8Array(size); let offset = 0;
    for (const chunk of chunks) { bytes.set(chunk, offset); offset += chunk.byteLength; }
    const digest = Array.from(new Uint8Array(await crypto.subtle.digest('SHA-256', bytes)), byte => byte.toString(16).padStart(2, '0')).join('');
    signal.throwIfAborted();
    if (digest !== AVIATION_CONTEXT_ASSET.sha256) throw new Error('Aviation reference integrity failed');
    return parseAviationContext(JSON.parse(new TextDecoder('utf-8', { fatal: true }).decode(bytes)) as unknown);
  } catch (error) { void reader.cancel().catch(() => undefined); throw error; }
  finally { signal.removeEventListener('abort', abort); reader.releaseLock(); }
}

export type AviationPreviewMode = '3d' | '2d' | 'slice';
const PREFIX = 'welcome-aviation';
const SOURCES = [`${PREFIX}-zones`];
const LAYERS = ['zones-flat', 'zones-3d', 'zones-edge', 'zones-label'].map(id => `${PREFIX}-${id}`);
const GROUPS = new Set((Object.keys(AIRSPACE_GROUPS) as AirspaceGroup[]).filter(id => AIRSPACE_GROUPS[id].defaultOn));

/** Zones-only welcome hint. The full Aviation layer retains its other features. */
export function createWelcomeAviation(map: MapLibreMap, changed: () => void) {
  let context: AviationContext | null = null, pending = false, failed = false, renderFailed = false, disposed = false;
  let abort: AbortController | null = null, collections: ReturnType<typeof build> | null = null, drawnMode: AviationPreviewMode | null = null;
  const build = (value: AviationContext) => ({ zones: airspaceFeatures(value, GROUPS, 1) });
  const hide = () => { for (const id of LAYERS) if (map.getLayer(id)) map.setLayoutProperty(id, 'visibility', 'none'); };
  const remove = () => {
    for (const id of [...LAYERS].reverse()) if (map.getLayer(id)) map.removeLayer(id);
    for (const id of SOURCES) if (map.getSource(id)) map.removeSource(id);
    drawnMode = null;
  };
  return {
    prepare() {
      if (disposed || context || pending) return;
      failed = false; pending = true; abort = new AbortController();
      const signal = AbortSignal.any([abort.signal, AbortSignal.timeout(12_000)]);
      void readWelcomeAviation(signal).then(value => {
        if (disposed) return;
        collections = build(value); context = value; pending = false; changed();
      }).catch(() => { if (!disposed) { pending = false; failed = true; changed(); } });
    },
    status(visible = true) {
      return { state: !visible ? 'hidden' : failed || renderFailed ? 'unavailable' : context ? 'ready' : 'loading',
        ...(context ? { edition: aviationEditionStatus(context, Date.now()), cycle: context.nasrCycle,
          volumes: context.volumes.length } : {}) };
    },
    render(visible: boolean, mode: AviationPreviewMode) {
      if (disposed) return;
      const font = ['Noto Sans Regular'];
      try {
        if (!visible || !collections) { hide(); return; }
        if (!map.getSource(`${PREFIX}-zones`)) {
          remove();
          map.addSource(`${PREFIX}-zones`, { type: 'geojson', data: collections.zones });
          map.addLayer({ id: `${PREFIX}-zones-flat`, type: 'fill', source: `${PREFIX}-zones`, paint: { 'fill-color': ['get', 'color'], 'fill-opacity': .14 } });
          map.addLayer({ id: `${PREFIX}-zones-3d`, type: 'fill-extrusion', source: `${PREFIX}-zones`, paint: { 'fill-extrusion-color': ['get', 'color'], 'fill-extrusion-base': ['get', 'base'], 'fill-extrusion-height': ['get', 'top'], 'fill-extrusion-opacity': .35 } });
          map.addLayer({ id: `${PREFIX}-zones-edge`, type: 'line', source: `${PREFIX}-zones`, paint: { 'line-color': ['get', 'color'], 'line-width': 2, 'line-dasharray': ['match', ['get', 'type'], ['CLASS_D', 'CLASS_E2', 'CLASS_E3', 'CLASS_E4'], ['literal', [3, 2]], ['literal', [1, 0]]] } });
          map.addLayer({ id: `${PREFIX}-zones-label`, type: 'symbol', source: `${PREFIX}-zones`, minzoom: 7.5, layout: { 'text-font': font, 'text-field': ['get', 'label'], 'text-size': 11, 'symbol-placement': 'line', 'symbol-spacing': 420, 'text-optional': true }, paint: { 'text-color': ['get', 'color'], 'text-halo-color': '#fff', 'text-halo-width': 1.4 } });
        }
        if (drawnMode !== mode) {
          const zones = sliceCollection(collections.zones, mode === 'slice' ? { kind: 'msl', ft: 4000 } : ALL_ALTITUDES, 1, () => 0);
          (map.getSource(`${PREFIX}-zones`) as unknown as { setData(data: GeoJSON.FeatureCollection): void }).setData(zones);
          map.setLayoutProperty(`${PREFIX}-zones-label`, 'text-field', ['get', mode === '3d' ? 'label' : 'chart']);
          drawnMode = mode;
        }
        for (const id of LAYERS) map.setLayoutProperty(id, 'visibility', 'visible');
        map.setLayoutProperty(`${PREFIX}-zones-flat`, 'visibility', mode === '3d' ? 'none' : 'visible');
        map.setLayoutProperty(`${PREFIX}-zones-3d`, 'visibility', mode === '3d' ? 'visible' : 'none');
        renderFailed = false;
      } catch { renderFailed = true; try { remove(); } catch { /* style teardown */ } }
    },
    dispose() { disposed = true; abort?.abort(); context = null; collections = null; try { remove(); } catch { /* map teardown */ } },
  };
}
