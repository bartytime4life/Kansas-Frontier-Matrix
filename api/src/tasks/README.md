# 🧰 API Tasks (Background Jobs)

> ⚙️ **Goal:** run long or asynchronous work *outside* the request/response path (simulations, exports, ingestion triggers, maintenance).  
> 🧵 **Pattern:** API enqueues ➜ workers execute ➜ results stored ➜ client polls job status. :contentReference[oaicite:0]{index=0}

---

## 📌 What lives in `api/src/tasks/`

This folder is the **home for background “tasks”** that would otherwise:
- block the API thread/event-loop,
- exceed request timeouts,
- or require retries / backoff / concurrency limits.

KFM’s architecture explicitly supports **task queues + worker pools** for heavy computation, external API calls, and long-running analysis. :contentReference[oaicite:1]{index=1}:contentReference[oaicite:2]{index=2}

---

## 🧭 When to use Tasks vs Pipelines vs Cron

| Need | Use | Why |
|---|---|---|
| Multi-step ETL + dependencies + backfills + lineage + dashboards | **Pipelines (Airflow DAGs)** | Pipeline-as-code, scheduled runs, retries, lineage, incremental processing, deduplication, and data-quality checks. :contentReference[oaicite:3]{index=3} |
| Simple operational chores (backup, prune cache/logs) | **Cron / Kubernetes CronJob** | Lightweight scheduling for “small tasks not worth a whole pipeline DAG”. :contentReference[oaicite:4]{index=4} |
| User-triggered long analysis / async processing | **Task Queue + Workers** | Enqueue jobs so the API can return a job id immediately; workers process and store results. :contentReference[oaicite:5]{index=5}:contentReference[oaicite:6]{index=6} |
| Event-driven reactions (e.g., new imagery arrives) | **Queue/Event Stream + Subscribers** | Publish/subscribe decouples ingestion from processing and improves resilience. :contentReference[oaicite:7]{index=7} |

> ⚠️ **Rule of thumb:**  
> If it’s **ETL that produces official datasets**, it should live in the **pipeline subsystem** (single source of truth), not scattered across multiple places. :contentReference[oaicite:8]{index=8}

---

## 🔁 Task lifecycle (how the pieces fit)

```mermaid
flowchart LR
  UI[🖥️ UI / Client] -->|POST action| API[🌐 API Endpoint]
  API -->|Validate + Auth| AUTH[🔐 AuthZ/AuthN]
  API -->|Enqueue job + return job_id| Q[(📬 Queue / Broker)]
  Q -->|pull| W[👷 Worker Pool]
  W -->|run task| T[🧠 Task Handler]
  T -->|write outputs| DB[(🗄️ DB / Cache / Object Storage)]
  UI -->|GET status(job_id)| API
  API -->|read status/results| DB
```

- The API can authenticate, validate inputs, **enqueue**, and immediately return a **job ID** that the client can poll. :contentReference[oaicite:9]{index=9}
- Workers run tasks and **store results** in the DB/cache, then mark the task as done. :contentReference[oaicite:10]{index=10}

---

## 🧩 Common task types in KFM

- 🧪 **Simulation / Monte Carlo** (CPU heavy)  
- 📦 **Exports** (CSV/GeoJSON/PDF report generation)
- 🌦️ **External API pulls** (e.g., NOAA forecasts; pushes to dashboards) :contentReference[oaicite:11]{index=11}
- 🧠 **ML jobs** (retrain requests, batch inference kickoffs)
- 🗺️ **Geo operations** (tile/cache warmers, layer refresh)
- 🧹 **Maintenance** (cache cleanup, log pruning, backups) :contentReference[oaicite:12]{index=12}

---

## 🗂️ Suggested folder layout (expand as needed)

> This is a recommended structure — align it to the actual codebase conventions.

```text
📁 api/
  📁 src/
    📁 tasks/
      📄 README.md              # you are here ✅
      📄 registry.*             # task name ➜ handler mapping
      📄 worker.*               # worker bootstrap (connect broker, concurrency)
      📄 scheduler.*            # optional recurring schedules (if not handled by Airflow/cron)
      📁 handlers/              # task implementations
        📄 analysis.*           # long-running compute
        📄 exports.*            # exports & reports
        📄 ingest.*             # pull/push integrations
        📄 maintenance.*        # cleanup & housekeeping
      📁 models/                # task status/results schemas (DB)
      📁 utils/                 # retry, idempotency, tracing helpers
      📁 __tests__/             # unit/integration tests
```

---

## 🧾 Task “Contract” (what every task should declare)

Think of each task as a mini-service with a stable interface:

### ✅ Required
- **Name**: stable identifier (used in logs, metrics, UI status checks)
- **Inputs**: validated + serialized parameters
- **Outputs**: where results are persisted (DB/cache/files)
- **Status model**: `queued → running → succeeded|failed` (plus optional: `canceled`, `expired`)
- **Retry policy**: max attempts + exponential backoff when appropriate :contentReference[oaicite:13]{index=13}
- **Idempotency strategy**: safe to rerun without duplicating outcomes (critical for retries) :contentReference[oaicite:14]{index=14}
- **Observability**: log start/finish + key steps + failures :contentReference[oaicite:15]{index=15}

