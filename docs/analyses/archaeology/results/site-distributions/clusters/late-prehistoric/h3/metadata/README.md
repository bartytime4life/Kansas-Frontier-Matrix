---
title: "📍 Kansas Frontier Matrix: Late Prehistoric H3 Metadata Registry (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/metadata/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly / Archaeology Working Group · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../schemas/telemetry/archaeology-site-distribution-clusters-late-prehistoric-h3-metadata-v1.json"
governance_ref: "../../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Metadata"
intent: "archaeology-late-prehistoric-h3-metadata"
fair_category: "F1-A1-I1-R1"
care_label: "Public / CARE-Governed"
sensitivity_level: "Medium"
public_exposure_risk: "Medium"
indigenous_rights_flag: true
data_steward: "Archaeology Working Group · FAIR+CARE Council"
risk_category: "Metadata Registry"
redaction_required: true
provenance_chain:
  - "docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/metadata/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E31 Document"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"
json_schema_ref: "../../../../../../../../../schemas/json/archaeology-site-distribution-clusters-late-prehistoric-h3-metadata.schema.json"
shape_schema_ref: "../../../../../../../../../schemas/shacl/archaeology-site-distribution-clusters-late-prehistoric-h3-metadata-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:results:site-distribution-clusters-late-prehistoric-h3-metadata-v11.0.0"
semantic_document_id: "kfm-arch-results-late-prehistoric-h3-metadata"
event_source_id: "ledger:docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/metadata/README.md"
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
classification: "Public / Metadata"
role: "archaeology-results-site-distribution-clusters-late-prehistoric-h3-metadata"
lifecycle_stage: "stable"
ttl_policy: "Review every 12 months"
sunset_policy: "Superseded upon next metadata revision"
---

<div align="center">

# 📍 **Kansas Frontier Matrix — Late Prehistoric H3 Cluster Metadata Registry**  
`docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/metadata/README.md`

**Purpose:**  
Provide the **complete metadata registry** for Late Prehistoric H3 generalized archaeological settlement clusters in KFM, including DCAT metadata, model lineage, provenance descriptors, CARE flags, spatial/temporal extents, and dataset-level documentation.

![Docs](https://img.shields.io/badge/Docs·MCP_v6.3-blue)
![License](https://img.shields.io/badge/License-CC--BY--4.0-green)
![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Certified-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

</div>

---

## 📘 Overview

This directory contains **machine-readable metadata artifacts** (mostly DCAT, JSON-LD, and CSV descriptors) for public-safe H3 generalizations of Late Prehistoric archaeological clusters.

Metadata provides:

- Dataset descriptions  
- Spatial & temporal extents  
- Provenance and lineage  
- CARE constraints  
- Environmental and cultural context notes  
- Crosswalks to STAC Items & Story Nodes  
- Validation details for CI/CD governance  

These metadata records ensure compliance with:

- **FAIR Principles** (Findability, Accessibility, Interoperability, Reusability)  
- **CARE Principles** for Indigenous data governance  
- **KFM-MDP v11** metadata standards  
- **DCAT 3.0**, **schema.org**, **CIDOC-CRM**, **GeoSPARQL**  

---

## 🗂️ Directory Layout

```text
docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/metadata/
├── README.md                          # This file
├── dcat.json                           # DCAT metadata for H3 cluster layers
├── dataset.jsonld                      # schema.org/JSON-LD metadata
├── lineage.csv                         # Lineage summary table (PROV-O / pipeline logs)
├── spatial_extent.geojson              # BBOX + approximate extent geometries
├── temporal_extent.json                # Time interval metadata (OWL-Time)
├── care_review.md                      # CARE governance notes and cultural review log
├── validation_report.json              # CI/CD validation results (schema + a11y + FAIR+CARE)
└── transformations-log.csv             # Modeling + generalization provenance logs
````

---

## 🌐 DCAT Metadata (Key Fields)

The `dcat.json` file must include:

* `dct:title` — Dataset name
* `dct:description` — Summary of dataset purpose
* `dct:license` — Always CC-BY 4.0
* `dcat:keyword` — “archaeology”, “Late Prehistoric”, “H3”, “generalized clusters”
* `dcat:theme` — Cultural geography, heritage data
* `dcat:distribution` — Links to H3 GeoJSON layers & summary CSVs
* `dcat:spatial` — BBOX + reference systems
* `dcat:temporal` — OWL-Time interval (`start`, `end`, `precision`)
* `prov:wasGeneratedBy` — Pipeline activity ID
* `care:sensitivity` — “generalized”

This metadata enables indexing in KFM’s catalog browser and external DCAT systems.

---

## 🧬 Provenance & Lineage (PROV-O)

Lineage is preserved using:

* `transformations-log.csv`
* `prov:Activity` → modeling runs
* Input references:

  * generalized archaeological points
  * hydrology / environmental rasters
  * predictive model outputs
* H3 resolution parameters
* Smoothing specifications
* Any redactions mandated by tribal partners

The lineage log ensures **full reproducibility** and compliance with **WAL → Retry → Rollback → Lineage**.

---

## 🧭 CARE Review & Cultural Safety Notes

`care_review.md` must document:

* Cultural landscape intersections
* Tribal review outcomes
* Required generalization levels (r7/r8)
* Any redacted/masked cells
* Conditions for public release
* Ethical flags applicable to cluster interpretations

---

## 📊 Validation Artifacts

`validation_report.json` includes CI/CD checks for:

* JSON schema compliance
* SHACL shape conformance
* DCAT alignment
* CARE rule compliance
* Accessibility metadata completeness
* Link integrity

This validation ensures metadata consistency across the entire KFM monorepo.

---

## 🧠 Integration With STAC & Story Nodes

Metadata files must cross-reference:

* STAC Item IDs from `../stac/`
* Story Node IDs where Late Prehistoric H3 clusters support narrative context
* Neo4j node identifiers for:

  * Dataset
  * Place (generalized H3 regions)
  * Provenance activities

Example:

```json
{
  "kfm:related_stac_items": ["kfm-late-prehistoric-h3-r7-v1"],
  "kfm:related_story_nodes": ["urn:kfm:story:late-prehistoric-overview"]
}
```

---

## 🕰️ Version History

| Version | Date       | Author                                        | Summary                                                                               |
| ------: | ---------- | --------------------------------------------- | ------------------------------------------------------------------------------------- |
| v11.0.0 | 2025-11-17 | Archaeology Working Group · FAIR+CARE Council | Initial metadata registry for Late Prehistoric H3 generalized clusters under MDP v11. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0
Metadata Registry · FAIR+CARE Certified · MCP-DL v6.3 Compatible
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

[Back to H3 Directory](../README.md) · [Late Prehistoric Cluster Index](../../README.md)

</div>
