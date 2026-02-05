<!-- According to a document from 2026-02-05 -->
# 🗺️ Layer Definitions (Registry + Contracts)

![Layers](https://img.shields.io/badge/layers-registry-blue)
![Provenance](https://img.shields.io/badge/provenance-required-success)
![Governance](https://img.shields.io/badge/governance-fail--closed-critical)
![MapLibre](https://img.shields.io/badge/2D-MapLibre-informational)
![Cesium](https://img.shields.io/badge/3D-Cesium-informational)

> **This folder is the single source of truth** for how datasets become **toggleable map layers** (2D/3D), with **legend + info + provenance hooks**.  
> If a layer can appear in the UI, it must be defined here — **no ad-hoc layers in components**.

---

## 🎯 Purpose

Layer definitions are **structured metadata + rendering instructions** that let the UI:

- Render layers in **2D** (MapLibre) and/or **3D** (Cesium)
- Fetch data via the **governed API** (tiles, GeoJSON, metadata)
- Populate **Layer Switcher / Legend / Info Panels**
- Enforce **access + redaction + sensitivity**
- Maintain the “**map behind the map**” principle: every layer points back to its dataset record & provenance

---

## 🧠 Design Goals

✅ **Registry-first**  
One canonical registry → consistent menus, legends, and story/focus integrations.

✅ **Contract-driven**  
Definitions are data. They should be **validatable** (schema/TS types) and **testable** (lint + unit tests).

✅ **Provenance-first**  
Every layer must include metadata pointers (dataset ID, license, attribution), so the UI can cite sources.

✅ **No leakage**  
A layer definition must never enable a UI path that bypasses server-side governance (zoom/filters/sensitive geometry).

✅ **Dual-renderer aware**  
A layer can be:
- **2D only**
- **3D only**
- **2D + 3D paired** (same dataset, different renderer config)

---

## 🗂️ What Belongs Here (and what doesn’t)

### ✅ Put here
- Layer registry entries (IDs, titles, groups, ordering)
- Data source config (tiles/GeoJSON endpoints, params, min/max zoom)
- Styling references (MapLibre layer paint/layout snippets or style hooks)
- Legend spec (labels, swatches, ranges, icons)
- Interaction rules (click/hover behavior, feature-info strategy)
- Time support (year/range fields, slider behavior)
- Governance labels (sensitivity, redaction behavior, auth hints)

### ❌ Do NOT put here
- Hardcoded datasets (GeoJSON blobs, large arrays)
- Direct DB logic, SQL strings beyond allowed client params
- UI component code (belongs in components/renderers)
- “Magic styling” spread around the app (keep styling in a dedicated style module and reference it here)

---

## 📁 Folder Anatomy (Suggested)

> Actual filenames may vary — **keep the pattern**: *small, composable, testable definitions*.

```text
📦 web/
 └─ 📦 src/
    └─ 📦 layers/
       ├─ 📦 definitions/             👈 YOU ARE HERE
       │  ├─ 📄 README.md
       │  ├─ 📄 index.ts              🧠 exports the registry
       │  ├─ 📦 groups/               🗂️ optional: group bundles
       │  ├─ 📦 base/                 🧱 basemaps / reference layers
       │  ├─ 📦 overlays/             🧭 thematic overlays
       │  ├─ 📦 time/                 🕰️ time-aware layers
       │  └─ 📦 _shared/              🧩 shared legend + helpers
       ├─ 📦 renderers/               🖼️ MapLibre/Cesium wiring
       ├─ 📦 styles/                  🎨 style fragments + helpers
       └─ 📦 utils/                   🧰 layer helpers, parsing, etc.
```

---

## 🔁 How Definitions Flow Through the App

```mermaid
flowchart LR
  A[📄 Layer Definitions] --> B[🧠 Layer Registry]
  B --> C[🗺️ MapLibre Renderer (2D)]
  B --> D[🌎 Cesium Renderer (3D)]
  B --> E[🧾 Legend & Layer Panel]
  B --> F[ℹ️ Layer Info / Provenance UI]
  C --> G[/tiles/{layer}/{z}/{x}/{y}.pbf or .png]
  C --> H[/api/v1/datasets/{id}/data?format=geojson]
  D --> I[3D tiles / terrain / imagery endpoints]
  F --> J[/api/v1/datasets/{id} (DCAT + links)]
```

---

## 🧬 Layer Definition Contract

> Think of a definition as: **UI metadata** + **data source** + **render rules** + **governance**.

### ✅ Minimum required fields (recommended)
| Field | Type | Why it exists |
|---|---|---|
| `id` | `string` | Stable identifier used across UI, stories, URLs, analytics |
| `title` | `string` | Human-friendly name |
| `summary` | `string` | Tooltip + layer picker description |
| `group` | `string` | Layer panel grouping (“Hydrology”, “Trails”, “Demography”, etc.) |
| `kind` | `"vector-tile" \| "raster-tile" \| "geojson" \| "3d-tiles" \| "terrain" \| ...` | Determines renderer behavior |
| `sources` | object | API endpoints + parameters |
| `legend` | object | How to explain symbology |
| `provenance` | object | Dataset IDs, license, attribution, citation hooks |
| `visibility` | object | Default on/off + zoom limits |
| `time` | object (optional) | Timeline integration |

---

## 🧱 Recommended TypeScript Interface (Example)

```ts
export type LayerKind =
  | "vector-tile"
  | "raster-tile"
  | "geojson"
  | "3d-tiles"
  | "terrain"
  | "imagery";

export type Sensitivity =
  | "public"
  | "limited"
  | "restricted"
  | "sacred_or_sensitive";

export interface LayerDefinition {
  /** Stable, kebab-case, never-reused */
  id: string;

  /** Human label shown in UI */
  title: string;

  /** Short description for tooltips + search */
  summary: string;

  /** UI group bucket (drives panel structure) */
  group: string;

  /** Rendering behavior */
  kind: LayerKind;

  /** Visibility + performance boundaries */
  visibility: {
    defaultVisible: boolean;
    minZoom?: number;
    maxZoom?: number;
    /** If true, UI should avoid loading unless explicitly enabled */
    optIn?: boolean;
  };

  /** Data sources served via governed API */
  sources: {
    /** Dataset ID in catalog (DCAT/STAC pointer) */
    datasetId: string;

    /** Tile endpoints (if used) */
    tiles?: {
      /** e.g., `/tiles/historic_trails/{z}/{x}/{y}.pbf` */
      urlTemplate: string;
      format: "mvt" | "png" | "webp";
      attribution?: string;
      maxzoom?: number;
    };

    /** GeoJSON endpoint (if used) */
    geojson?: {
      /** e.g., `/api/v1/datasets/{id}/data?format=geojson&bbox=...` */
      url: string;
      /** Hint to protect UX (avoid huge downloads) */
      streaming?: boolean;
    };

    /** 3D config (if used) */
    cesium?: {
      tilesetUrl?: string;   // 3D Tiles
      terrainUrl?: string;   // Terrain provider
      imageryUrl?: string;   // Imagery provider
    };
  };

  /** Styling hooks (keep heavy style logic in styles/ and reference it here) */
  style?: {
    maplibre?: {
      /** MapLibre sourceId + layerIds to attach */
      sourceId: string;
      layerIds: string[];
    };
    cesium?: {
      /** Named style preset or styling params */
      preset?: string;
    };
  };

  /** Legend definition for the UI */
  legend?: {
    title?: string;
    items: Array<
      | { type: "swatch"; label: string; color: string }
      | { type: "line"; label: string; color: string; width?: number; dash?: number[] }
      | { type: "range"; label: string; min: number; max: number; unit?: string }
    >;
  };

  /** Governance + ethics + safety */
  governance: {
    sensitivity: Sensitivity;
    /** If true, never show exact geometry/coords in UI popups */
    hidePreciseGeometry?: boolean;
    /** If true, requires authenticated session */
    requiresAuth?: boolean;
    /** Optional policy tags (OPA-ish) */
    policyTags?: string[];
  };

  /** Provenance hooks (for “map behind the map”) */
  provenance: {
    license?: string;
    attribution?: string;
    /** Link-out key used by the UI to open dataset metadata panel */
    datasetId: string;
    /** Optional PROV activity/entity IDs if tracked */
    prov?: { entity?: string; activity?: string };
  };

  /** Timeline integration */
  time?: {
    enabled: boolean;
    /** how to interpret time (year, date range, categorical eras) */
    mode: "year" | "range" | "era";
    /** optional fields/params used by API requests */
    param?: string; // e.g. "year"
    defaultYear?: number;
  };

  /** Optional: feature inspection rules */
  interaction?: {
    hover?: boolean;
    click?: boolean;
    /** How to fetch details for a clicked feature */
    featureInfo?: { mode: "tilequery" | "dataset-query" | "none"; url?: string };
  };
}
```

---

## 🧪 Validation Rules (Strongly Recommended)

### ✅ Invariants
- `id` is **unique**, **stable**, and **never renamed** once released
- `datasetId` must exist in the catalog (and be valid DCAT/STAC)
- Large datasets should prefer **tiles** over raw GeoJSON
- A layer must not allow **bypassing redaction** via zoom, bbox, or feature-info

### Suggested automation
- JSON Schema / Zod validation for definitions
- CI checks: “registry loads”, “no duplicate IDs”, “required fields present”
- Snapshot tests for layer panel ordering/grouping

---

## ➕ Adding a New Layer (Checklist)

### 1) Pick the right path 🔀
- **Vector tiles (MVT)**: best for large boundaries/lines/points
- **Raster tiles**: best for imagery, heatmaps, scanned maps
- **GeoJSON**: small overlays only (or streaming + bbox filtered)

### 2) Create the definition file 📄
- Add `my-layer.ts` exporting a `LayerDefinition`
- Include: legend + provenance + governance from day one

### 3) Register it 🧠
- Export from `index.ts` (or group bundle)
- Keep ordering consistent with UI/Story expectations

### 4) Wire renderer hooks 🖼️
- If MapLibre: ensure referenced style fragments exist
- If Cesium: ensure tileset/terrain config is present

### 5) Pass governance gates 🛡️
- sensitivity classification correct
- no precise coordinates if sensitive
- ensure UI cannot reveal redacted data

### 6) Test ✅
- run lint/unit tests
- verify legend/info panel renders
- verify time slider behavior (if enabled)

---

## ⚡ Performance + UX Guardrails

- 🧱 Prefer **tiles** for anything beyond “small overlay”
- 🧊 Keep layer toggles “fast”: debounce heavy fetches
- 🔎 Use bbox/time filtering wherever possible
- 🧾 Always include legend items that match rendered symbology
- 🧭 Don’t overload the user: group layers by purpose and time period
- ♿ Ensure accessibility: readable labels, keyboard-friendly toggles, and minimal cognitive load

---

## 🪶 CARE + Sensitive Data Notes

Some layers (especially around Indigenous knowledge, sacred sites, culturally sensitive places, or vulnerable ecology) require extra handling:

- Use `governance.sensitivity = "sacred_or_sensitive"` when applicable
- Set `hidePreciseGeometry = true` to prevent exact coordinates exposure
- Prefer aggregated/generalized geometries where appropriate
- Ensure the UI’s info panel clearly communicates constraints & provenance

---

## 🧩 FAQ

<details>
  <summary><strong>Why can’t I just add a layer directly in a component?</strong></summary>

Because this folder is the **contract boundary**. It keeps layers consistent, testable, and governed — and ensures the UI always has provenance + legend + policy context.

</details>

<details>
  <summary><strong>When should I use GeoJSON instead of tiles?</strong></summary>

Only for small overlays (or when streaming + bbox filtering is guaranteed). If you’re worried about size, you almost certainly want tiles.

</details>

<details>
  <summary><strong>How do stories / Focus Mode connect to layers?</strong></summary>

Stories should reference stable layer IDs from this registry. That way narratives can safely toggle the correct layers and the UI can still display provenance.

</details>

---

## ✅ “Done right” Definition Smells

- 🧾 Layer has a **clean legend**
- 🔗 Layer has **dataset/provenance hooks**
- 🛡️ Layer has **explicit governance labels**
- 🗺️ Layer renders correctly in **2D and/or 3D**
- 🧪 Layer passes **schema + CI validation**
- 🧭 Layer integrates cleanly with **timeline & stories**