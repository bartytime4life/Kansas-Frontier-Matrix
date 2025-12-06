---
title: "🌿 Kansas Frontier Matrix — Ecology Datasets Registry (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/ecology/datasets/README.md"
version: "v11.2.4"
last_updated: "2025-12-06"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x datasets-registry compatible"
status: "Active / Enforced"

doc_kind: "DatasetRegistry"
intent: "ecology-datasets-registry"
role: "data-registry"
header_profile: "standard"
footer_profile: "standard"

scope:
  domain: "ecology"
  applies_to:
    - "analyses"
    - "pipelines"
    - "sdm"
    - "ecosystem-services"
    - "landcover"
    - "telemetry"
    - "governance"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Ecology (masked)"
sensitivity: "Mixed (biodiversity + environment; masking rules apply)"
sensitivity_level: "Medium"
public_exposure_risk: "Medium"
classification: "KFM-Open"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
risk_category: "Ecology · Datasets"
redaction_required: true

commit_sha: "<latest-commit-hash>"
previous_version_hash: "docs/analyses/ecology/datasets/README.md@v10.2.2"
doc_integrity_checksum: "<sha256-of-this-file>"

sbom_ref: "../../../../../releases/v11.2.4/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.4/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.4/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/analyses-ecology-datasets-v3.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
ontology_protocol_version: "KFM-OP v11"

ontology_alignment:
  cidoc: "E31 Document"
  schema_org: "Dataset"
  prov_o: "prov:Collection"
  owl_time: "ProperInterval"

metadata_profiles:
  - "PROV-O"
  - "FAIR+CARE"
  - "STAC 1.x"
  - "DCAT 3.0"

provenance_chain:
  - "docs/analyses/ecology/README.md"
  - "docs/analyses/ecology/datasets/README.md@v10.2.2"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "schemas/json/docs-analyses-ecology-datasets-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/docs-analyses-ecology-datasets-v11.2.4-shape.ttl"
story_node_refs: []

immutability_status: "version-pinned"

doc_uuid: "urn:kfm:doc:analyses:ecology:datasets-registry:v11.2.4"
semantic_document_id: "kfm-analyses-ecology-datasets-registry-v11.2.4"
event_source_id: "ledger:kfm:doc:analyses:ecology:datasets-registry:v11.2.4"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "metadata-extraction"
ai_transform_prohibited:
  - "speculative-additions"
  - "unverified-historical-claims"
  - "species-location-de-anonymization"
  - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

lifecycle_stage: "stable"
ttl_policy: "Review every 12 months"
sunset_policy: "Superseded upon next ecology datasets registry revision"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "metadata-check"
  - "provenance-check"
  - "footer-check"
  - "accessibility-check"
---

<div align="center">

# 🌿 **Kansas Frontier Matrix — Ecology Datasets Registry**  
`docs/analyses/ecology/datasets/README.md`

**Purpose:**  
Document all **biodiversity, land cover, and ecological datasets** used for modeling and analysis within the Kansas Frontier Matrix (KFM).  
These datasets are registered and validated under **FAIR+CARE**, **STAC/DCAT 3.0**, and **ISO 19115-3**, ensuring open data interoperability and environmental governance transparency.

