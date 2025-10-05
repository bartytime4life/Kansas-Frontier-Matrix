<div align="center">

# 🛠️ Kansas Frontier Matrix — API Route Handlers  
`src/api/routes/README.md`

**FastAPI Endpoints · REST & GraphQL Resolvers · Data Delivery Layer**

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../../.github/workflows/codeql.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../docs/)
[![License: Code](https://img.shields.io/badge/License-MIT-green)](../../../../LICENSE)

</div>

---

## 🎯 Purpose

The **`src/api/routes/`** directory defines all **FastAPI endpoint routes** for the **Kansas Frontier Matrix (KFM)**.  
Each route file contains REST and (optionally) GraphQL endpoint definitions that interface with the **Knowledge Graph**,  
**STAC catalog**, and **AI/NLP enrichment layer** to provide interactive data to the frontend and external clients.

Routes are modularized by data domain (events, places, people, etc.) and follow consistent patterns for  
query parameters, pagination, and metadata enrichment.

---

## 🏗️ System Role

```mermaid
flowchart TD
    A["Frontend (React · MapLibre)"] --> B["FastAPI Routes<br/>/events · /places · /people · /stac · /ask"]
    B --> C["Graph Layer<br/>Neo4j Queries / Cypher / GraphQL"]
    B --> D["STAC Catalog<br/>data/stac/*.json"]
    B --> E["AI Layer<br/>Summarization / Entity Search"]
````

<!-- END OF MERMAID -->

Each route acts as a **controller** between the backend data layers and user-facing clients:

* REST endpoints return **structured JSON** or **GeoJSON**
* GraphQL resolvers allow **flexible, nested queries**
* All routes enforce **schema validation** (Pydantic) and **logging** per MCP protocol

---

## 📂 Directory Layout

```
src/api/routes/
├── __init__.py
├── events.py          # Historical event queries (timeline integration)
├── places.py          # Geographic / geospatial entity routes
├── people.py          # Person and organization endpoints
├── stac.py            # STAC catalog and item retrieval endpoints
├── search.py          # Keyword and semantic search endpoints
├── ai.py              # AI-driven summarization and Q/A interface
└── README.md          # (this file)
```

---

## 🌎 Core Route Modules

### `/events` — Event & Timeline API

**Purpose:** Returns all historical events within a temporal or spatial range.
**Integrations:** Knowledge Graph (Neo4j), OWL-Time, CIDOC CRM.

**Example Usage:**

```bash
GET /events?start=1850&end=1900&type=treaty
```

**Response:**

```json
[
  {
    "id": "event_1857_battle_solomon_fork",
    "title": "Battle of Solomon Fork",
    "start_date": "1857-07-29",
    "end_date": "1857-07-30",
    "places": [{"name": "Solomon River", "lat": 39.36, "lon": -98.92}],
    "participants": ["John Smith", "U.S. Army Cavalry"],
    "summary": "Conflict between U.S. forces and Cheyenne near Solomon River, Kansas."
  }
]
```

---

### `/places` — Geographic & Spatial API

**Purpose:** Retrieves spatial features (forts, towns, rivers, counties, etc.) as GeoJSON.
**Example Usage:**

```bash
GET /places?bbox=-102,36,-94,40
```

**Response:**

```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {"name": "Fort Larned", "category": "Fort"},
      "geometry": {"type": "Point", "coordinates": [-99.13, 38.19]}
    }
  ]
}
```

---

### `/people` — People & Organizations API

**Purpose:** Returns details about individuals, tribal nations, or institutions involved in Kansas history.
**Example Usage:**

```bash
GET /people?id=truman_1870
```

**Response:**

```json
{
  "id": "truman_1870",
  "name": "Harry S. Truman",
  "roles": ["Senator", "President"],
  "associated_places": ["Independence, MO"],
  "events": ["Kansas City Flood 1951"]
}
```

---

### `/stac` — Geospatial Catalog API

**Purpose:** Exposes the **SpatioTemporal Asset Catalog (STAC)** for map layers and imagery.
**Endpoints:**

* `GET /stac/collections` → List all STAC collections
* `GET /stac/items/{id}` → Retrieve a specific dataset’s metadata

**Response Example:**

```json
{
  "stac_version": "1.0.0",
  "id": "ks_1m_dem_2018_2020",
  "type": "Feature",
  "assets": {
    "cog": {
      "href": "https://data.kansas.gov/dem/ks_1m_2018_2020.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized"
    }
  }
}
```

---

### `/search` — Semantic & Keyword Search

**Purpose:** Provides cross-entity search powered by Neo4j full-text index and NLP embedding vectors.

**Example Usage:**

```bash
GET /search?q=cheyenne
```

**Response:**

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

### `/ai` — AI Query & Summarization Endpoint

**Purpose:** Provides AI-assisted question answering and contextual summaries using the project’s NLP models.

**Example:**

```bash
POST /ask
{
  "question": "Which Kansas counties were most affected by the Dust Bowl?"
}
```

**Response:**

```json
{
  "answer": "Western Kansas counties such as Finney, Ford, and Haskell experienced the most severe dust storms between 1933–1938.",
  "sources": [
    "noaa_storms_1933.csv",
    "kansas_newspapers_1935.txt",
    "fema_disasters_dustbowl.json"
  ]
}
```

---

## ⚙️ Implementation Details

Each route module:

* Uses **Pydantic schemas** for response validation
* Logs every query to `logs/api/access.log` with duration and status
* Applies FastAPI dependency injection for database sessions
* Returns consistent metadata headers (API version, timestamp, data license)

**Example Boilerplate:**

```python
from fastapi import APIRouter, Query
from src.api.schemas.event_schema import Event
from src.api.utils.db import get_graph_session

router = APIRouter(prefix="/events", tags=["Events"])

@router.get("/", response_model=list[Event])
def list_events(start: int = 1800, end: int = 2025):
    """Return all historical events within a time range."""
    session = get_graph_session()
    query = f"""
        MATCH (e:Event)
        WHERE e.start_year >= {start} AND e.start_year <= {end}
        RETURN e
    """
    return [dict(record["e"]) for record in session.run(query)]
```

---

## 🧰 Development Commands

```bash
# Run only /events route for testing
uvicorn src.api.routes.events:router --reload

# Validate all endpoints with pytest
pytest tests/api/test_routes.py

# Generate route documentation
curl http://localhost:8080/docs
```

---

## 🔍 Best Practices

✅ **Consistency**
All routes return JSON with predictable structures and `meta` fields for pagination and provenance.

✅ **Documentation-First**
Each route includes a descriptive docstring following **MCP format** (Problem → Method → Output → Provenance).

✅ **Traceability**
Every response includes source identifiers and timestamps (e.g., `data_source`, `last_updated`).

✅ **Security**
Sensitive endpoints (e.g., `/ai`) are rate-limited and protected by optional API keys.

---

## 📚 References

* [Kansas Frontier Matrix – API Layer](../../README.md)
* [AI System Developer Documentation](../../../../docs/ai-system.md)
* [Neo4j Graph Queries](../../../graph/graph_queries.py)
* [STAC 1.0.0 Specification](https://stacspec.org/)
* [FastAPI Documentation](https://fastapi.tiangolo.com/)

---

<div align="center">

**Kansas Frontier Matrix © 2025**
*Open Knowledge · Transparent APIs · Reproducible Science*

</div>

