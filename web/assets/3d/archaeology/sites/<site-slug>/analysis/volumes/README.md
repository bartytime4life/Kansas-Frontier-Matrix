# 🧱 Volumes (3D/4D) — Archaeology Site Analysis

> 📍 **Path:** `web/assets/3d/archaeology/sites/<site-slug>/analysis/volumes/`  
> 🎯 **Goal:** store **web-ready volumetric analysis artifacts** (and their provenance) for a single archaeology site.

KFM is built around **evidence-first, provenance-first** delivery: *no mystery layers, no black boxes, no “trust me” outputs.* Every visualization and derived artifact should be traceable to sources, processing steps, and governance rules. ✅[^contract-first][^provenance-first]

---

## 🧠 What counts as a “volume” here?

A **volume** is any **3D raster / voxel grid / subsurface cube** (and derivatives) tied to this site, such as:

- 🕳️ **Subsurface volumes**: GPR amplitude/time-slices, resistivity tomography, magnetometry interpolation (where represented volumetrically), etc.
- 🧱 **Above-ground volumetrics**: density grids, occupancy voxels, uncertainty cubes, segmentation labels.
- 🧪 **Interpretation & uncertainty**: label volumes, probability volumes, confidence intervals, scenario alternatives. (Treat these as first-class data artifacts, with the same rigor as “raw” layers.)[^kfm-ml]

> 🔒 **Archaeology note:** treat looting-sensitive locations and subsurface interpretations as **sensitive-by-default**. KFM explicitly supports sensitive handling in UI and governance (e.g., lock indicators and generalized display such as showing an area/hex instead of exact points).[^sensitive-ui][^fair-care]

---

## 🧭 Non‑negotiable KFM rules (apply here too)

### 1) Evidence-first ordering (don’t bypass the chain)
Volumes should arrive here **only after** controlled ingestion + processing + cataloging. KFM explicitly enforces that outputs must remain traceable through a strict sequence; if any documentation suggests bypassing that order, it’s considered wrong by design.[^pipeline-order]

### 2) Contract-first data (no “mystery layers”)
Every volume published to a user-facing surface must have a **data contract** and metadata sufficient for automatic attribution, method tracing, and auditability.[^contract-first]

### 3) Provenance must be machine-readable (STAC/DCAT/PROV)
KFM relies on **STAC + DCAT + PROV** as the metadata backbone so that any layer, story, or AI answer can link back to evidence.[^stac-dcat-prov]

### 4) “Fail closed” policy gates
If metadata is missing, licensing is unclear, sensitivity is unlabeled, or provenance is incomplete → **don’t publish**. KFM’s governance model emphasizes automated gates (schema validation, license presence, sensitivity handling, provenance completeness, citation enforcement) and “fail closed” behavior.[^policy-gates]

---

## 🗂️ Folder layout (recommended)

This folder should be **publishable** and **web-consumable**, not the place for raw instrument exports.

```text
📊 analysis/
└── 🧊 volumes/
    ├── 📄 README.md
    ├── 🧾 _index.json                         (optional: local index for UI/loader)
    └── 🏷️ <volume-slug>/
        ├── 🧾 volume.kfm.json                 (recommended: contract + UI-friendly metadata)
        ├── 🛰️ stac-item.json                  ✅ required (STAC Item for cataloging)
        ├── 🏷️ dcat.json                       ✅ required (DCAT Dataset/Distribution for cataloging)
        ├── 🧬 prov.jsonld                      ✅ required (PROV-O lineage for auditability)
        ├── 📦 volume/                          (one of: zarr/ | nrrd/ | etc — see “Formats”)
        ├── 🔐 checksums.txt                    (recommended: sha256/sha512 for important assets)
        ├── 🖼️ previews/
        │   ├── 🖼️ thumb.png                    (UI thumbnail)
        │   ├── 🧫 slice_xy_z000.png            (representative slices; small + fast)
        │   ├── 🧫 slice_xz_y050.png
        │   └── 🧫 slice_yz_x050.png
        └── 🧪 derivatives/
            ├── 🧊 isosurface.glb               (optional: extracted isosurface mesh; web-friendly)
            ├── 🧭 footprint.geojson            (optional: AOI footprint / coverage hull)
            └── 📊 histogram.json               (optional: intensity distribution for UI legend)
```

> ✅ The UI is designed to surface “the map behind the map” and connect visuals to source/metadata. Keep previews and contracts lightweight so the UI can explain what the user is seeing without loading the full cube first.[^ui-trace]

---

## 🧾 Volume package contract (`volume.kfm.json`) — suggested minimum

