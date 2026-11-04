import type { ErrorEvent as MapErrorEvent, Map as MapLibreMap } from '../maplibre-seam';
import type { WelcomeScientificLayer } from '../welcome-map-view';
import { LAND_COVER_SOURCE_ID, syncLandCover } from '../land-cover';
import { CDL_LATEST_YEAR, CDL_SOURCE_ID, syncCropland } from '../cropland';
import { setDaylightMapLayer } from '../map-runtime';

const LABELS: Record<WelcomeScientificLayer, string> = {
  'land-cover': 'USGS NLCD 2021 · land cover · 30 m',
  'animal-records': 'GBIF Animalia · 2025 · coarse occurrence records',
  cropland: `USDA NASS CDL ${CDL_LATEST_YEAR} · crop classes · 30 m`,
  daylight: 'Calculated daylight + twilight',
};
export const ANIMAL_RECORDS_SOURCE_ID = 'welcome-gbif-animal-records-2025';
export const ANIMAL_RECORDS_TILE_URL = '/api/event-atlas/tile?kind=fauna&date=2025-01-01&z={z}&x={x}&y={y}';
const RASTER_SOURCES: Partial<Record<WelcomeScientificLayer, string>> = {
  'land-cover': LAND_COVER_SOURCE_ID,
  'animal-records': ANIMAL_RECORDS_SOURCE_ID,
  cropland: CDL_SOURCE_ID,
};
type State = 'loading' | 'map-layer' | 'calculated' | 'unavailable';

/** The Observatory's existing aggregate carrier: never exact occurrence sites. */
function syncAnimalRecords(map: MapLibreMap, on: boolean) {
  const id = ANIMAL_RECORDS_SOURCE_ID;
  if (!on) {
    if (map.getLayer(id)) map.removeLayer(id);
    if (map.getSource(id)) map.removeSource(id);
    return;
  }
  if (!map.getSource(id)) map.addSource(id, { type: 'raster', tiles: [ANIMAL_RECORDS_TILE_URL], tileSize: 512, minzoom: 0, maxzoom: 6,
    bounds: [-102.1, 36.9, -94.5, 40.1], attribution: 'GBIF occurrence contributors · Animalia · 2025 generalized records' });
  if (!map.getLayer(id)) map.addLayer({ id, type: 'raster', source: id,
    paint: { 'raster-opacity': 0.52, 'raster-resampling': 'nearest', 'raster-fade-duration': 0 } }, map.getStyle().layers?.find(layer => layer.type === 'symbol')?.id);
}

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
    if (visible && id && states.get(id) !== 'unavailable') {
      states.set(id, 'unavailable');
      // An incomplete aggregate must not look like complete record coverage.
      if (id === 'animal-records' && map.getLayer(ANIMAL_RECORDS_SOURCE_ID)) map.setLayoutProperty(ANIMAL_RECORDS_SOURCE_ID, 'visibility', 'none');
      changed();
    }
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
      const animals = show && layers.includes('animal-records');
      if (animals && !map.getSource(ANIMAL_RECORDS_SOURCE_ID)) { states.set('animal-records', 'loading'); content.delete('animal-records'); }
      try { syncAnimalRecords(map, animals); } catch { if (animals) states.set('animal-records', 'unavailable'); }
      const solar = show && layers.includes('daylight');
      instant = solar ? Date.now() : null;
      const drawn = setDaylightMapLayer(map, solar, instant ?? Date.now());
      if (solar) states.set('daylight', drawn ? 'calculated' : 'unavailable');
    },
    status() {
      return selected.map(id => ({ id, label: LABELS[id], state: !visible ? 'hidden' : states.get(id) ?? 'loading',
        observedAt: id === 'daylight' && instant !== null ? new Date(instant).toISOString() : null,
        product: id === 'daylight' ? 'calculated' : id === 'animal-records' ? 'occurrence-records' : 'classification' }));
    },
    dispose() { map.off('sourcedata', sourcedata); map.off('error', error); },
  };
}
