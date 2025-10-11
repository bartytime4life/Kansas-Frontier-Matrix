<div align="center">

# 🌾 Kansas Frontier Matrix — Landcover Derivative Metadata Summary  
`data/derivatives/metadata/metadata/landcover/`

**Purpose:** Aggregate and summarize all **landcover derivative metadata** entries across the Kansas Frontier Matrix (KFM),  
providing a centralized registry for vegetation, land-use, and surface classification datasets derived through ETL workflows.

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

This folder contains the **domain summary registry** for landcover derivative metadata from  
`data/derivatives/landcover/metadata/`.

It provides a unified reference for:
- 🌿 **Landcover change products** (e.g., NLCD composites, historical vegetation rasters)  
- 🪵 **Ecological layers** (canopy height, biome zones, prairie extent)  
- 🌾 **Land-use transformations** and categorical classification models  

The summary aligns the domain with KFM’s **Global Derivative Metadata Registry** and **STAC Catalog**, enabling complete **traceability**, **validation**, and **interoperability**.

---

## 🧭 Metadata Summary Flow

```mermaid
flowchart TD
  A["Landcover Metadata JSONs\n(data/derivatives/landcover/metadata/)"] --> B["Landcover Summary JSON\n(this dir)"]
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
            └── landcover/
                ├── landcover_metadata_summary.json
                └── README.md
```

> The summary JSON acts as the **authoritative domain-level manifest** for all processed landcover derivatives, linking each dataset to its metadata file and **STAC item**.

---

## 🧾 Summary JSON Schema

> Validate `landcover_metadata_summary.json` against:
> `data/derivatives/metadata/metadata/schema/domain_metadata_summary.schema.json`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "KFM Landcover Domain Metadata Summary",
  "type": "object",
  "required": ["id","title","domain","count","entries","last_updated","mcp_stage"],
  "properties": {
    "id": {"type":"string","const":"landcover_metadata_summary"},
    "title": {"type":"string"},
    "description": {"type":"string"},
    "domain": {"type":"string","const":"landcover"},
    "count": {"type":"integer","minimum":0},
    "entries": {
      "type":"array",
      "items": {
        "type":"object",
        "required": ["id","title","path","format","source","stac_item"],
        "properties": {
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
  "id": "landcover_metadata_summary",
  "title": "Landcover Derivative Metadata Summary",
  "description": "Aggregated metadata summary of all landcover derivative datasets in KFM.",
  "domain": "landcover",
  "entries": [
    {
      "id": "nlcd_1992_2021",
      "title": "National Land Cover Database (1992–2021, Kansas)",
      "path": "../../../../landcover/metadata/nlcd_1992_2021.json",
      "temporal_range": "1992–2021",
      "variables": ["landcover_class"],
      "format": "COG",
      "source": "../../../../sources/usgs_nlcd.json",
      "stac_item": "../../../../stac/items/nlcd_1992_2021.json",
      "license": "Public Domain (USGS)"
    },
    {
      "id": "vegetation_zones_1850_ks",
      "title": "Vegetation Zones (1850s, Kansas)",
      "path": "../../../../landcover/metadata/vegetation_zones_1850_ks.json",
      "temporal_range": "1850",
      "variables": ["vegetation_type"],
      "format": "GeoJSON",
      "source": "../../../../sources/kars_historic_veg.json",
      "stac_item": "../../../../stac/items/vegetation_zones_1850_ks.json",
      "license": "CC-BY 4.0"
    },
    {
      "id": "landuse_1900_2000_composite",
      "title": "Land Use Composite (1900–2000, Kansas)",
      "path": "../../../../landcover/metadata/landuse_1900_2000_composite.json",
      "temporal_range": "1900–2000",
      "variables": ["landuse_type"],
      "format": "COG",
      "source": "../../../../sources/usda_landuse.json",
      "stac_item": "../../../../stac/items/landuse_1900_2000_composite.json",
      "license": "CC-BY 4.0"
    }
  ],
  "count": 3,
  "license": "CC-BY 4.0",
  "last_updated": "2025-10-11",
  "mcp_stage": "derivatives"
}
```

> 💡 **Tip:** When adding or updating any file in `data/derivatives/landcover/metadata/`, update `entries`, bump `count`, and set `last_updated` (ISO).

---

## 🔁 Validation & CI Hooks

Add/ensure these Make targets:

```make
validate-landcover-summary:
\tjsonschema -i data/derivatives/metadata/metadata/landcover/landcover_metadata_summary.json \
\t  data/derivatives/metadata/metadata/schema/domain_metadata_summary.schema.json

crosscheck-landcover-vs-local:
\tpython scripts/validate_registry_crossrefs.py \
\t  --domain landcover \
\t  --summary data/derivatives/metadata/metadata/landcover/landcover_metadata_summary.json \
\t  --local-root data/derivatives/landcover/metadata

stac-validate-landcover:
\tstac-validator $(shell jq -r '.entries[].stac_item' data/derivatives/metadata/metadata/landcover/landcover_metadata_summary.json)
```

**CI should fail** if any `path`/`stac_item` is missing, `count` ≠ `entries.length`, or schemas aren’t satisfied.

---

## ✅ Best Practices

| Category          | Guideline                                                                 |
| ----------------- | ------------------------------------------------------------------------- |
| **Completeness**  | Include *all* files from `landcover/metadata/`.                           |
| **Cross-Refs**    | Paths must be relative & resolvable; every entry includes a `stac_item`.  |
| **Licensing**     | Prefer explicit per-entry license; default `CC-BY-4.0` when applicable.   |
| **Versioning**    | Update `last_updated` & increment `count` on every change.                |
| **Consistency**   | Keep IDs aligned across filenames, STAC items, and metadata.              |
| **CI Discipline** | Run validation locally before pushing; ensure checksums exist for assets. |

---

## 🔗 Relationships

| Layer                        | Path                                            | Purpose                                              |
| ---------------------------- | ----------------------------------------------- | ---------------------------------------------------- |
| 🌾 **Landcover Metadata**    | `data/derivatives/landcover/metadata/`          | Individual metadata files for landcover derivatives. |
| 🧾 **Domain Summary (this)** | `data/derivatives/metadata/metadata/landcover/` | Aggregated, validated landcover manifest.            |
| 🧮 **Global Registry**       | `data/derivatives/metadata/metadata/`           | Cross-domain index of summaries.                     |
| 🗺️ **STAC Catalog**         | `data/stac/`                                    | Global spatial-temporal asset index.                 |
| 🧠 **Knowledge Graph**       | (Neo4j)                                         | Semantic mapping of datasets and provenance.         |

---

## 🗓 Changelog

| Version    | Date       | Notes                                                                                                         |
| :--------- | :--------- | :------------------------------------------------------------------------------------------------------------ |
| **v1.1.0** | 2025-10-11 | Added frontmatter/versioning, schema excerpt, Make targets, CI guidance; tightened Mermaid and relationships. |
| **v0.1.0** | 2025-10-10 | Initial creation of landcover domain metadata summary.                                                        |

```
```
