---
title: "🗺️ Kansas Frontier Matrix — LiDAR & GLO Integration Field Guide (v1.1)"
path: "docs/workflows/lidar-glo-integration.md"

version: "v11.2.4"
last_updated: "2025-12-06"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · Autonomous"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
signature_ref: "releases/v11.2.4/signature.sig"
attestation_ref: "releases/v11.2.4/slsa-attestation.json"
sbom_ref: "releases/v11.2.4/sbom.spdx.json"
manifest_ref: "releases/v11.2.4/manifest.zip"
data_contract_ref: "docs/contracts/data-contract-v3.json"
telemetry_ref: "releases/v11.2.4/lidar-glo-integration-telemetry.json"
telemetry_schema: "schemas/telemetry/lidar-glo-integration-workflow-v11.2.4.json"
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
doc_uuid: "urn:kfm:doc:workflows:lidar-glo-integration:v11.2.4"
semantic_document_id: "kfm-lidar-glo-integration-field-guide-v11.2.4"
event_source_id: "ledger:kfm:doc:workflows:lidar-glo-integration:v11.2.4"
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
Define a **FAIR+CARE‑aligned workflow** for fusing **bare‑earth LiDAR** terrain products with **19th‑century General Land Office (GLO) plats** to locate and document historical features (settlements, roads, field boundaries) across Kansas.  
This guide provides a **reproducible, auditable** method that feeds results into the **KFM Knowledge Graph**, STAC/DCAT catalogs, and Focus Mode.

<img src="https://img.shields.io/badge/Docs-MCP--DL_v6.3-blueviolet" />
<img src="https://img.shields.io-badge/KFM--MDP-v11.2.4-purple" />
<img src="https://img.shields.io/badge/License-CC--BY%204.0-green" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Certified-orange" />
<img src="https://img.shields.io/badge/Status-Operational-brightgreen" />

</div>

---

## 📘 Overview

### 1. Scope & Intent

Bare‑earth **LiDAR‑derived DTMs** expose subtle microtopography—berms, ditches, mounds, wagon ruts—often corresponding to cultural features mapped in **GLO plats (ca. 1854–1900)**.  
By georeferencing GLO plats to **PLSS** and overlaying them with derived terrain products (hillshade, SVF, slope, MDI), this workflow supports:

- Systematic **discovery and documentation** of historic features.  
- Consistent **FAIR+CARE handling** of potentially sensitive cultural sites.  
- Direct publication into **STAC/DCAT** and ingestion into the **KFM Neo4j** graph.  

Within the KFM pipeline:

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j knowledge graph → API layer → React/MapLibre/Cesium frontend → Story Nodes → Focus Mode

this guide defines the **geospatial ETL and analysis segment** for LiDAR × GLO fusion.

### 2. High-Level Workflow (Conceptual)

At a high level, the process:

1. Ingest and normalize **LiDAR DEMs** and **GLO plats**.  
2. Derive enhanced terrain layers (hillshade, MDI, SVF, slope, contours).  
3. Georeference GLO plats to PLSS and align to the LiDAR grid.  
4. Overlay plats and terrain to identify candidate features.  
5. Digitize and attribute features, including **FAIR+CARE and sovereignty tags**.  
6. Export to STAC/DCAT, ingest to Neo4j, and register for Focus Mode use.

---

## 🗂️ Directory Layout

~~~text
docs/workflows/lidar-glo-integration.md      # ← This field guide

data/
├── raw/
│   ├── lidar/                               # LiDAR DEM tiles (GeoTIFF, LAZ)
│   └── glo_plats/                           # GLO plats (TIFF, PDF, GeoTIFF) + field notes
├── processed/
│   ├── lidar/                               # Mosaics, hillshades, MDI, SVF, slope, contours
│   └── glo/                                 # Georeferenced plats + digitized vectors
└── work/
    └── staging/
        └── geospatial/                      # Intermediate rasters, masks, QA outputs

src/
└── pipelines/
    └── geospatial/
        ├── lidar_glo_pipeline.py            # Batch ETL/orchestration entrypoint
        ├── lidar_derivatives.py             # RVT/MDI/SVF/slope helpers
        └── glo_georef.py                    # GLO georeferencing and alignment

