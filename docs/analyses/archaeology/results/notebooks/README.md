---
title: "📓 Kansas Frontier Matrix — Archaeology Analysis Notebooks (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/notebooks/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly / Archaeology Working Group · FAIR+CARE Council · AI Governance Board"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/archaeology-analysis-notebooks-v1.json"
governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Notebook Index"
intent: "archaeology-analysis-notebooks"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed"
sensitivity_level: "High"
public_exposure_risk: "Medium"
indigenous_rights_flag: true
data_steward: "Archaeology WG · FAIR+CARE Council"
risk_category: "Analytical Notebook Outputs"
redaction_required: true
provenance_chain:
  - "docs/analyses/archaeology/results/notebooks/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E31 Document"
  schema_org: "TechArticle"
  prov_o: "prov:Entity"
json_schema_ref: "../../../../../schemas/json/archaeology-analysis-notebooks.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/archaeology-analysis-notebooks-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:notebooks-results-v11.0.0"
semantic_document_id: "kfm-arch-results-notebooks"
event_source_id: "ledger:docs/analyses/archaeology/results/notebooks/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Restricted"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "contextualization"
ai_transform_prohibited:
  - "speculation"
  - "sensitive-site-inference"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Internal"
role: "archaeology-results-notebooks-root"
lifecycle_stage: "stable"
ttl_policy: "Review every 6 months"
sunset_policy: "Superseded upon next analytical notebook framework"
---

<div align="center">

# 📓 **Kansas Frontier Matrix — Archaeology Analysis Notebooks**  
`docs/analyses/archaeology/results/notebooks/README.md`

**Purpose:**  
Serve as the centralized index for **all analytical Jupyter notebooks** used in archaeological research workflows within the Kansas Frontier Matrix (KFM).  
These notebooks generate **scientifically validated, FAIR+CARE–aligned results**, and record deterministic computations, model experiments, explainability outputs, and reproducible pipelines.

</div>

---

## 📘 Overview

This directory houses **processed, public-safe notebooks** that support:

- archaeological spatial modeling  
- environmental correlation analyses  
- predictive modeling experiments  
- artifact distribution analytics  
- cultural landscape reconstruction  
- geophysics pattern analysis  
- paleoenvironmental context modeling  
- temporal/chronological sequence testing  

All notebooks:

- exclude sensitive coordinates  
- mask archaeological and cultural features via H3 generalization  
- are fully governed under FAIR+CARE  
- are reproducible via WAL → Retry → Rollback lineage  
- produce results validated through KFM-MDP v11.0.0  

Notebooks may be run in:

- KFM Compute Environment  
- KFM Gov-Safe Local Execution Mode  
- containerized notebook runners (JupyterLab, nbgitpuller-safe)

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/results/notebooks/
├── README.md                         # This file
├── spatial/                          # Spatial notebooks (H3, KDE, GIS workflows)
├── temporal/                         # OWL-Time, chronology, sequence modeling
├── environmental/                    # Climate, hydrology, soils, eco-analysis
├── cultural-landscapes/              # Interaction sphere + corridor modeling notebooks
├── artifacts/                        # Lithic, ceramic, faunal analyses
├── geophysics/                       # Magnetometry/GPR/resistivity notebooks
├── predictive/                       # ML/GAM predictive modeling pipelines
├── explainability/                   # SHAP/LIME notebooks for transparency
├── stac/                             # Notebook-generated STAC items
├── metadata/                         # DCAT, JSON-LD metadata for notebooks
└── provenance/                       # PROV-O lineage of computations
~~~

---

## 🧭 Notebook Classes

### **1️⃣ Spatial Modeling Notebooks (`spatial/`)**
Examples:

- H3 layer generation  
- KDE smoothing & cluster analysis  
- hydrology adjacency modeling  
- environmental overlays  

Outputs: generalized rasters, pattern summaries, STAC Items.

---

### **2️⃣ Temporal Modeling Notebooks (`temporal/`)**
Workflows:

- OWL-Time interval expansion  
- radiocarbon Bayesian modeling (generalized)  
- occupation-phase correlation  

Outputs: temporal heatmaps, phase transitions.

---

### **3️⃣ Environmental Analysis (`environmental/`)**
Includes:

- climate reconstruction notebooks  
- drought/wet cycle models  
- vegetation/soil affordance analyses  

Outputs feed Story Node v3 and predictive pipelines.

---

### **4️⃣ Cultural Landscape Notebooks (`cultural-landscapes/`)**
Generate:

- corridor-cost surfaces  
- interaction-sphere affinities  
- ecological affordance clusters  
- cultural-region generalizations  

---

### **5️⃣ Artifact-Centered Notebooks (`artifacts/`)**
Includes:

- lithic typology  
- ceramic analysis  
- faunal summaries  
- distribution modeling (generalized)  

Always excludes restricted materials.

---

### **6️⃣ Geophysics Notebooks (`geophysics/`)**
Generalized analysis of:

- magnetometry  
- GPR  
- EM  
- resistivity  

Outputs: anomaly probability surfaces (public-safe).

---

### **7️⃣ Predictive Modeling (`predictive/`)**
Workflows using:

- random forests  
- GAMs  
- GLMs  
- environmental predictors  
- ensemble models  

Outputs include explainability overlays and uncertainty ranges.

---

### **8️⃣ Explainability Notebooks (`explainability/`)**
Generate:

- SHAP values  
- LIME explanations  
- residual maps  
- uncertainty commentary  

Used heavily in Focus Mode v3.

---

## 🧬 Metadata & Provenance

### **STAC Metadata (`stac/`)**
Each notebook producing spatial products must export:

- STAC Item with raster/vector asset references  
- temporal/spatial extents  
- CARE sensitivity tags  

### **DCAT Metadata (`metadata/`)**
Captures:

- dataset purpose  
- authorship  
- lifecycle stage  
- FAIR+CARE statements  

### **PROV-O Lineage (`provenance/`)**
Includes:

- `prov:used` datasets  
- `prov:wasGeneratedBy` notebook run  
- hash-locked notebook versions  
- WAL → Retry → Rollback checkpoints  
- computational environment metadata  

---

## 🧠 Focus Mode Integration

Focus Mode v3 consumes notebook outputs to:

- enrich narratives with safe summaries  
- generate context-aware environmental insights  
- provide temporal & spatial reasoning blocks  
- support 3D + timeline overlays  
- show trustworthy explainability chips  

Example Focus Summary:

> **Focus Summary:**  
> Notebook-derived analyses reveal generalized Late Prehistoric environmental patterns and settlement tendencies across stable hydrology zones. Results have been CARE-filtered, generalized, and verified through reproducible workflows.

---

## ⚠️ Ethical & CARE Requirements

All notebooks must:

- exclude restricted archaeological or cultural data  
- generalize spatial features (H3 r7+)  
- distinguish environmental predictors from cultural interpretations  
- document uncertainty and model limitations  
- avoid speculative inference  
- be reviewed by FAIR+CARE Council for public release  

---

## 🕰️ Version History

| Version | Date       | Author                           | Summary |
|--------:|------------|----------------------------------|---------|
| v11.0.0 | 2025-11-17 | Archaeology WG · FAIR+CARE Council | Initial notebook results directory under KFM-MDP v11.0.0. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Notebook-Based Archaeology · CARE-Governed · FAIR+CARE Certified  
MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Archaeology Results](../README.md)

</div>