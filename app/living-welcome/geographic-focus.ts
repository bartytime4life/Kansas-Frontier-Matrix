import type { Map as MapLibreMap } from '../maplibre-seam';
import type { OfficialContextPayload } from '../live-context';

const ID = 'welcome-census-record-focus';
const LAYERS = [`${ID}-glow`, `${ID}-line`, `${ID}-label`];

/** Highlight the actual source geometry and attributes, never a drawn substitute. */
export function syncGeographicFocus(map: MapLibreMap, topic: string | null, shown: boolean, counties?: OfficialContextPayload) {
  const feature = topic === 'evidence' && shown
    ? counties?.data.features.find(item => item.properties?.geoid === '20177') : null;
  if (!feature) {
    for (const id of [...LAYERS].reverse()) if (map.getLayer(id)) map.removeLayer(id);
    if (map.getSource(ID)) map.removeSource(ID);
    return;
  }
  if (!map.getSource(ID)) map.addSource(ID, { type: 'geojson', data: { type: 'FeatureCollection', features: [feature] } });
  // No artificial extrusion, estimated population, sample sites or time series.
  if (!map.getLayer(LAYERS[0])) map.addLayer({ id: LAYERS[0], type: 'line', source: ID,
    paint: { 'line-color': '#167e93', 'line-width': 10, 'line-opacity': 0.22, 'line-blur': 5 } });
  if (!map.getLayer(LAYERS[1])) map.addLayer({ id: LAYERS[1], type: 'line', source: ID,
    paint: { 'line-color': '#08768d', 'line-width': 2.5, 'line-opacity': 0.95 } });
  if (!map.getLayer(LAYERS[2])) map.addLayer({ id: LAYERS[2], type: 'symbol', source: ID,
    layout: { 'text-field': ['concat', ['get', 'name'], ' County\n', ['number-format', ['get', 'population'], { 'max-fraction-digits': 0 }], ' people · Census 2020'],
      'text-font': ['Noto Sans Regular'], 'text-size': 14, 'text-line-height': 1.5, 'text-max-width': 22 },
    paint: { 'text-color': '#074552', 'text-halo-color': '#fff', 'text-halo-width': 2 } });
}
