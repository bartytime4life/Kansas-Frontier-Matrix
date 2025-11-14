---
title: "⚖️ Kansas Frontier Matrix — Governance Requirements for Versioning (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/architecture/versioning/rules/governance_requirements.md"
version: "v10.3.1"
last_updated: "2025-11-13"
review_cycle: "Quarterly · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../../../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/pipelines-versioning-governance-v1.json"
governance_ref: "../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# ⚖️ **Kansas Frontier Matrix — Governance Requirements for Versioning**  
`src/pipelines/architecture/versioning/rules/governance_requirements.md`

**Purpose:**  
Define the **mandatory governance requirements** that every versioned artifact, dataset, lineage record, STAC/DCAT item, AI model, and Story Node must meet before publication in the Kansas Frontier Matrix (KFM).  
These rules enforce **FAIR+CARE sovereignty**, **ethical transparency**, **licensing integrity**, **immutability**, and **SLSA-grade provenance**.

<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Certified-orange"/>
<img alt="Docs" src="https://img.shields.io/badge/Docs-MCP_v6.3-blue"/>
<img alt="Governance" src="https://img.shields.io/badge/Governance-Active-success"/>
<img alt="License" src="https://img.shields.io/badge/License-MIT-green"/>

</div>

---

## 📘 Overview

Every version in KFM—whether it is a dataset, geospatial derivative, graph export, lineage record, metadata block, or AI/Focus Mode output—must pass a **governance review gate**.

Governance requirements cover:

- CARE ethics  
- Indigenous Data Sovereignty  
- Licensing & attribution  
- Masking rules  
- Provenance completeness  
- STAC/DCAT consistency  
- Immutable versioning  
- Long-term reproducibility  

Version publication **cannot proceed** unless all rules in this document are satisfied.

---

## 🗂️ Directory Context

~~~~~text
src/pipelines/architecture/versioning/rules/
├── README.md
├── semver_enforcement.md
├── artifact_immutability.md
├── catalog_versioning.md
├── lineage_rules.md
└── governance_requirements.md      # This file
~~~~~

---

## 🧩 Governance Review Architecture

~~~~~mermaid
flowchart TD
  A["Version Candidate<br/>vX.Y.Z"] --> B["Governance Evaluation<br/>CARE · Licensing · Sovereignty"]
  B --> C{"Compliant?"}
  C -->|No| D["Reject Version<br/>Log to Governance Ledger"]
  C -->|Yes| E["Approve Version<br/>Publish Artifact + Metadata"]
  E --> F["Archive<br/>Immutable, Append-Only"]
  F --> G["Replay-Compatible<br/>Deterministic Lineage"]
~~~~~

---

## 🧠 CARE Requirements (Mandatory)

All versions must include:

### Required Fields
- `care_label`  
  - `public`  
  - `sensitive`  
  - `restricted`  

- `sovereignty` object for any Indigenous or tribal source data:
  - `tribal_authority`  
  - `review_status` (`required`, `approved`, `exempt`)  
  - `masking` strategy (`h3_r7`, `fuzz_500m`, `bbox_generalization`)  

### Governance Flags

| care_label | Required Action |
|------------|------------------|
| **public** | Standard governance review |
| **sensitive** | CARE consent validation; masking review |
| **restricted** | Tribal approval **mandatory** before publication |

If sovereignty metadata is missing for datasets that require it → **version rejected**.

---

## 📜 Licensing Requirements (SPDX)

All versions must specify:

- SPDX-compatible license  
- Source attribution  
- License inheritance across versions  
- Third-party asset license review  

### Forbidden Licenses  
- Closed, proprietary, or restrictive licenses  
- Non-redistributable datasets  
- Licenses incompatible with CC-BY or MIT publication requirements  

License violations → **critical governance block**.

---

## 🔐 Masking & Redaction Requirements

Geospatial & cultural data must follow:

### For **archaeology** or **heritage** layers:
- Mask exact coordinates → H3 resolution ≥ r7  
- Provide generalized bounding polygons  
- Do not publish precise locations without tribal authorization  

### For **historical sensitive events** (e.g., violence, trauma):
- Apply temporal blurring if required  
- Review narrative framing in Story Nodes  

Masking failures → **critical alert** and version rejection.

---

## 🔗 Provenance Requirements (PROV-O / CIDOC CRM)

Every version MUST include:

- Full lineage JSON in:
  
~~~~~text
data/lineage/{dataset_id}/{version}/lineage.json
~~~~~

- Checksums for:
  - Inputs  
  - Outputs  
  - Tools (Python, GDAL, transformer, spaCy, etc.)  
- Canonical `source_ids`  
- PROV-O relations (`wasGeneratedBy`, `used`, `wasDerivedFrom`)  

If lineage is missing or incomplete → version invalid.

---

## 📦 Metadata Requirements (STAC/DCAT)

### STAC

Versioned STAC Items MUST include:

- `properties.version`  
- `kfm:checksum`  
- `kfm:provenance`  
- `kfm:care_label`  
- `links[rel="version"]`  
- Immutable asset references  

### DCAT

DCAT entries MUST:

- Match the STAC version  
- Use stable `dct:identifier`  
- Preserve history across versions  

Metadata mismatch → version rejected.

---

## 🧬 Replay & Deterministic Reprocessing

Versioned artifacts MUST support:

- Full replay by the replay engine  
- Deterministic checksum matching  
- Divergence detection  

If replay output differs from stored version:

- Version flagged  
- Governance-led investigation required  
- Version may be deprecated  

---

## 📡 Telemetry Requirements

Every version MUST emit telemetry including:

- `dataset_id`  
- `new_version`  
- `old_version` (if applicable)  
- `break_type` (major/minor/patch)  
- `checksum`  
- `care_label`  
- Energy (Wh)  
- CO₂e (g)  
- Validation pass/fail  

Telemetry appended to:

~~~~~text
../../../../../../../releases/v10.3.0/focus-telemetry.json
~~~~~

---

## 🧾 Governance Decision Record (Required)

Each version MUST produce a governance decision entry:

~~~~~json
{
  "governance_decision_id": "gov_version_approval_2025_11_13_hydro_4",
  "dataset_id": "hydrology_flow_ks",
  "version": "v10.3.1",
  "reviewer": "FAIR+CARE Council",
  "approval_status": "approved",
  "care_impact": "none",
  "sovereignty_notes": null,
  "timestamp": "2025-11-13T20:44:00Z"
}
~~~~~

Stored in:

~~~~~text
docs/reports/audit/versioning_ledger.json
~~~~~

---

## 🚫 Forbidden Governance Violations

- Publishing new version **without** CARE label  
- Missing sovereignty metadata for tribal datasets  
- Masking not applied where required  
- Publishing STAC/DCAT metadata with mismatched version  
- Overwriting historical versions  
- Publishing a version without checksum  
- Failing to register governance decision  

Any violation triggers **Critical CI Failure**.

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|--------|--------|---------|
| v10.3.1 | 2025-11-13 | FAIR+CARE Council · Pipeline Architecture Team | Established required governance contracts for all versioned artifacts, metadata, lineage, and STAC/DCAT items. |

---

<div align="center">

**Kansas Frontier Matrix — Governance for Versioning**  
Ethical Data · Immutable History · Sovereignty-Respecting Versioning  
© 2025 Kansas Frontier Matrix — MIT License  

[Back to Versioning Rules](../README.md)

</div>
