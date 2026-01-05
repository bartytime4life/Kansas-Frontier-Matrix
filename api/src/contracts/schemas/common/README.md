According to a document from 2025-12-28, this repository is **contract-first**: schemas + API specs are first-class artifacts, and APIs should remain **backwards-compatible** unless a version bump is declared.

# 🧩 Common Schemas (API Contracts)

![Contract-first](https://img.shields.io/badge/contract--first-%E2%9C%85-blue)
![Machine-validated](https://img.shields.io/badge/validation-machine--checked-brightgreen)
![JSON%20Schema](https://img.shields.io/badge/contracts-JSON%20Schema-informational)
![Path](https://img.shields.io/badge/path-api%2Fsrc%2Fcontracts%2Fschemas%2Fcommon-lightgrey)

> [!IMPORTANT]
> This folder is the **shared toolbox** for API contract schemas. Keep it boring, stable, and reusable.  
> If you find duplicated schema shapes elsewhere, consolidate them here to prevent drift 🧭

---

## 📍 Location

`api/src/contracts/schemas/common/`

This directory contains **reusable, cross-endpoint** schema components (building blocks) that are referenced by:
- endpoint request/response schemas (e.g., `api/src/contracts/schemas/<domain>/...`)
- API specs (OpenAPI / GraphQL) when they reference shared shapes

---

## 🧠 What is a “contract artifact”?

A **contract artifact** is a machine-validated schema/spec that defines an interface boundary (examples: JSON Schema, OpenAPI, GraphQL SDL, UI config). In KFM-style architecture, contracts are “real code” — they’re versioned and enforced just like implementations.

---

## ✅ What belongs in `common/`

Think: **generic shapes** that multiple endpoints/domains need.

### Good fits ✅
- 🧾 `error` objects (standard error envelope)
- 📄 pagination (`page`, `pageSize`, `cursor`, `totalCount`)
- 🔎 sorting & filtering primitives
- 🧷 identifier formats (`uuid`, `ulid`, `slug`, etc.)
- 🕒 time primitives (`timestamp`, `dateRange`)
- 🌍 GeoJSON building blocks (Point/Polygon/Feature/FeatureCollection) *if used widely*
- 🧬 provenance / reference pointers (e.g., `datasetId`, `recordId`, `provRef`) *if used widely*
- 📦 response envelopes (`data`, `meta`, `links`, `warnings`)

---

## 🚫 What does **not** belong in `common/`

### Avoid these ❌
- 🧠 domain-specific entities (put those under a domain folder, not `common/`)
- 🎯 endpoint-specific request bodies (belongs with the endpoint contract)
- 🧪 “implementation hints” (DB column names, ORM shapes, internal IDs)
- 🧵 business rules that require code execution (“if X then Y”)  
  *(schemas can validate structure; logic belongs in the application layer)*

---

## 🗂️ Suggested structure

> [!NOTE]
> This is a *recommended* layout. Keep it small. Split only when it improves reuse/readability.

```text
📁 api/
  📁 src/
    📁 contracts/
      📁 schemas/
        📁 common/
          📄 README.md 👈 you are here
          📄 index.md (optional: human index of common schemas)
          📁 primitives/
            📄 id.schema.json
            📄 timestamp.schema.json
          📁 envelopes/
            📄 error.schema.json
            📄 response-envelope.schema.json
          📁 paging/
            📄 pagination.schema.json
          📁 geo/
            📄 geojson-point.schema.json
            📄 geojson-feature.schema.json
```

---

## 🔗 How to reference common schemas

### Option A: JSON Schema `$ref` (recommended for schema-to-schema reuse)

In a domain schema file:

```json
{
  "$id": "schemas/domain/example.schema.json",
  "type": "object",
  "properties": {
    "pagination": {
      "$ref": "../common/paging/pagination.schema.json"
    }
  }
}
```

**Tips**
- Prefer **relative** `$ref` paths inside the repo for portability.
- Keep your `$id` values stable once published (treat them like public API).

---

### Option B: OpenAPI `components.schemas` (when exposing via REST)

If your API spec is OpenAPI-based, you can reference JSON Schemas as components.

```yaml
components:
  schemas:
    Pagination:
      $ref: ./schemas/common/paging/pagination.schema.json
```

> [!TIP]
> If your backend framework generates OpenAPI automatically, treat the resulting spec as a **contract artifact** and keep the shared shapes aligned with these schemas.

---

## 🧱 Schema authoring conventions

### Naming 📛
- Prefer `kebab-case` file names: `response-envelope.schema.json`
- Use a consistent suffix: `*.schema.json`

### Strictness 🔒
- Default to `additionalProperties: false` on objects unless you explicitly need extensibility.
- Keep `required` minimal and intentional.

### Documentation 📝
- Add `title` + `description` (and `examples` if your validator supports them).
- If the schema is reused broadly, include an example snippet in `index.md` or this README.

---

## 🧬 Compatibility & versioning rules

> [!WARNING]
> “Common” schemas are shared dependencies. Small breaking changes here can ripple across the entire API surface.

### Compatibility policy (practical rules)
| Change type | Example | Usually safe without version bump? | Notes |
|---|---|---:|---|
| Add optional field | `meta.traceId` | ✅ | safest change |
| Add new enum value | `status += "archived"` | ⚠️ | can break strict clients |
| Tighten validation | new `pattern`, new `minLength` | ❌ | breaking in practice |
| Rename field | `id` → `recordId` | ❌ | breaking |
| Remove field | delete `warnings` | ❌ | breaking |
| Change meaning | `count` becomes “estimated” | ❌ | breaking even if shape unchanged |

### Deprecation strategy 🧯
If you need to evolve a shared schema:
1. Add a new schema alongside the old (e.g., `pagination.v2.schema.json`)
2. Mark the old one as deprecated in `description`
3. Update API specs + endpoint schemas incrementally
4. Remove only after a major version bump (or explicit policy window)

---

## 🧪 Validation expectations

At minimum, changes to `common/` should trigger:
- ✅ JSON Schema validation (all schemas parse + resolve `$ref`)
- ✅ Contract tests for impacted endpoints (golden inputs/outputs or snapshot tests)
- ✅ API spec validation (OpenAPI/GraphQL) if contracts are referenced there

> [!TIP]
> If there’s no existing validator script yet, add one. “Contracts that aren’t checked” become “suggestions,” not contracts.

---

## 🛠️ How to add a new common schema (checklist)

- [ ] Put it in the smallest meaningful subfolder (`primitives/`, `paging/`, `envelopes/`, etc.)
- [ ] Give it: `title`, `description`, strict object rules
- [ ] Add/confirm `$ref` paths resolve correctly
- [ ] Update any referencing domain schemas
- [ ] Add/update contract tests that cover real endpoint payloads
- [ ] Document it (briefly) in `index.md` or this README

---

## 🔁 When adding a **new endpoint**

> [!IMPORTANT]
> Define the contract **first** (OpenAPI / GraphQL + JSON Schemas), then implement.

Practical flow:
1. Add/extend endpoint schema(s) in `api/src/contracts/schemas/...`
2. Reuse `common/` blocks whenever possible
3. Update the API spec (OpenAPI/GraphQL)
4. Implement endpoint handler + serialization
5. Add contract tests

---

## 📚 Related docs & sources (project context)

- `docs/MASTER_GUIDE_v13.md` — canonical pipeline + contract-first rules  
- `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` — how to propose contract changes  
- KFM Technical Documentation — backend patterns (OpenAPI, FastAPI notes)

---

## 🧭 Ownership

- **Primary owner:** API Contracts maintainers
- **Review required:** Any change to `common/` schemas should be treated as a high-impact change ✅


