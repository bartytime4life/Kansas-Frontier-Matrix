---
title: "📝 Kansas Frontier Matrix — Artifact Inventory STAC Examples (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/artifact-inventories/stac/examples/README.md"
version: "v10.4.0"
last_updated: "2025-11-17"
review_cycle: "Biannual · Archaeology Working Group · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/archaeology-artifact-stac-examples-v1.json"
governance_ref: "../../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "STAC Examples"
intent: "artifact-inventory-stac-examples"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 📝 **Kansas Frontier Matrix — Artifact Inventory STAC Examples**  
`docs/analyses/archaeology/datasets/artifact-inventories/stac/examples/README.md`

**Purpose:**  
Provide **validated, annotated STAC examples** for artifact inventory datasets in the Kansas Frontier Matrix (KFM).  
These examples illustrate the required structure, metadata fields, CARE sensitivity tags, provenance references, and KFM archaeology extensions needed for full compliance with **STAC 1.0**, **DCAT 3.0**, **PROV-O**, **CIDOC-CRM**, **GeoSPARQL**, and **MCP-DL v6.3**.

These examples serve as templates for contributors creating new inventory datasets.

</div>

---

## 📘 Overview

This directory contains examples for:

- Full STAC Items  
- Full STAC Collections  
- Annotated field-by-field guides  
- Minimal working examples  
- Multi-file linked examples (Item + Collection + Provenance + DCAT)

All examples use **generalized**, desensitized artifact datasets.

Sensitive or restricted examples are forbidden.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/artifact-inventories/stac/examples/
├── README.md                      # This file
├── item_example_flint_lithics.json
├── item_example_prairie_ceramics.json
├── collection_example_lithics.json
├── collection_example_ceramics.json
└── annotated/                    # Fully annotated versions of each example
~~~

---

## 🧱 Example: Minimal STAC Item (Lithics)

~~~json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "flint-hills-lithics-v1",
  "bbox": [-101.2, 37.5, -95.4, 40.1],
  "geometry": {
    "type": "MultiPoint",
    "coordinates": [[/* generalized */]]
  },
  "properties": {
    "kfm:phase": "Late Prehistoric",
    "care:sensitivity": "generalized",
    "kfm:provenance": "../provenance/flint-hills-lithics-v1.json"
  },
  "assets": {
    "data": {
      "href": "../inventories/flint-hills-lithics-v1.csv",
      "type": "text/csv",
      "roles": ["data"]
    }
  }
}
~~~

---

## 🧱 Example: Annotated STAC Item (Ceramics)

~~~json
{
  "stac_version": "1.0.0",
  "type": "Feature",

  "id": "prairie-ceramics-v1",
  "_comment_id": "Unique ID for dataset versioning",

  "bbox": [-101.9, 37.2, -95.9, 40.2],
  "_comment_bbox": "Generalized bounding box (H3-derived)",

  "geometry": {
    "type": "MultiPoint",
    "coordinates": [[/* generalized coordinates */]]
  },
  "_comment_geometry": "Precise provenience prohibited — all coordinates must be generalized",

  "properties": {
    "kfm:phase": "Middle Ceramic",
    "_comment_phase": "Cultural-phase classification",

    "care:sensitivity": "generalized",
    "_comment_sensitivity": "CARE sensitivity level",

    "kfm:provenance": "../provenance/prairie-ceramics-v1.json",
    "_comment_provenance": "PROV-O lineage file"
  },

  "assets": {
    "data": {
      "href": "../inventories/prairie-ceramics-v1.csv",
      "type": "text/csv",
      "roles": ["data"]
    }
  },

  "_comment_assets": "Each STAC Item must include at least one asset"
}
~~~

---

## 🧱 Example: Minimal STAC Collection (Lithics)

~~~json
{
  "stac_version": "1.0.0",
  "type": "Collection",
  "id": "lithics-collection",
  "description": "Collection of public-domain lithic artifact inventories for the Kansas Frontier.",
  "license": "CC-BY-4.0",

  "extent": {
    "spatial": { "bbox": [[-102.1, 37.0, -94.6, 40.1]] },
    "temporal": { "interval": [["1200-01-01T00:00:00Z", "1500-01-01T00:00:00Z"]] }
  },

  "links": [],

  "kfm:material_class": "lithic",
  "kfm:domain": "archaeology:artifact-inventories",
  "kfm:review_cycle": "Biannual",

  "care:sensitivity": "general",
  "care:notes": "All lithic data generalized via H3.",
  "care:review": "faircare"
}
~~~

---

## 🧱 Example: Annotated STAC Collection (Ceramics)

~~~json
{
  "stac_version": "1.0.0",
  "type": "Collection",
  "id": "ceramics-collection",
  "_comment_id": "Semantic grouping for all ceramic datasets",

  "description": "Ceramic artifact datasets for Kansas archaeological phases.",
  "_comment_description": "Human-readable summary of dataset group",

  "license": "CC-BY-4.0",
  "_comment_license": "Must match dataset-level licenses",

  "extent": {
    "spatial": { "bbox": [[-101.9, 37.0, -94.9, 40.0]] },
    "temporal": { "interval": [["1000-01-01T00:00:00Z", "1800-01-01T00:00:00Z"]] }
  },
  "_comment_extent": "Combined extent of all ceramic inventories",

  "links": [],

  "kfm:material_class": "ceramic",
  "kfm:domain": "archaeology:artifact-inventories",
  "kfm:review_cycle": "Biannual",

  "care:sensitivity": "general",
  "care:notes": "Motif data filtered for cultural safety.",
  "care:review": "faircare"
}
~~~

---

## 🧪 Validation Guidance for Contributors

Before submitting new STAC Items or Collections:

1. Validate against provided **STAC schemas**.  
2. Ensure all coordinates are **generalized (H3-level)**.  
3. Confirm dataset licensing (PD/CC-BY only).  
4. Verify CARE review status.  
5. Confirm all assets resolve correctly.  
6. Include **provenance** and **metadata** references.  
7. Confirm compatibility with:
   - `inventories/`  
   - `metadata/`  
   - `provenance/`   
   - `../collections/`  

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v10.4.0 | 2025-11-17 | Archaeology WG · FAIR+CARE Council | Added full suite of artifact STAC examples; included annotated guidance and FAIR+CARE metadata rules |
| v10.0.0 | 2025-11-10 | Artifact Metadata Team | Initial placeholder example structure |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE Certified · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[⬅ Back to Artifact STAC Catalog](../README.md)

</div>