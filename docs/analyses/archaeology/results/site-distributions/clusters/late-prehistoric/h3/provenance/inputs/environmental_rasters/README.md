---
title: "🌦️ Kansas Frontier Matrix: Late Prehistoric H3 — Environmental Raster Inputs (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/provenance/inputs/environmental_rasters/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly / FAIR+CARE Council · Archaeology Working Group"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../../../../../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../../../../../../schemas/telemetry/archaeology-late-prehistoric-h3-environmental-rasters-v1.json"
governance_ref: "../../../../../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Provenance Inputs"
intent: "archaeology-late-prehistoric-h3-environmental-rasters"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
indigenous_rights_flag: true
data_steward: "Archaeology Working Group · FAIR+CARE Council"
risk_category: "Environmental Input Layers"
redaction_required: false
provenance_chain:
  - "docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/provenance/inputs/environmental_rasters/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E73 Information Object"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  geosparql: "geo:Feature"
json_schema_ref: "../../../../../../../../../../../../../../schemas/json/archaeology-late-prehistoric-h3-environmental-rasters.schema.json"
shape_schema_ref: "../../../../../../../../../../../../../../schemas/shacl/archaeology-late-prehistoric-h3-environmental-rasters-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:inputs:late-prehistoric-h3-environmental-rasters-v11.0.0"
semantic_document_id: "kfm-arch-results-late-prehistoric-h3-environmental-rasters"
event_source_id: "ledger:docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/provenance/inputs/environmental_rasters/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
ai_transform_prohibited:
  - "fabricated-environmental-relationships"
  - "unverified-inference"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Internal / CARE-Governed"
role: "archaeology-late-prehistoric-h3-environmental-rasters"
lifecycle_stage: "stable"
ttl_policy: "Review every 12 months"
sunset_policy: "Superseded upon next environmental input revision"
---

<div align="center">

# 🌦️ **Late Prehistoric H3 — Environmental Raster Inputs**  
`docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/provenance/inputs/environmental_rasters/README.md`

**Purpose:**  
Provide complete documentation for all **environmental raster layers** used in generating Late Prehistoric H3 generalized cluster surfaces.  
These datasets underpin KDE surfaces, predictive modeling, affordance analysis, and hydrology-linked spatial reasoning, and are essential to PROV-O lineage and FAIR+CARE governance.

![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Governed-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

</div>

---

## 📘 Overview

Environmental rasters used in the Late Prehistoric H3 workflow include:

- Climate reconstructions  
- Historical precipitation & drought indices  
- Vegetation / landcover surfaces  
- Soil fertility & drainage  
- Terrain-derived layers (DEM, slope, aspect, ruggedness)  
- Environmental suitability surfaces used in predictive modeling  

These inputs are:

- **Generalized** when necessary  
- **Reviewed under CARE governance**  
- **Versioned and reproducible**  
- Logged in **STAC/DCAT** and **PROV-O**  

All rasters originate from open-data sources or CARE-approved reconstructions.

---

## 🗂️ Directory Layout

```text
docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/provenance/inputs/environmental_rasters/
├── README.md                          # This file
├── climate/                           # Precip/temp/humidity/drought rasters
├── vegetation/                        # Historical landcover, biomass models
├── soils/                             # Soil classification & fertility surfaces
├── terrain/                           # DEM, slope, aspect, ruggedness
├── hydrology_derived/                 # Floodplains, distance-to-stream rasters
├── suitability/                       # Predictive modeling suitability composites
└── metadata/                          # STAC/DCAT metadata for raster layers
````

---

## 🌡️ Climate Rasters

Located in: `climate/`

Common layers:

* Reconstructed annual precipitation
* Mean annual temperature
* Drought indices (PDSI, SPEI)
* Seasonality models

**Provenance Requirements:**

* Source dataset citation
* Spatial resolution
* Temporal coverage
* Generalization applied (if any)
* CARE notes (avoid sensitive eco-cultural inference)

---

## 🌿 Vegetation & Landcover Rasters

Located in: `vegetation/`

Includes:

* Historical vegetation models
* Landcover reconstructions
* Biomass models
* Ecotone rasters

Vegetation surfaces often influence:

* settlement likelihood
* mobility corridors
* subsistence strategies

---

## 🌱 Soil & Fertility Rasters

Located in: `soils/`

Contains:

* Soil type
* Drainage
* Fertility class
* Parent material

All layers must include:

* CRS
* Spatial resolution
* Transformations & masking
* PROV-O lineage

---

## 🏔️ Terrain Rasters

Located in: `terrain/`

Includes:

* DEM (generalized/public-safe resolution)
* Slope
* Aspect
* Roughness
* Terrain position index

Used for:

* corridor modeling
* settlement affordance
* KDE smoothing corrections

---

## 🌊 Hydrology-Derived Rasters

Located in: `hydrology_derived/`

Includes:

* Floodplain models
* Distance-to-stream rasters
* Alluvial boundary models

These layers often explain clustered activity patterns in Late Prehistoric Kansas.

---

## ⚙️ Suitability Surfaces

Located in: `suitability/`

Inputs include:

* Environmental suitability composites
* Predictive model multi-layer stacks
* Weighted predictor grids

These must:

* Log transformation parameters
* Include reproducibility metadata
* Reflect CARE constraints
* Provide STAC lineage entries

---

## 🧬 Metadata Requirements (STAC/DCAT)

All environmental rasters must include:

### **STAC Metadata**

* `stac_version: 1.0.0`
* `properties.kfm:domain = archaeology`
* `properties.kfm:analysis = environmental`
* `properties.care:sensitivity = generalized`

### **DCAT Metadata**

* Title, description, themes
* Spatial + temporal extent
* Distribution links
* CARE review notes
* Provenance references

Stored under:

```
metadata/
```

---

## 🧠 Focus Mode Integration Notes

Focus Mode v3 uses environmental rasters to:

* Explain environmental affordances
* Provide context for H3 cluster interpretations
* Link climatic patterns with Late Prehistoric settlement trends
* Generate narrative-safe summaries, e.g.:

> **Focus Summary:**
> Environmental rasters indicate favorable hydrology and fertile soils across terrace systems,
> aligning with generalized Late Prehistoric H3 clusters.

Focus Mode enforces:

* CARE sensitivity warnings
* Uncertainty disclaimers
* Provenance chip links

---

## 🕰️ Version History

| Version | Date       | Author                             | Summary                                                                                     |
| ------: | ---------- | ---------------------------------- | ------------------------------------------------------------------------------------------- |
| v11.0.0 | 2025-11-17 | Archaeology WG · FAIR+CARE Council | Initial environmental raster input documentation for Late Prehistoric H3 cluster workflows. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0
Environmental Inputs · CARE-Governed · FAIR+CARE Certified
MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

[Back to Inputs](../README.md) · [Back to H3 Directory](../../../../README.md)

</div>
