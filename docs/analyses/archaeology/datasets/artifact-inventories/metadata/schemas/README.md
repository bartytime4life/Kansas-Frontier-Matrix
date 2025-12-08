---
title: "📐 Kansas Frontier Matrix — Artifact Inventory Metadata Schemas (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/artifact-inventories/metadata/schemas/README.md"
description: "JSON Schema index for validating KFM v11 artifact-inventory metadata (DCAT, STAC, CARE, and provenance crosswalks)."
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Archaeology Working Group · FAIR+CARE Council · Metadata Standards Subcommittee"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_uuid: "urn:kfm:doc:archaeology-artifact-inventory-metadata-schemas-v11.2.3"
doc_kind: "Schema Index"
intent: "artifact-inventory-metadata-schemas"
semantic_document_id: "kfm-doc-archaeology-artifact-inventory-metadata-schemas-v11.2.3"
category: "Analyses · Archaeology · Metadata · Schemas"

sbom_ref: "releases/v11.2.3/sbom.spdx.json"
manifest_ref: "releases/v11.2.3/manifest.zip"
telemetry_ref: "releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "schemas/telemetry/archaeology-artifact-metadata-schemas-v1.json"
energy_schema: "schemas/telemetry/energy-v2.json"
carbon_schema: "schemas/telemetry/carbon-gco2e-v1.json"

governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.5"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

fair_category: "F1-A1-I1-R1"
care_label: "High-Sensitivity · Sovereignty-Governed"
sensitivity: "Cultural / Archaeological / Heritage"
sensitivity_level: "High"
indigenous_rights_flag: true
risk_category: "Moderate"
public_exposure_risk: "Governed"
redaction_required: true

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
classification: "Public (Governed)"
jurisdiction: "Kansas / United States"
immutability_status: "version-pinned"

header_profile: "standard"
footer_profile: "standard"

data_steward: "Archaeology Working Group · Metadata Standards Subcommittee · FAIR+CARE Council"
provenance_chain:
  - "docs/analyses/archaeology/datasets/artifact-inventories/metadata/schemas/README.md@v10.4.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true
---

<div align="center">

# 📐 **Kansas Frontier Matrix — Artifact Inventory Metadata Schemas (v11)**  

`docs/analyses/archaeology/datasets/artifact-inventories/metadata/schemas/README.md`

**Purpose**  
Define and govern the **JSON Schema standards** used to validate **metadata files** for artifact inventory datasets within the Kansas Frontier Matrix (KFM) v11.

</div>

---

## 🗂️ Directory Layout

```text
KansasFrontierMatrix/
├── 📁 docs/
│   └── 📁 analyses/
│       └── 📁 archaeology/
│           └── 📁 datasets/
│               └── 📁 artifact-inventories/
│                   └── 📁 metadata/
│                       ├── 📄 README.md                         # Metadata standard
│                       ├── 📄 flint-hills-lithics-v11.json      # DCAT + STAC + CARE + KFM metadata
│                       ├── 📄 prairie-ceramics-v11.json         # Ceramic inventory metadata
│                       ├── 📄 contact-era-metals-v11.json       # Protohistoric metals metadata (governed)
│                       ├── 📄 fauna-open-v11.json               # Faunal (public-domain oriented) metadata
│                       └── 📁 schemas/
│                           ├── 📄 README.md                     # ← This file (schema index)
│                           ├── 📄 metadata-core-schema.json     # Core metadata fields validator
│                           ├── 📄 dcat-metadata-schema.json     # DCAT 3.0 validation schema
│                           ├── 📄 care-metadata-schema.json     # CARE cultural-safety metadata validator
│                           ├── 📄 provenance-link-schema.json   # Metadata ↔ provenance linkage
│                           ├── 📄 stac-crosswalk-schema.json    # STAC–metadata alignment
│                           └── 📁 templates/                    # Schema templates for contributors
└── 📁 schemas/
    └── 📁 json/
        └── 📄 archaeology-artifact-inventory-metadata-master.schema.json   # Aggregating/master schema (optional)
```

This layout is **normative** for artifact-inventory metadata schemas in KFM v11.

---

