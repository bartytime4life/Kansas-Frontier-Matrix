<div align="center">

# 🏔️ Kansas Frontier Matrix — Terrain Derivative Metadata Summary  
`data/derivatives/metadata/metadata/terrain/`

**Purpose:** Provide an aggregated **terrain domain registry** summarizing all topographic, elevation, and geomorphologic  
derivative metadata files within KFM — unifying hillshades, slope maps, DEMs, and contour layers into a single validated summary.

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

This directory defines the **terrain domain summary registry** for all metadata describing KFM’s topographic and elevation derivatives.  
It consolidates metadata from `data/derivatives/terrain/metadata/` and records **provenance links**, **STAC references**, and **ETL lineage** for:

- 🗺️ Digital Elevation Models (DEMs; LiDAR/3DEP)  
- 🌄 Hillshade & slope rasters  
- 🧭 Contour line vectors  
- 🪨 Terrain classification / geomorphology models  

The summary enables **STAC cross-validation**, **CI checks**, and **Knowledge Graph** indexing for all terrain datasets.

---

## 🧭 Metadata Summary Flow

```mermaid
flowchart TD
  A["Terrain Metadata JSONs\n(data/derivatives/terrain/metadata/)"] --> B["Terrain Summary JSON\n(this dir)"]
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
            └── terrain/
                ├── terrain_metadata_summary.json
                └── README.md
```

> This summary JSON is the **authoritative domain-level manifest** for processed terrain derivatives, linking each dataset to its metadata file and STAC item.

---

## 🧾 Summary JSON Schema

> Validate `terrain_metadata_summary.json` against the (shared) domain summary schema:
> `data/derivatives/metadata/metadata/schema/domain_metadata_summary.schema.json`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "KFM Terrain Domain Metadata Summary",
  "type": "object",
  "required": ["id","title","domain","count","entries","last_updated","mcp_stage"],
  "properties": {
    "id": {"type":"string", "const":"terrain_metadata_summary"},
    "title": {"type":"string"},
    "description": {"type":"string"},
    "domain": {"type":"string", "const":"terrain"},
    "count": {"type":"integer","minimum":0},
    "entries": {
      "type":"array",
      "items":{
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
  "additionalProperties": false}
```

---

## 🧪 Example Summary File

```json
{
  "id": "terrain_metadata_summary",
  "title": "Terrain Derivative Metadata Summary",
  "description": "Aggregated metadata summary for terrain and topographic derivatives across Kansas Frontier Matrix.",
  "domain": "terrain",
  "entries": [
    {
      "id": "dem_1m_ks_lidar",
      "title": "Kansas 1 m LiDAR Digital Elevation Model (USGS 3DEP)",
      "path": "../../../../terrain/metadata/dem_1m_ks_lidar.json",
      "temporal_range": "2018–2023",
      "variables": ["elevation"],
      "format": "COG",
      "source": "../../../../sources/usgs_3dep_dem.json",
      "stac_item": "../../../../stac/items/dem_1m_ks_lidar.json",
      "license": "Public Domain (USGS)"
    },
    {
      "id": "hillshade_ks_1m",
      "title": "Hillshade Raster (Kansas 1 m DEM-derived)",
      "path": "../../../../terrain/metadata/hillshade_ks_1m.json",
      "temporal_range": "Derived from DEM (2018–2023)",
      "variables": ["illumination"],
      "format": "COG",
      "source": "../../../../sources/usgs_3dep_dem.json",
      "stac_item": "../../../../stac/items/hillshade_ks_1m.json",
      "license": "CC-BY 4.0"
    },
    {
      "id": "slope_map_ks",
      "title": "Slope Map of Kansas (degrees)",
      "path": "../../../../terrain/metadata/slope_map_ks.json",
      "temporal_range": "Derived from DEM (2018–2023)",
      "variables": ["slope"],
      "format": "COG",
      "source": "../../../../sources/usgs_3dep_dem.json",
      "stac_item": "../../../../stac/items/slope_map_ks.json",
      "license": "CC-BY 4.0"
    }
  ],
  "count": 3,
  "license": "CC-BY 4.0",
  "last_updated": "2025-10-11",
  "mcp_stage": "derivatives"
}
```

> 💡 **Tip:** When adding new files in `data/derivatives/terrain/metadata/`, update `entries`, bump `count`, and set `last_updated` (ISO).

---

## 🔁 Validation & CI Hooks

Add/ensure these targets exist:

```make
validate-terrain-summary:
\tjsonschema -i data/derivatives/metadata/metadata/terrain/terrain_metadata_summary.json \
\t  data/derivatives/metadata/metadata/schema/domain_metadata_summary.schema.json

crosscheck-terrain-vs-local:
\tpython scripts/validate_registry_crossrefs.py \
\t  --domain terrain \
\t  --summary data/derivatives/metadata/metadata/terrain/terrain_metadata_summary.json \
\t  --local-root data/derivatives/terrain/metadata

stac-validate-terrain:
\tstac-validator $(shell jq -r '.entries[].stac_item' data/derivatives/metadata/metadata/terrain/terrain_metadata_summary.json)
```

> CI should **fail** if any `path` or `stac_item` is missing/invalid, or if `count` doesn’t match `entries.length`.

---

## ✅ Best Practices

| Category          | Guideline                                                                |
| ----------------- | ------------------------------------------------------------------------ |
| **Completeness**  | Include *all* files from `terrain/metadata/`.                            |
| **Cross-Refs**    | Paths should be relative & resolvable; always include a `stac_item`.     |
| **Licensing**     | Prefer explicit license per entry; default repository license if absent. |
| **Versioning**    | Update `last_updated` & increment `count` on every change.               |
| **Consistency**   | Keep `id`/filenames aligned: `terrain_<product>_<res>_<region>`.         |
| **CI Discipline** | Run validation targets locally before pushing.                           |

---

## 🔗 Relationships

| Layer                        | Path                                          | Purpose                                                    |
| ---------------------------- | --------------------------------------------- | ---------------------------------------------------------- |
| 🏔️ **Terrain Metadata**     | `data/derivatives/terrain/metadata/`          | Individual terrain metadata files (DEM, slope, hillshade). |
| 🧾 **Domain Summary (this)** | `data/derivatives/metadata/metadata/terrain/` | Aggregated, validated terrain manifest.                    |
| 🧮 **Global Registry**       | `data/derivatives/metadata/metadata/`         | Cross-domain index of summaries.                           |
| 🗺️ **STAC Catalog**         | `data/stac/`                                  | Global spatial-temporal asset index.                       |
| 🧠 **Knowledge Graph**       | (Neo4j)                                       | Semantic mapping of datasets and provenance.               |

---

## 🗓 Changelog

| Version    | Date       | Notes                                                                                                                        |
| :--------- | :--------- | :--------------------------------------------------------------------------------------------------------------------------- |
| **v1.1.0** | 2025-10-11 | Added frontmatter/versioning, domain schema excerpt, Makefile targets, and CI guidance; tightened Mermaid and relationships. |
| **v0.1.0** | 2025-10-10 | Initial creation of terrain domain metadata summary.                                                                         |

```
```
