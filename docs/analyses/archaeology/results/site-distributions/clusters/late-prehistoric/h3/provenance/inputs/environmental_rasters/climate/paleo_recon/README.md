---
title: "🌍🕰️ Kansas Frontier Matrix: Late Prehistoric H3 — Paleoenvironmental Climate Reconstructions (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/provenance/inputs/environmental_rasters/climate/paleo_recon/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Annual / FAIR+CARE Council · Archaeology Working Group"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../../../../../../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../../../../../../../schemas/telemetry/archaeology-late-prehistoric-h3-paleo-recon-v1.json"
governance_ref: "../../../../../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Provenance Inputs"
intent: "archaeology-late-prehistoric-h3-paleo-recon"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
indigenous_rights_flag: true
data_steward: "Archaeology Working Group · FAIR+CARE Council"
risk_category: "Paleoenvironmental Inputs"
redaction_required: false
provenance_chain:
  - "docs/.../paleo_recon/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E73 Information Object"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  owl_time: "TemporalEntity"
json_schema_ref: "../../../../../../../../../../../../../../../schemas/json/archaeology-late-prehistoric-h3-paleo-recon.schema.json"
shape_schema_ref: "../../../../../../../../../../../../../../../schemas/shacl/archaeology-late-prehistoric-h3-paleo-recon-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:paleo-recon-late-prehistoric-h3-v11.0.0"
semantic_document_id: "kfm-arch-results-late-prehistoric-h3-paleo-recon"
event_source_id: "ledger:docs/.../paleo_recon/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
ai_transform_prohibited:
  - "fabricated-paleoclimate-links"
  - "unverified-inference"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Internal / CARE-Governed"
role: "archaeology-late-prehistoric-h3-paleo-recon"
lifecycle_stage: "stable"
ttl_policy: "Review every 24 months"
sunset_policy: "Superseded upon next paleoenvironmental dataset revision"
---

<div align="center">

# 🌍🕰️ **Late Prehistoric H3 — Paleoenvironmental Climate Reconstructions**  
`docs/.../paleo_recon/README.md`

**Purpose:**  
Document the full set of **paleoenvironmental raster datasets** used in Late Prehistoric H3 modeling workflows, including long-term climate reconstructions, Holocene-era proxy surfaces, and deep-time environmental models contributing to predictive modeling and archaeological interpretation.

These layers form the **deep environmental context** for Late Prehistoric settlement patterns and climate-linked cultural narratives in Focus Mode v3.

![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Governed-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

</div>

---

## 📘 Overview

Paleoenvironmental reconstruction inputs include:

- Holocene temperature & precipitation reconstructions  
- Multi-proxy climate surfaces  
- Paleo-hydrology indicators  
- Proxy-based vegetation–climate models  
- Long-term drought/wet cycle reconstructions  

These rasters help contextualize:

- settlement clustering  
- hydrology-linked behaviors  
- ecological affordances  
- environmental constraints  
- temporal transitions leading into the Late Prehistoric period  

All inputs undergo:

- CARE sovereignty review  
- STAC/DCAT metadata validation  
- PROV-O lineage integration  
- uncertainty assessment  
- reproducibility validation via WAL → Retry → Rollback → Lineage

---

## 🗂️ Directory Layout

```text
docs/.../paleo_recon/
├── README.md                                  # This file
├── holocene_temp_recon.tif                    # Temperature reconstruction raster
├── holocene_precip_recon.tif                  # Precipitation reconstruction raster
├── holocene_moisture_balance.tif              # Hydroclimate model layer
├── vegetation_recon.tif                        # Paleo-vegetation model (generalized)
├── proxy_weights.json                          # Proxy source weights per reconstruction
├── calibration_models/                         # Calibration & tuning models
│   ├── temp_calibration.json
│   └── precip_calibration.json
├── uncertainty/                                # Uncertainty surfaces (linked to uncertainty module)
│   ├── temp_uncertainty_ref.json
│   └── precip_uncertainty_ref.json
└── metadata/                                   # STAC/DCAT metadata & provenance files
````

---

## 🌡️ Temperature Reconstructions

**File:** `holocene_temp_recon.tif`

Derived from:

* isotopic proxies
* pollen climate analog datasets
* lake sediment geochemistry

Used for:

* thermal envelope modeling
* long-term habitability interpretations
* predictive model calibration

Metadata includes:

* OWL-Time ranges
* uncertainty references
* proxy weighting details
* spatial smoothing notes

---

## 🌧️ Precipitation Reconstructions

**File:** `holocene_precip_recon.tif`

Derived from:

* SPEI-like proxy indicators
* pollen-based precipitation estimates
* hydroclimate modeling from sediment proxies

Used for:

* moisture-related clustering
* drought/wet cycles
* paleohydrological analysis

---

## 🌱 Paleo-Vegetation Reconstructions

**File:** `vegetation_recon.tif`

Includes:

* generalized landcover assemblages
* biomass reconstructions
* ecozone transitions

Used for understanding ecological affordances and cultural-landscape interactions.

---

## 💧 Moisture-Balance / Hydroclimate Models

**File:** `holocene_moisture_balance.tif`

Constructed via:

* integrated proxy sources
* hydrological reconstruction models
* climate calibration datasets

Links strongly with cluster interpretations in floodplains and terrace-dominated regions.

---

## 📦 Proxy Weighting Metadata

**File:** `proxy_weights.json`

Describes:

* contribution of pollen, isotopes, sediments
* calibration weights
* spatially varying reliability
* inputs to suitability/predictive models

---

## 🔧 Calibration Model Records

Located under: `calibration_models/`

Includes:

* regression/ML model parameters
* environmental tuning processes
* proxy comparison logic

All models must include:

* config hashes
* reproducibility metadata
* WAL-safe execution IDs

---

## 🧬 Metadata Requirements (STAC/DCAT)

All paleoenvironmental inputs require:

### STAC

* `stac_version: 1.0.0`
* `type: Feature`
* CARE sensitivity flag
* provenance entries (`prov:wasGeneratedBy`)
* uncertainty asset references

### DCAT

* proxy dataset citations
* methodology summaries
* distribution metadata
* spatial/temporal descriptors (OWL-Time & GeoSPARQL)

Stored in:

```
metadata/
```

---

## 🧠 Focus Mode Integration Notes

Focus Mode v3 uses paleoenvironmental reconstructions to generate:

* long-range environmental timelines
* context layers for Story Nodes
* narrative-safe hydrological/climatic explanations
* comparisons between Holocene climate cycles and Late Prehistoric settlement trends

Example Focus Summary:

> **Focus Summary:**
> Paleoenvironmental reconstructions reveal moderate long-term climatic variability leading into the Late Prehistoric period,
> helping explain settlement clustering along stable hydrological corridors.

---

## 🕰️ Version History

| Version | Date       | Author                             | Summary                                                                                       |
| ------: | ---------- | ---------------------------------- | --------------------------------------------------------------------------------------------- |
| v11.0.0 | 2025-11-17 | Archaeology WG · FAIR+CARE Council | Initial documentation for paleoenvironmental climate inputs for Late Prehistoric H3 clusters. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0
Paleoenvironmental Inputs · CARE-Governed · FAIR+CARE Certified
MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

[Back to Climate Inputs](../README.md) · [Back to Environmental Rasters](../../../README.md)

</div>
