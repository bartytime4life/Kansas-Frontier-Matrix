---
title: "🗺️🏺 Kansas Frontier Matrix — Artifact Results: Spatial Distributions (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/artifacts/spatial-distributions/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly · Archaeology WG · Spatial Modeling WG · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../../releases/v11.0.0/schemas/telemetry/archaeology-artifact-spatial-distributions-v1.json"
governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Spatial Result Registry"
intent: "archaeology-artifacts-spatial-distributions"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed / Spatially Generalized"
sensitivity_level: "High"
public_exposure_risk: "Medium"
indigenous_rights_flag: true
data_steward: "Archaeology WG · FAIR+CARE Council"
risk_category: "Spatial Interpretation of Cultural Materials"
redaction_required: true
provenance_chain:
  - "docs/analyses/archaeology/results/artifacts/spatial-distributions/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E53 Place"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"
json_schema_ref: "../../../../../../schemas/json/archaeology-artifact-spatial-distributions.schema.json"
shape_schema_ref: "../../../../../../schemas/shacl/archaeology-artifact-spatial-distributions-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:artifact:spatial-distributions-v11.0.0"
semantic_document_id: "kfm-arch-artifact-spatial-distributions"
event_source_id: "ledger:docs/analyses/archaeology/results/artifacts/spatial-distributions/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Restricted"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "environmental-context-linking"
ai_transform_prohibited:
  - "site-location-inference"
  - "reverse-provenience"
  - "cultural-boundary-reconstruction"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Internal / CARE-Governed"
role: "archaeology-artifacts-spatial-distributions-root"
lifecycle_stage: "stable"
ttl_policy: "Review every 6 months"
sunset_policy: "Superseded upon next spatial-distribution update"
---

<div align="center">

# 🗺️🏺 **Artifact Results — Spatial Distributions**  
`docs/analyses/archaeology/results/artifacts/spatial-distributions/README.md`

**Purpose:**  
Define and document all **spatially generalized artifact distribution results** used in archaeological analysis across the Kansas Frontier Matrix (KFM).  
These distributions provide **safe, aggregated, H3-generalized spatial patterns** of public-domain artifact datasets without exposing provenience, site boundaries, or culturally restricted material distributions.

</div>

---

## 📘 Overview

Spatial distribution modeling supports:

- landscape-scale artifact pattern detection  
- cross-material distribution comparison  
- eco-hydrological pattern recognition  
- predictive environmental modeling  
- generalized settlement-pattern support  
- Focus Mode and Story Node spatial context  

All spatial distributions are:

- **H3 r7+ generalized**  
- **derived only from public-domain artifact datasets**  
- **stripped of exact coordinates**  
- **validated under FAIR+CARE**  
- **paired with uncertainty layers**  
- **linked to PROV-O lineage & STAC/DCAT**  

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/results/artifacts/spatial-distributions/
├── README.md                                   # This file
├── ceramics/                                   # Generalized ceramic spatial distributions
├── lithics/                                    # Generalized lithic spatial distributions
├── faunal/                                     # Faunal distribution tendencies (PD only)
├── metals/                                     # Metal artifact distribution generalizations
├── composite/                                  # Multi-material distribution overlays
├── environmental-links/                        # Hydrology/soils/vegetation correlations
├── temporal/                                   # OWL-Time aligned distribution sequences
├── uncertainty/                                # Uncertainty + proxy disagreement surfaces
├── stac/                                       # STAC Items for distribution layers
├── metadata/                                   # DCAT + JSON-LD metadata
└── provenance/                                 # PROV-O lineage for distribution modeling
~~~

---

## 🧩 Spatial Distribution Types

### **1️⃣ Ceramic Distributions (`ceramics/`)**
Include:

- H3-generalized ceramic density surfaces  
- KDE smoothing layers  
- hydrology/soil/climate overlays  

No provenience-level data.

---

### **2️⃣ Lithic Distributions (`lithics/`)**
Provide:

- generalized lithic density maps  
- environmental co-occurrence surfaces  
- cross-material comparison layers  

All spatial patterns generalized.

---

### **3️⃣ Faunal Distributions (`faunal/`)**
Derived from PD-safe faunal datasets:

- H3 hex density grids  
- eco-functional spatial tendencies  

Never include restricted species locations.

---

### **4️⃣ Metal Distributions (`metals/`)**
Include:

- H3 spatial generalizations of metal artifacts  
- environmental layers (soils, hydrology, terrain)  
- KDE smoothing outputs  

No colonial/restricted or sensitive metal patterns included.

---

### **5️⃣ Composite Multi-Material Patterns (`composite/`)**
Integrate:

- ceramics  
- lithics  
- faunal  
- metals  

Used for broad, generalized landscape-pattern inference.

---

### **6️⃣ Environmental Correlation Layers (`environmental-links/`)**
Contain:

- hydrology-linked distribution tendencies  
- soils & vegetation correlations  
- terrain & climate co-patterns  

Environmental-only context.

---

### **7️⃣ Temporal Distribution Patterns (`temporal/`)**
OWL-Time aligned tendencies:

- broad environmental shifts  
- cross-period distribution persistence or attenuation  
- NOT cultural chronologies  

---

## ⚠️ Uncertainty (`uncertainty/`)

Include:

- smoothed variance surfaces  
- KDE uncertainty  
- environmental disagreement  
- dataset sparsity indicators  

Focus Mode shows these as **Distribution Confidence Chips**.

---

## 🧬 Metadata & Provenance Requirements

### **STAC (`stac/`)**
Spatial distributions must include:

- H3 multipolygon geometry  
- uncertainty assets  
- environmental driver metadata  
- CARE classification  
- PROV-O lineage bundles  

### **DCAT (`metadata/`)**
Must define:

- dataset description  
- access/license  
- FAIR+CARE metadata  
- distribution formats  

### **PROV-O (`provenance/`)**
Tracks:

- dataset sources  
- distribution modeling steps  
- H3 generalization  
- smoothing & interpolation  
- uncertainty propagation  
- WAL → Retry → Rollback lineage  

---

## 🧠 Focus Mode Integration

Spatial distributions power:

- map overlays  
- cluster comparisons  
- environmental-context explanations  
- Story Node v3 landscape panels  

Example Focus Summary:

> **Focus Summary:**  
> Spatially generalized artifact distributions reveal broad environmental tendencies across the Kansas region, without exposing provenience or culturally sensitive geography. All layers have undergone FAIR+CARE review.

---

## 🛡 CARE & Ethical Requirements

All spatial distributions must:

- avoid revealing provenience or site boundaries  
- avoid cultural or tribal inference  
- be generalized to H3 r7+  
- include uncertainty  
- be derived only from PD datasets  
- pass FAIR+CARE review before release  

If a distribution risks cultural sensitivity → it must be masked or excluded.

---

## 🕰️ Version History

| Version | Date       | Author                                    | Summary |
|--------:|------------|-------------------------------------------|---------|
| v11.0.0 | 2025-11-17 | Archaeology WG · FAIR+CARE Council        | Initial artifact spatial distribution registry under MDP v11.0.0. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Artifact Spatial Distributions · CARE-Governed · FAIR+CARE Certified  
MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Artifact Results](../README.md)

</div>
