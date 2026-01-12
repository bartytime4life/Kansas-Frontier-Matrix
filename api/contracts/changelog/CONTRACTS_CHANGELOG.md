---
title: "KFM API Contracts Changelog"
status: "active"
owner: "API Team"
scope: "api/contracts/** + schemas/** (+ contract-shaped payload standards & telemetry that affect API consumers)"
last_updated: "2026-01-12"
---

# 📜 KFM API Contracts Changelog 🧾

![SemVer](https://img.shields.io/badge/SemVer-2.0.0-blue) ![Keep a Changelog](https://img.shields.io/badge/Keep%20a%20Changelog-1.1.0-orange) ![Contract First](https://img.shields.io/badge/Contract--first-required-brightgreen) ![OpenAPI](https://img.shields.io/badge/OpenAPI-source%20of%20truth-informational) ![GraphQL](https://img.shields.io/badge/GraphQL-SDL%20is%20a%20contract-informational) ![OpenTelemetry](https://img.shields.io/badge/OpenTelemetry-contract--shaped-informational) ![FAIR/CARE](https://img.shields.io/badge/FAIR%2FCARE-governance--gated-blueviolet)

> [!IMPORTANT]
> This file is the **single source of truth for externally observable API contract changes**:
> - REST/OpenAPI + GraphQL SDL
> - Contract-shaped metadata payloads (STAC/DCAT/PROV, GeoJSON/COG access patterns)
> - Contract-shaped telemetry/event payloads that clients/partners/tools rely on  
> If a consumer can notice it, it belongs here ✅

---

## 🧭 Scope

### ✅ Tracks changes to
- **REST contract**: OpenAPI/Swagger snapshot exported from FastAPI.
- **GraphQL contract**: GraphQL SDL/schema (types, inputs, queries, mutations).
- **Contract-shaped payload standards** that the API emits/relies on:
  - GeoJSON responses (vector layers)
  - Raster distribution via **COG-friendly access patterns** (URLs/tiles/ranges, not DB blobs)
  - **STAC** Items/Collections (dataset metadata)
  - **DCAT** feeds (discovery/distribution)
  - **PROV(-O)** JSON/JSON-LD (lineage/provenance bundles)
- **Auth surfaces**: required scopes/roles, token claims, required headers, CORS-facing behavior.
- **Error semantics**: error envelope shape, error codes, status code behavior that clients depend on.
- **Pagination/query semantics**: bbox/time filtering, cursor rules, sorting guarantees, default limits.
- **Telemetry & audit signals (contract-shaped)** used by clients/ops/governance tooling:
  - Event names and minimum required fields (e.g., redaction notice emitted when data withheld)
  - Trace/span correlation fields (so consumers can debug or reconcile audit trails)
  - Sustainability/energy telemetry fields when treated as a required pipeline output

### ❌ Does not track
- Internal refactors with identical request/response behavior.
- Pure performance changes that don’t alter outputs, status codes, headers, or semantics.

> [!NOTE]
> **Story content** (Markdown narratives) is not a contract **unless** it is served via an API surface (REST/GraphQL) using a stable story-node schema. In that case, the story-node schema is tracked here.

---

## 🧱 Contract-first rules (non-negotiable)

1. **OpenAPI is the REST contract.** 🧾  
2. **GraphQL SDL is the GraphQL contract.** 🧬  
3. **Breaking changes require versioning or negotiation** (e.g., `/v2/...` pathing, or explicit content negotiation).  
4. **Every contract change must be covered by contract tests** (positive + negative cases). 🧪  
5. **Deprecations must be explicit** (marked as deprecated + include a sunset plan). ⏳  
6. **Evidence-first boundary**: anything user-visible must remain traceable to catalog/provenance artifacts (STAC/DCAT/PROV) — no silent “magic” outputs. 🔗

> [!TIP]
> If you changed a schema, response shape, status code, auth rule, or “audit-visibility” signal — assume it’s a contract change until proven otherwise.

---

## 🧬 Canonical pipeline invariants (cross-cutting)

These are “system contracts” that shape what the API can promise:

- **Non-negotiable ordering**:
  1) ETL pipelines produce datasets  
  2) **Catalogs** (STAC/DCAT) and **PROV** are generated/updated  
  3) Knowledge graph references those catalog artifacts  
  4) API serves catalog-backed assets  
  5) UI consumes API  
  6) Stories + Focus Mode consume catalogs/graph  
  (No skipping steps; “catalog before narrative” is a hard invariant.) 🔁
