# OpenAPI Components 🧩

![OpenAPI](https://img.shields.io/badge/OpenAPI-3.x-informational?logo=openapi-initiative&logoColor=white)
![Swagger](https://img.shields.io/badge/Swagger-Docs-success?logo=swagger&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi&logoColor=white)
![Contract-first](https://img.shields.io/badge/Contract--first-✅-blue)
![GeoJSON](https://img.shields.io/badge/GeoJSON-Geospatial-orange)

Welcome to the **shared component library** for the **KFM REST API** contract ✍️  
This folder contains reusable OpenAPI `components/*` fragments (schemas, parameters, responses, etc.) that get `$ref`’d throughout the API spec.

> [!NOTE]
> In KFM, the API contract is treated as a **first‑class artifact** (contract-first), and **backwards-compatibility matters**. Components are how we keep the contract consistent, readable, and testable.

---

## Why this folder exists 🎯

**Components are our “one place per concept”** rule for the API boundary:

- ✅ **Reuse** across endpoints (avoid copy/pasting request/response shapes)
- ✅ **Consistency** for clients (UI, SDKs, integrations, federation peers)
- ✅ **Stability** so clients aren’t broken by accidental shape drift
- ✅ **Contract testing** becomes realistic when the building blocks are centralized

---

## What belongs here ✅

Put definitions here when they’re **used by 2+ endpoints** or are **core primitives**:

- `DatasetId`, `TimeRange`, `Bbox`, pagination structures
- Geo outputs like `GeoJSONFeatureCollection`, `TileUrlSet`
- Standard error bodies, validation errors, and async-job envelopes
- Shared parameters like `datasetId`, `limit`, `offset`, `bbox`, `time`, `format`
- Security schemes, standard headers, and common response wrappers

---

## What does NOT belong here 🚫

- Endpoint-specific one-off schemas that won’t be reused
- Implementation details (DB tables, internal queue payloads, private logs)
- “Convenience fields” that leak internals (raw stack traces, unredacted PII)

> [!WARNING]
> If a component exposes an internal detail, it becomes a **public promise** once shipped.

---

## Recommended folder layout 🗂️

This repo may evolve, but this is the **intended shape** for maintainability:

```text
api/contracts/openapi/
├─ 📄 openapi.yaml (or openapi.yml)    # 👈 Root spec entrypoint (paths + refs into components/)
└─ 🧩 components/
   ├─ 📄 README.md                     # 👈 you are here 📌 How components are named, referenced, and kept DRY
   ├─ 🧱 schemas/                      # Reusable data models (request/response bodies; domain entities; enums)
   ├─ 🧷 parameters/                   # Reusable params (path/query/header): pagination, bbox, time, filters, ids
   ├─ 📦 requestBodies/                # Reusable request body definitions (content-types + schema refs)
   ├─ 📤 responses/                    # Reusable responses (success envelopes + standard errors)
   ├─ 🧪 examples/                     # Example payloads (small + focused; validated in contract tests)
   ├─ 🪪 headers/                      # Shared headers (e.g., X-Request-Id, traceparent) + documentation
   └─ 🔐 securitySchemes/              # Auth schemes (bearer, apiKey, OAuth2 flows) referenced by operations
```

---

## Conventions 🧭

### 1) One component per file
Keep each file narrowly scoped, and **name it after the component**.

✅ Good:
- `schemas/DatasetId.yaml`
- `schemas/GeoJSONFeatureCollection.yaml`
- `responses/StandardError.yaml`

🚫 Avoid:
- `schemas/misc.yaml`
- `schemas/everything.yaml`

---

### 2) File content rule (important)
Each file should contain **only the component object**, not the wrapper key.

✅ `schemas/DatasetId.yaml`
```yaml
type: string
description: Canonical dataset identifier (stable across releases)
example: kfm.ks.railroads.1850-1900.v1
```

Then in the root spec:
```yaml
components:
  schemas:
    DatasetId:
      $ref: "./components/schemas/DatasetId.yaml"
```

---

### 3) Naming conventions ✨
- **Schemas:** `PascalCase`
- **Parameters/Responses:** `PascalCase` or `camelCase` is acceptable — pick one and stay consistent.
- Suffixes that help:
  - `*Request`, `*Response`
  - `*Error`, `*Problem`
  - `*Filter`, `*Query`
  - `*FeatureCollection`, `*TileSet`

---

### 4) Vendor extensions (KFM-specific) 🧷
When we need KFM-specific semantics that aren’t standard OpenAPI, use:

- `x-kfm-*` (lowercase, hyphenated)

Examples:
- `x-kfm-provenance: required`
- `x-kfm-redaction: "policy:public|restricted"`
- `x-kfm-datasetIdPattern: "kfm.ks.topic.year_range.v#"`

---

## KFM primitives you’ll see a lot 🧱

### Dataset IDs 🆔
KFM dataset naming is expected to follow a pattern like:

`kfm.ks.topic.year_range.v#`

Add/keep a canonical component:
- `schemas/DatasetId.yaml`
- `parameters/DatasetIdPath.yaml` (for `/datasets/{datasetId}`)

**Why:** stable identifiers are the backbone of caching, provenance, and reproducibility.

---

### Geospatial payloads 🗺️
KFM uses open geospatial formats, so we standardize around:
- **GeoJSON** for vector payloads
- **Raster distribution** via tile URLs / COG access patterns (not embedding raw rasters in JSON)

Recommended core schemas:
- `GeoJSONGeometry`
- `GeoJSONFeature`
- `GeoJSONFeatureCollection`
- `TileUrlSet` (array of `{ url, type, format, minZoom, maxZoom }`)

> [!TIP]
> Keep geospatial schemas **lightweight**: geometry + properties + minimal metadata. Heavy metadata belongs in catalogs (STAC/DCAT) and provenance records (PROV).

---

### Provenance + metadata 📜
Because KFM is **evidence-first**, API payloads frequently reference:
- STAC items / collections
- DCAT dataset/distribution info
- PROV lineage records

If the API returns these, create components for:
- `STACItemRef` (a small “pointer” shape)
- `ProvRecordRef`
- `CatalogLinks`

---

## Versioning & backwards compatibility 🧨➡️✅

> [!IMPORTANT]
> **APIs must remain backwards-compatible** unless we explicitly declare a version bump.

### What is usually safe (non-breaking) ✅
- Adding optional fields
- Adding new endpoints
- Adding new enum values **only if clients can tolerate unknown values**
- Adding new components that don’t change existing behavior

### What is usually breaking 🚫
- Renaming/removing fields
- Changing types (`string → object`, `number → string`)
- Tightening constraints that reject previously valid inputs
- Changing required fields
- Removing enum values
- Changing response status codes or semantics

If it’s breaking, do one of these:
- introduce a **new versioned path** (e.g. `/v2/...`)
- or implement **negotiation** (headers/media types) where appropriate

---

## Contract test mindset 🧪
Components are designed to make it easy to enforce:

- **Known inputs → known outputs**
- Schema-valid request & response bodies
- Stable error shapes
- Stable pagination behavior

Recommended checks:
- OpenAPI validation in CI
- Lint rules for `$ref` hygiene
- Snapshot tests for critical response shapes (especially GeoJSON + dataset registries)

---

## Adding a new component (workflow) 🛠️

1) **Decide the component type**
   - Schema? Parameter? Response? RequestBody?

2) **Create the file**
   - `components/<type>/<Name>.yaml`

3) **Reference it**
   - from the root OpenAPI document via `$ref`

4) **Use it**
   - in one or more endpoints

