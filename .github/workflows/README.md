# Kansas-Frontier-Matrix — GitHub Workflows

This folder (`.github/workflows/`) contains **CI/CD automation** for the project.  
Each workflow is scoped, cached, and permissioned for least surprise.

---

## At-a-glance

| Workflow | What it does | Triggers (key paths) | Outputs / Artifacts |
|---|---|---|---|
| **CI** (`ci.yml`) | Lint (ruff/black autodetect), optional mypy, multi-Python **pytest**, geo deps on-demand, web test/build | Changes in `src/`, `stac/`, `data/`, `web/`, `tests/`, `pyproject.toml`, `requirements*.txt` | `.artifacts/pytest-report.xml`, `.artifacts/coverage.xml`, build summary |
| **Tests** (`tests.yml`) | Lightweight Python + web test matrix (quicker than full CI) | Same as CI or narrowed to `tests/**` | `pytest-web-configs.xml` (when targeted), coverage (if `pytest-cov`) |
| **Web Config Validate** (`web-config-validate.yml`) | `jq` JSON lint; validate by `$schema` when present; explicit `app.config.json` / `layers.json`; targeted pytest | `web/app.config.json`, `web/layers.json`, `web/config/**/*.json`, `tests/test_web_configs.py` | Step summaries; `pytest-web-configs.xml` |
| **STAC Validate** (`stac-validate.yml`) | `stac-validator` (recursive if `stac/catalog.json`) → `pystac` fallback; HTTP(S) link checks; local asset existence + optional checksum | `stac/**` | `.artifacts/stac_validator.txt` |
| **STAC & Config** (`stac.yml`) | Validate STAC (+ checksum pass); **render** `web/app.config.json` via `kgt` CLI or module fallback; schema-check rendered config | `stac/**`, `src/**`, `web/**`, `pyproject.toml`, `requirements*.txt` | `.artifacts/stac_report.json`, `web/app.config.json` |
| **STAC Validate & Badges** (`stac-badges.yml`) | Validate STAC → produce per-source Shields endpoint JSONs; weekly + push | `stac/**`, `data/sources/**`, `scripts/**` | `web/badges/*.json`, `build/stac_report.json`, run summary |
| **Site** (`site.yml`) | Build & deploy **MapLibre** site to GitHub Pages; optional MkDocs under `/docs`; Lychee link check | `web/**`, `stac/**`, `data/sources/**`, `mkdocs.yml` | `_site/` artifact (Pages), link-check summary |
| **SBOM** (`sbom.yml`) | Generate **CycloneDX/SPDX** for repo and (if `Dockerfile`) image; attest; **Grype** SARIF | Manual, scheduled weekly, pushes | `artifacts/sbom/**`, SARIF uploads |
| **Docker Build & Publish** (`docker.yml`) | Multi-arch **Buildx** to GHCR (edge/semver/latest); SBOM+provenance; Trivy SARIF; PRs build but don’t push | `Dockerfile`, `docker/**`, `web/**`, `stac/**` | Pushed image (main/tags), `trivy-image.sarif` |
| **CodeQL** (`codeql.yml`) | Security/quality analysis for **Python** and **JS/TS** (autobuild; optional local config) | Push/PR to `main`, weekly schedule | Code Scanning results |
| **Release** (`release.yml`) | Tag-driven build (**sdist+wheel**); tag↔version gate; smoke import; checksums; optional SBOMs; **GitHub Release** | Tags `v*`, manual | `dist/**`, `CHECKSUMS.txt` attached to Release |
| **Roadmap Sync** (`roadmap.yml`) | Parse `.github/roadmap/roadmap.yaml` → labels/milestones/issues; **DRY_RUN on PRs/forks**; optional AJV schema | Roadmap files, sync script, package files | `build/roadmap-sync.log`, `build/plan.json` |
| **Link Check** *(optional)* (`link-check.yml`) | **Lychee** over README/`docs/`/`web/`; PR-diff mode; honors `.lychee.toml`; GIS/API excludes by default | README, `docs/**`, `web/**` | `lychee.md`, `lychee/results.json` |

