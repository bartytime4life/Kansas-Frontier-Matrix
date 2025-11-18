---
title: "🪨🌍 Kansas Frontier Matrix — Stratigraphy Results: Geomorphology Models (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/stratigraphy/geomorphology/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly · Stratigraphy WG · Paleoenvironment WG · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/archaeology-stratigraphy-geomorphology-v1.json"
governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Stratigraphy Result"
intent: "archaeology-stratigraphy-geomorphology-results"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed / Subsurface-Generalized"
sensitivity_level: "High"
public_exposure_risk: "High"
indigenous_rights_flag: true
data_steward: "Stratigraphy WG · FAIR+CARE Council"
risk_category: "Geomorphic Interpretation (Generalized)"
redaction_required: true
provenance_chain:
  - "docs/analyses/archaeology/results/stratigraphy/geomorphology/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E1 CRM Entity"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"
  owl_time: "TemporalEntity"
json_schema_ref: "../../../../../schemas/json/archaeology-stratigraphy-geomorphology-results.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/archaeology-stratigraphy-geomorphology-results-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:stratigraphy:geomorphology-v11.0.0"
semantic_document_id: "kfm-arch-stratigraphy-geomorphology-results"
event_source_id: "ledger:docs/analyses/archaeology/results/stratigraphy/geomorphology/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Restricted / Environmental-Only"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "uncertainty-explanation"
ai_transform_prohibited:
  - "feature-level geomorphic inference"
  - "burial-or-structure attribution"
  - "cultural landscape speculation"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
classification: "Internal / Highly Sensitive / CARE-Governed"
jurisdiction: "Kansas / United States"
role: "archaeology-stratigraphy-geomorphology-root"
lifecycle_stage: "stable"
ttl_policy: "Review every 6 months"
sunset_policy: "Updated when geomorphic modeling framework changes"
---

<div align="center">

# 🪨🌍 **Stratigraphy Results — Geomorphology Models**  
`docs/analyses/archaeology/results/stratigraphy/geomorphology/README.md`

**Purpose:**  
Document all **generalized geomorphology models** used in Kansas Frontier Matrix (KFM) stratigraphy and paleoenvironmental reconstruction.  
These models describe **broad geomorphic tendencies**—terrain evolution, landscape processes, sediment mobility—without revealing sensitive subsurface or cultural information.

</div>

---

## 📘 Overview

Geomorphological results in KFM:

- describe **landform evolution** (generalized)  
- model **erosion–deposition balances**  
- estimate **sediment transport regimes**  
- integrate climate, hydrology, terrain, and soil predictors  
- mask all spatial detail using **H3 r7+ generalization**  
- align with **OWL-Time** for multi-period interpretation  
- quantify geomorphic **uncertainty**  
- avoid any cultural or feature-level inference  

Outputs support:

- environmental context for archaeology  
- broad geomorphic setting for Story Nodes  
- Focus Mode geomorphic reasoning panels  

Absolutely prohibited:

- inferring archaeological site formation  
- predicting or revealing buried cultural features  
- detailed horizon-level stratigraphy  
- any fine-scale morphology that could compromise sovereignty  

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/results/stratigraphy/geomorphology/
├── README.md                           # This file
├── landforms/                          # Generalized landform classifications
├── erosion/                            # Erosion-rate tendencies & geomorphic stress
├── deposition/                         # Deposition/accumulation envelopes
├── surfaces/                           # Geomorphic surface reconstructions
├── terrain-derivatives/                # Slope, TPI, TRI, ruggedness (generalized)
├── composite/                          # Multi-driver geomorphic models
├── temporal/                           # OWL-Time aligned geomorphic changes
├── uncertainty/                        # Variance & geomorphic disagreement
├── stac/                               # STAC Items for geomorphology layers
├── metadata/                           # DCAT + JSON-LD metadata
└── provenance/                         # PROV-O lineage bundles
~~~

---

## 🪨 Geomorphology Model Types

### **1️⃣ Landforms (`landforms/`)**
Generalized landform categories:

- terrace belts  
- valley floors  
- upland ridges  
- eolian plains  
- alluvial fans  

Never feature- or site-specific.

---

### **2️⃣ Erosion Models (`erosion/`)**
Include:

- broad erosion stress zones  
- slope–climate erosion tendencies  
- hydrological erosion categories  
- generalized geomorphic vulnerability  

---

### **3️⃣ Deposition Models (`deposition/`)**
Contain:

- deposition tendency envelopes  
- floodplain/debris-flow generalizations  
- sediment accumulation windows  

---

### **4️⃣ Geomorphic Surfaces (`surfaces/`)**
Provide:

- geomorphic stability surfaces  
- paleo-surface tendencies  
- general uplift/subsidence summaries  

---

### **5️⃣ Terrain Derivatives (`terrain-derivatives/`)**
Generalized:

- slope  
- ruggedness  
- topographic position index  
- cost-surface tendencies  

---

### **6️⃣ Composite Geomorphology (`composite/`)**
Integrate:

- hydrology  
- climate  
- soils  
- vegetation  
- terrain  
- sediment transport  

All outputs remain environmental-only.

---

### **7️⃣ Temporal Geomorphology (`temporal/`)**
OWL-Time aligned:

- multi-period geomorphic change  
- landform transitions  
- geomorph stability windows  

---

## ⚠️ Uncertainty (`uncertainty/`)

Tracks:

- model fragility  
- environmental disagreement  
- smoothing & generalization variance  
- “Geomorph Confidence Chips” for Focus Mode  

---

## 🧬 Metadata & Provenance Requirements

### **STAC (`stac/`)**
STAC Items must include:

- H3-masked geometry  
- temporal extent  
- geomorph drivers  
- uncertainty layers  
- PROV-O lineage references  

### **DCAT (`metadata/`)**
Defines:

- dataset purpose  
- FAIR+CARE constraints  
- distribution metadata  
- environmental-only scope  

### **PROV-O (`provenance/`)**
Tracks:

- reconstruction procedure  
- environmental drivers used  
- redaction & generalization  
- WAL → Retry → Rollback lineage  
- uncertainty propagation  

---

## 🧠 Focus Mode Integration

Geomorphology results provide:

- environmental setting  
- landform-level reasoning  
- uncertainty/context chips  
- temporal narrative backdrops  

**Example Focus Summary:**  
> Geomorphology models describe environmental evolution and terrain tendencies without implying subsurface cultural features or site formation processes.

---

## 🛡 CARE & Ethical Requirements

All geomorphology datasets must:

- avoid cultural or archaeological inference  
- enforce H3 r7+ masking  
- disclose uncertainty  
- document redaction steps  
- maintain sovereignty safeguards  
- pass FAIR+CARE review  

If unsafe geomorphic detail appears → **generalize or remove.**

---

## 🕰️ Version History

| Version | Date       | Author                                      | Summary |
|--------:|------------|---------------------------------------------|---------|
| v11.0.0 | 2025-11-17 | Stratigraphy WG · FAIR+CARE Council         | Initial geomorphology model registry (MDP v11). |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Geomorphology Results · FAIR+CARE Certified · Sovereignty-Protected  
Diamond⁹ Ω · Crown∞Ω Ultimate Certified  

[Back to Stratigraphy Results](../README.md)

</div>
