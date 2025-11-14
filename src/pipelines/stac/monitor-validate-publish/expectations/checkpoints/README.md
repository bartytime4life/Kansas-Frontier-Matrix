---
title: "🧪 Kansas Frontier Matrix — STAC Validation Checkpoints (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/stac/monitor-validate-publish/expectations/checkpoints/README.md"
version: "v10.3.1"
last_updated: "2025-11-14"
review_cycle: "Quarterly · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/pipelines-stac-checkpoints-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🧪 **Kansas Frontier Matrix — STAC Validation Checkpoints**  
`src/pipelines/stac/monitor-validate-publish/expectations/checkpoints/README.md`

**Purpose:**  
Explain the **Great Expectations Checkpoints** used as **hard gates** in the STAC Monitor → Validate → Publish Orchestrator.  
Each checkpoint defines a **strict pass/fail contract** for STAC Items, ensuring all incoming data meets **STAC 1.0**, **KFM metadata extensions**, **FAIR+CARE**, and **schema-validation criteria** before publication.

<img alt="GE" src="https://img.shields.io/badge/Great_Expectations-Checkpoint-blue"/>
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Enforced-orange"/>
<img alt="Status" src="https://img.shields.io/badge/Status-Active-success"/>
<img alt="License" src="https://img.shields.io/badge/License-CC--BY--4.0-green"/>

</div>

---

## 📘 Overview

Checkpoints in this directory serve as **validation entrypoints** for batches of STAC Items retrieved by the orchestrator.  
They ensure that **no invalid data** proceeds into:

- The published STAC catalog  
- Neo4j scene/dataset/theme graph  
- Downstream pipelines (geospatial, Focus Mode, predictive layers)  

Each checkpoint is executed automatically by:

- `stac-orchestrator.yml` (GitHub Actions)  
- Local dry-runs during development  
- Manual re-validations in investigation workflows  

---

## 🗂️ Directory Layout

~~~~~text
src/pipelines/stac/monitor-validate-publish/expectations/checkpoints/
├── README.md                     # This file
└── stac_items.yml                # Main validation checkpoint
~~~~~

---

## 🧩 Checkpoint Architecture (Indented Mermaid)

~~~~~mermaid
flowchart TD
  A["Incoming STAC JSONL<br/>data/stac/incoming/**"] --> B["Instantiate Checkpoint<br/>stac_items.yml"]
  B --> C["Apply Validation Suite<br/>stac_item_suite.json"]
  C -->|PASS| D["Allow → Transform → Publish"]
  C -->|FAIL| E["Quarantine Batch<br/>Open GitHub Issue"]
~~~~~

---

## 🧪 stac_items.yml — Overview

This is the **primary checkpoint** governing STAC Item validation.

### Key Characteristics:

- **Batch-oriented** – validates all Items from a polling run  
- **Strict mode** – no soft-fails, no warnings  
- **Bound to suite:** `stac_item_suite`  
- **Uses datasource** defined in `great_expectations.yml`  
- **Produces HTML data docs** (WCAG 2.1 AA)

#### Required Outcomes:

| Outcome | Action |
|---------|--------|
| PASS | STAC assets proceed to `transform.py` |
| FAIL | Batch is quarantined + issue opened |

---

## 🧱 What the Checkpoint Validates

| Category | Checks |
|----------|--------|
| **Schema** | Matches `stac_item_schema.json` |
| **Properties** | datetime, cloud cover, proj fields, eo fields |
| **Links** | self, root, collection links must exist & be valid |
| **Assets** | roles, MIME types, validity of hrefs |
| **KFM Fields** | kfm:checksum, kfm:care_label, kfm:provenance, kfm:ingest_version |
| **Geospatial** | geometry validity, bbox bounds |
| **Governance** | CARE compliance: geometry masking for sensitive/restricted |

---

## 📡 Telemetry Integration

Each checkpoint run contributes telemetry:

- `stac_items_validated`  
- `stac_items_failed`  
- `validation_runtime_sec`  
- `schema_errors`  
- `care_errors`  
- `energy_wh`  
- `co2_g`  

Telemetry written to:

~~~~~text
../../../../../releases/v10.3.0/focus-telemetry.json
~~~~~

---

## 🧯 Failure Handling Workflow

1. Move failed batch to quarantine:

   ~~~~~text
   data/stac/quarantine/<timestamp>/
   ~~~~~

2. Write `last_failure_summary.md` with:
   - Error types  
   - Schema mismatches  
   - CARE violations  
   - Governance notes  

3. Automatically open a GitHub Issue with:
   - Run metadata  
   - Quarantine folder path  
   - Failure summary contents  

4. Telemetry updated with failure classification.

---

## 🧰 Local Development Example

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
| v10.3.1 | 2025-11-14 | STAC Pipelines Team | Added complete checkpoint docs per KFM Markdown rules; aligned with orchestrator v10.3. |
| v10.3.0 | 2025-11-14 | STAC Pipelines Team | Initial creation for v10.3 orchestrator. |

---

<div align="center">

**Kansas Frontier Matrix — STAC Validation Checkpoints**  
Schema Integrity × FAIR+CARE × Governance-Driven Validation  
© 2025 Kansas Frontier Matrix — CC-BY 4.0  

[Back to STAC Expectations](../README.md)

</div>
