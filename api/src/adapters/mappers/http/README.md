---
title: "🌐 HTTP Mappers — REST DTOs ↔ Domain (Pydantic • Geo • Errors • Provenance)"
path: "api/src/adapters/mappers/http/README.md"
version: "v0.1.0"
last_updated: "2026-01-11"
status: "draft"
doc_kind: "Module README"
license: "CC-BY-4.0"

# KFM governance header
fair_category: "FAIR+CARE"
care_label: "Public"
sensitivity: "public"
classification: "open"
pipeline_ordering: "ETL → Catalogs → Graph → API → UI → Story Nodes → Focus Mode"
---

![Layer](https://img.shields.io/badge/layer-adapters-informational)
![Module](https://img.shields.io/badge/module-mappers%2Fhttp-7b2cbf)
![Boundary](https://img.shields.io/badge/boundary-REST%20%2F%20HTTP-0ea5e9)
![Contracts](https://img.shields.io/badge/contracts-OpenAPI%20%7C%20Pydantic-22c55e)
![Geo](https://img.shields.io/badge/geo-GeoJSON%20%7C%20MVT%20%7C%20BBox-16a34a)
![Safety](https://img.shields.io/badge/safety-pure%20functions%20%7C%20no%20I%2FO-ef4444)

# 🌐 HTTP Mappers (`api/src/adapters/mappers/http/`)

HTTP mappers translate between:
- 🌐 **REST/HTTP contract shapes** (path/query/body DTOs; OpenAPI/Pydantic)
- 🧠 **Domain commands/queries/results** (service/use-case layer)
- 📚 **Catalog/provenance references** (STAC/DCAT/PROV IDs embedded in responses)
- 🔐 **Classification/redaction metadata** (never downgrade)

> [!IMPORTANT]
> HTTP mappers are the **wire-format firewall**:
> - ✅ parse, validate, normalize, map (pure)
> - ✅ stable error codes
> - ✅ consistent geo/time parsing
> - ❌ no DB/Neo4j/PostGIS calls
> - ❌ no filesystem/network
> - ❌ no auth decisions (routes/services enforce policy)

---

## 🔗 Neighbor links

- 📦 Parent: `📁 api/src/adapters/mappers/README.md`
- 🧰 Shared primitives: `📁 api/src/adapters/mappers/common/README.md`
- 🗺️ Geo helpers: `📁 api/src/adapters/mappers/geo/README.md`
- 📚 Catalog helpers: `📁 api/src/adapters/mappers/catalog/README.md`
- 🛬 Inbound adapters: `📁 api/src/adapters/inbound/README.md`
- 🛫 Outbound adapters: `📁 api/src/adapters/outbound/README.md`
- 🧯 Adapter errors: `📄 api/src/adapters/errors.py`

---

## 📁 Folder map (emoji layout)

```text
📁 api/
  📁 src/
    📁 adapters/
      📁 mappers/
        📁 http/                          🌐 REST DTO ↔ domain mapping (pure)
          📄 README.md                    👈 you are here
          📄 __init__.py                  🧬 package init (optional)

          📄 requests.py                  🧾 request DTOs (Pydantic/dataclasses) + normalization
          📄 responses.py                 📤 response DTO shaping + provenance embedding
          📄 params.py                    🔎 query/path param parsing helpers (pure)
          📄 pagination.py                🔁 limit/offset or cursor mapping helpers
          📄 filters.py                   🎛️ filter mapping (time, bbox, tags, classification)
          📄 errors.py                    🧯 mapper error codes + HTTP mapping (problem details)
          📄 examples.py                  🧪 example payload builders (optional; pure)
```

> [!TIP]
> If you already keep Pydantic models in `api/src/schemas/`, it’s fine.
> The *mapping* logic still belongs here.

---

## 🎯 What belongs here (and what does not)

### ✅ In scope
- Query/path/body normalization (strings, enums, numbers)
- Geo/time parameter parsing (`bbox`, `crs`, time ranges)
- Pagination & sorting mapping (bounded; deterministic)
- Domain → response DTO shaping (including `provenance_ref`)
- Stable error translation metadata (mapper-level)
- “Compatibility shims” for evolving endpoints (v1 to v2 DTO mapping)

### ❌ Out of scope
- FastAPI router code (that’s inbound)
- Business rules / orchestration (services/use-cases)
- Database access (outbound)
- Authorization & policy decisions (inbound/services)
- Caching and retries (services/outbound)

---

## ✅ HTTP mapper rules (KFM-style)

### 1) Contract-first 📜
- DTOs reflect the OpenAPI contract.
- Contract changes require tests + examples + docs updates.

### 2) Explicit validation 🧾
- Reject invalid inputs instead of silently coercing.
- Especially strict for geo/time:
  - bbox ordering
  - coordinate bounds
  - zoom bounds
  - timezone semantics
  - max limits

### 3) Deterministic outputs 🔁
- Same domain result → same response DTO
- Stable ordering for list responses (document the sort)
- Stable precision policies for geometry/time

### 4) Evidence-first outputs 🧾✨
Responses should include:
- catalog references (STAC/DCAT IDs)
- provenance references (PROV activity/entity IDs)
- license/attribution where applicable
- uncertainty summaries for modeled outputs (when present)

### 5) Never downgrade classification 🔐
If any input/result is restricted:
- output classification must be >= (not less restricted)
- redaction notes must propagate
- precision must not increase

---

## 🗺️ Geo & time: the two common footguns 🧨

### Geo rules (use geo mappers)
- Prefer delegating to `mappers/geo` for bbox, CRS, GeoJSON shaping.
- Enforce max bbox area and max result limits (“planet query” defense 🌍🛑).
- Document coordinate order and CRS.

### Time rules (use common time utilities)
- ISO-8601 on the wire.
- Normalize to UTC internally.
- Don’t fabricate precision for historical uncertainty.

> [!TIP]
> Build one shared “filter DTO” for endpoints that commonly accept `bbox`, `time`, `q`, and `classification`.

---

## 🔁 Pagination conventions

Pick one (or support both, carefully):

### Option A: `limit` / `offset`
- simple, familiar
- can be slow at high offsets
- requires stable sort key

### Option B: cursor pagination (recommended for large datasets)
- opaque cursor (base64 json)
- stable sort key and tie-breaker (e.g., `updated_at`, `id`)
- bounded `limit`

> [!IMPORTANT]
> Always enforce `limit <= MAX_LIMIT`. Default to something sane (20–200).  
> Never allow “give me everything”.

---

## 🧯 Error handling (problem details-style)

HTTP mappers should produce safe error objects that inbound adapters can turn into HTTP responses.

### Recommended mapper error codes
- `INVALID_QUERY_PARAM`
- `INVALID_PATH_PARAM`
- `INVALID_BODY`
- `INVALID_BBOX`
- `INVALID_TIME_RANGE`
- `INVALID_ENUM`
- `LIMIT_TOO_LARGE`
- `UNSUPPORTED_FORMAT`
- `CLASSIFICATION_DOWNGRADE_ATTEMPT`

### Suggested “problem details” shape
```json
{
  "type": "https://kfm.dev/problems/invalid_bbox",
  "title": "Invalid bbox",
  "status": 400,
  "detail": "bbox must be 'minx,miny,maxx,maxy' with min<=max and valid bounds",
  "instance": "req_01HXYZ...",
  "fields": {
    "bbox": "invalid ordering"
  }
}
```

> [!TIP]
> Keep the public `detail` message short; logs can contain richer context (sanitized).

---

## 📤 Response shaping patterns (examples)

### “Refs-first” response pattern 🧾
Prefer returning:
- `stac_item_id`, `dcat_dataset_id`, `prov_activity_id`
- `asset_links[]` (safe hrefs)
- `lineage_summary` (small + safe)

Over returning:
- giant raw STAC payloads everywhere
- raw database objects
- nested graph dumps

### Geometry delivery patterns 🗺️
- For sparse layers: return GeoJSON features
- For dense layers: return a tile URL template + metadata
- For rasters: return COG asset links + STAC refs + optional preview PNG links

---

## 🧪 Testing strategy (HTTP mappers)

### ✅ Unit tests
- request DTO normalization + validation
- pagination guards
- error code stability
- response DTO shapes (including provenance fields)

### ✅ Golden fixtures
```text
🧪 tests/
  📁 fixtures/
    📁 http/
      📄 request_layer_query_valid.json
      📄 request_layer_query_invalid_bbox.json
      📄 response_layer_geojson_min.json
      📄 response_layer_tiles_min.json
      📄 response_problem_invalid_bbox.json
```

### ✅ Contract tests (recommended)
- snapshot OpenAPI schema
- ensure examples match DTOs (no drift)

---

## 🧑‍💻 Minimal templates (copy/paste)

### 1) Query DTO (Pydantic) 🧾
```python
# 📄 api/src/adapters/mappers/http/requests.py

from pydantic import BaseModel, Field
from typing import Optional, Literal

class LayerQueryDTO(BaseModel):
    dataset_id: str = Field(min_length=1)
    bbox: Optional[str] = Field(default=None, description="minx,miny,maxx,maxy in EPSG:4326 unless crs provided")
    crs: Literal["EPSG:4326", "EPSG:3857"] = "EPSG:4326"
    format: Literal["geojson", "mvt"] = "geojson"
    limit: int = Field(default=500, ge=1, le=10000)
    offset: int = Field(default=0, ge=0)
```

### 2) Map request DTO → domain query 🔁
```python
# 📄 api/src/adapters/mappers/http/params.py

from dataclasses import dataclass
from typing import Optional, Tuple

@dataclass(frozen=True)
class DomainLayerQuery:
    dataset_id: str
    bbox: Optional[Tuple[float, float, float, float]]
    crs: str
    output_format: str
    limit: int
    offset: int

def to_domain_layer_query(dto) -> DomainLayerQuery:
    dataset_id = dto.dataset_id.strip()
    if not dataset_id:
        raise ValueError("INVALID_BODY")

    bbox_tuple = None
    if dto.bbox:
        parts = [p.strip() for p in dto.bbox.split(",")]
        if len(parts) != 4:
            raise ValueError("INVALID_BBOX")
        bbox_tuple = tuple(map(float, parts))  # (minx, miny, maxx, maxy)

    return DomainLayerQuery(
        dataset_id=dataset_id,
        bbox=bbox_tuple,
        crs=dto.crs,
        output_format=dto.format,
        limit=dto.limit,
        offset=dto.offset,
    )
```

### 3) Domain result → response DTO (refs-first) 📤
```python
# 📄 api/src/adapters/mappers/http/responses.py

from pydantic import BaseModel
from typing import Optional

class DatasetSummaryResponse(BaseModel):
    dataset_id: str
    title: str
    stac_item_id: Optional[str] = None
    dcat_dataset_id: Optional[str] = None
    prov_activity_id: Optional[str] = None
    classification: Optional[str] = None

def to_dataset_summary_response(domain_obj) -> DatasetSummaryResponse:
    return DatasetSummaryResponse(
        dataset_id=domain_obj.dataset_id,
        title=domain_obj.title,
        stac_item_id=getattr(domain_obj.catalog_refs, "stac_item_id", None),
        dcat_dataset_id=getattr(domain_obj.catalog_refs, "dcat_dataset_id", None),
        prov_activity_id=getattr(domain_obj.catalog_refs, "prov_activity_id", None),
        classification=getattr(domain_obj, "classification", None),
    )
```

---

## ✅ Definition of done (HTTP mapper work)

- [ ] Pure mapping (no I/O)
- [ ] DTOs match OpenAPI contract
- [ ] Validation is strict (geo/time/limits)
- [ ] Pagination bounded and deterministic
- [ ] Stable error codes + problem details mapping
- [ ] Evidence-first outputs (STAC/DCAT/PROV refs where applicable)
- [ ] Classification/redaction propagation enforced
- [ ] Unit tests + golden fixtures added
- [ ] Docs/examples updated when contracts change

---

## 📚 Project bookshelf (all project files, mapped to HTTP-mapper needs)

<details>
<summary>📚 Click to expand — how the full project library informs HTTP mapping conventions</summary>

### 🧭 KFM architecture, governance, contracts
- 📄 **Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.docx** → API boundary as governed surface; endpoints for layers, story nodes, analysis
- 📄 **🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx** → interoperability and future endpoint surface direction
- 📄 **MARKDOWN_GUIDE_v13.md.gdoc** → pipeline ordering and contract-first documentation norms
- 📄 **Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx** → doc structure and checklists to avoid drift

### 🗺️ GIS & representation (why bbox/CRS/precision validation is strict)
- 📄 **python-geospatial-analysis-cookbook.pdf**
- 📄 **making-maps-a-visual-guide-to-map-design-for-gis.pdf**
- 📄 **Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf**
- 📄 **compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf**
- 📄 **webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf**
- 📄 **responsive-web-design-with-html5-and-css3.pdf**

### 🛰️ Remote sensing + modeled outputs (why responses should include uncertainty + provenance refs)
- 📄 **Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf**
- 📄 **Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf**
- 📄 **Understanding Statistics & Experimental Design.pdf**
- 📄 **regression-analysis-with-python.pdf**
- 📄 **Regression analysis using Python - slides-linear-regression.pdf**
- 📄 **think-bayes-bayesian-statistics-in-python.pdf**
- 📄 **graphical-data-analysis-with-r.pdf**
- 📄 **Deep Learning for Coders with fastai and PyTorch - Deep.Learning.for.Coders.with.fastai.and.PyTorchpdf**

### 🗄️ Systems & interoperability (why deterministic outputs and stable IDs matter)
- 📄 **PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf**
- 📄 **Scalable Data Management for Future Hardware.pdf**
- 📄 **Data Spaces.pdf**
- 📄 **Spectral Geometry of Graphs.pdf**
- 📄 **Generalized Topology Optimization for Structural Design.pdf**

### 🧠 Human-centered accountability + policy (why contracts must be safe & explainable)
- 📄 **Introduction to Digital Humanism.pdf**
- 📄 **On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf**
- 📄 **Principles of Biological Autonomy - book_9780262381833.pdf**

### 🛡️ Security mindset (why strict validation & safe error messages are required)
- 📄 **ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf**
- 📄 **Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf**

### 🧵 Concurrency / distributed background (why explicit time/idempotency matters)
- 📄 **concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf**

### 🧰 Programming compendium shelf (implementation reference)
- 📄 **A programming Books.pdf**
- 📄 **B-C programming Books.pdf**
- 📄 **D-E programming Books.pdf**
- 📄 **F-H programming Books.pdf**
- 📄 **I-L programming Books.pdf**
- 📄 **M-N programming Books.pdf**
- 📄 **O-R programming Books.pdf**
- 📄 **S-T programming Books.pdf**
- 📄 **U-X programming Books.pdf**

</details>

