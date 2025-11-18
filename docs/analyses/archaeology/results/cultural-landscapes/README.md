---
title: "🌾 Kansas Frontier Matrix — Cultural Landscape Results (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/cultural-landscapes/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly / Archaeology Working Group · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/archaeology-cultural-landscape-results-v1.json"
governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Results"
intent: "archaeology-cultural-landscapes"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed"
sensitivity_level: "High"
public_exposure_risk: "Medium"
indigenous_rights_flag: true
data_steward: "Archaeology Working Group · FAIR+CARE Council"
risk_category: "Cultural Landscape Analysis"
redaction_required: true
provenance_chain:
  - "docs/analyses/archaeology/results/cultural-landscapes/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E27 Site"
  schema_org: "Place"
  prov_o: "prov:Entity"
  owl_time: "TemporalEntity"
json_schema_ref: "../../../../../schemas/json/archaeology-cultural-landscape-results.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/archaeology-cultural-landscape-results-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:cultural-landscape-results-v11.0.0"
semantic_document_id: "kfm-arch-results-cultural-landscapes"
event_source_id: "ledger:docs/analyses/archaeology/results/cultural-landscapes/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Restricted"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "contextual-linking"
ai_transform_prohibited:
  - "speculative-ethnogenesis"
  - "precise-boundary-inference"
  - "unauthorized-cultural-attribution"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Internal / CARE-Governed"
role: "archaeology-cultural-landscape-results-root"
lifecycle_stage: "stable"
ttl_policy: "Review every 6 months"
sunset_policy: "Superseded upon next cultural-landscape synthesis"
---

<div align="center">

# 🌾 **Kansas Frontier Matrix — Cultural Landscape Results**  
`docs/analyses/archaeology/results/cultural-landscapes/README.md`

**Purpose:**  
Provide a comprehensive, FAIR+CARE–aligned synthesis of **cultural landscape results** derived from archaeological data, environmental reconstructions, hydrological modeling, spatial analyses, and predictive modeling within the Kansas Frontier Matrix (KFM).  

These outputs describe **generalized**, ethically governed cultural-landscape patterns across Kansas from prehistoric through protohistoric periods.

</div>

---

## 📘 Overview

KFM cultural landscape results integrate:

- archaeological datasets (generalized)  
- hydrology & terrain analysis  
- paleoenvironmental reconstructions  
- predictive modeling (ML + GAM)  
- OWL-Time temporal sequencing  
- cultural interaction spheres  
- corridor modeling & affinity surfaces  
- Story Node v3 context layers  

These results reveal **broad-scale patterns** in:

- settlement landscapes  
- movement corridors  
- ecological affordances  
- cultural interaction systems  
- historical transitions  

While ensuring:

- **no exact site coordinates**  
- **no restricted cultural boundaries**  
- **CARE-based generalization (H3 r7/r8)**  
- **ethical, non-speculative narrative limits**  

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/results/cultural-landscapes/
├── README.md                                # This file
├── interaction-spheres/                     # Generalized cultural interaction regions
├── corridors/                                # Movement, trade, and travel corridor models
├── ecological-affordances/                   # Affordance surfaces (soils, hydrology, biomass)
├── settlement-patterns/                      # Landscape-scale settlement generalizations
├── temporal/                                 # Cultural-landscape sequences over time (OWL-Time)
├── predictive/                               # Predictive cultural-landscape modeling outputs
├── stac/                                     # STAC Items for landscape result files
├── metadata/                                 # DCAT & JSON-LD metadata
└── provenance/                               # PROV-O lineage & dataset transformation logs
~~~

---

## 🧭 Cultural Landscape Result Categories

### **1️⃣ Interaction Spheres (`interaction-spheres/`)**
Generalized representations of:

- Late Prehistoric interaction landscapes  
- Protohistoric exchange regions  
- eco-cultural territories (generalized & CARE-filtered)  

Includes:

- polygonal H3 generalizations  
- environmental correlates  
- corridor/affinity overlays  

---

### **2️⃣ Corridor Models (`corridors/`)**
AI- and GIS-derived corridor analysis:

- cost-distance models  
- hydrological corridor modeling  
- movement route probability surfaces  
- multi-scalar path networks  

All corridors are **generalized**, never exact trails.

---

### **3️⃣ Ecological Affordances (`ecological-affordances/`)**
Surfaces identifying:

- resource/activity zones  
- ecotone transitions  
- soil/vegetation suitability  
- hydrology-linked affordances  

Each layer includes FAIR+CARE metadata & uncertainty.

---

### **4️⃣ Settlement Patterns (`settlement-patterns/`)**
Landscape summaries of:

- generalized settlement density  
- H3 cluster generalizations  
- corridor adjacency patterns  
- eco-cultural interpretation anchors  

These are **patterns**, not locations.

---

### **5️⃣ Temporal Landscape Sequences (`temporal/`)**
Time-sliced landscape interpretations:

- OWL-Time interval models  
- occupation phase transitions  
- migration & dispersal patterns (generalized)  
- event-linked landscape shifts  

---

### **6️⃣ Predictive Landscape Models (`predictive/`)**
Includes ML/GAM-based prediction surfaces:

- cultural-landscape likelihood grids  
- environmental predictor analysis  
- corridor-settlement coupling models  
- uncertainty surfaces  

All predictions include **explainability overlays** and **cultural-safety checks**.

---

## 🧬 Metadata & Provenance Requirements

### **STAC**
Cultural landscape STAC Items must include:

- geometry: **H3 generalized only**  
- assets: rasters, vectors, explainability layers  
- lineage: all datasets used  
- `care:sensitivity`: always defined  
- `kfm:domain = archaeology`  

### **DCAT**
DCAT metadata documents:

- dataset purpose  
- CARE governance  
- distribution & licensing  
- temporal extent (OWL-Time)  
- thematic categories  

### **PROV-O Lineage (`provenance/`)**
Every result includes:

- modeling workflow lineage  
- source datasets  
- transformations  
- explainability artifact references  

---

## 🧠 Focus Mode Integration

These layers contribute to:

- Story Node v3 landscape narratives  
- interactive map overlays  
- cultural-landscape summaries  
- environmental context blocks  
- time-layered exploration  

A **Focus Mode–safe summary** must accompany each result.

Example:

> **Focus Summary:**  
> Generalized cultural-landscape patterns in central Kansas reflect hydrology-linked settlement and movement dynamics across Late Prehistoric and Protohistoric periods. These results are culturally safe, generalized, and aligned with FAIR+CARE sovereignty guidelines.

---

## ⚠️ CARE / Ethical Safeguards

All outputs must:

- mask sensitive cultural geographies  
- generalize boundaries with H3 r7+  
- avoid tribal identity inference  
- avoid describing sacred landscapes  
- never map exact site distributions  
- flag uncertainty transparently  

---

## 🕰️ Version History

| Version | Date       | Author                            | Summary |
|--------:|------------|-----------------------------------|---------|
| v11.0.0 | 2025-11-17 | Archaeology WG · FAIR+CARE Council | Initial cultural-landscape results registry under KFM-MDP v11.0.0. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Cultural Landscape Results · CARE-Governed · FAIR+CARE Certified  
MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Archaeology Results](../README.md)

</div>