---
title: "🏺 Kansas Frontier Matrix — Archaeological Artifact Results (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/artifacts/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly / Archaeology Working Group · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/archaeology-artifact-results-v1.json"
governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Results"
intent: "archaeology-artifact-results"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed"
sensitivity_level: "High"
public_exposure_risk: "Medium"
indigenous_rights_flag: true
data_steward: "Archaeology Working Group · FAIR+CARE Council"
risk_category: "Artifact Result Summary"
redaction_required: true
provenance_chain:
  - "docs/analyses/archaeology/results/artifacts/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E31 Document"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
json_schema_ref: "../../../../../schemas/json/archaeology-artifact-results.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/archaeology-artifact-results-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:artifact-results-v11.0.0"
semantic_document_id: "kfm-arch-results-artifacts"
event_source_id: "ledger:docs/analyses/archaeology/results/artifacts/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Restricted"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
ai_transform_prohibited:
  - "speculative-cultural-attribution"
  - "site-specific interpretations"
  - "restricted-material-description"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Internal / CARE-Governed"
role: "archaeology-artifact-results-root"
lifecycle_stage: "stable"
ttl_policy: "Review every 6 months"
sunset_policy: "Superseded upon next artifact-result synthesis"
---

<div align="center">

# 🏺 **Kansas Frontier Matrix — Archaeological Artifact Results**  
`docs/analyses/archaeology/results/artifacts/README.md`

**Purpose:**  
Provide a controlled, FAIR+CARE–aligned synthesis of **artifact-based analytical results** from the Kansas Frontier Matrix (KFM).  
These results reflect **generalized, sovereignty-respecting**, and **scientifically validated** interpretations of artifact distributions, typologies, material compositions, technological traits, and chronological signatures—without revealing sensitive provenience or restricted cultural information.

</div>

---

## 📘 Overview

This directory contains **artifact-derived analytical outputs**, produced through:

- validated material analysis (ceramics, lithics, metals, faunal, etc.)  
- typological classification backed by controlled vocabularies  
- chemical and mineralogical composition studies  
- distributional modeling (H3 generalized)  
- environmental and cultural correlation studies  
- temporal alignment using OWL-Time intervals  
- integration with predictive modeling & Story Node v3  

All results adhere to:

- **FAIR** principles (Findable, Accessible, Interoperable, Reusable)  
- **CARE** principles (Collective Benefit, Authority to Control, Responsibility, Ethics)  
- KFM Ethics Guidelines and Tribal Data Governance  
- MCP-DL v6.3 reproducibility standards  
- PROV-O lineage and metadata validation  

No file in this directory contains exact site locations, restricted cultural items, or direct tribal cultural attributions.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/results/artifacts/
├── README.md                                 # This file
├── lithics/                                  # Generalized lithic results
├── ceramics/                                 # Ceramic typology & composition results
├── metals/                                   # Metallurgical and elemental analysis results
├── faunal/                                   # Public-domain faunal datasets and analyses
├── spatial-distributions/                    # H3 generalized artifact distribution analyses
├── temporal/                                 # Time-linked artifact synthesis (OWL-Time)
├── clustering/                               # Artifact clustering & similarity results
├── stac/                                     # STAC Items for artifact-based result layers
├── metadata/                                 # DCAT, JSON-LD, schema metadata
└── provenance/                               # PROV-O lineage & processing logs
~~~

---

## 🧱 Result Categories

### **1️⃣ Lithic Artifact Results (`lithics/`)**
Includes:

- generalized lithic density patterns  
- material categories (chert, quartzite, obsidian where PD)  
- manufacturing stages (debitage, bifaces, retouched tools)  
- geochemical sourcing results (public-domain only)  
- H3 generalized spatial summaries  

---

### **2️⃣ Ceramic Artifact Results (`ceramics/`)**
Contains:

- ceramic typology summaries  
- decorative motif clusters (CARE-filtered)  
- mineralogical & petrographic analyses  
- temporal groupings (OWL-Time aligned)  
- distributional summaries  

---

### **3️⃣ Metal Artifact Results (`metals/`)**
Includes:

- elemental composition (XRF/ICP-MS; PD-only datasets)  
- alloy signatures  
- manufacturing traits  
- trade-route correlation summaries  

---

### **4️⃣ Faunal Artifact Results (`faunal/`)**
Contains:

- faunal species summaries (public-domain)  
- butchering pattern analyses (non-sensitive)  
- environmental and dietary correlation studies  

Restricted species or culturally restricted fauna are NEVER included.

---

### **5️⃣ Artifact Spatial Distribution Models (`spatial-distributions/`)**
Includes:

- H3-level generalized artifact density maps  
- KDE surface summaries  
- spatial correlations with hydrology, soils, landforms  
- CARE-driven masking of sensitive regions  

---

### **6️⃣ Temporal Artifact Results (`temporal/`)**
Includes:

- OWL-Time artifact phase summaries  
- cross-phase comparative analysis  
- radiocarbon-linked artifact groupings (generalized)  

---

### **7️⃣ Artifact Clustering & Similarity (`clustering/`)**
Provides:

- cluster memberships (generalized)  
- similarity matrices for artifact types  
- cultural-technological patterns (generalized)  

---

## 🧬 Metadata & Provenance

All artifact results require:

### **STAC Metadata**
- itemized assets  
- spatial extents (generalized)  
- descriptive tags  
- provenance references  

### **DCAT Metadata**
- artifact class descriptions  
- rights & accessibility  
- sensitivity classifications  

### **PROV-O Lineage**
Stored in `provenance/`, includes:

- dataset source references  
- classification processes  
- material analysis workflows  
- generalization steps  
- quality assurance records  

---

## 🧠 Focus Mode Integration

Artifact results power:

- Story Node material-culture segments  
- narrative building blocks for cultural timelines  
- cross-domain environmental + artifact correlations  
- AI explanation layers in Focus Mode v3  

All outputs must include **Focus Safe Summaries**, for example:

> **Focus Summary:**  
> Generalized artifact patterns indicate recurring Late Prehistoric tool use and ceramic activity within broad hydrology-linked zones. Data are generalized for cultural sovereignty and do not reflect specific site locations.

---

## ⚠️ CARE / Ethics Requirements

- No culturally sensitive artifacts described.  
- No funerary or ceremonial objects included.  
- No attribution to tribal identity without explicit approval.  
- Spatial masking must use H3 r7+.  
- Chemical sourcing results must avoid identifying restricted quarries or sacred landscapes.  

---

## 🕰️ Version History

| Version | Date       | Author                           | Summary |
|--------:|------------|----------------------------------|---------|
| v11.0.0 | 2025-11-17 | Archaeology WG · FAIR+CARE Council | Initial comprehensive artifact-results registry under KFM-MDP v11. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Artifact Results · CARE-Governed · FAIR+CARE Certified  
MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Archaeology Results](../README.md)

</div>