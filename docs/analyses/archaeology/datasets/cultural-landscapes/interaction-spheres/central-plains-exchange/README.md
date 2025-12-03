---
title: "🔄 Kansas Frontier Matrix — Central Plains Exchange Interaction Sphere (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/central-plains-exchange/README.md"
description: "Generalized, CARE-governed Central Plains Exchange interaction-sphere dataset for KFM v11, representing multi-phase interaction and exchange networks across the central Great Plains."
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Cultural Landscape Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_uuid: "urn:kfm:doc:cultural-landscape-interaction-sphere-central-plains-exchange-v11.2.3"
doc_kind: "Dataset"
intent: "cultural-landscape-interaction-sphere-central-plains-exchange"
semantic_document_id: "kfm-doc-archaeology-cultural-landscapes-central-plains-exchange-v11.2.3"
category: "Analyses · Archaeology · Cultural Landscapes"

sbom_ref: "../../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/archaeology-central-plains-exchange-v1.json"
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

data_steward: "Cultural Landscape Working Group · FAIR+CARE Council"
provenance_chain:
  - "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/central-plains-exchange/README.md@v10.4.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true
---

# 🔄 Central Plains Exchange Interaction Sphere (v11)

`docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/central-plains-exchange/README.md`

**Purpose**  
Document, govern, and ethically contextualize the **Central Plains Exchange Interaction Sphere**, a generalized cultural region representing broad-scale interaction, exchange, technological circulation, and shared traditions across the central Great Plains.

This dataset synthesizes archaeological, paleoenvironmental, geophysical, and ethnohistoric evidence into a **multi-phase, generalized interaction zone**, supporting:

- Network-based archaeological context and cultural-region modeling.  
- Story Node v3 narrative anchors.  
- Focus Mode v3 interpretive overlays and explanation chips.  
- MapLibre/Cesium polygon and density layers.  
- CARE-compliant, sovereignty-aware territory modeling.

---

## 📘 Overview

The **Central Plains Exchange Interaction Sphere** encompasses a large, multi-century cultural zone defined by:

- Shared material culture distributions (ceramics, lithics, architectural patterns).  
- Exchange of raw materials (for example, chert, ceramic tempers, faunal resources).  
- Overlapping house forms and settlement architectures.  
- Ceramic style continuities across major river drainages.  
- Paleoenvironmental correlates (prairie ecotones, alluvial valleys, hydrology).  
- Inter-valley social connectivity along the **Republican**, **Smoky Hill**, **Platte**, **Solomon**, and **Kansas** Rivers.

It represents a **generalized regional interaction environment** during:

- The **Central Plains Tradition (CPT)** (ca. AD 900–1400).  
- Transitional Late Prehistoric phases.  
- Early protohistoric networks prior to sustained European intrusion.

This dataset is an interpretive, generalized model, **not** a fixed cultural boundary or territorial claim.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/central-plains-exchange/
├── 📄 README.md                                  # This file
├── 📄 central-plains-exchange.geojson            # Generalized MultiPolygon representation
├── 📂 stac/                                      # STAC Collection + Item(s)
│   └── 📄 central-plains-exchange-v1.json        # STAC Item (generalized)
├── 📂 metadata/                                  # DCAT + CARE + KFM metadata
│   └── 📄 central-plains-exchange-v1.json
└── 📂 provenance/                                # PROV-O lineage + review logs
    └── 📄 central-plains-exchange-v1.json
~~~

IDs like `central-plains-exchange-v1` must match across GeoJSON, STAC, metadata, and provenance.

---

## 🌀 Cultural Definition

