# 📚 Kansas-Frontier-Matrix — GitHub Automation, CI/CD & Governance

This folder centralizes **automation, workflows, and governance assets** that make the repo **mission-grade: reproducible, secure, testable, and contributor-friendly**.

> Scope: everything under `.github/**` — GitHub Actions, issue/PR templates, security policies, automation configs.

---

## 🚀 What’s Inside

- **README.md** — (this file) overview & governance standards for `.github/`
- **workflows/** — GitHub Actions CI/CD:
  - `site.yml` → Build & publish MapLibre viewer + STAC-driven config
  - `stac-badges.yml` → Generate & commit STAC/source coverage badges
  - `codeql.yml` → CodeQL scanning (Python + JS/TS)
  - `automerge.yml` → Guarded auto-merge for green PRs with labels
  - *(optional)* `tests.yml` → Py/JS tests, schema validation, quick web build
- **ISSUE_TEMPLATE/** — structured templates (bug, data/source request, experiment log)
- **PULL_REQUEST_TEMPLATE.md** — contributor checklist (schemas, STAC, security, docs, tests)
- **SECURITY.md** — vulnerability reporting & security posture
- **dependabot.yml** — automated dependency updates (Actions, npm, pip, docker)

> 🔎 Note: GitHub requires **`.github/dependabot.yml`** (lowercase) and workflows in **`.github/workflows/*.yml`**.

---

## 🛰️ CI/CD Principles

- **Reproducible by design** → workflows call `make` targets (`make prebuild`, `make stac`, `make site`) so **CI = local dev**.
- **Fail-safe defaults** → jobs gracefully skip if inputs are missing (first-run, empty caches).
- **Minimal & pinned** → actions pinned to versions; least-privilege permissions; concurrency to prevent stampedes.
- **Fast feedback first** → linting, STAC + schema checks before heavy builds.
- **Artifacted** → validation reports & site bundles uploaded for inspection.

---

## 🧪 Workflows at a Glance

| Workflow                  | Purpose                                            | Triggers                         | Key Paths / Inputs                                   | Notes                                      |
|---------------------------|----------------------------------------------------|----------------------------------|------------------------------------------------------|--------------------------------------------|
| **Site** (`site.yml`)     | Build & publish `web/` to Pages; validate configs  | `push` → `main`, manual          | `web/**`, `stac/**`, `data/**`, `scripts/**`, `Makefile` | Calls repo `make site`, `make site-config` |
| **STAC Badges**           | Generate STAC/source coverage badges & commit      | schedule, manual                 | `data/sources/**`, `stac/**`, `web/badges/**`        | Commits shields; safe no-op if unchanged   |
| **CodeQL** (`codeql.yml`) | Static analysis (Python + JS/TS)                   | `push`, `pull_request`, schedule | `src/**`, `web/**`, `scripts/**`                     | Uploads SARIF → Code Scanning              |
| **Auto-merge**            | Auto-merge passing PRs with label                  | `pull_request`                   | n/a                                                  | Respects branch protection rules           |
| **Tests (optional)**      | Unit tests + schema validation + quick web build   | `pull_request`, manual           | `tests/**`, `web/**`, `stac/**`                      | Enable once tests exist                    |

---

## 🔁 Dependency Management

- **Ecosystems** → Actions, npm (web), pip, docker  
- **Cadence** → weekly for routine, daily for security advisories  
- **Timezone** → `America/Chicago`  
- **Noise control** → minor/patch grouped where supported  

---

## 🔐 Security Posture

- **Reporting** → see [`SECURITY.md`](./SECURITY.md) or email `security@kansasfrontier.org`  
- **Static analysis** → CodeQL for Python + JS/TS  
- **Secret hygiene** → scoped to jobs only; no long-lived repo-wide secrets  
- **Runner hardening** → minimal `permissions`; `GITHUB_TOKEN` write disabled unless needed; concurrency avoids duplicate runs  

---

## 🧰 Local Pre-flight (Match CI)

Reproduce CI/CD checks locally:

```bash
# Hygiene
pre-commit run -a

# Validation
make prebuild

# Optional tests/docs
pytest -q            # if tests/ exists
mkdocs build -q      # if docs/ exists

If pre-commit isn’t installed:
pipx install pre-commit && pre-commit install

⸻

🧩 Adding or Updating Workflows
	1.	Add a new file under .github/workflows/NAME.yml
	2.	Pin actions (e.g., uses: actions/checkout@v4)
	3.	Set minimal permissions:

permissions:
  contents: read
  actions: read
  security-events: write   # only if uploading SARIF


	4.	Reuse repo make targets → don’t embed logic in YAML
	5.	Cache sanely (lockfiles, pyproject, package.json)
	6.	Document inputs in this README if reusable (env, matrix vars, secrets)

⸻

✅ Standards & Conventions
	•	Branch protection → main requires CI green + reviews
	•	Commit style → imperative + linked issues (Fix: STAC schema validation for topo / Closes #123)
	•	Artifacts → large rasters/vectors tracked in LFS/DVC; configs & STAC JSONs versioned in-repo
	•	Schemas everywhere → update JSON Schemas when config keys change; CI enforces them
	•	Badges → generated by stac-badges.yml under web/badges/; never hand-edit

⸻

🧭 Cross-References
	•	Root docs: README · Makefile · Roadmap
	•	Web config: web/config/ (legends, categories, schemas)
	•	STAC catalog: stac/collections/ · stac/items/
	•	Contribution flow: PR template · Issue templates (.github/ISSUE_TEMPLATE/)

⸻

🧯 Troubleshooting CI/CD
	•	Pre-commit fails → ensure .pre-commit-config.yaml is up to date; run pre-commit autoupdate.
	•	Schema validation fails → run make prebuild; check .artifacts/validation-report.json (uploaded in CI).
	•	Pages deployment stuck → site.yml must set pages permissions + pinned actions/deploy-pages.
	•	CodeQL stalled → confirm language matrix; grant security-events: write only to CodeQL job.

⸻

📝 Philosophy

Automation here enforces the project’s MCP principles:
	•	Reproducibility → schema checks, STAC validation, pre-commit hygiene
	•	Traceability → checksums, provenance manifests, artifacted builds
	•	Safety rails → minimal permissions, pinned actions, enforced schemas

Thin YAML → tested Makefile + scripts handle the heavy lifting.

---
