---
title: "🔪🪨 Kansas Frontier Matrix — Artifact Results: Lithics (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/artifacts/lithics/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly · Archaeology WG · Lithics Analysis WG · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/archaeology-artifact-lithics-results-v1.json"
governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Artifact Analysis Results"
intent: "archaeology-artifacts-lithics-results"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed / Public-Domain Lithics Only"
sensitivity_level: "High"
public_exposure_risk: "Medium"
indigenous_rights_flag: true
data_steward: "Archaeology WG · Lithic Analysts · FAIR+CARE Council"
risk_category: "Material Culture (Generalized Lithics)"
redaction_required: true
provenance_chain:
  - "docs/analyses/archaeology/results/artifacts/lithics/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E22 Man-Made Object"
  schema_org: "CreativeWork"
  prov_o: "prov:Entity"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"
json_schema_ref: "../../../../../../schemas/json/archaeology-artifact-lithics-results.schema.json"
shape_schema_ref: "../../../../../../schemas/shacl/archaeology-artifact-lithics-results-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:artifact:lithics-results-v11.0.0"
semantic_document_id: "kfm-arch-artifact-lithics-results"
event_source_id: "ledger:docs/analyses/archaeology/results/artifacts/lithics/README.md"
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
  - "restricted-quarry-inference"
  - "provenience-reconstruction"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Internal / CARE-Governed"
role: "archaeology-artifacts-lithics-results-root"
lifecycle_stage: "stable"
ttl_policy: "Review every 6 months"
sunset_policy: "Superseded upon next lithics-results update"
---

<div align="center">

# 🔪🪨 **Lithic Artifact Results**  
`docs/analyses/archaeology/results/artifacts/lithics/README.md`

**Purpose:**  
Provide a controlled, FAIR+CARE–aligned registry of **lithic analytical results** used in the Kansas Frontier Matrix (KFM).  
This includes **public-domain, generalized** lithic material summaries, reduction-sequence indicators, distribution patterns, and environmental correlations.  
No restricted quarry information, sensitive stone sources, or culturally restricted materials are included.

</div>

---

## 📘 Overview

Lithics results in KFM include:

- material composition generalizations  
- flake/debitage patterning  
- tool-class summaries (projectile points, scrapers, bifaces; PD-only)  
- technological reduction indicators  
- H3-generalized spatial distribution patterns  
- environmental & affordance-linked lithic correlations  
- temporal (OWL-Time) lithic tendencies  
- uncertainty layers & provenance logs  

These outputs **exclude**:

- restricted chert/quarry locations  
- culturally sensitive stone sources  
- sacred-use tool types  
- any provenience-level lithic data  
- tribal identity assignments  

All results pass FAIR+CARE validation and full PROV-O lineage checks.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/results/artifacts/lithics/
├── README.md                                   # This file
├── material/                                   # Lithic raw material categories (generalized)
├── reduction/                                  # Reduction sequence indicators
├── tool-classes/                               # Generalized tool classifications
├── distribution/                               # H3 lithic distribution surfaces
├── environmental-links/                        # Lithics ↔ hydrology/terrain/soils patterns
├── temporal/                                   # OWL-Time aligned lithic patterns
├── uncertainty/                                # Uncertainty & variance layers
├── stac/                                       # STAC Items for lithic result layers
├── metadata/                                   # DCAT + JSON-LD metadata
└── provenance/                                  # PROV-O lineage & workflow logs
~~~

---

## 🪨 Lithic Result Types

### **1️⃣ Material Categories (`material/`)**
Includes aggregated categories such as:

- generalized chert groups (no quarry inference)  
- quartzite, obsidian (only PD-accessible)  
- heat alteration indicators  
- material-frequency bands  

All sensitive or tribal-source-linked materials are excluded.

---

### **2️⃣ Reduction Sequence Indicators (`reduction/`)**
Generalized summaries of:

- debitage size classes  
- platform preparation indicators  
- flake termination types  
- technological stage groupings  

Never tied to specific cultural practices.

---

### **3️⃣ Tool-Class Summaries (`tool-classes/`)**
Provide generalized counts/trends of:

- projectile points (PD-only typologies)  
- bifaces & preforms  
- scrapers & utilized flakes  
- core types  

Restricted or sensitive tool forms are omitted.

---

### **4️⃣ Lithic Distribution Patterns (`distribution/`)**
Contain:

- H3 r7+ generalized density surfaces  
- KDE smoothing layers  
- environmental co-distribution overlays  

No provenience-level mapping.

---

### **5️⃣ Environmental Correlation Layers (`environmental-links/`)**
Explore generalized links to:

- hydrology corridors  
- soils & pedogenic indicators  
- vegetation/biomass availability  
- terrain cost surfaces  

Environmental-only explanations.

---

### **6️⃣ Temporal Lithic Patterns (`temporal/`)**
OWL-Time aligned patterns describing:

- generalized lithic distribution shifts  
- long-term material/technology tendencies  
- multi-period environmental-lithic relationships  

No cultural chronologies.

---

## ⚠️ Uncertainty Layers (`uncertainty/`)

Include:

- material classification variance  
- reduction-sequence uncertainty  
- distribution variance  
- proxy disagreement metrics  

Shown in Focus Mode as **Lithic Confidence Chips**.

---

## 🧬 Metadata & Provenance

### **STAC (`stac/`)**  
Lithic STAC Items must include:

- H3 geometry  
- environmental drivers  
- uncertainty layers  
- material class metadata  
- lineage references  

### **DCAT (`metadata/`)**  
Contains:

- dataset purpose  
- PD-only verification  
- FAIR+CARE governance metadata  
- distribution & licensing  

### **PROV-O (`provenance/`)**
Tracks:

- source datasets  
- classification pipelines  
- transformation & generalization steps  
- uncertainty propagation  
- WAL → Retry → Rollback lineage  

---

## 🧠 Focus Mode Integration

Lithic results support:

- Story Node v3 material-culture summaries  
- safe AI narrative explanations  
- environmental-context overlays  
- comparative multi-material analyses  

Example Focus Summary:

> **Focus Summary:**  
> Lithic analyses show broad material and technological tendencies across Kansas landscapes, generalized for cultural safety. These summaries exclude quarry information and sensitive materials, following strict FAIR+CARE review.

---

## 🛡 CARE & Ethical Requirements

All lithic datasets must:

- exclude sensitive quarries and sources  
- avoid cultural or tribal inference  
- avoid reconstructing tool-use traditions  
- apply H3 r7+ generalization  
- disclose uncertainty  
- undergo FAIR+CARE review prior to publication  

If a dataset risks cultural sensitivity → it must be masked or removed.

---

## 🕰️ Version History

| Version | Date       | Author                                   | Summary |
|--------:|------------|------------------------------------------|---------|
| v11.0.0 | 2025-11-17 | Archaeology WG · Lithics Analysts · FAIR+CARE Council | Initial lithics-results registry under KFM-MDP v11.0.0. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Lithic Artifact Results · CARE-Governed · FAIR+CARE Certified  
MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Artifact Results](../README.md)

</div>