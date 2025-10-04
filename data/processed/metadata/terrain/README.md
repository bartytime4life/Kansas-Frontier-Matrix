<div align="center">

# 🏔️ Kansas Frontier Matrix — Terrain Metadata (`data/processed/metadata/terrain/`)

**Mission:** Document, organize, and standardize all **terrain-related processed data layers**  
for the Kansas Frontier Matrix spatiotemporal knowledge hub — ensuring full provenance,  
semantic alignment, and reproducible ETL lineage.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../.github/workflows/codeql.yml)
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../.github/workflows/trivy.yml)
[![Pre-Commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen.svg)](https://pre-commit.com/)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../LICENSE)

</div>

---

## 📚 Overview

This directory contains **metadata documentation** for all processed **terrain datasets**  
used in Kansas-Frontier-Matrix (KFM). It defines the provenance, STAC metadata,  
spatial coverage, coordinate systems, and lineage for **elevation-based geospatial layers**  
such as DEMs, hillshade rasters, slope/aspect grids, and historical topography.

All terrain layers are derived through reproducible ETL pipelines defined in the  
`Makefile` and Python scripts under `src/pipelines/terrain/`.

---

## 🗺️ Terrain Layers (Processed Assets)

| Layer | Source | Format | Spatial Resolution | Temporal Coverage | Output |
|-------|---------|---------|--------------------|------------------|---------|
| **DEM (1 m LiDAR, 2018–2020)** | KS DASC / USGS 3DEP | GeoTIFF → COG | 1 m | 2018–2020 | `data/processed/terrain/ks_1m_dem_2018_2020.tif` |
| **Hillshade (Derived)** | Derived from DEM | GeoTIFF → COG | 1 m | 2018–2020 | `data/processed/terrain/ks_hillshade_2018_2020.tif` |
| **Slope / Aspect Maps** | Derived | GeoTIFF → COG | 1 m | 2018–2020 | `data/processed/terrain/slope_aspect_2018_2020.tif` |
| **Historic Topo Overlays (1890s–1950s)** | USGS Historical Topo | GeoTIFF → COG | 1:62 500–1:125 000 | 1894–1950 | `data/processed/terrain/usgs_topo_*.tif` |

All processed rasters follow **Cloud-Optimized GeoTIFF (COG)** standards and  
are referenced in the project’s **STAC catalog** (`data/stac/terrain/`).

---

## 🧭 Metadata Schema

Each dataset here is accompanied by a **JSON sidecar** (`.json`)  
conforming to the **SpatioTemporal Asset Catalog (STAC 1.0.0)** specification:

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "ks_1m_dem_2018_2020",
  "properties": {
    "title": "Kansas LiDAR Digital Elevation Model (1m, 2018–2020)",
    "datetime": "2020-01-01T00:00:00Z",
    "providers": [
      {"name": "Kansas DASC", "roles": ["producer"]},
      {"name": "USGS 3DEP", "roles": ["licensor"]}
    ],
    "created": "2025-10-01T00:00:00Z",
    "license": "Public Domain (US Gov)",
    "proj:epsg": 4326,
    "raster:bands": [
      {"name": "elevation", "data_type": "float32", "unit": "meters"}
    ]
  },
  "assets": {
    "data": {
      "href": "../terrain/ks_1m_dem_2018_2020.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["data"]
    },
    "thumbnail": {"href": "../thumbnails/ks_1m_dem_2018_2020.png"}
  },
  "bbox": [-102.05, 36.99, -94.59, 40.00],
  "geometry": null
}
````

---

## 🧩 Semantic Alignment

Terrain datasets align with **CIDOC CRM** and **OWL-Time** classes for
cross-domain interoperability:

| Entity                | Ontology Mapping                                  | Example                        |
| --------------------- | ------------------------------------------------- | ------------------------------ |
| Elevation raster      | `E73_Information_Object` → `E25_Man-Made_Feature` | Digital elevation model        |
| Hillshade / slope map | `E73` + `E29_Design_or_Procedure`                 | Derived visualization products |
| Acquisition date      | `P4_has_time-span` / OWL-Time interval            | `2018-01-01` → `2020-12-31`    |

---

## 🧰 ETL & Processing Notes

* **Pipeline:**
  `make terrain` → runs `src/pipelines/terrain/terrain_pipeline.py`
* **Dependencies:**
  `rasterio`, `rio-cogeo`, `gdal`, `numpy`, `pyproj`
* **Transform Steps:**

  1. Fetch raw DEM tiles from Kansas LiDAR service.
  2. Merge → reproject to EPSG 4326.
  3. Generate hillshade, slope, aspect derivatives.
  4. Convert to COG with `rio cogeo create`.
  5. Write checksum (`.sha256`) and STAC item.
  6. Validate with `make stac-validate`.

All steps are logged with timestamps and checksums for **MCP-grade reproducibility**.

---

## 🧮 Provenance & Validation

* **Checksums:** `.sha256` sidecars for every file
* **Validation:** JSON Schema + STAC validator in CI
* **Licenses:** KS DASC / USGS data → Public Domain;
  Derived products → CC-BY 4.0 with attribution
* **Source URLs:** see `data/sources/terrain/*.json`

---

## 🔗 Connections & Use

Terrain metadata links directly into:

* `data/stac/terrain/` — catalog entries for all terrain assets
* `web/config/layers.json` — frontend layer definitions
* `src/graph/terrain_nodes.py` — knowledge graph integration
* `data/processed/metadata/schema/` — shared JSON Schema definitions

The **web app** uses these layers to render:

* Base elevation surface (hillshade + DEM)
* 3D terrain effects and elevation profiles
* Historical map comparisons (1890 topos vs modern LiDAR)

---

## 🧠 MCP Alignment

Following **Master Coder Protocol (MCP)** principles:

* Documentation-first → every terrain layer has explicit metadata
* Reproducibility → all scripts + outputs versioned & checksummed
* Provenance → source → transform → output chain logged
* Transparency → open formats and schemas only
* Auditability → all data verifiable via SHA-256 + CI STAC tests

---

## 📅 Version History

| Version | Date       | Summary                                                                                             |
| ------- | ---------- | --------------------------------------------------------------------------------------------------- |
| v1.0    | 2025-10-04 | Initial release of terrain metadata directory and schema definitions (DEM, hillshade, slope/aspect) |

---

## 📎 References

* [USGS 3DEP LiDAR Program](https://www.usgs.gov/3dep)
* [Kansas DASC GIS Hub](https://hub.kansasgis.org)
* [rio-cogeo Documentation](https://cogeotiff.github.io/rio-cogeo)
* [STAC Specification 1.0.0](https://stacspec.org)
* [Master Coder Protocol Templates](../../../docs/templates/)

---

<div align="center">

**Kansas Frontier Matrix** — *“Where Time, Terrain, and History Intersect.”*
📍 [`data/processed/metadata/terrain/`](.) · 🔗 Part of the Spatiotemporal Data Architecture Layer

</div>

