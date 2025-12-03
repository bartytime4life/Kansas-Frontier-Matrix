---
title: "🗂️ Kansas Frontier Matrix — Interaction Sphere STAC Collections (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/stac/collections/README.md"
description: "STAC 1.0 Collections index for KFM v11 cultural interaction-sphere datasets, grouping generalized connectivity zones under FAIR+CARE and sovereignty governance."
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Cultural Landscape Working Group · FAIR+CARE Council · Metadata Standards Subcommittee"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_uuid: "urn:kfm:doc:archaeology-interaction-spheres-stac-collections-v11.2.3"
doc_kind: "STAC Collections Index"
intent: "interaction-spheres-stac-collections"
semantic_document_id: "kfm-doc-archaeology-interaction-spheres-stac-collections-v11.2.3"
category: "Analyses · Archaeology · Cultural Landscapes · STAC"

sbom_ref: "../../../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/archaeology-interaction-spheres-stac-collections-v1.json"
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
  - "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/stac/collections/README.md@v11.0.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true
---

# 🗂️ Kansas Frontier Matrix — Interaction Sphere STAC Collections (v11)

`docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/stac/collections/README.md`

**Purpose**  
Provide the **governed index of STAC 1.0 Collections** for interaction-sphere datasets in KFM v11.

These Collections:

- Group related **interaction-sphere** STAC Items (for example, Great Bend, Central Plains exchange).  
- Expose generalized spatial and temporal coverage for cultural connectivity zones.  
- Carry CARE and sovereignty metadata at the collection level.  
- Anchor integration with DCAT, PROV-O, and the KFM knowledge graph.

This document is the **Collections-level companion** to the interaction-sphere STAC catalog README.

---

## 📘 Overview

Interaction-sphere STAC Collections represent:

- High-level **cultural regions of interaction**, exchange, or contact.  
- Time-bounded, generalized **zones of shared material-culture patterns**.  
- Ethically governed, sovereignty-aware representations of cultural landscapes.

Each Collection:

- Summarizes a family of related Items (for example, all versions of Great Bend interaction spheres).  
- Publishes **spatial extent** (generalized) and **temporal coverage** (OWL-Time).  
- Encodes CARE and sovereignty metadata that apply to all child Items.  
- Provides a stable discovery surface for Focus Mode v3, Story Nodes, and graph queries.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/stac/collections/
├── 📄 README.md                          # This file (Collections index)
├── 📄 interaction-spheres.json           # Root interaction-spheres Collection
├── 📄 great-bend-aspect.json             # Great Bend Aspect interaction-sphere Collection
├── 📄 central-plains-exchange.json       # Central Plains exchange-sphere Collection
└── 📄 protohistoric-wichita.json         # Protohistoric Wichita corridor Collection
~~~

Each `.json` file is a **STAC Collection** compliant with STAC 1.0 + KFM + CARE extensions.

---

## 📚 Controlled Vocabularies (Collections)

Collections should use the same controlled vocabularies as other interaction-sphere docs:

| Field                 | Allowed / Example Values                                       |
|-----------------------|----------------------------------------------------------------|
| `kfm:region_type`     | `interaction_sphere`, `exchange_zone`, `contact_region`        |
| `kfm:domain`          | `archaeology-cultural-landscapes`                              |
| `care:consent_status` | `approved`, `conditional`, `not-approved`, `not-applicable`    |

Additional vocabularies (for example, `interaction_type`) may be defined in shared schemas in `stac/schemas/`.

---

## 📦 Required Structure for STAC Collections

All interaction-sphere Collections must satisfy the following.

### STAC Core

Required fields:

- `stac_version: "1.0.0"`  
- `type: "Collection"`  
- `id`:
  - Stable identifier (for example, `"interaction-spheres"`, `"great-bend-aspect"`).  
- `description`:
  - Human-readable summary of the interaction sphere family.  
- `license`:
  - SPDX identifier (for example, `"CC-BY-4.0"`).  
- `extent`:
  - `extent.spatial.bbox`: generalized bounding boxes for all child Items.  
  - `extent.temporal.interval`: list of `[start, end]` intervals (OWL-Time compatible).

Collections may also include:

- `keywords` / `keywords[]` for search.  
- `links` to child Items, parent/root Collections, and related catalogs.

### KFM Extensions (`kfm:*`)

Typical required fields:

| Field            | Description                                              |
|------------------|----------------------------------------------------------|
| `kfm:domain`     | Must be `"archaeology-cultural-landscapes"`             |
| `kfm:region_type`| Collection-level region category (see vocab table)      |
| `kfm:review_cycle` | `"Biannual"` or `"Annual"` (as governed)             |
| `kfm:provenance` | Optional reference to Collection-level provenance       |

### CARE & Sovereignty Metadata (`care:*`)

At the Collection level, `care:*` should express the **least permissive** sensitivities across child Items:

