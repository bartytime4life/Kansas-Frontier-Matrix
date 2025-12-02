---
title: "📝 Kansas Frontier Matrix — Annotated Artifact STAC Examples (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/artifact-inventories/stac/examples/annotated/README.md"
description: "Deeply annotated STAC 1.0 Items and Collections for KFM v11 artifact inventories, with field-by-field KFM and CARE commentary."
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Archaeology Working Group · FAIR+CARE Council · Metadata Standards Subcommittee"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_uuid: "urn:kfm:doc:archaeology-artifact-stac-examples-annotated-v11.2.3"
doc_kind: "STAC Example Commentary"
intent: "artifact-stac-annotated-examples"
semantic_document_id: "kfm-doc-archaeology-artifact-stac-examples-annotated-v11.2.3"
category: "Analyses · Archaeology · STAC Examples · Templates"

sbom_ref: "../../../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/archaeology-artifact-stac-examples-annotated-v1.json"
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
  - "docs/analyses/archaeology/datasets/artifact-inventories/stac/examples/annotated/README.md@v10.4.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true
---

# 📝 Kansas Frontier Matrix — Annotated Artifact STAC Examples (v11)

`docs/analyses/archaeology/datasets/artifact-inventories/stac/examples/annotated/README.md`

**Purpose**  
Provide **deeply annotated**, line-by-line STAC examples for artifact inventory metadata used in the Kansas Frontier Matrix (KFM).

These examples are intended for:

- Developers and ETL engineers  
- Archaeologists and data stewards  
- FAIR+CARE and sovereignty reviewers  
- Metadata and schema specialists  

They explain:

- Exact field-by-field semantics  
- STAC 1.0 structural rules  
- KFM archaeology extension usage (`kfm:*`)  
- CARE sensitivity and sovereignty metadata (`care:*`)  
- DCAT and PROV-O crosswalk implications  

Annotated examples are **authoritative teaching references**. Production STAC documents must be derived from non-annotated templates.

---

## 📘 Overview

Annotated examples in this directory include:

- Fully annotated STAC Items (lithics, ceramics)  
- Fully annotated STAC Collections (lithics, ceramics)  
- Commentary for each important field and controlled vocabulary  
- Cultural sensitivity notes for artifact metadata  
- Pointers to the field guide (`field_guide.md`) for deeper reference  

All examples are **synthetic or generalized** and never contain real sensitive data.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/artifact-inventories/stac/examples/annotated/
├── 📄 README.md                           # This file
├── 📄 item_lithics_annotated.json         # Annotated lithic STAC Item
├── 📄 item_ceramics_annotated.json        # Annotated ceramic STAC Item
├── 📄 collection_lithics_annotated.json   # Annotated lithic STAC Collection
├── 📄 collection_ceramics_annotated.json  # Annotated ceramic STAC Collection
└── 📄 field_guide.md                      # Definitions for STAC, KFM, CARE, DCAT fields
~~~

This layout is **normative** for annotated STAC examples.

---

## 🧱 Annotated STAC Item Example (Lithics)

~~~json
{
  "stac_version": "1.0.0",
  "_comment_stac_version": "STAC version must be 1.0.0 for KFM archaeology Items.",

  "type": "Feature",
  "_comment_type": "STAC Items representing datasets are always type=\"Feature\".",

  "id": "flint-hills-lithics-v11",
  "_comment_id": "Stable, versioned dataset identifier; should match inventory and provenance stems.",

  "bbox": [-101.2, 37.5, -95.4, 40.1],
  "_comment_bbox": "Bounding box derived from H3-generalized geometry; no site-level precision.",

  "geometry": {
    "type": "MultiPoint",
    "coordinates": [
      /* generalized coordinates only */
    ]
  },
  "_comment_geometry": "MultiPoint or simplified polygons only; all coordinates generalized (H3 or equivalent).",

  "properties": {
    "kfm:domain": "archaeology-artifact-inventories",
    "_comment_kfm_domain": "KFM domain identifier used in ETL and graph mapping.",

    "kfm:phase": "Late Prehistoric",
    "_comment_kfm_phase": "Cultural-phase classification used across Focus Mode and Story Nodes.",

    "kfm:generalization": "H3-r7",
    "_comment_kfm_generalization": "Spatial generalization level; must match transformation applied.",

    "care:sensitivity": "generalized",
    "_comment_care_sensitivity": "Indicates coordinates and context have been generalized for safety.",

    "care:sovereignty": "protected",
    "_comment_care_sovereignty": "Marks this dataset as governed by sovereignty policies.",

    "kfm:provenance": "../../provenance/flint-hills-lithics-v11.json",
    "_comment_kfm_provenance": "Path to PROV-O lineage JSON for this inventory.",

    "dct:license": "CC-BY-4.0",
    "_comment_license": "SPDX license identifier consistent with repo license.",

    "datetime": null
  },

  "assets": {
    "data": {
      "href": "../../inventories/flint-hills-lithics-v11.csv",
      "_comment_href": "Relative path to the artifact inventory table.",

      "type": "text/csv",
      "_comment_type": "MIME type for the main data asset.",

      "roles": ["data"],
      "_comment_roles": "Roles array must include \"data\" for the primary inventory asset."
    }
  },

  "links": [
    {
      "rel": "collection",
      "href": "../collection_example_lithics.json"
    }
  ],
  "_comment_links": "Item should link to its parent Collection when one exists."
}
~~~

