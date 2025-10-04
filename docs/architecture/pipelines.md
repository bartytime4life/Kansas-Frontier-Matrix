<div align="center">

# ⚙️ Kansas Frontier Matrix — Pipeline Architecture  
`docs/architecture/pipelines.md`

**Mission:** Document the **Extract–Transform–Load (ETL) pipeline system**  
that powers the Kansas Frontier Matrix (KFM) — defining how raw datasets are  
fetched, standardized, validated, and transformed into reproducible and  
STAC-compliant knowledge assets.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../docs/)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../.github/workflows/stac-validate.yml)
[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../.github/workflows/site.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue)](../../LICENSE)

</div>

---

## 📚 Overview

The **KFM ETL pipeline architecture** automates the ingestion, cleaning, validation,  
and transformation of diverse datasets — ensuring that every published product  
can be rebuilt deterministically from source manifests.

The pipelines operate under these design goals:
- 🧠 **Documentation-first**: Every process has a README, manifest, and schema.  
- 🔁 **Reproducible**: Outputs regenerated identically from raw sources.  
- 🧩 **Modular**: Each domain operates independently via Makefile targets.  
- 🧾 **Auditable**: All operations logged, checksummed, and CI-validated.  
- 🌎 **Open-standard**: Outputs adhere to STAC, GeoTIFF, GeoJSON, and JSON Schema.

---

## 🏗️ ETL Pipeline Workflow

```mermaid
flowchart TD
  A["🌐 Sources\n(data/sources/)"] --> B["📦 Raw Data\n(data/raw/)"]
  B --> C["⚙️ Domain Pipelines\n(src/pipelines/)"]
  C --> D["✅ Processed Data\n(data/processed/)"]
  D --> E["🧩 Metadata & STAC\n(data/stac/)"]
  E --> F["🔐 Validation & Checksums\n(data/checksums/)"]
  F --> G["🌍 Visualization\n(data/tiles/, web/)"]

  style A fill:#fafafa,stroke:#999
  style B fill:#eef7ff,stroke:#0088cc
  style C fill:#fff0f5,stroke:#cc0088
  style D fill:#e8fff0,stroke:#33aa33
  style E fill:#fffbea,stroke:#e8a500
  style F fill:#f0e8ff,stroke:#8855cc
  style G fill:#f7f7f7,stroke:#555
````

<!-- END OF MERMAID -->

---

## 🧩 Pipeline Design Principles

| Principle                      | Implementation                                              |
| :----------------------------- | :---------------------------------------------------------- |
| **Deterministic Execution**    | Every run produces identical outputs from the same sources. |
| **Configurable via YAML/JSON** | Each pipeline uses a domain config file under `configs/`.   |
| **Composability**              | Pipelines can be chained (e.g., terrain → hydrology).       |
| **Logging & Checkpoints**      | Every step logs events in `data/work/logs/`.                |
| **Error Tolerance**            | Fails gracefully and reports traceable errors in CI/CD.     |
| **Version Control**            | Output files include temporal or version identifiers.       |

---

## ⚙️ Pipeline Directory Structure

```bash
src/pipelines/
├── terrain_pipeline.py
├── hydrology_pipeline.py
├── landcover_pipeline.py
├── climate_pipeline.py
├── hazards_pipeline.py
├── tabular_pipeline.py
└── text_pipeline.py
```

Each pipeline is responsible for:

* Fetching raw datasets from `data/sources/`
* Processing files from `data/raw/`
* Writing validated outputs to `data/processed/`
* Generating metadata, checksums, and logs

---

## 🧱 Domain-Specific Pipelines

| Domain        | Script                  | Input Sources                  | Output Directory            | Description                                             |
| :------------ | :---------------------- | :----------------------------- | :-------------------------- | :------------------------------------------------------ |
| **Terrain**   | `terrain_pipeline.py`   | USGS 3DEP LiDAR, KS DASC DEMs  | `data/processed/terrain/`   | Processes elevation, slope, and hillshade rasters.      |
| **Hydrology** | `hydrology_pipeline.py` | NHD, WBD, FEMA NFHL            | `data/processed/hydrology/` | Extracts rivers, watersheds, and flood zones.           |
| **Landcover** | `landcover_pipeline.py` | NLCD, USDA CDL                 | `data/processed/landcover/` | Generates vegetation and land use classifications.      |
| **Climate**   | `climate_pipeline.py`   | NOAA, Daymet                   | `data/processed/climate/`   | Builds temperature, precipitation, and drought indices. |
| **Hazards**   | `hazards_pipeline.py`   | NOAA, FEMA, USGS               | `data/processed/hazards/`   | Produces hazard datasets (tornado, wildfire, flood).    |
| **Tabular**   | `tabular_pipeline.py`   | Census, USDA, BEA              | `data/processed/tabular/`   | Cleans and aggregates socio-economic tables.            |
| **Text**      | `text_pipeline.py`      | OCR, KSHS, Library of Congress | `data/processed/text/`      | Parses, cleans, and annotates historical text archives. |

---

## 🧮 Pipeline Execution Model

### CLI (Makefile-driven)

Each pipeline is callable via Makefile for reproducibility:

```bash
# Run all pipelines
make all

