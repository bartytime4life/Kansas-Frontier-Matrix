# ⚙️ Kansas Frontier Matrix — GitHub Automation & Governance
**Path:** `.github/`

---

### 🎯 Mission
Provide a **centralized automation and governance hub** for the **Kansas Frontier Matrix (KFM)** — ensuring **reproducibility**, **security**, **provenance**, and **MCP compliance** across all datasets, pipelines, and documentation.

---

### 🏷️ Status Badges

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml)
[![Pre-Commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen.svg)](https://pre-commit.com/)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue.svg)](../docs/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](../LICENSE)

---

## 🧠 Overview
The `.github/` directory defines how **Kansas Frontier Matrix** automates, validates, and governs its codebase and datasets using **GitHub Actions**, **pre-commit hooks**, and **Master Coder Protocol (MCP)** principles.

Automation here ensures the repository is:

- ✅ Deterministic  
- 🔍 Traceable  
- 🔐 Secure  
- 🧾 Self-documenting  
- 🧮 MCP-aligned  

---

## 🧱 Directory Layout

```bash
.github/
├── workflows/
│   ├── site.yml               # Build & deploy docs and web UI (Pages)
│   ├── stac-validate.yml      # Validate STAC + JSON Schemas
│   ├── codeql.yml             # Static analysis and dependency scanning
│   ├── trivy.yml              # Vulnerability scan (containers & deps)
│   ├── pre-commit.yml         # Linting, formatting, and unit tests
│   └── auto-merge.yml         # Safe PR auto-merge when all checks pass
│
├── ISSUE_TEMPLATE/
│   ├── bug_report.md
│   ├── feature_request.md
│   └── data_request.md
│
├── PULL_REQUEST_TEMPLATE.md   # MCP-compliant PR checklist
└── FUNDING.yml


⸻

⚙️ Core Workflows

Workflow	Purpose	Trigger	Primary Output
site.yml	Build & deploy documentation and static site	push to main	_site/ (GitHub Pages)
stac-validate.yml	Validate STAC collections/items & JSON Schema	push, pull_request	stac-report.json
codeql.yml	CodeQL static analysis for code security	schedule, push	CodeQL dashboard
trivy.yml	Scan containers/dependencies for CVEs	push, pull_request	Trivy SARIF report
pre-commit.yml	Run linting, formatting, & tests	pull_request	Pre-commit report
auto-merge.yml	Auto-merge PRs when all checks succeed	status checks + (optional) label	Merged PR

ℹ️ Note: Ensure “Allow auto-merge” is enabled in repository settings for auto-merge.yml to operate.

⸻

🧩 CI/CD Flow Diagram

flowchart TD
    A([Push or Pull Request]) --> B([Pre-Commit Hooks])
    B --> C([Lint & Unit Tests])
    C --> D([STAC + Checksum Validation])
    D --> E([CodeQL + Trivy Security Scans])
    E --> F([Build & Deploy Docs / Web UI])
    F --> G([Auto-Merge if All Checks Pass])
    G --> H([End])

    %% Color styles (GitHub Mermaid safe)
    classDef default fill:#ffffff,stroke:#555,stroke-width:1px,color:#111;
    classDef test fill:#d7ebff,stroke:#0078d4,stroke-width:1px,color:#111;
    classDef validate fill:#eafaf1,stroke:#1a7f37,stroke-width:1px,color:#111;
    classDef secure fill:#fff8e1,stroke:#ffb300,stroke-width:1px,color:#111;
    classDef deploy fill:#ede7f6,stroke:#6a1b9a,stroke-width:1px,color:#111;
    classDef end fill:#d1ffd7,stroke:#1a7f37,stroke-width:1.5px,color:#111;

    class A default;
    class B test;
    class C test;
    class D validate;
    class E secure;
    class F deploy;
    class G end;
    class H end;

<!-- END OF MERMAID -->


✅ Tip: This diagram renders cleanly with GitHub’s native Mermaid renderer.

⸻

🧮 MCP Compliance Matrix

MCP Principle	Implementation in .github/
Documentation‑First	Every workflow is documented, versioned, and reviewed in PRs.
Reproducibility	Deterministic CI/CD with pinned action versions and caches.
Provenance	STAC + SHA‑256 validation links all datasets and artifacts.
Auditability	CI logs & artifacts retained; SARIF uploads for security scans.
Open Standards	YAML configs, STAC 1.0.x, JSON Schema validation in CI.


⸻

🧾 Issue & PR Governance

✅ Pull Request Template (excerpt)
	•	Documentation updated
	•	STAC + checksum validation passed
	•	CodeQL + Trivy scans clean
	•	All CI workflows succeeded
	•	MCP reproducibility verified

🧩 Issue Templates
	•	🐞 Bug Report — reproducible steps, logs, environment
	•	💡 Feature Request — proposed enhancement & rationale
	•	🗺️ Data Request — dataset proposal with source & license

⸻

🔒 Security & Maintenance

Focus Area	Policy / Action
🔑 Secrets	Store only in Settings → Secrets → Actions; never commit credentials.
🧩 Weekly Scans	Run Trivy & CodeQL automatically via scheduled workflows.
🧰 Peer Review	Required for workflow changes; protected branches enforce review + CI pass.
🧼 Maintenance	Monthly: update pinned action versions; refresh caches; rotate tokens.
🧱 Branch Protection	Require status checks; restrict force‑push; enable signed commits if applicable.


⸻

🧱 Integration Overview

Repository Area	Managed By
data/	STAC + checksum validation workflows
src/pipelines/	ETL & CI validation (lint/tests)
docs/	Built and deployed via site.yml
web/	Static frontend deployed via GitHub Pages


⸻

🧭 Maintainer Guidelines
	1.	Keep workflows modular — one YAML per purpose.
	2.	Pin all action versions (avoid @latest).
	3.	Use actions/cache for dependencies to speed CI.
	4.	Fail fast with clear logs and exit codes.
	5.	Auto‑merge only when all checks pass and policies are met.

⸻

💻 Quick Commands

# Run pre-commit locally (recommended before PR)
pre-commit install
pre-commit run --all-files

# Trigger workflow manually (requires GitHub CLI)
gh workflow run site.yml

# View recent runs
gh run list


⸻

🕓 Version History

Version	Date	Summary
v1.0.0	2025-10-04	Initial automation & governance documentation
v1.1.0	2025-10-06	Improved table layout & readability
v1.2.0	2025-10-07	Final MCP‑aligned formatting for GitHub rendering


⸻

Kansas Frontier Matrix
Automation with Integrity — Every Workflow Proven.
.github/ serves as the automation, validation, and governance hub for the KFM Knowledge Infrastructure.

