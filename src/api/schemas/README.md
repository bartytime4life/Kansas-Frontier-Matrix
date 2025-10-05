<div align="center">

# 🧾 Kansas Frontier Matrix — API Schemas  
`src/api/schemas/README.md`

**Pydantic Models · Data Validation · OpenAPI Compliance**

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../../.github/workflows/codeql.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../docs/)
[![License: Code](https://img.shields.io/badge/License-MIT-green)](../../../../LICENSE)

</div>

---

## 🎯 Purpose

The **`src/api/schemas/`** directory defines all **Pydantic models** used by the  
**FastAPI** and **GraphQL** endpoints of the **Kansas Frontier Matrix (KFM)** API layer.  

Schemas enforce **data structure, type safety, and documentation consistency** across  
API responses and requests — forming the foundation for the system’s **OpenAPI (Swagger)** specification.

Each schema corresponds to a data domain in the **Knowledge Graph** or **STAC Catalog**, ensuring:  
- ✅ Validation of REST and GraphQL responses  
- ✅ Automatic schema generation for `/docs` and `/openapi.json`  
- ✅ Uniform metadata fields across all endpoints  
- ✅ Integration with the **Master Coder Protocol (MCP)** for provenance and reproducibility  

---

## 🧩 Role in the System

```mermaid
flowchart TD
    A["Neo4j Graph / STAC Catalog"] --> B["FastAPI Routes"]
    B --> C["Pydantic Schemas<br/>src/api/schemas/*"]
    C --> D["API Responses<br/>validated JSON / GeoJSON"]
    D --> E["Frontend · Clients · Researchers"]
````

<!-- END OF MERMAID -->

Schemas act as the **contract** between the backend data structures and frontend consumers,
providing clear, versioned data models that define the Kansas Frontier Matrix API.

---

## 📂 Directory Layout

```
src/api/schemas/
├── __init__.py
├── base.py             # Shared base models and metadata definitions
├── event_schema.py     # Event and timeline entities
├── place_schema.py     # Geospatial place / location entities
├── person_schema.py    # People, organizations, and tribal entities
├── stac_schema.py      # SpatioTemporal Asset Catalog (STAC) models
└── README.md           # (this file)
```

---

## 🧱 Common Schema Structure

Each schema inherits from **`BaseSchema`** in `base.py`, which defines global attributes
and provenance fields following the **Master Coder Protocol (MCP)** conventions.

```python
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class BaseSchema(BaseModel):
    id: str = Field(..., description="Unique identifier for the entity.")
    title: Optional[str] = Field(None, description="Readable name or title.")
    description: Optional[str] = Field(None, description="Short summary or context.")
    license: Optional[str] = Field(None, description="Usage license for the data.")
    last_updated: datetime = Field(default_factory=datetime.utcnow)
    source: Optional[str] = Field(None, description="Provenance of the record (dataset, API, etc.).")

    class Config:
        orm_mode = True
```

All derived schemas inherit these fields to guarantee consistent provenance tracking and OpenAPI generation.

---

## 🧭 Example: Event Schema

```python
from typing import List, Optional
from pydantic import BaseModel, Field
from .base import BaseSchema

class PlaceRef(BaseModel):
    name: str
    latitude: float
    longitude: float

class Participant(BaseModel):
    name: str
    role: Optional[str]

class Event(BaseSchema):
    start_date: Optional[str] = Field(None, description="Event start date (ISO 8601).")
    end_date: Optional[str] = Field(None, description="Event end date (ISO 8601).")
    places: List[PlaceRef] = []
    participants: List[Participant] = []
    event_type: Optional[str] = Field(None, description="Category of event (treaty, battle, flood, etc.)")
    summary: Optional[str] = Field(None, description="AI-generated summary or context snippet.")
```

---

## 🌍 Example: Place Schema

```python
from typing import Optional
from pydantic import BaseModel, Field
from .base import BaseSchema

class Place(BaseSchema):
    name: str
    latitude: float
    longitude: float
    county: Optional[str] = None
    category: Optional[str] = Field(None, description="Type of place (fort, town, river, etc.)")
    elevation_m: Optional[float] = None
    gnis_id: Optional[str] = None
```

---

## 👥 Example: Person Schema

```python
from typing import Optional, List
from pydantic import BaseModel
from .base import BaseSchema

class Person(BaseSchema):
    name: str
    birth_date: Optional[str] = None
    death_date: Optional[str] = None
    roles: Optional[List[str]] = []
    affiliations: Optional[List[str]] = []
    tribal_entity: Optional[str] = None
```

---

## 🗺️ Example: STAC Schema (GeoJSON Integration)

Each STAC schema maps to a `Collection` or `Item` entry in the **STAC 1.0.0** specification.

```python
from typing import Dict, Any, Optional
from pydantic import BaseModel, Field

class STACItem(BaseModel):
    id: str
    stac_version: str = "1.0.0"
    type: str = "Feature"
    properties: Dict[str, Any]
    assets: Dict[str, Any]
    bbox: Optional[list] = None
    geometry: Optional[dict] = None
```

---

## 🧾 Schema Validation and OpenAPI

FastAPI automatically validates all responses and request bodies using these schemas.
Every endpoint returning a schema automatically documents itself under `/docs` and `/openapi.json`.

Example auto-generated documentation:

```
GET /events → 200 OK → Response: List[Event]
GET /places/{id} → 200 OK → Response: Place
```

If data fails validation (missing or incorrect field types), FastAPI returns a detailed JSON error response.

---

## 🧰 Testing & Linting

All schemas are unit-tested under `tests/api/test_schemas.py` to ensure structural integrity and correct typing.

```bash
pytest tests/api/test_schemas.py
```

Linting uses **Ruff** and **Black** via pre-commit hooks to enforce code consistency:

```bash
make lint
```

---

## 🧩 Integration Flow

* **Upstream:** Feeds from the **graph layer** (`src/graph/`) and **STAC data** (`data/stac/`)
* **Downstream:** Used by the **FastAPI routes** (`src/api/routes/`) and OpenAPI docs generation
* **Automation:** `make api` or `make test-api` ensures all schemas pass validation before deployment

---

## 📚 References

* [Kansas Frontier Matrix – API Layer](../../README.md)
* [AI System Developer Documentation](../../../../docs/ai-system.md)
* [CIDOC CRM Specification](https://cidoc-crm.org/)
* [STAC 1.0.0 Specification](https://stacspec.org/)
* [FastAPI & Pydantic Docs](https://fastapi.tiangolo.com/tutorial/body/)

---

<div align="center">

**Kansas Frontier Matrix © 2025**
*Data Standards · Provenance Integrity · Reproducible API Design*

</div>

