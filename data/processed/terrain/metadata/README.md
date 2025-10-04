<div align="center">

# 🏔️ Kansas Frontier Matrix — Terrain Metadata  
`data/processed/terrain/metadata/`

**Mission:** Curate and document all **processed terrain and elevation datasets**  
that define Kansas’s physical landscape — forming the spatial foundation for hydrology, landcover,  
and historical geography within the Kansas Frontier Matrix (KFM) system.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../.github/workflows/codeql.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../LICENSE)

</div>

---

## 📚 Overview

This directory contains **STAC-compliant metadata** for all processed terrain layers  
within the Kansas Frontier Matrix. These datasets capture Kansas’s **elevation, topography, and geomorphology**  
through modern LiDAR models and historic topographic map data.

Each metadata file documents:
- Provenance (source, processing date, and version)  
- Dataset lineage and transformations (ETL history)  
- STAC 1.0 structure for spatial-temporal cataloging  
- Validation schema references (`data/processed/metadata/schema/`)  
- Thumbnail linkage for map and catalog previews  

---

## 🗂️ Directory Layout

```bash
data/processed/terrain/metadata/
├── README.md
├── ks_1m_dem_2018_2020.json
├── ks_hillshade_2018_2020.json
├── slope_aspect_2018_2020.json
└── thumbnails/
    ├── ks_1m_dem_2018_2020.png
    ├── ks_hillshade_2018_2020.png
    └── slope_aspect_2018_2020.png
````

> **Note:**
> Each `.json` file is a STAC Item describing a corresponding dataset in
> `data/processed/terrain/` and linking to its checksum (`data/processed/checksums/terrain/`).

---

## 🌍 Terrain Datasets (Processed Assets)

| Dataset                      | Source              | Format        | Resolution | Temporal Range | Output                                              |
| :--------------------------- | :------------------ | :------------ | :--------- | :------------- | :-------------------------------------------------- |
| **DEM (1m LiDAR)**           | USGS 3DEP / KS DASC | GeoTIFF (COG) | 1 m        | 2018–2020      | `data/processed/terrain/ks_1m_dem_2018_2020.tif`    |
| **Hillshade (Derived)**      | Derived from DEM    | GeoTIFF (COG) | 1 m        | 2018–2020      | `data/processed/terrain/ks_hillshade_2018_2020.tif` |
| **Slope & Aspect (Derived)** | Derived from DEM    | GeoTIFF (COG) | 1 m        | 2018–2020      | `data/processed/terrain/slope_aspect_2018_2020.tif` |

All datasets follow **EPSG:4326 (WGS84)** and are cataloged in `data/stac/terrain/`.

---

## 💾 Example STAC Metadata

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "ks_hillshade_2018_2020",
  "properties": {
    "title": "Kansas Hillshade (1m LiDAR, 2018–2020)",
    "datetime": "2020-01-01T00:00:00Z",
    "description": "Derived hillshade generated from 1m LiDAR DEM tiles across Kansas.",
    "proj:epsg": 4326,
    "themes": ["terrain", "elevation", "visualization"],
    "license": "Public Domain (USGS 3DEP)",
    "providers": [
      {"name": "USGS 3DEP", "roles": ["producer"]},
      {"name": "Kansas DASC", "roles": ["processor"]},
      {"name": "Kansas Frontier Matrix", "roles": ["curator"]}
    ]
  },
  "assets": {
    "data": {
      "href": "../terrain/ks_hillshade_2018_2020.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["data"]
    },
    "thumbnail": {
      "href": "thumbnails/ks_hillshade_2018_2020.png"
    }
  },
  "bbox": [-102.05, 36.99, -94.59, 40.00]
}
```

---

## 🧩 Semantic & Ontological Alignment

| Entity          | Ontology Mapping                                     | Example                         |
| :-------------- | :--------------------------------------------------- | :------------------------------ |
| DEM Raster      | `E73_Information_Object` + `E25_Man-Made_Feature`    | LiDAR-derived elevation grid    |
| Hillshade       | `E73_Information_Object` + `E29_Design_or_Procedure` | Derived shaded-relief raster    |
| Slope & Aspect  | `E16_Measurement` + OWL-Time interval                | Gradient and directional raster |
| Metadata Record | `E31_Document` + `E73_Information_Object`            | STAC metadata for 1m DEM        |

These mappings connect terrain data to **CIDOC CRM** and **OWL-Time ontologies**,
ensuring interoperability across historical, environmental, and spatial domains.

---

## ⚙️ ETL & Processing Workflow

**Pipeline Command:**

```bash
make terrain
```

**Python Script:**

```bash
python src/pipelines/terrain/terrain_pipeline.py
```

**Steps:**

1. Retrieve LiDAR DEM tiles from USGS or KS DASC.
2. Reproject to WGS84 (EPSG:4326).
3. Generate derivative layers (hillshade, slope, aspect).
4. Export to Cloud-Optimized GeoTIFF (COG) format.
5. Compute `.sha256` checksums for integrity validation.
6. Generate STAC metadata and preview thumbnails.
7. Validate metadata using JSON Schema + STAC CI checks.

---

## 🧮 Provenance & Validation

* **Checksums:** Stored in `data/processed/checksums/terrain/`
* **Licensing:** Public domain (USGS / DASC)
* **Validation:** JSON Schema + STAC validation during CI/CD workflows
* **Cross-links:** Source manifests under `data/sources/terrain/*.json`

---

## 🔗 Integration Points

| Component                           | Role                                                   |
| :---------------------------------- | :----------------------------------------------------- |
| `data/stac/terrain/`                | STAC Items and Collections for terrain layers          |
| `data/processed/checksums/terrain/` | Integrity tracking for each output file                |
| `web/config/layers.json`            | Configuration for elevation and hillshade layers       |
| `src/graph/terrain_nodes.py`        | Knowledge graph ingestion and ontology linkage         |
| `docs/architecture.md`              | Data architecture reference and workflow documentation |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                               |
| :---------------------- | :----------------------------------------------------------- |
| **Documentation-first** | README + STAC JSON per dataset                               |
| **Reproducibility**     | Deterministic pipeline execution with logged transformations |
| **Open Standards**      | STAC 1.0, COG, JSON Schema                                   |
| **Provenance**          | Source URLs, license, checksum, and timestamped processing   |
| **Auditability**        | CI validation ensures dataset and metadata consistency       |

---

## 📅 Version History

| Version | Date       | Summary                                                                                  |
| :------ | :--------- | :--------------------------------------------------------------------------------------- |
| v1.0    | 2025-10-04 | Initial release of terrain metadata — includes DEM, hillshade, and slope/aspect datasets |

---

<div align="center">

**Kansas Frontier Matrix** — *“Mapping the Foundation: Elevation, Form, and Flow.”*
📍 [`data/processed/terrain/metadata/`](.) · Linked to the **Terrain STAC Collection**

</div>
