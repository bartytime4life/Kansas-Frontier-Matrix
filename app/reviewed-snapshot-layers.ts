import type { FeatureCollection } from "geojson";
import type { LayerSpecification, Map as MapLibreMap } from "./maplibre-seam";
import { dischargeRadius, earthquakeColor, earthquakeRadius, GAUGE_APPROVED_RING, GAUGE_FILL_COLOR, GAUGE_PROVISIONAL_RING, nwsSeverityColor } from "./map-keys";

/**
 * How a reviewed snapshot from the site database is drawn (see
 * reviewed-snapshots.ts): alert areas by NWS severity, gauges with circle area
 * in proportion to discharge, earthquakes by magnitude as the live catalog
 * draws them. The context renderer applies it on every pass,
 * so a style reload keeps it.
 */
export const REVIEWED_SOURCE_ID = "external-reviewed-snapshot";
export const REVIEWED_LAYER_IDS = Object.freeze(["external-reviewed-snapshot-areas", "external-reviewed-snapshot-edges", "external-reviewed-snapshot-gauges", "external-reviewed-snapshot-earthquakes",
  "external-reviewed-snapshot-selected-area", "external-reviewed-snapshot-selected-point"]);
/** Each drawn feature carries its release feature id here, so a click and the highlight agree on it. */
export const REVIEWED_FEATURE_ID = "kfmFeatureId";
const SELECTED_COLOR = "#ffe9a8";
const selectedFilter = (id: string | null) => ["==", ["get", REVIEWED_FEATURE_ID], id ?? ""] as const;
/** NWS severity, strongest first, with the colour each alert area takes. */
// Alert areas take the same severity palette as the live alerts (map-keys.ts).
export { NWS_SEVERITY_COLORS } from "./map-keys";
const severityColor = nwsSeverityColor();
// Circle area grows with discharge: radius by the square root of the value, from a floor (map-keys.ts, which the dock keys).

export const reviewedLayers = (): LayerSpecification[] => [
  { id: REVIEWED_LAYER_IDS[0], type: "fill", source: REVIEWED_SOURCE_ID, filter: ["==", ["geometry-type"], "Polygon"], paint: { "fill-color": severityColor, "fill-opacity": 0.32 } },
  { id: REVIEWED_LAYER_IDS[1], type: "line", source: REVIEWED_SOURCE_ID, filter: ["==", ["geometry-type"], "Polygon"], paint: { "line-color": severityColor, "line-width": 1.6 } },
  { id: REVIEWED_LAYER_IDS[2], type: "circle", source: REVIEWED_SOURCE_ID, filter: ["all", ["==", ["geometry-type"], "Point"], ["==", ["typeof", ["get", "value"]], "number"]], paint: {
    "circle-radius": dischargeRadius(), "circle-color": GAUGE_FILL_COLOR, "circle-opacity": 0.72,
    // Provisional USGS values carry an amber ring; approved values a white one.
    "circle-stroke-color": ["case", ["==", ["get", "provisional"], true], GAUGE_PROVISIONAL_RING, GAUGE_APPROVED_RING], "circle-stroke-width": 1.5,
  } },
  // Released earthquakes carry an event page; the same amber/white ring tells an automatic USGS solution from a reviewed one.
  { id: REVIEWED_LAYER_IDS[3], type: "circle", source: REVIEWED_SOURCE_ID, filter: ["all", ["==", ["geometry-type"], "Point"], ["has", "eventUrl"]], layout: { "circle-sort-key": ["coalesce", ["get", "magnitude"], 0] }, paint: {
    "circle-radius": earthquakeRadius(), "circle-color": earthquakeColor(), "circle-opacity": 0.85,
    "circle-stroke-color": ["case", ["==", ["get", "status"], "reviewed"], GAUGE_APPROVED_RING, GAUGE_PROVISIONAL_RING], "circle-stroke-width": 1.4,
  } },
  // The feature selected in the dock: a pale outline for an alert area, a halo for a gauge or an earthquake.
  { id: REVIEWED_LAYER_IDS[4], type: "line", source: REVIEWED_SOURCE_ID, filter: ["all", ["==", ["geometry-type"], "Polygon"], selectedFilter(null)] as never, paint: { "line-color": SELECTED_COLOR, "line-width": 3.4 } },
  { id: REVIEWED_LAYER_IDS[5], type: "circle", source: REVIEWED_SOURCE_ID, filter: ["all", ["==", ["geometry-type"], "Point"], selectedFilter(null)] as never, paint: {
    "circle-color": "rgba(0,0,0,0)", "circle-radius": 15, "circle-stroke-color": SELECTED_COLOR, "circle-stroke-width": 2.4,
  } },
];

const drawn = new WeakMap<MapLibreMap, Readonly<{ data: FeatureCollection | null; selected: string | null }>>();
const tagged = new WeakMap<FeatureCollection, FeatureCollection>();
/** The release data with each feature's id copied into its properties (computed once per release). */
export function taggedSnapshot(data: FeatureCollection): FeatureCollection {
  let copy = tagged.get(data);
  if (!copy) {
    copy = { type: "FeatureCollection", features: data.features.map(feature => ({ ...feature, properties: { ...feature.properties, [REVIEWED_FEATURE_ID]: String(feature.id ?? "") } })) };
    tagged.set(data, copy);
  }
  return copy;
}
/** The snapshot this map draws (null draws none) and the feature selected in it; the context renderer applies both on each pass. */
export const setReviewedSnapshot = (map: MapLibreMap, data: FeatureCollection | null, selected: string | null = null): void => { drawn.set(map, { data, selected }); };
export function drawReviewedSnapshot(map: MapLibreMap): void {
  const state = drawn.get(map), data = state?.data ? taggedSnapshot(state.data) : null;
  const source = map.getSource(REVIEWED_SOURCE_ID) as { setData?: (value: FeatureCollection) => void } | undefined;
  if (!data) {
    for (const id of REVIEWED_LAYER_IDS) if (map.getLayer(id)) map.setLayoutProperty(id, "visibility", "none");
    return;
  }
  if (source?.setData) source.setData(data);
  else map.addSource(REVIEWED_SOURCE_ID, { type: "geojson", data });
  for (const layer of reviewedLayers()) {
    if (!map.getLayer(layer.id)) map.addLayer(layer);
    map.setLayoutProperty(layer.id, "visibility", "visible");
  }
  map.setFilter(REVIEWED_LAYER_IDS[4], ["all", ["==", ["geometry-type"], "Polygon"], selectedFilter(state?.selected ?? null)] as never);
  map.setFilter(REVIEWED_LAYER_IDS[5], ["all", ["==", ["geometry-type"], "Point"], selectedFilter(state?.selected ?? null)] as never);
}
