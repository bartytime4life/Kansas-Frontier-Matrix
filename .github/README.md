<div align="center">

# ⚙️ Kansas Frontier Matrix — GitHub Automation & Governance  
`/.github/`

**Mission:** Centralize and manage **automation, CI/CD workflows, issue templates, and governance tools**  
to ensure **reproducibility, security, and Master Coder Protocol (MCP) compliance**  
across all data and code pipelines.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../.github/workflows/codeql.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../.github/workflows/trivy.yml)
[![Pre-Commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen.svg)](https://pre-commit.com/)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../docs/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue)](../LICENSE)

</div>

---

## 📚 Overview

The `.github/` directory defines **automation, CI/CD, validation, and governance**  
for the **Kansas Frontier Matrix (KFM)** — ensuring everything remains reproducible,  
secure, and auditable under the **Master Coder Protocol (MCP)** framework.

### Includes
- 🔁 Continuous Integration / Deployment (CI/CD)
- 🧩 STAC, checksum, and data validation
- 🛡️ Security scanning (CodeQL, Trivy)
- 🪶 Issue / Pull Request templates
- ⚙️ Governance policies enforcing MCP standards

---

## 🗂️ Directory Structure

```bash
.github/
├── README.md
├── workflows/                 # CI/CD workflow definitions
│   ├── site.yml               # Build & deploy docs and web UI
│   ├── stac-validate.yml      # Validate STAC + JSON Schemas
│   ├── codeql.yml             # Static analysis and code scanning
│   ├── trivy.yml              # Container & dependency vulnerability scan
│   ├── pre-commit.yml         # Linting, formatting, and testing
│   └── auto-merge.yml         # Auto-merges passing PRs
├── ISSUE_TEMPLATE/            # Issue templates for collaboration
│   ├── bug_report.md
│   ├── feature_request.md
│   └── data_request.md
├── PULL_REQUEST_TEMPLATE.md   # PR checklist for reproducibility
└── FUNDING.yml                # Optional: funding/sponsorship config

🧭 All workflows follow MCP standards — deterministic, documented, and reproducible.

⸻

⚙️ Core Workflows

Workflow	Purpose	Trigger	Output
site.yml	Builds and deploys the documentation and static site	push to main	_site/ static docs
stac-validate.yml	Validates all STAC collections and items in data/stac/	pull_request, push	Validation report (stac-report.json)
codeql.yml	Runs static analysis for code quality and security	schedule, push	CodeQL report
trivy.yml	Scans for CVEs in dependencies and containers	push, pull_request	Trivy SARIF / HTML report
pre-commit.yml	Runs linting, formatting, and test hooks	pull_request	Pre-commit log
auto-merge.yml	Auto-merges PRs when all checks pass	Post-check success	Auto-merged PRs


⸻

🧩 Issue & PR Governance

🪶 Pull Request Template

All PRs must follow .github/PULL_REQUEST_TEMPLATE.md
to ensure consistency, reproducibility, and transparency.

Example Checklist

- [ ] Updated all relevant README files
- [ ] STAC + checksum validation passed
- [ ] CodeQL and Trivy scans clean
- [ ] All CI workflows succeeded

🧾 Issue Templates

Under .github/ISSUE_TEMPLATE/, templates ensure structured collaboration:
	•	Bug Reports — reproducible steps, logs, environment info
	•	Feature Requests — proposed enhancements or pipeline upgrades
	•	Data Requests — new dataset integration proposals

⸻

🧠 CI/CD Integration Diagram

flowchart TD
  A["🧑‍💻 Push or Pull Request"] --> B["🧹 Pre-Commit Hooks"]
  B --> C["🔍 Lint & Test"]
  C --> D["🧱 STAC + Checksum Validation"]
  D --> E["🛡️ CodeQL + Trivy Security Scans"]
  E --> F["📦 Build & Deploy Docs (site.yml)"]
  F --> G["✅ Auto-Merge if All Checks Pass"]

  style A fill:#ffffff,stroke:#555,stroke-width:1px
  style D fill:#eafaf1,stroke:#0a6,stroke-width:1px
  style E fill:#e8f0ff,stroke:#006,stroke-width:1px

<!-- END OF MERMAID -->



⸻

🧮 MCP Compliance Matrix

MCP Principle	Implementation
Documentation-First	All workflows documented here and version-controlled
Reproducibility	Deterministic builds, pinned dependencies, and schema validation
Provenance	STAC metadata + checksum tracking for every dataset
Auditability	All CI logs and reports archived in workflow history
Open Standards	YAML-based configs, STAC 1.0.0 compliance, JSON Schema validation


⸻

🔒 Security & Maintenance
	•	🔑 Secrets stored in: Settings → Secrets → Actions
	•	🧩 Dependency Scans: Weekly (Trivy + CodeQL)
	•	🧰 Peer Review: Required for workflow changes
	•	🗓️ Maintenance: Monthly workflow dependency check

⸻

🧱 Integration Overview

Directory	Linked to
data/	Validated by STAC + checksum workflows
src/pipelines/	Used in ETL and validation workflows
docs/	Built and deployed via site.yml
web/	Deployed as static frontend via GitHub Pages


⸻

🧭 Maintainer Notes
	1.	Use modular workflows (1 purpose per YAML).
	2.	Pin all action versions (never @latest).
	3.	Use actions/cache for build optimization.
	4.	Fail fast, log clearly.
	5.	Auto-merge only when all CI checks pass.

⸻

📅 Version History

Version	Date	Summary
v1.0.0	2025-10-04	Initial complete automation + governance documentation
v1.1.0	2025-10-05	Formatting upgrade for GitHub rendering (centered, badges, tables)


⸻


<div align="center">


Kansas Frontier Matrix
“Automation with Integrity — Every Workflow Proven.”

📍 /.github/ — Centralized automation, CI/CD, and governance hub
for the Kansas Frontier Matrix project.

</div>
