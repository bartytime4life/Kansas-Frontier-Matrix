---
title: "🌱 KFM v11 — Soil & Landscape Data Domain (gNATSGO · gSSURGO · STATSGO2)"
description: "Domain-level overview for USDA NRCS soil datasets (gNATSGO, gSSURGO, STATSGO2) and their integration into KFM’s geospatial, archaeological, hydrological, and environmental workflows."
path: "docs/data/soils/README.md"
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Soils & Landscape Council · Hydrology & Archaeology Liaisons"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x soils-contract compatible"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../releases/v11.2.3/soils-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/soils-v1.json"

governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

status: "Active / Enforced"
doc_kind: "Data Domain Overview"
header_profile: "standard"
footer_profile: "standard"

intent: "soils-landscape-domain"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"

scope:
  domain: "soils"
  applies_to:
    - "gnatsgo"
    - "gssurgo"
    - "statsgo2"
    - "soil-rasters"
    - "soil-tables"
    - "soil-story-nodes"

semantic_intent:
  - "dataset-architecture"
  - "ingestion-coordination"
  - "story-node-source"
category: "Data · Soils · Domain"

sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / CONUS · USDA NRCS"
indigenous_rights_flag: false

data_steward: "Soils & Landscape Council · Hydrology & Archaeology Liaisons"
ttl_policy: "Indefinite (versioned by release year)"
sunset_policy: "Supersede when v12 soils architecture is adopted"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "Dataset"
  prov_o: "prov:Plan"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "GeoSPARQL"
  - "FAIR+CARE"

provenance_chain:
  - "docs/data/soils/README.md@v11.2.2"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "schemas/json/docs-soils-domain-v11.2.3.schema.json"
shape_schema_ref: "schemas/shacl/docs-soils-domain-v11.2.3-shape.ttl"
story_node_refs:
  - "soil.landscape"
  - "soil.hydrology"
  - "soil.archaeology"

immutability_status: "mutable"

doc_uuid: "urn:kfm:doc:data:soils:domain:v11.2.3"
semantic_document_id: "kfm-data-soils-domain-v11.2.3"
event_source_id: "ledger:kfm:doc:data:soils:domain:v11.2.3"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "diagram-extraction"
  - "metadata-extraction"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "metadata-check"
  - "provenance-check"
  - "footer-check"
---

<div align="center">

# 🌱 Kansas Frontier Matrix — Soil & Landscape Data Domain  
## gNATSGO · gSSURGO · STATSGO2

`docs/data/soils/README.md`

