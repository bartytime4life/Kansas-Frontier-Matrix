---
title: "📓🏺 Kansas Frontier Matrix — Analysis Notebooks: Artifact Results (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/notebooks/artifacts/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly · Archaeology WG · Material Culture WG · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/archaeology-artifacts-notebooks-v1.json"
governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Notebook Index"
intent: "archaeology-artifacts-notebooks"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed / Analysis Notebooks"
sensitivity_level: "High"
public_exposure_risk: "Medium"
indigenous_rights_flag: true
data_steward: "Archaeology WG · FAIR+CARE Council"
risk_category: "Artifact Analysis / Notebook Output"
redaction_required: true
provenance_chain:
  - "docs/analyses/archaeology/results/notebooks/artifacts/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "HowTo"
  prov_o: "prov:Plan"
  owl_time: "TemporalEntity"
json_schema_ref: "../../../../../schemas/json/archaeology-artifacts-notebooks.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/archaeology-artifacts-notebooks-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:results:notebooks:artifacts-v11.0.0"
semantic_document_id: "kfm-arch-artifacts-notebooks"
event_source_id: "ledger:docs/analyses/archaeology/results/notebooks/artifacts/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Restricted / Notebook-Safe"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "provenience-reconstruction"
  - "identity-attribution"
  - "restricted cultural inference"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
classification: "Internal / CARE-Governed"
jurisdiction: "Kansas / United States"
role: "archaeology-artifacts-notebooks-root"
lifecycle_stage: "stable"
ttl_policy: "Review every 6 months"
sunset_policy: "Superseded when new notebook framework adopted"
---

<div align="center">

# 📓🏺 **Artifact Analysis Notebooks — Results Index**  
`docs/analyses/archaeology/results/notebooks/artifacts/README.md`

**Purpose:**  
Provide a **centralized index** of all **artifact-focused analysis notebooks** (ceramics, lithics, faunal, metals, clustering, spatial distributions, temporal analyses) produced in the Kansas Frontier Matrix (KFM).  
These notebooks contain **intermediate analytical steps**, **visualizations**, **quality checks**, and **FAIR+CARE–filtered derivations**, feeding final artifact results.

</div>

---

## 📘 Overview

Artifact analysis notebooks:

- execute **controlled, reproducible workflows**  
- produce **intermediate diagnostic plots**, **tables**, and **exported layers**  
- implement **sensitivity masking** (H3 r7+) at notebook runtime  
- generate **uncertainty and proxy disagreement summaries**  
- document pipeline logic for **transparency and reproducibility**  
- never expose restricted or sensitive data  
- contribute inputs to Story Nodes, Focus Mode, and final result layers  

All notebooks must comply with:

- MCP-DL v6.3  
- KFM-MDP v11  
- FAIR+CARE cultural-safety rules  
- AI governance (no speculative model outputs)  
- full PROV-O lineage export  

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/results/notebooks/artifacts/
├── README.md                       # This file
├── ceramics/                       # Ceramic-analysis notebooks (PD-only)
├── lithics/                        # Lithic reduction + material-group notebooks
├── faunal/                         # Faunal ecological-group notebooks (PD-only)
├── metals/                         # Metallurgical / elemental-analysis notebooks
├── clustering/                     # PCA/UMAP + clustering workflows
├── spatial-distributions/          # H3 generalized distribution modeling notebooks
├── temporal/                       # OWL-Time aligned artifact temporal notebooks
├── composite/                      # Multi-material cross-domain analysis notebooks
├── qa/                             # Quality assurance notebooks (lineage, masking, variance)
└── exports/                        # Outputs: plots, tables, JSON-LD summaries
~~~

---

## 🧪 Notebook Categories

### **1️⃣ Ceramic Analysis Notebooks (`ceramics/`)**
Contain:

- PD-safe typology batches  
- compositional PCA (public-domain only)  
- motif clusters (generalized)  
- distribution diagnostics  

---

### **2️⃣ Lithic Analysis Notebooks (`lithics/`)**
Include:

- reduction-sequence summaries  
- debitage size distributions  
- material grouping PCA  
- H3 distribution visualizations  

---

### **3️⃣ Faunal Notebooks (`faunal/`)**
Provide:

- eco-functional category summaries  
- skeletal-element distribution QC  
- PD-only faunal analyses  

No sensitive species allowed.

---

### **4️⃣ Metal Analysis Notebooks (`metals/`)**
Cover:

- PD-safe elemental spectra  
- alloy grouping runs  
- corrosion-environment modeling  

---

### **5️⃣ Clustering Notebooks (`clustering/`)**
Support:

- PCA / UMAP notebooks  
- k-means / hierarchical clustering  
- silhouette / cluster-stability QC  

---

### **6️⃣ Spatial Distribution Notebooks (`spatial-distributions/`)**
Generate:

- H3 r7+ distributions  
- KDE smoothing checks  
- eco-hydrological overlays  

---

### **7️⃣ Temporal Notebooks (`temporal/`)**
Provide:

- OWL-Time alignment  
- cross-period artifact tendencies  
- uncertainty across temporal windows  

---

### **8️⃣ Composite Notebooks (`composite/`)**
Used for:

- multi-material comparison  
- cross-domain correlation  
- combined uncertainty panels  

---

### **9️⃣ QA Notebooks (`qa/`)**
Perform:

- masking-verification  
- generalization integrity checks  
- uncertainty aggregation audits  
- PROV-O lineage testing  

---

## 🧬 Provenance & Metadata Integration

Each notebook must export:

- `prov:Bundle` lineage JSON-LD  
- STAC-compatible metadata for derived layers  
- DCAT dataset descriptors  
- uncertainty & sensitivity chips  
- model parameters (seed, config hash, environment snapshot)  

All exports feed the final results directories.

---

## 🧠 Focus Mode Integration

Notebooks feed:

- safe narrative context blocks  
- pattern explanations backed by environmental drivers  
- artifact summaries included in Story Node scaffolding  
- uncertainty chips used in map/timeline overlays  

Example Focus Summary:

> **Focus Summary:**  
> Notebook-derived artifact analyses contribute generalized distributions, material summaries, and uncertainty layers used for safe narrative reasoning in Focus Mode.

---

## 🛡 CARE & Ethical Requirements

All notebooks must:

- avoid culturally sensitive material  
- never include restricted provenience or sacred artifacts  
- enforce H3 r7+ generalization at export  
- transparently annotate uncertainty  
- pass CARE review before publication  

---

## 🕰️ Version History

| Version | Date       | Author                                   | Summary |
|--------:|------------|------------------------------------------|---------|
| v11.0.0 | 2025-11-17 | Archaeology WG · FAIR+CARE Council        | Initial notebook index under KFM-MDP v11.0.0. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Artifact Analysis Notebooks · CARE-Governed · FAIR+CARE Certified  
MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Notebooks Index](../README.md)

</div>
