---
title: "🌦️ Kansas Frontier Matrix: Late Prehistoric H3 — Climate Raster Inputs (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/provenance/inputs/environmental_rasters/climate/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly / Archaeology Working Group · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../../../../../../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../../../../../../../schemas/telemetry/archaeology-late-prehistoric-h3-climate-rasters-v1.json"
governance_ref: "../../../../../../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Provenance Inputs"
intent: "archaeology-late-prehistoric-h3-climate-rasters"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
indigenous_rights_flag: true
data_steward: "Archaeology Working Group · FAIR+CARE Council"
risk_category: "Environmental Input Layers"
redaction_required: false
provenance_chain:
  - "docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/provenance/inputs/environmental_rasters/climate/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E73 Information Object"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  owl_time: "TemporalEntity"
  geosparql: "geo:Feature"
json_schema_ref: "../../../../../../../../../../../../../../../schemas/json/archaeology-late-prehistoric-h3-climate-rasters.schema.json"
shape_schema_ref: "../../../../../../../../../../../../../../../schemas/shacl/archaeology-late-prehistoric-h3-climate-rasters-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:late-prehistoric-h3-climate-rasters-v11.0.0"
semantic_document_id: "kfm-arch-results-late-prehistoric-h3-climate-rasters"
event_source_id: "ledger:docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/provenance/inputs/environmental_rasters/climate/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
ai_transform_prohibited:
  - "fabricated-climate-relationships"
  - "unverified-inference"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Internal / CARE-Governed"
role: "archaeology-late-prehistoric-h3-climate-rasters"
lifecycle_stage: "stable"
ttl_policy: "Review every 12 months"
sunset_policy: "Superseded upon next climate input update"
---

<div align="center">

# 🌦️ **Late Prehistoric H3 — Climate Raster Inputs**  
`docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/provenance/inputs/environmental_rasters/climate/README.md`

**Purpose:**  
Document all **climate raster layers** used during the generation of Late Prehistoric H3 generalized clusters, including precipitation, drought indices, temperature surfaces, and seasonality models.  
These climate datasets form a key part of predictive modeling, environmental affordance analysis, hydrology-linked spatial reasoning, and Story Node contextualization.

![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Governed-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

</div>

---

## 📘 Overview

Climate rasters included in the Late Prehistoric H3 workflow provide essential environmental context for:

- settlement likelihood modeling  
- corridor and movement analysis  
- hydrology-linked clustering  
- seasonal resource patterns  
- paleoenvironmental reconstruction

All layers are:

- **generalized or resampled** when needed  
- **documented via STAC/DCAT metadata**  
- **governed under CARE rules**  
- **included in PROV-O lineage as input entities**  
- **validated for uncertainty, accuracy, and reproducibility**

---

## 🗂️ Directory Layout

```text
docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/provenance/inputs/environmental_rasters/climate/
├── README.md                         # This file
├── precip_annual.tif                 # Reconstructed annual precipitation (generalized if required)
├── temp_mean_annual.tif              # Reconstructed annual mean temperature
├── drought_pdsi.tif                  # Palmer Drought Severity Index raster
├── seasonality/                      # Subdirectory for seasonal climate surfaces
│   ├── winter_precip.tif
│   ├── summer_precip.tif
│   ├── winter_temp.tif
│   └── summer_temp.tif
├── paleo_recon/                      # Paleoenvironmental reconstructions
│   ├── pollen_climate_recon.tif
│   ├── holocene_temp_recon.tif
│   └── holocene_precip_recon.tif
└── metadata/                         # STAC/DCAT metadata files describing climate rasters
````

---

## 🌧️ Climate Raster Categories

### 1️⃣ Precipitation Rasters (`precip_annual.tif`)

Used for:

* hydrology-linked clustering
* environmental suitability modeling
* terrace/river proximity interpretations

**Metadata must include:**

* source dataset
* temporal coverage
* spatial resolution
* resampling or masking
* uncertainty notes

---

### 2️⃣ Temperature Rasters (`temp_mean_annual.tif`)

Used to contextualize:

* subsistence strategy modeling
* thermal comfort zones
* vegetation transitions

Includes seasonal composites under `seasonality/`.

---

### 3️⃣ Drought Index Rasters (`drought_pdsi.tif`)

Includes:

* PDSI
* SPEI (if available)
* drought frequency reconstruction

Used in:

* cultural stress analysis
* cluster interpretation
* environmental constraint evaluation

---

### 4️⃣ Paleoenvironmental Reconstructions (`paleo_recon/`)

Contain:

* Early–Late Holocene reconstructions
* Climate surfaces derived from pollen, lake cores, and proxy datasets

These layers require:

* proxy dataset citations
* uncertainty notes
* temporal bounding (OWL-Time)
* provenance for reconstruction methods

---

## 🧬 Metadata Requirements (STAC/DCAT)

Metadata stored in:

```
metadata/
```

Must include:

### STAC Required Fields

* `stac_version: 1.0.0`
* `type: "Feature"`
* `kfm:domain = archaeology`
* `kfm:analysis = climate`
* `care:sensitivity = generalized`
* `prov:wasGeneratedBy` for preprocessing activities

### DCAT Required Fields

* `dct:title`
* `dct:description`
* `dcat:distribution`
* `dcat:spatial` (BBOX)
* `dcat:temporal` (OWL-Time interval)
* `care:notes`
* provenance chain links

---

## 🧠 Focus Mode Integration

Focus Mode v3 uses climate inputs to:

* explain why clusters appear in specific hydrological or ecological settings
* support environmental narrative context for Story Nodes
* highlight drought-era or climate-shift influences on Late Prehistoric landscapes

Example Focus Summary:

> **Focus Summary:**
> Climate rasters show Late Prehistoric settlement clusters aligning with regions of moderate precipitation and fertile terraces,
> suggesting environmental stability during peak occupation periods.

---

## 🕰️ Version History

| Version | Date       | Author                             | Summary                                                                                  |
| ------: | ---------- | ---------------------------------- | ---------------------------------------------------------------------------------------- |
| v11.0.0 | 2025-11-17 | Archaeology WG · FAIR+CARE Council | Initial documentation for climate raster inputs supporting Late Prehistoric H3 clusters. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0
Climate Inputs · CARE-Governed · FAIR+CARE Certified
MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

[Back to Environmental Rasters](../README.md) · [Back to Provenance Inputs](../../README.md)

</div>