| Dimension             | Description                                                                 |
|-----------------------|-----------------------------------------------------------------------------|
| **Cultural Cohesion** | Shared house forms, ceramic typologies, mound and village features (generalized). |
| **Exchange Networks** | Raw-material flows (for example, Flint Hills sources into Republican/Platte basins). |
| **Settlement Dynamics** | Semi-sedentary villages with horticulture and bison exploitation.       |
| **Environmental Context** | Tallgrass–shortgrass prairie transitions, alluvial valleys, ecotonal mosaics. |
| **Subsistence**       | Mixed horticulture, bison hunting, broad-spectrum resource use.            |
| **Multi-Phase Overlap** | Legacies of Plains Woodland and early Caddoan systems, Late Prehistoric transitions. |

Interpretations are based on published archaeological and environmental research; expressions here are **generalized** to protect sensitive landscapes.

---

## 🌍 Spatial Representation

Spatial representation uses:

- A **generalized MultiPolygon** describing the exchange interaction region.  
- H3-based generalization (for example, levels r5–r7) or equivalent discretion as determined by schemas and provenance.  
- CRS: **EPSG:4326** for all public-facing geometry and bounding boxes.

Generalization is mandatory for:

- Sensitive village landscapes.  
- High-density artifact distributions or specific site clusters.  
- Any spatial representation that could imply restricted cultural knowledge or site-level detail.

All generalization parameters and methods must be documented in `provenance/central-plains-exchange-v1.json`.

---

## 🕰️ Temporal Context

| Phase                        | Approx. Dates | Notes                                                   |
|------------------------------|--------------|---------------------------------------------------------|
| Early Central Plains Tradition | AD 900–1050 | Initial formation of regional coherence                 |
| Middle CPT                   | AD 1050–1250 | Peak cultural exchange and settlement expansion         |
| Late CPT / Transitional      | AD 1250–1400 | Greater mobility and interaction with neighboring spheres (e.g., Great Bend) |

Temporal coverage must be OWL-Time–compatible and match:

- DCAT `dct:temporal`.  
- STAC `extent.temporal` / Item-level temporal properties.  
- KFM cultural-phase ontology used in graph and narrative systems.

---

## 📦 STAC Item Summary (Excerpt)

The main STAC Item is stored at:

- `stac/central-plains-exchange-v1.json`

Illustrative snippet:

~~~json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "central-plains-exchange-v1",
  "bbox": [-103.0, 36.8, -94.5, 43.2],
  "geometry": {
    "type": "MultiPolygon",
    "coordinates": [
      [ /* generalized coordinates */ ]
    ]
  },
  "properties": {
    "kfm:domain": "archaeology-cultural-landscapes",
    "kfm:region_type": "interaction_sphere",
    "kfm:culture_phase": ["CPT-Early", "CPT-Middle", "CPT-Late"],
    "kfm:generalization": "H3-r7",
    "care:sensitivity": "generalized",
    "care:review": "faircare",
    "kfm:provenance": "../provenance/central-plains-exchange-v1.json"
  }
}
~~~

The full STAC Item must validate against schemas under `../../stac/schemas/`.

---

## ⚖️ Cultural & Ethical Considerations (FAIR+CARE)

The **Central Plains Exchange Interaction Sphere** is culturally significant for multiple descendant Indigenous communities and must be treated accordingly.

### Mandatory Rules

- No exact settlement coordinates in public-facing products.  
- No explicit sacred or ceremonial boundary geometries.  
- No restricted ethnographic or oral-history content without explicit consent.  
- Narrative framing must:
  - Avoid colonial language and deterministic interpretations.  
  - Emphasize the interpretive nature and uncertainty of inferred boundaries.  
- Spatial generalization is enforced for sensitive contexts.

### CARE Metadata Expectations

In metadata and STAC:

- `care:sensitivity: "generalized"` (baseline public-governed stance).  
- `care:review: "faircare"` (additional tribal review may be recommended where overlaps with specific descendant communities arise).  
- `care:notes`: must describe:
  - Generalization strategy.  
  - Removed/filtered content.  
  - Major ethical decisions.  
- `care:visibility_rules`: typically `"polygon-generalized"`; can be tightened to `"h3-only"` for any especially sensitive zones.

CARE settings must remain consistent across:

