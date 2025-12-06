---
title: "🌿 Kansas Frontier Matrix — Ecology Raw Datasets (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/ecology/datasets/raw/README.md"
version: "v11.2.4"
last_updated: "2025-12-06"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x raw-datasets compatible"
status: "Active / Enforced"

doc_kind: "DatasetCollection"
intent: "ecology-raw-datasets"
role: "raw-datasets-registry"
header_profile: "standard"
footer_profile: "standard"

scope:
  domain: "ecology"
  applies_to:
    - "datasets"
    - "etl"
    - "analysis"
    - "stac"
    - "provenance"
    - "telemetry"
    - "governance"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Ecology (masked for sensitive biodiversity)"
sensitivity: "General (raw; potential sensitive species locations)"
sensitivity_level: "Medium"
public_exposure_risk: "Medium"
classification: "KFM-Open"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
risk_category: "Ecology · Raw Data"
redaction_required: true

commit_sha: "<latest-commit-hash>"
previous_version_hash: "docs/analyses/ecology/datasets/raw/README.md@v10.2.2"
doc_integrity_checksum: "<sha256-of-this-file>"

sbom_ref: "../../../../../../releases/v11.2.4/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.4/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.2.4/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/analyses-ecology-datasets-raw-v3.json"
governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"

ontology_alignment:
  cidoc: "E73 Information Object"
  schema_org: "Dataset"
  prov_o: "prov:Collection"
  owl_time: "ProperInterval"

json_schema_ref: "schemas/json/docs-analyses-ecology-datasets-raw-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/docs-analyses-ecology-datasets-raw-v11.2.4-shape.ttl"

doc_uuid: "urn:kfm:doc:analyses:ecology:datasets:raw:v11.2.4"
semantic_document_id: "kfm-analyses-ecology-datasets-raw-v11.2.4"
event_source_id: "ledger:kfm:doc:analyses:ecology:datasets:raw:v11.2.4"

immutability_status: "version-pinned"

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
sunset_policy: "Superseded upon next ecology raw-datasets revision"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "metadata-check"
  - "provenance-check"
  - "footer-check"
  - "accessibility-check"
---

<div align="center">

# 🌿 **Kansas Frontier Matrix — Ecology Raw Datasets**  
`docs/analyses/ecology/datasets/raw/README.md`

**Purpose:**  
List and describe the **unaltered biodiversity, land cover, and ecological datasets** sourced for Kansas Frontier Matrix (KFM) analyses.  
These raw datasets are directly retrieved from authoritative sources (GBIF, USDA, EPA, NASA, NOAA) and governed under **FAIR+CARE**, **STAC/DCAT 3.0**, and **ISO 19115** standards to ensure data integrity and transparency.

