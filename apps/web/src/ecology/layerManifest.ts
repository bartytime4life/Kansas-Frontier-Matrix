export type EcologyLayerManifest = {
  schema_version: "v1";
  object_type: "EcologyLayerManifest";
  layer_id: string;
  title: string;
  description?: string;
  source_type: "vector" | "raster" | "raster-dem" | "geojson";
  tiles_url: string;
  source_layer: string;
  stac_catalog_ref: string;
  stac_collection_ref: string;
  stac_item_ref?: string;
  evidence_bundle_ref: string;
  promotion_decision_ref: string;
  run_receipt_ref: string;
  minzoom: number;
  maxzoom: number;
  bounds?: [number, number, number, number];
  time_start?: string;
  time_end?: string;
  allowed_fields: string[];
  public_safe: true;
  sensitivity?: "public" | "generalize";
  rights_status?: "public" | "open";
  policy_label?: string;
  limitations?: string[];
};

export async function fetchEcologyLayerManifest(
  id = "example-pass",
  apiBase = "/api"
): Promise<EcologyLayerManifest> {
  const response = await fetch(`${apiBase}/ecology/layers/${id}`);

  if (!response.ok) {
    throw new Error(`Failed to load ecology layer manifest: ${response.status}`);
  }

  const manifest = (await response.json()) as EcologyLayerManifest;

  if (manifest.object_type !== "EcologyLayerManifest") {
    throw new Error("Invalid ecology layer manifest response");
  }

  if (manifest.public_safe !== true) {
    throw new Error("Ecology layer manifest is not public-safe");
  }

  return manifest;
}
