<a id="top"></a>

# 🧰 `.github/workflows/` — CI/CD for Kansas Frontier Matrix (KFM)

[![CI](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/ci.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/ci.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml)
[![Pages](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pages.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pages.yml)

![DevSecOps](https://img.shields.io/badge/DevSecOps-enabled-black)
![Data QA](https://img.shields.io/badge/data-QA%20gates-purple)
![Provenance](https://img.shields.io/badge/provenance-STAC%20%7C%20DCAT%20%7C%20PROV-6f42c1)
![Boring by design](https://img.shields.io/badge/CI-boring%20by%20design-success)

> 🧭 This folder contains GitHub Actions workflows that keep KFM **buildable**, **testable**, **secure**, and **shippable** — across **pipelines → catalogs → graph → API → UI**.
>
> ✅ **North Star:** CI/CD protects *trust* (provenance + integrity) first, then *speed* (caching + parallelism).  
> 🧾 **KFM order (don’t break it):** **ETL → Metadata (STAC/DCAT/PROV) → Graph → API → UI**.

> [!IMPORTANT]
> CI is intentionally **boring** (predictable, repeatable, least‑privilege, auditable).  
> The data, story, and models are the interesting part. 🗺️✨

---

## ⚡ Quick links

| Action | Link |
|---|---|
| ✅ All Action runs | https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions |
| 📦 Releases | https://github.com/bartytime4life/Kansas-Frontier-Matrix/releases |
| 🐛 Issues | https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues |
| 🤝 `.github/` Collaboration hub | [`../README.md`](../README.md) |
| 🧭 Repo root overview | [`../../README.md`](../../README.md) |
| 🔐 Security policy | [`../../SECURITY.md`](../../SECURITY.md) *(or `../SECURITY.md` if you keep it inside `.github/`)* |

> [!TIP]
> If a badge 404s, that workflow file probably doesn’t exist yet.  
> This README doubles as a **spec + target shape** for what we intend to add next. 🧾

---

<details>
<summary><b>🧭 Table of contents</b></summary>

- [📺 Mermaid Workflow TV](#-mermaid-workflow-tv)
- [🧠 CI/CD principles](#-cicd-principles)
- [📁 What lives here](#-what-lives-here)
- [🗂️ Workflow catalog](#️-workflow-catalog-baseline--lanes)
- [🧱 KFM-MDP promotion gates](#-kfm-mdp-promotion-gates-data--models)
- [✅ Quality gates](#-quality-gates-what-must-pass)
- [🗺️ Data + catalog gates](#️-data--catalog-gates-kfm-specific)
- [🕸️ Graph + semantics gates](#️-graph--semantics-gates)
- [🧪 Integration tests](#-integration-tests-postgis--graph--api)
- [🌐 Web UI gates](#-web-ui-gates-responsive--webgl)
- [🔐 Security scanning](#-security-scanning-sast-deps-secrets-containers)
- [📦 Artifacts & traceability](#-artifacts--traceability)
- [🧷 Secrets & environments](#-secrets--environments-least-privilege-by-default)
- [🧩 Reusable workflows & composite actions](#-reusable-workflows--composite-actions)
- [🛠️ Starter templates](#️-starter-templates-copy--paste)
- [🧰 Debug locally](#-debugging-workflows-locally)
- [🧾 New workflow checklist](#-adding-a-new-workflow-checklist)
- [📚 Reference library & influence map](#-reference-library--influence-map)

</details>

---

## 📺 Mermaid Workflow TV

A “TV guide” of how work moves through KFM CI/CD (fast lane → promotion → heavy jobs). 📺🧪

```mermaid
flowchart TB
  subgraph PR["🧪 PR Lane (fast • required)"]
    PR1["ci.yml<br/>lint • unit • typecheck"]
    PR2["catalog-qa.yml<br/>STAC/DCAT quick gate"]
    PR3["security.yml<br/>dep review • secrets • scans"]
    PR4["ui.yml<br/>build • lint • tests"]
  end

  subgraph MAIN["🚀 Main Lane (promotion)"]
    M1["docker.yml<br/>build • tag • push (GHCR)"]
    M2["publish-catalog.yml<br/>promote catalogs + provenance"]
    M3["pages.yml<br/>docs / viewer deploy (optional)"]
  end

  subgraph NIGHTLY["🌙 Nightly Lane (slow • scheduled)"]
    N1["integration.yml<br/>PostGIS + graph + API contracts"]
    N2["data-refresh.yml<br/>ETL refresh + diffs"]
    N3["model-regression.yml<br/>metrics + drift + UQ baselines"]
    N4["perf.yml<br/>bundle size + query timing (budgeted)"]
  end

  subgraph RELEASE["🏷️ Release Lane (tags)"]
    R1["release.yml<br/>notes + artifacts + provenance"]
    R2["sbom-attest.yml<br/>SBOM + attestations (recommended)"]
  end

  PR1 --> M1
  PR2 --> M2
  PR3 --> M1
  PR4 --> M3

  M1 --> R1
  M2 --> R1
  R1 --> R2

  PR1 --> N1
  PR2 --> N2
  N1 --> N2
  N2 --> N3
  N3 --> N4
```

> [!TIP]
> Mermaid on GitHub can be picky. To avoid parse errors:
> - keep **one edge per line**
> - use simple IDs (`PR1`, `M1`, etc.)
> - labels go inside quotes if punctuation/emoji cause trouble 😄

---

## 🧠 CI/CD principles

### ✅ 1) “Contracts over vibes”
KFM treats key interfaces as contracts:
- 📜 **API** contracts (OpenAPI / GraphQL)
- 🗂️ **Catalog** contracts (STAC/DCAT)
- 🧾 **Lineage** contracts (W3C PROV)
- 🕸️ **Graph** contracts (ontology IDs + relationship shapes)
- 📈 **Model / analysis** contracts (metrics + seeds + manifests)

If a contract drifts, CI should fail **before** it ships. ✅

### ✅ 2) “Layered gates” beat “mega workflows”
KFM is modular, so CI mirrors that structure:

1) **Code gate** → lint, unit tests, type checks  
2) **Metadata gate** → catalogs, schemas, provenance checks  
3) **Integration gate** → real DBs/services via containers  
4) **Security gate** → SAST, dependency review, secret scanning, container scan  
5) **Promotion gate** → publish/deploy with protected environments

This prevents CI from becoming a single slow pipeline nobody trusts. 🛣️

### ✅ 3) Deterministic, idempotent, auditable
- same inputs → same outputs (seeded, config-driven)
- artifacts and logs are uploaded on failure
- promotion is atomic (no half-published catalogs)

### ✅ 4) Least privilege by default 🔐
- minimal `permissions:` per workflow/job
- no secrets on untrusted PRs (especially forks)
- avoid `pull_request_target` unless you *really* know why

---

## 📁 What lives here

> Target shape — add as needed, but keep intent stable.

```text
📁 .github/workflows/
├─ 🧪 ci.yml                        # fast PR lane: lint + unit tests + type checks
├─ 🌐 ui.yml                        # frontend lint/test/build (recommended)
├─ 🧾 catalog-qa.yml                 # STAC/DCAT quick gate + link check (recommended)
├─ 🕸️ graph-qa.yml                   # ontology/ID/schema checks for graph assets (recommended)
├─ 🧬 integration.yml                # PostGIS + graph + API contract integration tests (nightly)
├─ 🔐 codeql.yml                     # SAST (CodeQL)
├─ 🔐 security.yml                   # dep review + secret scan helpers + container scan hooks
├─ 🐳 docker.yml                     # build/push images (GHCR)
├─ 🚦 publish-catalog.yml            # catalog promotion (env-gated)
├─ 🌙 data-refresh.yml               # scheduled ETL + catalog refresh + diffs (optional)
├─ 📈 model-regression.yml           # metrics drift checks + UQ baselines (optional)
├─ ⚡ perf.yml                        # bundle size + query timing budgets (optional)
├─ 📚 docs.yml                       # docs build + link checks (optional)
├─ 🌐 pages.yml                      # GitHub Pages deploy (optional)
├─ 🏷️ release.yml                    # release packaging + changelog + provenance (optional)
├─ 🧾 sbom-attest.yml                # SBOM + build attestations (recommended later)
└─ 📄 README.md                      # you are here 👋
```

---

## 🗂️ Workflow catalog (baseline + lanes)

> If a workflow file isn’t present yet, treat this table as the **spec** for creating it.

| Workflow 📄 | Lane | Protects ✅ | Typical triggers ⏱️ | Budget 🎯 | Outputs 📦 |
|---|---|---|---|---:|---|
| `ci.yml` | PR | lint + unit + typecheck | `pull_request`, `push` | ≤ 10 min | junit, coverage |
| `ui.yml` | PR | web lint/test/build | `pull_request`, `push` | ≤ 12 min | build logs, bundle report |
| `catalog-qa.yml` | PR | STAC/DCAT quick gate | PR paths (`data/**`) | ≤ 5 min | QA report |
| `graph-qa.yml` | PR | graph schema/IDs | PR paths (`graph/**`, `docs/ontology/**`) | ≤ 5 min | QA report |
| `security.yml` | PR | dependency review + secret checks | PR + schedule | ≤ 15 min | SARIF/logs |
| `codeql.yml` | scheduled | SAST | schedule + PR | n/a | SARIF |
| `integration.yml` | nightly | PostGIS + graph + API contracts | schedule + dispatch | 10–45 min | logs, junit |
| `docker.yml` | main/tag | container build & push | `push main`, tags | ≤ 25 min | OCI images |
| `publish-catalog.yml` | main/env | catalog promotion | `workflow_dispatch` + env approvals | n/a | published catalogs |
| `pages.yml` | main | docs/viewer publish | `push main`, dispatch | n/a | Pages deploy |
| `release.yml` | tag | release notes + pinned artifacts | tags | n/a | release assets |
| `sbom-attest.yml` | tag | SBOM + attestations | tags | n/a | SBOM, attest |

---

## 🧱 KFM-MDP promotion gates (data + models)

KFM uses an intentionally gate-enforced lifecycle: **stage → validate → publish**.

```mermaid
flowchart LR
  RAW["📥 Stage<br/>raw inputs"] --> VAL["🔎 Validate<br/>schema + links + bounds + license"]
  VAL -->|pass ✅| PUB["📦 Publish (atomic)<br/>assets + catalogs + provenance"]
  VAL -->|fail ❌| STOP["🧯 Stop / Rollback<br/>no broken catalogs"]
  PUB --> FED["🌐 Federation-ready<br/>STAC + DCAT"]
```

### ✅ What “promotion” means here
Promotion is not “copying files somewhere.” It means:
- 🗂️ catalogs are complete (STAC/DCAT)
- 🧾 lineage exists (PROV, inputs → transforms → outputs)
- 🧪 QA has passed (links, schema, bounds, sensitive-location rules)
- 🔐 access rules are respected (public vs restricted)

> [!IMPORTANT]
> If it touches `data/**`, expect **Catalog QA** and **metadata contracts** to run.

---

## ✅ Quality gates (what must pass)

### 1) Code health 🧼
- formatting + linting (fast fail)
- unit tests (core logic)
- type checks where applicable
- basic packaging sanity (`pip install`, `npm ci`, etc.)

### 2) Metadata + contracts 🗃️
- JSON/YAML schema validity
- STAC/DCAT/PROV requirements (license, providers, extensions, links)
- link integrity (top-level asset hrefs)
- provenance presence (source + processing steps)

### 3) Integration fidelity 🧪
- PostGIS integration
- graph DB integration (if used)
- API contract tests (OpenAPI/GraphQL snapshots)
- tiny end-to-end pipeline on fixtures (nightly/dispatch)

### 4) Security posture 🔐
- dependency review (PR gate)
- CodeQL (SAST)
- secret scanning (prevents foot-guns)
- container scan on promoted images (recommended)

### 5) Governance & policy 🏛️
- license + attribution checks for new data
- optional: sensitive-location / redaction checklist automation
- optional: model cards required for ML/analytics outputs

---

## 🗺️ Data + catalog gates (KFM-specific)

### ✅ The STAC/DCAT quick gate (recommended)
Run a fast, deterministic QA pass on every PR that touches catalogs:

- `license` present + non-empty  
- `providers` present + non-empty  
- `stac_extensions` present *(warn if empty; fail if missing)*  
- top-level `links[].href` **HEAD/GET link-check**  
- optional: enforce “Stable-only” extensions for **production** catalogs

### 🧭 CRS + projection sanity checks
Geospatial bugs often come from silent CRS drift:
- required EPSG values present where expected
- bbox/footprint fields valid
- raster assets include grid metadata where required

### 🧪 Geometry validity checks
For vector assets:
- invalid/self-intersecting geometries
- empty geometries
- unexpected coordinate ranges (Kansas bounds sanity)

> [!CAUTION]
> PR gates should be **fast** (fixtures + metadata).  
> Deep checks belong in **nightly lanes**.

---

## 🕸️ Graph + semantics gates

If you store ontology schemas, entity definitions, or graph ingestion manifests:

- ✅ stable IDs (no renaming without migration notes)
- ✅ relationship shape validation (allowed types/edges)
- ✅ reference integrity (entity IDs referenced by Story Nodes exist)
- ✅ temporal schema validation (OWL-Time-like structures)
- ✅ optional: “graph build dry-run” on a small fixture dataset

💡 Why this matters: Story Nodes + Focus Mode depend on stable entity IDs and traceable links, not ad-hoc strings.

---

## 🧪 Integration tests (PostGIS + Graph + API)

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

**Neo4j (optional)**
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
> The #1 cause of CI flake is “tests started before DB was ready.”  
> Always add health checks + explicit waits. ✅

### Option B: Docker Compose (multi-service parity)
Best when you need API + workers + DB + cache for realistic end-to-end tests.

---

## 🌐 Web UI gates (responsive + WebGL)

KFM’s UI is map-first and often includes WebGL content (MapLibre/Cesium-style).

Recommended CI checks:
- ✅ `npm ci` (lockfile respected)
- ✅ lint (`eslint`) + format (`prettier`)  
- ✅ typecheck (`tsc --noEmit`)
- ✅ tests (unit/component)
- ✅ build (`npm run build`) + size budgets (optional)

WebGL-specific hygiene:
- treat 3D assets (tilesets/models) as **untrusted inputs**
- do not allow unsafe HTML injection patterns in popups/tooltips
- keep bundle size predictable (budgets catch bloat early)

---

## 🔐 Security scanning (SAST, deps, secrets, containers)

Baseline expectations:
- ✅ Dependency Review on PRs
- ✅ CodeQL scanning (Python + JS/TS + Actions as applicable)
- ✅ Secret scanning + push protection (GitHub features)
- ✅ Container scan on `main` + tags (recommended)

Supply chain hardening (recommended later):
- SBOM generation (SPDX/CycloneDX)
- build attestations (SLSA-ish)
- signed images (Sigstore/cosign)

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
- optional: provenance outputs (`prov.jsonld`, run manifests)

💡 Naming tip: include workflow + sha → `ci-unit-${{ github.sha }}`

---

## 🧷 Secrets & environments (least privilege by default)

Common secrets:
- `GITHUB_TOKEN` (often enough for GHCR with `packages: write`)
- deploy credentials (only in protected environments)
- third-party tokens (scoped + rotated)

✅ Use GitHub **Environments** (`dev`, `stage`, `prod`) to:
- scope secrets safely
- require approvals for `prod`
- attach deploy history to commits

Recommended permissions defaults:

```yaml
permissions:
  contents: read
```

Escalate only when needed (examples):
- `packages: write` for GHCR push
- `security-events: write` for SARIF upload
- `id-token: write` for OIDC to cloud (preferred over long-lived keys)

---

## 🧩 Reusable workflows & composite actions

When workflows multiply, duplication becomes entropy. Prefer:
- ✅ **Reusable workflows** (`workflow_call`) for common CI building blocks
- ✅ **Composite actions** for tiny shared step sets (setup + caching)

Suggested layout:

```text
📁 .github/
├─ 📁 actions/
│  ├─ 📁 setup-python/
│  └─ 📁 setup-node/
└─ 📁 workflows/
   ├─ 🔁 _reusable-python-ci.yml
   ├─ 🔁 _reusable-node-ci.yml
   └─ ...
```

Example: call a reusable workflow
```yaml
jobs:
  python:
    uses: ./.github/workflows/_reusable-python-ci.yml
    with:
      python-version: "3.12"
```

---

## 🛠️ Starter templates (copy / paste)

> Keep PR checks fast, make slow lanes scheduled, and always upload logs on failure. 🥇

<details>
<summary><strong>🧪 <code>ci.yml</code> — Python Lint + Unit Tests (fast PR lane)</strong></summary>

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
    runs-on: ubuntu-latest
    timeout-minutes: 15

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
          cache: "pip"

      - name: Install deps
        run: |
          python -m pip install -U pip
          # Adjust paths for monorepo layouts:
          if [ -f api/requirements.txt ]; then pip install -r api/requirements.txt; fi
          if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
          if [ -f requirements-dev.txt ]; then pip install -r requirements-dev.txt; fi

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
<summary><strong>🌐 <code>ui.yml</code> — Web UI Lint + Test + Build (recommended)</strong></summary>

```yaml
name: UI

on:
  pull_request:
    paths:
      - "web/**"
      - ".github/workflows/ui.yml"
  push:
    branches: [main]
    paths:
      - "web/**"

permissions:
  contents: read

concurrency:
  group: ui-${{ github.ref }}
  cancel-in-progress: true

jobs:
  web:
    runs-on: ubuntu-latest
    timeout-minutes: 15
    defaults:
      run:
        working-directory: web

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-node@v4
        with:
          node-version: "20"
          cache: "npm"
          cache-dependency-path: web/package-lock.json

      - name: Install
        run: npm ci

      - name: Lint
        run: npm run lint --if-present

      - name: Typecheck
        run: npm run typecheck --if-present

      - name: Test
        run: npm test --if-present

      - name: Build
        run: npm run build

      - name: Upload build report (optional)
        uses: actions/upload-artifact@v4
        if: always()
        with:
          name: web-build-${{ github.sha }}
          path: |
            web/dist/**
            web/.eslintcache
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
      - ".github/workflows/catalog-qa.yml"
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
          if [ -f requirements-dev.txt ]; then pip install -r requirements-dev.txt; fi

      - name: Run catalog QA
        run: |
          # Adjust flags to match your tool implementation
          python tools/validation/catalog_qa/run_catalog_qa.py \
            --root data/ \
            --glob "**/collection.json" \
            --fail-on-warn

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
  integration:
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

      # Optional graph service:
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
          if [ -f api/requirements.txt ]; then pip install -r api/requirements.txt; fi
          if [ -f requirements-dev.txt ]; then pip install -r requirements-dev.txt; fi

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
            logs/**
            .pytest_cache/**
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

  container-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Build image (local)
        run: docker build -t kfm:scan .
      - name: Scan image (TODO)
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
          if [ -d web/dist ]; then cp -R web/dist/* dist/; fi
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
1) ✅ run the same commands CI runs (best parity)  
2) 🐳 use Compose profiles to mimic integration dependencies  
3) 🧪 use `act` to simulate Actions locally *(helpful, not perfect)*

---

## 🧾 Adding a new workflow checklist

- [ ] Name jobs after outcomes (`lint`, `unit-tests`, `catalog-qa`, `integration-tests`, `build-image`)
- [ ] Keep PR checks fast (aim ≤ ~10–12 minutes)
- [ ] Put slow jobs behind schedules or manual dispatch
- [ ] Cache dependencies (pip/npm) and Docker layers
- [ ] Upload artifacts on failure (logs are gold 🥇)
- [ ] Pin action versions (at least major versions; commit SHA pin later if desired)
- [ ] Avoid secrets on `pull_request` from forks
- [ ] Use minimal `permissions:` and elevate only when needed
- [ ] Add `concurrency:` cancellation to reduce queue noise
- [ ] Keep the KFM order intact: **ETL → Metadata → Graph → API → UI**
- [ ] If data/model outputs ship: add **PROV + checksums + manifest** expectations

---

## 📚 Reference library & influence map

> ⚠️ Reference materials may have different licenses than repo code.  
> Keep them under `docs/library/` (or outside the repo) and respect upstream terms.

<details>
<summary><strong>🧠 Why CI/CD mentions the “reading pack”</strong></summary>

KFM is a hybrid platform: **GIS + data engineering + web + modeling + governance**.  
CI/CD is where those disciplines turn into repeatable guardrails.

The docs below influence:
- ✅ data integrity gates (catalogs, provenance, checksums)
- ✅ modeling hygiene (V&V, UQ, experimental design)
- ✅ secure-by-default workflows (DevSecOps + supply chain)
- ✅ performance strategy (caching, parallelism, scale lanes)
- ✅ map/UI constraints (responsive + WebGL realities)

</details>

<details>
<summary><strong>📚 Full reference list (project files)</strong></summary>

### 🧭 Canonical KFM system specs
- `docs/specs/Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.docx`

### 🛰️ Modeling, simulation, V&V, and UQ
- `docs/library/Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf`
- `docs/library/Understanding Statistics & Experimental Design.pdf`
- `docs/library/regression-analysis-with-python.pdf`
- `docs/library/Regression analysis using Python - slides-linear-regression.pdf`
- `docs/library/graphical-data-analysis-with-r.pdf`
- `docs/library/think-bayes-bayesian-statistics-in-python.pdf`
- `docs/library/scipy-lecture-notes-1.pdf`
- `docs/library/Understanding Machine Learning: From Theory to Algorithms (2014).pdf`
- `docs/library/Deep Learning for Coders with fastai and PyTorch - Deep.Learning.for.Coders.with.fastai.and.PyTorchpdf` *(note: availability/indexing may vary)*

### 🗺️ GIS + cartography + spatial databases
- `docs/library/python-geospatial-analysis-cookbook.pdf`
- `docs/library/PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf`
- `docs/library/making-maps-a-visual-guide-to-map-design-for-gis.pdf`
- `docs/library/Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf`

### 🛰️ Remote sensing workflows
- `docs/library/Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf`

### 🌐 Web, UX, and graphics (WebGL / 3D)
- `docs/library/responsive-web-design-with-html5-and-css3.pdf`
- `docs/library/webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf`
- `docs/library/compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf`

### ⚙️ Systems & scalability
- `docs/library/Scalable Data Management for Future Hardware.pdf`
- `docs/library/concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf`
- `docs/library/Data Spaces.pdf`

### 🧮 Graphs, optimization, and advanced math
- `docs/library/Spectral Geometry of Graphs.pdf`
- `docs/library/Generalized Topology Optimization for Structural Design.pdf`

### ❤️ Ethics, autonomy, governance, and AI/legal framing
- `docs/library/Introduction to Digital Humanism.pdf`
- `docs/library/Principles of Biological Autonomy - book_9780262381833.pdf`
- `docs/library/On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf`

### 🛡️ Security (defensive references)
- `docs/library/ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf`
- `docs/library/Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf`

### 🧰 General programming shelf (bundles)
- `docs/library/A programming Books.pdf`
- `docs/library/B-C programming Books.pdf`
- `docs/library/D-E programming Books.pdf`
- `docs/library/F-H programming Books.pdf`
- `docs/library/I-L programming Books.pdf`
- `docs/library/M-N programming Books.pdf`
- `docs/library/O-R programming Books.pdf`
- `docs/library/S-T programming Books.pdf`
- `docs/library/U-X programming Books.pdf`

</details>

---

<p align="right"><a href="#top">⬆️ Back to top</a></p>