---
title: "🌿📜 Kansas Frontier Matrix — Paleoenviron. Results: Vegetation & Ecozone Reconstructions (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/paleoenvironment/vegetation/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly · Paleoenvironment WG · Ecology WG · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/archaeology-paleoenv-vegetation-v1.json"
governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Paleoenvironmental Result"
intent: "archaeology-paleoenvironment-vegetation-results"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed / Paleoenvironmental Data"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
indigenous_rights_flag: true
data_steward: "Paleoenvironment WG · FAIR+CARE Council"
risk_category: "Environmental Reconstruction"
redaction_required: true
provenance_chain:
  - "docs/analyses/archaeology/results/paleoenvironment/vegetation/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E1 CRM Entity"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"
json_schema_ref: "../../../../../schemas/json/archaeology-paleoenv-vegetation-results.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/archaeology-paleoenv-vegetation-results-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:paleoenvironment:vegetation-v11.0.0"
semantic_document_id: "kfm-arch-paleoenv-vegetation-results"
event_source_id: "ledger:docs/analyses/archaeology/results/paleoenvironment/vegetation/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Restricted / Environmental-Only"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "uncertainty-explanation"
ai_transform_prohibited:
  - "cultural-inference"
  - "migration-reconstruction"
  - "identity-association"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
classification: "Internal / CARE-Governed"
jurisdiction: "Kansas / United States"
role: "archaeology-paleoenvironment-vegetation-root"
lifecycle_stage: "stable"
ttl_policy: "Review every 6 months"
sunset_policy: "Revised when paleo-vegetation model framework updates"
---

<div align="center">

# 🌿📜 **Paleoenvironmental Results — Vegetation & Ecozone Reconstructions**  
`docs/analyses/archaeology/results/paleoenvironment/vegetation/README.md`

**Purpose:**  
Document all **generalized, sovereignty-safe paleovegetation and ecozone reconstructions** integrated into the Kansas Frontier Matrix (KFM).  
Vegetation surfaces describe long-term environmental transitions—biomass, ecozones, canopy/groundcover shifts—derived from proxy datasets with strict FAIR+CARE alignment.

</div>

---

## 📘 Overview

Vegetation reconstructions in KFM:

- integrate multi-proxy records (pollen assemblages, charcoal, phytoliths, sediment chemistry)
- produce **generalized ecozone distributions**  
- derive **paleo-biomass envelopes**  
- compute **vegetation stability/transition surfaces**  
- align with **OWL-Time periods**  
- enforce **H3 r7+ spatial generalization**  
- quantify **uncertainty**, proxy disagreement, and reconstruction spread  
- supply safe environmental narratives for Focus Mode & Story Nodes  

Strictly prohibited:

- cultural-inference linkage  
- habitat → cultural group attribution  
- reconstructing culturally sensitive paleo-landscapes  
- providing sub-H3 spatial precision  

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/results/paleoenvironment/vegetation/
├── README.md                          # This file
├── ecozones/                          # Broad paleo-ecozone reconstructions
├── biomass/                           # Biomass & vegetation density envelopes
├── canopy-groundcover/                # Canopy vs groundcover reconstructions (generalized)
├── proxy-assemblages/                 # Proxy-source composites (pollen/charcoal/phytolith)
├── temporal/                          # OWL-Time aligned vegetation sequences
├── uncertainty/                       # Disagreement & reconstruction ambiguity
├── stac/                              # STAC Items for paleovegetation outputs
├── metadata/                          # DCAT + JSON-LD metadata
└── provenance/                        # PROV-O lineage for vegetation modeling
~~~

---

## 🌿 Paleovegetation Result Types

### **1️⃣ Ecozones (`ecozones/`)**
Contain:

- generalized ecozone maps (prairie, woodland, savanna, wetland analogs)  
- proxy-weighted paleoecological region boundaries  
- H3 r7+ envelopes  

---

### **2️⃣ Biomass Reconstructions (`biomass/`)**
Include:

- biomass density envelopes  
- vegetation productivity indicators  
- moisture/soil-linked biomass response  

No cultural interpretation allowed.

---

### **3️⃣ Canopy / Groundcover (`canopy-groundcover/`)**
Provide:

- generalized canopy density  
- grass/forb vs tree-shrub distributions  
- proxy-derived shading envelopes  

---

### **4️⃣ Proxy Assemblages (`proxy-assemblages/`)**
Combine:

- pollen  
- charcoal  
- phytoliths  
- sediment chemistry  

Outputs become multi-proxy paleoecological composites.

---

## ⚠️ Uncertainty (`uncertainty/`)

Tracks:

- proxy disagreement  
- reconstruction variance  
- driver-associated uncertainty  
- ensemble spread  

Displayed in Focus Mode as **Vegetation Confidence Chips**.

---

## 🧬 Metadata & Provenance Requirements

### **STAC (`stac/`)**  
STAC Items must include:

- generalized H3 geometry  
- vegetation domain metadata  
- proxy-source descriptors  
- uncertainty data  
- PROV lineage references  

### **DCAT (`metadata/`)**
Defines:

- dataset scope  
- environmental-only framing  
- FAIR+CARE requirements  
- distribution formats  

### **PROV-O (`provenance/`)**
Tracks:

- proxy datasets used  
- reconstruction method  
- smoothing/interpolation routines  
- masking/generalization  
- uncertainty propagation  
- WAL → Retry → Rollback lineage  

---

## 🧠 Focus Mode Integration

Vegetation layers support:

- ecozone narrative blocks  
- environmental temporal slices  
- uncertainty chips  
- safe vegetation-related summaries  

**Example Focus Summary:**  
> Paleovegetation reconstructions describe long-term ecological patterns and biomass changes without cultural inference, fully generalized and sovereignty-safe.

---

## 🛡 CARE & Ethical Requirements

All vegetation results must:

- avoid cultural interpretations  
- apply H3 r7+ masking  
- be generalized beyond sensitive proxy locations  
- document uncertainty clearly  
- pass FAIR+CARE review  
- maintain environmental-only framing  

If any layer risks cultural inference → **generalize or remove**.

---

## 🕰️ Version History

| Version | Date       | Author                                     | Summary |
|--------:|------------|--------------------------------------------|---------|
| v11.0.0 | 2025-11-17 | Paleoenvironment WG · FAIR+CARE Council    | Initial paleo-vegetation results registry. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Paleovegetation Results · FAIR+CARE Certified · Sovereignty-Protected  
Diamond⁹ Ω · Crown∞Ω Ultimate Certified  

[Back to Paleoenvironment Results](../README.md)

</div>
