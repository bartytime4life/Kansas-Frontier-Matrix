---
title: "📄 Kansas Frontier Matrix — Artifact Inventory STAC Items (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/artifact-inventories/stac/items/README.md"
description: "Canonical index and requirements for STAC 1.0 Items describing KFM v11 artifact inventory datasets."
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Archaeology Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_uuid: "urn:kfm:doc:archaeology-artifact-stac-items-v11.2.3"
doc_kind: "STAC Items Index"
intent: "artifact-inventory-stac-items"
semantic_document_id: "kfm-doc-archaeology-artifact-stac-items-v11.2.3"
category: "Analyses · Archaeology · STAC Items"

sbom_ref: "../../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/archaeology-artifact-stac-items-v1.json"
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
  - "docs/analyses/archaeology/datasets/artifact-inventories/stac/items/README.md@v10.4.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true
---

# 📄 Kansas Frontier Matrix — Artifact Inventory STAC Items (v11)

`docs/analyses/archaeology/datasets/artifact-inventories/stac/items/README.md`

**Purpose**  
Provide the **canonical index** and **governed requirements** for all STAC Items that describe artifact inventory datasets in the Kansas Frontier Matrix (KFM).

Each STAC Item represents machine-readable metadata for a single, cleaned, culturally reviewed inventory stored under:

- `inventories/`  
- `metadata/`  
- `provenance/`  

All Items must comply with:

- STAC 1.0  
- KFM archaeology extensions (`kfm:*`)  
- CARE cultural safety metadata (`care:*`)  
- DCAT crosswalk expectations  
- PROV-O provenance linkage  
- FAIR+CARE and sovereignty rules

---

## 📘 Overview

STAC Items in this directory:

- Provide spatial, temporal, cultural, and provenance metadata for artifact inventories.  
- Enable machine discovery via STAC crawlers and KFM’s metadata engine.  
- Govern dataset ingestion into Neo4j, Story Nodes, and Focus Mode pipelines.  
- Enforce cultural sensitivity and sovereignty through `care:*` metadata.  
- Support reproducibility and traceable lineage via `kfm:provenance`.

Every STAC Item **must** link to:

- Its dataset file in `../inventories/` (via `assets.data.href`).  
- Its metadata / DCAT description in `../metadata/` (where present).  
- Its provenance file in `../provenance/`.  
- Its parent STAC Collection in `../collections/`.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/artifact-inventories/stac/items/
├── 📄 README.md                         # This file (STAC Items index)
├── 📄 flint-hills-lithics-v11.json      # Lithic artifact STAC Item
├── 📄 prairie-ceramics-v11.json         # Ceramic artifact STAC Item
├── 📄 contact-era-metals-v11.json       # Protohistoric metal artifacts (governed)
├── 📄 fauna-open-v11.json               # Public-domain faunal STAC Item
└── 📂 templates/                        # STAC Item templates for new datasets
~~~

This layout is **normative** for artifact-inventory STAC Items.

---

## 🧭 Requirements for All STAC Items

Every STAC Item in this directory must satisfy all of the following.

### STAC Core Fields

| Field                         | Requirement / Notes                                           |
|-------------------------------|---------------------------------------------------------------|
| `id`                          | Stable identifier; must match JSON filename (without `.json`) |
| `stac_version`                | `"1.0.0"`                                                     |
| `type`                        | `"Feature"`                                                   |
| `bbox`                        | Generalized bounding box (H3-derived; no site precision)     |
| `geometry`                    | `MultiPoint`, `Polygon`, or `MultiPolygon` (generalized)     |
| `properties.datetime`         | `null` or representative timestamp                           |
| `assets.data.href`            | Relative path to inventory file in `../inventories/`         |
| `assets.data.type`           | Correct MIME type (for example, `"text/csv"`)                |
| `assets.data.roles`          | Must include `"data"`                                        |
| `links[rel="collection"]`     | Must point to parent Collection JSON in `../collections/`    |

---

### KFM Archaeology Extension (`kfm:*`)

| Field                | Description / Requirement                                               |
|----------------------|-------------------------------------------------------------------------|
| `kfm:domain`         | Must be `"archaeology-artifact-inventories"`                           |
| `kfm:phase`          | Cultural-phase label (for example, `Late Prehistoric`)                 |
| `kfm:material_class` | `"lithic"`, `"ceramic"`, `"metal"`, or `"faunal"`                      |
| `kfm:generalization` | Spatial generalization level (for example, `"H3-r7"`)                  |
| `kfm:provenance`     | Relative path to PROV-O lineage JSON in `../provenance/`               |
| `kfm:datatype`       | When used, should be `"artifact-inventory"`                            |

