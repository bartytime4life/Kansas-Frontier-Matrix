# Kansas-Frontier-Matrix — GitHub Workflows

This folder (`.github/workflows/`) contains the **CI/CD + security automation** for the project.
Every workflow is **scoped, cached, concurrent-safe, and least-privilege permissioned**.

---

## At-a-glance

| Workflow                                               | What it does                                                                                                                            | Triggers (key paths)                                                                          | Outputs / Artifacts                                                  |
| ------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| **CI** (`ci.yml`)                                      | Lint (ruff/black autodetect), optional mypy, multi-Python **pytest**, geo deps on-demand, web test/build                                | `src/**`, `stac/**`, `data/**`, `web/**`, `tests/**`, `pyproject.toml`, `requirements*.txt`   | `.artifacts/pytest-report.xml`, `.artifacts/coverage.xml`, summary   |
| **Tests** (`tests.yml`)                                | Lightweight Python + web test matrix (quicker than full CI)                                                                             | same as CI or narrowed to `tests/**`                                                          | `pytest-web-configs.xml` (when targeted), coverage (if `pytest-cov`) |
| **Web Config Validate** (`web-config-validate.yml`)    | `jq` JSON lint; `$schema` validation; explicit `web/app.config.json` / `web/layers.json`; targeted pytest                               | `web/app.config.json`, `web/layers.json`, `web/config/**/*.json`, `tests/test_web_configs.py` | step summaries; `pytest-web-configs.xml`                             |
| **STAC Validate** (`stac-validate.yml`)                | `stac-validator` (recursive if `stac/catalog.json`) → `pystac` fallback; HTTP(S) link checks; local asset existence + optional checksum | `stac/**`                                                                                     | `.artifacts/stac_validator.txt`                                      |
| **STAC & Config** (`stac.yml`)                         | Validate STAC (+ checksum pass); **render** `web/app.config.json` via `kgt` CLI or module fallback; schema-check rendered config        | `stac/**`, `src/**`, `web/**`, deps                                                           | `.artifacts/stac_report.json`, `web/app.config.json`                 |
| **STAC Validate & Badges** (`stac-badges.yml`)         | Validate STAC → produce per-source Shields endpoint JSONs                                                                               | `stac/**`, `data/sources/**`, `scripts/**`                                                    | `web/badges/*.json`, `build/stac_report.json`, run summary           |
| **Site** (`site.yml`)                                  | Build & deploy **MapLibre** site to GitHub Pages; optional MkDocs `/docs`; Lychee link check                                            | `web/**`, `stac/**`, `data/sources/**`, `mkdocs.yml`                                          | `_site/` artifact (Pages), link-check summary                        |
| **SBOM** (`sbom.yml`)                                  | Generate **CycloneDX/SPDX** for repo and (if `Dockerfile`) image; attest; **Grype** SARIF                                               | Manual, weekly, pushes                                                                        | `artifacts/sbom/**`, SARIF uploads                                   |
| **Docker Build & Publish** (`docker.yml`)              | Multi-arch **Buildx** to GHCR (edge/semver/latest); SBOM + provenance; Trivy SARIF; PRs build but don’t push                            | `Dockerfile`, `docker/**`, plus `web/**`, `stac/**` when included                             | Pushed image (main/tags), `trivy-image.sarif`                        |
| **CodeQL** (`codeql.yml`)                              | Security/quality analysis for **Python** and **JS/TS** (autobuild; optional local config)                                               | Push/PR to `main`, weekly                                                                     | Code Scanning results                                                |
| **Trivy** (`trivy.yml`)                                | Filesystem + config + image scans; SARIF to Code Scanning; Cdx/SPDX SBOM                                                                | Push/PR/scheduled                                                                             | `trivy-*.sarif`, `sbom.cdx.json`, `sbom.spdx.json`                   |
| **Secret Scanning (Gitleaks)** (`secret-scanning.yml`) | Detects secrets in PR diffs and full repo; SARIF to Code Scanning                                                                       | Push/PR/scheduled                                                                             | `gitleaks.sarif`                                                     |
| **OpenSSF Scorecard** (`ossf-scorecard.yml`)           | Repo health checks; SARIF + optional publish to OpenSSF                                                                                 | Push/PR/weekly                                                                                | `scorecard.sarif`                                                    |
| **Release** (`release.yml`)                            | Tag-driven build (**sdist+wheel**); tag↔version gate; smoke import; checksums; optional SBOMs; **GitHub Release**                       | Tags `v*`, manual                                                                             | `dist/**`, `CHECKSUMS.txt` (release assets)                          |
| **Roadmap Sync** (`roadmap.yml`)                       | Parse `.github/roadmap/roadmap.yaml` → labels/milestones/issues; **DRY_RUN on PRs/forks**                                               | Roadmap files, sync script                                                                    | `build/roadmap-sync.log`, `build/plan.json`                          |
| **Link Check** *(optional)* (`link-check.yml`)         | **Lychee** over README/`docs/`/`web/`; PR-diff mode; honors `.lychee.toml`                                                              | README, `docs/**`, `web/**`                                                                   | `lychee.md`, `lychee/results.json`                                   |
| **Automerge** (`automerge.yml`)                        | Label-gated auto-merge once required checks pass (squash, branch delete)                                                                | PR with `automerge`                                                                           | —                                                                    |
| **Labels Sync** (`labels.yml`)                         | Sync labels from `.github/labels.yml`                                                                                                   | Push to `.github/labels.yml`, manual                                                          | —                                                                    |
| **Close Stale** (`close-stale.yml`)                    | Mark/close inactive issues & PRs with exemptions                                                                                        | nightly, manual                                                                               | bot comments                                                         |
| **Issue Lock** (`issue-lock.yml`)                      | Lock closed issues/PRs after inactivity                                                                                                 | nightly, manual                                                                               | bot comments                                                         |
| **PR Auto Labeler** (`pr-labeler.yml`)                 | Labels by paths via `.github/labeler.yml`, size, docs/tests-only, Dependabot                                                            | PR open/update                                                                                | labels                                                               |
| **PR Size Labels** (`size-label.yml`)                  | Adds `size/XS`→`size/XL` based on changed lines                                                                                         | PR open/update                                                                                | labels                                                               |
| **Greetings** (`greetings.yml`)                        | Welcome first-time issues & PRs                                                                                                         | issue/PR open                                                                                 | bot comments                                                         |

