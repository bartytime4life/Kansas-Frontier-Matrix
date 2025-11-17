---
title: "📝 Kansas Frontier Matrix — Annotated Artifact STAC Examples (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/artifact-inventories/stac/examples/annotated/README.md"
version: "v10.4.0"
last_updated: "2025-11-17"
review_cycle: "Biannual · Archaeology Working Group · FAIR+CARE Council · Metadata Standards Subcommittee"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/archaeology-artifact-stac-examples-annotated-v1.json"
governance_ref: "../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "STAC Example Commentary"
intent: "artifact-stac-annotated-examples"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 📝 **Kansas Frontier Matrix — Annotated Artifact STAC Examples**  
`docs/analyses/archaeology/datasets/artifact-inventories/stac/examples/annotated/README.md`

**Purpose:**  
Provide **deeply annotated**, line-by-line STAC examples for artifact inventory metadata used in the Kansas Frontier Matrix (KFM).  
These examples are designed for developers, archaeologists, data stewards, and metadata specialists who require:

- Exact field-by-field explanations  
- Schema-aligned commentary  
- CARE sensitivity guidance  
- STAC 1.0 structural rules  
- KFM archaeology extension notes  
- DCAT + PROV-O crosswalk indicators  

These annotated models serve as authoritative teaching references inside the repository.

</div>

---

## 📘 Overview

Annotated examples in this directory include:

- **Fully annotated STAC Items**  
- **Fully annotated STAC Collections**  
- Explanation of each field’s purpose & required values  
- Cultural sensitivity notes for artifact metadata  
- Crosswalks linking STAC → DCAT → PROV-O → KFM Graph  

All examples are **synthetic or generalized**, never containing real sensitive data.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/artifact-inventories/stac/examples/annotated/
├── README.md                           # This file
├── item_lithics_annotated.json         # Annotated lithic STAC Item
├── item_ceramics_annotated.json        # Annotated ceramic STAC Item
├── collection_lithics_annotated.json   # Annotated lithic STAC Collection
├── collection_ceramics_annotated.json  # Annotated ceramic STAC Collection
└── field_guide.md                      # Definitions for each STAC + CARE + KFM field
~~~

---

## 🧱 Annotated STAC Item Example (Lithics)

~~~json
{
  "stac_version": "1.0.0",
  "_comment_stac_version": "STAC version must always be 1.0.0 for KFM archaeology datasets.",

  "type": "Feature",
  "_comment_type": "All STAC Items describing datasets must use type=Feature.",

  "id": "flint-hills-lithics-v1",
  "_comment_id": "Stable versioned dataset identifier. Matches metadata + provenance + inventory file stems.",

  "bbox": [-101.2, 37.5, -95.4, 40.1],
  "_comment_bbox": "Derived from H3-level generalized geometry. No exact coordinates allowed.",

  "geometry": {
    "type": "MultiPoint",
    "coordinates": [[ /* generalized coordinates */ ]]
  },
  "_comment_geometry": "Only MultiPoint or simplified polygons; actual coordinates are generalized via H3.",

  "properties": {
    "kfm:phase": "Late Prehistoric",
    "_comment_kfm_phase": "Cultural-phase classification used throughout KFM for timelines & graph entities.",

    "care:sensitivity": "generalized",
    "_comment_care_sensitivity": "Artifact inventories must be general or generalized; never restricted.",

    "kfm:provenance": "../../provenance/flint-hills-lithics-v1.json",
    "_comment_kfm_provenance": "PROV-O lineage JSON that describes raw → processed → final dataset steps.",

    "sci:doi": "10.1234/example.lithics.dataset",
    "_comment_sci_doi": "Optional but encouraged for reproducibility."
  },

  "assets": {
    "data": {
      "href": "../../inventories/flint-hills-lithics-v1.csv",
      "_comment_href": "Path to the CSV inventory table.",

      "type": "text/csv",
      "_comment_type": "Correct MIME type is required for validation.",

      "roles": ["data"],
      "_comment_roles": "Roles array identifies how assets are used. 'data' is required for inventory files."
    }
  },

  "links": [
    {
      "rel": "collection",
      "href": "../collections/lithics.json"
    }
  ],
  "_comment_links": "STAC Item must link to its Collection."
}
~~~

---

## 🧱 Annotated STAC Collection Example (Ceramics)

~~~json
{
  "stac_version": "1.0.0",
  "_comment_stac_version": "Required STAC core spec.",

  "type": "Collection",
  "_comment_type": "All STAC Collections must use type=Collection.",

  "id": "ceramics",
  "_comment_id": "Collection identifier; must match directory + semantic grouping.",

  "description": "Generalized ceramic artifact datasets for prehistoric Kansas.",
  "_comment_description": "Human-readable summary describing the cultural dataset group.",

  "license": "CC-BY-4.0",
  "_comment_license": "Must match dataset-level licenses.",

  "extent": {
    "spatial": { "bbox": [[-101.9, 37.0, -94.9, 40.0]] },
    "_comment_extent_spatial": "Combined generalized spatial coverage for all ceramic inventories.",

    "temporal": { "interval": [["1000-01-01T00:00:00Z", "1800-01-01T00:00:00Z"]] },
    "_comment_extent_temporal": "Earliest & latest cultural-phase intervals across all ceramic datasets."
  },

  "links": [],
  "_comment_links": "Optional for internal use; STAC API would populate these.",

  "kfm:material_class": "ceramic",
  "_comment_kfm_material_class": "Controlled vocabulary defined by archaeology KFM extension.",

  "kfm:domain": "archaeology:artifact-inventories",
  "_comment_kfm_domain": "Ensures cross-domain semantic consistency.",

  "kfm:review_cycle": "Biannual",
  "_comment_kfm_review_cycle": "Must match MCP review cycles for artifact metadata.",

  "care:sensitivity": "general",
  "_comment_care_sensitivity": "Collections must default to general unless all child items are generalized or restricted-generalized.",

  "care:review": "faircare",
  "_comment_care_review": "Indicates the reviewing authority.",

  "care:notes": "Motif categories have been filtered for cultural sensitivity.",
  "_comment_care_notes": "Required explanation of any transformations applied for cultural safety."
}
~~~

---

## 📚 Field Guide (Located at `field_guide.md`)

The field guide provides:

- All **STAC core fields** with meanings  
- All **KFM archaeology extension fields** (`kfm:*`)  
- All **CARE cultural safety fields** (`care:*`)  
- **Expected value types**  
- **Validation constraints**  
- **Crosswalk examples** (STAC ↔ DCAT ↔ PROV-O ↔ Graph schema)  
- **Common failure cases** encountered in CI  

---

## 🧪 Contributor Workflow for Annotated Examples

1. Examine **annotated JSON** before creating new datasets.  
2. Use matching template from:  
   - `../../collections/templates/`  
   - `../../items/templates/`  
3. Populate fields with actual dataset metadata.  
4. Validate via:  
   - `stac-item-schema.json`  
   - `stac-collection-schema.json`  
   - `kfm-archaeology-extension.json`  
   - `care-sensitivity-extension.json`  
5. Submit dataset + STAC metadata to archaeology WG for approval.  
6. FAIR+CARE Council performs ethical + cultural review.  
7. Upon approval, add to KFM release manifest.

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v10.4.0 | 2025-11-17 | Archaeology WG · FAIR+CARE Council | Added annotated STAC example library with commentary, field guide crosswalks, and schema notes |
| v10.0.0 | 2025-11-10 | Artifact Metadata Team | Initial annotated example placeholders |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE Certified · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[⬅ Back to STAC Examples](../README.md)

</div>