---
title: "🪶 Kansas Frontier Matrix — Protohistoric Wichita Interaction Sphere (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/protohistoric-wichita/README.md"
description: "High-sensitivity, sovereignty-governed interaction-sphere dataset for the Protohistoric Wichita cultural landscape in KFM v11."
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Cultural Landscape Working Group · FAIR+CARE Council · Tribal Advisory Review Required"
content_stability: "stable"
status: "Active / Enforced (Tribal Review Required)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_uuid: "urn:kfm:doc:archaeology-protohistoric-wichita-interaction-sphere-v11.2.3"
doc_kind: "Dataset"
intent: "cultural-landscape-interaction-sphere-protohistoric-wichita"
semantic_document_id: "kfm-doc-archaeology-protohistoric-wichita-interaction-sphere-v11.2.3"
category: "Analyses · Archaeology · Cultural Landscapes"

sbom_ref: "../../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/archaeology-protohistoric-wichita-v1.json"
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
  - "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/protohistoric-wichita/README.md@v10.4.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true
---

# 🪶 Protohistoric Wichita Interaction Sphere (v11)

`docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/protohistoric-wichita/README.md`

**Purpose**  
Define, document, and ethically govern the **Protohistoric Wichita Interaction Sphere**, a high-sensitivity, multi-layer interaction region spanning approximately **AD 1500–1700**, during which ancestral Wichita groups engaged in:

- Widespread mobility and seasonal movements  
- Trade and exchange within and beyond the Central Plains  
- Diplomatic and social relationships with neighboring groups  
- Early European contact and its consequences  

This dataset is treated with **high cultural sensitivity** under **CARE and sovereignty policies**, with **mandatory tribal review**.

---

## ⚠️ Cultural Sensitivity Statement

The Protohistoric Wichita Interaction Sphere includes culturally significant, descendant-community–relevant information tied to:

- Early colonial contact  
- Migration and relocation  
- Ceremonial interactions and alliances  
- Trade, diplomacy, and potential conflict/displacement  

Therefore:

- **No exact settlement, burial, ceremonial, or sacred locations** are included.  
- All geometries are **highly generalized** (polygon simplification + H3 mosaics).  
- **Tribal review is required** before any public-facing publication or structural modification.  
- Narrative framing must:
  - Avoid colonial or essentialist terminology.  
  - Acknowledge uncertainty and contested interpretations.  
  - Respect descendant-community perspectives.

---

## 📘 Overview

The **Protohistoric Wichita Interaction Sphere** models an evolving, generalized cultural landscape bridging:

- Late **Great Bend Aspect** continuity and transformations  
- Emergence of **protohistoric Wichita identities**  
- Interactions with **Caddoan**, **Plains Apache**, proto-**Pawnee**, and other groups  
- Shifting settlement dynamics along the:
  - **Arkansas**, **Walnut**, **Ninnescah**, and **Little Arkansas** Rivers  
- Expanding trade networks (metal, shell, pigments, stone, other materials)  
- Selectively included oral histories and ethnohistoric synthesis  
  - Only at generalized scales and **only when explicitly reviewed and approved**

This sphere is a **generalized interpretive model**, **not** a territorial claim or fixed boundary.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/protohistoric-wichita/
├── 📄 README.md                               # This file
├── 📄 protohistoric-wichita.geojson           # Generalized MultiPolygon (H3-based mosaic)
├── 📂 stac/
│   └── 📄 protohistoric-wichita-v2.json       # STAC Item for this interaction sphere
├── 📂 metadata/
│   └── 📄 protohistoric-wichita-v2.json       # DCAT + CARE metadata
└── 📂 provenance/
    └── 📄 protohistoric-wichita-v2.json       # PROV-O lineage & tribal review record
~~~

File IDs (`protohistoric-wichita-v2`) should be consistent across GeoJSON, STAC, metadata, and provenance.

---

## 🧭 Cultural Definition

### Cultural Identity

