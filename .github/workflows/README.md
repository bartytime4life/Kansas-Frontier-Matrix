---
title: "⚙️ Kansas Frontier Matrix — GitHub Actions Workflows (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: ".github/workflows/README.md"
version: "v9.3.2"
last_updated: "2025-10-28"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../releases/v9.3.2/sbom.spdx.json"
manifest_ref: "../../releases/v9.3.2/manifest.zip"
data_contract_ref: "../../docs/contracts/data-contract-v3.json"
governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"
---

<div align="center">

# ⚙️ Kansas Frontier Matrix — **GitHub Actions Workflows**
`.github/workflows/README.md`

**Purpose:** Describes all Continuous Integration / Continuous Deployment (CI/CD) workflows that automate builds, validations, and ethical AI governance for the Kansas Frontier Matrix (KFM).  
Implements full-stack reproducibility and compliance checks under the **Master Coder Protocol (MCP-DL v6.3)**.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](./site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](./stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](./codeql.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](./trivy.yml)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliance%20Enforced-gold)](../../docs/standards/faircare-validation.md)

</div>

---

## 🗂️ Directory Layout

```plaintext
.github/workflows/
├── README.md                      # This file — documentation for all workflows
│
├── site.yml                       # Build & deploy React + MapLibre frontend and documentation portal
├── stac-validate.yml              # Validate STAC metadata and schema conformance
├── codeql.yml                     # Perform static code analysis with GitHub CodeQL
├── trivy.yml                      # Scan container and dependency security vulnerabilities
├── pre-commit.yml                 # Run MCP-DL markdown & style lint checks before merge
├── faircare-validate.yml          # Automate FAIR+CARE data ethics and governance validation
└── governance-ledger.yml          # Update provenance ledger and generate SHA-256 checksums
```

> **In summary:**  
> The `.github/workflows/` directory houses all **CI/CD pipelines** that ensure data, code, and documentation are reproducible, validated, secure, and ethically governed.

---

## 📚 Overview

These workflows coordinate every automation process in the Kansas Frontier Matrix monorepo.  
Each pipeline performs a modular role, together forming an auditable system that validates:
- Build and deployment consistency  
- Geospatial metadata integrity  
- FAIR+CARE ethical compliance  
- AI/ML reproducibility and model drift prevention  
- System and dependency security  

All actions are executed through GitHub Actions and produce logs under the `/reports/` directory for MCP verification.

---

## ⚙️ Workflow Summary

| Workflow File | Description | Trigger | Output Reports |
|----------------|-------------|----------|----------------|
| `site.yml` | Builds and deploys frontend, backend docs, and the project site. | Push / PR to `main` | `reports/deploy/site_build.log` |
| `stac-validate.yml` | Runs STAC 1.0 validation and schema conformance checks for all geospatial datasets. | Push to `data/` / Nightly cron | `reports/self-validation/stac_*.json` |
| `codeql.yml` | Performs static code analysis for vulnerabilities using GitHub CodeQL. | Push / Weekly schedule | `reports/security/codeql_analysis.json` |
| `trivy.yml` | Scans containers and dependencies for CVEs and generates SBOM reports. | Push / Weekly schedule | `reports/security/trivy_scan_results.json` |
| `pre-commit.yml` | Runs pre-commit formatting, linting, and documentation checks. | Push / Pull Request | `reports/lint/precommit_validation.log` |
| `faircare-validate.yml` | Enforces FAIR+CARE validation for new data and governance updates. | Push / PR / Manual trigger | `reports/fair/` & `reports/audit/` |
| `governance-ledger.yml` | Updates provenance ledger, hash integrity, and governance audit files. | On merge to `main` | `reports/audit/ai_hazards_ledger.json` |

---

## 🧠 Workflow Relationships

```mermaid
flowchart TD
A[Commit / PR / Scheduled Task] --> B[Pre-Commit Validation]
B --> C[Build & Site Deploy (site.yml)]
B --> D[STAC Validation (stac-validate.yml)]
C --> E[FAIR+CARE Audit (faircare-validate.yml)]
D --> F[Governance Ledger (governance-ledger.yml)]
E --> G[Security Scans (codeql.yml / trivy.yml)]
F --> H[Artifact + Telemetry Upload]
H --> I[Focus Mode Dashboard + Governance Ledger]
```

Each workflow feeds its results into the **FAIR+CARE governance pipeline**, linking artifacts to the Focus Mode telemetry system for traceability and auditability.

---

## 🧩 Workflow Descriptions

