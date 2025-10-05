# ⚙️ Kansas Frontier Matrix — GitHub Automation & Governance
**Path:** `.github/`

---

### 🎯 Mission
Provide a **centralized automation and governance hub** for the **Kansas Frontier Matrix (KFM)** —  
ensuring **reproducibility, security, provenance, and MCP compliance** across all datasets, pipelines, and documentation.

---

### 🏷️ Status Badges
[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../.github/workflows/codeql.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../.github/workflows/trivy.yml)
[![Pre-Commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen.svg)](https://pre-commit.com/)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue.svg)](../docs/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](../LICENSE)

---

## 📚 Overview

The `.github/` directory defines how **Kansas Frontier Matrix** automates, validates, and governs  
its codebase and datasets using **GitHub Actions**, **pre-commit hooks**, and **MCP (Master Coder Protocol)** principles.

Automation ensures the repository is:

- ✅ Deterministic  
- 🔍 Traceable  
- 🔐 Secure  
- 🧾 Self-documenting  
- 🧮 MCP-aligned  

---

## 📁 Directory Layout

.github/
├── workflows/
│   ├── site.yml               → Build & deploy docs and web UI
│   ├── stac-validate.yml      → Validate STAC + JSON Schemas
│   ├── codeql.yml             → Static analysis and dependency scanning
│   ├── trivy.yml              → Vulnerability scan (containers & deps)
│   ├── pre-commit.yml         → Linting, formatting, and unit tests
│   └── auto-merge.yml         → Safe PR auto-merge when all checks pass
├── ISSUE_TEMPLATE/
│   ├── bug_report.md
│   ├── feature_request.md
│   └── data_request.md
├── PULL_REQUEST_TEMPLATE.md   → MCP-compliant PR checklist
└── FUNDING.yml

---

## ⚙️ Core Workflows

| Workflow | Purpose | Trigger | Output |
|-----------|----------|----------|--------|
| **`site.yml`** | Build & deploy documentation and static site | Push → `main` | `_site/` |
| **`stac-validate.yml`** | Validate STAC collections/items & JSON Schemas | Push, PR | `stac-report.json` |
| **`codeql.yml`** | Run CodeQL static analysis for Python code | Scheduled, Push | CodeQL dashboard |
| **`trivy.yml`** | Scan containers and dependencies for CVEs | Push, PR | Trivy report |
| **`pre-commit.yml`** | Run linting, formatting, and tests | Pull Request | Pre-commit log |
| **`auto-merge.yml`** | Auto-merge PRs when all checks succeed | On check success | Merged PR |

---

## 🧩 CI/CD Flow Diagram

```mermaid
flowchart TD
    A([Push or Pull Request])
    B([Pre-Commit Hooks])
    C([Lint & Unit Tests])
    D([STAC + Checksum Validation])
    E([CodeQL + Trivy Scans])
    F([Build & Deploy Docs])
    G([Auto-Merge if All Checks Pass])
    H([End])

    A --> B --> C --> D --> E --> F --> G --> H

Legend

Stage	Description
🩵 Testing	Lint & unit tests
🟩 Validation	STAC + Checksum verification
🟨 Security	CodeQL + Trivy scans
🟪 Deployment	Build & deploy docs
🟢 End	Auto-merge success


⸻

🧮 MCP Compliance Matrix

MCP Principle	Implementation
Documentation-First	All workflows are documented and versioned
Reproducibility	Deterministic CI/CD with pinned dependencies
Provenance	STAC + SHA-256 validation links to source data
Auditability	Logs and artifacts retained for review
Open Standards	YAML, STAC 1.0.0, JSON Schema


⸻

🧾 Issue & PR Governance

Pull Request Template

- [ ] Documentation updated  
- [ ] STAC + checksum validation passed  
- [ ] CodeQL + Trivy scans clean  
- [ ] All CI workflows succeeded  
- [ ] MCP reproducibility verified  

Issue Templates
	•	🐞 Bug Report — steps to reproduce + logs
	•	💡 Feature Request — new feature or improvement
	•	🗺️ Data Request — new dataset or source manifest

⸻

🔒 Security & Maintenance

Focus	Policy
Secrets	Store only in Settings → Secrets → Actions
Weekly Scans	Run Trivy + CodeQL automatically
Peer Review	Required for all workflow changes
Maintenance	Update pinned action versions monthly
Branch Protection	Enforce review + CI pass before merge


⸻

🧱 Integration Overview

Component	Managed By
data/	STAC + checksum workflows
src/pipelines/	ETL + CI validation
docs/	Built and deployed via site.yml
web/	Deployed as static frontend (GitHub Pages)


⸻

🧭 Maintainer Guidelines
	1.	Keep workflows modular — one purpose per YAML
	2.	Pin all action versions (avoid @latest)
	3.	Use actions/cache for dependencies
	4.	Fail fast with clear logs
	5.	Auto-merge only when all checks pass

⸻

💻 Quick Commands

# Run pre-commit locally
pre-commit install
pre-commit run --all-files

# Trigger workflow manually
gh workflow run site.yml


⸻

🕓 Version History

Version	Date	Summary
v1.0.0	2025-10-04	Initial automation & governance documentation
v1.1.0	2025-10-06	Improved rendering & layout
v1.2.0	2025-10-07	Final MCP-aligned formatting


⸻

📍 Repository Philosophy

“Automation with Integrity — Every Workflow Proven.”

.github/ is the automation and governance core for the Kansas Frontier Matrix,
managing validation, deployment, and compliance for all data and documentation pipelines.

⸻