**Purpose:**  
Provide a **KFM-aligned reference** for USDA NRCS soil datasets (gNATSGO, gSSURGO, STATSGO2) and define how they integrate into **geospatial, archaeological, hydrological, and environmental** workflows, including STAC catalogs, raster registries, and Story Node context layers.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../README.md) ·
[![KFM-MDP v11.2.2](https://img.shields.io/badge/KFM%E2%80%93MDP-v11.2.2-informational)](../../standards/kfm_markdown_protocol_v11.2.2.md) ·
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold)](../../standards/faircare/FAIRCARE-GUIDE.md) ·
[![Status: Active](https://img.shields.io/badge/Status-Active-success)](../../../releases/v11.2.3/manifest.zip)

</div>

---

## 🧩 1. Dataset Overview

### 1.1 gNATSGO

- Annual composite soil–geographic database maintained by **USDA NRCS**.  
- Combines **SSURGO + STATSGO2 + Raster Soil Survey (RSS)**.  
- Complete, gap-free coverage for **CONUS and territories**.  
- Rasterized map units (commonly **10 m** for state layers, **30 m** for CONUS).  
- Linked tabular attributes for:
  - Chemistry  
  - Hydrology  
  - Structure  
  - Suitability / interpretations  
  - Ecological properties  

### 1.2 gSSURGO

- State-level, **detailed soil survey** dataset.  
- Vector with accompanying raster products.  
- Best suited for:
  - Local detail  
  - Site-level studies  
  - **Archaeological micro-context** and fine-scale landscape modeling.

### 1.3 STATSGO2

- Generalized, broad units suitable for **regional analyses**.  
- Often used when models do not require high granularity or when:
  - Large-scale climate / hydrology experiments are run.  
  - Only broad soil patterns are needed.

---

## 🕒 2. Update Cadence & KFM Strategy

### 2.1 Annual Soils Refresh (ASR)

- Occurs **once per year**, typically around **October 1**.  
- All official NRCS soil survey areas receive updates.  
- New **gNATSGO / gSSURGO** publications follow shortly after.  
- Attribute schema is generally kept **consistent across refreshes**.

### 2.2 Recommended KFM Strategy

- **Monthly polling** for new NRCS releases.  
- Automated **download → validation → checksum → catalog** flow.  
- Keep **all past versions live** (e.g., yearly directories) for reproducibility.  
- Propagate changes into:
  - **STAC collections** (per year / per product).  
  - **Raster registries** (data/soils/rasters).  
  - **Archaeology & hydrology domain pipelines**.  
  - **Story Node context builders** (soil-driven narratives and maps).

---

## 🧪 3. Validation Requirements (KFM Standard)

### 3.1 Spatial Validation

- Confirm projection — commonly:
  - **EPSG:5070** (CONUS Albers) or  
  - **EPSG:4326** (geographic) depending on source.  
- Verify tile boundaries for CONUS and state layers.  
- Ensure **CRS metadata is present** (soil rasters often ship with incomplete metadata).

### 3.2 Raster Integrity

- Check that:

  - Cell count matches expected resolution (10 m or 30 m) and extent.  
  - No missing map units (no unexpected “gaps”).  
  - No-data mask is correctly defined.  
  - Raster attributes match the **mapunit (mukey)** domain.

### 3.3 Tabular Attributes

Validate core attribute groups for consistency and schema alignment:

- **Hydrology / physical behavior**
  - Hydrologic soil group  
  - Horizon depths  
  - Saturated hydraulic conductivity  

- **Chemistry**
  - pH  
  - Cation Exchange Capacity (CEC)  
  - Organic matter  
  - Electrical conductivity (EC)  

- **Structure & physical properties**
  - Texture class  
  - Sand / silt / clay percentages  
  - Rock fragments  
  - Horizon boundary properties  

- **Ecological / interpretive**
  - Ecological site descriptors  
  - Productivity indices  
  - Suitability ratings (land-use, infrastructure, etc.)

### 3.4 Provenance

For each release, produce **SHA-256** checksums for:

- Entire **ZIP archive**.  
- Raster layer(s) (e.g., GeoTIFF).  
- All tabular files.  
- Final merged / harmonized products used by KFM.

Checksums MUST be stored under:

- `data/soils/<product>/<year>/provenance/`  
- And/or referenced in STAC and DCAT metadata.

---

## 🗂️ 4. KFM Integration Model & Directory Layout

### 4.1 Documentation Layout (This Tree)

~~~text
docs/data/soils/
├── 📄 README.md                       # This file (soil & landscape domain overview)
│
├── 🌎 gnatsgo/                        # gNATSGO-specific docs (per year, STAC, usage)
│   └── 📄 README.md
│
├── 🧱 gssurgo/                        # gSSURGO-specific docs (state-level detail)
│   └── 📄 README.md
│
├── 🗺️ statsg o2/                      # STATSGO2 high-level docs & patterns
│   └── 📄 README.md
│
└── 🧾 metadata/                       # Shared schema docs, code lists, attribute guides
    └── 📄 README.md
~~~

### 4.2 Data Layout (Recommended Raw/Processed Tree)

~~~text
data/soils/
├── gnatsgo/
│   ├── 2023/
│   │   ├── rasters/                  # 10 m / 30 m GeoTIFFs or Cloud-Optimized GeoTIFFs
│   │   ├── tables/                   # Tabular attributes (CSV/Parquet/Geodatabase exports)
│   │   ├── stac/                     # STAC Collection/Items for gNATSGO 2023
│   │   └── provenance/               # Checksums, source metadata, processing logs
│   └── 2024/
│       └── ...
│
├── gssurgo/
│   ├── ks/                           # Kansas-focused subsets
│   ├── regional/                     # Multi-state subsets for basins / eco-regions
│   └── provenance/
│
├── statsg o2/
│   ├── conus/
│   └── provenance/
│
└── metadata/
    ├── attribute-dictionaries/
    ├── schemas/
    └── mappings/                     # Mapping gNATSGO/gSSURGO/STATSGO2 → KFM ontology
~~~

> Note: Within the repo, paths may be adjusted to align with data storage backends (e.g. S3, lakeFS); this README treats `data/soils/` as the logical root.

### 4.3 How Soils Connect into the Frontier Matrix

Soil properties feed directly into:

- **Landscape evolution models**  
- **Hydrology networks** (infiltration, runoff, baseflow potential)  
- **Archaeology Sensitivity Engine** (burial depth, preservation probability)  
- **Vegetation & land-use reconstructions**  
- **Story Node contextual layers** for historical/environmental narratives  

Examples:

- **Soil horizon depth & structure** help:
  - Identify likely **stable surfaces** for cultural deposits.  
  - Estimate erosion and burial processes.  
  - Compute **preservation probability** maps.

- **Organic content & chemistry** inform:
  - Paleoenvironment reconstructions.  
  - Carbon modeling and flux estimates.  
  - Settlement pattern analysis and resource availability.

---

## 🧭 5. Recommended Auto-Update Workflow

### 5.1 Triggering

- **Monthly schedule** via CI/CD.  
- Manual trigger allowed for:
  - Major Annual Soils Refresh (ASR).  
  - Hotfixes or specific study needs.

### 5.2 Stages

1. **Fetch metadata** from NRCS (gNATSGO/gSSURGO/STATSGO2 portals / Soil Data Access).  
2. **Check version** against previous KFM manifest.  
3. **Download new release** archives.  
4. **Extract all components** (rasters, tables, ancillary files).  
5. **Validate** raster + tables + schema (see section 3).  
6. **Compute checksums** (ZIP, rasters, tables, merged products).  
7. **Generate STAC catalog entries** (Collections/Items).  
8. **Publish** to KFM registries (STAC, DCAT, graph).  
9. **Update Story Node sources** and Focus Mode soil context.  
10. **Log energy + carbon metrics** (via Autonomy Matrix / energy modules).

All steps should be codified as a reproducible pipeline with provenance events (e.g., OpenLineage).

---

## 🗝️ 6. Essential Reference Tables (High-Value Attributes)

### 6.1 Hydrology

- Hydrologic soil group.  
- Available water capacity.  
- Saturated hydraulic conductivity.  
- Flooding frequency and duration.  
- Depth to water table (where available).

### 6.2 Structure & Physical

- Texture class (topsoil & subsoil horizons).  
- Sand / silt / clay percentages.  
- Rock fragment content.  
- Horizon boundaries (depths, distinctness, shape).

### 6.3 Chemistry

- pH.  
- CEC (Cation Exchange Capacity).  
- Organic matter content.  
- EC (electrical conductivity).  

### 6.4 Ecological / Interpretive

- Ecological site identifiers and summaries.  
- Productivity indices (for relevant land uses).  
- Suitability ratings (e.g., for infrastructure, agriculture, habitat).

All attributes should be mapped into:

- **KFM’s semantic model** (ontology entities/fields).  
- **PROV-O lineage** linking raw NRCS tables → harmonized KFM datasets.

---

## 🗺️ 7. Practical Usage Examples

### 7.1 Archaeology

- **Burial depth modeling** using profile/horizon information.  
- **Site preservation estimation** (stability, drainage, erosion risk).  
- **Paleosurface detection** (stable buried surfaces / buried A horizons).  
- **Terrain stability mapping** for excavation planning and hazard assessment.

### 7.2 Hydrology

- Basin-level **infiltration** capacity mapping.  
- **Runoff estimation** integrated with climate and land-cover data.  
- **Water quality predictions** using soil chemistry and hydrologic groups.

### 7.3 Climate & Vegetation

- Soil–vegetation interaction models (e.g., rooting depth vs. water availability).  
- **Moisture availability mapping** for ecological niches.  
- Long-term **ecological modeling** that couples soils with climate and land-use histories.

---

## 🛠️ 8. STAC Catalog Template (Skeleton)

A minimal STAC Collection template for a gNATSGO release:

~~~json
{
  "type": "Collection",
  "id": "kfm-soils-gnatsgo-<year>",
  "title": "KFM Soil Dataset — gNATSGO <year>",
  "description": "Harmonized USDA NRCS gNATSGO soil dataset for <year>, curated for the Kansas Frontier Matrix.",
  "stac_version": "1.0.0",
  "extensions": ["proj", "raster"],
  "providers": [
    {
      "name": "USDA NRCS",
      "roles": ["producer", "licensor"],
      "url": "https://www.nrcs.usda.gov/"
    },
    {
      "name": "Kansas Frontier Matrix",
      "roles": ["processor", "host"],
      "url": "https://example.org/kfm"
    }
  ],
  "license": "CC-BY-4.0",
  "assets": { },
  "summaries": { },
  "links": [ ]
}
~~~

> In practice, KFM-specific STAC profiles and schemas MUST be applied (e.g., soil-specific fields and attribute mappings).

---

## 📚 9. External Resources (High-Quality References)

- USDA NRCS Official Soil Data portals.  
- NRCS Soil Data Access (API).  
- Annual Soils Refresh (ASR) documentation.  
- Raster Soil Survey (RSS) program documentation.  
- STATSGO2 / SSURGO metadata dictionaries and data models.

These should be linked in the `metadata/` subdirectory once URLs and citations are standardized for KFM documentation.

---

## 🕰️ 10. Version History

| Version  | Date       | Author                    | Summary                                                         |
|----------|------------|---------------------------|-----------------------------------------------------------------|
| v11.2.3  | 2025-12-02 | Soils & Landscape Council | Initial soils domain overview for gNATSGO / gSSURGO / STATSGO2. |

---

<div align="center">

🌱 **Kansas Frontier Matrix — Soil & Landscape Data Domain**  
Soil Intelligence · Hydrology & Archaeology Aware · FAIR+CARE-Aligned  

[📘 Data Index](../README.md) · [🌞 Space-Weather Domain](../space-weather/README.md) · [⚖ Governance](../../standards/governance/ROOT-GOVERNANCE.md)

</div>