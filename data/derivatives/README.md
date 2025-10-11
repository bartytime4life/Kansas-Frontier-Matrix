<div align="center">

# 🧭 Kansas Frontier Matrix — Derived Geospatial Products  
`data/derivatives/`

**Mission:** Maintain a **version-controlled repository** of **analysis-ready geospatial derivatives** —  
terrain, hydrology, land cover, hazards, and climate composites — generated reproducibly from canonical  
datasets in `data/cogs/` and `data/sources/`, validated under MCP and STAC governance.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../.github/workflows/codeql.yml)
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../.github/workflows/trivy.yml)
[![Pre-Commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](../../.github/workflows/pre-commit.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../LICENSE)
[![License: Code](https://img.shields.io/badge/License-MIT-yellow)](../../LICENSE)

</div>

---

## 📚 Table of Contents
- [Overview](#overview)
- [Directory Layout](#directory-layout)
- [Core Products](#core-products)
- [STAC Integration](#stac-integration)
- [Versioning Framework](#versioning-framework)
- [Reproducibility & Provenance](#reproducibility--provenance)
- [Contributing New Derivatives](#contributing-new-derivatives)
- [References](#references)
- [Version History](#version-history)

---

## 🗺️ Overview

The `data/derivatives/` directory hosts **versioned geospatial derivatives** derived from primary KFM data layers.  
These datasets support **research reproducibility**, **machine learning**, and **spatiotemporal visualization**.  

**Derivative Examples**
- 🏔️ **Terrain analytics:** slope, aspect, curvature, hillshade.  
- 💧 **Hydrology:** flow direction, accumulation, watershed boundaries.  
- 🌾 **Landcover:** vegetation indices (NDVI, NDWI), historical transitions.  
- ⚠️ **Hazards:** drought, wildfire, flood, and tornado frequency composites.  
- 🌦️ **Climate:** interpolated normals, anomaly rasters, and time-series grids.  

All derivatives are:
- **Reproducible** — generated via version-controlled ETL pipelines.  
- **Traceable** — each dataset includes lineage links in STAC metadata.  
- **Auditable** — validated by checksums and continuous integration workflows.

---

## 🧱 Directory Layout

```bash
data/
└── derivatives/
    ├── terrain/           # DEM-based slope, aspect, curvature
    ├── hydrology/         # Flow accumulation, drainage, basins
    ├── landcover/         # NDVI, land-use change, vegetation composites
    ├── hazards/           # Multi-hazard drought/flood/fire indices
    ├── climate/           # Climate normals and interpolations
    ├── metadata/          # JSON schema and STAC metadata
    ├── versions/          # Version manifests and changelogs
    ├── README.md          # (this file)
    └── .gitkeep
````

> **Note:** Large rasters use **DVC or Git LFS** tracking.
> Metadata, schemas, and checksums are committed directly for transparency.

---

## 🌐 Core Products

| Category      | Format            | Description                         | Example                                               |
| :------------ | :---------------- | :---------------------------------- | :---------------------------------------------------- |
| **Terrain**   | COG GeoTIFF       | Hillshade, slope, aspect, curvature | `terrain/slope_1m_ks_v1.2.tif`                        |
| **Hydrology** | GeoTIFF + GeoJSON | Flow direction and drainage network | `hydrology/flowdir_ks_v2.0.tif`, `streams_v2.geojson` |
| **Landcover** | COG GeoTIFF       | NLCD change and vegetation indices  | `landcover/nlcd_change_1992_2021_v1.0.tif`            |
| **Hazards**   | GeoTIFF           | Flood or drought hazard composites  | `hazards/flood_frequency_1950_2025_v1.1.tif`          |
| **Climate**   | CSV + Parquet     | Climate normals and anomalies       | `climate/temp_normals_1991_2020_v1.3.parquet`         |

Each filename encodes a **semantic version number** (`_vX.Y`), synchronized with STAC metadata and version manifests.

---

## 🧩 STAC Integration

Each derivative dataset is described and versioned via a **STAC Item** in `data/stac/items/`.

**Example:**

```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "terrain_slope_1m_ks_v1.2",
  "properties": {
    "datetime": "2020-01-01T00:00:00Z",
    "description": "1m statewide slope layer derived from Kansas LiDAR DEM",
    "kfm_version": "v1.2.0",
    "etl_commit": "4e9b5d9",
    "derived_from": [
      "data/cogs/terrain/ks_dem_1m_2018_2020_v1.0.tif"
    ],
    "mcp_provenance": "sha256:f1d2d2f924e986ac86fdf7b36c94bcdf32beec15",
    "license": "CC-BY 4.0"
  },
  "assets": {
    "data": {
      "href": "../terrain/slope_1m_ks_v1.2.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized"
    }
  }
}
```

All STAC metadata includes **`kfm_version`**, **`derived_from`**, and **`etl_commit`** fields
to maintain direct lineage between versions and datasets.

---

## 🧮 Versioning Framework

The **KFM Derivative Versioning System (KDVS)** ensures clarity between revisions, releases, and rebuilds:

| Version Type | Scope                                  | Example  | Trigger                            |
| :----------- | :------------------------------------- | :------- | :--------------------------------- |
| **Patch**    | Metadata or checksum fix               | `v1.2.1` | Typo correction or schema update   |
| **Minor**    | Recalculation or algorithm improvement | `v1.3.0` | Improved slope or interpolation    |
| **Major**    | Structural or source dataset overhaul  | `v2.0.0` | New DEM input or pipeline refactor |

### Version Manifests

Each release generates an entry in `data/derivatives/versions/manifest.json`:

```json
{
  "id": "terrain_slope_1m_ks",
  "latest_version": "v1.2.0",
  "changelog": [
    { "version": "v1.0.0", "date": "2025-10-01", "changes": "Initial release" },
    { "version": "v1.1.0", "date": "2025-10-07", "changes": "Added shadow correction" },
    { "version": "v1.2.0", "date": "2025-10-10", "changes": "Recomputed curvature using improved DEM" }
  ]
}
```

> 🧾 Version manifests provide consistent tracking of all derivative datasets for STAC and MCP validation.

---

## 🔁 Reproducibility & Provenance

| Component         | Description                                                        |
| :---------------- | :----------------------------------------------------------------- |
| **Make Targets**  | `make derivatives` rebuilds all products deterministically.        |
| **Checksums**     | Each derivative includes a `.sha256` sidecar for binary integrity. |
| **Schemas**       | JSON Schemas enforce STAC and KFM metadata standards.              |
| **Version Links** | `"derived_from"` and `"kfm_version"` ensure traceable lineage.     |
| **Audit Logs**    | Stored in `data/work/tmp/logs/` for pipeline traceability.         |

---

## 🧠 Contributing New Derivatives

1. Create a new subfolder in `data/derivatives/<domain>/`.
2. Export your dataset in **open, standardized formats** (COG, GeoJSON, CSV, Parquet).
3. Generate a `.sha256` checksum file for reproducibility.
4. Add a STAC item JSON with:

   * `id`, `version`, and `derived_from`
   * `etl_commit` (Git hash)
   * License and metadata fields
5. Document the derivation method in a `DERIVATION.md` file.
6. Register the derivative in `versions/manifest.json`.
7. Run automated validation:

```bash
make validate
make stac-validate
```

> ✅ CI will fail automatically if STAC or version metadata are missing or inconsistent.

---

## 🧩 MCP Compliance Summary

| MCP Principle           | Implementation                                                          |
| :---------------------- | :---------------------------------------------------------------------- |
| **Documentation-first** | Each derivative includes README, version manifest, and STAC references. |
| **Reproducibility**     | Deterministic ETL ensures identical results across runs.                |
| **Open Standards**      | Follows GeoTIFF (COG), GeoJSON, CSV, and STAC 1.0.                      |
| **Provenance**          | Versioned lineage links connect all derived assets to source data.      |
| **Auditability**        | Checksums, manifests, and CI logs ensure full traceability.             |

---

## 📅 Version History

| Version | Date       | Summary                                                                         |
| :------ | :--------- | :------------------------------------------------------------------------------ |
| v1.0.0  | 2025-10-04 | Initial release of derived product documentation.                               |
| v1.1.0  | 2025-10-08 | Added expanded STAC integration and example manifest.                           |
| v1.2.0  | 2025-10-10 | Introduced formal versioning system (KDVS) with manifests and lineage tracking. |

---

## 🔍 References

* [**STAC 1.0.0 Specification**](https://stacspec.org)
* [**OGC GeoTIFF & Cloud-Optimized GeoTIFF**](https://www.cogeo.org/)
* [**GeoJSON RFC 7946**](https://datatracker.ietf.org/doc/html/rfc7946)
* [**Master Coder Protocol (MCP)** — Documentation Standards](../../docs/standards/)
* [**USGS 3DEP LiDAR & DEM Program**](https://www.usgs.gov/3dep)
* [**Kansas DASC GIS Hub**](https://www.kansasgis.org/)

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Derived Layer Tells a Story — Versioned, Verified, and Reproducible.”*
📍 [`data/derivatives/`](.) · MCP-compliant repository for version-controlled geospatial derivatives.

</div>
```
