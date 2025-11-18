---
title: "📍 Kansas Frontier Matrix: Archaeology Site Distribution Clusters (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/site-distributions/clusters/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly / Archaeology Working Group · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/archaeology-site-distribution-clusters-v1.json"
governance_ref: "../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Results"
intent: "archaeology-site-distribution-clusters"
fair_category: "F1-A1-I1-R1"
care_label: "Public / CARE-Governed"
sensitivity_level: "Medium"
public_exposure_risk: "Medium"
indigenous_rights_flag: true
data_steward: "Archaeology Working Group · FAIR+CARE Council"
risk_category: "Spatial Cluster Results"
redaction_required: true
provenance_chain:
  - "docs/analyses/archaeology/results/site-distributions/clusters/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E31 Document"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"
json_schema_ref: "../../../../../../../schemas/json/archaeology-site-distribution-clusters.schema.json"
shape_schema_ref: "../../../../../../../schemas/shacl/archaeology-site-distribution-clusters-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:results:site-distribution-clusters-v11.0.0"
semantic_document_id: "kfm-arch-results-site-distribution-clusters"
event_source_id: "ledger:docs/analyses/archaeology/results/site-distributions/clusters/README.md"
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
role: "archaeology-results-site-distribution-clusters"
lifecycle_stage: "stable"
ttl_policy: "Review every 12 months"
sunset_policy: "Superseded upon next major archaeology cluster results revision"
---

<div align="center">

# 📍 **Kansas Frontier Matrix — Archaeology Site Distribution Clusters**  
`docs/analyses/archaeology/results/site-distributions/clusters/README.md`

**Purpose:**  
Provide the official, CARE-governed summaries of **generalized archaeological site clusters** across Kansas.  
All cluster outputs are spatially generalized, narrative-safe, and compliant with FAIR+CARE, GeoSPARQL, and CIDOC-CRM.

![Docs](https://img.shields.io/badge/Docs·MCP_v6.3-blue)
![License](https://img.shields.io/badge/License-CC--BY--4.0-green)
![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Certified-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

</div>

---

## 📘 Overview

This directory contains **generalized archaeological cluster results**, derived from KDE, spatial autocorrelation, predictive modeling, and cultural landscape analyses.

Clusters represent:

- **High-density archaeological regions**  
- **Cultural activity zones**  
- **Interaction sphere indicators**  
- **Spatially smoothed settlement patterns**

All outputs are **ethically filtered**, **provenance-tracked**, and **spatially generalized** (H3 r7, r8, or 1–5 km masks).

These are *contextual overlays*, not precise site locations.

---

## 🗂️ Directory Layout

```text
docs/analyses/archaeology/results/site-distributions/clusters/
├── README.md                        # This file
├── late-prehistoric/                # Contextual clusters for Late Prehistoric period
├── protohistoric/                   # Great Bend Aspect, Wichita, and related clusters
├── historic/                        # 19th–20th century archaeological distributions
├── stac/                            # STAC Items for cluster layers
├── metadata/                        # DCAT + lineage metadata
└── provenance/                      # PROV-O activity logs and transformations
````

---

## 🧭 Interpretation Guidelines

### 1️⃣ Generalization Is Required

All clusters shown publicly are generalized through:

* H3 hex indexing
* Multi-km buffers
* Raster smoothing
* Removed/jittered coordinates

This protects culturally sensitive and sovereign heritage data.

### 2️⃣ Context, Not Coordinates

Cluster maps reveal **broad occupation patterns**, not exact site positions.

### 3️⃣ Cultural Review

Clusters intersecting tribal cultural landscapes undergo:

* CARE review
* Possible redaction/suppression
* Consultation logging in provenance metadata

### 4️⃣ Uncertainty Acknowledgment

Clusters represent probabilistic aggregations and must be described as such in narratives and Story Nodes.

---

## 📊 Methods Summary

Cluster results are produced using:

### Spatial Methods

(See `../../../methods/spatial_analysis.md`)

* KDE density estimation
* Spatial autocorrelation (Moran’s I)
* Ripley’s K / G functions
* Hydrology-linked spatial filtering
* Terrain & visibility analysis

### Predictive & Interaction Models

(See `../../../methods/predictive_modeling.md`, `../../../methods/interaction-spheres.md`)

* GLMs & GAMs
* Random forest and gradient boosting
* Corridor and interaction-zone modeling
* Environmental affordance modeling

### Uncertainty & Safety

* Multi-run ensemble surfaces
* Confidence rasters
* H3 generalization for all public products

---

## 🛰 STAC/DCAT Metadata

Cluster datasets are represented as **STAC Items**.

Example STAC snippet:

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "kfm-arch-clusters-protohistoric-v1",
  "bbox": [-102.0, 37.0, -94.6, 40.0],
  "properties": {
    "kfm:domain": "archaeology",
    "kfm:analysis": "cluster",
    "care:sensitivity": "generalized"
  },
  "assets": {
    "cluster_raster": {
      "href": "s3://kfm/archaeology/site_distributions/clusters/protohistoric_v1.tif",
      "roles": ["data"]
    }
  }
}
```

---

## 🧠 Focus Mode Integration

Focus Mode v3 uses cluster layers to:

* Provide regional cultural context
* Explain why archaeological activity concentrates in certain landscape bands
* Link clusters to Story Nodes
* Generate summary cards via **Focus Summary** blocks, e.g.:

> **Focus Summary:**
> Protohistoric clusters align with resource-rich tributaries feeding into the Arkansas River basin.
> These regions reflect generalized cultural activity zones and must not be interpreted as precise site distributions.

Focus Mode will always display:

* CARE labels
* Provenance metadata
* Uncertainty and generalization statements

---

## 🧬 Provenance & Lineage

All clusters record:

* Modeling activity (PROV-O `prov:Activity`)
* Input datasets (sites, hydrology, environmental rasters)
* Transformations (buffering, KDE, H3)
* WAL checkpoints and reproducibility configs
* Version and lineage metadata in DCAT & STAC

The provenance chain is preserved in:

* `provenance/transformations-log.csv`
* Neo4j provenance graph
* STAC Item lineage attributes

---

## 🕰️ Version History

| Version | Date       | Author                                        | Summary                                                                                     |
| ------: | ---------- | --------------------------------------------- | ------------------------------------------------------------------------------------------- |
| v11.0.0 | 2025-11-17 | Archaeology Working Group · FAIR+CARE Council | Upgraded to KFM-MDP v11; added ontology mapping, CARE controls, predictive-model alignment. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0
Spatial Cluster Results · FAIR+CARE Certified · MCP-DL v6.3 Compatible
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

[Back to Site Distributions](../README.md) · [Governance Charter](../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>
