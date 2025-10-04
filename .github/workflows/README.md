<div align="center">

# ⚙️ Kansas Frontier Matrix — CI/CD Workflows  
`.github/workflows/`

**Mission:** Orchestrate **validation, security, data governance, and deployment**  
for the Kansas Frontier Matrix (KFM) — delivering a fully reproducible, standards-compliant pipeline.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../docs/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue)](../../LICENSE)

</div>

---

## 📚 Overview

This directory contains **GitHub Actions workflows** that power the KFM repository’s  
**build, validation, and deployment** lifecycle:

- **Data governance:** STAC catalog and checksum verification  
- **Security & quality:** CodeQL, Trivy, pre-commit/lint  
- **Acquisition & publishing:** Fetch raw data, build site, deploy artifacts  
- **Automation:** Auto-merge when all checks pass

All workflows are **declarative** (YAML), **reproducible**, and **MCP-aligned**.

---

## 🗂️ Directory Layout

```bash
.github/workflows/
├── README.md
├── site.yml              # Build & deploy docs / static site
├── stac-validate.yml     # STAC + metadata validation
├── fetch.yml             # Fetch raw data via source manifests
├── checksums.yml         # Compute & verify SHA-256 hashes
├── codeql.yml            # CodeQL code scanning
├── trivy.yml             # Container & dependency vulnerability scans
├── pre-commit.yml        # Linting, formatting, and static checks
└── auto-merge.yml        # Merge PRs automatically when policies pass
````

> **Note:** File names here are canonical; if you rename a workflow file, update links in this README and any badges that reference it.

---

## 🧩 Workflow Summary

| Workflow                | Purpose                                                                    | Triggers                                  | Key Artifacts / Effects                       |
| :---------------------- | :------------------------------------------------------------------------- | :---------------------------------------- | :-------------------------------------------- |
| **`site.yml`**          | Build & deploy documentation/site                                          | `push` to `main`, manual                  | Publishes `_site/` or GitHub Pages            |
| **`stac-validate.yml`** | Validate `data/stac/` items & collections; JSON Schema checks for metadata | `pull_request`, `push`                    | STAC report, failing PR if invalid            |
| **`fetch.yml`**         | Fetch raw data from `data/sources/*.json` (manifest-driven)                | Scheduled, manual dispatch                | Updated `data/raw/` snapshots                 |
| **`checksums.yml`**     | Generate & verify SHA-256 for `data/**`                                    | On data changes, PR                       | `.sha256` files; fails on mismatch            |
| **`codeql.yml`**        | Source scanning & code analysis                                            | Schedule, PR to `main`                    | CodeQL alerts                                 |
| **`trivy.yml`**         | CVE scanning (containers, SBOM/deps)                                       | Schedule, PR, push                        | Security report, failing job on critical CVEs |
| **`pre-commit.yml`**    | Lint, format, static checks (repo-wide)                                    | All PRs                                   | Pre-commit logs; blocks non-compliant diffs   |
| **`auto-merge.yml`**    | Merge safe PRs automatically                                               | After all checks green + required reviews | Auto-merged PRs                               |

---

## ⚙️ Common Configuration Patterns

**Permissions (principle of least privilege):**

```yaml
permissions:
  contents: read
  actions: read
  checks: write
  security-events: write   # only where needed (CodeQL/Trivy)
```

**Concurrency (avoid duplicate runs):**

```yaml
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true
```

**Caching (speed up CI):**

```yaml
- uses: actions/cache@v4
  with:
    path: |
      ~/.cache/pip
      ~/.cache/pre-commit
    key: ${{ runner.os }}-py${{ matrix.python-version }}-${{ hashFiles('**/requirements*.txt') }}
```

**Matrix (example for Python):**

```yaml
strategy:
  matrix:
    python-version: [ "3.10", "3.11" ]
```

---

## 🔐 Secrets & Environment

Some workflows rely on **repository/environment secrets**:

| Secret                    | Used by          | Purpose                                        |
| :------------------------ | :--------------- | :--------------------------------------------- |
| `PAGES_TOKEN` or `GH_PAT` | `site.yml`       | Deploy docs/site                               |
| `DATA_API_KEY_*`          | `fetch.yml`      | Access controlled data endpoints (if required) |
| `GH_TOKEN`                | `auto-merge.yml` | Merge PRs programmatically                     |

> Store secrets via **Settings → Secrets and variables → Actions**.
> Never commit credentials to the repository.

---

## 🧪 Validation Pipelines

### STAC Validation (`stac-validate.yml`)

* Validates **STAC 1.0.0** Items & Collections in `data/stac/`
* Cross-checks **asset links**, **relative paths**, **bbox/time ranges**
* Fails PR if any dataset is **inconsistent or missing metadata**

### Checksums (`checksums.yml`)

* Recomputes **SHA-256** for `data/**`
* Compares to stored `.sha256` manifests in `data/checksums/**`
* Fails PR on **mismatch**, enforcing integrity and reproducibility

---

## 🧰 Typical Commands (referenced in workflows)

```bash
# Build docs/site
make site

# Validate STAC catalog
make stac-validate
stac-validator data/stac/catalog.json

# Compute checksums
make checksums

# Fetch via source manifest
python src/utils/fetch_data.py --manifest data/sources/hydrology/usgs_nhd_flowlines.json
```

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                                    |
| :---------------------- | :-------------------------------------------------------------------------------- |
| **Documentation-first** | Every workflow is described here with purpose, triggers, and outputs.             |
| **Reproducibility**     | Deterministic steps (build, validate, checksum) executed on each run.             |
| **Open Standards**      | YAML workflows; STAC 1.0.0; JSON Schema validation; SHA-256 hashing.              |
| **Provenance**          | Logs & artifacts retained in Actions; data lineage enforced via STAC & checksums. |
| **Auditability**        | PRs blocked unless all checks pass; logs provide full traceability.               |

---

## 🧹 Maintenance

* **Monthly** review of actions versions (e.g., `actions/checkout`, `actions/cache`)
* **Weekly** CodeQL & Trivy scans (auto-scheduled)
* **On data model changes** update STAC schemas & validation rules
* **Onboard contributors** with clear PR template & MCP checklist

---

## 📅 Version History

| Version | Date       | Summary                                                                                |
| :------ | :--------- | :------------------------------------------------------------------------------------- |
| v1.0    | 2025-10-04 | Initial CI/CD workflows documentation (validation, security, fetch, site, automation). |

---

<div align="center">

**Kansas Frontier Matrix** — *“Automation with Integrity: Every Run Proven.”*
📍 [`.github/workflows/`](.) · CI/CD, validation, and governance for the KFM repository.

</div>
