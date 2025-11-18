---
title: "🌿🌾 Kansas Frontier Matrix — Cultural Landscapes: Ecological Affordance Results (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/cultural-landscapes/ecological-affordances/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly / Archaeology Working Group · Paleoenvironment WG · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/archaeology-cultural-landscape-ecological-affordances-v1.json"
governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Results"
intent: "archaeology-cultural-landscapes-ecological-affordances"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
indigenous_rights_flag: true
data_steward: "Archaeology WG · Paleoenvironment WG · FAIR+CARE Council"
risk_category: "Environmental Interpretation"
redaction_required: false
provenance_chain:
  - "docs/analyses/archaeology/results/cultural-landscapes/ecological-affordances/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E27 Site"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"
  owl_time: "TemporalEntity"
json_schema_ref: "../../../../../../schemas/json/archaeology-cultural-landscape-ecological-affordances.schema.json"
shape_schema_ref: "../../../../../../schemas/shacl/archaeology-cultural-landscape-ecological-affordances-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:cultural-landscapes:ecological-affordances-v11.0.0"
semantic_document_id: "kfm-arch-cultural-landscapes-ecological-affordances"
event_source_id: "ledger:docs/analyses/archaeology/results/cultural-landscapes/ecological-affordances/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "contextual-environment-linking"
ai_transform_prohibited:
  - "cultural-identity-derivation"
  - "restricted-landscape-inference"
  - "site-proximity-prediction"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Internal / CARE-Governed"
role: "archaeology-cultural-landscapes-ecological-affordances-root"
lifecycle_stage: "stable"
ttl_policy: "Review every 6 months"
sunset_policy: "Superseded upon next affordance synthesis"
---

<div align="center">

# 🌿🌾 **Cultural Landscapes — Ecological Affordance Results**  
`docs/analyses/archaeology/results/cultural-landscapes/ecological-affordances/README.md`

**Purpose:**  
Summarize all **ecological affordance result layers** supporting cultural-landscape interpretations within the Kansas Frontier Matrix (KFM).  
These affordance layers encapsulate environmental opportunities, constraints, and landscape potentials relevant to generalized settlement patterns, mobility, and cross-period land-use tendencies—**without revealing sensitive cultural geographies or site-level detail**.

</div>

---

## 📘 Overview

Ecological affordance results describe how combinations of:

- hydrology  
- soils  
- vegetation  
- terrain  
- climate  
- seasonal conditions  

shape the **potential usability** of landscapes over long temporal spans.

These affordances:

- are **environmental**, not cultural attributions  
- use **H3 r7+ generalization**  
- remain fully compliant with **FAIR+CARE**  
- support **Focus Mode** narrative context  
- integrate with **Story Node v3** environmental backdrops  
- are grounded in paleoenvironment, hydrology, and geomorphology datasets  

No outputs infer tribal territory, identity, sovereignty claims, sacred landscapes, or restricted ecological knowledge.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/results/cultural-landscapes/ecological-affordances/
├── README.md                                   # This file
├── soils/                                      # Soil suitability & resource indicators
├── vegetation/                                 # Biomass, ecozone, resource zones
├── hydrology/                                  # Hydrology-affordance models
├── terrain/                                    # Slope, ruggedness, elevation potentials
├── climate/                                    # Climate-linked affordance scores
├── seasonality/                                # Seasonal affordance (winter/summer)
├── composite/                                  # Aggregated multi-factor affordance surfaces
├── uncertainty/                                # Uncertainty + proxy disagreement layers
├── stac/                                       # STAC Items for affordance outputs
├── metadata/                                   # DCAT + JSON-LD metadata
└── provenance/                                 # PROV-O lineage & modeling logs
~~~

---

## 🌱 Soil Affordance Results (`soils/`)

Includes:

- drainage classes  
- fertility indices  
- pedogenic stability  
- resource-gathering suitability  
- soil–hydrology interaction models  

Ecological only — never cultural.

---

## 🌾 Vegetation Affordances (`vegetation/`)

Includes:

- ecozone boundaries  
- productivity surfaces  
- vegetation stability zones  
- forage potential layers  

All generalized, no species linked to cultural practices.

---

## 💧 Hydrology Affordances (`hydrology/`)

Includes:

- perennial/ephemeral water proximity  
- floodplain stability  
- terrace accessibility  
- seasonal water availability  

Hydrology-linked suitability is **environmental only**.

---

## 🏞️ Terrain Affordances (`terrain/`)

Contains:

- slope-grade potential  
- ruggedness vs mobility cost  
- elevation-linked affordances  
- terrain variability surfaces  

Used for generalized mobility insights.

---

## 🌡️ Climate Affordances (`climate/`)

Includes:

- long-term climate suitability  
- moisture balance  
- drought/wet cycle impacts  
- seasonally stable regions  

Environmental context only.

---

## ❄️☀️ Seasonal Affordance Layers (`seasonality/`)

Captures:

- winter mobility barriers  
- summer resource windows  
- seasonal hydrology patterns  
- climatic extremes  

Critical for time-aware landscape modeling.

---

## 🧮 Composite Affordance Models (`composite/`)

Aggregated layers combining:

- hydrology  
- soils  
- climate  
- terrain  
- vegetation  

Outputs feed:

- predictive cultural-landscape models  
- environmental narrative generators  
- Story Node v3 summaries  

---

## ⚠️ Ecological Affordance Uncertainty (`uncertainty/`)

Includes:

- uncertainty rasters  
- proxy disagreement maps  
- spatial confidence scores  
- environmental model limitations  

Displayed in Focus Mode as **Affordance Confidence Chips**.

---

## 🧬 Metadata & PROV-O Requirements

### **STAC (`stac/`)**
Affordance STAC Items must include:

- H3 geometry only  
- dataset cross-links  
- uncertainty fields  
- CARE labels  
- environmental domain flags  
- explainability artifacts (if AI-assisted)

### **DCAT (`metadata/`)**
Documents:

- dataset purpose  
- environmental drivers  
- FAIR+CARE governance  
- distribution metadata  

### **PROV-O (`provenance/`)**
Tracks:

- datasets used  
- modeling pipelines  
- transformations  
- generalization processes  
- uncertainty propagation  

All outputs must pass CI validation.

---

## 🧠 Focus Mode Integration

Ecological affordance layers inform:

- environmental explanations  
- corridor & mobility reasoning  
- temporal affordance transitions  
- general settlement landscape narratives  

Example Focus Summary:

> **Focus Summary:**  
> Ecological affordance layers suggest broad hydrology–soil–vegetation stability zones that align with generalized cultural-landscape patterns. These insights are environmental and fully CARE-governed.

---

## 🛡️ CARE & Ethical Requirements

All outputs must:

- avoid cultural attribution  
- avoid projecting identity, motives, or meaning  
- be spatially generalized (H3 r7+)  
- disclose uncertainty  
- avoid sensitive ecological knowledge  
- undergo FAIR+CARE review  

If the dataset presents cultural risk → it must be **masked or declined**.

---

## 🕰️ Version History

| Version | Date       | Author                                  | Summary |
|--------:|------------|-----------------------------------------|---------|
| v11.0.0 | 2025-11-17 | Archaeology WG · Paleoenvironment WG · FAIR+CARE Council | Initial ecological-affordance results registry. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Ecological Affordance Results · CARE-Governed · FAIR+CARE Certified  
MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Cultural Landscape Results](../README.md)

</div>