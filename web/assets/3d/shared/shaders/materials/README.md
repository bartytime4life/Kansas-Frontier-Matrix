# 🎨 Shader Materials (Shared) — KFM 3D

`📁 web/assets/3d/shared/shaders/materials/`

`🧩 materials` `⚡ WebGL` `🌍 CesiumJS` `🗺️ MapLibre` `🧠 Explainable AI` `🔎 Provenance‑First`

These shader **materials** are KFM’s “last mile” between curated datasets and trustworthy visuals: they help make 2D/3D maps *feel alive* without turning into a black box. KFM’s UI goal is that every visualization stays linked to its source data + metadata — “the map behind the map.”:contentReference[oaicite:0]{index=0}

> 🔐 **Ethics + trust are requirements (not vibes):** materials must respect governance rules (sensitivity flags, generalization, access control) and support provenance/attribution surfacing in the UI.:contentReference[oaicite:1]{index=1}:contentReference[oaicite:2]{index=2}

---

## 🧭 Why this folder exists

KFM supports:
- **2D mapping** (MapLibre/Leaflet patterns) with a timeline slider concept for temporal layers:contentReference[oaicite:3]{index=3}
- **3D globe + terrain** using **CesiumJS**, including streaming **3D Tiles** for large 3D datasets like point clouds, building models, and volumetric data:contentReference[oaicite:4]{index=4}

Materials here are designed to plug into that dual-mode experience:
- Switching 2D ↔ 3D should preserve context (camera, layers where possible).:contentReference[oaicite:5]{index=5}
- 3D Tiles should progressively load more detail as you zoom, so materials must handle LOD + streaming cleanly.:contentReference[oaicite:6]{index=6}
- “Focus Mode” and story experiences can highlight map features (points/paths) and must remain explainable + citable.:contentReference[oaicite:7]{index=7}

---

## 🗂️ Folder layout (recommended)

> This repo path implies a “shared shader kit” used by multiple render targets. If the surrounding repo differs, treat this as the target structure we’re standardizing toward.

```text
web/assets/3d/shared/shaders/
├─ 🧱 includes/                          # 🧱 Reusable GLSL chunks (math, color, noise, picking, common uniforms)
│  ├─ 📐🧾 kfm_precision.glsl             # Precision + numeric guards (mobile-safe defaults, epsilon helpers)
│  ├─ 🎨🧾 kfm_color.glsl                 # Color utilities (linear↔sRGB helpers, blending, luminance, contrast helpers)
│  ├─ 🌈🧾 kfm_colormap.glsl              # Colormap/ramp sampling helpers (scalar→color, quantize/bins, ramp textures)
│  ├─ 🌫️🧾 kfm_noise.glsl                 # Noise helpers (hash/noise functions for dithering, procedural patterns)
│  └─ 🖱️🧾 kfm_picking.glsl               # GPU picking helpers (ID encode/decode, picking buffer conventions)
└─ 🎨 materials/                         # 🎨 Ready-to-use shader “materials” (programs + TS bindings + metadata)
   ├─ 📄 README.md                        # 👈 you are here 📌 How shader materials are registered, parameterized, and versioned
   ├─ 📦🧾 index.ts                        # Registry exports (material id → shader program + defaults)
   ├─ 🧾📄 types.ts                        # TypeScript contracts for material params/uniforms and binding signatures
   ├─ 🏞️ terrain/                         # Terrain shaders (height/relief, drape textures, hillshade, LOD transitions)
   │  ├─ 🧾 terrain.vert.glsl              # Vertex shader (terrain positions, morphing/LOD, UVs, normals)
   │  ├─ 🧾 terrain.frag.glsl              # Fragment shader (drape sampling, lighting, color ramps, fog)
   │  └─ 🧾 terrain.material.ts            # TS material wrapper (uniforms, textures, defines, default params)
   ├─ 🧱 tiles3d/                          # 3D Tiles shaders (classification, PBR shading, feature ids)
   │  ├─ 🧾 tileset_classify.frag.glsl     # Fragment shader for classification/highlight (by feature id/class)
   │  ├─ 🧾 tileset_pbr.frag.glsl          # PBR-ish fragment shader for tiles (lighting, roughness/metallic)
   │  └─ 🧾 tiles3d.materials.ts           # TS wrappers/registry for 3D tiles materials (variants + params)
   ├─ 🧩 overlays/                         # Overlay shaders (analysis layers, uncertainty, heatmaps, masks)
   │  ├─ 🔥🧾 heatmap.frag.glsl             # Heatmap rendering (kernel/ramp sampling, alpha, blending rules)
   │  ├─ 🟫🧾 uncertainty_hatch.frag.glsl   # Uncertainty hatch/pattern overlay (a11y-friendly; deterministic)
   │  └─ 🧾 overlays.materials.ts          # TS wrappers for overlay materials (uniforms, toggles, blending modes)
   └─ ✨ ui_fx/                             # UI visual effects shaders (outlines, pulses, attention cues)
      ├─ ✨🧾 outline.frag.glsl              # Outline effect (edges/IDs/depth-based outlines)
      ├─ 🧵✨🧾 pulse_thread.frag.glsl        # Pulse effect for story/pulse highlights (time-based animation, gated)
      └─ 🧾 ui_fx.materials.ts              # TS wrappers/registry for UI FX materials (params, enable flags)
```

