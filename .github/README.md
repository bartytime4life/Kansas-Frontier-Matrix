<div align="center">


⚙️ Kansas Frontier Matrix — GitHub Automation & Governance

.github/

Mission: Centralize and manage automation, CI/CD workflows, templates, and governance
to keep the Kansas Frontier Matrix (KFM) reproducible, secure, and standards-compliant.

</div>



⸻

📚 Overview

This directory houses GitHub-specific automation for KFM:
	•	🔄 CI/CD workflows for build, validation, and deploy
	•	🧪 Data and metadata validation (e.g., STAC, JSON Schema)
	•	🛡️ Security scanning (dependencies & container images)
	•	🧩 Issue / PR templates and contribution guardrails
	•	📜 Governance aligned to MCP (documentation-first, provenance, reproducibility)

All automation is designed to make KFM auditable, deterministic, and easy to contribute to.

⸻

🗂️ Directory Layout

.github/
├─ README.md                  # (this file)
├─ workflows/                 # CI/CD workflow definitions
│  ├─ site.yml                # Build & deploy static docs/site
│  ├─ stac-validate.yml       # STAC + JSON Schema validation
│  ├─ codeql.yml              # CodeQL code scanning
│  ├─ trivy.yml               # Trivy vulnerability scanning (containers/deps)
│  ├─ pre-commit.yml          # Lint/format hooks (ruff/black/eslint, etc.)
│  └─ auto-merge.yml          # Safe automerge when all checks pass
├─ ISSUE_TEMPLATE/
│  ├─ bug_report.md
│  ├─ feature_request.md
│  └─ data_request.md
├─ PULL_REQUEST_TEMPLATE.md
└─ FUNDING.yml                # (optional)


⸻

🚦 Core Workflows

Workflow	What it does	Triggers	Key Artifacts / Signals
site.yml	Builds and deploys project docs / static site	push to main, manual dispatch	_site/ or published pages
stac-validate.yml	Validates STAC collections/items and JSON Schemas	pull_request, push	Validation report / check status
pre-commit.yml	Runs linters/formatters/tests (Python/JS)	pull_request	Pre-commit summary
codeql.yml	Static analysis for security/code quality	schedule, push	CodeQL alerts in repo security tab
trivy.yml	Container and dependency vulnerability scan	pull_request, push	Trivy SARIF / annotations
auto-merge.yml	Automerges when all checks & required reviews pass	Post-checks	PR merged automatically (if eligible)

Tip: keep workflow-specific README notes in comments at the top of each YAML.

⸻

🧩 Issue & PR Templates

Issue templates (.github/ISSUE_TEMPLATE/) standardize requests:
	•	Bug report: repro steps, expected vs. actual, env, logs
	•	Feature request: user story, acceptance criteria, design notes
	•	Data request: source URL(s), license, temporal/spatial coverage, intended layer/category

PR template enforces a lightweight governance checklist:
	•	Updated relevant docs / READMEs
	•	Pre-commit hooks pass (lint/format/tests)
	•	STAC / schema validation (if data/metadata changed)
	•	Security scans green (CodeQL/Trivy)
	•	Provenance / license noted for any new data

⸻

🔧 How to Add / Update a Workflow
	1.	Create or edit .github/workflows/<name>.yml.
	2.	Use small, focused jobs and matrix where appropriate.
	3.	Prefer actions with pinned SHAs or version tags.
	4.	Add necessary secrets in Repo → Settings → Secrets and variables → Actions.
	5.	Test on a branch via workflow_dispatch before enabling on main.

⸻

🧠 MCP Compliance (at a glance)
	•	Documentation-first: CI pipelines are documented and linked from docs; changes to CI require doc updates.
	•	Reproducibility: Deterministic builds, checksums, pinned images/deps, and schema/metadata validation.
	•	Provenance: Data PRs must cite source, license, temporal/spatial coverage, and include STAC entries.
	•	Auditability: Every job leaves artifacts or annotations; security alerts are visible and triaged.

⸻

🧪 Local Pre-commit (recommended)

# one-time
pipx install pre-commit    # or pip install --user pre-commit
pre-commit install

# run hooks on all files
pre-commit run --all-files

Configure hooks in .pre-commit-config.yaml (linters/formatters for Python, JS/TS, Markdown, YAML, etc.).

⸻

🔒 Secrets & Security
	•	Store secrets only in Actions secrets (never in repo).
	•	Rotate credentials regularly; prefer OIDC-based cloud auth when possible.
	•	Treat CodeQL/Trivy findings as must-fix before release; suppressions require justification in PR.

⸻

🧭 Maintainer Playbook
	•	Fail fast: Workflows should fail early with actionable logs.
	•	Right-sized jobs: Keep jobs modular; avoid monolithic “do everything” workflows.
	•	Cache prudently: Use actions/cache for large deps, set reliable keys, and validate cache hits.
	•	Permissions-least: permissions: block should be minimal for each job.
	•	Stability: Prefer scheduled runs (e.g., weekly CodeQL/Trivy) to catch silent regressions.

⸻

🧱 Example: Add a New Validation Check
	1.	Create ./.github/workflows/<validator>.yml.
	2.	Add a job that:
	•	Checks out repo
	•	Sets up runtime (e.g., Python)
	•	Installs the tool (pin version)
	•	Runs validation (fail on error)
	•	Uploads reports (e.g., SARIF or HTML) with actions/upload-artifact@vX
	3.	Add a short note to this README under Core Workflows.

⸻

🗺️ Quick Links
	•	Docs: ../docs/
	•	Architecture: ../docs/architecture/
	•	Data & STAC: ../data/ · ../data/stac/
	•	Contributing: ../CONTRIBUTING.md
	•	License: ../LICENSE

⸻


<div align="center">


Kansas Frontier Matrix — automation with integrity.
Every commit should make the system clearer, safer, and more reproducible.

</div>
