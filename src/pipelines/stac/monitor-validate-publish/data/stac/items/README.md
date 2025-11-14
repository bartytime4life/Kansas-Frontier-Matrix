---
title: "🛰️ Kansas Frontier Matrix — STAC Items Storage (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/stac/monitor-validate-publish/data/stac/items/README.md"
version: "v10.3.1"
last_updated: "2025-11-14"
review_cycle: "Quarterly · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../../../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/pipelines-stac-items-v1.json"
governance_ref: "../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🛰️ **Kansas Frontier Matrix — STAC Items Storage**  
`src/pipelines/stac/monitor-validate-publish/data/stac/items/README.md`

**Purpose:**  
Define the authoritative, FAIR+CARE-certified storage rules for **validated and normalized STAC Items** produced by the STAC Monitor → Validate → Publish pipeline.  
Every Item in this directory is fully **immutable**, **versioned**, **provenance-linked**, and **safe for system-wide usage** (Neo4j graph hydration, timeline overlays, Focus Mode v2.4, and catalog exports).

<img alt="STAC Items" src="https://img.shields.io/badge/STAC_Items-Versioned-blue"/>
<img alt="Governance" src="https://img.shields.io/badge/FAIR%2BCARE-Governed-orange"/>
<img alt="Immutable" src="https://img.shields.io/badge/Immutable-Strict-green"/>
<img alt="Status" src="https://img.shields.io/badge/Status-Active-success"/>

</div>

---

## 📘 Overview

The **Items layer** represents the **lowest-level geospatial entities** in the STAC hierarchy.  
After passing validation + transformation, each STAC Item is written to:

~~~~~text
src/pipelines/stac/monitor-validate-publish/data/stac/items/<collection_id>/<item_id>.json
~~~~~

Each Item:

- Has passed JSON Schema + Great Expectations validation  
- Includes all required KFM metadata fields (checksum, care_label, provenance, ingest_version)  
- Is fully immutable  
- Is valid for indexing in the STAC Catalog and Neo4j Scene graph  
- Can be consumed by map renderers, timelines, and Focus Mode reasoning  

---

## 🗂️ Directory Layout

~~~~~text
src/pipelines/stac/monitor-validate-publish/data/stac/items/
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

Each `collection_id` corresponds to a published STAC Collection.

---

## 🧩 Required STAC Item Structure

Each STAC Item MUST satisfy:

### STAC Core (Required)
- `"type": "Feature"`
- `"id": "<item_id>"`
- `"geometry"` (valid GeoJSON)
- `"bbox"` optional but recommended
- `"properties.datetime"` (ISO8601)
- `"assets"` dictionary with valid roles and MIME types
- `"links"` including:
  - `self`
  - `collection`
  - `root`

### STAC Extensions (When applicable)
- `eo:*` — cloud cover, bands, platform  
- `proj:*` — epsg, transform, bbox, shape  
- `sar:*` — polarizations, look direction  
- `scientific:*` — citations, DOIs  
- Any applicable KFM standard extensions

### KFM Metadata Extensions (Required)

All Items MUST include:

| Field | Description |
|-------|-------------|
| `kfm:checksum` | sha256 checksum for immutability |
| `kfm:care_label` | public / sensitive / restricted |
| `kfm:provenance` | lineage path |
| `kfm:ingest_version` | orchestrator version |
| `kfm:sovereignty_notes` | optional, cultural/tribal metadata |
| `kfm:masking_strategy` | required if care_label = sensitive/restricted |

---

## 🔒 Immutability Rules

Once written to this directory, a STAC Item becomes **permanent**.

Forbidden:

- ❌ Editing existing JSON files  
- ❌ Updating metadata in-place  
- ❌ Changing geometry or properties after publication  
- ❌ Altering CARE labels post-hoc  
- ❌ Overwriting Items with regenerated versions  

Allowed:

- ✔ Publishing a **new version** (via SemVer rules)  
- ✔ Adding **new Items** with new IDs  
- ✔ Updating Collections to reference new Items  

KFM considers each Item a **historical record**.

---

## 🧬 Versioning Requirements

Each Item must:

- Belong to a versioned Collection  
- Use implicit versioning via Collection version or explicit:
  - `properties.version`  
  - or ID-level encoding in advanced pipelines  

Lineage MUST reference:

~~~~~text
data/lineage/<dataset_id>/<version>/lineage.json
~~~~~

Example:

~~~~~json
"kfm:provenance": "data/lineage/landsat-c2-l2/v10.3.1/lineage.json"
~~~~~

---

## 🧭 Governance: FAIR+CARE Enforcement

### CARE Requirements

If Item is labeled `sensitive` or `restricted`:

- Geometry MUST be generalized:
  - H3 r7+, bbox padding, centroid perturbation  
- Metadata MUST declare:
  - `kfm:masking_strategy`
  - `kfm:sovereignty_notes` if tribal territory intersects  

### FAIR Requirements

- **Findable:** predictable paths & IDs  
- **Accessible:** STAC 1.0 JSON  
- **Interoperable:** validated STAC Extensions  
- **Reusable:** lineage, license, checksums required  

Governance events logged to:

~~~~~text
../../../../../docs/reports/audit/versioning_ledger.json
~~~~~

---

## 📡 Telemetry Integration

Each Item publication emits telemetry into:

~~~~~text
../../../../../releases/v10.3.0/focus-telemetry.json
~~~~~

Telemetry fields for Items include:

- `item_id`  
- `collection_id`  
- `validation_passed`  
- `care_label`  
- `artifact_checksum`  
- `geometry_masked`  
- `publish_latency_ms`  
- `energy_wh`, `co2_g`  

---

## 🧪 Local Inspection Examples

Inspect Item metadata:

~~~~~bash
jq '.' src/pipelines/stac/monitor-validate-publish/data/stac/items/<collection>/<item_id>.json
~~~~~

Check CARE label:

~~~~~bash
jq '.["kfm:care_label"]' <item>.json
~~~~~

Check geometry validity:

~~~~~bash
jq '.geometry' <item>.json | geojsonhint -
~~~~~

Inspect provenance:

~~~~~bash
jq '.["kfm:provenance"]' <item>.json
~~~~~

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|--------|--------|---------|
| v10.3.1 | 2025-11-14 | STAC Pipelines Team | Created complete documentation for STAC Item storage with CARE, governance, lineage and telemetry alignment. |

---

<div align="center">

**Kansas Frontier Matrix — STAC Item Storage**  
Immutable Geospatial Assets × FAIR+CARE × Provenance Enforcement  
© 2025 Kansas Frontier Matrix — CC-BY 4.0  

[Back to STAC Storage Root](../README.md)

</div>
