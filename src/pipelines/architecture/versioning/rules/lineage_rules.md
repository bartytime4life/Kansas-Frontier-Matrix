---
title: "🧬 Kansas Frontier Matrix — Lineage Rules for Versioned Pipelines (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/architecture/versioning/rules/lineage_rules.md"
version: "v10.3.1"
last_updated: "2025-11-13"
review_cycle: "Quarterly · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../../../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/pipelines-versioning-lineage-rules-v1.json"
governance_ref: "../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🧬 **Kansas Frontier Matrix — Lineage Rules for Versioned Pipelines**  
`src/pipelines/architecture/versioning/rules/lineage_rules.md`

**Purpose:**  
Define the **mandatory lineage requirements** for every versioned artifact, dataset, STAC/DCAT entry, geospatial derivative, AI output, and Story Node in the Kansas Frontier Matrix (KFM).  
Lineage rules ensure **deterministic reproducibility**, **scientific traceability**, **FAIR+CARE ethics**, and **immutable provenance** across all versions.

<img alt="Lineage" src="https://img.shields.io/badge/Lineage-Immutable-blue"/>
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Certified-orange"/>
<img alt="MCP" src="https://img.shields.io/badge/MCP_v6.3-Compliant-green"/>
<img alt="Status" src="https://img.shields.io/badge/Status-Enforced-success"/>

</div>

---

## 📘 Overview

Lineage rules govern how KFM pipelines must record:

- Input datasets, versions, and checksums  
- Toolchains and environment specifications  
- Transformations and configuration parameters  
- Governance decisions  
- CARE and sovereignty metadata  
- Derived artifacts and final outputs  
- Provenance mappings (PROV-O, CIDOC CRM)  

Lineage is the **single source of truth** for reproducibility and is *immutable per version*.

---

## 🗂️ Directory Context

~~~~~text
src/pipelines/architecture/versioning/rules/
├── README.md
├── semver_enforcement.md
├── artifact_immutability.md
├── catalog_versioning.md
├── lineage_rules.md              # This file
└── governance_requirements.md
~~~~~

---

## 🧬 Lineage Architecture (Indented Mermaid)

~~~~~mermaid
flowchart TD
  A["Pipeline Execution<br/>Transform · Validate · Publish"]
    --> B["Capture Lineage<br/>Inputs · Parameters · Tools · Governance"]
  B --> C["Construct PROV-O Graph<br/>Entities · Activities · Agents"]
  C --> D["Generate Lineage Bundle<br/>JSON · Immutable"]
  D --> E["Store Versioned Lineage<br/>data/lineage/{dataset}/{version}/"]
  E --> F["Replay Engine<br/>Determinism Checks"]
~~~~~

---

## 🧱 Required Lineage Fields

Each lineage bundle MUST contain the following:

### 1. **Version Metadata**
- `dataset_id`
- `version` (SemVer strict)
- `care_label`
- `governance_ref`
- `timestamp`

### 2. **Input Sources**
- `source_ids`
- `source_versions`
- `source_checksums`
- `source_uris`

### 3. **Processing Environment**
- Python version  
- GDAL version  
- spaCy version  
- AI model versions (Focus Mode, embeddings, classifiers)  
- OS/environment hashes (optional but recommended)

### 4. **Transform Parameters**
- Reprojection profiles  
- Normalization settings  
- Filter windows  
- OCR/NLP model arguments  
- Raster kernel settings  
- Masking rules (if sensitive)

### 5. **Output Metadata**
- Output checksum  
- Output artifact URI  
- Output data types  
- Output STAC Item reference  
- Output DCAT metadata reference  

### 6. **Governance Annotations**
- care_label  
- sovereignty metadata (if applicable)  
- license information  
- consent records  
- masking strategy used  

### 7. **PROV-O / CIDOC CRM Graph**
- `prov:Entity` (inputs/outputs)  
- `prov:Activity` (pipeline stages)  
- `prov:Agent` (software/actors)  
- `prov:wasGeneratedBy`  
- `prov:used`  
- CIDOC entities for historical/archival data if relevant  

---

## 📦 Lineage File Location

All lineage files MUST be stored at:

~~~~~text
data/lineage/{dataset_id}/{version}/lineage.json
~~~~~

This path is immutable.

---

## 🔐 Immutable Lineage Rules

Lineage files MUST be:

- **Immutable after publication**  
- Never edited, overwritten, truncated, or regenerated  
- Only *supplemented* via governance addendum files (rare, approved)  

Historical lineage MUST remain intact **forever**.

---

## ♻️ Lineage in Version Chains

Each lineage file must reference its predecessor:

~~~~~json
{
  "version": "v10.3.1",
  "previous_version": "v10.3.0"
}
~~~~~

If no predecessor (initial version), use:

~~~~~json
"previous_version": null
~~~~~

---

## 🔍 Lineage Validation Requirements

Lineage files must pass:

- JSON Schema validation (`lineage_version.schema.json`)  
- Checksum validation (sha256-only)  
- STAC/DCAT metadata linkage validation  
- FAIR+CARE compliance checks  
- Provenance completeness checks  

Validation is run by:

- `schema_check.py`
- `faircare_validator.py`
- `checksum_audit.py`
- `ai_explainability_audit.py` (for AI-derived outputs)

---

## 📡 Telemetry Requirements

Every lineage publication must produce telemetry containing:

- `dataset_id`
- `version`
- `lineage_checksum`
- `care_label`
- `governance_result`
- `runtime_sec`
- `energy_wh`
- `co2_g`
- `validation_passed`

Stored at:

~~~~~text
../../../../../../../releases/v10.3.0/focus-telemetry.json
~~~~~

---

## ⚖️ Forbidden Lineage Violations

❌ Changing lineage after publication  
❌ Missing input checksums  
❌ Missing output checksum  
❌ Unspecified tool versions  
❌ Missing CARE metadata  
❌ Publishing version without lineage file  
❌ Using outdated or broken PROV-O structures  
❌ Publishing lineage that does not match actual outputs  
❌ Publishing lineage referencing unpublished or nonexistent datasets  

Any violation results in **Critical CI Failure**.

---

## 🧪 Lineage Example (Abbreviated)

~~~~~json
{
  "dataset_id": "hydrology_flow_ks",
  "version": "v10.3.1",
  "previous_version": "v10.3.0",
  "care_label": "public",
  "provenance": {
    "source_ids": ["noaa_station_ks", "usgs_streamflow_ks"],
    "source_checksums": [
      "sha256:aaaa...",
      "sha256:bbbb..."
    ]
  },
  "tools": {
    "python": "3.11.5",
    "gdal": "3.12.0",
    "spaCy": "3.7.3"
  },
  "output_checksum": "sha256:9393aa331...",
  "stac_item_ref": "data/stac/hydrology_flow_ks_v10.3.1.json",
  "governance_ref": "docs/reports/audit/versioning_ledger.json"
}
~~~~~

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|--------|--------|---------|
| v10.3.1 | 2025-11-13 | Pipeline Architecture Team | Established full lineage requirements for all versioned artifacts, mapping PROV-O, CARE, and immutable metadata. |

---

<div align="center">

**Kansas Frontier Matrix — Lineage Version Rules**  
Deterministic Provenance × Immutable History × FAIR+CARE Ethics  
© 2025 Kansas Frontier Matrix — MIT License  

[Back to Versioning Rules](../README.md)

</div>