---

## 🧱 Annotated STAC Item Example (Ceramics)

~~~json
{
  "stac_version": "1.0.0",
  "_comment_stac_version": "Required STAC core header.",

  "type": "Feature",
  "_comment_type": "Artifact inventory datasets are encoded as STAC Features.",

  "id": "prairie-ceramics-v11",
  "_comment_id": "Unique, versioned ID for this ceramic inventory.",

  "bbox": [-101.9, 37.2, -95.9, 40.2],
  "_comment_bbox": "H3-derived generalized bounding box for the ceramics dataset.",

  "geometry": {
    "type": "MultiPoint",
    "coordinates": [
      /* generalized coordinates only */
    ]
  },
  "_comment_geometry": "Coordinates must never expose exact provenience; all points are generalized.",

  "properties": {
    "kfm:domain": "archaeology-artifact-inventories",
    "_comment_domain": "Domain string used across artifact systems.",

    "kfm:phase": "Middle Ceramic",
    "_comment_phase": "Cultural-phase assignment for this dataset.",

    "kfm:generalization": "H3-r7",
    "_comment_generalization": "Indicates the generalization level applied to spatial data.",

    "care:sensitivity": "generalized",
    "_comment_sensitivity": "CARE label after redaction and generalization.",

    "care:sovereignty": "protected",
    "_comment_sovereignty": "Indicates that sovereignty policies govern downstream use.",

    "kfm:provenance": "../../provenance/prairie-ceramics-v11.json",
    "_comment_provenance": "PROV-O file location for this ceramic inventory.",

    "dct:license": "CC-BY-4.0",
    "_comment_license": "Open license required for public-governed artifact datasets.",

    "datetime": null
  },

  "assets": {
    "data": {
      "href": "../../inventories/prairie-ceramics-v11.csv",
      "_comment_href": "Path to ceramics inventory table.",

      "type": "text/csv",
      "_comment_type": "MIME type for the main inventory asset.",

      "roles": ["data"],
      "_comment_roles": "Roles must include \"data\" for the primary artifact table."
    }
  },

  "_comment_assets": "Each Item must include at least one primary data asset."
}
~~~

---

## 🧱 Annotated STAC Collection Example (Lithics)

~~~json
{
  "stac_version": "1.0.0",
  "_comment_stac_version": "STAC Collections always declare the STAC version.",

  "type": "Collection",
  "_comment_type": "Grouping of lithic artifact Items.",

  "id": "lithics",
  "_comment_id": "Collection identifier; must match filename and semantic grouping.",

  "description": "Generalized public-governed lithic artifact inventories for the Kansas Frontier Matrix.",
  "_comment_description": "Human-readable explanation of the Collection scope.",

  "license": "CC-BY-4.0",
  "_comment_license": "License must be compatible with all child Items.",

  "extent": {
    "spatial": {
      "bbox": [[-102.1, 37.0, -94.6, 40.1]]
    },
    "_comment_extent_spatial": "Generalized spatial coverage for all lithic Items.",

    "temporal": {
      "interval": [["1200-01-01T00:00:00Z", "1500-01-01T00:00:00Z"]]
    },
    "_comment_extent_temporal": "Time interval spanning all lithic cultural phases represented."
  },

  "links": [],
  "_comment_links": "May be populated with child Item links and root catalog links when exposed via STAC API.",

  "kfm:material_class": "lithic",
  "_comment_kfm_material_class": "Controlled vocabulary identifying the material class.",

  "kfm:domain": "archaeology-artifact-inventories",
  "_comment_kfm_domain": "Domain identifier shared by all artifact inventories.",

  "kfm:review_cycle": "Biannual",
  "_comment_kfm_review_cycle": "Used by governance tooling for periodic review scheduling.",

  "care:sensitivity": "general",
  "_comment_care_sensitivity": "Collection-level sensitivity; child Items may be generalized.",

  "care:review": "faircare",
  "_comment_care_review": "Indicates review through FAIR+CARE structures.",

  "care:notes": "All lithic data is generalized via H3 and reviewed for cultural safety.",
  "_comment_care_notes": "Summary of cultural safety measures for this Collection."
}
~~~