- STAC Items (`stac/central-plains-exchange-v1.json`).  
- Metadata (`metadata/central-plains-exchange-v1.json`).  
- Provenance (`provenance/central-plains-exchange-v1.json`).

---

## 🧪 Provenance Requirements (PROV-O)

The provenance file:

- `provenance/central-plains-exchange-v1.json`

MUST document:

- Raw input sources:
  - Literature, open GIS datasets, PD resources, etc.  
- Spatial and attribute transformations:
  - H3 generalization, simplification tolerances, normalization steps.  
- Integrative modeling:
  - How multiple streams of evidence were combined to define the interaction sphere.  
- Ethical and CARE review:
  - FAIR+CARE review details.  
  - Any recorded tribal advisory review.  
- Timeline and agent information:
  - Key activities with `prov:startTime` and `prov:endTime`.  
  - Analysts, reviewers, and institutional agents involved.

Provenance must validate against interaction-sphere provenance schemas and follow templates defined in:

- `../../provenance/templates/`

---

## 🧠 Integration Into KFM Ecosystem

### Knowledge Graph

From this dataset, ingestion will create/enrich:

**Nodes**

- `InteractionSphere` (Central Plains Exchange).  
- `CulturalPhase` nodes for CPT phases.  
- `CulturalRegion` / `GeneralizedRegion` nodes.  
- `MetadataRecord` and CARE-related nodes.

**Relationships**

- `HAS_METADATA` (InteractionSphere → MetadataRecord).  
- `HAS_PROVENANCE` (InteractionSphere → ProvenanceRecord).  
- `HAS_CARE_SENSITIVITY` (InteractionSphere → CARE node).  
- `OCCURRED_DURING` (InteractionSphere → CulturalPhase / TimeInterval).  
- `ASSOCIATED_WITH` (links to artifact inventories, landscape layers, Story Nodes).

### Story Nodes

- Provide region-level context for CPT-related narratives.  
- Support cross-sphere narratives (for example, interactions between CPT and Great Bend Aspect).  
- Provide generalized interaction scaffolding for time-sliced stories.

### Focus Mode v3

- Uses metadata, STAC, and provenance to:
  - Generate sensitivity-aware explanations.  
  - Place the interaction sphere in time and space.  
  - Indicate data quality and interpretive uncertainty.  
  - Attach provenance chips and CARE badges.

---

## 📊 Dataset Status (Illustrative)

| Version | Status   | Review     | Notes                                                        |
|--------:|----------|-----------|--------------------------------------------------------------|
| v1      | 🟢 Active | 2025-11   | Generalized; STAC/DCAT/CARE validated; provenance linked.    |

Authoritative status is maintained in release manifests and governance records.

---

## 🔗 Related Specifications

- `../README.md`  
  – Interaction-spheres dataset overview and governance.  
- `../stac/README.md`  
  – Great Bend Aspect / Central Plains Exchange STAC catalog documentation.  
- `../metadata/README.md`  
  – Interaction-sphere metadata standards.  
- `../provenance/README.md`  
  – Provenance standards and patterns for interaction spheres.  
- `../../metadata/README.md`  
  – Global interaction-sphere metadata standards.

---

## 🕰 Version History

| Version   | Date       | Author                                   | Summary                                                                 |
|-----------|------------|------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3   | 2025-12-02 | Cultural Landscape WG · FAIR+CARE Council | Updated for KFM v11.2.3; aligned with interaction-sphere STAC/metadata/provenance schemas; added telemetry references. |
| v10.4.0   | 2025-11-17 | Cultural Landscape WG · FAIR+CARE Council | Initial release of Central Plains Exchange interaction-sphere dataset documentation. |
| v10.0.0   | 2025-11-10 | Landscape Modeling Team                  | Prototype polygons and early metadata drafts.                           |

---

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
FAIR+CARE · Sovereignty-Aligned  
KFM-MDP v11.2.2 · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Interaction Spheres](../README.md)
