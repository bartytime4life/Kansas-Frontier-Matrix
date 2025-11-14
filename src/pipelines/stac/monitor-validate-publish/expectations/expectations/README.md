---
title: "📏 Kansas Frontier Matrix — STAC Expectation Suites (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/stac/monitor-validate-publish/expectations/expectations/README.md"
version: "v10.3.1"
last_updated: "2025-11-14"
review_cycle: "Quarterly · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/pipelines-stac-expectation-suites-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 📏 **Kansas Frontier Matrix — STAC Expectation Suites**  
`src/pipelines/stac/monitor-validate-publish/expectations/expectations/README.md`

**Purpose:**  
Define the **Great Expectations expectation suites** that enforce STAC 1.0, EO/SAR, PROJ, FAIR+CARE, and KFM metadata contracts for all incoming STAC Items.  
These suites act as the **schema + semantic + ethical backbone** of the *Monitor → Validate → Publish* pipeline.

<img alt="GE Suite" src="https://img.shields.io/badge/Great_Expectations-Expectation_Suite-blue"/>
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Enforced-orange"/>
<img alt="STAC" src="https://img.shields.io/badge/STAC-1.0_Compliant-green"/>
<img alt="Status" src="https://img.shields.io/badge/Status-Active-success"/>

</div>

---

## 📘 Overview

Expectation suites perform **semantic enforcement** beyond JSON schema validation.  
These tests ensure that each STAC Item is:

- Structurally correct  
- Semantically coherent (datetime, cloud cover, projection fields)  
- **Governance-aligned** (CARE labels & masking requirements)  
- **Interoperable** with downstream AI, geospatial, and catalog subsystems  
- Ready for **graph hydration** and **KFM-wide analytics**  

Expectation suites are executed via:

- `stac_items.yml` checkpoint  
- CI (`stac-orchestrator.yml`)  
- Local development runs  
- Quarantine triage workflows  

---

## 🗂️ Directory Layout

~~~~~text
src/pipelines/stac/monitor-validate-publish/expectations/expectations/
├── README.md                      # This file
├── stac_item_schema.json          # STAC 1.0 + KFM extensions schema
├── stac_item_suite.json           # Generated GE suite for all Items
└── custom_rules.json              # KFM-specific expectation definitions
~~~~~

---

## 🧩 Suite Architecture (Indented Mermaid)

~~~~~mermaid
flowchart TD
  A["Incoming STAC JSONL"] --> B["Schema Validation<br/>stac_item_schema.json"]
  B --> C["GE Suite Execution<br/>stac_item_suite.json<br/>+ custom_rules.json"]
  C -->|PASS| D["Publish"]
  C -->|FAIL| E["Quarantine → GitHub Issue → Telemetry"]
~~~~~

---

## 📜 1. `stac_item_schema.json` — JSON Schema Enforcement

This schema defines:

### Required STAC 1.0 fields:
- `id`  
- `type = "Feature"`  
- `geometry`  
- `properties.datetime`  
- `assets`  
- `links[]` with valid `rel`

### EO/SAR fields (when applicable):
- `eo:cloud_cover` ∈ [0,100]  
- `eo:bands`  
- `sar:polarizations`

### Projection fields:
- `proj:epsg`  
- `proj:bbox`  
- `proj:shape`  
- `proj:transform`

### KFM extensions:
- `kfm:checksum` (sha256)  
- `kfm:care_label` (public/sensitive/restricted)  
- `kfm:provenance` (lineage path)  
- `kfm:ingest_version`

**Purpose:**  
Guarantee **minimum viable STAC integrity** before semantic testing begins.

---

## 🧪 2. `stac_item_suite.json` — Great Expectations Core Suite

This suite enforces **semantic constraints**, such as:

### Field existence
- Item ID must exist  
- Geometry must exist and be valid  
- Assets must include required keys (href, type, roles)  

### Value ranges
- `eo:cloud_cover` in `[0,100]`  
- `proj:epsg` must be numeric  
- `properties.gsd` must be ≥ 0  

### Structural integrity
- **Links** must include:
  - `rel=self`
  - `rel=collection`
  - `rel=root`
- **Assets** must have consistent MIME types:
  - `.tif` → `image/tiff; application=geotiff`
  - `.json` → `application/geo+json`

### ID rules
- No duplicates within a batch  
- IDs must match `collection/item` naming rules if present  

### Timestamp structure
- Datetime must be ISO 8601  
- Start/end ranges must be valid if present  

---

## 🧩 3. `custom_rules.json` — KFM-Specific Expectations

KFM extends STAC with governance & provenance metadata.  
Custom expectations include:

### CARE governance rules
- `kfm:care_label` MUST be one of:  
  `["public", "sensitive", "restricted"]`
- If label is **sensitive** or **restricted**, geometry MUST be generalized:
  - H3 (≥ r7),  
  - bbox expansion, or  
  - centroid fuzzing  

### Provenance & Lineage
- `kfm:provenance` must point to a valid lineage path  
- Lineage must contain:
  - checksum  
  - source IDs  
  - ingest version  
  - governance reference  

### License & Ethical Metadata
- `properties.license` must be present  
- Valid SPDX identifier (if publicly licensed)  

### Projection & EO rules
- `proj:epsg` required for rasters  
- `eo:platform` required for optical/satellite sensors  
- All Items with assets of type COG/GeoTIFF must include:
  - gsd  
  - resolution metadata  

---

## 📡 Telemetry Integration

All suite executions contribute the following telemetry:

- `schema_valid`  
- `expectations_passed`  
- `expectations_failed`  
- `care_errors`  
- `governance_errors`  
- `runtime_sec`  
- `energy_wh`  
- `co2_g`  

Telemetry appended to:

~~~~~text
../../../../../releases/v10.3.0/focus-telemetry.json
~~~~~

---

## 🧯 Failure Workflow Integration

If any suite fails:

1. Batch is **quarantined** into  
   ~~~~~text
   data/stac/quarantine/<timestamp>/
   ~~~~~

2. Summary written to:
   ~~~~~text
   last_failure_summary.md
   ~~~~~

3. Issue auto-opened with:
   - Error classes  
   - Failing STAC IDs  
   - Links to quarantined data  

4. Telemetry updated accordingly.

---

## 🧪 Local Development Example

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
| v10.3.1 | 2025-11-14 | STAC Pipelines Team | Added suite documentation per KFM Markdown rules; aligned with GE v1.0 and KFM extensions. |

---

<div align="center">

**Kansas Frontier Matrix — STAC Expectation Suites**  
Schema Integrity × Ethical Metadata × FAIR+CARE × Deterministic Validation  
© 2025 Kansas Frontier Matrix — CC-BY 4.0  

[Back to Expectations Root](../README.md)

</div>
