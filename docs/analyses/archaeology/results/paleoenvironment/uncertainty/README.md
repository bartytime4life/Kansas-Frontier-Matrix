---
title: "🌫️📜 Kansas Frontier Matrix — Paleoenviron. Results: Uncertainty & Proxy Disagreement (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/paleoenvironment/uncertainty/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly · Paleoenvironment WG · Archaeology WG · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/archaeology-paleoenv-uncertainty-v1.json"
governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Uncertainty Registry"
intent: "archaeology-paleoenvironment-uncertainty-results"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed / Environmental Reconstruction Uncertainty"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
indigenous_rights_flag: true
data_steward: "Paleoenvironment WG · FAIR+CARE Council"
risk_category: "Environmental Uncertainty Modeling"
redaction_required: true
provenance_chain:
  - "docs/analyses/archaeology/results/paleoenvironment/uncertainty/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E1 CRM Entity"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  owl_time: "TemporalEntity"
json_schema_ref: "../../../../../schemas/json/archaeology-paleoenv-uncertainty-results.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/archaeology-paleoenv-uncertainty-results-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:paleoenvironment:uncertainty-v11.0.0"
semantic_document_id: "kfm-arch-paleoenv-uncertainty-results"
event_source_id: "ledger:docs/analyses/archaeology/results/paleoenvironment/uncertainty/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Restricted / Environmental-Only"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "uncertainty-explanation"
ai_transform_prohibited:
  - "cultural-inference"
  - "sensitive-locational-deduction"
  - "historical or cultural reconstruction"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
classification: "Internal / CARE-Governed"
jurisdiction: "Kansas / United States"
role: "archaeology-paleoenvironment-uncertainty-root"
lifecycle_stage: "stable"
ttl_policy: "Review every 6 months"
sunset_policy: "Updated when paleoenvironment uncertainty framework changes"
---

<div align="center">

# 🌫️📜 **Paleoenvironmental Results — Uncertainty Registry**  
`docs/analyses/archaeology/results/paleoenvironment/uncertainty/README.md`

**Purpose:**  
Define the **uncertainty modeling framework** for all paleoenvironmental reconstructions in the Kansas Frontier Matrix (KFM).  
This includes proxy disagreement, variance surfaces, ensemble spread, reconstruction ambiguity, and multi-proxy uncertainty envelopes—always generalized, sovereignty-safe, and environmentally framed.

</div>

---

## 📘 Overview

Paleoenvironmental uncertainty layers:

- quantify **proxy disagreement** (pollen/charcoal/isotopes/lake cores)  
- capture **environmental-model reconstruction error**  
- express **spatial/temporal variance** in OWL-Time aligned sequences  
- represent **ensemble spread** from multi-model or multi-proxy runs  
- record **environmental ambiguity**, not cultural ambiguity  
- provide **uncertainty chips** used in Focus Mode v3  
- support Story Node environmental-context generation  
- enforce **H3 r7+ spatial generalization**  
- maintain sovereignty and cultural-safety  

Prohibited:

- using uncertainty to infer cultural timelines  
- implying cultural events or behaviors  
- revealing sensitive paleo-locations  
- connecting paleoenvironment variability to cultural identity  

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/results/paleoenvironment/uncertainty/
├── README.md                        # This file
├── proxy-disagreement/              # Proxy conflict (pollen/charcoal/isotopes)
├── variance/                        # Variance / spread layers
├── ensemble/                        # Ensemble spread + model fragility
├── temporal/                        # OWL-Time uncertainty windows
├── spatial/                         # H3 r7+ spatial uncertainty fields
├── drivers/                         # Uncertainty tied to climate/hydrology/soil drivers
├── stac/                            # STAC Items for uncertainty layers
├── metadata/                        # DCAT + JSON-LD metadata
└── provenance/                      # PROV-O lineage for uncertainty modeling
~~~

---

## 🌫️ Uncertainty Types

### **1️⃣ Proxy Disagreement (`proxy-disagreement/`)**
Tracks:

- pollen vs charcoal  
- charcoal vs isotopes  
- isotopes vs sediment proxies  
- disagreement clusters  

Outputs define *environmental ambiguity*, not cultural signals.

---

### **2️⃣ Variance Surfaces (`variance/`)**
Include:

- reconstruction variance  
- anomaly-spread metrics  
- temporal smoothing error  
- model-derived environmental uncertainty  

---

### **3️⃣ Ensemble Spread (`ensemble/`)**
Represent:

- multi-model divergence  
- environmental fragility  
- proxy-weight variability  
- scenario-wide disagreement  

---

### **4️⃣ Temporal Uncertainty (`temporal/`)**
OWT-Time aligned:

- period-based reconstruction spread  
- time-window variance envelopes  
- temporal ambiguity surfaces  

---

### **5️⃣ Spatial Uncertainty (`spatial/`)**
Provide:

- H3 r7+ generalized spatial error patterns  
- proxy-density uncertainty  
- smoothing-range effects  
- no sub-H3 detail  

---

### **6️⃣ Driver-Based Uncertainty (`drivers/`)**
Track ambiguity in:

- climate  
- hydrology  
- soils  
- vegetation  
- ecohydrological cycles  

Never cultural or archaeological drivers.

---

## 🧬 Metadata & Lineage Requirements

### **STAC (`stac/`)**
Uncertainty STAC Items must include:

- generalized geometry  
- uncertainty-type designation  
- proxy sources (generalized, PD-safe)  
- lineage linking to provenance bundles  
- environmental-only roles  

### **DCAT (`metadata/`)**
Documents:

- dataset purpose  
- FAIR+CARE constraints  
- uncertainty methodology  
- distribution & licensing  

### **PROV-O (`provenance/`)**
Tracks:

- reconstruction methods  
- interpolation & smoothing  
- environmental models used  
- masking/generalization  
- uncertainty propagation steps  

---

## 🧠 Focus Mode Integration

Uncertainty layers provide:

- “Uncertainty Chips”  
- environmental ambiguity summaries  
- temporal-spread indicators  
- context for Story Nodes (environment-only)  

**Example Focus Summary:**  
> Paleoenvironmental uncertainty layers reflect where proxy data disagree or models produce ambiguous environmental outcomes—never cultural or historical interpretations.

---

## 🛡 CARE & Ethical Requirements

All uncertainty outputs must:

- avoid cultural-inference pathways  
- maintain generalized spatial/temporal forms  
- include redaction + generalization logs  
- ensure proxy anonymity where required  
- be sovereignty-reviewed  
- disclose methodological limits  

If a layer risks misinterpretation → **it must be generalized or removed**.

---

## 🕰️ Version History

| Version | Date       | Author                                       | Summary |
|--------:|------------|----------------------------------------------|---------|
| v11.0.0 | 2025-11-17 | Paleoenvironment WG · FAIR+CARE Council      | Initial paleoenvironment uncertainty registry. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Paleoenvironment Uncertainty Layers · FAIR+CARE Certified · Sovereignty-Safe  
Diamond⁹ Ω · Crown∞Ω Ultimate Certified  

[Back to Paleoenvironment Results](../README.md)

</div>
