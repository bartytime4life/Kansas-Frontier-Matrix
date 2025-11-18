---
title: "📜 Kansas Frontier Matrix: Late Prehistoric H3 Provenance & Lineage (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/provenance/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly / Archaeology Working Group · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../schemas/telemetry/archaeology-site-distribution-clusters-late-prehistoric-h3-provenance-v1.json"
governance_ref: "../../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Provenance"
intent: "archaeology-late-prehistoric-h3-provenance"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed"
sensitivity_level: "Medium"
public_exposure_risk: "Medium"
indigenous_rights_flag: true
data_steward: "Archaeology Working Group · FAIR+CARE Council"
risk_category: "Lineage & Provenance"
redaction_required: true
provenance_chain:
  - "docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/provenance/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E7 Activity"
  schema_org: "Dataset"
  prov_o: "prov:Activity"
  geosparql: "geo:FeatureCollection"
json_schema_ref: "../../../../../../../../../schemas/json/archaeology-site-distribution-clusters-late-prehistoric-h3-provenance.schema.json"
shape_schema_ref: "../../../../../../../../../schemas/shacl/archaeology-site-distribution-clusters-late-prehistoric-h3-provenance-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:results:late-prehistoric-h3-provenance-v11.0.0"
semantic_document_id: "kfm-arch-results-late-prehistoric-h3-provenance"
event_source_id: "ledger:docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/provenance/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
ai_transform_prohibited:
  - "speculative-additions"
  - "fabricated-lineage"
  - "unverified-inference"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Public / Provenance"
role: "archaeology-results-late-prehistoric-h3-provenance"
lifecycle_stage: "stable"
ttl_policy: "Review every 12 months"
sunset_policy: "Superseded upon next provenance revision"
---

<div align="center">

# 📜 **Kansas Frontier Matrix — Late Prehistoric H3 Provenance & Lineage**  
`docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/provenance/README.md`

**Purpose:**  
Document the **full PROV-O lineage**, transformation steps, modeling workflows, redaction decisions, and CARE-governed modifications applied during the creation of **Late Prehistoric H3 generalized cluster layers**.

![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Certified-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![Docs](https://img.shields.io/badge/Docs·MCP_v6.3-blue)

</div>

---

## 📘 Overview

This provenance module provides a **complete, auditable history** of:

- Input datasets  
- Transformations performed  
- Modeling activities  
- Generalization steps  
- CARE-driven redactions  
- STAC/DCAT lineage integration  
- WAL → Retry → Rollback lineage safety  

All Late Prehistoric H3 layers must maintain **verifiable, machine-readable provenance**.

---

## 🗂️ Directory Layout

```text
docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/provenance/
├── README.md                       # This file
├── transformations-log.csv         # Ordered list of all H3 modeling steps
├── lineage.csv                     # High-level PROV-O lineage summary
├── prov_graph.json                 # PROV-O graph encoding of modeling process
├── activity_records/               # Detailed per-step PROV-O JSON-LD
├── inputs/                         # Generalized site inputs + filtered datasets
├── care/                           # CARE-driven redaction logs & explanations
└── validation/                     # Provenance validation reports (schema/SHACL)
````

---

## 🧬 Provenance Model (PROV-O)

Late Prehistoric H3 lineage follows PROV-O structure:

### **Entities (`prov:Entity`)**

* Generalized archaeological points
* H3 r7/r8 hex layers
* KDE & smoothing rasters
* Metadata artifacts (DCAT, STAC)

### **Activities (`prov:Activity`)**

* Generalization
* H3 encoding
* KDE smoothing
* Spatial autocorrelation validation
* CARE review + redaction
* Output packaging & STAC generation

### **Agents (`prov:Agent`)**

* Archaeology Working Group
* FAIR+CARE Council
* Tribal review representatives
* KFM automated pipelines

---

## 🔧 Transformation Steps (summarized)

Each step appears in **transformations-log.csv** and is preserved in STAC lineage.

### 1️⃣ Input Preparation

* Sensitive site coordinates generalized and masked
* Survey bias handled via spatial thinning where required

### 2️⃣ H3 Generalization

* r7 (public-safe) / r8 (context-safe)
* Cells created using centroid or boundary geometry

### 3️⃣ KDE Smoothing

* Density surfaces calculated
* Values normalized across eco-regions

### 4️⃣ Spatial Validation

* Moran’s I on weighted hex distributions
* ENS (effective neighborhood size) checks

### 5️⃣ CARE Review

* Sensitive cells collapsed or replaced with coarse H3 aggregations
* Public version created

### 6️⃣ Packaging & Lineage Export

* STAC Item creation
* DCAT metadata export
* PROV graph generation

---

## 🧭 CARE-Driven Redactions

All redactions must be:

* Logged in `care/`
* Referenced in PROV-O via `prov:invalidated` or `prov:wasDerivedFrom`
* Reflected in STAC `care:sensitivity` fields
* Reviewed by tribal partners and FAIR+CARE Council

Redaction categories:

* **R1** — Mask individual sensitive cells
* **R2** — Collapse region into coarser H3 level
* **R3** — Remove/omit region entirely from public layer

---

## 🛰 STAC/DCAT Lineage Integration

Every H3 layer MUST contain:

* `prov:wasGeneratedBy` referencing a modeling activity
* `prov:used` listing environmental/cultural datasets
* H3 resolution parameters in STAC `properties` fields
* CARE sensitivity flags
* Links to corresponding DCAT metadata in `metadata/`

---

## 🧠 Focus Mode Integration

Focus Mode v3 relies on provenance to:

* Display modeling + redaction steps
* Generate explainability narratives
* Provide context for why certain areas are masked or collapsed
* Surface uncertainties and CARE considerations

Example Focus Note:

> **Focus Summary:**
> These H3 clusters were generated through a multi-step workflow involving generalization, KDE smoothing, and cultural stewardship review.
> Several cells were redacted or collapsed into coarse regions per tribal governance protocols.

---

## 📜 Required Provenance Files

### `transformations-log.csv`

Chronological log of modeling stages, with:

* step_id
* activity
* input_entities
* output_entities
* tool/script
* operator / agent
* CARE flags
* QA status

### `lineage.csv`

Simplified, human-readable lineage table.

### `prov_graph.json`

Formal PROV-O graph encoded in JSON-LD.

### `activity_records/`

Directory of fine-grained PROV-O records per modeling step.

### `inputs/`

Generalized inputs used to generate H3 layers.

### `care/`

Details on cultural review and redaction decisions.

---

## 🕰️ Version History

| Version | Date       | Author                             | Summary                                                          |
| ------: | ---------- | ---------------------------------- | ---------------------------------------------------------------- |
| v11.0.0 | 2025-11-17 | FAIR+CARE Council · Archaeology WG | Initial full provenance record for Late Prehistoric H3 clusters. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0
Provenance & Lineage · CARE-Governed · FAIR+CARE Certified
MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

[Back to Metadata](../metadata/README.md) · [Back to H3 Directory](../../README.md)

</div>