outputs/
├── analysis/
│   ├── terrain/                             # Slope, SVF, MDI, contours
│   └── historic/                            # Digitized features, overlays, QA maps
└── tiles/
    └── web/                                 # PMTiles / vector tiles for frontend
~~~

---

## 🧭 Context

### 1. Kansas LiDAR & GLO Landscape

- **LiDAR** (e.g., USGS 3DEP, Kansas DASC) provides statewide bare‑earth DTMs.  
- **GLO plats** record 19th‑century property boundaries, roads, schools, mills, and other structures.  
- **PLSS (Township–Range–Section)** is the key common spatial framework.  

Combining these sources enables:

- Reconstruction of **historic transportation networks**.  
- Identification of **settlement clusters** and agricultural patterns.  
- Support for **cultural heritage management**, including tribal concerns.

### 2. Integration with KFM Systems

- **ETL layer**: `src/pipelines/geospatial/lidar_glo_pipeline.py` reads from `data/raw/*` and writes to `data/processed/*` and `outputs/analysis/*`.  
- **Catalogs**: processed rasters/vectors are indexed as STAC Items and DCAT Datasets.  
- **Graph**: features become nodes and relationships in Neo4j with full provenance.  
- **Frontend & Focus Mode**: MapLibre/Cesium frontends consume tiles and Story Nodes to guide users through historic landscapes.

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

---

## 🧠 Story Node & Focus Mode Integration

### 1. Story Node Types

LiDAR × GLO integration produces Story Nodes such as:

- **Feature discovery nodes**  
  - e.g., `urn:kfm:story-node:geo:lidar-glo:feature:<feature_uuid>`  
  - Narrative: how a road, mound, or ditch was identified.  

- **Area synthesis nodes**  
  - e.g., `urn:kfm:story-node:geo:lidar-glo:township:<trs_id>`  
  - Summary: major features and interpretation for a township.  

- **Methodology nodes**  
  - e.g., `urn:kfm:story-node:geo:lidar-glo:method:v1_1`  
  - High‑level description of the workflow in this guide.

Each Story Node links back to:

- STAC/DCAT records (rasters, vectors, reports).  
- Neo4j entities (places, events, documents).  
- This guide via `semantic_document_id`.

### 2. Focus Mode Behavior

When Focus Mode is activated on an area or feature:

- **May**:
  - Summarize the local LiDAR × GLO evidence.  
  - Show how features evolved across time (via timelines).  
  - Surface FAIR+CARE and sovereignty notes for the site.

- **Must not**:
  - Reveal redacted locations or override `care_tag` and sovereignty rules.  
  - Infer historical claims not grounded in data and documented interpretations.

---

## 🧪 Validation & CI/CD

### 1. Workflow Hooks

LiDAR × GLO pipelines should be integrated into CI/CD as follows:

- **On data changes** (`data/raw/lidar/**`, `data/raw/glo_plats/**`):
  - Run:
    - `faircare-validate.yml` for FAIR+CARE and sovereignty checks.  
    - `stac-validate.yml` once STAC Items are emitted.  

- **On guide or schema changes**:
  - Run:
    - `docs-lint.yml` for KFM‑MDP v11.2.4 compliance.  
    - `schema-lint.yml` for JSON/SHACL schemas used by the pipeline.

### 2. Quality Assurance Checklist

Use this checklist as part of the QA step in the pipeline:

- [ ] LiDAR DTM aligned to expected CRS (e.g., EPSG:26914) and grid.  
- [ ] GLO georeference RMS within documented tolerance (e.g., 3–10 m); control points archived.  
- [ ] SVF/MDI/slope layers generated and visually reviewed.  
- [ ] Features digitized with attributes:
  - `feature_id`, `feature_type`, `confidence`, `source_raster`, `source_glo_sheet`.  
- [ ] STAC/DCAT Items validated by `stac-validate.yml`.  
- [ ] `care_tag` assigned (`public`, `restricted`, `sensitive`) and reviewed.  
- [ ] Sensitive sites (e.g., burial mounds) generalised or withheld per policy.  
- [ ] Neo4j ingest tested; Focus Mode summaries verified against underlying data.

