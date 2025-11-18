---
title: "📍 Kansas Frontier Matrix: Late Prehistoric Site Distribution Clusters (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly / Archaeology Working Group · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/archaeology-site-distribution-clusters-late-prehistoric-v1.json"
governance_ref: "../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Results"
intent: "archaeology-site-distribution-clusters-late-prehistoric"
fair_category: "F1-A1-I1-R1"
care_label: "Public / CARE-Governed"
sensitivity_level: "Medium"
public_exposure_risk: "Medium"
indigenous_rights_flag: true
data_steward: "Archaeology Working Group · FAIR+CARE Council"
risk_category: "Spatial Cluster Results"
redaction_required: true
provenance_chain:
  - "docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E31 Document"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"
json_schema_ref: "../../../../../../../../schemas/json/archaeology-site-distribution-clusters-late-prehistoric.schema.json"
shape_schema_ref: "../../../../../../../../schemas/shacl/archaeology-site-distribution-clusters-late-prehistoric-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:results:site-distribution-clusters-late-prehistoric-v11.0.0"
semantic_document_id: "kfm-arch-results-site-distribution-clusters-late-prehistoric"
event_source_id: "ledger:docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/README.md"
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
role: "archaeology-results-site-distribution-clusters-late-prehistoric"
lifecycle_stage: "stable"
ttl_policy: "Review every 12 months"
sunset_policy: "Superseded upon next major Late Prehistoric cluster revision"
---

<div align="center">

# 📍 **Kansas Frontier Matrix — Late Prehistoric Site Distribution Clusters**  
`docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/README.md`

**Purpose:**  
Present the **generalized spatial clusters** of Late Prehistoric archaeological activity in Kansas as rendered in the Kansas Frontier Matrix (KFM).  
These clusters derive from validated KDE, spatial autocorrelation, environmental affordance modeling, and CARE-governed redaction rules.

![Docs](https://img.shields.io/badge/Docs·MCP_v6.3-blue)
![License](https://img.shields.io/badge/License-CC--BY--4.0-green)
![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Certified-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

</div>

---

## 📘 Overview

The Late Prehistoric period (~900–1450 CE) in Kansas features:

- Growing sedentism  
- Flourishing regional trade  
- Increased pottery diversity  
- Expanding horticultural landscapes  
- Cultural developments antecedent to the Great Bend Aspect  

These generalized clusters provide **safe, public-facing summaries** of archaeological activity during this era, avoiding any exposure of sensitive site coordinates.

All layers conform to:

- **FAIR+CARE ethical handling rules**  
- **Generalization requirements (H3 r7/r8)**  
- **CIDOC-CRM / GeoSPARQL semantic integration**  
- **Story Node v3 + Focus Mode v3 compatibility**  
- **WAL → Retry → Rollback lineage safety**

---

## 🗂️ Directory Layout

```text
docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/
├── README.md                    # This file
├── clusters.geojson             # Generalized Late Prehistoric cluster polygons (public-safe)
├── h3/                          # H3-based hex generalizations
├── rasters/                     # KDE and predictive smoothing rasters
├── stac/                        # STAC Items for each cluster layer
├── metadata/                    # DCAT + provenance metadata
└── provenance/                  # PROV-O logs for transformations
````

---

## 🧭 Interpretation Guidelines

### 1️⃣ Generalized Public Data Only

These clusters are NOT precise archaeological locations.
All coordinates are:

* Hex-aggregated
* Smoothed
* Buffered
* Ethically filtered via CARE authority

### 2️⃣ Environmental Context

Late Prehistoric clusters typically correlate with:

* River terraces
* Alluvial fans
* Low-slope margins
* Resource-rich ecotones

### 3️⃣ Cultural Considerations

Spatial patterns correspond to:

* Settlement basin structures
* Horticulture-supported communities
* Seasonal mobility corridors
* Trade networks with adjacent regions

Tribal partners determine the level of generalization for culturally sensitive landscapes.

---

## 📊 Methods Summary

### Spatial Methods

(See `../../../methods/spatial_analysis.md`)

* KDE with optimal bandwidth selection
* Spatial autocorrelation (Moran’s I, adjusted for survey bias)
* Ripley’s K for point clustering significance
* Hydrology adjacencies (GeoSPARQL-based)

### Predictive & Interaction Methods

(See `../../../methods/predictive_modeling.md`)

* GLM / GAM modeling
* Random forest / gradient boosting ensemble comparison
* Environmental affordance surfaces

### Uncertainty

All cluster outputs must include:

* Confidence surfaces
* Summary statistics
* Descriptions of survey bias and mitigation

---

## 🛰 STAC/DCAT Metadata

Example STAC Item:

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "kfm-late-prehistoric-clusters-v1",
  "bbox": [-102.0, 37.0, -94.6, 40.0],
  "properties": {
    "kfm:domain": "archaeology",
    "kfm:analysis": "cluster",
    "kfm:temporal_scope": "Late Prehistoric",
    "care:sensitivity": "generalized"
  },
  "assets": {
    "cluster_raster": {
      "href": "s3://kfm/archaeology/clusters/late_prehistoric/cluster_v1.tif",
      "roles": ["data"]
    }
  }
}
```

---

## 🧠 Focus Mode Integration

Late Prehistoric clusters contribute to:

* Story Node v3 regional narratives
* Hydrology–settlement linkage summaries
* Temporal-layer comparatives (Prehistoric → Protohistoric)
* Focus Summary callouts, such as:

> **Focus Summary:**
> Late Prehistoric clusters form around terrace systems along central Kansas river corridors.
> These represent generalized cultural activity zones and must not be interpreted as precise archaeological sites.

Focus Mode v3 always displays:

* CARE labels
* Provenance chain badges
* Generalization / uncertainty explanations

---

## 🧬 Provenance & Lineage

All cluster outputs MUST include:

* PROV-O `prov:Activity` for modeling
* Input datasets (generalized archaeological points, hydrology layers, environmental rasters)
* Transformations logs (`provenance/transformations-log.csv`)
* WAL safety metadata
* Version pinning + lineage entry in Neo4j

---

## 🕰️ Version History

| Version | Date       | Author                                        | Summary                                                                       |
| ------: | ---------- | --------------------------------------------- | ----------------------------------------------------------------------------- |
| v11.0.0 | 2025-11-17 | Archaeology Working Group · FAIR+CARE Council | Initial v11 Late Prehistoric cluster documentation; CARE compliance enforced. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0
Spatial Cluster Results · CARE-Governed · FAIR+CARE Certified
MCP-DL v6.3 Compatible · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

[Back to Cluster Index](../README.md) · [Governance Charter](../../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>
