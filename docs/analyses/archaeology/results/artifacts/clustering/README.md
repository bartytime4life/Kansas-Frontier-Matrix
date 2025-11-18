---
title: "🧩🏺 Kansas Frontier Matrix — Artifact Results: Clustering Analyses (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/artifacts/clustering/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly / Archaeology WG · Material Analysis WG · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/archaeology-artifact-clustering-results-v1.json"
governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Artifact Analysis Results"
intent: "archaeology-artifacts-clustering-results"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed / Generalized Cluster Modeling"
sensitivity_level: "High"
public_exposure_risk: "Medium"
indigenous_rights_flag: true
data_steward: "Archaeology WG · FAIR+CARE Council"
risk_category: "Pattern Recognition (Generalized)"
redaction_required: true
provenance_chain:
  - "docs/analyses/archaeology/results/artifacts/clustering/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E22 Man-Made Object"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"
  owl_time: "TemporalEntity"
json_schema_ref: "../../../../../../schemas/json/archaeology-artifact-clustering-results.schema.json"
shape_schema_ref: "../../../../../../schemas/shacl/archaeology-artifact-clustering-results-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:artifact:clustering-results-v11.0.0"
semantic_document_id: "kfm-arch-artifact-clustering-results"
event_source_id: "ledger:docs/analyses/archaeology/results/artifacts/clustering/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Restricted"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "pattern-description"
ai_transform_prohibited:
  - "tribal-identity-inference"
  - "cultural-unit-assignment"
  - "site-level pattern reconstruction"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Internal / CARE-Governed"
role: "archaeology-artifacts-clustering-root"
lifecycle_stage: "stable"
ttl_policy: "Review every 6 months"
sunset_policy: "Superseded upon next clustering-analysis update"
---

<div align="center">

# 🧩🏺 **Artifact Results — Clustering Analyses**  
`docs/analyses/archaeology/results/artifacts/clustering/README.md`

**Purpose:**  
Provide a **FAIR+CARE–aligned**, sovereignty-safe, scientifically grounded registry of **artifact clustering analyses** used in archaeological interpretation across the Kansas Frontier Matrix (KFM).  
These analyses identify **generalized, environmental, and material-based artifact clusters**—never cultural identities, exact locations, or restricted archaeological information.

</div>

---

## 📘 Overview

Artifact clustering analyses in the KFM describe:

- generalized pattern groupings of public-domain artifact attributes  
- cross-material cluster relationships (ceramics, lithics, faunal PD datasets)  
- environmental or spatial co-occurrence (generalized via H3 r7+)  
- material-composition similarity (PCA, k-means, hierarchical clustering)  
- distributional surface smoothing (KDE)  
- explainability overlays for cluster drivers (optional SHAP)  

These clusters are **analytical abstractions**, not:

- cultural communities  
- tribal identities  
- political/territorial groupings  
- sacred or restricted clusters  
- excavation or provenience reconstructions  

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/results/artifacts/clustering/
├── README.md                                  # This file
├── material/                                  # Composition & material-based clusters
├── typology/                                  # Typology & motif-based clusters (generalized)
├── distribution/                              # H3 spatial distribution clustering
├── environmental-links/                       # Hydrology/soil/vegetation cluster correlations
├── pca-reductions/                            # PCA/UMAP dimensionality reductions
├── temporal/                                  # Time-aware clustering (OWL-Time)
├── uncertainty/                               # Uncertainty & stability metrics
├── stac/                                      # STAC Items for clustering-based layers
├── metadata/                                  # DCAT + JSON-LD metadata
└── provenance/                                 # PROV-O lineage for cluster modeling steps
~~~

---

## 🧱 Cluster Types

### **1️⃣ Material-Based Clusters (`material/`)**
Include:

- geochemical composition groupings (PD datasets only)  
- mineral inclusion clusters  
- PCA/UMAP material subgroups  
- k-means or hierarchical cluster categories  

All sensitive or culturally restricted materials are excluded.

---

### **2️⃣ Typological Clusters (`typology/`)**
Generalized clusters of:

- decorative motifs  
- vessel/body shapes  
- surface-treatment categories  

No restricted iconography or culturally sensitive symbolism included.

---

### **3️⃣ Spatial Distribution Clusters (`distribution/`)**
Contain:

- H3 r7+ generalized spatial cluster envelopes  
- KDE smoothing of artifact density  
- spatial co-occurrence groupings  

No site-level distribution or provenience is represented.

---

### **4️⃣ Environmental Correlation Clusters (`environmental-links/`)**
Describe:

- hydrology-linked artifact groupings  
- soil/vegetation/terrain correlation clusters  
- climate-driven distribution tendencies  

These are environmental, not cultural interpretations.

---

### **5️⃣ Dimensionality Reduction Outputs (`pca-reductions/`)**
Include:

- PCA component plots  
- UMAP embeddings  
- variance explanations  
- cluster separation summaries  

All minimized to public-domain artifact datasets.

---

### **6️⃣ Temporal Clusters (`temporal/`)**
Generalized OWL-Time aligned:

- broad artifact temporal windows  
- cluster persistence/attenuation  
- multi-period comparisons  

Never represent cultural timelines.

---

## ⚠️ Uncertainty Layers (`uncertainty/`)

Store:

- cluster stability metrics  
- silhouette scores  
- proxy disagreement  
- environmental variance  

Shown in Focus Mode as **Cluster Confidence Chips**.

---

## 🧬 Metadata & Provenance

### **STAC (`stac/`)**
Artifact-cluster STAC Items must include:

- H3-generalized geometries  
- cluster metrics  
- uncertainty layers  
- environmental-driver metadata  
- lineage bundles  

### **DCAT (`metadata/`)**
Contain:

- dataset scope  
- cluster methodology  
- CARE governance  
- distribution metadata  

### **PROV-O (`provenance/`)**
Track:

- source datasets  
- methods (PCA, k-means, H3 aggregation)  
- smoothing & transformation  
- generalization steps  
- uncertainty propagation  
- WAL → Retry → Rollback lineage  

---

## 🧠 Focus Mode Integration

Clustering results enhance:

- Story Node v3 material-culture context  
- Focus Mode’s pattern-explanation overlays  
- environmental + artifact co-pattern summaries  
- multi-domain correlation narratives  

Example Focus Summary:

> **Focus Summary:**  
> Artifact clustering identifies broad material and environmental pattern groups across Kansas. These cluster envelopes are fully generalized, public-domain, and CARE-reviewed—without implying cultural identity or precise locations.

---

## 🛡 CARE & Ethical Requirements

All artifact-clustering results must:

- avoid cultural or tribal identity inference  
- avoid reconstructing provenance  
- avoid restricted materials  
- apply H3 r7+ masking  
- disclose uncertainty  
- follow FAIR+CARE + sovereignty review  

If clustering suggests culturally sensitive interpretations → it must be masked or removed.

---

## 🕰️ Version History

| Version | Date       | Author                                      | Summary |
|--------:|------------|---------------------------------------------|---------|
| v11.0.0 | 2025-11-17 | Archaeology WG · FAIR+CARE Council          | Initial artifact clustering results registry under KFM-MDP v11.0.0. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Artifact Clustering Results · CARE-Governed · FAIR+CARE Certified  
MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Artifact Results](../README.md)

</div>