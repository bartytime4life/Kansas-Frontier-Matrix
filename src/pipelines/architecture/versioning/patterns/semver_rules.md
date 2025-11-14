---
title: "🔢 Kansas Frontier Matrix — Semantic Versioning Pattern Rules (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/architecture/versioning/patterns/semver_rules.md"
version: "v10.3.1"
last_updated: "2025-11-13"
review_cycle: "Quarterly · Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../../../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/pipelines-versioning-semver-patterns-v1.json"
governance_ref: "../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🔢 **Kansas Frontier Matrix — Semantic Versioning Pattern Rules**  
`src/pipelines/architecture/versioning/patterns/semver_rules.md`

**Purpose:**  
Define the **practical, pattern-oriented SemVer rules** that all KFM pipelines, datasets, models, STAC/DCAT artifacts, lineage bundles, and Story Nodes must follow.  
These patterns operationalize the **SemVer enforcement spec** into concrete usage for **ETL**, **geospatial**, **AI**, **metadata**, and **governance** workflows.

<img alt="SemVer" src="https://img.shields.io/badge/SemVer-Patterns-blue"/>
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Certified-orange"/>
<img alt="Status" src="https://img.shields.io/badge/Status-Active-success"/>
<img alt="License" src="https://img.shields.io/badge/License-MIT-green"/>

</div>

---

## 📘 Overview

This file turns the **SemVer enforcement rules** into **concrete patterns** for:

- When to bump **MAJOR / MINOR / PATCH**  
- How to version **pipelines vs datasets vs models**  
- How version changes propagate into **STAC/DCAT**  
- How to reflect version changes in **lineage** and **governance**  
- How to avoid **SemVer anti-patterns** that break reproducibility  

All KFM versioned assets MUST follow:

~~~~~text
MAJOR.MINOR.PATCH  →  e.g. v10.3.1
~~~~~

---

## 🗂️ Directory Context

~~~~~text
src/pipelines/architecture/versioning/patterns/
├── README.md
├── artifact_lifecycle.md
├── semver_rules.md                 # This file
├── stac_dcat_alignment.md
├── lineage_version_links.md
└── governance_version_contract.md
~~~~~

---

## 🧩 SemVer Pattern Matrix

| Change Type | Version Bump | Typical Examples |
|-------------|-------------|------------------|
| **MAJOR**   | X.0.0       | Breaking schema changes, new ontology model, masking rule overhaul |
| **MINOR**   | X.Y.0       | Adding new fields, adding new layers, adding non-breaking features |
| **PATCH**   | X.Y.Z       | Fixing metadata typos, updating non-functional details, doc-only corrections |

---

## 1️⃣ MAJOR Version Patterns

### When to bump MAJOR (X.0.0)

Use **MAJOR** when:

- Schema changes are **breaking**:
  - Removing or renaming fields
  - Changing field types or semantics
- Geospatial representation changes:
  - New CRS that breaks downstream assumptions
  - Switching coordinate systems from local to global
- CARE & governance rule changes:
  - Revised masking rules (e.g., H3 r7 → r6)
  - New sovereignty constraints that alter what is visible
- Ontology or graph breakage:
  - New CIDOC classes replacing old ones
  - Neo4j schema migrations that change relationships

**Pattern:**

~~~~~text
v9.7.0 → v10.0.0
~~~~~

This implies **downstream re-validation** and **governance re-review**.

---

## 2️⃣ MINOR Version Patterns

### When to bump MINOR (X.Y.0)

Use **MINOR** when changes are:

- Backward-compatible
- Additive or optional

Examples:

- Adding new STAC properties (without removing existing)
- Adding new map layers (e.g., new hazard or climate product)
- Adding explainability fields to AI output (without changing structure)
- Adding optional lineage metadata fields

**Pattern:**

~~~~~text
v10.2.0 → v10.3.0
~~~~~

Downstream consumers continue to work but may **optionally adopt** new fields.

---

## 3️⃣ PATCH Version Patterns

### When to bump PATCH (X.Y.Z)

Use **PATCH** when changes are:

- Non-breaking
- Corrective
- Do **not** change the core artifact content

Examples:

- Correcting typos in metadata
- Fixing STAC/DCAT URLs that were wrong but point to the same artifact
- Updating documentation-only fields
- Adjusting lineage annotations that do **not** change provenance facts

