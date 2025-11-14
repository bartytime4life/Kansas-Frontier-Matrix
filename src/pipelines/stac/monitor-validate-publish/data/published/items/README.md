---
title: "🛰️ Kansas Frontier Matrix — Published STAC Items (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/stac/monitor-validate-publish/data/published/items/README.md"
version: "v10.3.1"
last_updated: "2025-11-14"
review_cycle: "Quarterly · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../../../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/pipelines-stac-published-items-v1.json"
governance_ref: "../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🛰️ **Kansas Frontier Matrix — Published STAC Items**  
`src/pipelines/stac/monitor-validate-publish/data/published/items/README.md`

**Purpose:**  
Document the authoritative, immutable, FAIR+CARE-governed **STAC Items** produced by the STAC Monitor → Validate → Publish pipeline.  
These files represent **validated, normalized, versioned geospatial assets** ready for use across KFM’s mapping engine, Neo4j knowledge graph, AI (Focus Mode v2.4), catalog publishing, and scientific analysis workflows.

<img alt="STAC Items" src="https://img.shields.io/badge/STAC_Items-Canonical-blue"/>
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Governed-orange"/>
<img alt="Immutable" src="https://img.shields.io/badge/Immutable-Enforced-green"/>
<img alt="Status" src="https://img.shields.io/badge/Status-Active-success"/>

</div>

---

## 📘 Overview

The **published STAC Items** directory contains finalized STAC Item JSON files that have:

- Passed **JSON Schema validation**
- Passed **Great Expectations semantic validation**
- Passed **FAIR+CARE governance checks**
- Passed **KFM metadata extension validation**
- Been **normalized** by the orchestrator’s `transform.py`
- Been **approved for publication** and **graph hydration**

These Items are **immutable snapshots** of geospatial, temporal, and provenance data.

---

## 🗂️ Directory Layout

~~~~~text
src/pipelines/stac/monitor-validate-publish/data/published/items/
├── README.md
└── <collection_id>/
    └── <item_id>.json
~~~~~

Examples:

~~~~~text
landsat-c2-l2/
  LC09_L2SP_030033_20230813_20230819_02_T1.json

sentinel-2-l2a/
  S2A_31TCJ_20230711_0_L2A.json
~~~~~

---

## 🧩 Required STAC Item Structure

STAC Items MUST follow STAC **1.0.0** specification plus required KFM metadata extensions.

### STAC Core Requirements
- `"type": "Feature"`
- `"id": "<item_id>"`
- `"geometry"` — valid GeoJSON
- `"properties.datetime"` — ISO 8601 datetime
- `"assets"` — valid roles, MIME types, hrefs
- `"links"` — MUST include:
  - `rel=self`
  - `rel=collection`
  - `rel=root`

### STAC Extensions (conditional)
- EO (`eo:*`)
- PROJ (`proj:*`)
- SAR (`sar:*`)
- Scientific (`sci:*`)
- Others required by dataset type

### KFM Metadata Extensions (MANDATORY)

| Field | Description |
|-------|-------------|
| `kfm:checksum` | sha256 checksum for immutability |
| `kfm:care_label` | public / sensitive / restricted |
| `kfm:provenance` | lineage JSON reference |
| `kfm:ingest_version` | orchestrator version (SemVer) |
| `kfm:masking_strategy` | required if sensitive/restricted |
| `kfm:sovereignty_notes` | optional cultural/tribal metadata |

These fields are enforced by GE + custom validators.

---

## 🧬 Versioning & Lineage

Published Items MUST:

- Belong to a versioned Collection  
- Include explicit lineage reference:

~~~~~text
data/lineage/<dataset_id>/<version>/lineage.json
~~~~~

Example:

~~~~~json
"kfm:provenance": "data/lineage/landsat-c2-l2/v10.3.1/lineage.json"
~~~~~

Lineage bundles contain:

- Checksums  
- Source STAC IDs  
- Original provider metadata  
- Ingest metadata  
- From/derived-from relationships  

---

## 🔒 Immutability Rules

Published Items are **never modified**.

Forbidden:

- ❌ Editing Item JSON files  
- ❌ Changing metadata in-place  
- ❌ Adjusting geometry, assets, or timestamps  
- ❌ Replacing files for same ID/version  
- ❌ Updating CARE labels after publication  

Allowed:

- ✔ Creating **new versioned Items**  
- ✔ Publishing additional Items under same Collection  
- ✔ Updating Collection files to include version links  

KFM's governance requires that **historical STAC Items remain pristine for reproducibility**.

---

## 🧭 FAIR+CARE Governance Enforcement

### CARE Requirements

If Item is **sensitive** or **restricted**:

- Geometry MUST be generalized (H3 r7+, centroid fuzzing, buffered bbox, etc.)
- `kfm:masking_strategy` MUST be present
- Governance reviewers must confirm:
  - Sovereignty impact  
  - Cultural sensitivity  
  - Redistribution limitations  

### FAIR Requirements

- **Findable:** predictable path structure  
- **Accessible:** STAC 1.0 JSON  
- **Interoperable:** STAC Extensions + PROJ + EO/SAR  
- **Reusable:** provenance metadata required  

Governance log reference:

~~~~~text
../../../../../../docs/reports/audit/versioning_ledger.json
~~~~~

---

## 📡 Telemetry Requirements

Publication writes telemetry fields:

- `item_id`
- `collection_id`
- `validation_passed`
- `artifact_checksum`
- `care_label`
- `masking_applied`
- `publish_latency_ms`
- `energy_wh`
- `co2_g`

Telemetry appended to:

~~~~~text
../../../../../../releases/v10.3.0/focus-telemetry.json
~~~~~

---

## 🧪 Validation Requirements

Items MUST pass:

- JSON Schema validation  
- GE suite validation (`stac_item_suite`)  
- Link integrity checks  
- MIME/asset role checks  
- CARE enforcement rules  
- Provenance chain check  
- Lineage consistency check  
- File checksum verification  

Any failure → **quarantine**, GitHub Issue, governance review.

---

## 🧰 Local Inspection Examples

Inspect full metadata:

~~~~~bash
jq '.' src/pipelines/stac/monitor-validate-publish/data/published/items/<collection>/<item_id>.json
~~~~~

Check CARE compliance:

~~~~~bash
jq '.["kfm:care_label"]' <item>.json
~~~~~

Validate geometry:

~~~~~bash
jq '.geometry' <item>.json | geojsonhint -
~~~~~

Inspect lineage link:

~~~~~bash
jq '.["kfm:provenance"]' <item>.json
~~~~~

---

## 🕰️ Version History

| Version | Date       | Author | Summary |
|---------|------------|--------|---------|
| v10.3.1 | 2025-11-14 | STAC Pipelines Team | Added authoritative documentation for Published STAC Items, including FAIR+CARE, immutability, lineage, and telemetry requirements. |

---

<div align="center">

**Kansas Frontier Matrix — Published STAC Items**  
Immutable Geospatial Records × FAIR+CARE × Provenance-Linked × Machine-Ready  
© 2025 Kansas Frontier Matrix — CC-BY 4.0  

[Back to Published Root](../README.md)

</div>
