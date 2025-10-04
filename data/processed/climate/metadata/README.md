<div align="center">

# 🌦️ Kansas-Frontier-Matrix — Processed Climate Metadata (`data/processed/climate/metadata/`)

**Mission:** Maintain **metadata records** for all processed climate datasets — documenting provenance,  
data lineage, spatial and temporal coverage, and processing software — ensuring every climate grid or  
timeseries in Kansas Frontier Matrix is fully auditable and reproducible.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../../.github/workflows/codeql.yml)
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)
[![License: Code](https://img.shields.io/badge/License-MIT-yellow)](../../../../LICENSE)

</div>

---

## 📚 Table of Contents
- [Overview](#overview)
- [Directory Layout](#directory-layout)
- [Metadata Schema](#metadata-schema)
- [STAC Integration](#stac-integration)
- [Validation & Provenance](#validation--provenance)
- [Adding or Updating Metadata](#adding-or-updating-metadata)
- [References](#references)

---

## 🧠 Overview

This directory contains **JSON metadata records** for all processed climate datasets  
found in `data/processed/climate/`. Each file describes a specific dataset’s attributes —  
including source lineage, temporal coverage, processing tools, and checksum provenance —  
providing a transparent record for scientific reproducibility.

These metadata files act as the authoritative **climate dataset registry** within  
the Kansas Frontier Matrix framework, used to populate the STAC catalog and MCP provenance chain.

---

## 🧱 Directory Layout

```bash
data/
└── processed/
    └── climate/
        └── metadata/
            ├── temp_mean_annual_1895_2024.json
            ├── precip_total_annual_1895_2024.json
            ├── drought_spi12_1895_2024.json
            ├── climate_normals_1991_2020.json
            ├── template.json
            └── README.md
````

Each file documents one processed dataset stored in `data/processed/climate/`.
A `template.json` is provided for new metadata creation following MCP + STAC schemas.

---

## 🧩 Metadata Schema

Each metadata file follows the **MCP-STAC hybrid schema** shared across Kansas Frontier Matrix.
It defines the dataset’s provenance, spatial-temporal extent, and reproducibility context.

### Example

```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "precip_total_annual_1895_2024",
  "properties": {
    "title": "Total Annual Precipitation (1895–2024) – Kansas",
    "datetime": "2024-01-01T00:00:00Z",
    "description": "Gridded total annual precipitation for Kansas aggregated from NOAA and PRISM datasets (1895–2024).",
    "processing:software": "Python + xarray + rasterio + GDAL 3.8.0",
    "mcp_provenance": "sha256:4bd72e...",
    "license": "CC-BY 4.0",
    "derived_from": [
      "data/raw/noaa_precip_1895_2024.csv",
      "data/raw/prism_precip_monthly.nc"
    ],
    "temporal_extent": {
      "start": "1895-01-01",
      "end": "2024-12-31"
    },
    "spatial_extent": [-102.05, 36.99, -94.59, 40.01],
    "keywords": ["precipitation", "climate", "Kansas", "PRISM", "NOAA"]
  },
  "assets": {
    "data": {
      "href": "../precip_total_annual_1895_2024.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["data"]
    }
  }
}
```

### Required Metadata Fields

| Field                 | Description                               | Example                                          |
| --------------------- | ----------------------------------------- | ------------------------------------------------ |
| `id`                  | Unique dataset identifier                 | `"temp_mean_annual_1895_2024"`                   |
| `title`               | Human-readable dataset title              | `"Mean Annual Temperature (1895–2024) – Kansas"` |
| `description`         | Short description of dataset content      | `"Derived from NOAA and PRISM sources"`          |
| `datetime`            | Processing date or dataset reference date | `"2024-01-01T00:00:00Z"`                         |
| `derived_from`        | Source datasets                           | `["data/raw/prism_temp.nc"]`                     |
| `processing:software` | Tools used for data creation              | `"Python + xarray + rasterio"`                   |
| `mcp_provenance`      | SHA-256 checksum reference                | `"sha256:de23a9..."`                             |
| `license`             | License type                              | `"CC-BY 4.0"`                                    |
| `spatial_extent`      | Bounding box [W, S, E, N]                 | `[-102.05, 36.99, -94.59, 40.01]`                |
| `temporal_extent`     | Start and end date                        | `{"start": "1895-01-01", "end": "2024-12-31"}`   |

---

## 🌐 STAC Integration

Each metadata JSON is synchronized with the project-wide **STAC catalog** under
`data/stac/items/climate_*`. These entries allow:

* Spatial filtering of climate datasets by bounding box
* Temporal filtering by observation period
* Search by tag (e.g., “precipitation”, “drought”)
* Direct data linking for web applications and notebooks

The project’s CI automatically rebuilds STAC indexes whenever new metadata is added.

---

## 🔍 Validation & Provenance

Validation steps ensure that each file adheres to STAC and MCP standards:

1. **JSON Schema Validation:** Confirms required fields and value types.
2. **Checksum Validation:** Confirms the `mcp_provenance` hash matches the `.sha256` checksum file.
3. **Temporal Validation:** Ensures `temporal_extent` aligns with dataset content.
4. **License Compliance:** Verifies declared licenses align with source datasets.

Run local validation:

```bash
make validate-climate
```

Results are logged in `validation_report.json` in this directory.

---

## 🧠 Adding or Updating Metadata

1. Copy `template.json` → rename appropriately (e.g. `temp_mean_annual_1895_2024.json`).
2. Fill in all required fields (see table above).
3. Add checksum from the processed file’s `.sha256`.
4. Validate:

   ```bash
   make validate-climate
   ```
5. Commit and open a Pull Request. CI/CD will automatically validate schema compliance.

If data are reprocessed, update both:

* The dataset’s checksum (`.sha256`)
* The metadata `mcp_provenance` and `datetime` fields

---

## 📖 References

* **STAC Specification 1.0:** [https://stacspec.org](https://stacspec.org)
* **NOAA National Centers for Environmental Information (NCEI):** [https://www.ncei.noaa.gov/](https://www.ncei.noaa.gov/)
* **PRISM Climate Group:** [https://prism.oregonstate.edu/](https://prism.oregonstate.edu/)
* **NASA Daymet:** [https://daac.ornl.gov/DAYMET/](https://daac.ornl.gov/DAYMET/)
* **xarray Documentation:** [https://docs.xarray.dev/](https://docs.xarray.dev/)
* **JSON Schema Specification:** [https://json-schema.org](https://json-schema.org)
* **Master Coder Protocol (MCP):** [`docs/standards/`](../../../../docs/standards/)

---

<div align="center">

*“Every temperature, every raindrop — these metadata records preserve the provenance of Kansas’s climate story.”*

</div>
```