| Field              | Description / Notes                                        |
|--------------------|-----------------------------------------------------------|
| `care:sensitivity` | `"general"`, `"generalized"`, or `"restricted-generalized"` |
| `care:review`      | `"faircare"` and/or `"tribal"` as appropriate             |
| `care:notes`       | Summary of cultural-safety and sovereignty considerations |
| `care:sovereignty` | For example, `"protected"`                                |

Collections that include any high-sensitivity Items should reflect that in their `care:sensitivity` and notes.

---

## 📚 Collection Descriptions (v11)

### `interaction-spheres.json` (Root Collection)

- **Scope:** All interaction-sphere datasets cataloged in KFM v11.  
- **Extent:** Kansas and adjacent regions (generalized).  
- **Purpose:** Top-level index for interaction-sphere Items and sub-Collections.  
- **Use:** Root entry point for clients that need a single discovery node.

### `great-bend-aspect.json`

- **Scope:** Great Bend Aspect interaction-sphere datasets (multiple versions or resolutions).  
- **Interpretation:** Material-culture and settlement evidence often associated with protohistoric Wichita ancestors.  
- **CARE:** `generalized` sensitivity; sovereignty-governed where relevant.

### `central-plains-exchange.json`

- **Scope:** Exchange spheres connecting Central Plains drainages; multi-era.  
- **Interpretation:** Emphasizes exchange and contact, not rigid territorial claims.  
- **CARE:** `generalized` sensitivity; careful narrative framing around fluid boundaries.

### `protohistoric-wichita.json`

- **Scope:** Protohistoric Wichita corridor datasets (high sensitivity).  
- **Interpretation:** Heavily dependent on tribal review and ethnohistoric synthesis.  
- **CARE:** Typically `restricted-generalized` with `care:review = "tribal"` and stricter visibility rules.

---

## 🧪 Validation Requirements

All Collections in this directory must:

1. Validate against `stac-collection-schema.json` in `stac/schemas/`.  
2. Satisfy KFM extension constraints (for example, `kfm-archaeology-extension.json` or cultural-landscapes-specific extension).  
3. Satisfy CARE extension constraints (`care-sensitivity-extension.json`).  
4. Align with DCAT metadata:
   - Where DCAT Collections/Groups are defined for interaction spheres.  
5. Maintain consistency with:
   - Items in `../items/` (ids, extents, domains).  
   - Provenance in `../provenance/`.  
   - Metadata in `../metadata/`.

Validation is enforced via CI workflows (for example: `artifact-stac-validate.yml`, `metadata-validate.yml`, `faircare-audit.yml`).

---

## 🧠 Integration Into KFM Ecosystem

### Knowledge Graph

Collections act as higher-level graph entities:

- `InteractionSphereCollection` nodes.  
- Relationships to:
  - `InteractionSphere` nodes (child Items).  
  - `CulturePhase`, `CulturalRegion`, and other landscape layers.

Edges may include:

- `GROUPS` (Collection → InteractionSphere)  
- `HAS_CARE_SENSITIVITY` (Collection → CARE state)  
- `HAS_EXTENT` (Collection → spatial/temporal extent nodes)  

### Discovery & APIs

- Root Collection (`interaction-spheres.json`) is the primary discovery entry for STAC clients.  
- Sub-Collections provide topic- or culture-specific views for UI and API layers.  
- Focus Mode and Story Nodes can query by Collection ID to retrieve all associated spheres.

---

## 🔗 Related Specifications

- `../README.md`  
  – Interaction-spheres dataset overview (semantics, categories, governance).  
- `../metadata/README.md`  
  – DCAT + CARE metadata standards for interaction spheres.  
- `../provenance/README.md`  
  – PROV-O lineage and sovereignty review logging.  
- `../stac/README.md`  
  – Interaction-sphere STAC catalog (Items + Collections).  
- `../../../../artifact-inventories/stac/schemas/README.md`  
  – Shared STAC schemas and extension definitions reused by cultural landscape layers.

---

## 🕰 Version History

| Version   | Date       | Author                                                   | Summary                                                                 |
|-----------|------------|----------------------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3   | 2025-12-02 | Cultural Landscape WG · FAIR+CARE Council · Metadata Standards Subcommittee | Created Collections index for interaction spheres; aligned with v11 STAC catalog, controlled vocabularies, and governance patterns. |
| v11.0.0   | 2025-11-24 | Cultural Landscape WG                                   | Initial v11 interaction-spheres STAC Collection definitions.           |
| v10.4.0   | 2025-11-17 | Cultural Landscape WG · FAIR+CARE Council               | v10 STAC Collections for interaction spheres.                          |

---

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
FAIR+CARE · Sovereignty-Governed  
KFM-MDP v11.2.2 · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Interaction Sphere STAC Catalog](../README.md)

