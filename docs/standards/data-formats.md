<div align="center">

# 🗂️ Kansas Frontier Matrix — **Data Format Standards**

`docs/standards/data-formats.md`

**Purpose:** Define approved and required **data, metadata, and file formats** used across the
**Kansas Frontier Matrix (KFM)** — guaranteeing **reproducibility, interoperability, and MCP compliance**.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../LICENSE)

</div>

---

## 📚 Overview

KFM uses **open, non-proprietary** formats that are **scriptable, validated, and portable** with free tools.
This guide specifies:

* 📦 **Approved file formats** by data domain (spatial, tabular, text).
* 🧾 **Metadata models** and **validation rules** (STAC + JSON Schema).
* 🧱 **Encoding, naming, compression** conventions.
* 🔁 CI-enforced **integrity** (checksums) and **conformance** (schemas).

> **MCP Principles:** Documentation-first · Reproducible · Open-standard · Provenance-tracked · Auditable

---

## 🧩 Approved Formats by Domain

| Domain        | Data Type                      | Approved Formats                                     | Notes                                  |
| :------------ | :----------------------------- | :--------------------------------------------------- | :------------------------------------- |
| **Terrain**   | Raster (DEM, hillshade, slope) | **COG GeoTIFF** (`.tif`), preview `.png`             | Elevation & derivatives                |
| **Hydrology** | Vector (rivers, basins)        | **GeoJSON** (`.geojson`), **GeoPackage** (`.gpkg`)   | Flowlines, watersheds                  |
| **Landcover** | Raster (classes, NDVI)         | **COG GeoTIFF** (`.tif`), preview `.png`             | Class maps or indices                  |
| **Climate**   | Raster / Time-series           | **COG** (`.tif`), **NetCDF4 CF-1.8** (`.nc`), `.csv` | CF-compliant NetCDF for multi-var time |
| **Hazards**   | Vector / Raster                | `.geojson`, `.tif`, `.csv`                           | Tornadoes, floods, wildfires           |
| **Tabular**   | Structured tables              | `.csv` (+ CSVW schema), **Parquet** (`.parquet`)     | Parquet for large/partitioned data     |
| **Text**      | Unstructured / corpora         | **JSON Lines** (`.jsonl`), `.txt`, `.csv`            | OCR, transcripts, articles             |
| **Metadata**  | Dataset & catalog descriptors  | **STAC 1.0.0 JSON**, **JSON Schema**                 | Items/Collections/Assets               |

---

## 🌍 Spatial Data Standards

### Raster (Terrain, Climate, Landcover)

| Property        | Standard / Requirement                                                                                       |
| :-------------- | :----------------------------------------------------------------------------------------------------------- |
| **Format**      | **Cloud-Optimized GeoTIFF** (COG)                                                                            |
| **CRS**         | Default **EPSG:4326** (WGS84). Exceptions allowed (e.g., EPSG:5070) **only** if documented in STAC + README. |
| **Compression** | **DEFLATE** or **LZW**, predictor where applicable.                                                          |
| **Tiling**      | Internal tiles, **512×512** preferred.                                                                       |
| **Overviews**   | Internal, pyramid {2,4,8,16} (or auto).                                                                      |
| **Nodata**      | Explicit nodata value set; documented in STAC `raster:nodata`.                                               |
| **Bit depth**   | Float32 for continuous (DEM/temperature), UInt8/UInt16 for categorical.                                      |
| **Aux data**    | Color tables for categorical rasters; add `classification:classes` in STAC.                                  |

**COG creation (reference)**

```bash
rio cogeo create input.tif output_cog.tif \
  --blocksize 512 \
  --overview-level 4 \
  --overview-resampling average \
  --web-optimized \
  --compress DEFLATE --bigtiff IF_SAFER
```

> **Projection exceptions** (e.g., analysis in EPSG:2163 or EPSG:5070) must include a WGS84 over-view or a companion WGS84 COG, and document rationale in STAC `proj:epsg` + README.

---

### Vector (Hydrology, Hazards, Boundaries)

| Property     | Standard / Requirement                                                                                |
| :----------- | :---------------------------------------------------------------------------------------------------- |
| **Format**   | **GeoJSON** (RFC 7946) default; **GPKG** for multi-layer or very large feature sets.                  |
| **CRS**      | **EPSG:4326** (lon, lat).                                                                             |
| **Encoding** | UTF-8 (no BOM).                                                                                       |
| **Schema**   | Attribute names: lowercase, snake_case; include units in STAC/CSVW; use domain schemas where defined. |
| **Topology** | Validate geometry (no self-intersections); simplify for web if necessary, preserve a high-res copy.   |