5) **Validate**
   - OpenAPI validates
   - examples (if any) validate

6) **Update tests**
   - if behavior or payloads changed

---

## Quick templates 📎

<details>
<summary><strong>Standard error schema (suggested)</strong> ⚠️</summary>

```yaml
type: object
required: [code, message, requestId]
properties:
  code:
    type: string
    description: Stable, machine-readable error code
    example: "DATASET_NOT_FOUND"
  message:
    type: string
    description: Human-readable error message (safe to display)
  requestId:
    type: string
    description: Correlation ID for tracing
  details:
    type: object
    additionalProperties: true
    description: Optional structured context (no secrets!)
```
</details>

<details>
<summary><strong>Pagination parameters (suggested)</strong> 📄</summary>

```yaml
name: limit
in: query
required: false
schema:
  type: integer
  minimum: 1
  maximum: 1000
  default: 100
description: Max number of items to return.
```
</details>

---

## Review checklist ✅

Before merging changes to components:

- [ ] Do existing clients still work without changes?
- [ ] Are new fields optional (or clearly versioned)?
- [ ] Are examples minimal and valid?
- [ ] Are component names stable and consistent?
- [ ] Are geospatial outputs consistent (GeoJSON for vectors)?
- [ ] Is provenance/metadata linkage preserved (where required)?
- [ ] Does CI validate the OpenAPI spec and contract tests?

---

## Where to look next 👀

- The **root OpenAPI file** one directory up (e.g. `../openapi.yaml`)
- `components/schemas/` for data models 🧱
- `components/parameters/` for reusable path/query params 🧷
- `components/responses/` for reusable response envelopes 📤

---

## Component philosophy in one sentence ✨

**If it’s part of the public API promise, it deserves a reusable component, a stable name, and a compatibility story.**
