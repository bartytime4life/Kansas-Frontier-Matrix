---
title: "🧭 KFM v11.2.2 — Soil Data Domain (SDA + gNATSGO · Tile-Lineage & Differential Updates)"
path: "docs/soil/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · FAIR+CARE Council · Earth Systems Working Group"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

signature_ref: "../../releases/v11.2.2/signature.sig"
attestation_ref: "../../releases/v11.2.2/slsa-attestation.json"

sbom_ref: "../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../releases/v11.2.2/soil-domain-telemetry.json"
telemetry_schema: "../../schemas/telemetry/soil-domain-v11.2.json"
energy_schema: "../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../schemas/telemetry/carbon-v2.json"

governance_ref: "../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

status: "Active / Enforced"
doc_kind: "Domain Overview"
header_profile: "standard"
footer_profile: "standard"

scope:
  domain: "soil"
  applies_to:
    - "sda"
    - "gnatsgo"
    - "soil-etl"
    - "differential-updates"
    - "tile-lineage"
    - "soil-stac"
    - "soil-governance"

semantic_intent:
  - "soil-data"
  - "landscape-analysis"
  - "deterministic-refresh"
  - "provenance-governance"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "Environmental (non-sensitive)"
public_exposure_risk: "Low"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"
  - "ISO-19115"

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:soil:index:v11.2.2"
semantic_document_id: "kfm-soil-index-v11.2.2"
event_source_id: "ledger:soil-index-v11.2.2"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
requires_purpose_block: true
requires_directory_layout_section: true
requires_governance_links_in_footer: true
requires_version_history: true
diagram_profiles:
  - "mermaid-flowchart-v1"
  - "mermaid-timeline-v1"
---

<div align="center">

# 🧭 **KFM v11.2.2 — Soil Data Domain (SDA + gNATSGO)**  
`docs/soil/README.md`

**Purpose:**  
Provide the canonical reference for all soil datasets, pipelines, governance, lineage, STAC integration, differential updates, and deterministic tile refresh workflows within the Kansas Frontier Matrix.

</div>

---

## 📘 Overview

The **Soil Domain** of KFM unifies USDA soil products:

- **SDA (Soil Data Access)**  
- **gNATSGO (Gridded National Soil Geodatabase)**  

These datasets underpin:

- Hydrology analyses  
- Ecological & archaeological affordance modeling  
- Land-use suitability analyses  
- Story Node & Focus Mode environmental reasoning  

KFM v11.2.2 standardizes these datasets under:

- **Tile-level lineage anchors**  
- **Checksum-based differential updates**  
- **COG + GeoParquet harmonization**  
- **Complete PROV-O histories**  
- **STAC v11 collections & items**  

This reduces compute load while maintaining exact reproducibility and ethical compliance.

---

## 🧩 Soil Data Model (v11.2.2)

Each soil tile is defined by:

- `kfm:tile_id` (XYZ tiling index)  
- `checksum:multihash` (SHA-256)  
- `properties.updated` (source timestamp)  
- SDA/gNATSGO release metadata  
- Full provenance chain (USDA → KFM ETL → downstream models)  

Downstream joins use:

- `(tile_id, src_checksum)`  

locking interpretability to the exact soil snapshot.

---

## 🌍 Soil STAC Structure

The Soil STAC Catalog includes:

- **Collections:** `soil-sda`, `soil-gnatsgo`  
- **Items:** One per tile  
- **Assets:** GeoParquet, COGs, horizon tables, metadata files  
- **PROV-O lineage:** `prov:used`, `prov:wasGeneratedBy`  
- **DCAT fields:** contact, license, spatial extent, distribution metadata  

All files adhere to **KFM-STAC v11**.

---

## 🧱 Soil Pipelines

| Pipeline | Function |
|----------|----------|
| **Differential Soil Updates** | Evaluate tile deltas, re-ingest only changed tiles |
| **Soil Normalization Engine** | Apply units, CRS, horizon, and attribute normalization |
| **Soil Raster Harmonization** | Create COGs, hillshade, grid alignment |
| **Soil Parquet Generator** | Produce columnar GeoParquet layers |
| **Soil STAC Publisher** | Generate STAC Items with full lineage |
| **Soil QA / GE Suite** | Validate tiles and data-quality standards |

---

## 📂 Directory Layout

    docs/soil/
    ├── 📄 README.md                                 # This file
    │
    ├── 📁 differential-updates/                     # Differential soil update pipeline
    │   └── 📄 README.md
    │
    ├── 📁 normalization/                            # Soil normalization & unit harmonization
    │   └── 📄 README.md
    │
    ├── 📁 stac/                                     # Soil STAC collections & templates
    │   ├── 🌐 soil-sda-collection.json
    │   ├── 🌐 soil-gnatsgo-collection.json
    │   └── 📂 items/
    │       └── 📄 template-item.json
    │
    ├── 📁 governance/                               # Soil governance & provenance policies
    │   ├── 📄 lineage-policy.md
    │   ├── 📄 freshness-rules.md
    │   └── 📄 soil-license-matrix.md
    │
    └── 📁 examples/                                 # Example tiles, metadata, and joins
        ├── 📄 example-stac-item.json
        └── 📄 example-geoparquet-metadata.json

---

## 🧭 Story Node & Focus Mode Integration

Soil data contributes to Story Nodes describing:

- Land-use and settlement patterns  
- Agricultural transitions  
- Hydrological interactions  
- Archaeological affordances  
- Ecological changes across time  

Focus Mode v3 uses soil:

- Tile lineage  
- Property changes  
- Soil–hydrology links  
- Regional suitability narratives  

All generated nodes cite source datasets, tile checksums, and provenance pointers.

---

## 🧪 Validation, Drift Detection & QA

Soil domain CI includes:

- Great Expectations suite  
- Schema drift detection  
- Freshness windows for SDA/gNATSGO  
- STAC validation  
- Telemetry collection (energy, carbon)  
- OpenLineage span tracking  
- Hash-based drift alarms  
- WAL-safe recovery  

---

## 🕰️ Version History

| Version | Date | Notes |
|---------|------|--------|
| v11.2.2 | 2025-11-28 | Domain-wide update; emoji directory tree; STAC/lineage upgrades |
| v11.2.0 | 2025-11-20 | Introduced differential tile model; harmonized soil pipelines |
| v11.1.x | 2025-10-10 | Added registry + checksum enforcement |
| v11.0.x | 2025-09-01 | Initial Soil Domain documentation |

---

<div align="center">

### 🔗 Footer  
[🌐 KFM Home](../README.md) · [📚 Standards](../standards/README.md) · [📦 STAC Catalog](../data/stac/)

</div>

