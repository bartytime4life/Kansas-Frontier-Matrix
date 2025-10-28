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

**Purpose:** Defines all Continuous Integration / Continuous Deployment (CI/CD) pipelines for the Kansas Frontier Matrix (KFM) repository.  
These workflows automate validation, deployment, and FAIR+CARE governance enforcement under **Master Coder Protocol (MCP-DL v6.3)**.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](./site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](./stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](./codeql.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](./trivy.yml)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliance%20Enforced-gold)](../../docs/standards/faircare-validation.md)

</div>

---

## 📚 Overview

This directory contains **automated GitHub Actions** powering CI/CD, governance validation, and ethical AI compliance for the entire monorepo.  
Each YAML workflow encapsulates a distinct subsystem:
- **Builds and deploys** frontend and documentation artifacts.  
- **Validates** STAC catalogs, FAIR metadata, and schema compliance.  
- **Scans** code, containers, and dependencies for vulnerabilities.  
- **Audits** ethical AI practices through FAIR+CARE and governance workflows.  

All pipelines are reproducible, versioned, and logged under `reports/` per MCP-DL reproducibility standards.

---

## 🧩 Workflow Inventory

| Workflow File | Description | Trigger | Output Reports |
|----------------|-------------|----------|----------------|
| `site.yml` | Builds and deploys the React + MapLibre frontend and docs site. | `push` / `pull_request` to `main` | `reports/deploy/site_build.log` |
| `stac-validate.yml` | Validates STAC catalog and schema conformance for datasets. | `push` to `data/` / nightly cron | `reports/self-validation/` |
| `codeql.yml` | Runs static analysis on Python/JS code using GitHub CodeQL. | `push` / `schedule` | `reports/security/codeql_analysis.json` |
| `trivy.yml` | Performs container and dependency vulnerability scanning. | `push` / weekly schedule | `reports/security/trivy_scan_results.json` |
| `pre-commit.yml` | Enforces MCP-DL formatting and Markdown style guide compliance. | `push` / `pull_request` | `reports/lint/precommit_validation.log` |
| `faircare-validate.yml` | Executes FAIR+CARE data ethics validation. | `push` / `pull_request` / `workflow_dispatch` | `reports/fair/` & `reports/audit/` |
| `governance-ledger.yml` | Updates cryptographic provenance and FAIR+CARE ledger. | On merge to `main` | `reports/audit/ai_hazards_ledger.json` |

---

## 🧠 Workflow Relationships

```mermaid
flowchart TD
A[Code / Data Commit] --> B[Pre-Commit Validation]
B --> C[Build & Site Deploy (site.yml)]
B --> D[STAC + Schema Validation (stac-validate.yml)]
C --> E[FAIR+CARE Ethics Validation (faircare-validate.yml)]
D --> F[Governance Ledger Update (governance-ledger.yml)]
E --> G[Security Scans (codeql.yml / trivy.yml)]
F --> H[Artifacts + Telemetry Export]
H --> I[Releases · Reports · Focus Telemetry]
```

Each workflow feeds into **Focus Mode Telemetry** and **Governance Ledger** for transparency, traceability, and reproducibility.

---

## 🧾 Workflow Summaries

### 🧱 **1. site.yml — Build & Deploy**
Builds the MapLibre-based web application and deploys it to GitHub Pages or Netlify.  
Includes environment setup, dependency caching, and artifact uploads for reproducibility.

**Key Steps:**
- Setup Python + Node environments  
- Build React frontend and documentation  
- Deploy via `gh-pages`  
- Upload reports to `releases/v9.3.2/`  

---

### 🧪 **2. stac-validate.yml — Data Validation**
Validates all geospatial datasets against **STAC 1.0** and internal metadata schemas.  
Enforces FAIR compliance by checking completeness of:
- `bbox`, `datetime`, `license`, `keywords`, and `providers` fields.  
- Cross-referencing datasets with `data/sources/*.json`.  

---

### 🔍 **3. codeql.yml — Code Security**
Performs GitHub’s CodeQL analysis to detect vulnerabilities in:
- Python ETL and AI modules  
- React frontend and build scripts  
- YAML and shell configuration files  

Results are uploaded to the **Security Tab** and `reports/security/`.

---

### 🧰 **4. trivy.yml — Container & Dependency Security**
Uses **Trivy** to scan:
- Dockerfiles and base images  
- Python and Node dependencies  
- GitHub Actions and workflow dependencies  

Produces SBOM (`releases/v9.3.2/sbom.spdx.json`) and alerts maintainers of vulnerabilities.

---

### 🧩 **5. pre-commit.yml — Documentation & Code Quality**
Runs local and CI pre-commit hooks for:
- Markdown linting (KFM Markdown Rules)
- Black (Python), ESLint (JS)
- YAML/JSON schema validation  

Ensures all documentation adheres to **MCP-DL formatting standards**.

---

### 🧭 **6. faircare-validate.yml — FAIR+CARE Compliance**
Automatically verifies all changes meet FAIR+CARE data ethics standards.  
This includes:
- Validating `data/stac/` entries  
- Confirming metadata completeness  
- Running provenance verification  
- Updating governance ledger  

Results populate:
- `reports/fair/hazards_summary.json`  
- `reports/audit/ai_hazards_ledger.json`  

---

### 🧠 **7. governance-ledger.yml — Provenance Tracking**
Generates **cryptographic checksums** for all datasets and commits results to:
- `reports/audit/hazards_archive_provenance.json`
- `releases/v9.3.2/focus-telemetry.json`

Ensures **traceability** for all model outputs, STAC assets, and dataset changes.

---

## ⚙️ Workflow Triggers

| Type | Description |
|------|--------------|
| `push` | Executes on commits to `main`, `develop`, or `data/*` branches. |
| `pull_request` | Validates incoming PRs for documentation, governance, and code quality. |
| `schedule` | Weekly or nightly maintenance tasks (security scans, revalidations). |
| `workflow_dispatch` | Manual triggers for on-demand governance checks. |

---

## 🧩 Governance Integration

All workflows write validation results to:
- `reports/audit/` — Governance and provenance logs  
- `reports/fair/` — FAIR+CARE ethics metrics  
- `data/stac/` — Updated dataset catalog items  
- `releases/v9.3.2/` — Telemetry and SBOM records  

Governance workflows cross-link with:
- `docs/standards/governance/`  
- `docs/standards/faircare-validation.md`  
- `data/work/tmp/hazards/logs/system/`  

---

## 🧾 Version History

| Version | Date       | Author             | Summary                                         |
|----------|------------|--------------------|------------------------------------------------|
| v9.3.2   | 2025-10-28 | @kfm-architecture  | Unified all GitHub workflows and governance linkages. |
| v9.3.1   | 2025-10-27 | @bartytime4life    | Added FAIR+CARE and governance-ledger pipelines. |
| v9.3.0   | 2025-10-26 | @kfm-etl-ops       | Established CI/CD structure and validation flows. |

---

<div align="center">

**Kansas Frontier Matrix** · *Automation × Ethics × Open Science*  
[🔗 Project Repository](https://github.com/bartytime4life/Kansas-Frontier-Matrix) • [🧭 Docs Portal](../../docs/) • [⚖️ Governance Ledger](../../docs/standards/governance/)

</div>