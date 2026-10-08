import { installMapProtocol, type Map as MapLibreMap, type MapLibreModule } from "./maplibre-seam";
import type { LocalReviewPackage } from "./local-geopdf-review";

export const LOCAL_REVIEW_SOURCE = "kfm-device-geopdf-source";
export const LOCAL_REVIEW_LAYER = "kfm-device-geopdf-raster";
export type ReviewMapState = "enabled" | "hidden" | "flat-map-required" | "unavailable";

/** Exact Web Mercator tile corners, not a catalog outline or PDF preview warp. */
export function reviewTileCorners(address: string): [[number, number], [number, number], [number, number], [number, number]] {
  const [z, x, y] = address.split("/").map(Number), n = 2 ** z;
  const lng = (v: number) => v / n * 360 - 180;
  const lat = (v: number) => Math.atan(Math.sinh(Math.PI * (1 - 2 * v / n))) * 180 / Math.PI;
  return [[lng(x), lat(y)], [lng(x + 1), lat(y)], [lng(x + 1), lat(y + 1)], [lng(x), lat(y + 1)]];
}

/** Bytes stay in memory; this protocol never calls fetch or exposes a server route. */
export function attachLocalReview(map: MapLibreMap, runtime: MapLibreModule, pack: LocalReviewPackage,
  flatMap: boolean, onState: (state: ReviewMapState) => void, identity = crypto.randomUUID()) {
  const protocol = `kfm-review-${identity}`;
  let disposed = false, visible = true, opacity = .65, failed = false;
  const sourceIds = [LOCAL_REVIEW_SOURCE], layerIds = [LOCAL_REVIEW_LAYER], urls: string[] = [];
  const remove = () => {
    for (const id of layerIds) try { if (map.getLayer(id)) map.removeLayer(id); } catch { /* Replaced style. */ }
    for (const id of sourceIds) try { if (map.getSource(id)) map.removeSource(id); } catch { /* Removed map. */ }
    for (const url of urls.splice(0)) URL.revokeObjectURL(url);
  };
  const update = () => {
    if (disposed) return;
    try {
      const flat = flatMap && map.getPitch() === 0 && !map.getTerrain() && map.getProjection()?.type === "mercator";
      const show = visible && flat && !failed;
      for (const id of layerIds) {
        map.setLayoutProperty(id, "visibility", show ? "visible" : "none");
        map.setPaintProperty(id, "raster-opacity", opacity);
      }
      onState(failed ? "unavailable" : !visible ? "hidden" : !flat ? "flat-map-required" : "enabled");
    } catch { failed = true; remove(); onState("unavailable"); }
  };
  const error = (event: unknown) => {
    if (event && typeof event === "object" && "sourceId" in event && sourceIds.includes(String(event.sourceId))) { failed = true; update(); }
  };
  installMapProtocol(runtime, protocol, async (params, abort) => {
    if (disposed || abort.signal.aborted) throw new DOMException("Review removed.", "AbortError");
    const address = params.url.slice(`${protocol}://`.length);
    const tile = params.url.startsWith(`${protocol}://`) && /^\d{1,2}\/\d{1,5}\/\d{1,5}\.png$/.test(address)
      ? pack.tiles.get(address.slice(0, -4)) : undefined;
    if (!tile) { failed = true; update(); throw new Error("Prepared tile unavailable; review overlay withheld."); }
    // MapLibre may transfer/detach the returned buffer. Preserve verified originals.
    return { data: tile.slice(0) };
  });
  try {
    const paint = { "raster-opacity": opacity, "raster-fade-duration": 0, "raster-resampling": "nearest" as const };
    const attribution = pack.attribution;
    // A raster source hides below minzoom. Reuse the four *actual* coarsest
    // georeferenced tiles as image quads at overview zooms, so Fit works on small
    // screens too. There is no generated mosaic, color interpolation or new data.
    const overviewMaxZoom = pack.minZoom - 1; // MapLibre camera uses 512px; tiles use 256px.
    for (const [address, bytes] of pack.tiles) if (address.startsWith(`${pack.minZoom}/`)) {
      const suffix = address.replaceAll("/", "-"), source = `${LOCAL_REVIEW_SOURCE}-${suffix}`, layer = `${LOCAL_REVIEW_LAYER}-${suffix}`;
      sourceIds.push(source); layerIds.push(layer);
      const url = URL.createObjectURL(new Blob([bytes], { type: "image/png" })); urls.push(url);
      map.addSource(source, { type: "image", url, coordinates: reviewTileCorners(address) });
      map.addLayer({ id: layer, type: "raster", source, maxzoom: overviewMaxZoom,
        layout: { visibility: "none" }, paint: { ...paint } });
    }
    map.addSource(LOCAL_REVIEW_SOURCE, { type: "raster", tiles: [`${protocol}://{z}/{x}/{y}.png`], tileSize: 256,
      bounds: pack.bounds, minzoom: pack.minZoom, maxzoom: pack.maxZoom, attribution });
    map.addLayer({ id: LOCAL_REVIEW_LAYER, type: "raster", source: LOCAL_REVIEW_SOURCE, minzoom: overviewMaxZoom,
      layout: { visibility: "none" }, paint: { ...paint } });
    map.on("move", update); map.on("error", error); update();
  } catch {
    disposed = true; map.off("move", update); map.off("error", error); remove(); runtime.removeProtocol(protocol); onState("unavailable");
  }
  return {
    setVisible(value: boolean) { visible = value; update(); },
    setOpacity(value: number) { opacity = Math.max(0, Math.min(1, Number.isFinite(value) ? value : .65)); update(); },
    dispose() {
      if (disposed) return;
      disposed = true; map.off("move", update); map.off("error", error); remove(); runtime.removeProtocol(protocol);
    },
  };
}
