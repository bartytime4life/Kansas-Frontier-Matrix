---
title: "🗺️ Kansas Frontier Matrix — LiDAR & GLO Integration Field Guide (v1.1)"
path: "docs/workflows/lidar-glo-integration.md"

version: "v11.2.6"
last_updated: "2025-12-11"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · Autonomous"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
signature_ref: "releases/v11.2.6/signature.sig"
attestation_ref: "releases/v11.2.6/slsa-attestation.json"
sbom_ref: "releases/v11.2.6/sbom.spdx.json"
manifest_ref: "releases/v11.2.6/manifest.zip"
data_contract_ref: "docs/contracts/data-contract-v3.json"
telemetry_ref: "releases/v11.2.6/lidar-glo-integration-telemetry.json"
telemetry_schema: "schemas/telemetry/lidar-glo-integration-workflow-v11.2.6.json"
energy_schema: "schemas/telemetry/energy-v2.json"
carbon_schema: "schemas/telemetry/carbon-v2.json"

governance_ref: "../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

status: "Active / Enforced"
doc_kind: "Guide"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"
  - "mermaid-timeline-v1"

scope:
  domain: "geospatial-workflows"
  applies_to:
    - "data/raw/lidar/**"
    - "data/raw/glo_plats/**"
    - "data/processed/lidar/**"
    - "data/processed/glo/**"
    - "src/pipelines/geospatial/**"

fair_category: "F1-A1-I2-R2"
care_label: "FAIR+CARE Governance Aligned"
sensitivity: "Potentially sensitive cultural features; auto-mask rules apply"
sensitivity_level: "Medium"
public_exposure_risk: "Moderate"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

ttl_policy: "24 months"
sunset_policy: "Superseded by LiDAR & GLO Integration Field Guide v2"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/workflows/lidar-glo-integration.md@v10.1.0"
  - "docs/workflows/lidar-glo-integration.md@v1.0.0"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "schemas/json/kfm-markdown-protocol-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/kfm-markdown-protocol-v11.2.4-shape.ttl"
story_node_refs: []

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:workflows:lidar-glo-integration:v11.2.6"
semantic_document_id: "kfm-lidar-glo-integration-field-guide-v11.2.6"
event_source_id: "ledger:kfm:doc:workflows:lidar-glo-integration:v11.2.6"
doc_integrity_checksum: "<sha256>"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "3d-context-render"
  - "a11y-adaptations"
  - "diagram-extraction"
  - "metadata-extraction"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"
transform_registry:
  allowed:
    - "summary"
    - "timeline-generation"
    - "semantic-highlighting"
    - "3d-context-render"
    - "a11y-adaptations"
    - "diagram-extraction"
    - "metadata-extraction"
  prohibited:
    - "content-alteration"
    - "speculative-additions"
    - "unverified-architectural-claims"
    - "narrative-fabrication"
    - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "🧭 Context"
    - "🗺️ Diagrams"
    - "🧠 Story Node & Focus Mode Integration"
    - "🧪 Validation & CI/CD"
    - "📦 Data & Metadata"
    - "🌐 STAC, DCAT & PROV Alignment"
    - "🧱 Architecture"
    - "⚖ FAIR+CARE & Governance"
    - "🕰️ Version History"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "metadata-check"
  - "diagram-check"
  - "accessibility-check"
  - "provenance-check"
  - "footer-check"

ci_integration:
  workflow: ".github/workflows/geospatial-lidar-glo.yml"
  environment: "dev → staging → production"

branding_registry:
  standard: "Scientific Insight × FAIR+CARE Ethics × Sustainable Intelligence"
  architecture: "Designed for Longevity · Governed for Integrity"
  analysis: "Research-Driven · Evidence-Led · FAIR+CARE Grounded"
  data-spec: "Open Data × Responsible Stewardship"
  pipeline: "Deterministic Pipelines · Explainable AI · Open Provenance"
  telemetry: "Transparent Systems · Ethical Metrics · Sustainable Intelligence"
  graph: "Semantics × Provenance × Spatial Intelligence"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

