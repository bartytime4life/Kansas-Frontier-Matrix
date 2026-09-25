import type { LayerRecord } from "./explorer-data";

// Preserve the provider's exact role label. A synthetic aggregate must never
// silently become an observed or authoritative aggregate in this catalog.
export function catalogSourceRoles(layers: readonly LayerRecord[]): string[] {
  return [...new Set(layers.flatMap((layer) => layer.data.features.map((feature) => feature.properties.sourceRole.trim())).filter(Boolean))]
    .sort((a, b) => a.localeCompare(b));
}

export function layerHasSourceRole(layer: LayerRecord, role: string): boolean {
  return role === "ALL" || layer.data.features.some((feature) => feature.properties.sourceRole.trim() === role);
}