## 📘 Overview

These schemas enforce that artifact-inventory metadata:

- Complies with **DCAT 3.0**, **STAC 1.0**, and **KFM-OP v11**.  
- Honors **FAIR+CARE** and sovereignty obligations by validating cultural-safety metadata.  
- Correctly links to **provenance logs**, **STAC Items**, and **inventory files**.  
- Is suitable for:
  - Neo4j graph ingestion,  
  - Search and discovery,  
  - Story Node and Focus Mode v3 use,  
  - Analytical reproducibility and auditing.

Every metadata file in `metadata/` MUST validate against one or more schemas from this directory as part of CI.

---

## 1️⃣ Core Metadata Schema (`metadata-core-schema.json`)

The **core metadata schema** validates the baseline structure for artifact-inventory metadata files.

### Required fields

| Field              | Description                               |
|--------------------|-------------------------------------------|
| `dct:title`        | Human-readable dataset title             |
| `dct:description`  | Summary of dataset contents              |
| `dct:license`      | SPDX ID (for example, `CC-BY-4.0`, `CC0-1.0`) |
| `kfm:phase`        | Cultural-phase classification            |
| `kfm:material_class` | Artifact material type                 |
| `kfm:source`       | Data origin institution / repository     |
| `kfm:provenance`   | Path or ID for PROV-O JSON log           |

### Optional but strongly encouraged

- `dcat:keyword`  
- Citation information (`dct:bibliographicCitation`)  
- Contact point (`dcat:contactPoint`)  

The core schema ensures all metadata records carry the minimal information required for FAIR discovery, attribution, and governance.

---

## 2️⃣ DCAT 3.0 Schema (`dcat-metadata-schema.json`)

The **DCAT metadata schema** enforces DCAT 3.0 compliance for artifact-inventory metadata.

### Required DCAT fields

| DCAT Field          | Example                                           |
|---------------------|---------------------------------------------------|
| `dct:title`         | `"Flint Hills Lithic Inventory v11"`             |
| `dct:license`       | `"CC-BY-4.0"`                                     |
| `dcat:distribution` | `"inventories/flint-hills-lithics-v11.csv"`      |
| `dct:temporal`      | `"1200–1400 CE"` or explicit interval object      |
| `dcat:keyword`      | `["lithic", "archaeology", "inventory"]`         |

### DCAT ↔ STAC Crosswalk Expectations

The schema ensures that:

| DCAT Field          | Must Align With STAC                             |
|---------------------|--------------------------------------------------|
| `dct:title`         | STAC `id` or `properties.title/description`     |
| `dcat:distribution` | STAC `assets.data.href`                         |
| `dct:temporal`      | STAC temporal properties / collection extent    |
| `dct:license`       | STAC `license` / `dct:license`                  |

Any inconsistency between DCAT and STAC is treated as a validation failure.

---

## 3️⃣ CARE Metadata Schema (`care-metadata-schema.json`)

The **CARE metadata schema** validates cultural-safety information at the metadata level.

### Required CARE fields

| Field                | Allowed Values / Notes                                      |
|----------------------|------------------------------------------------------------|
| `care:sensitivity`   | `"general"`, `"generalized"`, `"restricted-generalized"`   |
| `care:review`        | `"faircare"`, `"tribal"`, `"none-required"`                |
| `care:notes`         | Required for `generalized` or `restricted-generalized`     |
| `care:visibility_rules` | `"h3-only"`, `"no-exact-points"`                      |

Enforced rules:

- `care:sensitivity = "restricted"` is **forbidden** for metadata in this public-governed directory  
  (such datasets belong in restricted storage).  
- Entries flagged `care:review = "tribal"` require evidence of Tribal review/approval.  
- All spatial generalization and redaction steps must be documented in `care:notes`.

---

## 4️⃣ Provenance Link Schema (`provenance-link-schema.json`)

The **provenance link schema** ensures that metadata records correctly reference PROV-O lineage logs.

It checks that:

- `kfm:provenance` exists in metadata and:  
  - Matches a corresponding file in `provenance/` (same stem).  
  - Uses valid relative paths (e.g., `"provenance/flint-hills-lithics-v11.json"`).  

