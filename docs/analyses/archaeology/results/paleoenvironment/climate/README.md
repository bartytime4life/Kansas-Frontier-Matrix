---
title: "🌡️📜 Kansas Frontier Matrix — Paleoenviron. Results: Climate Reconstructions (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/paleoenvironment/climate/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly · Paleoenvironment WG · Archaeology WG · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/archaeology-paleoenv-climate-v1.json"
governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Paleoenvironmental Result"
intent: "archaeology-paleoenvironment-climate-results"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed / Paleoenvironmental Reconstruction"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
indigenous_rights_flag: true
data_steward: "Paleoenvironment WG · FAIR+CARE Council"
risk_category: "Environmental Reconstruction"
redaction_required: true
provenance_chain:
  - "docs/analyses/archaeology/results/paleoenvironment/climate/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E1 CRM Entity"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  owl_time: "TemporalEntity"
json_schema_ref: "../../../../../schemas/json/archaeology-paleoenv-climate-results.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/archaeology-paleoenv-climate-results-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:results:paleoenvironment:climate-v11.0.0"
semantic_document_id: "kfm-arch-paleoenv-climate-results"
event_source_id: "ledger:docs/analyses/archaeology/results/paleoenvironment/climate/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Restricted / Environmental-Only"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "uncertainty-explanation"
ai_transform_prohibited:
  - "cultural-identity-inference"
  - "history-reconstruction"
  - "speculative paleo-cultural links"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
classification: "Internal / CARE-Governed"
jurisdiction: "Kansas / United States"
role: "archaeology-paleoenv-climate-results-root"
lifecycle_stage: "stable"
ttl_policy: "Review every 6 months"
sunset_policy: "Updated upon next paleoenvironmental model revision"
---

<div align="center">

# 🌡️📜 **Paleoenvironmental Results — Climate Reconstructions**  
`docs/analyses/archaeology/results/paleoenvironment/climate/README.md`

**Purpose:**  
Document all **generalized, sovereignty-safe paleoclimate reconstructions** integrated into the Kansas Frontier Matrix (KFM), including temperature, precipitation, seasonality, drought/flood intervals, and multi-proxy paleoenvironmental climate surfaces.

</div>

---

## 📘 Overview

Paleoclimate results in KFM:

- synthesize multi-proxy datasets (pollen, charcoal, lake cores, isotopes, soil profiles)
- generate environmental, **non-cultural** paleoclimate surfaces
- generalize temporally using **OWL-Time intervals**
- generalize spatially using **H3 r7+ masking**
- quantify uncertainty and proxy disagreement
- produce environmental-only Story Node context blocks
- avoid any cultural interpretation, historical reconstruction, or sensitive attribution

Strict prohibitions:

- no cultural timelines  
- no cultural-environment narrative implication  
- no spatial precision revealing sensitive paleo-locations  

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/results/paleoenvironment/climate/
├── README.md                         # This file
├── temperature/                      # Paleo-temperature reconstructions
├── precipitation/                    # Paleo-precipitation & moisture indices
├── seasonality/                      # Multi-proxy seasonality indicators
├── drought-flood/                    # Drought/flood paleo events (generalized)
├── proxy-assemblages/                # Proxy group composites (pollen, charcoal, isotopes)
├── temporal/                         # OWL-Time aligned paleoclimate sequences
├── uncertainty/                      # Variance, proxy disagreement, reconstruction spread
├── stac/                             # STAC Items for paleoclimate rasters
├── metadata/                         # DCAT + JSON-LD metadata
└── provenance/                       # PROV-O lineage for paleoclimate reconstructions
~~~

---

## 🌡️ Paleoclimate Result Types

### **1️⃣ Temperature Reconstructions (`temperature/`)**
Includes:

- generalized mean annual temperature  
- seasonal temperature envelopes  
- reconstruction uncertainty  
- multi-proxy smoothing  

---

### **2️⃣ Precipitation Reconstructions (`precipitation/`)**
Produce:

- annual & seasonal precipitation grids  
- hydrology-correlated paleo-moisture indices  
- speleothem/charcoal/pollen-driven reconstructions  

---

### **3️⃣ Seasonality (`seasonality/`)**
Provide:

- proxy-weighted seasonal extremes  
- frost-free period envelopes  
- climatic seasonality bands across OWL-Time slices  

---

### **4️⃣ Drought/Flood Indicators (`drought-flood/`)**
Contain:

- paleo-drought events (generalized)  
- floodplain-stability indicators  
- multi-century moisture variability  

All events strictly **environmental**, NOT cultural.

---

### **5️⃣ Proxy Assemblages (`proxy-assemblages/`)**
Combine:

- pollen  
- charcoal  
- isotopes  
- lake cores  
- sediment stratigraphy  

Producing composite environmental paleoclimate signals.

---

## ⚠️ Uncertainty (`uncertainty/`)
Tracks:

- proxy disagreement  
- variance in multi-proxy reconstructions  
- temporal-spread uncertainty  
- spatial reconstruction ambiguity  

Displayed in Focus Mode as **Paleoenvironmental Confidence Chips**.

---

## 🧬 Metadata & Provenance

### **STAC (`stac/`)**  
Each climate layer must include:

- H3-masked geometry  
- temporal extent  
- environmental drivers  
- proxy details (public-safe only)  
- uncertainty metadata  
- lineage references  

### **DCAT (`metadata/`)**
Documents:

- dataset scope  
- FAIR+CARE conditions  
- environmental framing  
- generalized spatial/temporal summaries  

### **PROV-O (`provenance/`)**
Tracks:

- proxy datasets used  
- reconstruction method  
- temporal smoothing  
- spatial masking  
- uncertainty propagation  
- WAL → Retry → Rollback lineage  

---

## 🧠 Focus Mode Integration

Outputs provide:

- environmental paleoclimate context  
- narrative-safe temporal envelopes  
- proxy conflict indicators  
- uncertainty summaries  

**Example Focus Summary:**

> Paleoclimate reconstructions summarize environmental trends across long time spans without cultural interpretation. All layers are generalized, uncertainty-weighted, and sovereignty-safe.

---

## 🛡 CARE & Ethical Requirements

All paleoclimate results must:

- avoid cultural interpretation  
- exclude sensitive proxy sources  
- apply spatial generalization (H3 r7+)  
- disclose uncertainty  
- undergo sovereign data and FAIR+CARE review  

If a reconstruction risks cultural inference → **it must be generalized or removed**.

---

## 🕰️ Version History

| Version | Date       | Author                                          | Summary |
|--------:|------------|-------------------------------------------------|---------|
| v11.0.0 | 2025-11-17 | Paleoenvironment WG · FAIR+CARE Council        | Initial paleoclimate results registry. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Paleoenvironmental Climate Results · FAIR+CARE Certified · Sovereignty-Safe  
Diamond⁹ Ω · Crown∞Ω Ultimate Certified  

[Back to Paleoenvironment Results](../README.md)

</div>
