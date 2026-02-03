# 🧩 `api/adapters/` — Integration Layer (Ports & Adapters)

![Layer](https://img.shields.io/badge/layer-integration%20%2F%20adapters-blue)
![Architecture](https://img.shields.io/badge/architecture-clean%20%2B%20hexagonal-6f42c1)
![Scope](https://img.shields.io/badge/scope-external%20I%2FO-orange)
![Governance](https://img.shields.io/badge/governance-fail--closed-critical)

> [!NOTE]
> **Adapters are the only place where we “touch the outside world”** from the API codebase: databases, search, object storage, external services, and policy engines.  
> Everything above this layer stays **framework-agnostic** and **storage-agnostic**.

---

## 🧭 What belongs in `api/adapters/`?

This directory implements the **Integration / Adapter Layer** (aka **Ports & Adapters**, **Hexagonal Architecture**) that bridges:

- ✅ **Service / Use-case layer** (business logic)
- ✅ **Domain models** (Pydantic / plain models)
- ⛔ External systems (PostGIS, Neo4j, search indices, STAC/DCAT catalogs, object storage, 3rd-party APIs, OPA)

**Adapters translate “our language” ↔ “their language”**:
- Domain objects ↔ DB rows / graph nodes / search documents
- Domain queries ↔ SQL / Cypher / search DSL / REST calls
- Domain errors ↔ external error formats

---

## 🧱 Where this sits in the architecture

```mermaid
flowchart TB
  subgraph Domain["🧠 Domain Layer"]
    D["Domain Models\n(Pydantic / Plain Models)"]
  end

  subgraph Services["🧪 Service / Use-Case Layer"]
    S["Services / Use-cases\n(Orchestrate domain + rules)"]
  end

  subgraph Adapters["🧩 Integration Layer (THIS FOLDER)"]
    A["Adapters / Repositories\n(DB/Graph/Search/API clients)"]
  end

  subgraph Infra["🧰 Infrastructure Layer"]
    API["FastAPI Routers / Controllers\n(HTTP contract)"]
    DI["Dependency Injection\n(Settings, Sessions, Clients)"]
  end

  subgraph External["🌍 External Systems"]
    PG[(PostGIS)]
    N4J[(Neo4j)]
    IDX[(Search Index)]
    OBJ[(Object Storage)]
    EXT[(External APIs)]
    OPA[(OPA Policy Engine)]
  end

  API --> S
  S --> A
  A --> PG
  A --> N4J
  A --> IDX
  A --> OBJ
  A --> EXT
  API -.policy checks.-> OPA
```

---

## 🧩 Adapter types you’ll typically see

> [!TIP]
> If you’re unsure where code goes: **If it performs I/O, it’s an adapter.**  
> If it decides *what should happen*, it’s a service.  
> If it defines *what something is*, it’s domain.

### 🗺️ Databases & stores
- **PostGIS adapters**: spatial queries, geometry handling, spatial joins, bounding boxes
- **Neo4j adapters**: relationship traversal, context linking, provenance/graph navigation
- **Search adapters**: keyword search, faceting, autocomplete, ranking
- **Object storage adapters**: COGs/tiles/assets, signed URLs, blob lifecycle

### 🌦️ External services
- Weather feeds, geocoders, enrichment services, notification hooks, etc.

### 🛡️ Governance helpers
- OPA / policy-check clients (often called as middleware or route-level checks)

---

## ✅ Golden rules (non-negotiables)

### ✅ DO
- Keep adapters **thin**, **boring**, and **predictable**
- Use **parameterized queries** (SQL/Cypher) — never string-concat user input
- Return **domain models** (or DTOs) that services can consume cleanly
- Centralize configuration via a **settings module** (env-driven)
- Add **structured logging** and propagate **request/correlation IDs**
- **Fail closed**: if policy/data/provenance checks cannot be performed, deny/stop
- Prefer **small, composable methods** over “do-everything” mega calls

### ❌ DON’T
- Put business rules in adapters (no scoring logic, no governance decisions, no UI shaping)
- Import FastAPI request objects into adapters
- Return raw DB cursors/rows to services
- Bake environment lookups (`os.environ[...]`) into every method (use settings + DI)
- Bypass the canonical pipeline/canonical stores “just to ship faster”

---

## 📦 Suggested folder layout

> [!NOTE]
> Exact names vary by repo evolution — but keep the intent consistent.

```text
api/
  adapters/
    README.md ✅
    __init__.py

    postgis/
      __init__.py
      client.py              # engine/session/pool creation helpers
      parcels_repo.py        # example repository focused on one bounded context
      sql/                   # optional: .sql templates kept separate from logic
        parcels.sql

    neo4j/
      __init__.py
      client.py
      graph_repo.py
      cypher/
        related_events.cypher

    search/
      __init__.py
      client.py
      search_repo.py

    external/
      __init__.py
      weather_adapter.py     # example external integration
      geocode_adapter.py

    policy/
      __init__.py
      opa_client.py          # if policy checks are invoked from API or services

    common/
      __init__.py
      errors.py              # shared exception types + mapping helpers
      retries.py             # backoff, circuit breakers (if used)
      telemetry.py           # tracing helpers (if used)
```

---

## 🔌 Ports (interfaces) live above adapters

Adapters should implement **ports** (interfaces) defined in a more “inner” layer (often `api/services/ports.py`, `api/domain/ports.py`, or similar).

### Example: define a port (protocol)

```python
from typing import Protocol, Iterable, Optional
from api.domain.models import LandParcel

class LandParcelRepository(Protocol):
    async def get_by_id(self, parcel_id: str) -> Optional[LandParcel]:
        ...

    async def search_by_bbox(
        self,
        west: float,
        south: float,
        east: float,
        north: float,
        limit: int = 100,
    ) -> Iterable[LandParcel]:
        ...
```

### Example: implement the port in a PostGIS adapter

```python
from typing import Optional, Iterable
from api.domain.models import LandParcel
from api.adapters.common.errors import RepositoryError

class PostGISLandParcelRepository:
    def __init__(self, pool):
        self._pool = pool

    async def get_by_id(self, parcel_id: str) -> Optional[LandParcel]:
        try:
            row = await self._pool.fetchrow(
                "SELECT id, owner, geom_geojson FROM parcels WHERE id = $1",
                parcel_id,
            )
            if not row:
                return None
            return LandParcel(
                id=row["id"],
                owner=row["owner"],
                geom=row["geom_geojson"],
            )
        except Exception as e:
            raise RepositoryError("postgis:get_by_id failed") from e

    async def search_by_bbox(
        self, west: float, south: float, east: float, north: float, limit: int = 100
    ) -> Iterable[LandParcel]:
        # Keep queries parameterized + indexed (geom && bbox + ST_Intersects, etc.)
        ...
```

> [!TIP]
> Keep SQL/Cypher readable. If a query becomes long, move it to `sql/` / `cypher/` and load it as a template.

---

## 🧯 Error handling & “translation”

Adapters should **translate low-level failures** into a small set of meaningful exceptions for services to handle.

### Recommended exception taxonomy
- `RepositoryError` — store failed / driver failure / malformed query
- `NotFoundError` — if you want explicit not-found signals (optional)
- `ConflictError` — constraint violations / duplicate keys (optional)
- `UpstreamUnavailable` — external API down / timeout (optional)
- `PolicyDenied` — if adapters are doing policy checks (usually route-level instead)

> [!WARNING]
> Never leak credentials, raw query text, or internal stack traces into API responses.

---

## 🧷 Connection lifecycle & dependency injection

**Create connections once** (startup) and **inject them** (request scope) rather than recreating per call.

- PostGIS: connection pool / SQLAlchemy session managed by DI
- Neo4j: driver singleton + session per request (or per operation)
- Search: client singleton

> [!TIP]
> If you see `create_engine()` or `GraphDatabase.driver()` inside adapter methods, it’s a smell.

---

## 🧪 Testing strategy

### ✅ Unit tests (fast)
- Mock ports and test services in isolation
- Test adapter “mappers” (row → domain) without needing a DB

### 🧱 Integration tests (real)
- Run PostGIS / Neo4j / search with Docker Compose
- Validate:
  - migrations / schema
  - spatial indexes and query performance basics
  - Cypher correctness and relationship traversals
  - end-to-end adapter calls

Suggested pattern:
- `tests/unit/...` for service logic
- `tests/integration/...` for adapters
- Use `pytest` + fixtures (`db_pool`, `neo4j_driver`, etc.)

---

## ➕ Adding a new adapter (checklist)

1. **Define the port** (interface) in the inner layer
2. Create adapter module under `api/adapters/<system>/...`
3. Implement:
   - connection/client wiring (prefer centralized DI)
   - mapper(s): external ↔ domain
   - minimal, well-named methods (avoid “kitchen sink”)
4. Add:
   - unit tests for mapping
   - integration test hitting the real system (if applicable)
5. Wire into service via DI (route → service → port → adapter)

---

## 🔍 PR review checklist (quick)

- [ ] No business rules in adapter ✅
- [ ] No raw SQL/Cypher concatenation ✅
- [ ] Domain models returned (or clear DTOs) ✅
- [ ] Errors translated into adapter exceptions ✅
- [ ] Logging is structured + safe ✅
- [ ] Integration tests added/updated ✅
- [ ] No direct DB calls from routes/controllers ✅

---

## 📚 Related docs (recommended reading)

- `docs/architecture/system_overview.md` (architecture + “truth path”)
- `docs/governance/` (policy + compliance)
- `api/README.md` or `api/docs/` (API conventions)

---

### 🏁 Bottom line

Adapters are the **controlled boundary** between KFM’s governed “truth path” and the outside world.  
Keep them **thin**, **secure**, **testable**, and **boringly reliable** ✅