---
title: "🌎 Kansas Frontier Matrix — Geo Standards Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/standards/geo/README.md"

version: "v11.2.2"
last_updated: "2025-11-27"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Semiannual · FAIR+CARE Council"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../releases/v11.2.2/standards-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/standards-geo-readme-v11.2.2.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../governance/ROOT-GOVERNANCE.md"
ethics_ref: "../faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

status: "Active / Enforced"
doc_kind: "Standard Index"
intent: "geo-standards-index"
semantic_document_id: "kfm-geo-standards-index"
doc_uuid: "urn:kfm:docs:standards:geo:index:v11.2.2"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
immutability_status: "version-pinned"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"
  owl_time: "TemporalEntity"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "metadata-extraction"
  - "diagram-extraction"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "governance-override"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"

requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true

classification: "Public (Governed)"
jurisdiction: "Kansas / United States"
ttl_policy: "24 months"
sunset_policy: "Superseded by Geo Standards v12"
---

<div align="center">

# 🌎 **Kansas Frontier Matrix — Geo Standards Index (v11.2.2)**  
`docs/standards/geo/README.md`

**Purpose**  
Serve as the **authoritative entrypoint** for all geospatial standards in the Kansas Frontier Matrix.  
Defines the required rules for **CRS**, **vertical datums**, **DEM/DoD conventions**, **tiling**, **geospatial metadata**, **hydrology schemas**, **sensitive-location masking**, and **STAC/DCAT geospatial fields**.  
Ensures deterministic, FAIR+CARE-aligned, governance-safe usage of spatial data across ETL, AI, graph, API, UI, and Focus Mode v3 systems.

</div>

---

## 📘 Overview

All KFM v11.2.2 spatial datasets—raster, vector, point clouds, DEMs, bathymetry, hydrology, archaeological survey data, landcover layers, and STAC Items—must conform to geospatial standards defined in this directory.

These standards govern:

- Coordinate Reference Systems (**CRS**)  
- Vertical datums & **CF/DoD** conventions  
- Raster & tile pyramids (**COG**)  
- Spatial metadata (**STAC**, **DCAT**, **JSON-LD**)  
- MapLibre & Cesium rendering constraints  
- Spatial accuracy and topology requirements  
- Sensitive-location (**H3**) generalization for sovereignty protection  
- Hydrology domain spatial schema (streams, bathymetry, reservoir models)  
- Semantic grounding (CIDOC-CRM, GeoSPARQL, OWL-Time)

All geospatial ETL, STAC ingest, tile pipelines, and graph loaders enforce these standards automatically.

---

## 🗂 Directory Layout (Canonical)

```text
📁 docs/
└── 📁 standards/
    └── 📁 geo/
        📄 README.md                      — ← Geo Standards Index (this file)
        📄 crs-standard.md                — CRS, reprojection SOPs, horizontal accuracy
        📄 vertical-axis-and-dod.md       — Vertical datum rules, CF Z-axis, DoD convention
        📄 tiling-and-pyramids.md         — COG, tile matrix sets, MapLibre/Cesium rules
        📄 stac-geo-spec.md               — STAC geospatial extension requirements
        📄 hydrology-standards.md         — Hydrology geospatial schemas
        📄 soil-source-comparison.md      — SDA/SSURGO/STATSGO2/gNATSGO provenance rules
        📄 archaeology-sensitive-locations.md — H3 masking, sovereignty safeguards
```

This structure follows the global KFM canonical format (folders = 📁, files = 📄).

---

## 🧩 Core Geo Standards (Summary)

### 📐 Vertical Axis & DoD  
(`vertical-axis-and-dod.md`)

- Required vertical datum: **NAVD88**  
- Required geoid model: **GEOID18**  
- CF Z-axis rules:
  - `"positive": "up"` for elevation  
  - `"positive": "down"` for depth  
- DoD interpretation:
  - **Negative = erosion**
  - **Positive = deposition**  
- Mandatory STAC vertical metadata + provenance  
- Required for DEM, bathymetry, DoD rasters

---

### 🗺 CRS Standard  
(`crs-standard.md`)

- Allowed CRSs:
  - **EPSG:4326** (WGS84) — STAC/DCAT canonical  
  - **EPSG:26914** (NAD83 / UTM 14N) — local precision  
- All STAC Items MUST declare CRS explicitly  
- Reprojection requires:
  - Metadata updates  
  - PROV-O lineage entries  
  - CRS-specific accuracy notes  
- Invalid geometries automatically fail CI checks

---

### 🧱 Tiling & Pyramids  
(`tiling-and-pyramids.md`)

- All rasters MUST be **COG** (Cloud-Optimized GeoTIFF)  
- Required:
  - Pyramid overviews (power-of-2)  
  - Proper tile matrix set (`WebMercatorQuad` or project-specific)  
- Cesium & MapLibre must use identical tile metadata  
- Raster alignment required for multi-layer rendering

---

### 🛰 STAC Geospatial Extensions  
(`stac-geo-spec.md`)

- Mandatory fields:
  - `bbox`, `geometry`, `proj:*`, `vertical:*`  
- Must be valid GeoJSON  
- DCAT mapping required for dataset-level descriptions  
- JSON-LD context auto-generated and validated in CI

---

### 💧 Hydrology Geospatial Standards  
(`hydrology-standards.md`)

- Orthometric elevation required for all water-surface products  
- Depth & stage must follow DoD conventions  
- Reservoir models require:
  - CF-time compliance  
  - Datum-specific metadata  
  - Spatial topologies (shoreline, bathymetry, delta, plume forms)  
- WID (Water Injection Dredging) layers follow special masking and QA rules

---

### 🛡️ Archaeology & Sensitive Locations  
(`archaeology-sensitive-locations.md`)

- Indigenous and culturally sensitive points MUST NOT be published directly  
- H3 generalization required (r7 or safer)  
- Multi-layer masking must propagate through:
  - STAC collections  
  - Tiles  
  - Vector geometries  
  - Knowledge graph nodes  
  - Story Node & Focus Mode narratives  
- CARE ethics integrated into spatial publication workflows

---

## ⚙ CI/CD Requirements for Geo Assets

All geospatial datasets MUST pass the following automated validations:

- `stac-validate`  
- `crs-lint`  
- `vertical-axis-validate`  
- `geojson-schema-validate`  
- `raster-meta-validate` (COG compliance)  
- `provenance-audit` (PROV-O completeness)  
- `faircare-audit` (ethics + sovereignty compliance)

Any failing check **blocks PR merge**.

---

## 🕰 Version History

| Version | Date | Summary |
|--------:|------|---------|
| v11.2.2 | 2025-11-27 | Upgraded to KFM-MDP v11.2.2; unified layout; updated CRS/vertical/tile/soil standards; FAIR+CARE and STAC/DCAT consistency hardened. |
| v11.0.0 | 2025-11-22 | Initial v11 release; organized geo standards under unified directory; CRS, vertical axis, tiling, and STAC geo-spec baseline. |

---

<div align="center">

🌎 **Kansas Frontier Matrix — Geo Standards Index (v11.2.2)**  
*Spatial Integrity · Semantic Consistency · FAIR+CARE Governance*

[⬅ Back to Standards Directory](../README.md) ·  
[⚖ Root Governance Charter](../governance/ROOT-GOVERNANCE.md)

</div>
