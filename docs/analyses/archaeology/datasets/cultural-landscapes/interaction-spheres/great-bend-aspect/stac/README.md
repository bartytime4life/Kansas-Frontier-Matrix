---
title: "🏺🗂️ Kansas Frontier Matrix — Great Bend Aspect Interaction Sphere STAC Catalog (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/great-bend-aspect/stac/README.md"
description: "STAC 1.0 Collection + Item documentation for the Great Bend Aspect interaction-sphere dataset in KFM v11, with KFM and CARE extensions."
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Cultural Landscape Working Group · FAIR+CARE Council · Tribal Advisory Consultation Recommended"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_uuid: "urn:kfm:doc:cultural-landscape-interaction-sphere-great-bend-aspect-stac-v11.2.3"
doc_kind: "STAC Catalog"
intent: "great-bend-aspect-stac"
semantic_document_id: "kfm-doc-archaeology-cultural-landscapes-great-bend-aspect-stac-v11.2.3"
category: "Analyses · Archaeology · Cultural Landscapes · STAC"

sbom_ref: "../../../../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../schemas/telemetry/archaeology-great-bend-aspect-stac-v1.json"
energy_schema: "../../../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../../../schemas/telemetry/carbon-gco2e-v1.json"

governance_ref: "../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant (Elevated Sensitivity)"
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
  - "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/great-bend-aspect/stac/README.md@v10.4.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true
---

# 🏺🗂️ STAC Catalog — Great Bend Aspect Interaction Sphere (v11)

`docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/great-bend-aspect/stac/README.md`

**Purpose**  
Document the **STAC 1.0 Collection and Item** used to represent the **Great Bend Aspect interaction sphere** in KFM v11.

This catalog defines:

- The **STAC Collection** for the Great Bend Aspect.  
- The **STAC Item** for the generalized interaction-sphere geometry.  
- Required KFM (`kfm:*`) and CARE (`care:*`) properties.  
- Crosswalk expectations with DCAT metadata and PROV-O provenance.  

For dataset context, see:

- `../README.md` (Great Bend Aspect dataset overview).  

For global interaction-sphere STAC rules, see:

- `../../stac/README.md` (interaction-sphere STAC catalog).

---

## 📘 Overview

The **Great Bend Aspect Interaction Sphere** STAC artifacts:

- Provide a **machine-readable** description of the generalized Late Prehistoric–Protohistoric interaction region.  
- Encode spatial and temporal extents at safe, generalized scales.  
- Integrate KFM cultural-landscape semantics (`kfm:*` fields).  
- Capture CARE metadata used to govern visibility and narrative framing.  
- Link to provenance and metadata artifacts for full FAIR+CARE traceability.

This directory is the **dataset-specific STAC catalog** for Great Bend Aspect, nested within the global interaction-sphere catalog.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/great-bend-aspect/stac/
├── 📄 README.md                       # This file (STAC catalog for Great Bend Aspect)
├── 📄 great-bend-aspect-v2.json       # STAC Item (generalized interaction sphere geometry)
└── 📂 collections/
    └── 📄 great-bend-aspect.json      # STAC Collection definition
~~~

IDs and filenames must be consistent across:

- `stac/great-bend-aspect-v2.json` (Item)  
- `stac/collections/great-bend-aspect.json` (Collection)  
- `../metadata/great-bend-aspect-v2.json` (metadata)  
- `../provenance/great-bend-aspect-v2.json` (provenance)

---

## 📚 Controlled Vocabularies

Following the interaction-sphere standards:

| Field / Property               | Allowed / Example Values                                           |
|--------------------------------|--------------------------------------------------------------------|
| `kfm:domain`                   | `"archaeology-cultural-landscapes"`                               |
| `kfm:region_type`              | `"interaction_sphere"`                                            |
| `kfm:interaction_type` (if used) | `"influence_sphere"`, `"exchange_corridor"`, `"contact_zone"`  |
| `care:consent_status`          | `"approved"`, `"conditional"`, `"not-approved"`, `"not-applicable"` |

These may appear under `properties.kfm:*` and `properties.care:*` in Items and at the Collection level as needed.

---

## 📦 STAC Item Requirements (`great-bend-aspect-v2.json`)

The Great Bend Aspect interaction-sphere STAC Item must satisfy:

### STAC Core Fields

- `stac_version: "1.0.0"`  
- `type: "Feature"`  
- `id: "great-bend-aspect-v2"`  
- `collection`: ID of the associated Collection (for example, `"great-bend-aspect"`).  
- `bbox`: generalized bounding box (for example, `[-101.8, 37.0, -95.3, 40.5]`).  
- `geometry`:
  - `type`: `"Polygon"` or `"MultiPolygon"`  
  - `coordinates`: generalized (H3-derived or simplified) polygons.

### KFM Extensions (`properties.kfm:*`)

At minimum:

| Field                 | Description                                      | Example                                        |
|-----------------------|--------------------------------------------------|------------------------------------------------|
| `kfm:domain`          | Domain identifier                                | `"archaeology-cultural-landscapes"`           |
| `kfm:region_type`     | Region type (interaction sphere)                 | `"interaction_sphere"`                        |
| `kfm:culture_phase`   | Cultural phases                                  | `["GBA-Early", "GBA-Middle", "GBA-Late"]`     |
| `kfm:generalization`  | Generalization level                             | `"H3-r7"`                                      |
| `kfm:provenance`      | Provenance reference                             | `"../provenance/great-bend-aspect-v2.json"`   |
| `kfm:review_cycle`    | Review cadence                                   | `"Biannual"`                                   |

Other KFM fields (for example, interaction-type descriptors) may be defined in shared schemas.

### CARE Extensions (`properties.care:*`)

Recommended values (subject to review):

| Field                   | Description / Example                                            |
|-------------------------|------------------------------------------------------------------|
| `care:sensitivity`      | `"generalized"` (elevated but not restricted-generalized)        |
| `care:review`           | `"faircare"` (with optional tribal consultation for later phases) |
| `care:sovereignty`      | `"protected"`                                                    |
| `care:notes`            | For example: `"Protohistoric features generalized; no restricted cultural information included."` |
| `care:visibility_rules` | `"polygon-generalized"`; may be tightened if required           |
| `care:consent_status`   | `"approved"` or `"conditional"` depending on governance         |

CARE values must align with metadata and provenance for this dataset.

### Temporal Properties

- `properties.start_datetime` (for example, `"1350-01-01T00:00:00Z"`).  
- `properties.end_datetime` (for example, `"1700-01-01T00:00:00Z"`).  

Temporal fields must be compatible with OWL-Time and match DCAT `dct:temporal`.

### Assets

At minimum:

- `assets.data`:
  - `href`: `"../great-bend-aspect.geojson"` or equivalent.  
  - `type`: `"application/geo+json"` (or appropriate MIME).  
  - `roles`: must include `"data"`.

---

## 📂 STAC Collection Requirements (`collections/great-bend-aspect.json`)

The Collection groups the Great Bend Aspect interaction-sphere Items (currently just `v2`).

### Required STAC Core Fields

- `stac_version: "1.0.0"`  
- `type: "Collection"`  
- `id: "great-bend-aspect"`  
- `description`: summary of the Great Bend Aspect interaction sphere.  
- `license: "CC-BY-4.0"`  
- `extent`:
  - `extent.spatial.bbox`: generalized bounding box.  
  - `extent.temporal.interval`: intervals spanning AD 1350–1700.

### KFM & CARE Fields

Collection-level properties should reflect the least permissive settings across child Items:

| Field            | Example                                             |
|------------------|-----------------------------------------------------|
| `kfm:domain`     | `"archaeology-cultural-landscapes"`                |
| `kfm:region_type`| `"interaction_sphere"`                             |
| `kfm:review_cycle` | `"Biannual"`                                     |
| `care:sensitivity` | `"generalized"`                                  |
| `care:review`    | `"faircare"`                                       |
| `care:notes`     | `"Generalized due to elevated protohistoric sensitivity"` |

### Links

The Collection should link to:

- Its own STAC Item(s) (`"item"` links).  
- Root/parent collections in the global interaction-sphere catalog (where applicable).

---

## 🧪 Validation & CI Requirements

The Item and Collection in this directory must pass validation via:

- Interaction-sphere STAC schemas in `../../stac/schemas/`:
  - `stac-item-schema.json`  
  - `stac-collection-schema.json`  
  - `kfm-interaction-extension.json`  
  - `care-sensitivity-extension.json`  
  - `dcat-crosswalk.json` (where used).  
- Crosswalk checks with:
  - `../metadata/great-bend-aspect-v2.json` (metadata).  
  - `../provenance/great-bend-aspect-v2.json` (provenance).  

CI workflows (for example):

- `.github/workflows/artifact-stac-validate.yml`  
- `.github/workflows/metadata-validate.yml`  
- `.github/workflows/faircare-audit.yml`  

must succeed before changes are merged.

---

## 🔗 Related Specifications

- `../README.md`  
  – Great Bend Aspect interaction-sphere dataset overview and governance.  
- `../../stac/README.md`  
  – Interaction-sphere STAC catalog (global Items + Collections).  
- `../../stac/schemas/README.md`  
  – STAC schemas for interaction spheres.  
- `../metadata/README.md`  
  – Great Bend Aspect metadata specification.  
- `../provenance/README.md`  
  – Great Bend Aspect provenance logs and requirements.

---

## 🕰 Version History

| Version   | Date       | Author                                   | Summary                                                                 |
|-----------|------------|------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3   | 2025-12-02 | Cultural Landscape WG · FAIR+CARE Council | Updated to KFM v11.2.3; aligned with global interaction-sphere STAC schemas; clarified CARE and KFM fields and validation requirements. |
| v10.4.0   | 2025-11-17 | Cultural Landscape WG · FAIR+CARE Council | Initial Great Bend Aspect STAC catalog documentation; established Item and Collection requirements. |
| v10.0.0   | 2025-11-10 | Landscape Metadata Team                  | Prototype STAC files and basic documentation.                          |

---

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
FAIR+CARE · Sovereignty-Aligned  
KFM-MDP v11.2.2 · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Great Bend Aspect Dataset](../README.md)