badge_profiles:
  - "root-centered-badge-row"

requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true

deprecated_fields:
  - "old_markdown_standard_v10.4"
---

<div align="center">

# 🗺️ **Kansas Frontier Matrix — LiDAR & GLO Integration Field Guide**  
`docs/workflows/lidar-glo-integration.md`

**Purpose**  
Define a **FAIR+CARE-aligned workflow** for fusing **bare-earth LiDAR** terrain products with **19th-century General Land Office (GLO) plats** to locate and document historical features (settlements, roads, field boundaries) across Kansas.  
This guide provides a **reproducible, auditable** method that feeds results into the **KFM Knowledge Graph**, STAC/DCAT catalogs, and Focus Mode.

<img src="https://img.shields.io/badge/Docs-MCP--DL_v6.3-blueviolet" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.4-purple" />
<img src="https://img.shields.io/badge/Data-FAIR%2BCARE-gold" />
<img src="https://img.shields.io/badge/License-CC--BY%204.0-green" />
<img src="https://img.shields.io/badge/Status-Operational-brightgreen" />

</div>

---

## 📘 Overview

### 1. Scope & Intent

Bare-earth **LiDAR-derived DTMs** expose subtle microtopography—berms, ditches, mounds, wagon ruts—often corresponding to cultural features mapped in **GLO plats (ca. 1854–1900)**.  
By georeferencing GLO plats to **PLSS** and overlaying them with derived terrain products (hillshade, SVF, slope, MDI), this workflow supports:

- Systematic **discovery and documentation** of historic features.  
- Consistent **FAIR+CARE handling** of potentially sensitive cultural sites.  
- Direct publication into **STAC/DCAT** and ingestion into the **KFM Neo4j** graph.  

Within the KFM pipeline:

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j knowledge graph → API layer → React/MapLibre/Cesium frontend → Story Nodes → Focus Mode

this guide defines the **geospatial ETL and analysis segment** for LiDAR × GLO fusion.

### 2. High-Level Phases

1. **Ingest & Normalize** LiDAR DEMs and GLO plats.  
2. **Derive Terrain Layers**: hillshade, MDI, SVF, slope, contours.  
3. **Georeference** GLO plats to PLSS and align rasters.  
4. **Overlay & Interpret**: compare plats and terrain for candidate features.  
5. **Digitize & Attribute** features with FAIR+CARE and sovereignty tags.  
6. **Publish & Ingest** into STAC/DCAT and Neo4j; register Story Nodes.

---

## 🗂️ Directory Layout

~~~text
📁 KansasFrontierMatrix/
├── 📚 docs/                                   # Documentation (standards, workflows, guides)
│   └── ⚙️ workflows/
│       📄 README.md                           # Workflows index
│       📄 lidar-glo-integration.md            # 🗺️ LiDAR & GLO integration field guide (this file)
│
├── 🗂️ data/
│   ├── 📁 raw/                                # Immutable source data (DVC/LFS)
│   │   ├── 📡 lidar/                          # LiDAR DEM tiles (GeoTIFF, LAZ)
│   │   └── 🧭 glo_plats/                      # GLO plats (TIFF, PDF, GeoTIFF) + field notes
│   ├── 📁 processed/
│   │   ├── 🏔️ lidar/                         # Mosaics, hillshades, MDI, SVF, slope, contours
│   │   └── 🧾 glo/                            # Georeferenced plats, digitized vectors, QA masks
│   └── 📁 work/
│       └── 🧪 staging/
│           └── 🗺️ geospatial/                 # Intermediates & scratch rasters
│
├── 🧩 src/
│   └── 🌐 pipelines/
│       └── 🗺️ geospatial/
│           📄 lidar_glo_pipeline.py           # Orchestrates LiDAR × GLO ETL/analysis
│           📄 lidar_derivatives.py            # Derives hillshade/MDI/SVF/slope rasters
│           📄 glo_georef.py                   # GLO georeferencing & PLSS alignment
│
├── 📊 outputs/
│   ├── 🧮 analysis/
│   │   ├── 🏔️ terrain/                       # Slope, SVF, MDI, contours, QA maps
│   │   └── 🏛️ historic/                      # Digitized features, overlays, interpretation notes
│   └── 🧱 tiles/
│       └── 🗺️ web/
│           📄 *.pmtiles                       # Vector/raster tiles for MapLibre/Cesium
│
└── 📦 releases/
    └── 📁 v11.2.6/
        📄 lidar-glo-integration-telemetry.json  # Telemetry for this workflow
        📄 sbom.spdx.json                        # Geospatial tooling SBOM
        📄 manifest.zip                          # ETL configs, checksums, provenance pointers
