<div align="center">

# 🧭 Kansas Frontier Matrix — Derivative Metadata Registry  
`data/derivatives/metadata/metadata/`

**Purpose:** Act as a **central registry** describing all derivative metadata layers across KFM domains  
(climate · hydrology · hazards · landcover · terrain · soils · geology), ensuring consistency, version traceability, and STAC cross-references.

[![Build & Deploy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Build%20%26%20Deploy)](../../../../.github/workflows/site.yml)
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../../.github/workflows/codeql.yml)
[![Trivy](https://img.shields.io/badge/Container-Scan-informational)](../../../../.github/workflows/trivy.yml)
[![Pre-Commit](https://img.shields.io/badge/Pre--Commit-enabled-success)](../../../../.github/workflows/pre-commit.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-green)](../../../../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC-BY%204.0-lightgrey)](../../../../LICENSE)

</div>

---

## 📚 Table of Contents
- [Overview](#overview)
- [Registry Flow & Context](#registry-flow--context)
- [Directory Layout](#directory-layout)
- [Registry JSON Schemas](#registry-json-schemas)
- [Domain Summary Example](#domain-summary-example)
- [Global Registry Example](#global-registry-example)
- [Validation & CI Hooks](#validation--ci-hooks)
- [Best Practices](#best-practices)
- [Related Documentation](#related-documentation)
- [Changelog](#changelog)

---

## 🧠 Overview

This directory defines the **master metadata registry** for all KFM derivative domains.  
While each derivative group (`climate/`, `hydrology/`, `hazards/`, `landcover/`, `terrain/`, `soils/`, `geology/`) maintains a local `metadata/` folder,  
this **registry** aggregates high-level JSON entries summarizing **dataset families**, **lineage**, **cross-domain linkages**, and **STAC references**.

The registry provides:
- 🗂 **Domain-level summaries** (counts, coverage, variables)
- 🔗 **STAC cross-references** (collections/items)
- 🧾 **Consistent versioning & licensing**
- 🧠 **Semantic tags** (CIDOC CRM, OWL-Time) & **PeriodO** alignment
- 🧪 **CI-verifiable** completeness across domains

---

## 🧩 Registry Flow & Context

```mermaid
flowchart TD
  A["Domain Derivatives\n(climate · hydrology · hazards · landcover · terrain · soils · geology)"] --> B["Local Metadata\n(domain/*/metadata/*.json)"]
  B --> C["Derivative Metadata Registry\nAggregate domain summaries"]
  C --> D["STAC Catalog\n(data/stac/collections · items)"]
  D --> E["Knowledge Graph\nCIDOC CRM · OWL-Time · PeriodO"]
  E --> F["API & Web UI\nSearch · Timeline · Layer panels"]
````

<!-- END OF MERMAID -->

---

## 🗂️ Directory Layout

```bash
data/
└── derivatives/
    └── metadata/
        └── metadata/
            ├── climate/
            │   ├── climate_metadata_summary.json
            │   └── README.md
            ├── hydrology/
            │   ├── hydrology_metadata_summary.json
            │   └── README.md
            ├── hazards/
            │   ├── hazards_metadata_summary.json
            │   └── README.md
            ├── landcover/
            │   ├── landcover_metadata_summary.json
            │   └── README.md
            ├── terrain/
            │   ├── terrain_metadata_summary.json
            │   └── README.md
            ├── soils/
            │   ├── soils_metadata_summary.json
            │   └── README.md
            ├── geology/
            │   ├── geology_metadata_summary.json
            │   └── README.md
            ├── schema/
            │   ├── domain_metadata_summary.schema.json
            │   ├── global_derivative_registry.schema.json
            │   └── README.md
            ├── global_derivative_registry.json         # optional: single-file index of all domains
            └── README.md
```

> Each domain summary references **all derivative metadata** for that domain (e.g., `data/derivatives/climate/metadata/*.json`),
> plus links to **STAC** (`data/stac/`) and **sources** (`data/sources/*.json`).

---

## 🧾 Registry JSON Schemas

### `schema/domain_metadata_summary.schema.json` (excerpt)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://kfm.local/schemas/domain_metadata_summary.schema.json",
  "title": "KFM Domain Metadata Summary",
  "type": "object",
  "required": ["id","title","domain","count","entries","last_updated"],
  "properties": {
    "id": {"type":"string"},
    "title": {"type":"string"},
    "description": {"type":"string"},
    "domain": {"type":"string","enum":["climate","hydrology","hazards","landcover","terrain","soils","geology"]},
    "count": {"type":"integer","minimum":0},
    "entries": {
      "type":"array",
      "items":{
        "type":"object",
        "required":["id","path"],
        "properties":{
          "id":{"type":"string"},
          "path":{"type":"string"},
          "temporal_range":{"type":"string"},
          "variables":{"type":"array","items":{"type":"string"}},
          "format":{"type":"string"},
          "stac_item":{"type":"string"},
          "source":{"type":"string"},
          "license":{"type":"string"}
        },
        "additionalProperties": false
      }
    },
    "last_updated": {"type":"string","format":"date"},
    "mcp_stage": {"type":"string","enum":["derivatives"]}
  },
  "additionalProperties": false
}
```

### `schema/global_derivative_registry.schema.json` (excerpt)

```json
{
  "$schema":"https://json-schema.org/draft/2020-12/schema",
  "$id":"https://kfm.local/schemas/global_derivative_registry.schema.json",
  "title":"KFM Global Derivative Registry",
  "type":"object",
  "required":["version","domains","generated_at"],
  "properties":{
    "version":{"type":"string"},
    "generated_at":{"type":"string","format":"date-time"},
    "domains":{
      "type":"array",
      "items":{
        "type":"object",
        "required":["domain","summary_path","count"],
        "properties":{
          "domain":{"type":"string"},
          "summary_path":{"type":"string"},
          "count":{"type":"integer","minimum":0}
        },
        "additionalProperties": false
      }
    }
  },
  "additionalProperties": false
}
```

---

## 📑 Domain Summary Example

```json
{
  "id": "climate_metadata_summary",
  "title": "Climate Derivative Metadata Summary",
  "description": "Registry of all climate derivative metadata entries, aggregating sources, time coverage, and variable definitions.",
  "domain": "climate",
  "count": 4,
  "entries": [
    {
      "id": "daymet_1980_2024_tmin_ks",
      "path": "../../climate/metadata/daymet_1980_2024_tmin_ks.json",
      "temporal_range": "1980–2024",
      "variables": ["tmin","tmax","prcp"],
      "format": "COG",
      "stac_item": "../../../stac/items/daymet_1980_2024_tmin_ks.json",
      "source": "../../../sources/daymet.json",
      "license": "CC-BY 4.0"
    },
    {
      "id": "normals_1991_2020_prcp",
      "path": "../../climate/metadata/normals_1991_2020_prcp.json",
      "temporal_range": "1991–2020",
      "variables": ["prcp"],
      "format": "COG",
      "stac_item": "../../../stac/items/normals_1991_2020_prcp.json",
      "source": "../../../sources/noaa_normals.json",
      "license": "Public Domain"
    }
  ],
  "last_updated": "2025-10-11",
  "mcp_stage": "derivatives"
}
```

---

## 🌐 Global Registry Example (optional)

```json
{
  "version": "v1.1.0",
  "generated_at": "2025-10-11T13:00:00Z",
  "domains": [
    {"domain":"climate","summary_path":"./climate/climate_metadata_summary.json","count":4},
    {"domain":"hydrology","summary_path":"./hydrology/hydrology_metadata_summary.json","count":5},
    {"domain":"hazards","summary_path":"./hazards/hazards_metadata_summary.json","count":6},
    {"domain":"landcover","summary_path":"./landcover/landcover_metadata_summary.json","count":3},
    {"domain":"terrain","summary_path":"./terrain/terrain_metadata_summary.json","count":5},
    {"domain":"soils","summary_path":"./soils/soils_metadata_summary.json","count":2},
    {"domain":"geology","summary_path":"./geology/geology_metadata_summary.json","count":2}
  ]
}
```

---

## 🔁 Validation & CI Hooks

**Local Make targets (add to repo Makefile):**

```make
validate-domain-summaries:
\tjsonschema -i data/derivatives/metadata/metadata/*/*_metadata_summary.json \
\t  data/derivatives/metadata/metadata/schema/domain_metadata_summary.schema.json

validate-global-registry:
\tjsonschema -i data/derivatives/metadata/metadata/global_derivative_registry.json \
\t  data/derivatives/metadata/metadata/schema/global_derivative_registry.schema.json

validate-derivative-crossrefs:
\tpython scripts/validate_registry_crossrefs.py \
\t  --registry data/derivatives/metadata/metadata \
\t  --stac-root data/stac
```

**CI recommendations:**

* Run the three targets above in `.github/workflows/stac-validate.yml`.
* Fail build if:

  * a domain summary is missing, stale `count`, or bad path
  * a listed `stac_item` doesn’t exist or fails STAC validation
  * an entry’s `path` doesn’t resolve to a real metadata JSON

**Pre-commit hooks:**

* `prettier --parser json` on `*_metadata_summary.json`
* JSON Schema validation (domain & global)
* Lint for missing `stac_item`, `source`, or `license`

---

## ✅ Best Practices

| Category              | Guideline                                                                    |
| --------------------- | ---------------------------------------------------------------------------- |
| **Completeness**      | Every derivative domain present in KFM must have a summary file.             |
| **Cross-Referencing** | Each entry should link both **local metadata** and **STAC item**.            |
| **Licensing**         | Use consistent license strings; default **CC-BY 4.0** when applicable.       |
| **Versioning**        | Update `last_updated` and increment domain `count` with any change.          |
| **Semantics**         | Add `cidoc:EntityType`, `time:Interval` tags (optional) for graph alignment. |
| **PeriodO**           | When historical ranges apply, include PeriodO `period_id` or label.          |
| **Provenance**        | Encourage `commit` field in local metadata for git SHA pinning.              |

---

## 🔗 Related Documentation

* `data/derivatives/metadata/README.md` — per-dataset metadata & schemas
* `data/stac/` — STAC catalog (collections & items)
* `docs/architecture.md` — data lineage & provenance design
* `docs/standards/markdown_protocol.md` — documentation/versioning rules

---

## 🗓️ Changelog

| Version    | Date       | Notes                                                                                               |
| :--------- | :--------- | :-------------------------------------------------------------------------------------------------- |
| **v1.1.0** | 2025-10-11 | Added schemas, global registry example, CI hooks, semantics (CIDOC/OWL-Time), and PeriodO guidance. |
| **v1.0.0** | 2025-10-10 | Initial creation of the Derivative Metadata Registry with domain summaries.                         |

```
```
