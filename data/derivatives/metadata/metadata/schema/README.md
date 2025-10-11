<div align="center">

# 🧩 Kansas Frontier Matrix — Derivative Metadata Registry Schema  
`data/derivatives/metadata/metadata/schema/`

**Purpose:** Define and validate **JSON Schema specifications** for all domain-level and global derivative metadata summaries  
within the Kansas Frontier Matrix (KFM) system — ensuring semantic consistency, reproducibility, and interoperability.

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
- [Schema Integration Flow](#schema-integration-flow)
- [Directory Layout](#directory-layout)
- [Domain Summary Schema (authoritative)](#domain-summary-schema-authoritative)
- [Global Registry Schema (authoritative)](#global-registry-schema-authoritative)
- [Validation Workflow](#validation-workflow)
- [Makefile & CI Hooks](#makefile--ci-hooks)
- [Best Practices](#best-practices)
- [Changelog](#changelog)

---

## 📖 Overview

This folder contains **JSON Schema definitions** governing the structure and validation rules for all **derivative metadata summaries** under  
`data/derivatives/metadata/metadata/`.

Schemas cover:

- 🌦️ **Climate** (`climate/climate_metadata_summary.json`)  
- ⚠️ **Hazards** (`hazards/hazards_metadata_summary.json`)  
- 💧 **Hydrology** (`hydrology/hydrology_metadata_summary.json`)  
- 🌾 **Landcover** (`landcover/landcover_metadata_summary.json`)  
- 🏔️ **Terrain** (`terrain/terrain_metadata_summary.json`)  
- 🧪 **Soils** (`soils/soils_metadata_summary.json`)  
- 🪨 **Geology** (`geology/geology_metadata_summary.json`)  
- 🧭 **Global** registry (`global_derivative_registry.json`)

These schemas power **automated validation** in CI, guaranteeing consistent keys, resolvable cross-links to **STAC**, and MCP-grade provenance.

---

## 🧭 Schema Integration Flow

```mermaid
flowchart TD
  A["Domain Summaries\n(climate · hazards · hydrology · landcover · terrain · soils · geology)"] --> B["Schemas\n(data/derivatives/metadata/metadata/schema/)"]
  B --> C["JSON Schema Validation\n(pre-commit · make validate · CI)"]
  C --> D["STAC Catalog\nCollections · Items"]
  D --> E["Knowledge Graph\nCIDOC CRM · OWL-Time"]
````

<!-- END OF MERMAID -->

---

## 🗂️ Directory Layout

```bash
data/
└── derivatives/
    └── metadata/
        └── metadata/
            └── schema/
                ├── domain_metadata_summary.schema.json
                ├── global_derivative_registry.schema.json
                └── README.md
```

> Each schema defines **required structure, types, and constraints**; CI invokes them before any metadata changes are merged.

---

## 🧾 Domain Summary Schema (authoritative)

> Save as: `data/derivatives/metadata/metadata/schema/domain_metadata_summary.schema.json`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://kfm.data/schema/domain_metadata_summary.schema.json",
  "title": "KFM Domain Metadata Summary Schema",
  "description": "Validates domain-level derivative metadata summary files.",
  "type": "object",
  "required": ["id","title","domain","entries","count","last_updated","mcp_stage"],
  "properties": {
    "id": { "type": "string" },
    "title": { "type": "string" },
    "description": { "type": "string" },
    "domain": {
      "type": "string",
      "enum": ["climate","hazards","hydrology","landcover","terrain","soils","geology"]
    },
    "entries": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["id","title","path","format","source","stac_item"],
        "properties": {
          "id": { "type": "string" },
          "title": { "type": "string" },
          "path": { "type": "string" },
          "temporal_range": { "type": "string" },
          "variables": { "type": "array", "items": { "type": "string" } },
          "format": { "type": "string" },
          "source": { "type": "string" },
          "stac_item": { "type": "string" },
          "license": { "type": "string" }
        },
        "additionalProperties": false
      }
    },
    "count": { "type": "integer", "minimum": 0 },
    "license": { "type": "string" },
    "last_updated": { "type": "string", "format": "date" },
    "mcp_stage": { "type": "string", "enum": ["derivatives"] }
  },
  "additionalProperties": false
}
```

---

## 🧾 Global Registry Schema (authoritative)

> Save as: `data/derivatives/metadata/metadata/schema/global_derivative_registry.schema.json`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://kfm.data/schema/global_derivative_registry.schema.json",
  "title": "KFM Global Derivative Registry Schema",
  "description": "Validates consolidated registry indexing all derivative-domain summaries.",
  "type": "object",
  "required": ["version","generated_at","domains"],
  "properties": {
    "version": { "type": "string" },
    "generated_at": { "type": "string", "format": "date-time" },
    "domains": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["domain","summary_path","count"],
        "properties": {
          "domain": {
            "type": "string",
            "enum": ["climate","hazards","hydrology","landcover","terrain","soils","geology"]
          },
          "summary_path": { "type": "string" },
          "count": { "type": "integer", "minimum": 0 }
        },
        "additionalProperties": false
      }
    }
  },
  "additionalProperties": false
}
```

---

## 🔍 Validation Workflow

| Stage          | Tool                                     | Description                                                                              |
| -------------- | ---------------------------------------- | ---------------------------------------------------------------------------------------- |
| **Local**      | `make validate`                          | Runs JSON Schema checks against all domain summaries + global registry.                  |
| **CI**         | `.github/workflows/stac-validate.yml`    | Executes JSON Schema and STAC validation; fails on missing/invalid references.           |
| **Cross-Refs** | `scripts/validate_registry_crossrefs.py` | Confirms every `entries[].path` & `stac_item` resolves to a real file.                   |
| **Graph Sync** | Neo4j Loader                             | Imports validated summaries as **domain registry** entities and links to STAC & sources. |

---

## 🧰 Makefile & CI Hooks

Add (or ensure) these targets:

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

validate: validate-domain-summaries validate-global-registry validate-derivative-crossrefs
```

**CI recommendations**

* Run `make validate` in `stac-validate.yml`.
* Fail build when:

  * `count` ≠ number of `entries`
  * any `path`/`stac_item` is missing or non-resolving
  * domain not in the allowed set (enum)

---

## ✅ Best Practices

* **Strict completeness:** Every derivative domain present in the repo must have a summary file and be listed in the global registry.
* **Stable relative paths:** Use paths resolvable from the summary file location; avoid absolute links.
* **Version hygiene:** Update `last_updated`, `count`, and the **global registry** on any domain change.
* **Semantics-ready:** Optionally include `license` per entry and maintain consistent IDs for clean **Knowledge Graph** mapping.
* **Pin STAC:** Ensure `stac_item` paths point to **versioned/pinned** STAC items (commit SHA where feasible).

---

## 🗓 Changelog

| Version    | Date       | Notes                                                                                                                                         |
| :--------- | :--------- | :-------------------------------------------------------------------------------------------------------------------------------------------- |
| **v1.2.0** | 2025-10-11 | Added terrain/soils/geology domains to enums; introduced global registry schema; added Makefile roll-up target; clarified CI fail conditions. |
| **v1.1.0** | 2025-10-10 | Hardened field requirements (`entries[].stac_item` mandatory), added `mcp_stage` enum.                                                        |
| **v1.0.0** | 2025-10-10 | Initial schema definitions & README for domain summaries.                                                                                     |

```
```
