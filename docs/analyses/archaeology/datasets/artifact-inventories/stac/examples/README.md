---
title: "📝 Kansas Frontier Matrix — Artifact Inventory STAC Examples (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/artifact-inventories/stac/examples/README.md"
description: "Example STAC 1.0 Items and Collections for KFM v11 artifact inventories, demonstrating required KFM, CARE, and provenance fields."
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Archaeology Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_uuid: "urn:kfm:doc:archaeology-artifact-stac-examples-v11.2.3"
doc_kind: "STAC Examples"
intent: "artifact-inventory-stac-examples"
semantic_document_id: "kfm-doc-archaeology-artifact-stac-examples-v11.2.3"
category: "Analyses · Archaeology · STAC Examples"

sbom_ref: "../../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/archaeology-artifact-stac-examples-v1.json"
energy_schema: "../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../schemas/telemetry/carbon-gco2e-v1.json"

governance_ref: "../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

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

data_steward: "Archaeology Working Group · FAIR+CARE Council"
provenance_chain:
  - "docs/analyses/archaeology/datasets/artifact-inventories/stac/examples/README.md@v10.4.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true
---

# 📝 Kansas Frontier Matrix — Artifact Inventory STAC Examples (v11)

`docs/analyses/archaeology/datasets/artifact-inventories/stac/examples/README.md`

**Purpose**  
Provide **validated STAC examples** for artifact inventory datasets in the Kansas Frontier Matrix (KFM).  
These examples demonstrate:

- Required STAC 1.0 structure  
- KFM archaeology extension fields (`kfm:*`)  
- CARE cultural safety metadata (`care:*`)  
- Provenance references to PROV-O files  
- Alignment with DCAT and knowledge-graph usage  

All examples are **generalized** and **culturally safe** and are intended as starting points for contributors.

---

## 📘 Overview

This directory contains examples for:

- Minimal STAC Items  
- Annotated STAC Items  
- Minimal STAC Collections  
- Annotated STAC Collections  

Each example illustrates:

- Generalized spatial coverage (H3-derived extents)  
- Cultural-phase metadata (`kfm:phase`)  
- CARE sensitivity and review metadata (`care:*`)  
- Links to inventories, metadata, and provenance directories in the archaeology dataset tree  

Sensitive or sovereignty-restricted examples are **not** allowed here.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/artifact-inventories/stac/examples/
├── 📄 README.md                          # This file (examples index)
├── 📄 item_example_flint_lithics.json    # Minimal lithics Item example
├── 📄 item_example_prairie_ceramics.json # Minimal ceramics Item example
├── 📄 collection_example_lithics.json    # Minimal lithics Collection example
├── 📄 collection_example_ceramics.json   # Minimal ceramics Collection example
└── 📂 annotated/                         # Fully annotated versions of each example
~~~

This layout is **normative** for artifact-inventory STAC examples.

---

## 🧱 Example: Minimal STAC Item (Lithics)

