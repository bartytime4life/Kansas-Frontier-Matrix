---
title: "🔢 Kansas Frontier Matrix — Semantic Versioning Enforcement Rules (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/architecture/versioning/rules/semver_enforcement.md"
version: "v10.3.1"
last_updated: "2025-11-13"
review_cycle: "Quarterly · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../../../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/pipelines-versioning-semver-v1.json"
governance_ref: "../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🔢 **Kansas Frontier Matrix — Semantic Versioning Enforcement Rules**  
`src/pipelines/architecture/versioning/rules/semver_enforcement.md`

**Purpose:**  
Define the **strict semantic versioning (SemVer) rules** that all pipelines, datasets, geospatial derivatives, lineage bundles, STAC/DCAT assets, Story Nodes, and AI models must follow in the Kansas Frontier Matrix (KFM).  
These rules ensure **consistent evolution**, **immutable historical records**, **FAIR+CARE governance**, and **MCP-DL v6.3 documentation discipline**.

<img alt="SemVer" src="https://img.shields.io/badge/SemVer-Strict-blue"/>
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Certified-orange"/>
<img alt="Status" src="https://img.shields.io/badge/Status-Enforced-success"/>

</div>

---

## 📘 Overview

All KFM versioned entities must use **strict semantic versioning:**

~~~~~text
MAJOR.MINOR.PATCH
~~~~~

Semantic versioning governs:

- ETL outputs  
- Geospatial derivatives (COG, GeoParquet, NetCDF)  
- AI/Focus Mode outputs  
- STAC/DCAT metadata  
- Lineage bundles  
- Governance decision records  
- Story Nodes & narrative metadata  

No entity may be published without **SemVer-compliant versioning**.

---

## 🗂️ Directory Context

~~~~~text
src/pipelines/architecture/versioning/rules/
├── README.md
├── semver_enforcement.md          # This file
├── artifact_immutability.md
├── catalog_versioning.md
├── lineage_rules.md
└── governance_requirements.md
~~~~~

---

## 🔢 SemVer Rule Definitions

### ✔ MAJOR (X.0.0)

Triggered by **breaking changes**:

| Category | Breaking Example |
|----------|------------------|
| Schema | Removing or renaming fields; changing data types |
| Geography | Changing projection, CRS, or coordinate structure |
| Ethics | Changing CARE masking rules or sovereignty structures |
| Ontology | Updating CIDOC CRM/PROV-O mappings incompatibly |
| AI Models | Changing model architecture that alters output semantics |

MAJOR changes require:

- FAIR+CARE Council approval  
- Governance ledger entry  
- Version chain update (previous → next)  
- Replay validation against prior version  

---

### ✔ MINOR (X.Y.0)

Triggered by **backward-compatible additions**, including:

| Category | Additive Example |
|----------|------------------|
| Fields | Adding metadata fields to STAC/DCAT Without removing existing |
| Layers | Adding new geospatial layers |
| AI | Optional new columns, new explainability fields |
| Lineage | Additional provenance annotations |

MINOR updates must:

- Preserve backward compatibility  
- Maintain checksum stability for unchanged assets  
- Pass full validation  

---

### ✔ PATCH (X.Y.Z)

Triggered by **non-breaking fixes**, such as:

| Category | Patch Example |
|----------|--------------|
| Metadata | Fixing typos or missing optional metadata |
| Processing | Correcting minor calculation errors |
| Schema | Non-breaking rule relaxations |
| Pipeline | Updating dependencies without altering outputs |

PATCH versions **must not** change artifact content.  
If content changes, MINOR or MAJOR is required.

---

## 🧩 SemVer Enforcement Logic

### Required pattern:

~~~~~text
^v\d+\.\d+\.\d+$
~~~~~

### Required checks:

- Version MUST appear in:
  - Artifact paths  
  - STAC `properties.version`  
  - DCAT `dct:hasVersion`  
  - Lineage JSON  
  - Telemetry entries  
  - Governance decisions  

- Version MUST be consistent across:
  - STAC/DCAT  
  - Lineage bundle  
  - Outbox events  
  - State store records  

Mismatch → **Critical CI Failure**.

---

## 🧠 SemVer Decision Matrix

| Change Type | Version Required | Example |
|------------|------------------|---------|
| Breaking schema change | MAJOR | New CRS; field removal |
| Backward-compatible addition | MINOR | New dataset field |
| Fix with identical output | PATCH | Metadata correction |
| CARE masking rule change | MAJOR | New sovereignty logic |
| New predictive layer | MINOR | Climate scenario raster |
| Re-running with identical output | No new version | Replay-only |

---

## 🧬 SemVer in Version Chains

Each version chain must be stored in lineage:

~~~~~json
{
  "version": "v10.3.1",
  "previous_version": "v10.3.0",
  "break_type": "patch"
}
~~~~~

If no earlier version:

~~~~~json
"previous_version": null
~~~~~

---

## 📡 Telemetry Requirements

Every version update must log:

- `dataset_id`  
- `old_version` (optional)  
- `new_version`  
- `break_type` (`major`, `minor`, `patch`)  
- `checksum`  
- `care_label`  
- `validation_passed`  
- `energy_wh`, `co2_g`  
- Governance decision result  

Telemetry appended to:

~~~~~text
../../../../../../../releases/v10.3.0/focus-telemetry.json
~~~~~

---

## ⚖️ Governance Requirements for SemVer

- All **MAJOR** changes require governance approval  
- All **MINOR** changes require ethical screening  
- All **PATCH** changes require lineage checksum confirmation  
- All version increments MUST be logged in:

~~~~~text
docs/reports/audit/versioning_ledger.json
~~~~~

---

## 🚫 Forbidden Behaviors

❌ No editing artifacts after publication  
❌ No reusing version tags  
❌ No skipping required version increments  
❌ No publishing version without lineage  
❌ No version without governance review for sensitive datasets  
❌ No semantic drift across STAC/DCAT/lineage  

All violations → **Critical CI Failure**.

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|--------|--------|---------|
| v10.3.1 | 2025-11-13 | Pipeline Architecture Team | Established strict SemVer rules for versioned assets, lineage, STAC/DCAT, and governance. |

---

<div align="center">

**Kansas Frontier Matrix — Semantic Versioning Enforcement**  
Immutable Versions × Ethical Stewardship × Total Reproducibility  
© 2025 Kansas Frontier Matrix — MIT License  

[Back to Versioning Rules](../README.md)

</div>
