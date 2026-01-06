# 🧰 `.github/workflows` — CI/CD for Kansas Frontier Matrix (KFM)

![CI](https://github.com/<ORG>/<REPO>/actions/workflows/ci.yml/badge.svg)
![Security](https://github.com/<ORG>/<REPO>/actions/workflows/security.yml/badge.svg)
![Docker](https://github.com/<ORG>/<REPO>/actions/workflows/docker.yml/badge.svg)

> 🧩 This folder contains GitHub Actions workflows that keep KFM **buildable, testable, secure, and shippable**—from geospatial pipelines to web UI.

---

## 🧭 Quick navigation

- [🗂️ Workflow catalog](#️-workflow-catalog-recommended-baseline)
- [🧱 Why our workflows are “layered”](#-why-our-workflows-are-layered)
- [✅ Quality gates](#-quality-gates-what-must-pass)
- [🧪 PostGIS integration tests](#-integration-tests-with-postgis-kfm-specific)
- [🐳 Docker builds](#-docker-builds-caching--multi-arch)
- [🔐 Security scanning](#-security-scanning-containers--deps)
- [🧠 Data/AI + Earth Engine](#-dataai-workflows-earth-engine-analytics-reproducibility)
- [📦 Artifacts & reporting](#-artifacts--reporting)
- [🧷 Secrets & environments](#-secrets--environments-keep-it-boring)
- [🛠️ Starter templates](#️-starter-templates-copy--paste)
- [🧰 Debug locally](#-debugging-workflows-locally)
- [🧾 New workflow checklist](#-adding-a-new-workflow-checklist)
- [📚 References](#-references-for-this-folder)

---

## 📁 What lives here

```text
📁 .github/
  └─ 📁 workflows/
     ├─ 🧪 ci.yml
     ├─ 🧬 integration.yml
     ├─ 🐳 docker.yml
     ├─ 🔐 security.yml
     ├─ 📚 docs.yml
     ├─ 🚀 deploy.yml
     └─ 🧾 README.md  ← you are here
```

---

## 🧱 Why our workflows are “layered”

KFM is intentionally modular (domain logic separated from infrastructure details), so our CI mirrors that separation:

1) ✅ Validate **core logic** (lint, unit tests, type checks)  
2) ✅ Validate **adapters/integration** (DB + services, PostGIS, contracts)  
3) ✅ Package & ship (**Docker**, artifacts, deploy lanes)

This lines up with KFM’s architectural principles: **layer separation, dependency direction, interface-based integration, testability, replaceability**. See internal architecture docs for the full rationale. 📄

KFM spans multiple system surfaces (data ingestion → repositories → AI/analysis → visualization UI), so CI uses multiple “lanes” to avoid coupling everything into one mega-job. 🛣️

```mermaid
flowchart LR
  PR[Pull Request] --> CI[🧪 ci.yml<br/>fast checks]
  CI --> INT[🧬 integration.yml<br/>DB + adapters]
  INT --> IMG[🐳 docker.yml<br/>build/publish]
  CI --> SEC[🔐 security.yml<br/>deps + scans]
  CI --> DOCS[📚 docs.yml<br/>docs build]
  IMG --> DEPLOY[🚀 deploy.yml<br/>env promotion]
```

---

## 🗂️ Workflow catalog (recommended baseline)

> If a workflow file isn’t present yet, treat this README as the **spec** for creating it.

| Workflow 📄 | What it protects ✅ | Typical triggers ⏱️ | Outputs 📦 |
|---|---|---|---|
| `ci.yml` | Fast PR checks (lint + unit tests) | `pull_request`, `push` | Test results, coverage |
| `integration.yml` | PostGIS + service integration tests | optional `pull_request`, nightly | Logs, reports |
| `docker.yml` | Build/push images + cache | `push` to `main`, tags | OCI images → GHCR |
| `security.yml` | Dependency + container scanning | `pull_request`, nightly | SARIF, scan reports |
| `docs.yml` | Docs build/link checks | `pull_request` | Built docs artifact |
| `deploy.yml` | Promote to envs (dev/stage/prod) | tags / manual dispatch | Deployment logs |

---

## ✅ Quality gates (what must pass)

### 1) Code health 🧼
- Formatting + linting (fast fail)
- Unit tests (core logic first)
- Type checks (if applicable)
- Coverage floor (optional, but recommended)

### 2) Geo + data correctness 🗺️
Geospatial work tends to fail from schema drift + “it works on my machine” toolchains, so CI should enforce:
- schema validation
- reproducible pipelines
- deterministic outputs where possible (pin versions & seeds)

### 3) Infra parity 🐳
Use containers to keep build/test environments consistent across dev + CI:
- containerize integration dependencies (DB/services)
- keep CI image builds close to prod images
- cache build layers aggressively

---

## 🧪 Integration tests with PostGIS (KFM-specific)

KFM uses PostgreSQL + PostGIS for geospatial storage, so integration tests should run against a real PostGIS container.

### Option A: GitHub Actions service container (fastest + simplest)
✅ Great for PR integration tests

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

### Option B: Docker Compose (best when multiple services are involved)
✅ Great when you also spin up API + workers + cache

Example `docker-compose.ci.yml` snippet:

```yaml
services:
  db:
    image: postgis/postgis:15-3.4
    environment:
      POSTGRES_DB: kfm_test
      POSTGRES_PASSWORD: postgres
    ports:
      - "5432:5432"
```

> 🔎 Tip: Always add healthchecks + explicit waits. The #1 flake cause is “tests started before DB was ready”.

---

## 🐳 Docker builds: caching + multi-arch

### ✅ Prefer buildx cache via GitHub Actions cache (simple + fast)
This avoids manual cache folder management and works well with BuildKit:

```yaml
- uses: docker/setup-buildx-action@v3
- uses: docker/build-push-action@v6
  with:
    context: .
    push: true
    tags: ghcr.io/<ORG>/<REPO>:${{ github.sha }}
    cache-from: type=gha
    cache-to: type=gha,mode=max
```

### 🧪 Matrix tests (runtime compatibility)
Use matrices to validate multiple runtime versions in parallel (especially for Node services).

```yaml
strategy:
  matrix:
    node: ["20", "22"]
```

---

## 🔐 Security scanning (containers + deps)

**Baseline expectations:**
- dependency review on PRs
- SAST / CodeQL (where applicable)
- container image scanning on `main` + tags
- upload results as SARIF when possible

**Policy note:** For forks, avoid workflows that expose secrets. Prefer:
- `pull_request` with read-only permissions  
- scheduled scans on `main`  
- manual dispatch for sensitive publishing steps

---

## 🧠 Data/AI workflows (Earth Engine, analytics, reproducibility)

CI shouldn’t run “planet-scale” pipelines on every PR. Instead:

- ✅ PR lane: lightweight unit tests + static checks  
- 🗓️ Nightly/weekly: heavy geospatial pipelines + regression checks  
- 📦 Artifacts: store summaries, metrics, and diffs

**Rule of thumb:** if it needs credentials, long runtimes, or big compute → schedule it.

---

## 📦 Artifacts & reporting

Recommended artifacts to standardize across workflows:

- ✅ `unit-test-results.xml` / `pytest.xml`
- ✅ coverage report (`coverage.xml`, HTML)
- ✅ integration logs (zipped)
- ✅ security reports (SARIF)
- ✅ built image digests (for deploy traceability)

💡 **Naming tip:** include job + sha in artifact names to make debugging painless.

---

## 🧷 Secrets & environments (keep it boring)

Common secrets you’ll likely need:
- `GHCR_TOKEN` (or use `GITHUB_TOKEN` with correct permissions for GHCR)
- `DEPLOY_SSH_KEY` / `CLOUD_CREDENTIALS` (deployment)
- `POSTGRES_PASSWORD` (CI integration DB, or use ephemeral defaults)

✅ Use GitHub **Environments** (dev/stage/prod) to:
- scope secrets safely
- require approvals for prod
- attach deployment history to commits

> 🧱 Keep “outer layer” concerns (networking, cloud provider details) at the workflow/env layer—don’t leak them into domain tests.

---

## 🛠️ Workflow hygiene (do this everywhere)

### 🔏 Minimal permissions by default
Set workflow permissions explicitly and only elevate where required:

```yaml
permissions:
  contents: read
```

For container pushes to GHCR, add:
```yaml
permissions:
  contents: read
  packages: write
```

For SARIF uploads, add:
```yaml
permissions:
  security-events: write
```

### 🧵 Concurrency (avoid dogpiling)
Cancel older runs for the same branch:

```yaml
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true
```

### 📌 Pin actions (reduce supply-chain risk)
Prefer pinning to major versions at minimum (and to commit SHA if you want maximum safety).

---

## 🧩 Starter templates (copy / paste)

> These are **baseline skeletons**. Keep them small, fast, and easy to reason about. 🧠  
> Replace tool choices (`pytest`, `ruff`, `npm`, `pnpm`, etc.) with your stack.

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

      - name: Lint (example)
        run: |
          ruff check .
          ruff format --check .

      - name: Unit tests (example)
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
<summary><strong>🔐 <code>security.yml</code> — Dependency + Image Scanning</strong></summary>

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
      # Build image locally, then scan with your preferred tool (Trivy, Grype, etc.)
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
<summary><strong>🚀 <code>deploy.yml</code> — Promote to Environments</strong></summary>

```yaml
name: Deploy

on:
  workflow_dispatch:
    inputs:
      environment:
        description: "Target environment"
        required: true
        type: choice
        options: [dev, stage, prod]

permissions:
  contents: read

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: ${{ inputs.environment }}
    steps:
      - uses: actions/checkout@v4
      - name: Deploy (placeholder)
        run: |
          echo "Deploying to ${{ inputs.environment }}..."
          echo "TODO: run deployment scripts"
```
</details>

---

## 🧰 Debugging workflows locally

Options:
- ✅ Run the same commands as CI (recommended)
- 🧪 Use `act` to simulate GitHub Actions locally (best effort; not perfect parity)
- 🐳 Use Docker Compose profiles to run targeted service subsets (front/back splits)

---

## 🧾 Adding a new workflow (checklist)

- [ ] Name jobs after outcomes (e.g., `lint`, `unit-tests`, `integration-tests`, `build-image`)
- [ ] Keep PR checks fast (aim ≤ ~10 minutes)
- [ ] Put slow jobs behind schedules or manual dispatch
- [ ] Cache dependencies and Docker layers
- [ ] Upload artifacts on failure (logs are gold 🥇)
- [ ] Pin action versions (avoid surprise breakage)
- [ ] Avoid secrets on `pull_request` from forks
- [ ] Add minimal `permissions:` and only elevate when required
- [ ] Add `concurrency:` cancellation to reduce queue noise

---

## 📚 References for this folder

> 📌 Recommend storing PDFs/books under `docs/references/` with **slugged filenames** (no spaces) for stable links.

- 🧱 KFM architecture principles + layering rationale  
  - `docs/references/kfm-technical-documentation.pdf`  
- 🗺️ KFM mapping hub architecture (data → AI → UI)  
  - `docs/references/kfm-mapping-hub-design.pdf`
- 🧭 GIS workflows + requirements discipline  
  - `docs/references/gis-basics.pdf`
- 🐳 Docker in CI/CD (compose, scanning, caching, matrices)  
  - `docs/references/introduction-to-docker.pdf`
- 🔐 Governance + assurance framing (why we enforce security & lifecycle checks)  
  - `docs/references/introduction-to-digital-humanism.pdf`
- 🛰️ Earth Engine + remote sensing workflows  
  - `docs/references/cloud-remote-sensing-gee.pdf`

> 🔁 If you rename or relocate references, update links here (this README is the “single source of truth” for CI/CD design intent).
