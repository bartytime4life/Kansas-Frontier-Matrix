# 🏎️ Performance & Load Testing (`tests/perf`)

![Scope](https://img.shields.io/badge/scope-API%20%7C%20DB%20%7C%20Pipelines%20%7C%20UI-informational)
![Discipline](https://img.shields.io/badge/discipline-repeatable%20benchmarks-blueviolet)
![Goal](https://img.shields.io/badge/goal-catch%20regressions%20early-brightgreen)
![Ethos](https://img.shields.io/badge/ethos-provenance--first%20%F0%9F%A7%AD-blue)

> [!IMPORTANT]
> KFM is built as a **pipeline → catalog/provenance → database → API → UI** system.  
> Performance tests should respect the same “truth path” as production (no sneaky shortcuts unless the test is explicitly a *database microbenchmark*). 🧭

---

## 📌 Why this folder exists

Performance is a feature. This directory is where we **measure**, **compare**, and **prevent regressions** across the KFM stack:

- 🧱 **Data pipelines**: ingest → process → catalog/prov generation → database load
- 🗺️ **Geospatial runtime**: PostGIS/PostgreSQL query latency & throughput
- 🕸️ **Knowledge graph**: Neo4j traversals and relationship queries
- ⚙️ **Backend API**: FastAPI REST/GraphQL endpoints, tile endpoints, search endpoints
- 🧠 **Focus Mode AI**: retrieval + tool calls + LLM response time (and error rates)
- 🧑‍💻 **UI experience** (optional but recommended): map load, layer toggles, timeline scrubbing, 2D/3D switches

---

## TL;DR 🚀

1. 🐳 Start the stack (Compose)
2. 🌱 Seed a **representative** dataset
3. 🧪 Run the perf suite(s)
4. 📦 Save a report with **full run metadata** (git SHA, config, dataset, environment)

---

## 🧠 Benchmarking principles (KFM-flavored)

### ✅ Do
- **Decide what you’re optimizing for**: latency targets vs max throughput.
- **Start small, then scale** (phased approach): validate your harness before big runs.
- **Warm caches intentionally** and measure **steady state** (don’t benchmark cold starts by accident).
- **Instrument first**: you can’t optimize what you can’t see (DB stats, API metrics, system metrics).
- **Document everything**: environment, dataset, workload parameters, warmup strategy, versions.

### ❌ Don’t
- Don’t “win” a benchmark by bypassing the pipeline/catalog/prov layer (unless the suite is explicitly `db_micro/`).
- Don’t trust results that can’t be reproduced.
- Don’t hide tail latencies (watch P95/P99/P99.9).
- Don’t ignore coordinated omission risks in latency measurement (tooling + methodology matters).

---

## 🧱 What we measure

### Core metrics 📏
- **Latency**: P50 / P95 / P99 / P99.9 (plus max)  
- **Throughput**: req/s, tiles/s, queries/s, rows/s, features/s  
- **Correctness signals**: error rate, timeouts, partial failures, response validation  
- **Resource usage**: CPU, RAM, disk I/O, network, container limits  
- **System-specific**:
  - PostGIS: query plans (EXPLAIN), index usage, cache hit ratios
  - Neo4j: traversal depth costs, hotspot node patterns
  - Pipelines: wall time per stage, rows/features processed, I/O amplification
  - AI: retrieval latency, tool-call counts, response time distribution

---

## 🐳 Quick start (local dev)

> [!NOTE]
> The blueprint expects a Docker Compose dev workflow with PostGIS + Neo4j + API + web UI.  
> Typical ports include **5432** (Postgres), **7474** (Neo4j), **8000** (API), **3000** (web). 🧷

### 1) Start the stack
```bash
docker-compose up -d
```

### 2) Verify services are reachable
- API docs: `http://localhost:8000/docs`
- Web UI: `http://localhost:3000`
- Neo4j Browser: `http://localhost:7474`

### 3) Seed a dataset (sample/representative)
Examples (depending on what exists in your repo):
```bash
# Option A: a convenience script (if present)
docker-compose exec api python scripts/init_sample_data.py

# Option B: run a pipeline directly (example)
docker-compose exec api python pipelines/import_rainfall.py
```

### 4) Run perf suites
This repo may wire perf tests via any of these patterns—pick the one your project uses:

```bash
# Option A: pytest marker pattern (recommended)
docker-compose exec api pytest -m perf tests/perf

# Option B: a custom runner module (if present)
docker-compose exec api python -m tests.perf.run --suite api_smoke

# Option C: load tool (k6/locust/vegeta) driven from host
# (see suites below)
```

---

## 🧪 Perf suites

<details>
<summary><strong>🧱 Pipelines</strong> — ingest → processed → catalog/prov → DB</summary>

**Goal:** measure *end-to-end* pipeline throughput + stage timing.

Typical checks:
- time per stage (raw parse, transform, enrich, metadata, PROV generation, DB insert)
- rows/features processed per second
- disk + network I/O (especially when mounting volumes)

Recommended outputs:
- `reports/<run>/pipeline_timeline.json`
- `reports/<run>/prov_run_manifest.json` (see template below)

</details>

<details>
<summary><strong>🗺️ PostGIS / PostgreSQL</strong> — spatial query performance</summary>

**Goal:** ensure spatial queries remain fast as datasets grow.

Representative query classes:
- bbox queries (viewport)
- point-in-polygon
- distance/radius queries
- clustering/aggregation
- tile-backed feature extraction (if applicable)

Deliverables:
- query set (SQL files)
- dataset manifest (size + checksums)
- EXPLAIN plans saved with results

</details>

<details>
<summary><strong>🕸️ Neo4j</strong> — knowledge graph traversal & joins</summary>

**Goal:** prevent graph traversals from becoming “accidentally exponential”.

Representative query classes:
- story node neighborhood expansion
- entity-to-source provenance hops
- multi-filter traversals (time + place + topic)

Deliverables:
- cypher query set
- traversal depth limits + expected cardinalities

</details>

<details>
<summary><strong>⚙️ API (FastAPI)</strong> — REST/GraphQL endpoints</summary>

**Goal:** measure user-facing latency and throughput under realistic load.

Suggested endpoint mix (adjust to your API):
- `GET /datasets`
- `GET /features/{id}`
- `GET /search?q=...`
- `POST /ai/query`
- GraphQL queries (if enabled at `/graphql`)
- tile endpoints (vector/raster) if present

Load modes:
- **Latency-focused:** fixed throughput, measure tail percentiles
- **Throughput-focused:** saturate until a resource maxes out

</details>

<details>
<summary><strong>🧠 Focus Mode AI</strong> — retrieval + tools + LLM response</summary>

**Goal:** keep AI assistance responsive while remaining **governed** and **source-grounded**.

Measure:
- end-to-end response time
- retrieval time (semantic search / DB reads)
- tool-call count & latency
- timeout rate and fallback behaviors

Also track:
- response size (tokens/chars)
- error classes (tool failures vs model failures)

</details>

<details>
<summary><strong>🧑‍💻 UI (optional)</strong> — perceived performance</summary>

**Goal:** measure *what users feel*.

Candidate scenarios:
- first map render
- layer toggle (tile requests & render time)
- timeline scrubbing (state sync)
- 2D↔3D switch (MapLibre ↔ Cesium)

Tooling idea:
- Playwright trace runs (recommended)
- Lighthouse runs for baseline front-end metrics

</details>

---

## 🗂️ Suggested directory layout

```text
📁 tests/
└─ 📁 perf/                                   ⚡ performance + benchmarking lane
   ├─ 📄 README.md                              👈 you are here 📍
   ├─ 📁 suites/                                🧪 benchmark entrypoints (python/js)
   │  ├─ 📁 api/                                🌐 API latency/throughput suites
   │  ├─ 📁 db_postgis/                         🐘 PostGIS query/mutation suites
   │  ├─ 📁 db_neo4j/                            🕸️ Neo4j traversal/index suites
   │  ├─ 📁 pipelines/                          🏗️ ETL/pipeline runtime suites
   │  ├─ 📁 ai/                                 🤖 RAG/LLM evaluation + latency suites
   │  └─ 📁 ui/                                 🖥️ UI performance (render, interaction, trace replay)
   ├─ 📁 workloads/                             🎛️ workload definitions (YAML/JSON)
   ├─ 📁 queries/                               🧾 SQL/Cypher bundles (versioned!)
   ├─ 📁 datasets/                              📦 dataset manifests (size, checksums, provenance pointers)
   ├─ 📁 reports/                               📊 generated outputs (gitignored except summaries)
   └─ 📁 tools/                                 🧰 helper scripts (parsers, formatters, charting)
```

> [!TIP]
> Keep perf artifacts **separate from correctness tests**. Perf tests can be slower, more environment-sensitive, and often run on a schedule (nightly) rather than on every PR.

---

## 📊 Reporting & reproducibility checklist ✅

Every run should record:

- 🔖 **Git SHA** + dirty state
- 🐳 **container images** / tags / digests (API, DBs, web)
- 🧾 **workload definition** (exact parameters)
- 🗃️ **dataset manifest** (source pointers + checksums)
- 🧊 **warmup strategy** (what was warmed and how long)
- 🧰 **runner versions** (pytest/k6/locust/etc)
- 💻 **hardware + OS** (CPU, RAM, disk type, Docker resource limits)
- 🕒 **time window** (and whether other workloads were running)

### Output format suggestion 📦
Store per-run artifacts under:
```text
tests/perf/reports/YYYY-MM-DD__<gitsha>__<suite>/
  run.json
  summary.md
  raw_results/...
  charts/...
```

---

## 🎯 “Perf budgets” (starter targets)

> [!WARNING]
> These are *starting points*—calibrate with real production traces and your expected dataset sizes.

- ⚙️ **API read endpoints**: P95 < 300ms, P99 < 800ms (steady state, representative load)
- 🗺️ **Tile endpoints**: P95 < 250ms per tile (cached), P95 < 800ms (uncached)
- 🗃️ **Pipeline batch imports**: define *rows/sec* targets per dataset class
- 🧠 **AI query endpoint**: P95 < 3s for “typical” queries, track >10s tail carefully

---

## 🧯 Troubleshooting (common dev-stack perf traps)

- 🔌 **Port conflicts**: if 5432/7474/8000/3000 are already in use, stop the conflicting service or remap ports in `docker-compose.yml`.
- 🧠 **Docker resources**: big datasets can silently thrash if Docker RAM/CPU limits are too low.
- 🗃️ **Volume permissions**: mounted `data/` directories can block pipeline writes on some hosts.
- 🔁 **Hot reload overhead**: disable `--reload` for serious benchmarks (reload is great for dev, bad for perf truth).

---

## 🧾 Appendix: Run manifest template (copy/paste)

```json
{
  "project": "kfm",
  "suite": "api",
  "git": { "sha": "abcdef123", "dirty": false },
  "timestamp_utc": "2026-01-29T00:00:00Z",
  "environment": {
    "docker": { "compose": true },
    "host": { "os": "linux", "cpu": "unknown", "ram_gb": 0 }
  },
  "services": {
    "api": { "image": "kfm-api:dev", "port": 8000 },
    "web": { "image": "kfm-web:dev", "port": 3000 },
    "postgis": { "image": "postgis:...", "port": 5432 },
    "neo4j": { "image": "neo4j:...", "port": 7474 }
  },
  "dataset": {
    "name": "sample",
    "manifest": "tests/perf/datasets/sample.json",
    "checksums": []
  },
  "workload": {
    "definition": "tests/perf/workloads/api_smoke.yaml",
    "warmup_seconds": 30,
    "duration_seconds": 180,
    "concurrency": 20
  },
  "results": {
    "latency_ms": { "p50": 0, "p95": 0, "p99": 0, "max": 0 },
    "throughput_rps": 0,
    "error_rate": 0
  }
}
```

---

## 🔗 Quick links (repo-local)

- 📁 `data/raw/` → raw inputs  
- 📁 `data/processed/` → processed outputs  
- 📁 `data/provenance/` → PROV logs (lineage + parameters)  
- ⚙️ `api/` → backend services  
- 🌐 `web/` → frontend

---

### 🧭 North Star

If a perf result can’t be explained, reproduced, and tied back to a known dataset + workload + environment… it’s not a result. It’s a rumor. 🕯️

