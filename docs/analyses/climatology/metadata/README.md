---
title: "🌦️ Kansas Frontier Matrix — Climatology Metadata Standards (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/climatology/metadata/README.md"
version: "v10.4.0"
last_updated: "2025-11-17"
review_cycle: "Biannual / Climatology Working Group · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/climatology-metadata-v1.json"
governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Metadata Standard"
intent: "climatology-metadata"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🌦️ **Kansas Frontier Matrix — Climatology Metadata Standards**  
`docs/analyses/climatology/metadata/README.md`

**Purpose:**  
Define the **complete metadata specification** for all climatology datasets, derived products, analyses, visualizations, and forecast models used within the Kansas Frontier Matrix (KFM).  
Ensures compliance with **FAIR+CARE**, **STAC 1.0**, **DCAT 3.0**, **CF-Conventions**, **ISO 19115**, and **MCP-DL v6.3**.

These standards guarantee that all climate-related layers—historical, contemporary, and predictive—remain reproducible, documented, ethically governed, and machine-discoverable across the KFM ecosystem.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../README.md)  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../../../standards/faircare.md)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)  
[![Status: Active](https://img.shields.io/badge/Status-Active-success)](../../../../releases/v10.4.0/manifest.zip)

</div>

---

## 📘 Overview

Climatology metadata in KFM covers:

- **Historical climate datasets** (NOAA GHCN-D, Daymet, PRISM, Kansas Mesonet)  
- **Environmental indices** (SPI, SPEI, PDSI, drought classifications)  
- **Hydroclimate datasets** (precipitation, snow water equivalent, streamflow)  
- **Derived rasters** (anomaly maps, degree-day surfaces, kernel density precipitation events)  
- **Predictive model outputs** (CMIP6 downscaled forecasts, AI-based projections)  
- **Spatiotemporal climate layers** for MapLibre, Cesium, and Focus Mode v2  

All climatology metadata must satisfy:

- Machine-readability  
- Full provenance  
- Reproducibility  
- Ethical framing (FAIR+CARE)  
- Accessibility requirements  
- Integration with **KFM Knowledge Graph**

---

## 🗂️ Directory Layout

~~~text
docs/analyses/climatology/metadata/
├── README.md                       # This file
├── stac/                           # STAC Items & Collections for climate data
├── dcat/                           # DCAT dataset descriptions
├── provenance/                     # PROV-O lineage logs for each dataset
├── schemas/                        # JSON schemas for climate metadata validation
├── variables/                      # CF-Conventions variable dictionaries
└── examples/                       # Sample metadata files + annotated examples
~~~

---

## 📦 Required Metadata Components

Every climatology dataset MUST include the following metadata structures:

### ✔ STAC 1.0 Item / Collection  
Required fields:

| Field | Description |
|---|---|
| `id` | Globally unique dataset identifier |
| `bbox` | Spatial extent |
| `geometry` | Coverage footprint |
| `datetime` or `start_datetime` + `end_datetime` | Temporal coverage |
| `assets` | Links to rasters, tables, or models |
| `proj:*` | CRS, transform, shape |
| `kfm:variable` | CF variable key |
| `care:sensitivity` | CARE sensitivity label |
| `kfm:provenance` | PROV-O reference |

### ✔ DCAT 3.0 Dataset  
Required fields:

| DCAT Field | Example Entry |
|---|---|
| `dct:title` | "Kansas Precipitation Anomalies (1895–2024)" |
| `dct:license` | `"CC-BY 4.0"` |
| `dcat:keyword` | `["climate", "precipitation", "drought"]` |
| `dct:temporal` | Time range (OWL-Time compatible) |
| `dcat:distribution` | COG/GeoJSON/NetCDF endpoints |

### ✔ PROV-O Lineage  
Every file must capture:

- `prov:wasGeneratedBy` → Model / script / notebook  
- `prov:used` → Source datasets  
- `prov:wasDerivedFrom` → Parent dataset IDs  
- Timestamps + parameter logs  

### ✔ CF-Conventions Climate Variables  
Each variable must declare:

| Element | Example |
|---|---|
| `standard_name` | `air_temperature` |
| `long_name` | "Daily maximum near-surface air temperature" |
| `units` | `"degC"` |
| `cell_methods` | `"time: mean"` |
| `grid_mapping` | `"latitude_longitude"` |

---

## 🧭 Metadata Categories

| Category | Description | Examples |
|---|---|---|
| **Historical Observational Data** | Raw sensor & weather station data | GHCN-D, Mesonet |
| **Derived Climate Products** | Computed eco/climate indicators | SPI, SPEI, anomalies |
| **Remote Sensing Climate Data** | Gridded rasters | Daymet, PRISM |
| **Paleoclimate Reconstructions** | Proxy datasets | Drought atlas tree rings |
| **AI & ML Climate Models** | KFM predictive ETL outputs | Transformer v2 forecasts |
| **Hydroclimate Datasets** | Water-related climate | Streamflow, SWE, soil moisture |

---

## 🗺️ Spatial Metadata Requirements

Every climatology dataset must include:

| Requirement | Standard |
|---|---|
| CRS | EPSG:4326 (default) or documented alternative |
| BBOX | Four-value min/max lat/long |
| Geometry | GeoJSON polygon or multipolygon |
| Pixel Alignment | If raster → `proj:transform` defined |
| Resolution | Explicit (e.g., 1km Daymet, 4km PRISM) |
| Spatial Sensitivity | CARE classification, if environmental justice areas affected |

---

## 🕰️ Temporal Metadata Requirements

| Requirement | Standard |
|---|---|
| Interval | OWL-Time (`time:hasBeginning`, `time:hasEnd`) |
| Precision | `"year"`, `"month"`, `"day"`, `"hour"` |
| Time Zone | UTC for all timestamps |
| Multi-era Linked Data | Tags historical, modern, and predictive layers distinctly |
| Publication Date | ISO 8601 date |
| Update Frequency | `"daily"`, `"annual"`, `"static"`, `"model-run"` |

---

## 🔗 Provenance Metadata (PROV-O)

Required chain:

~~~text
Raw Inputs → Transform Steps → Derived Product → Validation → Publication
~~~

Stored in:

- `provenance/` JSON-LD files  
- Embedded in STAC with `"kfm:provenance"`  
- Linked to notebooks in `docs/analyses/climatology/results/`  

---

## 🧪 Validation Requirements

Climatology metadata **must** pass:

- **STAC Item validation**
- **DCAT JSON schema validation**
- **CF variable validation**
- **Provenance completeness**
- **Fair+CARE environmental & climate ethics**
- **Reproducibility check** (parameters, versions, seeds)
- **Accessibility metadata** (alt text, captioning for figures)

Validation workflows are defined in:

- `docs/analyses/climatology/validation/`  
- `docs/accessibility/audits/`  
- `.github/workflows/climate-metadata-validate.yml`

---

## 📊 Example Metadata Snippet (STAC)

~~~json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "kfm-temp-anomaly-1895-2024",
  "bbox": [-102.05, 37.0, -94.6, 40.0],
  "properties": {
    "start_datetime": "1895-01-01T00:00:00Z",
    "end_datetime": "2024-12-31T00:00:00Z",
    "kfm:variable": "temperature_anomaly",
    "care:sensitivity": "general",
    "kfm:provenance": "provenance/temp-anomaly-derivation.json"
  },
  "assets": {
    "rasters": {
      "href": "https://example.com/climate/temp_anomaly_1895_2024.tif",
      "type": "image/tiff; application=geotiff",
      "roles": ["data"]
    }
  }
}
~~~

---

## ⚖️ FAIR+CARE Climate Metadata Constraints

To protect communities and ensure ethical modeling:

- Climate visualizations in environmental justice areas must include **CARE labels**.  
- Predictive climate layers must be tagged **speculative** or **scenario-based**.  
- AI-generated forecasts must include:
  - Model version  
  - Seed  
  - Training datasets  
  - Known biases or uncertainties  

Forbidden:

- Misrepresentation of climate projections  
- Uncontextualized doom framing  
- Non-attributed environmental data  
- Predictive content without uncertainty metrics  

---

## 🧠 Integration Into KFM Ecosystem

Climatology metadata drives:

- Map layers (`climate/`, `hazards/`, `hydrology/`)  
- Focus Mode v2 climate context  
- Story Nodes (climate timelines, drought sequences)  
- Predictive ETL pipelines  
- Knowledge Graph nodes:
  - `ClimateEvent`
  - `DroughtPeriod`
  - `TemperatureRecord`
  - `HydroEvent`

AI layers depend on robust metadata for explainability overlays.

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v10.4.0 | 2025-11-17 | Climatology WG · FAIR+CARE Council | Established climate metadata standards; added STAC/DCAT/CF/CARE requirements; ensured box-safe formatting |
| v10.0.0 | 2025-11-10 | Climatology Metadata Team | Initial draft for metadata specification |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE Certified · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[⬅ Back to Climatology Analysis](../README.md)

</div>
