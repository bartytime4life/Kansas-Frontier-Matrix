---
title: "KFM Web — API Endpoints"
path: "web/src/api/endpoints/README.md"
version: "v1.0.0"
last_updated: "2025-12-25"
status: "draft"
doc_kind: "Directory README"
license: "CC-BY-4.0"

markdown_protocol_version: "KFM-MDP v11.2.6"
mcp_version: "MCP-DL v6.3"
ontology_protocol_version: "KFM-ONTO v4.1.0"
pipeline_contract_version: "KFM-PPC v11.0.0"
stac_profile: "KFM-STAC v11.0.0"
dcat_profile: "KFM-DCAT v11.0.0"
prov_profile: "KFM-PROV v11.0.0"

governance_ref: "docs/governance/ROOT_GOVERNANCE.md"
ethics_ref: "docs/governance/ETHICS.md"
sovereignty_policy: "docs/governance/SOVEREIGNTY.md"
fair_category: "FAIR+CARE"
care_label: "TBD"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:web:api:endpoints:readme:v1.0.0"
semantic_document_id: "kfm-web-api-endpoints-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:api:endpoints:readme:v1.0.0"
commit_sha: "<latest-commit-hash>"

ai_transform_permissions:
  - "summarize"
  - "structure_extract"
  - "translate"
  - "keyword_index"
ai_transform_prohibited:
  - "generate_policy"
  - "infer_sensitive_locations"

doc_integrity_checksum: "sha256:<calculate-and-fill>"
---

# Web API Endpoints

> **Purpose (required):** Define how the KFM **web client** (UI) calls **contracted APIs** and how endpoint wrappers in this directory are organized, typed, and reviewed—without violating KFM invariants (no direct graph reads, contract-first, provenance-first).

---

## 📘 Overview

### Purpose

This directory contains the **frontend API endpoint wrappers** used by the web application.  
These wrappers must reflect the **API boundary**: the UI consumes data through the API layer only, and relies on declared contracts (OpenAPI and/or GraphQL) as the source of truth.

### Scope

| In Scope | Out of Scope |
|---|---|
| Frontend endpoint wrapper conventions (request/response typing, naming, grouping, errors) | Backend endpoint implementation (lives under `src/server/`) |
| How UI endpoints map to contract artifacts (OpenAPI/GraphQL) | Authoring or changing API contracts (use `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`) |
| Provenance propagation expectations for UI-visible data | Direct Neo4j access from the UI (explicitly forbidden) |
| Review + CI expectations for endpoint changes | Domain-specific dataset documentation (see `data/<domain>/README.md` and governed domain docs) |

### Audience

- Primary: web/UI contributors working in `web/` (React/MapLibre UI + Focus Mode).
- Secondary: API maintainers and reviewers validating contract alignment and governance posture.

### Definitions

- **Contract artifact:** machine-validated interface definition (e.g., OpenAPI, GraphQL SDL, JSON Schema).
- **Evidence artifact:** catalog + provenance outputs (STAC/DCAT/PROV) consumed downstream.
- **Provenance refs:** identifiers that let the UI trace returned data back to STAC/DCAT/PROV and/or source documents.
- **Focus Mode:** immersive narrative view that must only show provenance-linked content.

Glossary location is **not confirmed in repo**; if present, link it here:
- `docs/glossary.md` (**not confirmed in repo**)

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master guide (pipeline + invariants) | `docs/MASTER_GUIDE_v12.md` | TBD | Canonical ordering + “do not break” rules |
| API Contract Extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | Docs team | Required for any new/changed API surface |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs team | Governs this README structure |
| API contracts (contract-first source) | `src/server/contracts/` | API team | OpenAPI/GraphQL schemas (folder is canonical) |
| Human-readable API docs | `docs/api/` | TBD | **not confirmed in repo** (add if missing) |

### Definition of done (for this document)

- [x] Front-matter complete + `path` matches file location
- [x] Responsibilities and boundaries for `web/src/api/endpoints/` documented
- [x] Contract-first + provenance-first expectations stated (and linked to canonical docs by path)
- [ ] Endpoint inventory section populated with real modules (as they exist in repo)
- [ ] Validation steps listed are mapped to actual repo scripts/workflows (replace placeholders)
- [ ] Maintainer review completed

