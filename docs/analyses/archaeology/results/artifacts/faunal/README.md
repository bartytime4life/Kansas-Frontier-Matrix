---
title: "🐾🦴 Kansas Frontier Matrix — Artifact Results: Faunal (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/artifacts/faunal/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly · Archaeology WG · Faunal Analysis WG · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/archaeology-artifact-faunal-results-v1.json"
governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Artifact Analysis Results"
intent: "archaeology-artifacts-faunal-results"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed / Public-Domain Faunal Only"
sensitivity_level: "High"
public_exposure_risk: "Medium"
indigenous_rights_flag: true
data_steward: "Archaeology WG · Faunal Specialists · FAIR+CARE Council"
risk_category: "Faunal Interpretation (Generalized)"
redaction_required: true
provenance_chain:
  - "docs/analyses/archaeology/results/artifacts/faunal/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E20 Biological Object"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"
json_schema_ref: "../../../../../../schemas/json/archaeology-artifact-faunal-results.schema.json"
shape_schema_ref: "../../../../../../schemas/shacl/archaeology-artifact-faunal-results-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:artifact:faunal-results-v11.0.0"
semantic_document_id: "kfm-arch-artifact-faunal-results"
event_source_id: "ledger:docs/analyses/archaeology/results/artifacts/faunal/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Restricted"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "environmental-context-linking"
ai_transform_prohibited:
  - "species-linked cultural inference"
  - "sacred-fauna-reconstruction"
  - "restricted ecological knowledge inference"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Internal / CARE-Governed"
role: "archaeology-artifacts-faunal-results-root"
lifecycle_stage: "stable"
ttl_policy: "Review every 6 months"
sunset_policy: "Superseded upon next faunal-results update"
---

<div align="center">

# 🐾🦴 **Faunal Artifact Results**  
`docs/analyses/archaeology/results/artifacts/faunal/README.md`

**Purpose:**  
Provide a FAIR+CARE–aligned registry of **faunal artifact analytical results** within the Kansas Frontier Matrix (KFM).  
These datasets include **public-domain, non-sensitive** faunal distributions, eco-functional groupings, environmental correlations, and generalized temporal patterns—excluding all culturally restricted, sacred, or sensitive faunal classifications.

</div>

---

## 📘 Overview

Faunal artifact results in the KFM include:

- generalized species-group summaries (PD-only)  
- eco-functional classifications (herbivore/carnivore/omnivore generalities)  
- skeletal element frequency (non-sensitive)  
- broad subsistence indicators (environment-only context)  
- H3 r7+ faunal distribution generalizations  
- eco-hydrological correlation summaries  
- temporal affordance patterns (OWL-Time aligned)  

Excluded from KFM:

- funerary/faunal remains tied to sensitive contexts  
- culturally restricted species  
- sacred ecological knowledge  
- species-level inference where culturally sensitive  
- any specimen requiring tribal or cultural permission  

All faunal outputs must pass FAIR+CARE + PROV-O lineage validation.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/results/artifacts/faunal/
├── README.md                                   # This file
├── taxonomy/                                   # PD-safe taxonomic groups (generalized)
├── skeletal-elements/                          # Generalized element frequencies
├── distribution/                               # H3 r7+ faunal distribution surfaces
├── environmental-links/                        # Hydrology/soil/vegetation faunal correlations
├── subsistence/                                # Ecological/energetic grouping summaries
├── temporal/                                   # OWL-Time aligned faunal patterns
├── uncertainty/                                # Uncertainty, variance & proxy disagreement
├── stac/                                       # STAC Items for faunal result layers
├── metadata/                                   # DCAT + JSON-LD metadata
└── provenance/                                  # PROV-O lineage & modeling logs
~~~

---

## 🐾 Faunal Result Types

### **1️⃣ Taxonomic Groups (`taxonomy/`)**
Contain:

- generalized fauna categories (large mammal / small mammal / bird / fish)  
- PD-safe subcategories  
- eco-functional groups (browser, grazer, omnivore)  

No culturally restricted species or sensitive identifications.

---

### **2️⃣ Skeletal Element Summaries (`skeletal-elements/`)**
Provide:

- bone-element frequency summaries  
- generalized fragmentation analyses  
- environmental-use interpretations  

No cultural practices or ceremonial associations inferred.

---

### **3️⃣ Faunal Distribution Patterns (`distribution/`)**
Include:

- H3 generalized density surfaces  
- KDE smoothed faunal distribution  
- eco-hydrological overlays  

Never show exact site or specimen provenance.

---

### **4️⃣ Environmental Correlation Summaries (`environmental-links/`)**
Analyze:

- hydrology proximity  
- soil/vegetation linkages  
- climate/seasonality relationships  

Environmental-only interpretation.

---

### **5️⃣ Subsistence & Ecological Indicators (`subsistence/`)**
Document generalized:

- foraging zones  
- energetic categories  
- eco-functional subsistence relationships  

No cultural subsistence reconstructions allowed.

---

### **6️⃣ Temporal Faunal Patterns (`temporal/`)**
OWL-Time aligned summaries:

- broad ecological shifts  
- faunal distribution changes across phases  
- generalized environmental trends  

No cultural chronology or people-fauna relationships.

---

## ⚠️ Uncertainty & Variance (`uncertainty/`)

Contains:

- taxonomic uncertainty  
- distribution variance  
- proxy disagreement  
- eco-functional classification uncertainty  

Displayed in Focus Mode as **Faunal Confidence Chips**.

---

## 🧬 Metadata & Provenance

### **STAC (`stac/`)**
Requirements:

- generalized H3 geometry  
- faunal metadata tags  
- environmental-driver references  
- uncertainty and lineage assets  

### **DCAT (`metadata/`)**
Provides:

- dataset purpose  
- FAIR+CARE compliance info  
- PD-only status  
- access/licensing  

### **PROV-O (`provenance/`)**
Tracks:

- dataset origins  
- analytical transformations  
- generalization & masking processes  
- uncertainty propagation  
- WAL → Retry → Rollback lineage  

---

## 🧠 Focus Mode Integration

Faunal results contribute to:

- Story Node v3 ecological context  
- Focus Mode environmental summaries  
- generalized subsistence-affordance explanations  
- non-cultural, eco-functional reasoning blocks  

Example Focus Summary:

> **Focus Summary:**  
> Generalized faunal patterns reveal broad ecological tendencies across Kansas, shaped by hydrology, vegetation, and terrain. All interpretations exclude sensitive species and follow FAIR+CARE review.

---

## 🛡 CARE & Ethical Requirements

All faunal datasets must:

- avoid culturally sensitive species or contexts  
- avoid funerary or ceremonial associations  
- apply H3 r7+ spatial generalization  
- disclose uncertainty  
- remain purely environmental/ecological  
- pass FAIR+CARE Council review  

If a dataset risks cultural harm → it must be masked or removed.

---

## 🕰️ Version History

| Version | Date       | Author                                   | Summary |
|--------:|------------|------------------------------------------|---------|
| v11.0.0 | 2025-11-17 | Archaeology WG · Faunal Specialists · FAIR+CARE Council | Initial faunal-results registry under KFM-MDP v11.0.0. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Faunal Artifact Results · CARE-Governed · FAIR+CARE Certified  
MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Artifact Results](../README.md)

</div>