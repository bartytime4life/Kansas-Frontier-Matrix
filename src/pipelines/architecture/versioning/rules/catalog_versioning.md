---
title: "🗂️ Kansas Frontier Matrix — STAC/DCAT Catalog Versioning Rules (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/architecture/versioning/rules/catalog_versioning.md"
version: "v10.3.1"
last_updated: "2025-11-13"
review_cycle: "Quarterly · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../../../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/pipelines-versioning-catalog-rules-v1.json"
governance_ref: "../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🗂️ **Kansas Frontier Matrix — STAC/DCAT Catalog Versioning Rules**  
`src/pipelines/architecture/versioning/rules/catalog_versioning.md`

**Purpose:**  
Define the **versioning rules, structural contracts, metadata invariants, and FAIR+CARE governance constraints** for all STAC 1.0 and DCAT 3.0 catalog entries within Kansas Frontier Matrix (KFM).  
These rules ensure **immutable catalog history**, **consistent dataset discovery**, **sovereignty-aware metadata**, and **MCP-DL v6.3 compliance**.

<img alt="STAC" src="https://img.shields.io/badge/STAC-1.0-blue"/>
<img alt="DCAT" src="https://img.shields.io/badge/DCAT-3.0-green"/>
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Certified-orange"/>
<img alt="Status" src="https://img.shields.io/badge/Status-Enforced-success"/>

</div>

---

## 📘 Overview

STAC & DCAT catalogs in KFM must:

- Reflect **exact dataset versions**  
- Provide **append-only version chains**  
- Preserve **lineage, CARE, and license metadata**  
- Maintain **strict metadata consistency**  
- Be fully interoperable across **2D, 3D, AI, temporal, and geospatial layers**  
- Support **version-aware Focus Mode** and **Predictive Futures (2030–2100)**  

This document defines the **rules enforced in CI** and required for all catalog entries.

---

## 📁 Directory Context

~~~~~text
src/pipelines/architecture/versioning/rules/
├── README.md
├── semver_enforcement.md
├── artifact_immutability.md
├── catalog_versioning.md          # This file
├── lineage_rules.md
└── governance_requirements.md
~~~~~

---

## 🧩 STAC/DCAT Versioning Architecture (Indented Mermaid)

~~~~~mermaid
flowchart TD
  A["Versioned Artifact<br/>vX.Y.Z"] --> B["STAC Item<br/>Versioned ID & Properties"]
  B --> C["DCAT Dataset<br/>Version-Coupled Metadata"]
  C --> D["Version Chain<br/>Graph of Releases"]
  D --> E["FAIR+CARE Governance<br/>CARE Labels · Sovereignty"]
  E --> F["Catalog Publication<br/>Immutable · Append-Only"]
~~~~~

---

## 🗂️ STAC Versioning Rules

### 1. STAC Item Naming  
STAC Items MUST follow:

~~~~~text
{dataset_id}_{version}.json
~~~~~

Example:

~~~~~text
hydrology_flow_ks_v10.3.1.json
~~~~~

---

### 2. Required STAC Properties

Each STAC Item MUST include:

| Field | Requirement |
|-------|-------------|
| `properties.version` | MUST equal SemVer version |
| `kfm:checksum` | sha256 of artifact |
| `kfm:care_label` | CARE label (`public`, `sensitive`, `restricted`) |
| `kfm:provenance` | Lineage file reference |
| `kfm:sovereignty` | REQUIRED for Indigenous or heritage data |

---

### 3. Version Graph Links

Each STAC Item MUST include:

~~~~~json
{
  "rel": "version",
  "href": "hydrology_flow_ks_v10.3.0.json"
}
~~~~~

Rules:

- Must link backward to previous version  
- Must NOT link forward  
- No deletion of historical version links  

---

### 4. Asset Rules

All `assets.data` entries must be:

- Immutable  
- Version-scoped  
- Checksummed (via `kfm:checksum`)  
- Free of absolute paths to private storage unless restricted via CARE  

Forbidden:

- Replacing assets under a version  
- Storing coordinate-sensitive assets without masking metadata  

---

## 📚 DCAT Versioning Rules

### 1. Dataset Version Identification

DCAT fields must contain:

| Field | Rules |
|-------|-------|
| `dct:identifier` | Stable across versions |
| `dct:hasVersion` | MUST list SemVer version |
| `dct:provenance` | Lineage reference |
| `dct:license` | SPDX-compatible |
| `dct:temporal` | MUST match STAC temporal extent |
| `dct:spatial` | MUST match STAC geometry (or generalized representation) |

---

### 2. Version Mapping Consistency

STAC and DCAT MUST agree on:

- Version  
- Dataset ID  
- Checksum  
- CARE label  
- Sovereignty metadata  
- Provenance references  
- Bounding box / geometry  
- Temporal extent  

Mismatch → **Critical CI Failure**.

---

## 🔗 Version Chain Rules

Version chains MUST be recorded in:

~~~~~text
data/lineage/{dataset_id}/{version}/lineage.json
~~~~~

And represented in catalogs:

~~~~~json
{
  "version": "v10.3.1",
  "previous": "v10.3.0"
}
~~~~~

Rules:

- Chains MUST be complete  
- No gaps allowed  
- Previous version must exist  
- Chains must be immutable  

---

## ⚖️ CARE + Sovereignty Requirements

Every catalog entry MUST include:

- `kfm:care_label`  
- `kfm:sovereignty` if Indigenous or heritage content exists  
- Masking metadata (`h3_r7`, bbox generalization, fuzzing)  
- No publication allowed without sovereignty review for restricted datasets  

Missing sovereignty metadata → **automatic rejection**.

---

## 📦 Example STAC Versioned Item

~~~~~json
{
  "id": "hydrology_flow_ks_v10.3.1",
  "type": "Feature",
  "stac_version": "1.0.0",
  "properties": {
    "title": "Hydrology Flow (Kansas)",
    "version": "v10.3.1",
    "kfm:checksum": "sha256:c7bbf233a1...",
    "kfm:care_label": "public",
    "kfm:provenance": "data/lineage/hydrology_flow_ks/v10.3.1/lineage.json"
  },
  "links": [
    { "rel": "version", "href": "hydrology_flow_ks_v10.3.0.json" }
  ]
}
~~~~~

---

## 📡 Telemetry Rules

Each versioned STAC/DCAT entry MUST generate telemetry with:

- Version  
- Dataset ID  
- CARE label  
- Checksum  
- Energy/CO₂ usage  
- Governance review result  

Telemetry written to:

~~~~~text
../../../../../../../releases/v10.3.0/focus-telemetry.json
~~~~~

---

## 🚫 Forbidden Catalog Behaviors

- Overwriting STAC Items for an existing version  
- Mismatched STAC/DCAT metadata  
- Missing provenance fields  
- Publishing sensitive data without masking rules  
- Publishing without governance approval  
- Publishing future/backdated links breaking version graph  

Any violation → **Critical CI Failure**.

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|--------|--------|---------|
| v10.3.1 | 2025-11-13 | Pipeline Architecture Team | Added full STAC/DCAT versioning rules including CARE, sovereignty, lineage chain, and telemetry requirements. |

---

<div align="center">

**Kansas Frontier Matrix — Catalog Versioning Rules**  
Immutable Metadata × FAIR+CARE × Deterministic Discovery  
© 2025 Kansas Frontier Matrix — MIT License  

[Back to Versioning Rules](../README.md)

</div>
