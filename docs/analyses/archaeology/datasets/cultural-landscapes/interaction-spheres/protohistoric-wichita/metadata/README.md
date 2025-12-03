---
title: "🪶📑 Kansas Frontier Matrix — Protohistoric Wichita Interaction Sphere Metadata (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/protohistoric-wichita/metadata/README.md"
description: "High-sensitivity DCAT + STAC + CARE metadata specification for the Protohistoric Wichita interaction-sphere dataset in KFM v11."
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Cultural Landscape Working Group · FAIR+CARE Council · Tribal Sovereignty Advisory Review Required"
content_stability: "stable"
status: "Active / Enforced (High Sensitivity · Tribal Review Required)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_uuid: "urn:kfm:doc:protohistoric-wichita-interaction-sphere-metadata-v11.2.3"
doc_kind: "Dataset Metadata"
intent: "protohistoric-wichita-metadata"
semantic_document_id: "kfm-doc-archaeology-protohistoric-wichita-interaction-sphere-metadata-v11.2.3"
category: "Analyses · Archaeology · Cultural Landscapes · Metadata"

sbom_ref: "../../../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/archaeology-protohistoric-wichita-metadata-v1.json"
energy_schema: "../../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../../schemas/telemetry/carbon-gco2e-v1.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

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

data_steward: "Cultural Landscape Working Group · FAIR+CARE Council · Tribal Sovereignty Advisory Review"
provenance_chain:
  - "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/protohistoric-wichita/metadata/README.md@v10.4.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true
---

# 🪶📑 Protohistoric Wichita Interaction Sphere — Metadata (v11)

`docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/protohistoric-wichita/metadata/README.md`

**Purpose**  
Define the **official metadata specification** for the **Protohistoric Wichita Interaction Sphere**, a high-sensitivity cultural dataset requiring **mandatory tribal review**, CARE governance, and strict spatial generalization.

This metadata:

- Documents temporal, spatial, cultural, and ethical dimensions of the dataset.  
- Ensures restricted visibility modes for sensitive regions.  
- Provides cross-standard compatibility (**DCAT**, **STAC**, **KFM extensions**, **CARE**, **PROV-O**).  
- Supports Story Nodes and Focus Mode v3 interpretive layers.  
- Controls how the dataset enters and behaves inside the KFM Knowledge Graph.

For dataset context see:

- `../README.md` (dataset overview).  

For global interaction-sphere metadata standards see:

- `../../metadata/README.md` (interaction-sphere metadata standards).

---

## 📘 Overview

The **Protohistoric Wichita Interaction Sphere** metadata describes:

- Interaction networks, mobility patterns, and exchange corridors across **AD 1500–1700**.  
- Cultural transformations involving ancestral Wichita communities and neighbors.  
- Generalized representations only (no site-level or sacred-geography detail).  
- High-sensitivity status under CARE and sovereignty rules.

Metadata stored here is represented as **JSON-LD** that combines:

- DCAT 3.0 dataset metadata.  
- STAC-aligned Item metadata (mirroring `../stac/items/protohistoric-wichita-v2.json`).  
- CARE and sovereignty metadata.  
- KFM archaeology extension fields (`kfm:*`).  

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/protohistoric-wichita/metadata/
├── 📄 README.md                               # This file
└── 📄 protohistoric-wichita-v2.json           # DCAT + STAC + CARE + KFM metadata
~~~

The JSON file name (`protohistoric-wichita-v2.json`) MUST match:

- STAC Item ID in `../stac/items/protohistoric-wichita-v2.json`.  
- Provenance ID in `../provenance/protohistoric-wichita-v2.json` (via stems).

---

## 📦 Required Metadata Specification

Every metadata file for this dataset MUST include:

- **DCAT 3.0** Dataset fields.  
- **STAC-aligned** fields that mirror the Item.  
- **KFM archaeology and cultural-landscape extensions**.  
- **CARE** cultural-safety metadata.  
- Consistency with **provenance** and **STAC** artifacts.

Below describes expectations for `protohistoric-wichita-v2.json`.

---

## 🧾 DCAT 3.0 Metadata

Required DCAT fields:

