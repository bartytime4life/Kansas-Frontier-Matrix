---
title: "📂 Kansas Frontier Matrix — STAC Dataset Storage (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/stac/monitor-validate-publish/data/stac/README.md"
version: "v10.3.1"
last_updated: "2025-11-14"
review_cycle: "Quarterly · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/pipelines-stac-storage-v1.json"
governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 📂 **Kansas Frontier Matrix — STAC Dataset Storage**  
`src/pipelines/stac/monitor-validate-publish/data/stac/README.md`

**Purpose:**  
Define the FAIR+CARE-governed storage conventions, directory layout, retention rules, and metadata requirements for all STAC Items and Collections used in the STAC Monitor → Validate → Publish pipeline.  
This directory houses the **canonical, versioned, immutable STAC assets** used across KFM geospatial, graph, and AI reasoning pipelines.

<img alt="STAC" src="https://img.shields.io/badge/STAC-1.0_Compliant-blue"/>
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Aligned-orange"/>
<img alt="Immutable" src="https://img.shields.io/badge/Data-Immutable-green"/>
<img alt="Status" src="https://img.shields.io/badge/Status-Active-success"/>

</div>

---

## 📘 Overview

This directory is the **persistent storage home** for validated, normalized, and governance-approved STAC assets.

It contains:

- Versioned **Collections**  
- Versioned **Items**  
- Derived & normalized metadata  
- Provenance + lineage references  
- CARE labels + sovereignty metadata  
- Immutable records used for:
  - Neo4j hydration  
  - STAC/DCAT catalog publishing  
  - Focus Mode dataset reasoning  
  - Temporal & geospatial overlays  

Only artifacts that **pass validation**, **pass CARE review**, and **complete telemetry export** are stored here.

---

## 🗂️ Directory Layout (Authoritative)

~~~~~text
src/pipelines/stac/monitor-validate-publish/data/stac/
├── collections/                     # Versioned STAC Collections
│   └── <collection_id>.json
│
└── items/                           # Versioned STAC Items by collection
    └── <collection_id>/
        └── <item_id>.json
~~~~~

Each file is:

- Fully **versioned**  
- Strictly **immutable**  
- Validated by **Great Expectations**  
- CARE-governed  
- Linked to **lineage** and **telemetry**  

---

## 🧩 Storage Flow (Indented Mermaid)

~~~~~mermaid
flowchart TD
  A["Incoming Raw<br/>STAC JSONL"] --> B["Great Expectations<br/>Validation"]
  B -->|PASS| C["Normalized STAC<br/>transform.py"]
  C --> D["Publish to STAC Storage<br/>collections/** · items/**"]
  D --> E["Neo4j Hydration"]
  D --> F["Catalog Exports<br/>STAC/DCAT"]
  D --> G["Telemetry + Governance Logging"]
  B -->|FAIL| Z["Quarantine<br/>Failed Batch"]
~~~~~

---

## 📦 Collections (`collections/`)

### Requirements:

Each file must include:

- Full STAC 1.0 Collection structure  
- Temporal extent  
- Spatial extent (bbox + proj fields if relevant)  
- Version pointer  
- Links: `self`, `root`, `parent`, `items`  
- KFM metadata:
  - `kfm:checksum`  
  - `kfm:care_label`  
  - `kfm:provenance`  
  - `kfm:ingest_version`  

**Example filename:**

~~~~~text
collections/landsat-c2-l2.json
~~~~~

Collections may be rehydrated by the STAC Catalog Builder pipeline.

---

## 🛰️ Items (`items/<collection_id>/`)

### Requirements:

Each Item file must be:

- A valid **STAC Item 1.0**  
- Normalized by `transform.py`  
- Passed through:
  - Schema validation  
  - Great Expectations suite  
  - CARE/Sovereignty masking checks  
  - Provenance consistency checks  
- Immutable after creation  

**Example path:**

~~~~~text
items/landsat-c2-l2/LC09_L2SP_030033_20230813_20230819_02_T1.json
~~~~~

### Mandatory KFM metadata fields:

- `kfm:checksum` (sha256)  
- `kfm:care_label`  
- `kfm:provenance` (lineage path)  
- `kfm:ingest_version`  
- For sensitive datasets, masking details (H3 r7, bbox generalization, etc.)

---

## 🔒 Immutability Guarantees

Once published:

- ❌ Items cannot be edited  
- ❌ Collections cannot be rewritten  
- ❌ Metadata cannot be corrected in-place  
- ✔ New versions must be published using SemVer rules  
- ✔ Lineage & provenance must reflect the exact published state  

Violations → **Critical CI Failure** + governance escalation.

---

## 📡 Telemetry Bindings

Each publish event writes telemetry fields including:

- `dataset_id`  
- `item_id`  
- `collection_id`  
- `validation_passed`  
- `care_label`  
- `publish_latency_ms`  
- `artifact_checksum`  
- `energy_wh`, `co2_g`  

Telemetry appended to:

~~~~~text
../../../../../releases/v10.3.0/focus-telemetry.json
~~~~~

Additional per-run logs stored in:

~~~~~text
src/pipelines/stac/monitor-validate-publish/data/telemetry/
~~~~~

---

## ⚖️ FAIR+CARE & Governance Requirements

All stored STAC assets must:

### FAIR Principles
- **Findable:** predictable path structure, unique IDs  
- **Accessible:** JSON, STAC 1.0 semantics  
- **Interoperable:** EO, SAR, PROJ, STAC Extensions  
- **Reusable:** versioning, lineage, license metadata  

### CARE Principles
- Label datasets with `public`, `sensitive`, or `restricted`  
- Apply geometry generalization for cultural/archaeological content  
- Leverage sovereignty metadata for tribal dataset overlap  
- Log governance decisions to:

  ~~~~~text
  ../../../../../docs/reports/audit/versioning_ledger.json
  ~~~~~

---

## 🧪 Local Inspection Examples

Inspect collection:

~~~~~bash
jq '.' src/pipelines/stac/monitor-validate-publish/data/stac/collections/landsat-c2-l2.json
~~~~~

Inspect an item:

~~~~~bash
jq '.properties' src/pipelines/stac/monitor-validate-publish/data/stac/items/landsat-c2-l2/<item>.json
~~~~~

Check CARE label:

~~~~~bash
jq '.properties["kfm:care_label"]' <item>.json
~~~~~

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|--------|--------|---------|
| v10.3.1 | 2025-11-14 | STAC Pipelines Team | Added authoritative documentation for STAC dataset storage layer; aligned with orchestrator v10.3 and KFM markdown rules. |

---

<div align="center">

**Kansas Frontier Matrix — STAC Dataset Storage**  
Immutable Records × FAIR+CARE Compliance × Provenance-Linked Metadata  
© 2025 Kansas Frontier Matrix — CC-BY 4.0  

[Back to STAC Orchestrator Data Layer](../README.md)

</div>
