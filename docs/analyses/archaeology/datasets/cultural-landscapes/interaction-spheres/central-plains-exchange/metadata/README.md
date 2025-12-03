---
title: "🔄📑 Kansas Frontier Matrix — Central Plains Exchange Interaction Sphere Metadata (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/central-plains-exchange/metadata/README.md"
description: "DCAT + STAC + KFM + CARE metadata specification for the Central Plains Exchange interaction-sphere dataset in KFM v11."
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Cultural Landscape WG · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_uuid: "urn:kfm:doc:cultural-landscape-interaction-sphere-central-plains-exchange-metadata-v11.2.3"
doc_kind: "Dataset Metadata"
intent: "central-plains-exchange-metadata"
semantic_document_id: "kfm-doc-archaeology-cultural-landscapes-central-plains-exchange-metadata-v11.2.3"
category: "Analyses · Archaeology · Cultural Landscapes · Metadata"

sbom_ref: "../../../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/archaeology-central-plains-exchange-metadata-v1.json"
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
care_label: "CARE-Compliant"
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

data_steward: "Cultural Landscape WG · FAIR+CARE Council"
provenance_chain:
  - "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/central-plains-exchange/metadata/README.md@v10.4.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true
---

# 🔄📑 Central Plains Exchange Interaction Sphere Metadata (v11)

`docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/central-plains-exchange/metadata/README.md`

**Purpose**  
Provide the **DCAT + STAC-aligned + CARE-governed metadata specification** for the **Central Plains Exchange Interaction Sphere** dataset in KFM v11.

This metadata governs:

- Dataset-level description and discoverability.  
- Cultural and ethical framing under FAIR+CARE.  
- Temporal and spatial extents (generalized).  
- KFM cultural-landscape semantics (`kfm:*`).  
- Crosswalks to STAC Items and PROV-O provenance for reproducibility.

For dataset context, see:

- `../README.md` (interaction-sphere overview).  

For global interaction-sphere metadata standards, see:

- `../../metadata/README.md`.

---

## 📘 Overview

The **Central Plains Exchange Interaction Sphere** describes a multi-century cultural network zone associated with:

- Central Plains Tradition (CPT) communities.  
- Cross-drainage interaction among Republican, Solomon, Smoky Hill, Platte, and Kansas rivers.  
- Shared ceramic, lithic, architectural, and subsistence patterns.  
- Long-distance material exchange and interaction.  
- Paleoenvironmental drivers (prairie–riverine ecotones, alluvial systems).

This README defines the expected structure of:

- `central-plains-exchange-v1.json` — the primary metadata record for this interaction sphere.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/central-plains-exchange/metadata/
├── 📄 README.md                             # This file
└── 📄 central-plains-exchange-v1.json       # DCAT + KFM + CARE metadata for v1
~~~

---

## 📦 Required Metadata (DCAT + KFM + CARE)

Each interaction-sphere metadata file MUST:

- Implement required **DCAT 3.0** fields.  
- Include KFM cultural-landscape fields (`kfm:*`).  
- Include CARE fields (`care:*`).  
- Remain consistent with:
  - STAC Item `../stac/central-plains-exchange-v1.json`.  
  - Provenance log `../provenance/central-plains-exchange-v1.json`.

Below summarizes expected fields for `central-plains-exchange-v1.json`.

---

### 1️⃣ DCAT 3.0 Fields

| Field             | Example                                              | Purpose                                  |
|-------------------|------------------------------------------------------|------------------------------------------|
| `dct:title`       | `"Central Plains Exchange Interaction Sphere v1"`   | Human-readable title                     |
| `dct:description` | `"Generalized multi-phase cultural interaction region across Central Plains drainages."` | Dataset summary                          |
| `dct:license`     | `"CC-BY-4.0"`                                       | Open data requirement                    |
| `dct:temporal`    | `"AD 900–1400"`                                     | OWL-Time–compatible span (expressed textually or via structured interval) |
| `dct:creator`     | `"Cultural Landscape Working Group"`                | Primary creator/steward                  |
| `dcat:keyword`    | `["CPT","exchange zone","archaeology","Kansas"]`    | Searchability and thematic grouping      |
| `dcat:distribution` | `"../stac/central-plains-exchange-v1.json"`       | STAC Item reference                      |

DCAT fields must crosswalk cleanly to STAC and provenance (temporal coverage, license, title).

---

### 2️⃣ KFM Cultural-Landscape Metadata (`kfm:*`)

KFM extensions embed domain semantics:

| Field                     | Example                                        | Description                                    |
|---------------------------|------------------------------------------------|------------------------------------------------|
| `kfm:domain`              | `"archaeology-cultural-landscapes"`           | Domain identifier                              |
| `kfm:landscape_type`      | `"interaction_sphere"`                        | Dataset class                                  |
| `kfm:culture_phase`       | `["CPT-Early","CPT-Middle","CPT-Late"]`       | Phases represented                             |
| `kfm:generalization`      | `"H3-r7"`                                     | Spatial generalization mechanism               |
| `kfm:source`              | `"Archaeological synthesis (public-domain)"`  | Main lines of evidence                         |
| `kfm:provenance`          | `"../provenance/central-plains-exchange-v1.json"` | Link to PROV-O provenance record           |
| `kfm:schema_version`      | `"v11.0.0"`                                   | Metadata schema/template version               |

