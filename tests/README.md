# 🧪 Tests (KFM / Kansas Matrix System)

![CI](https://github.com/<ORG>/<REPO>/actions/workflows/ci.yml/badge.svg)
![Coverage](https://img.shields.io/badge/coverage-target%3A%2080%25-informational)
![Policy](https://img.shields.io/badge/policy-fail--closed-critical)
![Stack](https://img.shields.io/badge/stack-FastAPI%20%7C%20PostGIS%20%7C%20Neo4j%20%7C%20React-blue)

> This folder contains the automated tests (unit + integration + more) for the Kansas Frontier Matrix (KFM) system. 🧭🗺️  
> KFM is designed as a provenance-first pipeline → catalog → database → API → UI platform; our tests mirror that reality. ✅[^kfm-overview]

---

## 📌 Contents

- [⚡ Quickstart](#-quickstart)
- [🧭 KFM invariants we must never break](#-kfm-invariants-we-must-never-break)
- [🗂️ What belongs in `tests/`](#️-what-belongs-in-tests)
- [🧪 Test suites](#-test-suites)
- [🔁 CI gates (what runs on PRs)](#-ci-gates-what-runs-on-prs)
- [🧱 Writing great tests here](#-writing-great-tests-here)
- [🧯 Troubleshooting](#-troubleshooting)
- [📚 References](#-references)

---

## ⚡ Quickstart

### 0) Prereqs ✅
- Docker + Docker Compose (recommended for consistent DB + services)
- Python tooling (for backend tests)
- Node tooling (for frontend tests)

> **Heads-up:** port conflicts happen most often on `5432` (Postgres/PostGIS), `7474` (Neo4j), and typical app ports like `8000/3000`. 🧯[^ports]

### 1) Start the dev stack 🧱
```bash
docker-compose up -d
```

### 2) Run backend tests (FastAPI / Python) 🐍
```bash
docker-compose exec api pytest
```
> Backend tests are `pytest`-based and runnable inside the `api` container. ✅[^ci-tests]

### 3) Run frontend tests (React / TypeScript) ⚛️
```bash
docker-compose exec web npm test
```
> Frontend test command is `npm test` (or equivalent) as wired in the web app. ✅[^ci-tests]

### 4) Run policy checks (fail-closed governance) 🔒
```bash
conftest test .
```
> We use **Conftest (OPA)** to validate governance rules (licenses, required metadata, dataset manifests, etc.). Policy failures should **block merges** (“fail closed”). 🔐[^ci-policy]

---

## 🧭 KFM invariants we must never break

These are the *structural truths* of the system. If a change violates one, tests should catch it.

1) **Canonical flow:**  
   **Raw → Processed → Catalog/Provenance → Database → API → UI**  
   Tests should validate each hop produces what the next hop expects. ✅[^kfm-flow]

2) **UI never talks to databases directly** (PostGIS/Neo4j).  
   All access is mediated through the backend API. 🧱[^kfm-overview]

3) **Provenance-first outputs**  
   Data products must be traceable + attributable (metadata + provenance artifacts are not optional). 🧾[^kfm-overview]

4) **Governance fails closed**  
   If policy checks fail (missing license, missing required metadata, schema violations), the pipeline/CI should stop. 🔒[^ci-policy]

---

## 🗂️ What belongs in `tests/`

The repo-wide guide defines `tests/` as the place for automated tests across modules. 🧩[^tests-folder]

### ✅ Suggested layout (evolve as needed)
```text
tests/
├─ unit/                 # 🔬 pure logic tests (no network, no DB)
├─ integration/          # 🔌 API↔DB↔services integration tests
├─ e2e/                  # 🌐 end-to-end (API + UI flows)
├─ policy/               # 🔒 conftest/OPA validations + fixtures
├─ data/                 # 🧾 schema + metadata + provenance validations
├─ geo/                  # 🗺️ spatial correctness tests (CRS, GeoJSON, geometry)
├─ perf/                 # 🚀 performance/scale tests (optional but recommended)
└─ fixtures/             # 🧰 tiny deterministic sample datasets
```

### 🧠 Repo context (why this layout matches KFM)
The KFM monorepo is organized around:
- `api/` (FastAPI backend)
- `web/` (React + TypeScript frontend)
- `pipelines/` (data ingest/processing)
- `data/` (raw + processed datasets)
- `policy/` (governance rules)
- `docs/` (architecture + guides)  
…so tests should map cleanly to those boundaries. 🧭[^kfm-monorepo]

---

## 🧪 Test suites

### 1) 🔬 Unit tests (fast + deterministic)
**Goal:** prove core logic works without needing containers.

Examples:
- provenance builders (pure functions)
- schema validators
- coordinate conversion utilities
- parsing + normalizing metadata

**Why it’s easy in KFM:** KFM’s layered/clean architecture is designed so domain/service logic can be tested in isolation with mocks/stubs (DB and external services are behind interfaces). 🧱[^clean-arch]

---

### 2) 🔌 API integration tests (FastAPI ↔ PostGIS/Neo4j)
**Goal:** validate the backend API’s behavior + contracts.

Typical checks:
- endpoint status codes + error shapes
- pagination, filtering, sorting
- auth/roles (if enabled)
- DB query correctness & joins
- provenance links returned with datasets/layers

The blueprint explicitly calls out `api/tests/` and recommends FastAPI test clients + temporary DB/fixtures for integration coverage. ✅[^api-tests]

---

### 3) 🗺️ Geospatial correctness tests (CRS, geometry, GeoJSON)
**Goal:** prevent “maps that look right but are wrong.”

Suggested checks:
- **CRS sanity** (expected EPSG/CRS, coordinate ranges)
- geometry validity (self-intersections, empty geometries, winding)
- bounding box correctness
- point-in-polygon and distance sanity for known fixtures
- raster metadata sanity (pixel size, extent, nodata)

#### 🧩 GeoJSON gotcha (test it!)
If you generate GeoJSON from PostGIS, note that PostGIS can return *geometry-only* JSON rather than a complete GeoJSON Feature/FeatureCollection, so tests should assert final outputs are valid GeoJSON documents (FeatureCollection with Features + properties). 🧾[^geojson]

---

### 4) 🧭 Navigation & grid overlay tests (MGRS / UTM / lat-long)
KFM’s UI concept includes classical navigation aids (scale bar, north arrow) and optional grids like UTM/MGRS; if we implement those features, **we should test the conversions** and display logic. 🧭🗺️[^mgrs-ui]

Recommended tests:
- known lat/long ↔ UTM ↔ MGRS conversions (fixture-based)
- “read right then up” grid interpretation helpers (UI + helper utilities)
- formatting: precision, truncation rules, zone letters, etc.

The land navigation manual emphasizes the “read RIGHT then UP” convention when reporting grid coordinates—perfect for deterministic unit tests. ✅[^mgrs-rule]

---

### 5) 🧾 Data + metadata + license tests (quality gates)
**Goal:** make the catalog and downstream research trustworthy.

Suggested checks:
- required metadata fields exist
- temporal fields parse correctly
- provenance links exist for processed outputs
- license fields present + consistent
- dataset identifiers stable (no accidental renames)

Map-design literature also stresses metadata (including spatial reference info) and copyright/license awareness for digital GIS data—aligning well with KFM’s governance stance. 🧾⚖️[^metadata-copyright]

---

### 6) 🔒 Policy tests (Conftest / OPA)
**Goal:** encode governance so it’s enforceable.

Run locally:
```bash
conftest test .
```

Common patterns:
- keep policy rules in `policy/`
- add minimal fixtures in `tests/policy/fixtures/`
- write tests that prove the policy blocks bad states:
  - missing `license`
  - missing provenance file
  - missing required metadata
  - invalid schema versions

CI explicitly lists Conftest as part of the enforcement loop and encourages treating policy checks as merge gates. 🔐[^ci-policy]

---

### 7) 🤖 AI / “Focus Mode” tests (optional, but powerful)
If the backend integrates an LLM assistant, treat it like any other dependency: **stub it by default** and enable “live” tests only when explicitly requested.

#### 🧰 Local-first testing with Ollama
Ollama provides a local server + CLI for running open-source LLMs; it can be run via `ollama serve` and models can be run with `ollama run <model>`. 🤖[^ollama-run]  
It also exposes a local HTTP endpoint (commonly `http://localhost:11434`) and may offer an OpenAI-compatible API surface. 🌐[^ollama-api]

#### 🔧 Config hooks referenced in KFM blueprint
The blueprint mentions env-style configuration like `AI_BACKEND_URL` and `OLLAMA_MODEL` for local inference routing. 🧪[^kfm-ai-env]

Recommended AI test layers:
- **unit:** prompt templates, citation formatting, “no hallucinated sources” guards
- **integration:** request/response contract to AI gateway (mock server)
- **live (manual):** talk to a real local Ollama instance (opt-in only)

---

## 🔁 CI gates (what runs on PRs)

KFM’s CI is intended to run linting + tests on every PR. ✅  
The blueprint explicitly calls out:
- backend tests: `pytest`
- frontend tests: `npm test` (or similar)
- linters (Python + frontend)
- Conftest policy checks 🔒[^ci-tests]

> **Design intent:** broken tests or broken policy checks should block merges (“fail closed”). 🔐[^ci-policy]

---

## 🧱 Writing great tests here

### ✅ Principles (practical, not preachy)
- **Deterministic**: no random without a fixed seed
- **Fast**: default suite should be quick; heavier suites can be opt-in
- **Small fixtures**: tiny, legible sample datasets beat huge dumps
- **Evidence-first**: tests should produce artifacts/logs that explain failures
- **Automate early**: automated tests + CI are core to quality engineering practices (not a “nice to have”). 🧠[^qa-principles]

### 🧾 Suggested test naming
- `test_<module>_<behavior>_<expected>()`
- prefer “behavior” tests over implementation tests

### 🧪 Test pyramid (recommended)
- lots of unit tests 🔬
- fewer integration tests 🔌
- fewest e2e tests 🌐 (but still have them)

---

## 🧯 Troubleshooting

### 🧨 “Port already in use”
- Stop the conflicting local service, or change ports in `docker-compose.yml`
- Common conflicts: `5432` Postgres, `7474` Neo4j, and app ports like `8000/3000`. 🧯[^ports]

### 🧱 DB container not ready / migrations not applied
- Restart stack:
```bash
docker-compose down
docker-compose up -d
```
- re-run tests after DB is healthy

### 🧩 Flaky e2e tests
- Make sure fixtures are stable
- Avoid time-based assumptions; use explicit waits / polling on readiness endpoints
- Prefer API stubs for non-critical external integrations

---

## 📚 References

> These are the core project documents that informed this test strategy. 📌  
> (In this chat, the `filecite` markers link to the source PDFs; in-repo, consider placing them under `docs/library/` and updating links.)

- **KFM Blueprint**:  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)  
  - Architecture, repo layout, CI/test commands, policy posture. 🧱  
  - See citations: [^kfm-overview], [^kfm-monorepo], [^ci-tests], [^ci-policy]

- **Repo Markdown Guide / Structure**:  [oai_citation:1‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
  - Defines `tests/` role across modules. 🧩[^tests-folder]

- **Ollama Guide (local LLM testing)**:  [oai_citation:2‡Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf](sediment://file_00000000a58071f586f00793dee712d6)  
  - `ollama serve`, `ollama run`, local API conventions. 🤖[^ollama-run] [^ollama-api]

- **Geospatial Analysis Cookbook (PostGIS ⇄ GeoJSON)**:  [oai_citation:3‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)  
  - Notes about GeoJSON output completeness. 🗺️[^geojson]

- **Map Reading & Land Navigation (FM 3-25.26)**:  [oai_citation:4‡Map Reading & Land Navigation.pdf](sediment://file_00000000b14c7230b1b262ddd9df4e5d)  
  - Grid coordinate conventions (“right then up”). 🧭[^mgrs-rule]

- **Making Maps (GIS map design + metadata/copyright)**:  [oai_citation:5‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](sediment://file_00000000602471f786dfbbaac9329fb9)  
  - Coordinate systems + metadata expectations. 🧾[^metadata-copyright]

- **Scientific Method / Research / Master Coder Protocol**:  [oai_citation:6‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)  
  - Reinforces automated testing + CI as quality practice. 🧠[^qa-principles]

---

## 🧾 Footnotes (source anchors)

[^kfm-overview]: KFM is described as a pipeline → catalog → database → API → UI system with a provenance-first, traceable design.  [oai_citation:7‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

[^kfm-flow]: Canonical flow is called out as “Raw → Processed → Catalog/Prov → Database → API → UI”.  [oai_citation:8‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

[^kfm-monorepo]: Monorepo layout includes `api/` (FastAPI), `web/` (React+TS), `pipelines/`, `data/`, `policy/`, `docs/`.  [oai_citation:9‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

[^ports]: Common port conflicts noted for Postgres (`5432`), Neo4j (`7474`), and typical app ports (`8000/3000`).  [oai_citation:10‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

[^ci-tests]: CI expectations: backend `pytest`, frontend `npm test` (or similar), plus linters. Also suggests running backend tests locally via `docker-compose exec api pytest`.  [oai_citation:11‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

[^ci-policy]: Conftest/OPA policy checks are described as a way to enforce governance (e.g., licenses and metadata) and align with “fail closed”.  [oai_citation:12‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

[^api-tests]: Blueprint notes backend tests live under `api/tests/` and recommends FastAPI’s test client plus a temporary DB or fixtures for integration testing.  [oai_citation:13‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) [oai_citation:14‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

[^clean-arch]: The blueprint explains that service/domain logic is decoupled from database access, enabling isolation testing with mock data.  [oai_citation:15‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

[^tests-folder]: The repo guide describes `tests/` as the folder for automated tests (unit + integration) for modules.  [oai_citation:16‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

[^geojson]: Cookbook note: PostGIS may not output complete GeoJSON (FeatureCollection syntax), so additional wrapping/validation can be needed.  [oai_citation:17‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)

[^mgrs-ui]: Blueprint describes UI support for grid overlays like UTM/MGRS and displaying coordinates in multiple formats; it explicitly references “read right and up”.  [oai_citation:18‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

[^mgrs-rule]: Land navigation manual: when reading/reporting grid coordinates, “always read to the RIGHT and then UP”.  [oai_citation:19‡Map Reading & Land Navigation.pdf](sediment://file_00000000b14c7230b1b262ddd9df4e5d)

[^metadata-copyright]: Map design guidance emphasizes coordinate systems, conversions, and the importance of metadata (including spatial reference information) and copyright awareness for digital GIS data.  [oai_citation:20‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](sediment://file_00000000602471f786dfbbaac9329fb9) [oai_citation:21‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](sediment://file_00000000602471f786dfbbaac9329fb9) [oai_citation:22‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](sediment://file_00000000602471f786dfbbaac9329fb9)

[^kfm-ai-env]: Blueprint mentions environment-driven configuration for AI routing (e.g., `AI_BACKEND_URL`, `OLLAMA_MODEL`).  [oai_citation:23‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

[^ollama-run]: Ollama guide: models can be run via `ollama run <model>` and it will download/pull the model if needed.  [oai_citation:24‡Comprehensive Guide to Ollama and Its Supported Open-Source LLMs.pdf](file-service://file-WLPhJVNoBxYKcy3utQSwBi)

[^ollama-api]: Ollama guide: Ollama can run as a local server and exposes a local HTTP endpoint (commonly `http://localhost:11434`) with API options (including OpenAI compatibility).  [oai_citation:25‡Comprehensive Guide to Ollama and Its Supported Open-Source LLMs.pdf](file-service://file-WLPhJVNoBxYKcy3utQSwBi) [oai_citation:26‡Comprehensive Guide to Ollama and Its Supported Open-Source LLMs.pdf](file-service://file-WLPhJVNoBxYKcy3utQSwBi)

[^qa-principles]: Protocol doc stresses automated testing, CI/CD, and test coverage as part of quality assurance practices.  [oai_citation:27‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)