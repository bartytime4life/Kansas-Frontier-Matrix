---
title: "📍 Kansas Frontier Matrix: Archaeology Site Distribution Results (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/site-distributions/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly / Archaeology Working Group · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/archaeology-site-distributions-v1.json"
governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Results"
intent: "archaeology-site-distributions"
fair_category: "F1-A1-I1-R1"
care_label: "Public / CARE-Governed"
sensitivity_level: "Medium"
public_exposure_risk: "Medium"
indigenous_rights_flag: true
data_steward: "Archaeology Working Group · FAIR+CARE Council"
risk_category: "Spatial Results"
redaction_required: true
provenance_chain:
  - "docs/analyses/archaeology/results/site-distributions/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E31 Document"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"
json_schema_ref: "../../../../../../schemas/json/archaeology-site-distributions.schema.json"
shape_schema_ref: "../../../../../../schemas/shacl/archaeology-site-distributions-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:results:site-distributions-v11.0.0"
semantic_document_id: "kfm-archaeology-results-site-distributions"
event_source_id: "ledger:docs/analyses/archaeology/results/site-distributions/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "timeline-generation"
ai_transform_prohibited:
  - "speculative-additions"
  - "unverified-historical-claims"
  - "re-attribution-of-cultural-ownership"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Public / Results"
role: "archaeology-results-site-distributions"
lifecycle_stage: "stable"
ttl_policy: "Review every 12 months"
sunset_policy: "Superseded upon next major archaeology results update"
---

<div align="center">

# 📍 **Kansas Frontier Matrix — Archaeology Site Distribution Results**  
`docs/analyses/archaeology/results/site-distributions/README.md`

**Purpose:**  
Provide the authoritative summary of **archaeology site distribution analyses** within the Kansas Frontier Matrix (KFM), including generalized settlement clusters, occupation densities, interaction zones, and CARE-governed spatial redactions.

![Docs](https://img.shields.io/badge/Docs·MCP_v6.3-blue)
![License](https://img.shields.io/badge/License-CC--BY--4.0-green)
![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Certified-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

</div>

---

## 📘 Overview

The **site distributions** module documents archaeological site clustering, spatial patterning, and cultural geography across Kansas.

All results follow:

- **FAIR+CARE governance**  
- **CIDOC-CRM + GeoSPARQL alignment**  
- **STAC/DCAT dataset registration**  
- **Generalization of sensitive geometries** (H3 r7/r8 or 1–5 km buffers)  
- **WAL → Retry → Rollback → Lineage** safety & reproducibility model  
- **Focus Mode v3 narrative compatibility**

This directory provides **public-safe**, ethically governed outputs derived from internal analyses.

---

## 🗂️ Directory Layout

```text
docs/analyses/archaeology/results/site-distributions/
├── README.md                         # This file
├── clusters/                         # Generalized cluster outputs
│   ├── late-prehistoric/             # Example cluster sets
│   ├── protohistoric/                # Wichita/Great Bend distributions
│   └── historic/                     # 19th-century archaeological distributions
├── heatmaps/                         # KDE + density maps (generalized)
├── stac/                             # STAC Items for each result surface
├── metadata/                         # DCAT + lineage metadata
└── provenance/                       # PROV-O activity logs, transformations logs
````

Supporting pipeline code:

```text
src/pipelines/archaeology/site_distributions/
data/work/archaeology/site_distributions/
```

---

## 🧭 Interpretation Guidelines

### 1️⃣ Generalized Outputs Only

All public KFM site distribution layers are **generalized**:

* H3 hexagons
* 1–5 km buffers
* Raster smoothing
* Removed or jittered coordinates

This enforces **CARE sovereignty protections** and prevents misuse.

### 2️⃣ Contextual, Not Deterministic

Site distribution layers describe **patterns**, not absolute truths:

* Settlement intensity
* Cultural influence regions
* Occupation-era spatial dynamics
* Correlation with hydrology, soils, climate

They **cannot** be used to infer precise locations of archaeological sites.

### 3️⃣ Cultural Safety Rules

* Sensitive site clusters are **collapsed to higher-order regions**
* Tribal partners may request suppression of specific areas
* No high-resolution or identifying geometries are included
* Focus Mode must include **CARE warnings** when rendering clusters

---

## 📊 Methods Summary

### Spatial Analyses

(See `../methods/spatial_analysis.md`)

* GeoSPARQL topological relationships
* Buffering and overlay
* River & hydrology proximity
* Least-cost path modeling
* Viewshed & terrain affordance modeling

### Statistical Analyses

(See `../methods/proximity_statistics.md`)

* KDE density surfaces
* Spatial autocorrelation (Moran’s I)
* Permutation tests
* Confidence/uncertainty surfaces

### Predictive Modeling

(See `../methods/predictive_modeling.md`)

* GLMs & GAMs
* Random forest/boosted models
* Interaction sphere corridor modeling
* H3 coarse generalization for public outputs

---

## 🛰 STAC/DCAT Metadata

All outputs are registered as **STAC Items** and **DCAT Datasets**.

Example:

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "kfm-site-distributions-protohistoric-v1",
  "bbox": [-102.0, 37.0, -94.6, 40.0],
  "properties": {
    "kfm:domain": "archaeology",
    "kfm:analysis": "site-distribution",
    "care:sensitivity": "generalized"
  },
  "assets": {
    "raster": {
      "href": "s3://kfm/archaeology/site_distributions/protohistoric_kde_v1.tif",
      "roles": ["data"]
    }
  }
}
```

---

## 🧠 Focus Mode Integration

Site distribution layers appear in Focus Mode v3 as:

* **Context overlays**
* **Cluster explanation cards**
* **Settlement density summaries**
* **Hydrology & environmental narrative hooks**

Focus Mode must:

* Show provenance chips
* Warn about generalization & CARE constraints
* Distinguish model-based layers from verified historical data

Example Focus Summary:

> **Focus Summary:**
> Protohistoric settlement intensity increases along major tributaries into the Arkansas River basin.
> These results are generalized and serve as interpretive context, not precise site indicators.

---

## 🧬 Provenance & Lineage

All site distribution outputs must include:

* PROV-O modeling activities
* Input dataset references
* Versioning and transformations
* WAL checkpoints and rollback restoration paths
* Full lineage recorded in:

  * `provenance/transformations-log.csv`
  * Neo4j provenance graph
  * STAC Item `wasGeneratedBy` fields

---

## 🕰️ Version History

| Version | Date       | Author                                        | Summary                                                                                     |
| ------: | ---------- | --------------------------------------------- | ------------------------------------------------------------------------------------------- |
| v11.0.0 | 2025-11-17 | Archaeology Working Group · FAIR+CARE Council | Upgraded to KFM-MDP v11; added ontology alignment, CARE constraints, STAC/DCAT integration. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0
FAIR+CARE Certified · MCP-DL v6.3 Compatible · Diamond⁹ Ω / Crown∞Ω Ultimate Certified
Spatial Results (Generalized · Public-Safe)

</div>
