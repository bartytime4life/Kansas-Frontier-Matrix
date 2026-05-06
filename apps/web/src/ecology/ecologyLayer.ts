import type { EcologyLayerManifest } from "./layerManifest";

export const ECOLOGY_SOURCE_ID = "kfm-ecology-timeslice-source";
export const ECOLOGY_LAYER_ID = "kfm-ecology-timeslice-layer";

export function buildEcologyVectorSource(manifest: EcologyLayerManifest) {
  return {
    type: "vector" as const,
    tiles: [manifest.tiles_url],
    minzoom: manifest.minzoom,
    maxzoom: manifest.maxzoom
  };
}

export function buildEcologyFillLayer(manifest: EcologyLayerManifest) {
  return {
    id: ECOLOGY_LAYER_ID,
    type: "fill" as const,
    source: ECOLOGY_SOURCE_ID,
    "source-layer": manifest.source_layer,
    minzoom: manifest.minzoom,
    maxzoom: manifest.maxzoom,
    paint: {
      "fill-opacity": 0.55
    },
    metadata: {
      "kfm:layer_id": manifest.layer_id,
      "kfm:evidence_bundle_ref": manifest.evidence_bundle_ref,
      "kfm:promotion_decision_ref": manifest.promotion_decision_ref,
      "kfm:run_receipt_ref": manifest.run_receipt_ref,
      "kfm:allowed_fields": manifest.allowed_fields,
      "kfm:public_safe": manifest.public_safe
    }
  };
}
