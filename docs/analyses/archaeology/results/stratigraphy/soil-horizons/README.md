---
title: "🧱⛏️ Kansas Frontier Matrix — Stratigraphy Results: Soil Horizon Reconstructions (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/stratigraphy/soil-horizons/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly · Stratigraphy WG · Soil Science WG · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/archaeology-stratigraphy-soil-horizons-v1.json"
governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Stratigraphy Result"
intent: "archaeology-stratigraphy-soil-horizon-results"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed / Subsurface-Generalized"
sensitivity_level: "High"
public_exposure_risk: "High"
indigenous_rights_flag: true
data_steward: "Stratigraphy WG · Soil Science WG · FAIR+CARE Council"
risk_category: "Subsurface Stratigraphy"
redaction_required: true
provenance_chain:
  - "docs/analyses/archaeology/results/stratigraphy/soil-horizons/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E1 CRM Entity"
  prov_o: "prov:Entity"
  schema_org: "Dataset"
  geosparql: "geo:FeatureCollection"
  owl_time: "TemporalEntity"
json_schema_ref: "../../../../../schemas/json/archaeology-stratigraphy-soil-horizons.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/archaeology-stratigraphy-soil-horizons-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:stratigraphy:soil-horizons-v11.0.0"
semantic_document_id: "kfm-arch-stratigraphy-soil-horizons"
event_source_id: "ledger:docs/analyses/archaeology/results/stratigraphy/soil-horizons/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Restricted / Environmental-Only"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "uncertainty-explanation"
ai_transform_prohibited:
  - "horizon-level inference"
  - "burial or structure identification"
  - "cultural or temporal attribution"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
classification: "Internal / Highly Sensitive / CARE-Governed"
jurisdiction: "Kansas / United States"
role: "archaeology-stratigraphy-soil-horizons-root"
lifecycle_stage: "stable"
ttl_policy: "Review every 6 months"
sunset_policy: "Updated on next soil-horizon modeling revision"
---

<div align="center">

# 🧱⛏️ **Stratigraphy Results — Soil Horizon Reconstructions**  
`docs/analyses/archaeology/results/stratigraphy/soil-horizons/README.md`

**Purpose:**  
Document the **generalized soil horizon reconstructions** produced within the Kansas Frontier Matrix (KFM).  
These reconstructions describe **broad pedogenic patterns**—A/B/C horizon tendencies, soil development regimes, stability windows, paleo-pedology envelopes—while preventing sensitive stratigraphic, archaeological, or feature-level inference.

</div>

---

## 📘 Overview

Soil horizon results in KFM:

- synthesize soil surveys, pedology datasets, paleoenvironmental proxies  
- produce **environment-only generalized horizon envelopes**  
- provide **A/B/C horizon likelihood** at coarse resolution  
- support geomorphology, paleoenvironment, and stratigraphy workflows  
- mask all spatial detail with **H3 r7+ generalization**  
- apply OWL-Time alignment for long-term soil development  
- propagate uncertainty, proxy disagreement, pedogenic ambiguity  
- prevent revealing depths, thicknesses, or buried horizon structures  
- maintain sovereignty & strict cultural-safety controls  

Prohibited:

- feature-level stratigraphy  
- pit/feature horizon description  
- archaeological soil-layer inference  
- any precise soil depth or thickness reconstruction  

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/results/stratigraphy/soil-horizons/
├── README.md                           # This file
├── horizons/                           # A/B/C horizon envelopes (generalized)
├── pedogenesis/                        # Soil-formation & developmental trend models
├── stability/                          # Stability windows (erosion/deposition balance)
├── environmental/                      # Climate/hydrology/vegetation soil drivers
├── temporal/                           # OWL-Time aligned temporal pedogenesis models
├── uncertainty/                        # Variance & proxy disagreement
├── stac/                               # STAC Items for soil horizon layers
├── metadata/                           # DCAT + JSON-LD metadata
└── provenance/                         # PROV-O lineage bundles
~~~

---

## 🧱 Soil Horizon Result Types

### **1️⃣ Horizon Envelopes (`horizons/`)**
Include:

- generalized A, B, C horizon distributions  
- coarse-scale soil-layer likelihoods  
- H3-masked horizon envelopes  
- no vertical horizon detail  

---

### **2️⃣ Pedogenesis Models (`pedogenesis/`)**
Describe:

- long-term soil formation  
- environmental drivers (climate, vegetation, topography)  
- pedogenic process envelopes  

---

### **3️⃣ Stability Models (`stability/`)**
Include:

- erosion/deposition balance envelopes  
- soil profile stability windows  
- geomorphic–pedogenic interplay  

---

### **4️⃣ Environmental Drivers (`environmental/`)**
Contain:

- climate-driven soil development  
- hydrology-linked soil moisture tendencies  
- vegetation/biomass influence  
- generalized eco-pedo coupling  

---

### **5️⃣ Temporal Soil Models (`temporal/`)**
OWL-Time aligned:

- multi-period soil formation sequences  
- paleo-soil transitions  
- long-term pedogenic envelopes  

---

## ⚠️ Uncertainty (`uncertainty/`)
Tracks:

- pedogenic disagreement  
- proxy conflict  
- reconstruction variance  
- smoothing ambiguity  
- environmental fragility  

Displayed in Focus Mode as **Soil Horizon Confidence Chips**.

---

## 🧬 Metadata & Provenance Requirements

### **STAC (`stac/`)**
Must include:

- H3 r7+ generalization  
- uncertainty metadata  
- driver metadata (climate, hydrology, terrain)  
- lineage references  

### **DCAT (`metadata/`)**
Specifies:

- dataset purpose  
- FAIR+CARE constraints  
- distribution metadata  
- temporal/scientific context  

### **PROV-O (`provenance/`)**
Documents:

- proxy sources  
- pedogenesis model steps  
- masking/generalization logs  
- uncertainty propagation  
- WAL → Retry → Rollback lineage  

---

## 🧠 Focus Mode Integration

Soil horizon layers support:

- environmental-only Story Node context  
- geomorphic + stratigraphic background  
- uncertainty chips  
- sovereign-safe explanations  

**Example Focus Summary:**  
> Soil horizon reconstructions describe broad pedogenic tendencies—generalized, uncertainty-weighted, and sovereignty-protected—without revealing sensitive stratigraphy.

---

## 🛡 CARE & Ethical Requirements

All soil horizon datasets must:

- avoid stratigraphic detail  
- prevent sensitive subsurface inference  
- apply H3 r7+ masking  
- document uncertainty & redaction  
- maintain environmental framing only  
- pass FAIR+CARE cultural-safety review  

If unsafe → **generalize further or remove**.

---

## 🕰️ Version History

| Version | Date       | Author                                  | Summary |
|--------:|------------|-----------------------------------------|---------|
| v11.0.0 | 2025-11-17 | Stratigraphy WG · FAIR+CARE Council     | Initial soil-horizon registry under MDP v11. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Soil Horizon Reconstructions · Sovereignty-Protected · FAIR+CARE Certified  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Stratigraphy Results](../README.md)

</div>
