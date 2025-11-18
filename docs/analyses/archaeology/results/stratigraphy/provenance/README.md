---
title: "📜⛏️ Kansas Frontier Matrix — Stratigraphy Results: Provenance & Lineage (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/stratigraphy/provenance/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly · Stratigraphy WG · Metadata WG · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/archaeology-stratigraphy-provenance-v1.json"
governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Provenance Registry"
intent: "archaeology-stratigraphy-provenance"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed / Subsurface Lineage"
sensitivity_level: "High"
public_exposure_risk: "High"
indigenous_rights_flag: true
data_steward: "Stratigraphy WG · FAIR+CARE Council"
risk_category: "Subsurface Provenance"
redaction_required: true
provenance_chain:
  - "docs/analyses/archaeology/results/stratigraphy/provenance/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E7 Activity"
  schema_org: "Dataset"
  prov_o: "prov:Bundle"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"
json_schema_ref: "../../../../../schemas/json/archaeology-stratigraphy-provenance.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/archaeology-stratigraphy-provenance-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:stratigraphy:provenance-v11.0.0"
semantic_document_id: "kfm-arch-stratigraphy-provenance"
event_source_id: "ledger:docs/analyses/archaeology/results/stratigraphy/provenance/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Restricted / Lineage-Only"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "lineage-explanation"
ai_transform_prohibited:
  - "subsurface inference"
  - "cultural or temporal attribution"
  - "reverse horizon reconstruction"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
classification: "Internal / Highly Sensitive / CARE-Governed"
jurisdiction: "Kansas / United States"
role: "archaeology-stratigraphy-provenance-root"
lifecycle_stage: "stable"
ttl_policy: "Review every 6 months"
sunset_policy: "Updated whenever stratigraphy lineage framework changes"
---

<div align="center">

# 📜⛏️ **Stratigraphy Results — Provenance & Lineage**  
`docs/analyses/archaeology/results/stratigraphy/provenance/README.md`

**Purpose:**  
Define the **complete PROV-O lineage, masking records, transformation logs, and sovereignty-required generalization metadata** for stratigraphy-related outputs in the Kansas Frontier Matrix (KFM).  
This registry ensures all stratigraphic surfaces remain **environment-only**, fully **redacted**, and **SAFE** from any feature-level, cultural, or subsurface structural inference.

</div>

---

## 📘 Overview

Stratigraphic provenance documents:

- multi-proxy source inputs (PD-only, never precise coordinates)  
- depositional/geomorphic reconstruction chains  
- smoothing, interpolation, envelope-generation steps  
- H3 r7+ masking and stratigraphic redaction  
- uncertainty propagation and disagreement tracking  
- OWL-Time temporal alignment lineage  
- environmental drivers used (climate / hydrology / terrain / soils)  
- WAL → Retry → Rollback lineage for reproducibility  

This provenance **does not and must not** include:

- cultural strata  
- archaeological horizons  
- feature-level interpretation  
- fine-scale sediment geometry  
- any actionable or sensitive subsurface detail  

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/results/stratigraphy/provenance/
├── README.md                           # This file
├── proxy-sources/                      # PD-safe paleo/soil/geomorphic proxies
├── reconstruction/                     # Steps used to build stratigraphic surfaces
├── generalization/                     # H3 masking + redaction receipts
├── smoothing/                          # KDE / spline / interpolation lineage
├── temporal/                           # OWL-Time alignment lineage
├── uncertainty/                        # Proxy disagreement + model fragility
├── stac/                               # STAC provenance fields + crosswalks
├── metadata/                           # DCAT provenance enrichment
└── bundles/                            # Final PROV-O lineage bundles (JSON-LD)
~~~

---

## 🧩 Provenance Components

### **1️⃣ Proxy Source Provenance (`proxy-sources/`)**
Covers:

- paleoenvironment proxies (pollen, charcoal, sediment chemistry)  
- soils + pedogenic indicators  
- geomorphological inputs  
- hydrology/terrain environment signals  
- PD-safe generalization (no sensitive attributes)

---

### **2️⃣ Reconstruction Provenance (`reconstruction/`)**
Documents:

- depositional/geomorphic reconstruction approaches  
- interpolation + smoothing parameters  
- environmental modeling logic  
- stratigraphy-safe filter chains  
- masking triggers  

---

### **3️⃣ Generalization & Redaction (`generalization/`)**
Tracks:

- H3 r7+ masking operations  
- sovereignty constraints  
- geometry redaction logs  
- sensitive feature suppression  

---

### **4️⃣ Smoothing (`smoothing/`)**
Includes:

- KDE smoothing lineage  
- environmental envelope creation  
- spline/rolling-window steps  
- stratigraphic fragility indicators  

---

### **5️⃣ Temporal Provenance (`temporal/`)**
Defines:

- OWL-Time intervals  
- multi-period stratigraphic windows  
- smoothing across time slices  

---

### **6️⃣ Uncertainty Provenance (`uncertainty/`)**
Captures:

- variance surfaces  
- proxy disagreement  
- model fragility  
- “Stratigraphy Confidence Chips” logic  
- ensemble spread lineage  

---

### **7️⃣ STAC Provenance (`stac/`)**
Includes:

- STAC → PROV links  
- lineage metadata blocks  
- dataset relation chains  

---

### **8️⃣ Metadata Provenance (`metadata/`)**
Documents:

- FAIR+CARE fields  
- dataset-level governance descriptors  
- redaction metadata  
- distribution info  

---

### **9️⃣ PROV-O Bundles (`bundles/`)**
Final, machine-readable provenance exports:

- prov:Activity / prov:Entity / prov:Agent  
- masking justification  
- environmental drivers  
- WAL lineage  
- uncertainty documents  

---

## 🧠 Focus Mode Integration

Provenance is used to generate:

- lineage chips  
- uncertainty chips  
- sovereignty badges  
- safe contextualization of stratigraphic envelopes  

**Example Focus Summary:**  
> Stratigraphy provenance explains how environmental-only stratigraphic surfaces were built—generalized, redacted, and uncertainty-weighted—without exposing sensitive subsurface information.

---

## 🛡 CARE & Ethical Requirements

All stratigraphy provenance must:

- avoid disclosing sensitive stratigraphy  
- log generalization + masking steps  
- include CARE classification  
- prohibit any cultural or archaeological linkage  
- meet sovereignty standards  
- fully disclose uncertainty  
- pass FAIR+CARE Council review  

If provenance reveals unacceptable detail → **block dataset.**

---

## 🕰️ Version History

| Version | Date       | Author                                   | Summary |
|--------:|------------|------------------------------------------|---------|
| v11.0.0 | 2025-11-17 | Stratigraphy WG · FAIR+CARE Council      | Initial stratigraphy provenance registry under MDP v11. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Stratigraphy Provenance Registry · FAIR+CARE Certified · Sovereignty-Safe  
Diamond⁹ Ω · Crown∞Ω Ultimate Certified  

[Back to Stratigraphy Results](../README.md)

</div>