~~~

---

## 🧭 Context

### 1. Kansas LiDAR & GLO Landscape

- **LiDAR** (USGS 3DEP, Kansas DASC) provides statewide bare-earth DTMs.  
- **GLO plats** record 19th-century property boundaries, roads, schools, mills, and other structures.  
- **PLSS (Township–Range–Section)** is the common spatial frame linking survey records with modern data.

Combining these sources enables:

- Reconstruction of **historic transportation networks**.  
- Identification of **settlement clusters** and agricultural patterns.  
- Support for **cultural heritage management**, including tribal concerns.

### 2. Integration with KFM Systems

- **ETL layer**  
  - `src/pipelines/geospatial/lidar_glo_pipeline.py` reads from `data/raw/**` and writes to `data/processed/**` and `outputs/analysis/**`.

- **Catalogs**  
  - Processed rasters/vectors are indexed as STAC Items and DCAT Datasets (see **🌐 STAC, DCAT & PROV Alignment**).

- **Graph**  
  - Features become nodes and relationships in Neo4j with full provenance and CARE tags.

- **Frontend & Focus Mode**  
  - MapLibre/Cesium frontends consume PMTiles and GeoJSON from `outputs/tiles/web/`.  
  - Focus Mode presents Story Nodes about specific features, townships, or workflows.

---

## 🗺️ Diagrams

### 1. LiDAR & GLO Integration Flow

~~~mermaid
flowchart LR
    A["LiDAR DEM Import"] --> B["Bare-Earth Derivatives (Hillshade · MDI)"]
    B --> C["SVF · Slope · Contours"]
    C --> D["GLO Plat Import"]
    D --> E["Georeference to PLSS (section corners · hydro)"]
    E --> F["Overlay & Compare (transparency · blend modes)"]
    F --> G["Anomaly Review (multi-illumination QA)"]
    G --> H["Digitize · Attribute · FAIR+CARE Tagging"]
    H --> I["Publish (STAC/DCAT) · Ingest (Neo4j) · Register for Focus Mode"]
~~~

### 2. Run Timeline (Per Township / AOI)

~~~mermaid
timeline
    title LiDAR & GLO Integration — Run Lifecycle
    section ETL & Prep
      T0 : Ingest raw LiDAR and GLO plats
      T1 : Normalize DEMs and generate derivatives
    section Interpretation
      T2 : Georeference GLO to PLSS
      T3 : Overlay terrain + plats and inspect anomalies
      T4 : Digitize and attribute features
    section Publication & Governance
      T5 : STAC/DCAT export and validation
      T6 : Neo4j ingest and Story Node registration
      T7 : FAIR+CARE review and telemetry update
~~~

---

## 🧠 Story Node & Focus Mode Integration

### 1. Story Node Types

LiDAR × GLO integration produces several Story Node classes:

- **Feature discovery nodes**  
  - `urn:kfm:story-node:geo:lidar-glo:feature:<feature_uuid>`  
  - Explain how a specific road, mound, ditch, or field boundary was identified.