- **Graph references catalogs** (does not store bulky payloads): graph nodes should point to STAC/DCAT IDs/DOIs/URIs rather than embedding large assets. 🧷
- **Deterministic pipelines & atomic publish**: a dataset publish is all-or-nothing, and each run emits provenance that can be audited later. 🧾

---

## 🌍 Data & format invariants (what clients can safely assume)

These are the “do-not-break” expectations that guide changelog classification:

- **Vector geodata** is served as **GeoJSON** (client-friendly interchange format). 🗺️  
- **Raster imagery** is served via **COG-friendly access patterns** (tiles/URLs/range-friendly hosting rather than DB blobs). 🛰️  
- **CRS expectation**: API-facing geometries default to **WGS84 / EPSG:4326** for web compatibility; any internal reprojection must be recorded in provenance. 🌐
- **Dataset IDs** follow a stable convention (used across catalogs/keys), e.g.:  
  `kfm.<state|region>.<theme>.<year_range>.v<version>` 🏷️
- **Published datasets** have:
  - a **STAC** JSON record (spatiotemporal metadata),
  - are discoverable via **DCAT** feed(s),
  - and include provenance via **PROV** (ideally PROV-O JSON-LD). 🔗
- **DCAT → STAC/distribution linking**: DCAT distributions must link to STAC entries and/or the underlying data resource so discovery → access remains reliable. 🧭
- **PROV end-to-end**: provenance must link raw inputs → intermediate steps → outputs, including pipeline run IDs/config and (when applicable) commit hashes. 🧬
- **Geospatial compatibility bias**: default to widely supported formats and predictable HTTP/JSON semantics.

---

## ⚖️ Governance & safety gates 🔒

> [!WARNING]
> Any contract change that increases exposure risk **must** trigger governance review.

Examples that require a governance gate:
- A new **public** endpoint or download capability
- Increasing spatial/temporal resolution that could expose sensitive locations
- Changes to **redaction/generalization** behavior (including Focus Mode)
- Reclassification (private → public) or weakening access control
- Changes to **policy gate behavior** (e.g., OPA/Conftest policies) that alter what can be published/served
- Changes to **audit/telemetry signals** used to demonstrate compliance (e.g., redaction notice events)
- AI/assistant outputs presented as factual without evidence hooks

Tag such entries with: **`GOV-REVIEW REQUIRED`** ✅

---

## 📦 Contract Artifact Registry (what this changelog covers)

> [!NOTE]
> Paths may evolve; if the repo layout shifts, update this table (the *IDs* should remain stable).

