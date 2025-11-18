---
title: "🏺 Kansas Frontier Matrix: Archaeology Methods Framework (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/methods/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly / Archaeology Working Group · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/analyses-archaeology-methods-v2.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Methods"
intent: "archaeology-methods-index"
fair_category: "F1-A1-I1-R1"
care_label: "Public / CARE-Governed"
sensitivity_level: "Medium"
public_exposure_risk: "Medium"
indigenous_rights_flag: true
data_steward: "Archaeology Working Group · FAIR+CARE Council"
risk_category: "Methods"
redaction_required: false
provenance_chain:
  - "docs/analyses/archaeology/methods/README.md@v10.1.0"
  - "docs/analyses/archaeology/methods/README.md@v10.0.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "CreativeWork"
  prov_o: "prov:Plan"
  owl_time: "TemporalEntity"
json_schema_ref: "../../../../../schemas/json/archaeology-methods-index.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/archaeology-methods-index-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:methods:index-v11.0.0"
semantic_document_id: "kfm-archaeology-methods-index"
event_source_id: "ledger:docs/analyses/archaeology/methods/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "timeline-generation"
  - "3d-context-render"
ai_transform_prohibited:
  - "speculative-additions"
  - "unverified-historical-claims"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Public / Methods"
role: "archaeology-methods-root"
lifecycle_stage: "stable"
ttl_policy: "Review every 12 months"
sunset_policy: "Superseded when next major v11.x archaeology methods revision is released"
---

<div align="center">

# 🏺 **Kansas Frontier Matrix — Archaeology Methods Framework**  
`docs/analyses/archaeology/methods/README.md`

**Purpose:**  
Define the **complete methodological ecosystem** for archaeology within the Kansas Frontier Matrix (KFM), covering:  
- spatial, temporal, and environmental correlation workflows  
- predictive modeling and interaction-sphere analytics  
- uncertainty, provenance, and ethical constraints  
- Story Node v3 + Focus Mode v3 integration  
- FAIR+CARE–aligned archaeological interpretation rules  

![Docs](https://img.shields.io/badge/Docs·MCP_v6.3-blue)
![License](https://img.shields.io/badge/License-CC--BY--4.0-green)
![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Certified-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

</div>

---

## 📘 Overview

The Archaeology Methods Framework defines **how archaeological analyses are structured, validated, documented, and governed** inside the Kansas Frontier Matrix.

This includes:

- Multiscale spatial correlation  
- Temporal alignment using OWL-Time  
- Hydrology- and climate-linked contextualization  
- Cultural landscape interaction modeling  
- Uncertainty propagation and provenance logging  
- Full integration with **Neo4j (CIDOC-CRM, PROV-O, GeoSPARQL)**  
- Support for **Story Node v3** and **Focus Mode v3** narrative generation  

All workflows must follow:

- **MCP-DL v6.3** (documentation-first, deterministic pipelines)  
- **KFM-MDP v11.0.0** (metadata + structure rules)  
- **FAIR+CARE cultural ethics** (generalization, sovereignty, consent)  
- **Governance-as-code** (validation → ledger → ingestion)

---

## 🗂️ Directory Layout

```text
docs/analyses/archaeology/methods/
├── README.md                      # This file
├── temporal_alignment.md          # OWL-Time based interval alignment & uncertainty models
├── spatial_analysis.md            # GeoSPARQL spatial correlation workflows
├── proximity_statistics.md        # KDE, enrichment tests, Monte Carlo permutations
├── predictive_modeling.md         # ML, GLM, heuristic settlement likelihood modeling
└── validation/
    └── README.md                  # Archaeology validation framework (Tier 1/2/3 checks)
````

Corresponding pipeline implementations:

```text
src/pipelines/archaeology/
    ├── spatial/
    ├── temporal/
    ├── predictive_modeling/
    └── validation/
```

---

## 🧱 Method Categories

### 1️⃣ Temporal Alignment (OWL-Time)

* Interval intersection + uncertainty bands
* Temporal clustering (occupation bands, cultural phases)
* Multi-source time normalization
* Provenance tracking for date ranges & precision

### 2️⃣ Spatial Analysis (GeoSPARQL)

* Overlay, buffer, and mask operations
* River-terrace + hydrology-linked analysis
* Viewshed and least-cost corridor modeling
* Integration with CIDOC-CRM `E53 Place` + PROV-O lineage

### 3️⃣ Proximity & Statistical Methods

* KDE surface creation
* Distance-based enrichment vs. randomized landscapes
* Monte Carlo permutation tests
* Error surfaces and uncertainty quantification

### 4️⃣ Predictive Modeling

* GLMs, GAMs, spatial point process models
* Random forest, gradient boosting
* Scenario & interaction-sphere modeling
* H3 generalization for public layers (CARE compliance)

---

## 🧭 FAIR+CARE Alignment

### FAIR

| Principle     | Implementation                         |
| ------------- | -------------------------------------- |
| Findable      | STAC/DCAT dataset registration         |
| Accessible    | CC-BY metadata; transparent lineage    |
| Interoperable | CIDOC-CRM · GeoSPARQL · OWL-Time       |
| Reusable      | Fully versioned workflows + SBOM links |

### CARE

| Principle            | Implementation                                     |
| -------------------- | -------------------------------------------------- |
| Collective Benefit   | Insights support education & heritage preservation |
| Authority to Control | Tribal partners govern sensitive site handling     |
| Responsibility       | Redaction, generalization, and cultural reviews    |
| Ethics               | Oversight by FAIR+CARE Council & governance hooks  |

---

## 🧩 Integration With Story Nodes & Focus Mode

* Story Nodes use outputs as **context surfaces**, not primary evidence
* Focus Mode v3 summarizes:

  * temporal alignment explanations
  * spatial affordance narratives
  * predictive layer caveats + uncertainty
* Every method includes:

  * provenance chips
  * CARE labels
  * narrative-safe summaries

Example Focus Summary block:

> **Focus Summary:**
> Archaeological sites cluster along terraces with stable hydrology.
> Temporal alignment suggests multi-century occupation continuity.
> These interpretations are probabilistic and CARE-governed.

---

## 🧪 Validation Rules (Tier 1/2/3)

### Tier 1 — Scientific & Statistical

* Parameter transparency
* Reproducibility
* Spatial/temporal correctness
* Uncertainty quantification

### Tier 2 — Cultural & Ethical (FAIR+CARE)

* H3 masking
* Sensitive site handling
* Cultural sovereignty review

### Tier 3 — Technical

* STAC/DCAT compliance
* Schema conformance
* Provenance completeness
* File + metadata layout checks

---

## 🕰️ Version History

| Version | Date       | Author                     | Summary                                                                                             |
| ------: | ---------- | -------------------------- | --------------------------------------------------------------------------------------------------- |
| v11.0.0 | 2025-11-17 | FAIR+CARE + Archaeology WG | Upgraded to KFM-MDP v11; added ontology alignment, CARE enhancements, predictive modeling linkages. |
| v10.1.0 | 2025-11-11 | FAIR+CARE Council          | Original correlation methods index.                                                                 |

---

<div align="center">

© 2025 Kansas Frontier Matrix · MCP-DL v6.3
**FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified**

[Back to Analyses Index](../../README.md) · [Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
