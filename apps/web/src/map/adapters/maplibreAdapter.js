export function toMaplibreLayerDescriptor(layerBinding) {
  return {
    id: layerBinding.id,
    type: layerBinding.type,
    source: layerBinding.source,
    paint: layerBinding.paint ?? {},
    layout: layerBinding.layout ?? {}
  };
}
