# 🚀 Performance & Load Testing (`tests/perf/`)

![Status](https://img.shields.io/badge/status-active%20development-orange)
![Type](https://img.shields.io/badge/tests-performance%20%26%20load-blue)
![Principle](https://img.shields.io/badge/principle-provenance--first-6f42c1)
![Target](https://img.shields.io/badge/targets-API%20%7C%20DB%20%7C%20ETL%20%7C%20AI-success)

This folder is the **repeatable performance test harness** for **Kansas-Matrix-System** (aligned to the KFM architecture): a **pipeline → catalog → databases → API → UI** platform where *all user access goes through the backend API + governance policies*. ✅

> [!IMPORTANT]
> These tests are meant to be **reproducible** and **comparable over time** (same scenario, same dataset size, same config → comparable outputs).  
> Think “CI-friendly perf guardrails” + “deep-dive profiling runbook”.

---

## 🧭 Table of Contents

- [🎯 Goals](#-goals)
- [📏 What We Measure](#-what-we-measure)
- [🧪 Test Types](#-test-types)
- [🗂️ Folder Layout](#️-folder-layout)
- [⚡ Quickstart](#-quickstart)
- [🏃 Running Scenarios](#-running-scenarios)
- [📈 Results, Baselines, Regression Rules](#-results-baselines-regression-rules)
- [🧰 Profiling & Debugging Runbook](#-profiling--debugging-runbook)
- [🧩 Adding a New Perf Test](#-adding-a-new-perf-test)
- [🤖 CI / Automation](#-ci--automation)
- [🧱 Safety & Guardrails](#-safety--guardrails)

---

## 🎯 Goals

### ✅ What “good” looks like
- **Interactive** UX: map + search + story navigation feel fast.
- **Scalable** backend: query latency stays stable under concurrency.
- **Governed** access: policy enforcement doesn’t silently become the bottleneck.
- **Provenance-aligned** runs: every perf run records *what* was tested, *against which dataset*, *with what settings*, and *from which git commit*.

### 🧨 What we want to catch early
- Latency regressions (p95/p99 spikes)
- Throughput collapses under load
- Memory leaks / container OOMs
- Slow database queries introduced by schema/index changes
- External adapter calls that block the system (timeouts / slow retries)
- AI “Focus Mode” latency explosions (retrieval + generation)

---

## 📏 What We Measure

> [!NOTE]
> We aim to measure **end-to-end** (client → API → DB/policy/AI → response) *and* **component-level** (PostGIS vs Neo4j vs Search vs OPA vs Ollama) so regressions are diagnosable.

| Layer 🔩 | What we measure 📐 | Examples |
|---|---|---|
| 🌐 API (FastAPI) | p50/p95/p99 latency, RPS, error rate | `/datasets`, `/search?q=...`, `/features/{id}`, `/graphql` queries |
| 🧭 Policy (OPA) | decision latency, cache hit ratio | auth checks, content rules, “fail closed” behavior |
| 🗺️ PostGIS | query latency, planning time, rows scanned | point-in-polygon, distance, clustering, bounding box queries |
| 🧠 Neo4j | traversal latency, query plan regressions | story graph navigation, entity linking queries |
| 🔎 Search index | query latency, recall/latency tradeoffs | keyword search, embeddings similarity search |
| 🧱 Pipelines/ETL | ingest time, CPU/mem, IO throughput | raw → processed, metadata/provenance generation |
| 🤖 AI (Ollama) | time-to-first-token, tokens/sec, end-to-end answer time | retrieval + prompt build + generate |

---

## 🧪 Test Types

### 1) 🟢 Smoke (CI-friendly)
Fast checks that run on PRs:
- small dataset
- low concurrency
- short duration (30–90s)
- detects *obvious* regressions

### 2) 🟡 Local “Quick”
Developer loop:
- run before/after a change
- compare to a local baseline

### 3) 🔵 Nightly / Full Suite
Bigger dataset + more scenarios:
- heavier concurrency
- captures “real-ish” performance curves

### 4) 🟣 Soak
Long-running stability:
- leaks, GC pressure, connection pool issues
- cache drift or unbounded growth

### 5) 🪶 Edge Profile (low-resource)
Targets offline/community deployments:
- constrained CPU/RAM
- validates “still usable” budgets

---

## 🗂️ Folder Layout

> [!TIP]
> Keep perf assets **scenario-driven** and **data-versioned**. Results are artifacts: store locally or in CI artifacts, not in git.

```text
tests/perf/
├── README.md                # 👈 you are here
├── scenarios/               # 🧪 scenario definitions (yaml/json)
│   ├── smoke.yaml
│   ├── api_read_heavy.yaml
│   ├── spatial_queries.yaml
│   ├── graph_traversal.yaml
│   └── ai_focus_mode.yaml
├── workloads/               # 🏋️ load generators (choose one “default”)
│   ├── locust/              # ✅ recommended (Python ecosystem)
│   │   ├── locustfile.py
│   │   └── user_flows.py
│   └── k6/                  # optional (JS load testing)
│       └── api.js
├── datasets/                # 📦 dataset manifests + seeds (NO giant blobs)
│   ├── manifests/
│   │   ├── small.json
│   │   ├── medium.json
│   │   └── large.json
│   └── seeds/
│       ├── postgis.sql
│       ├── neo4j.cypher
│       └── search_index.jsonl
├── scripts/                 # 🛠️ orchestrators + helpers
│   ├── up.sh
│   ├── seed.sh
│   ├── run.sh
│   ├── report.py
│   └── diff.py
├── docker/                  # 🐳 perf overlay compose (optional)
│   └── docker-compose.perf.yml
└── results/                 # 📈 output artifacts (gitignored)
    └── .gitkeep
```

---

## ⚡ Quickstart

### ✅ Prereqs
- Docker + Docker Compose
- The project dev stack (API + DBs) runs via compose
- (Optional for AI scenarios) **Ollama** installed and running locally, or containerized in the perf stack

> [!WARNING]
> Performance numbers are only meaningful when the machine is not overloaded. Close “heavy stuff” (VMs, builds, video calls), and avoid running other benchmarks concurrently.

---

### 1) 🐳 Start the stack

**Option A — Use the main dev compose**
```bash
docker-compose up --build
```

**Option B — Use a perf overlay compose**
```bash
docker-compose -f docker-compose.yml -f tests/perf/docker/docker-compose.perf.yml up --build
```

> [!NOTE]
> Common local ports (defaults) you may need free:
> - Postgres/PostGIS: `5432`
> - Neo4j HTTP: `7474`  | Bolt: `7687`
> - FastAPI: `8000`
> - React dev server: `3000`

---

### 2) 🌱 Seed the perf dataset

```bash
bash tests/perf/scripts/seed.sh --dataset small
```

Expected behavior:
- Initializes PostGIS + Neo4j (and search index if enabled)
- Loads a **known dataset manifest**
- Leaves the system in a “ready to benchmark” state

---

### 3) 🟢 Run smoke

```bash
bash tests/perf/scripts/run.sh smoke
```

---

## 🏃 Running Scenarios

### Scenario philosophy
A **scenario** is a named workload with:
- a dataset manifest (small/medium/large)
- request mix (read-heavy vs write-heavy vs mixed)
- concurrency + duration
- pass/fail budgets (optional but recommended)

Example command patterns:

```bash
# Run a named scenario
bash tests/perf/scripts/run.sh api_read_heavy --dataset small --duration 60s --users 20

# Run the full suite locally (takes longer)
bash tests/perf/scripts/run.sh suite --dataset medium
```

### Minimal environment variables (suggested)
```bash
export PERF_BASE_URL="http://localhost:8000"
export PERF_RESULTS_DIR="tests/perf/results"
export PERF_DATASET="small"
export PERF_DURATION="60s"
export PERF_USERS="20"
```

---

## 📈 Results, Baselines, Regression Rules

### Where results go
Each run should create a unique run folder:
```text
tests/perf/results/
└── 2026-01-30T203500Z__api_read_heavy__small__git-abc123/
    ├── run.json              # 🧾 provenance: commit, host, dataset, config
    ├── summary.json          # 📌 p50/p95/p99, rps, errors
    ├── timeseries.csv        # 📉 optional timeline (latency over time)
    ├── locust_stats.csv      # 🏋️ raw generator output
    └── report.html           # 🧠 human-friendly output
```

### Baselines (recommended)
Store baselines outside git, or in CI artifacts:
- `baseline/main` (nightly)
- `baseline/release/*` (tagged releases)

### Regression rules (starter template)
> [!TIP]
> Pick budgets that match your reality. Start loose, then tighten.

- ❌ **Fail** if error rate > `0.5%`
- ❌ **Fail** if p95 latency worsens by > `25%` vs baseline
- ❌ **Fail** if p99 latency worsens by > `35%` vs baseline
- ⚠️ **Warn** if RPS drops by > `15%` vs baseline

---

## 🧰 Profiling & Debugging Runbook

### Step 0: Verify you’re not benchmarking your laptop’s chaos 😅
- Docker has enough memory allocated
- No port conflicts
- No container restarts (OOM / crash loops)
- Your dataset seed finished successfully

### Step 1: Identify *which* layer regressed
Use the scenario mix to isolate:
- API only (no AI)
- DB-heavy (spatial + graph)
- Policy-heavy (OPA checks)
- AI-heavy (Focus Mode)

### Step 2: Collect the “standard bundle”
**Always attach these when reporting perf regressions:**
- `run.json`, `summary.json`
- docker compose logs
- DB query plans for the top slow queries
- container stats (CPU/mem)

Example:
```bash
docker-compose logs --no-color > tests/perf/results/latest/docker-logs.txt
docker stats --no-stream > tests/perf/results/latest/docker-stats.txt
```

### Step 3: Database triage
- PostGIS: use `EXPLAIN (ANALYZE, BUFFERS)` on slow queries
- Neo4j: inspect query plan + indexes
- Search: check slow query logs and shard/refresh settings

### Step 4: Policy triage (OPA)
- Measure decision time (cold vs warm)
- Ensure policy evaluations are cached where safe
- Confirm “fail closed” behavior didn’t introduce retry storms

### Step 5: AI triage (Ollama)
- Confirm model choice is intentional (`OLLAMA_MODEL`)
- Record:
  - time-to-first-token
  - tokens/sec
  - context size (prompt length)
- Beware: larger models can require **significantly more RAM/VRAM**.

---

## 🧩 Adding a New Perf Test

1) Add a scenario file:
```text
tests/perf/scenarios/my_new_scenario.yaml
```

2) Implement the workload flow:
- add a Locust task set under `tests/perf/workloads/locust/`

3) Add/extend dataset seed artifacts if needed:
- `tests/perf/datasets/seeds/*`

4) Make sure the run produces:
- `run.json` (provenance metadata)
- `summary.json` (KPIs)

5) Add it to:
- smoke suite (if fast)
- nightly suite (if heavier)

---

## 🤖 CI / Automation

> [!NOTE]
> Typical setup:
> - PRs: run `smoke`
> - Nightly: run `full suite` + upload artifacts
> - Release: run `large dataset` + publish baseline

Suggested workflow files (not in this folder):
```text
.github/workflows/perf-smoke.yml
.github/workflows/perf-nightly.yml
```

---

## 🧱 Safety & Guardrails

- ✅ Prefer running against **local compose** or a dedicated staging environment
- ❌ Don’t point load tests at production without explicit approval
- ✅ External adapters should default to **mocks** in perf runs (avoid quotas/ToS issues)
- ✅ Keep results **out of git** (store as CI artifacts)

---

### 🏁 Done
If you can run `smoke` locally and it produces `run.json` + `summary.json`, you’ve got a working perf harness foundation ✅