<div align="center">

# ⚙️ Kansas Frontier Matrix — GitHub Automation & Governance  
`/.github/`

**Mission:** Centralize and manage **automation, CI/CD workflows, issue templates, and governance tools**  
to ensure **reproducibility, security, and Master Coder Protocol (MCP) compliance** across all data and code pipelines.

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

The `.github/` directory provides the **automation, policy, and validation framework**  
that keeps Kansas Frontier Matrix (KFM) reproducible, secure, and auditable.  

It defines how GitHub Actions integrate with the project’s ETL, documentation, and governance systems.

### Includes

- 🔁 Continuous Integration / Deployment (CI/CD)
- 🧩 Data, STAC, and checksum validation
- 🛡️ Code security and container scanning
- 🪶 Issue / Pull Request templates
- ⚙️ Governance rules ensuring **MCP reproducibility**

---

## 🗂️ Directory Structure

```bash
.github/
├── README.md
├── workflows/                 # GitHub Actions (CI/CD, validation, build)
│   ├── site.yml               # Build & deploy documentation and web UI
│   ├── stac-validate.yml      # STAC + JSON Schema validation
│   ├── codeql.yml             # Static analysis / security scanning
│   ├── trivy.yml              # Container & dependency vulnerability scan
│   ├── pre-commit.yml         # Lint / format enforcement
│   └── auto-merge.yml         # Auto-merges verified PRs
├── ISSUE_TEMPLATE/            # Issue templates
│   ├── bug_report.md
│   ├── feature_request.md
│   └── data_request.md
├── PULL_REQUEST_TEMPLATE.md   # PR checklist enforcing reproducibility
└── FUNDING.yml                # (Optional) Funding / sponsorship links

🧭 All workflows follow MCP standards — deterministic, documented, and fully auditable.

⸻

⚙️ Core Workflows

Workflow	Purpose	Trigger	Output / Artifact
site.yml	Builds and deploys the documentation site.	push to main	_site/ static docs site
stac-validate.yml	Validates STAC collections/items in data/stac/.	pull_request, push	Validation report (stac-report.json)
codeql.yml	Static analysis for Python security and code quality.	schedule, push	CodeQL security report
trivy.yml	Scans for dependency and container CVEs.	push, pull_request	Security report (SARIF/HTML)
pre-commit.yml	Linting, formatting, and testing pipeline.	pull_request	Pre-commit validation log
auto-merge.yml	Merges PRs after all checks and reviews pass.	Post-check success	Auto-merged PR


⸻

🧩 Issue & PR Governance

🪶 Pull Request Template

All contributors must use .github/PULL_REQUEST_TEMPLATE.md to ensure:
	•	📘 Proper documentation
	•	🔍 Validation of STAC / data / schema
	•	🧮 Checksum verification
	•	🧠 Compliance with MCP standards

Example Checklist

- [ ] Documentation updated
- [ ] STAC + checksum validation passed
- [ ] CodeQL and Trivy reports clean
- [ ] All CI workflows succeeded

🧾 Issue Templates

Under .github/ISSUE_TEMPLATE/, these enable consistent and reproducible collaboration:
	•	Bug Report: Detailed reproduction, environment, logs
	•	Feature Request: New feature proposals or pipeline improvements
	•	Data Request: Integration of new datasets, sources, or layers

⸻

🧠 CI/CD Integration Map

flowchart TD
  A["🧑‍💻 Push / PR"] --> B["🧹 Pre-Commit Hooks"]
  B --> C["🔍 Lint & Test"]
  C --> D["🧱 STAC + Checksum Validation"]
  D --> E["🛡️ CodeQL + Trivy Security Scans"]
  E --> F["📦 Build + Deploy Docs (site.yml)"]
  F --> G["✅ Auto-Merge if All Checks Pass"]

  style A fill:#fff,stroke:#555,stroke-width:1px
  style D fill:#eafaf1,stroke:#0a6,stroke-width:1px
  style E fill:#e8f0ff,stroke:#006,stroke-width:1px

<!-- END OF MERMAID -->



⸻

🧮 MCP Compliance Matrix

Principle	Implementation Example
Documentation-First	All workflows documented here & version-controlled
Reproducibility	Deterministic builds, pinned deps, consistent schema validation
Provenance	Hashes, STAC metadata, & CI logs preserve data lineage
Auditability	CI/CD logs & validation artifacts stored in workflow history
Open Standards	YAML configuration, JSON Schema, STAC 1.0.0 compliance


⸻

🔒 Security & Maintenance
	•	🔑 Secrets: Manage via GitHub → Settings → Secrets → Actions
	•	🧩 Dependencies: Pinned & scanned weekly (Trivy + CodeQL)
	•	🧰 Reviews: Every major change requires 1 peer review & MCP compliance check
	•	🗓️ Audit Frequency: Monthly workflow dependency review

⸻

🧱 Integration Overview

Directory	Relation to Automation Workflows
data/	STAC + checksum validation on PRs
src/pipelines/	Linked to fetch, process, and validation workflows
docs/	Built and deployed via site.yml
web/	Static frontend deployed with site build workflow


⸻

🧭 Maintainer Notes
	1.	Prefer modular workflows → 1 purpose per YAML.
	2.	Pin action versions → use SHA or tag, not @latest.
	3.	Cache safely → validate cache keys to avoid stale results.
	4.	Fail fast, log clearly → output actionable messages.
	5.	Auto-merge only trusted branches → PRs must pass all MCP checks.

⸻

📅 Version History

Version	Date	Summary
v1.0.0	2025-10-04	Initial full automation & governance documentation rebuild
v1.1.0	2025-10-05	Enhanced formatting, badges, and Mermaid CI/CD diagram for KFM standard


⸻


<div align="center">


Kansas Frontier Matrix
“Automation with Integrity — Every Workflow Proven.”

📍 /.github/ — Centralized automation, CI/CD, and governance hub
for the entire Kansas Frontier Matrix system.

</div>
