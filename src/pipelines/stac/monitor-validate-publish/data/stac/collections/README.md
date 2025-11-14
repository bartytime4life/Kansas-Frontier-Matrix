---
title: "📚 Kansas Frontier Matrix — STAC Collections Storage (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/stac/monitor-validate-publish/data/stac/collections/README.md"
version: "v10.3.1"
last_updated: "2025-11-14"
review_cycle: "Quarterly · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../../../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/pipelines-stac-collections-v1.json"
governance_ref: "../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 📚 **Kansas Frontier Matrix — STAC Collections Storage**  
`src/pipelines/stac/monitor-validate-publish/data/stac/collections/README.md`

**Purpose:**  
Define the storage rules, metadata requirements, immutability guarantees, and FAIR+CARE governance constraints for **STAC Collections** published by the STAC Monitor → Validate → Publish orchestrator.  
Collections stored here serve as the **canonical dataset definitions** for all STAC Items, timeline layers, geospatial pipelines, and graph hydration in the Kansas Frontier Matrix (KFM).

<img alt="STAC Collections" src="https://img.shields.io/badge/STAC_Collections-Versioned-blue"/>
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Governed-orange"/>
<img alt="Immutable" src="https://img.shields.io/badge/Immutable-Enforced-green"/>
<img alt="Status" src="https://img.shields.io/badge/Status-Active-success"/>

</div>

---

## 📘 Overview

This directory contains **validated, transformed, immutable STAC 1.0 Collections**.  
Each Collection provides:

- Dataset identity  
- Spatial and temporal extents  
- Dataset-wide metadata (license, providers, summaries)  
- Links to items, root catalog, and version chains  
- KFM-specific metadata (provenance, CARE labels, lineage references)  

Collections here represent **FAIR+CARE–certified datasets** and anchor the entire Item structure.

---

## 🗂️ Directory Layout

~~~~~text
src/pipelines/stac/monitor-validate-publish/data/stac/collections/
├── README.md                        # This file
└── <collection_id>.json             # One STAC Collection per dataset
~~~~~

Examples:

~~~~~text
landsat-c2-l2.json
sentinel-2-l2a.json
noaa-storm-events.json
historic-topography.json
~~~~~

---

## 🧩 Collection Responsibilities

A STAC Collection defines the **dataset envelope**, including:

- Dataset **identity**  
- Dataset **version** (if applicable)  
- **Spatial extent** (bbox)  
- **Temporal range**  
- **Provider metadata**  
- **License & access constraints**  
- **Links to Items**, root catalog, and version chains  
- **STAC Extensions** (proj, eo, sar, kfm)  
- **KFM metadata** for governance & provenance  

Each Collection must be consistent with:

- Published Items (`data/stac/items/<collection_id>/*.json`)  
- DCAT export  
- Lineage bundles  
- Telemetry records  
- Governance contracts  

---

## 📦 Required Fields in STAC Collections

All Collection JSON files must include the following:

### STAC Core

- `"type": "Collection"`
- `"id": "<collection_id>"`
- `"stac_version": "1.0.0"`
- `"description"` (non-empty)
- `"license"` (SPDX or provider-compliant)
- `"extent"`:
  - `"spatial.bbox"` (EPSG:4326)
  - `"temporal.interval"`

### STAC Extensions

- `"stac_extensions"` (proj, eo, sar, scientific, etc.)

### Links

Must contain:

- `rel: "self"`
- `rel: "root"`
- `rel: "parent"`
- `rel: "items"`

Optional but recommended:

- `rel: "version"` (links to previous version when applicable)
- `rel: "derived_from"`

### KFM Metadata (Required)

- `kfm:checksum` (sha256)
- `kfm:care_label` (public / sensitive / restricted)
- `kfm:provenance` (path to lineage)
- `kfm:ingest_version`
- Optional sovereignty fields:
  - `kfm:masking_strategy`
  - `kfm:sovereignty_notes`

---

## 🧭 Governance Rules (FAIR+CARE)

### CARE Compliance

Collections MUST explicitly declare:

- CARE label  
- Sovereignty or cultural-sensitivity notes  
- Masking/generalization rules for sensitive datasets  

If a Collection includes:

- tribal land boundaries  
- cultural heritage data  
- archaeological site references  
- restricted ecological species locations  

Then:

- `kfm:care_label = "sensitive" | "restricted"`  
- `kfm:masking_strategy` MUST be present  

### FAIR Compliance

- **Findable:** predictable paths + STAC 1.0 structure  
- **Accessible:** open metadata, machine-readable JSON  
- **Interoperable:** EO/SAR/PROJ extensions must match Items  
- **Reusable:** provenance, license, lineage required  

Governance oversight stored in:

~~~~~text
../../../../../docs/reports/audit/versioning_ledger.json
~~~~~

---

## 🔒 Immutability Rules

Collections stored here are **immutable**.

Forbidden:

- ❌ Editing fields in-place  
- ❌ Replacing a Collection with new metadata  
- ❌ Correcting typos without a new version  
- ❌ Changing license, CARE label, or extents post-publication  

Allowed:

- ✔ Publishing a **new version** (SemVer required)  
- ✔ Adding new Collection IDs  
- ✔ Regenerating Items for a new version  

---

## 🧬 Versioning & Lineage

Every Collection must include:

- `properties.version` OR `version` field (SemVer recommended)
- Lineage reference in KFM metadata:
  - `kfm:provenance` → `data/lineage/<dataset_id>/<version>/lineage.json`
- Checksum (sha256)
- Version links (`rel=version`) if applicable

Example versioned Collection:

~~~~~text
landsat-c2-l2_v10.3.1.json
~~~~~

---

## 📡 Telemetry Bindings

Each Collection publish event MUST include telemetry:

- `collection_id`
- `collection_checksum`
- `care_label`
- `item_count`
- `publish_latency_ms`
- `validation_passed`
- Energy/CO₂ metrics

Telemetry appended to:

~~~~~text
../../../../../releases/v10.3.0/focus-telemetry.json
~~~~~

---

## 🧪 Validation Rules (CI Enforced)

Collections MUST pass:

- JSON Schema validation (`stac_item_schema.json` where applicable)
- Great Expectations suite (Collection-level, if defined)
- CARE governance checks
- License verification
- Link integrity checks  
- KFM metadata presence

CI workflows:

- `stac-validate.yml`
- `faircare-validate.yml`
- `docs-lint.yml`
- `telemetry-export.yml`

---

## 🧰 Local Inspection Examples

View collection metadata:

~~~~~bash
jq '.' src/pipelines/stac/monitor-validate-publish/data/stac/collections/<id>.json
~~~~~

Check for KFM metadata:

~~~~~bash
jq '.["kfm:provenance"]' <id>.json
~~~~~

Inspect spatial extent:

~~~~~bash
jq '.extent.spatial.bbox' <id>.json
~~~~~

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|--------|--------|---------|
| v10.3.1 | 2025-11-14 | STAC Pipelines Team | Created full Collections storage documentation with governance, versioning, immutability, and telemetry rules. |

---

<div align="center">

**Kansas Frontier Matrix — STAC Collections Storage**  
Immutable Dataset Definitions × FAIR+CARE Ethics × Provenance-Linked Metadata  
© 2025 Kansas Frontier Matrix — CC-BY 4.0  

[Back to STAC Storage Root](../README.md)

</div>
