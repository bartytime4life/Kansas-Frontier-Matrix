Here’s a nicely formatted markdown version you can copy-paste into your repo docs (e.g. .github/workflows/README.md):

# Kansas-Frontier-Matrix — GitHub Workflows

This folder (`.github/workflows/`) contains all **CI/CD automation** for the project.  
Workflows are modular so each part of the repo is validated and deployed independently.

---

## At-a-glance

| Workflow | What it does | Triggers (key paths) | Outputs / Artifacts |
|----------|--------------|----------------------|---------------------|
| **CI** (`ci.yml`) | Lint (ruff autodetect), multi-Python **pytest**, optional geo deps, web test/build | Changes in `src/`, `stac/`, `data/`, `web/`, `tests/`, `pyproject.toml`, `requirements*.txt` | `pytest-report.xml`, `coverage.xml` |
| **Tests** (`tests.yml`) | Pure test matrix for Python + web (lighter/faster than full CI) | Same as CI or narrowed to `tests/**` | `pytest-report.xml`, optional coverage |
| **Web Config Validate** (`web-config-validate.yml`) | `jq` JSON syntax + `jsonschema` / `pytest -k web_configs` | `web/app.config.json`, `web/layers.json`, `web/config/**/*.json`, `tests/test_web_configs.py` | `pytest-web-configs.xml` |
| **STAC Validate** (`stac-validate.yml`) | `stac-validator` (preferred) → `pystac` fallback, plus `data/sources/**` JSON/YAML lint, runs custom `scripts/validate_*.py` | `stac/**`, `data/sources/**`, `scripts/validate_*.py`, `pyproject.toml`, `requirements*.txt` | `build/stac_report.json`, validator logs |
| **STAC & Config** (`stac.yml`) | Validates STAC, then **renders** `web/app.config.json` from STAC via `kgt` or module CLI | `stac/**`, `src/**`, `web/**`, `pyproject.toml`, `requirements*.txt` | `web/app.config.json`, `.artifacts/stac_report.json` |
| **Site** (`site.yml`) | Build & deploy static **MapLibre viewer** (and `/docs` via MkDocs) to GitHub Pages | `web/**`, `stac/**`, `data/sources/**`, `mkdocs.yml` | `_site/` Pages artifact; link-check summary |
| **SBOM** (`sbom.yml`) | Generate **CycloneDX/SPDX** for repo & (conditional) image, attest, optional **Grype** SARIF | Manual, weekly, pushes | `artifacts/sbom/**`, SARIF uploads |
| **Docker** (`docker.yml`) | Multi-arch Buildx image to **GHCR** with SBOM+provenance, Trivy scan | `Dockerfile`, `docker/**`, `web/**`, `stac/**` | GHCR image; Trivy SARIF |
| **CodeQL** (`codeql.yml`) | Security & quality analysis for **Python** and **JS/TS** | Push/PR to `main`, weekly | Code Scanning results |
| **Release** (`release.yml`) | Tag-driven build (sdist+wheel), tag↔version gate, wheel smoke test, checksums, extras, SBOM, **GitHub Release** | Tags `v*`, manual | `dist/**`, `CHECKSUMS.txt` attached to Release |
| **Link Check** *(optional)* (`link-check.yml`) | **Lychee** against Markdown/HTML; PR-diff mode; honors `.lychee.toml` | README, `docs/**`, `web/**` | `lychee.md`, `lychee/results.json` |
| **Roadmap Sync** (`roadmap.yml`) | Parse `.github/roadmap/roadmap.yaml` → labels/milestones/issues; **DRY_RUN on PRs/forks**; optional schema via AJV | Roadmap files, sync script, package files | `build/roadmap-sync.log`, `build/plan.json` |

---

## How these fit together

```mermaid
flowchart TD
  A["Push/PR"] --> B["web-config-validate.yml\n(JSON lint + schema)"]
  A --> C["stac-validate.yml\n(stac-validator → pystac)"]
  A --> D["ci.yml / tests.yml\n(pytest, ruff, web)"]
  C --> E["stac.yml\n(render app.config.json)"]
  E --> F["site.yml\n(build + Pages + link check)"]
  A --> G["docker.yml\n(buildx → GHCR)"]
  A --> H["codeql.yml\n(security)"]
  A --> I["sbom.yml\n(CycloneDX/SPDX + attest)"]
  J["Tag vX.Y.Z"] --> K["release.yml\n(sdist+wheel+SBOM → Release)"]
  L["roadmap.yml\n(dry-run on PRs)"] -. manual/push .-> L

⚠️ Mermaid on GitHub is picky — labels with punctuation must be quoted and line breaks use \n.

⸻

Conventions & tips
	•	Least-privilege: workflows request only the permissions they need (e.g., packages: write only in Docker publish).
	•	Concurrency: each workflow uses a group: guard to prevent overlapping runs on the same ref.
	•	Caching:
	•	actions/setup-python + pip cache (keyed to requirements*.txt / pyproject.toml)
	•	Node caches keyed to lockfiles (npm, yarn, pnpm)
	•	Docker Buildx uses GHA cache (cache-from/to: gha)
	•	Geo stacks: CI auto-detects heavy GIS deps and installs system packages (GDAL/PROJ/Spatialite) only when required.
	•	Schema first: JSON/YAML configs are linted early with jq / jsonschema / yamllint to fail fast.
	•	PR safety: workflows that write (Roadmap, Docker pushes, Pages deploy) either skip on PRs or run in DRY_RUN for forks.

⸻

Common tasks
	•	Add a new web layer → update STAC → stac.yml validates & renders web/app.config.json → site.yml publishes.
	•	Release a package → tag vX.Y.Z → release.yml builds wheels/sdists, SBOMs, checksums → attaches to Release.
	•	Update dependencies → see .github/dependabot.yml (grouped weekly updates for Actions, pip, npm, Docker).

⸻

Troubleshooting quick hits
	•	Mermaid errors in README → quote labels with commas/parentheses and use \n for line breaks.
	•	GDAL build failures in CI → ensure wheels are available or keep system GDAL install step enabled; pin rasterio/fiona to known-good combos.
	•	STAC validator flakes → if stac-validator rate-limits remote link checks, use local paths or add --links only on root catalog.json.

⸻

Next steps (suggested)
	•	Enable branch protection requiring CI, Web Config Validate, STAC Validate, and CodeQL to pass before merge.
	•	Add automerge workflow for Dependabot minor/patch with passing checks and label gate (e.g., automerge:minor).
	•	Add PR annotations step for STAC/schema errors (inline review comments).

⸻

🚀 With these workflows, every commit is validated, configs are schema-checked, STAC is standards-compliant, artifacts are reproducible, and deploys are push-button.

