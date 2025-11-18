---
title: "📜🧲 Kansas Frontier Matrix — Geophysics Results: Provenance Registry (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/geophysics/provenance/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly · Geophysics WG · Archaeology WG · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/archaeology-geophysics-provenance-v1.json"
governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Provenance Registry"
intent: "archaeology-geophysics-results-provenance"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed / Sensitive Subsurface Provenance"
sensitivity_level: "High"
public_exposure_risk: "Medium"
indigenous_rights_flag: true
data_steward: "Geophysics WG · FAIR+CARE Council"
risk_category: "Generalized Subsurface Provenance"
redaction_required: true
provenance_chain:
  - "docs/analyses/archaeology/results/geophysics/provenance/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E7 Activity"
  schema_org: "Dataset"
  prov_o: "prov:Bundle"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"
json_schema_ref: "../../../../../schemas/json/archaeology-geophysics-provenance.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/archaeology-geophysics-provenance-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:geophysics:provenance-v11.0.0"
semantic_document_id: "kfm-arch-geophysics-provenance"
event_source_id: "ledger:docs/analyses/archaeology/results/geophysics/provenance/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Restricted"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
ai_transform_prohibited:
  - "feature-inference"
  - "burial-or-structure-implied-lineage"
  - "reverse-subsurface-reconstruction"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Internal / CARE-Governed"
role: "archaeology-geophysics-provenance-root"
lifecycle_stage: "stable"
ttl_policy: "Review every 6 months"
sunset_policy: "Superseded when v11.x geophysical provenance model is updated"
---

<div align="center">

# 📜🧲 **Geophysics Results — Provenance Registry**  
`docs/analyses/archaeology/results/geophysics/provenance/README.md`

**Purpose:**  
Provide the **full PROV-O lineage framework** for all generalized geophysical results—magnetometry, GPR, resistivity, EMI, and multi-sensor composites—within the Kansas Frontier Matrix (KFM).  
Ensures **traceability**, **ethical safeguards**, **data sovereignty**, and **FAIR+CARE–aligned transparency**, while preventing any reconstruction of sensitive subsurface features.

</div>

---

## 📘 Overview

Geophysical provenance documents:

- raw sensor inputs (no coordinates published)  
- drift correction & instrument normalization  
- filtering, stacking, migration, cleaning workflows  
- H3 r7+ spatial generalization steps  
- uncertainty propagation pathways  
- multi-sensor fusion lineage  
- environmental driver integration  
- masking/redaction history  
- WAL → Retry → Rollback operational lineage  
- model reproducibility metadata (if predictive)  

All provenance records must avoid:

- feature identification  
- burial inference  
- reconstruction of structures or pits  
- sensitive subsurface pattern disclosure  

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/results/geophysics/provenance/
├── README.md                                   # This file
├── magnetometry/                               # Magnetic-field processing lineage
│   ├── drift-correction/
│   ├── filtering/
│   ├── gridding/
│   └── generalization/
├── gpr/                                        # GPR slice-stack & depth-band lineage
│   ├── filtering/
│   ├── migration/
│   ├── compositing/
│   └── masking/
├── resistivity/                                 # Electrical resistivity provenance bundles
│   ├── acquisition/
│   ├── processing/
│   └── generalization/
├── electromagnetic/                             # EMI multi-frequency lineage
│   ├── drift/
│   ├── calibration/
│   └── frequency-composites/
├── composite/                                   # Multi-sensor integration & harmonized lineage
│   ├── sensor-fusion/
│   ├── environmental-drivers/
│   └── uncertainty/
├── uncertainty/                                 # Cross-method uncertainty propagation
├── stac/                                        # STAC ↔ PROV crosswalk bundles
├── metadata/                                    # DCAT ↔ PROV harmonization
└── lineage-bundles/                             # Final PROV-O JSON-LD bundles
    ├── magnetometry-prov.jsonld
    ├── gpr-prov.jsonld
    ├── resistivity-prov.jsonld
    ├── emi-prov.jsonld
    └── composite-prov.jsonld
~~~

---

## 🧬 Required Provenance Elements

### **1️⃣ PROV-O Core**
Each dataset must define:

- `prov:Entity` — derived geophysical layer  
- `prov:Activity` — all transformations  
- `prov:Agent` — system/pipeline roles  

### **2️⃣ Input Dataset Documentation**
Includes:

- raw sensor files (mag, GPR, EMI, resistivity)  
- acquisition logs (but **never** shown publicly)  
- environmental layers used for safe modeling  

### **3️⃣ Transformation Tracking**
Tracks:

- filtering (dewow, bandpass, median)  
- drift correction  
- amplitude/phase normalization  
- depth-slicing or frequency-compositing  
- interpolation/gridding  
- H3 r7+ generalization  
- masking & sovereignty-based redaction  

### **4️⃣ Multi-Sensor Integration**
For composite products:

- cross-sensor alignment  
- covariance/weighting  
- harmonized uncertainty fields  

### **5️⃣ Uncertainty Propagation**
Documents:

- sensor disagreement  
- noise floor contributions  
- drift-variance  
- environmental-model uncertainty  

### **6️⃣ CARE Governance**
Logs:

- sensitivity level  
- redaction justification  
- generalization method and H3 resolution  
- sovereignty constraints invoked  

### **7️⃣ WAL → Retry → Rollback Lineage**
Every step maintains:

- WAL checkpoints  
- retry history  
- rollback snapshots  
- validation timestamps  

---

## 🧠 Focus Mode Integration

Provenance supports:

- environmental-only explanations  
- uncertainty chips  
- dataset traceability badges  
- safe narrative mode during Story Node rendering  

Example Focus Summary:

> **Focus Summary:**  
> Provenance confirms that this geophysical layer derives from generalized, sovereignty-protected processing steps with full FAIR+CARE governance. No feature-level interpretations are possible.

---

## 🛡 CARE & Ethical Safeguards

All provenance must:

- prevent reconstruction of sensitive subsurface features  
- disclose masking & generalization steps  
- adhere to sovereignty & cultural-safety requirements  
- retain environmental-only framing  
- record all redactions explicitly  

If provenance risks enabling sensitive inference → **reject the dataset**.

---

## 🕰️ Version History

| Version | Date       | Author                                   | Summary |
|--------:|------------|------------------------------------------|---------|
| v11.0.0 | 2025-11-17 | Geophysics WG · Archaeology WG · FAIR+CARE Council | Initial geophysics provenance registry under MDP v11.0.0. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Geophysics Provenance Registry · CARE-Governed · FAIR+CARE Certified  
MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Geophysics Results](../README.md)

</div>
