import type { ErrorEvent as MapErrorEvent, Map as MapLibreMap } from '../maplibre-seam';
import type { WelcomeScientificLayer } from '../welcome-map-view';
import { LAND_COVER_SOURCE_ID, syncLandCover } from '../land-cover';
import { CDL_LATEST_YEAR, CDL_SOURCE_ID, syncCropland } from '../cropland';
import { setDaylightMapLayer } from '../map-runtime';

const LABELS: Record<WelcomeScientificLayer, string> = {
  'land-cover': 'USGS NLCD 2021 · land cover · 30 m',
  cropland: `USDA NASS CDL ${CDL_LATEST_YEAR} · crop classes · 30 m`,
  daylight: 'Calculated daylight + twilight',
};
const RASTER_SOURCES: Partial<Record<WelcomeScientificLayer, string>> = {
  'land-cover': LAND_COVER_SOURCE_ID,
  cropland: CDL_SOURCE_ID,
};
type State = 'loading' | 'map-layer' | 'calculated' | 'unavailable';

/** Existing scientific renderers, owned only by the welcome's one map. */
export function createWelcomeScientificLayers(map: MapLibreMap, changed: () => void) {
  let selected: readonly WelcomeScientificLayer[] = [], visible = true, instant: number | null = null;
  const states = new Map<WelcomeScientificLayer, State>();
  const content = new Set<WelcomeScientificLayer>();
  const sourceLayer = (sourceId: string | undefined) => selected.find(id => RASTER_SOURCES[id] === sourceId && sourceId !== undefined);
  const sourcedata = (event: { sourceId?: string; isSourceLoaded?: boolean; sourceDataType?: string }) => {
    const id = sourceLayer(event.sourceId);
    if (visible && id && event.sourceDataType === 'content') content.add(id);
    if (visible && id && content.has(id) && event.isSourceLoaded && states.get(id) === 'loading') {
      states.set(id, 'map-layer'); changed();
    }
  };
  const error = (event: MapErrorEvent) => {
    const detail = event as MapErrorEvent & { sourceId?: string; error: MapErrorEvent['error'] & { sourceId?: string } };
    const id = sourceLayer(detail.sourceId ?? detail.error?.sourceId);
    if (visible && id && states.get(id) !== 'unavailable') { states.set(id, 'unavailable'); changed(); }
  };
  map.on('sourcedata', sourcedata);
  map.on('error', error);
  return {
    sync(layers: readonly WelcomeScientificLayer[], show: boolean) {
      selected = layers; visible = show;
      for (const id of [...states.keys()]) if (!layers.includes(id)) { states.delete(id); content.delete(id); }
      for (const id of ['land-cover', 'cropland'] as const) {
        const on = show && layers.includes(id);
        const source = RASTER_SOURCES[id]!;
        if (on && !map.getSource(source)) { states.set(id, 'loading'); content.delete(id); }
        try {
          if (id === 'land-cover') syncLandCover(map, on);
          else syncCropland(map, on ? CDL_LATEST_YEAR : null);
        } catch { if (on) states.set(id, 'unavailable'); }
      }
      const solar = show && layers.includes('daylight');
      instant = solar ? Date.now() : null;
      const drawn = setDaylightMapLayer(map, solar, instant ?? Date.now());
      if (solar) states.set('daylight', drawn ? 'calculated' : 'unavailable');
    },
    status() {
      return selected.map(id => ({ id, label: LABELS[id], state: !visible ? 'hidden' : states.get(id) ?? 'loading',
        observedAt: id === 'daylight' && instant !== null ? new Date(instant).toISOString() : null,
        product: id === 'daylight' ? 'calculated' : 'classification' }));
    },
    dispose() { map.off('sourcedata', sourcedata); map.off('error', error); },
  };
}
