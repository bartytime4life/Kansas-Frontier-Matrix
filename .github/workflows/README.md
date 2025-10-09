<div align="center">

# ⚙️ Kansas Frontier Matrix — CI/CD Workflows  
**Directory:** `.github/workflows/`

**Mission:** Orchestrate **validation, security, data governance, and deployment**  
for the Kansas Frontier Matrix (KFM) — delivering a fully **reproducible**, **auditable**, and **standards-compliant** automation framework.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../.github/workflows/codeql.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../.github/workflows/trivy.yml)
[![Pre-Commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen.svg)](https://pre-commit.com/)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue.svg)](../../docs/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](../../LICENSE)

</div>

---

## 📚 Overview

This directory defines **GitHub Actions workflows** that form the backbone of  
KFM’s **continuous integration and deployment (CI/CD)** system.

Each workflow aligns with the **Master Coder Protocol (MCP)**, ensuring that every build, validation, and deploy step is:

🧾 **Documented** 🔍 **Traceable** 🔒 **Secure** ♻️ **Reproducible** 🧮 **Verifiable**

Automation covers five major domains:

1. **Validation:** STAC catalog, schema, checksum integrity  
2. **Security:** CodeQL analysis, Trivy CVE scans, dependency hygiene  
3. **Data Ingestion:** Fetching and snapshotting external datasets  
4. **Build/Deploy:** Generating documentation and web artifacts  
5. **Governance:** Automated merges, deterministic provenance logging  

---

## 🗂️ Directory Layout

```bash
.github/workflows/
├── README.md
├── site.yml              # Build & deploy docs / static site (GitHub Pages)
├── stac-validate.yml     # STAC + metadata validation (Items/Collections)
├── fetch.yml             # Manifest-based raw data acquisition
├── checksums.yml         # Compute & verify SHA-256 hashes for datasets
├── codeql.yml            # Static source code scanning
├── trivy.yml             # CVE + dependency scanning for containers
├── pre-commit.yml        # Linting, formatting, and static analysis
└── auto-merge.yml        # Safe automatic merges when policies pass

⚠️ Note: If workflow filenames are modified, update links in badges, this README, and downstream documentation.

⸻

🧩 Workflow Summary

Workflow	Purpose	Trigger	Output
site.yml	Build + deploy documentation & site	push to main or manual dispatch	Publishes _site/ to GitHub Pages
stac-validate.yml	Validate STAC metadata + JSON Schemas	push, pull_request	Validation report; fails PR on schema errors
fetch.yml	Fetch raw datasets from data/sources/*.json	Scheduled (daily) or manual	Updated data/raw/ snapshots
checksums.yml	Generate + verify SHA-256 digests	PRs affecting data	.sha256 files and validation logs
codeql.yml	CodeQL static analysis	Schedule or push to main	Security dashboard alerts
trivy.yml	Trivy CVE + SBOM scan	Schedule or PR	SARIF vulnerability report
pre-commit.yml	Repo-wide lint/format/tests	All PRs	Pre-commit report; blocks noncompliant code
auto-merge.yml	Auto-merges safe PRs after checks pass	Workflow success + review	Merged PR with audit log


⸻

🧠 MCP Governance & Flow

flowchart TD
  A([Pull Request / Push]) --> B([Pre-Commit Checks])
  B --> C([STAC + Checksum Validation])
  C --> D([Security Scans → CodeQL / Trivy])
  D --> E([Build + Deploy Site])
  E --> F([Auto-Merge / Provenance Log])
  F --> G([Artifact Archival & MCP Verification])

  classDef default fill:#fff,stroke:#555,color:#111;
  classDef lint fill:#e3f2fd,stroke:#1565c0,color:#111;
  classDef validate fill:#e8f5e9,stroke:#2e7d32,color:#111;
  classDef secure fill:#fffde7,stroke:#f9a825,color:#111;
  classDef deploy fill:#ede7f6,stroke:#4527a0,color:#111;
  classDef audit fill:#f3e5f5,stroke:#6a1b9a,color:#111;

  class A default;
  class B lint;
  class C validate;
  class D secure;
  class E deploy;
  class F,G audit;

<!-- END OF MERMAID -->



⸻

⚙️ Workflow Design Patterns

🧩 Permissions — Least Privilege

permissions:
  contents: read
  actions: read
  checks: write
  security-events: write  # used only in CodeQL/Trivy

🚦 Concurrency — Avoid Duplicate Runs

concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true

⚡ Caching — Speed Optimization

- uses: actions/cache@v4
  with:
    path: |
      ~/.cache/pip
      ~/.cache/pre-commit
    key: ${{ runner.os }}-py${{ matrix.python-version }}-${{ hashFiles('**/requirements*.txt') }}

🧪 Matrix Builds — Example

strategy:
  matrix:
    python-version: ["3.10", "3.11"]


⸻

🔐 Secrets & Environment Variables

Secret	Workflow	Purpose
PAGES_TOKEN / GH_PAT	site.yml	Deploy GitHub Pages
DATA_API_KEY_*	fetch.yml	Secure access to external APIs
GH_TOKEN	auto-merge.yml	Auth for PR merge automation

🔒 Secrets Storage: Use Settings → Secrets and variables → Actions.
🚫 Never commit credentials or API keys.

⸻

🧪 Validation Workflows

🗺️ STAC Validation (stac-validate.yml)
	•	Enforces STAC 1.0.0 compliance for all data/stac/ items and collections
	•	Verifies asset URLs, bounding boxes, temporal extents, and schemas
	•	Fails PR if metadata is malformed, missing, or nonstandard

🔢 Checksums (checksums.yml)
	•	Computes SHA-256 for every dataset or derived artifact
	•	Detects discrepancies between computed and stored digests
	•	Fails CI on mismatch to maintain deterministic reproducibility

🧰 Fetch / Acquisition (fetch.yml)
	•	Reads each data/sources/*.json manifest and downloads new or updated datasets
	•	Applies provenance stamps and records metadata into logs
	•	Validates new data using existing STAC schema

⸻

🧰 Common CLI Commands (Used in CI)

# 🔧 Build documentation + web site
make site

# 🔍 Validate STAC catalog & metadata
make stac-validate
stac-validator data/stac/catalog.json

# 🧮 Compute new checksums
make checksums

# 🌊 Fetch external datasets
python src/utils/fetch_data.py --manifest data/sources/hydro/usgs_nhd_flowlines.json


⸻

🧮 MCP Compliance Matrix

MCP Principle	Implementation
Documentation-first	Each workflow is documented here with inputs, outputs, and purpose.
Reproducibility	Build + validate pipelines are deterministic and version-controlled.
Open Standards	YAML (CI), STAC (data), JSON Schema (validation), SHA-256 (integrity).
Provenance	Actions artifacts + logs stored for every run; lineage tracked via STAC.
Auditability	All PRs gated by checks; SARIF + logs retained for 90 days.
Security	CodeQL + Trivy enforce zero-CVE baseline and dependency transparency.


⸻

♻️ Maintenance & Versioning
	•	Weekly: CodeQL + Trivy scans scheduled automatically
	•	Monthly: Review and pin actions/* versions
	•	Quarterly: Revalidate STAC schemas & MCP docs
	•	Continuous: Contributors follow PR template & reproducibility checklist

⸻

🕓 Version History

Version	Date	Summary
v1.0.0	2025-10-04	Initial CI/CD workflow documentation
v1.1.0	2025-10-06	Added security context, validation flow diagram
v1.2.0	2025-10-07	Updated secrets table + MCP compliance matrix
v1.3.0	2025-10-09	Refined flowchart, badges, and modular patterns


⸻


<div align="center">


⚙️ Kansas Frontier Matrix — Automation with Integrity

CI/CD under .github/workflows/ ensures that every dataset, model, and site build
is verifiable, reproducible, and governed by the Master Coder Protocol.

🧭 Every run leaves a trail. Every artifact is proven.

</div>
```
