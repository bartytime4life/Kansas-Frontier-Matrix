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
Provide a fully documented, MCP-aligned command-line interface for running **ETL**, **STAC generation**, **rollback/restore**, **retry-safe job execution**, and **Focus Mode telemetry operations** within the KFM v10.3 pipeline ecosystem.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue.svg)]()
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange.svg)]()
[![Status: Stable](https://img.shields.io/badge/Status-Stable-success.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)]()

</div>

---

## 🧭 Overview

The **KFM Operations CLI** is the unified command surface for executing all validated operational workflows inside the Kansas Frontier Matrix monorepo.  
It provides:

- **Atomic pipeline execution** with retry / checkpointing  
- **Trustworthy rollback** support (aligns with v10.3 rollback playbook)  
- **ETL job orchestration** for all sources in `data/sources/`  
- **STAC & DCAT publishing** for datasets in `data/stac/`  
- **GraphDB sync/refresh hooks**  
- **Focus Telemetry ingestion**  
- **CI-compliant dry-runs**  
- **Disaster-safe replays** with guardrails  

All commands must be reproducible, idempotent, and compliant with MCP-DL v6.3.

---

## 📁 Directory Layout

```
src/pipelines/operations/cli/
│
├── __init__.py
├── cli.py                    # Main entrypoint
├── commands/
│   ├── etl_run.py            # Run ETL batches or single-source ETL
│   ├── etl_retry.py          # Safe retry logic with checkpoint resume
│   ├── rollback.py           # Trustworthy rollback executor
│   ├── stac_build.py         # Build STAC Items/Collections
│   ├── stac_publish.py       # Push STAC to static catalog or API
│   ├── graph_sync.py         # Neo4j schema sync & hot-refresh
│   ├── telemetry_ingest.py   # Focus Mode telemetry ingestion
│   └── validate.py           # Full pipeline validation suite
│
└── utils/
    ├── io.py
    ├── config.py
    ├── locks.py
    ├── sandbox.py
    └── checkpoint.py
```

---

## ⚙️ Installation

### Development install

```
pip install -e .
```

### Global CLI entrypoint

The CLI is exposed as:

```
kfm
```

or, alternatively:

```
python -m kfm
```

---

## 🧩 Command Groups

### **1. ETL Execution**

#### Run all ETL sources

```
kfm etl run --all
```

#### Run a single source

```
kfm etl run --source usgs_historic_topo
```

#### Dry-run mode (no writes)

```
kfm etl run --all --dry
```

---

### **2. Retry & Checkpoint Operations**

Safe retry pipeline with MCP-compliant checkpoint resumption:

```
kfm etl retry --job <job-id>
```

List checkpoints:

```
kfm etl retry --list
```

---

### **3. Trustworthy Rollback (v10.3)**

Rollback to a named snapshot:

```
kfm ops rollback --to snapshot_2025_11_13
```

Create a snapshot:

```
kfm ops rollback --snapshot
```

Snapshots include:

- GraphDB export  
- STAC catalog frozen state  
- Manifest + SBOM integrity check  
- Telemetry state  

---

### **4. STAC / DCAT Build & Publish**

Generate all STAC Items & Collections:

```
kfm stac build
```

Publish to static catalog:

```
kfm stac publish --target local
```

Publish to API endpoint:

```
kfm stac publish --target remote --url https://stac.kfm.dev/
```

---

### **5. GraphDB Sync**

Apply schema migrations and refresh indexes:

```
kfm graph sync --schema
kfm graph sync --indexes
```

Rebuild the entire graph from ETL outputs:

```
kfm graph rebuild
```

---

### **6. Focus Telemetry Ingestion**

Import Focus Mode telemetry logs:

```
kfm telemetry ingest ./telemetry/*.json
```

Run validation:

```
kfm telemetry validate
```

---

### **7. Validation Suite**

Full pre-publish validation pipeline:

```
kfm validate all
```

Individual checks:

```
kfm validate stac
kfm validate graph
kfm validate etl
kfm validate provenance
```

---

## 🧪 CI Integration

The CLI is used heavily inside:

- `.github/workflows/pipelines.yml`  
- `stac-validate.yml`  
- `faircare-validate.yml`  
- `rollback-tests.yml`  
- `graph-integrity.yml`  

All commands support a deterministic `--ci` flag to force non-interactive behavior.

---

## 🛡️ Safety & Guardrails

All commands follow Trustworthy Ops Protocol:

- Atomic execution  
- SHA256 verification for all artifacts  
- Automatic lockfiles (`utils/locks.py`)  
- Sandboxed write mode  
- Rejection of ambiguous or partial job states  
- Telemetry logging for governance auditing  

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

This produces:

- Clean ETL outputs  
- Updated graph  
- Rebuilt STAC  
- Fresh validation  
- Governance-compliant audit trail  

---

## 📚 Version History

| Version | Date | Notes |
|--------|-------|--------|
| v10.3.0 | 2025-11-14 | Initial creation of CLI README, MCP-DL v6.3 alignment |
| v10.2.0 | — | CLI module introduced with operations grouping |
| v10.1.0 | — | Added rollback & checkpoint features |

---

## 🧾 Governance & Compliance

This section is governed by:

- **ROOT-GOVERNANCE.md**  
- **FAIR+CARE Council quarterly reviews**  
- **MCP-DL v6.3 protocols**  
- **AI Safety & Provenance Standards**  

---

## 📨 Contact

For operational issues, open:

```
/issues/new?template=pipelines-operations.md
```

or tag:

**@kfm-ops-team**

---


