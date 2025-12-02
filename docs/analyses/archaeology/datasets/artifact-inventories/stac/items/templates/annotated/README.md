---
title: "📄📝 Kansas Frontier Matrix — Annotated STAC Item Templates for Artifact Inventories (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/artifact-inventories/stac/items/templates/annotated/README.md"
description: "Annotated STAC 1.0 Item templates for KFM v11 artifact inventories, with field-by-field KFM and CARE guidance."
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Archaeology Working Group · FAIR+CARE Council · Metadata Standards Subcommittee"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_uuid: "urn:kfm:doc:archaeology-artifact-stac-item-templates-annotated-v11.2.3"
doc_kind: "Annotated Templates"
intent: "artifact-inventory-stac-item-templates-annotated"
semantic_document_id: "kfm-doc-archaeology-artifact-stac-item-templates-annotated-v11.2.3"
category: "Analyses · Archaeology · STAC Items · Templates"

sbom_ref: "../../../../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../schemas/telemetry/archaeology-artifact-stac-item-templates-annotated-v1.json"
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
immutability_status: "mutable-plan"

header_profile: "standard"
footer_profile: "standard"

data_steward: "Archaeology Working Group · Metadata Standards Subcommittee"
provenance_chain:
  - "docs/analyses/archaeology/datasets/artifact-inventories/stac/items/templates/annotated/README.md@v10.4.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true
---

# 📄📝 Kansas Frontier Matrix — Annotated STAC Item Templates for Artifact Inventories (v11)

`docs/analyses/archaeology/datasets/artifact-inventories/stac/items/templates/annotated/README.md`

**Purpose**  
Provide **line-by-line annotated STAC Item templates** for all artifact inventory types in KFM v11.

These annotated templates show how to construct fully valid, culturally safe, machine-readable STAC Items that integrate with:

- STAC 1.0 core  
- KFM archaeology extension (`kfm:*`)  
- CARE cultural safety extension (`care:*`)  
- DCAT 3.0 crosswalks (where used)  
- PROV-O provenance chains  
- KFM knowledge graph ingestion  
- Focus Mode v3 and Story Node pipelines  
- MCP-DL v6.3 and KFM-MDP v11.2.2 documentation rules  

They are **teaching artifacts**; production Items must be based on the non-annotated templates one directory up.

---

## 📘 Overview

Annotated templates in this directory describe:

- Lithic STAC Item  
- Ceramic STAC Item  
- Metal / protohistoric STAC Item  
- Faunal STAC Item (public-domain oriented)

Each annotated example includes:

- Field-level explanations and allowed values  
- CARE and sovereignty notes  
- Spatial generalization expectations (H3-based)  
- DCAT / PROV-O / graph integration hints  
- Validation cues for CI and governance

All examples use synthetic, non-sensitive data.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/artifact-inventories/stac/items/templates/annotated/
├── 📄 README.md                      # This file
├── 📄 item_lithics_annotated.json    # Annotated lithic STAC Item example
├── 📄 item_ceramics_annotated.json   # Annotated ceramic STAC Item example
├── 📄 item_metals_annotated.json     # Annotated metal/protohistoric STAC Item example
├── 📄 item_faunal_annotated.json     # Annotated faunal STAC Item example
└── 📄 field_guide.md                 # Field reference for STAC / KFM / CARE
~~~

This layout is **normative** for annotated artifact-inventory STAC Item templates.

---

## 🧱 Annotated STAC Item Template — Lithics

