# 🧩 Layer Type Contracts (`web/src/layers/types/`)

![TypeScript](https://img.shields.io/badge/TypeScript-Strict-informational?logo=typescript&logoColor=white)
![React](https://img.shields.io/badge/React-UI-informational?logo=react&logoColor=white)
![MapLibre](https://img.shields.io/badge/MapLibre-2D%20Maps-informational)
![Cesium](https://img.shields.io/badge/Cesium-3D%20Globe-informational)
![KFM](https://img.shields.io/badge/KFM-Contract--First%20%26%20Evidence--First-success)

> **Purpose:** This folder defines the **canonical TypeScript contracts** for “layers” in the KFM web app — what a layer *is*, how it’s referenced, how it’s rendered (2D/3D), and how it stays **traceable, governable, and safe**.

---

## 🎯 Why this folder exists

KFM’s UI is intentionally “thin” — it should never invent data, bypass governance, or hardcode mystery sources. Layer definitions are therefore treated as a **contract boundary** between:

- 🌐 **Governed backend distributions** (tiles / geojson / assets)
- 🧠 **Cataloged metadata** (STAC / DCAT) + lineage (PROV)
- 🗺️ **Map runtimes** (MapLibre 2D + Cesium 3D)
- 🧭 **User controls** (layer toggles, legend, info panels, popups)

This folder is where we make those expectations *compile-time enforceable*.

> [!IMPORTANT]
> **If you can’t express a layer safely in types, we don’t ship it.**  
> Types are the first line of defense for provenance, redaction, and predictable rendering.

---

## 🧠 Mental model (KFM “pipeline ordering” reflected in UI types)

KFM enforces an “evidence-first” chain:

`ETL → Catalogs (STAC/DCAT/PROV) → Graph → API → UI`

In the web app, **layers are UI representations of cataloged + governed evidence**.

So a layer type should answer, in a structured way:

- **What is it?** (kind / geometry / semantics)
- **Where does it come from?** (dataset ref / license / provenance)
- **How is it delivered?** (tiles / geojson / imagery / 3D tiles)
- **How is it rendered?** (style, legend, min/max zoom, filters)
- **What are the constraints?** (sensitivity, redaction, access rules)

---

## ✅ What belongs in `types/` (and what doesn’t)

### ✅ Belongs here
- 🧾 `LayerSpec` / `LayerConfig` contracts (discriminated unions)
- 🔗 Catalog references (dataset IDs, STAC/DCAT pointers, PROV lineage hooks)
- 🧱 Source contracts (tile templates, TileJSON, GeoJSON endpoints)
- 🎨 Style contracts (MapLibre-friendly, Cesium-friendly)
- 🔒 Sensitivity & redaction *descriptors* (not enforcement logic)
- 🧪 Runtime validation schemas **if** we validate external JSON (recommended)

### ❌ Does **not** belong here
- ❌ MapLibre/Cesium runtime code (no `new maplibregl.Map()` here)
- ❌ Fetching data directly (no `fetch()` / API calls here)
- ❌ UI components (controls, panels, widgets)
- ❌ Business logic (policy decisions, RBAC checks)
- ❌ “Magic defaults” that hide risk (prefer explicit fields)

---

## 🗂️ Recommended file layout (typical)

> Your repo may vary — but keep the intent: **stable types, discoverable contracts**.

```text
📁 web/src/layers/
  📁 types/                 👈 you are here
    ├─ README.md
    ├─ layerKind.ts
    ├─ layerSpec.ts
    ├─ layerSource.ts
    ├─ layerStyle.ts
    ├─ layerLegend.ts
    ├─ layerProvenance.ts
    ├─ layerSensitivity.ts
    └─ index.ts
```

---

## 🧱 Core design rules (non-negotiables)

### 1) 🔖 Discriminated unions over “optional soup”
Every layer must have a `kind` (or `type`) that selects a precise shape:

- ✅ `kind: "vector_tile"` → requires vector tile source + vector styling
- ✅ `kind: "raster_tile"` → requires raster tile source + raster styling
- ✅ `kind: "geojson"` → requires GeoJSON source + feature styling
- ✅ `kind: "image_overlay"` → requires image bounds + attribution
- ✅ `kind: "tileset_3d"` → requires 3D tileset source + Cesium options

This prevents the slow death of “one mega interface with 60 optional fields”.

### 2) 🧾 Provenance is a first-class field, not a comment
If a layer appears in the UI, it must be able to point to:

- 📌 a **dataset identity** (catalog ID)
- 📌 a **distribution** (how it’s served)
- 📌 a **license/attribution**
- 📌 optional **lineage** references (PROV activity / derivation)

### 3) 🔒 Sensitivity is explicit
Sensitive layers must be describable in a way the rest of the app can enforce:

- zoom ceilings
- generalized geometry requirements
- “no precise coordinates” rules
- access gating metadata

> [!NOTE]
> Enforcement usually lives elsewhere, but **types must make enforcement possible**.

### 4) 🧭 “One fact, one place”
If multiple layers reference the same dataset, they should reference the **same canonical dataset ID** — no copies, no divergent duplicates.

---

## 🧬 Canonical type shapes (reference)

> These are *illustrative* — align names with your existing codebase.  
> The key is the **contract structure**, not the exact identifiers.

### 🏷️ Layer kind

```ts
export type LayerKind =
  | "vector_tile"
  | "raster_tile"
  | "geojson"
  | "image_overlay"
  | "tileset_3d"
  | "terrain";
```

### 🧱 Shared base

```ts
export interface LayerBase {
  /** Stable ID: used in registries, URLs, telemetry, story references */
  id: string;

  /** Discriminant for the union */
  kind: LayerKind;

  /** UI labels */
  title: string;
  description?: string;

  /** Layer list organization */
  group?: string;        // e.g., "Base", "Hydrology", "Treaties", "Infrastructure"
  tags?: string[];       // searchable keywords
  icon?: string;         // if you use an icon system

  /** Visibility & ordering */
  defaultVisible?: boolean;
  zIndex?: number;

  /** View constraints */
  minZoom?: number;
  maxZoom?: number;
  opacity?: number;

  /** UI affordances */
  legend?: LayerLegendSpec;
  infoPanel?: LayerInfoSpec;

  /** Provenance & governance hooks */
  provenance: LayerProvenanceRef;
  sensitivity?: LayerSensitivitySpec;
}
```

---

## 🔗 Provenance contracts

Layers should be able to link to catalog metadata, and show it in a popup/legend/info panel.

```ts
export interface LayerProvenanceRef {
  /** Canonical dataset ID (DCAT dataset ID, or KFM dataset key) */
  datasetId: string;

  /** Optional pointers for spatial assets */
  stac?: {
    collectionId?: string;
    itemIds?: string[];
  };

  /** Optional lineage pointers */
  prov?: {
    activityId?: string;    // how it was produced
    derivedFrom?: string[]; // parent dataset IDs
  };

  /** Attribution + licensing (surface in UI) */
  license?: string;
  attribution?: string;

  /** Human-friendly external source link if appropriate */
  sourceUrl?: string;

  /** For layer freshness badges / tooltips */
  updatedAt?: string; // ISO 8601
}
```

> [!TIP]
> If a layer is derived (AI/analysis), include `prov.activityId` and `prov.derivedFrom` so Focus Mode + Story Nodes can trace it cleanly.

---

## 🧊 Tile sources (vector + raster)

KFM commonly serves tiles as:
- Vector tiles: `{z}/{x}/{y}.pbf` (MVT)
- Raster tiles: `{z}/{x}/{y}.png` or `.webp`

Your types should encode the template **and** how the app is allowed to build it (prefer API-provided TileJSON when possible).

```ts
export type TileScheme = "xyz";

export interface TileSourceBase {
  scheme: TileScheme; // z/x/y
  tileSize?: 256 | 512;

  /**
   * Prefer TileJSON endpoints when available.
   * If templates are used, they should be API-governed and not random third-party URLs.
   */
  tileJsonUrl?: string;
  urlTemplate?: string; // e.g. "/tiles/historic_trails/{z}/{x}/{y}.pbf"
}
```

---

## 🗺️ Layer variants

### 🧭 Vector tile layer (MapLibre)

```ts
export interface VectorTileLayerSpec extends LayerBase {
  kind: "vector_tile";
  source: TileSourceBase & { format: "pbf" };

  /**
   * Style can be a thin wrapper around MapLibre style fragments,
   * or a safer internal subset (recommended).
   */
  style: MapLibreVectorStyleSpec;

  /** If your tiles have multiple source-layers */
  sourceLayer?: string;

  /** Optional feature identity config for popups */
  featureId?: string;
}
```

### 🛰️ Raster tile layer (MapLibre + Cesium imagery)

```ts
export interface RasterTileLayerSpec extends LayerBase {
  kind: "raster_tile";
  source: TileSourceBase & { format: "png" | "webp" };
  style?: MapLibreRasterStyleSpec;

  /** In 3D mode, you may map this to a Cesium ImageryProvider */
  cesium?: CesiumImagerySpec;
}
```

### 🧾 GeoJSON overlay (small payloads only)

```ts
export interface GeoJsonLayerSpec extends LayerBase {
  kind: "geojson";
  source: {
    url: string;                 // governed API endpoint preferred
    format: "geojson";
    /** Optional caching semantics */
    cacheTtlSeconds?: number;
  };
  style: MapLibreVectorStyleSpec;
}
```

> [!WARNING]
> **GeoJSON is for small/interactive overlays.**  
> If it’s “big Kansas data”, it probably wants tiles.

### 🖼️ Image overlay (georeferenced)

```ts
export interface ImageOverlayLayerSpec extends LayerBase {
  kind: "image_overlay";
  source: {
    imageUrl: string;
    /** [west, south, east, north] in WGS84 */
    bounds: [number, number, number, number];
  };
  /** Optional opacity override for imagery */
  opacity?: number;
}
```

### 🌍 3D tileset layer (Cesium)

```ts
export interface Tileset3DLayerSpec extends LayerBase {
  kind: "tileset_3d";
  source: {
    tilesetUrl: string; // 3D Tiles tileset.json
  };
  cesium: {
    maximumScreenSpaceError?: number;
    enableShadows?: boolean;
  };
}
```

### 🧩 Union export

```ts
export type LayerSpec =
  | VectorTileLayerSpec
  | RasterTileLayerSpec
  | GeoJsonLayerSpec
  | ImageOverlayLayerSpec
  | Tileset3DLayerSpec;
```

---

## 🧾 Legend + Info panel contracts (minimum viable)

Layers should have enough structure to produce **consistent, accessible UI**.

```ts
export interface LayerLegendSpec {
  title?: string;
  items: Array<{
    label: string;
    /** Optional: icon key, swatch descriptor, line style descriptor, etc. */
    symbol?: Record<string, unknown>;
    description?: string;
  }>;
}

export interface LayerInfoSpec {
  /** Short text shown in info drawer/popup */
  summary?: string;

  /** Optional “learn more” links */
  links?: Array<{ label: string; href: string }>;

  /** Optional disclosure text for uncertainty / caveats */
  caveats?: string[];
}
```

> [!NOTE]
> “Legend exists” is not enough — **legend must be renderable** and not just a screenshot.

---

## 🔒 Sensitivity & redaction descriptors

This is where we encode “this layer can’t be shown at parcel-level” type rules.

```ts
export type Sensitivity =
  | "public"
  | "restricted"
  | "confidential"
  | "sacred_or_culturally_sensitive";

export interface LayerSensitivitySpec {
  classification: Sensitivity;

  /** Prevent “zooming past” redaction */
  maxSafeZoom?: number;

  /** UI messaging requirements */
  disclosureRequired?: boolean;
  disclosureText?: string;

  /**
   * Redaction expectation for geometry:
   * - "none": no redaction
   * - "coarsen": generalize geometry
   * - "hide": hide entirely for some users
   */
  redaction?: "none" | "coarsen" | "hide";

  /** CARE / sovereignty reminder hook */
  careNotes?: string;
}
```

---

## 🧪 Runtime validation (recommended for registry-driven layers)

If layer configs are loaded from JSON (registry file, API response, CMS, etc.), pair TypeScript with runtime validation:

- ✅ prevents “undefined in production” styling failures
- ✅ catches schema drift earlier
- ✅ allows safe upgrades / deprecations

Recommended approach:
- `zod` schemas that mirror `LayerSpec`
- a `parseLayerSpec()` helper that fails closed

---

## 🧭 Adding a new layer (the safe, KFM-compliant path)

When adding a new layer, treat it like a **public interface**:

1. 🧾 **Ensure the dataset exists in the catalogs**
   - STAC/DCAT published (and PROV if derived)
2. 🧠 **Ensure the API exposes a governed distribution**
   - Tiles (vector/raster) or controlled data endpoint
3. 🧩 **Express the layer as a typed `LayerSpec`**
   - pick the correct `kind`
   - include `provenance.datasetId`
   - include `sensitivity` if needed
4. 🗺️ **Add it to the layer registry**
   - must render with a legend + info content
5. 🧪 **Add tests**
   - compile-time checks
   - runtime schema validation tests if registry is JSON
6. ♿ **Accessibility + disclosure**
   - layer title/description meaningful
   - disclosures surfaced when required

> [!IMPORTANT]
> If you need a new *kind* (not just a new instance), update:
> - this folder’s union + schemas
> - registry tooling
> - rendering adapters (MapLibre/Cesium)
> - legend/info panel mapping

---

## ✅ Definition of Done (DoD) for any new layer instance

- [ ] `LayerSpec` compiles and is discriminated correctly
- [ ] `provenance.datasetId` is present and valid
- [ ] License/attribution can be surfaced in UI
- [ ] Legend renders (not “TODO: later”)
- [ ] Sensitive layers have explicit `LayerSensitivitySpec`
- [ ] Works in 2D (MapLibre) and has a 3D story (Cesium) if applicable
- [ ] No direct DB/graph calls from UI (API boundary respected)
- [ ] No bypass of redaction via zoom/popup/details
- [ ] Registry validation passes (if runtime schemas exist)

---

## 🧰 Practical tips (so types stay healthy)

- 🧊 Prefer **small, composable interfaces** over one mega-interface
- 🧷 Treat `id` as a stable contract — changing it is a breaking change
- 🧭 Keep `LayerSpec` “data-only” (serializable) when possible
- 🧼 Avoid importing heavy runtime libs just for types (use `import type`)
- 🧱 Add `Deprecated*` types when migrating — don’t break the world in one PR

---

## 🧷 Glossary

- **DCAT**: Dataset catalog metadata (discoverability)
- **STAC**: Spatiotemporal asset indexing (spatial/time-bound assets)
- **PROV**: Lineage (how the dataset/evidence was produced)
- **MVT / PBF**: Vector tiles (Mapbox Vector Tile format, `.pbf`)
- **XYZ**: Tile addressing scheme `/{z}/{x}/{y}`
- **Redaction**: Rules that prevent exposing sensitive detail in UI

---

## 🔚 Summary

This folder is the **type-level contract** that keeps KFM’s map layers:

- ✅ discoverable (catalog IDs)
- ✅ governable (sensitivity descriptors)
- ✅ renderable (explicit source + style)
- ✅ portable (2D/3D capable)
- ✅ auditable (provenance-first)