---
title: "🗂️🔄 Kansas Frontier Matrix — Central Plains Exchange Interaction Sphere STAC Collections (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/central-plains-exchange/stac/collections/README.md"
description: "STAC 1.0 Collection documentation for the Central Plains Exchange interaction-sphere dataset in KFM v11, including KFM and CARE extensions."
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Cultural Landscape WG · FAIR+CARE Council · Metadata Standards Subcommittee"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_uuid: "urn:kfm:doc:cultural-landscape-interaction-sphere-central-plains-exchange-stac-collections-v11.2.3"
doc_kind: "STAC Collection Index"
intent: "central-plains-exchange-stac-collections"
semantic_document_id: "kfm-doc-archaeology-cultural-landscapes-central-plains-exchange-stac-collections-v11.2.3"
category: "Analyses · Archaeology · Cultural Landscapes · STAC"

sbom_ref: "../../../../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../schemas/telemetry/archaeology-central-plains-exchange-stac-collections-v1.json"
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

data_steward: "Cultural Landscape WG · FAIR+CARE Council · Metadata Standards Subcommittee"
provenance_chain:
  - "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/central-plains-exchange/stac/collections/README.md@v10.4.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true
---

# 🗂️🔄 STAC Collections — Central Plains Exchange Interaction Sphere (v11)

`docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/central-plains-exchange/stac/collections/README.md`

**Purpose**  
Document the **STAC Collection layer** for the **Central Plains Exchange Interaction Sphere** in KFM v11.

The Collection:

- Groups all STAC Items describing this interaction sphere.  
- Declares shared spatial and temporal coverage.  
- Applies KFM (`kfm:*`) and CARE (`care:*`) metadata at the collection level.  
- Serves as the discovery entry point for this sphere in KFM’s STAC catalogs.

---

## 📘 Overview

A **STAC Collection**:

- Aggregates related STAC Items.  
- Defines generalized spatial and temporal extents.  
- Encodes domain-specific metadata (via `kfm:*`) and sensitivity metadata (via `care:*`).  
- Enables DCAT crosswalks and downstream graph/narrative integrations.

This directory contains one Collection:

- `central-plains-exchange.json`

For Item-level documentation, see:

- `../README.md` (STAC Item docs for this sphere).  

For dataset context, see:

- `../../README.md` (Central Plains Exchange dataset overview).

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/central-plains-exchange/stac/collections/
├── 📄 README.md                      # This file
└── 📄 central-plains-exchange.json   # STAC Collection for this interaction sphere
~~~

---

## 📦 Required Fields for `central-plains-exchange.json`

The Collection must satisfy **STAC 1.0** core requirements plus KFM + CARE extension rules defined in the interaction-sphere schemas.

### 1️⃣ STAC Core Fields

| Field          | Description                        | Example                                        |
|----------------|------------------------------------|------------------------------------------------|
| `stac_version` | STAC version                       | `"1.0.0"`                                      |
| `type`         | Object type                        | `"Collection"`                                 |
| `id`           | Collection identifier              | `"central-plains-exchange"`                    |
| `description`  | Cultural/landscape summary         | `"Generalized Central Plains Exchange interaction sphere in the central Great Plains."` |
| `license`      | SPDX license                       | `"CC-BY-4.0"`                                  |

---

### 2️⃣ Extent (Spatial & Temporal)

#### Spatial Extent

- `extent.spatial.bbox` represents the **generalized** spatial extent of the interaction sphere.  
- BBOX must be derived from generalized geometry and be coarse enough to avoid site-level inference.

Example BBOX (illustrative):

- `[-103.0, 36.8, -94.5, 43.2]`

#### Temporal Extent

- `extent.temporal.interval` captures the cultural span (approximately AD 900–1400).  
- Intervals must be OWL-Time–compatible and align with DCAT and STAC Item temporal properties.

Example interval (illustrative):

- `[["0900-01-01T00:00:00Z","1400-01-01T00:00:00Z"]]`

---

### 3️⃣ KFM Cultural-Landscape Extensions (`kfm:*`)

