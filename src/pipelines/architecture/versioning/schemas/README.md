---
title: "📚 Kansas Frontier Matrix — Versioning Schemas Specification (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/architecture/versioning/schemas/README.md"
version: "v10.3.1"
last_updated: "2025-11-13"
review_cycle: "Quarterly · Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/pipelines-versioning-schemas-v1.json"
governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 📚 **Kansas Frontier Matrix — Versioning Schemas Specification**  
`src/pipelines/architecture/versioning/schemas/README.md`

**Purpose:**  
Define the **canonical JSON Schemas** governing versioned artifacts, STAC/DCAT metadata, lineage bundles, and governance-version records across the Kansas Frontier Matrix (KFM).  
These schemas ensure **immutable version history**, **deterministic lineage**, **FAIR+CARE compliance**, and **MCP-DL v6.3 documentation-first consistency**.

<img alt="Docs" src="https://img.shields.io/badge/Docs-MCP_v6.3-blue"/>
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Certified-orange"/>
<img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-green"/>
<img alt="Status: Stable" src="https://img.shields.io/badge/Status-Stable-success"/>

</div>

---

## 📘 Overview

Versioning schemas formalize:

- Artifact version metadata  
- STAC/DCAT versioning contract  
- Version→lineage linking  
- Governance approval structures  
- Version chain formation  
- Immutable publication rules  

All schemas MUST:

- Validate via JSON Schema Draft 2020-12  
- Pass FAIR+CARE governance gates  
- Emit provenance + telemetry references  
- Use deterministic field ordering  
- Be backward-compatible unless SemVer **MAJOR** bump occurs  

---

## 📁 Directory Layout

~~~~~text
src/pipelines/architecture/versioning/schemas/
├── README.md                         # This file
├── artifact_version.schema.json      # Schema for versioned artifacts
├── stac_item_version.schema.json     # Schema for versioned STAC Items
├── lineage_version.schema.json       # Schema for versioned lineage bundles
├── governance_version.schema.json    # Schema for governance decision records
└── version_chain.schema.json         # Schema for version history graphs
~~~~~

---

## 🧩 Schema Architecture (Indented Mermaid)

~~~~~mermaid
flowchart TD
  AV["artifact_version.schema.json"] --> VC["version_chain.schema.json"]
  ST["stac_item_version.schema.json"] --> VC
  LG["lineage_version.schema.json"] --> VC
  GV["governance_version.schema.json"] --> VC
  VC --> PUB["Immutable Version Archive<br/>Append-Only · FAIR+CARE Validated"]
~~~~~

---

## 📦 Artifact Version Schema (Summary)

Defines version metadata for pipeline outputs:

- `artifact_id`
- `version` (SemVer strict)
- `artifact_uri`
- `checksum` (sha256 required)
- `care_label`
- `lineage_ref`
- `telemetry_ref`
- `governance_ref`

Example Outline:

~~~~~json
{
  "type": "object",
  "required": ["artifact_id", "version", "artifact_uri", "checksum", "care_label"],
  "properties": {
    "artifact_id": { "type": "string" },
    "version": { "type": "string", "pattern": "^v\\d+\\.\\d+\\.\\d+$" },
    "checksum": { "type": "string", "pattern": "^sha256:" },
    "care_label": { "enum": ["public", "sensitive", "restricted"] }
  }
}
~~~~~

---

## 🗺️ STAC Item Version Schema (Summary)

Extends STAC 1.0 + Versioning Extension.

Requirements:

- `id = {dataset_id}_{version}`
- `properties.version`
- `properties.kfm:checksum`
- `links[rel="version"]` entries
- CARE label in `properties.kfm:care_label`

Example Outline:

~~~~~json
{
  "allOf": [
    { "$ref": "https://schemas.stacspec.org/v1.0.0/item-spec/json-schema/item.json" }
  ],
  "properties": {
    "properties": {
      "type": "object",
      "required": ["version", "kfm:checksum"],
      "properties": {
        "version": { "type": "string" },
        "kfm:checksum": { "type": "string" }
      }
    }
  }
}
~~~~~

---

## 🔗 Lineage Version Schema (Summary)

Formalizes version-bound lineage:

- PROV-O entity/activity/agent triples  
- Deterministic ordering  
- Immutable historical dimension  
- Checksums of lineage file itself  
- References to previous lineage versions (if applicable)

Example Outline:

~~~~~json
{
  "type": "object",
  "required": ["version", "prov", "tools", "source_ids"],
  "properties": {
    "version": { "type": "string" },
    "prov": { "type": "array" },
    "tools": { "type": "object" },
    "source_ids": { "type": "array" }
  }
}
~~~~~

---

## ⚖️ Governance Version Schema (Summary)

Captures FAIR+CARE review for each version:

- `reviewer`
- `approval_status`
- `care_impact`
- `sovereignty_notes`
- `license_verification`
- Decision timestamp

Example Outline:

~~~~~json
{
  "type": "object",
  "required": ["dataset_id", "version", "approval_status", "reviewer"],
  "properties": {
    "approval_status": {
      "type": "string",
      "enum": ["approved", "approved_with_conditions", "rejected", "escalated"]
    }
  }
}
~~~~~

---

## 🧬 Version Chain Schema (Summary)

Defines:

- Graph of versions  
- `previous_version` link  
- MAJOR/MINOR/PATCH metadata  
- Immutable chaining rules  
- CARE label inheritance logic  

Example Outline:

~~~~~json
{
  "type": "object",
  "required": ["dataset_id", "versions"],
  "properties": {
    "dataset_id": { "type": "string" },
    "versions": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["version", "previous"],
        "properties": {
          "version": { "type": "string" },
          "previous": { "type": ["string", "null"] }
        }
      }
    }
  }
}
~~~~~

---

## 📡 Telemetry Integration

All schema operations emit telemetry including:

- version changes  
- schema diffs  
- validation outcomes  
- CARE rule breakage  
- energy & CO₂ estimates  

Telemetry appended to:

~~~~~text
../../../../../../releases/v10.3.0/focus-telemetry.json
~~~~~

---

## ⚠️ Schema Change Governance

Any schema change requires:

- FAIR+CARE Council review  
- MCP-DL compliance audit  
- Updated versioning rule references  
- Regeneration of STAC/DCAT schema mappings  
- Patch/Minor/Major bump depending on impact  

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|--------|--------|---------|
| v10.3.1 | 2025-11-13 | Pipeline Architecture Team | Added full suite of versioning schemas for artifacts, STAC Items, lineage bundles, governance decisions, and version chains. |

---

<div align="center">

**Kansas Frontier Matrix — Versioning Schemas**  
Immutable Metadata × Provenance Integrity × FAIR+CARE Governance  
© 2025 Kansas Frontier Matrix — MIT License  

[Back to Versioning Architecture](../README.md)

</div>
