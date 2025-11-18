---
title: "🕰️❄️☀️ Kansas Frontier Matrix: Late Prehistoric H3 — Paleo-Seasonal Climate Reconstructions (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/provenance/inputs/environmental_rasters/climate/seasonality/paleoseasonal/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Annual / FAIR+CARE Council · Archaeology Working Group"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../../../../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../../../../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../../../../../../../../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../../../../../../../../../schemas/telemetry/archaeology-late-prehistoric-h3-paleoseasonal-v1.json"
governance_ref: "../../../../../../../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Provenance Inputs"
intent: "archaeology-late-prehistoric-h3-paleoseasonal-rasters"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
indigenous_rights_flag: true
data_steward: "Archaeology Working Group · FAIR+CARE Council"
risk_category: "Environmental Paleoclimate Inputs"
redaction_required: false
provenance_chain:
  - "docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/provenance/inputs/environmental_rasters/climate/seasonality/paleoseasonal/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E73 Information Object"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  owl_time: "TemporalEntity"
  geosparql: "geo:Feature"
json_schema_ref: "../../../../../../../../../../../../../../../../../schemas/json/archaeology-late-prehistoric-h3-paleoseasonal-raster.schema.json"
shape_schema_ref: "../../../../../../../../../../../../../../../../../schemas/shacl/archaeology-late-prehistoric-h3-paleoseasonal-raster-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:late-prehistoric-h3-paleoseasonal-v11.0.0"
semantic_document_id: "kfm-arch-results-late-prehistoric-h3-paleoseasonal"
event_source_id: "ledger:docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/provenance/inputs/environmental_rasters/climate/seasonality/paleoseasonal/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
ai_transform_prohibited:
  - "fabricated-paleoclimate-relationships"
  - "unverified-inference"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Internal / CARE-Governed"
role: "archaeology-late-prehistoric-h3-paleoseasonal-inputs"
lifecycle_stage: "stable"
ttl_policy: "Review every 12 months"
sunset_policy: "Superseded upon next paleo-seasonal input revision"
---

<div align="center">

# 🕰️❄️☀️ **Late Prehistoric H3 — Paleo-Seasonal Climate Reconstructions**  
`docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/provenance/inputs/environmental_rasters/climate/seasonality/paleoseasonal/README.md`

**Purpose:**  
Document the **paleo-seasonal climate reconstruction datasets** used as environmental inputs in generating Late Prehistoric H3 generalized clusters.  
These layers include proxy-based reconstructions (pollen, lake cores, sediment chemistry), providing deep-time seasonal climate context essential for understanding Late Prehistoric settlement patterns, ecological adaptation, and Story Node v3 narratives.

![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Governed-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

</div>

---

## 📘 Overview

Paleo-seasonal climate layers reconstruct winter/summer temperature and precipitation patterns across Holocene and Late Prehistoric Kansas using:

- palynology (pollen analysis)  
- lacustrine (lake core) climate proxies  
- isotopic geochemistry  
- sedimentological climate indicators  
- multi-proxy climate reconstructions  

These rasters inform:

- environmental affordance modeling  
- temporal transitions across the Late Prehistoric period  
- paleo-ecological constraints relevant to settlement clustering  
- long-term drought/wet cycle interpretation  
- integrative narratives for Focus Mode and Story Nodes  

All datasets are subject to:

- CARE review  
- Uncertainty analysis  
- Provenance registration  
- STAC/DCAT metadata integration  

---

## 🗂️ Directory Layout

```text
docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/provenance/inputs/environmental_rasters/climate/seasonality/paleoseasonal/
├── README.md                                      # This file
├── holocene_winter_temp_recon.tif                 # Winter temperature reconstruction
├── holocene_summer_temp_recon.tif                 # Summer temperature reconstruction
├── holocene_winter_precip_recon.tif               # Winter precipitation reconstruction
├── holocene_summer_precip_recon.tif               # Summer precipitation reconstruction
├── proxy_sources.csv                              # Proxy study citations + metadata
├── uncertainty/                                   
│   ├── holocene_temp_uncertainty.tif
│   └── holocene_precip_uncertainty.tif
└── metadata/                                      # STAC/DCAT metadata for paleo-seasonal layers
````

---

## 🧭 Paleo-Seasonal Raster Descriptions

### ❄️ Winter Reconstructions

**Files:**

* `holocene_winter_temp_recon.tif`
* `holocene_winter_precip_recon.tif`

**Used for:**

* winter habitability modeling
* cold-season mobility constraints
* cultural seasonality reconstructions

**Metadata requires:**

* proxy dataset citations
* temporal extent (OWL-Time)
* uncertainty surface references

---

### ☀️ Summer Reconstructions

**Files:**

* `holocene_summer_temp_recon.tif`
* `holocene_summer_precip_recon.tif`

**Used for:**

* growing-season suitability
* horticultural feasibility modeling
* warm-season settlement patterns

**Metadata includes:**

* proxy methods
* spatial resolution
* reconstruction algorithm parameters

---

## 🧪 Uncertainty & Proxy Integrity

Located under: `uncertainty/`

Each paleo-raster must include:

* uncertainty rasters (`*_uncertainty.tif`)
* reconstruction method explanation
* proxy weights (pollen vs. sediment vs. isotope)
* sensitivity to calibration windows
* STAC uncertainty metadata fields

---

## 🌐 STAC/DCAT Metadata Requirements

All paleo-seasonal rasters must provide:

### STAC

* `stac_version: 1.0.0`
* `type: "Feature"`
* `properties.kfm:domain = archaeology`
* `properties.kfm:analysis = paleo-seasonality`
* `prov:wasGeneratedBy` → activity URN
* CARE sensitivity tag
* Uncertainty asset links

### DCAT

* proxy dataset citation block
* uncertainty notes
* spatial + temporal descriptors
* distribution entries

Stored in:

```
metadata/
```

---

## 🧠 Focus Mode Integration Notes

Focus Mode v3 uses paleo-seasonal layers to generate:

* environmental deep-time context
* narrative explanations for hydrology/settlement links
* long-duration climate cycle insights
* region-specific drought/wet oscillation commentary

Example Focus Summary:

> **Focus Summary:**
> Paleo-seasonal reconstructions indicate stable winter temperatures and moderate summer precipitation
> across central Kansas, conditions that likely supported Late Prehistoric horticulture and seasonal mobility
> reflected in generalized H3 clusters.

---

## 🕰️ Version History

| Version | Date       | Author                             | Summary                                                                      |
| ------: | ---------- | ---------------------------------- | ---------------------------------------------------------------------------- |
| v11.0.0 | 2025-11-17 | Archaeology WG · FAIR+CARE Council | Initial paleo-seasonal climate documentation for Late Prehistoric H3 inputs. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0
Paleo-Seasonal Climate Inputs · CARE-Governed · FAIR+CARE Certified
MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

[Back to Seasonal Climate](../README.md) · [Back to Climate Inputs](../../README.md)

</div>