### ⭐ Strongly recommended
- **Lineage tags**: dataset/run identifiers so outputs can be traced to inputs and pipeline runs :contentReference[oaicite:16]{index=16}
- **Concurrency class**: e.g., `cpu-heavy`, `io-heavy`, `latency-sensitive` so we can cap parallelism :contentReference[oaicite:17]{index=17}
- **Timeouts**: prevent runaway jobs
- **Ownership**: who maintains this task + on-call expectations

---

## 🧪 Template: Task Spec (drop this into a PR description or `docs/`)

```yaml
name: "analysis.run_simulation"
purpose: "Run scenario simulation asynchronously; store results; expose status"
triggered_by:
  - "POST /api/simulation/run"
queue: "cpu-heavy"
concurrency_limit: 2
retries:
  max_attempts: 3
  backoff: "exponential"
timeout_seconds: 3600
idempotency:
  key_fields: ["user_id", "scenario_id", "params_hash"]
outputs:
  location: "postgres"
  tables: ["simulation_runs", "simulation_run_artifacts"]
observability:
  logs: ["start", "finish", "step", "error"]
  metrics: ["duration_ms", "success_count", "failure_count", "queue_lag"]
security:
  auth: "JWT"
  required_role: "analyst"
lineage:
  include: ["input_dataset_versions", "pipeline_run_id"]
```

---

## 🩺 Observability & ops expectations

Background tasks must be **operationally visible**:
- Log **start + finish** and meaningful steps; log stack traces internally; return safe error IDs to clients when needed. :contentReference[oaicite:18]{index=18}
- Monitor queue health: if tasks pile up or fail repeatedly, alert (watchdog / monitors). :contentReference[oaicite:19]{index=19}
- Prefer instrumenting task duration + success/failure counters.

> 🔎 Tip: treat tasks like production endpoints — because they *are* production pathways, just asynchronous.

---

## ♻️ Reliability rules (idempotency, dedup, incremental runs)

Tasks that touch durable data must assume they can be retried or re-run:
- Keep a **marker** (DB state / last processed date) for incremental work. :contentReference[oaicite:20]{index=20}
- Prevent duplicates via **upsert**, unique constraints, or pre-checks. :contentReference[oaicite:21]{index=21}
- Add **data-quality checks** and fail early if inputs look wrong or empty. :contentReference[oaicite:22]{index=22}

---

## 🗓️ Scheduling notes

- If a job is **recurring** and is part of data production → **Airflow** (preferred): monitoring, retries, lineage, backfills. :contentReference[oaicite:23]{index=23}
- If it’s a small operational chore → **Cron/Kubernetes CronJob** (simple + explicit). :contentReference[oaicite:24]{index=24}
- If it’s reactive or user-triggered → **Queue + Workers** (keeps API responsive). :contentReference[oaicite:25]{index=25}

---

## 🔐 Security expectations

Tasks are part of the backend security boundary:
- Tasks triggered via API must enforce **authorization** (JWT + role/permission checks). :contentReference[oaicite:26]{index=26}
- Never log sensitive payloads unredacted; store secrets only in environment/secret managers.
- If tasks call external APIs, treat responses as untrusted input and validate/sanitize.

---

## ➕ Adding a new task (checklist)

1. 🧠 **Decide the right home**  
   - ETL/data product? → pipeline subsystem. :contentReference[oaicite:27]{index=27}  
   - Async work / long compute? → task queue + workers. :contentReference[oaicite:28]{index=28}

2. 🧱 **Implement the handler**  
   - Validate inputs  
   - Write deterministic outputs  
   - Log steps + errors :contentReference[oaicite:29]{index=29}

3. 🗂️ **Register it** (task name ➜ handler mapping)

4. 🧪 **Add tests** (unit + integration for DB writes / external calls mocked)

5. 🩺 **Add observability** (metrics + structured logs + status transitions)

6. 📚 **Document the task** (spec + ownership + operational notes)

---

## ✅ Definition of Done (for a new task)

Inspired by KFM’s doc rigor: templates + checklists help keep work reviewable and trustworthy. :contentReference[oaicite:30]{index=30}

- [ ] Task has a stable **name** and **purpose**
- [ ] Inputs validated (schema/type checks)
- [ ] Task is **idempotent** or has dedup protections
- [ ] Retries/backoff defined (and safe)
- [ ] Concurrency class defined (CPU/IO) and limits set
- [ ] Logs include start/finish + key steps
- [ ] Status is persisted and queryable (job id flow)
- [ ] Tests added/updated
- [ ] Owner listed + operational runbook notes included

---

## 📚 References (project grounding)

- Task queue + workers (Celery/RQ/message queue), workers execute and store results, status polling, concurrency limits. :contentReference[oaicite:31]{index=31}
- API coordinates jobs and returns job IDs; FastAPI/OpenAPI/async context. :contentReference[oaicite:32]{index=32}
- Pipeline workflow governance: retries, lineage, incremental processing, deduplication, data quality checks. :contentReference[oaicite:33]{index=33}
- Cron/Kubernetes CronJob for small scheduled ops tasks. :contentReference[oaicite:34]{index=34}
- Logging/monitoring expectations + watchdog for jammed queues; /health checks. :contentReference[oaicite:35]{index=35}
- Canonical subsystem homes (avoid scattering ETL; one source of truth). :contentReference[oaicite:36]{index=36}
- Definition-of-done checklist pattern for docs/work items. :contentReference[oaicite:37]{index=37}