| Field            | Description                      | Example                                                   |
|------------------|----------------------------------|-----------------------------------------------------------|
| `dct:title`      | Dataset title                   | `"Protohistoric Wichita Interaction Sphere v2"`           |
| `dct:description`| Generalized cultural summary    | `"Generalized protohistoric Wichita interaction region across Arkansas–Walnut–Ninnescah valleys."` |
| `dct:license`    | License (open)                  | `"CC-BY-4.0"`                                             |
| `dct:temporal`   | OWL-Time interval / description | `"AD 1500–1700"` or an interval representation           |
| `dct:creator`    | Primary source institution(s)   | `"Cultural Landscape Working Group"`                      |
| `dcat:keyword`   | Tags                            | `["Wichita", "Protohistoric", "Kansas", "Interaction Sphere"]` |
| `dcat:distribution` | Link to distribution        | `"../stac/items/protohistoric-wichita-v2.json"` or dataset asset URL |

DCAT content must be consistent with:

- STAC Item fields (ID, description, temporal coverage, license).  
- CARE and provenance metadata.

---

## 🧭 KFM Archaeology & Landscape Metadata (`kfm:*`)

KFM fields capture domain semantics and governance:

| Field                     | Purpose                               | Example                                                    |
|---------------------------|----------------------------------------|------------------------------------------------------------|
| `kfm:domain`              | Domain identifier                      | `"archaeology-cultural-landscapes"`                       |
| `kfm:landscape_type` or `kfm:region_type` | Dataset class          | `"interaction_sphere"`                                    |
| `kfm:culture_phase`       | Cultural phase(s) represented          | `["Protohistoric-Wichita"]`                               |
| `kfm:generalization`      | Spatial generalization mechanism       | `"H3-r7"` or `"H3-r8"`                                    |
| `kfm:source`              | PD + tribal-approved source synthesis  | `"Archaeological syntheses + approved ethnohistoric summaries"` |
| `kfm:provenance`          | PROV-O lineage reference               | `"../provenance/protohistoric-wichita-v2.json"`           |
| `kfm:schema_version`      | Metadata template/schema version       | `"v11.0.0"` or relevant version string                    |

These fields must match values present in:

- STAC Item properties (`kfm:*`).  
- PROV-O provenance (`kfm:provenance`, `kfm:source`, etc.).

---

## ⚖️ CARE Cultural-Safety Metadata

**This dataset is high-sensitivity.** CARE metadata determines what can be shared and at what level of detail.

Required CARE fields:

| CARE Field             | Required / Expected Values                       | Notes                                               |
|------------------------|--------------------------------------------------|-----------------------------------------------------|
| `care:sensitivity`     | `"restricted-generalized"`                       | Reflects high sensitivity with generalization applied |
| `care:review`          | `"tribal"` (and FAIR+CARE where recorded)       | Tribal/sovereignty review is mandatory              |
| `care:notes`           | Explanation of cultural considerations          | Must note removal/generalization of sensitive content |
| `care:visibility_rules`| `"h3-only"` (or stricter, if mandated)          | Public view uses H3 mosaic rather than polygons     |
| `care:consent_status`  | `approved`, `conditional`, `not-approved`, or `not-applicable` | For v11, likely `"conditional"` until fully approved |

**Forbidden** in metadata:

- `care:sensitivity = "restricted"` for cataloged metadata.  
- Any text that exposes restricted oral histories or ceremonial knowledge without explicit approval.  
- Claims or descriptions that contradict sovereignty policy.

CARE values here MUST be consistent with:

- STAC Item `properties.care:*`.  
- Provenance log `care:*` fields.

---

## 🌍 Spatial Metadata Requirements

Spatial metadata described in this file must reflect:

- CRS: **EPSG:4326** for all public-facing geometry references.  
- Geometry: for this dataset, **H3 mosaic only** (levels ~6–7) is recommended in public contexts:
  - The underlying STAC Item may have polygons, but `care:visibility_rules` may force H3-only exposure.  
- No site-level inference:
  - BBoxes and spatial descriptions must be **coarse**, referencing regions, not sites.  
- Environmental context (hydrology, landforms, etc.) must also be generalized and described at regional scales.

Any H3 or generalization parameters used should be duplicated in provenance and documented in `kfm:generalization`.

---

## 🕰 Temporal Metadata Requirements

Temporal metadata must:

