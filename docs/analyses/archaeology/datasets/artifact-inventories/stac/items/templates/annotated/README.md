---
title: "📄📝 Kansas Frontier Matrix — Annotated STAC Item Templates for Artifact Inventories (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/artifact-inventories/stac/items/templates/annotated/README.md"
version: "v10.4.0"
last_updated: "2025-11-17"
review_cycle: "Biannual · Archaeology Working Group · FAIR+CARE Council · Metadata Standards Subcommittee"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../schemas/telemetry/archaeology-artifact-stac-item-templates-annotated-v1.json"
governance_ref: "../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Annotated Templates"
intent: "artifact-inventory-stac-item-templates-annotated"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 📄📝 **Kansas Frontier Matrix — Annotated STAC Item Templates (Artifact Inventories)**  
`docs/analyses/archaeology/datasets/artifact-inventories/stac/items/templates/annotated/README.md`

**Purpose:**  
Provide **line-by-line annotated STAC Item templates** for all artifact inventory types within the Kansas Frontier Matrix (KFM).  
These annotated templates teach contributors how to construct fully valid, culturally safe, machine-readable STAC Items that integrate cleanly with:

- STAC 1.0 Core Specification  
- DCAT 3.0  
- PROV-O Provenance  
- KFM Archaeology Extension (`kfm:*`)  
- CARE Cultural Safety Extension (`care:*`)  
- Neo4j Graph ingestion  
- Focus Mode v2 narrative engines  
- MCP-DL v6.3 Documentation-First Rules  
- KFM-MDP v10.4 Markdown Protocol  

These annotated examples provide authoritative guidance for writing STAC Items across lithic, ceramic, metal, and faunal domains.

</div>

---

# 📘 Overview

Annotated templates in this directory describe:

- **Lithic STAC Item**  
- **Ceramic STAC Item**  
- **Metal / Protohistoric STAC Item**  
- **Faunal STAC Item (PD-only)**  

Each annotated example includes:

- Field-level explanations  
- Allowed values and constraints  
- CARE cultural safety logic  
- DCAT/STAC crosswalk notes  
- Generalization rules (H3 levels 5–7)  
- Graph + Story Node integration notes  
- Validation requirements for CI pipelines  

All examples use synthetic, non-sensitive placeholder data.

---

# 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/artifact-inventories/stac/items/templates/annotated/
├── README.md                              # This file
├── item_lithics_annotated.json            # Annotated lithic STAC Item example
├── item_ceramics_annotated.json           # Annotated ceramic STAC Item example
├── item_metals_annotated.json             # Annotated metal/protohistoric STAC Item example
├── item_faunal_annotated.json             # Annotated faunal (PD-only) STAC Item example
└── field_guide.md                         # Complete field reference for STAC/KFM/CARE
~~~

---

# 🧱 Annotated STAC Item Template — Lithics

~~~json
{
  "stac_version": "1.0.0",
  "_comment_stac_version": "STAC version is always 1.0.0 for KFM archaeology.",

  "type": "Feature",
  "_comment_type": "All artifact STAC Items must use type=Feature.",

  "id": "lithics-TEMPLATE-ID",
  "_comment_id": "Must be lowercase, hyphenated, versioned (e.g., flint-hills-lithics-v1).",

  "bbox": [-102.1, 37.0, -94.6, 40.1],
  "_comment_bbox": "Generalized bounding box covering the dataset extent. Never include true provenience.",

  "geometry": {
    "type": "MultiPoint",
    "_comment_geometry_type": "MultiPoint required for artifact inventories; no exact points permitted.",
    "coordinates": [[ /* H3-generalized coordinates only */ ]]
  },

  "properties": {
    "kfm:phase": "PHASE-HERE",
    "_comment_phase": "Cultural-phase of dataset; used across Story Nodes + Focus Mode.",

    "care:sensitivity": "generalized",
    "_comment_sensitivity": "Artifact inventories must be 'generalized' unless PD-only (faunal).",

    "care:notes": "Explanation of generalization strategy (H3 5–7).",
    "_comment_care_notes": "Important for cultural review transparency.",

    "kfm:material_class": "lithic",
    "_comment_material_class": "Controlled vocabulary from archaeology extension schema.",

    "kfm:datatype": "artifact-inventory",
    "_comment_datatype": "Constant for all artifact inventory Items.",

    "kfm:source": "INSTITUTION",
    "_comment_source": "Provenance institution name.",

    "kfm:provenance": "../../provenance/FILE.json",
    "_comment_provenance": "Links to PROV-O lineage JSON."
  },

  "assets": {
    "data": {
      "href": "../../inventories/FILE.csv",
      "_comment_data_href": "Relative path to inventory data table.",
      "type": "text/csv",
      "_comment_data_type": "Correct MIME type required.",
      "roles": ["data"]
    }
  },

  "links": [
    {
      "rel": "collection",
      "href": "../collections/lithics.json",
      "_comment_collection_link": "Every STAC Item must link back to its STAC Collection."
    }
  ]
}
~~~

