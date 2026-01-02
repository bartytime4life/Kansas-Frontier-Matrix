<div align="center">

# 🧠 `kfm_api.application`

_The **use-case orchestration layer** for the Kansas Frontier Matrix (KFM) API — where workflows live, not frameworks._

![Clean Architecture](https://img.shields.io/badge/Clean%20Architecture-layered%20%26%20testable-brightgreen)
![Ports & Adapters](https://img.shields.io/badge/Ports%20%26%20Adapters-interfaces%20first-blue)
![API Edge](https://img.shields.io/badge/API%20Edge-FastAPI%20%2F%20Flask%20(outside%20this%20layer)-teal)
![Focus](https://img.shields.io/badge/Focus-Use%20cases%20%26%20orchestration-orange)

</div>

---

## 🎯 Purpose (what this folder is for)

The `application/` package is the **“service layer”** of KFM’s backend: it implements the system’s **use cases** (cohesive workflows) and coordinates domain logic with the outside world **through interfaces**.

Think “_what the system does_” (policy + orchestration), not “_how HTTP works_” or “_how PostGIS stores geometries_”.

Examples of KFM-style use cases:
- 🌱 **Calculate irrigation recommendation** for a field
- 🌾 **Generate NDVI time series** for a selected field/time range
- 🌧️ **Identify areas at risk of drought**
- 🧪 **Run a simulation scenario** and return a job ID
- 🔐 **User login / authentication orchestration** (policy-level flow)

---

## 🧭 Golden rule (memorize this)

> **Talk inwards with simple structures, talk outwards through interfaces.**

If you remember only one thing about `application/`, make it that. ✅

---

## ✅ What belongs here

### 🧩 Use-case orchestration
- A use case = a focused workflow that coordinates domain entities and calls outward via ports.
- Keep each use case **small & single-responsibility** (one coherent goal per use case).

### 🔌 Ports (interfaces) for the outside world
Define **contracts** for things the use case needs, such as:
- `FieldRepository`, `SoilDataRepository`, `TimeseriesRepository`
- `SimulationQueue`, `JobStatusStore`
- `ModelInferenceGateway` (ML inference)
- `TileServiceGateway` (rendering / tiles)
- `EventBus` / `Publisher`

### 📦 App DTOs (request/response objects)
- Use-case **request objects**: validated input to the use case (not HTTP-specific)
- Use-case **response objects**: structured success/error output (not HTTP-specific)

### 🧯 Application-level errors
- Input validation errors
- Not-found errors
- Authorization/policy failures (if not fully handled at the API edge)
- Error mapping into response objects

---

## 🚫 What does *not* belong here

> ⚠️ Rule of thumb: **If it needs a running DB, web server, or cloud account to unit-test, it probably does not belong here.**

Avoid importing or depending on:
- 🌐 **FastAPI/Flask routers/controllers**
- 🧬 **SQLAlchemy / raw SQL / PostGIS specifics**
- 📡 `requests`, cloud SDKs (e.g., `boto3`), direct network calls
- 🧰 environment parsing (`os.environ`), config loading, secrets
- 🧵 background worker frameworks (Celery/RQ/etc) **directly**  
  ✅ Instead: define a `TaskQueuePort` (or similar) and inject an implementation.

---

## 🗺️ Layer map (where `application` sits)

```text
🧅 Clean Architecture (KFM backend)

┌─────────────────────────────────────────────────────────────┐
│  🌐 Interface Layer (FastAPI/Flask, controllers, schemas)    │
│  - HTTP/JSON concerns, auth middleware, request parsing      │
└───────────────▲───────────────────────────────┬─────────────┘
                │ maps HTTP → Request DTO       │ maps Response → HTTP
                │                               
┌───────────────┴───────────────────────────────▼─────────────┐
│  🧠 Application Layer  ← YOU ARE HERE                         │
│  - Use cases + orchestration                                  │
│  - Port interfaces (repositories, gateways, queues)            │
│  - Request/Response objects                                    │
└───────────────▲───────────────────────────────┬─────────────┘
                │ imports domain models          │ calls ports (interfaces)
                │
┌───────────────┴───────────────────────────────▼─────────────┐
│  🧱 Domain Layer (entities, value objects, rules)              │
│  - Pure models (no DB, no HTTP, no framework)                  │
└───────────────▲───────────────────────────────┬─────────────┘
                │                               │ implements ports
                │                               │
┌───────────────┴───────────────────────────────▼─────────────┐
│  🏗️ Infrastructure Layer (DB, PostGIS, queues, external APIs)  │
│  - Adapters implementing ports                                 │
│  - ORM/SQL, Celery/RQ, HTTP clients, SDKs                       │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔁 Typical data flow (end-to-end)

```mermaid
flowchart LR
  UI[🧑‍🌾 Frontend / External Client] -->|HTTP| API[🌐 Interface Layer\n(FastAPI router/controller)]
  API -->|Request DTO| UC[🧠 Application Use Case]
  UC -->|calls Port interface| PORT[🔌 Port\n(Repository/Gateway/Queue)]
  PORT -->|implemented by| ADAPTER[🏗️ Infrastructure Adapter]
  ADAPTER -->|SQL/PostGIS / RPC / Queue| EXT[(External System)]
  UC -->|Response DTO| API -->|JSON| UI
```

---

## 📦 Suggested module layout (inside `application/`)

<details>
<summary><strong>📁 Recommended structure</strong> (adjust to match current code)</summary>

```text
application/
  README.md                      👈 you are here
  __init__.py

  use_cases/
    field_timeseries/
      __init__.py
      use_case.py                # orchestration
      request.py                 # request object / validation
      response.py                # response object (success + errors)
    simulation_run/
      use_case.py
      request.py
      response.py

  ports/
    repositories.py              # Protocols / ABCs
    gateways.py                  # external service interfaces
    queues.py                    # background task interfaces

  dto/
    common.py                    # shared DTOs (pagination, time-range, etc.)

  errors.py                      # shared app-level error types
```

</details>

---

## 🧪 How to add a new use case (KFM pattern)

### 1) Define the use case goal 🎯
Example: “Return NDVI time series for a field” or “Start simulation run and return job ID”.

### 2) Create Request / Response DTOs 📬📤
- Request: parse + validate inputs the use case needs
- Response: represent success data and standardized errors

### 3) Define required ports 🔌
If you need IO (DB, queue, HTTP), define an interface here:
- `TimeseriesRepositoryPort`
- `SimulationQueuePort`
- `JobStatusPort`

### 4) Implement the use case 🧠
- Keep it pure orchestration
- Use ports for IO
- Compose domain entities (and call domain rules) to produce the result

### 5) Implement adapters elsewhere 🏗️
Infrastructure layer implements the ports (Postgres/PostGIS, Celery/RQ, ML service, etc.).

### 6) Wire it at the edge 🌐
Interface layer:
- Convert HTTP → Request DTO
- Instantiate use case with adapters
- Convert Response DTO → HTTP response

### 7) Tests ✅
- Unit test the use case with fake/mocked ports
- Integration test adapters separately

### 8) Contract-first docs 📜
When a use case affects the API surface:
- Update the API contract docs & templates (and version appropriately)

---

## 🧱 Minimal use case template (copy/paste friendly)

> This is intentionally “framework-free” to keep `application/` portable and testable.

```python
# application/use_cases/field_timeseries/use_case.py

from dataclasses import dataclass
from typing import Protocol, Sequence

# --- Ports (interfaces) ---

class TimeseriesRepositoryPort(Protocol):
    def get_field_timeseries(self, *, field_id: str, var: str) -> Sequence[dict]:
        """Return time series points (domain objects or plain dicts)."""
        ...


# --- Request/Response DTOs ---

@dataclass(frozen=True)
class FieldTimeseriesRequest:
    field_id: str
    var: str  # e.g., "ndvi"

    def validate(self) -> None:
        if not self.field_id:
            raise ValueError("field_id is required")
        if not self.var:
            raise ValueError("var is required")


@dataclass(frozen=True)
class FieldTimeseriesResponse:
    points: Sequence[dict]


# --- Use case ---

class GetFieldTimeseriesUseCase:
    def __init__(self, repo: TimeseriesRepositoryPort):
        self._repo = repo

    def execute(self, req: FieldTimeseriesRequest) -> FieldTimeseriesResponse:
        req.validate()
        points = self._repo.get_field_timeseries(field_id=req.field_id, var=req.var)
        return FieldTimeseriesResponse(points=points)
```

---

## 🧯 Error handling style

A clean, consistent approach is:

- Request validation errors → structured error response (not raw exceptions)
- Not found / forbidden → explicit “typed” errors the interface layer can map to HTTP codes
- External failures (DB down, queue unavailable) → port-level errors mapped into application-level errors

<details>
<summary><strong>✅ Practical guideline</strong></summary>

- **Do**: return a response object that can represent success or failure.
- **Do**: keep error types in `application/errors.py` (app-level meaning).
- **Don’t**: leak SQLAlchemy exceptions, HTTP errors, or framework-specific errors across the boundary.

</details>

---

## 🧪 Testing strategy (what “good” looks like)

### Unit tests (fast, most important) ⚡
- Run use cases against **fake/mocked ports**
- Assert on response DTOs (not HTTP, not DB state)

### Integration tests (slower) 🧱
- Test infrastructure adapters against real services (Postgres/PostGIS, queue, etc.)
- Keep them separate from use-case unit tests

> ✅ Goal: business logic is testable “in isolation” without running the stack.

---

## ✅ PR checklist (application layer)

- [ ] New use case is **single-purpose** and named clearly
- [ ] No FastAPI/Flask/ORM imports in `application/`
- [ ] IO done only through **ports**
- [ ] Request/Response objects exist (or clearly justified)
- [ ] Unit tests added (mock ports)
- [ ] API contract updated if endpoints changed
- [ ] Logging/telemetry is boundary-safe (no secrets, no PII)

---

## 🔗 Related docs (project-wide)

- 📘 KFM master technical documentation (architecture, layering, backend/API approach)
- 🧾 Contract-first templates & standards (API contract extension template, master guide)
- 🧱 Clean Architecture references (ports/adapters, use cases, request/response objects)

> If you’re unsure where something belongs, start by asking:
> **“Is this policy/orchestration, or is this a technical detail?”**  
> Policy → `application/` ✅ | Technical detail → outer layers 🏗️