> **Permissions & safety:** Every workflow asks only for what it needs.  
> Writers (Pages, GHCR, Releases) **skip or run in DRY** on pull requests.

---

## How they connect

```mermaid
flowchart TD
  A["Push/PR"] --> B["web-config-validate.yml\n(\"JSON lint\" + schema)"]
  A --> C["stac-validate.yml\n(\"stac-validator\" → \"pystac\")"]
  A --> D["ci.yml / tests.yml\n(\"pytest\", \"ruff\", web)"]
  C --> E["stac.yml\n(\"render app.config.json\")"]
  E --> F["site.yml\n(\"build + Pages + link check\")"]
  A --> G["docker.yml\n(\"buildx → GHCR\")"]
  A --> H["codeql.yml\n(\"security\")"]
  A --> I["sbom.yml\n(\"CycloneDX/SPDX + attest\")"]
  A --> M["stac-badges.yml\n(\"validate → badges\")"]
  J["Tag \"vX.Y.Z\""] --> K["release.yml\n(\"sdist+wheel+SBOM → Release\")"]
  L["roadmap.yml\n(\"dry-run on PRs\")"] -. "manual/push" .-> L
````

> ⚠️ **Mermaid on GitHub is picky** — quote labels with punctuation and use `\n` for line breaks.

---

## Conventions we follow

* **Least-privilege:** only the permissions required (e.g., `packages: write` only where we push images).
* **Concurrency guards:** each workflow uses a `group: ${{ github.workflow }}-${{ github.ref }}` to prevent overlapping runs on the same ref.
* **Caching:**

  * Python via `actions/setup-python` keyed to `requirements*.txt` / `pyproject.toml`
  * Node via lockfiles (`package-lock.json`, `yarn.lock`, `pnpm-lock.yaml`)
  * Docker Buildx via `cache-from/to: gha`
* **Geo stacks:** CI auto-detects heavy GIS deps and installs system packages (GDAL/PROJ/Spatialite) **only** when required.
* **Schema-first:** JSON/YAML configs lint early with `jq` / `jsonschema` / `ajv` (for roadmap) to **fail fast**.
* **PR safety:** anything that writes (Roadmap sync, Docker publish, Pages deploy) either **skips** on PRs or runs **DRY**.

---

## Common tasks

* **Add a web layer** → update STAC → **`stac.yml`** validates & renders `web/app.config.json` → **`site.yml`** publishes to Pages.
* **Release a package** → tag `vX.Y.Z` → **`release.yml`** builds wheels/sdists, creates SBOMs & checksums → uploads to GitHub Release.
* **Surface STAC health** → **`stac-badges.yml`** writes `web/badges/*.json` for Shields endpoints (overall + per-source).
* **Refresh dependencies** → **Dependabot** (`.github/dependabot.yml`) groups weekly updates for Actions, pip, npm, Docker.

---

## Troubleshooting quick hits

* **Mermaid errors** → quote any label with commas/parentheses and use `\n` for line breaks.
* **GDAL build failures in CI** → keep the system GDAL step enabled; pin `rasterio/fiona` to known-good combos when needed.
* **STAC validation flakes** → if `stac-validator` struggles with remote links, prefer local assets; link checks run separately in `stac-validate.yml`.
* **Pages deploy empty** → ensure the site build writes to `_site/`; `site.yml` fails fast if the directory is empty.
* **Docker context gotcha** → if `docker/Dockerfile` expects `docker/` as context, flip the `context` in `docker.yml`’s detection step.

---

## Next steps (suggested)

* Enable **branch protection** to require **CI**, **Web Config Validate**, **STAC Validate**, and **CodeQL** before merge.
* Add **automerge** for Dependabot minor/patch with passing checks (label-gated).
* Add **PR annotations** for STAC/schema errors via review comments for faster triage.

---

With these workflows, every commit is validated, configs are schema-checked, STAC stays standards-compliant, artifacts are reproducible, and deploys are push-button. 🚀

```
```