~~~json
{
  "stac_version": "1.0.0",
  "_comment_stac_version": "STAC version must be 1.0.0 for KFM v11.",

  "type": "Feature",
  "_comment_type": "All artifact inventory Items are STAC Features.",

  "id": "lithics-TEMPLATE-ID",
  "_comment_id": "Lowercase, hyphenated, versioned (e.g., flint-hills-lithics-v11). Must match filename stem.",

  "bbox": [-102.1, 37.0, -94.6, 40.1],
  "_comment_bbox": "Generalized bounding box for the dataset extent; never use site-precise bounds.",

  "geometry": {
    "type": "MultiPoint",
    "_comment_geometry_type": "MultiPoint or simplified polygons only; all coordinates generalized.",
    "coordinates": [
      /* H3-generalized coordinates only */
    ]
  },

  "properties": {
    "kfm:domain": "archaeology-artifact-inventories",
    "_comment_kfm_domain": "Domain identifier shared by all artifact-inventory Items.",

    "kfm:phase": "PHASE-HERE",
    "_comment_phase": "Cultural-phase label used in timelines, Story Nodes, and Focus Mode.",

    "kfm:material_class": "lithic",
    "_comment_material_class": "Controlled vocabulary value for lithic inventories.",

    "kfm:datatype": "artifact-inventory",
    "_comment_datatype": "Constant for all artifact inventory Items.",

    "kfm:generalization": "H3-r7",
    "_comment_generalization": "Records spatial generalization level applied to geometry.",

    "kfm:source": "INSTITUTION",
    "_comment_source": "Institution or program responsible for the dataset.",

    "kfm:provenance": "../provenance/FILE.json",
    "_comment_provenance": "Relative path to PROV-O lineage JSON.",

    "care:sensitivity": "generalized",
    "_comment_care_sensitivity": "Coordinates and possibly context generalized to avoid exposing sensitive locations.",

    "care:sovereignty": "protected",
    "_comment_sovereignty": "Indicates dataset use is governed by sovereignty policies.",

    "care:notes": "Explanation of generalization strategy and any cultural-safety adjustments.",
    "_comment_care_notes": "Short description of H3 strategy and review outcomes.",

    "dct:license": "CC-BY-4.0",
    "_comment_license": "SPDX license identifier.",

    "datetime": null
  },

  "assets": {
    "data": {
      "href": "../inventories/FILE.csv",
      "_comment_data_href": "Relative path to artifact inventory table.",
      "type": "text/csv",
      "_comment_data_type": "MIME type for the main data asset.",
      "roles": ["data"],
      "_comment_roles": "Roles must include \"data\" for the primary inventory."
    }
  },

  "links": [
    {
      "rel": "collection",
      "href": "../collections/lithics.json",
      "_comment_collection_link": "Every Item must reference its parent Collection."
    }
  ]
}
~~~

---

## 🧱 Annotated STAC Item Template — Ceramics

~~~json
{
  "stac_version": "1.0.0",
  "_comment_stac_version": "STAC core header.",

  "type": "Feature",
  "_comment_type": "Artifact inventory → STAC Feature.",

  "id": "ceramics-TEMPLATE-ID",
  "_comment_id": "Lowercase ID, matching filename stem and version.",

  "bbox": [-102.1, 37.0, -94.9, 40.0],
  "_comment_bbox": "Generalized ceramic dataset extent.",

  "geometry": {
    "type": "MultiPoint",
    "coordinates": [
      /* generalized coordinates */
    ]
  },
  "_comment_geometry": "All coordinates generalized; no exact provenience.",

  "properties": {
    "kfm:domain": "archaeology-artifact-inventories",

    "kfm:phase": "PHASE-HERE",
    "_comment_phase": "Phase label consistent with archaeology phase lists.",

    "kfm:material_class": "ceramic",
    "_comment_material_class": "Controlled material class for ceramics.",

    "kfm:datatype": "artifact-inventory",
    "kfm:generalization": "H3-r7",
    "kfm:source": "INSTITUTION",
    "kfm:provenance": "../provenance/FILE.json",

    "care:sensitivity": "generalized",
    "_comment_care_sensitivity": "Ceramic motifs and contexts generalized as needed.",

    "care:sovereignty": "protected",
    "care:notes": "Motif categories generalized and filtered for cultural safety.",
    "_comment_care_notes": "Explain motif filtering and any additional safeguards.",

    "dct:license": "CC-BY-4.0",
    "datetime": null
  },

  "assets": {
    "data": {
      "href": "../inventories/FILE.csv",
      "type": "text/csv",
      "roles": ["data"]
    }
  },

  "links": [
    {
      "rel": "collection",
      "href": "../collections/ceramics.json"
    }
  ]
}
~~~

---

## 🧱 Annotated STAC Item Template — Metals / Protohistoric