> **Permissions & safety:** Every workflow requests **only what it needs**.
> Anything that **writes** (Pages, GHCR, Releases, Roadmap) **skips** on PRs or runs **DRY**.

---

## How they connect

```mermaid
flowchart TD
  A["Push/PR"] --> B["web-config-validate.yml\n(\"JSON lint\" + schema)"]
  A --> C["stac-validate.yml\n(\"stac-validator\" → \"pystac\")"]
  A --> D["ci.yml / tests.yml\n(\"pytest\", \"ruff\", web)"]
  C --> E["stac.yml\n(\"render app.config.json\")"]
  E --> F["site.yml\n(\"build + Pages + link check\")"]
  A --> G["docker.yml\n(\"buildx\" → GHCR)"]
  A --> H["codeql.yml\n(\"security\")"]
  A --> I["sbom.yml\n(\"CycloneDX/SPDX + attest\")"]
  A --> M["stac-badges.yml\n(\"validate\" → badges)"]
  A --> S["trivy.yml\n(\"fs/config/image scans + SBOM\")"]
  A --> T["secret-scanning.yml\n(\"Gitleaks\")"]
  A --> U["ossf-scorecard.yml\n(\"repo health\")"]
  J["Tag vX.Y.Z"] --> K["release.yml\n(\"sdist+wheel+SBOM\" → Release)"]
  L["roadmap.yml\n(\"dry-run on PRs\")"] -. "manual/push" .-> L
```

> ⚠️ **Mermaid on GitHub is picky** — *quote labels that contain punctuation* and use `\n` for line breaks.

---

## Conventions we follow

* **Least-privilege:** workflows set only the permissions they require (e.g., `packages: write` only in image publishers).
* **Concurrency guards:** `concurrency: { group: "${{ github.workflow }}-${{ github.ref }}", cancel-in-progress: true }` to prevent overlapping runs per ref.
* **Caching:**

  * Python via `actions/setup-python` keyed to `pyproject.toml` / `requirements*.txt`
  * Node via lockfiles (`package-lock.json`, `yarn.lock`, `pnpm-lock.yaml`)
  * Docker Buildx via `cache-from`/`cache-to: gha`
  * Trivy/Gitleaks/Scorecard DBs via `actions/cache`
* **Geo stacks:** CI auto-detects heavy GIS deps and installs GDAL/PROJ/SpatiaLite **only when needed**.
* **Schema-first:** JSON/YAML configs lint early with `jq` / `jsonschema` / `ajv` (for roadmap) to **fail fast**.
* **PR safety:** labeler/automerge only act when gated (`automerge`, `no-automerge`, `wip`, etc.); all writers are PR-safe.

---

## Common tasks

* **Add a web layer** → update STAC → **`stac.yml`** re-validates & renders `web/app.config.json` → **`site.yml`** publishes to Pages.
* **Release a package** → tag `vX.Y.Z` → **`release.yml`** builds wheels/sdists, creates SBOMs & checksums → uploads to GitHub Release.
* **Surface STAC health** → **`stac-badges.yml`** writes `web/badges/*.json` for Shields endpoints (overall + per-source).
* **Harden security** → **`trivy.yml`** + **`secret-scanning.yml`** + **`codeql.yml`** + **`ossf-scorecard.yml`** create a defense-in-depth baseline.
* **Keep labels tidy** → edit `.github/labels.yml` → **`labels.yml`** syncs; **`close-stale.yml`** + **`issue-lock.yml`** handle lifecycle.

---

## Troubleshooting quick hits

* **Mermaid errors** → quote labels and use `\n` for newlines (see diagram above).
* **GDAL build failures** → keep the system-GDAL step; pin `rasterio/fiona` to known-good combos if wheels lag.
* **STAC validation flakes** → if `stac-validator` struggles with remotes, prefer local assets; link checks run separately in `stac-validate.yml`.
* **Pages deploy empty** → ensure site build writes to `_site/`; `site.yml` fails if dir is empty.
* **Docker context gotcha** → if `docker/Dockerfile` expects `docker/` as context, set `context: docker/` in `docker.yml`.
* **Security SARIF not visible** → verify workflow `permissions.security-events: write` and that SARIF path matches upload step.

---

## Next steps (suggested)

* Enable **branch protection** to require **CI**, **Web Config Validate**, **STAC Validate**, **CodeQL**, **Trivy**, and **Secret Scanning** before merge.
* Enable **automerge** for Dependabot minor/patch when checks pass (label-gated).
* Add **PR review annotations** for STAC/schema errors via review comments for faster triage.

---

With these workflows, every commit is validated, configs are schema-checked, STAC stays standards-compliant, security is continuous, artifacts are reproducible, and deploys are push-button. 🚀
