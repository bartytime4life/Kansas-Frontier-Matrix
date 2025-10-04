<div align="center">

# ⚠️ Kansas-Frontier-Matrix — Processed Hazards Metadata (`data/processed/hazards/metadata/`)

**Mission:** Maintain **metadata documentation** for all processed hazard datasets —  
floods, droughts, tornadoes, wildfires, and severe weather events — ensuring transparent  
provenance, schema compliance, and reproducibility for Kansas’s hazard history.

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

## 🌪️ Overview

This directory contains **metadata JSON records** for all processed hazard datasets  
stored in `data/processed/hazards/`.  

Each record captures **data lineage, processing parameters, software environment, and license details**,  
enabling reproducibility and long-term discoverability through the **Master Coder Protocol (MCP)**  
and the **SpatioTemporal Asset Catalog (STAC 1.0)**.

These files provide a transparent record of Kansas’s environmental hazards — ensuring that  
every flood extent, tornado track, and drought index is traceable from source to product.

---

## 🧱 Directory Layout

```bash
data/
└── processed/
    └── hazards/
        └── metadata/
            ├── tornado_tracks_1950_2024.json
            ├── fema_disasters_1953_2024.json
            ├── drought_spi12_1950_2024.json
            ├── wildfire_points_2000_2023.json
            ├── flood_events_1900_2020.json
            ├── template.json
            └── README.md
````

Each JSON metadata file corresponds to a dataset in `data/processed/hazards/`.
The `template.json` provides a reusable metadata skeleton consistent with MCP-STAC schemas.

---

## 🧩 Metadata Schema

All hazard metadata files follow the **hybrid MCP-STAC schema**, ensuring compatibility with
geospatial standards and reproducibility frameworks.

### Example Metadata File

```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "tornado_tracks_1950_2024",
  "properties": {
    "title": "Tornado Tracks (1950–2024) – Kansas",
    "datetime": "2024-01-01T00:00:00Z",
    "description": "Cleaned and merged tornado path dataset from NOAA SPC, including EF scale, track length, and fatalities.",
    "processing:software": "Python + GeoPandas + Shapely",
    "mcp_provenance": "sha256:a3c9b5...",
    "derived_from": [
      "data/raw/noaa_tornado_tracks.zip",
      "data/raw/noaa_storm_events.csv"
    ],
    "spatial_extent": [-102.05, 36.99, -94.59, 40.01],
    "temporal_extent": {
      "start": "1950-01-01",
      "end": "2024-12-31"
    },
    "license": "CC-BY 4.0",
    "keywords": ["tornado", "hazard", "Kansas", "NOAA", "severe weather"]
  },
  "assets": {
    "data": {
      "href": "../tornado_tracks_1950_2024.geojson",
      "type": "application/geo+json",
      "roles": ["data"]
    }
  }
}
```

### Required Metadata Fields

| Field                 | Description                          | Example                                                  |
| --------------------- | ------------------------------------ | -------------------------------------------------------- |
| `id`                  | Unique dataset identifier            | `"flood_events_1900_2020"`                               |
| `title`               | Human-readable dataset name          | `"Flood Events (1900–2020) – Kansas"`                    |
| `description`         | Summary of dataset contents          | `"Digitized flood polygons from USGS and FEMA archives"` |
| `datetime`            | Dataset or processing reference date | `"2020-12-31T00:00:00Z"`                                 |
| `derived_from`        | Source datasets                      | `["data/raw/usgs_floods.zip"]`                           |
| `processing:software` | Software stack used                  | `"GDAL 3.8.0 + Python GeoPandas"`                        |
| `mcp_provenance`      | SHA256 checksum reference            | `"sha256:d83a1f..."`                                     |
| `license`             | Data license (default CC-BY 4.0)     | `"CC-BY 4.0"`                                            |
| `spatial_extent`      | Bounding box [W, S, E, N]            | `[-102.05, 36.99, -94.59, 40.01]`                        |
| `temporal_extent`     | Period of record                     | `{"start": "1900-01-01", "end": "2020-12-31"}`           |

Optional fields include:

* `keywords` (array of thematic tags)
* `quality:metrics` (validation or confidence indicators)
* `hazard:type` (e.g., `"drought"`, `"flood"`, `"tornado"`)

---

## 🌐 STAC Integration

Each metadata file feeds directly into the **STAC catalog** (`data/stac/items/hazards_*`),
supporting search and filtering by hazard type, time range, or region.

STAC integration enables:

* **Interoperable catalog access** (via APIs and Python clients)
* **Time-aware mapping** of events in the Frontier Matrix web viewer
* **Metadata synchronization** with the project’s graph database

All metadata are validated against the STAC 1.0 JSON Schema before deployment.

---

## 🔍 Validation & Provenance

Validation ensures metadata accuracy and completeness through multiple checks:

1. **JSON Schema Validation:** Confirms required fields and formats.
2. **Checksum Verification:** Ensures `mcp_provenance` hashes match `.sha256` records.
3. **STAC Compliance:** Validates assets, types, and version numbers.
4. **Cross-Linkage:** Confirms all `derived_from` sources exist and are referenced in metadata.

Local validation command:

```bash
make validate-hazards
```

Results are logged to `validation_report.json`.

---

## 🧠 Adding or Updating Metadata

1. Copy `template.json` → rename to match dataset ID (e.g., `wildfire_points_2000_2023.json`).
2. Fill out required MCP and STAC fields (see schema above).
3. Add checksum reference under `mcp_provenance` using the dataset’s `.sha256` hash.
4. Validate:

   ```bash
   make validate-hazards
   ```
5. Commit changes and open a Pull Request — CI/CD will auto-run validation checks.

If updating a dataset (new version or expanded date range), ensure:

* `datetime` and `temporal_extent` are updated
* Corresponding `.sha256` checksum is regenerated

---

## 📖 References

* **NOAA Storm Events Database:** [https://www.ncei.noaa.gov/stormevents/](https://www.ncei.noaa.gov/stormevents/)
* **FEMA Disaster Declarations:** [https://www.fema.gov/openfema-data-page/disaster-declarations-summaries-v2](https://www.fema.gov/openfema-data-page/disaster-declarations-summaries-v2)
* **NASA FIRMS Fire Archive:** [https://firms.modaps.eosdis.nasa.gov/](https://firms.modaps.eosdis.nasa.gov/)
* **US Drought Monitor:** [https://droughtmonitor.unl.edu/](https://droughtmonitor.unl.edu/)
* **USGS Flood Hazards:** [https://www.usgs.gov/mission-areas/water-resources/science/floods](https://www.usgs.gov/mission-areas/water-resources/science/floods)
* **STAC Specification 1.0:** [https://stacspec.org](https://stacspec.org)
* **JSON Schema Specification:** [https://json-schema.org](https://json-schema.org)
* **Master Coder Protocol (MCP):** [`docs/standards/`](../../../../docs/standards/)

---

<div align="center">

*“Storms fade, fires cool, rivers recede — but these metadata preserve the memory of Kansas’s hazards for generations.”*

</div>
```

