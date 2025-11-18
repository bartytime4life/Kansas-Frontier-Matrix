---
title: "📡📶 Kansas Frontier Matrix — Geophysics Results: Ground-Penetrating Radar (GPR) Analyses (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/geophysics/gpr/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly · Geophysics WG · Archaeology WG · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/archaeology-geophysics-gpr-v1.json"
governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Geophysics Result"
intent: "archaeology-geophysics-gpr-results"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed / Sensitive-Surface Geophysics"
sensitivity_level: "High"
public_exposure_risk: "Medium"
indigenous_rights_flag: true
data_steward: "Geophysics WG · Archaeology WG · FAIR+CARE Council"
risk_category: "Subsurface Interpretation (Generalized GPR)"
redaction_required: true
provenance_chain:
  - "docs/analyses/archaeology/results/geophysics/gpr/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E26 Physical Feature"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"
  owl_time: "TemporalEntity"
json_schema_ref: "../../../../../schemas/json/archaeology-geophysics-gpr-results.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/archaeology-geophysics-gpr-results-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:geophysics:gpr-results-v11.0.0"
semantic_document_id: "kfm-arch-geophysics-gpr-results"
event_source_id: "ledger:docs/analyses/archaeology/results/geophysics/gpr/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Restricted"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
ai_transform_prohibited:
  - "feature-level inference"
  - "burial-or-structure-detection"
  - "restricted-subsurface-interpretation"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Internal / CARE-Governed"
role: "archaeology-geophysics-gpr-root"
lifecycle_stage: "stable"
ttl_policy: "Review every 6 months"
sunset_policy: "Superseded on next GPR-results update"
---

<div align="center">

# 📡📶 **Geophysics Results — Ground-Penetrating Radar (GPR)**  
`docs/analyses/archaeology/results/geophysics/gpr/README.md`

**Purpose:**  
Document **generalized, culturally safe, sovereignty-aligned GPR results** for use in archaeological analysis within the Kansas Frontier Matrix (KFM).  
GPR outputs describe **broad, non-specific subsurface signal tendencies**—NEVER feature interpretations, burial/structure identification, or culturally sensitive inference.

</div>

---

## 📘 Overview

GPR (Ground-Penetrating Radar) analyses in KFM:

- summarize **generalized subsurface reflection patterns**
- provide **slice-stack amplitude regions, not features**
- describe **broad anomaly-density envelopes (H3 r7+)**
- integrate **environmental/geomorphic influences**
- include **uncertainty layers + proxy disagreement summaries**
- combine with EMI / magnetometry / resistivity for safe multi-sensor interpretation
- follow **FAIR+CARE cultural protection rules**

Strictly prohibited:

- Inference of graves, structures, pits, houses, enclosures  
- Identification of ceremonial/sacred features  
- Interpretations implying cultural occupation or activity at specific locations  

All spatial outputs are **fully generalized**.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/results/geophysics/gpr/
├── README.md                                   # This file
├── slices/                                     # Time-slice amplitude summaries (generalized)
├── envelopes/                                  # H3 anomaly-density envelopes
├── composite/                                  # Multi-slice GPR composite layers
├── depth-bands/                                # Depth-binned generalized pattern summaries
├── environmental-links/                        # Correlations with soils/hydrology/terrain
├── temporal/                                   # OWL-Time aligned GPR signal tendencies
├── uncertainty/                                # Noise metrics, coherence scores, variance maps
├── stac/                                       # STAC Items for GPR result datasets
├── metadata/                                   # DCAT + JSON-LD metadata
└── provenance/                                 # PROV-O lineage for GPR processing
~~~

---

## 📶 GPR Result Types

### **1️⃣ Time-Slice Summaries (`slices/`)**
Contain:

- amplitude-range envelopes  
- slice-stack max/min/mean surfaces  
- generalized “zones of radar variation”  

No structural or feature interpretation.

---

### **2️⃣ Envelope Surfaces (`envelopes/`)**
H3 r7+ generalized representations of:

- amplitude concentration zones  
- broad anomaly density blocks  
- non-specific subsurface variation patterns  

---

### **3️⃣ Composite GPR Models (`composite/`)**
Include:

- multi-slice density aggregations  
- PCA/composite amplitude summaries  
- standardized environmental masking  

Used to detect *environmental* radar responses, not archaeological features.

---

### **4️⃣ Depth-Band Patterns (`depth-bands/`)**
Summaries of:

- shallow/mid/deep reflection coherence  
- depth-dependent signal tendencies  
- hydrology/soil-linked radar behavior  

Generalized across grid.

---

### **5️⃣ Environmental Links (`environmental-links/`)**
Correlations with:

- hydrology  
- soil conductivity  
- terrain/geomorphology  
- vegetation/biomass  

Environmental only—zero cultural inference.

---

### **6️⃣ Temporal GPR Patterns (`temporal/`)**
OWL-Time aligned summaries capturing:

- long-term soil moisture changes  
- environmental radar-signal shifts  
- multi-period environmental envelopes  

No cultural chronology or occupation inference.

---

## ⚠️ Uncertainty Layers (`uncertainty/`)

Include:

- noise floors  
- coherence metrics  
- motion-artifact probability  
- slice-stack disagreement  
- environmental disagreement surfaces  

Displayed in Focus Mode as **GPR Confidence Chips**.

---

## 🧬 Metadata & Provenance Requirements

### **STAC (`stac/`)**
Each GPR dataset must include:

- H3 masked geometry  
- slice metadata (depth, window, amplitude range)  
- environmental drivers  
- uncertainty layers  
- CARE classification  
- PROV-O lineage references  

### **DCAT (`metadata/`)**
Defines:

- dataset description  
- PD-verification (if any)  
- access & governance metadata  
- FAIR+CARE compliance  

### **PROV-O (`provenance/`)**
Tracks:

- raw radar files used  
- slice extraction  
- filtering (dewow, migration, stacking)  
- amplitude normalization  
- masking/generalization  
- WAL → Retry → Rollback lineage  
- uncertainty propagation  

---

## 🧠 Focus Mode Integration

GPR results fuel:

- environmental radar-response context panels  
- multi-sensor explanation blocks  
- narrative-safe interpretations of variation zones  
- Story Node contextual overlays  

Example Focus Summary:

> **Focus Summary:**  
> Generalized GPR amplitudes reveal broad zones of subsurface signal variation related to soils and hydrology. All outputs are spatially masked, feature-safe, and reviewed under FAIR+CARE sovereignty protections.

---

## 🛡 CARE & Ethical Requirements

GPR datasets must:

- avoid ANY feature-level interpretation  
- use H3 r7+ generalization  
- include uncertainty metrics  
- avoid implying graves/structures/pits  
- undergo sovereignty & FAIR+CARE review  
- track all redaction & masking steps  

If any layer risks cultural harm → it must be **generalized further or removed**.

---

## 🕰️ Version History

| Version | Date       | Author                                    | Summary |
|--------:|------------|-------------------------------------------|---------|
| v11.0.0 | 2025-11-17 | Geophysics WG · Archaeology WG · FAIR+CARE Council | Initial GPR results registry under MDP v11. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
GPR Geophysics Results · CARE-Governed · FAIR+CARE Certified  
MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Geophysics Results](../README.md)

</div>