KFM emphasizes **data contracts** for reliable downstream behavior.[^contract-first]  
Use this as a **site-local** contract for volumes (even if STAC/DCAT/PROV are the system-level contracts).

```json
{
  "kfm": {
    "schema_version": "0.1.0",
    "artifact_type": "volume"
  },
  "id": "gpr-amplitude-2025-10",
  "site": {
    "slug": "<site-slug>",
    "name": "Site Name"
  },
  "title": "GPR Amplitude Volume (Processed)",
  "summary": "Web-ready voxel cube aligned to site grid; includes preview slices and an isosurface derivative.",
  "method": {
    "domain": "archaeology",
    "technique": "gpr",
    "processing": [
      "time-zero correction",
      "background removal",
      "gain",
      "migration"
    ]
  },
  "spatial": {
    "crs": "EPSG:4326",
    "bbox_wgs84": [-100.0, 38.0, -99.9, 38.1],
    "vertical": {
      "datum": "local",
      "units": "m",
      "min": 0.0,
      "max": 3.0
    }
  },
  "grid": {
    "axis_order": "x,y,z",
    "voxel_size_m": [0.05, 0.05, 0.05],
    "shape": [800, 600, 60]
  },
  "time": {
    "survey_date": "2025-10-14"
  },
  "governance": {
    "sensitivity": "restricted",
    "display_policy": "generalized"
  },
  "assets": {
    "volume_root": "volume/",
    "previews": "previews/",
    "derivatives": "derivatives/"
  },
  "catalog": {
    "stac_item": "stac-item.json",
    "dcat": "dcat.json",
    "prov": "prov.jsonld"
  }
}
```

### 🔐 Sensitivity fields (don’t skip)
Policies and UI affordances depend on explicit labeling (sensitivity classification, handling rules, and access expectations).[^policy-gates][^sensitive-ui]

---

## 🌍 CRS + units (do not hand-wave)

- Prefer publishing **WGS84 / EPSG:4326** for UI interoperability, while tracking original CRS and processing transformations in provenance.[^crs]
- Always declare:
  - voxel spacing & units
  - vertical datum / interpretation of “depth”
  - axis order and orientation (is z increasing upward or downward?)

---

## 📦 Formats & delivery strategy

KFM’s UI stack supports 2D + 3D exploration, including Cesium-based 3D visualization and 3D Tiles streaming for 3D datasets.[^stack-2d-3d]  
For volumes, assume we need **progressive loading**, **preview-first UX**, and **multiple representations**:

| Need | Recommended artifact | Why |
|---|---|---|
| Fast UI previews | PNG slices + thumbnail | Loads instantly; supports “what is this?” UX |
| Interactive 3D “shape” | `isosurface.glb` (or point cloud tiles) | Great for Cesium/Three.js style viewing |
| Full voxel cube | Chunked volume (e.g., Zarr-like layout) | Progressive fetch; scalable |
| Map overlay | footprint/coverage GeoJSON | Lets UI show where the cube exists |
| Trust & repeatability | checksums + PROV + run manifest references | Auditable + reproducible |

> 🌦️ KFM already contemplates volumetric-style 3D representations (e.g., radar-like volumetric layers) in the broader 3D ecosystem; apply the same streaming mindset here.[^stack-2d-3d]

---

## 🏗️ Publishing workflow (how a volume should land here)

> This is intentionally aligned with KFM’s **controlled transformations → catalogs → UI** architecture.[^pipeline-order][^provenance-first]

1. 📥 **Ingest** raw survey exports into `data/raw/...` *as-received* (immutable evidence).[^provenance-first]
2. 🧰 **Transform** in `data/work/...` and publish deterministic outputs to `data/processed/...` (no manual edits).
3. 🧾 **Catalog** with STAC/DCAT/PROV so the cube is discoverable, indexable, and auditable.[^stac-dcat-prov]
4. 🚚 **Publish** web-facing assets into `web/assets/.../analysis/volumes/...` along with:
   - previews
   - an optional isosurface derivative
   - a lightweight local index (`_index.json`)
5. ✅ **Pass policy gates** (schema, license, sensitivity, provenance, citations).[^policy-gates]

---

## 🧪 Provenance + reproducibility extras (recommended)

### 🔎 Run manifest (audit trail)
KFM describes structured run manifests (tool versions, record counts, inputs/outputs, errors) saved under a run ID and used for policy checks and reproducibility.[^run-manifest]

If you generate a volume, include a pointer/reference to:

- `data/audits/<run_id>/run_manifest.json` (or equivalent in your repo layout)
- a canonical digest / idempotency key so the run can be uniquely identified and replayed deterministically.[^run-manifest]

