---
title: "🏺🗂️ Kansas Frontier Matrix — Great Bend Aspect Interaction Sphere STAC Collections (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/great-bend-aspect/stac/README.md"
description: "STAC 1.0 Collection documentation for the Great Bend Aspect interaction-sphere dataset in KFM v11, with KFM and CARE extensions."
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Cultural Landscape Working Group · FAIR+CARE Council · Tribal Advisory Consultation Recommended"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_uuid: "urn:kfm:doc:cultural-landscape-interaction-sphere-great-bend-aspect-stac-collections-v11.2.3"
doc_kind: "STAC Collection Index"
intent: "great-bend-aspect-stac-collections"
semantic_document_id: "kfm-doc-archaeology-cultural-landscapes-great-bend-aspect-stac-collections-v11.2.3"
category: "Analyses · Archaeology · Cultural Landscapes · STAC"

sbom_ref: "../../../../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../schemas/telemetry/archaeology-great-bend-aspect-stac-collections-v1.json"
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

data_steward: "Cultural Landscape Working Group · FAIR+CARE Council · Tribal Advisory Consultation Recommended"
provenance_chain:
  - "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/great-bend-aspect/stac/collections/README.md@v10.4.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true
---

# 🏺🗂️ STAC Collections — Great Bend Aspect Interaction Sphere (v11)

`docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/great-bend-aspect/stac/collections/README.md`

**Purpose**  
Define and document the **STAC Collection layer** for the **Great Bend Aspect (GBA) Interaction Sphere** within the Kansas Frontier Matrix (KFM).

The Collection:

- Groups all STAC Items belonging to the Great Bend Aspect interaction sphere.  
- Declares shared spatial and temporal coverage.  
- Applies CARE and sovereignty metadata at the collection level.  
- Ensures alignment with DCAT, provenance, and global interaction-sphere STAC schemas.  

The Great Bend Aspect includes **Late Prehistoric and Protohistoric** components, which carry **elevated cultural sensitivity** and therefore require enhanced CARE compliance and recommended tribal advisory consultation.

---

## 📘 Overview

This directory defines a single STAC Collection for the Great Bend Aspect interaction sphere:

- `great-bend-aspect.json`  

This Collection:

- Serves as the **entry point** for STAC-based discovery of GBA-related interaction-sphere data.  
- Provides generalized spatial extent and time span for the sphere.  
- Encodes KFM and CARE metadata to be inherited or refined by child Items.  
- Connects to:
  - STAC Item(s) (for example, `../great-bend-aspect-v2.json`)  
  - Metadata (`../../metadata/great-bend-aspect-v2.json`)  
  - Provenance (`../../provenance/great-bend-aspect-v2.json`)  

For broader context on interaction-sphere STAC collections, see:

- `../../stac/collections/README.md`

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/great-bend-aspect/stac/collections/
├── 📄 README.md                # This file (Collection index)
└── 📄 great-bend-aspect.json   # STAC Collection for the Great Bend Aspect interaction sphere
~~~

---

## 📦 Required Structure for `great-bend-aspect.json`

The Collection must satisfy STAC 1.0 core requirements plus KFM and CARE extensions.

### 1️⃣ STAC Core Fields

| Field          | Description                               | Example                       |
|----------------|-------------------------------------------|-------------------------------|
| `stac_version` | STAC version                              | `"1.0.0"`                     |
| `type`         | STAC object type                          | `"Collection"`                |
| `id`           | Collection identifier                     | `"great-bend-aspect"`         |
| `description`  | Generalized cultural/landscape summary    | `"Generalized Great Bend Aspect interaction sphere in central Kansas."` |
| `license`      | SPDX license                              | `"CC-BY-4.0"`                  |

Collections may also define `keywords`, `links`, and other optional STAC metadata consistent with global schemas.

---

### 2️⃣ Extent (Spatial & Temporal)

#### Spatial Extent

- `extent.spatial.bbox` must represent the **generalized** geographic extent of the interaction sphere.  
- BBOX must not imply site-level precision; it should be derived from generalized polygons (for example, using convex hulls or buffered H3 mosaics).

Example:

~~~json
"extent": {
  "spatial": {
    "bbox": [
      [-101.8, 37.0, -95.3, 40.5]
    ]
  },
  "temporal": {
    "interval": [
      ["1350-01-01T00:00:00Z", "1700-01-01T00:00:00Z"]
    ]
  }
}
~~~

#### Temporal Extent

- `extent.temporal.interval` must cover the Late Prehistoric–Protohistoric range of the Great Bend Aspect (for example, AD 1350–1700).  
- Intervals must be OWL-Time–compatible and align with cultural-phase metadata used in Story Nodes and Focus Mode.

---

### 3️⃣ KFM Cultural-Landscape Extensions (`kfm:*`)

The Collection should include KFM fields consistent with global interaction-sphere standards:

| Field            | Description                                   | Example                            |
|------------------|-----------------------------------------------|------------------------------------|
| `kfm:domain`     | Domain identifier                             | `"archaeology-cultural-landscapes"` |
| `kfm:region_type`| Region type                                   | `"interaction_sphere"`             |
| `kfm:culture_phase` (optional) | Phases represented in the sphere | `["GBA-Early","GBA-Middle","GBA-Late"]` |
| `kfm:review_cycle` | Review cadence                             | `"Biannual"`                       |

`kfm:domain` and `kfm:region_type` are required by KFM cultural-landscape schemas and must match those used in the corresponding Items and metadata.

---

### 4️⃣ CARE & Sovereignty Fields (`care:*`)

Because this dataset carries **elevated sensitivity** but is not in the same high-sensitivity category as, for example, Protohistoric Wichita, typical Collection-level values are:

| Field              | Recommended Value / Notes                                 |
|--------------------|-----------------------------------------------------------|
| `care:sensitivity` | `"generalized"`                                           |
| `care:review`      | `"faircare"` (with optional tribal advisory consultation) |
| `care:notes`       | For example: `"Generalized due to protohistoric sensitivity; no site-level or sacred geographic data included."` |
| `care:visibility_rules` | `"polygon-generalized"` or `"h3-only"` for specific contexts |

These values should reflect the **least permissive** sensitivity across all Items in the Collection. If a future GBA-related Item is assessed as more sensitive, the Collection’s CARE fields may need to be updated accordingly.

---

### 5️⃣ Links (`links[]`)

The Collection must provide `links` to:

- Its own STAC Items:

  ```json
  {
    "rel": "item",
    "href": "../great-bend-aspect-v2.json"
  }
