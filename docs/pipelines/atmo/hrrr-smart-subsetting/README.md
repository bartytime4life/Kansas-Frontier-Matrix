---
title: "🌀 KFM v11.2.2 — HRRR Smart Subsetting & Change-Aware Storage (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/atmo/hrrr-smart-subsetting/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Atmospheric Systems · FAIR+CARE Council"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"
signature_ref: "../../../releases/v11.2.2/signature.sig"
attestation_ref: "../../../releases/v11.2.2/slsa-attestation.json"

sbom_ref: "../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../releases/v11.2.2/atmo-hrrr-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/pipelines-hrrr-v11.2.2.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

status: "Active / Enforced"
doc_kind: "Pipeline Runbook"
header_profile: "standard"
footer_profile: "standard"

scope:
  domain: "pipelines/atmo"
  applies_to:
    - "etl"
    - "subset"
    - "delta-detection"
    - "stac-publication"

semantic_intent:
  - "atmospheric-data"
  - "cost-optimization"
  - "change-aware-storage"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "Environmental (non-sensitive)"
sensitivity_level: "None"
public_exposure_risk: "Low"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:pipelines:atmo:hrrr-smart-subsetting:v11.2.2"
semantic_document_id: "kfm-pipelines-atmo-hrrr-smart-subsetting-v11.2.2"
event_source_id: "ledger:pipelines-atmo-hrrr-smart-subsetting-v11.2.2"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

requires_purpose_block: true
requires_version_history: true
requires_directory_layout_section: true
requires_governance_links_in_footer: true
diagram_profiles:
  - "mermaid-flowchart-v1"
  - "mermaid-timeline-v1"
---

<div align="center">

# 🌀 **KFM v11.2.2 — HRRR Smart Subsetting & Change-Aware Storage**  
`docs/pipelines/atmo/hrrr-smart-subsetting/README.md`

**Purpose:**  
Cost-optimized, deterministic, change-aware HRRR ETL producing KFM-STAC v11 Items with full lineage and FAIR+CARE ethics.

</div>

---

## 📘 Overview

The HRRR Smart Subsetting pipeline ingests NOAA HRRR (CONUS) from AWS Open Data and applies:

1. **AOI-aware spatial clipping**  
2. **Selective variable retention**  
3. **Delta detection (change-aware)**  
4. **STAC v11 Item publication with PROV-O lineage**

Result: **>90% storage reduction** with preserved atmospheric signal.

---

## 🧱 Architecture

### 1. HRRR Loader
- fsspec + zarr lazy reads  
- CF metadata normalization  
- UTC alignment  

### 2. AOI Subsetting
- CRS-correct `.rio.clip()`  
- AOI masks stored in: `data/work/atmo/hrrr/aoi_masks/`

### 3. Variable Selector
- Wind, smoke, temp, clouds, visibility  
- Configured via `variables.yaml`

### 4. Delta Engine
- Mean / Max / directional Δ  
- Smoke class shifts  
- Visibility drops  
- Cloud layer transitions  
- Commit only when thresholds exceeded  

### 5. lakeFS Commit & Tagging
- `hrrr-{YYYYMMDDHH}-subset`  
- `hrrr-change-{YYYYMMDDHH}-{category}`  

### 6. STAC v11 Output
- CF variable spec  
- `proj:*`, `grid:*` metadata  
- Full provenance  
- Per-asset checksums  
- Energy/carbon telemetry  

---

## 📦 Directory Layout

    📁 docs/pipelines/atmo/hrrr-smart-subsetting/
        └── 📄 README.md

    📁 src/pipelines/atmo/hrrr/
        ├── 📄 loader.py
        ├── 📄 subsetter.py
        ├── 📄 delta_engine.py
        ├── 📄 publisher.py
        └── 🗂️ config/
            ├── 📄 variables.yaml
            └── 📄 thresholds.yaml

    📁 data/work/atmo/hrrr/
        ├── 📁 aoi_masks/
        └── 📁 subsets/

    📁 data/stac/atmo/hrrr/
        ├── 📄 collection.json
        └── 📁 items/

    📁 .github/workflows/
        └── 📄 hrrr-smart-subsetting.yml

*(Directory layout is rendered via 4-space indentation—fully box-safe, zero nested fences.)*

---

## 🔧 Delta Thresholds (Default v11)

| Variable | Condition |
|---------|-----------|
| Wind @10m | Max Δ ≥ 1.0 m/s OR direction shift ≥10° on ≥5% AOI |
| Temp @2m | Mean Δ ≥ 0.5 K |
| Visibility | Drop ≥ 1 km |
| Smoke | Any class transition |
| Cloud Cover | ≥20% change per layer |

---

## 🧭 STAC Metadata Alignment

Each STAC Item includes:

- `stac_version: 1.0.0`  
- Spatial + temporal extents  
- PROV-O lineage (`prov:used`, `prov:wasGeneratedBy`)  
- CF variables  
- Grid metadata  
- Energy & carbon metrics  

---

## 🧪 Validation & CI/CD

This pipeline enforces:

- Deterministic ETL  
- lakeFS reproducibility  
- STAC schema validation  
- FAIR+CARE audit  
- Linting (flake8/mypy/black)  
- Pipeline contract (`KFM-PDC v11`)  

---

## 🧠 Story Node & Focus Mode Integration

Story Nodes written from this pipeline include:

- Wind stress on landscapes  
- Smoke transport interactions  
- Visibility + corridor inference  
- Temperature → settlement dynamics  

Stored in:  
`data/story/atmo/hrrr/`

---

## 🕰️ Version History

- **v11.2.2** — Fixed nested-fence issue; emoji directory layout; full KFM-MDP v11.2.2 compliance  
- **v11.0.0** — Original canonical release  

---

<div align="center">

### 🔗 Footer

[🌐 KFM Home](../../../README.md) · [📚 Standards](../../standards/README.md) · [📦 STAC Catalog](../../../data/stac/)

</div>
