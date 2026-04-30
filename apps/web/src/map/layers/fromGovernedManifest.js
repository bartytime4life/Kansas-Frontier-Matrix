import { toMaplibreLayerDescriptor } from "../adapters/maplibreAdapter.js";

export function releasedLayerDescriptors(manifest) {
  return (manifest.layers ?? [])
    .filter((layer) => layer.source?.kind === "released")
    .map((layer) => toMaplibreLayerDescriptor(layer));
}
