export const ECOLOGY_SOURCE_ID = "kfm-ecology-timeslice-source";
export const ECOLOGY_LAYER_ID = "kfm-ecology-timeslice-layer";

export function buildEcologyVectorSource(tilesUrl: string) {
  return {
    type: "vector" as const,
    tiles: [tilesUrl],
    minzoom: 0,
    maxzoom: 14
  };
}

export function buildEcologyFillLayer() {
  return {
    id: ECOLOGY_LAYER_ID,
    type: "fill" as const,
    source: ECOLOGY_SOURCE_ID,
    "source-layer": "ecology",
    paint: {
      "fill-opacity": 0.55
    }
  };
}
