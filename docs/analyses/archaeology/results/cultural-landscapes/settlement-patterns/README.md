---
title: "🏘️🌾 Kansas Frontier Matrix — Cultural Landscapes: Settlement Pattern Results (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/cultural-landscapes/settlement-patterns/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly / Archaeology WG · Cultural Landscape WG · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/archaeology-cultural-landscape-settlement-patterns-v1.json"
governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Results"
intent: "archaeology-cultural-landscape-settlement-patterns"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed / Generalized Settlement Patterns"
sensitivity_level: "High"
public_exposure_risk: "Medium"
indigenous_rights_flag: true
data_steward: "Archaeology WG · FAIR+CARE Council"
risk_category: "Settlement Pattern Interpretation"
redaction_required: true
provenance_chain:
  - "docs/analyses/archaeology/results/cultural-landscapes/settlement-patterns/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E27 Site"
  schema_org: "Place"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"
  owl_time: "TemporalEntity"
json_schema_ref: "../../../../../../schemas/json/archaeology-cultural-landscape-settlement-patterns.schema.json"
shape_schema_ref: "../../../../../../schemas/shacl/archaeology-cultural-landscape-settlement-patterns-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:cultural-landscapes:settlement-patterns-v11.0.0"
semantic_document_id: "kfm-arch-cultural-landscapes-settlement-patterns"
event_source_id: "ledger:docs/analyses/archaeology/results/cultural-landscapes/settlement-patterns/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Restricted"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "environmental-context-linking"
ai_transform_prohibited:
  - "site-level inference"
  - "tribal identity attribution"
  - "reconstruction of restricted cultural geographies"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Internal / CARE-Governed"
role: "archaeology-cultural-landscapes-settlement-patterns-root"
lifecycle_stage: "stable"
ttl_policy: "Review every 6 months"
sunset_policy: "Superseded upon next settlement-pattern synthesis"
---

<div align="center">

# 🏘️🌾 **Cultural Landscapes — Settlement Pattern Results**  
`docs/analyses/archaeology/results/cultural-landscapes/settlement-patterns/README.md`

**Purpose:**  
Provide **generalized, FAIR+CARE–aligned settlement-pattern analyses** for use in cultural landscape reconstruction within the Kansas Frontier Matrix (KFM).  
These results describe **landscape-scale tendencies** in archaeological settlement distributions—never exact locations, cultural boundaries, nor restricted Indigenous knowledge.

</div>

---

## 📘 Overview

KFM settlement-pattern results synthesize:

- H3 r7+ generalized site density surfaces  
- cluster persistence tendencies  
- eco-hydrological settlement correlation patterns  
- terrain/soil/hydrology/climate-based settlement affordances  
- temporal changes in settlement density (OWL-Time aligned)  
- environmental predictors from ML/GAM models  
- uncertainty layers and proxy agreement patterns  

These outputs are used to describe **broad-scale, environmental settlement patterns** without implying:

- specific historic or cultural decisions  
- cultural ownership of landscape  
- tribal or social identity correlations  
- sacred or restricted geography  

All outputs undergo FAIR+CARE review and PROV-O lineage validation.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/results/cultural-landscapes/settlement-patterns/
├── README.md                                   # This file
├── density/                                    # Generalized H3 + KDE settlement density surfaces
├── clusters/                                   # Environmental + spatial settlement cluster patterns
├── hydrology/                                  # Settlement–hydrology correlation tendencies
├── soil/                                       # Soil-linked settlement tendencies
├── vegetation/                                 # Ecozone & biomass correlation summaries
├── terrain/                                    # Terrain-linked settlement patterns
├── climate/                                    # Climate & seasonality influences
├── temporal/                                   # OWL-Time aligned settlement dynamics
├── composite/                                  # Multi-factor aggregated settlement-pattern models
├── uncertainty/                                # Uncertainty, variance, proxy disagreement
├── stac/                                       # STAC Items for settlement-pattern layers
├── metadata/                                   # DCAT + JSON-LD metadata
└── provenance/                                 # PROV-O lineage tracking all modeling steps
~~~

---

## 🧱 Settlement Pattern Types

### **1️⃣ Density Surfaces (`density/`)**
Contain:

- H3 aggregated density maps  
- KDE-derived generalized settlement intensities  
- eco-hydrological overlays  
- uncertainty surfaces  

No point-level data.

---

### **2️⃣ Settlement Clusters (`clusters/`)**
Represent:

- environmental clustering tendencies  
- multi-factor cluster generalizations  
- spatially smoothed cluster envelopes  
- cluster–corridor relationships  

All cluster boundaries are heavily generalized.

---

### **3️⃣ Hydrology-Linked Patterns (`hydrology/`)**
Describe:

- settlement tendencies along terraces & floodplains  
- perennial water adjacency patterns  
- seasonal water-use affordances  

Environmental only, no cultural attribution.

---

### **4️⃣ Soil-Based Patterns (`soil/`)**
Include:

- soil stability  
- fertility indices  
- pedogenic influence patterns  

---

### **5️⃣ Vegetation & Biomass Patterns (`vegetation/`)**
Include:

- ecozone transition zones  
- biomass productivity correlation layers  
- vegetation stability surfaces  

---

### **6️⃣ Terrain-Based Patterns (`terrain/`)**
Model:

- slope-linked settlement tendencies  
- elevation preference tendencies  
- ruggedness constraints  

Generalized across regions.

---

### **7️⃣ Climate-Linked Patterns (`climate/`)**
Include:

- moisture balance  
- drought/wet frequency suitability  
- seasonal limitations  

---

### **8️⃣ Temporal Settlement Tendencies (`temporal/`)**
Use OWL-Time to define:

- broad occupation windows  
- multi-period settlement shifts  
- long-term tendencies (NOT chronologies)  

---

### **9️⃣ Composite Models (`composite/`)**
Integrate:

- hydrology  
- soils  
- climate  
- vegetation  
- terrain  
- uncertainty  

Output: multi-factor environmental suitability for generalized settlement, **not predictions of actual settlement**.

---

## ⚠️ Uncertainty Layers (`uncertainty/`)

Contain:

- model variance  
- proxy disagreement  
- environmental range envelopes  
- cluster stability metrics  

Used in Focus Mode as **Settlement Confidence Chips**.

---

## 🧬 Metadata & Provenance

### **STAC (`stac/`)**
Must include:

- H3-based geometry  
- environmental driver metadata  
- uncertainty layers  
- CARE classifications  
- lineage pointers  

### **DCAT (`metadata/`)**
Includes:

- dataset scope  
- environmental purpose  
- FAIR+CARE metadata  
- licensing & distribution  

### **PROV-O (`provenance/`)**
Tracks:

- input datasets  
- modeling algorithms  
- generalization rules  
- smoothing & interpolation  
- uncertainty propagation  
- full WAL → Retry → Rollback lineage  

All outputs must pass CI validation.

---

## 🧠 Focus Mode Integration

Settlement patterns fuel:

- environmental context blocks  
- narrative-safe settlement tendency summaries  
- multi-period pattern exploration  
- Story Node v3 environmental scaffolding  
- disambiguation of predictive model outputs  

Example Focus Summary:

> **Focus Summary:**  
> Settlement pattern modeling reveals broad hydrology- and terrain-linked tendencies across Kansas. These are environmental generalizations, not cultural predictions, and all spatial data is H3-masked for sovereignty protection.

---

## 🛡️ CARE & Ethical Requirements

All settlement-pattern outputs must:

- avoid cultural or tribal inference  
- avoid mapping or suggesting site locations  
- avoid implying territorial relationships  
- apply H3 r7+ generalization  
- disclose uncertainty  
- undergo FAIR+CARE review  
- maintain environmental neutrality  

If any dataset risks cultural misinterpretation → it must be masked or excluded.

---

## 🕰️ Version History

| Version | Date       | Author                                   | Summary |
|--------:|------------|------------------------------------------|---------|
| v11.0.0 | 2025-11-17 | Archaeology WG · Cultural Landscape WG · FAIR+CARE Council | Initial settlement-pattern results registry under KFM-MDP v11. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Settlement Pattern Results · CARE-Governed · FAIR+CARE Certified  
MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Cultural Landscape Results](../README.md)

</div>