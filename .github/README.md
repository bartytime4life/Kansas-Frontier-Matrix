<div align="center">

# ⚙️ Kansas-Frontier-Matrix — GitHub Automation & Governance (`.github/`)

**Mission:** Provide a **centralized automation and governance hub**  
for the Kansas Frontier Matrix (KFM), ensuring **reproducibility, security, provenance, and MCP compliance**  
across all datasets, pipelines, and documentation.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../.github/workflows/codeql.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../.github/workflows/trivy.yml)
[![Pre-Commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen.svg)](https://pre-commit.com/)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../docs/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../LICENSE)

</div>

---

## 📚 Table of Contents
- [Overview](#overview)
- [Directory Layout](#directory-layout)
- [Core Workflows](#core-workflows)
- [CI/CD Flow Diagram](#cicd-flow-diagram)
- [MCP Compliance Matrix](#mcp-compliance-matrix)
- [Issue & PR Governance](#issue--pr-governance)
- [Security & Maintenance](#security--maintenance)
- [Integration Overview](#integration-overview)
- [Maintainer Guidelines](#maintainer-guidelines)
- [Version History](#version-history)

---

## 🧠 Overview

The `.github/` directory defines how **Kansas Frontier Matrix** automates, validates, and governs  
its codebase and datasets using **GitHub Actions**, **pre-commit hooks**, and **Master Coder Protocol** standards.

Automation here keeps the entire repository:
- Deterministic ✅  
- Traceable 🔍  
- Secure 🧱  
- Self-documenting 🧾  
- Aligned with MCP reproducibility principles 🧮  

---

## 🧱 Directory Layout

```bash
.github/
├── workflows/
│   ├── site.yml               # Build & deploy docs and web UI
│   ├── stac-validate.yml      # Validate STAC + JSON Schemas
│   ├── codeql.yml             # Static analysis and dependency scanning
│   ├── trivy.yml              # Vulnerability scan (containers & deps)
│   ├── pre-commit.yml         # Linting, formatting, and unit tests
│   └── auto-merge.yml         # Safe PR auto-merge when all checks pass
├── ISSUE_TEMPLATE/
│   ├── bug_report.md
│   ├── feature_request.md
│   └── data_request.md
├── PULL_REQUEST_TEMPLATE.md   # MCP-compliant PR checklist
└── FUNDING.yml

⸻

🎯 Purpose
	•	Centralize CI/CD pipelines for validation, security, and deployment.
	•	Enforce STAC & MCP metadata standards on every PR.
	•	Provide consistent contributor templates (issues, PRs).
	•	Maintain auditable, version-controlled automation history.

⸻

⚙️ Core Workflows

Workflow	Purpose	Trigger	Primary Output
site.yml	Build & deploy documentation and static site.	push to main	_site/
stac-validate.yml	Validate STAC collections/items & JSON Schemas.	push, pull_request	stac-report.json
codeql.yml	Run CodeQL static analysis for Python code.	Weekly / push	CodeQL dashboard
trivy.yml	Scan containers and dependencies for CVEs.	push, pull_request	Trivy SARIF report
pre-commit.yml	Run linting, formatting, and tests.	pull_request	Pre-commit log
auto-merge.yml	Auto-merge PRs when all checks succeed.	Post-check success	Merged PR

⸻

🧩 CI/CD Flow Diagram

flowchart TD
    A["🧑‍💻 Push or Pull Request"] --> B["🧹 Pre-Commit Hooks"]
    B --> C["🧮 Lint & Test"]
    C --> D["🧱 STAC + Checksum Validation"]
    D --> E["🛡️ CodeQL + Trivy Scans"]
    E --> F["📦 Build & Deploy Docs (site.yml)"]
    F --> G["✅ Auto-Merge if All Checks Pass"]

    style A fill:#ffffff,stroke:#555,stroke-width:1px
    style D fill:#eafaf1,stroke:#0a6,stroke-width:1px
    style E fill:#e8f0ff,stroke:#006,stroke-width:1px

<!-- END OF MERMAID -->


⸻

🧮 MCP Compliance Matrix

MCP Principle	Implementation in .github/
Documentation-First	Each workflow documented, versioned, and traceable.
Reproducibility	Deterministic CI/CD with pinned actions and dependencies.
Provenance	SHA-256 checksums + STAC metadata link datasets to source.
Auditability	CI logs and reports retained in workflow history.
Open Standards	YAML configs, STAC 1.0.0, JSON Schema validation.

⸻

🧾 Issue & PR Governance

🪶 Pull Request Template

- [ ] Updated all relevant documentation
- [ ] STAC + checksum validation passed
- [ ] CodeQL + Trivy scans clean
- [ ] All CI workflows succeeded
- [ ] MCP reproducibility verified

🧾 Issue Templates

Located in .github/ISSUE_TEMPLATE/:
	•	🐞 Bug Report: reproducible steps, logs, and environment
	•	💡 Feature Request: proposed enhancement and rationale
	•	🗺️ Data Request: dataset proposal with source and license

⸻

🔒 Security & Maintenance
	•	🔑 Secrets: Use Settings → Secrets → Actions
	•	🧩 Weekly Scans: Trivy + CodeQL
	•	🧰 Peer Review: Required for workflow changes
	•	🧼 Monthly Maintenance: Update dependencies and pinned versions
	•	🧱 Branch Protection: Enforce review + CI pass before merge

⸻

🧱 Integration Overview

Repository Area	Validated / Managed By
data/	STAC + checksum validation workflows
src/pipelines/	Linked to ETL and validation CI
docs/	Built and deployed via site.yml
web/	Static frontend deployed via Pages

⸻

🧭 Maintainer Guidelines
	1.	Keep workflows modular — one purpose per YAML.
	2.	Pin action versions (avoid @latest).
	3.	Use actions/cache for large deps.
	4.	Fail fast with clear logs.
	5.	Only auto-merge PRs passing all CI checks.

⸻

🧾 Quick Commands

# Run pre-commit locally
pre-commit install
pre-commit run --all-files

# Manually trigger a workflow
gh workflow run site.yml

⸻

🕓 Version History

Version	Date	Summary
v1.0.0	2025-10-04	Initial automation & governance documentation
v1.1.0	2025-10-06	GitHub-verified rendering; uniform styling
v1.2.0	2025-10-07	Final MCP-aligned formatting & section dividers

⸻

<div align="center">


Kansas Frontier Matrix
“Automation with Integrity — Every Workflow Proven.”

📍 /.github/ — Centralized Automation, Validation, and Governance hub
for the Kansas Frontier Matrix Knowledge Infrastructure.

🌐 Full Documentation » · 📦 Data Architecture » · 🧮 STAC Catalog »

</div>
