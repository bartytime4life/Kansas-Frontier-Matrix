---
title: "🧰 Kansas Frontier Matrix — Operations CLI Toolkit (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/operations/cli/README.md"
version: "v10.3.0"
last_updated: "2025-11-14"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/pipelines-operations-cli-v1.json"
governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🧰 **Kansas Frontier Matrix — Operations CLI Toolkit**  
`src/pipelines/operations/cli/README.md`

**Purpose:**  
Define the unified operational command-line interface for ETL execution, retry-safe workflows, rollback automation, STAC publishing, Focus Mode telemetry ingestion, and governance-compliant operational procedures for KFM v10.3 pipelines.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue.svg)]()
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange.svg)]()
[![Status: Stable](https://img.shields.io/badge/Status-Stable-success.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)]()

</div>

---

## 📘 Overview

The **KFM Operations CLI** provides the authoritative and MCP-governed interface for:

- Running ETL batches or individual sources  
- Performing **trustworthy rollback** (aligned with the v10.3 rollback playbook)  
- Executing retry-safe job recovery with MCP-DL checkpointing  
- Building and publishing STAC Collections/Items  
- Syncing and rebuilding the Knowledge Graph schema  
- Ingesting Focus Mode telemetry  
- Executing CI-mode deterministic validation workflows  

Every command is fully reproducible, idempotent, and validated through KFM’s CI orchestration pipelines.

---

## 📁 Directory Layout

```
src/pipelines/operations/cli/
│
├── cli.py                      # Primary KFM CLI entrypoint
│
├── commands/
│   ├── etl_run.py              # Run ETL for all or specific data sources
│   ├── etl_retry.py            # Checkpoint-based retry mechanism
│   ├── rollback.py             # Trustworthy rollback engine (v10.3 playbook)
│   ├── stac_build.py           # Build STAC Items/Collections
│   ├── stac_publish.py         # Publish STAC to static or API endpoints
│   ├── graph_sync.py           # Neo4j schema + index operations
│   ├── telemetry_ingest.py     # Focus Mode telemetry ingestion and validation
│   └── validate.py             # Validation suite for pipelines & metadata
│
└── utils/
    ├── config.py
    ├── io.py
    ├── locks.py                # Concurrency guards for safe ops
    ├── sandbox.py              # Write sandboxing for CI/dry-runs
    └── checkpoint.py           # Checkpoint / resume state management
```

---

## ⚙️ Installation

Install CLI in development mode:

```
pip install -e .
```

Invoke commands via:

```
kfm
```

or:

```
python -m kfm
```

---

## 🧩 Command Groups

### 1. **ETL Execution**

Run all ETL pipelines:

```
kfm etl run --all
```

Run a specific source:

```
kfm etl run --source ks_historic_topo
```

Dry-run mode:

```
kfm etl run --all --dry
```

---

### 2. **Retry & Checkpoint Recovery**

List checkpoints:

```
kfm etl retry --list
```

Resume a failed job:

```
kfm etl retry --job <job-id>
```

---

### 3. **Trustworthy Rollback (v10.3)**

Create snapshot:

```
kfm ops rollback --snapshot
```

Rollback to snapshot:

```
kfm ops rollback --to <snapshot-name>
```

Rollback bundles include:

- GraphDB export  
- STAC catalog freeze  
- SBOM + manifest integrity verification  
- Telemetry state capture  

---

### 4. **STAC Build & Publish**

Build entire catalog:

```
kfm stac build
```

Publish locally:

```
kfm stac publish --target local
```

Publish to API:

```
kfm stac publish --target remote --url https://stac.kfm.dev/
```

---

### 5. **GraphDB Sync & Rebuild**

Apply schema:

```
kfm graph sync --schema
```

Rebuild indexes:

```
kfm graph sync --indexes
```

Full graph rebuild:

```
kfm graph rebuild
```

---

### 6. **Focus Telemetry Ingestion**

Ingest telemetry batch:

```
kfm telemetry ingest ./telemetry/*.json
```

Validate telemetry:

```
kfm telemetry validate
```

---

### 7. **Validation Suite**

Full validation:

```
kfm validate all
```

Individual validators:

```
kfm validate etl
kfm validate graph
kfm validate stac
kfm validate provenance
```

---

## 🧪 CI Integration

The CLI is invoked in:

- `pipelines.yml`  
- `stac-validate.yml`  
- `faircare-validate.yml`  
- `graph-integrity.yml`  
- `rollback-tests.yml`  

Use non-interactive mode:

```
kfm <command> --ci
```

---

## 🛡️ Safety & Guardrails

The CLI enforces:

- Atomic writes  
- Sandbox modes for CI  
- Lockfile protection against race conditions  
- SHA256 verification  
- Provenance capture  
- Full telemetry auditing  

If a job exits in a partial state, it is automatically quarantined until validated.

---

## 📊 Example Workflow

```
kfm etl run --all
kfm graph sync --schema
kfm stac build
kfm stac publish --target local
kfm telemetry ingest ./telemetry/session.json
kfm validate all
```

Produces:

- Updated ETL outputs  
- Synced graph  
- Regenerated STAC  
- Telemetry ingested  
- Complete governance audit trail  

---

## 📚 Version History

| Version | Date | Notes |
|--------|--------|--------|
| v10.3.0 | 2025-11-14 | Fully rebuilt CLI README using Markdown Output Protocol |
| v10.2.0 | — | Added rollback + checkpoint features |
| v10.1.0 | — | Introduced initial CLI module structure |

---

## 🧾 Governance

This document is governed by:

- MCP-DL v6.3  
- FAIR+CARE Council  
- ROOT-GOVERNANCE.md  
- CI validation workflows  

---
