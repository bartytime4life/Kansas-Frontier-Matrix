---
title: "🗂️ Kansas Frontier Matrix — Interaction Sphere STAC Items (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/stac/items/README.md"
description: "STAC 1.0 Item index and requirements for KFM v11 cultural interaction-sphere features, with KFM and CARE extensions."
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Cultural Landscape Working Group · FAIR+CARE Council · Metadata Standards Subcommittee"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_uuid: "urn:kfm:doc:archaeology-interaction-spheres-stac-items-v11.2.3"
doc_kind: "STAC Items Index"
intent: "interaction-spheres-stac-items"
semantic_document_id: "kfm-doc-archaeology-interaction-spheres-stac-items-v11.2.3"
category: "Analyses · Archaeology · Cultural Landscapes · STAC"

sbom_ref: "../../../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/archaeology-interaction-spheres-stac-items-v1.json"
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

data_steward: "Cultural Landscape Working Group · FAIR+CARE Council · Metadata Standards Subcommittee"
provenance_chain:
  - "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/stac/items/README.md@v11.0.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true
---

# 🗂️ Kansas Frontier Matrix — Interaction Sphere STAC Items (v11)

`docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/stac/items/README.md`

**Purpose**  
Define and govern the **STAC 1.0 Items** that represent individual **interaction spheres** in KFM v11.

Each Item encodes a **generalized cultural connectivity region**:

- Spatial footprint (generalized polygons/H3 mosaic)  
- Temporal coverage (OWL-Time compatible)  
- KFM archaeology + cultural-landscape semantics (`kfm:*`)  
- CARE and sovereignty metadata (`care:*`)  
- Provenance linkage to PROV-O lineage logs  

These Items are the feature-level building blocks for:

- Story Node v3 cultural network narratives  
- Focus Mode v3 context overlays  
- MapLibre/Cesium landscape visualizations  
- Neo4j graph ingestion of `InteractionSphere` nodes

---

## 📘 Overview

This directory holds all **interaction-sphere STAC Items**, each describing a single interpreted sphere such as:

- `great-bend-aspect-v3.json`  
- `central-plains-exchange-v2.json`  
- `protohistoric-wichita-v2.json`  

Each Item must:

- Be **generalized** (no site-precise geometries).  
- Align with its parent Collection in `../collections/`.  
- Align with DCAT + metadata in `../../metadata/`.  
- Align with provenance in `../../provenance/`.  
- Conform to shared STAC schemas in `../../../artifact-inventories/stac/schemas/` and local extensions.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/stac/items/
├── 📄 README.md                             # This file
├── 📄 great-bend-aspect-v3.json             # Great Bend Aspect interaction-sphere STAC Item
├── 📄 central-plains-exchange-v2.json       # Central Plains exchange-sphere STAC Item
├── 📄 protohistoric-wichita-v2.json         # Protohistoric Wichita corridor STAC Item
└── …                                        # Future interaction-sphere Items
~~~

File names (minus `.json`) must match the `id` field in each STAC Item and the stems used in metadata + provenance.

---

## 📚 Controlled Vocabularies (Item-Level)

Interaction-sphere Items should use the following vocabularies (as per the parent interaction-spheres docs):

| Field / Property      | Allowed / Example Values                                       |
|-----------------------|----------------------------------------------------------------|
| `properties.region_type` / `kfm:region_type` | `interaction_sphere`, `exchange_zone`, `contact_region` |
| `properties.route_type`                       | `trade`, `seasonal`, `migration`, `multimodal`, `other` |
| `properties.interaction_type`                | `influence_sphere`, `contact_zone`, `exchange_corridor` |
| `properties.care:consent_status`            | `approved`, `conditional`, `not-approved`, `not-applicable` |

These vocabularies are enforced or referenced by schemas in `../schemas/` where applicable.

---

## 📦 Required STAC Item Structure

All Items must satisfy the following structural requirements.

### STAC Core

Required core fields:

- `stac_version: "1.0.0"`  
- `type: "Feature"`  
- `id`: stable, versioned ID (for example, `"great-bend-aspect-v3"`)  
- `bbox`: generalized bounding box `[minLon, minLat, maxLon, maxLat]`  
- `geometry`:  
  - `type`: `"Polygon"` or `"MultiPolygon"`  
  - `coordinates`: generalized coordinates only  
- `properties`: object containing STAC + extension attributes  
- `assets`:
  - Must include a `data` asset with `href`, `type`, and `roles` (including `"data"`).  

### KFM Interaction-Sphere Extensions (`kfm:*`)

Typical required `properties` fields:

| Field                 | Description                                                  |
|-----------------------|--------------------------------------------------------------|
| `kfm:domain`          | Must be `"archaeology-cultural-landscapes"`                 |
| `kfm:culture_phase` / `kfm:phase` | Cultural-phase label for the sphere            |
| `kfm:region_type`     | From controlled vocabulary (`interaction_sphere`, etc.)     |
| `kfm:generalization`  | Generalization level (for example, `"H3-r7"`, `"H3-r8"`)    |
| `kfm:provenance`      | Relative path to PROV-O provenance log                      |
| `kfm:review_cycle`    | For example, `"Biannual"`                                   |