---

### CARE Sensitivity Extension (`care:*`)

| Field              | Allowed Values / Notes                                                     |
|--------------------|----------------------------------------------------------------------------|
| `care:sensitivity` | `general`, `generalized`, or `restricted-generalized` (no `restricted`)   |
| `care:review`      | `"faircare"`, `"tribal"`, or `"none-required"`                            |
| `care:notes`       | Required for ceramics, metals, and any dataset with motif or contact-era context |
| `care:sovereignty` | Indicates sovereignty governance (for example, `"protected"`)             |

Spatial precision and visibility must be consistent with `care:sensitivity` and governance rules.

---

### Required Extensions

Each Item must be valid against STAC 1.0 plus the following extensions (where implemented):

- Projection (`proj`)  
- Versioning (`version`)  
- Checksum (`checksum`)  
- Scientific (`sci`) where scientific metadata exists  
- KFM archaeology (`kfm`)  
- CARE cultural safety (`care`)

---

## 📄 Example STAC Item — Lithics

~~~json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "flint-hills-lithics-v11",
  "bbox": [-101.2, 37.5, -95.4, 40.1],
  "geometry": {
    "type": "MultiPoint",
    "coordinates": [
      /* generalized coordinates only */
    ]
  },
  "properties": {
    "kfm:domain": "archaeology-artifact-inventories",
    "kfm:phase": "Late Prehistoric",
    "kfm:material_class": "lithic",
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

## 📄 Example STAC Item — Ceramics

~~~json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "prairie-ceramics-v11",
  "bbox": [-101.9, 37.2, -95.9, 40.2],
  "geometry": {
    "type": "MultiPoint",
    "coordinates": [
      /* generalized coordinates only */
    ]
  },
  "properties": {
    "kfm:domain": "archaeology-artifact-inventories",
    "kfm:phase": "Middle Ceramic",
    "kfm:material_class": "ceramic",
    "kfm:generalization": "H3-r7",
    "care:sensitivity": "generalized",
    "care:sovereignty": "protected",
    "care:notes": "Motif categories filtered and generalized for cultural safety.",
    "kfm:provenance": "../provenance/prairie-ceramics-v11.json",
    "dct:license": "CC-BY-4.0",
    "datetime": null
  },
  "assets": {
    "data": {
      "href": "../inventories/prairie-ceramics-v11.csv",
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

## 🧪 Validation Requirements

All STAC Items in this directory must pass:

- STAC core JSON schema validation (Items + extensions).  
- KFM archaeology STAC extension checks (`kfm:*` fields).  
- CARE sensitivity validation (values and consistency with generalization).  
- Checksum verification where `checksum` extension is used.  
- Crosswalk checks that ensure:
  - Inventory file exists in `../inventories/`.  
  - Provenance file exists in `../provenance/`.  
  - Collection JSON exists in `../collections/`.  
  - DCAT / metadata alignment where applicable.

Validation is enforced via CI workflows such as:

- `.github/workflows/artifact-stac-validate.yml`  

---

## 📊 STAC Item Index (Illustrative)

| STAC Item                      | Category | Sensitivity   | Last Review | Status     |
|--------------------------------|----------|--------------|-------------|------------|
| `flint-hills-lithics-v11.json` | Lithics  | generalized  | 2025-11     | 🟢 Active  |
| `prairie-ceramics-v11.json`    | Ceramics | generalized  | 2025-11     | 🟢 Active  |
| `contact-era-metals-v11.json`  | Metals   | generalized  | 2025-09     | 🟡 Review  |
| `fauna-open-v11.json`          | Faunal   | general      | 2025-11     | 🟢 Active  |

The authoritative index of Items lives in this directory plus release manifests; this table is descriptive.

---

## 🕰 Version History

| Version   | Date       | Author                           | Summary                                                                 |
|-----------|------------|----------------------------------|-------------------------------------------------------------------------|
| v11.2.3   | 2025-12-02 | Archaeology WG · FAIR+CARE Council | Updated to KFM v11.2.3; added governance metadata, energy/carbon schemas, and clarified CARE requirements. |
| v10.4.0   | 2025-11-17 | Archaeology WG · FAIR+CARE Council | Added STAC Items index, examples, and validation rules with CARE extensions. |
| v10.0.0   | 2025-11-10 | Artifact Metadata Team           | Initial STAC Item directory creation.                                  |

---

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
FAIR+CARE Certified · Sovereignty-Governed  
KFM-MDP v11.2.2 · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to STAC Catalog](../README.md)