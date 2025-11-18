---
title: "📓🔮 Kansas Frontier Matrix — Analysis Notebooks: Predictive Modeling (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/notebooks/predictive/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly · Predictive Modeling WG · Archaeology WG · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/archaeology-predictive-notebooks-v1.json"
governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Notebook Index"
intent: "archaeology-predictive-analysis-notebooks"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed / Predictive Modeling"
sensitivity_level: "High"
public_exposure_risk: "Medium"
indigenous_rights_flag: true
data_steward: "Predictive Modeling WG · FAIR+CARE Council"
risk_category: "Environmental Predictive Modeling (Generalized)"
redaction_required: true
provenance_chain:
  - "docs/analyses/archaeology/results/notebooks/predictive/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "HowTo"
  prov_o: "prov:Plan"
  owl_time: "TemporalEntity"
json_schema_ref: "../../../../../schemas/json/archaeology-predictive-notebooks.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/archaeology-predictive-notebooks-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:results:notebooks:predictive-v11.0.0"
semantic_document_id: "kfm-arch-predictive-notebooks"
event_source_id: "ledger:docs/analyses/archaeology/results/notebooks/predictive/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Restricted / Environmental Only"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "uncertainty-explanation"
ai_transform_prohibited:
  - "cultural-prediction"
  - "feature-detection"
  - "burial-or-structure-inference"
  - "identity-attribution"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
classification: "Internal / CARE-Governed"
jurisdiction: "Kansas / United States"
role: "archaeology-predictive-notebooks-root"
lifecycle_stage: "stable"
ttl_policy: "Review every 6 months"
sunset_policy: "Replaced upon next predictive-modeling revision"
---

<div align="center">

# 📓🔮 **Predictive Modeling Notebooks — Results Index**  
`docs/analyses/archaeology/results/notebooks/predictive/README.md`

**Purpose:**  
Index and govern all **predictive modeling notebooks** used across archaeological, geophysical, environmental, and cultural-landscape analysis within the Kansas Frontier Matrix (KFM).  
These notebooks produce **environment-only, sovereignty-safe predictive surfaces**, uncertainty layers, and generalized model outputs for downstream results.

</div>

---

## 📘 Overview

Predictive notebooks in KFM:

- compute environmental-only predictive surfaces  
- drive generalized suitability/affordance modeling  
- feed predictive layers into archaeology, geophysics, and landscape workflows  
- enforce **H3 r7+ generalization** at export  
- propagate and quantify **uncertainty + model disagreement**  
- compute **proxy driver weights** (soil, hydrology, terrain, climate, vegetation)  
- document predictive variance and ensemble spread  
- export **PROV-O lineage**, reproducibility data, and masked outputs  
- produce Story Node–safe summaries and Focus Mode v3 predictive chips  

They must **NOT**:

- predict cultural groups  
- infer settlement events  
- identify features, structures, or burials  
- reconstruct sensitive archaeological phenomena  
- overfit or produce non-environmental predictions  

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/results/notebooks/predictive/
├── README.md                         # This file
├── environmental/                    # Environment-only predictive models
├── geophysics/                       # Predictive geophysical tendency models
├── artifacts/                        # Artifact-linked environmental predictors (generalized)
├── cultural-landscapes/              # Environmental drivers for landscape prediction
├── temporal/                         # OWL-Time aligned predictive surfaces
├── composite/                        # Multi-driver integrated predictive models
├── drivers/                          # Climate, hydrology, soils, vegetation predictors
├── uncertainty/                      # Variance, proxy conflict, ensemble spread notebooks
├── qa/                               # Predictive safety checks & compliance audits
└── exports/                          # Plots, rasters, CSV, JSON-LD, model summaries
~~~

---

## 🔮 Notebook Categories

### **1️⃣ Environmental Predictive Notebooks (`environmental/`)**
Generate:

- environmental suitability surfaces  
- ecological affordance models  
- hydrology/soil/terrain/vegetation drivers  
- seasonal/climatic predictor grids  

