# 🧩 `api/services/` — Service (Use‑Case) Layer

![Python](https://img.shields.io/badge/Python-3.11%2B-informational?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi&logoColor=white)
![Clean Architecture](https://img.shields.io/badge/Architecture-Clean%20%26%20Layered-blueviolet)
![Governance](https://img.shields.io/badge/Governance-Policy%20Enforced-critical)
![Provenance](https://img.shields.io/badge/Provenance-First-success)
![LLM](https://img.shields.io/badge/LLM-Ollama%20(Local)-orange)

> 🧠 **What this folder is:** the **business logic + orchestration layer** for the KFM backend.  
> 🔒 **What it is *not*:** FastAPI route handlers, database code, or framework glue.

---

## 📌 Why `services/` exists

KFM follows a layered approach where the **UI never talks to databases directly**—everything is mediated by the backend API, which performs validation + governance checks. The service layer is where we implement **use-cases**: workflows, analysis routines, and “do the thing” logic.

✅ Services should:
- Orchestrate **domain entities/models**
- Call **repository/adapters** via interfaces (not direct DB calls)
- Apply **decision rules**, algorithms, and governance rules
- Be **easy to test** (mock repositories)
- Return **domain objects / DTOs**, not web-framework responses

---

## 🧭 Mental Model (Request Flow)

```mermaid
flowchart LR
  UI[🖥️ Web UI] --> R[🧰 FastAPI Routes / GraphQL Resolvers]
  R --> S[🧩 Services (Use‑Cases)]
  S -->|interfaces| A[🔌 Adapters / Repositories]
  A --> P[(🗺️ PostGIS)]
  A --> N[(🕸️ Neo4j)]
  A --> E[(🔎 Search Index)]
  A --> X[(🌐 External APIs)]
  S --> G[🛡️ Policy / Governance Checks]
  S --> V[🧾 Provenance + Audit Logs]
```

---

## 🗂️ Suggested Layout

> Your exact files may vary — this is the **recommended convention**.

```text
📁 api/
  📁 routes/                # Thin controllers (HTTP)
  📁 graphql/               # Optional resolvers/schema
  📁 models/ or domain/     # Pydantic/domain entities (lingua franca)
  📁 repositories/          # Interfaces + implementations (or adapters/)
  📁 db/                    # Database clients (PostGIS, Neo4j, etc.)
  📁 services/              # ✅ You are here
    📄 analysis_service.py
    📄 story_service.py
    📄 search_service.py
    📁 ai/
      📄 ai_query_service.py
    📄 __init__.py
```

---

## ✅ Service Design Rules (The “Commandments”)

### 1) Keep services framework‑agnostic 🧼
- ✅ OK: pure Python + domain models
- ❌ Avoid: importing `fastapi.Request`, `Depends`, router objects, response classes

### 2) No direct DB calls from services 🚫🗄️
Services should never know whether data came from:
- PostGIS
- Neo4j
- CSV / file pipeline output
- External API

Instead, they call **interfaces** (repositories/adapters) and operate on **domain objects**.

### 3) Prefer dependency injection (constructor or explicit params) 🧩
Pass repositories/adapters into services:
- Constructor injection for long‑lived services
- Function arguments for simpler use-cases

### 4) Split “Queries” vs “Commands” ⚖️
- **Query**: read/aggregate/search → returns data
- **Command**: create/update/delete → returns result + writes provenance/audit trails

### 5) Provenance isn’t optional 🧾
If a service produces:
- an analysis output,
- an AI answer,
- a generated artifact,

…it should also produce/trigger whatever logging is required for provenance & auditability.

### 6) Fail closed by default 🛑
When policy checks fail:
- return a safe refusal / sanitized result
- don’t “best effort” leak restricted content

---

## 🧪 Testing Expectations

Services are intended to be highly testable.

### Unit tests (fast + pure) ✅
- Mock repository interfaces
- Provide synthetic domain objects
- Validate:
  - correct calculations
  - decision rules
  - policy outcomes (allow/deny/mask)

### Integration tests (endpoints) 🔗
- Use FastAPI test client at the route layer
- Optionally spin up ephemeral DB(s) for realistic queries

---

## 🧰 Common Service Patterns

### Pattern A — Thin service function (simple use-case)
```python
def get_story_node(story_repo, story_id: str):
    node = story_repo.get_story_node(story_id)
    if not node:
        raise ValueError("Story node not found")
    return node
```

### Pattern B — Service class (stateful dependencies + workflows)
```python
class StoryService:
    def __init__(self, story_repo, graph_repo, policy):
        self.story_repo = story_repo
        self.graph_repo = graph_repo
        self.policy = policy

    def get_story_with_related(self, user, story_id: str):
        self.policy.check_access(user=user, resource_id=story_id)
        story = self.story_repo.get_story_node(story_id)
        related = self.graph_repo.get_related_events(story_id)
        return {"story": story, "related": related}
```

---

## 🌾 Example Use‑Case: `DroughtAnalysisService`

This is the archetype for analytic services:
- Pull domain records via repositories (rainfall, yield, etc.)
- Compute a result (drought impact summary)
- Return a clean model/summary

```python
class DroughtAnalysisService:
    def __init__(self, rainfall_repo, yield_repo):
        self.rainfall_repo = rainfall_repo
        self.yield_repo = yield_repo

    def drought_report(self, year_range: tuple[int, int]):
        rainfall = self.rainfall_repo.get_records(year_range)
        yields = self.yield_repo.get_records(year_range)

        # 🔬 Domain logic here (compute drought index, correlate yield drop, etc.)
        report = compute_drought_impact(rainfall, yields)

        return report
```

---

## 🤖 AI Services: Focus Mode + Local LLM (Ollama)

KFM’s **Focus Mode** is designed to run a **local LLM via Ollama**, with governance:
- AI only uses **approved tools/APIs**
- AI must provide **citations** for factual claims
- Output is run through a **policy engine** before returning
- Typical backend endpoint shape: `POST /ai/query`

### Recommended service split
- `AiQueryService`: orchestration + policy + provenance
- `RetrievalService`: semantic search / “search database” tooling
- `CitationService`: normalizes and attaches citations
- `PolicyService`: allow/deny/sanitize decisions

```python
class AiQueryService:
    def __init__(self, llm_client, retrieval, policy, provenance, citation):
        self.llm = llm_client
        self.retrieval = retrieval
        self.policy = policy
        self.provenance = provenance
        self.citation = citation

    def answer(self, user, question: str):
        # 1) Pre-check question (fail closed)
        self.policy.precheck_ai_question(user=user, question=question)

        # 2) Retrieve grounded context (safe tools only)
        snippets = self.retrieval.fetch_context(question)

        # 3) Ask local LLM (Ollama) for answer + citations
        raw = self.llm.generate(question=question, context=snippets)

        # 4) Attach/normalize citations + enforce policy on final answer
        answered = self.citation.attach(raw, snippets)
        self.policy.postcheck_ai_answer(user=user, answer=answered)

        # 5) Record provenance / audit trail
        self.provenance.record_ai_interaction(user=user, question=question, answer=answered)

        return answered
```

> ✨ Design goal: AI isn’t an oracle — it “shows its work” by retrieving data and citing it.

---

## 🧩 How Routes Should Use Services

Routes/controllers should be *thin*:
- parse & validate inputs
- call service
- serialize outputs

### REST
- Swagger UI typically lives at: `/docs`

### GraphQL (optional)
Resolvers should call the **same services** as REST to avoid duplicating business logic.

---

## 🧱 Adding a New Service (Checklist)

1. **Name it by use-case**: `parcel_service.py`, `analysis_service.py`, `ai_query_service.py` 🏷️  
2. Define/confirm the **domain model** you’ll return (`api/models` or `api/domain`) 🧬  
3. Add or reuse **repository interfaces** (no direct DB calls) 🔌  
4. Implement service logic (pure, deterministic where possible) 🧠  
5. Add policy hooks (pre/post checks) 🛡️  
6. Add provenance hooks if outputs must be traceable 🧾  
7. Write unit tests with mocked repos ✅  
8. Wire it into routes/resolvers with DI 🧰  

---

## 🧨 Common Pitfalls (Avoid These)

- ❌ Service imports FastAPI objects (`Request`, `Depends`, `HTTPException`)
- ❌ SQL/Cypher query strings embedded in service methods
- ❌ Returning raw DB rows or ORM models instead of domain models
- ❌ Skipping policy checks because “it’s just internal”
- ❌ Generating AI answers without citations / provenance

---

## 🔗 Handy Navigation

- 📁 `api/routes/` — HTTP endpoints (thin controllers)
- 📁 `api/repositories/` / `api/adapters/` — external integration surface
- 📁 `api/db/` — PostGIS/Neo4j clients and sessions
- 📁 `policy/` — policy-as-code (OPA/Rego), governance rules

---

## 🧭 Service Quality Bar (Quick Scorecard)

| Requirement | Must? | Notes |
|---|:---:|---|
| Pure business logic (no framework) | ✅ | Keep route handlers thin |
| Uses repository interfaces | ✅ | No direct DB access |
| Easy to unit test | ✅ | Mock repos |
| Policy enforcement | ✅ | Fail closed |
| Provenance hooks where needed | ✅ | Especially for AI + derived artifacts |
| Returns domain models / DTOs | ✅ | Stable contracts |

---

<details>
  <summary>📦 “What belongs in services vs repositories vs routes?”</summary>

- **Routes**: request/response boundary (HTTP), validation, status codes  
- **Services**: orchestration + business rules + workflows  
- **Repositories/Adapters**: “how to fetch/store data” (PostGIS/Neo4j/external APIs)  
- **Domain Models**: shared language across all layers  

</details>