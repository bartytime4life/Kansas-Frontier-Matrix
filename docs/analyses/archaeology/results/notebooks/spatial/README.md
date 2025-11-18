---
title: "📓🗺️ Kansas Frontier Matrix — Analysis Notebooks: Spatial Modeling (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/notebooks/spatial/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly · Spatial Modeling WG · Archaeology WG · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/archaeology-spatial-notebooks-v1.json"
governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Notebook Index"
intent: "archaeology-spatial-analysis-notebooks"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed / Spatial Generalization"
sensitivity_level: "High"
public_exposure_risk: "Medium"
indigenous_rights_flag: true
data_steward: "Spatial Modeling WG · Archaeology WG · FAIR+CARE Council"
risk_category: "Spatial Modeling / Sovereignty-Generalized"
redaction_required: true
provenance_chain:
  - "docs/analyses/archaeology/results/notebooks/spatial/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "HowTo"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"
  owl_time: "TemporalEntity"
json_schema_ref: "../../../../../schemas/json/archaeology-spatial-notebooks.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/archaeology-spatial-notebooks-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:results:notebooks:spatial-v11.0.0"
semantic_document_id: "kfm-arch-spatial-notebooks"
event_source_id: "ledger:docs/analyses/archaeology/results/notebooks/spatial/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Restricted / Sovereignty-Safe"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "uncertainty-explanation"
ai_transform_prohibited:
  - "site-inference"
  - "settlement-reconstruction"
  - "boundary-prediction"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
classification: "Internal / CARE-Governed"
jurisdiction: "Kansas / United States"
role: "archaeology-spatial-notebooks-root"
lifecycle_stage: "stable"
ttl_policy: "Review every 6 months"
sunset_policy: "Superseded upon next spatial-modeling update"
---

<div align="center">

# 📓🗺️ **Spatial Modeling Notebooks — Results Index**  
`docs/analyses/archaeology/results/notebooks/spatial/README.md`

**Purpose:**  
Serve as the authoritative, culturally safe index for **spatial modeling analysis notebooks**—including H3 generalization, KDE, spatial clustering, spatial uncertainty, environmental-affordance mapping, and spatiotemporal smoothing—used throughout the Kansas Frontier Matrix (KFM).

These notebooks generate intermediate geospatial layers that later feed **artifact**, **geophysics**, **predictive**, and **cultural landscape** results.

</div>

---

## 📘 Overview

Spatial notebooks in KFM:

- produce **H3 r7+ generalized** spatial surfaces  
- generate KDE smoothing layers for safe distribution analysis  
- implement CARE-approved masking logic  
- derive landscape-scale spatial statistics  
- compute geospatial uncertainty (variance, disagreement, error surfaces)  
- harmonize spatial metadata via STAC/DCAT  
- export PROV-O lineage & redaction logs  
- validate map layers for Focus Mode v3  
- ensure all spatial outputs remain **non-provenience**, **non-site-level**, and **sovereignty-safe**

Strictly prohibited:

- deriving or revealing precise site locations  
- reconstructing settlement patterns at fine scale  
- generating spatial predictions tied to identity or culture  
- visualizing sensitive geometries below H3 r7  

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/results/notebooks/spatial/
├── README.md                         # This file
├── h3-generalization/                # H3 masking, resolution testing, spatial smoothing
├── kde/                              # KDE models, bandwidth optimization, smoothing QA
├── clustering/                       # Spatial clustering (H3, DBSCAN-safe, envelope methods)
├── spatial-statistics/               # Moran's I, Gi*, spatial entropy, spatial auto-correlation
├── environmental-links/              # Spatial correlation with hydrology, terrain, soils, vegetation
├── temporal/                         # Temporal-spatial surfaces (OWL-Time aligned)
├── composite/                        # Multi-driver spatial composites
├── uncertainty/                      # Spatial variance, proxy disagreement, surface stability
├── qa/                               # CARE compliance, spatial integrity, masking validation
└── exports/                          # Plots, rasters, CSV, JSON-LD, envelope geometries
~~~

