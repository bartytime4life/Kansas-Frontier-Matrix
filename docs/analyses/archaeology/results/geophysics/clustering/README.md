---
title: "🧲🧩 Kansas Frontier Matrix — Geophysics Results: Clustering Analyses (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/geophysics/clustering/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly · Geophysics WG · Archaeology WG · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/archaeology-geophysics-clustering-v1.json"
governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Geophysics Result"
intent: "archaeology-geophysics-clustering-results"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed / Sensitive-Surface Geophysics"
sensitivity_level: "High"
public_exposure_risk: "Medium"
indigenous_rights_flag: true
data_steward: "Geophysics WG · Archaeology WG · FAIR+CARE Council"
risk_category: "Subsurface Interpretation (Generalized)"
redaction_required: true
provenance_chain:
  - "docs/analyses/archaeology/results/geophysics/clustering/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E26 Physical Feature"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"
  owl_time: "TemporalEntity"
json_schema_ref: "../../../../../schemas/json/archaeology-geophysics-clustering-results.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/archaeology-geophysics-clustering-results-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:geophysics:clustering-results-v11.0.0"
semantic_document_id: "kfm-arch-geophysics-clustering-results"
event_source_id: "ledger:docs/analyses/archaeology/results/geophysics/clustering/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Restricted"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
ai_transform_prohibited:
  - "feature-level interpretation"
  - "burial-inference"
  - "sacred-site-detection"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Internal / CARE-Governed"
role: "archaeology-geophysics-clustering-root"
lifecycle_stage: "stable"
ttl_policy: "Review every 6 months"
sunset_policy: "Superseded on next clustering-model update"
---

<div align="center">

# 🧲🧩 **Geophysics Results — Clustering Analyses**  
`docs/analyses/archaeology/results/geophysics/clustering/README.md`

**Purpose:**  
Define and document all **generalized clustering analyses** derived from geophysical survey data (magnetometry, GPR, resistivity, EM) within the Kansas Frontier Matrix (KFM).  
These outputs identify **broad, environmentally grounded anomaly clusters**, supporting contextual archaeological analysis **without revealing sensitive subsurface features**.

</div>

---

## 📘 Overview

Geophysical clustering analyses in KFM:

- identify **generalized anomaly groupings**  
- support **environmental + geomorphic contextualization**  
- map **H3 r7+ clustered anomaly envelopes**  
- integrate across **magnetometry, GPR, EM, resistivity**  
- combine signals into **proxy-weighted cluster surfaces**  
- include **uncertainty + explainability layers**  
- maintain strict **CARE-governed redaction** for sensitive subsurface features  

These clusters represent **patterns**, not specific features.  
They do *not* identify buildings, burials, structures, ceremonial spaces, or cultural features.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/results/geophysics/clustering/
├── README.md                                   # This file
├── magnetometry/                               # Magnetometry-based anomaly cluster envelopes
├── gpr/                                        # GPR slice-stack clustering (generalized)
├── resistivity/                                # Resistivity anomaly-cluster generalizations
├── electromagnetic/                             # EM induction cluster surfaces
├── composite/                                   # Multi-sensor cluster integration
├── environmental-links/                         # Hydrology/soil/terrain correlations
├── temporal/                                    # OWL-Time aligned anomaly-cluster tendencies
├── uncertainty/                                 # Uncertainty metrics & proxy disagreement
├── stac/                                        # STAC Items for clustering outputs
├── metadata/                                    # DCAT + JSON-LD metadata
└── provenance/                                  # PROV-O lineage & modeling documentation
~~~

---

## 🧩 Cluster Types

### **1️⃣ Magnetometry Clusters (`magnetometry/`)**
Contain:

- generalized magnetic anomaly envelopes  
- H3 hexagonal smoothing  
- high-level “zones of variation”  
- no feature-level identification  

---

### **2️⃣ Ground-Penetrating Radar Clusters (`gpr/`)**
Include:

- time-slice stack anomaly groupings  
- amplitude-variance regions  
- depth-binned cluster summaries  

All spatial data are fully generalized.

---

### **3️⃣ Resistivity Clusters (`resistivity/`)**
Represent:

- resistivity-gradient anomaly clusters  
- broad electrical-zone envelopes  
- moisture-linked variation blocks  

Never show specific features.

---

### **4️⃣ Electromagnetic Induction Clusters (`electromagnetic/`)**
Generalized clusters of:

- conductivity/susceptibility variation regions  
- environmental + soil-linked signals  

Fully redacted of sensitive detail.

---

### **5️⃣ Composite Multi-Sensor Clusters (`composite/`)**
Integrate:

- magnetometry  
- GPR  
- EM  
- resistivity  

Produce weighted, generalized “multi-sensor cluster fields.”

---

### **6️⃣ Environmental Correlations (`environmental-links/`)**
Summaries of cluster relationships with:

- hydrology  
- soils  
- terrain  
- vegetation  
- geomorphic stability  

Environmental-only, no cultural inference.

---

### **7️⃣ Temporal Clusters (`temporal/`)**
OWL-Time aligned anomaly cluster sequences for:

- environmental stability  
- moisture/signal-change patterns  
- geomorphic transitions  

No cultural chronology associated.

---

## ⚠️ Uncertainty Layers (`uncertainty/`)

Document:

- sensor disagreement  
- cluster-boundary variance  
- noise sensitivity  
- environmental signal variance  

Used as **Cluster Confidence Chips** in Focus Mode.

---

## 🧬 Metadata & Provenance

### **STAC (`stac/`)**
Each clustering dataset must include:

- generalized H3 geometry  
- uncertainty layers  
- environmental-driver metadata  
- multi-sensor linkage (if applicable)  
- CARE classification  
- PROV-O lineage reference  

### **DCAT (`metadata/`)**
Documents:

- dataset scope  
- access-level classification  
- FAIR+CARE compliance  
- distribution metadata  

### **PROV-O (`provenance/`)**
Must track:

- raw sensor datasets  
- processing steps (filtering, gridding, stacking)  
- H3 generalization  
- clustering algorithms (k-means, DBSCAN, hierarchical, etc.)  
- uncertainty propagation  
- WAL → Retry → Rollback lineage  

---

## 🧠 Focus Mode Integration

Geophysical clustering datasets provide:

- spatial context for Story Nodes  
- environmental signal summaries  
- safe, generalized subsurface interpretation  
- map-layer anomaly explanations  
- narrative-safe anomaly-block descriptions  

Example Focus Summary:

> **Focus Summary:**  
> Multi-sensor geophysical clustering identifies broad zones of subsurface signal variation, generalized through H3 masking and CARE governance to avoid feature-level interpretation.

---

## 🛡 CARE & Ethical Requirements

All geophysical-clustering outputs must:

- avoid interpreting or suggesting features (e.g., structures, burials)  
- employ H3 r7+ generalization  
- include uncertainty  
- undergo FAIR+CARE review  
- avoid sensitive subsurface inference  
- document all redaction  
- restrict narrative use to environmental-only context  

If a cluster is at risk of implying sensitive cultural information →  
it must be **further generalized or removed**.

---

## 🕰️ Version History

| Version | Date       | Author                                   | Summary |
|--------:|------------|------------------------------------------|---------|
| v11.0.0 | 2025-11-17 | Geophysics WG · Archaeology WG · FAIR+CARE Council | Initial geophysical clustering results registry under KFM-MDP v11. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Geophysical Clustering Results · CARE-Governed · FAIR+CARE Certified  
MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Geophysics Results](../README.md)

</div>
