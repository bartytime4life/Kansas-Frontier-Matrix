---
title: "📏 Kansas Frontier Matrix — Versioning Rules & Compliance Specification (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/architecture/versioning/rules/README.md"
version: "v10.3.1"
last_updated: "2025-11-13"
review_cycle: "Quarterly · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/pipelines-versioning-rules-v1.json"
governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 📏 **Kansas Frontier Matrix — Versioning Rules & Compliance Specification**  
`src/pipelines/architecture/versioning/rules/README.md`

**Purpose:**  
Define the **enforceable versioning rules** for all datasets, pipelines, metadata structures, lineage files, STAC/DCAT artifacts, AI outputs, Story Nodes, and governance documents within the Kansas Frontier Matrix (KFM).  
These rules ensure **immutability**, **scientific reproducibility**, **FAIR+CARE governance alignment**, and **MCP-DL v6.3 documentation discipline**.

<img alt="Docs" src="https://img.shields.io/badge/Docs-MCP_v6.3-blue"/>
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Certified-orange"/>
<img alt="License" src="https://img.shields.io/badge/License-MIT-green"/>
<img alt="Status" src="https://img.shields.io/badge/Status-Rules_enforced-success"/>

</div>

---

## 📘 Overview

Versioning rules apply to:

- ETL outputs  
- Geospatial derivatives (COG, GeoParquet, NetCDF)  
- Metadata (STAC Items, DCAT Datasets, lineage JSONs)  
- Graph entities  
- AI/Focus Mode outputs  
- Story Nodes  
- Governance decisions and audit logs  

These rules guarantee that **every versioned asset is immutable, auditable, comparable, and FAIR+CARE-aligned** for all time.

---

## 📁 Directory Layout

~~~~~text
src/pipelines/architecture/versioning/rules/
├── README.md                         # This file
├── semver_enforcement.md             # Parsing & enforcement logic
├── artifact_immutability.md          # Immutability requirements
├── catalog_versioning.md             # STAC/DCAT version rules
├── lineage_rules.md                  # Version→lineage stability contracts
└── governance_requirements.md        # Governance rules for each version tier
~~~~~

---

## 🧩 Versioning Rule Framework (Indented Mermaid)

~~~~~mermaid
flowchart TD
  A["Semantic Version Input<br/>vX.Y.Z"] --> B["Rule Engine<br/>SemVer Parsing & Gates"]
  B --> C["Artifact Rules<br/>Immutable · Checksum-bound"]
  C --> D["Metadata Rules<br/>STAC/DCAT Alignment"]
  D --> E["Lineage Rules<br/>PROV-O Stability · Deterministic Chains"]
  E --> F["Governance Rules<br/>CARE · Sovereignty · Licensing"]
  F --> G["Publication Gate<br/>Release · Catalog · Archive"]
~~~~~

---

## 🔢 1. Semantic Versioning Enforcement (SemVer Strict Mode)

KFM uses strict **SemVer**:

~~~~~text
MAJOR.MINOR.PATCH
~~~~~

### Rules

| Component | Trigger Conditions | Notes |
|----------|--------------------|-------|
| **MAJOR** | Breaking schema changes, ontology shifts, ethical/policy transforms | Requires FAIR+CARE Council review |
| **MINOR** | Backward-compatible additions | No breaking field removals allowed |
| **PATCH** | Fixes, cleanup, metadata correction | Must not change computed artifacts |

### Forbidden SemVer Anti-Patterns

- ❌ Using dates or timestamps as versions  
- ❌ Using incremental counters with no meaning  
- ❌ Publishing `v1.0.0` without lineage  

---

## 📦 2. Artifact Immutability Rules

Every artifact stored at:

~~~~~text
s3://kfm/artifacts/{dataset_id}/{version}/
~~~~~

MUST follow:

- **Immutable after publication**  
- **Checksum required (sha256 only)**  
- **Artifact content must NEVER change per version**  
- **Reprocessing requires new version**  

### Immutability Violations (Immediate Block)

- Changing data inside an existing version folder  
- Publishing new files under an old version  
- Modifying metadata for a version after release  

---

## 🗂️ 3. Metadata Versioning Rules (STAC/DCAT)

STAC Items MUST include:

- `properties.version`  
- `properties.kfm:checksum`  
- `properties.kfm:provenance`  
- Version graph via `links[rel="version"]`  

DCAT Datasets MUST:

- Reflect same version history  
- Contain stable `dct:identifier`  
- Map 1:1 with STAC Collections  

---

## 🔗 4. Lineage Stability Rules (PROV-O / CIDOC)

Lineage files:

~~~~~text
data/lineage/{dataset_id}/{version}/lineage.json
~~~~~

MUST satisfy:

- Deterministic ordering  
- Stable PROV-O chain  
- Explicit tool versions (Python, GDAL, spaCy, AI model versions)  
- Immutable after publication  
- Must match artifact content & checksum  

### Lineage Violations

- Missing source references  
- Missing checksum entries  
- Modified lineage after version release  

---

## ⚖️ 5. Governance Version Rules (FAIR+CARE)

Every version MUST undergo governance review.

Governance review requires:

- CARE label (`public`, `sensitive`, `restricted`)  
- Sovereignty metadata (if applicable)  
- License verification (SPDX)  
- Masking rule enforcement for sensitive data  
- Ethical impact screening for AI-derived outputs  

Governance decisions stored in:

~~~~~text
docs/reports/audit/versioning_ledger.json
~~~~~

No version may be published without governance sign-off for sensitive data.

---

## 📡 6. Telemetry Versioning Rules

All version changes MUST produce a telemetry entry:

Fields required:

- `dataset_id`  
- `old_version` (if applicable)  
- `new_version`  
- `break_type` (major/minor/patch)  
- `checksum`  
- `care_label`  
- `energy_wh`, `co2_g`  
- `validation_passed`  

Stored at:

~~~~~text
../../../../../../releases/v10.3.0/focus-telemetry.json
~~~~~

---

## 📜 7. Version Lifecycle Phases

### 🧪 Phase 1 — Pre-Release

- Validation tests  
- Lineage generation  
- PROV-O consistency checks  
- STAC/DCAT schema tests  
- Governance pre-review  

### 🚀 Phase 2 — Release

- Artifact publication  
- Lineage persisted  
- STAC/DCAT item published  
- Telemetry exported  
- Governance ledger updated  

### 🗄️ Phase 3 — Archive

- Immutable archival storage  
- Multi-version comparison available  
- Replay-ready lineage context persisted  

---

## 🚫 Forbidden Versioning Behaviors (Violations Cause CI Failure)

- Overwriting artifacts for existing versions  
- Publishing versions with missing lineage  
- Reusing version tags for different content  
- Publishing geospatial assets without checksum  
- Bypassing governance approval for restricted datasets  
- Auto-incrementing versions without proper justification  
- Omitting version graph links in STAC Items  

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|--------|--------|---------|
| v10.3.1 | 2025-11-13 | Pipeline Architecture Team | Added full, enforceable versioning rules for artifacts, metadata, lineage, governance, and telemetry. |

---

<div align="center">

**Kansas Frontier Matrix — Versioning Rules Specification**  
Immutable History × FAIR+CARE × Scientific Reproducibility  
© 2025 Kansas Frontier Matrix — MIT License  

[Back to Versioning Architecture](../README.md)

</div>
