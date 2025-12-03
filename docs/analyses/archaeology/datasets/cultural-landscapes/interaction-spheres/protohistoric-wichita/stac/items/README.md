---
title: "🗺️ Kansas Frontier Matrix — STAC Items: Protohistoric Wichita Interaction Sphere (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/protohistoric-wichita/stac/items/README.md"
description: "STAC 1.0 Item documentation for the Protohistoric Wichita interaction-sphere feature in KFM v11, with KFM and CARE extensions."
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Cultural Landscape Working Group · FAIR+CARE Council · Tribal Advisory Review Required"
content_stability: "stable"
status: "Active · Enforced (Tribal Review Required)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_uuid: "urn:kfm:doc:archaeology-protohistoric-wichita-stac-items-v11.2.3"
doc_kind: "STAC Items Index"
intent: "interaction-spheres-protohistoric-wichita-stac-items"
semantic_document_id: "kfm-doc-archaeology-protohistoric-wichita-stac-items-v11.2.3"
category: "Analyses · Archaeology · Cultural Landscapes · STAC"

sbom_ref: "../../../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/stac-items-v1.json"
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

data_steward: "Cultural Landscape Working Group · FAIR+CARE Council · Tribal Advisory Review"
provenance_chain:
  - "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/protohistoric-wichita/stac/items/README.md@v10.4.4"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true
---

# 🗺️ STAC Items — Protohistoric Wichita Interaction Sphere (v11)

`docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/protohistoric-wichita/stac/items/README.md`

**Purpose**  
Define and govern the **STAC 1.0 Item(s)** representing the **Protohistoric Wichita Interaction Sphere** in KFM v11.

This README documents:

- The **protohistoric-wichita-v2** STAC Item (generalized interaction-sphere geometry).  
- Required core STAC fields and KFM + CARE extensions.  
- How this Item aligns with Collection, metadata, and provenance artifacts.  

For cultural and interpretive context, see:

- `../README.md` (dataset overview).  

For catalog-wide interaction-sphere rules, see:

- `../../stac/items/README.md` (global interaction-sphere Items index).

---

## 📘 Overview

The Protohistoric Wichita interaction-sphere STAC Item encodes:

- A **generalized MultiPolygon** footprint of the interaction sphere, derived from GIS and interpretive synthesis.  
- Temporal coverage for the protohistoric period (ca. AD 1500–1700).  
- Cultural-landscape semantics via `kfm:*` properties.  
- CARE and sovereignty metadata (`care:*`) capturing sensitivity, review, and consent status.  
- A pointer to the PROV-O provenance log used by Story Nodes, Focus Mode v3, and graph ingestion.

This directory is **Item-level only**; the Collection is described in:

- `../README.md` and `../collection.json`.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/protohistoric-wichita/stac/items/
├── 📄 README.md                       # This file
└── 📄 protohistoric-wichita-v2.json   # STAC Item for the generalized interaction sphere
~~~

The `id` inside `protohistoric-wichita-v2.json` MUST match the filename stem.

---

## 📚 Controlled Vocabularies (Item-Level)

The protohistoric Wichita Item must align with the interaction-sphere vocabularies:

| Field / Property             | Allowed / Example Values                                       |
|------------------------------|----------------------------------------------------------------|
| `properties.kfm:region_type` | `interaction_sphere`                                          |
| `properties.kfm:interaction_type` | `influence_sphere`, `exchange_corridor`, `contact_zone` |
| `properties.care:consent_status`  | `approved`, `conditional`, `not-approved`, `not-applicable` |

These vocabularies are enforced or referenced by schemas in:

- `../../stac/schemas/`

---

## 📦 Required STAC Item Structure

### STAC Core (Protohistoric Wichita Item)

`protohistoric-wichita-v2.json` must include:

- `stac_version: "1.0.0"`  
- `type: "Feature"`  
- `id: "protohistoric-wichita-v2"`  
- `collection`: `"protohistoric-wichita-interaction-sphere"` or equivalent Collection ID  
- `bbox`:
  - Generalized bounding box `[minLon, minLat, maxLon, maxLat]` matching the generalized geometry.  
- `geometry`:
  - `type`: `"Polygon"` or `"MultiPolygon"`  
  - `coordinates`: generalized only (no site- or cluster-level precision).  

