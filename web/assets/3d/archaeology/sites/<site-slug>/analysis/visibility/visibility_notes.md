---
title: "👁️ Visibility Analysis Notes — <SITE_NAME>"
site_slug: "<site-slug>"
domain: "archaeology"
analysis: "visibility"
status: "draft"
classification: "<public|sensitive|confidential>"
owners:
  - "<name-or-handle>"
created: "2026-01-25"
updated: "2026-01-25"
---

# 👁️ Visibility Analysis Notes (🏺 Archaeology)

> **File:** `web/assets/3d/archaeology/sites/<site-slug>/analysis/visibility/visibility_notes.md`
>
> ✅ This is a **human + UI-facing** note (renderable Markdown).  
> 🧾 The **canonical evidence artifacts** (data + metadata + provenance) must still flow through the KFM pipeline (`data/raw → data/processed → STAC/DCAT/PROV → graph → API → UI`).  
> 🔐 If this site is sensitive, this note must avoid publishing exact coordinates, observer points, or any “reverse-engineerable” geometry.

---

## 🧭 Quick Summary

| Badge | Value |
| --- | --- |
| 🟡 Status | Draft |
| 👁️ Analysis type | Viewshed / Intervisibility / Cumulative visibility |
| 🧱 Dimensions | 2D raster + optional 3D overlays (tiles/surfaces) |
| 🕰️ Time slices | `<present>` / `<historic-year>` / `<scenario>` |
| 🔐 Sensitivity | `<public|restricted>` |

---

## 🎯 Goal

Visibility analysis answers “what could be seen” given a terrain/surface model and one or more observers.

For this site, we use it to:

- 🧠 **Interpretation:** test hypotheses about landmark prominence, sightlines, and visual relationships between features.
- 🧭 **Planning:** understand lines-of-sight to modern disturbances (roads, developments) and viewpoints.
- 📖 **Storytelling:** create a clear “what you can see from here” narrative layer in 2D + 3D.

---

## ❓ Research Questions (fill in)

- From **Feature A** (mound / structure / overlook), what landscape areas are visible within `<N>` km?
- Are **Feature A ↔ Feature B** intervisible (mutual line-of-sight)?
- Which areas are visible from **many** observers (cumulative viewshed “hotspots”)?
- How does visibility change across **time slices** (historic vegetation/buildings/terrain reconstructions)?

---

## 🗂️ Inputs Inventory

> Tip: treat each input as a governed dataset with an ID + provenance + classification (even if it’s “local draft”).

| Input | Dataset ID | Path (canonical) | CRS | Resolution | Notes |
| --- | --- | --- | --- | --- | --- |
| DEM (bare earth) | `<kfm.dataset.id>` | `data/processed/.../dem.tif` | `<EPSG:####>` | `<m>` | baseline terrain |
| DSM (surface) | `<kfm.dataset.id>` | `data/processed/.../dsm.tif` | `<EPSG:####>` | `<m>` | includes buildings/vegetation if available |
| LiDAR point cloud | `<kfm.dataset.id>` | `data/processed/.../*.laz` | `<EPSG:####>` | `<n/a>` | optional, for DSM refinement |
| Land cover / canopy height | `<kfm.dataset.id>` | `data/processed/.../canopy.tif` | `<EPSG:####>` | `<m>` | optional occlusion model |
| Site features (observer/target) | `<kfm.dataset.id>` | `data/processed/.../features.geojson` | `<EPSG:####>` | `<n/a>` | points/lines/polys; **often sensitive** |

### 🔐 Sensitivity reminder

If any input is classified sensitive/restricted, derived outputs must **not** reduce that restriction.

Plan for one (or more) of:

- 🧩 generalized geometry (bins/hexes)  
- 🧊 resolution downgrades  
- 🧼 clipping/masking  
- 🔑 access control at API + UI  

---

## 🧑‍🦯 Observer & Target Model

### Observers (where we “look from”)

Define one or more observer sets:

1. 📍 **Primary observation points** (e.g., mound summit(s), overlook(s))  
2. 🧵 **Route-based observers** (sample points along a path/transect)  
3. 🟦 **Area-based observers** (grid or random points in a zone)  

Each observer should specify:

- `observer_height_m`: e.g., `1.6` (standing human) or feature-specific
- `positional_uncertainty_m`: e.g., `±5 m`
- `time_slice`: e.g., `present`, `1850s_recon`, `paleo_scenario_01`

### Targets (what we test visibility *to*)

Targets can be:

- 📍 specific points (other features)
- 🧭 areas (zones)  
- 🗺️ “any surface cell” (classic viewshed)

Optional target params:

