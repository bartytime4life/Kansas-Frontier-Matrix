---
title: "📜🌍 Kansas Frontier Matrix — Paleoenviron. Results: Provenance & Lineage (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/paleoenvironment/provenance/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly · Paleoenvironment WG · Metadata WG · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/archaeology-paleoenv-provenance-v1.json"
governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Provenance Registry"
intent: "archaeology-paleoenvironment-provenance-results"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed / Provenance-Sensitive"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
indigenous_rights_flag: true
data_steward: "Paleoenvironment WG · Metadata WG · FAIR+CARE Council"
risk_category: "Environmental Reconstruction Lineage"
redaction_required: true
provenance_chain:
  - "docs/analyses/archaeology/results/paleoenvironment/provenance/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E7 Activity"
  schema_org: "Dataset"
  prov_o: "prov:Bundle"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"
json_schema_ref: "../../../../../schemas/json/archaeology-paleoenv-provenance.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/archaeology-paleoenv-provenance-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:paleoenvironment:provenance-v11.0.0"
semantic_document_id: "kfm-arch-paleoenv-provenance"
event_source_id: "ledger:docs/analyses/archaeology/results/paleoenvironment/provenance/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Restricted / Environmental-Only"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "lineage-explanation"
ai_transform_prohibited:
  - "cultural-inference"
  - "reverse-location-reconstruction"
  - "historical-attribution"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
classification: "Internal / CARE-Governed"
jurisdiction: "Kansas / United States"
role: "archaeology-paleoenvironment-provenance-root"
lifecycle_stage: "stable"
ttl_policy: "Review every 6 months"
sunset_policy: "Updated with next paleoenvironment provenance framework"
---

<div align="center">

# 📜🌍 **Paleoenvironmental Results — Provenance & Lineage**  
`docs/analyses/archaeology/results/paleoenvironment/provenance/README.md`

**Purpose:**  
Define the authoritative **PROV-O lineage documentation** for all paleoenvironmental results in the Kansas Frontier Matrix (KFM), including paleoclimate, hydrology, vegetation, soils, drought cycles, and paleoenvironmental predictive models.  
Ensures fully transparent, sovereignty-safe environmental lineage without enabling cultural inference or sensitive spatial reconstruction.

</div>

---

## 📘 Overview

Paleoenvironmental provenance captures:

- multi-proxy source datasets (pollen, charcoal, isotopes, cores)  
- reconstruction methods (environment-only)  
- OWL-Time temporal alignment steps  
- spatial H3 r7+ generalization operations  
- proxy weighting and calibration  
- smoothing + interpolation logic  
- uncertainty propagation (variance, disagreement, ensemble spread)  
- environmental-only modeling transformations  
- masking justification and sovereignty-review logs  
- WAL → Retry → Rollback lineage events  

Strict prohibitions:

- **no cultural linkage**  
- **no fine-grained spatial origin data**  
- **no identity or group attribution**  
- **no speculative paleo-historical claims**  

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/results/paleoenvironment/provenance/
├── README.md                         # This file
├── proxy-sources/                    # Provenance of pollen, charcoal, isotopes, cores
├── reconstruction/                   # Steps + transformations for each paleo-surface
├── temporal/                         # OWL-Time interval lineage
├── generalization/                   # H3 masking & redaction logs
├── uncertainty/                      # Variance, disagreement & model-spread lineage
├── predictive/                       # Lineage for paleoenvironment predictive models
├── stac/                             # STAC provenance links
├── metadata/                         # DCAT provenance enrichments
└── bundles/                          # Final PROV-O bundles (JSON-LD)
~~~

---

## 🧩 Provenance Components

### **1️⃣ Proxy Source Provenance (`proxy-sources/`)**
Documents:

- pollen datasets  
- charcoal profiles  
- lake sediment cores  
- isotopic measurements  
- soil proxies  
- ecohydrological drivers  

All sources must be PD-safe and sovereignty-cleared.

---

### **2️⃣ Reconstruction Provenance (`reconstruction/`)**
Tracks:

- proxy weighting  
- harmonization + calibration  
- interpolation + smoothing  
- model selection  
- error controls  
- spatial masking  

---

### **3️⃣ Temporal Provenance (`temporal/`)**
Includes:

- OWL-Time intervals  
- multi-period reconstruction windows  
- smoothing/aggregation logs  

---

### **4️⃣ Spatial Generalization (`generalization/`)**
Contains:

- H3 r7+ generalization receipts  
- geometry simplification  
- masking operations  
- sovereignty-based redaction justifications  

---

### **5️⃣ Uncertainty Lineage (`uncertainty/`)**
Tracks:

- proxy disagreement pathways  
- variance decomposition  
- model fragility  
- reconstruction ambiguity  

---

### **6️⃣ Predictive Provenance (`predictive/`)**
Documents:

- paleoclimate prediction configuration  
- ensemble predictions  
- uncertainty surfaces  
- environmental-only scenario metadata  

---

### **7️⃣ STAC Provenance (`stac/`)**
Stores:

- lineage-linked STAC Item fields  
- relation references  
- dataset dependency chains  

---

### **8️⃣ Metadata Provenance (`metadata/`)**
Tracks:

- DCAT temporal extent  
- spatial generalization metadata  
- FAIR+CARE labels  
- reuse & governance descriptors  

---

### **9️⃣ PROV-O Bundles (`bundles/`)**
Final outputs:

- full provenance graph  
- entity/activity/agent chains  
- redaction + masking logs  
- reproducibility snapshots  
- WAL checkpoint lineage  

---

## 🧠 Focus Mode Integration

Provenance surfaces provide:

- sovereignty-safe environmental lineage context  
- temporal and proxy-weighted transparency  
- uncertainty chips  
- environmental summary segments  

**Example Focus Summary:**  
> Paleoenvironmental provenance clarifies data origins, proxy chains, masking steps, and reconstruction uncertainty, ensuring environmental transparency without cultural interpretation.

---

## 🛡 CARE & Ethical Requirements

All provenance must:

- avoid cultural implications  
- disclose uncertainty  
- record all masking + generalization  
- be sovereignty-reviewed  
- comply with FAIR+CARE  

If unsafe → **generalize or remove**.

---

## 🕰️ Version History

| Version | Date       | Author                                       | Summary |
|--------:|------------|----------------------------------------------|---------|
| v11.0.0 | 2025-11-17 | Paleoenvironment WG · FAIR+CARE Council      | Initial paleoenvironment provenance registry. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Paleoenvironmental Provenance · FAIR+CARE Certified · Sovereignty-Safe  
Diamond⁹ Ω · Crown∞Ω Ultimate Certified  

[Back to Paleoenvironment Results](../README.md)

</div>
