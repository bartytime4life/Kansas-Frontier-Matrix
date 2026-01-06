# 🧰 `.github/workflows/` — CI/CD for Kansas Frontier Matrix (KFM)

[![CI](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/ci.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/ci.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml)
[![Pages](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pages.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pages.yml)

> 🧩 This folder contains GitHub Actions workflows that keep KFM **buildable**, **testable**, **secure**, and **shippable** — from geospatial pipelines to the web map UI.

> [!IMPORTANT]
> ✅ **Principle:** CI mirrors KFM’s system order → **ETL → Catalogs → Graph → API → UI** (with policy + security checks throughout).

---

## ⚡ Quick links

- ✅ All Actions runs → https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions
- 🐛 Open issues → https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues
- 🔐 Security policy → [`../SECURITY.md`](../SECURITY.md)
- 🤝 Collaboration hub → [`../README.md`](../README.md) *(the `.github/` README)*

> [!TIP]
> If a badge 404s, that workflow file probably doesn’t exist yet. This README is also the **spec** for what we intend to add.

---

<details>
<summary><b>🧭 Table of contents</b></summary>

- [📁 What lives here](#-what-lives-here)
- [🧱 Why our workflows are layered](#-why-our-workflows-are-layered)
- [🗺️ Workflow map](#️-workflow-map)
- [🗂️ Workflow catalog](#️-workflow-catalog-recommended-baseline)
- [✅ Quality gates](#-quality-gates-what-must-pass)
- [🧪 Integration tests with PostGIS](#-integration-tests-with-postgis-kfm-specific)
- [🐳 Docker builds](#-docker-builds-caching--multi-arch)
- [🔐 Security scanning](#-security-scanning-containers--deps)
- [🧠 Data and AI lanes](#-data-and-ai-lanes-earth-engine-analytics-reproducibility)
- [📦 Artifacts and reporting](#-artifacts--reporting)
- [🧷 Secrets and environments](#-secrets--environments-keep-it-boring)
- [🧼 Workflow hygiene](#-workflow-hygiene-do-this-everywhere)
- [🛠️ Starter templates](#️-starter-templates-copy--paste)
- [🧰 Debug locally](#-debugging-workflows-locally)
- [🧾 New workflow checklist](#-adding-a-new-workflow-checklist)
- [📚 References](#-references-for-this-folder)

</details>

---

## 📁 What lives here

```text
📁 .github/workflows/
├─ 🧪 ci.yml                # fast PR lane: lint + unit tests
├─ 🧬 integration.yml       # PostGIS + adapter/service integration tests
├─ 🔐 codeql.yml            # SAST (CodeQL)
├─ 🔐 security.yml          # dep review, secret scan helpers, container scan hooks (optional)
├─ 🐳 docker.yml            # build/push images (optional)
├─ 📚 docs.yml              # docs build/link checks (optional)
├─ 🌐 pages.yml             # GitHub Pages deploy (optional)
├─ 🏷️ release.yml           # release packaging/changelog (optional)
└─ 🧾 README.md             # you are here 👋
```

> [!NOTE]
> It’s okay if you don’t have all of these yet — but the **intent** should stay stable as the repo grows.

---

## 🧱 Why our workflows are layered

KFM is intentionally modular (clean boundaries + contract-first integration), so CI mirrors that structure:

1) ✅ Validate **core logic** (lint, unit tests, type checks)  
2) ✅ Validate **adapters/integration** (DB + services, PostGIS, contracts)  
3) ✅ Package & ship (**images**, artifacts, deploy lanes)

This prevents a “mega-workflow” that is slow, flaky, and hard to debug. 🛣️

---

## 🗺️ Workflow map

> [!TIP]
> GitHub’s Mermaid renderer is strict. To avoid parse errors:
> - Keep **one edge per line**
> - Wrap labels in quotes when using punctuation/emoji
> - Avoid HTML (`<br/>`) inside nodes unless you *really* need it

```mermaid
flowchart LR
  PR["🔀 Pull Request"] --> CI["🧪 ci.yml · fast checks"]
  CI --> INT["🧬 integration.yml · PostGIS + adapters"]
  CI --> SEC["🔐 codeql.yml / security.yml · scans"]
  CI --> DOCS["📚 docs.yml · build + link checks (optional)"]
  INT --> IMG["🐳 docker.yml · build/publish (optional)"]
  IMG --> DEPLOY["🚀 pages.yml / release.yml · promotion (optional)"]
```

---

## 🗂️ Workflow catalog (recommended baseline)

> If a workflow file isn’t present yet, treat this section as the **spec** for creating it.

| Workflow 📄 | What it protects ✅ | Typical triggers ⏱️ | Outputs 📦 |
|---|---|---|---|
| `ci.yml` | fast PR checks (lint + unit tests + type checks) | `pull_request`, `push` | test reports, coverage |
| `integration.yml` | PostGIS + service integration (API/DB/worker boundaries) | `workflow_dispatch`, nightly; optionally PR | logs, reports |
| `codeql.yml` | SAST security scanning | `pull_request`, schedule | SARIF results |
| `security.yml` | dependency review + container scan glue | `pull_request`, schedule | SARIF/scan logs |
| `docker.yml` | build/push images + cache | `push` to `main`, tags | OCI images (GHCR) |
| `docs.yml` | docs build + link checks | `pull_request` | built docs artifact |
| `pages.yml` | web deploy to GitHub Pages | `push` to `main` or dispatch | deployed Pages site |
| `release.yml` | release packaging + notes | tags | release assets, notes |

---

## ✅ Quality gates (what must pass)

### 1) Code health 🧼
- Formatting + linting (fast fail)
- Unit tests (core logic first)
- Type checks (where applicable)
- Coverage floor (optional, but recommended)

### 2) Contracts and metadata boundaries 🧾
KFM treats interfaces as contracts:
- API contracts (OpenAPI/GraphQL)
- Data boundary artifacts (STAC/DCAT/PROV) when pipelines touch `data/`

### 3) Geo and data correctness 🗺️
Geospatial work fails from schema drift + toolchain mismatch:
- validate schemas
- validate links (assets exist)
- keep runs deterministic where possible (pin versions + stable IDs)

---

## 🧪 Integration tests with PostGIS (KFM-specific)

KFM uses PostgreSQL + PostGIS for spatial query integrity. Run integration tests against a **real** PostGIS container.

### Option A: GitHub Actions service container (fast lane)
✅ Best when your integration tests only need DB (and maybe Redis)

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

### Option B: Docker Compose (multi-service parity)
✅ Best when you also run API + worker + cache

```yaml
services:
  db:
    image: postgis/postgis:15-3.4
    environment:
      POSTGRES_DB: kfm_test
      POSTGRES_PASSWORD: postgres
    ports:
      - "5432:5432"
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres -d kfm_test"]
      interval: 10s
      timeout: 5s
      retries: 10
```

> [!CAUTION]
> The #1 source of CI flake is “tests started before the DB was ready.”  
> Add health checks + explicit waits. Always.

---

## 🐳 Docker builds: caching + multi-arch

### ✅ Prefer BuildKit + GHA cache
Fast builds, minimal setup:

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

### 🧪 Compatibility via matrix
Useful for Node tooling or Python versions:

```yaml
strategy:
  matrix:
    python: ["3.11", "3.12"]
```

---

## 🔐 Security scanning (containers + deps)

Baseline expectations:
- ✅ dependency review on PRs
- ✅ CodeQL (SAST)
- ✅ secret scanning (and push protection)
- ✅ container image scanning on `main` + tags (optional but recommended)

> [!NOTE]
> For forks: publishing workflows should not run with secrets on untrusted PRs. Keep publish steps on `push` to `main`, tags, or `workflow_dispatch`.

---

## 🧠 Data and AI lanes (Earth Engine, analytics, reproducibility)

CI shouldn’t run planet-scale pipelines on every PR. Instead:

- ✅ **PR lane:** lightweight unit tests + schema checks + small fixtures
- 🗓️ **Nightly/weekly:** heavy geospatial jobs + regression comparisons
- 📦 **Artifacts:** store summaries, metrics, diffs (don’t spam logs)

Rule of thumb:
- If it needs credentials or takes >10 minutes → schedule it (or manual dispatch).

---

## 📦 Artifacts & reporting

Recommended artifacts to standardize across workflows:

- `unit-test-results.xml` / `pytest.xml`
- `coverage.xml` (+ HTML if desired)
- integration logs (zipped)
- security reports (SARIF)
- image digests / SBOM outputs (optional)

💡 Naming tip: include workflow + sha → `ci-unit-${{ github.sha }}`

---

## 🧷 Secrets & environments (keep it boring)

Common secrets you’ll likely need:
- `GITHUB_TOKEN` (usually sufficient for GHCR with `packages: write`)
- deploy credentials (only in protected envs)
- 3rd-party tokens (e.g., Earth Engine), scoped and rotated

✅ Use GitHub **Environments** (`dev`, `stage`, `prod`) to:
- scope secrets safely
- require approvals for prod
- attach deploy history to commits

> [!CAUTION]
> Avoid `pull_request_target` unless you deeply understand the security model.  
> Default to `pull_request` + read-only permissions.

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
<summary><strong>🧪 <code>ci.yml</code> — Lint + Unit Tests (fast PR lane)</strong></summary>

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
  python-lint-test:
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
          name: unit-test-artifacts
          path: |
            unit-test-results.xml
            coverage.xml
```
</details>

<details>
<summary><strong>🧬 <code>integration.yml</code> — PostGIS + Integration Tests</strong></summary>

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
<summary><strong>🔐 <code>security.yml</code> — Dependency + Security Scans</strong></summary>

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
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Build image (local)
        run: docker build -t kfm:scan .
      - name: Scan image (placeholder)
        run: |
          echo "TODO: run container scan tool (e.g., Trivy) and upload SARIF"
```
</details>

<details>
<summary><strong>📚 <code>docs.yml</code> — Docs Build + Link Check</strong></summary>

```yaml
name: Docs

on:
  pull_request:

permissions:
  contents: read

jobs:
  build-docs:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      # Replace with your docs toolchain (mkdocs, docusaurus, sphinx, etc.)
      - name: Build docs (placeholder)
        run: |
          echo "TODO: build docs"
          mkdir -p site && echo "docs build output" > site/index.html

      - uses: actions/upload-artifact@v4
        with:
          name: docs-site
          path: site
```
</details>

<details>
<summary><strong>🌐 <code>pages.yml</code> — GitHub Pages Deploy (static web viewer)</strong></summary>

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

- [ ] Name jobs after outcomes (`lint`, `unit-tests`, `integration-tests`, `build-image`)
- [ ] Keep PR checks fast (aim ≤ ~10 minutes)
- [ ] Put slow jobs behind schedules or manual dispatch
- [ ] Cache dependencies and Docker layers
- [ ] Upload artifacts on failure (logs are gold 🥇)
- [ ] Pin action versions
- [ ] Avoid secrets on `pull_request` from forks
- [ ] Add minimal `permissions:` and only elevate when required
- [ ] Add `concurrency:` cancellation to reduce queue noise
- [ ] Keep the KFM order intact: **ETL → Catalogs → Graph → API → UI**

---

## 📚 References for this folder

> 📌 Repo convention (recommended): store reference PDFs under `docs/library/` and internal specs under `docs/specs/`.

- 🧱 Architecture and layering rationale → `docs/architecture/`
- 🗺️ Data staging and catalogs (STAC/DCAT/PROV) → `data/README.md`
- 🧪 Test strategy and CI gates → `tests/README.md`
- 🔐 Security and disclosure process → `.github/SECURITY.md`
- 🌐 Web viewer deployment notes → `web/README.md`

> 🔁 If you rename workflows or reorganize docs, update this README — it’s the “single source of truth” for CI/CD intent.
