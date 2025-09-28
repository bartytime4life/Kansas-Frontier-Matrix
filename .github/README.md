# 📚 Kansas-Frontier-Matrix — GitHub Automation, CI/CD & Governance

This folder centralizes **community docs, workflows, and project metadata** that make the repo **reproducible, secure, testable, and contributor-friendly**.

> Scope: everything under `.github/**` — actions, issue/PR templates, security, and automation configs.

---

## 📦 What’s here

* **README.md** — (this file) overview and standards for `.github/`
* **workflows/** — GitHub Actions CI/CD:

  * `site.yml` → Build & publish the static site (MapLibre viewer + STAC-backed config)
  * `stac-badges.yml` → Generate & commit STAC/source status badges
  * `codeql.yml` → CodeQL scanning (Python + JS/TS)
  * `automerge.yml` → Safe auto-merge for labeled/green PRs (optional & guarded)
  * *(optional)* `tests.yml` → Py/JS tests, schema checks, and lightweight web build
* **ISSUE_TEMPLATE/** — structured templates (bug, data/source request, experiment report)
* **PULL_REQUEST_TEMPLATE.md** — contributor checklist (tests, schemas, STAC, security, docs)
* **SECURITY.md** — Report handling & current security posture
* **dependabot.yml** — Automated dependency PRs (Actions, npm, pip, docker)

> 🔎 Tip: GitHub expects **`.github/dependabot.yml`** (lowercase) and **`.github/workflows/*.yml`**.

---

## 🛰️ CI/CD Principles

* **Reproducible by default**: pipelines call project make targets (e.g. `make prebuild`, `make stac`, `make site-config`) so local == CI.
* **Fail-safe**: workflows **gracefully skip** when optional inputs are missing (e.g., first-run repos, empty caches).
* **Pinned & minimal**: actions pinned to versions; permissions set to least-privilege; concurrency configured to prevent stampedes.
* **Fast feedback first**: JSON Schema + STAC validation and linting before heavy builds.
* **Artifacted**: validation reports and site bundles are uploaded as artifacts for inspection when applicable.

---

## 🧪 Current workflows at a glance

| Workflow                            | What it does                                             | Triggers                         | Key paths / Inputs                                       | Notes                                                        |
| ----------------------------------- | -------------------------------------------------------- | -------------------------------- | -------------------------------------------------------- | ------------------------------------------------------------ |
| **Site** (`site.yml`)               | Build & publish `web/` to Pages; validates viewer config | `push` to `main`, manual         | `web/**`, `stac/**`, `data/**`, `scripts/**`, `Makefile` | Uses repo targets (`make site`, `make site-config`)          |
| **STAC Badges** (`stac-badges.yml`) | Generate STAC/source status badges & push                | schedule, manual                 | `data/sources/**`, `stac/**`, `web/badges/**`            | Commits shields; safe no-op if nothing changed               |
| **CodeQL** (`codeql.yml`)           | CodeQL analysis (Python + JS/TS)                         | `push`, `pull_request`, schedule | `src/**`, `web/**`, `scripts/**`                         | Uploads SARIF to Code Scanning alerts                        |
| **Auto-merge** (`automerge.yml`)    | Auto-merge green PRs w/ specific labels                  | `pull_request`                   | n/a                                                      | Requires label & passing checks; adheres to protection rules |
| **Tests (optional)** (`tests.yml`)  | Unit tests + schema checks + quick web build             | `pull_request`, manual           | `tests/**`, `web/**`, `stac/**`                          | Enable once tests exist                                      |

---

## 🔁 Dependency updates (Dependabot)

* **Ecosystems**: GitHub Actions, npm (web), pip, docker.
* **Cadence**: weekly for routine updates; daily for **security** advisories.
* **Timezone**: `America/Chicago`.
* Grouping turned on for minor/patch where supported to reduce PR noise.

---

## 🔐 Security practices

* **Reporting**: see **`SECURITY.md`** (private advisories or `security@kansasfrontier.org`)
* **Static analysis**: CodeQL on Python & JS/TS
* **Secret hygiene**: ensure secrets are **only** scoped to workflows that need them; avoid repo-wide secrets for job-local needs
* **Runner hardening**: jobs declare minimal `permissions`; jobs disable `GITHUB_TOKEN` write unless required; concurrency blocks double-runs

---

## 🧰 Local pre-flight (match CI)

Run these locally to get the same signals CI uses:

```bash
# Fast hygiene
pre-commit run -a

# STAC + config validation + safe site fallback
make prebuild

# Optional: tests & docs if present
pytest -q             # if tests/ exists
mkdocs build -q       # if docs/ exists
```

> If pre-commit isn’t installed: `pipx install pre-commit && pre-commit install`

---

## 🧩 Adding/maintaining workflows

1. **Create a new file** in `.github/workflows/NAME.yml`
2. **Pin actions** (e.g., `uses: actions/checkout@v4`)
3. **Set minimal permissions**, e.g.:

```yaml
permissions:
  contents: read
  actions: read
  security-events: write   # only if uploading SARIF
```

4. **Use repo make targets** instead of re-implementing logic in YAML (easier to test & reuse)
5. **Cache sanely** (keyed by lockfiles, pyproject, etc.)
6. **Document inputs** in this README if the workflow is meant to be re-used (matrix vars, env, required secrets)

---

## ✅ Standards & conventions

* **Branch protection** on `main` (require CI green + reviews)
* **Commit style**: imperative + link issues (e.g., `Fix: STAC schema failure for topo` / `Closes #123`)
* **Artifacts**: large geospatial assets via Git LFS/DVC; keep STAC & config JSONs in-repo under version control
* **Schemas everywhere**: when adding/altering config keys, update relevant JSON Schemas (e.g., `web/config/layers.schema.json`) and let CI enforce them
* **Badges**: generated under `web/badges/` by the `stac-badges.yml` job; don’t hand-edit

---

## 🧭 Useful pointers

* Root: [README](../README.md) · [Makefile](../Makefile) · Roadmap ([`.github/roadmap/`](../.github/roadmap/))
* Web config: [`web/config/`](../web/config/) (legend, categories, sources, time, schemas)
* STAC: [`stac/collections/`](../stac/collections/) · [`stac/items/`](../stac/items/)
* Contribution flow: PR template ([`.github/PULL_REQUEST_TEMPLATE.md`](./PULL_REQUEST_TEMPLATE.md)) · Issue templates (`.github/ISSUE_TEMPLATE/**`)

---

## 🧯 Troubleshooting (common CI gotchas)

* **Pre-commit fails in CI**: make sure hooks & versions match (`.pre-commit-config.yaml`); run `pre-commit autoupdate` locally and commit.
* **Schema validation fails**: run `make prebuild` locally and inspect the produced validation report in `.artifacts/` (CI uploads as artifact on failure).
* **Pages deployment stuck**: ensure `site.yml` sets `pages` permissions and uses the **official** pages deploy action (pinned) with the artifact name used by the build step.
* **CodeQL stalled**: verify the language matrix matches repo contents and that `security-events: write` is granted only for the CodeQL job.

---

## 📝 Philosophy

All automation here exists to uphold the project’s **reproducibility**, **traceability**, and **safety rails**: consistent pre-commit hygiene, schema-enforced configs, STAC metadata integrity, and measurable build outputs. Keep YAML thin and push logic into tested scripts/Make targets.

---
