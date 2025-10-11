<div align="center">

# 🧮 Kansas Frontier Matrix — Climate Derivative Metadata  
`data/derivatives/climate/metadata/`

**Purpose:** Maintain structured, machine-readable **metadata JSONs** describing every processed  
**climate derivative artifact** (COG · GeoJSON · Parquet · CSV) and link them to their  
**provenance**, **checksums**, and **STAC representations** for full lifecycle transparency.

[![Build & Deploy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Build%20%26%20Deploy)](../../../../../.github/workflows/site.yml)  
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../../../.github/workflows/stac-validate.yml)  
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../../../.github/workflows/codeql.yml)  
[![Trivy](https://img.shields.io/badge/Container-Scan-informational)](../../../../../.github/workflows/trivy.yml)  
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-green)](../../../../../docs/)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../../LICENSE)

</div>

---

## 📚 Overview

The `metadata/` directory contains **JSON metadata files** describing each processed **climate derivative**  
under `data/derivatives/climate/`.  

Each file defines:
- dataset **origin, lineage, and version**
- **variables**, units, and temporal coverage  
- **coordinate reference system** and **spatial extent**
- relative links to **checksums** and **STAC items**

These metadata records form the connective tissue between:
- raw and derived datasets  
- integrity manifests (`/checksums`)  
- and the global **STAC catalog** (`data/stac/`)  

They ensure **traceability**, **reproducibility**, and **semantic interoperability** across the entire  
Kansas Frontier Matrix (KFM) ecosystem.

---

## 🧭 Metadata Generation Flow

```mermaid
flowchart TD
  A["Sources\nNOAA · Daymet · Normals"] --> B["ETL\nNormalize · Derive"]
  B --> C["Climate Derivatives\nCOG · GeoJSON · Parquet · CSV"]
  C --> D["Metadata JSONs\nvariables · CRS · temporal range · provenance"]
  D --> E["Checksums\n*.sha256 (validation)"]
  D --> F["STAC Items\nassets + metadata"]
  F --> G["Knowledge Graph\nnodes + relations"]
  G --> H["API + Web UI\ntimeline · search · layer metadata"]
%% END OF MERMAID
<!-- END OF MERMAID -->
````

---

## 🗂️ Directory Layout

```bash
metadata/
├── daymet_1980_2024_tmin_ks.json
├── daymet_1980_2024_prcp_ks.json
├── normals_1991_2020_prcp.json
├── drought_index_annual_ks.json
└── README.md
```

Each `.json` file corresponds to a single derivative dataset and follows
the **KFM STAC/DCAT-aligned schema**.

---

## 🧾 JSON Metadata Schema (Canonical Example)

```json
{
  "id": "daymet_1980_2024_tmin_ks",
  "title": "Daily Minimum Temperature (Daymet, 1980–2024, Kansas)",
  "description": "Derived daily minimum temperature dataset aggregated for Kansas from NASA Daymet v4.",
  "type": "raster",
  "format": "COG",
  "file": "../daymet_1980_2024_tmin_ks_cog.tif",
  "checksum": "../checksums/daymet_1980_2024_tmin_ks_cog.tif.sha256",
  "source": "../../../sources/daymet.json",
  "stac_item": "../../../stac/items/daymet_1980_2024_tmin_ks.json",
  "spatial": {
    "crs": "EPSG:4326",
    "bbox": [-102.05, 36.99, -94.59, 40.00]
  },
  "temporal": {
    "start": "1980-01-01",
    "end": "2024-12-31"
  },
  "variables": [
    {
      "name": "tmin",
      "units": "°C",
      "description": "Daily minimum temperature"
    }
  ],
  "license": "CC-BY-4.0",
  "created": "2025-10-10",
  "last_updated": "2025-10-11",
  "mcp_stage": "derivatives"
}
```

💡 **Tip:** Keep all relative paths valid and synchronized with
`data/sources/<source>.json` and `data/stac/items/<id>.json`.
This guarantees validation success during CI (`make validate` / `stac-validate.yml`).

---

## 🧩 Relationship to Other Metadata Layers

| Layer                  | Path                                  | Purpose                                                        |
| :--------------------- | :------------------------------------ | :------------------------------------------------------------- |
| 🧭 Source Metadata     | `data/sources/`                       | Defines raw dataset provenance (Daymet, NOAA, etc.)            |
| 🧮 Derivative Metadata | `data/derivatives/climate/metadata/`  | Documents ETL-processed derivative products                    |
| 🧾 Checksums           | `data/derivatives/climate/checksums/` | Ensures data file integrity                                    |
| 🗺️ STAC Catalog       | `data/stac/`                          | Registers spatial + temporal metadata and asset URIs           |
| 🧠 Knowledge Graph     | Neo4j                                 | Stores semantic relationships (HAS_DERIVATIVE, HAS_PROVENANCE) |

---

## 🧠 Usage in the Pipeline

* **ETL Stage:** Python ETL scripts auto-generate or update metadata after processing.
* **Validation:** JSON Schema + STAC validators confirm structural and referential integrity.
* **CI/CD:** `stac-validate.yml` ensures every derivative has a matching metadata + checksum file.
* **Graph Load:** Neo4j ingestion links metadata fields (`temporal.start`, `variables.name`, etc.)
  into the KFM knowledge graph entities.

---

## 🧱 Metadata Best Practices

| Category       | Guideline                                                       |
| :------------- | :-------------------------------------------------------------- |
| ✅ Completeness | Each derivative must include a metadata JSON file.              |
| 🔗 Linkage     | Reference checksum, STAC item, and source manifest explicitly.  |
| 🕓 Timestamps  | Include both `created` and `last_updated` in ISO 8601 format.   |
| 🧮 Variables   | List all derived/measured variables with units and definitions. |
| 🧾 Licensing   | Always record dataset-specific license (default: CC-BY-4.0).    |
| 🧪 Validation  | Run `make validate` or rely on CI schema enforcement.           |

---

## 🔒 Reproducibility & MCP Alignment

These metadata structures fully implement the **Master Coder Protocol (MCP)** principles:

* 📜 **Provenance:** Every artifact can trace its lineage back to original sources.
* 🧩 **Transparency:** Metadata bridges data, code, and documentation layers.
* 💡 **Machine-readability:** JSON/STAC/DCAT-aligned for cross-system interoperability.
* 🧮 **Reproducibility:** Metadata ensures anyone can rebuild, validate, and verify the pipeline.

Together, they make the Kansas Frontier Matrix a **verifiable scientific knowledge system**.

---

## 🧱 Related Documentation

* [`data/derivatives/climate/checksums/README.md`](../checksums/README.md) — Hash integrity workflow
* [`data/stac/README.md`](../../../stac/README.md) — STAC catalog schema
* [`data/sources/README.md`](../../../sources/README.md) — Source dataset manifests
* [`docs/architecture.md`](../../../../../docs/architecture.md) — ETL & provenance design

---

## 🗓️ Version History

| Version  | Date       | Notes                                                                                                |
| :------- | :--------- | :--------------------------------------------------------------------------------------------------- |
| **v1.1** | 2025-10-11 | Upgraded to KFM Markdown Protocols (v1.0); added front-matter, version block, CI/validation details. |
| **v1.0** | 2025-10-10 | Initial creation of climate derivative metadata schema and examples.                                 |

---

```
