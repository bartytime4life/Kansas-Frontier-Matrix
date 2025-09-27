# `graph/api/` — Knowledge Graph API Layer

This folder provides the **API surface** for interacting with the Kansas Geo Timeline
knowledge graph.  
It abstracts the underlying `graph/` models and builders into **queryable services**,
making the graph accessible to:

- **Python code** (internal modules, notebooks, scripts)
- **Web apps** (MapLibre viewer, timeline components)
- **External clients** (via JSON/HTTP endpoints if wrapped in FastAPI/Flask)

---

## Design Goals

- **Unified Access**: Single API to fetch nodes, edges, subgraphs, and metrics.
- **Temporal-Spatial Aware**: Query by time ranges, bounding boxes, or both.
- **Entity-Centric**: Lookup by canonical ID (e.g., `kfm:fort:larned`) or aliases.
- **Extensible**: Easy to add new query methods or export formats.
- **Web-Ready**: Functions return JSON-serializable dicts for UI layers.

---

## Directory Layout

```

src/kansas_geo_timeline/graph/api/
├── **init**.py
├── service.py       # Core API service class wrapping graph queries
├── routes.py        # (optional) FastAPI/Flask routes exposing API endpoints
├── schema.py        # Response models for validation/serialization
└── README.md        # This file

````

---

## Example API Usage

### Python Service

```python
from kansas_geo_timeline.graph.api.service import GraphAPI

api = GraphAPI("data/processed/graph/master_graph.json")

# Get a node by ID
fort = api.get_node("kfm:fort:larned")

# Find all trails active between 1820 and 1850
trails = api.query_nodes(type="Trail", time_range=("1820-01-01", "1850-12-31"))

# Get neighbors of a node
links = api.get_neighbors("kfm:river:kansas")
````

### Web Route (if routes.py implemented)

```python
# Example FastAPI usage
from fastapi import FastAPI
from kansas_geo_timeline.graph.api.routes import router

app = FastAPI(title="Kansas Geo Timeline Graph API")
app.include_router(router, prefix="/graph")
```

---

## Planned Endpoints (HTTP/JSON)

* `GET /graph/node/{id}` → node details
* `GET /graph/node/{id}/neighbors` → connected edges/nodes
* `GET /graph/query` → query by type, time range, bbox
* `GET /graph/stats` → basic graph metrics (node/edge counts, degree distribution)

---

## Dependencies

* [`networkx`](https://networkx.org/) — graph backbone
* [`pydantic`](https://docs.pydantic.dev/) — schema validation for API responses
* [`fastapi`](https://fastapi.tiangolo.com/) — (optional) web service layer
* [`uvicorn`](https://www.uvicorn.org/) — (optional) ASGI server

---

## Notes

* **Graph files** are read from `data/processed/graph/*.json` (produced by `graph/builder.py`).
* This API layer should remain **stateless** — all persistence is handled by the graph builder.
* Keep endpoints **read-only** to ensure provenance integrity (no ad-hoc mutations).

---

✅ **Mission-grade principle**: The API layer is the **bridge** between the historical
knowledge graph and all user interfaces — ensuring consistent, reproducible access
to Kansas history across tools.

```
