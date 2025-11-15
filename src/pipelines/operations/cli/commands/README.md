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
Document the command modules powering the Operations CLI, including ETL execution, retry-safe recovery, trustworthy rollback, STAC creation and publishing, graph synchronization, telemetry ingestion, and validation workflows — all managed under MCP-DL v6.3 and Diamond⁹ Ω / Crown∞Ω certification.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue.svg)]()
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange.svg)]()
[![Status: Stable](https://img.shields.io/badge/Status-Stable-success.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)]()

</div>

---

## 📘 Overview
This directory holds the **command-level modules** for the KFM Operations CLI. Each Python module corresponds to a top-level `kfm` subcommand and adheres to:

- Deterministic execution  
- Idempotent behavior  
- Checkpoint and rollback safety  
- FAIR+CARE metadata ethics  
- MCP-DL documentation-first design  

These commands remain thin orchestration layers that delegate I/O and state management to `utils/` modules.

---

## 📁 Directory Layout

```
src/pipelines/operations/cli/commands/
│
├── etl_run.py              # Execute ETL pipelines (single or all)
├── etl_retry.py            # Checkpoint-based resume engine
├── rollback.py             # Trustworthy rollback + snapshot orchestration
├── stac_build.py           # Build STAC Items and Collections
├── stac_publish.py         # Publish STAC Catalogs
├── graph_sync.py           # Apply Neo4j schema + index updates
├── telemetry_ingest.py     # Ingest and validate Focus Mode telemetry
└── validate.py             # Validation suite for all operations
```

---

## 🧱 Architecture Diagram

```mermaid
flowchart TB
    subgraph Commands
        C1[etl_run]
        C2[etl_retry]
        C3[rollback]
        C4[stac_build]
        C5[stac_publish]
        C6[graph_sync]
        C7[telemetry_ingest]
        C8[validate]
    end
    subgraph Utils
        U1[config]
        U2[io]
        U3[locks]
        U4[sandbox]
        U5[checkpoint]
    end
    C1 --> U1
    C1 --> U2
    C1 --> U4
    C2 --> U1
    C2 --> U2
    C2 --> U5
    C3 --> U1
    C3 --> U2
    C3 --> U3
    C4 --> U1
    C4 --> U2
    C5 --> U1
    C5 --> U2
    C6 --> U1
    C6 --> U2
    C7 --> U1
    C7 --> U2
    C8 --> U1
    C8 --> U2
    C8 --> U4
```

---

## 🔧 Command Module Descriptions

### 🗂️ `etl_run.py`
Executes full or source-specific ETL pipelines with dry-run and CI-safe flags.

### 🔁 `etl_retry.py`
Resumes failed ETL pipelines with checkpoint validation and lock protection.

### 🧵 `rollback.py`
Implements snapshot creation, verification, and system rollback aligned with the v10.3 Trustworthy Rollback Playbook.

### 🗺️ `stac_build.py`
Builds STAC 1.0.0-compliant Items and Collections with checksum + provenance metadata.

### 🌐 `stac_publish.py`
Publishes STAC catalogs to local or remote endpoints with pre-publish validation.

### 🧬 `graph_sync.py`
Applies Neo4j constraints, indexes, and triggers optional full graph rebuild.

### 📡 `telemetry_ingest.py`
Processes Focus Mode v2 telemetry with CARE filters and telemetry schema validation.

### 🧪 `validate.py`
Runs ETL, STAC, graph, and provenance validation chains for CI and governance.

---

## 🧾 Governance & Compliance
This directory is governed by:

- ROOT-GOVERNANCE.md  
- FAIR+CARE Council  
- MCP-DL v6.3  
- CI workflows (`docs-lint.yml`, `graph-integrity.yml`, `rollback-tests.yml`, `faircare-validate.yml`, `stac-validate.yml`)  

All changes require updating version metadata, passing CI, and documenting in the Version History.

---

## 📚 Version History

| Version | Date | Notes |
|--------|--------|--------|
| v10.3.0 | 2025-11-14 | File rebuilt with full Markdown Output Protocol compliance |
| v10.2.0 | — | Added telemetry + rollback command modules |
| v10.1.0 | — | Initial command suite established |

---
