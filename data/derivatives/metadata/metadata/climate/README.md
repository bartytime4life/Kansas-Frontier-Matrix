<div align="center">

# 🌡️ Kansas Frontier Matrix — Climate Derivative Metadata Summary  
`data/derivatives/metadata/metadata/climate/`

**Purpose:** Aggregate and summarize all **climate derivative metadata** files across the Kansas Frontier Matrix (KFM),  
providing a domain-level registry for provenance, validation, and cross-linking within the global derivative metadata system.

[![Build & Deploy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Build%20%26%20Deploy)](../../../../../.github/workflows/site.yml)
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../../../.github/workflows/codeql.yml)
[![Trivy](https://img.shields.io/badge/Container-Scan-informational)](../../../../../.github/workflows/trivy.yml)
[![Pre-Commit](https://img.shields.io/badge/Pre--Commit-enabled-success)](../../../../../.github/workflows/pre-commit.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-green)](../../../../../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC-BY%204.0-lightgrey)](../../../../../LICENSE)

</div>

---

## 📚 Table of Contents
- [Overview](#overview)
- [Metadata Summary Flow](#metadata-summary-flow)
- [Directory Layout](#directory-layout)
- [Summary JSON Schema](#summary-json-schema)
- [Example Summary File](#example-summary-file)
- [Validation & CI Hooks](#validation--ci-hooks)
- [Best Practices](#best-practices)
- [Relationships](#relationships)
- [Changelog](#changelog)

---

## 🧠 Overview

This directory serves as the **climate domain index** for all derivative metadata JSON files located in  
`data/derivatives/climate/metadata/`. It provides a unified, validated record of climate data layers  
including:

- 🌤️ **Temperature and precipitation composites** (Daymet, PRISM, NOAA Normals)  
- 💧 **Drought and anomaly indices** (SPI, PDSI, DSI)  
- ☀️ **Climatological trend layers** (mean annual, seasonal, anomaly rasters)  

This summary ensures that all climate derivatives are reproducible, linked to STAC assets,  
and accessible within the Knowledge Graph and KFM’s global registry.

---

## 🧭 Metadata Summary Flow

```mermaid
flowchart TD
  A["Climate Metadata JSONs\n(data/derivatives/climate/metadata/)"] --> B["Climate Summary JSON\n(this dir)"]
  B --> C["Derivative Metadata Registry\n(data/derivatives/metadata/metadata/)"]
  C --> D["STAC Catalog\n(data/stac/)"]
  D --> E["Knowledge Graph\nNeo4j · CIDOC CRM · OWL-Time"]
````

<!-- END OF MERMAID -->

---

## 🗂️ Directory Layout

```bash
data/
└── derivatives/
    └── metadata/
        └── metadata/
            └── climate/
                ├── climate_metadata_summary.json
                └── README.md
```

> The climate domain summary acts as an **authoritative manifest** connecting all climate datasets to their metadata, sources, and STAC items.

---

## 🧾 Summary JSON Schema

> Validate `climate_metadata_summary.json` with:
> `data/derivatives/metadata/metadata/schema/domain_metadata_summary.schema.json`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "KFM Climate Domain Metadata Summary",
  "type": "object",
  "required": ["id","title","domain","count","entries","last_updated","mcp_stage"],
  "properties": {
    "id": {"type":"string","const":"climate_metadata_summary"},
    "title": {"type":"string"},
    "description": {"type":"string"},
    "domain": {"type":"string","const":"climate"},
    "count": {"type":"integer","minimum":0},
    "entries": {
      "type":"array",
      "items": {
        "type":"object",
        "required":["id","title","path","format","source","stac_item"],
        "properties":{
          "id":{"type":"string"},
          "title":{"type":"string"},
          "path":{"type":"string"},
          "temporal_range":{"type":"string"},
          "variables":{"type":"array","items":{"type":"string"}},
          "format":{"type":"string"},
          "source":{"type":"string"},
          "stac_item":{"type":"string"},
          "license":{"type":"string"}
        },
        "additionalProperties": false
      }
    },
    "license":{"type":"string"},
    "last_updated":{"type":"string","format":"date"},
    "mcp_stage":{"type":"string","enum":["derivatives"]}
  },
  "additionalProperties": false
}
```

---

## 🧪 Example Summary File

```json
{
  "id": "climate_metadata_summary",
  "title": "Climate Derivative Metadata Summary",
  "description": "Aggregated summary of all processed climate derivative metadata files in KFM.",
  "domain": "climate",
  "entries": [
    {
      "id": "daymet_1980_2024_tmin_ks",
      "title": "Daily Minimum Temperature (Daymet, 1980–2024, Kansas)",
      "path": "../../../../climate/metadata/daymet_1980_2024_tmin_ks.json",
      "temporal_range": "1980–2024",
      "variables": ["tmin"],
      "format": "COG",
      "source": "../../../../sources/daymet.json",
      "stac_item": "../../../../stac/items/daymet_1980_2024_tmin_ks.json",
      "license": "Public Domain (NASA ORNL)"
    },
    {
      "id": "normals_1991_2020_prcp",
      "title": "Precipitation Normals (1991–2020, NOAA)",
      "path": "../../../../climate/metadata/normals_1991_2020_prcp.json",
      "temporal_range": "1991–2020",
      "variables": ["prcp"],
      "format": "COG",
      "source": "../../../../sources/noaa_normals.json",
      "stac_item": "../../../../stac/items/normals_1991_2020_prcp.json",
      "license": "Public Domain (NOAA NCEI)"
    },
    {
      "id": "drought_index_annual_ks",
      "title": "Annual Drought Severity Index (Kansas, 1895–2024)",
      "path": "../../../../climate/metadata/drought_index_annual_ks.json",
      "temporal_range": "1895–2024",
      "variables": ["drought_index"],
      "format": "Parquet",
      "source": "../../../../sources/noaa_ncei_drought.json",
      "stac_item": "../../../../stac/items/drought_index_annual_ks.json",
      "license": "CC-BY 4.0"
    }
  ],
  "count": 3,
  "license": "CC-BY 4.0",
  "last_updated": "2025-10-11",
  "mcp_stage": "derivatives"
}
```

> 💡 **Tip:** Always update `entries`, `count`, and `last_updated` when modifying or adding datasets in `data/derivatives/climate/metadata/`.

---

## 🔁 Validation & CI Hooks

```make
validate-climate-summary:
\tjsonschema -i data/derivatives/metadata/metadata/climate/climate_metadata_summary.json \
\t  data/derivatives/metadata/metadata/schema/domain_metadata_summary.schema.json

crosscheck-climate-vs-local:
\tpython scripts/validate_registry_crossrefs.py \
\t  --domain climate \
\t  --summary data/derivatives/metadata/metadata/climate/climate_metadata_summary.json \
\t  --local-root data/derivatives/climate/metadata

stac-validate-climate:
\tstac-validator $(shell jq -r '.entries[].stac_item' data/derivatives/metadata/metadata/climate/climate_metadata_summary.json)
```

> CI will **fail** if any `path` or `stac_item` is missing, invalid, or mismatched with `count`.

---

## ✅ Best Practices

| Category                  | Guideline                                                                 |
| ------------------------- | ------------------------------------------------------------------------- |
| **Completeness**          | Include all metadata files from `climate/metadata/`.                      |
| **Cross-Refs**            | Ensure paths to metadata, sources, and STAC items are valid and relative. |
| **Licensing**             | Use per-entry licenses; default to `CC-BY-4.0`.                           |
| **Versioning**            | Update `last_updated` and increment `count` after each addition or edit.  |
| **Naming Consistency**    | Match `id` across filenames, STAC items, and dataset paths.               |
| **Validation Discipline** | Run `make validate` before committing changes.                            |

---

## 🔗 Relationships

| Layer                        | Path                                          | Purpose                                                           |
| ---------------------------- | --------------------------------------------- | ----------------------------------------------------------------- |
| 🌡️ **Climate Metadata**     | `data/derivatives/climate/metadata/`          | Individual climate metadata JSONs.                                |
| 🧾 **Domain Summary (this)** | `data/derivatives/metadata/metadata/climate/` | Aggregated climate domain manifest.                               |
| 🧮 **Global Registry**       | `data/derivatives/metadata/metadata/`         | Central registry linking all domain summaries.                    |
| 🗺️ **STAC Catalog**         | `data/stac/`                                  | Global spatiotemporal catalog for all derivative datasets.        |
| 🧠 **Knowledge Graph**       | (Neo4j)                                       | Semantic layer connecting climate datasets and provenance chains. |

---

## 🗓 Changelog

| Version    | Date       | Notes                                                                                      |
| :--------- | :--------- | :----------------------------------------------------------------------------------------- |
| **v1.1.0** | 2025-10-11 | Added versioned frontmatter, schema excerpt, Make targets, and CI validation improvements. |
| **v0.1.0** | 2025-10-10 | Initial creation of climate domain metadata summary for registry.                          |

```
```
