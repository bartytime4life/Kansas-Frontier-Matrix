<!--
📌 Path: api/src/contracts/schemas/responses/README.md
-->

# 📦 Response Schemas (API Contracts)

![Contract-first](https://img.shields.io/badge/contract--first-✅-blue)
![JSON Schema](https://img.shields.io/badge/json%20schema-draft%202020--12-informational)
![Back-compat](https://img.shields.io/badge/backwards%20compat-required-brightgreen)
![Governance](https://img.shields.io/badge/FAIR%20%2B%20CARE-governed-purple)

> **TL;DR** 🧠  
> This folder defines the **canonical JSON Schema contracts** for all API response payloads.  
> If a response leaves the server, it should **validate against one of these schemas** ✅

---

## 🧭 What lives here?

This directory contains **response schemas** that define exactly what the API returns—success payloads, error payloads, and shared “response building blocks” (meta, pagination, provenance refs, etc.).

**Keep this folder:**
- ✅ Contract-first (schemas drive implementation)
- ✅ Machine-validated (CI + runtime checks)
- ✅ Backwards-compatible (or explicitly versioned)
- ✅ Provenance-aware (traceability as a feature)
- ✅ Governance-aware (classification + redaction are part of the contract)

**Keep this folder free of:**
- 🚫 Database models / ORM entities  
- 🚫 UI-only view models  
- 🚫 Business logic (that belongs in services/use-cases)

---

## 🗂️ Suggested layout

> If the repo already has an established structure, follow it. The below is a recommended baseline for clarity + reuse.

```text
api/src/contracts/schemas/
  responses/
    README.md
    envelopes/
      SuccessEnvelope.schema.json
      ErrorEnvelope.schema.json
      PaginatedEnvelope.schema.json
    components/
      Meta.schema.json
      Pagination.schema.json
      ProvenanceRef.schema.json
      ClassificationRef.schema.json
      RedactionNotice.schema.json
    endpoints/
      GetLayerResponse.schema.json
      ListLayersResponse.schema.json
      GetDatasetResponse.schema.json
```

---

## 🧱 Schema conventions

### ✅ General rules
- Prefer **JSON Schema draft 2020-12**
- Every schema should have:
  - `$schema`
  - `$id` (stable + unique)
  - `title`
  - `description`
  - `type`
  - `additionalProperties: false` (for objects)
  - `examples` (at least one)

### 🏷️ Naming
- Files: `PascalCaseResponse.schema.json` (endpoint responses)  
- Files: `PascalCase.schema.json` (shared components)  
- `$id`: pick a stable namespace strategy (example):
  - `kfm://contracts/responses/ListLayersResponse/v1`

---

## 🧩 Standard response envelopes

> **Rule:** Every endpoint must have a **single success envelope** and a **single error envelope**.  
> No “sometimes it returns X, sometimes Y” surprises.

### ✅ SuccessEnvelope

**Minimum**
- `ok: true`
- `data: <payload>`
- `meta: <Meta>`

**Example**
```json
{
  "ok": true,
  "data": {
    "id": "layer_123",
    "name": "NDVI (Weekly)",
    "kind": "raster"
  },
  "meta": {
    "request_id": "req_01HX3Y1Y6V5Z6YJ4Q0Q8C9D2J1",
    "timestamp": "2026-01-05T00:00:00Z",
    "api_version": "v1",
    "classification": { "level": "public" },
    "provenance": {
      "stac_item": "stac:item:kfm:ndvi:2026-01-01",
      "dcat_dataset": "dcat:dataset:kfm:ndvi",
      "prov_bundle": "prov:bundle:kfm:run:2026-01-05"
    }
  }
}
```

---

### ❌ ErrorEnvelope

**Minimum**
- `ok: false`
- `error: { code, message, details? }`
- `meta: <Meta>`

**Example**
```json
{
  "ok": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Query parameter `bbox` is invalid.",
    "details": {
      "bbox": "Expected 4 numeric values: [minLon, minLat, maxLon, maxLat]."
    }
  },
  "meta": {
    "request_id": "req_01HX3Y1Y6V5Z6YJ4Q0Q8C9D2J1",
    "timestamp": "2026-01-05T00:00:00Z",
    "api_version": "v1",
    "classification": { "level": "public" }
  }
}
```

**Recommended error codes**
- `VALIDATION_ERROR`
- `UNAUTHORIZED`
- `FORBIDDEN`
- `NOT_FOUND`
- `CONFLICT`
- `RATE_LIMITED`
- `INTERNAL_ERROR`
- `UPSTREAM_ERROR`

---

## 🧾 Meta schema

`meta` is where cross-cutting concerns live so every client can:
- debug (request IDs)
- trace (provenance)
- respect governance (classification + redaction)
- handle pagination consistently
- show warnings / notices

**Recommended shape**
```json
{
  "request_id": "string",
  "trace_id": "string (optional)",
  "timestamp": "RFC3339 timestamp",
  "api_version": "string",
  "classification": {
    "level": "public|internal|confidential|restricted",
    "caveats": ["string"]
  },
  "redaction": {
    "applied": true,
    "reason": "string",
    "fields_removed": ["string"]
  },
  "provenance": {
    "stac_item": "string",
    "dcat_dataset": "string",
    "prov_bundle": "string"
  },
  "warnings": ["string"]
}
```

> If an endpoint returns *evidence* or *derived results*, include provenance pointers.  
> If an endpoint returns *sensitive* or *generalized* results, include redaction + classification.

---

## 📚 List + pagination responses

Prefer **cursor pagination** for stability at scale.

**Example**
```json
{
  "ok": true,
  "data": [
    { "id": "layer_001", "name": "Soils (SDA)", "kind": "vector" },
    { "id": "layer_002", "name": "Air Quality (AQI)", "kind": "raster" }
  ],
  "meta": {
    "request_id": "req_01HX3Y1Y6V5Z6YJ4Q0Q8C9D2J1",
    "timestamp": "2026-01-05T00:00:00Z",
    "api_version": "v1"
  },
  "page": {
    "limit": 50,
    "cursor": "eyJvZmZzZXQiOjB9",
    "next_cursor": "eyJvZmZzZXQiOjUwfQ"
  }
}
```

---

## 🔐 Sovereignty, redaction, and “no data leakage”

When responses deal with sensitive data:
- **Never** loosen restrictions downstream (if input is restricted, output can’t become “public”).
- Redaction/generalization must be enforced server-side (UI can *also* defend, but never be the only defense).
- Make redaction visible:
  - `meta.redaction.applied = true`
  - include a `reason` + `fields_removed` (when safe to disclose)

---

## 🔁 Versioning rules

✅ **Non-breaking changes**
- Add a new optional field
- Add a new response schema for a new endpoint
- Add new enum values *only if clients can safely ignore unknown values*
- Extend `oneOf` carefully (avoid introducing ambiguity)

❌ **Breaking changes**
- Rename or remove fields
- Change meaning of a field without a new version
- Tighten validation in a way that rejects previously-valid payloads
- Change envelope semantics

**If it’s breaking:** create a new versioned endpoint (or negotiate versions) and ship a deprecation plan.

---

## ✅ Adding a new response schema

1. **Create schema file**
   - draft 2020-12 recommended
   - stable `$id`
   - `additionalProperties: false`
   - include `examples`

2. **Compose, don’t copy**
   - reuse `Meta`, `Pagination`, `ProvenanceRef`, etc.

3. **Update API contract**
   - OpenAPI/GraphQL must reference the schema used in production

4. **Add contract tests**
   - ✅ valid example fixture
   - ❌ invalid example fixture

5. **Validate in CI**
   - schema syntax validation
   - examples validate against schema
   - server responses validate in integration tests

### 🧪 Definition of Done
- [ ] Schema created with `$id`, `title`, `description`, `examples`
- [ ] Schema uses shared envelopes/components where possible
- [ ] Response validates at runtime (middleware/adapter layer)
- [ ] Contract tests updated with fixtures
- [ ] Back-compat reviewed (or version bump applied)
- [ ] Classification + provenance included where applicable
- [ ] Redaction documented + encoded where applicable

---

## 🚫 Common foot-guns (avoid these)

- Returning different shapes for the same endpoint based on “mode”
- Hand-copying types into the client instead of generating from schemas
- Free-form objects without `additionalProperties: false`
- Hiding redaction *only* in the UI
- Leaking internal IDs / raw DB fields accidentally

---

## 🗺️ Response flow (high level)

```mermaid
flowchart LR
  Client[Client/UI] --> API[API Route / Resolver]
  API --> ValidateIn[Validate Request (Contract)]
  ValidateIn --> UseCase[Domain Use Case]
  UseCase --> MapOut[Map Domain -> Response DTO]
  MapOut --> ValidateOut[Validate Response (Schema)]
  ValidateOut --> Client
```

---

## 🔗 Related docs (in-repo)

- `docs/MASTER_GUIDE_v13.md` (system-wide contract-first + evidence-first rules)
- `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` (adding/changing endpoints)
- `docs/standards/` (STAC/DCAT/PROV profiles, if applicable)

