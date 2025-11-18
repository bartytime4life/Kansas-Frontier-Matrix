---
title: "🌫️⛏️ Kansas Frontier Matrix — Stratigraphy Results: Uncertainty & Model Disagreement (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/stratigraphy/uncertainty/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly · Stratigraphy WG · Paleoenvironment WG · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/archaeology-stratigraphy-uncertainty-v1.json"
governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Uncertainty Registry"
intent: "archaeology-stratigraphy-uncertainty-results"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed / Subsurface Generalization Required"
sensitivity_level: "High"
public_exposure_risk: "High"
indigenous_rights_flag: true
data_steward: "Stratigraphy WG · FAIR+CARE Council"
risk_category: "Subsurface Uncertainty"
redaction_required: true
provenance_chain:
  - "docs/analyses/archaeology/results/stratigraphy/uncertainty/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E1 CRM Entity"
  prov_o: "prov:Entity"
  schema_org: "Dataset"
  geosparql: "geo:FeatureCollection"
  owl_time: "TemporalEntity"
json_schema_ref: "../../../../../schemas/json/archaeology-stratigraphy-uncertainty.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/archaeology-stratigraphy-uncertainty-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:stratigraphy:uncertainty-v11.0.0"
semantic_document_id: "kfm-arch-stratigraphy-uncertainty"
event_source_id: "ledger:docs/analyses/archaeology/results/stratigraphy/uncertainty/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Restricted / Environmental-Only"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "uncertainty-explanation"
ai_transform_prohibited:
  - "horizon inference"
  - "cultural-period correlation"
  - "feature-level subsurface reconstruction"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
classification: "Internal / Highly Sensitive / CARE-Governed"
jurisdiction: "Kansas / United States"
role: "archaeology-stratigraphy-uncertainty-root"
lifecycle_stage: "stable"
ttl_policy: "Review every 6 months"
sunset_policy: "Update upon next uncertainty-framework revision"
---

<div align="center">

# 🌫️⛏️ **Stratigraphy Results — Uncertainty & Model Disagreement**  
`docs/analyses/archaeology/results/stratigraphy/uncertainty/README.md`

**Purpose:**  
Define the uncertainty modeling, variance tracking, proxy disagreement analysis, and fragility assessment for **generalized stratigraphic surfaces** within the Kansas Frontier Matrix (KFM).  
All stratigraphic uncertainty outputs must be fully **environment-only**, **H3-generalized**, **sovereignty-safe**, and **FAIR+CARE compliant**.

</div>

---

## 📘 Overview

Stratigraphic uncertainty layers:

- quantify **disagreement** between depositional/geomorphic/pedogenic models  
- track **variance** in environmental drivers (climate, hydrology, soils, terrain)  
- document **model fragility** and smoothing ambiguity  
- propagate **uncertainty** across OWL-Time temporal windows  
- enforce H3 r7+ masking of all spatial outputs  
- include sovereignty-review logs  
- power **Confidence Chips** in Focus Mode  
- supply environmental-only uncertainty context for Story Nodes  
- MUST NOT support archaeological inference of any kind  

Explicit prohibitions:

- subsurface feature prediction  
- horizon-level interpretation  
- cultural attribution or period correlation  
- revealing sensitive geomorph or pedogenic detail  

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/results/stratigraphy/uncertainty/
├── README.md                         # This file
├── variance/                         # Variance surfaces for stratigraphic processes
├── disagreement/                     # Proxy & model conflict layers
├── ensemble/                         # Ensemble spread analysis
├── drivers/                          # Driver-specific uncertainty (climate, hydrology, soils)
├── temporal/                         # OWL-Time aligned uncertainty windows
├── spatial/                          # H3-generalized spatial error surfaces
├── stac/                             # STAC Items for uncertainty layers
├── metadata/                         # DCAT + JSON-LD metadata
└── provenance/                       # PROV-O lineage for uncertainty processing
~~~

---

## 🌫️ Uncertainty Categories

### **1️⃣ Variance (`variance/`)**
Includes:

- reconstruction variance  
- smoothing ambiguity  
- proxy-spread metrics  
- stratigraphic envelope fragility  

---

### **2️⃣ Model & Proxy Disagreement (`disagreement/`)**
Tracks:

- depositional model conflict  
- geomorphic disagreement  
- pedogenic divergence  
- climate/hydrology/soil-driver disagreement  

---

### **3️⃣ Ensemble Spread (`ensemble/`)**
Documents:

- multi-model spread  
- environmental fragility  
- long-term divergence  
- composite stratigraphic uncertainty  

---

### **4️⃣ Driver Uncertainty (`drivers/`)**
Contains uncertainty from:

- climate variability  
- hydrologic fluctuation  
- vegetation/biomass influence  
- soil-formation drivers  
- terrain instability  

---

### **5️⃣ Temporal Uncertainty (`temporal/`)**
OWL-Time aligned:

- multi-period disagreement  
- shift windows  
- forward/backward uncertainty  
- paleo-to-present ambiguity  

---

### **6️⃣ Spatial Uncertainty (`spatial/`)**
Includes:

- H3 r7+ spatial masking  
- smoothing window variability  
- local-to-regional environmental fragility  

Never sub-H3.

---

## 🧬 Metadata & Provenance Requirements

### **STAC (`stac/`)**
Uncertainty STAC Items must include:

- H3-generalized geometry  
- uncertainty blocks  
- environmental drivers  
- PROV-O lineage links  
- sovereignty classification  

### **DCAT (`metadata/`)**
Documents:

- dataset purpose  
- FAIR+CARE metadata  
- access rights  
- temporal extent  
- environmental-only framing  

### **PROV-O (`provenance/`)**
Tracks:

- lineage of environmental predictors  
- uncertainty propagation steps  
- smoothing/interpolation decisions  
- masking & redaction logs  
- WAL → Retry → Rollback lineage  

---

## 🧠 Focus Mode Integration

Uncertainty layers provide:

- “Stratigraphy Confidence Chips”  
- environmental contextual uncertainty  
- proxy/driver disagreement summaries  
- sovereignty-safe interpretation aids  

**Example Focus Summary:**  
> Stratigraphy uncertainty layers reflect where environmental models diverge, documenting fragility and proxy disagreement while avoiding any feature-level or cultural interpretation.

---

## 🛡 CARE & Ethical Requirements

All uncertainty layers must:

- remain environmental-only  
- NOT enable subsurface inference  
- mask spatial detail to H3 r7+  
- include masking/redaction logs  
- disclose uncertainty transparently  
- pass FAIR+CARE & sovereignty review  

If unsafe → **redact or remove**.

---

## 🕰️ Version History

| Version | Date       | Author                                 | Summary |
|--------:|------------|----------------------------------------|---------|
| v11.0.0 | 2025-11-17 | Stratigraphy WG · FAIR+CARE Council    | Initial stratigraphy uncertainty registry under MDP v11. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Stratigraphy Uncertainty Registry · FAIR+CARE Certified · Sovereignty-Protected  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Stratigraphy Results](../README.md)

</div>
