# KFM API Routes 🧭

![Layer](https://img.shields.io/badge/layer-interface%20%26%20adapters-0b5fff)
![Ingress](https://img.shields.io/badge/trust%20membrane-API%20only-7b2cbf)
![Governance](https://img.shields.io/badge/governance-policy%20%2B%20provenance-1b9aaa)

This folder contains the **HTTP route/endpoint definitions** for the KFM backend API.

In KFM, the API is the *governed* “front door” for the UI and external clients. Routes should be thin,
consistent, and policy-aware.

> [!IMPORTANT]
> **No client (including the UI) should talk to databases directly.** All access must be mediated by the API.
> This is part of the project’s “trust membrane” and governance enforcement.

---

## What belongs in `src/api/routes/`

Routes are responsible for:

- **Defining public API surface area** (paths, methods, status codes, response models).
- **Parsing & validating input** (path/query params, request bodies).
- **Authentication & authorization hooks** (who is calling, what they’re allowed to see/do).
- **Calling the service/use-case layer** (business workflows).
- **Translating domain/service results into HTTP responses** (including consistent error shapes).
- **Light post-processing** (headers, small response shaping) — *no heavy compute*.

Routes are *not* responsible for:

- Complex business logic (belongs in **services/use-cases**).
- Direct database access (belongs in **repositories/adapters**).
- ETL/pipeline work (belongs in **pipelines**).
- Long-running computations (belongs in background workers/jobs).

---

## Route module conventions

### File naming

| Convention | Example | Notes |
|---|---|---|
| one router per domain/resource | `datasets.py`, `stories.py` | Prefer “noun” modules |
| auxiliary routers for cross-cutting concerns | `health.py`, `auth.py`, `admin.py` | Keep these small |
| versioned APIs (if used) | `v1/datasets.py` | Prefer additive evolution |

> [!NOTE]
> The exact list of routers will evolve. Keep the naming consistent so it’s easy to locate an endpoint.

### Router shape

- Each module exports a `router` object.
- Each router declares:
  - a `prefix` (e.g., `/datasets`)
  - `tags` for OpenAPI grouping
- All request/response types are explicit (Pydantic models or equivalents).

---

## Governance & provenance rules (routes are enforcement points)

Routes are where we can centralize “uniform rules” so they aren’t scattered across UI or storage access.

**At minimum, every route should consider:**

- **Policy checks:** verify caller’s access before returning governed/sensitive data.
- **Provenance logging:** record key request metadata for auditability (who/what/when + dataset/story IDs).
- **Redaction/generalization:** avoid returning precise locations or culturally restricted details unless policy allows.
- **Reproducibility hooks:** include stable identifiers (dataset version IDs, story node IDs, run IDs) in responses.

> [!WARNING]
> If an endpoint could expose sensitive locations or community-restricted knowledge, **default to generalizing**
> (e.g., county-level instead of parcel-level) and flag for governance review.

---

## Request flow overview

```mermaid
flowchart LR
  Client[Client / UI] -->|HTTP| Routes[src/api/routes/*]
  Routes -->|validate + authz| Policy[Policy / Governance]
  Routes -->|call| Services[Service / Use-Case Layer]
  Services -->|via interfaces| Repos[Repository Interfaces]
  Repos --> Adapters[DB / Search / External Adapters]
  Adapters --> Storage[(PostGIS / Neo4j / Object Store)]
  Routes -->|emit| Prov[Provenance / Audit Logs]
````

---

## Example: minimal router template (FastAPI-style)

```py
from fastapi import APIRouter, Depends, HTTPException, status

# from ..dependencies import get_current_user
# from ..services.datasets import DatasetService
# from ..schemas.datasets import DatasetOut

router = APIRouter(prefix="/datasets", tags=["datasets"])

@router.get("/{dataset_id}")  # response_model=DatasetOut
def get_dataset(
    dataset_id: str,
    # user=Depends(get_current_user),
    # svc: DatasetService = Depends(),
):
    # 1) Policy check (pseudo)
    # policy.check_access(user, dataset_id)

    # 2) Call service/use-case layer
    # dataset = svc.get_dataset(dataset_id)

    # 3) Translate to HTTP response
    # if not dataset:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Dataset not found")
    # return dataset
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Example stub")
```

> [!TIP]
> Keep endpoints “boring”: validate → authorize → call service → translate → return.

---

## Adding a new route (Definition of Done ✅)

* [ ] Endpoint has a clear **owner domain** (dataset, story, search, etc.).
* [ ] Request/response schemas are defined and used consistently.
* [ ] No direct DB calls from the route layer.
* [ ] Policy checks are applied (or explicitly documented as not required).
* [ ] Provenance/audit logging is present where relevant.
* [ ] Contract expectations are captured (OpenAPI/GraphQL schema updated if applicable).
* [ ] Tests:

  * [ ] unit tests for service logic
  * [ ] route-level tests for status codes + error shapes
  * [ ] contract/regression test for breaking changes
* [ ] Docs updated:

  * [ ] route list / examples updated (this README or higher-level API docs)

---

## Common pitfalls 🚫

<details>
  <summary><strong>Click to expand</strong></summary>

* **Leaking business logic into routes** → makes it hard to test and reuse.
* **Skipping policy checks “just for now”** → almost always becomes a data leak later.
* **Returning storage-shaped objects** (raw ORM rows, graph records) → breaks API stability.
* **Inconsistent error responses** → makes UI and client SDKs harder to maintain.
* **Doing heavy compute in request handlers** → causes latency + timeouts; use async jobs instead.

</details>

---

## Where to look next

* `src/api/main.py` or equivalent: app bootstrap + router registration (if present)
* `src/api/schemas/`: request/response models (if present)
* `src/services/` (or similar): business workflows / use cases (if present)
* `src/infra/` (or similar): adapters for PostGIS / Neo4j / search / external APIs (if present)

```
```
