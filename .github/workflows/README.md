# 🧰 `.github/workflows/` — CI/CD for Kansas Frontier Matrix (KFM)

[![CI](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/ci.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/ci.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml)
[![Pages](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pages.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pages.yml)

> 🧩 This folder contains GitHub Actions workflows that keep KFM **buildable, testable, secure, and shippable** — from geospatial pipelines to the web map UI.  
> ✅ **Principle:** CI mirrors KFM’s system order → **ETL → Catalogs → Graph → API → UI** (with policy + security checks throughout).

---

## ⚡ Quick links

- 🧪 **All Actions runs:** https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions
- 🐛 **Open issues:** https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues
- 🔐 **Security policy:** `../SECURITY.md` *(recommended)*
- 🧾 **Collaboration hub:** `../README.md` (the `.github/` README)

> [!TIP]
> If a badge 404s, that workflow file probably doesn’t exist yet. This README is also the **spec** for what we intend to add.

---

## 🧭 Table of contents

- [📁 What lives here](#-what-lives-here)
- [🧱 Why our workflows are layered](#-why-our-workflows-are-layered)
- [🗂️ Workflow catalog](#️-workflow-catalog-recommended-baseline)
- [✅ Quality gates](#-quality-gates-what-must-pass)
- [🧪 Integration tests with PostGIS](#-integration-tests-with-postgis-kfm-specific)
- [🐳 Docker builds](#-docker-builds-caching--multi-arch)
- [🔐 Security scanning](#-security-scanning-containers--deps--secrets)
- [🗺️ Data + catalogs workflows](#️-data--catalog-workflows-stacdcatsprov)
- [📦 Artifacts & reporting](#-artifacts--reporting)
- [🧷 Secrets & environments](#-secrets--environments-keep-it-boring)
- [🧼 Workflow hygiene](#-workflow-hygiene-do-this-everywhere)
- [🧩 Reusable workflows](#-reusable-workflows-optional-but-powerful)
- [🛠️ Starter templates](#️-starter-templates-copy--paste)
- [🧰 Debug locally](#-debugging-workflows-locally)
- [🧾 New workflow checklist](#-adding-a-new-workflow-checklist)
- [📚 References](#-references-for-this-folder)

---

## 📁 What lives here

```text
📁 .github/
  └─ 📁 workflows/
     ├─ 🧪 ci.yml                # fast lane: lint + unit tests
     ├─ 🧬 integration.yml       # PostGIS + service integration tests
     ├─ 🔐 codeql.yml            # SAST security scanning (recommended)
     ├─ 🔎 security.yml          # deps/secret/container scans (optional add-on)
     ├─ 🗺️ data-refresh.yml      # scheduled ETL/catalog refresh (optional)
     ├─ 🐳 docker.yml            # build/push images (optional)
     ├─ 🌐 pages.yml             # GitHub Pages deploy (optional)
     ├─ 🏷️ release.yml           # release automation (optional)
     └─ 🧾 README.md             # you are here 👋
```

> [!IMPORTANT]
> KFM’s CI is **not** “just tests.” It’s also lifecycle governance:
> - contracts (OpenAPI + STAC/DCAT/PROV)
> - provenance checks
> - security scans
> - reproducibility guardrails

---

## 🧱 Why our workflows are layered

KFM is intentionally modular (domain logic separated from infrastructure details), so our CI mirrors that separation:

1) ✅ **Fast lane**: lint + unit tests + type checks (quick PR feedback)  
2) ✅ **Integration lane**: PostGIS + API/worker integration + contract checks  
3) ✅ **Ship lane**: build images, publish artifacts, deploy (only when allowed)

```mermaid
flowchart LR
  PR["🔀 Pull Request"] --> CI["🧪 ci.yml<br>fast checks"];
  CI --> INT["🧬 integration.yml<br>DB + adapters"];
  CI --> SEC["🔐 codeql.yml / security.yml<br>scans"];
  CI --> DOCS["📚 docs checks (optional)"];
  INT --> IMG["🐳 docker.yml<br>build/publish (optional)"];
  IMG --> DEPLOY["🚀 deploy/pages/release<br>promotion (optional)"];
```

> 🛣️ Multiple “lanes” keeps PR checks fast while still allowing heavyweight geospatial validation on schedules or manual dispatch.

---

## 🗂️ Workflow catalog (recommended baseline)

> If a workflow file isn’t present yet, treat this table as the **roadmap/spec**.

| Workflow 📄 | Protects ✅ | Typical triggers ⏱️ | Scope 🎯 | Outputs 📦 |
|---|---|---|---|---|
| `ci.yml` | PR correctness | `pull_request`, `push` | lint • unit tests • type checks | junit • coverage |
| `integration.yml` | real service wiring | `workflow_dispatch`, scheduled, (optional PR) | PostGIS • API contracts • worker flows | logs • junit |
| `codeql.yml` | code security | schedule + PR | SAST (Python/JS) | SARIF |
| `security.yml` | supply chain security | schedule + PR | dependency review • secrets • container scan | SARIF • reports |
| `data-refresh.yml` | catalog freshness | schedule + manual | ETL sampling • STAC/DCAT/PROV validation | catalogs • QA report |
| `docker.yml` | reproducible images | push to `main`, tags | buildx • cache • SBOM/attest | GHCR images |
| `pages.yml` | web publishing | push to `main` | web build • deploy | Pages site |
| `release.yml` | packaged releases | tags / manual | build artifacts • changelog | GitHub Release |

---

## ✅ Quality gates (what must pass)

### 1) Code health 🧼
- formatting + linting (fast fail)
- unit tests (core logic)
- type checks (where applicable)
- optional: coverage floor (**target**, not a religion)

### 2) Contract integrity 📜
KFM is contract-first. CI should validate:
- OpenAPI/GraphQL schemas (if present)
- STAC/DCAT/PROV schema validity (if emitting catalogs)
- link integrity (STAC assets exist; DCAT distributions point somewhere real)

### 3) Geo + data correctness 🗺️
Geospatial pipelines fail in predictable ways; CI should catch:
- CRS surprises (meters vs degrees 😅)
- geometry validity (self-intersections, empties)
- raster metadata drift (nodata, resolution, alignment)
- deterministic outputs (stable IDs, pinned inputs/configs)

> [!NOTE]
> Heavy geospatial validation should be **scheduled** (nightly/weekly) unless a PR directly modifies the pipeline logic.

---

## 🧪 Integration tests with PostGIS (KFM-specific)

KFM uses PostgreSQL + PostGIS for spatial indexing and analysis, so integration tests should run against a real PostGIS engine.

### Option A: GitHub Actions service container ✅ (fast + simple)

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

### Option B: Docker Compose ✅ (best for API + worker + cache)

```yaml
# docker-compose.ci.yml (example)
services:
  db:
    image: postgis/postgis:15-3.4
    environment:
      POSTGRES_DB: kfm_test
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
    ports:
      - "5432:5432"
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres -d kfm_test"]
      interval: 10s
      timeout: 5s
      retries: 10
```

> 🔎 #1 cause of flaky integration CI: tests start **before** the DB is ready. Use healthchecks + explicit waits.

---

## 🐳 Docker builds: caching + multi-arch

### ✅ Buildx with GitHub cache (simple + fast)

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

### 🧪 Runtime matrix checks (recommended)
Validate multiple runtimes without slowing a single job:

```yaml
strategy:
  matrix:
    python: ["3.11", "3.12"]
    node: ["20", "22"]
```

> [!TIP]
> Keep matrices for PR lanes **small**. Push broad compatibility sweeps to nightly schedules.

---

## 🔐 Security scanning: containers + deps + secrets

**Baseline expectations (recommended):**
- ✅ dependency review on PRs (blocks risky dependency changes)
- ✅ CodeQL SAST on schedule + PR
- ✅ secret scanning (GitHub-native) + optional custom checks
- ✅ container image scanning on `main` + tags (Trivy/Grype/etc.)
- ✅ upload results as **SARIF** when possible (GitHub can surface findings in Security tab)

**Fork safety rule (non-negotiable):**
- avoid running secret-bearing jobs on `pull_request` from forks
- do not use `pull_request_target` unless you fully understand the security implications

---

## 🗺️ Data + catalog workflows: STAC/DCAT/PROV

CI should treat “catalog + provenance” as a first-class interface.

### Recommended patterns
- ✅ PR lane: validate schema + link integrity on **small fixtures**
- 🗓️ Scheduled lane: run heavyweight pipelines with sampling and produce:
  - diff summaries
  - QA reports
  - updated catalogs (if policy allows automation)

### Good triggers
- `workflow_dispatch` for manual reruns
- `schedule` for nightlies
- `push` for main-branch data publishing (only if trusted)

> 🧠 Rule of thumb: if it needs cloud credentials or has long runtimes → schedule or manual dispatch.

---

## 📦 Artifacts & reporting

Standardize outputs so debugging is painless:

- ✅ JUnit results: `**/*test-results*.xml`
- ✅ coverage: `coverage.xml` (+ HTML for deep dives)
- ✅ integration logs: zipped folder
- ✅ security: SARIF
- ✅ E2E failures: screenshots + videos

**Naming tip:** include workflow + job + sha
- `ci-unit-${{ github.sha }}`
- `integration-postgis-${{ github.sha }}`

---

## 🧷 Secrets & environments (keep it boring)

Common secrets you’ll likely need:
- `GITHUB_TOKEN` permissions for GHCR pushes *(preferred)*
- deploy credentials for cloud targets (only in environment-protected jobs)
- service tokens (Earth Engine, map providers, etc.) — **never** in PR lanes for forks

✅ Use GitHub **Environments** (`dev`, `stage`, `prod`) to:
- scope secrets safely
- require approvals for prod
- attach deployment history to commits

> [!CAUTION]
> If a job can deploy, publish catalogs, or push images: gate it behind an environment with review/approval.

---

## 🧼 Workflow hygiene (do this everywhere)

### 🔏 Minimal permissions by default
```yaml
permissions:
  contents: read
```

For GHCR push:
```yaml
permissions:
  contents: read
  packages: write
```

For SARIF uploads:
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

### 🧠 Path filters (keep PR CI fast)
Only run workflows when relevant files change:

```yaml
on:
  pull_request:
    paths:
      - "src/**"
      - "api/**"
      - "web/**"
      - "data/**"
      - ".github/workflows/**"
```

### 📌 Pin actions (reduce supply-chain risk)
- Minimum: pin to major versions (v4/v5/etc.)
- Maximum safety: pin third-party actions by commit SHA

---

## 🧩 Reusable workflows (optional but powerful)

When patterns repeat (setup Python, run tests, upload artifacts), consider reusable workflows:

- `.github/workflows/_reusable-python-test.yml` (`workflow_call`)
- `.github/workflows/_reusable-node-test.yml`
- `.github/workflows/_reusable-docker-build.yml`

✅ Benefits:
- consistent quality gates
- less YAML duplication
- easier upgrades

---

## 🛠️ Starter templates (copy / paste)

> These are baseline skeletons. Replace tool choices (`pytest`, `ruff`, `uv`, `npm`, `pnpm`) with the repo’s actual stack.

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
          name: unit-test-artifacts-${{ github.sha }}
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
          name: integration-artifacts-${{ github.sha }}
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
      - name: Build image (local)
        run: docker build -t kfm:scan .
      - name: Scan image (placeholder)
        run: |
          echo "TODO: run container scan tool (e.g., Trivy) and upload SARIF"
```
</details>

<details>
<summary><strong>🌐 <code>pages.yml</code> — Build + Deploy GitHub Pages</strong></summary>

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
    steps:
      - uses: actions/checkout@v4

      # Replace with your web build toolchain
      - name: Build site (placeholder)
        run: |
          mkdir -p web/dist
          echo "KFM web build output" > web/dist/index.html

      - name: Upload Pages artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: web/dist

      - name: Deploy to GitHub Pages
        uses: actions/deploy-pages@v4
```
</details>

---

## 🧰 Debugging workflows locally

Options:
- ✅ Run the same commands as CI (best parity)
- 🧪 Use `act` to simulate GitHub Actions (best-effort parity; not perfect)
- 🐳 Use Docker Compose profiles to run targeted service subsets (API-only / DB-only / full stack)

---

## 🧾 Adding a new workflow (checklist)

- [ ] Name jobs after outcomes (`lint`, `unit-tests`, `integration-tests`, `build-image`)
- [ ] Keep PR checks fast (aim ≤ ~10 minutes)
- [ ] Put slow jobs behind schedules or manual dispatch
- [ ] Cache dependencies and Docker layers
- [ ] Upload artifacts on failure (logs are gold 🥇)
- [ ] Pin action versions
- [ ] Avoid secrets on `pull_request` from forks
- [ ] Add minimal `permissions:` and only elevate where required
- [ ] Add `concurrency:` cancellation to reduce queue noise
- [ ] Add `paths:` filters so unrelated changes don’t burn CI minutes

---

## 📚 References for this folder

> 📌 Repo convention (recommended): keep CI/CD rationale docs under `docs/` and link them here.

- 🧱 KFM architecture principles + layering rationale → `docs/architecture/`
- 🗺️ Data lifecycle + catalogs (STAC/DCAT/PROV) → `data/README.md`
- 🧪 Test strategy + gates → `tests/README.md`
- 🔐 Security policy → `.github/SECURITY.md` *(recommended)*

---

🧭 **Goal:** green CI is not a vibe — it’s a contract.  
🧾 **Promise:** if it ships, it has receipts.