**GeoJSON feature schema (minimal)**

```json
{
  "type": "Feature",
  "properties": {
    "id": "ks_river_001",
    "name": "Kansas River",
    "source": "usgs_nhd",
    "date": "2024-01-01",
    "class": "river"
  },
  "geometry": { "type": "LineString", "coordinates": [ [ -95.0, 39.0 ], ... ] }
}
```

---

## 🧮 Tabular Data Standards

| Attribute          | Requirement                                               |
| :----------------- | :-------------------------------------------------------- |
| **Format**         | `.csv` (RFC 4180) with header row **or** **Parquet**.     |
| **Encoding**       | UTF-8.                                                    |
| **Delimiter**      | Comma (`,`); no stray delimiters/quotes.                  |
| **Missing values** | `NULL` or empty string (no sentinel values like `-9999`). |
| **Units**          | Record in CSVW / STAC; SI units preferred.                |
| **Validation**     | JSON Schema required for ingestion.                       |

**CSVW sidecar (example)** – `my_table.csv-metadata.json`

```json
{
  "@context": "http://www.w3.org/ns/csvw",
  "tables": [{
    "url": "my_table.csv",
    "tableSchema": {
      "columns": [
        {"name": "year", "datatype": "integer", "required": true},
        {"name": "county", "datatype": "string"},
        {"name": "population", "datatype": "integer", "aboutUrl": "http://example.org/county/{county}"},
        {"name": "median_income", "datatype": "integer", "titles": "USD"}
      ],
      "primaryKey": "year"
    }
  }]
}
```

**Parquet partitioning** (recommended for large tables)

```
data/processed/tabular/population/year=2020/part-000.parquet
data/processed/tabular/population/year=2021/part-001.parquet
```

---

## 🧠 Text / NLP Corpora

| Property          | Requirement                                                                     |
| :---------------- | :------------------------------------------------------------------------------ |
| **Container**     | **JSON Lines** (`.jsonl`) – one document per line.                              |
| **Fields (min)**  | `id`, `source`, `text`, `date` (ISO-8601), `lang` (ISO 639-1), optional `tags`. |
| **Attribution**   | `source` is mandatory (publication/archive, URL or accession).                  |
| **Normalization** | Maintain raw + normalized (tokenized/cleaned) forms in separate files/fields.   |

```json
{"id":"ks_news_1898_001","source":"Topeka Daily Capital","date":"1898-07-14","lang":"en","text":"Kansas River floodwaters rising rapidly."}
```

---

## 🧾 Metadata & Catalogs

| Type           | Format                        | Notes                                                             |
| :------------- | :---------------------------- | :---------------------------------------------------------------- |
| **Dataset**    | **STAC Item** (`.json`)       | Per dataset/asset; include `proj`, `raster`, `checksum:multihash` |
| **Collection** | **STAC Collection** (`.json`) | Groups Items by theme/domain/time                                 |
| **Checksum**   | `.sha256`                     | One per file; also include multihash in STAC when possible        |
| **Schema**     | **JSON Schema**               | Validate metadata, tabular schemas, configs                       |