This schema is used to confirm cross-file consistency across:

- `metadata/<dataset>.json`,  
- `provenance/<dataset>.json`,  
- `stac/items/<dataset>.json`,  
- `inventories/<dataset>.*`.

Any mismatch is treated as a validation error.

---

## 5️⃣ STAC Crosswalk Schema (`stac-crosswalk-schema.json`)

The **STAC crosswalk schema** ensures metadata and STAC Items remain synchronized.

It verifies that:

| Metadata Field        | Must Match STAC Field                                  |
|-----------------------|--------------------------------------------------------|
| `dct:title`           | STAC `id` or `properties.title/description`           |
| `kfm:phase`           | STAC `properties.kfm:phase`                           |
| `kfm:material_class`  | STAC `properties.kfm:material_class`                  |
| `kfm:source`          | STAC `properties.kfm:source` (if present)             |
| `kfm:provenance`      | STAC `properties.kfm:provenance`                      |

Validation failure indicates drift between metadata and STAC and MUST block CI and ingestion until resolved.

---

## 🧪 Validation & CI/CD

Artifact-inventory metadata is validated using:

- `.github/workflows/metadata-validate.yml`  
- `.github/workflows/artifact-stac-validate.yml`  
- `.github/workflows/faircare-audit.yml` (for CARE-related checks)  

Validators perform:

1. JSON Schema validation against:
   - `metadata-core-schema.json`  
   - `dcat-metadata-schema.json`  
   - `care-metadata-schema.json`  
   - `provenance-link-schema.json`  
   - `stac-crosswalk-schema.json`  

2. CARE cultural review enforcement.  
3. Provenance integrity checks (paths and filename stems).  
4. DCAT 3.0 completeness and crosswalk checks.  
5. STAC alignment and ontology consistency checks.  
6. FAIR+CARE ethical compliance.

Any mismatch or violation must be repaired before data enters:

- Graph ingestion pipelines,  
- Story Node production,  
- Public-facing Focus Mode overlays.

---

## 🧠 Graph & Story Node Integration

The schemas defined here:

- Drive Neo4j label/relationship expectations for:
  - `:ArtifactInventory`, `:CulturalPhase`, `:MaterialClass`, `:CareSensitivityState`.  
- Ensure Story Nodes referencing inventories can:
  - Reliably identify phases, materials, provenance logs, and CARE flags.  
- Provide a firm foundation for:
  - Phase-based timelines,  
  - Material-culture narratives,  
  - Sensitivity-aware views in Focus Mode.

Schema evolution must be:

- Versioned in this README and in the schemas themselves,  
- Reflected in graph ingestion and Story Node mapping tools.

---

## 📝 Contributor Workflow

1. Start from a schema template in `templates/`.  
2. Extend or adjust only with:
   - Clear, documented rationale,  
   - Backwards compatibility considerations.  
3. Update this README’s table(s) and references as needed.  
4. Run local validation against example metadata.  
5. Submit PR for:
   - Archaeology Working Group,  
   - Metadata Standards Subcommittee,  
   - FAIR+CARE governance review.

No schema change is **self-approving**; all require governance sign-off.

---

## 🕰️ Version History

| Version | Date       | Author / Steward                                     | Summary                                                                 |
|--------:|------------|-------------------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3 | 2025-12-02 | Archaeology WG · Metadata Standards Subcommittee · FAIR+CARE Council | Updated schema index for KFM v11.2.3; clarified DCAT/STAC/CARE crosswalk roles and CI integration. |
| v10.4.0 | 2025-11-17 | Archaeology WG · Metadata Standards Subcommittee · FAIR+CARE Council | Added full metadata schema index, DCAT/STAC crosswalk validation, and CARE requirements. |
| v10.0.0 | 2025-11-10 | Artifact Metadata Team                                | Initial schema structure and baseline validators.                        |

---

<div align="center">

📐 **Kansas Frontier Matrix — Artifact Inventory Metadata Schemas**  

[⬅ Metadata Standard](../README.md) ·  
[🏺 Inventory Files](../../inventories/README.md) ·  
[⚖️ Root Governance](../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>
