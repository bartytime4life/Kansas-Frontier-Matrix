# 🧩 `api/services/` — Service Layer (Use-Cases)

![Layer](https://img.shields.io/badge/layer-service%20%2F%20use--cases-blue)
![API](https://img.shields.io/badge/api-REST%20%2B%20GraphQL-informational)
![Data](https://img.shields.io/badge/data-PostGIS%20%7C%20Neo4j%20%7C%20Search%20%7C%20Object%20Store-orange)
![Governance](https://img.shields.io/badge/governance-OPA%20policy%20gates-success)
![AI](https://img.shields.io/badge/ai-Focus%20Mode%20%28RAG%29%20%2B%20Ollama-purple)

> **Purpose:** `api/services/` holds KFM’s *application services / use-cases* — the orchestration layer that turns domain intent into governed, traceable outcomes.  
> Services sit **between** API routers/controllers and **adapters** (DBs, search, LLM, storage), enforcing the “truth path” and KFM’s evidence-first rules.

---

## 📌 What belongs here?

✅ **DO put in `api/services/`:**
- Use-case orchestration (`CatalogService.search()`, `TilesService.get_tile()`, `FocusModeService.query()`)
- Business rules and workflow sequencing
- Evidence bundling and citation mapping (the “map behind the map” mindset)
- Governance hooks: policy checks, provenance logging, allowlists/guardrails

❌ **DO NOT put in `api/services/`:**
- FastAPI routers/controllers (HTTP parsing/response formatting)
- Raw SQL, Cypher, or vendor SDK calls (those belong in adapters/repos)
- Framework globals (request objects, app state, etc.)
- “Just a helper” utilities with no business meaning (put in `api/utils/`)

---

## 🧱 Architectural role (Clean Architecture fit)

KFM follows a layered architecture where services implement the **Service / Use-Case Layer**:
- **Domain layer** = core entities/models (framework-agnostic)
- **Service layer (this folder)** = workflows + decision rules + orchestration
- **Integration/Adapter layer** = PostGIS/Neo4j/search/object-store/LLM clients and repositories
- **Infrastructure** = FastAPI app wiring, DI, routers, startup config

**Rule of thumb:**  
> **Services depend on interfaces (ports), not implementations.**  
> This keeps use-cases testable and prevents DB/LLM details from leaking into business logic.

---

## 🗂️ Suggested folder map

> (Actual filenames may vary; keep the *intent* consistent.)

```text
api/
  services/ 🧩
    README.md  ← you are here 📍

    catalog_service.py        # DCAT/STAC dataset discovery & retrieval
    query_service.py          # constrained ad-hoc query interface (allowlisted)
    tiles_service.py          # vector/raster tile orchestration
    graph_service.py          # graph/relationship use-cases (GraphQL resolvers call here)
    focus_mode_service.py     # RAG pipeline orchestration (Prompt Gate → Retrieval → LLM → Policy)
    provenance_service.py     # provenance ledger logging + citation maps
    policy_service.py         # OPA wrapper (authorization + content/policy checks)

  adapters/ 🔌                # PostGIS/Neo4j/Search/Ollama/Object-store implementations
  domain/ 🧬                  # Pydantic/dataclass domain models (no I/O)
  routers/ 🌐                 # FastAPI routers/controllers
```

---

## 🧠 Service design principles

### 1) Evidence-first by default 🧾
Services should make it *easy* to do the right thing:
- Prefer return types that include **data + evidence metadata**
- Keep “citation mapping” close to the logic that selects evidence
- If evidence is missing, fail safely (or return “insufficient evidence”)

### 2) Governed access (policy gates) 🛡️
Every service that exposes data should:
- Validate inputs (bbox, time range, query params)
- Enforce allowlists (tables, layers, fields, datasets)
- Run authorization/policy checks (OPA or policy module)

### 3) Traceability (provenance logging) 🧷
Services that produce user-visible outputs should log:
- Request context (user/role, map context, time filters)
- The exact datasets/documents used
- The transformation steps (if any)
- Output IDs + citations map

### 4) Keep services stateless ♻️
- No hidden caches unless explicit and documented
- Prefer pure functions + injected dependencies
- Make operations idempotent where possible

---

## 📚 “Service catalog” (what we expect to find here)

| Service | What it owns 🧩 | Typical callers 🌐 | Notes |
|---|---|---|---|
| `CatalogService` | Dataset metadata, discovery, dataset asset links | `/api/v1/datasets/*`, `/api/v1/catalog/search` | Returns DCAT/STAC summaries + links |
| `QueryService` | Constrained “power user” querying | `/api/v1/query` | Must be allowlisted + logged |
| `TilesService` | Tile orchestration + layer gating | `/tiles/{layer}/{z}/{x}/{y}.*` | Keeps map clients on the same tile “well” |
| `GraphService` | Relationship-driven use-cases | `/graphql` resolvers | Often joins Neo4j + PostGIS |
| `FocusModeService` | RAG orchestration for Focus Mode | `/focus-mode/query` | Prompt Gate → retrieval → LLM → policy → citations |
| `PolicyService` | OPA integration + content rules | called by all services | Centralize policy logic here |
| `ProvenanceService` | Immutable audit + citation maps | called by key services | “No provenance, no publish” |

---

## 🔍 Focus Mode (RAG) service workflow

This is the *canonical* AI-related service orchestration pattern.

```mermaid
flowchart LR
  A[User question 🗨️] --> B[Prompt Gate 🧼]
  B --> C[Hybrid Retrieval 🔎\nNeo4j + PostGIS + Full-text + Vector]
  C --> D[Evidence Bundle 📦\nnumbered sources + IDs]
  D --> E[LLM Generate 🤖\n(Ollama)]
  E --> F[Policy Check 🛡️\n(OPA rules)]
  F --> G[Response + Citation Map 🧾]
  G --> H[Provenance Log 🧷\n(question, sources, model, prompt ver)]
```

### Implementation notes (service-level)
- Keep retrieval *compact and high-signal* (snippets, not whole documents).
- Ensure output contains required citation markers (e.g., `[1]`, `[2]`) before returning.
- If policy fails (missing citations, sensitive content, role mismatch), return a governed fallback.

---

## 🧪 Testing expectations

### ✅ Unit tests (fast)
- Services tested with **fake repositories/adapters**
- Assert:
  - policy hooks are called
  - allowlists enforce correctly
  - provenance is emitted on successful flows
  - “insufficient evidence” behavior is consistent

### 🔧 Integration tests (real deps)
- Adapter-level tests against PostGIS/Neo4j/search/ollama containers (compose profile)
- Golden tests for:
  - tile generation contract (headers/content-type)
  - query constraints (blocked tables/columns)
  - GraphQL resolver consistency

### 📜 Contract tests
- Ensure service return shapes remain stable for routers/controllers.

---

## 🧯 Error handling contract

Keep a consistent pattern so controllers can map to HTTP cleanly.

**Recommended:**
- Define service exceptions with:
  - `code` (stable string)
  - `message` (safe for users)
  - optional `details` (internal)
- Avoid leaking raw DB/LLM errors upward.

Example patterns:
- `NotFoundError("dataset_not_found")`
- `PolicyDeniedError("not_authorized")`
- `ValidationError("invalid_bbox")`
- `EvidenceError("no_source_no_answer")`

---

## 🧰 Example service skeleton (Python)

```python
from dataclasses import dataclass
from typing import Protocol

class DatasetRepo(Protocol):
    async def get_dataset(self, dataset_id: str) -> dict: ...
    async def search(self, *, q: str | None, bbox=None, time=None) -> list[dict]: ...

class Policy(Protocol):
    async def assert_allowed(self, *, actor, action: str, resource: dict) -> None: ...

class Provenance(Protocol):
    async def log(self, *, actor, action: str, inputs: dict, outputs: dict) -> None: ...

@dataclass
class CatalogService:
    repo: DatasetRepo
    policy: Policy
    prov: Provenance

    async def get_dataset(self, *, actor, dataset_id: str) -> dict:
        ds = await self.repo.get_dataset(dataset_id)
        await self.policy.assert_allowed(actor=actor, action="datasets:read", resource=ds)
        await self.prov.log(
            actor=actor,
            action="datasets:read",
            inputs={"dataset_id": dataset_id},
            outputs={"dataset_id": dataset_id},
        )
        return ds
```

---

## ➕ Adding a new service (checklist)

1. **Name the use-case** 🎯  
   Example: `WaterWellsAnalysisService` vs `utils_wells.py`

2. **Define the inputs/outputs** 🧬  
   Prefer domain models or small typed DTOs.

3. **Create ports (interfaces)** 🔌  
   Repositories/clients your service needs (PostGIS, Neo4j, search, object store).

4. **Write the service logic** 🧩  
   Keep DB/SDK details out.

5. **Wire dependencies** 🧷  
   Add DI bindings so routers can construct the service.

6. **Enforce governance** 🛡️  
   Policy checks + allowlists + provenance logging.

7. **Add tests** ✅  
   Unit tests first, then integration tests if needed.

8. **Document** 📝  
   Update this README and any domain README that applies.

---

## 🧭 Operational notes (dev + prod)

### Local dev via containers 🐳
The broader KFM stack is designed to run with Docker Compose (API + PostGIS + Neo4j + web + optional OPA/Ollama).  
Services should assume dependencies are reachable via container DNS names (e.g., `db`, `graph`, `ollama`) when running in compose.

### Scalability 📈
- Keep services stateless so the API layer can scale horizontally.
- Expensive operations should be cached *only if governed* (cache keys must include policy context).

---

## 🔗 Related docs (repo pointers)

> These are the docs that define system-level expectations for the service layer:
- `docs/architecture/system_overview.md` (truth path + API role)
- `docs/architecture/ai/AI_SYSTEM_OVERVIEW.md` (AI boundaries)
- `docs/architecture/ai/OLLAMA_INTEGRATION.md` (Focus Mode RAG pipeline)
- `pipelines/README.md` (data lifecycle + provenance artifacts)

---

## 🧼 Philosophy recap

- **One truth path:** Raw → Processed → Catalog → Databases → API → UI/AI  
- **No backdoors:** UIs don’t query DBs directly; services are the controlled gateway.  
- **No source, no answer:** If we can’t cite it, we shouldn’t claim it.

✨ If you keep services clean, everything else becomes easier: testing, governance, scaling, and trust.