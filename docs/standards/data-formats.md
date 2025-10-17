<div align="center">

# 🗂️ Kansas Frontier Matrix — **Data Format Standards**  
`docs/standards/data-formats.md`

**Master Coder Protocol (MCP-DL v6.3+) · Reproducibility · Interoperability · Provenance · Validation**

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)](../../docs/)
[![Docs Validated](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/docs-validate.yml?label=Docs%20Validated&color=blue)](../../.github/workflows/docs-validate.yml)
[![STAC Validate](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/stac-validate.yml?label=STAC%20Validate&color=green)](../../.github/workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL&logo=github)](../../.github/workflows/codeql.yml)
[![Trivy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/trivy.yml?label=Trivy&logo=security)](../../.github/workflows/trivy.yml)
[![Security: SLSA-3 (Target)](https://img.shields.io/badge/Security-SLSA--3%20(Target)-orange)](../standards/security.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../LICENSE)

</div>

---

```yaml
---
title: "Kansas Frontier Matrix — Data Format Standards"
version: "v1.3.0"
last_updated: "2025-10-18"
owners: ["@kfm-data","@kfm-architecture","@kfm-docs"]
tags: ["standards","formats","stac","csvw","netcdf","geotiff","geojson","provenance","validation"]
status: "Stable"
scope: "Monorepo-Wide"
license: "CC-BY 4.0"
semver_policy: "MAJOR.MINOR.PATCH"
audit_framework: "MCP-DL v6.3"
ci_required_checks:
  - docs-validate
  - stac-validate
  - pre-commit
  - codeql
  - trivy
semantic_alignment:
  - STAC 1.0
  - DCAT 2.0
  - JSON Schema
  - ISO 19115/19139 (subset via STAC fields)
  - ISO 8601 (time)
  - NetCDF CF-1.8
  - FAIR Principles
  - CIDOC CRM · OWL-Time (temporal semantics)
---
````

---

## 📚 Overview

KFM uses **open, non-proprietary** formats that are **scriptable, validated, portable**, and enforceable in CI.
This standard defines:

* 📦 **Approved file formats** by domain (spatial, tabular, text, catalogs).
* 🧾 **Metadata models** (**STAC**, **DCAT**) & **validation** (JSON Schema).
* 🧱 **Encoding, naming, compression** conventions & lifecycle states.
* 🔁 CI-enforced **integrity** (checksums/signatures) & **conformance** (schemas).

> **MCP Principles:** Documentation-first · Reproducible · Open-standard · Provenance-tracked · Auditable

---

## 🧩 Approved Formats by Domain

| Domain        | Data Type                       | Approved Formats                                                      | Notes                                           |
| :------------ | :------------------------------ | :-------------------------------------------------------------------- | :---------------------------------------------- |
| **Terrain**   | Raster (DEM, hillshade, slope)  | **COG GeoTIFF** (`.tif`), preview `.png`                              | Elevation & derivatives                         |
| **Hydrology** | Vector (rivers, basins, floods) | **GeoJSON** (`.geojson`), **GeoPackage** (`.gpkg`)                    | NHD-derived flowlines, watersheds               |
| **Landcover** | Raster (classes, NDVI)          | **COG GeoTIFF** (`.tif`), preview `.png`                              | Provide class table & palette                   |
| **Climate**   | Raster / Time-series            | **COG** (`.tif`), **NetCDF4 CF-1.8** (`.nc`), `.csv`                  | CF-compliant NetCDF for multi-var time          |
| **Hazards**   | Vector / Raster / Events        | `.geojson`, `.tif`, `.csv` / `.jsonl`                                 | Tornadoes, floods, wildfires (with STAC events) |
| **Tabular**   | Structured tables               | `.csv` (+ CSVW schema), **Parquet** (`.parquet`)                      | Parquet for large/partitioned data              |
| **Text**      | Unstructured / corpora          | **JSON Lines** (`.jsonl`), `.txt`, `.csv`                             | OCR, transcripts, articles                      |
| **Metadata**  | Dataset & catalog descriptors   | **STAC 1.0 JSON** (Items/Collections/Assets), **JSON Schema**         | STAC + custom schemas                           |
| **Tiles**     | Web map tiles (optional)        | **PMTiles** (`.pmtiles`) or MVT (`.pbf`), XYZ/WMTS, PNG/WEBP previews | Source & recipe documented in STAC `tiles` ext  |

---

## 🌍 Spatial Data Standards

### Raster (Terrain, Climate, Landcover)

| Property        | Standard / Requirement                                                                                                                                       |
| :-------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Format**      | **Cloud-Optimized GeoTIFF** (COG)                                                                                                                            |
| **CRS**         | Default **EPSG:4326** (WGS84). Analysis CRS (e.g., EPSG:5070/2163) allowed **only with** documented rationale in STAC + README and companion WGS84 view/COG. |
| **Compression** | **DEFLATE** or **LZW** (`PREDICTOR=2` for ints/`3` for floats where applicable).                                                                             |
| **Tiling**      | Internal tiles, **512×512** preferred.                                                                                                                       |
| **Overviews**   | Internal pyramid {2,4,8,16} (or `--overview-level auto`).                                                                                                    |
| **NoData**      | Explicit nodata; record in `raster:nodata`.                                                                                                                  |
| **Bit depth**   | Float32 for continuous (DEM/temperature), UInt8/UInt16 for categorical.                                                                                      |
| **Aux data**    | Color tables + `classification:classes` for categorical rasters.                                                                                             |
| **COG tags**    | Include `AREA_OR_POINT`, `TIFFTAG_COPYRIGHT` (license), `TIFFTAG_DATETIME` (UTC ISO-8601).                                                                   |

**COG creation (reference)**

```bash
rio cogeo create input.tif output_cog.tif \
  --blocksize 512 \
  --overview-level 4 \
  --overview-resampling average \
  --web-optimized \
  --compress DEFLATE --bigtiff IF_SAFER
```

> **Projection exceptions** must include a WGS84 companion or overview, and document `proj:epsg`, `proj:wkt2`, and rationale in STAC + dataset README.

---

### Vector (Hydrology, Hazards, Boundaries)

| Property     | Standard / Requirement                                                                                                  |
| :----------- | :---------------------------------------------------------------------------------------------------------------------- |
| **Format**   | **GeoJSON** (RFC 7946) default; **GPKG** for multi-layer/large sets.                                                    |
| **CRS**      | **EPSG:4326** (`[lon, lat]`).                                                                                           |
| **Encoding** | UTF-8 (no BOM).                                                                                                         |
| **Schema**   | Attribute names `snake_case`; SI units recorded in STAC/CSVW; domain schemas (NHD/USGS) where applicable.               |
| **Topology** | Valid geometries; repair self-intersections; web-simplified copy is allowed **in addition to** canonical high-res file. |

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
  "geometry": { "type": "LineString", "coordinates": [[-95.0,39.0], ...] }
}
```

---

## 🧮 Tabular Data Standards

| Attribute          | Requirement                                               |
| :----------------- | :-------------------------------------------------------- |
| **Format**         | `.csv` (RFC 4180) with header row **or** **Parquet**.     |
| **Encoding**       | UTF-8.                                                    |
| **Delimiter**      | Comma (`,`); no stray delimiters/quotes.                  |
| **Missing values** | `NULL` or empty string (avoid magic values like `-9999`). |
| **Units**          | Declare via CSVW/STAC; SI preferred.                      |
| **Validation**     | JSON Schema **required** for ingestion.                   |

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
        {"name": "population", "datatype": "integer", "aboutUrl": "https://example.org/county/{county}"},
        {"name": "median_income_usd", "datatype": "integer", "titles": "USD"}
      ],
      "primaryKey": ["year","county"]
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
| **Container**     | **JSON Lines** (`.jsonl`) — one document per line.                              |
| **Fields (min)**  | `id`, `source`, `text`, `date` (ISO-8601), `lang` (ISO 639-1), optional `tags`. |
| **Attribution**   | `source` (**required**) with URL/accession when available.                      |
| **Normalization** | Keep raw + normalized/tokenized variants in distinct fields/files.              |

```json
{"id":"ks_news_1898_001","source":"Topeka Daily Capital","date":"1898-07-14","lang":"en","text":"Kansas River floodwaters rising rapidly."}
```

---

## 🧾 Metadata & Catalogs

| Type           | Format                           | Notes                                                                             |
| :------------- | :------------------------------- | :-------------------------------------------------------------------------------- |
| **Dataset**    | **STAC Item** (`.json`)          | Per dataset; include `proj:*`, `raster:*`, `checksum:*`, license, temporal range. |
| **Collection** | **STAC Collection** (`.json`)    | Thematic/time grouping; include providers, keywords, license, `extent`.           |
| **Checksum**   | `.sha256` & `checksum:multihash` | One sidecar per file; multihash inside STAC asset.                                |
| **Schema**     | **JSON Schema**                  | Validate metadata, tabular schemas, and config files.                             |

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

**STAC Collection (skeleton)**

```json
{
  "stac_version": "1.0.0",
  "type": "Collection",
  "id": "kfm_hazards_tornadoes",
  "description": "Kansas tornado tracks and points (1950–present)",
  "extent": { "spatial": { "bbox": [[-102.1,36.9,-94.6,40.1]] }, "temporal": { "interval": [["1950-01-01T00:00:00Z", null]] } },
  "license": "cc-by-4.0",
  "keywords": ["tornado","severe-weather","hazards","kansas"],
  "providers": [{ "name": "NOAA NCEI", "roles": ["producer","licensor"] }]
}
```

---

## 🔐 Integrity, Signatures & Lifecycle

### Checksums & Manifests

| File                      | Purpose                                           |
| :------------------------ | :------------------------------------------------ |
| `*.sha256`                | Verify file integrity (SHA-256).                  |
| `manifest.checksums.json` | Repository/domain-wide list of checksums & sizes. |

`.sha256` example

```
4a2f7f3e94a1f12c7bde9b6d8120ee9876ab2b74d7c63c5c0a1a86b8a23de98a  ks_1m_dem_2018_2020.tif
```

### Lifecycle States

| State          | STAC Flag                    | Policy                                                                                                      |
| :------------- | :--------------------------- | :---------------------------------------------------------------------------------------------------------- |
| **Draft**      | `private:true` (out-of-tree) | Internal testing only; not published.                                                                       |
| **Active**     | default                      | Current canonical dataset.                                                                                  |
| **Deprecated** | `deprecated:true`            | Provide `rel` links to replacement; keep checksums & STAC for reproducibility until next **major** release. |
| **Archived**   | Collection-level note        | Retained for history; read-only.                                                                            |

> **Planned:** Cosign/Sigstore `provenance.yml` to sign artifacts (see Security Standards).

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
* Line endings **LF**.

### Packaging

| Purpose  | Format             | Notes                                              |
| :------- | :----------------- | :------------------------------------------------- |
| Delivery | `.zip` / `.tar.gz` | Preserve structure; include checksums + STAC JSON. |
| Internal | DEFLATE/LZW        | Use embedded compression in GeoTIFF/NetCDF.        |

> Avoid proprietary archives (e.g., `.rar`).

---

## ⏱️ Temporal & Units Conventions

* **Dates/times:** ISO-8601 (UTC).
* **Ranges:** STAC `start_datetime`/`end_datetime`.
* **Units:** SI preferred; record in CSVW/STAC (`unit`, `uom`).
* **CF Conventions:** For NetCDF, include units, long_name, standard_name, and QC flags; chunking + zlib/shuffle recommended.

---

## 🧪 Validation & CI Requirements

| Check                | Tool / Workflow                       | Applies To             |
| :------------------- | :------------------------------------ | :--------------------- |
| **Checksum**         | `make checksums`                      | All assets             |
| **STAC**             | `stac-validator`                      | Items/Collections      |
| **JSON Schema**      | `jsonschema`                          | Tables/config/metadata |
| **COG**              | `gdalinfo` / `cog_validate`           | Rasters                |
| **NetCDF CF**        | `ncdump` / custom CF checks           | `.nc`                  |
| **CI Orchestration** | `.github/workflows/stac-validate.yml` | Continuous             |

Example snippet:

```yaml
name: STAC & Data Validate
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: pipx install stac-validator jsonschema
      - run: stac-validator data/stac --recursive --links
      - run: python tools/validate_json.py --schema schemas/tabular.schema.json --data data/processed/tabular/**/*.json
```

---

## 🌐 Web & Tile Services (Optional)

* Raster tiles: **XYZ/WMTS** with PNG/WEBP; record tile endpoints in STAC `links` or `tiles` ext.
* Vector tiles: **PMTiles** or **MVT**, generated from canonical **GeoJSON/GPKG**; store recipe (tippecanoe/tiles build args) and include a `source` asset pointing to the canonical file.

---

## 🧭 FAIR & DCAT Crosswalk

| FAIR              | Implementation                                                                       |
| :---------------- | :----------------------------------------------------------------------------------- |
| **Findable**      | STAC catalog under `data/stac/` + keywords, providers, DOIs/URLs where applicable.   |
| **Accessible**    | HTTP/Git LFS/DVC references; license & access constraints in STAC `license`/`links`. |
| **Interoperable** | Open formats (COG/GeoJSON/NetCDF/Parquet), JSON Schema, CF conventions.              |
| **Reusable**      | Clear citation, license, provenance, checksums; deprecation links and versioning.    |

**DCAT Mapping (indicative)**

| DCAT Field        | STAC / File Field                         |
| :---------------- | :---------------------------------------- |
| `dct:title`       | STAC `id` / collection `title`            |
| `dct:description` | STAC `description`                        |
| `dct:license`     | STAC `license`                            |
| `dct:temporal`    | STAC `start_datetime`/`end_datetime`      |
| `dct:spatial`     | STAC `bbox` (collection `extent.spatial`) |

---

## 🧾 Repository Data Layout (Alignment)

| Directory         | Purpose                                                                      |
| :---------------- | :--------------------------------------------------------------------------- |
| `data/sources/`   | JSON **manifests** for external sources (URLs, license, notes).              |
| `data/raw/`       | Downloaded raw data (tracked via DVC/LFS pointers; not committed wholesale). |
| `data/processed/` | Canonical processed outputs (COGs/GeoJSON/Parquet/NetCDF) + thumbnails.      |
| `data/stac/`      | STAC **Items/Collections** describing all processed assets.                  |
| `data/work/logs/` | ETL provenance logs (runtime, inputs, hashes, script version).               |

---

## 🧠 MCP Compliance Summary

| MCP Principle       | Implementation                                                 |
| :------------------ | :------------------------------------------------------------- |
| Documentation-first | This standard governs formats & metadata before ingestion.     |
| Reproducibility     | Deterministic formats; CI validation & checksums.              |
| Open Standards      | COG, GeoJSON, NetCDF CF, CSV/Parquet, STAC, JSON Schema, DCAT. |
| Provenance          | STAC + checksums + manifests + README lineage.                 |
| Auditability        | CI workflows + logs + schema checks + lifecycle flags.         |

---

## 🔗 Related Documentation

| Path                                     | Description                                 |
| :--------------------------------------- | :------------------------------------------ |
| `docs/standards/metadata.md`             | Field-level metadata & JSON Schemas         |
| `docs/architecture/data-architecture.md` | Lifecycle & storage hierarchy               |
| `docs/standards/security.md`             | SLSA/CodeQL/Trivy policies & signing        |
| `docs/standards/provenance_dataset.md`   | Dataset provenance template                 |
| `.github/workflows/stac-validate.yml`    | CI enforcement of standards                 |
| `docs/audit/repository_compliance.md`    | Audit (RMI/DCI), governance plan, sign-offs |

---

## 📅 Version History

| Version | Date       | Author           | Summary                                                                                                   |
| :------ | :--------- | :--------------- | :-------------------------------------------------------------------------------------------------------- |
| v1.3.0  | 2025-10-18 | @kfm-data        | Added FAIR/DCAT crosswalk, lifecycle states, tiles guidance, CI snippets, CF notes, repo layout alignment |
| v1.1.0  | 2025-10-05 | @kfm-engineering | Added NetCDF CF, vector tiling, deprecation, CRS exceptions                                               |
| v1.0.0  | 2025-10-04 | @kfm-data        | Initial approved data/metadata formats                                                                    |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every File Open. Every Format Reproducible.”*
📍 `docs/standards/data-formats.md` — Official MCP-aligned format standards for KFM

</div>