---

## 🧱 What “material” means in KFM

A KFM material is **not just GLSL**. It is a small, auditable “visualization program” made of:

1) **Shader source** (`.glsl`)  
2) **A typed descriptor** (`.ts`) that defines:
   - uniform schema
   - render targets (Cesium / MapLibre custom layer / Three.js fallback)
   - legend + accessibility metadata
   - provenance hooks (dataset IDs, citation keys, sensitivity behaviors)

This is consistent with KFM’s broader documentation-first, modular approach and reproducibility mindset.:contentReference[oaicite:8]{index=8}

### ✅ Minimal TypeScript contract (example)

```ts
// materials/types.ts
export type MaterialTarget = "cesium-tiles3d" | "cesium-terrain" | "maplibre-custom" | "three";

export type SensitivityMode = "none" | "warn" | "generalize" | "redact";

export interface MaterialProvenance {
  /** KFM dataset IDs (from STAC/DCAT). */
  datasetIds: string[];
  /** Optional: cite keys for Layer Info / Layer Provenance UI. */
  citationKeys?: string[];
  /** Any extra audit notes for reviewers. */
  notes?: string;
}

export interface MaterialLegend {
  title: string;
  /** Human readable units (if applicable). */
  units?: string;
  /** Default ramp stops in normalized [0..1] */
  stops?: Array<{ t: number; label: string }>;
}

export interface KfmMaterial {
  id: string;                 // e.g., "heatmap.v1"
  label: string;              // UI name
  targets: MaterialTarget[];
  vertex?: string;            // GLSL source or key
  fragment: string;           // GLSL source or key
  uniforms: Record<string, { type: string; default: unknown }>;
  defines?: Record<string, boolean | number | string>;
  legend?: MaterialLegend;

  /** Governance behavior for sensitive layers. */
  sensitivityMode?: SensitivityMode;

  /** Evidence-first hooks (Layer Info / citations / export attribution). */
  provenance: MaterialProvenance;

  /** Accessibility knobs (high contrast, pattern overlays, etc.). */
  accessibility?: {
    highContrastVariant?: string;   // id of another material or define set
    patternAssist?: boolean;        // hatch/dots to avoid color-only meaning
  };
}
```

---

## 🔗 How materials connect to STAC/DCAT/PROV

KFM’s catalog structure treats metadata + provenance as first-class outputs of ingestion pipelines.:contentReference[oaicite:9]{index=9}  
STAC items/collections are expected to include links/pointers to provenance, and KFM adheres to WGS84 geometry conventions.:contentReference[oaicite:10]{index=10}

**Material rule:** every material must declare which dataset(s) it visualizes (by KFM dataset ID), so the UI can:
- show **Layer Info** (source, license, prep summary) and future Layer Provenance panels:contentReference[oaicite:11]{index=11}
- include attribution when exporting/sharing views:contentReference[oaicite:12]{index=12}

---

## 🧩 Runtime integration targets

### 🌍 CesiumJS (3D globe, terrain, 3D Tiles)

KFM’s 3D mode uses **CesiumJS**, including 3D Tiles streaming for point clouds/buildings/volumes.:contentReference[oaicite:13]{index=13}

Typical integration patterns:
- **3D Tiles custom shading** (classification, uncertainty, selection glow)
- **Terrain shading** (hillshade, slope, time-based drape)
- **Story/Focus effects** (camera flight + highlight overlays)

> 🧠 If you can’t explain what a shader does in Layer Info, it’s not ready. Focus Mode and ethical design require citations + context to stay visible.:contentReference[oaicite:14]{index=14}:contentReference[oaicite:15]{index=15}

### 🗺️ MapLibre (2D) custom layers

KFM’s 2D mapping approach emphasizes fast rendering (vector/raster tiles) and an interactive timeline slider for time slices.:contentReference[oaicite:16]{index=16}

Custom layers can reuse the same shared GLSL chunks (especially for:
- GPU heatmaps
- animated flowlines
- selection outlines
- pattern overlays for accessibility)

### 🧰 Three.js (optional fallback / special scenes)

KFM technical docs note that some 3D effects (extrusions, specialized 3D overlays) may be possible via Cesium or three.js integration ideas.:contentReference[oaicite:17]{index=17}