---

## 🧪 Notebook Categories

### **1️⃣ H3 Generalization Notebooks (`h3-generalization/`)**
Produce:

- resolution tests  
- generalization masks  
- geometry simplification  
- sovereignty redaction receipts  
- spatial complexity QA  

These ensure no sub-H3 detail escapes.

---

### **2️⃣ KDE Notebooks (`kde/`)**
Generate:

- kernel density estimations (generalized)  
- bandwidth tests  
- smoothing comparisons  
- KDE envelopes used in artifact/geophysics layers  

---

### **3️⃣ Spatial Clustering (`clustering/`)**
Support:

- H3 clustering  
- safe DBSCAN envelope extraction  
- spatial-density blocks  
- no sensitive cluster shapes  

---

### **4️⃣ Spatial Statistics (`spatial-statistics/`)**
Provide:

- Moran’s I  
- Getis–Ord Gi*  
- spatial autocorrelation maps  
- spatial entropy metrics  

All **generalized**, never site-level.

---

### **5️⃣ Environmental Spatial Links (`environmental-links/`)**
Model:

- hydrology proximity patterns  
- terrain–behavior interactions  
- soil/vegetation co-distributions  
- environmental drivers on generalized spatial surfaces  

---

### **6️⃣ Temporal-Spatial Surfaces (`temporal/`)**
Contain:

- OWL-Time aligned spatial grids  
- time-sliced KDE distributions  
- multi-period generalized envelopes  

---

### **7️⃣ Composite Spatial Models (`composite/`)**
Integrate:

- KDE  
- clustering  
- environmental drivers  
- terrain/hydrology/soils/vegetation  

Outputs feed predictive & cultural landscape pipelines.

---

### **8️⃣ Spatial Uncertainty (`uncertainty/`)**
Track:

- variance surfaces  
- disagreement between proxies  
- smoothing fragility  
- uncertainty envelopes  

Export as **Spatial Confidence Chips** for Focus Mode.

---

### **9️⃣ QA Notebooks (`qa/`)**
Perform:

- H3 masking validation  
- sovereignty compliance  
- CARE boundary checks  
- STAC/DCAT schema testing  
- spatial redaction verification  
- reproducibility audits  

---

## 🧬 Metadata & Provenance Integration

All spatial notebooks must export:

- **prov:Bundle** lineage  
- **STAC Items** with generalized geometry  
- **DCAT JSON-LD** metadata  
- uncertainty surfaces & statistics  
- masking + redaction logs  
- reproducibility hashes (parameters, seeds, environment)

Outputs populate:

- spatial/stac/  
- spatial/metadata/  
- spatial/provenance/

---

## 🧠 Focus Mode Integration

Spatial notebooks inform:

- generalized spatial overlays  
- environmental affordance maps  
- narrative-safe representation of spatial processes  
- spatial confidence chips  
- Story Node v3 map contexts  

**Example Focus Summary:**  
> Spatial notebooks generate H3-generalized, sovereignty-safe spatial layers and uncertainty envelopes that support environmental-only reasoning in Focus Mode without revealing sensitive archaeological information.

---

## 🛡 CARE & Ethical Requirements

All spatial analysis notebooks must:

- apply H3 r7+ generalization  
- exclude all sensitive spatial detail  
- avoid cultural or identity-linked spatial inference  
- document sovereign-masking steps  
- include uncertainty + environmental context  
- undergo FAIR+CARE review before release  

If unsafe → the notebook is **blocked**.

---

## 🕰️ Version History

| Version | Date       | Author                                       | Summary |
|--------:|------------|----------------------------------------------|---------|
| v11.0.0 | 2025-11-17 | Spatial Modeling WG · Archaeology WG · FAIR+CARE Council | Initial spatial-notebook index for KFM-MDP v11. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Spatial Modeling Notebooks · CARE-Governed · FAIR+CARE Certified  
MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Notebooks Index](../README.md)

</div>
