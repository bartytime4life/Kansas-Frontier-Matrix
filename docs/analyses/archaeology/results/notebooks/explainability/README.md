---
title: "📓🧠 Kansas Frontier Matrix — Analysis Notebooks: Explainability & Model Interpretation (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/notebooks/explainability/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly · Archaeology WG · Modeling WG · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/archaeology-explainability-notebooks-v1.json"
governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Notebook Index"
intent: "archaeology-explainability-analysis-notebooks"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed / Model-Explainability"
sensitivity_level: "High"
public_exposure_risk: "Medium"
indigenous_rights_flag: true
data_steward: "Archaeology WG · FAIR+CARE Council · Explainability Subgroup"
risk_category: "Model Interpretation / Sensitive Context"
redaction_required: true
provenance_chain:
  - "docs/analyses/archaeology/results/notebooks/explainability/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "HowTo"
  prov_o: "prov:Plan"
  owl_time: "TemporalEntity"
json_schema_ref: "../../../../../schemas/json/archaeology-explainability-notebooks.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/archaeology-explainability-notebooks-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:results:notebooks:explainability-v11.0.0"
semantic_document_id: "kfm-arch-explainability-notebooks"
event_source_id: "ledger:docs/analyses/archaeology/results/notebooks/explainability/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Restricted / Explainability-Only"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "variable-importance-explanation"
ai_transform_prohibited:
  - "inference-of-sensitive-cultural-meaning"
  - "identity-or-provenience-reconstruction"
  - "unsafe causal speculation"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
classification: "Internal / CARE-Governed"
jurisdiction: "Kansas / United States"
role: "archaeology-explainability-notebooks-root"
lifecycle_stage: "stable"
ttl_policy: "Review every 6 months"
sunset_policy: "Revised upon next modeling-governance update"
---

<div align="center">

# 📓🧠 **Explainability & Model Interpretation — Notebook Index**  
`docs/analyses/archaeology/results/notebooks/explainability/README.md`

**Purpose:**  
Serve as the authoritative index of **explainability-focused analysis notebooks** used to audit, interpret, validate, and culturally-safeguard modeling outputs across archaeology, geophysics, cultural landscapes, environmental modeling, and predictive workflows in the Kansas Frontier Matrix (KFM).

These notebooks ensure **transparency**, **model accountability**, **uncertainty clarity**, and **FAIR+CARE–aligned interpretive guardrails**.

</div>

---

## 📘 Overview

Explainability notebooks in KFM:

- evaluate model behavior and constrain interpretive drift  
- generate SHAP / LIME environmental driver summaries  
- compute proxy disagreement & model variance  
- validate feature contributions under sovereignty restrictions  
- produce Focus Mode v3 **Explainability Chips**  
- ensure all models remain **non-speculative**, **environment-only**, and **non-cultural**  
- audit predictive or clustering outputs for compliance  
- produce PROV-O lineage bundles documenting interpretability logic  
- export STAC-metadata-safe “explainability assets”  

These notebooks **never**:

- assign cultural identity  
- infer site-level meaning  
- interpret subsurface feature shapes  
- generate sensitive cultural implications  
- attribute agency, motivation, or group behavior  

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/results/notebooks/explainability/
├── README.md                               # This file
├── shap/                                   # SHAP values & driver-importance notebooks
├── lime/                                   # LIME local interpretability notebooks
├── feature-attribution/                    # Environmental-only feature attribution studies
├── proxy-disagreement/                     # Cross-model + cross-proxy disagreement notebooks
├── uncertainty-audits/                     # Variance, ensemble spread, noise analysis
├── fairness-audits/                        # CARE-focused interpretability tests
├── qa/                                     # Explainability governance QC workflow notebooks
└── exports/                                # Explainability chips, tables, plots, JSON-LD
~~~

---

## 🧪 Notebook Categories

### **1️⃣ SHAP Notebooks (`shap/`)**
Produce:

- global + local SHAP summaries  
- environmental-driver importance rankings  
- uncertainty-aware SHAP grids  
- H3-generalized SHAP surfaces for map layers  

---

### **2️⃣ LIME Notebooks (`lime/`)**
Generate:

- local perturbation-based explanations  
- factor-impact blocks for Focus Mode  
- sovereignty-filtered interpretability segments  

---

### **3️⃣ Feature Attribution Notebooks (`feature-attribution/`)**
Document:

- environmental-only contributor importance  
- hydrology/terrain/soil/vegetation/climate factors  
- contribution stability across models  
- non-cultural interpretability summaries  

---

### **4️⃣ Proxy Disagreement Notebooks (`proxy-disagreement/`)**
Measure:

- disagreement between environmental proxies  
- disagreement between models  
- disagreement across spatial/temporal slices  
- environmental ambiguity documentation  

---

### **5️⃣ Uncertainty Audit Notebooks (`uncertainty-audits/`)**
Include:

- ensemble variance  
- predictive spread  
- model fragility  
- environmental sensitivity checks  

Outputs become **Explainability Confidence Chips**.

---

### **6️⃣ FAIR+CARE Interpretability Audits (`fairness-audits/`)**
Evaluate:

- cultural-safety compliance  
- sovereignty indicators  
- masking adequacy  
- generalization sufficiency  
- narrative safety alignment  

---

### **7️⃣ Explainability QA Notebooks (`qa/`)**
Perform:

- model-governance tests  
- interpretability boundary enforcement  
- redaction verification  
- STAC/DCAT metadata integrity checks  

---

## 🧬 Metadata & Provenance Integration

All explainability notebooks must export:

- `prov:Bundle` lineage JSON-LD  
- STAC-ready explainability metadata  
- DCAT entries for explainability artifacts  
- uncertainty + disagreement tables  
- reproducibility parameters (seed, config hash, environment snapshot)  
- masking + redaction logs  

These outputs feed the final:

- `explainability/stac/`  
- `explainability/metadata/`  
- `explainability/provenance/`

directories elsewhere in the results tree.

---

## 🧠 Focus Mode Integration

Explainability notebooks supply:

- **Explainability Chips**  
- **Uncertainty Chips**  
- **Environmental Driver Blocks**  
- **Model Disagreement Panels**  
- narrative-safe reasoning capsules  

Example Focus Summary:

> **Focus Summary:**  
> Explainability notebooks clarify how environmental drivers shape model behavior, documenting uncertainty and ensuring sovereignty-safe interpretability for Focus Mode.

---

## 🛡 CARE & Ethical Requirements

Explainability notebooks must:

- avoid cultural interpretations  
- reject any sensitive inference pathways  
- avoid identity or group behavioral attribution  
- include masking + uncertainty checks  
- pass FAIR+CARE audit before release  
- explicitly flag any unsafe modeling behavior  

Notebooks that violate interpretability safety → **blocked from export**.

---

## 🕰️ Version History

| Version | Date       | Author                                      | Summary |
|--------:|------------|---------------------------------------------|---------|
| v11.0.0 | 2025-11-17 | Archaeology WG · FAIR+CARE Council · Modeling WG | Initial explainability notebook index under MDP v11. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Explainability Notebooks · CARE-Governed · FAIR+CARE Certified  
MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Notebooks Index](../README.md)

</div>
