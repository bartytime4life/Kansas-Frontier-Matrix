---
title: "🔮🧲 Kansas Frontier Matrix — Geophysics Results: Predictive Modeling (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/geophysics/predictive/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly · Geophysics WG · Archaeology WG · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/archaeology-geophysics-predictive-v1.json"
governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Geophysics Result"
intent: "archaeology-geophysics-predictive-results"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed / Predictive Geophysics"
sensitivity_level: "High"
public_exposure_risk: "Medium"
indigenous_rights_flag: true
data_steward: "Geophysics WG · Archaeology WG · FAIR+CARE Council"
risk_category: "Predictive Modeling (Generalized)"
redaction_required: true
provenance_chain:
  - "docs/analyses/archaeology/results/geophysics/predictive/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E26 Physical Feature"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"
  owl_time: "TemporalEntity"
json_schema_ref: "../../../../../schemas/json/archaeology-geophysics-predictive-results.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/archaeology-geophysics-predictive-results-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:geophysics:predictive-results-v11.0.0"
semantic_document_id: "kfm-arch-geophysics-predictive-results"
event_source_id: "ledger:docs/analyses/archaeology/results/geophysics/predictive/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Restricted"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
ai_transform_prohibited:
  - "feature-detection"
  - "occupation-inference"
  - "burial-or-structure-prediction"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Internal / CARE-Governed"
role: "archaeology-geophysics-predictive-root"
lifecycle_stage: "stable"
ttl_policy: "Review every 6 months"
sunset_policy: "Superseded upon next predictive-model upgrade"
---

<div align="center">

# 🔮🧲 **Geophysics Results — Predictive Modeling**  
`docs/analyses/archaeology/results/geophysics/predictive/README.md`

**Purpose:**  
Define the **generalized, FAIR+CARE–regulated geophysical predictive models** used to understand broad **environmental subsurface tendency zones**, without inferring archaeological features, site presence, burials, structures, or restricted cultural information.

Predictive outputs must strictly remain **environmental-only**, sovereignty-safe, and **H3 r7+ generalized**.

</div>

---

## 📘 Overview

Predictive geophysics models in KFM:

- combine **magnetometry, GPR, resistivity, EMI** into environmental-only multi-sensor models  
- generate **generalized subsurface tendency surfaces**, not features  
- integrate hydrology, soil conductivity, geomorphology, and terrain variables  
- include uncertainty, signal disagreement, and cross-sensor drift metadata  
- use ML/GAM/GLM models ONLY for **environmental prediction**, never cultural inference  
- harmonize with Focus Mode v3 & Story Node system  

These models produce **safe**, non-specific surfaces describing:

- subsurface variation probability  
- moisture & conductivity patterns  
- geomorphic stability fields  
- environmental signal predictability  

They never identify or imply:

- cultural features  
- structures  
- burial locations  
- pits, walls, hearths  
- restricted heritage features  

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/results/geophysics/predictive/
├── README.md                                   # This file
├── magnetometry/                               # Predictive magnetic-variation models
├── gpr/                                        # Predictive radar-response models
├── resistivity/                                # Predictive resistivity-envelope models
├── electromagnetic/                            # EMI-based environmental predictions
├── composite/                                   # Multi-sensor predictive models
├── environmental-drivers/                      # Environmental covariate surfaces
├── uncertainty/                                # Predictive uncertainty (variance, disagreement)
├── stac/                                        # STAC Items for predictive layers
├── metadata/                                    # DCAT + JSON-LD predictive metadata
└── provenance/                                  # PROV-O lineage & model-parameter logs
~~~

---

## 🔮 Predictive Model Types

### **1️⃣ Magnetometry Predictive Models (`magnetometry/`)**
Predict broad magnetic-variation zones using:

- environmental drivers  
- drift-corrected gradients  
- ML/GAM magnetic-surface regressions  

Generalized only; no anomaly interpretation.

---

### **2️⃣ GPR Predictive Models (`gpr/`)**
Generate probability surfaces for:

- amplitude-range variation  
- moisture-driven radar response  
- soil/geomorphic timing  

Entirely feature-safe.

---

### **3️⃣ Resistivity Predictive Models (`resistivity/`)**
Predict:

- electrical conductivity envelopes  
- moisture/soil-linked resistivity variation  
- geomorphic-stability signatures  

Never used for feature detection.

---

### **4️⃣ EMI Predictive Models (`electromagnetic/`)**
Model:

- multi-frequency conductivity behavior  
- soil moisture transitions  
- environmental-only signal envelopes  

---

### **5️⃣ Composite Predictive Models (`composite/`)**
Integrate:

- magnetometry  
- GPR  
- resistivity  
- EMI  
- environmental drivers  

Outputs describe **environmental subsurface stability**, not features.

---

### **6️⃣ Environmental Driver Surfaces (`environmental-drivers/`)**
Includes:

- soil conductivity  
- hydrology proximity  
- terrain ruggedness  
- vegetation biomass  
- climate/seasonality  

These serve as model inputs; none represent cultural data.

---

## ⚠️ Predictive Uncertainty (`uncertainty/`)
Tracks:

- model variance  
- cross-sensor disagreement  
- environmental ambiguity  
- sensitivity to noise or drift  
- H3 stability variance  

Displayed in Focus Mode as **Predictive Confidence Chips**.

---

## 🧬 Metadata & Provenance Requirements

### **STAC (`stac/`)**
Predictive geophysics STAC Items must include:

- H3-masked geometry  
- environmental-driver metadata  
- uncertainty layers  
- model configuration summary  
- CARE classification  
- PROV-O lineage references  

### **DCAT (`metadata/`)**
Defines:

- dataset scope  
- environmental purpose  
- FAIR+CARE compliance  
- distribution information  

### **PROV-O (`provenance/`)**
Tracks:

- dataset sources  
- model type + hyperparameters  
- cross-validation steps  
- H3 generalization  
- WAL → Retry → Rollback lineage  
- uncertainty propagation  

---

## 🧠 Focus Mode Integration

Predictive geophysics layers support:

- environmental subsurface narrative blocks  
- multi-sensor pattern explanations  
- uncertainty-aware overlays  
- Story Node v3 environmental-context anchors  

Example Focus Summary:

> **Focus Summary:**  
> Predictive models identify environmentally driven subsurface variability patterns across Kansas. All outputs are generalized, sovereignty-safe, and prohibited from implying archaeological feature presence.

---

## 🛡 CARE & Ethical Requirements

All predictive models must:

- avoid ANY cultural or feature inference  
- enforce H3 r7+ masking  
- remain environmental-only  
- disclose uncertainty transparently  
- pass FAIR+CARE Council review  
- log all generalization + redaction steps  

If any model output risks cultural sensitivity → it must be removed or generalized further.

---

## 🕰️ Version History

| Version | Date       | Author                                   | Summary |
|--------:|------------|------------------------------------------|---------|
| v11.0.0 | 2025-11-17 | Geophysics WG · Archaeology WG · FAIR+CARE Council | Initial predictive geophysics results registry under MDP v11. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Predictive Geophysics Results · CARE-Governed · FAIR+CARE Certified  
MCP-DL v6.3 · Diamond⁹ Ω · Crown∞Ω Ultimate Certified  

[Back to Geophysics Results](../README.md)

</div>