- **Area synthesis nodes**  
  - `urn:kfm:story-node:geo:lidar-glo:township:<trs_id>`  
  - Summarize features, interpretations, and caveats for a township/area.

- **Methodology nodes**  
  - `urn:kfm:story-node:geo:lidar-glo:method:v1_1`  
  - Describe the method defined by this guide and its constraints.

Each Story Node links back to:

- STAC/DCAT records for rasters, vectors, and reports.  
- Neo4j entities (`:Place`, `:Feature`, `:SurveyEvent`, `:Document`).  
- This document (`semantic_document_id`).

### 2. Focus Mode Behavior

When Focus Mode is activated on an area or feature:

- **MAY**:
  - Summarize the LiDAR × GLO evidence supporting a feature.  
  - Show evolution through time (e.g., plat → historic aerials → modern imagery).  
  - Surface FAIR+CARE and sovereignty notes for the site.

- **MUST NOT**:
  - Reveal coordinates of sites tagged as `sensitive` beyond what governance allows.  
  - Infer historical claims not grounded in curated data and documented interpretations.  
  - Override or reinterpret CARE tags or sovereignty rules.

---

## 🧪 Validation & CI/CD

### 1. Workflow Hooks

LiDAR × GLO pipelines should be wired into CI/CD as follows:

- On changes to `data/raw/lidar/**` or `data/raw/glo_plats/**`:
  - Run:
    - `faircare-validate.yml` for FAIR+CARE and sovereignty checks.  
    - `stac-validate.yml` after STAC Items are generated.

- On changes to this guide or related schemas:
  - Run:
    - `docs-lint.yml` for KFM-MDP v11.2.4 compliance.  
    - `schema-lint.yml` for geospatial schema updates.

### 2. Quality Assurance Checklist

- [ ] LiDAR DTM aligned to expected CRS (e.g., EPSG:26914) and pixel grid.  
- [ ] GLO georeference RMS within documented tolerance (e.g., 3–10 m) with control points recorded.  
- [ ] SVF / MDI / slope layers generated and visually inspected.  
- [ ] Features digitized with attributes:
  - `feature_id`, `feature_type`, `source_sheet_id`, `source_epoch`, `confidence`.  
- [ ] STAC/DCAT Items validated (STAC validator + schema checks).  
- [ ] `care_tag` assigned (`public`, `restricted`, `sensitive`) and reviewed.  
- [ ] Sensitive sites generalized or withheld according to sovereignty policy.  
- [ ] Neo4j ingest tests completed; Focus Mode summaries match underlying features.

### 3. Telemetry

Per run (per AOI / township), append telemetry to  
`releases/v11.2.6/lidar-glo-integration-telemetry.json`, for example:

- `tiles_processed`  
- `features_detected` vs. `features_accepted`  
- `sensitive_features_count`  
- `workflow_duration_sec`, `energy_wh`, `carbon_gco2e`

These metrics help governance track cost, coverage, and sensitivity trends.

---

## 📦 Data & Metadata

### 1. Core Data Sources

| Dataset                  | Provider                 | Typical Format          |
|-------------------------:|-------------------------|-------------------------|
| LiDAR Bare-Earth DEM     | Kansas DASC / USGS 3DEP | GeoTIFF, LAZ            |
| PLSS Grids (TRS)         | KDOT / DASC             | GeoPackage, Shapefile   |
| GLO Plats & Field Notes  | BLM GLO Records         | TIFF, PDF, GeoTIFF      |
| Hydrography (NHDPlus)    | USGS                    | FileGDB, GeoPackage     |
| Historic Aerials / Topos | USGS / archives         | GeoTIFF                 |

### 2. Feature Schema (Vectors)

Digitized features in `data/processed/glo/` (GPKG/GeoJSON) should include:

| Field             | Type     | Description                          |
|------------------:|----------|--------------------------------------|
| `feature_id`      | UUID     | Stable identifier                    |
| `feature_type`    | string   | e.g., `road`, `ditch`, `mound`       |
| `source_epoch`    | integer  | e.g., 1882 (GLO survey year)         |
| `source_sheet_id` | string   | GLO plat sheet identifier            |
| `elevation_ref`   | float    | LiDAR-derived elevation (m)          |
| `confidence`      | float    | 0–1 confidence score                 |
| `care_tag`        | string   | `public`, `restricted`, `sensitive`  |
| `notes`           | string   | Analyst notes and caveats            |

### 3. Raster Derivatives

Common outputs in `data/processed/lidar/` and `outputs/analysis/terrain/`:

- `*_dtm.tif` — bare-earth DTM.  
- `*_hillshade_mdi.tif` — multi-directional hillshade.  
- `*_svf.tif` — sky-view factor.  
- `*_slope.tif` — slope (degrees).  
- `*_contours.gpkg` — derived contour lines.

All rasters should include:

- CRS metadata (`EPSG`),  
- Pixel size, nodata values,  
- `CHECKSUM` / hash where tools allow.

---

## 🌐 STAC, DCAT & PROV Alignment

### 1. STAC

- **Collections**:
  - `kfm-lidar` — LiDAR derivatives (DTM, hillshade, SVF, slope).  
  - `kfm-glo` — GLO plats and digitized feature vectors.

- **Items**:
  - Per tile or township-level coverage:
    - `id`: `<collection>-<tile_id>` or `<trs_id>`.  
    - `geometry` / `bbox`: coverage extent.  
    - `properties.datetime`: acquisition or survey date when known.  

- **Assets**:
  - `dtm`, `hillshade_mdi`, `svf`, `slope`, `contours`, `glo-plat`, `glo-vectors`.  
  - Include:
    - `proj:*` for CRS and grid.  
    - `checksum:multihash` for integrity.  
    - `kfm:care_tag` for sensitivity.

### 2. DCAT

Define DCAT Datasets like:

- **"KFM LiDAR-Derived Terrain Products for Kansas"**  
- **"KFM GLO-Derived Historic Features"**

Required fields:

- `dct:title`, `dct:description`, `dct:identifier`.  
- `dct:license` (e.g., CC-BY 4.0).  
- `dct:spatial` (Kansas or local region).  
- `dct:temporal` (survey intervals).  

Distributions reference:

- COGs, GeoPackages, PMTiles, and QA reports.  
- Telemetry and FAIR+CARE summaries for governance.

### 3. PROV

For each LiDAR × GLO run:

- **Entities**:
  - LiDAR tiles, GLO sheets, derived rasters, vector features, QA reports.

- **Activities**:
  - `ex:LidarPreprocess_<run_id>`  
  - `ex:GloGeoref_<run_id>`  
  - `ex:LidarGloFusion_<run_id>`

- **Agents**:
  - `ex:KFM_Geospatial_Pipeline` (software agent).  
  - `ex:KFM_GeoTeam` (analysts).  
  - `ex:TribalReviewBody` (governance actor) where applicable.

PROV relations link all entities and activities, making it possible to reconstruct how each feature was derived and reviewed.

---

## 🧱 Architecture

### 1. Pipeline Structure

- **ETL & analysis** (`src/pipelines/geospatial/`):
  - `lidar_glo_pipeline.py` orchestrates:
    - LiDAR ingest, resampling, and derivative generation.  
    - GLO plat georeferencing with PLSS and hydrography control.  
    - Feature detection (human and AI-assisted) and digitization.

- **Config & contracts**:
  - YAML configs define AOIs, resolutions, thresholds, and masks.  
  - `docs/contracts/data-contract-v3.json` governs attribute and structural requirements.

- **Graph & API**:
  - Graph loaders create or update `:Place`, `:Feature`, `:SurveyEvent`, and `:Document` nodes.  
  - APIs surface summarized results and geometry-filtered outputs to the frontend.

### 2. Determinism & Reproducibility

