---
title: "🧭🧲 Kansas Frontier Matrix — Geophysics Results: Magnetometry Analyses (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/geophysics/magnetometry/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly · Geophysics WG · Archaeology WG · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/archaeology-geophysics-magnetometry-v1.json"
governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Geophysics Result"
intent: "archaeology-geophysics-magnetometry-results"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed / Sensitive-Surface Geophysics"
sensitivity_level: "High"
public_exposure_risk: "Medium"
indigenous_rights_flag: true
data_steward: "Geophysics WG · Archaeology WG · FAIR+CARE Council"
risk_category: "Subsurface Interpretation (Generalized Magnetometry)"
redaction_required: true
provenance_chain:
  - "docs/analyses/archaeology/results/geophysics/magnetometry/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E26 Physical Feature"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"
  owl_time: "TemporalEntity"
json_schema_ref: "../../../../../schemas/json/archaeology-geophysics-magnetometry-results.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/archaeology-geophysics-magnetometry-results-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:geophysics:magnetometry-results-v11.0.0"
semantic_document_id: "kfm-arch-geophysics-magnetometry-results"
event_source_id: "ledger:docs/analyses/archaeology/results/geophysics/magnetometry/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Restricted"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "environmental-linking"
ai_transform_prohibited:
  - "feature-inference"
  - "structure-identification"
  - "burial-detection"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Internal / CARE-Governed"
role: "archaeology-geophysics-magnetometry-root"
lifecycle_stage: "stable"
ttl_policy: "Review every 6 months"
sunset_policy: "Superseded on next magnetometry-results update"
---

<div align="center">

# 🧭🧲 **Geophysics Results — Magnetometry**  
`docs/analyses/archaeology/results/geophysics/magnetometry/README.md`

**Purpose:**  
Provide a FAIR+CARE–aligned registry of **magnetometry-based geophysics results**, documenting broad, environmentally grounded magnetic variation patterns that support archaeological landscape analysis while **never revealing feature-level subsurface information**.

</div>

---

## 📘 Overview

Magnetometry analyses in the Kansas Frontier Matrix (KFM):

- describe **generalized magnetic signal variation**, not feature shapes  
- integrate multi-sensor environmental drivers  
- produce **H3 r7+ masked anomaly envelopes**  
- include uncertainty, noise, and drift-correction metadata  
- avoid ANY structure/burial/pit inference  
- harmonize with Story Node v3 & Focus Mode v3 environmental narratives  
- rely exclusively on **sovereignty-approved, culturally safe workflows**

These results represent **patterns**, not archaeological features.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/results/geophysics/magnetometry/
├── README.md                                   # This file
├── gradients/                                  # Generalized magnetic gradient envelopes
├── envelopes/                                  # H3 anomaly envelope fields
├── composite/                                  # Multi-sensor integrated magnetic surfaces
├── environmental-links/                        # Hydrology/soil/terrain correlations
├── temporal/                                    # OWL-Time aligned magnetometry tendencies
├── uncertainty/                                 # Noise, drift, and disagreement layers
├── stac/                                        # STAC Items for magnetometry outputs
├── metadata/                                    # DCAT + JSON-LD metadata
└── provenance/                                  # PROV-O lineage & processing logs
~~~

---

## 🧲 Magnetometry Result Types

### **1️⃣ Magnetic Gradient Surfaces (`gradients/`)**
Contain:

- broad magnetic-field variation  
- slope/derivative summaries  
- anomaly-intensity zones (generalized)

No feature interpretation is permitted.

---

### **2️⃣ Magnetic Envelope Fields (`envelopes/`)**
Provide spatially masked:

- anomaly concentration envelopes (H3 r7+)  
- KDE smoothed variation zones  
- safe anomaly-block summaries  

Always generalized beyond feature resolution.

---

### **3️⃣ Composite Magnetic Models (`composite/`)**
Integrate:

- magnetometry  
- EMI susceptibilities  
- resistivity variation  
- GPR amplitude zones  

Produces multi-sensor “environmental magnetic tendency” surfaces.

---

### **4️⃣ Environmental Correlations (`environmental-links/`)**
Describe relationships with:

- hydrology (terraces, channels, drainage)  
- soil types / pedogenic horizons  
- terrain geometry  
- vegetation/biomass  
- geomorphic stability  

Environmental-only interpretations.

---

### **5️⃣ Temporal Magnetic Patterns (`temporal/`)**
Use OWL-Time to summarize:

- long-term magnetic field variability  
- environmental moisture-linked signal shifts  
- multi-period magnetic stability  

No cultural chronology inference.

---

## ⚠️ Uncertainty Layers (`uncertainty/`)  
Store:

- diurnal drift variation  
- noise-field envelopes  
- environmental disagreement surfaces  
- cross-sensor inconsistency metrics  

Displayed in Focus Mode as **Magnetometry Confidence Chips**.

---

## 🧬 Metadata & Provenance Requirements

### **STAC (`stac/`)**
Magnetometry STAC Items must include:

- H3-masked geometry  
- environmental drivers  
- uncertainty layers  
- diurnal/drift correction metadata  
- CARE classification  
- PROV-O lineage links  

### **DCAT (`metadata/`)**
Document:

- dataset description  
- access restrictions  
- FAIR+CARE governance metadata  
- distribution format  

### **PROV-O (`provenance/`)**
Tracks:

- raw magnetometry files  
- drift correction  
- filtering & gridding  
- H3 masking  
- smoothing (KDE/derivative)  
- uncertainty propagation  
- WAL → Retry → Rollback lineage  

---

## 🧠 Focus Mode Integration

Magnetometry results support:

- environmental-only magnetic context blocks  
- safe anomaly-explanation overlays  
- multi-sensor narrative integration  
- Story Node contextual enhancement  

Example Focus Summary:

> **Focus Summary:**  
> Generalized magnetometry surfaces highlight broad magnetic-variation zones shaped by soils, hydrology, and geomorphology. No feature-level interpretations are included; all outputs comply with FAIR+CARE cultural safety rules.

---

## 🛡 CARE & Ethical Requirements

All magnetometry outputs must:

- generalize to H3 r7+  
- avoid feature-level interpretation  
- avoid identifying structures, burials, or cultural features  
- include uncertainty indicators  
- undergo sovereignty + FAIR+CARE review  
- document masking and redaction steps  

If any output risks implying sensitive subsurface features →  
It must be **generalized further or removed**.

---

## 🕰️ Version History

| Version | Date       | Author                                   | Summary |
|--------:|------------|------------------------------------------|---------|
| v11.0.0 | 2025-11-17 | Geophysics WG · Archaeology WG · FAIR+CARE Council | Initial magnetometry results registry under MDP v11. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Magnetometry Geophysics Results · CARE-Governed · FAIR+CARE Certified  
MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Geophysics Results](../README.md)

</div>
