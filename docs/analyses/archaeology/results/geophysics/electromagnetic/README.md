---
title: "📡🧲 Kansas Frontier Matrix — Geophysics Results: Electromagnetic Induction (EMI) Analyses (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/geophysics/electromagnetic/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly · Geophysics WG · Archaeology WG · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/archaeology-geophysics-electromagnetic-v1.json"
governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Geophysics Result"
intent: "archaeology-geophysics-electromagnetic-results"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed / Sensitive-Surface Geophysics"
sensitivity_level: "High"
public_exposure_risk: "Medium"
indigenous_rights_flag: true
data_steward: "Geophysics WG · Archaeology WG · FAIR+CARE Council"
risk_category: "Subsurface Interpretation (Generalized, EMI)"
redaction_required: true
provenance_chain:
  - "docs/analyses/archaeology/results/geophysics/electromagnetic/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E26 Physical Feature"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"
  owl_time: "TemporalEntity"
json_schema_ref: "../../../../../schemas/json/archaeology-geophysics-electromagnetic-results.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/archaeology-geophysics-electromagnetic-results-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:geophysics:electromagnetic-results-v11.0.0"
semantic_document_id: "kfm-arch-geophysics-electromagnetic-results"
event_source_id: "ledger:docs/analyses/archaeology/results/geophysics/electromagnetic/README.md"
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
role: "archaeology-geophysics-electromagnetic-root"
lifecycle_stage: "stable"
ttl_policy: "Review every 6 months"
sunset_policy: "Superseded on next EMI-results update"
---

<div align="center">

# 📡🧲 **Geophysics Results — Electromagnetic Induction (EMI)**  
`docs/analyses/archaeology/results/geophysics/electromagnetic/README.md`

**Purpose:**  
Document all **FAIR+CARE–governed**, generalized **electromagnetic induction (EMI)** geophysical results used in the Kansas Frontier Matrix (KFM). EMI outputs provide **environmentally grounded conductivity/susceptibility insights**, fully generalized for sovereignty protection—**never revealing feature-level subsurface detail**.

</div>

---

## 📘 Overview

Electromagnetic Induction (EMI) datasets in KFM provide:

- broad conductivity / magnetic susceptibility variation zones  
- environmental correlation surfaces (hydrology, soils, terrain)  
- multi-depth or multi-frequency response summaries  
- generalized H3 r7+ cluster envelopes  
- multi-sensor integration with magnetometry, resistivity, and GPR  
- uncertainty and noise-sensitivity layers  
- provenance-validated transformations and filtering  

EMI is used for **environmental inference only**, *not* archaeological feature identification.

KFM explicitly prohibits:

- feature-level interpretation  
- burial or structure inference  
- culturally sensitive subsurface speculation  
- exact anomaly-shape reconstruction  

All EMI results undergo FAIR+CARE Council review.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/results/geophysics/electromagnetic/
├── README.md                                   # This file
├── frequency-bands/                            # Multi-frequency EMI responses (generalized)
├── conductivity/                               # Conductivity envelope surfaces
├── susceptibility/                             # Magnetic susceptibility clusters
├── composite/                                   # Combined EMI + other sensors (safe generalizations)
├── environmental-links/                         # Hydrology/soil/terrain/environment relationships
├── temporal/                                    # OWL-Time aligned EMI environmental patterns
├── uncertainty/                                 # Sensor noise, phase interference, confidence metrics
├── stac/                                        # STAC Items for EMI result layers
├── metadata/                                    # DCAT + JSON-LD EMI metadata
└── provenance/                                  # PROV-O lineage logs for all transformations
~~~

---

## 🧲 EMI Result Types

### **1️⃣ Multi-Frequency EMI Responses (`frequency-bands/`)**
Provides:

- generalized low/mid/high frequency response envelopes  
- spatially aggregated conductivity shifts  
- depth-proxied EMI summaries  
- noise-filtered, sovereignty-safe surfaces  

All responses masking feature-level or sensitive patterns.

---

### **2️⃣ Conductivity Surfaces (`conductivity/`)**
Document:

- broad conductivity variability zones  
- environmental moisture proxies  
- soil/geomorphic pattern sensitivity  

No interpretations regarding archaeological features.

---

### **3️⃣ Magnetic Susceptibility Patterns (`susceptibility/`)**
Contain:

- susceptibility gradient zones  
- generalized magnetic variation blocks  
- environmental-lens correlation summaries  

Sensitive magnetic signatures are generalized to H3 r7+.

---

### **4️⃣ Composite EMI Models (`composite/`)**
Integrate:

- EMI (all frequencies)  
- magnetometry  
- EM31/EM38 style real/quad-phase data  
- resistivity/GPR generalized envelopes  

Used to construct multi-sensor, non-specific “anomaly tendency zones.”

---

### **5️⃣ Environmental Relationships (`environmental-links/`)**
Generalized correlations with:

- hydrology (terraces, floodplains, alluvial systems)  
- soils & sediment profiles  
- terrain roughness  
- vegetation/biomass patterns  

Environmental only.

---

### **6️⃣ Temporal EMI Patterns (`temporal/`)**
Describe:

- moisture/soil conductivity shifts across OWL-Time intervals  
- long-term environmental variability windows  
- multi-period EMI stability patterns  

Absolutely no cultural chronology is inferred.

---

## ⚠️ EMI Uncertainty Layers (`uncertainty/`)

Include:

- noise-band characterization  
- instrument drift effects  
- environmental disagreement surfaces  
- cross-sensor signal variance  

Used in Focus Mode as **EMI Confidence Chips**.

---

## 🧬 Metadata & Provenance Requirements

### **STAC (`stac/`)**
EMI STAC Items must include:

- H3-masked geometry  
- sensor-frequency metadata  
- environmental driver metadata  
- uncertainty layers  
- CARE classification  
- PROV-O lineage references  

### **DCAT (`metadata/`)**
Defines:

- dataset description  
- hydrology/soil/climate links  
- access/licensing  
- FAIR+CARE compliance  

### **PROV-O (`provenance/`)**
Tracks:

- EMI acquisition datasets  
- filtering + drift correction  
- multi-frequency compositing  
- H3 generalization & masking  
- WAL → Retry → Rollback lineage  
- uncertainty propagation  

---

## 🧠 Focus Mode Integration

EMI datasets support:

- environmental-only anomaly explanations  
- contextual Story Node v3 environmental blocks  
- narrative-safe multi-sensor overlays  
- hydrology/soil correlation summaries  

Example Focus Summary:

> **Focus Summary:**  
> EMI data reveals broad zones of conductivity and magnetic variation linked to hydrology and soils. All surfaces are generalized, feature-safe, and reviewed under FAIR+CARE governance.

---

## 🛡 CARE & Ethical Requirements

All EMI datasets must:

- avoid subsurface feature inference  
- apply H3 r7+ spatial masking  
- disclose uncertainty and environmental limitations  
- avoid culturally sensitive interpretation  
- be sovereignty-reviewed before publication  
- maintain environmental-only framing  

Any EMI layer at risk of implying sensitive subsurface information → must be **generalized further or removed**.

---

## 🕰️ Version History

| Version | Date       | Author                                   | Summary |
|--------:|------------|------------------------------------------|---------|
| v11.0.0 | 2025-11-17 | Geophysics WG · Archaeology WG · FAIR+CARE Council | Initial EMI results registry under KFM-MDP v11.0.0. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
EMI Geophysics Results · CARE-Governed · FAIR+CARE Certified  
MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Geophysics Results](../README.md)

</div>