Schemas in `../schemas/` define the authoritative constraints and may require additional `kfm:*` fields (e.g., `kfm:interaction_type`).

### CARE Cultural-Safety Metadata (`care:*`)

Each interaction-sphere Item must include:

| Field                   | Description / Rules                                      |
|-------------------------|----------------------------------------------------------|
| `care:sensitivity`      | `"general"`, `"generalized"`, or `"restricted-generalized"` (no `"restricted"` in public catalog). |
| `care:review`           | `"faircare"`, `"tribal"`, or `"none-required"`           |
| `care:notes`            | Required for non-`general` sensitivities; describes safety decisions. |
| `care:visibility_rules` | For example, `"h3-only"` or `"no-exact-points"`          |
| `care:sovereignty`      | For example, `"protected"`                               |
| `care:consent_status`   | `approved`, `conditional`, `not-approved`, `not-applicable` |

Protohistoric/ethnohistoric spheres generally require `care:review = "tribal"` and stricter visibility rules.

### DCAT & Metadata Crosswalk

For each Item, the corresponding `../../metadata/*.json` file must be consistent:

- `dct:title` ↔ Item `id` / `description`.  
- `dct:license` ↔ STAC / Collection license.  
- `dct:temporal` ↔ Item temporal properties or Collection `extent.temporal`.  
- `dcat:distribution` ↔ `assets.data.href`.

### Provenance Linkage

- `properties.kfm:provenance` must reference a valid JSON-LD provenance file in `../../provenance/`.  
- Filename stems should align across:
  - `items/<id>.json`  
  - `metadata/<id>.json`  
  - `provenance/<id>.json`  

---

## 🌍 Spatial Requirements

Interaction-sphere Items must adhere to the following:

- **Generalized geometry only**:
  - No site- or household-level precision.  
  - Generalization via H3 mosaics, coarse polygons, or both.  
- CRS:
  - Geometries and bboxes in **EPSG:4326**.  
- For high sensitivity:
  - `care:visibility_rules = "h3-only"` may be applied, and geometry may be suppressed from public representations.

---

## 🕰 Temporal Requirements

Temporal modeling:

- Use OWL-Time–compatible ranges:
  - `properties.start_datetime` and `properties.end_datetime` where appropriate.  
- Align with:
  - Cultural phases referenced in `kfm:culture_phase`.  
  - Collection-level `extent.temporal`.  
  - Focus Mode and Story Node timelines.

---

## 📊 Item Index (Illustrative)

| STAC Item                         | Region Type         | CARE Sensitivity        | Review        | Status   |
|----------------------------------|---------------------|-------------------------|---------------|----------|
| `great-bend-aspect-v3.json`     | interaction_sphere  | generalized             | FAIR+CARE     | 🟢 Active |
| `central-plains-exchange-v2.json`| exchange_zone       | generalized             | FAIR+CARE     | 🟢 Active |
| `protohistoric-wichita-v2.json`  | interaction_sphere  | restricted-generalized  | Tribal + FAIR+CARE | 🟡 Review |

Authoritative status & review flags are maintained in metadata, provenance, and release manifests.

---

## 🧪 Validation Requirements

All Items in this directory must validate against:

- `stac-item-schema.json` in `../schemas/`  
- KFM extension schemas (for example, `kfm-archaeology-extension.json` or cultural-landscapes-specific schema)  
- CARE extension schema (`care-sensitivity-extension.json`)  
- DCAT crosswalk schemas where used  
- Provenance-link schemas confirming `kfm:provenance` correctness  

Validation is performed by CI workflows such as:

- `.github/workflows/artifact-stac-validate.yml`  
- `.github/workflows/metadata-validate.yml`  
- `.github/workflows/faircare-audit.yml`  

Any validation failure must be resolved before Items are considered governed and Active.

---

## 🔗 Related Specifications

- `../README.md`  
  – Interaction Sphere STAC Catalog (Items + Collections overview).  
- `../collections/README.md`  
  – Interaction-sphere STAC Collections index.  
- `../../metadata/README.md`  
  – DCAT + CARE metadata rules for interaction spheres.  
- `../../provenance/README.md`  
  – PROV-O lineage and review logs for interaction spheres.  
- `../../../../artifact-inventories/stac/schemas/README.md`  
  – Shared STAC schema and extension definitions reused by cultural-landscape layers.

---

## 🕰 Version History

| Version   | Date       | Author                                                   | Summary                                                                 |
|-----------|------------|----------------------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3   | 2025-12-02 | Cultural Landscape WG · FAIR+CARE Council · Metadata Standards Subcommittee | Created STAC Items index for interaction spheres; aligned with v11 STAC catalog, collections, and CARE/KFM extension schemas. |
| v11.0.0   | 2025-11-24 | Cultural Landscape WG                                   | Initial v11 interaction-sphere STAC Item patterns and requirements.    |

---

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
FAIR+CARE · Sovereignty-Governed  
KFM-MDP v11.2.2 · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Interaction Sphere STAC Catalog](../README.md)