### 3. Telemetry

The LiDAR × GLO pipeline may emit telemetry records (e.g., `lidar-glo-integration-telemetry.json`) including:

- Number of tiles processed, features detected, features accepted.  
- Runtime, energy, and carbon estimates.  
- Counts of features by `care_tag` for governance monitoring.

---

## 📦 Data & Metadata

### 1. Data Sources

| Dataset                  | Provider                 | Typical Format      |
|-------------------------:|-------------------------|---------------------|
| LiDAR Bare-Earth DEM     | Kansas DASC / USGS 3DEP | GeoTIFF, LAZ        |
| PLSS Grids (TRS)         | KDOT / DASC             | GeoPackage, Shapefile |
| GLO Plats & Field Notes  | BLM GLO Records         | TIFF, PDF, GeoTIFF  |
| Hydrography (NHDPlus)    | USGS                    | GDB, GeoPackage     |
| Historic Aerials / Topos | USGS / archives         | GeoTIFF             |

### 2. Feature Schema (Vectors)

Digitized features in `data/processed/glo/` should include:

| Field             | Type     | Description                          |
|------------------:|----------|--------------------------------------|
| `feature_id`      | UUID     | Stable identifier                    |
| `feature_type`    | string   | e.g., `road`, `ditch`, `mound`       |
| `source_epoch`    | integer  | e.g., 1882 (GLO survey year)         |
| `source_sheet_id` | string   | GLO plat sheet identifier            |
| `elevation_ref`   | float    | LiDAR‑derived elevation (m)          |
| `confidence`      | float    | 0–1 confidence score                 |
| `care_tag`        | string   | `public`, `restricted`, `sensitive`  |
| `notes`           | string   | Analyst notes and caveats            |

### 3. Raster Derivatives

Common outputs in `data/processed/lidar/` and `outputs/analysis/terrain/`:

- `*_dtm.tif` — bare‑earth DTM.  
- `*_hillshade_mdi.tif` — multi‑directional hillshade.  
- `*_svf.tif` — sky‑view factor.  
- `*_slope.tif` — slope in degrees.  
- `*_contours.gpkg` — derived contour lines.

---

## 🌐 STAC, DCAT & PROV Alignment

### 1. STAC

- **Collections**:
  - `kfm-lidar` — LiDAR derivatives.  
  - `kfm-glo` — GLO plats and digitized vectors.  

- **Items**:
  - One STAC Item per tile or township-scale coverage:
    - `id`: `<collection>-<tile_id>` or `<trs_id>`.  
    - `geometry` / `bbox`: coverage extent (typically township or tile).  
    - `properties.datetime`: acquisition or survey date when known.

- **Assets**:
  - `dtm`, `hillshade_mdi`, `svf`, `slope`, `contours`.  
  - `glo-plat`, `glo-vectors`.  
  - Include:
    - `proj:*` fields for CRS and grid.  
    - `checksum:multihash` for integrity.  
    - `kfm:care_tag` for sensitivity.

### 2. DCAT

- Define DCAT Datasets such as:

  - **"LiDAR‑Derived Terrain Products for Kansas (KFM)"**  
  - **"GLO Plat‑Derived Historic Features (KFM)"**

- Core fields:

  - `dct:title`, `dct:description`, `dct:identifier`.  
  - `dct:license` (CC‑BY 4.0 or source license).  
  - `dct:spatial` (Kansas or local extents).  
  - `dct:temporal` (survey dates).  

Distributions reference:

- COGs, GeoPackages, PMTiles, and reports.  
- Telemetry and QA summaries where appropriate.

### 3. PROV

For each processing run:

- **Entities**:
  - LiDAR source tiles, GLO sheets, derived rasters, digitized vectors, QA reports.  

- **Activities**:
  - `ex:LidarPreprocess_<run_id>`  
  - `ex:GloGeoref_<run_id>`  
  - `ex:LidarGloFusion_<run_id>`

- **Agents**:
  - `ex:KFM_Geospatial_Pipeline` (software).  
  - `ex:KFM_GeoTeam` (analysts).