Environmental only — never cultural.

---

### **2️⃣ Predictive Geophysics Notebooks (`geophysics/`)**
Produce:

- multi-sensor predictive “tendency” maps  
- conductivity/moisture proxies  
- geomorphic stability predictions  

Fully generalized, feature-safe.

---

### **3️⃣ Artifact-Predictive Notebooks (`artifacts/`)**
Support:

- artifact correlation → environmental prediction  
- PD-safe artifact–environment relationships  
- predictor surfaces that remain non-cultural  

---

### **4️⃣ Cultural Landscape Predictive Notebooks (`cultural-landscapes/`)**
Compute:

- environmental corridor suitability  
- eco-hydrological pathways  
- seasonal or climatic movement affordances  
- interaction-sphere environmental models  

No cultural boundary inference allowed.

---

### **5️⃣ Temporal Predictive Models (`temporal/`)**
Describe:

- OWL-Time aligned predictive envelopes  
- cross-period environmental shifts  
- long-term ecological stability models  

---

### **6️⃣ Composite Multi-Driver Models (`composite/`)**
Integrate:

- climate  
- hydrology  
- vegetation  
- soils  
- terrain  
- geophysics  

Results serve as **environmental composite predictors**.

---

### **7️⃣ Predictor Drivers (`drivers/`)**
Generate:

- climate indices  
- hydrology networks  
- soils + pedological predictors  
- vegetation/ecozone indices  
- terrain derivatives  

Used as ML/GAM/GLM inputs.

---

### **8️⃣ Uncertainty Notebooks (`uncertainty/`)**
Compute:

- ensemble spread  
- proxy disagreement  
- predictive fragility  
- variance decomposition  
- cross-model divergence  

Exported as **Predictive Confidence Chips**.

---

### **9️⃣ QA Notebooks (`qa/`)**
Verify:

- H3 generalization integrity  
- sovereignty-safe outputs  
- CARE-compliant predictor usage  
- STAC/DCAT/PROV consistency  
- masking rules & redaction logs  
- no feature-level inference from model behavior  

---

## 🧬 Metadata & Provenance Integration

Each predictive notebook must export:

- **prov:Bundle** lineage  
- **STAC Items** for generalized predictive surfaces  
- **DCAT JSON-LD** dataset descriptors  
- **uncertainty metadata**  
- **masking + redaction logs**  
- **model configuration hashes** (seed, environment, parameters)

Outputs feed final:

- predictive/stac/  
- predictive/metadata/  
- predictive/provenance/

directories elsewhere in the repository.

---

## 🧠 Focus Mode Integration

Predictive notebooks provide:

- environmental predictive blocks  
- uncertainty visualizations  
- driver explanations  
- narrative-safe predictive reasoning  
- Story Node v3 “predictive environmental context” layers  

Example Focus Summary:

> **Focus Summary:**  
> Predictive modeling notebooks produce environmental-only forecasts and explanatory layers, masked and generalized to protect cultural sovereignty while enabling safe narrative reasoning in Focus Mode.

---

## 🛡 CARE & Ethical Requirements

Predictive notebooks must:

- avoid ANY cultural inference  
- enforce H3 r7+ spatial masking  
- document masking & redaction paths  
- disclose model uncertainty  
- exclude sensitive ecological knowledge  
- pass FAIR+CARE review before publication  

If a notebook produces unsafe predictive potential → **it is blocked and must be reworked.**

---

## 🕰️ Version History

| Version | Date       | Author                                   | Summary |
|--------:|------------|------------------------------------------|---------|
| v11.0.0 | 2025-11-17 | Predictive Modeling WG · FAIR+CARE Council | Initial predictive modeling notebook index under KFM-MDP v11. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Predictive Analysis Notebooks · CARE-Governed · FAIR+CARE Certified  
MCP-DL v6.3 · Diamond⁹ Ω · Crown∞Ω Ultimate Certified  

[Back to Notebooks Index](../README.md)

</div>
