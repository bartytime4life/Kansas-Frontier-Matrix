<div align="center">

# ⚙️ Kansas Frontier Matrix — GitHub Automation & Governance  
`/.github/`

**Mission:** Provide a **centralized automation and governance hub**  
for the Kansas Frontier Matrix (KFM), ensuring **reproducibility, security, and transparency**  
across every workflow, dataset, and code commit.

---

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../.github/workflows/codeql.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../.github/workflows/trivy.yml)
[![Pre-Commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen.svg)](https://pre-commit.com/)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../docs/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](../LICENSE)
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-orange.svg)](../CONTRIBUTING.md)
[![Issues](https://img.shields.io/github/issues/bartytime4life/Kansas-Frontier-Matrix.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues)
[![Pull Requests](https://img.shields.io/github/issues-pr/bartytime4life/Kansas-Frontier-Matrix.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pulls)

</div>

---

## 📘 Overview

The `.github/` directory is the **automation and policy engine** for Kansas Frontier Matrix.  
It powers CI/CD pipelines, validation systems, issue templates, and governance policies  
— everything that keeps the repository **auditable, reproducible, and Master Coder Protocol (MCP) compliant**.

### Key Functions
- 🔁 **Continuous Integration / Deployment** (CI/CD)
- 🧩 **STAC & Checksum Validation** for data and metadata
- 🛡️ **Security Scanning** via CodeQL + Trivy
- 🧮 **Automated Testing & Pre-Commit Hooks**
- 🪶 **Standardized Issue and PR Templates**
- ⚙️ **Governance Policies** enforcing MCP reproducibility

---

## 🗂️ Directory Layout

```bash
.github/
├── README.md
├── workflows/                 # All CI/CD automation workflows
│   ├── site.yml               # Build & deploy documentation + web viewer
│   ├── stac-validate.yml      # STAC & metadata validation
│   ├── codeql.yml             # CodeQL static analysis
│   ├── trivy.yml              # Container + dependency CVE scanning
│   ├── pre-commit.yml         # Linting, formatting, testing
│   └── auto-merge.yml         # Auto-merges verified PRs
├── ISSUE_TEMPLATE/            # Templates for issue creation
│   ├── bug_report.md
│   ├── feature_request.md
│   └── data_request.md
├── PULL_REQUEST_TEMPLATE.md   # PR description + MCP checklist
└── FUNDING.yml                # (Optional) sponsorship links

🧭 All workflows adhere to MCP standards — deterministic, documented, and version-controlled.

⸻

⚙️ Core Workflows

Workflow	Purpose	Trigger	Output
site.yml	Build & deploy documentation and MapLibre viewer	push → main	_site/ static build
stac-validate.yml	Validate STAC collections/items in data/stac/	push, PR	stac-report.json
codeql.yml	Analyze code for security + maintainability	Weekly + push	CodeQL dashboard
trivy.yml	Scan dependencies & containers for CVEs	push, PR	Trivy SARIF/HTML report
pre-commit.yml	Enforce linting, testing, formatting	PR	Pre-commit validation
auto-merge.yml	Auto-merge PRs when all checks pass	Post-check success	Auto-merged PRs


⸻

🧩 Governance Templates

🪶 Pull Request Template

Structured PRs ensure MCP compliance and reproducibility.

Checklist Example

- [ ] Updated documentation
- [ ] STAC + checksum validation passed
- [ ] CodeQL + Trivy scans clean
- [ ] All CI workflows succeeded
- [ ] MCP reproducibility criteria met

🧾 Issue Templates

Each request type ensures structured, reproducible collaboration:
	•	🐞 Bug Report: Reproduction steps, environment, logs
	•	💡 Feature Request: Enhancement or new capability proposal
	•	🗺️ Data Request: Dataset integration request (with source & license)

⸻

🧠 CI/CD Workflow Overview

flowchart TD
  A["🧑‍💻 Push or Pull Request"] --> B["🧹 Pre-Commit Hooks"]
  B --> C["🧩 Lint + Tests"]
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
Documentation-First	All workflows are versioned + documented in this README
Reproducibility	Deterministic builds + pinned dependencies
Provenance	STAC metadata + checksum lineage tracking
Auditability	Workflow logs & artifacts stored automatically
Open Standards	YAML configs, JSON Schema, STAC 1.0.0 alignment


⸻

🔒 Security & Maintenance
	•	🔑 Secrets: Use GitHub → Settings → Secrets → Actions
	•	🧩 Scans: Trivy + CodeQL weekly
	•	🧰 Peer Review: Required for workflow updates
	•	🧼 Maintenance: Monthly dependency review
	•	🧱 Branch Protection: Enforced via required checks + review approval

⸻

🧱 Integration Overview

Directory	Validated/Managed by
data/	STAC & checksum validation workflows
src/pipelines/	Linked to ETL + build/test automation
docs/	Deployed via site.yml
web/	Built + published as static assets


⸻

🧭 Maintainer Playbook
	1.	🧩 Keep workflows modular – 1 purpose per YAML.
	2.	🔒 Pin versions – Avoid @latest; use SHAs or version tags.
	3.	🧠 Cache smartly – actions/cache with clear keys.
	4.	⚠️ Fail fast – Output actionable error messages.
	5.	✅ Auto-merge safely – Only after all checks & approvals.

⸻

🧾 Automation Tips

# Run pre-commit locally
pre-commit install
pre-commit run --all-files

# Manually trigger any workflow
gh workflow run <workflow_name.yml>


⸻

📅 Version History

Version	Date	Summary
v1.0.0	2025-10-04	Initial automation + governance documentation
v1.1.0	2025-10-05	Full formatting + badge suite + Mermaid CI/CD diagram
v1.2.0	2025-10-06	Enhanced footer, links, and cross-repo connectivity


⸻


<div align="center">


Kansas Frontier Matrix
“Automation with Integrity — Every Workflow Proven.”

📍 /.github/ — Centralized Automation, Validation, and Governance system
for the Kansas Frontier Matrix Knowledge Infrastructure.

🌐 View Full Documentation » · 📦 Data Architecture » · 🧮 STAC Catalog »

</div>
