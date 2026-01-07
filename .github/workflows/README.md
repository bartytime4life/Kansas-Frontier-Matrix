# 🧰 `.github/workflows/` — CI/CD for Kansas Frontier Matrix (KFM)

[![CI](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/ci.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/ci.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml)
[![Pages](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pages.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pages.yml)

> 🧩 This folder contains GitHub Actions workflows that keep KFM **buildable**, **testable**, **secure**, and **shippable** — from data pipelines to the map UI.  
> ✅ **Principle:** CI follows KFM’s governed system order → **ETL → Metadata (STAC/DCAT/PROV) → Graph → API → UI** (with policy + security checks throughout).

> [!IMPORTANT]
> CI is intentionally **boring** (predictable, repeatable, least-privilege) — because our *data* is the interesting part. 🗺️✨

---

## ⚡ Quick links

| Action | Link |
|---|---|
| ✅ All Actions runs | https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions |
| 🐛 Open issues | https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues |
| 🤝 `.github/` Collaboration hub | [`../README.md`](../README.md) |
| 🔐 Security policy | [`../SECURITY.md`](../SECURITY.md) *(or adjust if you keep it at repo root)* |
| 📦 Releases | https://github.com/bartytime4life/Kansas-Frontier-Matrix/releases |

> [!TIP]
> If a badge 404s, that workflow file probably doesn’t exist yet. This README doubles as the **spec** for what we intend to add next. 🧾

---

<details>
<summary><b>🧭 Table of contents</b></summary>

- [📺 Mermaid Workflow TV](#-mermaid-workflow-tv)
- [📁 What lives here](#-what-lives-here)
- [🧠 CI philosophy](#-ci-philosophy)
- [🗂️ Workflow catalog](#️-workflow-catalog-recommended-baseline)
- [✅ Quality gates](#-quality-gates-what-must-pass)
- [🗺️ Data + catalog gates](#️-data--catalog-gates-kfm-specific)
- [🧪 Integration tests (PostGIS + Graph)](#-integration-tests-postgis--graph)
- [🧱 Build & packaging](#-build--packaging-condamamba--docker)
- [🔐 Security scanning](#-security-scanning-sast-deps-secrets-containers)
- [📦 Artifacts & traceability](#-artifacts--traceability)
- [🧷 Secrets & environments](#-secrets--environments-keep-it-boring)
- [🛠️ Starter templates](#️-starter-templates-copy--paste)
- [🧰 Debug locally](#-debugging-workflows-locally)
- [🧾 New workflow checklist](#-adding-a-new-workflow-checklist)
- [📚 References](#-references-for-this-folder)

</details>

---

## 📺 Mermaid Workflow TV

A “TV guide” of how work flows through KFM CI/CD (fast lane → promotion → heavy jobs). 📺🧪

```mermaid
flowchart TB
  subgraph PR["🧪 PR Lane (fast • required)"]
    PR1["ci.yml<br/>lint • unit • typecheck"]
    PR2["catalog-qa.yml<br/>STAC/DCAT quick gate"]
    PR3["security.yml<br/>dep review • secrets • scans"]
  end

  subgraph MAIN["🚀 Main Lane (promotion)"]
    M1["docker.yml<br/>build • tag • push (GHCR)"]
    M2["deploy.yml / pages.yml<br/>deploy previews or docs"]
  end

  subgraph NIGHTLY["🌙 Nightly Lane (slow • scheduled)"]
    N1["integration.yml<br/>PostGIS + graph + API contracts"]
    N2["data-refresh.yml<br/>ETL refresh + diffs"]
    N3["model-regression.yml<br/>metrics + drift checks"]
  end

  subgraph RELEASE["🏷️ Release Lane (tags)"]
    R1["release.yml<br/>notes + artifacts + provenance"]
    R2["sbom.yml<br/>SBOM + attestations (optional)"]
  end

  PR1 --> M1
  PR2 --> M1
  PR3 --> M1

  M1 --> M2
  M1 --> R1
  R1 --> R2

  PR1 --> N1
  PR2 --> N2
  N1 --> N2
  N2 --> N3
```

> [!TIP]
> Mermaid on GitHub can be picky. To avoid parse errors:
> - Keep **one edge per line**
> - Use simple IDs (`PR1`, `M1`, etc.)
> - Prefer labels in quotes or brackets when using punctuation/emoji 😄

---

## 📁 What lives here

```text
📁 .github/workflows/
├─ 🧪 ci.yml                    # fast PR lane: lint + unit tests + type checks
├─ 🧾 catalog-qa.yml             # STAC/DCAT quick gate + link check (recommended)
├─ 🧬 integration.yml            # PostGIS + graph/db + adapter/service integration tests
├─ 🔐 codeql.yml                 # SAST (CodeQL)
├─ 🔐 security.yml               # dependency review + secret scan helpers + container scan hooks
├─ 🐳 docker.yml                 # build/push images (optional early, essential later)
├─ 🌙 data-refresh.yml           # scheduled ETL + catalog refresh + diffs (optional)
├─ 📚 docs.yml                   # docs build + link checks (optional)
├─ 🌐 pages.yml                  # GitHub Pages deploy (optional)
├─ 🏷️ release.yml                # release packaging + changelog + provenance (optional)
└─ 📄 README.md                  # you are here 👋
```

> [!NOTE]
> It’s okay if you don’t have all of these yet — but the **intent** should stay stable as the repo grows.

---

## 🧠 CI philosophy

### ✅ “Layered gates” beat “mega workflows”
KFM is modular by design, so CI mirrors that structure:

1) **Code gate**: lint, unit tests, type checks  
2) **Metadata gate**: catalogs, schemas, provenance checks  
3) **Integration gate**: DBs/services/queues with real containers  
4) **Security gate**: SAST, dependency review, secret detection, container scan  
5) **Promotion gate**: build/publish/deploy with protected environments

This prevents CI from becoming a single slow pipeline that no one trusts. 🛣️

### 🧾 Contracts over vibes
KFM treats key interfaces as contracts:
- API contracts (OpenAPI / GraphQL)
- Data catalogs (STAC/DCAT/PROV)
- Model & analysis artifacts (metrics + reproducibility notes)

If a contract drifts, CI should fail fast — **before** it ships. ✅

---

## 🗂️ Workflow catalog (recommended baseline)

> If a workflow file isn’t present yet, treat this section as the **spec** for creating it.

| Workflow 📄 | What it protects ✅ | Typical triggers ⏱️ | Budget 🎯 | Outputs 📦 |
|---|---|---|---:|---|
| `ci.yml` | lint + unit tests + type checks | `pull_request`, `push` | ≤ 10 min | junit, coverage |
| `catalog-qa.yml` | STAC/DCAT quick gate + link-check | `pull_request`, `workflow_dispatch` | ≤ 5 min | QA report |
| `integration.yml` | PostGIS + graph + adapter integration | nightly + dispatch | 10–45 min | logs, junit |
| `codeql.yml` | SAST (CodeQL) | `pull_request`, schedule | n/a | SARIF |
| `security.yml` | dep review + secrets + container scan glue | PR + schedule | ≤ 15 min | SARIF/logs |
| `docker.yml` | build + tag + push images | `push` to `main`, tags | ≤ 20 min | OCI images |
| `docs.yml` | docs build + link checks | PR | ≤ 10 min | docs artifact |
| `pages.yml` | deploy static docs/viewer | `push` to `main` or dispatch | n/a | Pages deploy |
| `release.yml` | release notes + pinned artifacts | tags | n/a | release assets |

---

## ✅ Quality gates (what must pass)

### 1) Code health 🧼
- Formatting + linting (fast fail)
- Unit tests (core logic)
- Type checks (where applicable)
- Coverage floor (optional, but recommended)

### 2) Metadata + contracts 🗃️
- JSON/YAML schema validity
- STAC/DCAT/PROV requirements (license, providers, extensions, etc.)
- Link integrity (top-level asset hrefs)
- Provenance presence (source + processing steps)

### 3) Integration fidelity 🧪
- PostGIS container integration
- Graph DB integration (if used)
- “Can we run the pipeline end-to-end on a tiny fixture?” ✅

### 4) Security posture 🔐
- Dependency review (PR gate)
- CodeQL (SAST)
- Secret scanning (prevents foot-guns)
- Container scan on promoted images (recommended)

### 5) Governance & policy 🏛️
- “No secrets” checks
- License + usage terms checks for new data
- Optional: FAIR/CARE checklist automation when data touches sensitive domains

---

## 🗺️ Data + catalog gates (KFM-specific)

### ✅ The STAC/DCAT quick gate (recommended)
Run a fast, deterministic QA pass on every PR that touches catalogs:

- `license` present + non-empty  
- `providers` present + non-empty  
- `stac_extensions` present *(warn if empty, fail if missing)*  
- Top-level `links[].href` **HEAD/GET link-check**  
- Optional: enforce “Stable-only” STAC extensions for production catalogs

> [!TIP]
> This gate pays for itself immediately: it stops schema drift and broken hrefs before they become “mystery failures” later.

### 🧭 CRS + projection sanity checks
Geospatial bugs often come from silent CRS drift. Add lightweight checks:
- Required `EPSG` values present where expected
- Raster grid metadata present for raster assets
- BBox/geometry validity for footprint fields

### 🧪 Geometry validity checks
Where vector data is involved, validate geometries:
- invalid/self-intersecting geometries
- empty geometries
- unexpected coordinate ranges

> [!CAUTION]
> Data QA should be **fast** on PRs (tiny fixtures), and **deep** on nightly jobs (full runs).

---

## 🧪 Integration tests (PostGIS + Graph)

KFM’s spatial correctness depends on real PostGIS (and often a graph DB for relationships). Prefer containerized integration tests.

### Option A: GitHub Actions service containers (fast + simple)

**PostGIS service**
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

**Neo4j (optional / if applicable)**
```yaml
services:
  neo4j:
    image: neo4j:5
    env:
      NEO4J_AUTH: neo4j/testpass
    ports:
      - 7474:7474
      - 7687:7687
```

> [!CAUTION]
> The #1 source of CI flake is “tests started before DB was ready.”  
> Always add health checks + explicit waits. ✅

### Option B: Docker Compose (multi-service parity)
Best when you need API + workers + cache + DB for a realistic end-to-end test.

---

## 🧱 Build & packaging (Conda/Mamba + Docker)

### ✅ Match production with reproducible environments
If KFM uses Conda/Mamba environments, CI should:
- resolve deps the same way every time
- build inside containers where possible
- output **build metadata** (versions, digests, checksums) as artifacts

### 🐳 Docker builds: caching + multi-arch
Use BuildKit + GHA cache:

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

---

## 🔐 Security scanning (SAST, deps, secrets, containers)

Baseline expectations:
- ✅ Dependency review on PRs
- ✅ CodeQL scanning
- ✅ Secret scanning (and push protection)
- ✅ Container image scan on `main` + tags (recommended)

> [!NOTE]
> For forks: publishing workflows should not run with secrets on untrusted PRs.  
> Keep publish steps on `push` to `main`, tags, or `workflow_dispatch`.

---

## 📦 Artifacts & traceability

Standardize artifacts across workflows (debuggability + audit):

- `unit-test-results.xml` / `pytest.xml`
- `coverage.xml` (+ optional HTML coverage)
- integration logs (zipped)
- security reports (SARIF)
- build metadata (`build-info.json`, image digest, lockfiles)
- optional: SBOM outputs (`spdx.json`, `cyclonedx.json`)

💡 Naming tip: include workflow + sha → `ci-unit-${{ github.sha }}`

---

## 🧷 Secrets & environments (keep it boring)

Common secrets:
- `GITHUB_TOKEN` (often enough for GHCR with `packages: write`)
- deploy credentials (only in protected envs)
- third-party tokens (scoped + rotated)

✅ Use GitHub **Environments** (`dev`, `stage`, `prod`) to:
- scope secrets safely
- require approvals for prod
- attach deploy history to commits

> [!CAUTION]
> Avoid `pull_request_target` unless you deeply understand the security model.  
> Default to `pull_request` + read-only permissions.

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
    timeout-minutes: 15

    steps:
      - uses: actions/checkout@v4

      # Option A (pip): good for early stage repos
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
<summary><strong>🧾 <code>catalog-qa.yml</code> — STAC/DCAT Quick Gate (recommended)</strong></summary>

```yaml
name: Catalog QA

on:
  pull_request:
    paths:
      - "data/**"
      - "catalog/**"
      - "tools/validation/**"
  workflow_dispatch:

permissions:
  contents: read

jobs:
  catalog-qa:
    runs-on: ubuntu-latest
    timeout-minutes: 10

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
          cache: "pip"

      - name: Install QA deps
        run: |
          python -m pip install -U pip
          pip install -r requirements-dev.txt

      - name: Run catalog QA
        run: |
          python tools/validation/catalog_qa/run_catalog_qa.py --fail-on-broken-links

      - uses: actions/upload-artifact@v4
        if: always()
        with:
          name: catalog-qa-${{ github.sha }}
          path: |
            tools/validation/catalog_qa/out/**
```
</details>

<details>
<summary><strong>🧬 <code>integration.yml</code> — PostGIS + Integration Tests (nightly)</strong></summary>

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
    timeout-minutes: 45

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

      # Optional graph service if your integration tests need it:
      # neo4j:
      #   image: neo4j:5
      #   env:
      #     NEO4J_AUTH: neo4j/testpass
      #   ports:
      #     - 7474:7474
      #     - 7687:7687

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
            .pytest_cache/**
            logs/**
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
    timeout-minutes: 30

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
          echo "TODO: run a container scan tool (e.g., Trivy) and upload SARIF"
```
</details>

<details>
<summary><strong>🌐 <code>pages.yml</code> — GitHub Pages Deploy (static docs/viewer)</strong></summary>

```yaml
name: Pages

on:
  push:
    branches: [main]
    paths:
      - "web/**"
      - "docs/**"
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

      # Replace with your build step (or skip if static)
      - name: Build (placeholder)
        run: |
          mkdir -p dist
          if [ -d web ]; then cp -R web/* dist/; fi
          if [ -d docs/site ]; then cp -R docs/site/* dist/; fi

      - uses: actions/upload-pages-artifact@v3
        with:
          path: dist

      - uses: actions/deploy-pages@v4
```
</details>

---

## 🧰 Debugging workflows locally

Preferred order:

1) ✅ Run the same commands CI runs (best parity)  
2) 🐳 Use Compose profiles to mimic integration dependencies  
3) 🧪 Use `act` to simulate GitHub Actions locally *(helpful, not perfect)*

---

## 🧾 Adding a new workflow checklist

- [ ] Name jobs after outcomes (`lint`, `unit-tests`, `integration-tests`, `catalog-qa`, `build-image`)
- [ ] Keep PR checks fast (aim ≤ ~10 minutes)
- [ ] Put slow jobs behind schedules or manual dispatch
- [ ] Cache dependencies and Docker layers
- [ ] Upload artifacts on failure (logs are gold 🥇)
- [ ] Pin action versions (at least major versions)
- [ ] Avoid secrets on `pull_request` from forks
- [ ] Use minimal `permissions:` and only elevate when required
- [ ] Add `concurrency:` cancellation to reduce queue noise
- [ ] Keep the KFM order intact: **ETL → Metadata → Graph → API → UI**

---

## 📚 References for this folder

> 📌 Convention (recommended): store reference PDFs under `docs/library/` and internal specs under `docs/specs/`.

- 🧱 Architecture & pipeline order → `docs/architecture/`
- 🗺️ Data staging + catalogs (STAC/DCAT/PROV) → `../../data/README.md`
- 🧪 Test strategy + CI gates → `../../tests/README.md`
- 🔐 Security & disclosure → `../SECURITY.md`
- 🌐 Web viewer deployment notes → `../../web/README.md`

---

<p align="right"><a href="#-kansas-frontier-matrix-kfm">⬆️ Back to top</a></p>