### 📦 Large binaries: OCI artifact storage (optional but powerful)
For very large volumes that shouldn’t live directly in git, KFM proposes storing artifacts in an **OCI registry** using ORAS and signing with Cosign, fetching by immutable digests and attaching provenance as referrers.[^oci-artifacts]

This works well for:
- chunky volumes
- derived meshes/tilesets
- offline packs

---

## 🧑‍🤖 How Focus Mode should “talk about” volumes

KFM’s AI design is explicit:

- It **must cite sources** and refuse/qualify when evidence isn’t available.[^ai-citations]
- It is **context-aware** (map view + active layers + timeframe).[^ai-citations]
- It supports **explainable AI** patterns (audit panel, feature attributions, governance flags like sensitive-data notices).[^ai-citations]
- The graph is designed to use **standard ontologies** including **CIDOC‑CRM (cultural heritage)** + **GeoSPARQL** + **PROV‑O** so queries and relationships are unambiguous.[^ontologies]

**Practical rule for this folder:**  
If a volume is shown in UI, Focus Mode should be able to:
1) identify it,  
2) summarize it,  
3) explain how it was produced, and  
4) cite STAC/DCAT/PROV + run context.

---

## 🧵 Story Nodes + Pulse Threads: turning volume findings into narrative

KFM’s storytelling model ties narrative content to map state and encourages evidence-backed narratives.[^story-nodes]  
For volumes, two high-leverage patterns:

### 1) 🗺️ Story Node “volume walkthrough”
A Story Node is commonly represented as a folder with Markdown narrative + JSON map config; it can drive map/camera state while text explains the evidence.[^story-nodes]  
Use Story Nodes when you want a durable interpretation (e.g., “Subsurface anomaly suggests structure footprint”).

### 2) ⚡ Pulse Thread “new finding” (fast + geotagged)
Pulse Threads are a proposed content type for timely, location-specific narrative updates with attached provenance and evidence manifests—discoverable spatially in the UI.[^pulse-threads]

**Archaeology example:**  
> “New GPR slice cluster shows rectilinear anomaly at depth ~1.2m; flagged for follow-up excavation unit.”

---

## ✅ Contributor checklist (volumes)

- [ ] Volume is derived via deterministic pipeline (no manual binary edits).[^provenance-first]
- [ ] `volume.kfm.json` exists (recommended) and matches the actual assets.
- [ ] STAC + DCAT + PROV exist and cross-reference correctly.[^stac-dcat-prov]
- [ ] Sensitivity classification is explicit and appropriate.[^policy-gates][^sensitive-ui]
- [ ] Preview slices + thumbnail exist (UI-first).
- [ ] Checksums exist for major artifacts (volume root, meshes, previews).
- [ ] Any large artifact is either git-safe or referenced via OCI digest with signatures (if used).[^oci-artifacts]
- [ ] `_index.json` updated (if you use local indexing).

---

## 📚 Reference library (project docs used)

### Core KFM specs (design + architecture)
- 📘 Data intake philosophy, ordering, catalogs: STAC/DCAT/PROV + provenance-first pipeline.[^provenance-first][^pipeline-order][^stac-dcat-prov]
- 🧩 Contract-first + “no mystery layers” trust model.[^contract-first]
- 🗺️ UI principles: provenance surfaced to users; sensitive handling patterns; decoupled frontend architecture.[^ui-trace][^sensitive-ui]
- 🧭 AI system: citation enforcement, explainability, governance flags, and standard ontologies (CIDOC‑CRM / GeoSPARQL / PROV‑O).[^ai-citations][^ontologies]
- 🧰 Policy gates + FAIR/CARE alignment (including sensitivity and licensing requirements).[^policy-gates][^fair-care]
- 🧱 Story nodes + evidence manifests; rapid “Pulse Thread” narratives; run manifests and governance workflows.[^story-nodes][^pulse-threads][^run-manifest]

### Big “reading pack” portfolios (embedded libraries)
Some project PDFs are **PDF portfolios** (multiple embedded docs) and are meant to be opened in Acrobat/Adobe Reader to browse the embedded materials.[^portfolios]
- 🤖 AI concepts bundle (models, ML background)
- 🌐 Maps/WebGL/Virtual Worlds bundle (web rendering & geospatial graphics)
- 🧑‍💻 Programming languages bundle (implementation references)
- 🗃️ Data management & Bayesian bundle (uncertainty, data engineering ideas)

---

## 🔧 Appendix: PostGIS helper pattern (for footprints / coverage)
If you derive a 2D footprint or coverage polygon for a volume, export GeoJSON from PostGIS in the pipeline (example pattern):[^postgis-export]

