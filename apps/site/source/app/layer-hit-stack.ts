// MapLibre already orders hits by rendered stacking order. Partition one query
// without letting a lower fire/registry layer steal input from a visible point.
export function layerHitStack<T extends { layer: { id: string }; source?: string }>(
  rendered: readonly T[], registryIds: readonly string[], officialIds: readonly string[],
) {
  const registry = new Set(registryIds), official = new Set(officialIds);
  const registryHits = rendered.filter(feature => registry.has(feature.layer.id));
  const officialHits = rendered.filter(feature => official.has(feature.layer.id));
  const first = rendered.find(feature => registry.has(feature.layer.id) || official.has(feature.layer.id));
  return { registryHits, officialHits, candidate: first && registry.has(first.layer.id) ? first : undefined,
    officialCandidate: first && official.has(first.layer.id) ? first : undefined };
}