These values must be synchronized with:

- STAC Item properties.  
- Provenance fields.

---

### 3️⃣ CARE Cultural-Safety Metadata (`care:*`)

Because this sphere is **moderate sensitivity**, CARE metadata is required but less restrictive than protohistoric spheres.

Required CARE fields:

| CARE Field             | Recommended Value / Notes                                |
|------------------------|-----------------------------------------------------------|
| `care:sensitivity`     | `"generalized"`                                          |
| `care:review`          | `"faircare"`                                             |
| `care:notes`           | e.g. `"Generalized polygons used; no site-level or sacred locations included."` |
| `care:visibility_rules`| `"polygon-generalized"` (or `"h3-only"` when needed)     |
| `care:consent_status`  | `approved`, `conditional`, `not-approved`, or `not-applicable` |

Forbidden for public-governed GBA/CPT spheres:

- `care:sensitivity = "restricted"`.  
- Inclusion of specific sacred or restricted geographies.  
- Embedding of sensitive oral histories without explicit consent.

---

## 🌍 Spatial Metadata Requirements

Spatial metadata described in `central-plains-exchange-v1.json` must reflect:

- CRS: **EPSG:4326** for all referenced coordinates.  
- Geometry: generalized `MultiPolygon` as defined in STAC.  
- Generalization strategy:
  - H3 mosaics and/or polygon simplification at appropriate scale.  
  - No site-level locational hints or explicit boundaries that allow sensitive inference.

Bounding boxes must be derived from generalized geometry and be coarse enough to protect sensitive landscapes.

---

## 🕰 Temporal Metadata Requirements

Temporal coverage:

- Must represent the CPT span (~AD 900–1400).  
- Must align with STAC temporal properties and OWL-Time semantics.  
- May include notes on uncertainty when phase boundaries are approximate.

Cultural-phase labels used (for example, `CPT-Early`, `CPT-Middle`, `CPT-Late`) must match KFM’s cultural-phase ontology and graph definitions.

---

## 🧪 Provenance Linkage

Metadata must clearly link to the provenance log:

- `kfm:provenance` → `../provenance/central-plains-exchange-v1.json`

The provenance file, in turn, documents:

- Raw sources, transformations, and generalization.  
- FAIR+CARE review events and decisions.  
- Major modeling and synthesis choices.

---

## ⚖️ Ethical & Cultural Governance

All Central Plains Exchange metadata must:

- Use culturally respectful, non-colonial language.  
- Emphasize interpretive nature and uncertainty (avoid territorial claims).  
- Clearly state generalization and redaction strategies.  
- Avoid publishing restricted or harmful content, even at generalized scales.

While tribal review is not required for this sphere, additional consultations may be pursued where appropriate.

---

## 🧠 Integration Into KFM Ecosystem

### Graph Integration

Metadata generated from this standard supports:

**Nodes**

- `InteractionSphere` (Central Plains Exchange).  
- `MetadataRecord`.  
- `CulturalPhase`.  
- CARE- and governance-related nodes.

**Relationships**

- `HAS_METADATA` (InteractionSphere → MetadataRecord).  
- `HAS_PROVENANCE` (via `kfm:provenance`).  
- `HAS_CARE_SENSITIVITY` (InteractionSphere → CARE node).  
- `OCCURRED_DURING` (InteractionSphere → CulturalPhase / TimeInterval).  

### Story Nodes & Focus Mode v3

- Provide dataset-level context, titles, descriptions, and warning banners.  
- Drive sensitivity badges and provenance chips.  
- Supply temporal and spatial scopes for narratives and overlays.

---

## 📊 Metadata Summary (Illustrative)

| Field            | Value                                          |
|------------------|------------------------------------------------|
| Title            | Central Plains Exchange Interaction Sphere v1 |
| Sensitivity      | generalized                                   |
| CARE Review      | FAIR+CARE                                     |
| Phases           | CPT-Early / CPT-Middle / CPT-Late             |
| Spatial Mode     | MultiPolygon (H3-r7 generalized)              |
| Provenance       | Linked (`../provenance/central-plains-exchange-v1.json`) |
| Status           | 🟢 Active                                      |

Authoritative state is maintained in manifests and governance documents.

---

## 🔗 Related Specifications

- `../README.md`  
  – Central Plains Exchange interaction-sphere dataset overview.  
- `../stac/README.md`  
  – Central Plains Exchange STAC documentation.  
- `../provenance/README.md`  
  – Central Plains Exchange provenance index.  
- `../../metadata/README.md`  
  – Global interaction-sphere metadata standards.

---

## 🕰 Version History

| Version   | Date       | Author                                   | Summary                                                                 |
|-----------|------------|------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3   | 2025-12-02 | Cultural Landscape WG · FAIR+CARE Council | Updated to KFM v11.2.3; aligned with interaction-sphere metadata standards; added telemetry refs and clarified CARE semantics. |
| v10.4.0   | 2025-11-17 | Cultural Landscape WG · FAIR+CARE Council | Initial metadata release for Central Plains Exchange interaction sphere. |
| v10.0.0   | 2025-11-10 | Landscape Metadata Team                  | Prototype metadata content and layout.                                  |

---

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
FAIR+CARE · Sovereignty-Aligned  
KFM-MDP v11.2.2 · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Central Plains Exchange Dataset](../README.md)