---

## 🧱 Annotated STAC Collection Example (Ceramics)

~~~json
{
  "stac_version": "1.0.0",
  "_comment_stac_version": "Required core field from STAC 1.0.",

  "type": "Collection",
  "_comment_type": "This document groups ceramic inventories as a Collection.",

  "id": "ceramics",
  "_comment_id": "Semantic grouping identifier for all public-governed ceramic datasets.",

  "description": "Ceramic artifact datasets for Kansas archaeological phases, with motifs generalized for cultural safety.",
  "_comment_description": "Explains both scope and treatment of potentially sensitive motif information.",

  "license": "CC-BY-4.0",
  "_comment_license": "SPDX license code used across KFM artifact datasets.",

  "extent": {
    "spatial": {
      "bbox": [[-101.9, 37.0, -94.9, 40.0]]
    },
    "_comment_extent_spatial": "Generalized extent for all ceramic inventories in this Collection.",

    "temporal": {
      "interval": [["1000-01-01T00:00:00Z", "1800-01-01T00:00:00Z"]]
    },
    "_comment_extent_temporal": "Covers the cultural phases represented in the ceramic datasets."
  },

  "links": [],
  "_comment_links": "For STAC API exposure, populate with links to Items and root catalog entries.",

  "kfm:material_class": "ceramic",
  "_comment_kfm_material_class": "Controlled class for ceramics.",

  "kfm:domain": "archaeology-artifact-inventories",
  "_comment_kfm_domain": "Shared domain identifier for artifact inventories.",

  "kfm:review_cycle": "Biannual",
  "_comment_kfm_review_cycle": "Ensures regular governance checks of Collections and Items.",

  "care:sensitivity": "generalized",
  "_comment_care_sensitivity": "Indicates generalized treatment of motif and context data.",

  "care:review": "faircare",
  "_comment_care_review": "Review conducted by FAIR+CARE processes.",

  "care:notes": "Motif categories are generalized and filtered to remove culturally restricted symbolism.",
  "_comment_care_notes": "Documents high-level cultural safety handling for ceramic inventories."
}
~~~

---

## 📚 Field Guide

See `field_guide.md` in this directory for:

- Definitions of STAC core fields used in examples  
- Detailed descriptions of KFM archaeology fields (`kfm:*`)  
- CARE field semantics and allowed values (`care:*`)  
- DCAT and PROV-O crosswalk notes  
- Common CI validation failure modes and how to avoid them  

The field guide and this README are intended to be used together.

---

## 🧪 Contributor Workflow for Annotated Examples

1. Review annotated examples in this directory for the relevant material class.  
2. Use the **non-annotated** templates from `../../..` (collections/templates, etc.) to create real STAC documents.  
3. Populate fields following:
   - This README  
   - `field_guide.md`  
   - KFM archaeology and CARE standards.  
4. Validate against:
   - STAC Item and Collection schemas  
   - KFM archaeology extension schemas  
   - CARE sensitivity extension schemas  
5. Confirm:
   - Spatial generalization (no site-level exposure)  
   - Correct licensing (CC0 or CC-BY only for public-governed artifacts)  
   - CARE and sovereignty metadata aligned with governance decisions  
6. Run the STAC validation CI workflow (for example, `artifact-stac-validate.yml`) before submitting a PR.

---

## 🕰 Version History

| Version   | Date       | Author                               | Summary                                                                 |
|-----------|------------|--------------------------------------|-------------------------------------------------------------------------|
| v11.2.3   | 2025-12-02 | Archaeology WG · Metadata Subcommittee | Aligned with KFM-MDP v11.2.2; added energy/carbon schemas; clarified CARE/sovereignty notes and workflow guidance. |
| v10.4.0   | 2025-11-17 | Archaeology WG · FAIR+CARE Council   | Added annotated STAC example library with commentary, field guide crosswalks, and schema notes. |
| v10.0.0   | 2025-11-10 | Artifact Metadata Team               | Initial annotated example placeholders.                                |

---

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
FAIR+CARE Certified · Sovereignty-Governed  
KFM-MDP v11.2.2 · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to STAC Examples](../README.md)