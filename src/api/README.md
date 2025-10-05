<div align="center">

# 🔌 Kansas Frontier Matrix — API Layer  
`src/api/README.md`

**FastAPI · GraphQL · Knowledge Graph Access · Timeline & Map Queries**

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../.github/workflows/codeql.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../docs/)
[![License: Code](https://img.shields.io/badge/License-MIT-green)](../../LICENSE)

</div>

---

## 🎯 Purpose

The **`src/api/`** directory implements the **application programming interface (API)** layer of the  
**Kansas Frontier Matrix (KFM)** system.  

This layer provides programmatic access to the **Knowledge Graph**, **SpatioTemporal Asset Catalog (STAC)**,  
and all derived datasets — powering both the **web frontend (React/MapLibre)** and external research tools.  

Built with **FastAPI** and optional **GraphQL** endpoints, the API layer enables users to:  

- Query Kansas historical events, places, and documents by time, location, or type  
- Access STAC metadata for geospatial assets  
- Retrieve AI-generated summaries and contextual “site dossiers”  
- Execute semantic graph queries (Neo4j / Cypher)  
- Serve datasets to the interactive map and timeline  

---

## 🏗️ Role in the System

```mermaid
flowchart TD
    A["Knowledge Graph<br/>Neo4j + CIDOC CRM"]
      --> B["API Layer<br/>FastAPI / GraphQL"]
      --> C["Frontend Web App<br/>React · MapLibreGL"]
      --> D["User Queries<br/>map · timeline · search"]
    B --> E["External Clients<br/>Jupyter · cURL · QGIS"]
    B --> F["STAC Catalog<br/>data/stac/*.json"]
````

<!-- END OF MERMAID -->

The API acts as the **mediator** between data storage and visualization:
it transforms graph and catalog data into consumable JSON/GeoJSON responses,
enabling **fast, contextual, and reproducible** access to Kansas’s historical datasets.

---

## 📂 Directory Layout

```
src/api/
├── __init__.py
├── main.py                # FastAPI app entry point
├── routes/
│   ├── events.py          # /events endpoints
│   ├── places.py          # /places endpoints
│   ├── people.py          # /people endpoints
│   ├── stac.py            # /stac endpoints (STAC catalog access)
│   ├── search.py          # /search?q= endpoints
│   └── ai.py              # /ask AI summarization & Q/A interface
├── schemas/
│   ├── event_schema.py    # Pydantic models for Event responses
│   ├── place_schema.py    # Pydantic models for Place responses
│   └── base.py            # Common data models & validators
├── graphql/
│   └── schema.graphql     # Optional GraphQL schema
├── utils/
│   ├── db.py              # Neo4j connection & query helpers
│   ├── cache.py           # In-memory cache (Redis / local)
│   └── logger.py          # Request & query logging utilities
└── README.md              # (this file)
```

---

## ⚙️ API Overview

### 🚀 FastAPI

The **main FastAPI server** (`main.py`) exposes a RESTful API with JSON and GeoJSON responses.
Each endpoint corresponds to an entity type or functional group within the knowledge graph.

Example server start command:

```bash
uvicorn src.api.main:app --reload --host 0.0.0.0 --port 8080
```

### 🧭 Example REST Endpoints

| Endpoint                      | Description                                         | Response Type     |
| :---------------------------- | :-------------------------------------------------- | :---------------- |
| `/events?start=1850&end=1900` | All Kansas events within time range                 | JSON / GeoJSON    |
| `/places?bbox=-102,36,-94,40` | All places (towns, forts, etc.) in bounding box     | GeoJSON           |
| `/people/{id}`                | Detailed info for a specific historical person      | JSON              |
| `/stac/collections`           | List all geospatial collections                     | STAC JSON         |
| `/stac/items/{id}`            | Get metadata for specific geospatial asset          | STAC Item JSON    |
| `/search?q=railroad`          | Keyword search across graph entities                | JSON              |
| `/ask`                        | AI-assisted query (summarization or contextual Q/A) | JSON + references |

Example request:

```bash
curl http://localhost:8080/events?start=1850&end=1870
```

---

## 🧱 GraphQL API (Optional)

A GraphQL schema (`graphql/schema.graphql`) provides flexible queries for advanced users.

Example query:

```graphql
{
  event(id: "battle_solomon_fork") {
    title
    date
    places { name latitude longitude }
    participants { name role }
  }
}
```

Example response:

```json
{
  "data": {
    "event": {
      "title": "Battle of Solomon Fork",
      "date": "1857-07-29",
      "places": [{"name": "Solomon River", "latitude": 39.36, "longitude": -98.92}],
      "participants": [{"name": "John Smith", "role": "commander"}]
    }
  }
}
```

GraphQL queries are processed using the `graph_queries.py` library from `src/graph/`.

---

## 🧩 Data Schemas (Pydantic)

All REST responses use **Pydantic models** for data validation and type safety.

Example schema (`schemas/event_schema.py`):

```python
from pydantic import BaseModel
from typing import List, Optional

class PlaceRef(BaseModel):
    name: str
    latitude: float
    longitude: float

class Event(BaseModel):
    id: str
    title: str
    start_date: str
    end_date: Optional[str]
    places: List[PlaceRef]
    summary: Optional[str]
```

---

## 🔍 Search and Query Capabilities

The **/search** endpoint integrates full-text and semantic search across multiple sources:

* Neo4j fulltext indexes (events, people, places)
* STAC metadata (titles, descriptions)
* AI embeddings for contextual similarity (optional)

Example:

```bash
curl http://localhost:8080/search?q=cheyenne
```

Response:

```json
{
  "results": [
    {"type": "TribalEntity", "name": "Cheyenne", "mentions": 132},
    {"type": "Event", "title": "Medicine Lodge Treaty (1867)"},
    {"type": "Place", "name": "Cheyenne Bottoms Wetlands"}
  ]
}
```

---

## 🧠 AI Integration Endpoints

The `/ask` endpoint bridges the FastAPI layer with the AI summarization and Q/A modules (`src/nlp/`).

Example:

```bash
curl -X POST http://localhost:8080/ask -H "Content-Type: application/json" \
-d '{"question": "Which Kansas counties were hit hardest by the Dust Bowl?"}'
```

Response:

```json
{
  "answer": "Western Kansas counties such as Finney, Ford, and Haskell saw the most severe dust storms between 1933–1938.",
  "sources": [
    "noaa_storms_1933.csv",
    "kansas_newspapers_1935.txt",
    "fema_disasters_dustbowl.json"
  ]
}
```

---

## 🧾 Logging, Caching & Monitoring

| Component         | Description                                                                               |
| :---------------- | :---------------------------------------------------------------------------------------- |
| **Logging**       | All requests are logged to `logs/api/access.log` with timestamps and execution times.     |
| **Caching**       | Optional in-memory (Redis or local) cache for frequent queries (e.g., STAC lookups).      |
| **Rate Limiting** | FastAPI middleware enforces per-user request caps to prevent abuse.                       |
| **Observability** | Prometheus-compatible metrics endpoint `/metrics` reports uptime, request count, latency. |

Example log:

```
[2025-10-05 14:03:21] GET /events?start=1850&end=1900 | 245ms | 124 results
[2025-10-05 14:04:02] POST /ask | 1.8s | AI query OK
```

---

## 🔁 Integration Flow

* **Upstream:** Receives data from `graph/` (Neo4j) and `data/stac/` (STAC catalogs).
* **Downstream:** Powers the `web/` React frontend, dashboards, and API clients.
* **Automation:** `make api` starts or tests the API; `make test-api` runs validation via CI/CD.

---

## 🧰 Example Development Commands

```bash
# Start local API server
make api

# Run endpoint tests
pytest tests/api/

# Generate OpenAPI documentation
curl http://localhost:8080/docs

# Run GraphQL query interactively
curl -X POST -H "Content-Type: application/json" -d '{"query": "{ allEvents { id title } }"}' http://localhost:8080/graphql
```

---

## 📚 References

* [Kansas Frontier Matrix – AI System Developer Docs](../../docs/ai-system.md)
* [File & Data Architecture Guide](../../docs/architecture.md)
* [Neo4j GraphQL Library](https://neo4j.com/docs/graphql-manual/current/)
* [FastAPI Documentation](https://fastapi.tiangolo.com/)
* [STAC 1.0.0 Specification](https://stacspec.org/)

---

<div align="center">

**Kansas Frontier Matrix © 2025**
*Open Science · Open Data · Interactive History*

</div>
