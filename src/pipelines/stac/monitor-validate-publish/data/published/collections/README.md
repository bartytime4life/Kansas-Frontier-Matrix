---
title: "📚 Kansas Frontier Matrix — Published STAC Collections (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/stac/monitor-validate-publish/data/published/collections/README.md"
version: "v10.3.1"
last_updated: "2025-11-14"
review_cycle: "Quarterly · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../../../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/pipelines-stac-published-collections-v1.json"
governance_ref: "../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 📚 **Kansas Frontier Matrix — Published STAC Collections**  
`src/pipelines/stac/monitor-validate-publish/data/published/collections/README.md`

**Purpose:**  
Document the authoritative, immutable, FAIR+CARE-certified **STAC Collections** produced by the STAC Monitor → Validate → Publish orchestrator.  
These Collections serve as the **dataset-level roots** for all STAC Items and provide the canonical metadata used across **Neo4j graph linking**, **STAC/DCAT catalog exports**, **timeline visualizations**, and **Focus Mode v2.4 dataset reasoning**.

<img alt="STAC Collections" src="https://img.shields.io/badge/STAC_Collections-Canonical-blue"/>
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Governed-orange"/>
<img alt="Immutable" src="https://img.shields.io/badge/Immutable-Enforced-green"/>
<img alt="Status" src="https://img.shields.io/badge/Status-Active-success"/>

</div>

---

## 📘 Overview

This directory contains **validated, normalized, immutable STAC 1.0 Collections**.  
Each Collection acts as a **dataset root**, describing:

- Dataset identity  
- Dataset version  
- Spatial & temporal extents  
- Providers & licensing  
- STAC extension usage  
- Link relations  
- KFM governance & lineage metadata  

Only Collections that **pass all validation, schema, CARE, and provenance requirements** are written here.

---

## 🗂️ Directory Layout

~~~~~text
src/pipelines/stac/monitor-validate-publish/data/published/collections/
├── README.md
└── <collection_id>.json
~~~~~

Example filenames:

~~~~~text
landsat-c2-l2.json
sentinel-2-l2a.json
noaa-storm-events.json
historic-topography.json
~~~~~

---

## 🧩 Required Collection Structure

All Collections MUST include the following:

### STAC Core
- `"type": "Collection"`
- `"id": "<collection_id>"`
- `"stac_version": "1.0.0"`
- `"description"` — non-empty, dataset-level summary  
- `"license"` — valid SPDX or provider license  
- `"links"` — must include:
  - `rel=self`
  - `rel=root`
  - `rel=items`
  - `rel=parent` (if nested)
  - Optional: `rel=version`, `rel=derived_from`  

### STAC Extent
- `"extent.spatial.bbox"` — WGS84  
- `"extent.temporal.interval"` — start/end time of dataset

### STAC Extensions
All applicable extensions must be declared:

- `proj` — for projected datasets  
- `eo` — for optical/satellite data  
- `sar` — radar collections  
- `scientific` — citations/DOIs  
- Any required KFM extension(s)

### KFM Governance Metadata (Required)

| Field | Purpose |
|-------|---------|
| `kfm:checksum` | sha256 integrity record |
| `kfm:care_label` | public / sensitive / restricted |
| `kfm:provenance` | full lineage path |
| `kfm:ingest_version` | orchestrator or ETL version |
| `kfm:sovereignty_notes` | optional tribal/heritage metadata |
| `kfm:masking_strategy` | required for sensitive/restricted |

---

## 🧩 Collection Publication Flow (Indented Mermaid)

~~~~~mermaid
flowchart TD
  A["Validated Items"] --> B["Normalize + Consolidate Metadata"]
  B --> C["Generate Collection JSON"]
  C --> D["Write to data/published/collections/"]
  D --> E["Neo4j Hydration<br/>Dataset Nodes"]
  D --> F["STAC/DCAT Catalog Exports"]
  D --> G["Telemetry + Governance Logging"]
~~~~~

---

## 🔒 Immutability & Version Requirements

Once written, **Collections cannot be edited**, modified, or overwritten.

Forbidden:

- ❌ Editing any published Collection JSON  
- ❌ Altering license, extents, CARE label, or links in-place  
- ❌ Rewriting a Collection for the same version  

Allowed:

- ✔ Publishing a new version via SemVer rules  
- ✔ Adding new Collections  
- ✔ Regenerating Items under a new dataset version  

SemVer enforcement documented in:

~~~~~text
src/pipelines/architecture/versioning/rules/semver_enforcement.md
~~~~~

---

## 🧠 Governance (FAIR+CARE)

STAC Collections MUST adhere to:

### CARE Requirements

- Label each dataset `public`, `sensitive`, or `restricted`  
- If cultural or tribal context applies:
  - Add sovereignty notes  
  - Require masking/generalization in Items  
- Sensitive or restricted datasets must not expose precise coordinates  

### FAIR Requirements

- **Findable:** predictable filename + directory structure  
- **Accessible:** JSON (UTF-8), open metadata  
- **Interoperable:** STAC 1.0 + declared extensions  
- **Reusable:** lineage, checksums, licenses, metadata completeness  

Governance decisions logged to:

~~~~~text
../../../../../../docs/reports/audit/versioning_ledger.json
~~~~~

---

## 📡 Telemetry Integration

Publishing a Collection writes telemetry entries containing:

- `collection_id`
- `item_count`
- `checksum`
- `care_label`
- `publish_latency_ms`
- `version`
- `lineage_checksum`
- Energy/CO₂ metrics

Stored at:

~~~~~text
../../../../../../releases/v10.3.0/focus-telemetry.json
~~~~~

---

## 🧪 Local Inspection Examples

Inspect a Collection:

~~~~~bash
jq '.' src/pipelines/stac/monitor-validate-publish/data/published/collections/<collection_id>.json
~~~~~

Check KFM fields:

~~~~~bash
jq '.["kfm:care_label"]' <collection_id>.json
~~~~~

Inspect extents:

~~~~~bash
jq '.extent' <collection_id>.json
~~~~~

---

## 🕰️ Version History

| Version | Date       | Author | Summary |
|---------|------------|--------|---------|
| v10.3.1 | 2025-11-14 | STAC Pipelines Team | Added complete FAIR+CARE, lineage, and immutability documentation for published STAC Collections. |

---

<div align="center">

**Kansas Frontier Matrix — Published STAC Collections**  
Dataset Roots × Immutable Metadata × FAIR+CARE Governance  
© 2025 Kansas Frontier Matrix — CC-BY 4.0  

[Back to Published Root](../README.md)

</div>
