# 🧰 `.github/workflows/` — CI/CD + Data Promotion Gates for Kansas Frontier Matrix (KFM)

[![CI](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/ci.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/ci.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml)
[![Pages](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pages.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pages.yml)

> 🧩 This folder contains GitHub Actions workflows that keep KFM **buildable**, **testable**, **secure**, and **shippable** — from **geospatial ETL + STAC catalogs** to the **MapLibre/Cesium web viewer**.

> [!IMPORTANT]
> ✅ **KFM CI/CD principle:** workflows follow the platform’s system order → **ETL → Catalogs → Graph → API → UI**, with **governance + security gates** throughout.

> [!NOTE]
> This README is both a **map** *and* a **spec**. If a workflow file doesn’t exist yet, consider the sections below the intended blueprint for adding it cleanly. 🧱✨

---

## ⚡ Quick links

- ✅ All Actions runs → https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions
- 🐛 Open issues → https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues
- 🔐 Security policy → [`../SECURITY.md`](../SECURITY.md)
- 🤝 Collaboration hub → [`../README.md`](../README.md) *(the `.github/` README)*
- 🧪 Workflow dispatch (manual runs) → https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows

> [!TIP]
> If a badge 404s, that workflow file probably doesn’t exist yet — or it was renamed. Update the badge + this README together so the repo stays “single source of truth.” ✅

---

<details>
<summary><b>🧭 Table of contents</b></summary>

- [📦 The workflow philosophy](#-the-workflow-philosophy)
- [🗺️ Workflow lanes](#️-workflow-lanes)
- [📁 What lives here](#-what-lives-here)
- [🗂️ Workflow catalog](#️-workflow-catalog-recommended-baseline)
- [✅ Quality gates](#-quality-gates-what-must-pass)
- [🧾 Data contracts & catalog gates](#-data-contracts--catalog-gates-stac--links)
- [🧪 Integration tests with PostGIS](#-integration-tests-with-postgis--optional-neo4j)
- [🌐 Web UI lane](#-web-ui-lane-maplibre--cesium-story-nodes)
- [🐳 Docker builds](#-docker-builds-caching--multi-arch)
- [🔐 Security scanning](#-security-scanning-code--deps--supply-chain)
- [📦 Artifacts & reporting](#-artifacts--reporting)
- [🧷 Secrets & environments](#-secrets--environments-keep-it-boring)
- [🧼 Workflow hygiene](#-workflow-hygiene-do-this-everywhere)
- [🛠️ Starter templates](#️-starter-templates-copy--paste)
- [🧰 Debug locally](#-debugging-workflows-locally)
- [🧾 New workflow checklist](#-adding-a-new-workflow-checklist)
- [📚 References](#-references-for-this-folder)

</details>

---

## 📦 The workflow philosophy

KFM isn’t “just an app” — it’s a **data + provenance + visualization system**. That means CI/CD must validate *more than code*:

- ✅ Code correctness (lint, unit tests, types)
- ✅ Data correctness (schemas, STAC required fields, link health, CRS/projection rules)
- ✅ Governance (licenses, provenance, “no secrets”, ethics constraints)
- ✅ Reproducibility (pinned environments, build metadata artifacts, deterministic steps)
- ✅ Shipping (containers, releases, Pages deploy)

> [!IMPORTANT]
> **CI is a safety rail, not a ritual.** If a check doesn’t prevent real breakage, remove it.  
> If a check prevents breakage but takes too long, move it to **nightly** or **manual dispatch**. 🛣️

---

## 🗺️ Workflow lanes

KFM uses multiple lanes so we don’t build a single “mega workflow” that’s slow, flaky, and impossible to debug.

| Lane | Runs when | Goal 🎯 | Typical workflows |
|---|---|---|---|
| 🧪 **PR lane (fast)** | `pull_request` | Catch breakage quickly | `ci.yml`, `catalog-qa.yml`, `codeql.yml` |
| 🟢 **Main lane (promote)** | `push` to `main` | Build artifacts we ship | `docker.yml`, `pages.yml`, `release-draft.yml` |
| 🗓️ **Nightly/weekly** | `schedule` | Heavy validation + regression | `integration.yml`, `data-refresh.yml`, `e2e.yml` |
| 🏷️ **Release lane** | tags `v*` | Package + sign + publish | `release.yml`, `docker.yml` |
| 🧰 **Manual** | `workflow_dispatch` | On-demand runs | `integration.yml`, `data-refresh.yml`, `catalog-qa.yml` |

---

## 📁 What lives here

```text
📁 .github/workflows/
├─ 🧪 ci.yml                      # fast PR lane: lint + unit tests + typecheck (code + docs)
├─ 🧾 catalog-qa.yml              # STAC quick gate: required fields + top-level link checks
├─ 🧬 integration.yml             # PostGIS (+ optional Neo4j) integration tests (nightly/dispatch)
├─ 🌐 web.yml                     # web UI build/tests (MapLibre + Story Nodes + Cesium)
├─ 🔎 e2e.yml                     # Playwright/Selenium end-to-end (nightly/dispatch)
├─ 🔐 codeql.yml                  # SAST (CodeQL)
├─ 🧯 dependency-review.yml        # PR dependency review (recommended)
├─ 🔐 security.yml                # container scan + secret scan helpers + policy gates (optional)
├─ 🐳 docker.yml                  # build/push images (optional until you ship containers)
├─ 🧾 attest.yml                  # cosign/SBOM/attestations (optional but 🔥)
├─ 📚 docs.yml                    # docs build + link checks (optional)
├─ 🗺️ data-refresh.yml            # scheduled ETL refresh / catalog rebuild (optional)
├─ 🏷️ release.yml                 # release packaging/changelog (optional)
├─ 🌐 pages.yml                   # GitHub Pages deploy (optional)
└─ 📄 README.md                   # you are here 👋
```

> [!NOTE]
> If you only implement **three** workflows to start, make them:
> 1) `ci.yml` ✅  
> 2) `catalog-qa.yml` 🧾  
> 3) `codeql.yml` 🔐

---

## 🗂️ Workflow catalog (recommended baseline)

| Workflow 📄 | Protects ✅ | Triggers ⏱️ | Outputs 📦 |
|---|---|---|---|
| `ci.yml` | code quality + unit tests + type checks + doc/config lint | PRs, pushes | junit/coverage, logs |
| `catalog-qa.yml` | STAC catalog health (required fields + link checks) | PRs touching `data/**`, dispatch | QA logs |
| `integration.yml` | DB/service integration boundaries | nightly, dispatch | integration logs + reports |
| `web.yml` | MapLibre/Cesium web build + unit tests | PRs touching `web/**`, pushes | built artifact |
| `e2e.yml` | user-flow tests (UI + API) | nightly, dispatch | videos/screenshots |
| `codeql.yml` | static analysis | PRs, schedule | SARIF |
| `dependency-review.yml` | dependency drift checks | PRs | PR annotations |
| `security.yml` | container scan glue + policy checks | schedule, dispatch | SARIF/scan logs |
| `docker.yml` | build/push images | `main`, tags | OCI images |
| `attest.yml` | SBOM + signing/attestations | `main`, tags | SBOM + attestations |
| `docs.yml` | docs build/link checks | PRs | built docs artifact |
| `pages.yml` | deploy viewer/docs | `main`, dispatch | Pages deploy |
| `release.yml` | release packaging | tags | release assets |

> [!TIP]
> Use **path filters** so PR lane jobs only run when they matter (example: only run `catalog-qa.yml` when `data/**` changes). This keeps CI fast and contributor-friendly. 🌱

---

## ✅ Quality gates (what must pass)

### 1) Code & config health 🧼
- Formatting + linting (fast fail)
- Unit tests (core logic first)
- Type checks (where applicable)
- JSON/YAML validity (configs, catalogs, metadata)

### 2) Contract-first boundaries 🧾
KFM treats interfaces as contracts:
- API contracts (OpenAPI/GraphQL, if present)
- “Data contracts” for catalogs + metadata (STAC/DCAT/PROV patterns)
- Build artifacts should include metadata: versions + checksums (traceability)

### 3) Governance gates 🧭
- License/provenance fields present for datasets
- Ethics constraints applied when relevant
- “No secrets” checks (and GitHub secret scanning enabled)

> [!IMPORTANT]
> **If CI fails, we don’t merge.**  
> Broken main breaks everyone. 🤖🚫

---

## 🧾 Data contracts & catalog gates (STAC + links)

KFM catalogs are discoverability infrastructure — if they drift, everything breaks downstream (indexing, browsing, automation, UI layer toggles).

### ✅ Minimum “fast gate” for STAC (high ROI)
A single fast workflow should verify:
- `license` is present + non-empty  
- `providers` is present + non-empty array  
- `stac_extensions` is present (warn if empty)  
- Root/collection `links[].href` respond (HEAD/GET)

> [!TIP]
> Keep this fast gate small + strict. Run heavier schema validation in a nightly lane.

### 🧭 Projection + CRS rules (STAC `proj:`)
For geo integrity, treat CRS metadata as a contract:
- Require `proj:code` (EPSG) on items/collections that represent spatial assets
- Encourage explicit `stac_extensions` schema URIs
- Prefer Stable STAC extensions for “production catalogs” (warn on Proposal/Pilot)

---

## 🧪 Integration tests with PostGIS (+ optional Neo4j)

KFM’s spatial correctness depends on real spatial query engines. Integration tests should run against **real** PostGIS containers.

### Option A: GitHub Actions service container ✅
```yaml
services:
  db:
    image: postgis/postgis:15-3.4
    env:
      POSTGRES_DB: kfm_test
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
    ports:
      - 5432:5432
    options: >-
      --health-cmd="pg_isready -U postgres -d kfm_test"
      --health-interval=10s
      --health-timeout=5s
      --health-retries=10
```

### Option B: Compose parity (multi-service) 🐳
Use Compose when you also need API + worker + cache + graph DB.

> [!CAUTION]
> The #1 source of CI flake is “tests started before DB was ready.”  
> Always use health checks + explicit waits. ✅

---

## 🌐 Web UI lane (MapLibre + Cesium Story Nodes)

KFM’s UI is not “just a map” — it’s also narrative + 2D/3D context. Keep CI aligned with that reality.

### 🧩 Story Nodes (2D → 3D → 2D)
Recommended shape (non-disruptive):

```text
🌐 web/
├─ 🧭 story_nodes/
│  └─ kansas_from_above/
│     ├─ config.json
│     ├─ cesium_scene.js
│     └─ narrative.md
├─ 🗺️ viewers/
│  ├─ maplibre/
│  └─ cesium/
│     └─ bootstrap.js
└─ 🎛️ assets/
   └─ tiles/
```

### ✅ Web workflow expectations
- Install deps with lockfiles (`npm ci` / `pnpm i --frozen-lockfile`)
- Unit tests for UI logic
- Build step produces a deterministic `dist/` (or equivalent)
- (Optional) Playwright E2E on nightly to avoid slowing PRs

> [!TIP]
> Treat 3D assets as **untrusted input**. If your viewer loads external tiles/models, validate + constrain origins and parse steps.

---

## 🐳 Docker builds: caching + multi-arch

### ✅ Prefer BuildKit + GHA cache
```yaml
- uses: docker/setup-buildx-action@v3

- uses: docker/build-push-action@v6
  with:
    context: .
    push: true
    tags: ghcr.io/${{ github.repository }}:${{ github.sha }}
    cache-from: type=gha
    cache-to: type=gha,mode=max
```

### 🧪 Multi-version compatibility via matrix
```yaml
strategy:
  matrix:
    python: ["3.11", "3.12"]
```

> [!NOTE]
> Build environments should be reproducible. If you use Conda/Mamba locally, mirror that in CI (or build inside Docker). 🔁

---

## 🔐 Security scanning (code + deps + supply chain)

Baseline expectations:
- ✅ dependency review on PRs
- ✅ CodeQL (SAST)
- ✅ secret scanning (and push protection)
- ✅ container image scanning on `main` + tags *(recommended once containers exist)*

### 🔏 Artifact trust (optional but 🔥)
Once you ship containers or data artifacts:
- generate SBOMs
- sign images/artifacts
- attach attestations (provenance)

> [!CAUTION]
> Avoid secrets on untrusted PRs from forks. Keep publish/sign steps on:
> - `push` to `main`
> - tags
> - protected environments
> - `workflow_dispatch`

---

## 📦 Artifacts & reporting

Standardize artifacts so debugging is easy:

- `unit-test-results.xml` / `pytest.xml`
- `coverage.xml` (+ HTML optional)
- integration logs (zipped)
- security reports (SARIF)
- build metadata: versions + checksums (traceability)

💡 Naming tip: include workflow + sha → `ci-unit-${{ github.sha }}`

---

## 🧷 Secrets & environments (keep it boring)

Common secrets:
- `GITHUB_TOKEN` (often enough for GHCR with `packages: write`)
- Deploy credentials (only in protected environments)
- Third-party tokens (Earth Engine, map tiles, etc.), scoped + rotated

✅ Use GitHub **Environments** (`dev`, `stage`, `prod`) to:
- scope secrets safely
- require approvals for prod
- attach deploy history to commits

---

## 🧼 Workflow hygiene (do this everywhere)

### 🔏 Minimal permissions by default
```yaml
permissions:
  contents: read
```

Common upgrades:
- Push images:
  ```yaml
  permissions:
    contents: read
    packages: write
  ```
- Upload SARIF:
  ```yaml
  permissions:
    security-events: write
  ```

### 🧵 Concurrency (avoid dogpiling)
```yaml
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true
```

### 📌 Pin action versions
At minimum, pin major versions. For maximum safety, pin commit SHAs.

---

## 🛠️ Starter templates (copy / paste)

> Keep PR checks fast, make slow lanes scheduled, and always upload logs on failure. 🥇

<details>
<summary><strong>🧪 <code>ci.yml</code> — Fast PR Lane (lint + unit tests + typecheck)</strong></summary>

```yaml
name: CI

on:
  pull_request:
  push:
    branches: [main]

permissions:
  contents: read

concurrency:
  group: ci-${{ github.ref }}
  cancel-in-progress: true

jobs:
  python:
    name: 🐍 Python — lint + unit tests
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
          cache: "pip"

      - name: Install deps
        run: |
          python -m pip install -U pip
          # Adjust to your repo (requirements.txt / pyproject.toml)
          pip install -r requirements.txt -r requirements-dev.txt

      - name: Lint
        run: |
          ruff check .
          ruff format --check .

      - name: Unit tests
        run: |
          pytest -q --junitxml=unit-test-results.xml --cov=. --cov-report=xml

      - name: Upload test artifacts
        uses: actions/upload-artifact@v4
        if: always()
        with:
          name: python-unit-artifacts
          path: |
            unit-test-results.xml
            coverage.xml

  web:
    name: 🌐 Web — build + tests (optional)
    runs-on: ubuntu-latest
    if: ${{ hashFiles('web/package.json') != '' }}
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-node@v4
        with:
          node-version: "20"
          cache: "npm"
          cache-dependency-path: web/package-lock.json

      - name: Install
        working-directory: web
        run: npm ci

      - name: Test
        working-directory: web
        run: npm test --if-present

      - name: Build
        working-directory: web
        run: npm run build --if-present

      - uses: actions/upload-artifact@v4
        if: always()
        with:
          name: web-build
          path: |
            web/dist
```
</details>

<details>
<summary><strong>🧾 <code>catalog-qa.yml</code> — STAC Quick Gate (fields + link checks)</strong></summary>

```yaml
name: Catalog QA (STAC quick gate)

on:
  pull_request:
    paths:
      - "data/**"
      - "tools/validation/catalog_qa/**"
  workflow_dispatch: {}

permissions:
  contents: read

jobs:
  qa:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Run catalog QA
        run: |
          python tools/validation/catalog_qa/run_catalog_qa.py \
            --root data/ \
            --glob "**/collection.json" \
            --fail-on-warn
```
</details>

<details>
<summary><strong>🧬 <code>integration.yml</code> — PostGIS Integration Tests (nightly/dispatch)</strong></summary>

```yaml
name: Integration

on:
  workflow_dispatch:
  schedule:
    - cron: "0 4 * * *" # daily @ 04:00 UTC (adjust)

permissions:
  contents: read

jobs:
  postgis-integration:
    runs-on: ubuntu-latest

    services:
      db:
        image: postgis/postgis:15-3.4
        env:
          POSTGRES_DB: kfm_test
          POSTGRES_USER: postgres
          POSTGRES_PASSWORD: postgres
        ports:
          - 5432:5432
        options: >-
          --health-cmd="pg_isready -U postgres -d kfm_test"
          --health-interval=10s
          --health-timeout=5s
          --health-retries=10

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
          cache: "pip"

      - name: Install deps
        run: |
          python -m pip install -U pip
          pip install -r requirements.txt -r requirements-dev.txt

      - name: Run integration tests
        env:
          DATABASE_URL: postgresql://postgres:postgres@localhost:5432/kfm_test
        run: |
          pytest -q -m "integration" --junitxml=integration-results.xml

      - uses: actions/upload-artifact@v4
        if: always()
        with:
          name: integration-artifacts
          path: |
            integration-results.xml
```
</details>

<details>
<summary><strong>🐳 <code>docker.yml</code> — Build + Push Images to GHCR</strong></summary>

```yaml
name: Docker

on:
  push:
    branches: [main]
    tags:
      - "v*"

permissions:
  contents: read
  packages: write

jobs:
  build-push:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: docker/setup-qemu-action@v3
      - uses: docker/setup-buildx-action@v3

      - name: Login to GHCR
        uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Build & Push
        uses: docker/build-push-action@v6
        with:
          context: .
          push: true
          platforms: linux/amd64,linux/arm64
          tags: |
            ghcr.io/${{ github.repository }}:${{ github.sha }}
            ghcr.io/${{ github.repository }}:latest
          cache-from: type=gha
          cache-to: type=gha,mode=max
```
</details>

<details>
<summary><strong>🔐 <code>security.yml</code> — Dependency Review + CodeQL + Image Scan Hooks</strong></summary>

```yaml
name: Security

on:
  pull_request:
  schedule:
    - cron: "30 3 * * 1" # weekly (adjust)

permissions:
  contents: read
  security-events: write

jobs:
  dependency-review:
    if: github.event_name == 'pull_request'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/dependency-review-action@v4

  codeql:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: github/codeql-action/init@v3
        with:
          languages: "javascript,python"
      - uses: github/codeql-action/analyze@v3

  image-scan:
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Build image (local)
        run: docker build -t kfm:scan .
      - name: Scan image (placeholder)
        run: |
          echo "TODO: run a container scan tool (e.g., Trivy) and upload SARIF"
```
</details>

<details>
<summary><strong>🌐 <code>pages.yml</code> — GitHub Pages Deploy (static viewer)</strong></summary>

```yaml
name: Pages

on:
  push:
    branches: [main]
    paths:
      - "web/**"
      - ".github/workflows/pages.yml"

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: pages
  cancel-in-progress: true

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment:
      name: github-pages
    steps:
      - uses: actions/checkout@v4

      # Replace with your build step (or skip if web/ is static)
      - name: Build (placeholder)
        run: |
          mkdir -p dist
          cp -R web/* dist/

      - uses: actions/upload-pages-artifact@v3
        with:
          path: dist

      - uses: actions/deploy-pages@v4
```
</details>

---

## 🧰 Debugging workflows locally

Options:
- ✅ Run the same commands as CI (best parity)
- 🐳 Use Compose profiles to mimic integration dependencies
- 🧪 Use `act` to simulate GitHub Actions locally (helpful, not perfect)

---

## 🧾 Adding a new workflow (checklist)

- [ ] Name jobs after outcomes (`lint`, `unit-tests`, `catalog-qa`, `integration-tests`, `build-web`, `build-image`)
- [ ] Keep PR checks fast (aim ≤ ~10 minutes)
- [ ] Put slow jobs behind schedules or manual dispatch
- [ ] Cache dependencies and Docker layers
- [ ] Upload artifacts on failure (logs are gold 🥇)
- [ ] Pin action versions
- [ ] Avoid secrets on `pull_request` from forks
- [ ] Add minimal `permissions:` and only elevate when required
- [ ] Add `concurrency:` cancellation to reduce queue noise
- [ ] Keep the KFM order intact: **ETL → Catalogs → Graph → API → UI**
- [ ] If it touches data: include provenance + STAC/DCAT validation hooks 🧾🗺️

---

## 📚 References for this folder

> 📌 Repo convention (recommended): store reference PDFs under `docs/library/`, internal specs under `docs/specs/`, and validation scripts under `tools/validation/`.

- 🧱 Architecture + CI/CD stages → `docs/architecture/` *(see KFM comprehensive engineering design docs)*
- 🧾 Catalog QA gate → `tools/validation/catalog_qa/` + `.github/workflows/catalog-qa.yml`
- 🗺️ Data staging/catlogs (STAC/DCAT/PROV) → `data/README.md`
- 🧪 Test strategy + CI gates → `tests/README.md`
- 🔐 Security & disclosure → `.github/SECURITY.md`
- 🌐 Web viewer deployment → `web/README.md`

> 🔁 If you rename workflows or reorganize docs, update this README — it’s the “single source of truth” for CI/CD intent.