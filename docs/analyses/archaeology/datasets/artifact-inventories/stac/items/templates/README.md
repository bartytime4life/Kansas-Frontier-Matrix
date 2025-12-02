---
title: "📄 Kansas Frontier Matrix — Artifact Inventory STAC Item Templates (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/artifact-inventories/stac/items/templates/README.md"
description: "Template library for STAC 1.0 Items describing KFM v11 artifact inventories, with KFM and CARE extensions pre-configured."
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Archaeology Working Group · FAIR+CARE Council · Metadata Standards Subcommittee"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_uuid: "urn:kfm:doc:archaeology-artifact-stac-item-templates-v11.2.3"
doc_kind: "Template Library"
intent: "artifact-stac-item-templates"
semantic_document_id: "kfm-doc-archaeology-artifact-stac-item-templates-v11.2.3"
category: "Analyses · Archaeology · STAC Items · Templates"

sbom_ref: "../../../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/archaeology-artifact-stac-item-templates-v1.json"
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
  - "docs/analyses/archaeology/datasets/artifact-inventories/stac/items/templates/README.md@v10.4.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true
---

# 📄 Kansas Frontier Matrix — Artifact Inventory STAC Item Templates (v11)

`docs/analyses/archaeology/datasets/artifact-inventories/stac/items/templates/README.md`

**Purpose**  
Provide the official **STAC Item templates** for contributing new artifact inventory datasets to the Kansas Frontier Matrix (KFM) v11.

These templates guarantee that new Items are:

- STAC 1.0–compliant  
- KFM archaeology–compatible (`kfm:*`)  
- CARE and sovereignty–aligned (`care:*`)  
- Ready for DCAT crosswalk and PROV-O linkage  
- Acceptable to KFM CI validation and governance checks  

Every new artifact inventory Item **must** be derived from one of these templates.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/artifact-inventories/stac/items/templates/
├── 📄 README.md                                   # This file (template library index)
├── 📄 template-lithic-item.json                   # Template for lithic artifact inventories
├── 📄 template-ceramic-item.json                  # Template for ceramic artifact inventories
├── 📄 template-metal-item.json                    # Template for protohistoric / metal inventories
├── 📄 template-faunal-item.json                   # Template for faunal (public-domain) inventories
└── 📂 annotated/                                  # Fully annotated versions of each template
~~~

This layout is **normative** for artifact-inventory STAC Item templates.

---

## 📘 General Instructions for Contributors

Before creating any new STAC Item:

1. **Choose the correct template** based on material class (`lithic`, `ceramic`, `metal`, `faunal`).  
2. **Copy the template** into `../` (the `items/` directory) and rename it to the final ID (for example, `flint-hills-lithics-v11.json`).  
3. Fill all required fields:
   - `id`, `bbox`, and `geometry` (generalized)  
   - `kfm:domain`, `kfm:phase`, `kfm:material_class`, `kfm:generalization`  
   - `care:sensitivity`, `care:review`, and `care:notes` (where needed)  
   - `kfm:provenance` → PROV-O file path  
   - `assets.data.href` → inventory table path  
4. Validate against schemas in `../../schemas/`.  
5. Submit to the Archaeology Working Group and FAIR+CARE governance for review.  
6. Only after approval should the Item be included in releases and catalog indices.

---

## 📦 Template: Lithic Artifact Inventory (Minimal)

~~~json
{
  "stac_version": "1.0.0",
  "type": "Feature",

  "id": "TEMPLATE-LITHICS-ID",

  "bbox": [-102.0, 37.0, -94.6, 40.1],
  "geometry": {
    "type": "MultiPoint",
    "coordinates": [
      /* H3-generalized sample coordinates */
    ]
  },

  "properties": {
    "kfm:domain": "archaeology-artifact-inventories",
    "kfm:phase": "PHASE-HERE",
    "kfm:material_class": "lithic",
    "kfm:datatype": "artifact-inventory",
    "kfm:generalization": "H3-r7",
    "kfm:source": "INSTITUTION",
    "kfm:provenance": "../provenance/FILE.json",

    "care:sensitivity": "generalized",
    "care:sovereignty": "protected",

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
      "href": "../collections/lithics.json"
    }
  ]
}
~~~

---

## 📦 Template: Ceramic Artifact Inventory (Minimal)

