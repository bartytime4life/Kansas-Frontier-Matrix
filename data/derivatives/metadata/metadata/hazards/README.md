<div align="center">

# ⚠️ Kansas Frontier Matrix — Hazard Derivative Metadata Summary  
`data/derivatives/metadata/metadata/hazards/`

**Purpose:** Provide a domain-level registry of all **hazard derivative metadata** entries  
(tornado tracks, floods, droughts, disaster composites, etc.) under the Kansas Frontier Matrix (KFM)  
for provenance tracking, validation, and STAC cross-linkage.

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

This folder is the **hazard domain summary registry**, aggregating all hazard derivative metadata from  
`data/derivatives/hazards/metadata/`. It lists core datasets (tornado, flood, drought, storm reports, etc.)  
and links them to their **source manifests**, **checksums**, and **STAC items** to guarantee reproducibility.

This summary ensures:
- ✅ Domain-level metadata completeness  
- 🔗 Consistent provenance across **ETL → STAC → Graph** workflows  
- 🧾 Easy validation in CI and graph synchronization  
- 🌍 Unified hazard layer discovery in API and UI  

---

## 🧭 Metadata Summary Flow

```mermaid
flowchart TD
  A["Hazard Metadata JSONs\n(data/derivatives/hazards/metadata/)"] --> B["Hazard Summary JSON\n(this dir)"]
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
            └── hazards/
                ├── hazards_metadata_summary.json
                └── README.md
```

> This directory summarizes all hazard derivative datasets registered within the KFM system.

---

## 🧾 Summary JSON Schema

> Validate `hazards_metadata_summary.json` with:
> `data/derivatives/metadata/metadata/schema/domain_metadata_summary.schema.json`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "KFM Hazards Domain Metadata Summary",
  "type": "object",
  "required": ["id","title","domain","count","entries","last_updated","mcp_stage"],
  "properties": {
    "id": {"type":"string","const":"hazards_metadata_summary"},
    "title": {"type":"string"},
    "description": {"type":"string"},
    "domain": {"type":"string","const":"hazards"},
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
  "id": "hazards_metadata_summary",
  "title": "Hazard Derivative Metadata Summary",
  "description": "Aggregated summary of hazard derivative datasets across Kansas Frontier Matrix.",
  "domain": "hazards",
  "entries": [
    {
      "id": "tornado_tracks_1950_2024",
      "title": "Kansas Tornado Tracks (1950–2024)",
      "path": "../../../../hazards/metadata/tornado_tracks_1950_2024.json",
      "temporal_range": "1950–2024",
      "variables": ["tornado_path","EF_rating"],
      "format": "GeoJSON",
      "source": "../../../../sources/noaa_spc_tornadoes.json",
      "stac_item": "../../../../stac/items/tornado_tracks_1950_2024.json",
      "license": "Public Domain (NOAA SPC)"
    },
    {
      "id": "flood_zones_1990_2025",
      "title": "FEMA Flood Zones (1990–2025)",
      "path": "../../../../hazards/metadata/flood_zones_1990_2025.json",
      "temporal_range": "1990–2025",
      "variables": ["flood_extent"],
      "format": "COG",
      "source": "../../../../sources/fema_flood_zones.json",
      "stac_item": "../../../../stac/items/flood_zones_1990_2025.json",
      "license": "Public Domain (FEMA)"
    },
    {
      "id": "drought_index_annual_ks",
      "title": "Kansas Drought Severity Index (1895–2024)",
      "path": "../../../../hazards/metadata/drought_index_annual_ks.json",
      "temporal_range": "1895–2024",
      "variables": ["drought_index"],
      "format": "Parquet",
      "source": "../../../../sources/noaa_ncei_drought.json",
      "stac_item": "../../../../stac/items/drought_index_annual_ks.json",
      "license": "Public Domain (NOAA NCEI)"
    }
  ],
  "count": 3,
  "license": "CC-BY 4.0",
  "last_updated": "2025-10-11",
  "mcp_stage": "derivatives"
}
```

> 💡 **Tip:** Update this JSON whenever adding/modifying hazard derivatives in `data/derivatives/hazards/metadata/`; keep `count` in sync with `entries.length`.

---

## 🔁 Validation & CI Hooks

```make
validate-hazards-summary:
\tjsonschema -i data/derivatives/metadata/metadata/hazards/hazards_metadata_summary.json \
\t  data/derivatives/metadata/metadata/schema/domain_metadata_summary.schema.json

crosscheck-hazards-vs-local:
\tpython scripts/validate_registry_crossrefs.py \
\t  --domain hazards \
\t  --summary data/derivatives/metadata/metadata/hazards/hazards_metadata_summary.json \
\t  --local-root data/derivatives/hazards/metadata

stac-validate-hazards:
\tstac-validator $(shell jq -r '.entries[].stac_item' data/derivatives/metadata/metadata/hazards/hazards_metadata_summary.json)
```

> CI should **fail** if any entry path is invalid, STAC item is missing/invalid, or `count` ≠ `entries.length`.

---

## ✅ Best Practices

| Category         | Guideline                                                                  |
| ---------------- | -------------------------------------------------------------------------- |
| **Completeness** | Include *all* metadata files from `hazards/metadata/`.                     |
| **Cross-Refs**   | Use relative, resolvable paths; every entry **must** include `stac_item`.  |
| **Licensing**    | Prefer explicit per-entry license; fall back to `CC-BY-4.0` if applicable. |
| **Versioning**   | Update `last_updated` & increment `count` on any change.                   |
| **Consistency**  | Keep IDs aligned across filenames, STAC items, and metadata.               |
| **Integrity**    | Ensure checksums exist for all underlying assets referenced by STAC.       |

---

## 🔗 Relationships

| Layer                        | Path                                          | Purpose                                             |
| ---------------------------- | --------------------------------------------- | --------------------------------------------------- |
| ⚠️ **Hazard Metadata**       | `data/derivatives/hazards/metadata/`          | Individual hazard derivative metadata files.        |
| 🧾 **Domain Summary (this)** | `data/derivatives/metadata/metadata/hazards/` | Aggregated hazards domain manifest.                 |
| 🧮 **Global Registry**       | `data/derivatives/metadata/metadata/`         | Cross-domain index of summaries.                    |
| 🗺️ **STAC Catalog**         | `data/stac/`                                  | Global spatial-temporal catalog for derivatives.    |
| 🧠 **Knowledge Graph**       | (Neo4j)                                       | Semantic mapping of hazard datasets and provenance. |

---

## 🗓 Changelog

| Version    | Date       | Notes                                                                                                           |
| :--------- | :--------- | :-------------------------------------------------------------------------------------------------------------- |
| **v1.1.0** | 2025-10-11 | Added frontmatter/versioning, schema excerpt, Make targets, and CI crosscheck guidance; hardened Mermaid block. |
| **v0.1.0** | 2025-10-10 | Initial hazard metadata summary for domain-level registry.                                                      |

```
```
