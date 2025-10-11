<div align="center">

# 💧 Kansas Frontier Matrix — Hydrology Derivative Metadata Summary  
`data/derivatives/metadata/metadata/hydrology/`

**Purpose:** Aggregate and summarize all **hydrology derivative metadata** files under  
`data/derivatives/hydrology/metadata/`, creating a domain-level index for provenance tracking,  
validation, and integration within KFM’s global metadata registry and STAC catalog.

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

This directory defines the **hydrology domain summary registry**, consolidating all derivative metadata JSON files  
from `data/derivatives/hydrology/metadata/`.  

It provides a domain-level summary for hydrological datasets such as:
- 🌊 **Streamflow & discharge composites**  
- 💧 **Aquifer depth & groundwater models**  
- ⚠️ **Floodplain and watershed boundaries**  
- 🛰️ **Hydrographic flow accumulation & direction grids**  

This registry ensures that every hydrological derivative in KFM is discoverable, validated, and cross-linked to its STAC and source metadata.

---

## 🧭 Metadata Summary Flow

```mermaid
flowchart TD
  A["Hydrology Metadata JSONs\n(data/derivatives/hydrology/metadata/)"] --> B["Hydrology Summary JSON\n(this dir)"]
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
            └── hydrology/
                ├── hydrology_metadata_summary.json
                └── README.md
```

> Each summary JSON consolidates all hydrology derivatives and links them to metadata, checksum, and STAC files for reproducibility.

---

## 🧾 Summary JSON Schema

> Validate `hydrology_metadata_summary.json` using:
> `data/derivatives/metadata/metadata/schema/domain_metadata_summary.schema.json`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "KFM Hydrology Domain Metadata Summary",
  "type": "object",
  "required": ["id","title","domain","count","entries","last_updated","mcp_stage"],
  "properties": {
    "id": {"type":"string","const":"hydrology_metadata_summary"},
    "title": {"type":"string"},
    "description": {"type":"string"},
    "domain": {"type":"string","const":"hydrology"},
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
  "id": "hydrology_metadata_summary",
  "title": "Hydrology Derivative Metadata Summary",
  "description": "Aggregated metadata summary for hydrology derivative datasets across Kansas Frontier Matrix.",
  "domain": "hydrology",
  "entries": [
    {
      "id": "streamflow_monthly_1990_2025",
      "title": "Monthly Streamflow Composite (1990–2025, USGS NWIS)",
      "path": "../../../../hydrology/metadata/streamflow_monthly_1990_2025.json",
      "temporal_range": "1990–2025",
      "variables": ["streamflow"],
      "format": "COG",
      "source": "../../../../sources/usgs_nwis_streamflow.json",
      "stac_item": "../../../../stac/items/streamflow_monthly_1990_2025.json",
      "license": "Public Domain (USGS)"
    },
    {
      "id": "floodplain_extent_2020",
      "title": "Floodplain Extent Map (2020, FEMA NFHL)",
      "path": "../../../../hydrology/metadata/floodplain_extent_2020.json",
      "temporal_range": "2020",
      "variables": ["flood_extent"],
      "format": "COG",
      "source": "../../../../sources/fema_flood_zones.json",
      "stac_item": "../../../../stac/items/floodplain_extent_2020.json",
      "license": "CC-BY 4.0"
    },
    {
      "id": "aquifer_depth_ks",
      "title": "Aquifer Depth Grid (Kansas, USGS Water Data)",
      "path": "../../../../hydrology/metadata/aquifer_depth_ks.json",
      "temporal_range": "Static",
      "variables": ["depth_to_water_table"],
      "format": "COG",
      "source": "../../../../sources/usgs_aquifers.json",
      "stac_item": "../../../../stac/items/aquifer_depth_ks.json",
      "license": "CC-BY 4.0"
    }
  ],
  "count": 3,
  "license": "CC-BY 4.0",
  "last_updated": "2025-10-11",
  "mcp_stage": "derivatives"
}
```

> 💡 **Tip:** After adding or modifying hydrology datasets, update `entries`, `count`, and `last_updated`.

---

## 🔁 Validation & CI Hooks

```make
validate-hydrology-summary:
\tjsonschema -i data/derivatives/metadata/metadata/hydrology/hydrology_metadata_summary.json \
\t  data/derivatives/metadata/metadata/schema/domain_metadata_summary.schema.json

crosscheck-hydrology-vs-local:
\tpython scripts/validate_registry_crossrefs.py \
\t  --domain hydrology \
\t  --summary data/derivatives/metadata/metadata/hydrology/hydrology_metadata_summary.json \
\t  --local-root data/derivatives/hydrology/metadata

stac-validate-hydrology:
\tstac-validator $(shell jq -r '.entries[].stac_item' data/derivatives/metadata/metadata/hydrology/hydrology_metadata_summary.json)
```

> CI should **fail** if any entry path is invalid, missing in STAC, or mismatched with `count`.

---

## ✅ Best Practices

| Category                  | Guideline                                                              |
| ------------------------- | ---------------------------------------------------------------------- |
| **Completeness**          | Include *all* metadata files from `hydrology/metadata/`.               |
| **Cross-Refs**            | Ensure valid relative paths to metadata, sources, and STAC items.      |
| **Licensing**             | Explicitly include per-entry license; default to `CC-BY-4.0`.          |
| **Versioning**            | Update `last_updated` and increment `count` whenever datasets change.  |
| **Naming Consistency**    | Follow the `hydro_<type>_<region>_<year>` pattern for dataset IDs.     |
| **Validation Discipline** | Run schema + STAC validation locally (`make validate`) before pushing. |

---

## 🔗 Relationships

| Layer                        | Path                                            | Purpose                                                  |
| ---------------------------- | ----------------------------------------------- | -------------------------------------------------------- |
| 💧 **Hydrology Metadata**    | `data/derivatives/hydrology/metadata/`          | Individual dataset metadata files.                       |
| 🧾 **Domain Summary (this)** | `data/derivatives/metadata/metadata/hydrology/` | Aggregated hydrology domain manifest.                    |
| 🧮 **Global Registry**       | `data/derivatives/metadata/metadata/`           | Central index linking all domain summaries.              |
| 🗺️ **STAC Catalog**         | `data/stac/`                                    | Global spatial-temporal catalog for derivative datasets. |
| 🧠 **Knowledge Graph**       | (Neo4j)                                         | Semantic mapping of hydrology datasets and provenance.   |

---

## 🗓 Changelog

| Version    | Date       | Notes                                                                                                 |
| :--------- | :--------- | :---------------------------------------------------------------------------------------------------- |
| **v1.1.0** | 2025-10-11 | Added version metadata, validation schema excerpt, Make targets, and improved CI crosscheck guidance. |
| **v0.1.0** | 2025-10-10 | Initial creation of hydrology domain metadata summary for registry.                                   |

```
```
