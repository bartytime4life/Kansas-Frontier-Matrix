<div align="center">

# ⚙️ Kansas-Frontier-Matrix — GitHub Automation (`.github/`)

**Mission:** Centralize **automation, CI/CD, and governance** to keep the repo  
**reproducible, secure, and contributor-friendly**, enforcing **MCP** standards  
(*documentation-first, reproducibility, provenance, safety*).

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml)  
[![STAC Badges](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml)  
[![Tests](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/tests.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/tests.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml)  
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml)  
[![Automerge](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/automerge.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/automerge.yml)  

![Dependabot](https://img.shields.io/badge/dependabot-active-brightgreen?logo=dependabot)  
![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)  
![Lint](https://img.shields.io/badge/lint-ruff%20%7C%20black-blueviolet?logo=python)  
![Schema](https://img.shields.io/badge/json--schema-validation-blue?logo=json)  
![Coverage](https://img.shields.io/badge/STAC-coverage-green?logo=stac)  
![Security](https://img.shields.io/badge/security-MCP%20standards-red?logo=github)  

</div>

---

## 🔄 Automation Lifecycle

```mermaid
flowchart TD
  A["Local Dev\nmake · pre-commit"] --> B["CI Jobs\n.github/workflows"]
  B --> C["Validation\nSTAC · schemas · tests"]
  C --> D["Build\nsite · configs"]
  D --> E["Artifacts\nPages · reports · badges"]
  E --> F["Governance\nPR templates · dependabot · security"]
````

<!-- END OF MERMAID -->

**Principles**

* 🌀 **Reproducible** — workflows call `make` targets (`make stac`, `make site`)
* 🛑 **Fail-safe** — jobs skip if inputs are missing
* ⚡ **Minimal** — pinned actions, least-privilege permissions
* 🏃 **Fast feedback** — lint & schema before heavy builds
* 📦 **Artifacted** — reports, sites, and badges uploaded & versioned

---

## 📂 Folder Layout

```
.github/
├─ workflows/              # GitHub Actions (CI/CD)
│  ├─ site.yml             # Build & deploy MapLibre site
│  ├─ stac-badges.yml      # Generate STAC coverage badges
│  ├─ codeql.yml           # Static analysis (Python + JS/TS)
│  ├─ automerge.yml        # Guarded auto-merge for green PRs
│  ├─ tests.yml            # Lint + schema + unit tests
│  └─ trivy.yml            # Container & dependency scanning
├─ ISSUE_TEMPLATE/         # Structured issue templates
├─ PULL_REQUEST_TEMPLATE.md
├─ SECURITY.md             # Vulnerability reporting policy
└─ dependabot.yml          # Automated dependency updates
```

---

## 🧪 Workflows at a Glance

| Workflow        | Purpose                          | Triggers           |
| --------------- | -------------------------------- | ------------------ |
| **Site**        | Build & deploy `/web` (MapLibre) | push→main, manual  |
| **STAC Badges** | Generate coverage shields        | schedule, manual   |
| **Tests**       | Lint + schema + unit tests       | PR, manual         |
| **CodeQL**      | Static analysis (Python + JS/TS) | push, PR, schedule |
| **Trivy**       | Dependency + container scans     | push, schedule     |
| **Automerge**   | Merge passing PRs w/ label       | pull_request       |

---

## 🔐 Security & Permissions

* 🔑 **Least privilege** — permissions scoped to jobs only
* 🛡️ **No long-lived secrets** — OIDC preferred, short-lived tokens only
* 🔍 **CodeQL & Trivy** — automated scans on push + schedule
* 🚨 **Branch protection** — CI green + review required on `main`

```yaml
permissions:
  contents: read
  actions: none
  checks: write
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true
```

---

## 🔁 Dependency Management

* **Ecosystems:** GitHub Actions, npm (`/web`), pip (root), Docker
* **Cadence:** weekly routine updates; daily security patches
* **Noise control:** group minor/patch upgrades where supported

**Example `dependabot.yml`:**

```yaml
- package-ecosystem: "npm"
  directory: "/web"
  schedule:
    interval: "weekly"
  groups:
    minor-and-patch:
      patterns: ["*"]
      update-types: ["minor", "patch"]
```

---

## 🧰 Local Pre-flight (Match CI)

```bash
# Hygiene
pre-commit run -a

# Validation
make prebuild

# Optional
pytest -q       # if tests/ exist
mkdocs build    # if docs/ exist
```

Install hooks if missing:

```bash
pipx install pre-commit && pre-commit install
```

---

## 📝 Governance Standards

* **Branches** → protect `main`, block force-push
* **Commits** → imperative mood, issue-linked (`Fixes #123`)
* **Schemas everywhere** → updated + validated in CI
* **Badges** → generated (e.g. `web/badges/`), never hand-edited
* **Artifacts** → large rasters in LFS/DVC, configs + STAC JSON in-repo

---

## ✅ Summary

`.github/` is the **automation + governance backbone** of Kansas-Frontier-Matrix.
Workflows, templates, and policies here enforce MCP principles:
**reproducibility · provenance · safety-first collaboration.**

One pipeline, two entrypoints: **local (`make`)** and **CI (`.github/workflows/`)**.
Keep them aligned → developers + CI/CD see the same results.
