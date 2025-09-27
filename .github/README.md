# 📚 Kansas-Frontier-Matrix — GitHub Workflows & Standards

This directory contains **automation, CI/CD, and governance files** for the  
[Kansas-Frontier-Matrix](../README.md) project.

The `.github/` folder centralizes **community docs, workflows, and project metadata** to keep the repo **reproducible**, **secure**, and **contributor-friendly**.

---

## 📖 Contents

- **README.md** — (this file) overview of `.github/`
- **workflows/** — GitHub Actions CI/CD:
  - [`site.yml`](./workflows/site.yml) → build & deploy the static site (MapLibre + STAC)
  - [`stac-badges.yml`](./workflows/stac-badges.yml) → generate STAC/source status badges
  - [`codeql.yml`](./workflows/codeql.yml) → CodeQL scanning (Python + JS/TS)
  - _(optional)_ add `tests.yml` (pytest/MkDocs/etc.) when ready
- **ISSUE_TEMPLATE/** — structured templates for bugs, data requests, experiment reports
- **PULL_REQUEST_TEMPLATE.md** — contributor checklist (tests, schemas, STAC, security)
- **SECURITY.md** — coordinated disclosure & current security practices
- **dependabot.yml** — automated dependency updates ([`.github/dependabot.yml`](./dependabot.yml))

> Tip: GitHub looks for **`.github/dependabot.yml`** (lowercase). Ensure the file name matches.

---

## 🛰️ CI/CD Philosophy

- **Reproducible by default** — pipelines prefer `make prebuild` (STAC + web config validation + site fallback).
- **Fail-safe scaffolding** — workflows **skip gracefully** when optional inputs are missing (e.g., first-run repos).
- **Version-pinned** — actions and containers use pinned versions to reduce supply-chain drift.
- **Least privilege** — workflows declare minimal permissions and use concurrency groups.
- **Fast feedback** — config/schema checks run early; heavy jobs (link check, audits) can be manual or scheduled.

---

## 🧪 What CI checks (today)

| Workflow | Purpose | Triggers | Key paths |
|---|---|---|---|
| `site.yml` | Build & publish `web/` to Pages | `push` to `main`, manual | `web/**`, `stac/**`, `scripts/**`, `Makefile` |
| `stac-badges.yml` | Generate source/status badges | scheduled, manual | `data/sources/**`, `stac/**`, `web/badges/**` |
| `codeql.yml` | CodeQL security analysis | `push`, `pull_request`, scheduled | `src/**`, `web/**`, `scripts/**` |

> Add a `tests.yml` when ready to run `pytest`, `mkdocs build`, or other checks per PR.

---

## 🔁 Dependency Updates

Managed by [Dependabot](./dependabot.yml):

- **Weekly** updates for **GitHub Actions**, **npm (web/)**, **pip**, and **docker** (minor/patch grouped)
- **Daily “security” lane** to raise advisories more quickly  
- Timezone is set to `America/Chicago` to align with project schedules

---

## 🔐 Security

- See **[SECURITY.md](./SECURITY.md)** for reporting instructions (use private advisories or `security@kansasfrontier.org`)
- CodeQL runs on Python + JS/TS
- Secrets scanning via pre-commit (`gitleaks` on push) and `detect-aws-credentials`
- Hardened runners (egress audit), least-privilege workflow permissions

---

## 🧰 Local pre-flight (before you push)

Run these locally to match CI:

```bash
# fast hygiene
pre-commit run -a

# STAC + config validation
make prebuild          # = stac-validate + config-validate + site (fallback)

# optional: full checks
pytest -q              # if tests are present
mkdocs build -q        # if using docs
````

---

## 🗺 Useful pointers

* Repo root: [README](../README.md) · [Makefile](../Makefile) · [Roadmap](../ROADMAP.md)
* Web configs: [`web/config/`](../web/config/) (legend/categories/sources/time/schema)
* STAC: [`stac/collections/`](../stac/collections/) · [`stac/items/`](../stac/items/)
* Contribution flow: [PR template](./PULL_REQUEST_TEMPLATE.md) · Issue templates in [`ISSUE_TEMPLATE/`](./ISSUE_TEMPLATE/)

---

## ✅ Standards & Conventions

* **Branch protection** on `main` (require CI + reviews)
* **Commit style**: imperative mood + linked issues (e.g., `Fixes #123`)
* **Artifacts**: large rasters/vectors via **Git LFS** or DVC; keep STAC & small JSON in-repo
* **Schemas**: update `web/config/schema.json` when adding new config keys; CI & pre-commit will enforce

---

## 📜 License

MIT (see [LICENSE](../LICENSE)). Data licensing follows original sources (USGS, NOAA, FEMA, KGS, etc.).

---

> 🧭 *The `.github/` directory is the governance anchor of Kansas-Frontier-Matrix —
> enabling open, reproducible, and scientifically rigorous collaboration across code, data, and history.*

```
```