Collection-level KFM fields should include:

| Field            | Description                          | Example                                |
|------------------|--------------------------------------|----------------------------------------|
| `kfm:domain`     | Domain identifier                    | `"archaeology-cultural-landscapes"`     |
| `kfm:region_type`| Region type                          | `"interaction_sphere"`                  |
| `kfm:review_cycle` | Governance review cadence         | `"Biannual"`                            |

Collections may optionally summarize phases:

- `kfm:culture_phase`: e.g. `["CPT-Early","CPT-Middle","CPT-Late"]`

These values must be consistent with:

- STAC Item `../central-plains-exchange-v1.json`.  
- Metadata in `../../metadata/central-plains-exchange-v1.json`.

---

### 4️⃣ CARE Cultural-Safety Metadata (`care:*`)

The Central Plains Exchange sphere is **CARE-Compliant** with medium sensitivity.

Recommended Collection-level CARE fields:

| Field              | Recommended Value / Notes                                    |
|--------------------|--------------------------------------------------------------|
| `care:sensitivity` | `"generalized"`                                              |
| `care:review`      | `"faircare"`                                                 |
| `care:notes`       | e.g. `"Generalized polygons used; no site-level or sacred locations represented."` |
| `care:visibility_rules` | `"polygon-generalized"` (or `"h3-only"` for tighter controls, if required) |

CARE metadata should express the least permissive sensitivity required across all child Items.

---

### 5️⃣ Links (`links[]`)

The Collection’s `links` array should include:

- At least one `item` link pointing to the associated STAC Item:
  - `rel: "item"`, `href: "../central-plains-exchange-v1.json"`  

- Links to parent or root interaction-sphere Collections in the global catalog (if used):
  - `rel: "parent"` or `rel: "root"` with appropriate href paths.

Additional documentation or license links may be added, following KFM link conventions.

---

## 🧪 Validation & CI Requirements

The `central-plains-exchange.json` Collection must validate against interaction-sphere STAC schemas in:

- `../../stac/schemas/`

Including, for example:

- `stac-collection-schema.json`  
- `kfm-interaction-extension.json`  
- `care-sensitivity-extension.json`  
- `dcat-crosswalk.json` (where Collection ↔ DCAT mappings are enforced)  

The Collection must remain consistent with:

- STAC Item: `../central-plains-exchange-v1.json`  
- Metadata: `../../metadata/central-plains-exchange-v1.json`  
- Provenance: `../../provenance/central-plains-exchange-v1.json`

CI workflows (for example):

- `.github/workflows/artifact-stac-validate.yml`  
- `.github/workflows/metadata-validate.yml`  
- `.github/workflows/faircare-audit.yml`  

must succeed before changes are merged or released.

---

## 🔗 Related Specifications

- `../README.md`  
  – Central Plains Exchange STAC documentation (Collection + Item).  
- `../../README.md`  
  – Central Plains Exchange dataset overview.  
- `../../metadata/README.md`  
  – Interaction-sphere metadata standards.  
- `../../provenance/README.md`  
  – Interaction-sphere provenance standards and templates.  
- `../../stac/README.md`  
  – Global interaction-sphere STAC catalog.

---

## 🕰 Version History

| Version   | Date       | Author                                                   | Summary                                                                 |
|-----------|------------|----------------------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3   | 2025-12-02 | Cultural Landscape WG · FAIR+CARE Council · Metadata Standards Subcommittee | Updated to KFM v11.2.3; ensured box-safe formatting; aligned with interaction-sphere STAC schemas and CARE fields. |
| v10.4.0   | 2025-11-17 | Cultural Landscape WG · FAIR+CARE Council               | Initial Central Plains Exchange Collection README; defined STAC, KFM, and CARE requirements. |
| v10.0.0   | 2025-11-10 | Landscape Metadata Team                                  | Prototype Collection metadata scaffold.                                |

---

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
FAIR+CARE · Sovereignty-Aligned  
KFM-MDP v11.2.2 · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Central Plains Exchange STAC Catalog](../README.md)