# Run domain-specific pipeline
make terrain
make hydrology
make landcover
```

### Direct Python Execution

```bash
python src/pipelines/terrain_pipeline.py --config configs/terrain_config.yaml
```

> All pipeline runs generate logs in `data/work/logs/<domain>_etl_debug.log`
> and checksums in `data/checksums/<domain>/`.

---

## 🧾 Pipeline Lifecycle

| Stage         | Function                                        | Validation                     | Artifacts                  |
| :------------ | :---------------------------------------------- | :----------------------------- | :------------------------- |
| **Fetch**     | Download raw data from registered sources.      | License + schema validation.   | `data/raw/`                |
| **Transform** | Clean, reproject, and standardize files.        | CRS and schema checks.         | `data/processed/`          |
| **Enrich**    | Derive additional features (e.g., slope, NDVI). | QA metrics.                    | `data/processed/derived/`  |
| **Metadata**  | Generate STAC-compliant items.                  | JSON Schema + STAC validation. | `data/processed/metadata/` |
| **Checksum**  | Hash and record output files.                   | SHA-256 validation.            | `data/checksums/`          |
| **Visualize** | Generate map tiles and previews.                | File format + naming check.    | `data/tiles/`              |
| **Deploy**    | Publish results and update docs.                | CI/CD validation.              | `_site/`                   |

---

## 🧩 Logging & Provenance

Every pipeline maintains a reproducible trace of operations:

| Artifact                | Description                                  | Location                                |
| :---------------------- | :------------------------------------------- | :-------------------------------------- |
| **Run Logs**            | Detailed logs of each ETL step.              | `data/work/logs/<domain>_etl_debug.log` |
| **Checksum Files**      | SHA-256 hash for every output dataset.       | `data/checksums/<domain>/`              |
| **Provenance Metadata** | JSON lineage linking outputs to sources.     | `data/processed/metadata/<domain>/`     |
| **Error Reports**       | Captured exceptions and validation warnings. | `data/work/logs/errors/`                |

> Provenance metadata includes fields such as:
>
> * `derived_from`
> * `processing_date`
> * `checksum_reference`
> * `source_manifest`

---

## 🔐 CI/CD Integration

| Workflow                       | Function                                      | Trigger            |
| :----------------------------- | :-------------------------------------------- | :----------------- |
| **`fetch.yml`**                | Downloads new data from manifests.            | Scheduled / manual |
| **`checksums.yml`**            | Verifies dataset integrity.                   | On data change     |
| **`stac-validate.yml`**        | Validates metadata & STAC compliance.         | On PR / commit     |
| **`site.yml`**                 | Rebuilds documentation and publishes results. | On merge to `main` |
| **`codeql.yml` / `trivy.yml`** | Code and dependency security scans.           | Weekly             |

Logs are generated for every run in `data/work/logs/ci/`.

---

## 🧩 Example Pipeline Snippet

**`src/pipelines/terrain_pipeline.py`**

```python
def run(config):
    """Process Kansas LiDAR terrain data."""
    import geopandas as gpd
    import rasterio
    from utils.checksum import sha256_file
    from utils.stac import build_stac_item

    print("Fetching terrain data...")
    dem = rasterio.open(config["input_path"])
    print("Generating hillshade...")
    # Perform hillshade derivation...
    output = "data/processed/terrain/ks_hillshade_2018_2020.tif"
    # Compute checksum
    sha256_file(output)
    # Write metadata
    build_stac_item(output, domain="terrain", year="2020")
```

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                     |
| :---------------------- | :----------------------------------------------------------------- |
| **Documentation-first** | Each pipeline documented via README and in this architecture file. |
| **Reproducibility**     | Deterministic outputs validated by SHA-256 hashes.                 |
| **Open Standards**      | Uses GeoTIFF, GeoJSON, CSV, JSON Schema, STAC 1.0.0.               |
| **Provenance**          | Metadata and logs record full lineage for each dataset.            |
| **Auditability**        | CI/CD ensures validation and reporting at every step.              |

---

## 🧱 Design Patterns

| Pattern                     | Purpose                        | Implementation                       |
| :-------------------------- | :----------------------------- | :----------------------------------- |
| **Modular Pipelines**       | Independent domain workflows   | `src/pipelines/<domain>_pipeline.py` |
| **Config-Driven Execution** | Custom YAML/JSON configs       | `configs/<domain>_config.yaml`       |
| **Idempotent Outputs**      | Avoid duplicates or overwrites | Hash + timestamp enforcement         |
| **Parallel Processing**     | Speed and scalability          | Python multiprocessing, Dask         |
| **Continuous Validation**   | Integrated with CI/CD          | GitHub Actions + Makefile            |

---

## 📎 Related Documentation

| Path                                       | Description                                        |
| :----------------------------------------- | :------------------------------------------------- |
| `data/ARCHITECTURE.md`                     | Data system architecture (storage & lifecycle).    |
| `docs/architecture/data-architecture.md`   | Detailed data flow + provenance model.             |
| `docs/architecture/knowledge-graph.md`     | Semantic integration of datasets into RDF graph.   |
| `docs/architecture/web-ui-architecture.md` | Visualization and UI architecture.                 |
| `.github/workflows/README.md`              | Workflow governance for validation and deployment. |

---

## 📅 Version History

| Version | Date       | Summary                                                                  |
| :------ | :--------- | :----------------------------------------------------------------------- |
| v1.0    | 2025-10-04 | Initial ETL pipeline architecture documentation (domain modular system). |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Transformation Documented. Every Dataset Reproducible.”*
📍 [`docs/architecture/pipelines.md`](.) · ETL and domain pipeline architecture documentation.

</div>