**Pattern:**

~~~~~text
v10.3.0 → v10.3.1
~~~~~

If the actual data content changes → **NOT** patch; use MINOR or MAJOR.

---

## 4️⃣ SemVer Patterns Across Asset Types

### Pipelines

Version pattern for pipelines:

~~~~~text
etl_hydrology_flow_v10.3.1
~~~~~

- Bump MAJOR when transformation logic breaks schema
- Bump MINOR when adding non-breaking transformations
- Bump PATCH for internal refactors with identical outputs

### Datasets / Artifacts

Stored under:

~~~~~text
s3://kfm/artifacts/{dataset_id}/{version}/
~~~~~

Example:

~~~~~text
hydrology_flow_ks / v10.3.1 / output.parquet
~~~~~

### AI Models

~~~~~text
focus-transformer-v2.4.1
~~~~~

- MAJOR: architecture change
- MINOR: new training regime or dataset
- PATCH: training bugfix with same general behavior and schema

---

## 5️⃣ STAC/DCAT SemVer Alignment Pattern

For a dataset:

~~~~~text
dataset_id = hydrology_flow_ks
version    = v10.3.1
~~~~~

STAC Item ID:

~~~~~text
hydrology_flow_ks_v10.3.1.json
~~~~~

STAC properties:

~~~~~json
{
  "properties": {
    "version": "v10.3.1",
    "kfm:checksum": "sha256:...",
    "kfm:care_label": "public"
  }
}
~~~~~

DCAT Dataset must match:

- Same `version`
- Same `checksum` (where recorded)
- Same `care_label` (via metadata mapping)

---

## 6️⃣ Lineage & SemVer Pattern

Lineage path:

~~~~~text
data/lineage/{dataset_id}/{version}/lineage.json
~~~~~

Example:

~~~~~text
data/lineage/hydrology_flow_ks/v10.3.1/lineage.json
~~~~~

Each lineage JSON MUST include:

~~~~~json
{
  "dataset_id": "hydrology_flow_ks",
  "version": "v10.3.1",
  "previous_version": "v10.3.0"
}
~~~~~

This forms an immutable **version chain** used by:

- Replay engine
- Governance Council
- Focus Mode historical reasoning
- Analyses and audits

---

## 7️⃣ Governance & SemVer Pattern

MAJOR changes **must** include:

- Governance contract update  
- CARE reassessment  
- Sovereignty review (if applicable)  

Minor/Patch changes must still pass:

- License review  
- Basic CARE review  

All governance decisions stored in:

~~~~~text
docs/reports/audit/versioning_ledger.json
~~~~~

---

## 8️⃣ Telemetry + SemVer Integration

Each new version MUST emit telemetry:

- `dataset_id`
- `old_version` (optional)
- `new_version`
- `break_type` (`major`, `minor`, `patch`)
- `checksum`
- `care_label`
- `validation_passed`
- `energy_wh`, `co2_g`

Telemetry path:

~~~~~text
../../../../../../../releases/v10.3.0/focus-telemetry.json
~~~~~

This enables longitudinal analysis of:

- Cost of changes
- FAIR+CARE drift
- Energy/CO₂ by version

---

## 🚫 SemVer Anti-Patterns (Forbidden)

- ❌ Using dates or integers only (e.g., `20251113`, `v5`)  
- ❌ Reusing old version tags with new content  
- ❌ Skipping version increments when schema changes  
- ❌ Publishing without linking lineage & STAC/DCAT  
- ❌ Assigning MAJOR/MINOR/PATCH arbitrarily without justification  

Such behavior breaks:

- Reproducibility  
- Governance traceability  
- FAIR+CARE audits  

And MUST be treated as a **Critical CI violation**.

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|--------|--------|---------|
| v10.3.1 | 2025-11-13 | Pipeline Architecture Team | Defined pattern-level SemVer guidance for pipelines, datasets, AI models, STAC/DCAT, and lineage. |

---

<div align="center">

**Kansas Frontier Matrix — SemVer Pattern Rules**  
Consistent Evolution × Immutable History × FAIR+CARE Governance  
© 2025 Kansas Frontier Matrix — MIT License  

[Back to Versioning Patterns](../README.md)

</div>
