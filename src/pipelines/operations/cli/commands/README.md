---
title: "🧩 Kansas Frontier Matrix — Operations CLI Command Modules (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/operations/cli/commands/README.md"
version: "v10.3.0"
last_updated: "2025-11-14"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/pipelines-operations-cli-commands-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🧩 **Kansas Frontier Matrix — Operations CLI Command Modules**  
`src/pipelines/operations/cli/commands/README.md`

**Purpose:**  
Document the modular command suite powering the Operations CLI, including ETL execution, retry safety, rollback automation, STAC publishing, graph synchronization, telemetry ingestion, and validation workflows for KFM v10.3.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue.svg)]()
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange.svg)]()
[![Status: Stable](https://img.shields.io/badge/Status-Stable-success.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)]()

</div>

---

## 📘 Overview

This directory contains the **modular command implementations** that form the operational backbone of the KFM CLI.  
Each module implements one operational domain (ETL, retry, STAC, rollback, graph sync, telemetry, validation) and conforms to:

- **MCP-DL v6.3**  
- **AI safety + provenance standards**  
- **Diamond⁹Ω / Crown∞Ω operational certification**  
- **Retry-safe, reversible, deterministic execution**  
- **Full CI validation compatibility**

Every command here is imported by `cli.py` and becomes a subcommand inside the global `kfm` interface.

---

## 📁 Directory Layout

```
src/pipelines/operations/cli/commands/
│
├── etl_run.py              # Run ETL pipelines (all or specific)
├── etl_retry.py            # Checkpoint + retry-safe execution
├── rollback.py             # Trustworthy rollback (snapshotting + restore)
├── stac_build.py           # Build STAC Items & Collections
├── stac_publish.py         # Publish STAC to local/remote catalogs
├── graph_sync.py           # Apply schema/index changes, rebuild graph
├── telemetry_ingest.py     # Ingest and validate Focus Mode telemetry
└── validate.py             # Comprehensive validator suite
```

---

## 🔧 Command Modules

### 🗂️ `etl_run.py` — ETL Execution Engine

**Description:**  
Runs full or partial ETL pipelines defined in `data/sources/*.json`.

**Capabilities:**  
- Run all sources or individual datasets  
- CI dry-run support  
- Schema validation on output  
- Deterministic ordering  

**Examples:**

```
kfm etl run --all
kfm etl run --source ks_historic_topo
```

---

### 🔁 `etl_retry.py` — Checkpointed Retry System

**Description:**  
Implements MCP-compliant checkpointing for failed or interrupted ETL runs.

**Capabilities:**  
- Job checkpoint listing  
- Resume broken pipelines  
- Protects partial writes via lockfiles  

**Examples:**

```
kfm etl retry --job 2025-11-14T05:32Z
kfm etl retry --list
```

---

### 🧵 `rollback.py` — Trustworthy Rollback (v10.3)

**Description:**  
Executes rollback and snapshot workflows aligned with the *Trustworthy Rollback & STAC Reversion Playbook*.

**Capabilities:**  
- Create snapshots (GraphDB, STAC, SBOM, manifest)  
- Restore system to a previous state  
- Integrity-checked operations  

**Examples:**

```
kfm ops rollback --snapshot
kfm ops rollback --to snapshot_2025_11_14
```

---

### 🗺️ `stac_build.py` — STAC Item/Collection Builder

**Description:**  
Builds complete STAC catalog for all processed datasets.

**Capabilities:**  
- Creates Items, Collections, assets  
- Enforces STAC 1.0.0 + projections extension  
- Inserts checksum + lineage metadata  

**Examples:**

```
kfm stac build
```

---

### 🌐 `stac_publish.py` — STAC Publisher

**Description:**  
Publishes STAC catalog to static storage or a remote STAC API endpoint.

**Capabilities:**  
- Local static hosting  
- Remote API publishing  
- CI validation before publishing  

**Examples:**

```
kfm stac publish --target local
kfm stac publish --target remote --url https://stac.kfm.dev/
```

---

### 🧬 `graph_sync.py` — Graph Schema + Index Management

**Description:**  
Synchronizes Neo4j schema definitions, indexes, and optionally rebuilds entire graph.

**Capabilities:**  
- Schema application  
- Index rebuild  
- Full graph refresh from ETL results  

**Examples:**

```
kfm graph sync --schema
kfm graph sync --indexes
kfm graph rebuild
```

---

### 📡 `telemetry_ingest.py` — Focus Mode Telemetry Ingestion

**Description:**  
Handles ingest, validation, and registration of telemetry signals generated by Focus Mode v2.

**Capabilities:**  
- Batch ingestion  
- CARE-compliant filtering  
- JSON Schema enforcement  

**Examples:**

```
kfm telemetry ingest ./telemetry/*.json
```

---

### 🧪 `validate.py` — System Validation Suite

**Description:**  
Runs all validation operations before publishing, deployment, or CI approval.

**Capabilities:**  
- STAC conformance  
- Graph integrity  
- Provenance contracts  
- ETL schema checks  

**Examples:**

```
kfm validate all
kfm validate stac
```

---

## 🧾 Governance & Compliance

These modules fall under:

- **ROOT-GOVERNANCE.md**  
- **FAIR+CARE Council oversight**  
- **CI enforcement layers** (`docs-lint`, `stac-validate`, `faircare-validate`, `rollback-tests`)  
- **Master Coder Protocol (MCP-DL v6.3)**  

All commands must remain:

- Deterministic  
- Idempotent  
- Fully logged  
- Reversible  
- Testable  

---

## 📚 Version History

| Version | Date | Notes |
|--------|--------|--------|
| v10.3.0 | 2025-11-14 | Initial fully compliant documentation for command modules |
| v10.2.0 | — | Added rollback & checkpoint features |
| v10.1.0 | — | Introduced command module directory layout |

---

