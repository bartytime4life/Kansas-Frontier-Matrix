---
title: "🌿🕰️ Kansas Frontier Matrix — Paleoenvironmental Results (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/paleoenvironment/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly / Paleoenvironment Working Group · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/archaeology-paleoenvironment-results-v1.json"
governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Results"
intent: "archaeology-paleoenvironment-results"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed / Environmental Context"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
indigenous_rights_flag: true
data_steward: "Paleoenvironment WG · FAIR+CARE Council"
risk_category: "Paleoenvironmental Interpretation"
redaction_required: false
provenance_chain:
  - "docs/analyses/archaeology/results/paleoenvironment/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E27 Site"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"
json_schema_ref: "../../../../../schemas/json/archaeology-paleoenvironment-results.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/archaeology-paleoenvironment-results-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:paleoenvironment-results-v11.0.0"
semantic_document_id: "kfm-arch-results-paleoenvironment"
event_source_id: "ledger:docs/analyses/archaeology/results/paleoenvironment/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "contextual-linking"
ai_transform_prohibited:
  - "fabricated-climate-inference"
  - "unverified-holocene-sequences"
  - "restricted-cultural-attribution"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Internal / CARE-Governed"
role: "archaeology-paleoenvironment-results-root"
lifecycle_stage: "stable"
ttl_policy: "Review every 6 months"
sunset_policy: "Superseded upon next paleoenvironment synthesis"
---

<div align="center">

# 🌿🕰️ **Kansas Frontier Matrix — Paleoenvironmental Results**  
`docs/analyses/archaeology/results/paleoenvironment/README.md`

**Purpose:**  
Provide a unified, FAIR+CARE–aligned collection of **paleoenvironmental analytical results** supporting Late Prehistoric, Protohistoric, and Historic-period archaeological interpretation in the Kansas Frontier Matrix (KFM).  
These datasets provide **deep-time environmental context** for cultural landscape dynamics, hydrology-linked settlement tendencies, ecological affordances, and temporal transitions.

</div>

---

## 📘 Overview

KFM Paleoenvironment results integrate:

- climate reconstructions (Holocene → Late Prehistoric)  
- paleo-hydrology models  
- seasonal climate reconstructions (winter/summer)  
- paleovegetation & ecozone transitions  
- drought/wet oscillation summaries  
- proxy-weighted environmental models  
- predictive paleo-likelihood surfaces  
- environmental uncertainty layers  

These results:

- are **fully generalized**  
- avoid speculative narratives  
- include **uncertainty metadata & provenance**  
- follow **FAIR+CARE** ethical and cultural protections  
- serve as **environmental scaffolding** for archaeological analyses, Story Nodes, and Focus Mode v3  

No dataset in this directory infers cultural identities or references restricted Indigenous knowledge.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/results/paleoenvironment/
├── README.md                             # This file
├── climate/                              # Temperature, precipitation, PDSI, SPEI reconstructions
├── paleohydrology/                        # Paleo-river, floodplain, moisture-balance models
├── vegetation/                            # Paleo-vegetation & ecozone reconstructions
├── seasonality/                           # Seasonal (winter/summer) paleo-climate layers
├── drought-cycles/                        # Holocene drought/wet oscillation summaries
├── predictive/                            # Predictive paleo-environmental modeling outputs
├── uncertainty/                           # Paleoenvironmental uncertainty layers
├── stac/                                  # STAC Items for paleoenvironment result layers
├── metadata/                              # DCAT and JSON-LD metadata
└── provenance/                            # PROV-O lineage for paleoenvironment transformations
~~~

---

## 🌡️ Climate Reconstruction Results (`climate/`)

Includes:

- Holocene temperature reconstructions  
- precipitation & moisture-balance models  
- seasonal anomalies (Late Prehistoric focus)  
- climate change trend surfaces  
- raster outputs for predictive modeling  

All climate surfaces include:

- uncertainty rasters  
- proxy-weight metadata  
- CARE metadata for safe interpretation  

---

## 🌊 Paleo-Hydrology Results (`paleohydrology/`)

Contains:

- reconstructed paleochannels  
- alluvial boundary generalizations  
- moisture-balance models  
- hydrology–settlement interaction summaries  

Critical for understanding **long-term settlement affordances**.

---

## 🌱 Paleo-Vegetation Results (`vegetation/`)

Includes:

- Holocene vegetation reconstruction  
- prairie–woodland transition summaries  
- ecozone stability/variability  
- biomass models  
- generalized vegetation belts  

---

## ❄️☀️ Paleo-Seasonality (`seasonality/`)

Contains:

- winter/summer temperature reconstructions  
- seasonal precipitation layers  
- seasonal environmental constraint models  
- seasonal uncertainty rasters  

These directly inform mobility, subsistence, and landscape usage patterns.

---

## 🌵 Drought & Wet Cycle Reconstructions (`drought-cycles/`)

Includes:

- time-series drought indices (PDSI-like proxies)  
- oscillation frequency summaries  
- drought/wet clustering  
- proxy agreement/variance maps  

---

## 🔮 Predictive Paleoenvironment Models (`predictive/`)

Generated using ML/GAM workflows:

- paleo-likelihood environmental surfaces  
- ecological stability models  
- hydrology-linked suitability  
- spatial explanatory maps & SHAP layers  

---

## ⚠️ Paleoenvironmental Uncertainty (`uncertainty/`)

Stores:

- uncertainty rasters  
- proxy disagreement metrics  
- temporal interpolation confidence  
- model-fit reports  

These are required for **scientific and ethical interpretation**.

---

## 🧬 Metadata & Provenance

### **STAC Metadata (`stac/`)**
Must include:

- spatial extent (generalized)  
- temporal extent (OWL-Time)  
- proxy references  
- CARE classification  
- data quality/uncertainty info  
- asset listings  

### **DCAT Metadata (`metadata/`)**
Includes:

- dataset purpose  
- method summaries  
- proxy citations  
- accessibility limits  
- FAIR+CARE statements  

### **PROV-O Lineage (`provenance/`)**
Documents:

- proxy datasets used  
- transformation activities  
- modeling pipelines  
- configuration versions  
- uncertainty propagation  

All files must pass CI validation before release.

---

## 🧠 Focus Mode Integration

Paleoenvironment layers provide context for:

- Story Node v3 environmental background  
- climate-linked settlement interpretations  
- corridor & affordance narratives  
- time-sliced environmental transitions  
- uncertainty-aware explanations  

Example Focus Summary:

> **Focus Summary:**  
> Paleoenvironmental reconstructions indicate stable hydrology and moderate climate variability during Late Prehistoric periods, supporting generalized cultural-landscape patterns across central Kansas. All interpretations are generalized, proxy-driven, and CARE-reviewed.

---

## ⚠️ Ethical & CARE Requirements

All paleoenvironment results must:

- avoid attributing climate shifts to cultural decisions  
- avoid speculative narratives  
- avoid linking proxies to specific tribal histories  
- include uncertainty explanations  
- be masked, generalized, and sovereignty-aligned  
- undergo FAIR+CARE review before publication  

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|--------:|------|--------|---------|
| v11.0.0 | 2025-11-17 | Paleoenvironment WG · FAIR+CARE Council | Initial paleoenvironment results registry under KFM-MDP v11. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Paleoenvironmental Results · CARE-Governed · FAIR+CARE Certified  
MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Archaeology Results](../README.md)

</div>