<div align="center">

# 🗃️ Kansas Frontier Matrix — Dataset Documentation Template  
`docs/templates/dataset.md`

**Mission:** Provide a **structured, reproducible template** for documenting datasets in the Kansas Frontier Matrix (KFM) —  
ensuring **provenance, FAIR compliance, MCP alignment, and STAC-ready metadata** across the data lifecycle.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../docs/)
[![FAIR](https://img.shields.io/badge/FAIR-F%20A%20I%20R-brightgreen)](#-fair--standards-mapping)
[![STAC 1.0](https://img.shields.io/badge/STAC-1.0.0-blue)](#-stac--catalog-entries)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../LICENSE)

</div>

---

> **How to use this file**
> 1) **Copy** this template next to your dataset (e.g., `docs/data/terrain_ks_1m_dem_2018_2020.md`).  
> 2) **Fill in** all sections.  
> 3) **Link** to this record from the dataset’s STAC Item and source manifest.  
> 4) **Commit** alongside data/metadata changes so this documentation tracks versions.

---

## 🧭 Dataset Metadata (Front-Matter)

```yaml
# --- Begin dataset front-matter (machine-readable) ---
dataset_id: DATASET-YYYY-NNN-<DOMAIN>-<NAME>
title: "<Full Descriptive Title>"
summary: "<One-sentence abstract for site/catalog cards.>"
authors:
  - name: "<Name, Role>"
    email: "<optional>"
curators:
  - name: "<Team/Role>"
contacts:
  - name: "<Primary Contact>"
    email: "<contact@org>"
doi: "<if available>"
created: YYYY-MM-DD
updated: YYYY-MM-DD
version: "vX.Y.Z"
domain: "<Terrain|Hydrology|Climate|Landcover|Hazards|Tabular|Text|Mixed>"
data_type: "<Raster|Vector|Tabular|Text|Mixed>"
license: "<CC-BY 4.0|Public Domain|MIT|Custom>"
usage_constraints: "<Any restrictions or required attributions>"
keywords: ["kansas", "dem", "hydrology", "example"]
spatial:
  crs: "EPSG:4326"
  bbox: [-102.05, 36.99, -94.61, 40.00]
temporal:
  start: "YYYY-MM-DD"
  end: "YYYY-MM-DD"
source_manifests:
  - path: data/sources/<domain>/<source>.json
checksums_manifest: data/checksums/<domain>/<dataset>.manifest.json
stac_items:
  - path: data/stac/<domain>/<dataset>.json
distribution:
  api_endpoints:
    - type: "stac-item"
      href: "/api/stac/items/<dataset_id>"
    - type: "download"
      href: "https://<host>/<path>/<file>"
# --- End dataset front-matter ---
````

---

## 🧩 Abstract / Description

> **Guidance:** Provide a clear description of what this dataset represents, why it exists, and how it fits into the KFM ecosystem.
> Include intended uses, known limitations, and the expected audience.

**Example:**
This dataset contains a 1-meter resolution Digital Elevation Model (DEM) derived from USGS 3DEP LiDAR (2018–2020) for Kansas.
It is the foundational layer for hydrology modeling (watersheds, flowlines), hazards analysis (flood exposure), and landcover derivatives.

---

## 🌐 Data Provenance & Sources

| Source Name   | Provider    | Access Method | License       | Link / API                                                             | Notes           |
| :------------ | :---------- | :------------ | :------------ | :--------------------------------------------------------------------- | :-------------- |
| USGS 3DEP DEM | USGS        | REST API      | Public Domain | [https://elevation.nationalmap.gov](https://elevation.nationalmap.gov) | 2018–2020 tiles |
| KS DASC LiDAR | Kansas DASC | FTP/HTTP      | CC-BY 4.0     | [https://www.kansasgis.org/](https://www.kansasgis.org/)               | County mosaics  |

> **All sources must have entries in** `data/sources/<domain>/` **and be referenced in this section.**

---

## ⚙️ Processing Workflow (ETL → Products)

| Step             | Description                | Command / Script                                             | Output                          |
| :--------------- | :------------------------- | :----------------------------------------------------------- | :------------------------------ |
| 1. Ingest        | Fetch raw tiles            | `make fetch` or `python src/pipelines/fetch/usgs_ingest.py`  | `data/raw/terrain/...`          |
| 2. Reproject     | Warp to EPSG:4326          | `gdalwarp -t_srs EPSG:4326 <in> <out>`                       | GeoTIFF                         |
| 3. Mosaic        | Merge tiles                | `gdal_merge.py -o ks_dem.tif ...`                            | `ks_dem.tif`                    |
| 4. Convert → COG | Cloud optimize             | `rio cogeo create ks_dem.tif ks_dem_cog.tif --web-optimized` | `ks_dem_cog.tif`                |
| 5. Derivatives   | Hillshade / Slope / Aspect | `python src/pipelines/terrain/derive.py`                     | `hillshade.tif`, `slope.tif`    |
| 6. STAC          | Generate Items             | `python src/pipelines/load/stac_writer.py`                   | `data/stac/terrain/<item>.json` |

**Make targets**

```bash
make fetch     # fetch raw sources
make process   # run standard transforms
make enrich    # optional (e.g., text or QA enrichment)
make load      # write STAC + graph entries
make checksums # compute/verify SHA-256 lineage
```

---

## 🧮 Specifications & Schema

| Attribute             | Description                 | Value / Example                         |
| :-------------------- | :-------------------------- | :-------------------------------------- |
| Spatial Resolution    | Ground sample distance      | 1 m                                     |
| CRS                   | Coordinate Reference System | EPSG:4326 (WGS84)                       |
| Spatial Extent (BBox) | minX, minY, maxX, maxY      | [-102.05, 36.99, -94.61, 40.00]         |
| Temporal Coverage     | Start / End                 | 2018-01-01 — 2020-12-31                 |
| Formats               | Primary / Aux               | GeoTIFF (COG), PNG (thumb), JSON (STAC) |
| Size                  | Total                       | ~12 GB                                  |
| Record Count          | N (if tabular)              | —                                       |
| Encoding              | Text/CSV/Parquet            | UTF-8 / CSV / Parquet                   |

**Data Dictionary (Tabular / Vector attributes)**

| Field       | Type    | Units   | Allowed Values / Range | Description                    |
| :---------- | :------ | :------ | :--------------------- | :----------------------------- |
| `elevation` | float32 | meters  | ≥ -500                 | Elevation above mean sea level |
| `slope_deg` | float32 | degrees | 0–90                   | Derived slope angle            |
| ...         | ...     | ...     | ...                    | ...                            |

---

## 🧾 Outputs & Distribution

| Type        | Path / URL                                                           | Description              |
| :---------- | :------------------------------------------------------------------- | :----------------------- |
| Primary     | `data/processed/terrain/ks_1m_dem_2018_2020.tif`                     | Core processed raster    |
| COG         | `data/processed/terrain/ks_1m_dem_2018_2020_cog.tif`                 | Cloud-Optimized GeoTIFF  |
| Derivatives | `data/processed/terrain/hillshade.tif`                               | Visualization & analysis |
| STAC Item   | `data/stac/terrain/ks_1m_dem_2018_2020.json`                         | Catalog metadata         |
| Checksums   | `data/checksums/terrain/ks_1m_dem_2018_2020.manifest.json`           | Integrity lineage        |
| Thumbnail   | `data/processed/metadata/terrain/thumbnails/ks_1m_dem_2018_2020.png` | Web preview              |

---

## ✅ Validation & QA

| Check       | Method / Tool                         | Evidence / Path                 | Result |
| :---------- | :------------------------------------ | :------------------------------ | :----- |
| Checksum    | `make checksums`                      | `data/checksums/...`            | ✅      |
| STAC Schema | `stac-validator`                      | `_reports/stac/<dataset>.json`  | ✅      |
| Spatial QA  | `gdalinfo`, bounds & CRS check        | `_reports/spatial/<dataset>.md` | ✅      |
| CI/CD       | `.github/workflows/stac-validate.yml` | Actions run ID                  | ✅      |

> **All QA logs** should be archived under `data/work/logs/<domain>/<dataset>/`.

---

## 🔗 Relationships & Dependencies

| Relation      | Target                   | Type      | Path / Ref                                               |
| :------------ | :----------------------- | :-------- | :------------------------------------------------------- |
| Derived From  | `usgs_3dep_dem`          | Source    | `data/sources/terrain/usgs_3dep_dem.json`                |
| Feeds         | `watersheds_huc12_2019`  | Dependent | `data/processed/hydrology/watersheds_huc12_2019.geojson` |
| Referenced In | `ks_hillshade_2018_2020` | Derived   | `data/processed/terrain/ks_hillshade_2018_2020.tif`      |

---

## 🔐 Ethics, Legal & Licensing

* Dataset license: **<insert>** (e.g., CC-BY 4.0).
* Attribution statement to include in derivative works.
* No PII or sensitive data included.
* Compliance with **USGS / DASC** distribution policies.
* If mixing licenses, document **compatibility** and **exceptions** here.

---

## 🧩 Integration with KFM Systems

| Component           | Role                   | Integration Notes                     |
| :------------------ | :--------------------- | :------------------------------------ |
| **Pipelines**       | ETL → products         | `src/pipelines/<domain>/*`            |
| **Metadata**        | STAC linkages          | `data/stac/<domain>/*`                |
| **CI/CD**           | Validation & deploy    | `.github/workflows/stac-validate.yml` |
| **Web Viewer**      | Map layer config       | `web/config/layers.json`              |
| **Knowledge Graph** | Provenance & relations | `src/graph/graph_loader.py`           |

---

## 🔎 FAIR & Standards Mapping

| FAIR              | Implementation                                                    |
| :---------------- | :---------------------------------------------------------------- |
| **Findable**      | STAC Items with rich keywords, DOIs/IDs, indexed in site/catalog. |
| **Accessible**    | Public endpoints + docs links; consistent URLs.                   |
| **Interoperable** | Open formats (COG, GeoJSON, CSV), EPSG codes, JSON Schema.        |
| **Reusable**      | Clear license, citation, and complete metadata with lineage.      |

**DCAT / JSON-LD (optional):** Provide a DCAT or JSON-LD snippet if publishing to external catalogs.

---

## 🧾 Citation

> **Suggested citation:**
> *Author(s) (Year). Title (Version). Kansas Frontier Matrix. DOI/URL. License.*

**Example:**
Doe, J., & KFM Data Team (2025). *Kansas 1m DEM (2018–2020), v1.1*. Kansas Frontier Matrix. [https://example.org/doi/xx.xxxx/xxx](https://example.org/doi/xx.xxxx/xxx). CC-BY 4.0.

---

## 📌 Known Issues & Risks

* **Edge artifacts** at tile seams; mitigated by feathering during mosaic.
* **Intermittent gaps** in LiDAR coverage for {counties}.
* **Large size** may impact low-bandwidth users (alternatives: WMTS, XYZ tiles).

---

## 🧯 Rollback & Retention

* **Retention policy:** Keep last **N** versions; archive older in cold storage.
* **Rollback plan:** Re-link web/catalog to previous STAC item; restore checksums and thumbnails.
* **Deprecation:** Mark STAC `deprecated: true`; point to replacement via `rel:alternate`/`rel:latest-version`.

---

## 🧠 MCP Compliance Summary

| MCP Principle       | Implementation                                      |
| :------------------ | :-------------------------------------------------- |
| Documentation-first | This record authored before publication.            |
| Reproducibility     | Make targets + checksums produce identical outputs. |
| Open Standards      | STAC 1.0, GeoTIFF (COG), GeoJSON, JSON Schema.      |
| Provenance          | Source manifests + checksum lineage + graph links.  |
| Auditability        | CI/CD logs, validation reports, versioning.         |

---

## 📎 Related Documentation

* `docs/architecture/data-architecture.md` — Data model & lineage
* `docs/templates/experiment.md` — For associated analyses
* `docs/templates/sop.md` — Operational procedures
* `.github/workflows/stac-validate.yml` — CI validation workflow

---

## 🗓️ Version History

| Version | Date       | Author | Summary                   |
| :------ | :--------- | :----- | :------------------------ |
| vX.Y.Z  | YYYY-MM-DD | <Name> | Initial release / updates |
