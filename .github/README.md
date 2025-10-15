---
title: "⚙️ Kansas Frontier Matrix — GitHub Automation & Governance"
document_type: "README"
version: "v1.6.2"
last_updated: "2025-10-15"
created: "2025-10-04"
owners: ["@bartytime4life", "@kfm-architecture", "@kfm-security"]
status: "Stable"
maturity: "Production"
tags: ["ci","cd","governance","security","mcp","stac","provenance","versioning","oidc","workflows","labels","issue-forms"]
license: "MIT"
semantic_alignment:
  - STAC 1.0.x
  - JSON Schema
  - CIDOC CRM (provenance)
  - OWL-Time (release windows)
  - DCAT 2.0
ci_required_checks:
  - pre-commit
  - unit-tests
  - codeql
  - trivy
  - stac-validate
  - pages-build-deployment
provenance:
  workflow_pin_policy: "actions pinned by tag or commit SHA"
  artifact_retention_days: 90
---

<div align="center">

# ⚙️ Kansas Frontier Matrix — **GitHub Automation & Governance**  
**Path:** `.github/`

**Mission:** Central **automation + governance hub** for the Kansas Frontier Matrix (KFM) — enforcing  
**reproducibility**, **security**, **provenance**, **versioning**, and **MCP compliance** across all code, data, and docs.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](./workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](./workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](./workflows/codeql.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](./workflows/trivy.yml)
[![Pre-Commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen.svg)](https://pre-commit.com/)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue.svg)](../docs/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](../LICENSE)

</div>

---

## 🧭 Overview

`.github/` defines how KFM **automates, validates, governs, versions, and secures** its lifecycle using GitHub Actions, branch protections, pre-commit, and MCP standards.  
Automation guarantees the repo is **✅ Deterministic · 🔍 Traceable · 🔐 Secure · 🧾 Auditable · 🧮 MCP-Verified**.  
Every commit, workflow, dataset, and artifact becomes part of the **verifiable chain of reproducibility**.

---

## 🗂️ Directory Layout

```bash
.github/
├── workflows/
│   ├── site.yml               # Build & deploy docs and site (GitHub Pages)
│   ├── stac-validate.yml      # Validate STAC collections/items & JSON Schemas
│   ├── codeql.yml             # Static analysis for Python/JS
│   ├── trivy.yml              # Container vulnerability scans (CVE reports)
│   ├── pre-commit.yml         # Lint + style enforcement + tests
│   ├── auto-merge.yml         # Automatically merge passing PRs (policy-bound)
│   └── reusables.yml          # Reusable jobs (lint, cache, matrix)
│
├── ISSUE_TEMPLATE/
│   ├── README.md
│   ├── bug_report.yml
│   ├── feature_request.yml
│   ├── data_request.yml
│   ├── data_correction.yml
│   ├── research_issue.yml
│   ├── accessibility_issue.yml
│   ├── security_vuln.yml
│   └── config.yml
│
├── PULL_REQUEST_TEMPLATE.md
├── FUNDING.yml
├── CODEOWNERS
├── GOVERNANCE.md
└── SECURITY.md

Pinning Policy: All Actions are pinned by tag or commit SHA for deterministic runs.

⸻

⚙️ Core Workflows

Workflow	Purpose	Trigger(s)	Output
site.yml	Build & deploy documentation + site	push→main, workflow_dispatch	_site/ → GitHub Pages
stac-validate.yml	Validate STAC catalogs + checksums + schema	push, pull_request	stac-report.json artifact
codeql.yml	Static analysis (security audit)	schedule, push, pull_request	SARIF report
trivy.yml	CVE scans for images/deps	push, pull_request	Vulnerability report (SARIF/SPDX)
pre-commit.yml	Lint / format / tests / spellcheck	pull_request	Pre-commit log
auto-merge.yml	Policy-gated auto-merge	All checks pass	Merged PR + provenance log
reusables.yml	Reusable jobs (lint/matrix/cache)	workflow_call	Shared, versioned steps


⸻

🧩 CI/CD Flow (Mermaid)

flowchart TD
  A["Push / Pull Request"] --> B["Pre-Commit Hooks"]
  B --> C["Lint & Tests"]
  C --> D["STAC + Checksum Validation"]
  D --> E["Security Scans: CodeQL + Trivy"]
  E --> F["Build & Deploy Docs + Site"]
  F --> G["Auto-Merge + Provenance Log"]
  G --> H["Artifact Archival · MCP Verification"]
%% END OF MERMAID


⸻

🧮 MCP Compliance Matrix

Principle	Implementation
Documentation-First	Inline workflow docs, PR templates, CHANGELOG entries
Reproducibility	Pinned actions, deterministic matrices, container digests
Provenance	SHA-256 checksums, STAC reports, commit SHAs in artifacts
Auditability	CI logs & artifacts retained ≥ 90 days
Open Standards	YAML · JSON Schema · STAC 1.0.x · SPDX
Security	CodeQL + Trivy (SARIF) · least-privilege permissions
Accessibility	Public workflow status, logs, and documentation


⸻

🔒 Security & Permissions Hardening

# Minimal permissions for standard jobs
permissions:
  contents: read
  actions: read
  security-events: write

# OIDC deployments (no long-lived secrets)
permissions:
  id-token: write
  contents: read

# Concurrency & timeouts
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true
timeout-minutes: 20

Pinned Actions (examples)

uses: actions/checkout@3df4f6c4d8c9b0d2f6b5f1e6e3f7a1c2b4d5e6f  # v4.1.1 (commit SHA)
uses: actions/setup-node@v4


⸻

🧾 Issue & Pull Request Governance

✅ PR Checklist (gate)
	•	Docs updated (MCP-DL v6.2)
	•	STAC & checksums pass
	•	Tests passed
	•	CodeQL/Trivy clean
	•	Provenance & license metadata included

🧩 Issue Templates

Template	Purpose
🐞 Bug Report	Repro errors w/ env + logs
💡 Feature Request	Enhancement proposal
🗃️ Data Request	Dataset addition + STAC metadata
🧰 Data Correction	Fix current data/metadata + evidence
🧪 Research Issue	Hypothesis / methods / ADR input
♿ Accessibility	WCAG/ARIA barriers
🔒 Security Vuln	Responsible disclosure path
🧭 Governance Q	Policy / roles / branch strategy


⸻

🌿 Versioning & Release Management

feature/*  →  PR  →  main
             ↓
            tag vX.Y.Z  →  GitHub Release  →  (optional) Zenodo DOI

Backports allowed only with Security + Maintainer approval.

⸻

🌳 Branching Strategy
	•	main — protected / signed / all checks required
	•	release/* — patch lines
	•	feature/* — short-lived, rebase before merge

Required checks: pre-commit · tests · CodeQL · Trivy · STAC validate · Pages build

⸻

👥 Roles & CODEOWNERS (Excerpt)

*                        @kfm-maintainers
.github/workflows/*      @kfm-security @kfm-architecture
data/stac/**             @kfm-data @kfm-architecture
web/**                   @kfm-web
src/**                   @kfm-data @kfm-ml

Policy: Ownership + 2-review rule for security-sensitive paths.

⸻

🧠 Maintainer Guidelines
	1.	Modular Workflows — one purpose per YAML
	2.	Document Everything — header docs + links
	3.	Pin Versions — never @latest
	4.	Fail Fast — clear exit codes & messages
	5.	Test Locally — act or gh workflow run
	6.	Cache Wisely — prune monthly
	7.	Audit Regularly — secrets · permissions · costs

⸻

🧭 Workflow Dependency Graph (Mermaid)

graph LR
  A["Pre-Commit Checks"] --> B["STAC Validation"]
  B --> C["CodeQL Scan"]
  C --> D["Trivy Audit"]
  D --> E["Build + Deploy"]
  E --> F["Auto-Merge + Provenance"]
  F --> G["Artifacts → MCP Verify"]
  G --> H["Audit Trail (SARIF + Logs)"]
%% END OF MERMAID


⸻

💻 CLI Utilities

pre-commit install
pre-commit run --all-files

gh workflow run site.yml
gh run list
gh run download --name "stac-report.json"


⸻

📜 Example Policy Stubs

GOVERNANCE.md (excerpt)

# Governance

## Roles
- Maintainers — roadmap & releases
- Security — secrets & CVE triage
- Data Stewards — STAC & provenance

## Decisions
- Lazy consensus; Maintainers tie-break

## Meetings
- Monthly triage; quarterly roadmap review

SECURITY.md (excerpt)

# Security Policy

- Report to security@kfm.org (PGP key in repo)
- SLA: triage 48h · fix plan 7d · patch 14d
- Secret rotation: quarterly or upon incident


⸻

🕓 Version History

Version	Date	Summary
v1.6.2	2025-10-15	House-style polish (GFM tables, fenced YAML & Mermaid), minor copyedits
v1.6.1	2025-10-15	House-style polish, fixed relative links, expanded templates & matrices
v1.6.0	2025-10-13	Hardened permissions/OIDC · added concurrency · reusable wf
v1.5.0	2025-10-10	Release flow + CODEOWNERS + governance/security
v1.4.0	2025-10-09	Dependency graph + CLI examples + badges
v1.3.0	2025-10-08	Enhanced MCP matrix + STAC reporting
v1.2.0	2025-10-07	Security policy + auto-merge
v1.1.0	2025-10-06	Workflow docs + diagrams
v1.0.0	2025-10-04	Initial CI/CD governance structure


⸻


<div align="center">


⚙️ Kansas Frontier Matrix — Automation with Integrity

“.github/” is the heartbeat of MCP — governing reproducibility, verification, versioning, and security.
Every workflow · Every commit · Every result — Proven · Versioned · Reproducible.

</div>
```