~~~json
{
  "stac_version": "1.0.0",
  "type": "Feature",

  "id": "metals-TEMPLATE-ID",
  "_comment_id": "ID and filename should match and carry version suffix.",

  "bbox": [-102.1, 37.0, -94.6, 40.1],
  "_comment_bbox": "Generalized bounding box for metals/protohistoric inventory.",

  "geometry": {
    "type": "MultiPoint",
    "coordinates": [
      /* generalized coordinates */
    ]
  },
  "_comment_geometry": "Generalized only; metals near sensitive sites must not be precise.",

  "properties": {
    "kfm:domain": "archaeology-artifact-inventories",

    "kfm:phase": "PHASE-HERE",
    "_comment_phase": "Phase/group representing contact or protohistoric context.",

    "kfm:material_class": "metal",
    "kfm:datatype": "artifact-inventory",
    "kfm:generalization": "H3-r7",
    "kfm:source": "INSTITUTION",
    "kfm:provenance": "../provenance/FILE.json",

    "care:sensitivity": "generalized",
    "care:review": "tribal",
    "_comment_review": "Contact-era materials require tribal/sovereignty review.",

    "care:sovereignty": "protected",
    "care:notes": "Cultural implications of contact-era materials reviewed via sovereignty processes.",
    "_comment_notes": "Summarize tribal consultation and any required restrictions.",

    "dct:license": "CC-BY-4.0",
    "datetime": null
  },

  "assets": {
    "data": {
      "href": "../inventories/FILE.csv",
      "type": "text/csv",
      "roles": ["data"]
    }
  },

  "links": [
    {
      "rel": "collection",
      "href": "../collections/metals.json"
    }
  ]
}
~~~

---

## 🧱 Annotated STAC Item Template — Faunal (Public-Domain Oriented)

~~~json
{
  "stac_version": "1.0.0",
  "type": "Feature",

  "id": "faunal-TEMPLATE-ID",
  "_comment_id": "ID for faunal inventory; PD or clearly non-sensitive only.",

  "bbox": [-102.1, 37.0, -94.6, 40.1],
  "_comment_bbox": "Generalized bounding box for faunal distribution.",

  "geometry": {
    "type": "MultiPoint",
    "coordinates": [
      /* generalized coordinates */
    ]
  },
  "_comment_geometry": "Even PD faunal data should avoid sacred-species exact locations.",

  "properties": {
    "kfm:domain": "archaeology-artifact-inventories",

    "kfm:phase": "PHASE-HERE",

    "kfm:material_class": "faunal",
    "kfm:datatype": "artifact-inventory",
    "kfm:generalization": "H3-r7",
    "kfm:source": "INSTITUTION",
    "kfm:provenance": "../provenance/FILE.json",

    "care:sensitivity": "general",
    "_comment_care_sensitivity": "Faunal inventories here must be PD-safe and exclude sacred species.",

    "care:sovereignty": "protected",
    "care:notes": "Faunal inventories checked to exclude sacred species and restricted contexts.",

    "dct:license": "CC-BY-4.0",
    "datetime": null
  },

  "assets": {
    "data": {
      "href": "../inventories/FILE.csv",
      "type": "text/csv",
      "roles": ["data"]
    }
  },

  "links": [
    {
      "rel": "collection",
      "href": "../collections/faunal.json"
    }
  ]
}
~~~

---

## 📚 Field Guide Reference

For detailed field definitions and allowed values, see:

`docs/analyses/archaeology/datasets/artifact-inventories/stac/items/templates/annotated/field_guide.md`

That guide covers:

- STAC core fields used in these templates  
- KFM archaeology extension fields (`kfm:*`)  
- CARE fields (`care:*`) and allowed values  
- DCAT crosswalk guidance  
- Graph and Focus Mode integration notes  

---

## 🧪 Validation Instructions

Every new STAC Item derived from these annotated templates (via the non-annotated templates) must pass:

1. STAC Item schema validation (core + configured extensions).  
2. KFM archaeology extension validation (`kfm:*`).  
3. CARE and sovereignty validation (`care:*` values and consistency with geometry).  
4. DCAT crosswalk validation (where DCAT metadata exists).  
5. Provenance linkage checks (`kfm:provenance` resolvable and valid PROV-O).  
6. Spatial generalization checks (no site-precise coordinates; H3-based generalization).

CI workflow example:

- `.github/workflows/artifact-stac-validate.yml`

---

## 🕰 Version History

| Version   | Date       | Author                               | Summary                                                                 |
|-----------|------------|--------------------------------------|-------------------------------------------------------------------------|
| v11.2.3   | 2025-12-02 | Archaeology WG · Metadata Standards Subcommittee | Updated annotated templates for KFM v11.2.3; added sovereignty, energy/carbon telemetry references, and Focus Mode v3 notes. |
| v10.4.0   | 2025-11-17 | Archaeology WG · FAIR+CARE Council   | Added annotated STAC Item templates for all artifact classes with CARE and KFM extension commentary. |
| v10.0.0   | 2025-11-10 | Artifact Metadata Team               | Initial annotated templates directory scaffold.                         |

---

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
FAIR+CARE · Sovereignty-Governed  
KFM-MDP v11.2.2 · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to STAC Item Templates](../README.md)