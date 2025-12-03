---
title: "📐 Kansas Frontier Matrix — Interaction Sphere STAC Schemas (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/stac/schemas/README.md"
description: "JSON Schema set for validating KFM v11 interaction-sphere STAC Items and Collections, including KFM and CARE extensions and DCAT crosswalks."
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Cultural Landscape Working Group · FAIR+CARE Council · Metadata Standards Subcommittee"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_uuid: "urn:kfm:doc:archaeology-interaction-spheres-stac-schemas-v11.2.3"
doc_kind: "Schema Documentation"
intent: "interaction-spheres-stac-schemas"
semantic_document_id: "kfm-doc-archaeology-interaction-spheres-stac-schemas-v11.2.3"
category: "Analyses · Archaeology · Cultural Landscapes · STAC · Schemas"

sbom_ref: "../../../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/archaeology-interaction-spheres-stac-schemas-v1.json"
energy_schema: "../../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../../schemas/telemetry/carbon-gco2e-v1.json"

governance_ref: "../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

fair_category: "F1-A1-I1-R1"
care_label: "High-Sensitivity · Sovereignty-Governed"
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

data_steward: "Cultural Landscape Working Group · Metadata Standards Subcommittee · FAIR+CARE Council"
provenance_chain:
  - "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/stac/schemas/README.md@v11.0.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true
---

# 📐 Kansas Frontier Matrix — Interaction Sphere STAC Schemas (v11)

`docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/stac/schemas/README.md`

**Purpose**  
Define and govern the **JSON Schema set** used to validate **STAC 1.0 Items and Collections** for interaction-sphere datasets in KFM v11.

These schemas ensure that interaction-sphere STAC documents are:

- Structurally STAC 1.0 compliant  
- Enriched with KFM cultural-landscape extensions (`kfm:*`)  
- Ethically governed using CARE (`care:*`) and sovereignty rules  
- Consistent with DCAT 3.0, PROV-O provenance, and the KFM knowledge graph  
- Suitable for Focus Mode v3, Story Nodes, and governed public catalogs  

Schemas here are specialized for interaction spheres, but reuse shared STAC patterns defined for artifact inventories and other landscape datasets.

---

## 📘 Overview

This directory provides:

- STAC Item and Collection schemas tailored for **interaction spheres**  
- KFM cultural-landscape extension schemas (`kfm:*`)  
- CARE sensitivity and sovereignty schemas (`care:*`)  
- DCAT ↔ STAC crosswalk schemas for catalog interoperability  
- Templates for defining additional cultural-landscape-specific schemas  

All schemas use **JSON Schema Draft 2020-12**, consistent with project-wide standards.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/stac/schemas/
├── 📄 README.md                         # This file
├── 📄 stac-item-schema.json             # Validator for interaction-sphere STAC Items
├── 📄 stac-collection-schema.json       # Validator for interaction-sphere STAC Collections
├── 📄 kfm-interaction-extension.json    # KFM cultural-landscapes/interaction-spheres extension schema
├── 📄 care-sensitivity-extension.json   # CARE cultural safety schema for interaction spheres
├── 📄 dcat-crosswalk.json               # DCAT ↔ STAC mapping schema for interaction spheres
└── 📂 templates/                        # Schema templates for future extensions
~~~

Some schemas may be thin wrappers around shared global schemas; this README focuses on the interaction-sphere–specific layer.

---

## 1️⃣ STAC Item Schema (`stac-item-schema.json`)

The **Item schema** validates interaction-sphere STAC Items in `../items/`.

### Core constraints

- `stac_version`:
  - Must be `"1.0.0"`.  
- `type`:
  - Must be `"Feature"`.  
- `id`:
  - String; must match filename stem.  
- `bbox`:
  - Array of numeric coordinates; generalized extents.  
- `geometry`:
  - `type` must be `"Polygon"` or `"MultiPolygon"`.  
  - Only **generalized** geometries allowed.  
- `properties`:
  - Object; must accept STAC core, `kfm:*`, and `care:*` fields.  
- `assets`:
  - Must include a `data` asset with `href`, `type`, and `roles` that include `"data"`.

The Item schema adds **interaction-sphere–specific** checks via the KFM extension schema (see below).

---

## 2️⃣ STAC Collection Schema (`stac-collection-schema.json`)

The **Collection schema** validates interaction-sphere Collections in `../collections/`.

### Core constraints

- `stac_version = "1.0.0"`  
- `type = "Collection"`  
- `id`:
  - Stable identifier matching filename (for example, `"interaction-spheres"`, `"great-bend-aspect"`).  
- `description`:
  - Human-readable description of the cultural domain.  
- `license`:
  - SPDX identifier (for example, `"CC-BY-4.0"`).  
- `extent`:
  - `spatial.bbox`: generalized bounding boxes (no site-precise extents).  
  - `temporal.interval`: OWL-Time–compatible intervals.  

Collections act as grouping and discovery surfaces for interaction-sphere Items.

---

## 3️⃣ KFM Interaction-Sphere Extension Schema (`kfm-interaction-extension.json`)

The **KFM interaction extension schema** encodes cultural-landscape–specific metadata fields.

Typical properties include:

| Field               | Purpose                                                      |
|---------------------|--------------------------------------------------------------|
| `kfm:domain`        | Must be `"archaeology-cultural-landscapes"`                 |
| `kfm:region_type`   | Controlled vocab: `interaction_sphere`, `exchange_zone`, `contact_region` |
| `kfm:interaction_type` | Controlled vocab: `influence_sphere`, `contact_zone`, `exchange_corridor` |
| `kfm:culture_phase` / `kfm:phase` | Cultural-phase label(s) for the sphere         |
| `kfm:generalization` | Record of generalization level (for example, `"H3-r7"`)    |
| `kfm:review_cycle` | For example, `"Biannual"`                                     |
| `kfm:provenance`   | Path to PROV-O provenance JSON                               |

The schema enforces:

- Use of controlled vocabularies defined in the parent interaction-spheres docs.  
- Required presence of `kfm:domain` and `kfm:region_type` on Items and Collections.  
- Appropriate value types for generalization and phase fields.

---

## 4️⃣ CARE Sensitivity Schema (`care-sensitivity-extension.json`)

The **CARE extension schema** governs cultural-safety metadata for interaction-sphere STAC objects.

Key fields:

| Field                | Rules / Notes                                                |
|----------------------|-------------------------------------------------------------|
| `care:sensitivity`   | `"general"`, `"generalized"`, or `"restricted-generalized"`; `"restricted"` is not permitted in the public catalog. |
| `care:review`        | `"faircare"`, `"tribal"`, or `"none-required"`              |
| `care:notes`         | Required for `generalized` and `restricted-generalized`; describes redaction/generalization decisions. |
| `care:visibility_rules` | For example, `"h3-only"` or `"no-exact-points"`.        |
| `care:consent_status` | `approved`, `conditional`, `not-approved`, `not-applicable`. |

The schema is used to ensure:

- CARE labels and review types are valid.  
- Required notes are present when sensitivity is elevated.  
- Visibility rules align with generalization practice (for example, `h3-only` for highly sensitive paths).

---

## 5️⃣ DCAT Crosswalk Schema (`dcat-crosswalk.json`)

The **DCAT crosswalk schema** validates mappings between DCAT metadata in `../../metadata/` and STAC documents validated by these schemas.

Sample mappings enforced:

| DCAT Field         | STAC Mapping                                      |
|--------------------|---------------------------------------------------|
| `dct:title`        | STAC `id` or `description`                        |
| `dct:license`      | STAC `license`                                    |
| `dct:temporal`     | STAC Collection `extent.temporal.interval` or Item temporal fields |
| `dcat:distribution`| STAC `assets.data.href`                           |
| `dcat:keyword`     | Optional mapping to STAC `keywords`               |

This schema helps prevent drift between DCAT and STAC catalogs and keeps external catalog views consistent with STAC-based views.

---

## 🧪 Validation Pipeline

Schemas in this directory are used by CI and tooling to validate interaction-sphere STAC content.

Typical validation steps:

1. **Schema self-validation** (JSON Schema Draft 2020-12).  
2. **STAC Item/Collection validation** using:
   - `stac-item-schema.json`  
   - `stac-collection-schema.json`  
3. **Extension validation**:
   - `kfm-interaction-extension.json` for `kfm:*` fields.  
   - `care-sensitivity-extension.json` for `care:*` fields.  
4. **DCAT crosswalk validation** using `dcat-crosswalk.json`.  
5. **Provenance linkage checks**:
   - Ensure `kfm:provenance` points to valid files in `../../provenance/`.  

These steps are usually executed via workflows such as:

- `.github/workflows/artifact-stac-validate.yml`  
- `.github/workflows/metadata-validate.yml`  
- `.github/workflows/faircare-audit.yml`

Any validation failure blocks merging of changes that introduce or modify STAC Items/Collections.

---

## 🧠 Graph & Narrative Integration

The schemas here are carefully aligned with:

- Global STAC schema docs under `docs/analyses/archaeology/datasets/artifact-inventories/stac/schemas/`.  
- Cultural-landscape docs under `docs/analyses/archaeology/datasets/cultural-landscapes/`.  

They ensure that:

- Interaction-sphere STAC metadata can be **losslessly mapped** into the knowledge graph using KFM-OP v11.  
- Story Nodes and Focus Mode v3 can **trust** the presence and semantics of key fields (`kfm:*`, `care:*`, temporal and spatial extents).  
- Sovereignty and CARE constraints are **machine-enforced** at the schema level, not just by convention.

---

## 🔗 Related Specifications

To work with interaction-sphere schemas effectively, see also:

- `../README.md`  
  – Interaction Sphere STAC Catalog (Items + Collections overview).  
- `../collections/README.md`  
  – STAC Collections index and requirements.  
- `../items/README.md`  
  – STAC Items index and field requirements.  
- `../../metadata/README.md`  
  – DCAT + CARE metadata for interaction spheres.  
- `../../provenance/README.md`  
  – PROV-O lineage & sovereignty review logs.  
- `../../../../../artifact-inventories/stac/schemas/README.md`  
  – Shared STAC schema patterns and extension definitions used across KFM.

---

## 🕰 Version History

| Version   | Date       | Author                                                   | Summary                                                                 |
|-----------|------------|----------------------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3   | 2025-12-02 | Cultural Landscape WG · Metadata Standards Subcommittee · FAIR+CARE Council | Created interaction-sphere STAC schema index; aligned with v11 catalog, KFM interaction extension, CARE extension, and DCAT crosswalk practices. |
| v11.0.0   | 2025-11-24 | Cultural Landscape WG                                   | Initial interaction-sphere STAC schema definitions and integration scaffolding. |

---

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
FAIR+CARE · Sovereignty-Governed  
KFM-MDP v11.2.2 · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Interaction Sphere STAC Catalog](../README.md)

