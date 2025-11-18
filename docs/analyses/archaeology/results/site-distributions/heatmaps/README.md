---
title: "🔥📍 Kansas Frontier Matrix — Site Distribution Results: Generalized Heatmaps (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/site-distributions/heatmaps/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly · Archaeology WG · Spatial Modeling WG · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/archaeology-site-distributions-heatmaps-v1.json"
governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Spatial Result"
intent: "archaeology-site-distributions-heatmaps"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed / Spatial Heritage (Generalized Only)"
sensitivity_level: "High"
public_exposure_risk: "High"
indigenous_rights_flag: true
data_steward: "Archaeology WG · FAIR+CARE Council"
risk_category: "Spatial Sensitivity"
redaction_required: true
provenance_chain:
  - "docs/analyses/archaeology/results/site-distributions/heatmaps/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E31 Document"
  prov_o: "prov:Entity"
  schema_org: "Dataset"
  geosparql: "geo:FeatureCollection"
  owl_time: "TemporalEntity"
json_schema_ref: "../../../../../schemas/json/archaeology-site-distributions-heatmaps.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/archaeology-site-distributions-heatmaps-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:site-distributions:heatmaps-v11.0.0"
semantic_document_id: "kfm-arch-site-distributions-heatmaps"
event_source_id: "ledger:docs/analyses/archaeology/results/site-distributions/heatmaps/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Restricted / Generalized-Only"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "uncertainty-explanation"
ai_transform_prohibited:
  - "coordinate-reconstruction"
  - "cluster-centroid inference"
  - "site-level boundary deduction"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
classification: "Internal / Highly Sensitive / CARE-Governed"
jurisdiction: "Kansas / United States"
role: "archaeology-site-distributions-heatmaps-root"
lifecycle_stage: "stable"
ttl_policy: "Review every 6 months"
sunset_policy: "Updated when heatmap-generation rules change"
---

<div align="center">

# 🔥📍 **Site Distribution Results — Generalized Heatmaps**  
`docs/analyses/archaeology/results/site-distributions/heatmaps/README.md`

**Purpose:**  
Define, document, and govern the **generalized heatmap layers** derived from smoothed, redacted, culturally protected archaeological site-distribution datasets within the Kansas Frontier Matrix (KFM).  
These heatmaps show broad **spatial density tendencies** without revealing specific site locations.

</div>

---

## 📘 Overview

Heatmaps in KFM:

- visualize **generalized site-density patterns**
- apply **H3 r7+ masking** before rendering  
- smooth spatial tendencies using **KDE with sovereignty-safe bandwidths**  
- remove all fine-scale clusters or location signals  
- incorporate **environmental-only correlation layers**  
- propagate **uncertainty and disagreement metadata**  
- generate **Focus Mode spatial reasoning blocks**  
- avoid all cultural inference or historically specific mapping  

Heatmaps represent **broad, safe spatial envelopes**, not archaeological data points.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/results/site-distributions/heatmaps/
├── README.md                          # This file
├── h3/                                # H3 generalized heatmap envelopes
├── kde/                               # KDE smoothing heatmaps (sovereignty-safe)
├── environmental/                      # Environmental correlation heatmaps
├── uncertainty/                        # Heatmap variance + smoothing ambiguity
├── stac/                               # STAC Items for heatmap layers
├── metadata/                           # DCAT + JSON-LD metadata for heatmaps
└── provenance/                         # PROV-O lineage for heatmap creation
~~~

---

## 🔥 Heatmap Result Types

### **1️⃣ H3 Heatmaps (`h3/`)**
Contain:

- H3 r7+ density envelopes  
- coarse spatial distributions  
- redaction/masking logs  

No sub-H3 detail, ever.

---

### **2️⃣ KDE Heatmaps (`kde/`)**
Include:

- KDE smoothed density surfaces  
- controlled bandwidth parameters  
- envelope extraction (not raw KDE grids)  
- sovereignty-validated smoothing QA  

---

### **3️⃣ Environmental Heatmaps (`environmental/`)**
Model:

- environmental affinity distributions  
- soil/terrain/hydrology-linked density envelopes  
- generalized eco-spatial overlays  

Always environmental-only.

---

### **4️⃣ Uncertainty Heatmaps (`uncertainty/`)**
Track:

- smoothing variance  
- proxy disagreement  
- model fragility  
- “Heatmap Confidence Chips” used in Focus Mode  

---

## 🧬 Metadata & Provenance Requirements

### **STAC (`stac/`)**
Heatmap STAC records must include:

- H3 generalized geometry  
- uncertainty metadata  
- environmental drivers  
- lineage references  
- CARE classification  

### **DCAT (`metadata/`)**
Define:

- dataset scope  
- redaction requirement  
- generalization rules  
- license and FAIR+CARE fields  

### **PROV-O (`provenance/`)**
Track:

- masking & smoothing decisions  
- transformation steps  
- WAL → Retry → Rollback lineage  
- uncertainty lineage  

---

## 🧠 Focus Mode Integration

Heatmaps support:

- safe spatial tendency visualization  
- uncertainty chips  
- environmental overlays  
- Story Node map-context blocks  

**Example Focus Summary:**  
> Heatmaps display broad spatial density patterns extracted from generalized site data. All layers are sovereignty-safe, fully redacted, and provide environmental-only context.

---

## 🛡 CARE & Ethical Requirements

All heatmaps must:

- show only generalized spatial envelopes  
- avoid any direct or indirect site-location inference  
- include masking logs  
- disclose uncertainty  
- undergo FAIR+CARE review  
- avoid cultural/identity associations  

If analysis risks revealing sensitive spatial information → **generalize or remove**.

---

## 🕰️ Version History

| Version | Date       | Author                                   | Summary |
|--------:|------------|------------------------------------------|---------|
| v11.0.0 | 2025-11-17 | Archaeology WG · FAIR+CARE Council       | Initial generalized heatmap registry. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Generalized Site Distribution Heatmaps · FAIR+CARE · Sovereignty-Protected  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Site Distribution Results](../README.md)

</div>
