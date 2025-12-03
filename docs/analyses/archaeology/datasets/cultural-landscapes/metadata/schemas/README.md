---
title: "📐 Kansas Frontier Matrix — Cultural Landscape Metadata Schemas (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/metadata/schemas/README.md"
description: "JSON Schema set for validating KFM v11 cultural-landscape metadata (DCAT + KFM + CARE + provenance crosswalks)."
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Cultural Landscape Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_uuid: "urn:kfm:doc:cultural-landscape-metadata-schemas-v11.2.3"
doc_kind: "Schema Documentation"
intent: "cultural-landscape-metadata-schemas"
semantic_document_id: "kfm-doc-archaeology-cultural-landscapes-metadata-schemas-v11.2.3"
category: "Analyses · Archaeology · Cultural Landscapes · Metadata · Schemas"

sbom_ref: "../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/archaeology-cultural-landscapes-metadata-schemas-v1.json"
energy_schema: "../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../schemas/telemetry/carbon-gco2e-v1.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
sensitivity: "Cultural / Historical / Archaeological"
sensitivity_level: "Medium"
indigenous_rights_flag: true
risk_category: "Moderate"
public_exposure_risk: "Governed"
redaction_required: true

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
classification: "Public (Governed)"
jurisdiction: "Kansas / United States"
immutability_status: "mutable-plan"

header_profile: "standard"
footer_profile: "standard"

data_steward: "Cultural Landscape Working Group · FAIR+CARE Council"
provenance_chain:
  - "docs/analyses/archaeology/datasets/cultural-landscapes/metadata/schemas/README.md@v10.4.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true
---

# 📐 Cultural Landscape Metadata Schemas (v11)

`docs/analyses/archaeology/datasets/cultural-landscapes/metadata/schemas/README.md`

**Purpose**  
Define and govern the **JSON Schema set** used to validate **cultural-landscape metadata JSON** in KFM v11.

These schemas ensure that metadata for:

- Regions and cultural areas  
- Interaction spheres  
- Mobility routes and trails  
- Resource procurement zones  
- Environmental–cultural synthesis layers  

is:

- DCAT 3.0 compliant.  
- Enriched with KFM cultural-landscape extensions (`kfm:*`).  
- CARE-governed (`care:*`).  
- Properly linked to PROV-O provenance and STAC Items/Collections.  

Schemas here are used by CI and tooling to guarantee that all cultural-landscape metadata under:

- `docs/analyses/archaeology/datasets/cultural-landscapes/metadata/`

meets KFM v11 standards.

---

## 📘 Overview

This directory contains:

- **Core metadata validation schemas** for cultural landscapes.  
- **DCAT alignment schemas** for catalog interoperability.  
- **CARE sensitivity schemas** for cultural-safety checks.  
- **Provenance link schemas** for metadata → PROV-O consistency.  
- **STAC crosswalk schemas** for metadata ↔ STAC alignment.

All schemas follow **JSON Schema Draft 2020-12** and are designed to integrate with global KFM validation flows.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/metadata/schemas/
├── 📄 README.md                         # This file
├── 📄 metadata-core-schema.json         # Core metadata fields validator
├── 📄 dcat-metadata-schema.json         # DCAT 3.0 alignment schema
├── 📄 care-metadata-schema.json         # CARE cultural-safety schema
├── 📄 provenance-link-schema.json       # KFM provenance linkage schema
└── 📄 stac-crosswalk-schema.json        # STAC ↔ metadata crosswalk schema
~~~

Subcategory-specific schemas (e.g., interaction spheres) are defined in their own subtrees and build on these global standards.

---

## 1️⃣ Core Metadata Schema (`metadata-core-schema.json`)

The **core metadata schema** validates the baseline structure of cultural-landscape metadata JSON files.

It enforces:

- Presence and type of required DCAT and KFM fields.  
- Reserved field names and allowed value types.  
- Minimal constraints for CARE fields (presence, basic patterning).

Typical constraints include:

- `dct:title` — required, string.  
- `dct:description` — required, string.  
- `dct:license` — required, string.  
- `kfm:domain` — must be `"archaeology-cultural-landscapes"`.  
- `kfm:landscape_type` / `kfm:region_type` — must be a string from a controlled set (e.g., `region`, `route`, `interaction_sphere`, `resource_area`).  
- `kfm:provenance` — required, string path to a provenance JSON file.

Subtrees (e.g., interaction-spheres) may require additional fields via their own schemas.

---

## 2️⃣ DCAT 3.0 Schema (`dcat-metadata-schema.json`)

The **DCAT schema** ensures that each cultural-landscape metadata record minimally satisfies **DCAT 3.0** semantics.

It validates:

