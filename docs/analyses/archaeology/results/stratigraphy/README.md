---
title: "🪨 Kansas Frontier Matrix — Stratigraphy Results (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/stratigraphy/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly / Archaeology Working Group · Paleoenvironment Group · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/archaeology-stratigraphy-results-v1.json"
governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Results"
intent: "archaeology-stratigraphy-results"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed / Environmental Context"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
indigenous_rights_flag: true
data_steward: "Archaeology WG · Paleoenvironment WG · FAIR+CARE Council"
risk_category: "Stratigraphic Interpretation"
redaction_required: false
provenance_chain:
  - "docs/analyses/archaeology/results/stratigraphy/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E26 Physical Feature"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"
json_schema_ref: "../../../../../schemas/json/archaeology-stratigraphy-results.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/archaeology-stratigraphy-results-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:stratigraphy-results-v11.0.0"
semantic_document_id: "kfm-arch-results-stratigraphy"
event_source_id: "ledger:docs/analyses/archaeology/results/stratigraphy/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "contextual-linking"
ai_transform_prohibited:
  - "layer-to-site-inference"
  - "unverified-cultural-association"
  - "speculative-stratigraphic-interpretation"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Internal / CARE-Governed"
role: "archaeology-stratigraphy-results-root"
lifecycle_stage: "stable"
ttl_policy: "Review every 6 months"
sunset_policy: "Superseded upon next stratigraphy synthesis"
---

<div align="center">

# 🪨 **Kansas Frontier Matrix — Stratigraphy Results**  
`docs/analyses/archaeology/results/stratigraphy/README.md`

**Purpose:**  
Summarize all **paleoenvironmental and archaeological stratigraphy results** that support the interpretation of cultural deposits, landform evolution, geomorphic processes, and temporal transitions within the Kansas Frontier Matrix (KFM).  
These outputs integrate geological, environmental, hydrological, and archaeological data in a **generalized**, culturally safe, FAIR+CARE–aligned format.

</div>

---

## 📘 Overview

Stratigraphy results in the KFM represent:

- generalized stratigraphic models (no exact excavation details)  
- soil horizon sequences  
- alluvial & colluvial processes  
- depositional & erosional surface reconstructions  
- temporal alignment using OWL-Time  
- geomorphic stability models  
- archaeological layer contextualization (safe/generalized)  

All outputs follow strict protocols:

- **no excavation-level detail**  
- **no burial references**  
- **no sensitive site-specific stratigraphic interpretations**  
- **H3 r7+ spatial generalization**  
- **FAIR+CARE cultural governance**  
- **full provenance (PROV-O)**  

The purpose is to provide **landscape-scale stratigraphic context**, not site-level excavation results.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/results/stratigraphy/
├── README.md                              # This file
├── soil-horizons/                          # Generalized soil profiles & pedology layers
├── geomorphology/                          # Alluvial/colluvial models, landform dynamics
├── depositional-models/                    # Stratigraphic reconstructions across landscapes
├── temporal-correlation/                   # OWL-Time stratigraphic alignment outputs
├── predictive/                             # Predictive stratigraphy & geomorphic stability
├── uncertainty/                            # Stratigraphic uncertainty layers
├── stac/                                   # STAC Items for stratigraphy result datasets
├── metadata/                               # DCAT + JSON-LD metadata
└── provenance/                             # PROV-O lineage & transformation workflow logs
~~~

---

## 🌱 Soil Horizon Results (`soil-horizons/`)

Includes:

- generalized A/B/C horizon patterns  
- soil moisture / drainage categories  
- pedogenic indicators  
- land–soil interaction models  
- alignments with Late Prehistoric settlement tendencies (generalized)

---

## 🏞️ Geomorphology Results (`geomorphology/`)

Covers:

- terrace evolution  
- floodplain sedimentation models  
- colluvial/alluvial boundaries  
- geomorphic stability grids  
- paleo-landscape reconstructions  

These contextualize long-term environmental affordances.

---

## 🪨 Depositional Models (`depositional-models/`)

Includes:

- landscape-scale stratigraphic stacking models  
- depositional & erosional surfaces  
- eolian/alluvial interfaces  
- proxy-linked depositional sequences  
- general sediment pathway interpretations  

---

## 🕰️ Temporal Correlation (`temporal-correlation/`)

Represents:

- OWL-Time aligned stratigraphic units  
- temporal stacking patterns  
- cross-dataset correlations  
- generalized depositional sequences across periods  

No site-level stratigraphy is used.

---

## 🔮 Predictive Stratigraphy Models (`predictive/`)

Generated with ML/GAM frameworks:

- geomorphic stability potential  
- depositional likelihood surfaces  
- soil/landform evolution predictions  
- terrain-proxy interactions  

These help explain long-term environmental patterns.

---

## ⚠️ Stratigraphic Uncertainty (`uncertainty/`)

Includes:

- uncertainty rasters  
- cross-proxy disagreement maps  
- geomorphic transition uncertainty  
- confidence scoring  
- environmental interpolation limitations  

Required for FAIR+CARE interpretation.

---

## 🧬 Metadata & Provenance Requirements

### **STAC**
Includes:

- surface assets (raster/vector)  
- temporal extent  
- spatial generalization notes  
- uncertainty assets  

### **DCAT**
Includes:

- dataset descriptions  
- method summaries  
- accessibility & licensing  
- FAIR+CARE governance  

### **PROV-O Lineage**
Encoded in:

`provenance/`

Tracking:

- data sources  
- transformations  
- modeling activities  
- lineage checkpoints (WAL → Retry → Rollback)  

---

## 🧠 Focus Mode Integration

Stratigraphy results feed:

- Story Node environmental/landform context  
- Focus Mode geomorphic explanations  
- climate–landform temporal transitions  
- deep-time environmental narratives  

Example Focus Summary:

> **Focus Summary:**  
> Landscape-scale stratigraphy models reveal stable terrace systems and gradual alluvial build-up across Late Prehistoric Kansas. These contextual layers support generalized interpretations of settlement patterns without revealing site-specific excavations.

---

## ⚠️ Ethical & CARE Requirements

All stratigraphy results must:

- avoid excavation-level detail  
- avoid burial/feature references  
- avoid cultural or tribal inferences  
- fully generalize all geographies (H3 r7+)  
- disclose uncertainty clearly  
- undergo FAIR+CARE review for public-safe use  

---

## 🕰️ Version History

| Version | Date       | Author                           | Summary |
|--------:|------------|----------------------------------|---------|
| v11.0.0 | 2025-11-17 | Archaeology WG · Paleoenvironment WG · FAIR+CARE Council | Initial stratigraphy results registry under KFM-MDP v11.0.0. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Stratigraphy Results · CARE-Governed · FAIR+CARE Certified  
MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Archaeology Results](../README.md)

</div>