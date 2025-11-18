---
title: "❄️☀️ Kansas Frontier Matrix: Late Prehistoric H3 — Seasonal Climate Raster Inputs (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/provenance/inputs/environmental_rasters/climate/seasonality/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly / FAIR+CARE Council · Archaeology Working Group"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../../../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../../../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../../../../../../../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../../../../../../../../schemas/telemetry/archaeology-late-prehistoric-h3-seasonal-climate-v1.json"
governance_ref: "../../../../../../../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Provenance Inputs"
intent: "archaeology-late-prehistoric-h3-seasonal-climate-rasters"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
indigenous_rights_flag: true
data_steward: "Archaeology Working Group · FAIR+CARE Council"
risk_category: "Environmental Input Layers"
redaction_required: false
provenance_chain:
  - "docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/provenance/inputs/environmental_rasters/climate/seasonality/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E73 Information Object"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  owl_time: "TemporalEntity"
  geosparql: "geo:Feature"
json_schema_ref: "../../../../../../../../../../../../../../../../schemas/json/archaeology-late-prehistoric-h3-seasonal-climate.schema.json"
shape_schema_ref: "../../../../../../../../../../../../../../../../schemas/shacl/archaeology-late-prehistoric-h3-seasonal-climate-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:late-prehistoric-h3-seasonal-climate-v11.0.0"
semantic_document_id: "kfm-arch-results-late-prehistoric-h3-seasonal-climate"
event_source_id: "ledger:docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/provenance/inputs/environmental_rasters/climate/seasonality/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
ai_transform_prohibited:
  - "fabricated-seasonal-relationships"
  - "unverified-inference"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Internal / CARE-Governed"
role: "archaeology-late-prehistoric-h3-seasonal-climate"
lifecycle_stage: "stable"
ttl_policy: "Review every 12 months"
sunset_policy: "Superseded upon next seasonal climate update"
---

<div align="center">

# ❄️☀️ **Late Prehistoric H3 — Seasonal Climate Raster Inputs**  
`docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/provenance/inputs/environmental_rasters/climate/seasonality/README.md`

**Purpose:**  
Document the **seasonal climate rasters** (winter/summer precipitation & temperature surfaces) used within Late Prehistoric H3 modeling workflows.  
These seasonal layers refine hydrology–settlement relationships, ecological affordances, and temporal patterns relevant to Story Node v3 and Focus Mode v3 narratives.

![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Governed-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

</div>

---

## 📘 Overview

Seasonal climate layers allow archaeologists to model how Late Prehistoric communities interacted with:

- seasonal moisture availability  
- thermal constraints on movement and habitation  
- growing-season variation  
- drought exposure patterns  
- ecological shifts tied to winter vs. summer conditions  

These surfaces underpin:

- predictive modeling inputs  
- environmental affordance analysis  
- seasonal activity interpretations in Story Nodes  
- multi-nodal analysis of settlement patterns  

All rasters are governed by CARE constraints and are generalized or resampled as required.

---

## 🗂️ Directory Layout

```text
docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/provenance/inputs/environmental_rasters/climate/seasonality/
├── README.md                       # This file
├── winter_precip.tif               # Winter precipitation (generalized)
├── summer_precip.tif               # Summer precipitation
├── winter_temp.tif                 # Winter temperature (mean)
├── summer_temp.tif                 # Summer temperature (mean)
├── paleoseasonal/                  # Paleo-seasonal reconstructions (if available)
│   ├── holocene_winter_temp_recon.tif
│   └── holocene_summer_precip_recon.tif
└── metadata/                       # STAC/DCAT metadata for these seasonal rasters
````

---

## ❄️ Winter Climate Rasters

### `winter_precip.tif`

Represents winter precipitation reconstructed or modeled for the region.

* Used in hydrology-linked cluster interpretation
* Helps distinguish winter-stable vs. winter-variable settlement landscapes

### `winter_temp.tif`

Represents mean winter temperatures.

* Supports mobility and site suitability modeling
* Linked to ecological constraints & subsistence windows

---

## ☀️ Summer Climate Rasters

### `summer_precip.tif`

Represents growing-season precipitation.

* Critical for horticulture-linked interpretations
* Helps contextualize density clusters along terrace systems

### `summer_temp.tif`

Represents mean summer temperatures.

* Used to assess energy expenditure & mobility constraints
* Influences predictive model weighting

---

## 🏺 Paleo-Seasonal Reconstructions

Stored under: `paleoseasonal/`

Examples:

* Holocene-era winter temperature reconstructions
* Summer drought-frequency surfaces

These must include:

* proxy dataset citations
* uncertainty bands
* OWL-Time fields in DCAT
* transformation documentation in provenance logs

---

## 🧬 Metadata Requirements (STAC/DCAT)

Seasonal climate rasters must include:

### STAC

* `type: "Feature"`
* `stac_version: "1.0.0"`
* `properties.kfm:temporal_scope = "Late Prehistoric"`
* `care:sensitivity = "generalized"`
* Links to provenance activities via `prov:wasGeneratedBy`

### DCAT

* `dct:title`, `dcat:theme`, `dct:description`
* Spatial/temporal extents
* Distribution URLs or paths
* `care:notes` for sensitive eco-cultural inference boundaries

Metadata files are stored in:

```
metadata/
```

---

## 🧠 Focus Mode Integration Notes

Focus Mode v3 uses seasonal climate inputs to enrich narratives:

* Why clusters appear near certain ecological zones
* Seasonal mobility patterns
* Shifting river terrace habitability through seasons
* Distinction between winter congregation vs. summer dispersal

Example Focus Summary:

> **Focus Summary:**
> Seasonal climate surfaces show that Late Prehistoric activity clusters align with regions warm enough in winter
> and moist enough in summer to support stable horticultural and foraging cycles.

---

## 🕰️ Version History

| Version | Date       | Author                             | Summary                                        |
| ------: | ---------- | ---------------------------------- | ---------------------------------------------- |
| v11.0.0 | 2025-11-17 | Archaeology WG · FAIR+CARE Council | Initial seasonal climate raster documentation. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0
Seasonal Climate Inputs · CARE-Governed · FAIR+CARE Certified
MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

[Back to Climate Rasters](../README.md) · [Back to Environmental Rasters](../../README.md)

</div>
