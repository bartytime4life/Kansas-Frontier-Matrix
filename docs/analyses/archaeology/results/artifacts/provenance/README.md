---
title: "📜🏺 Kansas Frontier Matrix — Artifact Results: Provenance Registry (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/artifacts/provenance/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly · Archaeology WG · Material Culture WG · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/archaeology-artifact-provenance-v1.json"
governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Provenance Registry"
intent: "archaeology-artifacts-provenance"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed / Provenance Sensitive"
sensitivity_level: "High"
public_exposure_risk: "Medium"
indigenous_rights_flag: true
data_steward: "Archaeology WG · FAIR+CARE Council"
risk_category: "Artifact Provenance Documentation"
redaction_required: true
provenance_chain:
  - "docs/analyses/archaeology/results/artifacts/provenance/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E7 Activity"
  schema_org: "Dataset"
  prov_o: "prov:Bundle"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"
json_schema_ref: "../../../../../../schemas/json/archaeology-artifact-provenance.schema.json"
shape_schema_ref: "../../../../../../schemas/shacl/archaeology-artifact-provenance-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:artifact:provenance-v11.0.0"
semantic_document_id: "kfm-arch-artifact-provenance"
event_source_id: "ledger:docs/analyses/archaeology/results/artifacts/provenance/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Restricted"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
ai_transform_prohibited:
  - "origin-reconstruction"
  - "provenience-guessing"
  - "cultural-identity-attribution"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Internal / CARE-Governed"
role: "archaeology-artifacts-provenance-root"
lifecycle_stage: "stable"
ttl_policy: "Review every 6 months"
sunset_policy: "Superseded upon next provenance rules update"
---

<div align="center">

# 📜🏺 **Artifact Results — Provenance Registry**  
`docs/analyses/archaeology/results/artifacts/provenance/README.md`

**Purpose:**  
Establish the **complete PROV-O lineage system** for all artifact-based result datasets—ceramics, lithics, faunal, metals, clustering, distributions, environmental links, and temporal summaries—within the Kansas Frontier Matrix (KFM).  
This registry guarantees **scientific transparency**, **sovereignty protection**, **FAIR+CARE compliance**, and **verifiable reproducibility** for every transformation applied to artifact datasets.

</div>

---

## 📘 Overview

The artifact provenance registry documents:

- all input datasets used (public-domain only)  
- all transformations applied (cleaning, aggregation, H3 generalization, smoothing)  
- all modeling steps (PCA, clustering, KDE, typology, petrography, etc.)  
- all environmental-link transformations  
- uncertainty propagation  
- access-level and CARE-governed redaction steps  
- WAL → Retry → Rollback lineage operations  
- STAC/DCAT/PROV crosswalk harmonization  

This ensures:

- no sensitive provenience is ever disclosed  
- artifact analyses remain culturally safe  
- analysts and downstream systems can trace all outputs with full accountability  
- Focus Mode only accesses narrative-safe lineage data  

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/results/artifacts/provenance/
├── README.md                                   # This file
├── ceramics/                                   # Provenance bundles for ceramic analyses
│   ├── typology/
│   ├── petrography/
│   ├── distribution/
│   └── temporal/
├── lithics/                                    # Lithic analysis provenance bundles
│   ├── material/
│   ├── reduction/
│   ├── distribution/
│   └── temporal/
├── faunal/                                     # Faunal analysis provenance bundles
│   ├── taxonomy/
│   ├── skeletal-elements/
│   ├── distribution/
│   └── temporal/
├── metals/                                     # Metallurgical analyses provenance bundles
│   ├── composition/
│   ├── alloys/
│   ├── distribution/
│   └── temporal/
├── clustering/                                 # PCA, UMAP, k-means, hierarchical clustering
│   ├── material/
│   ├── typology/
│   ├── distribution/
│   └── environmental-links/
├── environmental-links/                        # Hydrology/soil/vegetation/terrain correlations
├── distributions/                              # H3 generalized distribution lineage
├── stac/                                       # STAC → PROV crosswalk bundles
├── metadata/                                   # DCAT → PROV crosswalk bundles
├── uncertainty/                                # Uncertainty propagation tracking
│   ├── ceramics/
│   ├── lithics/
│   ├── faunal/
│   ├── metals/
│   └── clustering/
└── lineage-bundles/                            # Final PROV-O JSON-LD bundles
    ├── ceramics-prov.jsonld
    ├── lithics-prov.jsonld
    ├── faunal-prov.jsonld
    ├── metals-prov.jsonld
    └── clustering-prov.jsonld
