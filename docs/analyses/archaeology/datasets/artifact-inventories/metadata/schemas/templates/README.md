---
title: "📐 Kansas Frontier Matrix — Artifact Inventory Metadata Schema Templates (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/artifact-inventories/metadata/schemas/templates/README.md"
description: "Contributor templates for JSON Schemas that validate KFM v11 artifact-inventory metadata (DCAT, STAC, CARE, and provenance crosswalks)."
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Archaeology Working Group · FAIR+CARE Council · Metadata Standards Subcommittee"
content_stability: "stable"
status: "Active / Enforced"

doc_kind: "Schema Template Guide"
header_profile: "standard"
footer_profile: "standard"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_uuid: "urn:kfm:doc:archaeology-artifact-inventory-metadata-schemas-templates-v11.2.3"
intent: "artifact-inventory-metadata-schema-templates"
semantic_document_id: "kfm-doc-archaeology-artifact-inventory-metadata-schemas-templates-v11.2.3"
category: "Analyses · Archaeology · Metadata · Schemas · Templates"

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

data_steward: "Archaeology Working Group · Metadata Standards Subcommittee · FAIR+CARE Council"
provenance_chain:
  - "docs/analyses/archaeology/datasets/artifact-inventories/metadata/schemas/templates/README.md@v10.4.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true
---

<div align="center">

# 📐 **Kansas Frontier Matrix — Artifact Inventory Metadata Schema Templates (v11)**  

`docs/analyses/archaeology/datasets/artifact-inventories/metadata/schemas/templates/README.md`

**Purpose**  
Provide **governed templates** for JSON Schemas used to validate artifact-inventory metadata (DCAT, STAC, CARE, KFM extensions), ensuring new schemas are consistent, FAIR+CARE-aligned, and CI-friendly.

</div>

---

## 🗂️ Directory Layout

```text
KansasFrontierMatrix/
└── 📁 docs/
    └── 📁 analyses/
        └── 📁 archaeology/
            └── 📁 datasets/
                └── 📁 artifact-inventories/
                    └── 📁 metadata/
                        └── 📁 schemas/
                            ├── 📄 README.md                     # Schema index (standards)
                            ├── 📄 metadata-core-schema.json      # Core metadata validator
                            ├── 📄 dcat-metadata-schema.json      # DCAT 3.0 alignment
                            ├── 📄 care-metadata-schema.json      # CARE cultural-safety metadata
                            ├── 📄 provenance-link-schema.json    # Metadata ↔ provenance linkage
                            ├── 📄 stac-crosswalk-schema.json     # STAC–metadata crosswalk
                            └── 📁 templates/
                                📄 README.md                      # ← This file (schema templates guide)
                                📄 metadata-core-template.json    # Template: core metadata schema
                                📄 dcat-metadata-template.json    # Template: DCAT schema extension
                                📄 care-metadata-template.json    # Template: CARE metadata schema
                                📄 provenance-link-template.json  # Template: provenance-link schema
                                📄 stac-crosswalk-template.json   # Template: STAC crosswalk schema
```

Schema authors MUST base new schemas on these templates, rather than free-form JSON, to preserve alignment with KFM’s ontology and governance rules.

---

## 📘 Overview

This folder contains **starting points** for JSON Schemas that:

- Validate the structure and semantics of artifact-inventory metadata files.  
- Enforce alignment between:
  - DCAT 3.0 datasets,  
  - STAC 1.0 Items,  
  - CARE cultural-safety metadata,  
  - PROV-O provenance references,  
  - KFM archaeology extension fields (`kfm:*`).  
- Ensure that metadata remains:
  - FAIR (Findable, Accessible, Interoperable, Reusable),  
  - CARE-aligned,  
  - Sovereignty-aware,  
  - Machine-extractable and graph-ready.

These templates are **not** directly used for validation; instead, they are cloned/adapted by contributors and promoted to **governed schemas** in the parent directory following governance review.

---

## 🧱 Template Types

Each template file corresponds to a governed schema in the parent `schemas/` directory.

### 1️⃣ `metadata-core-template.json`

Purpose:

- Provide the **base skeleton** for metadata schemas enforcing:
  - Core fields (`dct:title`, `dct:description`, `dct:license`, `kfm:phase`, `kfm:material_class`, `kfm:source`, `kfm:provenance`),  
  - Basic type constraints (`string`, `array`, `object`),  
  - Required keys for FAIR discoverability.

