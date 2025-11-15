---
title: "🧩 Kansas Frontier Matrix — Operations CLI Utilities (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/operations/cli/utils/README.md"
version: "v10.3.0"
last_updated: "2025-11-14"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/pipelines-operations-cli-utils-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🧩 **Kansas Frontier Matrix — Operations CLI Utilities**  
`src/pipelines/operations/cli/utils/README.md`

**Purpose:**  
Document the utility modules that provide configuration loading, I/O primitives, sandboxing, locking, and checkpointing infrastructure required for safe, MCP-DL compliant command execution across the Operations CLI.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue.svg)]()
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange.svg)]()
[![Status: Stable](https://img.shields.io/badge/Status-Stable-success.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)]()

</div>

---

## 📘 Overview
The **Operations CLI Utility Layer** provides the foundational building blocks powering all command modules under:

```
src/pipelines/operations/cli/commands/
```

These utilities abstract away:

- Configuration parsing  
- Safe filesystem operations  
- Locking and concurrency control  
- Sandbox execution modes (CI-safe)  
- Checkpoint persistence for retry-safe ETL  
- Governance-grade logging and provenance hooks  

Every command in the KFM CLI depends on these utilities for deterministic, auditable, and reversible execution.

---

## 📁 Directory Layout

```
src/pipelines/operations/cli/utils/
│
├── config.py          # Centralized CLI configuration loader and schema checks
├── io.py              # Safe file I/O wrapper (atomic writes, checksums)
├── locks.py           # Concurrency lock manager for all operations
├── sandbox.py         # Sandbox execution mode for CI/dry-run isolation
└── checkpoint.py      # Checkpoint store for retry-safe ETL operations
```

---

## 🧱 Architecture Diagram

```mermaid
flowchart TB
    subgraph Utils
        U1[config]
        U2[io]
        U3[locks]
        U4[sandbox]
        U5[checkpoint]
    end
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

## 🔧 Utility Module Descriptions

### ⚙️ `config.py` — Configuration & Schema Loader
**Responsibilities:**
- Load CLI configuration from environment and `.kfm` files  
- Validate structure via JSON schema  
- Normalize paths, environment flags, and runtime context  
- Expose immutable config objects to all commands  

**Key guarantees:**
- Deterministic config resolution  
- MCP-DL reproducibility compliance  
- No side effects beyond config loading  

---

### 📁 `io.py` — Safe I/O Wrapper
**Responsibilities:**
- Atomic write operations  
- SHA256 checksum generation  
- Controlled read/write sandboxing  
- Error-resistant temp-file handling  

**Key guarantees:**
- Every write is reversible  
- No corruption under parallel workloads  
- Required for provenance tracking  

---

### 🔒 `locks.py` — Concurrency Lock Manager
**Responsibilities:**
- Process-safe lock files for all operations  
- Deadlock detection  
- Automatic lock cleanup on crash recovery  

**Key guarantees:**
- Prevents concurrent destructive operations  
- Required by rollback, retry, and STAC publishing  

---

### 🧪 `sandbox.py` — Sandbox Execution (CI Mode)
**Responsibilities:**
- Handle `--ci` and `--dry-run` flags  
- Block mutations to filesystem in CI  
- Emit synthetic outputs for simulation  

**Key guarantees:**
- CI workflows remain pure and side-effect free  
- Simulation outputs are telemetry-logged  

---

### 📌 `checkpoint.py` — Checkpoint Persistence Engine
**Responsibilities:**
- Store ETL pipeline checkpoint states  
- Resume or invalidate checkpoints safely  
- Track job lineage, timestamps, and failure metadata  

**Key guarantees:**
- Critical for retry-safe ETL via `etl_retry.py`  
- Integrated with governance telemetry  

---

## 🧾 Governance & Compliance
All utility modules must conform to:

- **ROOT-GOVERNANCE.md**  
- **FAIR+CARE ethical standards**  
- **MCP-DL v6.3** documentation-first rules  
- **CI validation gates** (docs-lint, provenance, rollout tests)

Changes require updating `version`, `last_updated`, tests, and metadata.

---

## 📚 Version History

| Version | Date | Notes |
|--------|--------|--------|
| v10.3.0 | 2025-11-14 | Initial creation of utils README under full Markdown Output Protocol |
| v10.2.0 | — | Introduced checkpoint + sandbox utilities |
| v10.1.0 | — | Initial utility layer established |

---

