---
title: "🔮🌾 Kansas Frontier Matrix — Cultural Landscapes: Predictive Modeling Results (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/cultural-landscapes/predictive/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly / Archaeology WG · Predictive Modeling WG · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/archaeology-cultural-landscapes-predictive-v1.json"
governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Predictive Modeling Results"
intent: "archaeology-cultural-landscapes-predictive"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed / Environmental Predictive Models"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
indigenous_rights_flag: true
data_steward: "Archaeology WG · Predictive Modeling WG · FAIR+CARE Council"
risk_category: "Environmental Predictive Interpretation"
redaction_required: false
provenance_chain:
  - "docs/analyses/archaeology/results/cultural-landscapes/predictive/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E30 Right"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"
json_schema_ref: "../../../../../../schemas/json/archaeology-cultural-landscapes-predictive.schema.json"
shape_schema_ref: "../../../../../../schemas/shacl/archaeology-cultural-landscapes-predictive-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:cultural-landscapes:predictive-results-v11.0.0"
semantic_document_id: "kfm-arch-cultural-landscapes-predictive-results"
event_source_id: "ledger:docs/analyses/archaeology/results/cultural-landscapes/predictive/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "environmental-context-linking"
ai_transform_prohibited:
  - "cultural-identity-derivation"
  - "restricted-geography-inference"
  - "precise-settlement-prediction"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Internal / CARE-Governed"
role: "archaeology-cultural-landscapes-predictive-root"
lifecycle_stage: "stable"
ttl_policy: "Review every 6 months"
sunset_policy: "Superseded upon next predictive model update"
---

<div align="center">

# 🔮🌾 **Cultural Landscapes — Predictive Modeling Results**  
`docs/analyses/archaeology/results/cultural-landscapes/predictive/README.md`

**Purpose:**  
Provide a culturally safe, environmentally grounded, FAIR+CARE–aligned collection of **predictive cultural-landscape models** used within the Kansas Frontier Matrix (KFM).  
These predictive models evaluate **environmental affordances**, **hydrology-linked potentials**, and **long-term ecological patterns** that may shape generalized cultural-landscape tendencies—without inferring cultural identity, ownership, site locations, or restricted knowledge.

</div>

---

## 📘 Overview

Predictive cultural-landscape models in KFM use **environmental variables only**, including:

- hydrology  
- soils  
- vegetation  
- terrain  
- climate  
- seasonality  
- paleoenvironmental reconstructions  
- uncertainty & model agreement metrics  

Predictive outputs identify:

- environmentally favorable regions  
- multi-factor affordance patterns  
- long-term landscape stability  
- generalized movement potentials  
- cross-period environmental tendencies  

All predictive outputs:

- are **non-deterministic**  
- are **H3 r7+ generalized**  
- **do not infer cultural behavior or decisions**  
- follow **FAIR+CARE governance**  
- include **explainability (SHAP/LIME)**  
- include **uncertainty metadata**  
- adhere to **KFM's predictive modeling ethics**  

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/results/cultural-landscapes/predictive/
├── README.md                                 # This file
├── hydrology/                                # Hydrology-linked environmental predictive surfaces
├── soils/                                     # Soil-driven suitability models
├── vegetation/                                # Biomass/ecozone predictive surfaces
├── terrain/                                   # Terrain-driven landscape predictions
├── climate/                                   # Climate & seasonality predictive models
├── composite/                                 # Multi-factor aggregated predictions
├── machine-learning/                          # ML/GAM/GLM predictive models + explainability
├── uncertainty/                               # Uncertainty, variance, model-agreement surfaces
├── stac/                                      # STAC Items for predictive outputs
├── metadata/                                  # DCAT + JSON-LD predictive metadata
└── provenance/                                # PROV-O lineage for models & transformations
~~~

---

## 🔮 Predictive Modeling Categories

### **1️⃣ Hydrology Predictive Models (`hydrology/`)**
Outputs include:

- floodplain stability likelihood  
- perennial water corridor suitability  
- terrace affordance predictions  
- hydroclimate-weighted models  

Environmental only. No cultural inference.

---

### **2️⃣ Soil-Based Predictive Models (`soils/`)**
Include:

- fertility indices  
- soil moisture stability  
- long-term pedogenic suitability  
- composite eco-hydrology predictions  

---

### **3️⃣ Vegetation Predictive Models (`vegetation/`)**
Capture:

- ecozone transitions  
- biomass production likelihoods  
- vegetation stability windows  

Used for environmental context, not cultural inference.

---

### **4️⃣ Terrain Predictive Models (`terrain/`)**
Based on:

- slope  
- ruggedness  
- elevation  
- mobility cost  
- terrain advantage scoring  

---

### **5️⃣ Climate Predictive Models (`climate/`)**
Model:

- moisture-balance likelihood  
- seasonal stability  
- drought/wet interval predictions  
- long-term climatic affordance potential  

---

### **6️⃣ Composite Multi-Factor Models (`composite/`)**
Weighted models integrating:

- terrain  
- hydrology  
- soils  
- vegetation  
- climate  
- uncertainty  

Outputs produce **environmental suitability surfaces**, never cultural forecasts.

---

### **7️⃣ Machine Learning Predictive Models (`machine-learning/`)**
Models include:

- Random Forest  
- Gradient Boost  
- GAM/GLM  
- ensemble environmental predictors  

All predictive ML outputs must include:

- SHAP importance layers  
- model confidence maps  
- proxy-weight metadata  
- reproducibility parameters (seed, config hash)  

---

## ⚠️ Predictive Uncertainty (`uncertainty/`)

Includes:

- model agreement surfaces  
- proxy disagreement maps  
- variance layers  
- environmental interpolation limits  

Displayed in Focus Mode as **Predictive Confidence Chips**.

---

## 🧬 Metadata & PROV-O Requirements

### **STAC (`stac/`)**
Predictive STAC Items require:

- generalized H3 geometry  
- uncertainty + explainability references  
- environmental drivers  
- lineage pointers  

### **DCAT (`metadata/`)**
Includes:

- dataset descriptions  
- FAIR + CARE indicators  
- distribution metadata  
- environmental purpose statements  

### **PROV-O (`provenance/`)**
Tracks:

- datasets used  
- modeling algorithms  
- hyperparameter settings  
- generalization transformations  
- uncertainty propagation  
- lineage version hashes  

All outputs must pass automated CI validation.

---

## 🧠 Focus Mode Integration

Predictive results feed:

- environmental narrative generation  
- cultural-landscape context blocks  
- generalized settlement-affordance explanations  
- multi-period environmental overlays  
- Story Node v3 context modeling  

Example Focus Summary:

> **Focus Summary:**  
> Predictive models indicate landscape regions where hydrology, soils, vegetation, and terrain affordances combine to create long-term environmental stability. These are environmental predictions, not cultural interpretations.

---

## 🛡️ CARE & Ethical Requirements

All predictive outputs must:

- avoid cultural or tribal identity inference  
- avoid suggesting settlement predictions  
- avoid reconstructing sacred or restricted landscapes  
- apply H3 r7+ masking  
- disclose uncertainty clearly  
- undergo FAIR+CARE review before publication  

If predictive outputs risk cultural misinterpretation → they must be masked or removed.

---

## 🕰️ Version History

| Version | Date       | Author                                    | Summary |
|--------:|------------|-------------------------------------------|---------|
| v11.0.0 | 2025-11-17 | Archaeology WG · Predictive Modeling WG · FAIR+CARE | Initial predictive cultural-landscape results registry. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Predictive Landscape Results · CARE-Governed · FAIR+CARE Certified  
MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Cultural Landscape Results](../README.md)

</div>