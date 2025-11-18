---
title: "📓🧲 Kansas Frontier Matrix — Analysis Notebooks: Geophysics Results (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/notebooks/geophysics/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly · Geophysics WG · Archaeology WG · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/archaeology-geophysics-notebooks-v1.json"
governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Notebook Index"
intent: "archaeology-geophysics-analysis-notebooks"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed / Sensitive-Surface Geophysics"
sensitivity_level: "High"
public_exposure_risk: "Medium"
indigenous_rights_flag: true
data_steward: "Geophysics WG · FAIR+CARE Council"
risk_category: "Subsurface Modeling & Safety"
redaction_required: true
provenance_chain:
  - "docs/analyses/archaeology/results/notebooks/geophysics/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "HowTo"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"
  owl_time: "TemporalEntity"
json_schema_ref: "../../../../../schemas/json/archaeology-geophysics-notebooks.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/archaeology-geophysics-notebooks-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:results:notebooks:geophysics-v11.0.0"
semantic_document_id: "kfm-arch-geophysics-notebooks"
event_source_id: "ledger:docs/analyses/archaeology/results/notebooks/geophysics/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Restricted / Environmental-Signal Only"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "uncertainty-context-explanation"
ai_transform_prohibited:
  - "feature-level inference"
  - "burial-or-structure-detection"
  - "reverse-subsurface-reconstruction"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
classification: "Internal / CARE-Governed"
jurisdiction: "Kansas / United States"
role: "archaeology-geophysics-notebooks-root"
lifecycle_stage: "stable"
ttl_policy: "Review every 6 months"
sunset_policy: "Updated upon next geophysics modeling revision"
---

<div align="center">

# 📓🧲 **Geophysics Analysis Notebooks — Results Index**  
`docs/analyses/archaeology/results/notebooks/geophysics/README.md`

**Purpose:**  
Provide the centralized index of **sovereignty-safe geophysical analysis notebooks** used for magnetometry, GPR, resistivity, electromagnetic induction (EMI), and composite multi-sensor modeling within the Kansas Frontier Matrix (KFM).  
These notebooks generate **intermediate analytical layers**, **QA diagnostics**, **uncertainty summaries**, and **generalized outputs** feeding final geophysical results.

</div>

---

## 📘 Overview

Geophysics notebooks perform:

- safe preprocessing (drift correction, filtering, stacking)  
- environmental-only interpretation safeguards  
- H3 r7+ spatial generalization routines  
- derive uncertainty layers (noise, disagreement, drift variance)  
- multi-sensor composite building (mag + GPR + resistivity + EMI)  
- temporal modeling (OWL-Time aligned)  
- creation of sovereignty-safe STAC + DCAT metadata  
- PROV-O lineage export (WAL → Retry → Rollback)  
- cultural-safety QA and masking enforcement  

They **never**:

- infer features, structures, burials, or pits  
- visualize sensitive anomaly shapes  
- reconstruct fine-grained subsurface patterns  
- assign cultural meaning to signals  

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/results/notebooks/geophysics/
├── README.md                       # This file
├── magnetometry/                   # Drift, filtering, gradient, envelope notebooks
├── gpr/                            # Slice-stack, depth-band, composite GPR notebooks
├── resistivity/                    # Conductivity/resistivity modeling & QC notebooks
├── electromagnetic/                # EMI frequency-band & susceptibility notebooks
├── composite/                      # Multi-sensor integrated notebooks
├── environmental-links/            # Hydrology/soil/terrain/climate correlation analyses
├── temporal/                       # OWL-Time aligned temporal-signal notebooks
├── uncertainty/                    # Noise, drift, disagreement, sensor variance
├── qa/                             # CARE/audit notebooks verifying sovereignty safety
└── exports/                        # Plots, rasters, CSV, JSON-LD summaries
~~~

---

## 🧪 Notebook Categories

### **1️⃣ Magnetometry (`magnetometry/`)**
Includes:

- diurnal drift correction  
- median/bandpass filtering  
- gradient + derivative diagnostics  
- H3 envelope construction  
- environmental-only interpretation constraints  

---

### **2️⃣ Ground-Penetrating Radar (`gpr/`)**
Contains:

- dewow, migration, stack routines  
- slice-based amplitude summaries  
- depth-band models  
- generalized anomaly-envelope formation  
- environmental-only GPR context  

---

### **3️⃣ Resistivity (`resistivity/`)**
Covers:

- electrical conductivity modeling  
- depth-resistivity envelopes  
- moisture/soil-linked variation  
- uncertainty and drift analysis  

---

### **4️⃣ Electromagnetic Induction (`electromagnetic/`)**
Includes:

- multi-frequency EMI composites  
- conductivity vs susceptibility modeling  
- environmental correlation panels  

---

### **5️⃣ Composite Multi-Sensor (`composite/`)**
Integrates:

- mag + GPR + resistivity + EMI  
- harmonized environmental drivers  
- composite confidence surfaces  

Outputs remain strictly generalized.

---

### **6️⃣ Environmental Links (`environmental-links/`)**
Generate:

- hydrology–signal correlations  
- soil conductivity & pedology links  
- terrain + geomorphic influence models  
- vegetation/biomass co-patterns  

Never cultural interpretation.

---

### **7️⃣ Temporal Notebooks (`temporal/`)**
Describe:

- OWL-Time aligned environmental signal transitions  
- long-term subsurface moisture proxies  
- multi-period uncertainty envelopes  

---

### **8️⃣ Uncertainty Notebooks (`uncertainty/`)**
Track:

- sensor disagreement  
- drift uncertainty  
- smoothing variance  
- environmental disagreement  
- predictive fragility  

Feed Focus Mode **Geophysics Confidence Chips**.

---

### **9️⃣ QA Notebooks (`qa/`)**
Perform:

- masking + generalization verification  
- sovereignty/CARE checks  
- STAC/DCAT metadata compliance  
- lineage + WAL correctness  
- environmental-only interpretation audits  

---

## 🧬 Provenance & Metadata Integration

Every notebook must export:

- `prov:Bundle` lineage  
- STAC metadata for derived geophysical layers  
- DCAT dataset descriptors  
- uncertainty metrics  
- generalization/masking logs  
- reproducibility hashes (model config, seeds, environment snapshot)

Exports map into `results/geophysics/*/metadata`, `stac`, and `provenance`.

---

## 🧠 Focus Mode Integration

Geophysics notebooks power:

- narrative-safe environmental signal explanations  
- uncertainty + drift chips  
- multi-sensor reasoning blocks  
- temporal-signal context  
- Story Node v3 environmental backdrops  

**Example Focus Summary:**  
> Geophysical notebooks generate generalized, sovereignty-protected environmental signal layers—with uncertainty and lineage—ensuring safe use in Focus Mode and site-neutral archaeological analysis.

---

## 🛡 CARE & Ethical Requirements

All notebooks:

- must avoid subsurface feature inference  
- must apply H3 r7+ masking  
- must not store restricted anomaly shapes  
- must disclose uncertainty  
- must log redaction/generalization steps  
- must pass FAIR+CARE review  

If unsafe → **blocked from export**.

---

## 🕰️ Version History

| Version | Date       | Author                                     | Summary |
|--------:|------------|--------------------------------------------|---------|
| v11.0.0 | 2025-11-17 | Geophysics WG · Archaeology WG · FAIR+CARE Council | Initial geophysics-notebook index under KFM-MDP v11. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Geophysics Analysis Notebooks · CARE-Governed · FAIR+CARE Certified  
MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Notebooks Index](../README.md)

</div>
