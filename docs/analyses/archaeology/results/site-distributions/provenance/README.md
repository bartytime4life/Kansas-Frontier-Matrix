---
title: "📜📍 Kansas Frontier Matrix — Site Distribution Results: Provenance & Lineage (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/site-distributions/provenance/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly · Archaeology WG · Metadata WG · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/archaeology-site-distributions-provenance-v1.json"
governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Provenance Registry"
intent: "archaeology-site-distributions-provenance"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed / Spatial Heritage Data"
sensitivity_level: "High"
public_exposure_risk: "High"
indigenous_rights_flag: true
data_steward: "Archaeology WG · FAIR+CARE Council"
risk_category: "Spatial Heritage Provenance"
redaction_required: true
provenance_chain:
  - "docs/analyses/archaeology/results/site-distributions/provenance/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E7 Activity"
  schema_org: "Dataset"
  prov_o: "prov:Bundle"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"
json_schema_ref: "../../../../../schemas/json/archaeology-site-distributions-provenance.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/archaeology-site-distributions-provenance-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:site-distributions:provenance-v11.0.0"
semantic_document_id: "kfm-arch-site-distributions-provenance"
event_source_id: "ledger:docs/analyses/archaeology/results/site-distributions/provenance/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Restricted / Safe-Generalized"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "uncertainty-explanation"
ai_transform_prohibited:
  - "coordinate-reconstruction"
  - "sensitive-site-inference"
  - "historical or cultural attribution"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
classification: "Internal / Highly Sensitive / CARE-Governed"
jurisdiction: "Kansas / United States"
role: "archaeology-site-distributions-provenance-root"
lifecycle_stage: "stable"
ttl_policy: "Review every 6 months"
sunset_policy: "Updated when distribution-derivation rules change"
---

<div align="center">

# 📜📍 **Site Distribution Results — Provenance & Lineage**  
`docs/analyses/archaeology/results/site-distributions/provenance/README.md`

**Purpose:**  
Define the full **PROV-O lineage**, masking logic, generalization workflow, and sovereignty safeguards for **site distribution results** within the Kansas Frontier Matrix (KFM).  
This registry ensures **complete transparency** while preventing any form of **sensitive location exposure**.

</div>

---

## 📘 Overview

This provenance registry documents how spatial heritage datasets were transformed into **generalized site-distribution layers**:

- H3 r7+ spatial masking  
- KDE smoothing & envelope creation  
- multi-proxy environmental correlation  
- uncertainty propagation  
- redaction of sensitive coordinates  
- CARE-based cultural safety review  
- lineage audits: WAL → Retry → Rollback  

These provenance files ensure every site-distribution layer is:

- sovereignty-protected  
- culturally safe  
- spatially generalized  
- reproducible  
- properly uncertainty-weighted  

No notebook or dataset may exit the pipeline without corresponding provenance entries.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/results/site-distributions/provenance/
├── README.md                                # This file
├── raw-sources/                             # Source datasets (paths only, never coordinates)
├── masking/                                 # H3 generalization & redaction receipts
├── smoothing/                               # KDE + envelope smoothing steps
├── environmental-links/                     # Hydrology/soil/terrain predictor lineage
├── temporal/                                # OWL-Time alignment lineage (if applicable)
├── uncertainty/                             # Variance, disagreement, confidence metrics
├── stac/                                    # STAC ↔ PROV linkage entries
├── metadata/                                # DCAT provenance enrichments
└── bundles/                                 # Final PROV-O JSON-LD lineage bundles
~~~

---

## 🧩 Provenance Components

### **1️⃣ Raw Source Provenance (`raw-sources/`)**
Documents (generalized, non-sensitive):

- dataset names  
- version identifiers  
- licensing & PD status  
- access class  
- data stewards  

Never includes coordinates, shapefiles, or site points.

---

### **2️⃣ Masking & Generalization (`masking/`)**
Tracks:

- H3 r7+ grid transforms  
- coordinate obfuscation steps  
- sovereignty-driven redactions  
- masking parameters  
- quality checks  

---

### **3️⃣ Smoothing Lineage (`smoothing/`)**
Includes:

- KDE parameters  
- envelope generalization  
- bandwidth constraints  
- artifact-free smoothing logic  
- sovereignty safety notes  

---

### **4️⃣ Environmental Correlation Lineage (`environmental-links/`)**
Captures:

- hydrology proximity modeling  
- terrain & slope relationships  
- soils/vegetation correlations  
- environmental-only rationale  

Never cultural inference.

---

### **5️⃣ Temporal Lineage (`temporal/`)**
Contains:

- OWL-Time layer alignment  
- multi-period generalization  
- temporal smoothing metadata  

---

### **6️⃣ Uncertainty Lineage (`uncertainty/`)**
Tracks:

- disagreement between predictors  
- variance surfaces  
- confidence envelopes  
- smoothing fragility  

Used by Focus Mode for “Distribution Confidence Chips.”

---

### **7️⃣ STAC Provenance (`stac/`)**
Stores:

- STAC → PROV-O pointers  
- asset-level lineage  
- crosswalk entries  

---

### **8️⃣ Metadata Provenance (`metadata/`)**
Includes:

- DCAT-provenance enrichment  
- dataset-level FAIR+CARE fields  
- distribution metadata  

---

### **9️⃣ PROV-O Bundles (`bundles/`)**
Final output:

- entities, activities, agents  
- lineage chain graph  
- masking receipts  
- redaction attestations  
- WAL → Retry → Rollback entries  

---

## 🧠 Focus Mode Integration

Provenance feeds:

- dataset transparency panels  
- sovereignty alerts  
- uncertainty badges  
- narrative-safe site-distribution context  

**Example Focus Summary:**  
> Site-distribution lineage documents how sensitive information was masked, generalized, and validated to produce sovereignty-safe spatial summaries.

---

## 🛡 CARE & Ethical Safeguards

All provenance must:

- avoid sensitive coordinate disclosure  
- document generalization rigorously  
- include CARE metadata  
- avoid cultural interpretation  
- disclose uncertainty & masking pathways  
- undergo sovereignty review  

If provenance reveals risk → data is **blocked** until corrected.

---

## 🕰️ Version History

| Version | Date       | Author                                   | Summary |
|--------:|------------|------------------------------------------|---------|
| v11.0.0 | 2025-11-17 | Archaeology WG · FAIR+CARE Council       | Initial site-distribution provenance registry. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Site Distribution Provenance · FAIR+CARE Certified · Sovereignty-Safe  
Diamond⁹ Ω · Crown∞Ω Ultimate Certified  

[Back to Site Distribution Results](../README.md)

</div>
