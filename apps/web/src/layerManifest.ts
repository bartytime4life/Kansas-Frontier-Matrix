// apps/web/src/layerManifest.ts
// KFM governed layer manifest client
// --------------------------------------------------
// This module is the ONLY allowed path for the web app
// to discover map layers. It enforces:
// - governed API usage
// - public-safe payloads
// - evidence linkage
// - rights + sensitivity awareness
// --------------------------------------------------

export type KfmRightsClass =
  | "public"
  | "open"
  | "controlled"
  | "restricted"
  | "unknown";

export type KfmSensitivityClass =
  | "public"
  | "generalize"
  | "restricted"
  | "review_required";

export type LayerManifestEntry = {
  // identity
  layer_id: string;

  // maplibre source definition
  source: {
    type: "vector" | "raster" | "raster-dem";
    url?: string; // e.g. pmtiles:// or tiles endpoint
    tiles?: string[];
    attribution?: string;
  };

  // optional style hints
  source_layer?: string;

  // zoom constraints
  minzoom?: number;
  maxzoom?: number;

  // governance
  evidence_ref: string;
  rights: KfmRightsClass;
  sensitivity: KfmSensitivityClass;

  // optional metadata
  title?: string;
  description?: string;

  // temporal context (optional but important for KFM)
  datetime?: string;
};

export type LayerManifestResponse = {
  schema_version: "v1";
  generated_at: string;
  layers: LayerManifestEntry[];
};

// --------------------------------------------------
// Errors
// --------------------------------------------------

export class LayerManifestError extends Error {
  constructor(message: string) {
    super(message);
    this.name = "LayerManifestError";
  }
}

// --------------------------------------------------
// Internal validation (fail-closed)
// --------------------------------------------------

function assertValidLayer(entry: LayerManifestEntry): void {
  if (!entry.layer_id) {
    throw new LayerManifestError("Layer missing layer_id");
  }

  if (!entry.source || !entry.source.type) {
    throw new LayerManifestError(
      `Layer ${entry.layer_id} missing source/type`
    );
  }

  if (!entry.evidence_ref) {
    throw new LayerManifestError(
      `Layer ${entry.layer_id} missing evidence_ref`
    );
  }

  if (!entry.rights) {
    throw new LayerManifestError(
      `Layer ${entry.layer_id} missing rights`
    );
  }

  if (!entry.sensitivity) {
    throw new LayerManifestError(
      `Layer ${entry.layer_id} missing sensitivity`
    );
  }

  // HARD RULE: never allow unknown rights into UI
  if (entry.rights === "unknown") {
    throw new LayerManifestError(
      `Layer ${entry.layer_id} has unknown rights (fail-closed)`
    );
  }

  // HARD RULE: restricted layers must not expose tiles directly
  if (
    entry.sensitivity === "restricted" &&
    (entry.source.url || entry.source.tiles)
  ) {
    throw new LayerManifestError(
      `Layer ${entry.layer_id} exposes tiles but is restricted`
    );
  }
}

function validateManifest(payload: LayerManifestResponse): void {
  if (!payload || payload.schema_version !== "v1") {
    throw new LayerManifestError("Invalid manifest schema_version");
  }

  if (!Array.isArray(payload.layers)) {
    throw new LayerManifestError("Manifest layers must be an array");
  }

  for (const layer of payload.layers) {
    assertValidLayer(layer);
  }
}

// --------------------------------------------------
// Fetch API
// --------------------------------------------------

export async function fetchLayerManifest(
  apiBase = "/api"
): Promise<LayerManifestResponse> {
  const res = await fetch(`${apiBase}/layers/manifest`, {
    method: "GET",
    headers: {
      "Accept": "application/json"
    }
  });

  if (!res.ok) {
    throw new LayerManifestError(
      `Failed to fetch layer manifest: ${res.status}`
    );
  }

  const payload = (await res.json()) as LayerManifestResponse;

  validateManifest(payload);

  return payload;
}

// --------------------------------------------------
// Convenience helpers
// --------------------------------------------------

export async function getLayerById(
  layerId: string,
  apiBase = "/api"
): Promise<LayerManifestEntry | null> {
  const manifest = await fetchLayerManifest(apiBase);

  return manifest.layers.find(l => l.layer_id === layerId) || null;
}

export async function listPublicLayers(
  apiBase = "/api"
): Promise<LayerManifestEntry[]> {
  const manifest = await fetchLayerManifest(apiBase);

  return manifest.layers.filter(
    l =>
      l.rights === "public" &&
      l.sensitivity !== "restricted"
  );
}

// --------------------------------------------------
// MapLibre integration helpers
// --------------------------------------------------

export function buildMapLibreSource(
  entry: LayerManifestEntry
): any {
  // NOTE: MapLibre expects a raw style spec object
  return {
    type: entry.source.type,
    url: entry.source.url,
    tiles: entry.source.tiles,
    attribution: entry.source.attribution
  };
}

export function buildDefaultLayer(
  entry: LayerManifestEntry
): any {
  // Minimal safe fallback styling
  return {
    id: entry.layer_id,
    type:
      entry.source.type === "raster"
        ? "raster"
        : "fill",
    source: entry.layer_id,
    "source-layer": entry.source_layer,
    paint:
      entry.source.type === "raster"
        ? {}
        : {
            "fill-color": "#3b82f6",
            "fill-opacity": 0.4
          }
  };
}

// --------------------------------------------------
// Evidence integration hook
// --------------------------------------------------

export function getEvidenceRef(
  entry: LayerManifestEntry
): string {
  return entry.evidence_ref;
}