- `dct:title`  
- `dct:description`  
- `dct:license`  
- `dct:temporal` (string or structured interval object)  
- `dcat:keyword` (array of strings)  
- `dcat:distribution` (string path or URL)

The associated DCAT crosswalk schema (see below) ensures consistency between DCAT metadata and STAC Items/Collections.

---

## 3️⃣ CARE Metadata Schema (`care-metadata-schema.json`)

The **CARE schema** validates cultural-safety fields in metadata records.

It checks:

- `care:sensitivity` — must be one of `"general"`, `"generalized"`, `"restricted-generalized"`.  
- `care:review` — must be one of `"faircare"`, `"tribal"`, `"none-required"`.  
- `care:notes` — when sensitivity is not `"general"`, `care:notes` is required.  
- `care:visibility_rules` — must be one of `"h3-only"`, `"no-exact-points"`, `"polygon-generalized"`.  
- `care:consent_status` — should be one of `approved`, `conditional`, `not-approved`, `not-applicable`.

Policies enforced by this schema (together with governance docs):

- `care:sensitivity = "restricted"` is **not allowed** in public-governed metadata.  
- `"restricted-generalized"` requires additional governance and subtree-specific checks (for example, protohistoric interaction spheres).

---

## 4️⃣ Provenance Link Schema (`provenance-link-schema.json`)

The **provenance-link schema** ensures that metadata records correctly reference PROV-O lineage logs.

It enforces:

- Presence of `kfm:provenance`.  
- Path format conventions (relative to metadata location).  
- Optional checks on path prefix (e.g., `../provenance/` for dataset-local provenance).

Downstream tooling may confirm:

- That the referenced file exists.  
- That it satisfies appropriate provenance schemas (under `../provenance/`).

---

## 5️⃣ STAC Crosswalk Schema (`stac-crosswalk-schema.json`)

The **STAC crosswalk schema** validates cross-consistency between:

- Cultural-landscape metadata JSON in this directory.  
- Associated STAC Items/Collections in `../stac/`.

Typical crosswalk checks include:

| Metadata Field        | STAC Field                                  |
|-----------------------|---------------------------------------------|
| `dct:title`           | STAC `id` / `title` / `description`         |
| `dct:license`         | STAC `license`                              |
| `dct:temporal`        | STAC temporal coverage (`extent.temporal` or Item temporal properties) |
| `kfm:culture_phase`   | STAC `properties.kfm:culture_phase`         |
| `care:sensitivity`    | STAC `properties.care:sensitivity`          |
| `kfm:provenance`      | STAC `properties.kfm:provenance`            |
| `dcat:distribution`   | STAC `assets.data.href` or Item path        |

Crosswalk errors indicate drift and must be corrected before release.

---

## 🧪 Validation & CI Integration

Schemas in this directory are used by KFM’s validation tooling and CI workflows.

Typical CI configuration:

- `.github/workflows/metadata-validate.yml`  
- `.github/workflows/faircare-audit.yml`  
- `.github/workflows/artifact-stac-validate.yml`  

Validation steps commonly include:

1. JSON Schema validation of each metadata JSON file against:
   - `metadata-core-schema.json`  
   - `dcat-metadata-schema.json`  
   - `care-metadata-schema.json`  

2. Provenance link checks using `provenance-link-schema.json`.  
3. Crosswalk checks with STAC using `stac-crosswalk-schema.json`.  

Any validation failure must be resolved before merge or inclusion in a KFM release.

---

## 🔗 Related Specifications

- `../README.md`  
  – Global cultural landscape metadata standards.  
- `../templates/README.md`  
  – Cultural landscape metadata templates (DCAT + KFM + CARE).  
- `../../interaction-spheres/metadata/schemas/README.md`  
  – Interaction-sphere-specific metadata schemas (specialized on top of these).  
- `../../interaction-spheres/stac/schemas/README.md`  
  – STAC schemas for interaction spheres.  
- `../../provenance/README.md`  
  – Cultural landscape provenance standards and QA templates.

---

## 🕰 Version History

| Version   | Date       | Author                                   | Summary                                                                 |
|-----------|------------|------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3   | 2025-12-02 | Cultural Landscape WG · FAIR+CARE Council | Created global cultural-landscape metadata schema index; aligned with interaction-sphere schemas; added energy/carbon telemetry references. |
| v10.4.0   | 2025-11-17 | Cultural Landscape WG · FAIR+CARE Council | Initial metadata schema definition; established DCAT/KFM/CARE/provenance crosswalk expectations. |
| v10.0.0   | 2025-11-10 | Landscape Metadata Team                  | Prototype schema scaffolding for cultural landscape metadata.          |

---

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
FAIR+CARE · Sovereignty-Aligned  
KFM-MDP v11.2.2 · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Cultural Landscape Metadata Standards](../README.md)

