---
title: "⚙️ Kansas Frontier Matrix — CI/CD Workflows"
document_type: "README"
version: "v2.5.0"
last_updated: "2025-10-15"
owners: ["@kfm-architecture", "@kfm-security", "@kfm-data"]
maturity: "Production"
tags: ["ci","cd","stac","security","provenance","versioning","governance","slsa","sbom","sarif","checksums","dependency-review"]
license: "MIT"
semver_policy: "MAJOR.MINOR.PATCH"
x-mcp: ["Documentation-First","Reproducibility","Provenance","Open-Standards","Auditability","Security"]
---

<div align="center">

# ⚙️ Kansas Frontier Matrix — **CI/CD Workflows**

**Directory:** `.github/workflows/`  
**Mission:** Orchestrate **validation, security, data governance, release/versioning, and deployment** for the  
**Kansas Frontier Matrix (KFM)** — delivering a fully **reproducible**, **auditable**, **secure**, and **standards-compliant** automation framework.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](./site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](./stac-validate.yml)  
[![Checksums](https://img.shields.io/badge/Checksums-SHA256-informational)](#-validation-workflows)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](./codeql.yml)  
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](./trivy.yml)  
[![Dependency Review](https://img.shields.io/badge/DepReview-enabled-brightgreen)](./dependency-review.yml)  
[![Pre-Commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen.svg)](https://pre-commit.com/)  
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue.svg)](../../docs/)  
[![SLSA Provenance](https://img.shields.io/badge/SLSA-provenance-purple)](./provenance.yml)  
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](../../LICENSE)

</div>

---

## 📚 Overview

This directory defines all **GitHub Actions workflows** that power the **Kansas Frontier Matrix (KFM) CI/CD system**.  
Each workflow complies with **MCP-DL v6.2**, ensuring all runs are:

🧾 **Documented** · 🔍 **Traceable** · 🔒 **Secure** · ♻️ **Reproducible** · 🧮 **Verifiable** · 🏷️ **Versioned**

**Automation Domains**

- **Validation** — STAC catalog / JSON Schema / checksum integrity  
- **Security** — CodeQL, Trivy, Dependency Review, SBOM/SARIF  
- **Data Ingestion** — Scheduled dataset fetching / provenance logging  
- **Build & Deploy** — Site, docs, and UI builds (GitHub Pages)  
- **Provenance** — SLSA attestations, artifact signing, retention policies  
- **Governance** — Auto-merge, approvals, SemVer releases  

> **Pinning Policy:** All Actions are pinned by tag or commit SHA for deterministic reproducibility.

---

## 🗂️ Directory Layout

```bash
.github/workflows/
├── README.md
├── site.yml               # Build & deploy docs/site (GitHub Pages)
├── stac-validate.yml      # STAC + JSON Schema validation (gates PRs)
├── fetch.yml              # Manifest-based data acquisition (cron/manual)
├── checksums.yml          # Compute & verify SHA-256 hashes
├── codeql.yml             # Static analysis for Python/JS
├── trivy.yml              # Container CVE scans + SBOM (SARIF)
├── pre-commit.yml         # Linting / formatting / unit tests
├── dependency-review.yml  # Dependency vulnerability gate
├── release.yml            # SemVer tagging, notes, artifact bundling
├── provenance.yml         # SLSA provenance attestations
└── auto-merge.yml         # Policy-gated automerge

⚠️ Note: If filenames change, update badge URLs, required checks, and docs references.

⸻

🧩 Workflow Summary

🧱 Workflow	🎯 Purpose	⏰ Trigger(s)	📦 Outputs
site.yml	Build & deploy documentation + site via GitHub Pages	push → main, workflow_dispatch	_site/ → GitHub Pages
stac-validate.yml	STAC + JSON Schema + link checks	push, pull_request	stac-report.json (artifact)
fetch.yml	Fetch datasets from data/sources/*.json	schedule, workflow_dispatch	data/raw/ snapshots + provenance logs
checksums.yml	Compute & verify SHA-256 integrity	Data PR, workflow_dispatch	.sha256 files + validation logs
codeql.yml	Static analysis (security audit)	schedule, push, pull_request	CodeQL SARIF report
trivy.yml	Container/dependency CVE scan + SBOM	schedule, pull_request	trivy.sarif + SPDX sbom.json
pre-commit.yml	Lint / format / tests / spellcheck	pull_request	PR annotations + summary
dependency-review.yml	Dependency vulnerability gate	pull_request	Inline PR annotations
release.yml	Semantic Version release + notes + assets	tag push, workflow_dispatch	GitHub Release + site bundle, STAC, SARIF, SBOM
provenance.yml	SLSA provenance attestation + signing	release	in-toto / SLSA attestations
auto-merge.yml	Policy-gated automerge	Green checks + approvals	Merged PR + audit log


⸻

🧠 Governance Flow (MCP + SemVer)

flowchart TD
  A["Pull Request / Push"] --> B["Pre-Commit Checks"]
  B --> C["STAC + Checksum Validation"]
  C --> D["Security Scans → CodeQL / Trivy / Dep Review"]
  D --> E["Build + Deploy Site (Preview/Pages)"]
  E --> F["Maintainer Approval / Auto-Merge"]
  F --> G["Release (SemVer) + Notes + SBOM"]
  G --> H["SLSA Provenance + Signing + Retention"]

  classDef default fill:#fff,stroke:#555,color:#111;
  classDef lint fill:#e3f2fd,stroke:#1565c0,color:#111;
  classDef validate fill:#e8f5e9,stroke:#2e7d32,color:#111;
  classDef secure fill:#fffde7,stroke:#f9a825,color:#111;
  classDef deploy fill:#ede7f6,stroke:#4527a0,color:#111;
  classDef audit fill:#f3e5f5,stroke:#6a1b9a,color:#111;

  class A default; class B lint; class C validate; class D secure;
  class E deploy; class F,G,H audit;
%% END OF MERMAID


⸻

⚙️ Design Patterns

🧩 Minimal Permissions (Least Privilege)

permissions:
  contents: read
  actions: read
  security-events: write   # only when uploading SARIF

🔐 OIDC Deployments (No Long-Lived Secrets)

permissions:
  id-token: write
  contents: read
# Cloud side: trust GitHub OIDC issuer; map repo/env to deploy role

🚦 Concurrency (Cancel Redundant Runs)

concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true

⚡ Caching (pip + pre-commit)

- uses: actions/cache@v4
  with:
    path: |
      ~/.cache/pip
      ~/.cache/pre-commit
    key: ${{ runner.os }}-py${{ matrix.python-version }}-${{ hashFiles('**/requirements*.txt') }}

🧪 Matrices (Example)

strategy:
  matrix:
    python-version: ["3.10","3.11"]
    os: ["ubuntu-latest"]

🧭 Triggers & Path Filters

on:
  pull_request:
    paths:
      - '**.py'
      - 'data/stac/**'
      - '.github/workflows/**'

🏷️ Environments & Approvals

environment:
  name: production
  url: https://bartytime4life.github.io/Kansas-Frontier-Matrix/


⸻

🔐 Secrets & Environment Variables

🔑 Secret/Var	🧰 Used by	📝 Purpose	🔒 Notes
PAGES_TOKEN / GH_PAT	site.yml	Pages deploy	Store in Actions → Secrets. Never commit creds.
DATA_API_KEY_*	fetch.yml	External data API auth	One per provider; least-privilege read-only.
GH_TOKEN	auto-merge.yml	PR merge automation	Prefer repo GITHUB_TOKEN; PAT only if needed.
SIGNING_KEY (optional)	provenance.yml	Artifact signing	Prefer keyless OIDC; rotate hardware-backed keys.


⸻

🧮 MCP Compliance Matrix

🧭 Principle	🧩 Implementation
Documentation-First	Header docs, x-kfm-version metadata, workflow annotations
Reproducibility	Pinned actions, deterministic builds, checksum validation
Open Standards	YAML, STAC 1.0, JSON Schema, SPDX, SARIF
Provenance	STAC lineage, SLSA attestations, SHA-256, immutable releases
Auditability	SARIF logs, retention ≥ 90 days, environments & approvals
Security	CodeQL, Trivy, Dependency Review, least-privilege actions
Versioning	SemVer releases, release notes, immutable tags


⸻

♻️ Maintenance & Versioning Cadence

🗓️ Cadence	🔧 Task	✅ Goal
Weekly	Run CodeQL + Trivy scans	Early vulnerability detection
Monthly	Pin / refresh actions/*, rotate caches, verify OIDC	Supply-chain hardening
Quarterly	Re-validate STAC Schemas, update MCP docs	Standards compliance
Per-Release	Tag with SemVer, attach SBOM / SARIF / site bundle	Immutable, attestable releases


⸻

🧰 Common CLI (CI & Local)

# 🔧 Build documentation and site
make site

# 🔍 Validate STAC catalog and metadata
make stac-validate
stac-validator data/stac/catalog.json --recursive

# 🧮 Compute / refresh checksums
make checksums

# 🌊 Fetch external datasets
python src/utils/fetch_data.py --manifest data/sources/hydro/usgs_nhd_flowlines.json

# 🧪 Run pre-commit locally
pre-commit run --all-files

<details><summary><b>gh CLI — Advanced Usage</b></summary>


# Trigger a workflow manually
gh workflow run stac-validate.yml

# Inspect latest runs
gh run list

# Download validation artifact
gh run download --name "stac-report.json"

</details>



⸻

🕓 Version History

🏷️ Version	📅 Date	✍️ Summary
v2.5.0	2025-10-15	Major upgrade for GFM table integrity and rendering fidelity
v2.4.4	2025-10-15	Refactored to strict GFM formatting, verified in GitHub
v2.4.3	2025-10-15	Finalized KFM house-style; badges & anchors verified
v2.4.2	2025-10-15	YAML/Mermaid fencing; copy edits
v2.4.1	2025-10-15	GFM alignment cheatsheet; visual fixes
v2.4.0	2025-10-15	Clarified provenance/signing; improved cadence tables


⸻


<div align="center">


⚙️ Kansas Frontier Matrix — Automation with Integrity

CI/CD under .github/workflows/ ensures every dataset, model, and site build is verifiable, versioned, reproducible,
and fully MCP-compliant.
🧭 Every run leaves a trail. Every artifact is proven.

</div>
```
