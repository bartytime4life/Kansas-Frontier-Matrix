<div align="center">

# 🏔️ Kansas Frontier Matrix — Terrain Metadata  
`data/processed/metadata/terrain/`

**Mission:** Curate, document, and standardize all **processed terrain and elevation datasets**  
that form the topographic foundation of the Kansas Frontier Matrix knowledge system —  
supporting historical analysis, hydrology modeling, and visual storytelling of the Kansas landscape.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../../.github/workflows/codeql.yml)
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../../.github/workflows/trivy.yml)
[![Pre-Commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen.svg)](https://pre-commit.com/)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)

</div>

---

## 📚 Overview

This directory documents **terrain and elevation datasets** processed within the Kansas Frontier Matrix (KFM).  
Layers include **elevation, hillshade, slope/aspect**, and **historic topographic overlays**.

Each dataset provides:
- **STAC 1.0** metadata (`.json`)  
- **Provenance & checksum** linkage (`.sha256`)  
- **Open licensing** and source attribution  
- **JSON Schema** validation & **MCP** reproducibility fields

---

## 🧭 System Flow (Mermaid)

```mermaid
flowchart TD
  A["Raw Elevation Inputs\n(USGS 3DEP · KS DASC · USGS Historic Topos)"] --> B["Processing\n(GDAL · PDAL · WhiteboxTools)"]
  B --> C["Processed Terrain\n(data/processed/terrain/*.tif)"]
  C --> D["Metadata Authoring\n(data/processed/metadata/terrain/*.json)"]
  D --> E["Validation\n(JSON Schema · STAC 1.0 · CI)"]
  E --> F["Catalog & UI\n(data/stac/terrain · web/config/layers.json)"]
  %% END OF MERMAID
````

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
```

> **Note:** Each `.json` describes a dataset in `data/processed/terrain/` and references a checksum in
> `data/processed/terrain/checksums/`. STAC items are synchronized under `data/stac/terrain/`.

---

## 🏔️ Terrain Layers (Processed Assets)

| Dataset                                | Source                        | Format        | Resolution | Temporal Range | Output                                              |
| :------------------------------------- | :---------------------------- | :------------ | :--------- | :------------- | :-------------------------------------------------- |
| **DEM (1 m LiDAR)**                    | USGS 3DEP / KS DASC           | GeoTIFF (COG) | 1 m        | 2018–2020      | `data/processed/terrain/ks_1m_dem_2018_2020.tif`    |
| **Hillshade (Derived)**                | Derived from DEM              | GeoTIFF (COG) | 1 m        | 2018–2020      | `data/processed/terrain/ks_hillshade_2018_2020.tif` |
| **Slope & Aspect (Derived)**           | Derived from DEM              | GeoTIFF (COG) | 1 m        | 2018–2020      | `data/processed/terrain/slope_aspect_2018_2020.tif` |
| **Historic Topo Overlays (1890–1950)** | USGS Historic Topo Collection | GeoTIFF       | map scale  | 1894–1950      | `data/processed/terrain/usgs_topo_larned_1894.tif`  |

All rasters are standardized to **EPSG:4326 (WGS 84)** and optimized as **COGs** where applicable.

---

## 💾 Example STAC Item (enhanced)

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "ks_1m_dem_2018_2020",
  "collection": "kfm_terrain",
  "bbox": [-102.05, 36.99, -94.59, 40.00],
  "geometry": {
    "type": "Polygon",
    "coordinates": [[
      [-102.05, 36.99], [-94.59, 36.99],
      [-94.59, 40.00], [-102.05, 40.00],
      [-102.05, 36.99]
    ]]
  },
  "properties": {
    "title": "Kansas LiDAR Digital Elevation Model (1 m, 2018–2020)",
    "description": "Hydrologically conditioned 1 m DEM from USGS 3DEP/KS DASC LiDAR tiles.",
    "datetime": "2020-01-01T00:00:00Z",
    "proj:epsg": 4326,
    "themes": ["terrain","elevation","topography"],
    "processing:software": "GDAL 3.8.0; WhiteboxTools 2.2.0",
    "kfm:mcp_provenance": "sha256:<PUT_FILE_HASH_HERE>",
    "license": "Public Domain (USGS 3DEP)"
  },
  "assets": {
    "data": {
      "href": "../terrain/ks_1m_dem_2018_2020.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["data"]
    },
    "thumbnail": {
      "href": "thumbnails/ks_1m_dem_2018_2020.png",
      "type": "image/png",
      "roles": ["thumbnail"]
    },
    "checksum:sha256": {
      "href": "../terrain/checksums/ks_1m_dem_2018_2020.tif.sha256",
      "type": "text/plain",
      "roles": ["metadata"]
    }
  },
  "links": [
    { "rel": "collection", "href": "../../../stac/collections/kfm_terrain.json", "type": "application/json" },
    { "rel": "self",       "href": "ks_1m_dem_2018_2020.json",               "type": "application/json" },
    { "rel": "parent",     "href": ".",                                      "type": "text/html" }
  ]
}
```

---

## 🧩 Semantic & Ontological Alignment

| Entity           | Ontology Mapping                                           | Example                    |
| :--------------- | :--------------------------------------------------------- | :------------------------- |
| Elevation Raster | CIDOC `E73_Information_Object` + `E25_Man-Made_Feature`    | LiDAR-based elevation grid |
| Hillshade        | CIDOC `E73_Information_Object` + `E29_Design_or_Procedure` | Shaded-relief raster       |
| Slope & Aspect   | CIDOC `E16_Measurement` + **OWL-Time** interval            | Gradient & aspect models   |
| Historic Topo    | CIDOC `E31_Document` + `E53_Place`                         | 1894 Larned topo sheet     |

These mappings enable cross-domain reasoning between landscape, environment, and history.

---

## ⚙️ ETL & Processing Workflow

**Makefile**

```bash
make terrain
```

**Pipeline**

```bash
python src/pipelines/terrain/terrain_pipeline.py
```

**Steps**

1. Fetch LiDAR/DEM tiles (USGS 3DEP / KS DASC).
2. Merge & reproject → **EPSG:4326**.
3. Generate **hillshade**, **slope**, **aspect**.
4. Convert to **COG** (overviews & compression).
5. Compute **`.sha256`** checksums (store in `data/processed/terrain/checksums/`).
6. Generate **STAC** items + thumbnails.
7. Validate via **JSON Schema** + **STAC 1.0** in CI.

---

## 🧮 Provenance & Validation

* **Checksums:** `data/processed/terrain/checksums/`
* **Licensing:** Public Domain sources; derived products **CC-BY 4.0**
* **Validation:** STAC + JSON Schema & MCP rule checks in CI
* **Source manifests:** `data/sources/terrain/*.json`

---

## 🔗 Integration Points

| Component                           | Role                                                   |
| :---------------------------------- | :----------------------------------------------------- |
| `data/stac/terrain/`                | STAC Items & Collections for terrain layers            |
| `web/config/layers.json`            | Frontend map configuration (base elevation & previews) |
| `src/graph/terrain_nodes.py`        | Knowledge graph ingestion & ontology binding           |
| `data/processed/terrain/checksums/` | Integrity tracking (SHA-256)                           |
| `docs/architecture.md`              | End-to-end data architecture & workflow references     |

---

## ✅ QA Checklist (copy into PRs)

* [ ] STAC item validates (CI green)
* [ ] `kfm:mcp_provenance` hash equals file checksum
* [ ] `assets.data` is COG and path is correct & relative
* [ ] Thumbnail present and referenced in `assets.thumbnail`
* [ ] EPSG/CRS & temporal fields correct
* [ ] Links (`self`, `collection`, `parent`) resolve

---

## 🧠 MCP Compliance Summary

| Principle           | Implementation                                                |
| :------------------ | :------------------------------------------------------------ |
| Documentation-first | README + per-dataset STAC item + thumbnail                    |
| Reproducibility     | Containerized ETL; deterministic transforms; checksums        |
| Open Standards      | **COG GeoTIFF**, **STAC 1.0**, **JSON Schema**                |
| Provenance          | Source URLs, licenses, and cryptographic hashes               |
| Auditability        | CI validation for schema/STAC; lineage tracked via MCP fields |

---

## 📅 Version History

|  Version  | Date       | Summary                                                                                                         |
| :-------: | :--------- | :-------------------------------------------------------------------------------------------------------------- |
| **1.1.0** | 2025-10-11 | Fixed badge paths; added Mermaid flow; enhanced STAC example (collection/geometry/checksum/links); QA checklist |
|   1.0.0   | 2025-10-04 | Initial terrain metadata release — DEM, hillshade, slope/aspect, and historic topo datasets                     |

---

<div align="center">

**Kansas Frontier Matrix** — *“Mapping the Ground Truth of the Kansas Frontier.”*
📍 [`data/processed/metadata/terrain/`](.)

</div>
```