[![Docs · MCP_v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../../../README.md)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../../../LICENSE)  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Ecology_Raw-orange)](../../../../../../docs/standards/README.md)  
[![Status](https://img.shields.io/badge/Status-Active_Data-brightgreen)](../../../../../../releases/v11.2.4/manifest.zip)

</div>

---

## 📘 Overview

This directory contains **raw, unmodified ecological data** forming the foundation of biodiversity, habitat, and ecosystem modeling within the Kansas Frontier Matrix.  
Each dataset includes metadata provenance, checksum verification, and licensing details compliant with **FAIR+CARE** and **ISO geospatial standards**.

Raw datasets are used as inputs for:

- Species Distribution Modeling (SDM)  
- Habitat connectivity & landcover change analysis  
- Ecosystem service valuation  
- Cross‑domain analyses in `docs/analyses/cross-domain/`  

They flow into:

- **Processed datasets** → `docs/analyses/ecology/datasets/processed/`  
- **Derived datasets** → `docs/analyses/ecology/datasets/derived/`  
- **Metadata registry** → `docs/analyses/ecology/datasets/metadata/`  

---

## 🗂️ Directory Layout

```plaintext
docs/analyses/ecology/datasets/raw/
├── 📘 README.md                      # This document (raw datasets registry)
├── 🧬 gbif_occurrences.csv           # Species occurrence data from GBIF
├── 🌿 usda_plants.csv                # Ecological site data from USDA PLANTS Database
├── 💧 epa_ecological_health.csv      # Aquatic and ecological condition indices
├── 🛰️ modis_ndvi.nc                  # NASA MODIS NDVI time series for vegetation
└── 🌦️ noaa_climate_covariates.csv    # Climate variables from NOAA NCEI
```

---

## ⚙️ Dataset Descriptions

| File                               | Source         | Description                                              | Temporal Range | Spatial Resolution     | License      |
|------------------------------------|----------------|----------------------------------------------------------|----------------|------------------------|-------------|
| **gbif_occurrences.csv**          | GBIF           | Global biodiversity occurrence records for Kansas species | 1900–2025     | Point                  | CC-BY 4.0    |
| **usda_plants.csv**               | USDA / NRCS    | Plant species distributions and ecological site data     | 1950–2025      | County-level           | Public Domain |
| **epa_ecological_health.csv**     | EPA / USGS     | Aquatic ecosystem health indices (IBI, habitat quality)  | 1970–2025      | River reach / basin    | Public Domain |
| **modis_ndvi.nc**                 | NASA MODIS     | Monthly NDVI and EVI vegetation indices                  | 2000–2025      | 250 m grid             | CC-BY 4.0    |
| **noaa_climate_covariates.csv**   | NOAA NCEI      | Climate covariates for ecological modeling               | 1880–2025      | Grid / station         | Public Domain |

All raw datasets are:

- stored **exactly as delivered** by upstream providers  
- validated through **checksum verification** and FAIR+CARE metadata ingestion pipelines  
- tagged with **CARE-aware masking requirements** for sensitive biodiversity content  

---

## 🧩 Ingestion & Provenance Workflow

```mermaid
flowchart TD
  A["Raw Ecological Data (GBIF / USDA / EPA / NASA / NOAA)"] --> B["Integrity Verification (Checksum + License Validation)"]
  B --> C["Metadata Registration (STAC/DCAT + FAIR+CARE)"]
  C --> D["Governance Ledger Sync + ISO 50001 / 14064 Telemetry Logging"]
  D --> E["Promotion to Processed Datasets (ETL Pipelines)"]
```

---

## 🧮 FAIR+CARE Metadata Example

```json
{
  "dataset_id": "gbif-occurrences-ks-2025",
  "title": "GBIF Species Occurrence Records for Kansas",
  "source_url": "https://www.gbif.org/occurrence/search?state=Kansas",
  "spatial_extent": [-102.05, 36.99, -94.6, 40.0],
  "temporal_coverage": ["1900-01-01", "2025-01-01"],
  "format": "CSV",
  "license": "CC-BY 4.0",
  "validation": {
    "integrity_check": "SHA-256 Verified",
    "missing_records": "2.3%",
    "duplicates_removed": 11458,
    "status": "Pass"
  },
  "auditor": "FAIR+CARE Council",
  "timestamp": "2025-11-09T17:00:00Z"
}
```

---

## ⚖️ FAIR+CARE Governance Matrix

| Principle         | Implementation                                               | Verification Source                  |
|-------------------|-------------------------------------------------------------|--------------------------------------|
| **Findable**      | Indexed in STAC/DCAT catalogs with persistent UUIDs         | `metadata/stac_catalog.json`         |
| **Accessible**    | Public datasets released under FAIR+CARE governance         | FAIR+CARE Ledger                     |
| **Interoperable** | Open formats (CSV, NetCDF, GeoTIFF)                         | `telemetry_schema`                   |
| **Reusable**      | Provenance and checksum metadata embedded                   | `manifest_ref`                       |
| **Responsibility**| Energy and carbon telemetry logged per ingestion workflow   | `telemetry_ref`                      |
| **Ethics**        | Sensitive species coordinates generalized ≥ 5 km            | FAIR+CARE Council Ethics Audit       |

---

## 🧾 Governance Ledger Record Example

```json
{
  "ledger_id": "ecology-raw-ledger-2025-11-09-0162",
  "component": "Ecology Raw Datasets Registry",
  "datasets": [
    "GBIF Biodiversity Occurrences",
    "USDA PLANTS",
    "EPA Ecological Health",
    "NASA MODIS NDVI",
    "NOAA Climate Covariates"
  ],
  "energy_joules": 11.5,
  "carbon_gCO2e": 0.0047,
  "faircare_status": "Pass",
  "auditor": "FAIR+CARE Council",
  "timestamp": "2025-11-09T17:02:00Z"
}
```

---

## 🧠 Sustainability Metrics

| Metric                 | Description                            | Value | Target | Unit   |
|------------------------|----------------------------------------|------:|-------:|--------|
| **Energy (J)**         | Energy consumed during dataset ingestion | 11.5 | ≤ 15   | Joules |
| **Carbon (gCO₂e)**     | Emissions equivalent per ingestion      | 0.0047 | ≤ 0.006 | gCO₂e |
| **Telemetry Coverage** | FAIR+CARE traceability completion       | 100   | ≥ 95   | %      |
| **Audit Pass Rate**    | FAIR+CARE compliance success            | 100   | 100    | %      |

---

## 🕰️ Version History

| Version | Date       | Author              | Summary                                                                                     |
|--------:|-----------:|---------------------|---------------------------------------------------------------------------------------------|
| v11.2.4 | 2025-12-06 | FAIR+CARE Council   | Upgraded ecology raw datasets registry to KFM‑MDP v11.2.4; added scope, lifecycle, emoji directory layout, and governance metadata. |
| v10.2.2 | 2025-11-09 | FAIR+CARE Council   | Published ecology raw dataset documentation with FAIR+CARE validation and telemetry tracking. |
| v10.2.1 | 2025-11-09 | Ecological Data Team| Added ingestion workflow and dataset metadata example.                                      |
| v10.2.0 | 2025-11-09 | KFM Ecology Group   | Created baseline raw dataset documentation aligned with climatology and hydrology standards. |

---

<div align="center">

© 2025 Kansas Frontier Matrix Project  
Master Coder Protocol v6.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Ecology Datasets](../README.md) · [Governance Charter](../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>