- `target_height_m` (e.g., ridge line, tower, reconstructed building height)

---

## 🧪 Method Plan

### 1) Baseline: Terrain viewshed (DEM-only)

- Normalize to a **common CRS & resolution**.
- Compute **binary viewshed** per observer: visible vs not visible.
- Combine observers as needed:
  - `ANY` visible (union)
  - `ALL` visible (intersection)
  - `COUNT` visible (cumulative count)
  - `PCT` visible (count / num_observers)

### 2) Surface viewshed (DSM)

Use DSM when modern/historic structures or canopy height matter.

### 3) Intervisibility graph (feature ↔ feature)

Create an **intervisibility matrix** between key features:

- nodes = features
- edges = LOS exists (optionally weighted by distance, percent of path occluded, etc.)

This is ideal for graph storage because it’s small, queryable, and “explainable” in UI (you can show edges + provenance).

### 4) Optional: Probabilistic visibility (uncertainty-aware)

If input accuracy is limited (terrain artifacts, uncertain paleo-vegetation), prefer probabilities:

- jitter observer location/height within uncertainty bounds (Monte Carlo)
- compute visibility frequency per cell
- output a `viewshed_probability` raster (0–1)

### 5) Optional: 4D / scenario viewsheds (time as first-class) 🕰️

Run the same analysis across time slices:

- `present_surface`
- `historic_surface_<year>`
- `paleo_surface_<scenario>`
- `leaf_on` vs `leaf_off`
- `with_structure_recon` vs `without`

Then compare:
- Δ visibility (difference raster)
- “newly visible” / “no longer visible” areas

---

## 📦 Outputs & Storage

### Canonical evidence artifacts (✅ required)

Store these in `data/processed/...` with STAC/DCAT/PROV metadata.

Recommended outputs per run:

- 🗺️ `viewshed_binary.cog.tif`
- 🧮 `viewshed_count.cog.tif`
- 🎲 `viewshed_probability.cog.tif` (optional)
- 🧩 `viewshed_polygons.geojson` (optional, derived contours)
- 🔗 `intervisibility_edges.parquet` (optional, feature graph edges)
- 🧾 `run_manifest.json` (inputs, params, versions, checksums)
- 🧾 `stac_item.json`, `dcat_dataset.json`, `prov.json`

### Web/UI assets (optional cache)

If the front-end needs fast rendering:

- raster served as tiles / COG range-requests
- vectors served as tiles (e.g., PMTiles)
- 3D overlays served as 3D Tiles

> ⚠️ `web/assets/...` is a delivery/cache layer, not the canonical truth.

### 📁 Suggested folder layout (site-scoped)

```text
🌐 web/assets/3d/archaeology/sites/
└── 🏷️ <site-slug>/
    └── 🧪 analysis/
        └── 👁️ visibility/
            ├── 📝 visibility_notes.md                 (scope, assumptions, decisions, caveats)
            ├── ⚙️ visibility_config.yml               (inputs + parameters + toolchain knobs)
            ├── 📦 outputs/
            │   └── 🆔 <run-id>/
            │       ├── 🗺️ viewshed_binary.cog.tif      (binary visible/not-visible)
            │       ├── 🧮 viewshed_count.cog.tif       (cumulative visibility count; multi-observer runs)
            │       ├── 🎲 viewshed_probability.cog.tif (probabilistic/uncertainty-weighted visibility)
            │       ├── 🧩 viewshed_polygons.geojson    (simplified vector footprint/contours)
            │       ├── 🧱 viewshed_3dtiles/
            │       │   └── 🧩 tileset.json             (optional: 3D Tiles entrypoint)
            │       └── 🧾 run_manifest.json            (what ran, when, with what inputs + hashes)
            └── 🖼️ thumbs/
                └── 🖼️ viewshed_preview.png            (small, fast UI preview)
```

---

## 🖥️ UI Integration Checklist (2D + 3D)

### Layer naming & UX

- Layer title format:
  - `Visibility (Viewshed) — <scenario> — <resolution>`
- Provide a **legend**:
  - binary: visible / not visible
  - cumulative: count bins or percent
  - probabilistic: 0–1 ramp (with text labels)

### Provenance (“map behind the map”) 🧾

For the visibility layer info panel, include:

- dataset ID(s)
- time slice
- run-id
- input list (DEM/DSM IDs)
- classification & access rules
- method summary (engine, params)

### 2D/3D pairing 🌐

- 2D overlay: raster/tiles in the map view
- 3D overlay: same run exposed in globe view (draped raster or extruded polygons)
- A single toggle should switch between 2D and 3D without losing the scenario selection.

### Story Nodes & Focus Mode 🧠

