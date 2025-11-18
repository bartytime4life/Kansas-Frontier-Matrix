---
title: "🕰️🌦️ Kansas Frontier Matrix: Late Prehistoric H3 — Paleo-Seasonal Climate Metadata Registry (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/provenance/inputs/environmental_rasters/climate/seasonality/paleoseasonal/metadata/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Annual / FAIR+CARE Council · Archaeology Working Group"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../../../../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../../../../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../../../../../../../../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../../../../../../../../../schemas/telemetry/archaeology-late-prehistoric-h3-paleoseasonal-metadata-v1.json"
governance_ref: "../../../../../../../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Metadata"
intent: "archaeology-late-prehistoric-h3-paleoseasonal-climate-metadata"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
indigenous_rights_flag: true
data_steward: "Archaeology Working Group · FAIR+CARE Council"
risk_category: "Environmental Paleoclimate Metadata"
redaction_required: false
provenance_chain:
  - "docs/.../paleoseasonal/metadata/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E73 Information Object"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  owl_time: "TemporalEntity"
json_schema_ref: "../../../../../../../../../../../../../../../../../schemas/json/archaeology-late-prehistoric-h3-paleoseasonal-metadata.schema.json"
shape_schema_ref: "../../../../../../../../../../../../../../../../../schemas/shacl/archaeology-late-prehistoric-h3-paleoseasonal-metadata-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:paleoseasonal-metadata-late-prehistoric-h3-v11.0.0"
semantic_document_id: "kfm-arch-results-late-prehistoric-h3-paleoseasonal-metadata"
event_source_id: "ledger:docs/.../paleoseasonal/metadata/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
ai_transform_prohibited:
  - "fabricated-environmental-metadata"
  - "unverified-inference"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Internal / CARE-Governed"
role: "archaeology-late-prehistoric-h3-paleoseasonal-climate-metadata"
lifecycle_stage: "stable"
ttl_policy: "Review every 24 months"
sunset_policy: "Superseded upon next paleo-seasonal metadata revision"
---

<div align="center">

# 🕰️🌦️ **Late Prehistoric H3 — Paleo-Seasonal Climate Metadata Registry**  
`docs/.../paleoseasonal/metadata/README.md`

**Purpose:**  
Document all **metadata records** associated with paleo-seasonal climate reconstructions used in Late Prehistoric H3 generalization workflows.  
These metadata files describe temperature/precipitation reconstructions, uncertainty models, proxy sources, and CARE-sensitive environmental contexts supporting KFM’s archaeological interpretations.

![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Governed-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

</div>

---

## 📘 Overview

This metadata registry includes:

- STAC Items describing paleo-seasonal climate rasters  
- DCAT dataset manifests for reconstructed temperature & precipitation surfaces  
- JSON-LD lineage metadata for environmental reconstructions  
- CARE governance notes  
- OWL-Time temporal descriptors  
- GeoSPARQL spatial geometries  

These metadata files ensure:

- FAIR+CARE compliance  
- Cultural sovereignty protections  
- Full provenance & reproducibility  
- Semantic interoperability (CIDOC-CRM, PROV-O, OWL-Time, STAC, DCAT)  
- Narrative-safe integration into Story Node v3 and Focus Mode v3  

---

## 🗂️ Directory Layout

```text
docs/.../paleoseasonal/metadata/
├── README.md                             # This file
├── paleo_temp_metadata.json               # Temperature reconstruction metadata
├── paleo_precip_metadata.json             # Precipitation reconstruction metadata
├── paleo_combined_metadata.jsonld         # Unified paleo-seasonal metadata
├── temporal_extent.json                   # OWL-Time interval definitions
├── spatial_extent.geojson                 # Spatial bounding boxes for reconstructions
└── validation_report.json                 # CI/CD schema validation output
````

---

## 🌡️ Temperature Reconstruction Metadata (`paleo_temp_metadata.json`)

Describes:

* Holocene and Late Prehistoric temperature reconstructions
* Proxy datasets used
* Calibration details
* Uncertainty model references
* Spatial and temporal extents
* CARE constraints
* STAC/DCAT crosswalk fields

---

## 🌧️ Precipitation Reconstruction Metadata (`paleo_precip_metadata.json`)

Includes:

* Annual & seasonal reconstructions
* Multi-proxy source links
* Reconstruction algorithm parameters
* Spatial smoothing metadata
* Confidence fields
* Temporal ranges (OWL-Time)

---

## 📦 Combined Paleo-Seasonal Metadata (`paleo_combined_metadata.jsonld`)

Provides:

* Unified environmental dataset metadata
* Links to all uncertainty layers
* Cross-proxy consensus metrics
* Narrative-safe environmental context
* STAC/DCAT composite entries
* PROV-O provenance linking to modeling activities

This is the recommended ingest file for pipelines & Focus Mode.

---

## 🕰️ Temporal Metadata (`temporal_extent.json`)

Defines:

* absolute temporal range
* seasonal sub-ranges
* Holocene calibration periods
* OWL-Time compliant interval objects

---

## 🌍 Spatial Metadata (`spatial_extent.geojson`)

Generalized extents recorded as:

* terrain masks
* bounding polygons
* generalized river-basin envelopes
* centroid-based proxies

GeoSPARQL classifications included.

---

## 🧪 Validation

`validation_report.json` contains:

* JSON Schema results
* SHACL shape validation
* CARE compliance checks
* Temporal & spatial integrity verification
* Provenance chain completeness audit

All metadata must pass validation before publication.

---

## 🧠 Focus Mode Integration Notes

Focus Mode v3 uses paleo-seasonal climate metadata to:

* contextualize environmental influences on Late Prehistoric settlement
* scale narrative confidence by uncertainty metadata
* explain long-term climate cycles
* support Story Node environmental panels

Example Focus Summary:

> **Focus Summary:**
> Paleo-seasonal metadata indicates moderate climate variability during the Late Prehistoric period,
> with strong agreement among proxy datasets across central Kansas—supporting stable settlement clustering in terrace regions.

---

## 🕰️ Version History

| Version | Date       | Author                             | Summary                                                           |
| ------: | ---------- | ---------------------------------- | ----------------------------------------------------------------- |
| v11.0.0 | 2025-11-17 | Archaeology WG · FAIR+CARE Council | Initial metadata documentation for paleo-seasonal climate inputs. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0
Paleo-Seasonal Climate Metadata · CARE-Governed · FAIR+CARE Certified
MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

[Back to Paleo-Seasonal Inputs](../README.md) · [Back to Uncertainty](../../uncertainty/README.md)

</div>
