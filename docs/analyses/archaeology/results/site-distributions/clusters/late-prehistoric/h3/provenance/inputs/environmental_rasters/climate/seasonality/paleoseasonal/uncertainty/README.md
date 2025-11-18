---
title: "📉 Kansas Frontier Matrix: Late Prehistoric H3 — Paleo-Seasonal Climate Uncertainty Models (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/provenance/inputs/environmental_rasters/climate/seasonality/paleoseasonal/uncertainty/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Annual / FAIR+CARE Council · Archaeology Working Group"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../../../../../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../../../../../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../../../../../../../../../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../../../../../../../../../../schemas/telemetry/archaeology-late-prehistoric-h3-paleoseasonal-uncertainty-v1.json"
governance_ref: "../../../../../../../../../../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Provenance Inputs"
intent: "archaeology-late-prehistoric-h3-paleoseasonal-uncertainty"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
indigenous_rights_flag: true
data_steward: "Archaeology Working Group · FAIR+CARE Council"
risk_category: "Uncertainty Modeling"
redaction_required: false
provenance_chain:
  - "docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/provenance/inputs/environmental_rasters/climate/seasonality/paleoseasonal/uncertainty/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E73 Information Object"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  owl_time: "TemporalEntity"
json_schema_ref: "../../../../../../../../../../../../../../../../../../schemas/json/archaeology-late-prehistoric-h3-paleoseasonal-uncertainty.schema.json"
shape_schema_ref: "../../../../../../../../../../../../../../../../../../schemas/shacl/archaeology-late-prehistoric-h3-paleoseasonal-uncertainty-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:paleoseasonal-uncertainty-late-prehistoric-h3-v11.0.0"
semantic_document_id: "kfm-arch-results-late-prehistoric-h3-paleoseasonal-uncertainty"
event_source_id: "ledger:docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/provenance/inputs/environmental_rasters/climate/seasonality/paleoseasonal/uncertainty/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
ai_transform_prohibited:
  - "fabricated-uncertainty"
  - "unverified-inference"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Internal / CARE-Governed"
role: "archaeology-late-prehistoric-h3-paleoseasonal-uncertainty"
lifecycle_stage: "stable"
ttl_policy: "Review every 12 months"
sunset_policy: "Superseded upon next paleo-seasonal uncertainty update"
---

<div align="center">

# 📉 **Late Prehistoric H3 — Paleo-Seasonal Climate Uncertainty Models**  
`docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/provenance/inputs/environmental_rasters/climate/seasonality/paleoseasonal/uncertainty/README.md`

**Purpose:**  
Describe all **uncertainty rasters** associated with paleo-seasonal climate reconstructions used in the Late Prehistoric H3 generalization pipeline.  
These uncertainty layers accompany temperature and precipitation reconstructions to ensure transparent interpretation, responsible modeling, and robust lineage documentation.

![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Governed-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

</div>

---

## 📘 Overview

Paleo-seasonal uncertainty datasets quantify the reliability, confidence, and limits of climate reconstructions derived from:

- pollen records  
- lake cores / lacustrine proxies  
- isotopic analysis  
- sedimentological climate indicators  
- multi-proxy climate composites  

Uncertainty rasters are required for:

- **predictive modeling weighting**
- **KDE contextual smoothing**
- **hydrology-linked cluster confidence**
- **Focus Mode narrative accuracy**
- **STAC/DCAT metadata completeness**
- **PROV-O uncertainty lineage references**

These layers *do not* indicate cultural or archaeological uncertainty—  
they represent reconstruction confidence for **environmental** variables only.

---

## 🗂️ Directory Layout

```text
docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/provenance/inputs/environmental_rasters/climate/seasonality/paleoseasonal/uncertainty/
├── README.md                                         # This file
├── holocene_temp_uncertainty.tif                     # Temperature reconstruction uncertainty
├── holocene_precip_uncertainty.tif                   # Precipitation reconstruction uncertainty
├── holocene_seasonal_uncertainty.csv                 # Tabular summary of uncertainty metrics
├── sources/                                          # Proxy dataset citations + metadata
│   ├── pollen_proxy_sources.csv
│   ├── isotopic_proxy_sources.csv
│   └── lake_core_metadata.csv
└── metadata/                                         # STAC/DCAT records describing uncertainty layers
````

---

## 🌡️ Temperature Reconstruction Uncertainty

**File:** `holocene_temp_uncertainty.tif`

Represents spatial uncertainty for reconstructed winter/summer temperatures.

Includes:

* standard deviation grids
* calibration window effects
* proxy weighting impacts
* model reconstruction error

Used to:

* adjust predictive model confidence
* assist in spatial interpretation of cluster patterns
* qualify environmental affordance interpretations

---

## 🌧️ Precipitation Reconstruction Uncertainty

**File:** `holocene_precip_uncertainty.tif`

Represents uncertainty for Holocene precipitation estimates.

Includes:

* variance in proxy interpretation
* calibration curve sensitivity
* sedimentological vs. palynological disagreement zones
* model residual error maps

Used to:

* contextualize moisture-linked prehistoric clustering
* support environmental scenario descriptions
* inform Story Node climate narratives

---

## 📊 Tabular Uncertainty Summary

**File:** `holocene_seasonal_uncertainty.csv`

Contains:

* proxy weights
* reconstruction methods
* site-level uncertainty contributions
* statistical summaries
* spatial summary indices

Supports transparency and replicability.

---

## 🧬 Proxy Source Metadata

Stored under: `sources/`

Tracks:

* pollen core locations
* lake sediment proxies
* isotope sampling data
* dating and calibration windows
* uncertainties per proxy family

Required for **provenance validation**.

---

## 🌐 Metadata Requirements (STAC/DCAT)

### STAC fields must include:

* `stac_version: "1.0.0"`
* `properties.care:sensitivity = "generalized"`
* `prov:wasGeneratedBy` activity URN
* uncertainty layer references (`kfm:uncertainty_asset`)

### DCAT fields must include:

* dataset description
* uncertainty summary
* proxy source citations
* spatial + temporal extents
* distribution metadata

Stored in:

```
metadata/
```

---

## 🧠 Focus Mode Integration Notes

Focus Mode v3 uses uncertainty metadata to:

* scale narrative confidence
* annotate climate-affordance explanations
* distinguish strong vs. weak reconstruction zones
* prevent overinterpretation of climate-linked settlement patterns

Example Focus Note:

> **Focus Summary:**
> Paleo-seasonal uncertainty layers indicate greater reconstruction confidence in central Kansas terrace systems
> and higher uncertainty in sandhills and southern uplands.
> Interpretation of cluster-environment relationships is adjusted accordingly.

---

## 🕰️ Version History

| Version | Date       | Author                             | Summary                                                               |
| ------: | ---------- | ---------------------------------- | --------------------------------------------------------------------- |
| v11.0.0 | 2025-11-17 | Archaeology WG · FAIR+CARE Council | Initial uncertainty documentation for paleo-seasonal climate rasters. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0
Paleo-Seasonal Climate Uncertainty · CARE-Governed · FAIR+CARE Certified
MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

[Back to Paleo-Seasonal Climate](../README.md) · [Back to Seasonal Climate](../../README.md)

</div>