- Reflect the protohistoric span **AD 1500–1700**.  
- Be **OWL-Time–compatible** (for example, using interval structures in STAC and DCAT).  
- Note uncertainty where source data are broader or narrower (for example, different ranges for specific lines of evidence).  
- Align with KFM cultural-phase ontology (for example, `Protohistoric-Wichita` as a recognized phase label).

Timelines used in Story Nodes and Focus Mode v3 should be derived from these intervals.

---

## 🧪 Provenance Linkage

The metadata file must link clearly to the PROV-O lineage:

- `kfm:provenance` → `../provenance/protohistoric-wichita-v2.json`.  
- Optionally, DCAT-level provenance fields (for example, `dct:provenance`) can recap key lineage information.

The provenance log must satisfy:

- Provenance schemas under `../../provenance/` and `../../stac/schemas/` (where relevant).  
- CARE and sovereignty rules for high-sensitivity interaction-sphere datasets.

---

## 🧠 KFM Knowledge Graph Integration

From the metadata, graph ingestion will create and/or enrich:

**Nodes**

- `InteractionSphere` (Protohistoric Wichita).  
- `MetadataRecord` for this dataset.  
- `CulturalPhase` nodes representing protohistoric phases.  
- CARE-related nodes (for example, `CareSensitivityState`).

**Relationships**

- `HAS_METADATA` (InteractionSphere → MetadataRecord).  
- `HAS_CARE_SENSITIVITY` (InteractionSphere → CARE state node).  
- `HAS_PROVENANCE` (via metadata → provenance linkage).  
- `OCCURRED_DURING` (InteractionSphere → CulturalPhase / TimeInterval).  
- `ASSOCIATED_WITH` (InteractionSphere ↔ other datasets and narratives).

These relationships govern how this dataset can be queried, visualized, and narrated inside KFM.

---

## 🎛 Story Nodes & Focus Mode Integration

This metadata controls:

- **Context-aware narratives** for Story Nodes referencing Protohistoric Wichita.  
- **Ethical framing** in Focus Mode v3 responses:
  - Warnings and sensitivity banners.  
  - Provenance chips linking to lineage logs.  
- Time-scope and spatial-scope used by:
  - Timeline sliders.  
  - Map overlays.  
  - Network/interaction storylines.

Story Nodes and Focus Mode must respect:

- `care:sensitivity` and `care:visibility_rules`.  
- Sovereignty policy linked in front matter.  
- Tribal review conditions and consent status.

---

## 📊 Metadata Summary (Illustrative)

| Field          | Value                                |
|----------------|--------------------------------------|
| Title          | Protohistoric Wichita Interaction Sphere v2 |
| Sensitivity    | restricted-generalized              |
| Review         | Tribal (mandatory), FAIR+CARE       |
| Geometry Mode  | H3-only (public-facing)             |
| Phase          | Protohistoric Wichita               |
| Provenance     | Linked (`../provenance/protohistoric-wichita-v2.json`) |
| Status         | 🟡 Conditional — cannot expand public exposure without renewed tribal sign-off |

Authoritative status and review decisions are recorded in governance and release manifests.

---

## 🔗 Related Specifications

- `../README.md`  
  – Protohistoric Wichita interaction-sphere dataset overview.  
- `../stac/README.md`  
  – STAC Collection documentation for Protohistoric Wichita.  
- `../stac/items/README.md`  
  – STAC Item documentation for Protohistoric Wichita.  
- `../provenance/README.md`  
  – Provenance index and requirements.  
- `../../metadata/README.md`  
  – Global interaction-sphere metadata standards.

---

## 🕰 Version History

| Version   | Date       | Author                                             | Summary                                                                 |
|-----------|------------|----------------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3   | 2025-12-02 | Cultural Landscape WG · FAIR+CARE Council · Tribal Sovereignty Advisory Review | Updated to KFM v11.2.3; aligned with global interaction-sphere metadata patterns; clarified CARE/sovereignty fields and crosswalk expectations. |
| v10.4.0   | 2025-11-17 | Cultural Landscape WG · FAIR+CARE Council · Tribal Advisors | Initial metadata release; defined high-sensitivity CARE requirements for Protohistoric Wichita. |
| v10.0.0   | 2025-11-12 | Landscape Metadata Team                           | Prototype metadata content and structure.                              |

---

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Tribal Approval Required · FAIR+CARE · Sovereignty-Governed  
KFM-MDP v11.2.2 · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Protohistoric Wichita Dataset](../README.md)
