<div align="center">

# 🏔️ Kansas Frontier Matrix — Terrain Metadata  
`data/processed/metadata/terrain/`

**Mission:** Curate, document, and standardize all **processed terrain and elevation datasets**  
that form the topographic foundation of the Kansas Frontier Matrix knowledge system —  
supporting historical analysis, hydrology modeling, and visual storytelling of the Kansas landscape.

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

This directory documents **terrain and elevation datasets** processed within the  
Kansas Frontier Matrix (KFM). These datasets define the physical surface of Kansas —  
including elevation, hillshade, slope/aspect, and historical topographic map layers.  

Each dataset includes:
- STAC 1.0-compliant metadata (`.json`)  
- Provenance and checksum linkage (`.sha256`)  
- Open license and data source information  
- JSON Schema validation for structure and metadata compliance  
- MCP-based reproducibility workflow and provenance logs  

---

## 🗂️ Directory Layout

```bash
data/processed/metadata/terrain/
├── README.md
├── ks_1m_dem_2018_2020.json
├── ks_hillshade_2018_2020.json
├── slope_aspect_2018_2020.json
└── thumbnails/
    ├── ks_1m_dem_2018_2020.png
    ├── ks_hillshade_2018_2020.png
    └── slope_aspect_2018_2020.png
````

> **Note:** Each `.json` metadata file describes a corresponding terrain dataset in
> `data/processed/terrain/`, linking to its STAC entry and checksum record under
> `data/processed/checksums/terrain/`.

---

## 🏔️ Terrain Layers (Processed Assets)

| Dataset                                | Source                          | Format        | Resolution         | Temporal Range | Output                                              |
| :------------------------------------- | :------------------------------ | :------------ | :----------------- | :------------- | :-------------------------------------------------- |
| **DEM (1 m LiDAR)**                    | USGS 3DEP / KS DASC             | GeoTIFF (COG) | 1 m                | 2018–2020      | `data/processed/terrain/ks_1m_dem_2018_2020.tif`    |
| **Hillshade (Derived)**                | Derived from DEM                | GeoTIFF (COG) | 1 m                | 2018–2020      | `data/processed/terrain/ks_hillshade_2018_2020.tif` |
| **Slope & Aspect**                     | Derived from DEM                | GeoTIFF (COG) | 1 m                | 2018–2020      | `data/processed/terrain/slope_aspect_2018_2020.tif` |
| **Historic Topo Overlays (1890–1950)** | USGS Historical Topo Collection | GeoTIFF       | 1:62,500–1:125,000 | 1894–1950      | `data/processed/terrain/usgs_topo_larned_1894.tif`  |

All datasets are standardized to **EPSG:4326 (WGS84)** and cataloged via STAC metadata in `data/stac/terrain/`.

---

## 💾 Example STAC Metadata

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "ks_1m_dem_2018_2020",
  "properties": {
    "title": "Kansas LiDAR Digital Elevation Model (1m, 2018–2020)",
    "datetime": "2020-01-01T00:00:00Z",
    "description": "High-resolution LiDAR-based DEM representing terrain elevation across Kansas.",
    "proj:epsg": 4326,
    "themes": ["terrain", "elevation", "topography"],
    "license": "Public Domain (USGS 3DEP)",
    "providers": [
      {"name": "USGS 3DEP", "roles": ["producer"]},
      {"name": "Kansas DASC", "roles": ["processor"]},
      {"name": "Kansas Frontier Matrix", "roles": ["curator"]}
    ]
  },
  "assets": {
    "data": {
      "href": "../terrain/ks_1m_dem_2018_2020.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["data"]
    },
    "thumbnail": {
      "href": "thumbnails/ks_1m_dem_2018_2020.png"
    }
  },
  "bbox": [-102.05, 36.99, -94.59, 40.00]
}
```

---

## 🧩 Semantic & Ontological Alignment

| Entity           | Ontology Mapping                                     | Example                     |
| :--------------- | :--------------------------------------------------- | :-------------------------- |
| Elevation Raster | `E73_Information_Object` + `E25_Man-Made_Feature`    | LiDAR-based elevation model |
| Hillshade        | `E73_Information_Object` + `E29_Design_or_Procedure` | Shaded relief map of DEM    |
| Slope & Aspect   | `E16_Measurement` + OWL-Time interval                | Derived gradient analysis   |
| Historic Topo    | `E31_Document` + `E53_Place`                         | 1894 Larned topographic map |

These ontological mappings allow cross-domain reasoning between physical landscape,
environmental processes, and cultural-historical data layers.

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

1. Fetch LiDAR DEM tiles from USGS 3DEP or KS DASC services.
2. Merge and reproject to WGS84 (EPSG:4326).
3. Generate hillshade, slope, and aspect derivatives.
4. Convert outputs to Cloud-Optimized GeoTIFF (COG).
5. Compute `.sha256` checksums for integrity validation.
6. Create STAC metadata entries and thumbnails.
7. Validate using JSON Schema and STAC CI workflow.

---

## 🧮 Provenance & Validation

* **Checksums:** Stored under `data/processed/checksums/terrain/` for every raster.
* **Licensing:** Public domain (USGS / KS DASC). Derived products are CC-BY 4.0.
* **Validation:** JSON Schema + STAC 1.0 validation performed automatically in CI.
* **Cross-links:** Source manifests located in `data/sources/terrain/*.json`.

---

## 🔗 Integration Points

| Component                           | Role                                                 |
| :---------------------------------- | :--------------------------------------------------- |
| `data/stac/terrain/`                | STAC Items and Collections for terrain datasets      |
| `web/config/layers.json`            | Frontend map configuration for base elevation layers |
| `src/graph/terrain_nodes.py`        | Knowledge graph ingestion and ontology mapping       |
| `data/processed/checksums/terrain/` | Contains corresponding checksum records              |
| `docs/architecture.md`              | Reference for data flow and component structure      |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                   |
| :---------------------- | :--------------------------------------------------------------- |
| **Documentation-first** | Each dataset includes README and STAC metadata                   |
| **Reproducibility**     | Deterministic ETL with logged outputs and checksums              |
| **Open Standards**      | GeoTIFF (COG), STAC 1.0, JSON Schema                             |
| **Provenance**          | Source URLs, licenses, and timestamps stored in metadata         |
| **Auditability**        | Continuous integration tests validate every dataset and checksum |

---

## 📅 Version History

| Version | Date       | Summary                                                                                     |
| :------ | :--------- | :------------------------------------------------------------------------------------------ |
| v1.0    | 2025-10-04 | Initial terrain metadata release — DEM, hillshade, slope/aspect, and historic topo datasets |

---

<div align="center">

**Kansas Frontier Matrix** — *“Mapping the Ground Truth of the Kansas Frontier.”*
📍 [`data/processed/metadata/terrain/`](.) · Integrated within the **Terrain STAC Collection**

</div>