~~~json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "flint-hills-lithics-v11",
  "bbox": [-101.2, 37.5, -95.4, 40.1],
  "geometry": {
    "type": "MultiPoint",
    "coordinates": [
      /* H3-generalized coordinates only */
    ]
  },
  "properties": {
    "kfm:domain": "archaeology-artifact-inventories",
    "kfm:phase": "Late Prehistoric",
    "kfm:generalization": "H3-r7",
    "care:sensitivity": "generalized",
    "care:sovereignty": "protected",
    "kfm:provenance": "../provenance/flint-hills-lithics-v11.json",
    "dct:license": "CC-BY-4.0",
    "datetime": null
  },
  "assets": {
    "data": {
      "href": "../inventories/flint-hills-lithics-v11.csv",
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

  "id": "prairie-ceramics-v11",
  "_comment_id": "Unique ID for this ceramics inventory version.",

  "bbox": [-101.9, 37.2, -95.9, 40.2],
  "_comment_bbox": "Generalized bounding box derived from H3 footprints (no site-level precision).",

  "geometry": {
    "type": "MultiPoint",
    "coordinates": [
      /* generalized coordinates only */
    ]
  },
  "_comment_geometry": "Coordinates must be generalized; exact provenience is prohibited.",

  "properties": {
    "kfm:domain": "archaeology-artifact-inventories",
    "_comment_domain": "Aligns with KFM archaeology artifact domain.",

    "kfm:phase": "Middle Ceramic",
    "_comment_phase": "Cultural-phase classification at appropriate resolution.",

    "kfm:generalization": "H3-r7",
    "_comment_generalization": "Indicates spatial generalization level.",

    "care:sensitivity": "generalized",
    "_comment_sensitivity": "CARE sensitivity level after redaction/generalization.",

    "care:sovereignty": "protected",
    "_comment_sovereignty": "Indicates that sovereignty-governed rules apply.",

    "kfm:provenance": "../provenance/prairie-ceramics-v11.json",
    "_comment_provenance": "Path to PROV-O lineage bundle for this inventory.",

    "dct:license": "CC-BY-4.0",
    "_comment_license": "SPDX license identifier.",

    "datetime": null
  },

  "assets": {
    "data": {
      "href": "../inventories/prairie-ceramics-v11.csv",
      "type": "text/csv",
      "roles": ["data"]
    }
  },
  "_comment_assets": "Each Item must expose at least one primary data asset."
}
~~~

---

## 🧱 Example: Minimal STAC Collection (Lithics)

~~~json
{
  "stac_version": "1.0.0",
  "type": "Collection",
  "id": "lithics",
  "description": "Collection of public-governed lithic artifact inventories for the Kansas Frontier.",
  "license": "CC-BY-4.0",
  "extent": {
    "spatial": {
      "bbox": [[-102.1, 37.0, -94.6, 40.1]]
    },
    "temporal": {
      "interval": [["1200-01-01T00:00:00Z", "1500-01-01T00:00:00Z"]]
    }
  },
  "links": [],
  "kfm:material_class": "lithic",
  "kfm:domain": "archaeology-artifact-inventories",
  "kfm:review_cycle": "Biannual",
  "care:sensitivity": "general",
  "care:notes": "All lithic inventories generalized via H3 and reviewed for cultural safety.",
  "care:review": "faircare"
}
~~~

---

## 🧱 Example: Annotated STAC Collection (Ceramics)

~~~json
{
  "stac_version": "1.0.0",
  "type": "Collection",

  "id": "ceramics",
  "_comment_id": "Semantic grouping for all public-governed ceramic inventories.",

  "description": "Ceramic artifact datasets for Kansas archaeological phases, with motifs generalized for cultural safety.",
  "_comment_description": "Human-readable summary describing scope and treatment of motifs.",

  "license": "CC-BY-4.0",
  "_comment_license": "Collection-level license must be compatible with all child Items.",

  "extent": {
    "spatial": {
      "bbox": [[-101.9, 37.0, -94.9, 40.0]]
    },
    "temporal": {
      "interval": [["1000-01-01T00:00:00Z", "1800-01-01T00:00:00Z"]]
    }
  },
  "_comment_extent": "Combined spatial and temporal coverage of all ceramic inventories in the Collection.",

  "links": [],
  "_comment_links": "Links to child Items, root artifact Collection, and related resources when integrated into a larger catalog.",

  "kfm:material_class": "ceramic",
  "_comment_material_class": "KFM-controlled value for material class.",

  "kfm:domain": "archaeology-artifact-inventories",
  "_comment_domain": "Stable identifier for the artifact-inventories domain.",

  "kfm:review_cycle": "Biannual",
  "_comment_review_cycle": "Used by governance systems for scheduled re-review.",

  "care:sensitivity": "generalized",
  "_comment_sensitivity": "Motif and design information can be sensitive; generalized patterns only.",

  "care:notes": "Motif categories filtered and generalized to remove culturally restricted symbolism.",
  "_comment_notes": "Documents CARE measures taken for this Collection.",

  "care:review": "faircare",
  "_comment_review": "Indicates review path via FAIR+CARE governance processes."
}
~~~

---

## 🧪 Validation Guidance for Contributors

Before submitting new STAC Items or Collections based on these examples:

1. **Schema validation**  
   - Validate against STAC 1.0 core schemas.  
   - Validate against KFM archaeology extensions and CARE extensions.  

2. **Spatial generalization**  
   - Confirm all coordinates are generalized (H3-derived or equivalently generalized).  
   - Ensure no site-precise locations or sensitive geometries are exposed.  

3. **Licensing**  
   - Confirm datasets are PD, CC0, or CC-BY only for public-governed inventories.  

4. **CARE and sovereignty**  
   - Set `care:sensitivity`, `care:review`, and `care:notes` according to governance decisions.  
   - Confirm alignment with the sovereignty policy referenced in front matter.  

5. **Link integrity**  
   - Ensure `assets.data.href` paths resolve to files in `../inventories/`.  
   - Ensure `kfm:provenance` paths resolve to PROV-O bundles in `../provenance/`.  
   - Ensure Collections link appropriately to child Items and root Collections.  

6. **CI workflow**  
   - Run the repository STAC validation workflow (for example: `.github/workflows/artifact-stac-validate.yml`) before opening a PR.

---

## 🕰 Version History

| Version   | Date       | Author                           | Summary                                                                 |
|-----------|------------|----------------------------------|-------------------------------------------------------------------------|
| v11.2.3   | 2025-12-02 | Archaeology WG · FAIR+CARE Council | Aligned with KFM-MDP v11.2.2; updated domain string; added energy/carbon schemas and governance notes. |
| v10.4.0   | 2025-11-17 | Archaeology WG · FAIR+CARE Council | Added artifact STAC examples; included annotated guidance and FAIR+CARE metadata rules. |
| v10.0.0   | 2025-11-10 | Artifact Metadata Team           | Initial placeholder example structure.                                  |

---

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
FAIR+CARE Certified · Sovereignty-Governed  
KFM-MDP v11.2.2 · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Artifact STAC Catalog](../README.md)