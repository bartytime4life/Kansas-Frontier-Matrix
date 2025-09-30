# Kansas-Frontier-Matrix — GitHub Workflows

Automation for **CI/CD, validation, security, and release**.
Every workflow is **scoped, cached, concurrent-safe, and least-privilege**.

> **Principles**
>
> * **Fail fast** (lint, schema, STAC) before heavy work.
> * **Reproducible** (pinned tools, caches, artifact logs).
> * **Auditable** (SBOMs, SARIF, run summaries, provenance labels).

---

## Index (what runs where)

| Workflow                                               | Purpose                                                                             | Key triggers (paths)                                        | Outputs / artifacts                                  |
| ------------------------------------------------------ | ----------------------------------------------------------------------------------- | ----------------------------------------------------------- | ---------------------------------------------------- |
| **CI** (`ci.yml`)                                      | Python lint/tests (ruff/pytest), optional mypy; light web build smoke               | `src/**`, `tests/**`, `pyproject.toml`, `requirements*.txt` | JUnit/coverage in `.artifacts/`, run summary         |
| **Tests** (`tests.yml`)                                | Quick test matrix (faster than full CI)                                             | `tests/**`                                                  | `pytest-report.xml`, coverage (if enabled)           |
| **Web Config Validate** (`web-config-validate.yml`)    | JSON lint + `$schema` validate; targeted pytest for web configs                     | `web/**.json`, `web/config/**/*.json`, `tests/**`           | `pytest-web-configs.xml`, step summaries             |
| **STAC Validate** (`stac-validate.yml`)                | `stac-validator` (recursive) → `pystac` fallback; HTTP link checks; asset existence | `stac/**`                                                   | `.artifacts/stac_validator.txt`, broken-link list    |
| **STAC & Config Render** (`stac.yml`)                  | Validate STAC, then render `web/app.config.json`; schema-check rendered config      | `stac/**`, `src/**`, `web/**`                               | `.artifacts/stac_report.json`, `web/app.config.json` |
| **STAC Badges** (`stac-badges.yml`)                    | Validate STAC → produce Shields-ready JSON badge payloads                           | `stac/**`, `data/sources/**`                                | `web/badges/*.json`, `build/stac_report.json`        |
| **Site (Pages)** (`site.yml`)                          | Build & deploy MapLibre site to GitHub Pages; optional MkDocs; Lychee link check    | `web/**`, `stac/**`, `mkdocs.yml`                           | `_site/` artifact → Pages                            |
| **Docker Build & Publish** (`docker.yml`)              | Multi-arch Buildx → GHCR; SBOM & provenance; Trivy image scan                       | `docker/**`, `Dockerfile`                                   | Image (tags), `trivy-image.sarif`                    |
| **SBOM** (`sbom.yml`)                                  | CycloneDX/SPDX for repo (and image if present); attest                              | push/schedule/manual                                        | `artifacts/sbom/**`                                  |
| **CodeQL** (`codeql.yml`)                              | Static analysis (Python, JS/TS)                                                     | push/PR to `main`, weekly                                   | Code scanning alerts                                 |
| **Trivy** (`trivy.yml`)                                | FS/config/image scans; SBOMs; SARIF                                                 | push/PR/schedule                                            | `trivy-*.sarif`, `sbom.*.json`                       |
| **Secret Scanning (Gitleaks)** (`secret-scanning.yml`) | Secrets in diffs & history; SARIF                                                   | push/PR/schedule                                            | `gitleaks.sarif`                                     |
| **OpenSSF Scorecard** (`ossf-scorecard.yml`)           | Repo health checks                                                                  | push/PR/weekly                                              | `scorecard.sarif`                                    |
| **Release** (`release.yml`)                            | Tag-driven build (sdist+wheel); checksums; optional SBOM; GitHub Release            | tags `v*`                                                   | `dist/**`, `CHECKSUMS.txt`                           |
| **Roadmap Sync** (`roadmap.yml`)                       | Parse `.github/roadmap/roadmap.yaml` → labels/milestones/issues                     | roadmap changes/manual                                      | `build/roadmap-sync.log`                             |
| **Labels Sync** (`labels.yml`)                         | Sync labels from `.github/labels.yml`                                               | push/manual                                                 | —                                                    |
| **Automerge** (`automerge.yml`)                        | Label-gated auto-merge once checks pass                                             | PR labeled `automerge`                                      | —                                                    |
| **Close Stale** (`close-stale.yml`)                    | Mark/close inactive issues/PRs                                                      | nightly/manual                                              | bot comments                                         |
| **Issue Lock** (`issue-lock.yml`)                      | Lock closed issues after inactivity                                                 | nightly/manual                                              | bot comments                                         |
| **PR Labeler** (`pr-labeler.yml`)                      | Path/size/docs/test/Dependabot labels                                               | PR open/sync                                                | labels                                               |
| **Link Check** *(optional)* (`link-check.yml`)         | Lychee over `README`/`docs`/`web`                                                   | push/PR                                                     | `lychee.md`, `results.json`                          |