---

# 🧱 Annotated STAC Item Template — Ceramics

~~~json
{
  "stac_version": "1.0.0",

  "type": "Feature",

  "id": "ceramics-TEMPLATE-ID",

  "bbox": [-102.1, 37.0, -94.9, 40.0],

  "geometry": {
    "type": "MultiPoint",
    "coordinates": [[ /* generalized */ ]]
  },

  "properties": {
    "kfm:phase": "PHASE-HERE",

    "care:sensitivity": "generalized",
    "_comment_sensitivity": "Ceramic motifs sometimes require extra filtering.",

    "care:notes": "Motif categories generalized to avoid cultural sensitivity.",
    "_comment_notes": "Document any filtering or motif masking done for cultural safety.",

    "kfm:material_class": "ceramic",
    "kfm:datatype": "artifact-inventory",
    "kfm:source": "INSTITUTION",
    "kfm:provenance": "../../provenance/FILE.json"
  },

  "assets": {
    "data": {
      "href": "../../inventories/FILE.csv",
      "type": "text/csv",
      "roles": ["data"]
    }
  },

  "links": [
    { "rel": "collection", "href": "../collections/ceramics.json" }
  ]
}
~~~

---

# 🧱 Annotated STAC Item Template — Metals / Protohistoric

~~~json
{
  "stac_version": "1.0.0",
  "type": "Feature",

  "id": "metals-TEMPLATE-ID",

  "bbox": [-102.1, 37.0, -94.6, 40.1],

  "geometry": {
    "type": "MultiPoint",
    "coordinates": [[ /* generalized */ ]]
  },

  "properties": {
    "kfm:phase": "PHASE-HERE",

    "care:sensitivity": "generalized",
    "care:review": "tribal",
    "_comment_review": "Contact-era metal artifacts require tribal review.",

    "care:notes": "Cultural implications reviewed by tribal representatives.",
    "_comment_notes": "Required for all contact-era materials.",

    "kfm:material_class": "metal",
    "kfm:datatype": "artifact-inventory",
    "kfm:source": "INSTITUTION",
    "kfm:provenance": "../../provenance/FILE.json"
  },

  "assets": {
    "data": {
      "href": "../../inventories/FILE.csv",
      "type": "text/csv",
      "roles": ["data"]
    }
  },

  "links": [
    { "rel": "collection", "href": "../collections/metals.json" }
  ]
}
~~~

---

# 🧱 Annotated STAC Item Template — Faunal (PD-only)

~~~json
{
  "stac_version": "1.0.0",
  "type": "Feature",

  "id": "faunal-TEMPLATE-ID",

  "bbox": [-102.1, 37.0, -94.6, 40.1],

  "geometry": {
    "type": "MultiPoint",
    "coordinates": [[ /* generalized */ ]]
  },

  "properties": {
    "kfm:phase": "PHASE-HERE",

    "care:sensitivity": "general",
    "_comment_sensitivity": "Faunal datasets must be PD-only and free of sacred species data.",

    "kfm:material_class": "faunal",
    "kfm:datatype": "artifact-inventory",
    "kfm:source": "INSTITUTION",
    "kfm:provenance": "../../provenance/FILE.json"
  },

  "assets": {
    "data": {
      "href": "../../inventories/FILE.csv",
      "type": "text/csv",
      "roles": ["data"]
    }
  },

  "links": [
    { "rel": "collection", "href": "../collections/faunal.json" }
  ]
}
~~~

---

# 📚 Field Guide Reference

A complete field-by-field reference with examples is provided in:

➡ `docs/analyses/archaeology/datasets/artifact-inventories/stac/items/templates/annotated/field_guide.md`

---

# 🧪 Validation Instructions

Every new STAC Item derived from these templates **must** pass:

1. `stac-item-schema.json`  
2. `kfm-archaeology-extension.json`  
3. `care-sensitivity-extension.json`  
4. `dcat-crosswalk.json`  
5. SHA-256 checksum generation & validation  
6. Provenance existence + accessibility check  
7. Matching inventory file under `inventories/`

CI pipeline:  
`.github/workflows/artifact-stac-validate.yml`

---

# 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v10.4.0 | 2025-11-17 | Archaeology WG · FAIR+CARE Council | Added fully annotated STAC Item templates for all artifact classes with CARE + KFM extension commentary |
| v10.0.0 | 2025-11-10 | Artifact Metadata Team | Initial placeholder annotation directory |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[⬅ Back to STAC Item Templates](../README.md)

</div>