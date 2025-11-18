---
title: "📍 Kansas Frontier Matrix: Late Prehistoric H3 Cluster Generalizations (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly / Archaeology Working Group · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../schemas/telemetry/archaeology-site-distribution-clusters-late-prehistoric-h3-v1.json"
governance_ref: "../../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Results"
intent: "archaeology-site-distribution-clusters-late-prehistoric-h3"
fair_category: "F1-A1-I1-R1"
care_label: "Public / CARE-Governed"
sensitivity_level: "Medium"
public_exposure_risk: "Medium"
indigenous_rights_flag: true
data_steward: "Archaeology Working Group · FAIR+CARE Council"
risk_category: "Generalized Spatial Results"
redaction_required: true
provenance_chain:
  - "docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E31 Document"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"
json_schema_ref: "../../../../../../../../../schemas/json/archaeology-site-distribution-clusters-late-prehistoric-h3.schema.json"
shape_schema_ref: "../../../../../../../../../schemas/shacl/archaeology-site-distribution-clusters-late-prehistoric-h3-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:results:site-distribution-clusters-late-prehistoric-h3-v11.0.0"
semantic_document_id: "kfm-arch-results-site-distribution-clusters-late-prehistoric-h3"
event_source_id: "ledger:docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/README.md"
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
role: "archaeology-results-site-distribution-clusters-late-prehistoric-h3"
lifecycle_stage: "stable"
ttl_policy: "Review every 12 months"
sunset_policy: "Superseded upon next major H3 cluster revision"
---

<div align="center">

# 📍 **Kansas Frontier Matrix — Late Prehistoric H3 Cluster Generalizations**  
`docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/README.md`

**Purpose:**  
Document the **H3-based generalized settlement clusters** for Late Prehistoric Kansas, ensuring cultural protection, interpretive value, FAIR+CARE-compliant redaction, and Story Node v3 / Focus Mode v3 integration.

![Docs](https://img.shields.io/badge/Docs·MCP_v6.3-blue)
![License](https://img.shields.io/badge/License-CC--BY--4.0-green)
![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Certified-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

</div>

---

## 📘 Overview

This directory contains **H3 hex-based generalizations** of Late Prehistoric archaeological settlement clusters.  
All geometries:

- remove precise site locations  
- aggregate to multi-kilometer hex cells  
- apply smoothing and density thresholds  
- incorporate cultural safety reviews  

These layers are safe for **public visualization** and adhere to all **FAIR+CARE**, **CIDOC-CRM**, **GeoSPARQL**, and **STAC/DCAT** requirements.

---

## 🗂️ Directory Layout

```text
docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/
├── README.md                         # This file
├── h3_r7.geojson                      # Public-safe hexagons (coarse)
├── h3_r8.geojson                      # Medium-resolution generalized hexagons
├── h3_summary.csv                     # Density + statistical summaries per hex
├── stac/                              # STAC Items describing each hex layer
├── metadata/                          # DCAT metadata
└── provenance/                        # PROV-O lineage and transformation logs
````

---

## 🧭 Interpretation Guidelines

### 1️⃣ These Are NOT Sites

H3 cells **do not** show archaeological sites.
They show **regional settlement patterns**, generalized to protect cultural heritage.

### 2️⃣ Cultural Safety Enforcement

* No cell corresponds to any individual site
* Sensitive cells may be collapsed into coarser H3 levels
* Tribal review determines masking levels

### 3️⃣ Environmental Context

Late Prehistoric hex clusters often align with:

* River terraces
* Resource-rich ecotones
* Alluvial margins
* Corridor systems

Interpretation requires contextual awareness, not coordinate-level inference.

---

## 📊 Methods Summary

### H3 Generalization Process

1. **Input Sites (Generalized)**

   * Buffered or jittered sensitive coordinates
   * CARE-reviewed redactions applied

2. **Hex Aggregation**

   * H3 resolution r7 (public-safe)
   * Optional refinement to r8 (context-safe)
   * Weighted density calculation

3. **Cluster Smoothing**

   * KDE smoothing
   * Neighborhood normalization

4. **Validation**

   * Spatial autocorrelation
   * Survey bias correction
   * Cultural landscape review

---

## 🛰 Example STAC Metadata

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "kfm-late-prehistoric-h3-r7-v1",
  "properties": {
    "kfm:domain": "archaeology",
    "kfm:analysis": "cluster-h3",
    "kfm:temporal_scope": "Late Prehistoric",
    "care:sensitivity": "generalized"
  },
  "assets": {
    "hexes": {
      "href": "s3://kfm/archaeology/clusters/late_prehistoric/h3/h3_r7.geojson",
      "roles": ["data"]
    }
  }
}
```

---

## 🧠 Focus Mode Integration

Focus Mode v3 uses these H3 layers to:

* Show generalized cultural activity bands
* Provide context on settlement corridors
* Connect environmental affordance narratives
* Summarize patterns via **Focus Summary** blocks:

> **Focus Summary:**
> Late Prehistoric settlement intensity concentrates in broad, river-adjacent H3 bands across central Kansas.
> These generalized layers reflect cultural activity, not specific archaeological sites.

Focus Mode always displays:

* CARE labels
* Uncertainty notes
* Provenance chips
* Resolution indicators (r7, r8)

---

## 🧬 Provenance & Lineage

The provenance chain includes:

* Generalization steps (H3 level, smoothing ops)
* Input dataset references
* PROV-O `prov:Activity` modeling logs
* `transformations-log.csv` entries
* STAC lineage metadata
* WAL → Retry → Rollback safety info

All provenance is accessible under:

```
provenance/
```

---

## 🕰️ Version History

| Version | Date       | Author                                        | Summary                                                                 |
| ------: | ---------- | --------------------------------------------- | ----------------------------------------------------------------------- |
| v11.0.0 | 2025-11-17 | Archaeology Working Group · FAIR+CARE Council | Initial Late Prehistoric H3 generalization documentation under MDP v11. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0
Generalized H3 Cluster Results · FAIR+CARE Certified · MCP-DL v6.3 Compatible
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

[Back to Late Prehistoric Clusters](../README.md) · [Cluster Index](../../README.md)

</div>
