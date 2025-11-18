---
title: "❄️☀️ Kansas Frontier Matrix: Late Prehistoric H3 — Seasonal Climate Metadata Registry (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/provenance/inputs/environmental_rasters/climate/seasonality/metadata/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Annual / FAIR+CARE Council · Archaeology Working Group"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../../../../../../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../../../../../../../schemas/telemetry/archaeology-late-prehistoric-h3-seasonal-climate-metadata-v1.json"
governance_ref: "../../../../../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Metadata"
intent: "archaeology-late-prehistoric-h3-seasonal-climate-metadata"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
indigenous_rights_flag: true
data_steward: "Archaeology Working Group · FAIR+CARE Council"
risk_category: "Environmental Seasonal Metadata"
redaction_required: false
provenance_chain:
  - "docs/.../seasonality/metadata/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E73 Information Object"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  owl_time: "TemporalEntity"
json_schema_ref: "../../../../../../../../../../../../../../../schemas/json/archaeology-late-prehistoric-h3-seasonal-climate-metadata.schema.json"
shape_schema_ref: "../../../../../../../../../../../../../../../schemas/shacl/archaeology-late-prehistoric-h3-seasonal-climate-metadata-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:late-prehistoric-h3-seasonal-climate-metadata-v11.0.0"
semantic_document_id: "kfm-arch-results-late-prehistoric-h3-seasonal-climate-metadata"
event_source_id: "ledger:docs/.../seasonality/metadata/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
ai_transform_prohibited:
  - "fabricated-seasonal-data"
  - "unverified-inference"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Internal / CARE-Governed"
role: "archaeology-late-prehistoric-h3-seasonal-metadata"
lifecycle_stage: "stable"
ttl_policy: "Review every 24 months"
sunset_policy: "Superseded upon next seasonal climate metadata revision"
---

<div align="center">

# ❄️☀️ **Late Prehistoric H3 — Seasonal Climate Metadata Registry**  
`docs/.../seasonality/metadata/README.md`

**Purpose:**  
Document all **metadata** associated with seasonal climate rasters (winter/summer precipitation and temperature) used in the Late Prehistoric H3 generalization workflow.  
This registry enables FAIR+CARE–aligned provenance tracking, STAC/DCAT interoperability, and safe integration into Story Node v3 and Focus Mode v3 environmental narratives.

![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Governed-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

</div>

---

## 📘 Overview

Seasonal climate metadata governs:

- winter/summer precipitation rasters  
- winter/summer temperature rasters  
- seasonal composites used in hydrology–settlement modeling  
- seasonal suitability indicators  
- STAC/DCAT metadata, extents & distributions  
- OWL-Time seasonal interval definitions  
- GeoSPARQL spatial envelopes  
- CARE governance of environmental interpretations  

These metadata files maintain:

- reproducibility  
- lineage integrity  
- narrative safety in Focus Mode  
- scientific transparency  
- cross-dataset interoperability  

---

## 🗂️ Directory Layout

```text
docs/.../seasonality/metadata/
├── README.md                                   # This file
├── winter_precip_metadata.json                  # STAC/DCAT metadata for winter precipitation
├── summer_precip_metadata.json                  # STAC/DCAT metadata for summer precipitation
├── winter_temp_metadata.json                    # STAC/DCAT metadata for winter temperature
├── summer_temp_metadata.json                    # STAC/DCAT metadata for summer temperature
├── seasonal_combined_metadata.jsonld            # Unified seasonal climate metadata bundle
├── temporal_extent.json                         # OWL-Time seasonal intervals
├── spatial_extent.geojson                       # Generalized spatial boundaries
└── validation_report.json                       # CI/CD schema validation results
````

---

## ❄️ Winter Metadata Records

### `winter_precip_metadata.json`

Includes:

* reconstructed winter precipitation summaries
* STAC Item fields
* proxy and reconstruction lineage notes
* CARE sensitivity class
* distribution metadata

### `winter_temp_metadata.json`

Documents:

* winter mean temperatures
* uncertainty references
* spatial & temporal metadata
* provenance references

Used in:

* winter movement constraints
* Late Prehistoric habitability models

---

## ☀️ Summer Metadata Records

### `summer_precip_metadata.json`

Contains:

* growing-season precipitation distributions
* suitability modeling notes
* semantic links (GeoSPARQL)
* CARE governance annotations

### `summer_temp_metadata.json`

Includes:

* summer thermal constraints
* hydrology-linked interpretation
* calibration model notes
* OWL-Time temporal bins

Used in:

* settlement intensity interpretation
* predictive model weighting

---

## 📦 Combined Seasonal Metadata (`seasonal_combined_metadata.jsonld`)

Provides unified metadata describing:

* all seasonal climate rasters
* all transformations
* uncertainty associations
* proxy sources
* narrative-safe environmental framing
* crosswalk entries for STAC + DCAT + PROV-O
* Focus Mode–ready semantic descriptors

This is the **canonical ingest file** for pipelines.

---

## 🕰️ Seasonal Temporal Extents (`temporal_extent.json`)

Defines:

* winter period intervals
* summer period intervals
* Late Prehistoric seasonal ranges
* OWL-Time compliant interval objects
* calibration and proxy-based temporal windows

---

## 🌍 Spatial Metadata (`spatial_extent.geojson`)

Generalized spatial extents include:

* coarse hydrology envelopes
* generalized corridor regions
* bounding polygons
* ecological transition zones

All spatial metadata uses GeoSPARQL classes.

---

## 🧪 Validation & Governance

### `validation_report.json` includes:

* STAC compliance checks
* DCAT schema validation
* SHACL shape constraints
* FAIR+CARE governance checks
* PROV-O lineage completeness

Metadata failing any checks *cannot* be ingested.

---

## 🧠 Focus Mode Integration Notes

Focus Mode v3 uses seasonal climate metadata to:

* generate seasonal environmental explanations
* contextualize cluster patterns
* display uncertainty and seasonal dynamics
* prevent overinterpretation of climate-linked archaeological narratives

Example Focus Summary:

> **Focus Summary:**
> Seasonal climate metadata indicates distinct winter–summer contrasts in hydrology and horticultural
> suitability, aligning with generalized Late Prehistoric settlement patterns visible in H3 clusters.

---

## 🕰️ Version History

| Version | Date       | Author                             | Summary                                                   |
| ------: | ---------- | ---------------------------------- | --------------------------------------------------------- |
| v11.0.0 | 2025-11-17 | Archaeology WG · FAIR+CARE Council | Initial seasonal climate metadata registry under MDP v11. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0
Seasonal Climate Metadata · CARE-Governed · FAIR+CARE Certified
MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

[Back to Seasonal Climate](../README.md) · [Back to Environmental Rasters](../../../README.md)

</div>
