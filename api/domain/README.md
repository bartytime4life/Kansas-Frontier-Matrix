# 🧠 Domain Layer — `api/domain/`  
![Layer](https://img.shields.io/badge/layer-domain-informational) ![Architecture](https://img.shields.io/badge/architecture-clean%20%2F%20hexagonal-blue) ![Backend](https://img.shields.io/badge/backend-FastAPI-success) ![Focus](https://img.shields.io/badge/principle-provenance--first-purple)

> **Purpose:** This package holds KFM’s **core domain models + invariants** (the “meaning” of the system), designed to be **framework-agnostic** and reusable across services, tests, and adapters.  
> In KFM, *all access flows through the backend API* (UI doesn’t touch databases directly), and the domain is how we keep that “truth path” consistent.  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 🔭 Why this folder exists

KFM is designed as a **Raw → Processed → Catalog/Prov → Database → API → UI** pipeline, and features that bypass this order are considered flawed unless proven otherwise. [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

The domain layer is where we encode the *meaning* of KFM objects (datasets, events, story nodes, places, provenance, etc.) independent of:
- web frameworks (FastAPI),
- storage engines (PostGIS / Neo4j / search),
- external APIs (GEE, weather, geocoding),
- UI concerns.

This aligns with KFM’s clean architecture approach: **domain at the center**, surrounded by use-cases/services, then adapters/integration, then delivery (routes). [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 🧱 Clean / Hexagonal positioning

The domain layer is the **center**. Inbound adapters (HTTP/REST endpoints) *invoke* domain-facing services; outbound adapters (DB/external) are *invoked by* use-cases. This is the same “business logic at the center” idea commonly described as **hexagonal architecture**. [oai_citation:3‡Data Spaces.pdf](sediment://file_0000000053c071f5a9733b1b09cc9f76)

```mermaid
flowchart LR
  UI[🖥️ Web UI] -->|REST/GraphQL| R[🚪 FastAPI Routers]
  AI[🤖 Focus Mode AI] -->|same API| R
  R --> S[🧰 Use-cases / Services]
  S --> D[🧠 Domain Models + Invariants]
  S --> P[🛡️ Policy checks (OPA + rules)]
  S --> A[🔌 Adapters / Repos]
  A --> PG[(🗺️ PostGIS)]
  A --> N4J[(🕸️ Neo4j)]
  A --> IDX[(🔎 Search/Embeddings)]
```

KFM explicitly centralizes governance checks and provenance logging at the API boundary (routes/services), so domain models must stay **compatible with audit + policy needs**. [oai_citation:4‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## ✅ What belongs in `api/domain/`

KFM’s blueprint describes a domain module such as `api/domain/` where core entities live, often as **Pydantic models for validation**, and with small helper methods (e.g., GeoJSON representation) *but no DB/framework coupling*. [oai_citation:5‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### 🧩 Typical contents

- **Entities (core concepts)**
  - `Dataset`, `Layer`, `StoryNode`, `HistoricalEvent`, `Place`, `Source`, `Citation`, `ProvenanceRecord`
- **Value Objects**
  - `TimeRange`, `BBox`, `GeoJSONGeometry`, `CRS`, `LicenseRef`, `SensitivityLabel`
- **Domain Errors**
  - `DomainValidationError`, `InvariantViolation`, `PolicyRequired`
- **Domain Events**
  - `DatasetPublished`, `StoryNodeRendered`, `PolicyDenied`, `ProvenanceAttached`
- **Repository Interfaces (Protocols)**
  - “ports” that services depend on; adapters implement these (PostGIS/Neo4j/etc.)
- **Minimal helpers**
  - serialization utilities, normalizers, ID parsing, etc.

---

## 🚫 What does *not* belong here

Keep domain “pure” and testable. [oai_citation:6‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

✅ **Avoid placing these in `api/domain/`:**
- FastAPI routers, dependencies, request handlers
- SQLAlchemy models/sessions, Cypher query strings, ORM mappings
- HTTP clients, external service SDK calls
- Background workers, queues, cron job logic
- Anything that reads env vars directly

👉 Those belong in:
- `api/routes/` (delivery layer)
- `api/services/` or `api/use_cases/` (business workflows)
- `api/db/`, `api/adapters/`, `api/repositories/` (integration layer) [oai_citation:7‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 📁 Suggested folder layout

> This is the recommended **shape** (adapt as needed, but keep the boundaries clean).

```text
📦 api/
  ├─ 📁 domain/
  │  ├─ README.md ✅ (you are here)
  │  ├─ 📁 entities/
  │  │  ├─ dataset.py
  │  │  ├─ story_node.py
  │  │  ├─ historical_event.py
  │  │  └─ place.py
  │  ├─ 📁 value_objects/
  │  │  ├─ ids.py
  │  │  ├─ geo.py
  │  │  ├─ time.py
  │  │  └─ provenance.py
  │  ├─ 📁 ports/               # repo interfaces (Protocols)
  │  │  ├─ dataset_repo.py
  │  │  ├─ story_repo.py
  │  │  └─ graph_repo.py
  │  ├─ 📁 events/
  │  │  └─ domain_events.py
  │  ├─ 📁 errors/
  │  │  └─ exceptions.py
  │  └─ __init__.py
```

---

## 🧷 Domain invariants (KFM-flavored)

KFM is **provenance-first**: “every layer, dataset, story, and even AI-generated answer is traceable back to original sources.” [oai_citation:8‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

So, in practice, domain entities should be able to support invariants like:

### 🔎 Provenance required (by design)
- A `Dataset` should be able to reference:
  - a catalog record (e.g., STAC/DCAT pointer),
  - provenance record (e.g., W3C PROV pointer),
  - license + attribution.

### 🛡️ Fail-closed governance posture
If checks fail, KFM blocks the action (“fail closed”). [oai_citation:9‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

**Implication for domain modeling:**  
Prefer explicit fields + validations that make it *hard* to create “source-less” objects.

---

## 🧪 Code patterns (recommended)

### 1) Repository port (interface) lives in the domain ✅
```python
# api/domain/ports/story_repo.py
from __future__ import annotations
from typing import Protocol, Sequence
from api.domain.value_objects.ids import StoryNodeId
from api.domain.entities.story_node import StoryNode

class StoryNodeRepository(Protocol):
    def get(self, id: StoryNodeId) -> StoryNode | None: ...
    def search(self, *, query: str, limit: int = 50) -> Sequence[StoryNode]: ...
```

### 2) Adapter implements the port ❇️ (outside domain)
```python
# api/adapters/story_repo_postgis.py  (example location)
from api.domain.ports.story_repo import StoryNodeRepository

class PostGISStoryNodeRepository(StoryNodeRepository):
    ...
```

### 3) Domain entity stays serialization-friendly 🧊
The blueprint suggests domain models may include helper methods like “to GeoJSON” but should avoid DB/framework dependencies. [oai_citation:10‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

```python
# api/domain/entities/place.py
from pydantic import BaseModel, Field
from api.domain.value_objects.geo import GeoJSONGeometry

class Place(BaseModel):
    id: str
    name: str
    geometry: GeoJSONGeometry = Field(..., description="GeoJSON geometry object")

    def as_geojson_feature(self) -> dict:
        return {
            "type": "Feature",
            "properties": {"id": self.id, "name": self.name},
            "geometry": self.geometry.model_dump(),
        }
```

---

## 🛠️ Adding a new domain concept

### ✅ Checklist
1. **Define IDs & value objects first** (`value_objects/`)
2. Create entity model in `entities/`
3. Add **invariants** via validation (required provenance fields, time bounds, etc.)
4. Define a **port** (Protocol) in `ports/` if it needs persistence/query access
5. Write **unit tests** for invariants (domain tests should not need DB)
6. Only then:
   - implement adapters (PostGIS/Neo4j/etc.)
   - wire it into service/use-case layer
   - expose via routes

---

## 🧾 Documentation protocol (recommended)

To keep docs trustworthy and reviewable, KFM-style docs may include consistent metadata + references to governance policies and ethics notes (when relevant). [oai_citation:11‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)

Consider adding (optional) metadata **in an HTML comment** to avoid cluttering README rendering:

```md
<!--
doc_kind: README
path: api/domain/README.md
owner: api-team
governance_ref: policy/
fair_care: FAIR+CARE
-->
```

---

## 🔗 Where to look next

- `api/services/` — use-cases that orchestrate domain objects and ports  
- `api/routes/` — FastAPI routers (delivery layer)  
- `api/db/` / `api/adapters/` — PostGIS, Neo4j, search adapters; keep SQL/Cypher here [oai_citation:12‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 📚 Sources & further reading

### Core architecture / domain placement
- Kansas Frontier Matrix (KFM) Blueprint (clean architecture, domain purity, api/domain mention) [oai_citation:13‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) [oai_citation:14‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) [oai_citation:15‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### Data-spaces / hexagonal framing
- Data Spaces (hexagonal architecture framing + cross-cutting concerns) [oai_citation:16‡Data Spaces.pdf](sediment://file_0000000053c071f5a9733b1b09cc9f76) [oai_citation:17‡Data Spaces.pdf](sediment://file_0000000053c071f5a9733b1b09cc9f76)  [oai_citation:18‡Data Spaces.pdf](sediment://file_0000000053c071f5a9733b1b09cc9f76)

### Time-series & temporal UX foundations (for future domain models)
- Visualization of Time-Oriented Data  [oai_citation:19‡Visualization of Time-Oriented Data.pdf](sediment://file_000000001468722f929b8752236e5a72)

### Remote sensing integration (for future domain models)
- Cloud-Based Remote Sensing with Google Earth Engine  [oai_citation:20‡Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf](sediment://file_00000000a58071f586f00793dee712d6)