> **Safety:** Writers (Pages, GHCR, Releases) **skip on PRs** or run **DRY**. Each workflow sets **minimal `permissions:`**.

---

## How workflows connect

```mermaid
flowchart TD
  A["Push / PR"] --> B["web-config-validate.yml\nJSON lint and schema"]
  A --> C["stac-validate.yml\nstac-validator and pystac with link checks"]
  A --> D["ci.yml / tests.yml\nruff and pytest (mypy optional)"]
  C --> E["stac.yml\nrender app.config.json"]
  E --> F["site.yml\nbuild and deploy to Pages"]
  A --> G["docker.yml\nbuildx to GHCR with Trivy"]
  A --> H["codeql.yml\nstatic analysis"]
  A --> I["sbom.yml\nCycloneDX or SPDX with attest"]
  A --> J["stac-badges.yml\nShields JSON badges"]
  K["Tag vX.Y.Z"] --> L["release.yml\nsdist wheel checksums"]

<!-- END OF MERMAID -->

---

## Reusable patterns (copy-paste ready)

### 1) Concurrency guard (no overlapping per ref)

```yaml
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true
```

### 2) Least-privilege permissions

```yaml
permissions:
  contents: read
  actions: read
  security-events: write   # only if uploading SARIF
  pages: write             # only in site.yml deploy job
  id-token: write          # only for OIDC publish (e.g., GHCR attest)
  packages: write          # only in docker.yml on default branch
```

### 3) Python + caches (ruff/pytest)

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
          cache: 'pip'
          cache-dependency-path: |
            requirements*.txt
            pyproject.toml
      - run: pip install -r requirements.txt
      - run: ruff check .
      - run: pytest -q --maxfail=1 --disable-warnings
```

### 4) JSON schema validation (web/STAC/config)

```yaml
- name: JSON lint
  run: jq -e . web/app.config.json > /dev/null
- name: Schema validate
  run: python -m jsonschema -i web/app.config.json web/schema/app.schema.json
```

### 5) STAC validate (local-first; robust)

```yaml
- name: stac-validator (recursive)
  run: stac-validator --recursive stac/catalog.json | tee .artifacts/stac_validator.txt
- name: pystac fallback
  run: python -m scripts.stac_fallback_validate stac/catalog.json
```

### 6) Pages deploy (safe on PRs)

```yaml
permissions:
  contents: read
  pages: write
  id-token: write
# …
- uses: actions/upload-pages-artifact@v3
  with: { path: _site }
- uses: actions/deploy-pages@v4
  if: github.ref == 'refs/heads/main' && github.event_name != 'pull_request'
```

### 7) Docker Buildx with cache + provenance

```yaml
- uses: docker/setup-buildx-action@v3
- uses: docker/login-action@v3
  if: github.ref == 'refs/heads/main'
  with:
    registry: ghcr.io
    username: ${{ github.actor }}
    password: ${{ secrets.GITHUB_TOKEN }}
- uses: docker/build-push-action@v6
  with:
    context: .
    file: docker/Dockerfile
    platforms: linux/amd64,linux/arm64
    push: ${{ github.ref == 'refs/heads/main' }}
    provenance: true
    tags: ghcr.io/${{ github.repository }}:edge
    cache-from: type=gha
    cache-to: type=gha,mode=max
```