~~~json
{
  "stac_version": "1.0.0",
  "type": "Feature",

  "id": "TEMPLATE-CERAMICS-ID",

  "bbox": [-102.0, 37.0, -94.6, 40.1],
  "geometry": {
    "type": "MultiPoint",
    "coordinates": [
      /* generalized coordinates */
    ]
  },

  "properties": {
    "kfm:domain": "archaeology-artifact-inventories",
    "kfm:phase": "PHASE-HERE",
    "kfm:material_class": "ceramic",
    "kfm:datatype": "artifact-inventory",
    "kfm:generalization": "H3-r7",
    "kfm:source": "INSTITUTION",
    "kfm:provenance": "../provenance/FILE.json",

    "care:sensitivity": "generalized",
    "care:sovereignty": "protected",
    "care:notes": "MOTIF-SAFETY-NOTES",

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

## 📦 Template: Metal / Protohistoric Artifact Inventory (Minimal)

~~~json
{
  "stac_version": "1.0.0",
  "type": "Feature",

  "id": "TEMPLATE-METALS-ID",

  "bbox": [-102.0, 37.0, -94.6, 40.1],
  "geometry": {
    "type": "MultiPoint",
    "coordinates": [
      /* generalized coordinates */
    ]
  },

  "properties": {
    "kfm:domain": "archaeology-artifact-inventories",
    "kfm:phase": "PHASE-HERE",
    "kfm:material_class": "metal",
    "kfm:datatype": "artifact-inventory",
    "kfm:generalization": "H3-r7",
    "kfm:source": "INSTITUTION",
    "kfm:provenance": "../provenance/FILE.json",

    "care:sensitivity": "generalized",
    "care:review": "tribal",
    "care:sovereignty": "protected",
    "care:notes": "Describe cultural consultation outcomes here.",

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

## 📦 Template: Faunal Artifact Inventory (Minimal — Public-Domain Oriented)

~~~json
{
  "stac_version": "1.0.0",
  "type": "Feature",

  "id": "TEMPLATE-FAUNAL-ID",

  "bbox": [-102.0, 37.0, -94.6, 40.1],
  "geometry": {
    "type": "MultiPoint",
    "coordinates": [
      /* generalized coordinates */
    ]
  },

  "properties": {
    "kfm:domain": "archaeology-artifact-inventories",
    "kfm:phase": "PHASE-HERE",
    "kfm:material_class": "faunal",
    "kfm:datatype": "artifact-inventory",
    "kfm:generalization": "H3-r7",
    "kfm:source": "INSTITUTION",
    "kfm:provenance": "../provenance/FILE.json",

    "care:sensitivity": "general",
    "care:sovereignty": "protected",

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

## 🧪 Validation Requirements

Any STAC Item created from these templates must pass:

1. **STAC 1.0 core validation**  
   - Item schema (plus configured extensions).  
2. **KFM archaeology extension validation**  
   - Presence and correctness of `kfm:*` fields.  
3. **CARE & sovereignty validation**  
   - `care:sensitivity`, `care:review`, `care:notes` consistent with data and governance rules.  
4. **DCAT alignment** (where DCAT records exist).  
5. **Provenance linkage**  
   - `kfm:provenance` must point to a valid PROV-O file in `../provenance/`.  
6. **Generalization checks**  
   - All coordinates generalized; no site-precise geometries.  

Validation workflows include (examples):

- `.github/workflows/artifact-stac-validate.yml`  
- Additional archaeology validation docs under `docs/analyses/archaeology/validation/`.

---

## 🧠 Tips for Contributors

- Use **ISO 8601** for all timestamps where needed.  
- Default CRS is **EPSG:4326** for coordinates.  
- When in doubt about cultural safety:
  - Use `care:review = "tribal"` and document in `care:notes`.  
  - Engage FAIR+CARE and sovereignty reviewers early.  
- Keep IDs, filenames, and `kfm:provenance` stems consistent across:
  - inventory → metadata → provenance → STAC.  
- Use H3 levels **5–7** for spatial generalization and record the level in `kfm:generalization`.

---

## 🕰 Version History

| Version   | Date       | Author                               | Summary                                                                 |
|-----------|------------|--------------------------------------|-------------------------------------------------------------------------|
| v11.2.3   | 2025-12-02 | Archaeology WG · Metadata Standards Subcommittee | Updated templates for KFM v11.2.3; added domain, sovereignty, and energy/carbon telemetry references. |
| v10.4.0   | 2025-11-17 | Archaeology WG · FAIR+CARE Council   | Added artifact STAC Item template suite with cultural safety rules and validation guidance. |
| v10.0.0   | 2025-11-10 | Artifact Metadata Team               | Initial structure and placeholder templates.                            |

---

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
FAIR+CARE Certified · Sovereignty-Governed  
KFM-MDP v11.2.2 · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to STAC Items](../README.md)