```sql
-- Example pattern (adapt to your schema): export a geometry as GeoJSON
SELECT ST_AsGeoJSON(geom) AS geojson
FROM some_table
WHERE id = '<volume-id>';
```

---

# Footnotes / Evidence

[^contract-first]: KFM’s contract-first approach requires metadata/data contracts and rejects “mystery layers,” enabling citations and trust in UI/AI outputs.:contentReference[oaicite:0]{index=0}

[^provenance-first]: KFM data intake is “provenance-first,” treating `data/raw/` as immutable evidence and requiring deterministic, config/code-driven transformations downstream (no ad-hoc edits).:contentReference[oaicite:1]{index=1}

[^pipeline-order]: KFM enforces a controlled sequence of transformations and explicitly reinforces that bypassing the order is wrong; outputs remain traceable through catalogs and provenance.:contentReference[oaicite:2]{index=2}

[^stac-dcat-prov]: STAC, DCAT, and PROV are described as KFM’s metadata backbone for discoverability, spatial/temporal indexing, and reproducibility, and enable tracing from UI → catalog → PROV.:contentReference[oaicite:3]{index=3}

[^policy-gates]: KFM policy gates include schema validation, STAC/DCAT/PROV completeness, license presence, sensitivity classification, and provenance completeness, with “fail closed” behavior and citation enforcement for AI outputs.:contentReference[oaicite:4]{index=4}

[^ui-trace]: UI is designed for scientific rigor and user trust by linking visualizations to source data/metadata (“the map behind the map”), and it is decoupled from backend via APIs to remain modular/extensible.:contentReference[oaicite:5]{index=5}

[^stack-2d-3d]: KFM’s map stack integrates 2D (MapLibre) and 3D (Cesium) and supports streaming 3D Tiles for 3D datasets/terrain visualization, with provenance surfaced in visualization and time navigation.:contentReference[oaicite:6]{index=6}

[^sensitive-ui]: KFM UI/visualization design explicitly calls for governance cues like lock icons and generalized display (e.g., showing a hex/area instead of exact point for sensitive archaeological sites).:contentReference[oaicite:7]{index=7}

[^crs]: KFM standardizes on WGS84 for UI while tracking original CRS and serving standardized outputs, emphasizing explicit CRS handling.:contentReference[oaicite:8]{index=8}

[^ai-citations]: KFM Focus Mode: always cites sources, refuses/qualifies without evidence, is UI-context-aware (location/timeframe/layers), and includes explainable AI/audit surfaces with governance flags (including sensitive notices).:contentReference[oaicite:9]{index=9}

[^ontologies]: KFM’s knowledge graph follows standard ontologies including CIDOC‑CRM (cultural heritage), GeoSPARQL (spatial), and PROV‑O (provenance) to clarify relationships and support AI interpretation.:contentReference[oaicite:10]{index=10}

[^fair-care]: KFM governance summarizes FAIR/CARE alignment and explicitly respects sensitive data governance and community authority for use (CARE principles).:contentReference[oaicite:11]{index=11}

[^kfm-ml]: KFM analytics may use ML models but emphasizes explainability, model documentation, citations, and confidence intervals/limitations for insights.:contentReference[oaicite:12]{index=12}

[^run-manifest]: Run manifests are described as structured ledgers saved under `data/audits/<run_id>/run_manifest.json`, including tool versions and counts; canonicalization/hashing (RFC 8785) supports idempotency and provenance linkage.:contentReference[oaicite:13]{index=13}

[^oci-artifacts]: KFM proposes packaging large artifacts into OCI registries via ORAS and signing with Cosign so artifacts are content-addressable (digest) and verifiable; provenance can be attached as referrers (including PROV JSON‑LD).:contentReference[oaicite:14]{index=14}:contentReference[oaicite:15]{index=15}

[^story-nodes]: Story Nodes are described as narrative building blocks combining Markdown content with configuration defining map layers/camera state; evidence manifests + PROV bundles are proposed to formalize narrative citations and verification.:contentReference[oaicite:16]{index=16}:contentReference[oaicite:17]{index=17}

[^pulse-threads]: Pulse Threads are described as geotagged, timely narrative updates stored as graph nodes with attached provenance and evidence manifests, discoverable spatially in UI and suitable for human-in-the-loop review. :contentReference[oaicite:18]{index=18}

[^postgis-export]: Example pattern for exporting GeoJSON from PostGIS (e.g., `ST_AsGeoJSON`) appears in the project’s geospatial cookbook material. :contentReference[oaicite:19]{index=19}

[^portfolios]: Several project PDFs are PDF portfolios intended to be opened in Acrobat/Adobe Reader to access embedded documents (AI, WebGL/Maps/Archaeology graphics, programming resources, data management/Bayesian ideas).

