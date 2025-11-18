---
title: "🕰️⛏️ Kansas Frontier Matrix — Stratigraphy Results: Temporal Correlation Models (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/stratigraphy/temporal-correlation/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly · Stratigraphy WG · Paleoenvironment WG · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/archaeology-stratigraphy-temporal-correlation-v1.json"
governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Stratigraphy Result"
intent: "archaeology-stratigraphy-temporal-correlation-results"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed / Subsurface-Generalized"
sensitivity_level: "High"
public_exposure_risk: "High"
indigenous_rights_flag: true
data_steward: "Stratigraphy WG · FAIR+CARE Council"
risk_category: "Temporal-Stratigraphic Modeling"
redaction_required: true
provenance_chain:
  - "docs/analyses/archaeology/results/stratigraphy/temporal-correlation/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E2 Temporal Entity"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"
json_schema_ref: "../../../../../schemas/json/archaeology-stratigraphy-temporal-correlation.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/archaeology-stratigraphy-temporal-correlation-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:stratigraphy:temporal-correlation-v11.0.0"
semantic_document_id: "kfm-arch-stratigraphy-temporal-correlation"
event_source_id: "ledger:docs/analyses/archaeology/results/stratigraphy/temporal-correlation/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Restricted / Environmental-Only"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "uncertainty-explanation"
ai_transform_prohibited:
  - "archaeological chronology inference"
  - "occupation-phase deduction"
  - "cultural-horizon correlation"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
classification: "Internal / Highly Sensitive / CARE-Governed"
jurisdiction: "Kansas / United States"
role: "archaeology-stratigraphy-temporal-correlation-root"
lifecycle_stage: "stable"
ttl_policy: "Review every 6 months"
sunset_policy: "Updated upon next temporal-stratigraphy framework revision"
---

<div align="center">

# 🕰️⛏️ **Stratigraphy Results — Temporal Correlation Models**  
`docs/analyses/archaeology/results/stratigraphy/temporal-correlation/README.md`

**Purpose:**  
Define and document generalized **temporal correlation models** used in the Kansas Frontier Matrix (KFM) to analyze **environmental-only stratigraphic transitions** across time.  
These models relate **broad depositional/geomorphic changes** to **paleoenvironmental intervals**, without allowing any cultural or archaeological inference.

</div>

---

## 📘 Overview

Temporal correlation models in KFM:

- align stratigraphic surfaces with **OWL-Time periods**  
- correlate depositional/geomorphic shifts with environmental drivers  
- propagate **uncertainty and variance across time windows**  
- apply **H3 r7+ spatial generalization**  
- provide environmental-only explanations for Focus Mode  
- map multi-period stratigraphic envelopes  
- avoid horizon-level, cultural, or archaeological interpretations  

They are expressly forbidden from:

- interpreting cultural layers  
- correlating soil/stratigraphy to occupations or people  
- modeling precise stratigraphic sequences  
- reconstructing buried features or horizons  

All outputs remain **coarse-scale, generalized environmental indicators**.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/results/stratigraphy/temporal-correlation/
├── README.md                         # This file
├── intervals/                        # OWL-Time interval alignment
├── multi-period/                     # Multi-interval environmental transitions
├── drivers/                          # Climate/hydrology/terrain drivers
├── envelopes/                        # Generalized temporal envelopes
├── uncertainty/                      # Temporal spread, disagreement, variance
├── stac/                             # STAC for temporal-correlation surfaces
├── metadata/                         # DCAT + JSON-LD metadata
└── provenance/                       # PROV-O lineage bundles
~~~

---

## 🕰️ Temporal Correlation Components

### **1️⃣ OWL-Time Interval Alignment (`intervals/`)**
Defines:

- generalized time spans  
- environmental-window correlation  
- temporal smoothing  

---

### **2️⃣ Multi-Period Models (`multi-period/`)**
Describe:

- transitions across multiple environmental eras  
- long-term geomorphic/depositional change  
- paleo-to-holocene environmental drift  

---

### **3️⃣ Driver Correlation (`drivers/`)**
Tracks:

- climate-driven stratigraphic shifts  
- soil moisture cycles  
- hydrologic phase changes  
- terrain-linked temporal patterns  

---

### **4️⃣ Temporal Envelopes (`envelopes/`)**
Include:

- probability envelopes for environmental stratigraphy  
- generalized “change windows”  
- sovereignty-safe temporal smoothing  

---

## ⚠️ Uncertainty (`uncertainty/`)
Covers:

- proxy disagreement  
- ensemble spread  
- smoothing variance  
- temporal ambiguity  

Displayed in Focus Mode as **Temporal Correlation Confidence Chips**.

---

## 🧬 Metadata & Provenance Requirements

### **STAC (`stac/`)**
Includes:

- generalized H3 geometry  
- temporal extent  
- driver metadata  
- PROV-O lineage  
- uncertainty blocks  

### **DCAT (`metadata/`)**
Documents:

- dataset scope  
- FAIR+CARE compliance  
- environmental narrative constraints  

### **PROV-O (`provenance/`)**
Tracks:

- environmental drivers  
- smoothing rules  
- masking logs  
- WAL → Retry → Rollback lineage  

---

## 🧠 Focus Mode Integration

Temporal-correlation layers supply:

- environmental-only temporal narratives  
- generalized geomorphic backgrounds  
- uncertainty-duration summaries  
- safe timeline anchors for Story Nodes  

**Example Focus Summary:**  
> Temporal-correlation models show environmental, multi-period stratigraphic tendencies without revealing or reconstructing sensitive subsurface information.

---

## 🛡 CARE & Ethical Requirements

Models **must**:

- prevent cultural/archaeological inference  
- mask all spatial detail at H3 r7+  
- disclose uncertainty  
- document masking & redaction  
- undergo FAIR+CARE review  

Violations → **generalize or remove**.

---

## 🕰️ Version History

| Version | Date       | Author                                | Summary |
|--------:|------------|---------------------------------------|---------|
| v11.0.0 | 2025-11-17 | Stratigraphy WG · FAIR+CARE Council   | Initial temporal-correlation registry under MDP v11. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Temporal Correlation Stratigraphy · FAIR+CARE Certified · Sovereignty-Protected  
Diamond⁹ Ω · Crown∞Ω Ultimate Certified  

[Back to Stratigraphy Results](../README.md)

</div>