---

## 🗂️ Directory Layout

### This document

- `path`: `web/src/api/endpoints/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| UI (web app) | `web/` | React/Map UI + Focus Mode |
| Frontend API client code | `web/src/api/` | Web-side API client + endpoint wrappers |
| API boundary (server) | `src/server/` | Contracted access layer (REST/GraphQL), redaction, provenance refs |
| API contracts | `src/server/contracts/` | OpenAPI/GraphQL contract artifacts |
| Documentation | `docs/` | Governed docs, templates, standards |
| Tests | `tests/` | Unit/integration/contract tests |
| Schemas | `schemas/` | JSON Schemas (data, UI registries, telemetry, etc.) |

### Expected file tree for this sub-area

The exact layout under `web/src/api/endpoints/` is **not confirmed in repo**. The intent is:

~~~text
📁 web/src/api/endpoints/
├── 📄 README.md
├── 📄 <resource>.ts              # endpoint wrapper(s) (not confirmed in repo)
├── 📄 <resource>.test.ts         # optional unit tests (not confirmed in repo)
└── 📁 <domain>/                  # optional grouping (not confirmed in repo)
    └── 📄 <resource>.ts
~~~

Guiding rule: keep endpoint wrappers **thin** and **contract-aligned**; do not embed backend semantics here.

---

## 🧭 Context

### Canonical pipeline placement

KFM’s canonical system order is:

**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

This directory is part of the **UI stage** and is only allowed to interact with upstream subsystems through the **API stage**.

### Non-negotiable invariants enforced by design/review

- **No UI direct-to-graph reads.** The web client must never query Neo4j directly or embed graph credentials.
- **Contracts are canonical.** The UI should prefer contract-derived types/clients rather than ad-hoc payload definitions.
- **Provenance is first-class.** Any UI-visible “facts” (especially in Focus Mode) must be traceable back to evidence artifacts.

### Practical implications for endpoint wrappers

- Do not import Neo4j drivers or write Cypher in `web/`.
- Do not hardcode “secret” URLs, tokens, or private endpoints.
- Prefer returning stable IDs + provenance refs over copying large blobs into the UI layer.

---

## 🗺️ Diagrams

### Pipeline orientation

~~~mermaid
flowchart LR
  A["Raw Sources"] --> B["ETL + Normalization"]
  B --> C["STAC Items + Collections"]
  C --> D["DCAT Dataset Views"]
  C --> E["PROV Lineage Bundles"]
  C --> G["Neo4j Graph"]
  G --> H["API Layer"]
  H --> I["Web UI (React · MapLibre · Focus Mode)"]
  I --> J["Story Nodes"]
  J --> K["Focus Mode"]
~~~

### Typical UI endpoint call pattern

~~~mermaid
sequenceDiagram
  participant UI as UI (web/)
  participant API as API (src/server/)
  participant Graph as Graph (Neo4j)

  UI->>API: Request (contracted route/query)
  API->>Graph: Query with redaction + provenance rules
  Graph-->>API: Result + provenance refs
  API-->>UI: Contracted payload (typed)
~~~

---

## 📦 Data & Metadata

### Minimum metadata expectations for UI-visible data

Exact fields depend on the contract, but endpoint wrappers should expect that the API can provide (or evolve toward providing) the following categories:

| Category | Examples (illustrative) | Why it matters |
|---|---|---|
| Stable identifiers | `id`, `entity_id`, `dataset_id` | Enables linking and caching |
| Provenance references | STAC item/collection IDs, DCAT dataset IDs, PROV run/activity IDs | Enables “evidence-first” UI and citation rendering |
| Sensitivity/classification hints | `classification`, `sensitivity`, `redaction_notice` | Prevents accidental leakage in UI |
| Time & geometry (where relevant) | ISO-8601 time fields, generalized geometry | Enables map/timeline; respects privacy |

If the current API payloads do not include these, treat the gaps as contract work (API contract extension + server changes), not as a reason to invent UI-only shadow metadata.

---

## 🌐 STAC, DCAT & PROV Alignment

Endpoint wrappers must preserve the project’s “round-trip traceability” goal:

- **STAC:** whenever returning geospatial or dataset-backed entities, prefer referencing STAC Collection/Item identifiers rather than duplicating dataset metadata.
- **DCAT:** where a response is fundamentally “dataset discovery,” include/retain DCAT dataset identifiers.
- **PROV-O:** for derived/aggregated outputs, preserve `prov:wasGeneratedBy` (run/activity) and `prov:wasDerivedFrom` (inputs), at least as identifiers.

If the API provides explicit provenance fields, the UI should pass them through to components responsible for citation/audit display.

---

## 🧱 Architecture

### Responsibilities of endpoint wrapper modules

Endpoint modules in this folder should:

- Provide a single importable function (or small set of functions) per API surface.
- Centralize request construction (path, query params, headers) and response typing.
- Normalize error handling so UI components are not forced to implement per-endpoint parsing logic.
- Avoid business logic that belongs in the API or domain layer.

### Contract-first alignment rules

- REST contracts (OpenAPI): UI should align to the OpenAPI-defined request/response shapes.
- GraphQL contracts (SDL): UI should align to the schema types and supported queries.

If contract-derived client generation exists, use it. If it does not exist, keep any locally defined types minimal and clearly derived from the contract (do not create competing definitions).

### Example pattern (illustrative)

~~~ts
// NOTE: Illustrative only — adjust to match the actual client utilities used in this repo.

export type ProvenanceRefs = {
  stac_item_ids?: string[];
  stac_collection_ids?: string[];
  dcat_dataset_ids?: string[];
  prov_activity_ids?: string[];
};

export type ApiEnvelope<T> = {
  data: T;
  provenance?: ProvenanceRefs;
  classification?: string;
  redaction_notice?: string;
};

export async function getSomething(id: string): Promise<ApiEnvelope<unknown>> {
  // Use a shared HTTP client if one exists (not confirmed in repo).
  const res = await fetch(`/api/something/${encodeURIComponent(id)}`);
  if (!res.ok) throw new Error(`Request failed: ${res.status}`);
  return res.json();
}
~~~

---

## 🧠 Story Node & Focus Mode Integration

If an endpoint’s payload is rendered in **Focus Mode** (directly or indirectly), it must support:

- **Provenance-linked rendering:** citations/provenance references available for each factual claim or included as structured refs that the UI can resolve.
- **AI-generated content labeling:** if any AI-derived summary/explanation is returned, it must be clearly labeled and should include uncertainty/confidence fields and model/version references (when applicable).
- **Audit affordances:** the UI should be able to show redaction notices and classification hints without guessing.

When adding a new endpoint explicitly intended for Focus Mode, document that endpoint using:
- `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` (REST/GraphQL)  
and ensure backend + tests exist before wiring into the UI.

---

## 🧪 Validation & CI/CD

### Practical validation checklist for changes in this folder

- [ ] Typecheck/build passes for web app
- [ ] Endpoint wrappers do not import forbidden graph access libraries/drivers
- [ ] Endpoint wrappers do not embed secrets, tokens, or private URLs
- [ ] Where applicable, contract alignment is validated (contract tests live outside web/)
- [ ] UI integration tests cover at least one “happy path” and one error path

### Recommended CI gate (policy-aligned idea)

A lightweight CI check can scan `web/` sources/bundles for forbidden graph-access indicators (e.g., `neo4j://`) and fail the build if found. (Exact tooling and forbidden patterns are **not confirmed in repo**.)

---

## ⚖ FAIR+CARE & Governance

- Do not expose sensitive locations by UI behavior (zooming, hover tooltips, deep links) if the API indicates redaction/generalization is required.
- Treat classification/sensitivity hints from the API as authoritative (do not “reconstruct” suppressed detail client-side).
- Do not log or persist sensitive response payloads in analytics/telemetry without an approved schema and governance review.
- Any new endpoint that can expose sensitive sites, Indigenous land context, or restricted data requires governance review per:
  - `docs/governance/ROOT_GOVERNANCE.md`
  - `docs/governance/SOVEREIGNTY.md`
  - `docs/governance/ETHICS.md`

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---:|---|---|
| v1.0.0 | 2025-12-25 | Initial governed README for `web/src/api/endpoints/` | TBD |

---

## Footer refs (do not remove)

- Master guide: `docs/MASTER_GUIDE_v12.md`
- Template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Template: `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Ethics: `docs/governance/ETHICS.md`
---