- Descendant communities of Late Great Bend Aspect complexes  
- Emerging **Wichita-speaking** communities in the Central Plains  
- Complex interactions with:
  - Caddoan groups  
  - Plains Apache groups  
  - Proto-Pawnee and allied communities  

### Subsistence & Economy

- Mixed horticulture: maize, beans, squash, and other crops  
- Bison hunting (communal and opportunistic)  
- Seasonal mobility between prairie, riparian, and wooded ecotones  

### Trade & Diplomacy

- Broad exchange networks (stone, metals, pigments, shells, and other materials)  
- Possible contact with early Spanish expeditions and other colonial-era parties  
  - Treated as **high-sensitivity** topics subject to sovereignty review  
- Riverine mobility corridors linking settlement clusters and interaction hubs  

---

## 🌍 Spatial Representation

The spatial representation of this interaction sphere uses:

- **Generalized MultiPolygon** geometries  
- **H3 generalization (levels r5–r8)** or equivalent discretization  
- CRS: **EPSG:4326** for all public-facing datasets and STAC Items  

Explicitly avoided:

- Site-level geometries or clusters that could expose sensitive locations  
- Sacred landscape geometries and known ceremonial centers  
- Direct visualization of protected or confidential archaeological site distributions  

Generalization choices must be logged in the `transformations-log.csv` and PROV-O provenance.

---

## 🕰 Temporal Context

| Phase                | Approx. Dates | Notes                                                    |
|----------------------|--------------|----------------------------------------------------------|
| Early Protohistoric  | AD 1500–1580 | Transition from Late Prehistoric patterns and Great Bend Aspect continuity |
| Middle Protohistoric | AD 1580–1650 | Highest mobility and trade activity; complex contact zones |
| Late Protohistoric   | AD 1650–1700 | Reorganization under colonial-era pressures and population shifts |

Temporal metadata is encoded in DCAT and STAC (OWL-Time–compatible intervals) and should align with Story Node timelines.

---

## 📦 STAC Item Summary (Excerpt)

~~~json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "protohistoric-wichita-v2",
  "bbox": [-102.2, 36.8, -94.7, 40.6],
  "properties": {
    "kfm:domain": "archaeology-cultural-landscapes",
    "kfm:culture_phase": ["Protohistoric-Wichita"],
    "kfm:region_type": "interaction_sphere",
    "kfm:generalization": "H3-r7",
    "care:sensitivity": "restricted-generalized",
    "care:review": "tribal",
    "care:sovereignty": "protected",
    "care:consent_status": "conditional",
    "kfm:provenance": "../provenance/protohistoric-wichita-v2.json"
  }
}
~~~

The full STAC Item is stored in `stac/protohistoric-wichita-v2.json` and must validate against the interaction-sphere STAC schemas.

---

## ⚖️ FAIR+CARE Cultural Governance

### Required Protections

- **Tribal review mandatory** for any substantive data or narrative change.  
- **No depiction** of sensitive ceremonial or sacred geographies in public-facing products.  
- **Strict generalization** (H3 + polygon simplification) for spatial features.  
- Language and metadata MUST avoid:
  - Colonial, extractive, or essentialist framing.  
  - Unsupported assertions about ownership or historical claims.  

### CARE Fields (Normative Expectations)

- `care:sensitivity: "restricted-generalized"` for the primary public interaction sphere.  
- `care:review: "tribal"` plus FAIR+CARE council review.  
- `care:notes`: MUST document cultural review outcomes and any conditions.  
- `care:visibility_rules: "h3-only"` for public-facing STAC/visualizations, unless explicitly relaxed via sovereignty policy.  

CARE and sovereignty rules must be reflected consistently in:

- STAC Items  
- DCAT/metadata  
- PROV-O provenance logs  

---

## 🧪 Provenance Requirements (PROV-O + KFM Extensions)

The provenance file (`provenance/protohistoric-wichita-v2.json`) MUST describe:

- Data origins:
  - Archaeological literature, PD datasets, tribally-approved sources, and ethnohistoric synthesis.  
- Processing steps:
  - Georeferencing, digitization, generalization, aggregation, modeling.  
- Cultural review:
  - Summary of tribal and FAIR+CARE review, including dates and decision outcomes.  
- Ethical decisions:
  - What was omitted, generalized, or redacted; why and at whose request.  
- Model assumptions and uncertainties:
  - Where interpretation is speculative vs. well-supported.  
- Timestamps and agents:
  - `prov:Activity` with `prov:startTime`/`prov:endTime`.  
  - `prov:Agent` entries for analysts, reviewers, and institutions.  

This log must validate against interaction-sphere provenance schemas and follow the interaction-sphere provenance template guidance.

---

## 🧠 Integration Into the KFM Ecosystem

### Knowledge Graph (Neo4j)

This interaction sphere will appear as:

**Nodes**

- `InteractionSphere` (Protohistoric Wichita)  
- `CulturalPhase` (phases listed above)  
- `CulturalRegion` / `EnvironmentalZone` as context nodes  

**Relationships**

- `ASSOCIATED_WITH` (InteractionSphere ↔ ArtifactInventories / StoryNodes)  
- `GENERALIZED_FROM` (public geometries ↔ internal higher-resolution representations where stored)  
- `OCCURRED_DURING` (InteractionSphere ↔ CulturalPhase / TimeInterval)  
- `HAS_PROVENANCE` (InteractionSphere ↔ ProvenanceRecord)  
- `HAS_CARE_SENSITIVITY` (InteractionSphere ↔ CARE/Sensitivity node)

### Story Nodes

Supports:

- Protohistoric movement and interaction narratives.  
- Cultural diffusion sequences and exchange networks.  
- Stories highlighting uncertainty and multiple perspectives.

### Focus Mode v3

- Applies **ethical warning banners** for high-sensitivity content.  
- Attaches **provenance chips** linking to provenance logs and metadata.  
- Dynamically enforces CARE and sovereignty filters in responses.

---

## 📊 Dataset Status (Illustrative)

| Version | Status      | Review                   | Notes                                                         |
|--------:|------------|--------------------------|---------------------------------------------------------------|
| v2      | 🟡 Review   | Tribal + FAIR+CARE       | High-sensitivity dataset; cannot be fully public-facing until review completed. |
| v1      | 🟥 Deprecated | Tribal Review Required | Superseded by v2; retained only for internal lineage.        |

Authoritative status and review disposition are in release manifests and governance records.

---

## 🔗 Related Specifications

- `../README.md`  
  – Interaction Spheres overview and governance.  
- `../stac/README.md`  
  – STAC catalog for interaction spheres (Items + Collections).  
- `../stac/items/README.md`  
  – STAC Items requirements for interaction spheres.  
- `../metadata/README.md`  
  – DCAT + CARE metadata for interaction spheres.  
- `../provenance/README.md`  
  – Interaction-sphere provenance index and standards.

---

## 🕰 Version History

| Version   | Date       | Author                                           | Summary                                                                 |
|-----------|------------|--------------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3   | 2025-12-02 | Cultural Landscape WG · FAIR+CARE Council · Tribal Advisors | Updated to KFM v11.2.3; aligned with interaction-sphere STAC/metadata/provenance schemas; clarified CARE/sovereignty expectations and Focus Mode v3 use. |
| v10.4.0   | 2025-11-17 | Cultural Landscape WG · FAIR+CARE Council · Tribal Advisors | First standardized v10.4 documentation of Protohistoric Wichita Interaction Sphere. |
| v10.0.0   | 2025-11-12 | Landscape Modeling Team                          | Initial generalized polygon prototype and conceptual notes.            |

---

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
FAIR+CARE · Sovereignty-Governed  
KFM-MDP v11.2.2 · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Interaction Spheres](../README.md)
