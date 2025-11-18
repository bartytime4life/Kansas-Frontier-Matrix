---
title: "🏺🔬 Kansas Frontier Matrix — Artifact Results: Ceramics (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/artifacts/ceramics/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly / Archaeology WG · Ceramic Analysis WG · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/archaeology-artifact-ceramics-results-v1.json"
governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Artifact Analysis Results"
intent: "archaeology-artifacts-ceramics-results"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed / Public-Domain Ceramics Only"
sensitivity_level: "High"
public_exposure_risk: "Medium"
indigenous_rights_flag: true
data_steward: "Archaeology WG · Ceramics Analysts · FAIR+CARE Council"
risk_category: "Material Culture Interpretation"
redaction_required: true
provenance_chain:
  - "docs/analyses/archaeology/results/artifacts/ceramics/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E22 Man-Made Object"
  schema_org: "CreativeWork"
  prov_o: "prov:Entity"
  owl_time: "TemporalEntity"
json_schema_ref: "../../../../../../schemas/json/archaeology-artifact-ceramics-results.schema.json"
shape_schema_ref: "../../../../../../schemas/shacl/archaeology-artifact-ceramics-results-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:artifact:ceramics-results-v11.0.0"
semantic_document_id: "kfm-arch-artifact-ceramics-results"
event_source_id: "ledger:docs/analyses/archaeology/results/artifacts/ceramics/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Restricted"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "material-description"
ai_transform_prohibited:
  - "tribal-identity-inference"
  - "provenience-reconstruction"
  - "restricted-cultural-attribution"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Internal / CARE-Governed"
role: "archaeology-artifacts-ceramics-results-root"
lifecycle_stage: "stable"
ttl_policy: "Review every 6 months"
sunset_policy: "Superseded upon next ceramics-results update"
---

<div align="center">

# 🏺🔬 **Ceramic Artifact Results**  
`docs/analyses/archaeology/results/artifacts/ceramics/README.md`

**Purpose:**  
Provide a FAIR+CARE–aligned, scientifically controlled registry of **ceramic artifact analytical results** within the Kansas Frontier Matrix (KFM).  
Ceramic results include **public-domain, culturally safe** typology summaries, compositional analyses, generalized distribution patterns, and environmental correlations—with **no restricted, sacred, or culturally sensitive materials** reported.

</div>

---

## 📘 Overview

Ceramic artifact results in KFM synthesize:

- typology & motif generalizations  
- mineralogical & petrographic analyses  
- surface-treatment summaries  
- compositional datasets (public-domain)  
- generalized distribution patterns (H3 r7+)  
- proxy-independent environmental correlations  
- explanatory materials for Story Node v3 & Focus Mode  

These analyses **never**:

- propose cultural identity or affiliation  
- infer site-level locations  
- interpret ceremonial/sacred content  
- display restricted archaeological materials  
- include unreviewed or restricted tribal heritage  

All datasets undergo **FAIR+CARE** review and **PROV-O lineage validation**.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/results/artifacts/ceramics/
├── README.md                                   # This file
├── typology/                                   # Ceramic typology + motif summaries (generalized)
├── petrography/                                # Mineralogical/compositional analyses
├── surface-treatment/                          # Slip, burnish, cordmark, texture summaries
├── distribution/                               # H3-generalized ceramic distributions
├── environmental-links/                        # Hydrology/soil/climate ceramic correlations
├── temporal/                                   # OWL-Time aligned generalized ceramic timelines
├── uncertainty/                                # Uncertainty + proxy disagreement layers
├── stac/                                       # STAC Items for ceramic-based result layers
├── metadata/                                   # DCAT + JSON-LD metadata
└── provenance/                                 # PROV-O lineage & modeling logs
~~~

---

## 🏺 Ceramic Result Types

### **1️⃣ Typology Summaries (`typology/`)**
Contain:

- generalized motif clusters  
- vessel category summaries  
- fabric analysis  
- shape/size distributions  
- public-domain reference groupings  

**No restricted iconography or culturally sensitive symbols.**

---

### **2️⃣ Petrographic & Mineralogical Analyses (`petrography/`)**
Include:

- thin-section summaries  
- mineral inclusions  
- clay-source generalizations  
- XRF/ICP-MS data (PD only)  
- compositional PCA/cluster summaries  

Always generalized; never tied to restricted clay sources.

---

### **3️⃣ Surface Treatment Analyses (`surface-treatment/`)**
Document:

- cordmarking  
- smoothing/burnishing  
- stamping/impressing (non-restricted)  
- resist/slip patterns  

Generalized pattern analysis, no cultural assignment.

---

### **4️⃣ Ceramic Distribution Patterns (`distribution/`)**
Provide:

- H3 generalized artifact density  
- KDE smoothed ceramic distribution surfaces  
- environmental overlay tendencies  
- eco-hydrological correlations  

Never show exact provenience.

---

### **5️⃣ Environmental Correlation Summaries (`environmental-links/`)**
Analyze:

- hydrology proximity  
- soil-resources  
- vegetation/biomass links  
- climate/seasonality constraints  

Environmental explanations only.

---

### **6️⃣ Temporal Ceramic Patterns (`temporal/`)**
Use OWL-Time to:

- define broad ceramic temporal windows  
- evaluate cross-period distribution tendencies  
- align environmental factors with ceramic change  

No cultural chronologies or attributions.

---

## ⚠️ Uncertainty Layers (`uncertainty/`)

Store:

- proxy disagreement  
- compositional variance  
- distribution uncertainty  
- clustering variance  

Displayed in Focus Mode as **Ceramic Confidence Chips**.

---

## 🧬 Metadata & Provenance

### **STAC (`stac/`)**
Ceramic STAC Items must include:

- generalized spatial geometry (H3 r7+)  
- environmental driver metadata  
- distribution rasters/vectors  
- uncertainty summaries  
- provenance linkage  

### **DCAT (`metadata/`)**
Define:

- dataset purpose  
- access constraints  
- FAIR+CARE governance notes  
- licensing  
- distribution metadata  

### **PROV-O (`provenance/`)**
Track:

- source datasets  
- transformation methods  
- typology/petrography processes  
- smoothing & generalization  
- uncertainty propagation  
- WAL → Retry → Rollback lineage  

---

## 🧠 Focus Mode Integration

Ceramic results support:

- Story Node v3 material-culture context  
- safe, generalized AI explanations  
- environmental/cultural landscape overlays  
- non-attributional narrative components  

Example Focus Summary:

> **Focus Summary:**  
> Ceramic analyses identify broad motifs, fabrics, and distribution tendencies that align with environmental affordances. All ceramic results are generalized, public-domain, and reviewed under FAIR+CARE safeguards.

---

## 🛡 CARE & Ethical Requirements

All ceramic result datasets must:

- avoid cultural/tribal identity inference  
- avoid sacred/restricted artifacts  
- avoid reconstructing provenance  
- apply spatial generalization (H3 r7+)  
- disclose uncertainty  
- undergo FAIR+CARE Council review  

If a dataset risks cultural sensitivity → it must be masked or removed.

---

## 🕰️ Version History

| Version | Date       | Author                                   | Summary |
|--------:|------------|------------------------------------------|---------|
| v11.0.0 | 2025-11-17 | Archaeology WG · Ceramics Analysts · FAIR+CARE Council | Initial ceramics-results registry under KFM-MDP v11.0.0. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Ceramic Artifact Results · CARE-Governed · FAIR+CARE Certified  
MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Artifact Results](../README.md)

</div>