---
title: "⚡🧲 Kansas Frontier Matrix — Geophysics Results: Electrical Resistivity Analyses (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/geophysics/resistivity/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly · Geophysics WG · Archaeology WG · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/archaeology-geophysics-resistivity-v1.json"
governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Geophysics Result"
intent: "archaeology-geophysics-resistivity-results"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed / Sensitive-Surface Geophysics"
sensitivity_level: "High"
public_exposure_risk: "Medium"
indigenous_rights_flag: true
data_steward: "Geophysics WG · Archaeology WG · FAIR+CARE Council"
risk_category: "Subsurface Interpretation (Generalized Resistivity)"
redaction_required: true
provenance_chain:
  - "docs/analyses/archaeology/results/geophysics/resistivity/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E26 Physical Feature"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"
  owl_time: "TemporalEntity"
json_schema_ref: "../../../../../schemas/json/archaeology-geophysics-resistivity-results.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/archaeology-geophysics-resistivity-results-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:geophysics:resistivity-results-v11.0.0"
semantic_document_id: "kfm-arch-geophysics-resistivity-results"
event_source_id: "ledger:docs/analyses/archaeology/results/geophysics/resistivity/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Restricted"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
ai_transform_prohibited:
  - "feature-level inference"
  - "identity-of-subsurface-objects"
  - "burial-or-structure-detection"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Internal / CARE-Governed"
role: "archaeology-geophysics-resistivity-root"
lifecycle_stage: "stable"
ttl_policy: "Review every 6 months"
sunset_policy: "Superseded on next resistivity-results update"
---

<div align="center">

# ⚡🧲 **Geophysics Results — Electrical Resistivity**  
`docs/analyses/archaeology/results/geophysics/resistivity/README.md`

**Purpose:**  
Define and document all **generalized, sovereignty-protected resistivity results** within the Kansas Frontier Matrix (KFM).  
Resistivity outputs model **broad electrical conductivity variation** across the landscape, not feature shapes or subsurface structures, and are fully compliant with **FAIR+CARE cultural safety** requirements.

</div>

---

## 📘 Overview

Electrical resistivity analyses in KFM:

- characterize **environment-driven subsurface conductivity patterns**  
- integrate soil moisture, sediment type, hydrology, terrain, and environmental factors  
- generate **H3 r7+ generalized electrical envelopes**  
- provide multi-depth resistivity summaries  
- produce uncertainty layers: noise, disagreement, drift  
- avoid any feature-level interpretation  

Resistivity datasets are strictly:

- **environmental-only**  
- **generalized**  
- **culturally neutral**  
- **sovereignty-reviewed**  

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/results/geophysics/resistivity/
├── README.md                                   # This file
├── conductivity/                               # Broad-zone electrical variation surfaces
├── gradients/                                  # Resistivity-gradient envelopes (generalized)
├── depth-bands/                                # Shallow/mid/deep variation summaries
├── composite/                                  # Multi-sensor integrated resistivity models
├── environmental-links/                        # Hydrology/soil/terrain relationships
├── temporal/                                    # OWL-Time aligned resistivity tendencies
├── uncertainty/                                 # Noise, drift, disagreement layers
├── stac/                                        # STAC Items for resistivity outputs
├── metadata/                                    # DCAT + JSON-LD metadata
└── provenance/                                  # PROV-O lineage & processing logs
~~~

---

## ⚡ Resistivity Result Types

### **1️⃣ Conductivity Surfaces (`conductivity/`)**
Document environmental-only conductivity:

- broad conductivity envelopes  
- moisture-linked variability  
- sediment/soil patterning  

Never feature-level interpretations.

---

### **2️⃣ Resistivity Gradients (`gradients/`)**
Contain:

- slope/derivative electrical-change surfaces  
- generalized envelope shapes  
- H3 generalized variation zones  

---

### **3️⃣ Depth-Band Resistivity Patterns (`depth-bands/`)**
Summaries of:

- shallow response  
- mid-depth coherence  
- deeper electrical variability  

No subsurface object identification.

---

### **4️⃣ Composite Multi-Sensor Models (`composite/`)**
Integrate:

- resistivity  
- magnetometry  
- EMI  
- GPR  

Outputs: **environmental conductivity tendency surfaces**, not cultural features.

---

### **5️⃣ Environmental Correlation Layers (`environmental-links/`)**
Relationships with:

- hydrology  
- pedology  
- terrain  
- vegetation  
- geomorphology  

Environmental-only reasoning.

---

### **6️⃣ Temporal Resistivity Trends (`temporal/`)**
OWL-Time aligned summaries of:

- soil moisture change  
- hydrology fluctuation  
- environmental conductivity shifts  

Not linked to cultural chronology.

---

## ⚠️ Uncertainty Layers (`uncertainty/`)

Include:

- instrument noise  
- drift variance  
- environmental disagreement  
- smoothing variance  
- multi-depth sensitivity  

Displayed in Focus Mode as **Resistivity Confidence Chips**.

---

## 🧬 Metadata & Provenance Rules

### **STAC (`stac/`)**
Resistivity STAC Items must include:

- H3-masked geometry  
- environmental driver metadata  
- uncertainty layers  
- CARE classification  
- PROV-O lineage references  

### **DCAT (`metadata/`)**
Defines:

- dataset purpose  
- environmental framing  
- FAIR+CARE metadata  
- access-level rules  

### **PROV-O (`provenance/`)**
Tracks:

- dataset sources  
- filtering, stacking, inversion steps  
- H3 generalization  
- sovereignty-based masking  
- uncertainty propagation  
- WAL → Retry → Rollback lineage  

---

## 🧠 Focus Mode Integration

Resistivity layers support:

- environmental subsurface narrative context  
- safe anomaly explanation overlays  
- cross-sensor syntheses  
- Story Node v3 spatial-temporal environmental panels  

Example Focus Summary:

> **Focus Summary:**  
> Resistivity modeling reveals broad conductivity variation across Kansas landscapes. All data are generalized, non-feature-specific, and fully governed under FAIR+CARE to ensure cultural and subsurface sovereignty.

---

## 🛡 CARE & Ethical Requirements

All resistivity datasets must:

- avoid any structure/burial inference  
- apply H3 r7+ spatial generalization  
- document masking steps  
- include uncertainty metadata  
- avoid revealing sensitive subsurface shapes  
- follow FAIR+CARE Council review  

If ANY dataset risks sensitive misinterpretation → **it must be generalized further or removed.**

---

## 🕰️ Version History

| Version | Date       | Author                                   | Summary |
|--------:|------------|------------------------------------------|---------|
| v11.0.0 | 2025-11-17 | Geophysics WG · Archaeology WG · FAIR+CARE Council | Initial resistivity results registry under KFM-MDP v11. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Resistivity Geophysics Results · CARE-Governed · FAIR+CARE Certified  
MCP-DL v6.3 · Diamond⁹ Ω · Crown∞Ω Ultimate Certified  

[Back to Geophysics Results](../README.md)

</div>