### 🧱 `site.yml` — Build & Deployment
Builds and deploys the MapLibre-based web app and static documentation site.  
Key stages:
- Install Node.js & Python dependencies  
- Run frontend build (`npm run build`)  
- Deploy with `gh-pages`  
- Log artifacts and provenance to `/releases/v9.3.2/`

---

### 🧪 `stac-validate.yml` — STAC Catalog Compliance
Validates all datasets in `data/stac/` for:
- Proper temporal, spatial, and license metadata  
- Linkage to source manifests (`data/sources/`)  
- Compliance with STAC 1.0 and DCAT 3.0 standards  

Outputs validation reports to `reports/self-validation/`.

---

### 🔍 `codeql.yml` — Static Code Security
Runs GitHub CodeQL to ensure code security across:
- Python backend (ETL, AI/ML)  
- React frontend (web/src)  
- YAML, shell, and build scripts  

Reports are exported to `reports/security/codeql_analysis.json`.

---

### 🧰 `trivy.yml` — Container & Dependency Vulnerability Scans
Performs security scans and generates SBOM artifacts (`.spdx.json`):
- Analyzes Docker images and dependencies  
- Checks Node and Python package CVEs  
- Records results to `reports/security/trivy_scan_results.json`

---

### 🧩 `pre-commit.yml` — Documentation & Style Checks
Runs all pre-commit hooks:
- Enforces **KFM Markdown Rules** (MCP-DL syntax)  
- Lints Python, JavaScript, and YAML  
- Validates docs metadata (frontmatter & badges)

---

### 🧭 `faircare-validate.yml` — FAIR+CARE Data Governance
Validates FAIR+CARE compliance for each dataset, manifest, and document:
- Verifies completeness of metadata fields  
- Ensures ethical use, consent, and attribution  
- Updates `reports/fair/hazards_summary.json` and `reports/audit/ai_hazards_ledger.json`

---

### 🧾 `governance-ledger.yml` — Provenance & Ledger Updates
Final step in CI/CD chain — generates immutable audit trails:
- Calculates SHA-256 checksums for data & AI outputs  
- Appends governance records to `reports/audit/`  
- Publishes results to `releases/v9.3.2/focus-telemetry.json`

---

## 🔍 Trigger Types

| Trigger | Purpose |
|----------|----------|
| **Push** | Executes validation and build jobs on code or dataset changes. |
| **Pull Request** | Runs MCP-DL validation to gate merges. |
| **Schedule (cron)** | Weekly audits and security scanning. |
| **Workflow Dispatch** | Manual FAIR+CARE or governance verification. |

---

## 🧭 Governance Integration

Every workflow feeds into the **Governance Ledger**, updating:
- `reports/audit/` — Provenance & ethical AI trace logs  
- `reports/fair/` — FAIR+CARE metrics  
- `releases/` — Telemetry & SBOM snapshots  
- `data/stac/` — Metadata sync and lineage validation  

Workflows cross-reference:
- `docs/standards/governance/`  
- `data/work/tmp/hazards/logs/system/`  
- `reports/audit/ai_hazards_ledger.json`

---

## 🧩 FAIR+CARE Compliance

FAIR Principles:
- **Findable:** All workflows register results in STAC and FAIR metadata.  
- **Accessible:** All logs and SBOMs are stored in open, reusable formats.  
- **Interoperable:** Workflows follow GitHub Actions + MCP-DL conventions.  
- **Reusable:** Each job logs build environments and dependency states.  

CARE Principles:
- **Collective Benefit:** Ensures equitable access to open-source science.  
- **Authority to Control:** FAIR+CARE Council reviews automated decisions.  
- **Responsibility:** Ethics validation pipelines prevent misuse.  
- **Ethics:** Ledger verification guarantees transparency for every action.

---

## 🧾 Version History

| Version | Date       | Author             | Summary |
|----------|------------|--------------------|----------|
| v9.3.2   | 2025-10-28 | @kfm-architecture  | Rebuilt documentation including directory structure. |
| v9.3.1   | 2025-10-27 | @bartytime4life    | Added FAIR+CARE and governance ledger workflow links. |
| v9.3.0   | 2025-10-26 | @kfm-etl-ops       | Established full CI/CD and security validation system. |

---

<div align="center">

**Kansas Frontier Matrix** · *Automation × Provenance × FAIR+CARE Compliance*  
[🔗 Project Repository](https://github.com/bartytime4life/Kansas-Frontier-Matrix) • [🧭 Docs Portal](../../docs/) • [⚖️ Governance Ledger](../../docs/standards/governance/)

</div>