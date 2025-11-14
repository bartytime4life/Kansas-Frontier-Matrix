---
title: "📤 Kansas Frontier Matrix — Published STAC Assets (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/stac/monitor-validate-publish/data/published/README.md"
version: "v10.3.1"
last_updated: "2025-11-14"
review_cycle: "Quarterly · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/pipelines-stac-published-v1.json"
governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 📤 **Kansas Frontier Matrix — Published STAC Assets**  
`src/pipelines/stac/monitor-validate-publish/data/published/README.md`

**Purpose:**  
Define the authoritative, immutable, FAIR+CARE-certified rules governing **published STAC Items and Collections**.  
This directory contains all **validated, normalized, governance-approved, versioned STAC assets** that power the KFM geospatial, graph, catalog, and Focus Mode reasoning engines.

<img alt="STAC Published" src="https://img.shields.io/badge/STAC_Published-Immutable-blue"/>
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Certified-orange"/>
<img alt="Versioned" src="https://img.shields.io/badge/Versioning-SemVer-green"/>
<img alt="Status" src="https://img.shields.io/badge/Status-Canonical-success"/>

</div>

---

## 📘 Overview

The **published** directory is the **final destination** of the STAC Monitor → Validate → Publish pipeline.  
It contains:

- Versioned **Collections**
- Versioned **Items**
- Fully normalized metadata
- Provenance + lineage references
- CARE label + masking metadata
- Assets suitable for:
  - STAC Catalog browsing  
  - DCAT dataset publishing  
  - Neo4j graph hydration  
  - Map & timeline rendering  
  - Focus Mode v2.4 entity reasoning  

Published assets are **immutable, permanent, and globally authoritative**.

---

## 🗂️ Directory Layout (Authoritative)

~~~~~text
src/pipelines/stac/monitor-validate-publish/data/published/
├── collections/
│   └── <collection_id>.json
│
└── items/
    └── <collection_id>/
        └── <item_id>.json
~~~~~

Example:

~~~~~text
collections/landsat-c2-l2.json
items/landsat-c2-l2/LC09_L2SP_030033_20230716.json
~~~~~

---

## 🧩 Publication Flow (Indented Mermaid)

~~~~~mermaid
flowchart TD
  A["Incoming STAC Batch<br/>data/incoming/**"] --> B["GE Validation<br/>stac_item_suite"]
  B -->|PASS| C["Normalize STAC<br/>transform.py"]
  C --> D["Write Published Assets<br/>collections/** · items/**"]
  D --> E["Neo4j Hydration<br/>Scenes · Datasets · Themes"]
  D --> F["STAC/DCAT Catalog Exports"]
  D --> G["Telemetry + Governance Logging"]
  B -->|FAIL| Z["Quarantine<br/>data/quarantine/**"]
~~~~~

---

## 📦 Published Collections

Published Collections contain:

- Dataset-wide metadata  
- Spatial + temporal extents  
- Provider details  
- STAC Extension declarations  
- Link relations (`self`, `root`, `items`, `version`)  
- KFM metadata (checksum, care_label, provenance, ingest_version)  

Collections **must** be internally consistent with:

- All Items beneath their collection path  
- DCAT exports  
- Lineage bundles  
- Telemetry records  
- SemVer versioning contracts  

---

## 🛰️ Published Items

Each STAC Item under `items/<collection_id>/` is:

- JSON Schema validated  
- Great Expectations validated  
- CARE-governance approved  
- Normalized by `transform.py`  
- Enriched with KFM metadata:

| Field | Required | Purpose |
|-------|----------|---------|
| `kfm:checksum` | ✔ | Asset immutability hash |
| `kfm:care_label` | ✔ | public / sensitive / restricted |
| `kfm:provenance` | ✔ | Lineage reference |
| `kfm:ingest_version` | ✔ | Orchestrator/ETL version |
| `kfm:masking_strategy` | conditional | For sensitive/restricted data |
| `kfm:sovereignty_notes` | optional | Indigenous/heritage context |

### Immutability

- ❌ Items cannot be edited  
- ❌ Items cannot be replaced  
- ❌ Items cannot be mutated post-publication  
- ✔ New versions require **new files** with updated SemVer lineage  

---

## 🔐 Immutability & Version Rules

Once an Item or Collection is published:

- It becomes a **permanent record**  
- It must not be changed or deleted  
- All updates require **SemVer increments**  
- Lineage references MUST reflect the correct version chain  

Governance violations → **Critical CI block**.

---

## 🧭 Governance Enforcement (FAIR+CARE)

### CARE Rules

- Sensitive or restricted datasets MUST:
  - Use masking/generalization  
  - Document `kfm:masking_strategy`  
  - Include sovereignty metadata (if applicable)  

### FAIR Rules

- Findable: predictable paths, IDs, version chains  
- Accessible: public JSON, schema-compliant  
- Interoperable: STAC 1.0 + EO/SAR/PROJ extensions  
- Reusable: full lineage, licensing, provenance  

Governance record stored at:

~~~~~text
../../../../../docs/reports/audit/versioning_ledger.json
~~~~~

---

## 📡 Telemetry Requirements

Every published asset triggers telemetry:

- `collection_id`
- `item_id`
- `item_count`
- `validation_passed`
- `care_label`
- `masking_applied`
- `artifact_checksum`
- `publish_latency_ms`
- `energy_wh`
- `co2_g`

Telemetry appended to:

~~~~~text
../../../../../../releases/v10.3.0/focus-telemetry.json
~~~~~

---

## 🧪 Local Inspection Examples

Inspect a Collection:

~~~~~bash
jq '.' src/pipelines/stac/monitor-validate-publish/data/published/collections/<collection>.json
~~~~~

Inspect an Item:

~~~~~bash
jq '.' src/pipelines/stac/monitor-validate-publish/data/published/items/<collection>/<item>.json
~~~~~

Check CARE metadata:

~~~~~bash
jq '.["kfm:care_label"]' <item>.json
~~~~~

Check lineage reference:

~~~~~bash
jq '.["kfm:provenance"]' <item>.json
~~~~~

---

## 🕰️ Version History

| Version | Date       | Author | Summary |
|---------|------------|--------|---------|
| v10.3.1 | 2025-11-14 | STAC Pipelines Team | Created complete documentation for Published STAC Assets directory with FAIR+CARE, lineage, immutability, and telemetry compliance. |

---

<div align="center">

**Kansas Frontier Matrix — Published STAC Assets**  
Validated × Immutable × FAIR+CARE × Provenance-Certified  
© 2025 Kansas Frontier Matrix — CC-BY 4.0  

[Back to STAC Data Layer](../README.md)

</div>
