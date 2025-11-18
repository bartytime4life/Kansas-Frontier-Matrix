---
title: "📚 Kansas Frontier Matrix: Late Prehistoric H3 — Proxy Source Metadata Registry (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/provenance/inputs/environmental_rasters/climate/seasonality/paleoseasonal/uncertainty/sources/metadata/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Annual / FAIR+CARE Council · Archaeology Working Group"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../../../../../../../../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../../../../../../../../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../../../../../../../../../../../../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../../../../../../../../../../../../../schemas/telemetry/archaeology-late-prehistoric-h3-paleoseasonal-proxy-metadata-v1.json"
governance_ref: "../../../../../../../../../../../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Metadata"
intent: "archaeology-late-prehistoric-h3-paleoseasonal-proxy-metadata"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
indigenous_rights_flag: true
data_steward: "Archaeology Working Group · FAIR+CARE Council"
risk_category: "Proxy Metadata"
redaction_required: false
provenance_chain:
  - "docs/analyses/.../metadata/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E73 Information Object"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  owl_time: "TemporalEntity"
json_schema_ref: "../../../../../../../../../../../../../../../../../../../../../schemas/json/archaeology-late-prehistoric-h3-paleoseasonal-proxy-metadata.schema.json"
shape_schema_ref: "../../../../../../../../../../../../../../../../../../../../../schemas/shacl/archaeology-late-prehistoric-h3-paleoseasonal-proxy-metadata-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:paleoseasonal-proxy-metadata-late-prehistoric-h3-v11.0.0"
semantic_document_id: "kfm-arch-results-late-prehistoric-h3-paleoseasonal-proxy-metadata"
event_source_id: "ledger:docs/analyses/.../metadata/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
ai_transform_prohibited:
  - "fabricated-proxy-info"
  - "unverified-inference"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Internal / CARE-Governed"
role: "archaeology-late-prehistoric-h3-paleoseasonal-proxy-metadata"
lifecycle_stage: "stable"
ttl_policy: "Review every 24 months"
sunset_policy: "Superseded upon next proxy metadata revision"
---

<div align="center">

# 📚 **Late Prehistoric H3 — Paleo-Seasonal Proxy Source Metadata Registry**  
`docs/analyses/.../metadata/README.md`

**Purpose:**  
Provide full **metadata documentation** for each proxy dataset contributing to paleo-seasonal reconstruction uncertainty surfaces, including pollen cores, isotopic data, and lacustrine sediment proxies.  
This registry ensures FAIR+CARE compliance, reproducible lineage, and complete transparency of environmental proxy usage.

![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Governed-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

</div>

---

## 📘 Overview

This directory contains **machine-readable metadata** (STAC, DCAT, JSON-LD) describing:

- Proxy datasets used in Holocene seasonal climate reconstructions  
- Uncertainty sources and calibration models  
- Spatial & temporal extents of proxy datasets  
- Cultural governance and CARE sensitivity notes  
- Provenance chain entries for each proxy source  
- Dataset-level lineage for Story Node v3 and Focus Mode v3 integrations  

All metadata files conform to:

- **KFM-MDP v11.0.0**  
- **DCAT 3.0**, **schema.org**, **OWL-Time**, **CIDOC-CRM**  
- **STAC 1.0.0** with KFM-specific extensions  
- **FAIR+CARE** cultural governance  

---

## 🗂️ Directory Layout

```text
docs/.../paleoseasonal/uncertainty/sources/metadata/
├── README.md                            # This file
├── pollen_proxy_sources_metadata.json    # Metadata for pollen-based proxies
├── isotopic_proxy_sources_metadata.json  # Metadata for isotope climate proxies
├── lake_core_metadata.json               # Metadata for sediment core datasets
└── combined_proxy_catalog.jsonld         # Unified metadata record for all proxy sources
````

---

## 🌿 Pollen Proxy Metadata (`pollen_proxy_sources_metadata.json`)

**Contains:**

* Proxy study citations
* Taxonomic group descriptions
* Generalized core locations
* Chronology details
* Proxy weights for uncertainty modeling
* CARE sensitivity notes
* STAC/DCAT crosswalk fields

**Used for:**

* vegetation–climate reconstructions
* precipitation and temperature seasonality estimation

---

## 💧 Lacustrine Core Metadata (`lake_core_metadata.json`)

**Includes:**

* Core identifiers
* Dating (14C/OSL)
* Sediment stratigraphy
* Paleo-hydrological indicators
* Proxy reliability metrics
* Model calibration ranges
* Uncertainty quantification inputs

---

## 🧪 Isotopic Proxy Metadata (`isotopic_proxy_sources_metadata.json`)

Documents:

* δ18O and δ13C values
* Water balance interpretations
* Analytical methods and uncertainty
* Calibration datasets
* Proxy-based seasonal temperature/precipitation modeling logic

---

## 📦 Combined Proxy Catalog (`combined_proxy_catalog.jsonld`)

A unified JSON-LD dataset containing:

* All proxy datasets
* Provenance chain for each proxy source
* CARE classification and cultural governance notes
* Links to uncertainty layers (temperature/precipitation)
* Cross-references to STAC Items and DCAT Datasets
* Story Node-relevant metadata (if applicable)

This file is the **canonical catalog** for pipeline ingestion.

---

## 🧬 Metadata Standards

All metadata records must include:

### **STAC Required Fields**

* `stac_version`
* `type`
* `bbox` (generalized)
* CARE sensitivity tags
* Provenance references (`prov:wasGeneratedBy`)
* Dataset identifiers

### **DCAT Required Fields**

* `dct:title`
* `dct:description`
* `dcat:spatial`
* `dcat:temporal` (OWL-Time interval)
* `dcat:distribution`
* Citation fields

### **KFM Extensions**

* `kfm:proxy_type`
* `kfm:uncertainty_model_notes`
* `kfm:proxy_weight`
* `kfm:confidence_estimates`

---

## 🧠 Focus Mode Integration Notes

Metadata in this directory is used by Focus Mode v3 to:

* Qualify paleo-environment interpretations
* Provide proxy-level explainability
* Generate narrative-safe uncertainty disclaimers
* Associate Story Node timelines with environmental shifts

Example Focus Summary:

> **Focus Summary:**
> Proxy metadata shows strong agreement between pollen, isotopic, and lacustrine climate indicators for central Kansas,
> producing higher-confidence paleo-seasonal reconstructions that contextualize Late Prehistoric settlement clustering.

---

## 🕰️ Version History

| Version | Date       | Author                             | Summary                                                     |
| ------: | ---------- | ---------------------------------- | ----------------------------------------------------------- |
| v11.0.0 | 2025-11-17 | Archaeology WG · FAIR+CARE Council | Initial metadata registry for paleo-seasonal proxy sources. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0
Proxy Metadata Registry · CARE-Governed · FAIR+CARE Certified
MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

[Back to Proxy Sources](../README.md) · [Back to Uncertainty](../../README.md)

</div>
