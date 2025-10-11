<div align="center">

# 🧮 Kansas Frontier Matrix — Processed Data  
`data/processed/`

**Mission:** Store all **cleaned, validated, and analysis-ready datasets** produced by the ETL pipeline —  
the bridge between **raw data ingestion (`data/raw/`)** and **derived analytical products (`data/derivatives/`)**  
within the Kansas Frontier Matrix (KFM) architecture.

[![Build & Deploy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Build%20%26%20Deploy)](../../.github/workflows/site.yml)  
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../.github/workflows/stac-validate.yml)  
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../.github/workflows/codeql.yml)  
[![Trivy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/trivy.yml?label=Trivy)](../../.github/workflows/trivy.yml)  
[![Pre-Commit](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/pre-commit.yml?label=Pre--Commit)](../../.github/workflows/pre-commit.yml)  
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../docs/)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../LICENSE)  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow)](../../LICENSE)  
[![Doc Version](https://img.shields.io/badge/Doc%20Version-v1.3-informational)](#-version--changelog)

</div>

---

## 📚 Overview

The `data/processed/` directory houses **post-ETL datasets** that have been standardized,  
cleaned, and reprojected for consistent analytical use.  
These represent the **intermediate data tier** in KFM — bridging **raw ingestion** and **derivative generation**,  
and ensuring reproducible, documented transformations in alignment with the **Master Coder Protocol (MCP)**.

### Contents

- 🗺️ Normalized spatial layers (GeoJSON, COG GeoTIFF)  
- 📊 Cleaned tabular datasets (CSV, Parquet)  
- 🧠 AI/NLP feature tables and summaries (entities, topics, events)  
- 🧾 Temporal, text, or event data standardized for timeline mapping  

Each dataset is traceable, reproducible, and indexed in the **STAC Catalog** with corresponding  
checksums and metadata entries.

---

## 🧭 Data Flow Context

```mermaid
flowchart LR
  R["data/raw/**\nRaw ingestion"] --> P["data/processed/**\nClean · Standardize · Reproject"]
  P --> D["data/derivatives/**\nComposite · Analytical layers"]
  P --> S["data/stac/**\nMetadata + Provenance"]
  P --> C["data/checksums/**\nIntegrity manifests"]
%% END OF MERMAID
````

<!-- END OF MERMAID -->

---

## 🗂️ Directory Layout

```bash
data/
└── processed/
    ├── terrain/                 # Clean DEMs, slope-ready rasters
    ├── hydrology/               # Flow accumulation, sink-filled DEMs
    ├── landcover/               # Pre-classified NDVI/landcover rasters
    ├── climate/                 # Aggregated temperature/precipitation grids
    ├── hazards/                 # Clean event frequency rasters, SPI datasets
    ├── tabular/                 # Processed CSV/Parquet tables
    ├── text/                    # Cleaned OCR/NLP text corpora
    ├── metadata/                # JSON metadata describing all processed datasets
    ├── checksums/               # SHA-256 hashes for integrity verification
    └── README.md
```

> Each subfolder mirrors `data/derivatives/`, maintaining one-to-one lineage between
> **raw → processed → derivative** data chains.

---

## ⚙️ Processing Standards

| Type        | Format        | CRS / Encoding | Description                             |
| :---------- | :------------ | :------------- | :-------------------------------------- |
| **Raster**  | GeoTIFF (COG) | EPSG:4326      | Reprojected, tiled, cloud-optimized     |
| **Vector**  | GeoJSON       | EPSG:4326      | Simplified geometries, topology-checked |
| **Tabular** | CSV / Parquet | UTF-8          | Normalized headers, schema-validated    |
| **Text**    | JSON / TXT    | UTF-8          | Cleaned OCR or NLP pipeline outputs     |

### ETL Quality Controls

* 🔄 **Reprojection:** All geospatial data normalized to WGS84.
* 🗜️ **Compression:** LZW/Deflate, ensuring web efficiency.
* 🧩 **Validation:** Schema checks, geometry repair, and missing value audits.
* 🧮 **Checksums:** `.sha256` files ensure deterministic verification.
* 🧠 **Metadata:** JSON metadata logs lineage and software parameters.

---

## 🌐 STAC Catalog Integration

All processed datasets are indexed in the KFM [STAC Catalog](../stac/).
Each entry (`data/stac/items/processed_*.json`) includes lineage, provenance, and processing metadata.

**Example:**

```json
{
  "id": "precipitation_processed_2024",
  "type": "Feature",
  "properties": {
    "title": "Precipitation (Processed) 2024",
    "datetime": "2024-06-01T00:00:00Z",
    "derived_from": ["data/raw/noaa_precip_2024.csv"],
    "processing:software": "Python + xarray + rasterio",
    "mcp_provenance": "sha256:e43f91..."
  },
  "assets": {
    "data": {
      "href": "./climate/precipitation_2024.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized"
    }
  }
}
```

---

## 🧬 Provenance & Versioning

| Aspect              | Implementation                                                                   |
| :------------------ | :------------------------------------------------------------------------------- |
| **Checksums**       | Every file has a `.sha256` integrity manifest under `data/processed/checksums/`. |
| **Metadata**        | JSON metadata in `metadata/` describes lineage, source, and processing params.   |
| **Version Control** | Large files tracked via **Git LFS** or **DVC**, lightweight via Git.             |
| **Automation**      | CI validates STAC consistency and checksum parity on each PR.                    |

**Document versioning policy (SemVer for docs):**

* **MAJOR**: structural changes to this README or directory contracts (e.g., required subfolders, required formats).
* **MINOR**: content additions/clarifications (new sections, examples, ETL flags).
* **PATCH**: typo fixes, broken link repairs, minor badge/wording tweaks.

---

## ➕ Adding New Processed Data

1. **Add dataset** under the appropriate subfolder (e.g., `climate/` or `hydrology/`).

2. **Generate checksum** file:

   ```bash
   sha256sum my_dataset.tif > checksums/my_dataset.tif.sha256
   ```

3. **Create STAC metadata** JSON under `metadata/`.

4. **Validate locally** before committing:

   ```bash
   make validate-processed
   ```

5. **Submit PR** including:

   * Data source reference
   * Processing method & software used
   * License & attribution

GitHub Actions will verify:

* STAC schema compliance
* Checksum validation
* Metadata completeness

---

## 🧠 MCP Compliance Matrix

| MCP Principle           | Implementation                                         |
| :---------------------- | :----------------------------------------------------- |
| **Documentation-first** | Every dataset includes README + STAC metadata.         |
| **Reproducibility**     | Deterministic ETL and checksum tracking.               |
| **Open Standards**      | Uses COG, GeoJSON, CSV, Parquet, STAC 1.0.             |
| **Provenance**          | Metadata + checksum lineage links ensure traceability. |
| **Auditability**        | CI validation + Git LFS/DVC change tracking.           |

---

## 📖 References

* [STAC Specification 1.0](https://stacspec.org)
* [GeoJSON RFC 7946](https://datatracker.ietf.org/doc/html/rfc7946)
* [Cloud Optimized GeoTIFF (COG)](https://www.cogeo.org)
* [GDAL & Rasterio](https://gdal.org)
* [DVC: Data Version Control](https://dvc.org)
* [Master Coder Protocol](../../docs/standards/)

---

## 🧱 Version & Changelog

| Version  | Date       | Notes                                                                                                            |
| :------- | :--------- | :--------------------------------------------------------------------------------------------------------------- |
| **v1.3** | 2025-10-11 | Added explicit **Version & Changelog** section, SemVer policy for docs, and version badge; minor clarifications. |
| **v1.2** | 2025-10-11 | Protocol alignment: badges, Mermaid flow, MCP matrix, STAC/Checksum parity notes.                                |
| **v1.1** | 2025-10-10 | Expanded layout and ETL quality controls; added PR validation guidance.                                          |
| **v1.0** | 2025-10-04 | Initial processed data README with STAC integration and directory contract.                                      |

---

<div align="center">

**Kansas Frontier Matrix** — *“From raw to ready: reproducible layers for Kansas’s digital frontier.”*
📍 [`data/processed/`](.) · Foundation for all analytical and derivative data products.

</div>
```
