# ⚙️ Kansas Frontier Matrix — GitHub Automation & Governance
**Path:** `.github/`

---

### 🎯 Mission
Provide a **centralized automation and governance hub** for the **Kansas Frontier Matrix (KFM)** —  
ensuring **reproducibility**, **security**, **provenance**, and **MCP compliance** across all datasets, pipelines, and documentation.

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

## 🧠 Overview

The `.github/` directory defines how **Kansas Frontier Matrix** automates, validates, and governs  
its codebase and datasets using **GitHub Actions**, **pre-commit hooks**, and **Master Coder Protocol (MCP)** principles.

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
│   ├── site.yml               # Build & deploy docs and web UI
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

---

## ⚙️ Core Workflows

| **Workflow** | **Purpose** | **Trigger** | **Primary Output** |
|---------------|-------------|--------------|--------------------|
| `site.yml` | Build & deploy documentation and static site | `push → main` | `_site/` |
| `stac-validate.yml` | Validate STAC collections/items & JSON Schemas | `push`, `pull_request` | `stac-report.json` |
| `codeql.yml` | Run CodeQL static analysis for Python code | `schedule`, `push` | CodeQL dashboard |
| `trivy.yml` | Scan containers and dependencies for CVEs | `push`, `pull_request` | Trivy SARIF report |
| `pre-commit.yml` | Run linting, formatting, and tests | `pull_request` | Pre-commit log |
| `auto-merge.yml` | Auto-merge PRs when all checks succeed | post-check success | Merged PR |

---

## 🧩 CI/CD Flow Diagram

```mermaid
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

✅ Tip: This diagram is 100% valid for GitHub’s native Mermaid renderer.
Just commit and view it directly in the repo — it will render cleanly.

⸻

🧮 MCP Compliance Matrix

MCP Principle	Implementation in .github/
Documentation-First	Every workflow documented and versioned
Reproducibility	Deterministic CI/CD with pinned dependencies
Provenance	STAC + SHA-256 validation links all datasets
Auditability	CI logs and artifacts retained for review
Open Standards	YAML configs, STAC 1.0.0, JSON Schema validation


⸻

🧾 Issue & PR Governance

✅ Pull Request Template

- [ ] Documentation updated  
- [ ] STAC + checksum validation passed  
- [ ] CodeQL + Trivy scans clean  
- [ ] All CI workflows succeeded  
- [ ] MCP reproducibility verified  

🧩 Issue Templates
	•	🐞 Bug Report — reproducible steps, logs, environment
	•	💡 Feature Request — proposed enhancement & rationale
	•	🗺️ Data Request — dataset proposal with source & license

⸻

🔒 Security & Maintenance

Focus Area	Policy / Action
🔑 Secrets	Store only in Settings → Secrets → Actions
🧩 Weekly Scans	Run Trivy + CodeQL automatically
🧰 Peer Review	Required for all workflow changes
🧼 Monthly Maintenance	Update pinned action versions
🧱 Branch Protection	Enforce review + CI pass before merge


⸻

🧱 Integration Overview

Repository Area	Managed By
data/	STAC + checksum validation workflows
src/pipelines/	ETL & CI validation
docs/	Built and deployed via site.yml
web/	Static frontend deployed via GitHub Pages


⸻

🧭 Maintainer Guidelines
	1.	Keep workflows modular — one YAML per purpose
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
v1.1.0	2025-10-06	Improved table layout & readability
v1.2.0	2025-10-07	Final MCP-aligned formatting for GitHub rendering


⸻

Kansas Frontier Matrix
Automation with Integrity — Every Workflow Proven.

.github/ serves as the automation, validation, and governance hub
for the Kansas Frontier Matrix Knowledge Infrastructure.
