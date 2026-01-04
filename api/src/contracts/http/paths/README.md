<!-- According to a document from 2025-12-28, KFM treats OpenAPI + endpoint definitions as *contracts* (contract-first) and requires compatibility + tests when contracts change. -->

# 🌐 HTTP Path Contracts (`api/src/contracts/http/paths/`)

**What is this folder?**  
This is the **contract-first “paths” registry** for our HTTP API: one place where each endpoint’s **method + path + input/output schemas + auth expectations** are declared so the server and clients stay aligned ✅

> [!IMPORTANT]
> Treat these definitions like a public promise: **breaking changes require versioning + clear deprecation** and are protected by **contract tests**. 🧪

---

## 🧭 Table of contents
- [🎯 Purpose](#-purpose)
- [🧱 How this fits the architecture](#-how-this-fits-the-architecture)
- [🔁 Contract-first workflow](#-contract-first-workflow)
- [🗂️ What lives here (and what doesn’t)](#️-what-lives-here-and-what-doesnt)
- [📁 Organization and naming](#-organization-and-naming)
- [🧩 Path contract shape](#-path-contract-shape)
- [🌾 KFM-flavored endpoint examples](#-kfm-flavored-endpoint-examples)
- [🧬 Versioning and compatibility rules](#-versioning-and-compatibility-rules)
- [🧪 Testing expectations](#-testing-expectations)
- [🔐 Security, privacy, and governance](#-security-privacy-and-governance)
- [✅ “Add a new endpoint” checklist](#-add-a-new-endpoint-checklist)
- [🧰 Template: new path contract](#-template-new-path-contract)
- [📎 Related repo docs](#-related-repo-docs)

---

## 🎯 Purpose

The `paths/` folder exists to:

- 🧾 Define **every HTTP endpoint** as a contract (method + route + schemas)
- 📜 Enable **OpenAPI** generation/consistency (or strict alignment with an OpenAPI source-of-truth)
- 🧪 Support **contract tests** (known inputs → known outputs) to prevent drift
- 🤝 Keep UI + integrations stable by enforcing **compatibility discipline**

---

## 🧱 How this fits the architecture

KFM is designed as a **layered system** (clean-architecture style): core domain logic stays isolated from delivery mechanisms like HTTP. This folder is part of that *outer* delivery boundary—**interface definition, not business logic**. 🧱

**Translation:**  
- ✅ “What is the endpoint contract?” → belongs here  
- ❌ “How do we compute NDVI, run simulations, query storage?” → belongs in services/use-cases

---

## 🔁 Contract-first workflow

```mermaid
flowchart LR
  A[🧾 Path contract<br/>paths/...] --> B[📜 OpenAPI<br/>(generated or validated)]
  B --> C[🧩 Server router/controllers]
  B --> D[🧠 Typed client SDK<br/>(optional)]
  A --> E[🧪 Contract tests]
  E --> C
  C --> F[🗃️ Use-cases + data access<br/>(not in contracts)]
```

---

## 🗂️ What lives here (and what doesn’t)

### ✅ Lives here
- 🧾 Path definitions (HTTP **method + path**)
- 🧩 Request shapes:
  - path params
  - query params
  - headers
  - body
- 📦 Response shapes (by status code)
- 🔐 Auth/role requirements (declared, not implemented)
- 🧪 Example payloads + contract-test fixtures hooks (if your contract system supports it)

### ❌ Does *not* live here
- 🧠 Business logic / orchestration
- 🗃️ Database queries / ORM models
- 🧵 Queue logic / background workers
- 🧱 Framework-specific handlers (FastAPI routes, Express routers, etc.)

> [!NOTE]
> If you feel tempted to import a DB client or call a service from a contract file, that’s your signal you’re crossing layers 🚧

---

## 📁 Organization and naming

### 📦 Recommended layout (example)
> Adjust to match the repo’s actual conventions, but keep the spirit: **group by resource** and keep paths discoverable.

```text
api/src/contracts/http/paths/
├── 📁 fields/
│   ├── 📄 get-timeseries.ts
│   └── 📄 ...
├── 📁 map/
│   ├── 📄 get-ndvi-by-date.ts
│   └── 📄 ...
├── 📁 simulation/
│   ├── 📄 post-run.ts
│   └── 📄 ...
├── 📄 index.ts   # exports/registry (if used)
└── 📄 README.md  # this file
```

### 🧠 Naming rules (pragmatic + consistent)
- Use **resource-first grouping** (`fields/`, `map/`, `simulation/`, `data/`, etc.)
- File names should be **verb + intent**:
  - `get-timeseries`, `post-run`, `post-upload`
- If your contract system maps directly to OpenAPI “paths”, prefer aligning file names with route intent rather than internal handler names.

---

## 🧩 Path contract shape

Even if the implementation details differ (TS types, Zod schemas, JSON Schema, OpenAPI YAML fragments), **every path contract should communicate the same minimum set**:

| Field 🧷 | What it means | Required |
|---|---|---|
| `id` | Stable identifier for the endpoint contract | ✅ |
| `method` | HTTP method (`GET`, `POST`, …) | ✅ |
| `path` | Route template (e.g. `/api/fields/{id}/timeseries`) | ✅ |
| `summary` | One-line purpose | ✅ |
| `description` | What it does + semantics | ✅ |
| `auth` | Authn/authz requirement (role/scope) | ✅ |
| `request.params` | Path params schema | when applicable |
| `request.query` | Query params schema | when applicable |
| `request.body` | Request body schema | when applicable |
| `responses[200/...]` | Status → response schema mapping | ✅ |
| `errors` | Known error cases (code, status, shape) | ✅ |
| `examples` | Example requests/responses | strongly recommended |
| `sensitivity` | Data sensitivity / redaction expectations | when applicable |

---

## 🌾 KFM-flavored endpoint examples

These are **representative KFM patterns** you’ll see reflected in contracts. The point is consistency: time series, map layers, and long-running jobs.

### 1) 📈 Field time series (NDVI, etc.)

**Intent:** return a time series for a field (e.g., NDVI).  
**Example route pattern:** `/api/fields/{id}/timeseries?variable=NDVI`

**Contract semantics to capture**
- `id` path param
- `variable` query param (enum)
- response = ordered time series

**Example response shape**
```json
{
  "field_id": "123",
  "variable": "NDVI",
  "unit": "index",
  "series": [
    { "date": "2025-03-01", "value": 0.62 },
    { "date": "2025-03-02", "value": 0.64 }
  ]
}
```

---

### 2) 🗺️ Map layer by date (NDVI map)

**Intent:** serve map-ready NDVI for a date.  
**Example route pattern:** `/api/map/ndvi/{date}`

**Contract semantics to capture**
- `date` param format (ISO date)
- response could be:
  - a **tile URL template**, or
  - simplified vector geometry (GeoJSON-like)

**Example response (tile template style)**
```json
{
  "date": "2025-03-01",
  "kind": "tile-template",
  "template": "/tiles/ndvi/2025-03-01/{z}/{x}/{y}.png",
  "attribution": "KFM"
}
```

---

### 3) 🧪 Start a simulation (long-running job)

**Intent:** kick off a simulation and return a job handle immediately.  
**Example route pattern:** `POST /api/simulation/run`

**Contract semantics to capture**
- request body = scenario parameters
- response = `{ job_id, status_url }` (or similar)
- job status polling endpoint should be defined as its own contract

**Example request body**
```json
{
  "scenario": "irrigation-what-if",
  "field_id": "123",
  "start_date": "2025-03-01",
  "duration_days": 30,
  "parameters": {
    "water_budget_mm": 120
  }
}
```

**Example response**
```json
{
  "job_id": "job_9f2b3c",
  "state": "queued",
  "poll": "/api/jobs/job_9f2b3c"
}
```

---

## 🧬 Versioning and compatibility rules

> [!IMPORTANT]
> **OpenAPI is the contract** (whether it’s generated from code or treated as the source of truth).  
> Breaking the contract requires **versioning** and a **deprecation plan**.

### ✅ Safe changes (usually non-breaking)
- Add **new endpoints**
- Add **new optional fields** to response objects
- Add **new optional query params**
- Add **new status codes** without removing old ones (e.g. introducing `202 Accepted` alongside `200`)

### 🚨 Breaking changes (require version bump or versioned endpoint)
- Remove/rename response fields
- Change field meaning/units without new field name
- Tighten validation (previously accepted input now rejected)
- Change auth requirements in a way that blocks existing clients
- Move endpoint path or change HTTP method

### 🧠 Practical versioning patterns
- **Path versioning:** `/v1/...` → introduce `/v2/...`
- **Parallel endpoints:** keep v1 until sunset date
- **Negotiation:** content-type or header-based (only if we truly need it)

---

## 🧪 Testing expectations

Contracts are only valuable if they’re enforced.

Minimum expectations per endpoint contract:
- 🧪 **Contract tests** covering at least:
  - a “happy path” request → canonical response
  - 1–2 common error cases (validation/auth/not found)
- ✅ Schema validation:
  - request validators (params/query/body)
  - response validators (status schemas)
- 🧾 Example payloads remain synchronized with schemas (no stale docs)

> [!TIP]
> Keep a small “golden fixture” for each endpoint. If a change is intentional, you update the fixture **and** you document the compatibility strategy.

---

## 🔐 Security, privacy, and governance

For each contract, explicitly declare:
- 🔐 **AuthN/AuthZ**: who can call it (role/scope)
- 🧾 **Sensitivity**: does it expose sensitive layers or restricted datasets?
- 🪪 **Audit hooks**: log-worthy events (especially when redaction occurs)

> [!WARNING]
> If the endpoint touches sensitive material, ensure you *also* declare redaction behavior (aggregation/generalization) and emit audit events when data is withheld.

---

## ✅ “Add a new endpoint” checklist

- [ ] 📄 Add a new contract file under the correct resource folder
- [ ] 🧾 Include `summary`, `description`, and stable `id`
- [ ] 🧩 Define schemas for:
  - [ ] path params
  - [ ] query params
  - [ ] headers (if applicable)
  - [ ] body (if applicable)
- [ ] 📦 Define responses for:
  - [ ] success (200/201/202)
  - [ ] validation errors (400/422)
  - [ ] auth errors (401/403)
  - [ ] not found (404) where applicable
- [ ] 🧪 Add/extend contract tests (fixtures + assertions)
- [ ] 🔐 Declare auth + sensitivity
- [ ] 🧬 Confirm compatibility impact (versioning if breaking)
- [ ] 📝 Update any central registry/index if this repo uses one

---

## 🧰 Template: new path contract

> The actual types/helpers will differ depending on our contract stack. This is a **shape template** to keep us consistent.

```ts
// 📄 api/src/contracts/http/paths/<resource>/<verb-intent>.ts

export const Contract__Example = {
  id: "fields.getTimeseries",            // ✅ stable ID
  method: "GET",
  path: "/api/fields/{id}/timeseries",
  summary: "Get field time series",
  description: "Returns a time series (e.g., NDVI) for a given field.",
  tags: ["fields", "timeseries"],

  auth: {
    required: true,
    roles: ["user", "admin"]             // adjust to project auth model
  },

  request: {
    params: {
      id: "string"                       // schema placeholder
    },
    query: {
      variable: ["NDVI", "rainfall"]     // schema placeholder
    }
  },

  responses: {
    200: {
      // response schema placeholder
    },
    401: { /* ... */ },
    403: { /* ... */ },
    404: { /* ... */ }
  },

  errors: [
    { code: "VALIDATION_ERROR", status: 422 },
    { code: "NOT_FOUND", status: 404 }
  ],

  examples: {
    request: { params: { id: "123" }, query: { variable: "NDVI" } },
    response200: { /* ... */ }
  },

  sensitivity: "public"                  // or "restricted" / "sensitive"
} as const;
```

---

## 📎 Related repo docs

If present in the repo, these are the canonical companions to contracts:
- 📄 `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` (for governed extension docs)
- 📄 `docs/architecture/*` (architecture + invariants)
- 📄 `docs/governance/*` (sensitivity, sovereignty, ethics)

---

<!--
📚 Project grounding / sources (do not remove; used for traceability in this repo)

Clean architecture + layered separation:
- :contentReference[oaicite:0]{index=0}

KFM example endpoint patterns (timeseries / map NDVI / simulation job):
- :contentReference[oaicite:1]{index=1}
- :contentReference[oaicite:2]{index=2}
- :contentReference[oaicite:3]{index=3}

FastAPI + OpenAPI auto documentation note:
- :contentReference[oaicite:4]{index=4}

Geospatial serving patterns (GeoTIFF tiles / GeoJSON vectors):
- :contentReference[oaicite:5]{index=5}

Contract-first rules: OpenAPI as contract, versioning, and contract tests/backwards-compat expectations:
- :contentReference[oaicite:6]{index=6}
- :contentReference[oaicite:7]{index=7}
- :contentReference[oaicite:8]{index=8}
- :contentReference[oaicite:9]{index=9}

Audit trails for sensitive/withheld data (governance posture):
- :contentReference[oaicite:10]{index=10}
-->