### KFM Interaction-Sphere Extensions (`properties.kfm:*`)

At minimum:

| Field                     | Description                                                     |
|---------------------------|-----------------------------------------------------------------|
| `kfm:domain`              | Must be `"archaeology-cultural-landscapes"`                    |
| `kfm:region_type`         | `"interaction_sphere"`                                         |
| `kfm:culture_phase` / `kfm:phase` | `"Protohistoric-Wichita"` or canonical phase label(s) |
| `kfm:generalization`      | Generalization level, e.g. `"H3-r7"` or `"H3-r8"`              |
| `kfm:provenance`          | `"../provenance/protohistoric-wichita-v2.json"`                |
| `kfm:review_cycle`        | `"Quarterly"` or `"Biannual"` as per governance                |

Additional fields may be required by shared schemas (for example, `kfm:interaction_type`).

### CARE & Sovereignty Extensions (`properties.care:*`)

For this high-sensitivity dataset:

| Field                   | Expected / Allowed Values                                      |
|-------------------------|----------------------------------------------------------------|
| `care:sensitivity`      | `"restricted-generalized"`                                     |
| `care:review`           | `"tribal"` (plus FAIR+CARE where recorded)                     |
| `care:sovereignty`      | `"protected"`                                                  |
| `care:consent_status`   | Initially `"conditional"` until fully approved                 |
| `care:notes`            | Must summarize review outcomes, redaction, and generalization. |
| `care:visibility_rules` | `"h3-only"` recommended; stricter modes may be used if required |

These values must match provenance and metadata records.

### Assets

Minimal `assets` block:

- `assets.data`:
  - `href`: path or URL to the generalized geometry (for example, `"../protohistoric-wichita.geojson"` or a remote path).  
  - `type`: `"application/geo+json"` (or format actually used).  
  - `roles`: must include `"data"`.

---

## 🧪 Validation Requirements

`protohistoric-wichita-v2.json` must pass:

- **STAC Item schema**:
  - `stac-item-schema.json` in `../../stac/schemas/`.  
- **KFM extension schema**:
  - Interaction-sphere KFM schema (`kfm-interaction-extension.json` or equivalent).  
- **CARE extension schema**:
  - `care-sensitivity-extension.json`.  
- **DCAT crosswalk**:
  - With `../metadata/protohistoric-wichita-v2.json`.  
- **Provenance link check**:
  - Ensuring `kfm:provenance` points to an existing `../provenance/protohistoric-wichita-v2.json`.  

CI workflows (for example, `artifact-stac-validate.yml`, `metadata-validate.yml`, `faircare-audit.yml`) must all pass before this Item is considered governed and Active.

---

## 🔗 Related Specifications

- `../README.md`  
  – Protohistoric Wichita interaction-sphere dataset overview and governance.  
- `../stac/README.md`  
  – Protohistoric Wichita STAC Collection documentation.  
- `../../stac/items/README.md`  
  – Global interaction-sphere STAC Items index and requirements.  
- `../../stac/schemas/README.md`  
  – STAC schemas and extensions for interaction spheres.  
- `../metadata/README.md`  
  – DCAT + CARE metadata for Protohistoric Wichita.  
- `../provenance/README.md`  
  – Provenance index for Protohistoric Wichita.

---

## 🕰 Version History

| Version   | Date       | Author                                           | Summary                                                                 |
|-----------|------------|--------------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3   | 2025-12-02 | Cultural Landscape WG · FAIR+CARE Council · Tribal Advisory Review | Rebuilt for KFM v11.2.3; aligned with global interaction-sphere STAC specs and CARE/sovereignty rules; dropped v10 multi-Item pattern in favor of single generalized Item. |
| v10.4.4   | 2025-11-17 | FAIR+CARE Council · Archaeology WG              | v10.4.4 STAC Items README; multi-layer v10-era STAC pattern.           |
| v10.4.0   | 2025-11-15 | Archaeology WG                                   | Initial STAC Items documentation for Protohistoric Wichita.            |

---

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
FAIR+CARE · Sovereignty-Governed  
KFM-MDP v11.2.2 · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Protohistoric Wichita STAC Collection](../README.md)
