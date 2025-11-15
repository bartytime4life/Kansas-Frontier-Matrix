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
Document the command-level modules that power the KFM Operations CLI, including ETL execution, retry safety, trustworthy rollback, STAC creation and publishing, graph synchronization, telemetry ingestion, and validation workflows, all aligned with MCP-DL v6.3 and Diamond⁹ Ω / Crown∞Ω operational standards.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue.svg)]()
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange.svg)]()
[![Status: Stable](https://img.shields.io/badge/Status-Stable-success.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)]()

</div>

---

## 📘 Overview

This directory contains the **command modules** that implement the operational logic for the **KFM CLI**.  
Each file under `commands/` corresponds to a top-level `kfm` subcommand and is responsible for:

- Dispatching user intent into specific pipeline actions  
- Enforcing **idempotent**, **retry-safe**, and **rollback-aware** behavior  
- Logging and telemetry capture for governance and audit trails  
- Respecting FAIR+CARE and MCP-DL v6.3 requirements  

These modules are imported by `src/pipelines/operations/cli/cli.py` and should not perform direct I/O beyond clearly defined interfaces in `utils/`.

---

## 📁 Directory Layout