If you add Three.js support:
- keep it **optional**
- keep shader sources **shared** (avoid forking GLSL unless unavoidable)

---

## 🧮 Coordinate & precision conventions

### 🌐 CRS

KFM’s internal display standard is **WGS84 (EPSG:4326)**, reprojecting at ingest and recording that in provenance.:contentReference[oaicite:18]{index=18}

**Shader implications:**
- Treat incoming layer coordinates as WGS84 unless the target engine provides a different space.
- For Cesium, expect engine-provided transforms (often ECEF / world space).  
- For MapLibre custom layers, expect Mercator space but keep data semantics tied to WGS84 metadata.

### 🛰️ Practical ingestion example

Geospatial workflows commonly transform geometries to EPSG:4326 for web output (e.g., PostGIS `ST_Transform(...,4326)` + GeoJSON).:contentReference[oaicite:19]{index=19}

---

## 🔒 Governance & privacy: materials must not leak sensitive data

KFM explicitly supports dataset sensitivity signals in the UI (lock/warning), hiding restricted layers or showing generalized versions (e.g., hex areas instead of exact points).:contentReference[oaicite:20]{index=20}

### 🧾 Sensitivity modes (recommended)

| Mode | What shader must do | Typical use |
|---|---|---|
| `none` | normal rendering | public datasets |
| `warn` | normal rendering + UI warning | mildly sensitive |
| `generalize` | render aggregates (hex bins / grids), jitter, blur | “location-protect” layers |
| `redact` | render placeholder/pattern, no exact marks | restricted layers |

**Privacy toolbox inspiration:** privacy-preserving techniques include *k-anonymity, l-diversity, t-closeness* and strategies like *generalization and suppression*, plus query auditing to detect inference risk.:contentReference[oaicite:21]{index=21}

### 🪶 CARE / Indigenous data sovereignty

KFM’s governance principles include CARE-aligned controls for sensitive data and community authority for its use.:contentReference[oaicite:22]{index=22}  
Future-facing concepts also emphasize cultural protocols / Indigenous data sovereignty for historical sites and related sensitive knowledge.:contentReference[oaicite:23]{index=23}

**Material rule:** if a dataset is flagged as CARE-restricted, the material must support a `generalize` or `redact` path and should avoid any shader behavior that reconstructs exact geometry via inference.

---

## ♿ Accessibility & “don’t mislead” requirements

KFM explicitly prioritizes:
- avoiding misleading visualizations
- semantic/ARIA accessibility
- high-contrast mode support:contentReference[oaicite:24]{index=24}

### ✅ Material accessibility checklist

- [ ] Don’t rely on color alone (use patterns/hatching when meaning-critical).
- [ ] Provide a high-contrast variant (define-set or alt material id).
- [ ] Legends are readable + units are declared.
- [ ] Opacity defaults avoid “lying by saturation” (don’t make weak evidence look bold).

---

## ⏱️ Time & narrative hooks (timeline, stories, pulse threads)

KFM supports temporal navigation (timeline slider) and narrative-driven story nodes, and future “Pulse Threads” concepts that connect events/places via dynamic UI signals.:contentReference[oaicite:25]{index=25}:contentReference[oaicite:26]{index=26}

### Recommended uniforms for time-aware materials

| Uniform | Type | Meaning |
|---|---|---|
| `u_kfm_year` | float | timeline year (or normalized time) |
| `u_kfm_time` | float | seconds since session start |
| `u_kfm_timeWindow` | vec2 | `[start,end]` for filtering/fading |
| `u_kfm_pulse` | float | pulse intensity (story/Focus Mode attention) |

---

## ⚡ Performance & reproducibility

### 🧪 Deterministic pipeline mindset

KFM pipelines are intended to be reproducible/deterministic: same inputs → same outputs, with updated metadata + provenance logs.:contentReference[oaicite:27]{index=27}

**Shader implication:** material behavior must be stable across builds. If you add randomness, it must be seeded (`u_kfm_seed`) and documented.

### 🧰 CI + validation culture

KFM includes catalog QA/validation tooling integrated with CI, failing builds on incomplete metadata or broken integrity expectations.:contentReference[oaicite:28]{index=28}

**Material implication:** add compilation + minimal render tests (see Testing section) so “shader broke on mobile GPU” doesn’t ship.

### 📦 Offline packs & content-addressed bundles

KFM aims for offline packs (subset of layers + story content) that can run locally, potentially including pre-rendered tiles and PMTiles/MBTiles archives.:contentReference[oaicite:29]{index=29}  
Future proposals also emphasize bundling outputs with **content-addressable hashes** and deterministic ETL to ensure integrity and trust.:contentReference[oaicite:30]{index=30}

