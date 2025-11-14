---
title: "🚀 Kansas Frontier Matrix — STAC Orchestrator GitHub Workflows (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/stac/monitor-validate-publish/.github/workflows/README.md"
version: "v10.3.1"
last_updated: "2025-11-14"
review_cycle: "Quarterly · Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/pipelines-stac-github-workflows-v1.json"
governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🚀 **Kansas Frontier Matrix — STAC Orchestrator GitHub Workflows**  
`src/pipelines/stac/monitor-validate-publish/.github/workflows/README.md`

**Purpose:**  
Document the **GitHub Actions workflow ecosystem** supporting the STAC Monitor → Validate → Publish pipeline.  
These workflows deliver **automated ingestion**, **schema + GE validation**, **governance enforcement**, **artifact handling**, and **telemetry export**, ensuring the pipeline meets **MCP-DL v6.3**, **FAIR+CARE**, **SLSA**, and **Diamond⁹ Ω / Crown∞Ω** compliance.

<img alt="GitHub Actions" src="https://img.shields.io/badge/GitHub_Actions-Automated-blue"/>
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Enforced-orange"/>
<img alt="SLSA" src="https://img.shields.io/badge/SLSA-Provenance-green"/>
<img alt="Status" src="https://img.shields.io/badge/Status-Operational-success"/>

</div>

---

## 📘 Overview

The workflows documented here orchestrate:

- **Scheduled STAC polling** (ETag-aware)
- **Great Expectations validation**
- **CARE + governance checks**
- **Normalization + publication**
- **Graph hydration**
- **Telemetry + sustainability metrics**
- **Artifact packaging**
- **Quarantine workflows with issue creation**
- **SLSA provenance + SBOM linkage**

These workflows live in the repo's root `.github/workflows/` directory, but this documentation describes how they integrate with the pipeline code in this folder.

---

## 🗂️ Directory Layout

~~~~~text
src/pipelines/stac/monitor-validate-publish/.github/workflows/
├── README.md                     # This document
└── (No actual workflow files here — they live in root .github/workflows/)
~~~~~

This folder documents workflow behavior and contracts.

---

## 🔧 Workflow Inventory

The STAC orchestrator depends on the following workflows:

| Workflow | File (root) | Purpose |
|----------|-------------|---------|
| **STAC Orchestrator** | `.github/workflows/stac-orchestrator.yml` | Poll → Validate → Publish |
| **STAC Validator** | `.github/workflows/stac-validate.yml` | Strict STAC schema/DCAT checks |
| **FAIR+CARE Validator** | `.github/workflows/faircare-validate.yml` | Governance + CARE enforcement |
| **Docs Lint** | `.github/workflows/docs-lint.yml` | Markdown + JSON + YAML validation |
| **Telemetry Export** | `.github/workflows/telemetry-export.yml` | Aggregate JSONL → focus-telemetry.json |
| **CodeQL** | `.github/workflows/codeql.yml` | Security/static analysis |
| **Trivy** | `.github/workflows/trivy.yml` | CVE scans against dependencies/images |

---

## 🧩 High-Level Workflow Flow (Indented Mermaid)

~~~~~mermaid
flowchart TD
  A["Cron Trigger / Dispatch"] --> B["Poll STAC API<br/>with ETag"]
  B -->|304| Z["Skip — No Change<br/>Emit Telemetry"]
  B -->|200| C["Write Incoming Batch"]
  C --> D["GE Validation<br/>stac_item_suite"]
  D -->|FAIL| Q["Quarantine + Issue"]
  D -->|PASS| E["Normalize STAC"]
  E --> F["Publish Items & Collections"]
  F --> G["Hydrate Neo4j Graph"]
  F --> H["Upload Artifacts"]
  G --> I["Telemetry Export"]
  Q --> I
~~~~~

---

## 🛠️ Workflow Contract Requirements

Each workflow interacting with the STAC pipeline must:

### 1. Enforce Schema Validation
- JSON Schema  
- GE Expectation Suites  
- KFM metadata extension rules  

### 2. Enforce CARE Governance
- CARE label presence  
- Masking compliance  
- Sovereignty rules  
- Governance ledger updates  

### 3. Enforce Telemetry Contract
Must write to JSONL:

- counts (polled/new/published)  
- schema & care failures  
- graph hydration status  
- ETag behavior  
- energy + CO₂e  

### 4. Protect Immutability
- No overwriting published STAC items  
- Version bumps required for updates  
- SemVer rules applied  

### 5. Publish Artifacts
- Incoming  
- Published  
- DataDocs  
- Quarantine packages  

### 6. Governance Sync
- Append governance logs  
- Append versioning ledger  
- Append quarantine ledger  

---

## 🔐 Workflow Permissions

| Permission | Justification |
|-----------|---------------|
| `contents: write` | Save ETAG cache, artifacts |
| `issues: write` | Open FAIR+CARE governance issues |
| `id-token: write` | SLSA provenance signing |
| `actions: read` | Retrieve prior logs/artifacts |

**No secret is ever printed in logs.**

---

## 🏗️ Workflow Environment & Dependencies

Workflows must provision:

- Python 3.11  
- Great Expectations  
- neo4j-driver  
- jsonschema  
- shapely + geopandas (optional)  
- H3 / quadbin (optional)  
- KFM pipeline utilities  

Minimum installation example:

~~~~~yaml
pip install -r requirements.txt
pip install great_expectations neo4j jsonschema shapely h3
~~~~~

---

## 📦 Artifact Structure

When a workflow uploads artifacts, they must follow:

~~~~~text
stac-run-<run_id>/
├── incoming/
├── published/
│   ├── collections/
│   └── items/
└── datadocs/
~~~~~

All artifacts must be:

- Complete  
- WCAG-accessible (for DataDocs)  
- Immutable  
- Linked in GitHub Issue (if failure)  

---

## 📡 Telemetry Aggregation

Workflow `telemetry-export.yml` merges JSONL into:

~~~~~text
releases/v10.3.0/focus-telemetry.json
~~~~~

Telemetry schema:

~~~~~text
src/pipelines/stac/monitor-validate-publish/.github/schemas/pipelines-stac-github-workflows-v1.json
~~~~~

---

## 🧭 Governance Integration

Governance pipeline requires:

- Quarantine events → governance-ledger  
- CARE decisions → CARE audit log  
- Version increments → versioning-ledger  
- STAC publication → provenance-ledger  

Primary reference:

~~~~~text
../../../../../docs/standards/governance/ROOT-GOVERNANCE.md
~~~~~

---

## ✨ Local Development Simulation

Simulate workflow steps:

```bash
python src/pipelines/stac/monitor-validate-publish/monitor.py
great_expectations checkpoint run stac_items \
  --config src/pipelines/stac/monitor-validate-publish/expectations/great_expectations.yml \
  --suite stac_item_suite
python src/pipelines/stac/monitor-validate-publish/publish.py
```

Review telemetry:

```bash
jq '.' src/pipelines/stac/monitor-validate-publish/data/telemetry/*.jsonl
```

---

## 🕰️ Version History

| Version | Date       | Author | Summary |
|---------|------------|--------|---------|
| v10.3.1 | 2025-11-14 | STAC Pipelines Team | Added full documentation for workflow ecosystem integration for STAC orchestration. |

---

<div align="center">

**Kansas Frontier Matrix — GitHub Workflow Integration**  
Secure Automation × FAIR+CARE × Provenance × Deterministic ETL  
© 2025 Kansas Frontier Matrix — MIT License  

[Back to Orchestrator GitHub Docs](../README.md)

</div>
