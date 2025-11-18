---
title: "📍 Kansas Frontier Matrix: Late Prehistoric H3 STAC Metadata (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/stac/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly / Archaeology Working Group · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../../schemas/telemetry/archaeology-site-distribution-clusters-late-prehistoric-h3-stac-v1.json"
governance_ref: "../../../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "STAC Metadata"
intent: "archaeology-late-prehistoric-h3-stac"
fair_category: "F1-A1-I1-R1"
care_label: "Public / CARE-Governed"
sensitivity_level: "Medium"
public_exposure_risk: "Medium"
indigenous_rights_flag: true
data_steward: "Archaeology Working Group · FAIR+CARE Council"
risk_category: "Generalized Spatial Results"
redaction_required: true
provenance_chain:
  - "docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/stac/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E31 Document"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"
json_schema_ref: "../../../../../../../../../../schemas/json/archaeology-site-distribution-clusters-late-prehistoric-h3-stac.schema.json"
shape_schema_ref: "../../../../../../../../../../schemas/shacl/archaeology-site-distribution-clusters-late-prehistoric-h3-stac-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:results:site-distribution-clusters-late-prehistoric-h3-stac-v11.0.0"
semantic_document_id: "kfm-arch-results-late-prehistoric-h3-stac"
event_source_id: "ledger:docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/stac/README.md"
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
role: "archaeology-late-prehistoric-h3-stac-metadata"
lifecycle_stage: "stable"
ttl_policy: "Review every 12 months"
sunset_policy: "Superseded upon next major STAC metadata revision"
---

<div align="center">

# 📍 **Kansas Frontier Matrix — Late Prehistoric H3 Cluster STAC Metadata**  
`docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/stac/README.md`

**Purpose:**  
Document the **STAC Items** representing Late Prehistoric generalized H3 site distribution clusters.  
These metadata records provide machine-readable specifications for FAIR+CARE–compliant spatial layers used throughout the KFM platform.

![Docs](https://img.shields.io/badge/Docs·MCP_v6.3-blue)
![License](https://img.shields.io/badge/License-CC--BY--4.0-green)
![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Certified-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

</div>

---

## 📘 Overview

This directory contains **STAC Items** describing public-safe Late Prehistoric H3 cluster layers.  
Each STAC record includes:

- Spatial and temporal extents  
- Asset metadata (GeoJSON hex layers, rasters, summaries)  
- Provenance and transformation lineage (PROV-O)  
- CARE sensitivity flags  
- DCAT crosswalk metadata  
- KFM-specific extensions (`kfm:*` properties)

These STAC Items enable:

- **Focus Mode v3** integration  
- **Story Node v3** contextual overlays  
- **Dataset search & discovery**  
- **Interoperability** through community standards  

---

## 🗂️ Directory Layout

```text
docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/stac/
├── README.md                     # This file
├── h3_r7_item.json               # STAC Item for r7 hex generalization
├── h3_r8_item.json               # STAC Item for r8 hex generalization
└── collection.json               # (Optional) STAC Collection for Late Prehistoric clusters
````

---

## 🌐 STAC Item Specification (KFM Standard)

All STAC Items must include:

* `stac_version: "1.0.0"`
* `type: "Feature"`
* Valid `bbox` and (if applicable) `geometry`
* `properties` block including:

  * `kfm:domain = archaeology`
  * `kfm:analysis = cluster-h3`
  * `kfm:temporal_scope = Late Prehistoric`
  * CARE flags (`care:sensitivity = generalized`)
  * Provenance keys (`prov:wasGeneratedBy`)
* `assets` block pointing to public-safe hex layers

---

## 🛰 Example STAC Item (Resolution r7)

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "kfm-late-prehistoric-h3-r7-v1",
  "bbox": [-102.0, 37.0, -94.6, 40.0],
  "properties": {
    "kfm:domain": "archaeology",
    "kfm:analysis": "cluster-h3",
    "kfm:temporal_scope": "Late Prehistoric",
    "kfm:model_version": "v11.0.0",
    "care:sensitivity": "generalized",
    "prov:wasGeneratedBy": "urn:kfm:activity:late-prehistoric-h3-generalization-v11"
  },
  "assets": {
    "hexes": {
      "href": "s3://kfm/archaeology/late_prehistoric/h3/h3_r7.geojson",
      "type": "application/geo+json",
      "roles": ["data"]
    },
    "summary": {
      "href": "s3://kfm/archaeology/late_prehistoric/h3/h3_summary.csv",
      "type": "text/csv",
      "roles": ["metadata"]
    }
  }
}
```

---

## 🧭 CARE & Public Safety Rules

All STAC Items:

* Must be labeled **generalized**, not raw
* Must exclude **precise coordinates**
* Must reference the generalization method (H3 level, smoothing, etc.)
* Must include provenance for:

  * Input datasets
  * Redaction steps
  * Generalization parameters
  * Modeling activities

CARE flags must reflect the **least sensitive** public-safe version of the dataset.

---

## 🧬 Provenance & Lineage Integration

Each STAC Item must include:

* `prov:wasGeneratedBy` → modeling activity
* Input dataset lineage (generalized archaeological points, environmental layers)
* Links to:

  * `provenance/transformations-log.csv`
  * STAC Collection (if present)
  * Neo4j provenance graph

KFM pipelines automatically validate STAC Items against:

* JSON schema
* SHACL shape
* CARE governance rules

---

## 🧠 Focus Mode & Story Node Integration

Focus Mode v3 uses STAC metadata to:

* Load H3 layers
* Display cluster context
* Generate summary cards
* Trigger 3D or timeline overlays
* Display provenance & CARE labels

Story Nodes reference STAC IDs to anchor:

* Cultural narrative zones
* Hydrological relationships
* Environmental affordance layers

Example Focus Summary:

> **Focus Summary:**
> Late Prehistoric H3 r7 clusters highlight broad settlement bands along central Kansas terrace systems.
> These cells reflect generalized cultural landscapes and follow CARE generalization protocols.

---

## 🕰️ Version History

| Version | Date       | Author                                        | Summary                                                               |
| ------: | ---------- | --------------------------------------------- | --------------------------------------------------------------------- |
| v11.0.0 | 2025-11-17 | Archaeology Working Group · FAIR+CARE Council | Initial STAC metadata documentation for Late Prehistoric H3 clusters. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0
STAC Metadata · CARE-Governed · FAIR+CARE Certified · MCP-DL v6.3
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

[Back to H3 Generalizations](../README.md) · [Late Prehistoric Cluster Index](../../README.md)

</div>