**Material rule for offline:** no hard dependency on remote textures/services; ship ramps/pattern textures as local assets if required.

---

## 🧠 AI overlays: confidence & uncertainty materials

KFM’s AI features are intended to remain provenance-first — AI-generated additions should be logged and marked for transparency.:contentReference[oaicite:31]{index=31}

Recommended material patterns:
- **confidence ramp**: continuous color + pattern assist
- **uncertainty hatch**: hatch density encodes uncertainty while color encodes mean
- **explainability highlight**: focus glow only for features with citations

---

## 🧷 Adding a new material (PR checklist)

### 1) Create the shader(s)
- `*.vert.glsl` (optional)
- `*.frag.glsl` (required)
- Prefer shared chunks in `../includes/` for math/color/noise/picking.

### 2) Add a descriptor
Create `*.material.ts` defining:
- uniforms & defaults
- targets (Cesium/MapLibre/Three)
- legend + accessibility settings
- provenance dataset IDs + citation keys

### 3) Register it
Export from `materials/index.ts` so the UI can discover it via config rather than hardcoding (matches KFM’s modular, schema-driven UI philosophy).:contentReference[oaicite:32]{index=32}

### 4) Governance audit
- Confirm sensitivity behavior is correct (none/warn/generalize/redact).
- If the dataset is sensitive, default to generalized rendering.

KFM policies already anticipate classification-aware handling (e.g., sensitive stations omitted or limited to authorized users).:contentReference[oaicite:33]{index=33}

### 5) Provenance compliance
- Ensure Layer Info can present: source, license, preparation summary.
- Ensure exports can carry attribution.

(And yes, policy gates can fail builds if provenance expectations aren’t met.):contentReference[oaicite:34]{index=34}

### 6) CI-friendly submission model
Automation can propose changes via PR, but **must not auto-merge**; everything goes through human review + CI policy gates.:contentReference[oaicite:35]{index=35}

---

## 🧪 Testing & debugging (recommended)

### ✅ Required tests
- **Compile test:** shader compiles in WebGL2 context (and WebGL1 if we target it).
- **Uniform schema test:** descriptor matches runtime binder (types + defaults).
- **Golden render:** render a tiny fixture scene (offline) and compare pixels within tolerance.

### 🕵️ Debug tips
- Add a `#define KFM_DEBUG 1` path that shows:
  - feature IDs
  - NaN/Inf highlights
  - tile boundaries (Cesium) for LOD debugging

---

## 🔏 Supply-chain + artifact integrity (forward-looking)

KFM’s roadmap includes treating data with the rigor of code: versioned, reviewable, and trustworthy — including signing artifacts and attaching provenance manifests.:contentReference[oaicite:36]{index=36}

**Material extension idea:** generate a `materials.manifest.json` during build:
- list of material IDs
- SHA256 of GLSL sources
- build version tag

This mirrors the “content-addressed, signed artifacts” mindset being explored for tiles/data bundles.:contentReference[oaicite:37]{index=37}

---

## 📚 Reference libraries (project files)

These internal PDFs are **reference bundles** used for deeper implementation details and patterns:
- `AI Concepts & more.pdf` (PDF portfolio):contentReference[oaicite:38]{index=38}
- `Various programming langurages & resources 1.pdf` (PDF portfolio):contentReference[oaicite:39]{index=39}
- `Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf` (PDF portfolio)
- `Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf` (PDF portfolio):contentReference[oaicite:41]{index=41}

---

## 🧾 Core KFM docs this folder aligns with

- UI transparency (“map behind the map”), modular React UI, provenance surfacing:contentReference[oaicite:42]{index=42}:contentReference[oaicite:43]{index=43}
- 3D mode via CesiumJS + 3D Tiles + smooth 2D/3D switching:contentReference[oaicite:44]{index=44}:contentReference[oaicite:45]{index=45}
- Avoid misleading visualizations + accessibility + Layer Info / provenance panels:contentReference[oaicite:46]{index=46}
- FAIR/CARE governance + provenance-first enforcement mindset:contentReference[oaicite:47]{index=47}
- WGS84 standard + 2D/3D integration patterns (Cesium/MapLibre):contentReference[oaicite:48]{index=48}:contentReference[oaicite:49]{index=49}
- Deterministic pipelines + CI validation patterns:contentReference[oaicite:50]{index=50}:contentReference[oaicite:51]{index=51}

---

### ✅ Definition of done (materials)

A material is “done” when:
- it renders correctly (2D/3D targets as declared)
- it has a legend + accessibility notes
- it declares dataset IDs + citations for Layer Info
- it respects sensitivity modes
- it passes compile + golden tests
- it stays reproducible (seeded + documented if stochastic)

🧠✨ Build visuals you can *defend*, not just visuals you can *demo*.

