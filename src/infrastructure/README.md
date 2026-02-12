# `src/infrastructure/` 🧱

![Layer](https://img.shields.io/badge/layer-infrastructure-6f42c1)
![Architecture](https://img.shields.io/badge/clean_architecture-enforced-2ea44f)
![Governance](https://img.shields.io/badge/trust_membrane-API_gatekeeper-blue)

KFM follows a **layered clean architecture**. This directory is the **outermost runtime layer**: it contains
**concrete technology implementations** and **environment-specific wiring** (datastores, framework setup,
configuration, container/runtime glue).

> [!IMPORTANT]
> **Trust membrane (non-negotiable):** the browser UI and any external clients **never** connect directly to
> PostGIS/Neo4j/search backends. All access must be mediated by the governed API boundary (policy checks,
> provenance/audit requirements, authorization, etc.).

---

## What belongs here ✅

| Area | Examples of what we store here |
|---|---|
| Database integrations | PostGIS engine/session wiring, Neo4j driver wiring, search client wiring (OpenSearch/Elasticsearch), connection pooling, health checks |
| Repository implementations | Concrete classes that implement repository interfaces/ports (e.g., `PostGISParcelRepository`, `Neo4jKnowledgeGraphRepository`) |
| Migrations & schema bootstrapping | SQL migrations, Cypher migrations, index templates/mappings |
| API/server runtime bootstrap | FastAPI app creation, router registration, dependency-injection wiring, request middleware hooks |
| Background jobs | Worker process setup (Celery/RQ/APS-like schedulers), queue client wiring (if used) |
| Cross-cutting “system” concerns | Auth integration, policy evaluation wiring (e.g., OPA client), audit/telemetry emitters |
| Deployment glue | Container entrypoints, runtime config loaders, environment variable parsing, Kubernetes config helpers |

> [!NOTE]
> A controller/router module *may* live here **if it is purely an adapter** (HTTP ↔ use-case invocation)
> and does **not** contain business rules.

---

## What does **not** belong here ❌

- **Domain entities/models** (pure concepts; no DB/UI/framework imports)
- **Use-cases / services / workflows** (business rules; should depend only on interfaces/ports)
- **Governed documentation artifacts** (Story Nodes, standards, templates) — those belong under `docs/`
- **Pipelines & catalog generation code** — those belong under `src/pipelines/`
- **Frontend UI** — belongs under `web/`

---

## Dependency direction (keep the “arrow of trust” intact)

```mermaid
flowchart LR
  D[Domain\n(pure entities)] --> U[Use-cases / Services\n(workflows)]
  U --> I[Interfaces / Integration\n(ports + contracts)]
  I --> INF[Infrastructure\n(concrete adapters + wiring)]

  %% Prevent reverse dependency
  INF -. must not depend on .-> D
  INF -. must not depend on .-> U
```

**Rule of thumb:** infrastructure *implements* interfaces; it does not *define* business meaning.

---

## Runtime services & common defaults

> [!WARNING]
> Treat the values below as *documented defaults*, not guaranteed truth. The authoritative source of truth
> is always the repo’s `.env` / `.env.example`, Compose, and Kubernetes manifests.

| Component | Default port(s) | Common env vars |
|---|---:|---|
| PostGIS (PostgreSQL + PostGIS) | `5432` | `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB`, (sometimes) `POSTGRES_ENABLE_POSTGIS` |
| Neo4j | `7474` (HTTP), `7687` (Bolt) | `NEO4J_AUTH`, memory tuning vars |
| FastAPI backend | `8000` | `DATABASE_URL`, `NEO4J_URL`, `ELASTICSEARCH_URL`/`OPENSEARCH_URL`, `DEBUG`, `ALLOWED_HOSTS` |
| React frontend (dev) | `3000` | `REACT_APP_API_URL` (or equivalent) |
| Elasticsearch/OpenSearch (optional) | `9200` (HTTP), `9300` (cluster) | `discovery.type=single-node`, credentials |

---

## Local development (infrastructure-centric)

If the repo provides a Compose stack, it typically orchestrates the core infra services (DB + graph + API + UI)
with one command.

```bash
# From repo root
docker-compose up --build
```

Common useful variants:

```bash
# Only start data stores (run API/UI on host)
docker-compose up db graph

# Tear down + wipe volumes (⚠ wipes PostGIS/Neo4j state)
docker-compose down -v
```

---

## Adding a new infrastructure adapter

When you introduce a new concrete technology (new datastore, new external API, new queue, etc.), keep the
change **small** and the boundaries **auditable**.

### Checklist

- [ ] Define/extend the **port / interface** in the Interfaces/Integration layer (the “contract”).
- [ ] Implement the port here in `src/infrastructure/…`.
- [ ] Centralize configuration in one place (env/config loader) — **no scattered `os.environ[...]`**.
- [ ] Add a health check (startup connectivity test + `/healthz` surface if applicable).
- [ ] Add unit tests for the adapter (mock the network), and at least one integration test (real service).
- [ ] Update Compose/K8s manifests to include the service **only if** it’s required for baseline dev.
- [ ] Ensure audit/provenance hooks are triggered where policy requires it.

---

## Governance & security gates (infrastructure-specific)

> [!TIP]
> Infrastructure is where “accidental data exfiltration” often happens (logs, error traces, dev defaults).
> Be conservative.

- [ ] **No secrets in git**: credentials are injected via `.env` (local) and Secrets (Kubernetes).
- [ ] **Least privilege**: service accounts/DB users should be scoped to required schemas/queries.
- [ ] **Structured logs**: avoid logging raw payloads that may include sensitive locations/identifiers.
- [ ] **Policy enforcement is centralized** at the API boundary (trust membrane).
- [ ] **Reproducible infra-as-code**: changes to runtime behavior must be encoded in Compose/K8s/Helm.

---

## Recommended folder layout (pattern)

This is a **suggested** layout to keep infra cohesive (exact paths may differ in the live repo).

<details>
<summary>📁 Suggested structure</summary>

```text
src/infrastructure/
  README.md

  config/
    settings.py            # env parsing (pydantic settings, etc.)

  db/
    postgis.py             # engine/session factories
    migrations/            # SQL migrations
    repositories/          # PostGIS-backed repository implementations

  graph/
    neo4j.py               # driver/session wiring
    migrations/            # Cypher migrations
    repositories/

  search/
    opensearch.py          # client wiring
    indices/               # index templates/mappings

  http/
    fastapi/
      app.py               # FastAPI create_app()
      routers/             # REST adapters
      middleware/          # auth/policy/audit hooks

  policy/
    opa.py                 # policy client + decision caching

  telemetry/
    audit.py               # audit ledger emitter
    metrics.py             # Prometheus/OTel wiring

  tasks/
    worker.py              # background worker bootstrap
```

</details>