Key relations:

- Derived entities `prov:wasGeneratedBy` activities.  
- Activities `prov:used` source entities.  
- Entities and activities `prov:wasAssociatedWith` agents.

---

## 🧱 Architecture

### 1. Pipeline Structure

- **ETL & Analysis** (`src/pipelines/geospatial/`):
  - `lidar_glo_pipeline.py` orchestrates:
    - LiDAR import and tiling.  
    - Derivative generation (RVT/MDI/SVF/slope).  
    - GLO georeferencing and vectorization.  
    - Feature QA and export.

- **Graph Integration** (`src/graph/`):
  - Loader scripts convert GeoPackages to Neo4j nodes and relationships:
    - `:Place`, `:Feature`, `:SurveyEvent`, `:Document`.  
    - Edges like `:RECORDED_IN`, `:DERIVED_FROM`, `:OVERLAYS`.

- **API & Frontend** (`src/api/`, `src/web/`):
  - APIs expose features and rasters as:
    - REST/GraphQL endpoints.  
    - Tiles and summaries for MapLibre/Cesium.  

### 2. Tools & Libraries

- **PDAL / GDAL** — point cloud to DTM, reprojection, raster alignment.  
- **RVT / QGIS** — hillshades, MDI, SVF, slope.  
- **QGIS Georeferencer** — manual/assisted GLO georeferencing with PLSS control.  
- **Python (GeoPandas, rasterio, shapely)** — scripting and pipeline glue.

All processing should be **config‑driven** (YAML/JSON configs per AOI or township) and logged with seeds, input hashes, and parameters.

---

## ⚖ FAIR+CARE & Governance

### 1. FAIR

| Principle        | Implementation                                                |
|-----------------:|---------------------------------------------------------------|
| **Findable**     | Stable UUIDs, STAC/DCAT catalogs, registry entries            |
| **Accessible**   | CC‑BY where possible, clear license tags, controlled access   |
| **Interoperable**| Standard CRS, GeoJSON/COG/GPKG, STAC/DCAT/PROV profiles       |
| **Reusable**     | Provenance, checksums, versioned configs, pipeline docs       |

### 2. CARE

| Principle              | Implementation                                            |
|-----------------------:|-----------------------------------------------------------|
| **Collective Benefit** | Supports preservation, education, and tribal interests   |
| **Authority to Control** | `care_tag` and sovereignty rules gate publication     |
| **Responsibility**     | Avoids exposing fragile or sacred sites; uses redaction  |
| **Ethics**             | Requires human‑in‑the‑loop review; AI is advisory only   |

### 3. Sensitive Feature Handling

- Sites flagged as **sensitive**:
  - May be generalized to broader polygons or removed from public layers.  
  - Are still tracked in registry/graph with restricted access flags.  
  - Require FAIR+CARE Council review before public release.

Governance outcomes (e.g., approved, withheld, generalized) should be recorded in both:

- Neo4j (governance relationships).  
- Telemetry / audit logs for long‑term accountability.

---

## 🕰️ Version History

| Version   | Date       | Author       | Summary                                                                                 |
|----------:|------------|-------------|-----------------------------------------------------------------------------------------|
| **v11.2.4** | 2025-12-06 | `@kfm-geo`  | Aligned with KFM‑MDP v11.2.4; added STAC/DCAT/PROV alignment, Story Node hooks, telemetry fields, and CI/CD integration notes. |
| v10.1.0  | 2025-11-10 | `@kfm-geo`   | Added MDI workflow, DCAT mirror, CARE tags; aligned with v10.1.0 telemetry & governance. |
| v1.0.0   | 2025-11-08 | `@kfm-geo`   | Initial publication — LiDAR + GLO integration guide.                                   |

---

<div align="center">

🗺️ **Kansas Frontier Matrix — LiDAR & GLO Integration Field Guide (v1.1)**  
Geospatial Insight · FAIR+CARE Governance · Cultural Stewardship  

[⬅ Back to Workflows Index](./README.md) ·  
[📘 Docs Root](../README.md) ·  
[⚖ Governance Charter](../standards/governance/ROOT-GOVERNANCE.md)

</div>