Usage:

- Clone → adjust `$id`, `title`, and `description`.  
- Add or refine `required` and `properties` as necessary for new metadata flavors.  
- Ensure any new fields are documented in the main metadata standard README.

---

### 2️⃣ `dcat-metadata-template.json`

Purpose:

- Enforce **DCAT 3.0-compliant** fields in metadata, including:
  - `dct:title`, `dct:description`, `dct:license`, `dct:creator`, `dct:temporal`, `dct:spatial`, `dcat:distribution`, `dcat:keyword`.  
- Provide a pattern for verifying DCAT constraints (arrays, URIs, controlled values).

Usage:

- Extend `metadata-core-template.json` (via `$ref` or `allOf`) for DCAT-specific requirements.  
- Add pattern checks for URLs/paths, license codes, and temporal coverage fields.

---

### 3️⃣ `care-metadata-template.json`

Purpose:

- Standardize **CARE cultural-safety metadata** across artifacts:

  - `care:sensitivity`,  
  - `care:review`,  
  - `care:notes`,  
  - `care:visibility_rules`.

Usage:

- Enforce allowed enumerations,  
- Require `care:notes` when sensitivity is `generalized` or `restricted-generalized`,  
- Support future CARE fields (e.g., `care:community`, `care:consent_reference`) with clear extensibility.

---

### 4️⃣ `provenance-link-template.json`

Purpose:

- Validate **metadata ↔ provenance links**:

  - `kfm:provenance` MUST reference an existing file path that matches naming conventions.  
  - Optional cross-check that the stem of `kfm:provenance` matches inventory and metadata stems.

Usage:

- Add relative-path patterns (`^provenance\/[a-z0-9\-]+\.json$`),  
- Optionally model relationships to STAC Items and dataset IDs as constraints.

---

### 5️⃣ `stac-crosswalk-template.json`

Purpose:

- Provide structure for **STAC–metadata crosswalk validation**:

  - Enforce consistent `id`, `kfm:phase`, `kfm:material_class`, etc. across metadata and STAC.  
  - Model references to external STAC validation or additional `$ref` schemas.

Usage:

- Template may include logical constraints (e.g., `const` or `$ref` to known enumerations),  
- Allow extension for specific inventory families (lithics, ceramics, etc.).

---

## 🧪 Validation & CI/CD Expectations

Templates themselves are:

- **Not** used for production validation,  
- Still expected to be:
  - JSON-schema valid,  
  - Lint-clean,  
  - Documented and versioned.

When a template is used to create or update a schema in `schemas/`:

1. The new/updated schema MUST be added to the parent `README.md` (schema index).  
2. CI MUST validate:
   - Schema correctness (`jsonschema` or equivalent),  
   - Compatibility with example metadata fixtures.  
3. FAIR+CARE and sovereignty impacts MUST be reviewed by:
   - Archaeology Working Group,  
   - Metadata Standards Subcommittee,  
   - FAIR+CARE Council.

---

## ⚖ FAIR+CARE & Governance

Templates represent **proposed schema patterns** and must:

- Uphold CARE constraints:
  - Do not introduce fields that could normalize unsafe patterns (e.g., precise coordinates in public metadata).  
- Respect sovereignty:
  - Ensure fields that require Tribal or community consent are clearly documented and not assumed.

Any new template:

- Must be treated as a **draft** until ratified,  
- Should be versioned and timestamped (even if not yet promoted to a “governed schema”).

---

## 🕰️ Version History

| Version | Date       | Author / Steward                                     | Summary                                                                 |
|--------:|------------|------------------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3 | 2025-12-02 | Archaeology WG · Metadata Standards Subcommittee · FAIR+CARE Council | Updated template guidance for KFM v11.2.3; aligned with new metadata and schema standards. |
| v10.4.0 | 2025-11-17 | Archaeology WG · Metadata Standards Subcommittee · FAIR+CARE Council | Initial schema template index; established contributor workflow and governance hooks. |

---

<div align="center">

📐 **Kansas Frontier Matrix — Artifact Inventory Metadata Schema Templates**  

[⬅ Metadata Schemas Index](../README.md) ·  
[📑 Metadata Standard](../README.md) ·  
[🏺 Inventory Files](../../inventories/README.md) ·  
[⚖️ Root Governance](../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>
