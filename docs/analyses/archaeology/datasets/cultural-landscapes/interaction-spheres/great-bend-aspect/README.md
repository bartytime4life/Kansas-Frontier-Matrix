---
title: "🏺 Kansas Frontier Matrix — Great Bend Aspect Interaction Sphere (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/great-bend-aspect/README.md"
description: "Generalized, CARE-governed Great Bend Aspect interaction-sphere dataset for KFM v11, representing Late Prehistoric–Protohistoric cultural landscapes in central Kansas."
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Cultural Landscape Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_uuid: "urn:kfm:doc:cultural-landscape-interaction-sphere-great-bend-aspect-v11.2.3"
doc_kind: "Dataset"
intent: "cultural-landscape-interaction-sphere-great-bend-aspect"
semantic_document_id: "kfm-doc-archaeology-cultural-landscapes-great-bend-aspect-v11.2.3"
category: "Analyses · Archaeology · Cultural Landscapes"

sbom_ref: "../../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/archaeology-great-bend-aspect-v1.json"
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
  - "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/great-bend-aspect/README.md@v10.4.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true
---

# 🏺 Great Bend Aspect Interaction Sphere (v11)

`docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/great-bend-aspect/README.md`

**Purpose**  
Define, document, and ethically govern the **Great Bend Aspect Interaction Sphere**, a major Late Prehistoric–Protohistoric cultural landscape spanning central Kansas and associated (in many interpretations) with ancestral **Wichita** and related Plains horticultural groups.

This dataset integrates archaeological, geomorphological, ecological, and ethnohistoric evidence into a **generalized, culturally safe interaction region** compatible with KFM’s FAIR+CARE and sovereignty-governed standards.

---

## 📘 Overview

The **Great Bend Aspect (GBA)** represents a cohesive cultural complex typically dated to approximately **AD 1350–1700**, characterized by:

- Distinctive ceramic traditions and regional variants.  
- Semi-sedentary horticultural settlements.  
- Bison hunting and mixed subsistence strategies.  
- Earthlodge / grass-house architectural patterns.  
- Extensive trade networks (stone, shell, and later metal).  
- Regional interaction with Central Plains traditions, southern Plains groups, and early protohistoric contact routes.

In KFM v11, the GBA is modeled as a **generalized interaction sphere**, **not** as an exact territorial boundary or claim.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/great-bend-aspect/
├── 📄 README.md                               # This file
├── 📄 great-bend-aspect.geojson               # Generalized MultiPolygon representation
├── 📂 stac/
│   └── 📄 great-bend-aspect-v2.json           # STAC Item (generalized interaction sphere)
├── 📂 metadata/
│   └── 📄 great-bend-aspect-v2.json           # DCAT + CARE + KFM metadata
└── 📂 provenance/
    └── 📄 great-bend-aspect-v2.json           # PROV-O lineage & ethics / CARE review record
~~~

IDs (for example, `great-bend-aspect-v2`) must be consistent across GeoJSON, STAC, metadata, and provenance.

---

## 🧭 Cultural Definition

### Cultural Cohesion

- Highly consistent ceramics (e.g., Ninnescah / Pratt / related variants, generalized).  
- Shared house forms and subsistence strategies.  
- Dense occupation along stretches of the **Arkansas River** valley and key tributaries.  

### Interaction & Exchange

- Trade and interaction networks connecting:
  - Central Plains traditions.  
  - Southern Plains and related groups.  
  - Protohistoric exchange systems which may later intersect with colonial routes.  
- Shared features with earlier Plains Woodland and Central Plains Tradition, interpreted cautiously.

### Environmental Setting

- Prairie–riparian interface along major valleys and tributaries.  
- Hydrologically rich valley systems supporting horticulture and hunting.  
- Ecotonal transitions shaping subsistence and settlement practices.

All of the above are represented as **generalized patterns** rather than precise or exclusive locations.

---

## 🌍 Spatial Representation

The Great Bend Aspect interaction sphere is represented using:

- A **generalized MultiPolygon** describing a broad interaction region.  
- **H3 generalization (levels r5–r7)** or equivalent discretization for spatial safety.  
- CRS: **EPSG:4326** for all geometries and bounding boxes.

Avoided in public datasets:

- Exact site coordinates or tightly clustered centroids.  
- Sacred or ceremonial locations and specific site geometries.  
- Direct visualizations that allow inference of protected archaeological sites.

Spatial generalization parameters and steps must be documented in the provenance file and transformation logs.

---

## 🕰️ Temporal Context

| Sub-Phase                      | Approx. Dates | Notes                                                  |
|--------------------------------|--------------|--------------------------------------------------------|
| Early Great Bend Aspect        | AD 1350–1450 | Emergent ceramic and architectural patterns           |
| Middle Great Bend Aspect       | AD 1450–1600 | Peak settlement density and trade networks             |
| Late Great Bend / Protohistoric| AD 1600–1700 | Increasing contact and interaction; higher sensitivity |

Temporal coverage for metadata and STAC should:

- Use OWL-Time–compatible intervals (start/end).  
- Align with KFM cultural-phase ontology and Story Node / Focus Mode timelines.

---

## 📦 STAC Item Overview (Excerpt)

The STAC Item for this dataset is stored at:

- `stac/great-bend-aspect-v2.json`

Illustrative excerpt:

~~~json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "great-bend-aspect-v2",
  "bbox": [-101.8, 37.0, -95.3, 40.5],
  "geometry": {
    "type": "MultiPolygon",
    "coordinates": [
      [ /* generalized coordinates */ ]
    ]
  },
  "properties": {
    "kfm:domain": "archaeology-cultural-landscapes",
    "kfm:region_type": "interaction_sphere",
    "kfm:culture_phase": ["GBA-Early", "GBA-Middle", "GBA-Late"],
    "kfm:generalization": "H3-r7",
    "care:sensitivity": "generalized",
    "care:review": "faircare",
    "care:sovereignty": "protected",
    "kfm:provenance": "../provenance/great-bend-aspect-v2.json"
  },
  "assets": {
    "data": {
      "href": "../great-bend-aspect.geojson",
      "type": "application/geo+json",
      "roles": ["data"]
    }
  }
}
~~~

The full Item must validate against interaction-sphere STAC schemas in `../../stac/schemas/`.

---

## ⚖️ Cultural & Ethical Governance (FAIR+CARE)

The Great Bend Aspect has significant meaning for descendant communities, including Wichita and other Indigenous nations.

### Required Protections

- **No exact settlement or sacred locations** included in public artifacts.  
- **No explicit ceremonial site representation** in public layers.  
- Cultural narratives must:
  - Avoid colonial framings and overly deterministic interpretations.  
  - Emphasize variability, uncertainty, and multiple perspectives.  
- Later protohistoric or contact-related content should be reviewed in coordination with relevant communities.

### CARE Fields (typical)

In metadata and STAC:

- `care:sensitivity: "generalized"` for the general public-governed sphere.  
- `care:review: "faircare"` (with `tribal` recommended or required for more sensitive components).  
- `care:notes`: must explain spatial and cultural generalizations and any exclusions.  
- `care:visibility_rules: "polygon-generalized"` by default; may be tightened to `"h3-only"` for more sensitive regions if needed.

CARE labels and notes must be consistent across:

- STAC Item(s).  
- Metadata JSON.  
- PROV-O provenance logs.

---

## 🧪 Provenance Requirements (PROV-O)

The provenance file:

- `provenance/great-bend-aspect-v2.json`

MUST describe:

- Data origins:
  - Archaeological literature and syntheses, PD datasets, and any approved ethnohistoric summaries.  
- GIS and modeling steps:
  - Polygon generalization, H3-based mosaics, and any filtering or masking.  
- Interpretive synthesis:
  - How boundaries or zones were conceptualized and what assumptions were made.  
- Cultural and ethical review:
  - FAIR+CARE review outcomes; any voluntary tribal review results.  
- Processing metadata:
  - Scripts/tools used, timestamps, and operator identities (subject to privacy rules).

This provenance log must validate against interaction-sphere provenance schemas and follow templates defined under:

- `../../provenance/templates/`

---

## 🧠 Integration Into KFM

### Knowledge Graph (Neo4j)

From this dataset, ingestion will create/enrich:

**Nodes**

- `InteractionSphere` (Great Bend Aspect).  
- `CulturalPhase` (`GBA-Early`, `GBA-Middle`, `GBA-Late`).  
- `CulturalRegion` / `GeneralizedRegion`.  
- `MetadataRecord` and CARE-related nodes.

**Relationships**

- `HAS_METADATA` (InteractionSphere → MetadataRecord).  
- `HAS_PROVENANCE` (InteractionSphere → ProvenanceRecord).  
- `HAS_CARE_SENSITIVITY` (InteractionSphere → CARE node).  
- `OCCURRED_DURING` (InteractionSphere → CulturalPhase / TimeInterval).  
- `ASSOCIATED_WITH` (InteractionSphere ↔ artifact inventories, routes, or other layers).  

### Story Nodes

- Drives Great Bend–related cultural narratives and timelines.  
- Provides context for artifact inventories, routes, and other landscape datasets.  
- Offers generalized region-level anchoring for Story Node maps and storylines.

### Focus Mode v3

- Supplies context-aware, sensitivity-aware explanations of the Great Bend Aspect.  
- Uses provenance and metadata to:
  - Render provenance chips.  
  - Bound narratives spatially and temporally.  
  - Enforce CARE and sovereignty rules (e.g., generalization levels).

---

## 📊 Dataset Status (Illustrative)

| Version | Status   | Review       | Notes                                                   |
|--------:|----------|-------------|---------------------------------------------------------|
| v2      | 🟢 Active | 2025-11     | Generalized; CARE-reviewed; STAC/DCAT/provenance linked |

Authoritative status is maintained in release manifests, metadata, and governance records.

---

## 🔗 Related Specifications

- `../README.md`  
  – Interaction-spheres overview and cultural interpretation.  
- `../stac/README.md`  
  – Interaction Sphere STAC Catalog (Items + Collections).  
- `../stac/items/README.md`  
  – STAC Item requirements for interaction spheres.  
- `../metadata/README.md`  
  – Interaction Sphere metadata standards.  
- `../provenance/README.md`  
  – Interaction Sphere provenance standards and QA templates.

---

## 🕰 Version History

| Version   | Date       | Author                                   | Summary                                                                 |
|-----------|------------|------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3   | 2025-12-02 | Cultural Landscape WG · FAIR+CARE Council | Updated to KFM v11.2.3; aligned with interaction-sphere STAC/metadata/provenance schemas; added telemetry refs and clarified CARE notes. |
| v10.4.0   | 2025-11-17 | Cultural Landscape WG · FAIR+CARE Council | Updated generalization, metadata, STAC compliance, and governance description. |
| v10.0.0   | 2025-11-10 | Landscape Modeling Team                  | Initial draft with early polygon model and basic description.          |

---

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
FAIR+CARE · Sovereignty-Aligned  
KFM-MDP v11.2.2 · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Interaction Spheres](../README.md)
