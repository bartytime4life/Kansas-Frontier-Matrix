# 🔌 `api/adapters/` — Integration Layer (Interfaces & Adapters)

![Python](https://img.shields.io/badge/Python-Adapters-informational)
![Architecture](https://img.shields.io/badge/Architecture-Clean%20%2F%20Hexagonal-blue)
![API](https://img.shields.io/badge/API-FastAPI-009688)
![Policy](https://img.shields.io/badge/Design-Provenance--first-important)

> 🧠 **Why this folder exists:** KFM uses a Clean Architecture style where the **integration (adapter) layer** bridges **pure service/use-case logic** to external systems like databases and third-party APIs. In this repo, those bridges live under modules like `api/db/` and `api/adapters/`. [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 🧭 What belongs in `api/adapters/`?

This folder contains **implementations** that talk to “the outside world”:

- 🗄️ Database access (repositories/adapters for PostGIS, Neo4j, etc.)
- 🌐 External services (geocoding, weather, enrichment APIs)
- 🔎 Search services (e.g., Elastic-like full-text search)
- 📦 File/stream connectors (if the API needs to read/write external filesystems, object stores, etc.)

KFM’s blueprint explicitly calls out this layer as the bridge between service logic and external systems, and even name-drops typical examples like `PostGISRepository`, `Neo4jAdapter`, `ElasticSearchAdapter`, and external API adapters such as an `OpenWeatherMapAdapter` or a geocoding service. [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

✅ **Golden rule:** adapters are *infrastructure glue* — they **do not** contain business decisions.

---

## 🚫 What does *not* belong here?

Avoid putting these in `api/adapters/`:

- 🧠 **Business logic / rules** (belongs in service/use-case layer)
- 🧾 Domain entities / schemas (belongs in domain models)
- 🛣️ FastAPI route handlers (belongs in the API “inbound” layer, typically `api/routes/` or similar)
- 🧩 Orchestration across multiple adapters (belongs in services/use-cases)

KFM is designed so the UI never talks directly to databases; access is mediated via the backend API and its governance/validation flow. [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 🧱 “Ports & Adapters” mental model (quick)

KFM follows a **Clean / Hexagonal** architecture style: business logic is central; adapters are on the outside. The “port” is the **interface** your service layer expects; the “adapter” is the concrete implementation.

A supporting reference describes hexagonal architecture as placing business logic at the center, with **inbound adapters** handling requests and **outbound controllers/adapters** invoked by business logic to call external systems. [oai_citation:4‡Data Spaces.pdf](sediment://file_0000000053c071f5a9733b1b09cc9f76)

### In KFM terms

- **Inbound adapters** ✅: FastAPI controllers/routers (request in → call service)
- **Outbound adapters** ✅: DB clients, API clients, repositories (service → fetch/store externally)

---

## 📁 Suggested structure (recommended)

Your exact layout may vary, but aim for **small, composable adapters** with clean boundaries:

```text
📦 api/
 ├─ 🧩 adapters/
 │   ├─ __init__.py
 │   ├─ 🗄️ neo4j/
 │   │   ├─ adapter.py          # Neo4jAdapter
 │   │   ├─ queries.py          # Cypher strings, query builders
 │   │   └─ mapping.py          # DB ↔️ Domain mapping
 │   ├─ 🔎 search/
 │   │   ├─ elastic.py          # ElasticSearchAdapter (if used)
 │   │   └─ mapping.py
 │   ├─ 🌐 external/
 │   │   ├─ geocoding.py        # GeocodingService adapter
 │   │   ├─ weather.py          # OpenWeatherMapAdapter (optional)
 │   │   └─ http_client.py      # shared resilient client
 │   └─ 🧰 shared/
 │       ├─ errors.py           # AdapterError, retryable vs non-retryable
 │       └─ telemetry.py        # logging/provenance hooks
 └─ 🗄️ db/
     ├─ postgis.py              # PostGISRepository (often fits here too)
     └─ session.py              # engine/session wiring (infra)
```

The blueprint explicitly lists integration/adapters as being under `api/` and mentions subdirectories like `db/`, `repositories/`, or `adapters/` for external system interaction. [oai_citation:5‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## ✨ Adapter conventions (KFM-style)

### 1) Interfaces live in the service layer ✅
Define **ports** (interfaces / protocols / ABCs) in the service layer. Then implement them here.

Why: This keeps business logic testable and independent of infrastructure. It also lets KFM swap implementations without changing upper layers (e.g., swap PostGIS or change an external API call). [oai_citation:6‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### 2) Adapters implement those interfaces ✅
The blueprint notes that adapters often implement interfaces defined in the service layer and should keep credentials/queries separate from logic. [oai_citation:7‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### 3) Configuration is handled at the edge ✅
Adapters manage configuration like DB URLs and API keys, typically from environment variables or config files. [oai_citation:8‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### 4) Keep “mapping” explicit ✅
Adapters should translate:
- External shapes (rows, JSON, Cypher results)
- → domain/service-level models (Pydantic/domain entities)

This is where subtle data-quality issues get handled *without contaminating business logic*.

---

## 🔐 Configuration & secrets

**Do:**
- ✅ Read connection URLs / keys from env or config
- ✅ Separate credentials from logic
- ✅ Keep queries (SQL/Cypher) in their own module when they get big
- ✅ Fail “loud” with actionable error messages for misconfig

**Don’t:**
- ❌ Commit secrets
- ❌ Hardcode endpoints
- ❌ Scatter query strings across the codebase

(These practices align with the blueprint’s guidance on adapters managing config and keeping credentials/queries separate.) [oai_citation:9‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 🧪 Testing strategy

### ✅ Unit tests (fast)
- Mock the external client
- Assert mapping + error handling
- Assert “port contract” behavior

### ✅ Contract tests (recommended)
- Use a lightweight test container (PostGIS/Neo4j/etc.)
- Verify schema expectations, query correctness, and mapping

### ✅ Service layer tests (most important)
Because service logic depends on **interfaces**, you can test services with in-memory fakes—no DB required.

---

## ➕ Add a new adapter (checklist)

1. 🧾 **Define the port** in the service layer (interface/protocol)
2. 🧩 **Implement the adapter** in `api/adapters/<name>/...`
3. 🧠 **Keep business logic out** (adapter = IO + mapping + resilience)
4. 🔐 **Add config** (env/config file; never hardcode secrets) [oai_citation:10‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
5. 🪝 **Wire it into DI** (FastAPI dependency injection or your wiring module)
6. 🧪 **Add tests** (unit + contract if relevant)
7. 📝 **Document usage** (update this README or add a README in the adapter subfolder)

---

## 🧰 Minimal skeleton (Python)

```python
# api/adapters/external/geocoding.py
from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


class GeocodingPort(Protocol):
    def geocode(self, query: str) -> "GeocodeResult": ...


@dataclass(frozen=True)
class GeocodeResult:
    lat: float
    lon: float
    label: str


class GeocodingAdapter(GeocodingPort):
    def __init__(self, base_url: str, api_key: str, http_client):
        self._base_url = base_url
        self._api_key = api_key
        self._http = http_client

    def geocode(self, query: str) -> GeocodeResult:
        # IO + mapping only ✅
        resp = self._http.get(
            f"{self._base_url}/geocode",
            params={"q": query, "key": self._api_key},
            timeout=10,
        )
        resp.raise_for_status()
        data = resp.json()

        # Explicit mapping ✅
        top = data["results"][0]
        return GeocodeResult(
            lat=float(top["lat"]),
            lon=float(top["lon"]),
            label=str(top.get("label", query)),
        )
```

---

## 📚 Sources & project grounding

- **KFM architecture blueprint (Clean Architecture + adapter layer, examples, and config practices)**  
   [oai_citation:11‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)  [oai_citation:12‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)  
  Key excerpts: adapters live in integration layer and commonly appear under `api/db/` or `api/adapters/` [oai_citation:13‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d); examples include PostGIS/Neo4j/search/external adapters and guidance on interfaces + configuration separation [oai_citation:14‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d); abstraction enables swapping implementations with minimal upper-layer changes [oai_citation:15‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d).

- **Hexagonal (“ports & adapters”) reference framing**  
   [oai_citation:16‡Data Spaces.pdf](sediment://file_0000000053c071f5a9733b1b09cc9f76)  
  Key excerpt: business logic at the center with inbound adapters and outbound controllers/adapters [oai_citation:17‡Data Spaces.pdf](sediment://file_0000000053c071f5a9733b1b09cc9f76).

- **Repo-level context (monorepo + `api/` is backend)**  
   [oai_citation:18‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)  
  The blueprint describes KFM’s monorepo layout including `api/` as the FastAPI backend. [oai_citation:19‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## ✅ Quick PR self-check (before you merge)

- [ ] Adapter implements a service-layer interface (port)
- [ ] No business rules in adapter (only IO + mapping + resilience)
- [ ] Config comes from env/config (no secrets committed)
- [ ] Errors are wrapped into meaningful adapter exceptions
- [ ] Unit tests added (and contract tests if it hits a real service)