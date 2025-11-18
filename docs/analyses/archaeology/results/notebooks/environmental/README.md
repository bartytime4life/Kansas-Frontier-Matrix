---
title: "📓🌎 Kansas Frontier Matrix — Analysis Notebooks: Environmental Results (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/notebooks/environmental/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly · Archaeology WG · Environmental Modeling WG · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/archaeology-environmental-notebooks-v1.json"
governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Notebook Index"
intent: "archaeology-environmental-analysis-notebooks"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed / Environmental Modeling"
sensitivity_level: "Medium"
public_exposure_risk: "Medium"
indigenous_rights_flag: true
data_steward: "Archaeology WG · Environmental Modeling WG · FAIR+CARE Council"
risk_category: "Environmental Modeling / Proxy-Based"
redaction_required: true
provenance_chain:
  - "docs/analyses/archaeology/results/notebooks/environmental/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "HowTo"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"
  owl_time: "TemporalEntity"
json_schema_ref: "../../../../../schemas/json/archaeology-environmental-notebooks.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/archaeology-environmental-notebooks-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:results:notebooks:environmental-v11.0.0"
semantic_document_id: "kfm-arch-environmental-notebooks"
event_source_id: "ledger:docs/analyses/archaeology/results/notebooks/environmental/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Restricted / Environmental Only"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "restricted-ecological-knowledge"
  - "tribal-landscape-inference"
  - "identity-attribution"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
classification: "Internal / CARE-Governed"
jurisdiction: "Kansas / United States"
role: "archaeology-environmental-notebooks-root"
lifecycle_stage: "stable"
ttl_policy: "Review every 6 months"
sunset_policy: "Revised upon next environmental-modeling update"
---

<div align="center">

# 📓🌎 **Environmental Analysis Notebooks — Results Index**  
`docs/analyses/archaeology/results/notebooks/environmental/README.md`

**Purpose:**  
Serve as the centralized, sovereignty-safe index of **environmental modeling notebooks** used in the Kansas Frontier Matrix (KFM)—including climate, hydrology, soils, vegetation/biomass, ecozone transitions, terrain derivatives, and composite environmental drivers that support archaeological, landscape, and predictive modeling workflows.

</div>

---

## 📘 Overview

Environmental notebooks provide:

- reproducible pipelines for environmental variable computation  
- derivation of hydrology, soils, vegetation, climate, and terrain predictors  
- environmental-only correlation layers for archaeology  
- H3 r7+ generalization of any spatial surfaces  
- multi-driver environmental composite modeling  
- ecological/geomorphic time-slice analysis  
- uncertainty propagation and proxy disagreement mapping  
- PROV-O lineage export + redaction logs  
- FAIR+CARE compliance gates (no restricted ecological knowledge)  

All notebooks must **avoid**:

- deducing cultural land-use  
- linking environmental data to specific cultural identities  
- producing sub-H3 spatial precision  
- including tribal, restricted, or sacred ecological information  

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/results/notebooks/environmental/
├── README.md                           # This file
├── climate/                            # Climate, seasonality, precipitation/temp surfaces
├── hydrology/                          # Rivers, basins, terrace models, flow/accumulation
├── soils/                              # Soil chemistry, texture, fertility, pedology
├── vegetation/                         # Biomass, ecozones, canopy/groundcover modeling
├── terrain/                            # Elevation derivatives: slope, ruggedness, TRI, cost
├── composite/                          # Multi-driver combined environmental indices
├── paleoenvironment/                   # Paleo-climate & paleo-ecology reconstructions
├── uncertainty/                        # Proxy disagreement, variance, ensemble uncertainty
├── qa/                                 # QA notebooks: masking, H3 checks, environmental audits
└── exports/                            # Plots, rasters, CSV, JSON-LD summaries
~~~

---

## 🌎 Notebook Categories

### **1️⃣ Climate Notebooks (`climate/`)**
Produce:

- precipitation & temperature grids  
- seasonality metrics  
- extreme-weather statistical envelopes  
- climate stability windows  
- predictive environmental surfaces (non-cultural)  

---

### **2️⃣ Hydrology Notebooks (`hydrology/`)**
Generate:

- flow accumulation & watershed models  
- perennial hydrology predictors  
- terrace stability surfaces  
- floodplain environmental contexts  

---

### **3️⃣ Soil Notebooks (`soils/`)**
Include:

- pedogenic classification  
- soil chemistry + moisture index modeling  
- fertility & texture grids  
- soil–terrain–vegetation environmental composites  

---

### **4️⃣ Vegetation / Biomass Notebooks (`vegetation/`)**
Provide:

- ecozone classification  
- biomass/cover indices  
- vegetation stability  
- environmental affinity grouping  

---

### **5️⃣ Terrain Notebooks (`terrain/`)**
Contain:

- slope, ruggedness, hillshade derivatives  
- mobility cost-surface models  
- terrain advantage summaries  

---

### **6️⃣ Composite Environmental Notebooks (`composite/`)**
Integrate:

- climate  
- hydrology  
- soils  
- vegetation  
- terrain  

Outputs used for archaeological environmental-correlative modeling.

---

### **7️⃣ Paleoenviron. Notebooks (`paleoenvironment/`)**
Model:

- paleo-climate transitions  
- paleo-vegetation estimates  
- long-term environmental envelopes  
- uncertainty-heavy reconstructions  

No speculative cultural inference allowed.

---

### **8️⃣ Uncertainty Notebooks (`uncertainty/`)**
Track:

- proxy disagreement  
- ensemble variance  
- reconstruction spread  
- multi-driver buffer envelopes  

Outputs power Focus Mode **Environmental Confidence Chips**.

---

### **9️⃣ QA Notebooks (`qa/`)**
Perform:

- H3 integrity checks  
- masking & sovereignty validation  
- CARE sensitivity checks  
- environmental-range audits  
- redaction verification  

---

## 🧬 Metadata & Provenance

Each notebook must export:

- full `prov:Bundle` lineage JSON-LD  
- STAC-ready metadata for derived layers  
- DCAT JSON-LD descriptors  
- uncertainty summaries  
- configuration + reproducibility hashes  
- masking + generalization logs  

Outputs map into:

- `environmental/*/metadata/`  
- `environmental/*/stac/`  
- `environmental/*/provenance/`

---

## 🧠 Focus Mode Integration

Environmental notebooks feed:

- Story Node environmental context  
- Focus Mode v3 environmental-only narrative scaffolding  
- uncertainty chips  
- composite environmental overlays  

**Example Focus Summary:**

> **Focus Summary:**  
> These notebooks generate environmental-only predictor surfaces—climate, hydrology, terrain, soils, vegetation—used for safe archaeological context and multi-driver landscape modeling.

---

## 🛡 CARE & Ethical Requirements

All environmental analysis notebooks must:

- avoid sacred/restricted ecological knowledge  
- maintain environmental framing only  
- never tie environmental variables to cultural identity  
- include uncertainty + masking metadata  
- comply with sovereignty reviews  
- apply H3 r7+ spatial generalization  

---

## 🕰️ Version History

| Version | Date       | Author                                           | Summary |
|--------:|------------|--------------------------------------------------|---------|
| v11.0.0 | 2025-11-17 | Archaeology WG · Environmental Modeling WG · FAIR+CARE Council | Initial environmental-analysis notebook index. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Environmental Analysis Notebooks · CARE-Governed · FAIR+CARE Certified  
MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Notebooks Index](../README.md)

</div>
