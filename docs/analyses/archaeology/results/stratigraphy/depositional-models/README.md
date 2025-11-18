---
title: "⛏️📚 Kansas Frontier Matrix — Stratigraphy Results: Depositional Models (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/stratigraphy/depositional-models/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly · Stratigraphy WG · Paleoenvironment WG · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/archaeology-stratigraphy-depositional-v1.json"
governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Stratigraphy Result"
intent: "archaeology-stratigraphy-depositional-models"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed / Subsurface-Generalized"
sensitivity_level: "High"
public_exposure_risk: "High"
indigenous_rights_flag: true
data_steward: "Stratigraphy WG · FAIR+CARE Council"
risk_category: "Stratigraphic Interpretation (Generalized)"
redaction_required: true
provenance_chain:
  - "docs/analyses/archaeology/results/stratigraphy/depositional-models/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E1 CRM Entity"
  prov_o: "prov:Entity"
  schema_org: "Dataset"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"
json_schema_ref: "../../../../../schemas/json/archaeology-stratigraphy-depositional-models.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/archaeology-stratigraphy-depositional-models-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:stratigraphy:depositional-models-v11.0.0"
semantic_document_id: "kfm-arch-stratigraphy-depositional-models"
event_source_id: "ledger:docs/analyses/archaeology/results/stratigraphy/depositional-models/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Restricted / Environmental-Only"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "uncertainty-explanation"
ai_transform_prohibited:
  - "feature-level stratigraphic inference"
  - "burial-or-structure interpretation"
  - "cultural stratigraphy speculation"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
classification: "Internal / Highly Sensitive / CARE-Governed"
jurisdiction: "Kansas / United States"
role: "archaeology-stratigraphy-depositional-models-root"
lifecycle_stage: "stable"
ttl_policy: "Review every 6 months"
sunset_policy: "Updated on next stratigraphic modeling framework revision"
---

<div align="center">

# ⛏️📚 **Stratigraphy Results — Depositional Models**  
`docs/analyses/archaeology/results/stratigraphy/depositional-models/README.md`

**Purpose:**  
Provide the sovereignty-safe documentation for **generalized depositional models** used across KFM stratigraphy, paleoenvironmental reconstruction, and archaeological landscape interpretation.  
These models characterize **broad depositional regimes**, **sediment dynamics**, and **geomorphic tendencies** without revealing or implying specific subsurface features.

</div>

---

## 📘 Overview

Depositional models in KFM provide:

- generalized stratigraphic surfaces  
- inferred depositional environments (alluvial, colluvial, eolian, lacustrine—but *generalized*)  
- environmental-only drivers (hydrology, climate, slope, vegetation)  
- long-term sedimentation tendencies  
- uncertainty envelopes & proxy disagreement  
- H3 r7+ masking of all spatial outputs  
- OWL-Time aligned depositional sequences  
- PROV-O lineage documenting environmental reconstruction steps  

They **never** include:

- site-level sediment interpretation  
- burial or structure-inference  
- cultural-period depositional claims  
- sub-H3 sediment horizon geometry  

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/results/stratigraphy/depositional-models/
├── README.md                           # This file
├── alluvial/                           # Generalized fluvial deposition models
├── colluvial/                          # Hillslope/colluvial accumulation envelopes
├── eolian/                             # Eolian deposition & mobility tendencies
├── lacustrine/                         # Paleo-lake & nearshore depositional surfaces
├── composite/                          # Multi-driver depositional models
├── temporal/                           # OWL-Time depositional sequences
├── uncertainty/                        # Variance, disagreement, reconstruction spread
├── stac/                               # STAC Items for depositional surfaces
├── metadata/                           # DCAT + JSON-LD metadata
└── provenance/                         # PROV-O depositional lineage bundles
~~~

---

## 🌎 Depositional Model Types

### **1️⃣ Alluvial Models (`alluvial/`)**
Represent:

- generalized fluvial deposition zones  
- floodplain accumulation envelopes  
- channel-migration broad patterns (non-feature)  
- hydrology-driven sediment mobility  

---

### **2️⃣ Colluvial Models (`colluvial/`)**
Include:

- hillslope sediment redistribution  
- gradient-controlled deposition tendencies  
- slope/sediment/vegetation interactions  

---

### **3️⃣ Eolian Models (`eolian/`)**
Contain:

- wind-driven sedimentation envelopes  
- dune-mobility zones (generalized)  
- deposition vs deflation tendencies  

---

### **4️⃣ Lacustrine Models (`lacustrine/`)**
Provide:

- paleo-lake margin deposition windows  
- sediment-loading gradients  
- shoreline environmental envelopes  

---

### **5️⃣ Composite Depositional Models (`composite/`)**
Integrate:

- hydrology  
- slope  
- wind  
- soils  
- vegetation  
- climate  

Outputs generate **environmental depositional envelopes**, never feature-level stratigraphy.

---

### **6️⃣ Temporal Depositional Models (`temporal/`)**
OWL-Time aligned:

- multi-period depositional trends  
- sedimentation regime transitions  
- long-term geomorphic windows  

---

## ⚠️ Uncertainty (`uncertainty/`)

Uncertainty layers track:

- proxy disagreement  
- model fragility  
- variance across reconstruction steps  
- smoothing/aggregation ambiguity  

Displayed as **Depositional Confidence Chips** in Focus Mode.

---

## 🧬 Metadata & Provenance Standards

### **STAC (`stac/`)**
Depositional STAC Items include:

- H3 generalized geometry  
- temporal extent metadata  
- environmental drivers  
- uncertainty metadata  
- lineage references  

### **DCAT (`metadata/`)**
Documents:

- environmental-only purpose  
- dataset scope  
- FAIR+CARE tags  
- spatial/temporal coverage  

### **PROV-O (`provenance/`)**
Tracks:

- proxy sources  
- environmental drivers  
- interpolation & smoothing  
- masking & redaction  
- WAL → Retry → Rollback lineage  

---

## 🧠 Focus Mode Integration

Depositional models provide:

- environmental geomorphic context  
- uncertainty chips  
- temporal depositional summaries  
- generalized stratigraphic background for Story Nodes  

**Example Focus Summary:**  
> Depositional models show broad sedimentation tendencies—generalized, sovereignty-safe, and environmental-only—without revealing sensitive stratigraphic information.

---

## 🛡 CARE & Ethical Requirements

All depositional model outputs must:

- apply H3 r7+ masking  
- avoid cultural or feature-level inference  
- include uncertainty documentation  
- undergo FAIR+CARE review  
- maintain environmental framing only  

If any model risks exposing sensitive subsurface knowledge → **generalize or remove**.

---

## 🕰️ Version History

| Version | Date       | Author                                   | Summary |
|--------:|------------|------------------------------------------|---------|
| v11.0.0 | 2025-11-17 | Stratigraphy WG · FAIR+CARE Council       | Initial depositional model registry under MDP v11. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Depositional Models · FAIR+CARE Certified · Sovereignty-Protected  
Diamond⁹ Ω · Crown∞Ω Ultimate Certified  

[Back to Stratigraphy Results](../README.md)

</div>
