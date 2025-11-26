---
title: "🌱 Kansas Frontier Matrix — Soil Data Integration Pipeline (SDA → gNATSGO → STAC)"
path: "src/pipelines/soil/README.md"
version: "v11.2.0"
last_updated: "2025-11-27"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council Oversight"
content_stability: "stable"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"

sbom_ref: "../../../releases/v11.2.0/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.0/manifest.zip"
telemetry_ref: "../../../releases/v11.2.0/pipelines-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/pipelines-soil-v11.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

status: "Active / Enforced"
doc_kind: "Pipeline"
intent: "soil-data-ingestion"
category: "Pipelines · Soil · Environmental Data"

fair_category: "F1-A1-I2-R1"
care_label: "Responsible · Indigenous-Respectful"
sensitivity_level: "Low"
public_exposure_risk: "Low"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

sensitivity: "General (non-sensitive; soil layers remain non-cultural but still subject to CARE)"
risk_category: "Low"
redaction_required: false

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "Dataset"
  owl_time: "ProperInterval"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/pipelines/soil/README.md@v11.1.0"
  - "docs/pipelines/soil/README.md@v10.4"
  - "USDA Soil Data Access (SDA)"
  - "gNATSGO MU Grids"
provenance_requirements:
  versions_required: true
  must_reference_superseded: true
  newest_first: true
  must_reference_origin_root: false

json_schema_ref: "../../../schemas/json/pipeline-soil-v11.schema.json"
shape_schema_ref: "../../../schemas/shacl/pipeline-soil-v11-shape.ttl"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "3d-context-render"
  - "diagram-extraction"
  - "metadata-extraction"
ai_transform_prohibited:
  - "content-alteration"
  - "unverified-architectural-claims"
  - "speculative-additions"
  - "narrative-fabrication"
  - "governance-override"
transform_registry:
  allowed:
    - "summary"
    - "timeline-generation"
    - "semantic-highlighting"
    - "diagram-extraction"
    - "metadata-extraction"
  prohibited:
    - "content-alteration"
    - "speculative-additions"
    - "governance-override"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"
requires_purpose_block: true
requires_version_history: true
requires_directory_layout_section: true
requires_governance_links_in_footer: true

doc_uuid: "urn:kfm:doc:pipelines:soil:v11.2.0"
semantic_document_id: "kfm-soil-pipeline"
event_source_id: "ledger:src/pipelines/soil/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

jurisdiction: "Kansas / United States"
classification: "Public Document"
lifecycle_stage: "stable"
ttl_policy: "Review required every 12 months"
sunset_policy: "Superseded by soil-pipeline-v12"
---

<div align="center">

# 🌱 **Kansas Frontier Matrix — Soil Data Integration Pipeline (SDA → gNATSGO → STAC)**  
`src/pipelines/soil/README.md`