~~~

---

## 🧩 Required Provenance Components

### **1️⃣ PROV-O Core Entities**
Each artifact result must define:

- `prov:Entity` — the derived dataset  
- `prov:Activity` — processing, modeling, transformation steps  
- `prov:Agent` — KFM pipeline, reviewers, lineage systems (role-only, no personal identifiers)  

### **2️⃣ Input Dataset Documentation**
Must record:

- artifact inventories (PD-only)  
- typology/attribute data  
- geochemistry (public-domain only)  
- safe faunal data  
- environmental layers used in correlations  

### **3️⃣ Transformation Tracking**
Including:

- H3 generalization  
- spatial redaction  
- KDE smoothing  
- PCA/UMAP dimensionality reduction  
- k-means / hierarchical clustering  
- petrography workflow operations  
- lithic reduction-sequence modeling  
- environmental correlation modeling  

### **4️⃣ Environmental & Predictive Modeling Lineage**
For derived layers:

- hydrology/soils/vegetation/terrain links  
- predictive environmental or cluster-affordance models  
- uncertainty & proxy-weight lineage  

### **5️⃣ Uncertainty Propagation**
Tracked for:

- classification variance  
- distribution variance  
- compositional uncertainty  
- interpretation uncertainty  

### **6️⃣ Generalization & Redaction Steps**
All provenance must log:

- H3-level used (min r7)  
- redaction decisions  
- sovereignty protections applied  
- masking of culturally sensitive data (automatic & manual)  

### **7️⃣ WAL → Retry → Rollback Lineage**
Every pipeline pass must retain:

- WAL checkpoints  
- retry histories  
- rollback snapshots  
- execution environment hashes  

---

## 🧠 Focus Mode Integration

Provenance supports:

- narrative-safe justification chips  
- dataset origin transparency  
- environmental vs artifact distinction  
- uncertainty insights  
- avoidance of interpretive drift  

Example Focus Summary:

> **Focus Summary:**  
> Artifact provenance documents all dataset sources, transformations, and generalization steps that support these generalized results. All lineage has passed FAIR+CARE and sovereignty review.

---

## 🛡 CARE & Ethical Requirements

All artifact provenance must:

- protect culturally sensitive or restricted data  
- avoid reverse inference of provenience  
- avoid identity-linked lineage descriptions  
- disclose all redaction/generalization stages  
- document sovereignty-based access rules  
- undergo FAIR+CARE Council review  

If provenance exposes sensitive pathways → dataset must be masked or removed.

---

## 🧪 Validation

Stored in the parent metadata validation system:

- JSON Schema validation  
- SHACL graph validation  
- H3 integrity checks  
- CARE classification consistency  
- lineage completeness  
- crosswalk consistency (STAC ↔ DCAT ↔ PROV)  

---

## 🕰️ Version History

| Version | Date       | Author                                   | Summary |
|--------:|------------|------------------------------------------|---------|
| v11.0.0 | 2025-11-17 | Archaeology WG · FAIR+CARE Council        | Initial artifact provenance registry under KFM-MDP v11.0.0. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Artifact Provenance Registry · CARE-Governed · FAIR+CARE Certified  
MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Artifact Results](../README.md)

</div>
