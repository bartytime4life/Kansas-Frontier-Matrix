import type { FeatureCollection } from "geojson";
import type { GeoJSONSource, Map as MapLibreMap } from "./maplibre-seam";
import type { ArchivePayload } from "./daily-archive";
const empty: FeatureCollection = { type: "FeatureCollection", features: [] };
/** Existing GeoJSON sources accept updates while a previous worker update is
 * pending. Waiting for isStyleLoaded() can lose a date/source change. */
export function applyArchiveMapData(map: Pick<MapLibreMap, "getSource">, payload: ArchivePayload | null, counties: FeatureCollection | null) {
  (map.getSource("capture") as GeoJSONSource | undefined)?.setData(payload?.data ?? empty);
  (map.getSource("counties") as GeoJSONSource | undefined)?.setData(counties ?? empty);
}
