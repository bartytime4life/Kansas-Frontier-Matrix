# 📜 KFM API Contracts — CHANGELOG

![Keep a Changelog](https://img.shields.io/badge/Keep%20a%20Changelog-1.1.0-orange)
![SemVer](https://img.shields.io/badge/SemVer-2.0.0-brightgreen)
![OpenAPI](https://img.shields.io/badge/OpenAPI-3.1-blue)
![GraphQL](https://img.shields.io/badge/GraphQL-schema-E10098)
![JSON%20Schema](https://img.shields.io/badge/JSON%20Schema-2020--12-0f62fe)
![Governance](https://img.shields.io/badge/Governance-OPA%20%2B%20Conftest-7b42bc)

> 🧭 **Contract-first + provenance-first.** Any change that alters *wire format*, *validation*, or *guarantees around evidence/citations* must be recorded here.

---

## What this changelog covers 🧩

This file tracks changes to contract artifacts under `api/contracts/`, including:

- 🛣️ **REST**: OpenAPI (request/response shapes, error envelope, pagination, auth hooks)
- 🧬 **GraphQL**: schema types, queries/mutations, deprecations
- 🧾 **JSON Schemas**: shared payloads (metadata profiles, Story Nodes, governance outputs, manifests)
- 📡 **Event payloads** (if present): WebSocket/SSE/pubsub message schemas

✅ **Not tracked here**
- Pure implementation refactors with **no contract change**
- UI-only changes that don’t touch API payloads
- Data refreshes/content updates that don’t alter schemas

---

## Versioning policy 🔢

We follow **Semantic Versioning** for *contracts*:

- **MAJOR** — 🔴 breaking changes (clients must update)
- **MINOR** — 🟢 backwards-compatible additions (new optional fields, new endpoints, new types)
- **PATCH** — 🧹 clarifications, docs, contract-bug fixes that don’t break clients

### Change impact legend 🧭
- 🟢 **BC**: backwards-compatible (safe for existing clients)
- 🟠 **Caution**: may require client updates depending on strictness (e.g., new enum values)
- 🔴 **Breaking**: client updates required

<details>
<summary><strong>🔴 What counts as a breaking change?</strong></summary>

- Removing/renaming an endpoint, field, type, or enum value  
- Changing a field’s type (e.g., `string` → `object`)  
- Tightening validation (e.g., `required`, smaller bounds, stricter regex)  
- Changing semantics (same shape, different meaning)  
- Making an optional field required (unless behind version bump + migration plan)

</details>

---

## [Unreleased] 🚧

> 🧪 Items below are **in design / draft**. Names may change before release.  
> If any draft item becomes required-on-wire, it triggers a **MAJOR** bump.

### Added 🟢
- 🧵 **Pulse Threads** (draft contract surface): threaded updates tied to evidence manifests and provenance, designed to complement Story + Focus workflows.
- 🧠 **Concept Attention Nodes** (draft): machine-readable “why this answer” artifacts (concept graph + evidence links) for explainability in Focus Mode.
- 🤖 **Agent activity contracts** (draft): Watcher → Planner → Executor event envelopes (alerts, deterministic plans, execution reports).
- 📥 **Bulk document ingestion** (draft): upload bundle, extraction job status, extracted entities/links, governance review outputs.
- 🌐 **Federation** (draft): capability discovery + export/import bundle contracts to interoperate across multiple “Frontier Matrix” instances.
- 🧾 **Signed artifact distribution metadata** (draft): schema additions for OCI-based dataset packaging + signature/attestation references.

### Changed 🟠
- 🧾 Focus Mode response envelope (draft): standardize `citations[]`, `provenance[]`, and `governance_flags[]` across REST + GraphQL to make “evidence-first” machine-checkable.
- 🧯 Error envelope (draft): one canonical error shape across REST and GraphQL (consistent `code`, `message`, `details`, `trace_id`).
- 🧊 Geospatial delivery (draft): broaden supported distribution media types for COG/GeoParquet/PMTiles/3D Tiles while keeping discovery consistent through catalog metadata.

### Security 🛡️
- 🔐 Contract-level hooks for **policy evaluation results** and **privacy-aware responses** (e.g., location generalization/redaction explanations, query auditing signals).
- ✅ Supply-chain posture (draft): enforce “signed-only” artifacts where applicable; add contract fields for signature verification status and attestation pointers.

---

## [0.1.0] — 2026-01-24 🎉

### Added 🟢
- 🛣️ **Baseline REST API contract** (OpenAPI) for:
  - dataset discovery & retrieval
  - geospatial tiles / map layers delivery
  - analysis endpoints
  - Story Node creation & retrieval
  - Focus Mode query/answer workflow (contracted as evidence-backed)
- 🧬 **Baseline GraphQL contract** for dataset search + metadata retrieval.
- 🗂️ **Metadata profile contracts** (versioned) supporting catalog + lineage:
  - STAC profile (KFM extensions)
  - DCAT profile (dataset/distribution rules)
  - PROV profile (lineage + activity logging)
- 🧭 **Governance hooks in contracts**:
  - sensitivity/permissions fields
  - policy outcomes for “what can be shown / downloaded”
  - expectations for evidence-backed outputs in AI-assisted surfaces
- 🧩 **UI-decoupling guarantee**: the UI is a first-class API client (contracts are designed to keep UI logic out of backend internals).

### Notes 🗒️ (non-normative examples)
Typical calls a client may rely on:

```text
GET  /api/datasets/{dataset_id}
GET  /api/analysis/ndvi?county={name}&year={yyyy}
POST /api/story
GET  /tiles/{layer}/{z}/{x}/{y}.pbf
```

Example GraphQL query shape:

```graphql
query {
  dataset(id: "landcover_1990") {
    title
    stac_collection_url
  }
}
```

---

## Maintaining this file ✍️

When you change a contract:
- [ ] Update OpenAPI / GraphQL / JSON Schemas
- [ ] Update policy gates / schema tests (and any contract fixtures)
- [ ] Add an entry under **[Unreleased]** with 🟢/🟠/🔴 impact
- [ ] On release: move items into a new version section + add the date ✅