### 8) Trivy + SARIF

```yaml
permissions: { contents: read, security-events: write }
- uses: aquasecurity/trivy-action@0.24.0
  with:
    scan-type: fs
    format: sarif
    output: trivy-fs.sarif
- uses: github/codeql-action/upload-sarif@v3
  with: { sarif_file: trivy-fs.sarif }
```

---

## Conventions we enforce

* **Schema-first:** JSON/YAML configs are linted and schema-validated before builds.
* **Geo deps on demand:** GDAL/PROJ/SpatiaLite installed only for jobs that need them.
* **Cache discipline:** Python/Node/Docker caches keyed to lockfiles & requirements.
* **Artifacts always:** Tests, STAC reports, and config renders land in `./.artifacts` (or `_site/` for deployables).
* **Branch safety:** Anything that writes (Pages, GHCR, Releases) is gated to default branch/tags and **never runs on PRs** with write perms.
* **Run summaries:** Jobs print a concise “What changed / What was validated / Next steps” in the step summary.

---

## Typical developer flows

* **Add/modify a web layer** → push changes to `stac/**` and `web/config/**`
  → `web-config-validate.yml` and `stac-validate.yml` fail fast
  → `stac.yml` re-renders `web/app.config.json`
  → `site.yml` publishes to Pages (main only).

* **Touch STAC items** → `stac-validate.yml` + `stac-badges.yml` run; badges JSON updated under `web/badges/`.

* **Release a Python package** → tag `vX.Y.Z` → `release.yml` builds sdist/wheel with checksums (+ optional SBOM) and creates a GitHub Release.

* **Harden security posture** → `trivy.yml` + `secret-scanning.yml` + `codeql.yml` + `ossf-scorecard.yml` provide defense-in-depth with SARIF surfaced in **Code scanning**.

---

## Troubleshooting (fast answers)

* **Mermaid errors in README** → Quote any node text with punctuation and use `\n` for newlines (see diagram above).
* **Pages deploys empty** → Ensure the site job writes to `_site/`; the deploy step uploads that directory.
* **STAC link flakiness** → Prefer validating local assets (relative `href`) in CI; remote HTTP checks can be toggled behind a flag.
* **GHCR push denied on PR** → Expected; publishers only push on default branch with `packages: write`.
* **SARIF missing in Security tab** → Ensure `permissions.security-events: write` and correct path in upload step.
* **Long CI due to caches** → Bump cache keys only when lockfiles/requirements change; avoid noisy cache misses.

---

## Governance & guardrails

* Protect `main` to require: **CI**, **Web Config Validate**, **STAC Validate**, **CodeQL**, **Trivy**, and **Secret Scanning**.
* Use `automerge` label for Dependabot minor/patch once required checks pass.
* Keep `.github/labels.yml`, `.github/labeler.yml`, and `.github/roadmap/roadmap.yaml` as the **source of truth** for planning and PR hygiene.

---

## File map (this folder)

```
.github/workflows/
├── ci.yml
├── tests.yml
├── web-config-validate.yml
├── stac-validate.yml
├── stac.yml
├── stac-badges.yml
├── site.yml
├── docker.yml
├── sbom.yml
├── codeql.yml
├── trivy.yml
├── secret-scanning.yml
├── ossf-scorecard.yml
├── release.yml
├── roadmap.yml
├── labels.yml
├── automerge.yml
├── close-stale.yml
├── issue-lock.yml
├── pr-labeler.yml
├── link-check.yml              # optional
└── README.md                   # (this file)
```

---

## Glossary

* **STAC** — SpatioTemporal Asset Catalog (1.0.0): standard metadata for geospatial assets.
* **SARIF** — Static Analysis Results Interchange Format (security reports).
* **SBOM** — Software Bill of Materials (CycloneDX/SPDX).
* **GHCR** — GitHub Container Registry.
* **Pages** — GitHub Pages static site hosting (`_site/` artifact).

---

**Questions or improvements?** Open an issue with `[workflows]` in the title and include a failing run URL plus the changed paths.
