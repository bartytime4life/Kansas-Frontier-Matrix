import type { Map as MapLibreMap } from "./maplibre-seam";
import type { MapKey } from "./map-keys";

/** Display context through the existing Observatory proxy, never occurrence coordinates. */
export const FLORA_FIRST_YEAR = 1995;
export const FLORA_LAST_YEAR = 2025;
export const FLORA_YEARS = Object.freeze(Array.from({ length: FLORA_LAST_YEAR - FLORA_FIRST_YEAR + 1 }, (_, i) => FLORA_LAST_YEAR - i));
export const FLORA_DEFAULT_YEAR = 2021;
export const FLORA_SOURCE_PREFIX = "tool-flora-records-";
export const floraSourceId = (year: number, revision = 0) => `${FLORA_SOURCE_PREFIX}${year}-${revision}`;
export const floraTileUrl = (year: number): string => {
  if (!Number.isInteger(year) || year < FLORA_FIRST_YEAR || year > FLORA_LAST_YEAR) throw new Error("Unsupported plant-record year");
  return `/api/event-atlas/tile?kind=flora&date=${year}-01-01&z={z}&x={x}&y={y}`;
};
export type FloraTileState = "loading" | "settled" | "failed";
export const floraReading = (year: number, state: FloraTileState) => state === "failed"
  ? `GBIF ${year} could not be loaded. Plant records are hidden; retry to request this year again.`
  : state === "loading" ? `Requesting GBIF plant-record tiles for ${year}…`
    : `GBIF ${year} tile requests settled. Blank hexagons do not establish plant absence; coverage and collecting effort vary.`;

export function floraKey(year: number): MapKey {
  return { id: "flora-records", title: `Plant records · ${year}`, items: [{ label: "GBIF record-density shading", color: "#68ab5f", shape: "area" }],
    note: "Provider-rendered Plantae records in coarse hexagons, source zoom ≤6. Shading depends on the provider's scale; it is not a count legend or a measure of abundance. Includes specimens and observations; no exact sites or KFM EvidenceBundle." };
}

/** One dated source at a time. Changing years removes the old image before requesting the new one. */
export function syncFloraContext(map: MapLibreMap, year: number | null, opacity = 0.75, revision = 0): void {
  const id = year === null ? null : floraSourceId(year, revision);
  const tiles = year === null ? null : floraTileUrl(year);
  for (const layer of map.getStyle().layers ?? []) {
    if (layer.id.startsWith(FLORA_SOURCE_PREFIX) && layer.id !== id) map.removeLayer(layer.id);
  }
  for (const source of Object.keys(map.getStyle().sources ?? {})) {
    if (source.startsWith(FLORA_SOURCE_PREFIX) && source !== id) map.removeSource(source);
  }
  if (id === null || tiles === null) return;
  if (!map.getSource(id)) map.addSource(id, { type: "raster", tiles: [tiles], tileSize: 512, minzoom: 0, maxzoom: 6,
    bounds: [-102.1, 36.9, -94.5, 40.1], attribution: "GBIF occurrence contributors · Plantae · annual generalized records" });
  const alpha = Number.isFinite(opacity) ? Math.max(0, Math.min(1, opacity)) : 0.75;
  const before = map.getStyle().layers?.find(layer => layer.type === "symbol")?.id;
  if (!map.getLayer(id)) map.addLayer({ id, type: "raster", source: id, paint: { "raster-opacity": alpha, "raster-resampling": "nearest", "raster-fade-duration": 0 } }, before);
  else map.setPaintProperty(id, "raster-opacity", alpha);
  placeFloraContext(map, id);
}

function placeFloraContext(map: MapLibreMap, id: string): void {
  const layers = map.getStyle().layers ?? [];
  const index = layers.findIndex(layer => layer.id === id);
  const cover = layers.findLastIndex(layer => ["tool-nlcd-land-cover-raster", "tool-usda-cdl-raster"].includes(layer.id));
  if (index >= 0 && cover > index) map.moveLayer(id, layers[cover + 1]?.id);
}

/** Observe only this generation. A failed tile hides the whole aggregate until explicit retry. */
export function watchFloraContext(map: MapLibreMap, year: number | null, revision: number,
  opacity: () => number, onState: (state: FloraTileState) => void): () => void {
  if (year === null) { syncFloraContext(map, null); return () => {}; }
  const id = floraSourceId(year, revision);
  let failed = false, disposed = false;
  const sync = () => {
    try {
      syncFloraContext(map, year, opacity(), revision);
      if (failed && map.getLayer(id)) map.setLayoutProperty(id, "visibility", "none");
    } catch { /* styledata retries once the replacement style is ready */ }
  };
  const restore = () => {
    if (disposed || !map.isStyleLoaded()) return;
    if (!map.getSource(id)) { if (!failed) onState("loading"); sync(); }
    else placeFloraContext(map, id);
  };
  const loaded = (event: { sourceId?: string; isSourceLoaded?: boolean }) => {
    if (!disposed && event.sourceId === id && !failed) onState(event.isSourceLoaded ? "settled" : "loading");
  };
  const error = (event: unknown) => {
    if (disposed || (event as { sourceId?: string })?.sourceId !== id) return;
    failed = true;
    onState("failed");
    if (map.getLayer(id)) map.setLayoutProperty(id, "visibility", "none");
  };
  onState("loading");
  map.on("sourcedata", loaded); map.on("error", error); map.on("styledata", restore);
  sync();
  return () => { disposed = true; map.off("sourcedata", loaded); map.off("error", error); map.off("styledata", restore); };
}
