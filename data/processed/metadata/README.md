<div align="center">

# 🧾 Kansas-Frontier-Matrix — Processed Metadata  
`data/processed/metadata/`

**Mission:** Maintain **metadata records** describing all processed datasets — their lineage,  
license, temporal coverage, and schema — ensuring traceability and reproducibility throughout  
the Kansas Frontier Matrix data lifecycle.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../.github/workflows/codeql.yml)
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../.github/workflows/trivy.yml)
[![Pre-Commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](../../../.github/workflows/pre-commit.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../LICENSE)
[![License: Code](https://img.shields.io/badge/License-MIT-yellow)](../../../LICENSE)

</div>

---

## 📚 Table of Contents
- [Overview](#overview)
- [Purpose & Scope](#purpose--scope)
- [System Flow (Mermaid)](#system-flow-mermaid)
- [Directory Layout](#directory-layout)
- [Metadata Standards](#metadata-standards)
- [STAC & MCP Integration](#stac--mcp-integration)
- [Validation & Provenance](#validation--provenance)
- [Adding or Updating Metadata](#adding-or-updating-metadata)
- [QA Checklist (copy into PRs)](#qa-checklist-copy-into-prs)
- [References](#references)
- [Version History](#version-history)

---

## 🧠 Overview

This directory contains the **metadata registry for all processed datasets** under `data/processed/`.  
It is the canonical record for **provenance, schema, licensing, coverage, and build context** for KFM’s intermediate and harmonized products.

Each JSON file documents:
- Source lineage (`derived_from`) and processing parameters  
- Spatial/temporal coverage and data quality notes  
- Licensing, versioning, and authorship  
- STAC-compliant fields and MCP provenance hooks

---

## 🎯 Purpose & Scope

1) **Traceability** — authoritative lineage for each processed artifact.  
2) **Validation** — CI/CD checks ensure schema, STAC, and checksum compliance.  
3) **Integration** — fuels the STAC catalog and UI/graph layers with rich metadata.

---

## 🧭 System Flow (Mermaid)

```mermaid
flowchart TD
  A["Processed Artifacts\n(data/processed/*)"] --> B["Metadata Authoring\n(data/processed/metadata/*/*.json)"]
  B --> C["Schema Validation\n(schema/*.json · MCP rules)"]
  C --> D["STAC Sync\n(data/stac/items/*)"]
  D --> E["Catalog & UI/Graph\n(web/* · src/graph/*)"]
  %% END OF MERMAID
````

---

## 🧱 Directory Layout

```bash
data/
└── processed/
    └── metadata/
        ├── schema/
        │   ├── processed_item.schema.json        # JSON schema for processed metadata
        │   ├── stac_item.schema.json             # STAC compliance reference
        │   └── validation_rules.json             # MCP policy & field rules
        ├── terrain/
        │   ├── dem_1m_ks_filled.json
        │   ├── dem_30m_ned_ks.json
        ├── hydrology/
        │   ├── flow_dir_d8_1m_ks.json
        │   ├── watermask_ks.json
        ├── landcover/
        │   ├── nlcd_2021_ks.json
        │   ├── vegetation_mask_ks.json
        ├── climate/
        │   ├── precip_total_annual_1895_2024.json
        │   ├── drought_spi12_1895_2024.json
        ├── hazards/
        │   ├── tornado_tracks_1950_2024.json
        │   ├── fema_disasters_1953_2024.json
        ├── tabular/
        │   ├── tornado_counts_1950_2024.json
        │   ├── county_population_1850_2020.json
        ├── text/
        │   ├── newspapers_1854_1925_cleaned.json
        │   ├── ocr_cleaned_diaries_1850_1900.json
        ├── template.json                         # Starter template for new datasets
        └── README.md
```

---

## 🧩 Metadata Standards

KFM uses a **hybrid MCP + STAC** approach: strict machine-readability with explicit scientific provenance.

### Required Fields (per item)

| Field                            | Description                          | Example                                       |
| -------------------------------- | ------------------------------------ | --------------------------------------------- |
| `id`                             | Unique dataset identifier            | `"dem_1m_ks_filled"`                          |
| `type`                           | STAC type                            | `"Feature"`                                   |
| `stac_version`                   | STAC version                         | `"1.0.0"`                                     |
| `properties.title`               | Human-friendly title                 | `"Filled DEM (1 m) – Kansas"`                 |
| `properties.description`         | Summary                              | `"Hydrologically conditioned DEM from LiDAR"` |
| `properties.datetime`            | Reference/processing date (ISO 8601) | `"2020-01-01T00:00:00Z"`                      |
| `properties.processing:software` | Tools/versions used                  | `"GDAL 3.8.0; WhiteboxTools 2.2.0"`           |
| `properties.kfm:mcp_provenance`  | SHA-256 or version hash              | `"sha256:cf1e98..."`                          |
| `assets`                         | At least one `data` asset            | path + media type                             |
| `license`                        | License string                       | `"CC-BY 4.0"`                                 |

### Common Extensions (optional but recommended)

* `bbox`, `geometry` (geospatial)
* `temporal_extent.start` / `temporal_extent.end`
* `quality:metrics.*` (accuracy, completeness, coverage)
* `derived_from[]` (raw or upstream products)
* `links[]` to collection, self, parent

---

## 🌐 STAC & MCP Integration

* **STAC Catalog:** Items auto-synchronized into `data/stac/` for discovery.
* **MCP Provenance Chain:** `kfm:mcp_provenance` provides cryptographic linkage to checksums and build logs.
* **CI Validation:** `.github/workflows/stac-validate.yml` enforces schema + STAC + rule compliance.

---

## 🔎 Validation & Provenance

Automated checks include:

* **JSON Schema validation** against `schema/processed_item.schema.json` & `schema/stac_item.schema.json`
* **Checksum verification** (hash exists & matches in sibling `data/processed/*/checksums/`)
* **STAC completeness** (`id`, `type`, `stac_version`, `properties`, `assets`)
* **Temporal/geometric consistency** where applicable

Run locally:

```bash
make validate-metadata
```

Outputs a `validation_report.json` with pass/fail details.

---

## ➕ Adding or Updating Metadata

1. **Copy** `template.json` into the correct domain folder.
2. **Fill** required fields (`id`, `properties.*`, `assets.data`, `license`).
3. **Compute** SHA-256 for primary asset and place in sibling `checksums/`; record in `kfm:mcp_provenance`.
4. **Validate** with:

   ```bash
   make validate-metadata
   ```
5. **PR** with:

   * new/updated metadata JSON
   * checksum file(s)
   * brief processing notes (software, parameters, changes)

---

## ☑️ QA Checklist (copy into PRs)

* [ ] STAC item validates (CI green)
* [ ] Required fields populated & accurate
* [ ] `kfm:mcp_provenance` hash present and matches checksum file
* [ ] `derived_from[]` references resolve to sources or upstream products
* [ ] Temporal/geometry fields correct (if spatial/temporal)
* [ ] Links (`self`, `parent`, `collection`) are relative & valid

---

## 📖 References

* **STAC 1.0** — `stacspec.org`
* **ISO 19115** — dataset metadata standard
* **Schema.org/Dataset** — semantic discovery
* **JSON Schema** — `json-schema.org`
* **Master Coder Protocol (MCP)** — `docs/standards/`
* **KFM STAC Catalog** — `data/stac/`

---

## 🧾 Version History

|  Version  | Date       | Summary                                                                                 |
| :-------: | :--------- | :-------------------------------------------------------------------------------------- |
| **1.2.0** | 2025-10-11 | Added Mermaid flow, QA checklist, expanded standards tables; clarified MCP/STAC linkage |
|   1.1.0   | 2025-08-27 | Strengthened schema rules and CI instructions                                           |
|   1.0.0   | 2025-07-14 | Initial metadata registry with STAC/MCP baseline                                        |

---

<div align="center">

*“Metadata is the foundation of reproducibility — every file tells its own origin story in the Kansas Frontier Matrix.”*

</div>
```