[![Pipelines](https://img.shields.io/badge/KFM%20Pipelines-v11-blue)]()
[![STAC](https://img.shields.io/badge/STAC-v1.0.0-green)]()
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold)]()
[![OpenLineage](https://img.shields.io/badge/Lineage-v2.5-purple)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-green)]()

**Purpose**  
Provide complete ingestion, harmonization, and STAC publication of **SSURGO/SDA tabular soil data** joined with **gNATSGO raster map-unit grids**, with optional **H3/S2 indexing**, **AI-ready generalization**, and **FAIR+CARE governance compliance**.

</div>

---

## 📘 1. Overview

This pipeline aligns three major soil sources into a unified, governed KFM v11 dataset:

1. **USDA Soil Data Access (SDA)**  
   SQL-based tabular retrieval of `mukey`, `cokey`, `chkey`, and horizon attributes.

2. **gNATSGO Map Unit Grids**  
   10–30 m rasters indexing spatial `mukey` coverage.

3. **KFM Soil Knowledge Layer**  
   STAC-conformant Items + Collections, JSON-LD metadata, and optional H3/S2-generalized soil units.

This module includes ETL routines, join kernels, validation utilities, and STAC emitters.

---

## 🗂️ 2. Directory Layout (v11 · Immediate + One-Branch · Emojis + Descriptions)

```text
📁 src/pipelines/soil/                         — Soil integration pipeline root
│   📂 queries/                                — SDA SQL templates (mapunit, component, horizon)
│   📂 extract/                                — SDA REST clients and fetch utilities
│   📂 raster/                                 — gNATSGO MU raster handling + grid metadata
│   📂 join/                                   — Tabular ↔ Raster mukey join algorithms
│   📂 index/                                  — H3/S2 encoding + CARE-compliant generalizations
│   📂 stac/                                   — STAC Collection + Item constructors (Soil v11)
│   📂 utils/                                  — Validation helpers, shared modules
│   📄 pipeline.py                             — Unified ETL workflow (Extract → Join → Index → STAC)
```

---

## 🔗 3. Data Flow (High-Level)

### 3.1 Extract (SDA)
- POST SQL queries  
- Collect mapunit/component/horizon tables  
- Normalize fields, enforce canonical identifiers

### 3.2 Load (gNATSGO)
- Load MU raster  
- Validate CRS, affine transforms, nodata handling  
- Build mukey-index grid

### 3.3 Join
- Map raster `mukey` cells → SDA tables  
- Produce enriched cell or polygon features  
- Validate across `mukey`, `cokey`, `chkey`

### 3.4 Index (Optional)
- H3/S2 encoding  
- CARE-compliant generalization  
- Indirection for sensitive soil-linked heritage layers

### 3.5 Publish (STAC)
- Output Collection + Items  
- Attach JSON-LD, provenance, soil extensions  
- Emit lineage & telemetry metadata

---

## 🛠️ 4. Key Modules

### `sda_client.py`
- Executes SDA POST queries  
- Handles paging, backoff, WAL retry-buffer  
- Guarantees schema-consistent results

### `gnatsgo_loader.py`
- Loads MU raster into masked arrays  
- Extracts resolution/dtype/nodata  
- Ensures CRS alignment with KFM Spatial Registry

### `mukey_joiner.py`
- Performs fast mukey raster-to-table joins  
- Validates mapping across soil keys  
- Handles multi-component mapping when needed

### `soil_stac_writer.py`
- Emits STAC Items + Collections  
- Enforces KFM Soil Extension v11  
- Writes provenance + JSON-LD annotations

---

## 🧪 5. Validation Rules (v11.2)

- SDA tables MUST contain canonical `mukey`, `cokey`, `chkey`.  
- Raster cells MUST contain valid MU integer domains.  
- CRS MUST match KFM registry (EPSG:4326 unless specified).  
- STAC Items MUST include:
  - `soil:version`
  - `soil:mukey_domain`
  - Complete `process:steps[]`
- All outputs MUST validate against:
  - Soil Pipeline JSON Schema  
  - STAC v1.0.0 + KFM Soil Extension  
  - PROV-O lineage constraints  
  - CARE + sovereignty policies (for indexing)

---

## 🤖 6. AI / Focus-Mode Integration

- Generates **Story Node v3 seeds** for soil-hydrology-ecology intersections  
- Provides contextual embeddings for AI reasoning  
- Exposes tile endpoints that can be H3-masked  
- Supplies soil-feature “affordances” for environmental narratives  
- Focus Mode uses this layer to generate:
  - Terrain-adjacent soil explanations  
  - Soil–hydrology interactions  
  - Ecological suitability overlays  

---

## 🧪 7. Testing

Run the full suite:

```bash
pytest src/pipelines/soil/tests/
```

Includes:
- SDA mocks  
- Raster ingestion samples  
- Join integrity tests  
- STAC schema validation  
- CARE-compliant indexing tests  

---

## 🕰 8. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| **v11.2.0** | 2025-11-27 | Upgraded to full KFM-MDP v11.2.2 formatting, directory layout, metadata rules, AI governance. |
| **v11.1.0** | 2025-11-26 | First v11 soil pipeline layout; added H3/S2 indexing + STAC v11 extensions. |
| **v10.4.x** | 2024        | Legacy implementation before v11 restructure. |

---

<div align="center">

[⬅ Pipelines Index](../README.md) ·  
[🏗 Repository Architecture](../../../ARCHITECTURE.md) ·  
[⚖ Governance Standards](../../../docs/standards/ROOT-GOVERNANCE.md)

</div>
