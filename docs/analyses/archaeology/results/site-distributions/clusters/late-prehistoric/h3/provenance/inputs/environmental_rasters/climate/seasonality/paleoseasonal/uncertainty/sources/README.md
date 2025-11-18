---
title: "📚 Kansas Frontier Matrix: Late Prehistoric H3 — Paleo-Seasonal Uncertainty Proxy Sources (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/provenance/inputs/environmental_rasters/climate/seasonality/paleoseasonal/uncertainty/sources/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Annual / FAIR+CARE Council · Archaeology Working Group"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../../../../../../../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../../../../../../../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../../../../../../../../../../../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../../../../../../../../../../../../schemas/telemetry/archaeology-late-prehistoric-h3-paleoseasonal-uncertainty-sources-v1.json"
governance_ref: "../../../../../../../../../../../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Provenance Inputs"
intent: "archaeology-late-prehistoric-h3-paleoseasonal-proxy-sources"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
indigenous_rights_flag: true
data_steward: "Archaeology Working Group · FAIR+CARE Council"
risk_category: "Proxy Data / Lineage Integrity"
redaction_required: false
provenance_chain:
  - "docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/provenance/inputs/environmental_rasters/climate/seasonality/paleoseasonal/uncertainty/sources/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E73 Information Object"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  owl_time: "TemporalEntity"
json_schema_ref: "../../../../../../../../../../../../../../../../../../../../schemas/json/archaeology-late-prehistoric-h3-paleoseasonal-proxy-sources.schema.json"
shape_schema_ref: "../../../../../../../../../../../../../../../../../../../../schemas/shacl/archaeology-late-prehistoric-h3-paleoseasonal-proxy-sources-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:paleoseasonal-uncertainty-sources-late-prehistoric-h3-v11.0.0"
semantic_document_id: "kfm-arch-results-late-prehistoric-h3-paleoseasonal-uncertainty-sources"
event_source_id: "ledger:docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/provenance/inputs/environmental_rasters/climate/seasonality/paleoseasonal/uncertainty/sources/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
ai_transform_prohibited:
  - "fabricated-proxy-data"
  - "unverified-inference"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Internal / CARE-Governed"
role: "archaeology-late-prehistoric-h3-paleoseasonal-proxy-sources"
lifecycle_stage: "stable"
ttl_policy: "Review every 12 months"
sunset_policy: "Superseded upon next proxy-source revision"
---

<div align="center">

# 📚 **Late Prehistoric H3 — Paleo-Seasonal Uncertainty Proxy Sources**  
`docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/provenance/inputs/environmental_rasters/climate/seasonality/paleoseasonal/uncertainty/sources/README.md`

**Purpose:**  
Document all **proxy datasets** used to generate uncertainty rasters for paleo-seasonal climate reconstructions.  
These proxy datasets underpin model reliability assessments and ensure transparent, reproducible interpretation of Late Prehistoric environmental conditions.

![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Governed-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

</div>

---

## 📘 Overview

Paleo-seasonal uncertainty estimates rely on **multi-proxy climate data**, including:

- palynological records (pollen)  
- lacustrine (lake sediment) cores  
- isotopic datasets  
- geochemical climate indicators  
- paleo-hydrological proxies  

Each proxy dataset contributes to reconstruction algorithms and must be:

- documented  
- versioned  
- CARE-reviewed  
- linked to STAC/DCAT  
- included in PROV-O lineage  

This ensures scientific rigor and cultural governance over deep-time environmental modeling.

---

## 🗂️ Directory Layout

```text
docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/provenance/inputs/environmental_rasters/climate/seasonality/paleoseasonal/uncertainty/sources/
├── README.md                          # This file
├── pollen_proxy_sources.csv           # Pollen study sites, metadata, weights
├── isotopic_proxy_sources.csv         # Isotope datasets (δ18O, δ13C, etc.)
├── lake_core_metadata.csv             # Lake sediment cores & geochronology
└── metadata/                          # STAC/DCAT proxy metadata
````

---

## 🌿 Palynological (Pollen) Proxy Sources

**File:** `pollen_proxy_sources.csv`

Includes:

* pollen taxa counts
* location of pollen cores (generalized)
* dating/chronology metadata
* calibration windows
* uncertainty weights per taxon group

Used to model:

* seasonal precipitation variation
* vegetation–climate linkage
* Late Prehistoric ecological conditions

---

## 💧 Lacustrine (Lake Core) Proxy Sources

**File:** `lake_core_metadata.csv`

Contains metadata for:

* sedimentation rates
* proxy climate indicators
* grain-size or organic composition data
* radiocarbon or OSL dating
* seasonal signals derived from microfossil assemblages

Supports:

* hydrological reconstructions
* drought frequency estimates
* ecohydrological seasonal variability

---

## 🧪 Isotopic Proxy Sources

**File:** `isotopic_proxy_sources.csv`

Captures:

* δ18O / δ13C data
* isotopic interpretations of precipitation/temperature
* site-level isotope uncertainty
* multi-proxy fusion weights
* model calibration series

Used for:

* temperature reconstruction
* moisture-balance modeling
* validation of pollen- and sediment-derived signals

---

## 🧬 Metadata Requirements (STAC/DCAT)

Proxy datasets must include:

* **STAC Items** with:

  * proxy type
  * temporal extent
  * uncertainty fields
  * CARE sensitivity classification

* **DCAT metadata** with:

  * full citations
  * methodology summaries
  * distribution metadata
  * `care:notes`
  * OWL-Time fields

Stored under:

```
metadata/
```

---

## 🧠 Focus Mode Integration Notes

Focus Mode v3 uses proxy metadata to:

* explain uncertainty sources
* differentiate strong vs weak climate reconstructions
* qualify narrative interpretations in Story Nodes
* show proxy weights and reliability levels

Example Focus Summary:

> **Focus Summary:**
> Paleo-seasonal uncertainty models incorporate pollen, lake core, and isotopic proxy records.
> Higher agreement among proxies produces higher-confidence reconstructions used in interpreting Late Prehistoric settlement patterns.

---

## 🕰️ Version History

| Version | Date       | Author                             | Summary                                                                     |
| ------: | ---------- | ---------------------------------- | --------------------------------------------------------------------------- |
| v11.0.0 | 2025-11-17 | Archaeology WG · FAIR+CARE Council | Initial proxy metadata documentation for paleo-seasonal uncertainty inputs. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0
Paleo-Seasonal Proxy Sources · CARE-Governed · FAIR+CARE Certified
MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

[Back to Uncertainty](../README.md) · [Back to Paleo-Seasonal Climate](../../README.md)

</div>
