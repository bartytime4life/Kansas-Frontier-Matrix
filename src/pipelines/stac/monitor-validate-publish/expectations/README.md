---
title: "🧪 Kansas Frontier Matrix — STAC Orchestrator Validation Suite (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/stac/monitor-validate-publish/expectations/README.md"
version: "v10.3.1"
last_updated: "2025-11-14"
review_cycle: "Quarterly · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/pipelines-stac-expectations-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🧪 **Kansas Frontier Matrix — STAC Orchestrator Validation Suite**  
`src/pipelines/stac/monitor-validate-publish/expectations/README.md`

**Purpose:**  
Define the **Great Expectations validation framework** used by the *STAC Monitor → Validate → Publish Orchestrator*.  
Enforces **STAC 1.0**, **EO/SAR**, **PROJ**, **KFM metadata extensions**, **FAIR+CARE**, and **schema integrity** requirements before STAC Items/Collections are allowed to be published into the KFM system.

<img alt="GE" src="https://img.shields.io/badge/Great_Expectations-Checkpoint-blue"/>
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Enforced-orange"/>
<img alt="Status" src="https://img.shields.io/badge/Validation-Active-success"/>
<img alt="License" src="https://img.shields.io/badge/License-CC--BY--4.0-green"/>

</div>

---

## 📘 Overview

This directory contains:

- **Great Expectations configuration**
- **Validation suites**
- **Checkpoints**
- **STAC JSON Schema definitions**
- **Custom KFM STAC extension tests**
- **Quarantine handling metadata**

The validation suite is the **hard gating layer** between:

1. **Raw incoming STAC JSONL** (untrusted)  
2. **Normalized & validated Items** eligible for publication and graph hydration  

Any failed validation batch is **quarantined**, logged, and escalated through GitHub Issues.

---

## 🗂️ Directory Layout

~~~~~text
src/pipelines/stac/monitor-validate-publish/expectations/
├── README.md                          # This file
│
├── great_expectations.yml             # Root GE configuration
│
├── checkpoints/
│   └── stac_items.yml                 # Main checkpoint for STAC Item batches
│
├── expectations/
│   ├── stac_item_schema.json          # JSON Schema for STAC 1.0 Items (+ KFM Extensions)
│   ├── stac_item_suite.json           # GE suite generated from schema/rules
│   └── custom_rules.json              # KFM-specific tests (eo, proj, care, roles)
│
└── data_docs/                         # Built by CI; HTML summaries, WCAG-compliant
~~~~~

---

## 🧭 Validation Flow (Indented Mermaid)

~~~~~mermaid
flowchart TD
  A["Incoming STAC JSONL"] --> B["Schema Validation<br/>stac_item_schema.json"]
  B --> C["Great Expectations Suite<br/>stac_item_suite"]
  C -->|PASS| D["Publish → data/stac/published/**"]
  C -->|FAIL| E["Quarantine<br/>data/stac/quarantine/**"]
  E --> F["Open GitHub Issue<br/>Validation Summary"]
  D --> G["Neo4j Graph Hydration + Telemetry"]
~~~~~

---

## 🧩 Validation Components

### 1️⃣ **JSON Schema Validation**  
Schema: `expectations/stac_item_schema.json`

Covers:

- Required keys (`id`, `type`, `geometry`, `assets`, `links`, `properties.datetime`)
- Valid STAC Item structure (1.0.0)
- Geometry correctness
- Properties validation:
  - `eo:cloud_cover`
  - `proj:*` fields
  - `landsat:*` / `sentinel:*` where applicable

KFM Extensions validated:

- `kfm:checksum`
- `kfm:care_label`
- `kfm:provenance`
- `kfm:ingest_version`

---

### 2️⃣ **Great Expectations Suite**  
Suite: `stac_item_suite.json`

Key Expectations:

- **expect_column_to_exist** for all mandatory STAC fields  
- **expect_column_values_to_be_between** for cloud cover, GSD, elevation  
- **expect_json_schema_to_match** for assets + links  
- **expect_column_values_to_not_be_null** for Item IDs and datetimes  
- **expect_link_relations_to_be_valid** (`self`, `collection`, `root`)  
- **expect_asset_roles_to_be_valid** (KFM-specific rules)  
- **expect_properties_to_contain_projections** when raster data present  

---

### 3️⃣ **KFM Custom Rules**  
Located in: `expectations/custom_rules.json`

Rules include:

- `kfm:care_label ∈ {public, sensitive, restricted}`
- If CARE=`sensitive` or `restricted`, geometry MUST be masked or generalized
- `proj:epsg` required for raster Items
- `eo:cloud_cover` required for optical sensors
- Asset MIME types MUST match extension  
- All Items MUST contain ingest metadata

---

### 4️⃣ **Quarantine Workflow**

On validation failure:

- Batch JSONL copied to:

  ~~~~~text
  data/stac/quarantine/<timestamp>/
  ~~~~~

- `last_failure_summary.md` generated  
- GitHub Issue automatically created via:

  ~~~~~text
  peter-evans/create-issue-from-file@v5
  ~~~~~

- Telemetry produced with:
  - `failed_items`
  - `error_classes`
  - `quarantine_path`
  - Governance flags (CARE rule failures)

---

## 🧪 GE Checkpoint (stac_items.yml)

Key features:

- Batch validation
- Environment-aware configuration
- CI integration with `stac-orchestrator.yml`
- Strict PASS/FAIL behavior (no warnings)

~~~~~text
name: stac_items
config_version: 1
class_name: Checkpoint
run_name_template: "%Y-%m-%d-%H-%M-stac_items"
validations:
  - batch_request:
      datasource_name: "stac_items_source"
      data_asset_name: "incoming_items"
    expectation_suite_name: "stac_item_suite"
~~~~~

---

## 📡 Telemetry Integration

Every validation run writes telemetry to:

~~~~~text
../../../../../releases/v10.3.0/focus-telemetry.json
~~~~~

Telemetry fields include:

- `validation_passed`
- `num_items_validated`
- `num_items_quarantined`
- `schema_errors`
- `care_errors`
- `runtime_sec`
- `energy_wh`
- `co2_g`

---

## 📚 Local Usage Example

~~~~~bash
cd src/pipelines/stac/monitor-validate-publish/expectations

great_expectations checkpoint run stac_items \
  --config great_expectations.yml \
  --suite stac_item_suite
~~~~~

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|--------|--------|---------|
| v10.3.1 | 2025-11-14 | STAC Pipelines Team | Updated for v10.3 orchestrator; refactored for KFM Markdown rules; added KFM metadata extension tests. |

---

<div align="center">

**Kansas Frontier Matrix — STAC Validation Suite**  
FAIR+CARE × Schema Integrity × Automated Governance  
© 2025 Kansas Frontier Matrix — CC-BY 4.0  

[Back to STAC Orchestrator](../README.md)

</div>