- Add a story step: “What could you see from `<feature>`?”
- Add 2–3 tested Focus Mode questions:
  - “Show me the viewshed from `<feature>` in `<year>`.”
  - “Are `<feature A>` and `<feature B>` intervisible?”
  - “What inputs were used to compute this layer?”

---

## 🔐 Governance, Ethics, and Safety

### Avoid “accidental disclosure” via outputs

Visibility products can reveal sensitive site locations even without raw coordinates.

Mitigations (pick what applies):

- Publish **generalized** outputs (bins/hexagons) for public audiences
- Reduce resolution (or clip/mask) around sensitive features
- Move exact results behind authenticated access
- Audit queries / deny “triangulation” behavior (repeated queries to infer restricted info)

### CARE-aware handling (when applicable)

If the site intersects with Indigenous knowledge/cultural protocols:

- document authority/ethics constraints
- use culturally appropriate access tiers
- attach protocol notes in metadata and UI

---

## ✅ Definition of Done (DoD)

**Data + Evidence**
- [ ] Inputs have dataset IDs, provenance, and classification recorded
- [ ] Viewshed outputs stored in `data/processed/...` (not only `web/assets/...`)
- [ ] STAC/DCAT/PROV created and linked for each run
- [ ] `run_manifest.json` captures:
  - inputs + hashes
  - parameters
  - software versions
  - execution timestamp
- [ ] Graph updated (no orphan entities)

**Policy + Safety**
- [ ] Output classification is **>=** max(input classification)
- [ ] Public UI contains no precise coordinates for sensitive sites
- [ ] API enforces access control and/or redaction for restricted layers

**UI + UX**
- [ ] Layer toggles + legend + opacity slider
- [ ] Layer info panel includes provenance + method summary
- [ ] 2D and 3D both supported (or 3D explicitly “not implemented” with rationale)
- [ ] Story Node step added (if the site has a narrative track)
- [ ] Focus Mode Q&A tested (with citations)

---

## 🧾 Appendix A — `visibility_config.yml` template

<details>
<summary>Click to expand template ⚙️</summary>

```yaml
# visibility_config.yml
site_slug: "<site-slug>"
run_id: "<YYYYMMDD>_<engine>_<scenario>_<res>"

scenario:
  time_slice: "<present|historic_####|paleo_##>"
  surface_model: "<DEM|DSM>"
  leaf_state: "<leaf_on|leaf_off|n/a>"
  structures: "<none|modern|reconstructed>"

crs: "EPSG:####"
resolution_m: <1|2|5|10>
max_distance_m: <5000>
earth_curvature: <true|false>   # consider when distances are large

observers:
  - id: "obs_001"
    kind: "<point|route|area>"
    dataset_id: "<kfm.dataset.id>"
    observer_height_m: 1.6
    positional_uncertainty_m: 5
    notes: "mound summit (generalized for public release)"

targets:
  kind: "<surface|feature_set>"
  target_height_m: 0.0

engine:
  name: "<gdal_viewshed|grass_viewshed|custom_gpu>"
  params:
    # engine-specific knobs go here

outputs:
  canonical_root: "data/processed/archaeology/sites/<site-slug>/analysis/visibility/<run_id>/"
  web_cache_root: "web/assets/3d/archaeology/sites/<site-slug>/analysis/visibility/outputs/<run_id>/"

governance:
  classification: "<public|sensitive|confidential>"
  redaction:
    generalize_geometry: true
    publish_probability_only: false
    min_public_resolution_m: 30
```

</details>

---

## 🧾 Appendix B — Project file alignment map

This note follows the “evidence-first” KFM patterns, pulling from the project docs:

- 🧱 **UI & 3D rendering:** 2D/3D layer behavior, provenance panels, sensitivity warnings
- 🗃️ **Data intake & catalogs:** STAC/DCAT/PROV, classification, no-bypass rules
- 🧠 **AI/Focus Mode:** Q&A + provenance citations + human review
- 🕰️ **Time & scenarios:** time slices, timeline slider, 4D thinking
- 🔐 **Privacy & disclosure risk:** outputs can leak sensitive info; mitigate with redaction & auditing
- 🧰 **Implementation resources:** geospatial + WebGL + data engineering references for buildout

### 📚 Full project corpus used (top-level)

- Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf
- Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf
- Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf
- Kansas Frontier Matrix – Comprehensive UI System Overview.pdf
- 📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf
- Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf
- Additional Project Ideas.pdf
- 🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf
- Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf (portfolio)
- AI Concepts & more.pdf (portfolio)
- Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf (portfolio)
- Various programming langurages & resources 1.pdf (portfolio)