**STAC Item (minimal)** – `data/stac/terrain/ks_1m_dem_2018_2020.json`

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "ks_1m_dem_2018_2020",
  "properties": {
    "description": "Kansas 1 m DEM derived from USGS 3DEP LiDAR (2018–2020)",
    "start_datetime": "2018-01-01T00:00:00Z",
    "end_datetime": "2020-12-31T23:59:59Z",
    "license": "public-domain"
  },
  "assets": {
    "data": {
      "href": "data/processed/terrain/ks_1m_dem_2018_2020.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["data"],
      "raster:bands": [{ "nodata": -9999, "data_type": "float32" }],
      "checksum:multihash": "1220<sha256-hex>"
    },
    "thumbnail": { "href": "data/processed/terrain/ks_1m_dem_2018_2020.png", "type": "image/png", "roles": ["thumbnail"] }
  }
}
```

---

## 🔐 Checksums & Integrity

| File       | Purpose                              |
| :--------- | :----------------------------------- |
| `*.sha256` | Verify file integrity (SHA-256).     |
| Manifest   | Domain-wide list of checksums (JSON) |

`.sha256` example

```
4a2f7f3e94a1f12c7bde9b6d8120ee9876ab2b74d7c63c5c0a1a86b8a23de98a  ks_1m_dem_2018_2020.tif
```

---

## 🧱 Naming, Encoding, Packaging

### Filenames

| Element   | Pattern                               | Example                          |
| :-------- | :------------------------------------ | :------------------------------- |
| Dataset   | `<region>_<topic>_<year-range>.<ext>` | `ks_1m_dem_2018_2020.tif`        |
| Metadata  | `<dataset>.json`                      | `ks_1m_dem_2018_2020.json`       |
| Checksum  | `<dataset>.<ext>.sha256`              | `ks_1m_dem_2018_2020.tif.sha256` |
| Thumbnail | `<dataset>.png`                       | `ks_1m_dem_2018_2020.png`        |

**Rules:** lowercase, underscores, ASCII only, no spaces.

### Encoding

* All text files **UTF-8** (no BOM).
* Newlines **LF**.

### Packaging

| Purpose  | Format             | Notes                                                 |
| :------- | :----------------- | :---------------------------------------------------- |
| Delivery | `.zip` / `.tar.gz` | Preserve relative structure; include checksums + STAC |
| Internal | DEFLATE/LZW        | Use embedded compression in GeoTIFF/NetCDF            |

> Avoid `.rar`, proprietary multi-part archives.

---

## ⏱️ Temporal & Units Conventions

* **Dates/times:** ISO-8601 (UTC).
* **Ranges:** Use STAC `start_datetime`/`end_datetime`.
* **Units:** SI where possible; record in CSVW/STAC fields (`unit`, `uom`).
* **QC flags:** For climate/hydrology, include **CF-convention** flags in NetCDF and STAC `xarray:open_kwargs` if relevant.

---

## 🧪 Validation & CI Requirements

| Check                | Tool / Workflow                       | Applies To             |
| :------------------- | :------------------------------------ | :--------------------- |
| **Checksum**         | `make checksums`                      | All files              |
| **STAC**             | `stac-validator`                      | STAC JSON              |
| **JSON Schema**      | `jsonschema`                          | Tables/config/metadata |
| **Projection & COG** | `gdalinfo` / `cog_validate`           | Rasters                |
| **CI Orchestration** | `.github/workflows/stac-validate.yml` | Continuous             |

---

## 🧩 Web & Tile Services (Optional)

* When publishing tiles, use **XYZ** or **WMTS** with transparent PNG/WEBP tiles.
* Vector tiles (if used) must be **PMTiles** or **Mapbox Vector Tiles** (MVT) generated from the canonical GeoJSON/GPKG, with the source kept in-repo and documented in STAC `tiles` extension.

---

## 🧯 Deprecation & Backward Compatibility

* Deprecated datasets must include `deprecated: true` in STAC and a `deprecation_reason`.
* Provide replacement `rel` links to superseding Items/Collections.
* Maintain checksums + STAC for deprecated assets for reproducibility until the next major release.

---

## 🧠 MCP Compliance Summary

| MCP Principle       | Implementation                                                  |
| :------------------ | :-------------------------------------------------------------- |
| Documentation-first | This standard governs formats before ingestion.                 |
| Reproducibility     | Deterministic, validated formats; CI enforces integrity.        |
| Open Standards      | COG, GeoJSON, NetCDF CF, CSV/Parquet, STAC, JSON Schema.        |
| Provenance          | STAC + checksums + manifests + README lineage.                  |
| Auditability        | CI workflows + logs + schema checks provide a verifiable trail. |

---

## 🔗 Related Documentation

| Path                                     | Description                    |
| :--------------------------------------- | :----------------------------- |
| `docs/standards/metadata.md`             | Field-level metadata & schemas |
| `docs/architecture/data-architecture.md` | Lifecycle & storage hierarchy  |
| `docs/templates/provenance.md`           | Provenance record template     |
| `.github/workflows/stac-validate.yml`    | CI enforcement of standards    |

---

## 📅 Version History

| Version | Date       | Author                   | Summary                                                      |
| :-----: | :--------- | :----------------------- | :----------------------------------------------------------- |
|   v1.0  | 2025-10-04 | KFM Data Governance Team | Initial approved data/metadata formats.                      |
|   v1.1  | 2025-10-05 | KFM Engineering          | Added NetCDF CF, vector tiling, deprecation, CRS exceptions. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every File Open. Every Format Reproducible.”*
📍 [`docs/standards/data-formats.md`](.) · Official guide to KFM format standards (MCP compliant)

</div>
