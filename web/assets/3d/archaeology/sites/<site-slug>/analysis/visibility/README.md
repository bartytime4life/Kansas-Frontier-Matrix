# 👁️ Visibility Analysis — `web/assets/3d/archaeology/sites/<site-slug>/analysis/visibility`

![Module](https://img.shields.io/badge/module-visibility%20analysis-blue)
![Domain](https://img.shields.io/badge/domain-archaeology-7a5c2e)
![2D](https://img.shields.io/badge/2D-MapLibre-informational)
![3D](https://img.shields.io/badge/3D-Cesium%20%2F%203D%20Tiles-informational)
![Metadata](https://img.shields.io/badge/metadata-STAC%20%7C%20DCAT%20%7C%20PROV-success)
![Governance](https://img.shields.io/badge/governance-fail--closed%20%2B%20policy%20pack-critical)

> **Purpose:** This folder holds **visualization-ready visibility products** (viewsheds, line-of-sight, cumulative visibility) for a single archaeological site in KFM’s **3D archaeology site assets**.  
> **Non-negotiable:** **Derived outputs can leak sensitive info** (even without sharing raw inputs). Treat visibility products as governed assets, not “just pretty overlays.”:contentReference[oaicite:0]{index=0}

---

## 🧭 KFM Principles This Module Must Obey (No Exceptions)

### 1) “PostGIS stores geo truth, catalogs describe assets, graph links context”
KFM’s ingestion rule-of-thumb: geospatial “truth” lives in **PostGIS** (vectors/rasters), while **STAC/DCAT** catalogs describe what those assets are and how to serve/filter them, and the **graph** provides the semantic context and linking.:contentReference[oaicite:1]{index=1}:contentReference[oaicite:2]{index=2}

### 2) Provenance-first + fail-closed governance
If provenance is missing (or a required check can’t be performed), KFM’s posture is to **block** rather than publish.:contentReference[oaicite:3]{index=3}

### 3) API boundary + policy pack enforcement
KFM explicitly enforces **API boundaries** so UI/code cannot bypass vetted API paths where redaction and classification can occur.:contentReference[oaicite:4]{index=4}

### 4) UI trust model = “map behind the map”
The UI is designed to surface provenance/metadata so users can trace the “map behind the map,” and the UI is decoupled from backend through REST/GraphQL APIs and configuration rather than hard-coded assumptions.:contentReference[oaicite:5]{index=5}:contentReference[oaicite:6]{index=6}

---

## 🔒 Archaeology-Specific Sensitivity Rules (Read Twice)

### Why visibility outputs are risky
A viewshed (or LOS set) can **implicitly reveal the observer location**, even if you never publish the “site point.” This is a known privacy issue: **data mining outputs can disclose sensitive information** even when raw data is not shared.:contentReference[oaicite:7]{index=7}

### KFM already anticipates “looting-risk” handling
KFM documentation explicitly discusses **fuzzing / generalizing** sensitive locations (including archaeological sites) to protect them from looting (e.g., show a **large hexagon** rather than the exact point).:contentReference[oaicite:8]{index=8}

### Geo-obfuscation patterns to use
KFM’s “sensitivity-aware” design references real-world approaches like rounding sensitive coordinates to ~**10 km accuracy** and showing generic markers for public maps.:contentReference[oaicite:9]{index=9}

### “No output may be less restricted than its inputs”
If your inputs are marked internal/restricted, your visibility outputs must **remain at least as restricted**—including derived artifacts and cached previews.:contentReference[oaicite:10]{index=10}

#### ✅ Decision table: what can live in this `web/assets/...` folder?

| Classification | Can commit to `web/assets/...`? | What can be public? | Recommended mitigation |
|---|---:|---|---|
| `public` | ✅ Yes | Full viewshed/LOS allowed | Still publish STAC/DCAT/PROV + manifest |
| `sensitive` | ⚠️ Only if sanitized | Obfuscated & generalized outputs only | Coarsen geometry, degrade resolution, mask origin |
| `restricted` | ❌ No | Nothing | Serve only via authenticated API/object storage |

> 💡 If you’re unsure, treat it as **restricted** until governance says otherwise (fail-closed).:contentReference[oaicite:11]{index=11}

---

## 📁 Folder Layout (Recommended Contract)

> This is the **target layout** this README documents. Keep it boring and consistent ✅

```text
🌐 web/
└── 🧰 assets/
    └── 🧊 3d/
        └── 🏺 archaeology/
            └── 🏞️ sites/
                └── 🏷️ <site-slug>/
                    └── 📊 analysis/
                        └── 👁️ visibility/
                            ├── 📄 README.md
                            ├── 🧾 manifest.json                     ✅ REQUIRED (what, how, governance)
                            ├── 🖼️ thumbs/                           (optional UI previews)
                            │   ├── 🖼️ viewshed.png
                            │   └── 🖼️ los_preview.png
                            ├── 🛰️ rasters/                          (viewsheds as web-friendly rasters)
                            │   ├── 🗺️ viewshed_obs-main_r10m.cog.tif
                            │   └── 🗺️ viewshed_cumulative_r30m.cog.tif
                            ├── 🧭 vectors/                          (simplified GeoJSON / topojson-ish outputs)
                            │   ├── 📍 viewshed_obs-main_r10m.geojson
                            │   ├── 📍 viewshed_cumulative_r30m.geojson
                            │   └── 🧵 los/
                            │       ├── 📍 los_obs-main_to_feature-001.geojson
                            │       └── 📍 los_obs-main_to_feature-002.geojson
                            └── 🧊 meshes/                           (optional 3D overlays)
                                ├── 🧊 viewshed_surface.glb
                                └── 🧱 tileset/
                                    └── 🧩 tileset.json              (optional: 3D Tiles entrypoint)
```

---

## 🧾 `manifest.json` (REQUIRED)

This folder is a **distribution/visualization surface**. The manifest is the minimum contract that ties each output back to:

- **Inputs** (DEM, observers, obstacles, time slice)
- **Processing** (tooling, parameters, CRS, resolution)
- **Governance** (classification, obfuscation, allowed audiences)
- **Provenance pointers** (STAC/DCAT/PROV identifiers/paths)

> KFM’s architecture depends on catalogs and provenance to avoid “mystery layers.”:contentReference[oaicite:12]{index=12}

### Minimal manifest skeleton (extend as needed)

```json
{
  "kfm": {
    "site_slug": "<site-slug>",
    "analysis": "visibility",
    "version": "1.0.0",
    "generated_at": "YYYY-MM-DD",
    "classification": "public",
    "care_label": null,
    "obfuscation": {
      "enabled": false,
      "method": null,
      "target_accuracy_m": null
    },
    "crs": {
      "compute_epsg": 26914,
      "publish_epsg": 4326
    },
    "inputs": {
      "dem": {
        "stac_item": "data/stac/.../dem.item.json",
        "notes": "Bare-earth DTM preferred for archaeology"
      },
      "observers": {
        "geojson": "data/processed/.../observers.geojson",
        "height_m": 1.7
      },
      "obstacles": {
        "included": false,
        "description": "Vegetation/buildings (optional, time-slice dependent)"
      }
    },
    "processing": {
      "method": "viewshed",
      "earth_curvature": false,
      "max_distance_m": 10000,
      "resolution_m": 10,
      "nodata_handling": "mask",
      "notes": "Record any smoothing, sink-fill, or DEM edits"
    },
    "outputs": {
      "rasters": [
        { "path": "rasters/viewshed_obs-main_r10m.cog.tif", "role": "viewshed" }
      ],
      "vectors": [
        { "path": "vectors/viewshed_obs-main_r10m.geojson", "role": "viewshed_polygon" }
      ],
      "meshes": [
        { "path": "meshes/viewshed_surface.glb", "role": "3d_overlay", "optional": true }
      ]
    },
    "provenance": {
      "stac": "data/stac/.../visibility.item.json",
      "dcat": "data/catalog/dcat/.../visibility.dataset.jsonld",
      "prov": "data/prov/.../visibility.activity.json"
    }
  }
}
```

---

## 🧪 Processing Workflow (Reproducible + Governed)

KFM ingestion/publishing strongly prefers a staged pipeline: **raw → work → processed → catalogs/prov → DB/graph → API → UI** (and policies enforce ordering + provenance).:contentReference[oaicite:13]{index=13}:contentReference[oaicite:14]{index=14}

### Pipeline sketch (Mermaid)

```mermaid
flowchart LR
  A[data/raw 🧱] --> B[data/work 🧪]
  B --> C[data/processed ✅]
  C --> D[data/stac 📦]
  C --> E[data/catalog/dcat 🗂️]
  C --> F[data/prov 🧾]
  D --> G[(PostGIS 🌍)]
  E --> G
  F --> G
  G --> H[API 🔌]
  H --> I[UI (MapLibre/Cesium) 🗺️]
  H --> J[web/assets mirror 🎒]
```

### Key implementation notes

- **CRS discipline:** KFM standardizes display in **WGS84** but may use Kansas-specific projections internally for calculations, converting to WGS84 for web display.:contentReference[oaicite:15]{index=15}  
- If exporting GeoJSON for web, ensure you transform to EPSG:4326 (example pattern shown via PostGIS `ST_Transform` + `ST_AsGeoJSON`).:contentReference[oaicite:16]{index=16}

---

## 🗺️ Serving + Rendering in KFM UI (2D + 3D)

### Map stack expectations
KFM UI supports both:
- **2D**: MapLibre-based interactive map viewer
- **3D**: CesiumJS globe/terrain view, with support for **3D Tiles** and layer draping/toggling:contentReference[oaicite:17]{index=17}:contentReference[oaicite:18]{index=18}

### API-driven delivery (preferred)
Even if you keep a **public** mirror in `web/assets/`, KFM’s policy posture is to keep access mediated via well-defined APIs (so classification/redaction rules can apply).:contentReference[oaicite:19]{index=19}

KFM’s PostGIS integration is explicitly designed to serve tiles efficiently (e.g., Mapbox Vector Tiles via `ST_AsMVT`) and support generalization/caching strategies.:contentReference[oaicite:20]{index=20}

> ✅ Recommendation: treat `web/assets/.../visibility/*` as a **cache/mirror** for public-safe assets; treat **PostGIS + API** as canonical distribution.

### Story Nodes integration (archaeology-friendly)
KFM Story Nodes are intended to be **configuration-driven** (Markdown + JSON convention), enabling guided tours with camera transitions between 2D/3D and analysis overlays.:contentReference[oaicite:21]{index=21}

For archaeology, visibility overlays are a perfect “story beat”:
- “Stand here → what could you see?”
- “How did terrain shape movement?”
- “Which landmarks were intervisible?”

---

## 🤖 Focus Mode + Explainability Hooks (Visibility Edition)

KFM’s Focus Mode pipeline is designed to retrieve data, generate an answer, run governance checks, and return answers with citations / traceability.:contentReference[oaicite:22]{index=22}

### Required explainability fields (put in `manifest.json`)
Visibility analysis is **model output**, not raw observation. To keep trust high (and align with KFM’s transparency goals), record:

- `method`: viewshed / LOS / cumulative / probabilistic
- `resolution_m`
- `max_distance_m`
- `observer_height_m`
- `earth_curvature` / refraction assumptions
- `obstacles_included` (veg/buildings) + time slice
- `compute_epsg` + `publish_epsg`
- governance: `classification`, `obfuscation`, `care_label`

> This supports UI “Layer Provenance” panels and policy gates that enforce citation/traceability expectations.:contentReference[oaicite:23]{index=23}

---

## 🛰️ Mobile / Offline / AR (Optional, But Designed-In)

KFM docs explicitly plan:
- **Offline packs** bundling layers + stories + a mini-app experience for field/classroom use:contentReference[oaicite:24]{index=24}
- **AR experiences** that reuse the same governed data endpoints and formats (AR is another client):contentReference[oaicite:25]{index=25}

Latest proposals emphasize AR layers still being **cataloged via STAC/DCAT** and served through APIs so new visualization modes remain governed and consistent.:contentReference[oaicite:26]{index=26}

✅ **Visibility-specific AR idea:** at a site, show “visible landmarks” as floating labels—BUT only if the site + overlay is public-safe (or the user is authorized).

---

## ✅ QA + Governance Checklist

### Spatial QA
- [ ] Observer points are correct (and **not leaking restricted coordinates**).
- [ ] DEM/DTM is correct type (bare-earth vs DSM) and documented.
- [ ] CRS is correct; computation performed in meters (projected) and outputs published in WGS84 if needed.:contentReference[oaicite:27]{index=27}
- [ ] Visual spot-check a few LOS lines against terrain profile.

### Provenance QA (KFM-standard)
- [ ] STAC/DCAT/PROV pointers exist and are correct.
- [ ] `manifest.json` captures parameters + versions.
- [ ] Output classification is **≥** input classification (“no output less restricted than inputs”).:contentReference[oaicite:28]{index=28}

### Privacy / abuse-resistance QA
- [ ] If any output is sensitive: geometry is generalized/obfuscated or removed from `web/assets/`.  
- [ ] Consider query auditing / inference risks for derived outputs (especially when users can repeatedly query by location/time).:contentReference[oaicite:29]{index=29}

---

## 🧩 Common Deliverables (Pick What You Need)

### 1) Viewshed Raster (fastest UI win)
- COG GeoTIFF for storage + tiling
- Optional PNG tile pyramid for super-fast web previews

### 2) Viewshed Polygon (better for story overlays)
- Simplify geometry aggressively for web
- Consider “ring-banding” (distance bins) for interpretability

### 3) LOS Bundle (best for intervisibility narratives)
- Store key LOS lines (observer → notable features)
- Optional: compute “blocked segment” and annotate occluder distance

### 4) 3D Overlay (flashy, optional)
- Convert polygon/raster to a mesh draped on terrain, or publish as a 3D Tileset for Cesium.

---

## 📚 Source Docs Used (Project Files) 🧠✨

> These are the **project documents** this README is grounded in. Keep them handy while implementing.

- 📘 **KFM Data Intake & Governance Guide** :contentReference[oaicite:30]{index=30}  
  (Provenance-first, policy pack, PostGIS/graph roles, classification rules):contentReference[oaicite:31]{index=31}:contentReference[oaicite:32]{index=32}
- 🧱 **KFM Comprehensive Technical Documentation** :contentReference[oaicite:33]{index=33}  
  (Repo layout, CRS conventions, 2D/3D stack, sensitive location handling):contentReference[oaicite:34]{index=34}:contentReference[oaicite:35]{index=35}
- 🖥️ **KFM UI System Overview** :contentReference[oaicite:36]{index=36}  
  (MapLibre + Cesium UI design, provenance surfacing, API decoupling):contentReference[oaicite:37]{index=37}:contentReference[oaicite:38]{index=38}
- 🤖 **KFM AI System Overview** :contentReference[oaicite:39]{index=39}  
  (Focus Mode pipeline, offline packs, AR/3D direction):contentReference[oaicite:40]{index=40}:contentReference[oaicite:41]{index=41}
- 🧭 **KFM Architecture, Features, and Design** :contentReference[oaicite:42]{index=42}  
  (2D↔3D toggle, AR as a client of the same APIs):contentReference[oaicite:43]{index=43}
- 💡 **Latest Ideas & Future Proposals** :contentReference[oaicite:44]{index=44}  
  (Story Markdown/JSON conventions, AR layers cataloged via STAC/DCAT + APIs):contentReference[oaicite:45]{index=45}:contentReference[oaicite:46]{index=46}
- 🌍 **Innovative Concepts to Evolve KFM** :contentReference[oaicite:47]{index=47}  
  (Cultural protocols, differential access, geo-obfuscation patterns):contentReference[oaicite:48]{index=48}
- 🧠 **Additional Project Ideas** :contentReference[oaicite:49]{index=49}  
  (Evidence-first mindset & narrative alignment concepts):contentReference[oaicite:50]{index=50}
- 🗺️ **Open-Source Geospatial Historical Mapping Hub Design** :contentReference[oaicite:51]{index=51}  
  (COG conversion approach for elevation/hillshade and web performance framing):contentReference[oaicite:52]{index=52}
- 🧰 **Python Geospatial Analysis Cookbook (embedded resource)** :contentReference[oaicite:53]{index=53}  
  (Practical PostGIS export/transforms and geospatial workflow examples):contentReference[oaicite:54]{index=54}
- 🔐 **Data Mining Concepts & Applications (embedded resource)** :contentReference[oaicite:55]{index=55}  
  (Why derived outputs still need privacy + query auditing):contentReference[oaicite:56]{index=56}:contentReference[oaicite:57]{index=57}

### 📦 Reference Libraries (Portfolios)
These are included in the project as broader reference packs (implementation + research context):

- 🧠 AI Concepts & more (portfolio) :contentReference[oaicite:58]{index=58}  
- 🗺️ Maps / Virtual Worlds / Archaeology / WebGL (portfolio) :contentReference[oaicite:59]{index=59}  
- 🧮 Data Management / Architectures / Bayesian Methods (portfolio) :contentReference[oaicite:60]{index=60}  
- 💻 Various programming languages & resources (portfolio) :contentReference[oaicite:61]{index=61}  

---

## 🏁 Done-Definition (Visibility Module)

A site’s visibility analysis is “done” when:

- [ ] Outputs exist (rasters/vectors/optional meshes) ✅
- [ ] `manifest.json` is complete ✅
- [ ] STAC/DCAT/PROV pointers resolve ✅
- [ ] Classification/obfuscation is correct and enforced ✅
- [ ] UI can render in 2D + 3D without hard-coded hacks ✅
- [ ] A Story Node can reference the visibility overlay as a guided narrative beat ✅

---

> 🧠 If you add new artifact types to this folder, update this README first (treat it as the contract).