| Contract ID | Artifact | Canonical path(s) (expected) | Owner | Notes |
|---|---|---|---|---|
| `REST_OPENAPI` | OpenAPI (YAML/JSON) | `api/contracts/openapi/openapi.yaml` (or `.json`) | API | Exported snapshot of FastAPI OpenAPI |
| `GRAPHQL_SDL` | GraphQL schema (SDL) | `api/contracts/graphql/schema.graphql` | API | Mirrors KG types exposed to clients |
| `ERROR_ENVELOPE` | Error shape | `api/contracts/common/error.schema.json` | API | Must remain stable across endpoints |
| `PAGINATION_ENVELOPE` | Paging/query shape | `api/contracts/common/pagination.schema.json` | API | Cursor/bbox/time filtering rules |
| `STAC_PROFILE` | STAC profile + schemas | `docs/standards/KFM_STAC_PROFILE.md` + `schemas/stac/**` | Standards | Validator-backed metadata contract |
| `DCAT_PROFILE` | DCAT profile + schemas | `docs/standards/KFM_DCAT_PROFILE.md` + `schemas/dcat/**` + `api/contracts/schemas/dcat/**` | Standards | DCAT distributions should link to STAC/data resources |
| `PROV_PROFILE` | PROV profile + schemas | `docs/standards/KFM_PROV_PROFILE.md` + `schemas/prov/**` | Standards | End-to-end lineage bundles (raw → derived) |
| `TELEMETRY_SCHEMA` | Telemetry event schemas | `api/contracts/schemas/telemetry/**` + `schemas/telemetry/**` | Platform/API | Contract-shaped events (audit + ops + energy/carbon + correlation fields) |
| `STORY_NODE_SCHEMA` | Story node contract (if served) | `schemas/story_nodes/**` + `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Standards | Only tracked here if story nodes are served via API |
| `FOCUS_CONTEXT_BUNDLE` | Focus Mode context bundle | `schemas/focus/**` | API/UX | Defines the API-delivered “context pack” for Focus Mode |
| `POLICY_PACK` | Governance policy pack (contract-adjacent) | `tools/validation/policy/**` | Governance | OPA/Conftest rules can change publish/serve outcomes → treat as contract-impacting |

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

### Metadata breaking examples (STAC/DCAT/PROV)
- Change dataset ID scheme or meaning (e.g., `kfm.*` convention) 🏷️
- Change STAC Item/Collection required fields or ID rules
- Break DCAT distribution links (discovery no longer reaches STAC/data)
- Remove/rename PROV fields that downstream lineage tooling relies on

### Telemetry breaking examples (contract-shaped events)
- Rename/remove event names used by tooling (e.g., redaction/audit events)
- Remove required correlation fields (trace/span IDs, run IDs, commit SHA)
- Change units/meaning for sustainability metrics (energy/carbon) without versioning
- Stop emitting required “coverage” spans/attributes if those are part of policy/SLO gates

---

## 🔢 Versioning model (SemVer for contract surface)

We version the **contract surface** with SemVer: `MAJOR.MINOR.PATCH`

- **MAJOR**: breaking change (or hard removals after sunset)
- **MINOR**: backwards-compatible additions (new optional fields, new endpoints, additive schema)
- **PATCH**: docs/examples/typos that don’t change runtime behavior

### Dataset-level versioning (related, but distinct)
Dataset updates/reprocessing should publish a new dataset version and link to prior versions via DCAT/PROV (e.g., `prov:wasRevisionOf`). Prefer persistent identifiers (DOI/ARK) when publishing externally. 📌

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
- [ ] If telemetry/policy-gated: update telemetry schema and ensure required spans/events still emit ✅

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
- **Who is impacted:** (web UI, SDKs, external integrators, data partners, governance tooling)
- **How to migrate:** (step-by-step)
- **Sunset date (if any):** YYYY-MM-DD
- **Compatibility strategy:** (new path / negotiation / parallel schema / dual-read)

### 🔗 Artifacts touched
- `api/contracts/openapi/openapi.yaml`
- `api/contracts/graphql/schema.graphql`
- `api/contracts/common/*.schema.json`
- `schemas/**`
- `api/contracts/schemas/**`
- `tools/validation/policy/**` (if policy gate behavior changes)
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

## [0.1.1] — 2026-01-12 🧩

### 🔄 Changed
- Clarified **canonical pipeline invariants** (catalog before narrative; graph references catalogs).
- Expanded “do-not-break” invariants to include **WGS84/EPSG:4326** API bias and **dataset ID** convention.
- Extended the **contract artifact registry** to explicitly include:
  - `api/contracts/schemas/dcat/**`
  - `api/contracts/schemas/telemetry/**`
  - governance policy pack (contract-adjacent, but contract-impacting)

### 🐛 Fixed
- Aligned contract language with v13 directory expectations (IDs stable, paths may evolve).

### 🔗 Artifacts touched
- `api/contracts/changelog/CONTRACTS_CHANGELOG.md`

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
- `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` — universal doc template 🧱
- `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` — proposing/adding endpoints 🧩
- `docs/templates/TEMPLATE__STORY_NODE_V3.md` — story-node schema/template 🧠
- `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` — v13 redesign blueprint 🧭
- `docs/architecture/KFM_NEXT_STAGES_BLUEPRINT.md` — roadmap extensions 🗺️
- `docs/architecture/KFM_VISION_FULL_ARCHITECTURE.md` — full system vision 🏛️
- `docs/standards/KFM_STAC_PROFILE.md` — STAC profile for dataset metadata 🗂️
- `docs/standards/KFM_DCAT_PROFILE.md` — DCAT discovery/distribution profile 🧭
- `docs/standards/KFM_PROV_PROFILE.md` — PROV lineage profile 🔗
- `docs/governance/ROOT_GOVERNANCE.md` — governance gates ⚖️
- `docs/governance/ETHICS.md` — ethical constraints 🧑‍⚖️
- `docs/governance/SOVEREIGNTY.md` — redaction & sensitive-data constraints 🛡️
- `schemas/**` — canonical schema home (STAC/DCAT/PROV/story/focus/telemetry) 📦
- `data/catalog/**` — published catalog outputs (STAC/DCAT) 📚
- `data/prov/**` — published provenance bundles 🧬

---

## 🤝 Federation readiness (forward-looking)

As KFM evolves toward federation (multiple hubs / “other state matrices”), treat public contracts as **shared infrastructure**:
- Prefer open standards (STAC/DCAT/PROV, GeoJSON/COG) 🌐
- Avoid silent breaks; use explicit version boundaries 🔁
- Keep contract IDs stable to support cross-hub tooling 🧷
- Preserve sovereignty rules + auditability as first-class contracts 🔒
