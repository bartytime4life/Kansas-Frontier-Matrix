export type ReleaseLayer = {
  id: string;
  name?: string;
  source?: {
    kind?: string;
    [key: string]: unknown;
  };
  trust?: {
    derivation?: "derived" | "observed";
    precision?: "generalized" | "exact";
  };
  [key: string]: unknown;
};

export type ReleaseManifest = {
  layers?: ReleaseLayer[];
  [key: string]: unknown;
};

/**
 * Returns only release-safe layers that can be rendered in the public map.
 */
export function releaseRenderableLayers(manifest?: ReleaseManifest): ReleaseLayer[] {
  if (!manifest?.layers) return [];

  return manifest.layers.filter((layer) => {
    const sourceKind = String(layer.source?.kind ?? "").toLowerCase();
    const isReleaseSource = sourceKind === "released" || sourceKind === "release_manifest";
    const isGeneralized = (layer.trust?.precision ?? "generalized") === "generalized";

    // Public UI must never render exact-sensitive geometry in this path.
    return isReleaseSource && isGeneralized;
  });
}
