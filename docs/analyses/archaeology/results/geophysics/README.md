---
title: "🧲 Kansas Frontier Matrix — Archaeological Geophysics Results (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/geophysics/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly / Archaeology Working Group · Geophysics Leads · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/archaeology-geophysics-results-v1.json"
governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Results"
intent: "archaeology-geophysics-results"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed / Sensitive Subsurface Data"
sensitivity_level: "High"
public_exposure_risk: "High"
indigenous_rights_flag: true
data_steward: "Archaeology Geophysics WG · FAIR+CARE Council"
risk_category: "Subsurface Interpretation"
redaction_required: true
provenance_chain:
  - "docs/analyses/archaeology/results/geophysics/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E27 Site"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"
json_schema_ref: "../../../../../schemas/json/archaeology-geophysics-results.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/archaeology-geophysics-results-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:geophysics-results-v11.0.0"
semantic_document_id: "kfm-arch-results-geophysics"
event_source_id: "ledger:docs/analyses/archaeology/results/geophysics/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Restricted"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
ai_transform_prohibited:
  - "speculative-feature-detection"
  - "subsurface-site-inference"
  - "geophysical-to-cultural-attribution"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Internal / CARE-Governed"
role: "archaeology-geophysics-results-root"
lifecycle_stage: "stable"
ttl_policy: "Review every 6 months"
sunset_policy: "Superseded upon next geophysics-result synthesis"
---

<div align="center">

# 🧲 **Kansas Frontier Matrix — Archaeological Geophysics Results**  
`docs/analyses/archaeology/results/geophysics/README.md`

**Purpose:**  
Summarize all **processed, generalized, FAIR+CARE–aligned geophysical results** derived from magnetometry, GPR, resistivity, electromagnetic, and related prospection datasets within the KFM system.  
All outputs in this directory are culturally safe, spatially generalized, and strictly non-locational.

</div>

---

## 📘 Overview

KFM geophysical results represent:

- **public-safe generalizations of subsurface features**  
- **pattern-based summaries**, not excavated or confirmed archaeological features  
- geophysical anomalies aggregated to **H3 r7/r8**  
- statistical raster summaries and vector abstractions  
- explainability layers describing uncertainty & signal strength  

These outputs support:

- settlement-pattern inference (generalized)  
- environmental correlations  
- corridor studies  
- cluster reinforcement  
- Story Node v3 context panels  
- Focus Mode explanations  

**No result in this directory reveals exact site outlines, structures, burials, ceremonial areas, or sensitive subsurface information.**

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/results/geophysics/
├── README.md                           # This file
├── magnetometry/                       # Generalized magnetometry results
├── gpr/                                # GPR slice summaries (public-safe)
├── resistivity/                        # Resistivity pattern generalizations
├── electromagnetic/                    # EM induction summaries
├── clustering/                         # Spatial pattern clustering (generalized)
├── predictive/                         # Predictive models derived from geophysics
├── stac/                               # STAC Items for geophysical result layers
├── metadata/                           # DCAT, JSON-LD metadata
└── provenance/                         # PROV-O lineage for processed results
~~~

---

## 🧲 Geophysical Result Categories

### **1️⃣ Magnetometry (`magnetometry/`)**
Public-safe datasets include:

- H3-level anomaly density rasters  
- filtered, de-striped intensity grids  
- generalized pattern abstractions  
- environmental correlations  

Excludes:

- precise feature shapes  
- identifiable structures  
- sensitive anomaly clusters  

---

### **2️⃣ Ground-Penetrating Radar (`gpr/`)**
Includes:

- depth slice summaries (heavily generalized)  
- signal coherence maps  
- anomaly probability envelopes  
- temporal/depth windows  

Nothing here represents:

- burials  
- architecture  
- subsurface cultural detail  

---

### **3️⃣ Resistivity (`resistivity/`)**
Contains:

- resistivity contrast surface summaries  
- zone-based conductivity groupings  
- environmental/climatic comparative layers  

Always generalized and non-specific.

---

### **4️⃣ Electromagnetic Induction (`electromagnetic/`)**
Includes:

- multi-frequency response summaries  
- derived soil moisture/enhancement models  
- background vs anomaly separation surfaces  

---

### **5️⃣ Geophysical Clustering (`clustering/`)**
Provides:

- cluster aggregations over H3 cells  
- PCA/UMAP-based generalizations  
- confidence-weighted summaries  

---

### **6️⃣ Predictive Models (`predictive/`)**
Includes:

- settlement-likelihood modifiers derived from geophysical signals  
- environmental overlay interactions  
- ML explainability layers (SHAP/LIME)  

These are **environmental predictors**, not cultural confirmations.

---

## 🧬 Metadata & Provenance Requirements

### **STAC**
STAC Items include:

- generalized anomaly assets  
- raster/vector layer summaries  
- spatial footprints (H3 only)  
- PROV lineage references  

### **DCAT**
DCAT metadata includes:

- dataset purpose & description  
- validity & uncertainty notes  
- CARE cultural-safety classifications  

### **PROV-O**
Stored in:

`provenance/`

Includes:

- processing steps (filters, corrections, masks)  
- generalization workflows  
- QA/QC logs  
- WAL → Retry → Rollback lineage  

---

## 🧠 Focus Mode Integration

Geophysical summaries enrich Story Node & Focus Mode views by:

- providing context on environmental affordances  
- describing generalized subsurface pattern tendencies  
- assisting in multi-domain correlation narratives  

Example Focus Summary:

> **Focus Summary:**  
> Generalized geophysical patterns reveal broad anomaly zones in terrace-adjacent regions. These reflect environmental affordances rather than specific features, and all spatial detail is masked to protect cultural heritage.

---

## ⚠️ CARE / Ethical Requirements

All geophysical results must:

- be generalized to H3 r7 or coarser  
- never portray raw slices or feature outlines  
- avoid any interpretation implying subsurface features  
- include uncertainty & signal-confidence notes  
- follow tribal review for sensitive landscapes  

---

## 🕰️ Version History

| Version | Date       | Author                            | Summary |
|--------:|------------|-----------------------------------|---------|
| v11.0.0 | 2025-11-17 | Archaeology WG · Geophysics Leads · FAIR+CARE Council | Initial geophysics results registry under KFM-MDP v11. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Geophysical Results · CARE-Governed · FAIR+CARE Certified  
MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Archaeology Results](../README.md)

</div>