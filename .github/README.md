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
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue.svg)](../docs/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](../LICENSE)
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-orange.svg)](../CONTRIBUTING.md)

</div>

---

## 📘 Overview

The `.github/` directory provides the **automation and governance backbone** of  
the Kansas Frontier Matrix (KFM). It manages how GitHub Actions, CI/CD, and validation systems  
enforce **reproducibility, security, and provenance** under the **Master Coder Protocol (MCP)**.

**Includes:**
- 🔁 Continuous Integration / Deployment (CI/CD)
- 🧩 STAC and checksum validation
- 🛡️ Code & dependency security scanning
- 🪶 Issue and PR templates
- ⚙️ MCP-aligned governance policies

---

## 🗂️ Directory Structure

```bash
.github/
├── README.md
├── workflows/                 
│   ├── site.yml               # Build & deploy docs and web assets
│   ├── stac-validate.yml      # STAC & schema validation
│   ├── codeql.yml             # CodeQL security scanning
│   ├── trivy.yml              # Container & dependency vulnerability scanning
│   ├── pre-commit.yml         # Linting, formatting, testing
│   └── auto-merge.yml         # Auto-merges verified PRs
├── ISSUE_TEMPLATE/
│   ├── bug_report.md
│   ├── feature_request.md
│   └── data_request.md
├── PULL_REQUEST_TEMPLATE.md
└── FUNDING.yml

🧭 All workflows follow MCP documentation-first standards — deterministic, documented, and traceable.

⸻

⚙️ Core Workflows

Workflow	Purpose	Trigger	Output / Artifact
site.yml	Builds & deploys the static documentation and MapLibre web interface.	push to main	_site/ build
stac-validate.yml	Validates STAC collections & JSON Schemas in data/stac/.	push, pull_request	stac-report.json
codeql.yml	Analyzes source code for security & quality issues.	Scheduled / push	CodeQL security dashboard
trivy.yml	Scans containers and dependencies for vulnerabilities.	push, pull_request	Trivy SARIF / HTML reports
pre-commit.yml	Runs linters, formatters, and test hooks.	pull_request	Pre-commit logs
auto-merge.yml	Merges PRs automatically after all checks pass.	Post-check success	Auto-merged PRs


⸻

🧩 Issue & PR Governance

🪶 Pull Request Template

All PRs must use .github/PULL_REQUEST_TEMPLATE.md
to ensure that reproducibility, documentation, and validation are complete.

Checklist Example:

- [ ] Documentation updated
- [ ] STAC + checksum validation passed
- [ ] CodeQL and Trivy reports clean
- [ ] All CI workflows succeeded

🧾 Issue Templates

Located in .github/ISSUE_TEMPLATE/, these guide structured collaboration:
	•	🐞 Bug Reports: Environment, logs, and reproducible steps
	•	💡 Feature Requests: Enhancement or new capability proposals
	•	🗺️ Data Requests: Dataset additions (with provenance, license, and coverage)

⸻

🧠 CI/CD Integration Flow

flowchart TD
    A["🧑‍💻 Push / PR"] --> B["🧹 Pre-Commit Hooks"]
    B --> C["🔍 Lint & Test"]
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

MCP Principle	Implementation
Documentation-First	Every workflow is version-controlled and documented here.
Reproducibility	Deterministic builds, pinned dependencies, and STAC validation.
Provenance	SHA-256 checksums and STAC metadata track dataset lineage.
Auditability	All CI logs and artifacts retained in GitHub workflow history.
Open Standards	YAML-based workflows, STAC 1.0.0 & JSON Schema compliant.


⸻

🔒 Security & Maintenance
	•	🔑 Secrets: Stored securely via Settings → Secrets → Actions
	•	🧩 Dependency Scanning: Weekly via Trivy + CodeQL
	•	🧰 Peer Review: Required for any workflow or policy modification
	•	🧼 Maintenance Schedule: Monthly dependency & action review
	•	🧱 Branch Protection: Enforced via required checks and review approval

⸻

🧱 Integration Overview

Repository Directory	Validated or Managed by
data/	STAC & checksum validation workflows
src/pipelines/	ETL and build/test automation
docs/	Built and deployed via site.yml
web/	Static web app deployed via Pages workflow


⸻

🧭 Maintainer Guidelines
	1.	🔩 Keep workflows modular – one purpose per file.
	2.	🧠 Always pin action versions – no @latest.
	3.	⚙️ Use actions/cache with stable keys for faster builds.
	4.	🚨 Fail fast with clear logs and annotations.
	5.	✅ Auto-merge only when all CI checks and reviews pass.

⸻

🧾 Quick Commands

# Run pre-commit checks locally
pre-commit install
pre-commit run --all-files

# Manually trigger a workflow
gh workflow run site.yml


⸻

📅 Version History

Version	Date	Summary
v1.0.0	2025-10-04	Initial .github automation and governance documentation
v1.1.0	2025-10-05	Refined formatting, tables, and Mermaid rendering for GitHub
v1.2.0	2025-10-06	Enhanced MCP compliance matrix & layout consistency


⸻


<div align="center">


Kansas Frontier Matrix
“Automation with Integrity — Every Workflow Proven.”

📍 /.github/ — Centralized Automation, Validation, and Governance hub
for the Kansas Frontier Matrix Knowledge Infrastructure.

🌐 Full Documentation » · 📦 Data Architecture » · 🧮 STAC Catalog »

</div>
