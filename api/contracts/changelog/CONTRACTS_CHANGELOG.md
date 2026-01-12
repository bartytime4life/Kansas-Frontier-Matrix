---
title: "KFM API Contracts Changelog"
status: "active"
owner: "API Team"
scope: "api/contracts/** (+ contract-shaped schemas that affect API payloads)"
last_updated: "2026-01-12"
---

# 📜 KFM API Contracts Changelog 🧾

![SemVer](https://img.shields.io/badge/SemVer-2.0.0-blue) ![Keep a Changelog](https://img.shields.io/badge/Keep%20a%20Changelog-1.1.0-orange) ![Contract First](https://img.shields.io/badge/Contract--first-required-brightgreen) ![OpenAPI](https://img.shields.io/badge/OpenAPI-source%20of%20truth-informational) ![GraphQL](https://img.shields.io/badge/GraphQL-SDL%20is%20a%20contract-informational)

> [!IMPORTANT]
> This file is the **single source of truth for externally observable API contract changes** (REST/OpenAPI + GraphQL + contract-shaped metadata payloads).
> If a consumer can notice it, it belongs here ✅

---

## 🧭 Scope

### ✅ Tracks changes to
- **REST contract**: OpenAPI/Swagger snapshot exported from FastAPI.
- **GraphQL contract**: GraphQL SDL/schema (types, inputs, queries, mutations).
- **Contract-shaped payload standards** that the API emits/relies on:
  - GeoJSON responses (vector layers)
  - STAC Items/Collections (dataset metadata)
  - DCAT feeds (discovery)
  - PROV(-O) JSON-LD (lineage/provenance)
- **Auth surfaces**: required scopes/roles, token claims, required headers, CORS-facing behavior.
- **Error semantics**: error envelope shape, error codes, status code behavior that clients depend on.
- **Pagination/query semantics**: bbox/time filtering, cursor rules, sorting guarantees, default limits.

### ❌ Does not track
- Internal refactors with identical request/response behavior.
- Pure performance changes that don’t alter outputs, status codes, headers, or semantics.

---

## 🧱 Contract-first rules (non-negotiable)

1. **OpenAPI is the REST contract.** 🧾  
2. **GraphQL SDL is the GraphQL contract.** 🧬  
3. **Breaking changes require versioning or negotiation** (e.g., `/v2/...` pathing, or explicit content negotiation).  
4. **Every contract change must be covered by contract tests** (positive + negative cases). 🧪  
5. **Deprecations must be explicit** (marked as deprecated + include a sunset plan). ⏳

> [!TIP]
> If you changed a schema, response shape, status code, or auth rule — assume it’s a contract change until proven otherwise.

---

## 🌍 Data & format invariants (what clients can safely assume)

These are the “do-not-break” expectations that guide changelog classification:

- **Vector geodata** is served as **GeoJSON** (client-friendly interchange format). 🗺️
- **Raster imagery** is served via **COG-friendly access patterns** (tiles/URLs rather than DB blobs). 🛰️
- **Published datasets** have:
  - a **STAC** JSON record (spatiotemporal metadata),
  - are discoverable via **DCAT** feed(s),
  - and include provenance via **PROV** (ideally PROV-O JSON-LD). 🔗
- **Geospatial compatibility bias**: default to widely supported formats and predictable HTTP/JSON semantics.

---

## ⚖️ Governance & safety gates 🔒

> [!WARNING]
> Any contract change that increases exposure risk **must** trigger governance review.

Examples that require a governance gate:
- A new **public** endpoint or download capability
- Increasing spatial/temporal resolution that could expose sensitive locations
- Changes to **redaction/generalization** behavior
- Reclassification (private → public) or weakening access control
- AI/assistant outputs presented as factual without evidence hooks

Tag such entries with: **`GOV-REVIEW REQUIRED`** ✅

---

## 📦 Contract Artifact Registry (what this changelog covers)

> [!NOTE]
> Paths may evolve; if the repo layout shifts, update this table (the *IDs* should remain stable).

| Contract ID | Artifact | Canonical path (expected) | Owner | Notes |
|---|---|---|---|---|
| `REST_OPENAPI` | OpenAPI (YAML/JSON) | `api/contracts/openapi/openapi.yaml` (or `.json`) | API | Exported snapshot of FastAPI OpenAPI |
| `GRAPHQL_SDL` | GraphQL schema (SDL) | `api/contracts/graphql/schema.graphql` | API | Mirrors KG types (e.g., `Person`, `Place`, `Event`) |
| `ERROR_ENVELOPE` | Error shape | `api/contracts/common/error.schema.json` | API | Must remain stable across endpoints |
| `PAGINATION_ENVELOPE` | Paging/query shape | `api/contracts/common/pagination.schema.json` | API | Cursor/bbox/time filtering rules |
| `STAC_PROFILE` | STAC profile + schemas | `docs/standards/KFM_STAC_PROFILE.md` + `schemas/stac/**` | Standards | Validator-backed metadata contract |
| `DCAT_PROFILE` | DCAT profile + schemas | `docs/standards/KFM_DCAT_PROFILE.md` + `schemas/dcat/**` | Standards | Discovery/distribution links to STAC/data |
| `PROV_PROFILE` | PROV profile + schemas | `docs/standards/KFM_PROV_PROFILE.md` + `schemas/prov/**` | Standards | End-to-end lineage bundles |

---

## 🧩 What counts as a breaking change? 🧨

### REST/OpenAPI breaking examples
- Remove/rename endpoint, path, method
- Change response shape (field removed, type changed, required-ness increased)
- Change status code behavior clients rely on (e.g., `200` → `204`, `404` → `200`)
- Introduce a new required header/query/body field
- Tighten auth requirements without a versioned path (public → auth-required)

### GraphQL breaking examples
- Remove/rename field/type
- Change field type in a non-covariant way (e.g., `String` → `Int`)
- Make an optional argument required
- Remove enum values used by clients

---

## 🔢 Versioning model (SemVer for contract surface)

We version the **contract surface** with SemVer: `MAJOR.MINOR.PATCH`

- **MAJOR**: breaking change (or hard removals after sunset)
- **MINOR**: backwards-compatible additions (new optional fields, new endpoints, additive schema)
- **PATCH**: docs/examples/typos that don’t change runtime behavior

### REST versioning strategy
- Prefer **path versioning** for breaking changes: `/v1/...`, `/v2/...`
- Mark deprecated endpoints in OpenAPI and include sunset guidance

### GraphQL versioning strategy
- Prefer additive evolution + `@deprecated(reason: "...")`
- For truly breaking changes: coordinate a schema version boundary or parallel schema exposure

### Default sunset policy ⏳
Unless explicitly overridden:
- Minimum notice window: **90 days**
- Removal requires:
  - a **MAJOR** bump **or** a versioned replacement path/schema
  - and a documented sunset completion date

---

## ✅ How to update this changelog (PR checklist)

- [ ] Update contract artifact(s): OpenAPI / GraphQL / schemas / examples
- [ ] Add/update **contract tests** (known inputs → expected outputs)
- [ ] Add an entry under **[Unreleased]**
- [ ] If breaking: include migration notes + version bump plan + sunset date
- [ ] If safety-sensitive: tag **GOV-REVIEW REQUIRED** + link the review record

---

## ✍️ Entry template (copy/paste)

<details>
<summary><strong>📦 Click to expand the standard entry template</strong></summary>

```markdown
## [X.Y.Z] — YYYY-MM-DD

### 🧨 Breaking
- ...

### ✨ Added
- ...

### 🔄 Changed
- ...

### 🧹 Deprecated
- ...

### 🗑️ Removed
- ...

### 🐛 Fixed
- ...

### 🔐 Security
- ...

### 🧭 Migration notes
- **Who is impacted:** (web UI, SDKs, external integrators, data partners)
- **How to migrate:** (step-by-step)
- **Sunset date (if any):** YYYY-MM-DD
- **Compatibility strategy:** (new path / negotiation / parallel schema / dual-read)

### 🔗 Artifacts touched
- `api/contracts/openapi/openapi.yaml`
- `api/contracts/graphql/schema.graphql`
- `api/contracts/common/*.schema.json`
- `schemas/**`
```

</details>

---

# 🗓️ Changelog

## [Unreleased] 🚧

### ✨ Added
- _TBD_

### 🔄 Changed
- _TBD_

### 🧹 Deprecated
- _TBD_

### 🗑️ Removed
- _TBD_

### 🐛 Fixed
- _TBD_

### 🔐 Security
- _TBD_

---

## [0.1.0] — 2026-01-12 🎉

### ✨ Added
- Initialized **contract changelog governance** for KFM API surfaces (REST/OpenAPI + GraphQL + contract-shaped schemas).
- Added a **contract artifact registry** (stable IDs + canonical paths) to make contract changes auditable and reviewable.
- Standardized a **SemVer + deprecation/sunset** policy for contract evolution.
- Added a reusable **changelog entry template** (with migration notes + artifacts touched).

### 🔗 Artifacts touched
- `api/contracts/changelog/CONTRACTS_CHANGELOG.md`

---

## 🔗 Internal references (repo links)

- `docs/MASTER_GUIDE_v13.md` — contract-first + versioning expectations 📘
- `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` — proposing/adding endpoints 🧩
- `docs/standards/KFM_STAC_PROFILE.md` — STAC profile for dataset metadata 🗂️
- `docs/standards/KFM_DCAT_PROFILE.md` — DCAT discovery/distribution profile 🧭
- `docs/standards/KFM_PROV_PROFILE.md` — PROV lineage profile 🔗
- `docs/governance/ROOT_GOVERNANCE.md` — governance gates ⚖️
- `docs/governance/SOVEREIGNTY.md` — redaction & sensitive-data constraints 🛡️

---

## 🤝 Federation readiness (forward-looking)

As KFM evolves toward federation (multiple hubs / “other state matrices”), treat public contracts as **shared infrastructure**:
- Prefer open standards (STAC/DCAT/PROV, GeoJSON/COG) 🌐
- Avoid silent breaks; use explicit version boundaries 🔁
- Keep contract IDs stable to support cross-hub tooling 🧷