- Use **config-driven runs**:
  - `configs/geospatial/lidar_glo_<aoi>.yaml` for each AOI.  
- Log:
  - Input file lists and checksums.  
  - Tool versions (GDAL/PDAL/QGIS).  
  - Important parameters (e.g., MDI illumination angles, SVF parameters).  
- Ensure that re-running the pipeline with the same config and inputs reproduces outputs within numerical tolerances.

---

## ⚖ FAIR+CARE & Governance

### 1. FAIR

| Principle        | Implementation                                                |
|-----------------:|---------------------------------------------------------------|
| **Findable**     | UUIDs, STAC/DCAT catalogs, consistent directory layout       |
| **Accessible**   | CC-BY assets, documented access rules for restricted layers  |
| **Interoperable**| Standard CRS, open formats (COG, GPKG, GeoJSON, PMTiles)     |
| **Reusable**     | Clear provenance, checksums, versioned configs, AI model cards |

### 2. CARE

| Principle              | Implementation                                            |
|-----------------------:|-----------------------------------------------------------|
| **Collective Benefit** | Supports preservation, education, and tribal priorities  |
| **Authority to Control** | `care_tag` and sovereignty policies gate publication |
| **Responsibility**     | Redaction, generalization, or non-publication of sensitive sites |
| **Ethics**             | Human-in-the-loop review; AI detections are advisory     |

### 3. Governance Flow

- LiDAR × GLO outputs enter the **FAIR+CARE validation workflow** (see `faircare-validate.yml`).  
- Sensitive or contentious features can be:
  - Quarantined,  
  - Generalized, or  
  - Marked for council review.  

Governance decisions are mirrored in:

- Neo4j (governance relationships).  
- Telemetry and audit logs.

---

## 🕰️ Version History

| Version    | Date       | Author      | Summary                                                                                 |
|-----------:|------------|------------|-----------------------------------------------------------------------------------------|
| **v11.2.6** | 2025-12-11 | `@kfm-geo` | Aligned to KFM v11.2.6; updated release & telemetry paths, emoji directory layout, and footer/navigation profile; preserved v1.1 methodological content. |
| v11.2.4   | 2025-12-06 | `@kfm-geo`  | Aligned with KFM-MDP v11.2.4; updated directory layout to emoji/tree profile; added STAC/DCAT/PROV alignment, Story Node hooks, telemetry wiring, and CI/CD integration notes. |
| v10.1.0   | 2025-11-10 | `@kfm-geo`  | Added MDI workflow, DCAT mirror, CARE tags; aligned with v10.1.0 telemetry & governance. |
| v1.0.0    | 2025-11-08 | `@kfm-geo`  | Initial publication — LiDAR + GLO integration guide.                                   |

---

<div align="center">

🗺️ **Kansas Frontier Matrix — LiDAR & GLO Integration Field Guide (v1.1 · doc v11.2.6)**  
Geospatial Insight · FAIR+CARE Governance · Cultural Stewardship  

<img src="https://img.shields.io/badge/Docs-MCP--DL_v6.3-blue" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.4-purple" />
<img src="https://img.shields.io/badge/Data-FAIR%2BCARE-gold" />
<img src="https://img.shields.io/badge/Workflow-lidar_glo_integration_v11.2.6-informational" />

[⬅ Back to Workflows Index](./README.md) ·  
[📘 Docs Root](../README.md) ·  
[📚 Glossary](../glossary.md) ·  
[📐 Markdown Protocol (KFM-MDP v11.2.4)](../standards/kfm_markdown_protocol_v11.2.4.md) ·  
[⚖ Governance Charter](../standards/governance/ROOT-GOVERNANCE.md) ·  
[🤝 FAIR+CARE Guide](../standards/faircare/FAIRCARE-GUIDE.md)

  
© 2025 Kansas Frontier Matrix — CC-BY 4.0 for this document  
MCP-DL v6.3 · KFM-MDP v11.2.4 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω  

</div>