[![Docs · MCP_v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../../README.md)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../../LICENSE)  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Ecology_Datasets-orange)](../../../../../docs/standards/README.md)  
[![Status](https://img.shields.io/badge/Status-Active_Build-brightgreen)](../../../../../releases/v11.2.4/manifest.zip)

</div>

---

## 📘 Overview

The **Ecology Datasets Registry** defines all biodiversity, vegetation, and environmental data resources used in the KFM **Ecology Module**.  
These datasets inform species distribution models (SDMs), habitat suitability analyses, and ecosystem service assessments.  
All entries conform to **FAIR+CARE governance**, **ISO 50001** energy management, and ethical environmental data stewardship principles.

---

## 🗂️ Directory Layout

```plaintext
docs/analyses/ecology/datasets/
├── 📄 README.md                                  # This document
├── 📁 raw/                                       # Original GBIF, USDA, EPA, MODIS, NOAA datasets
│   ├── 📄 README.md
│   ├── 📄 gbif_occurrences.csv
│   ├── 📄 usda_plants.csv
│   ├── 📄 epa_ecological_health.csv
│   ├── 📄 modis_ndvi.nc
│   └── 📄 noaa_climate_covariates.csv
├── 📁 processed/                                 # Cleaned, harmonized, and quality-controlled datasets
│   ├── 📄 README.md
│   ├── 📄 biodiversity_cleaned.csv
│   ├── 📄 habitat_variables.nc
│   ├── 📄 landcover_harmonized.tif
│   └── 📄 ecosystem_variables.json
├── 📁 derived/                                   # Derived metrics and indices
│   ├── 📄 README.md
│   ├── 📄 species_richness_index.csv
│   ├── 📄 habitat_suitability_model.nc
│   ├── 📄 ecosystem_service_value.nc
│   └── 📄 biodiversity_hotspots.geojson
└── 📁 metadata/                                  # Metadata and FAIR+CARE validation reports
    ├── 📄 README.md
    ├── 📄 stac_catalog.json
    ├── 📄 dcat_metadata.json
    ├── 📄 faircare_validation.json
    └── 📄 provenance_log.json
```

---

## ⚙️ Core Ecological Datasets

| Source                   | Dataset                         | Description                                   | Format  | FAIR+CARE Status |
|--------------------------|---------------------------------|-----------------------------------------------|---------|------------------|
| **GBIF**                 | Biodiversity Occurrences        | Global species presence/absence data          | CSV     | ✅ Certified     |
| **USDA PLANTS / NRCS**   | Plant & ecological site data    | Species and habitat attributes                | CSV     | ✅ Certified     |
| **EPA / USGS**           | Ecological health indices       | Water quality & habitat metrics               | CSV     | ✅ Certified     |
| **NASA MODIS / ESA CCI** | Vegetation cover & NDVI series  | Remote-sensed ecosystem trends                | NetCDF  | ✅ Certified     |
| **NOAA NCEI**            | Climate covariates              | Temperature, precipitation, humidity          | CSV     | ✅ Certified     |

---

## 🧩 Data Workflow Overview

```mermaid
flowchart TD
  A["Raw Ecological Data<br/>(GBIF, USDA, EPA, MODIS, NOAA)"] --> B["Preprocessing & Cleaning<br/>(QC, CRS Alignment)"]
  B --> C["Standardization<br/>(Units, Taxonomy, Time Series)"]
  C --> D["Derived Metrics<br/>(SDM Inputs, Indices, Trends)"]
  D --> E["FAIR+CARE Validation<br/>+ ISO Telemetry Logging"]
```

---

## 🧮 FAIR+CARE Metadata Example

```json
{
  "dataset_id": "gbif-occurrences-kansas-2025",
  "title": "Global Biodiversity Information Facility (GBIF) — Species Occurrence Records for Kansas",
  "source_url": "https://www.gbif.org/occurrence/search?state=Kansas",
  "spatial_extent": [-102.05, 36.99, -94.6, 40.0],
  "temporal_coverage": ["1900-01-01", "2025-01-01"],
  "license": "CC-BY 4.0",
  "format": "CSV",
  "validation": {
    "integrity_check": "SHA-256 Verified",
    "missing_records": "1.8%",
    "duplicate_removed": 10542,
    "status": "Pass"
  },
  "auditor": "FAIR+CARE Council",
  "timestamp": "2025-11-09T16:55:00Z"
}
```

---

## ⚖️ FAIR+CARE Governance Matrix

| Principle        | Implementation                                         | Verification Source                             |
|------------------|--------------------------------------------------------|-------------------------------------------------|
| **Findable**     | Indexed via STAC/DCAT 3.0 metadata with UUIDs         | `metadata/stac_catalog.json`                    |
| **Accessible**   | Datasets distributed under CC‑BY / Open Data          | FAIR+CARE Ledger                                |
| **Interoperable**| CSV, NetCDF, GeoTIFF, and JSON‑LD formats             | `telemetry_schema`                              |
| **Reusable**     | Provenance, licensing, and telemetry embedded         | `manifest_ref`                                  |
| **Responsibility** | Energy/carbon telemetry validated via ISO 50001     | `telemetry_ref`                                 |
| **Ethics**       | Sensitive species locations masked ≥ 5 km             | FAIR+CARE Council Review                        |

---

## 🧾 Governance Ledger Record Example

```json
{
  "ledger_id": "ecology-datasets-ledger-2025-11-09-0161",
  "component": "Ecology Datasets Registry",
  "datasets": [
    "GBIF Biodiversity Occurrences",
    "USDA PLANTS / NRCS Ecology",
    "EPA Ecological Health",
    "NASA MODIS NDVI",
    "NOAA Climate Covariates"
  ],
  "energy_joules": 13.6,
  "carbon_gCO2e": 0.0053,
  "faircare_status": "Pass",
  "auditor": "FAIR+CARE Council",
  "timestamp": "2025-11-09T16:57:00Z"
}
```

---

## 🧠 Sustainability Metrics

| Metric                   | Description                                   | Value | Target | Unit   |
|--------------------------|-----------------------------------------------|------:|-------:|--------|
| **Energy (J)**           | Energy used during dataset ingestion & validation | 13.6 | ≤ 15   | Joules |
| **Carbon (gCO₂e)**       | Emissions per data workflow                   | 0.0053| ≤ 0.006| gCO₂e  |
| **Telemetry Coverage**   | FAIR+CARE trace completion                    | 100   | ≥ 95   | %      |
| **Audit Pass Rate**      | FAIR+CARE validation success                  | 100   | 100    | %      |

---

## 🕰️ Version History

| Version | Date       | Author                 | Summary                                                                                  |
|--------:|-----------:|------------------------|------------------------------------------------------------------------------------------|
| v11.2.4 | 2025-12-06 | FAIR+CARE Council      | Aligned ecology datasets registry with KFM‑MDP v11.2.4; added extended metadata + scope. |
| v10.2.2 | 2025-11-09 | FAIR+CARE Council      | Published ecology dataset registry with FAIR+CARE governance and ISO telemetry tracking. |
| v10.2.1 | 2025-11-09 | Ecological Data Governance Group | Added STAC/DCAT metadata schema and biodiversity ethics provisions.            |
| v10.2.0 | 2025-11-09 | KFM Ecology Team       | Created baseline dataset registry aligned with hydrology and climatology standards.      |

---

<div align="center">

© 2025 Kansas Frontier Matrix Project  
Master Coder Protocol v6.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Ecology Overview](../README.md) · [Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>