---
title: "Web UI — API Client (web/src/api) README"
path: "web/src/api/README.md"
version: "v1.0.0"
last_updated: "2025-12-25"
status: "draft"
doc_kind: "README"
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

doc_uuid: "urn:kfm:doc:web:api-client-readme:v1.0.0"
semantic_document_id: "kfm-web-api-client-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:api-client-readme:v1.0.0"
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

# Web UI — API Client (`web/src/api`)

This folder is the **canonical home for web UI API consumption code**: request helpers, endpoint wrappers, client-side response typing/validation, and policy-aligned handling of provenance/citations.

It exists to prevent:
- ad-hoc `fetch()` scattered across components,
- accidental drift from server contracts,
- and violations of the KFM invariant: **UI → API only** (no direct graph access).

---

## 📘 Overview

### Purpose

- Provide a **single, consistent** place for the React/map UI to call KFM backend services.
- Enforce KFM architectural constraints at the UI boundary:
  - **UI never reads Neo4j directly**; all graph access is through contracted APIs.
  - **Provenance-first**: the UI should render citations and provenance references that come from the API; it must not invent or “guess” sources.
- Make it easy to add/upgrade endpoints while remaining contract-first:
  - contract update (server) → client wrapper update (here) → UI feature update.

### Scope

| In Scope | Out of Scope |
|---|---|
| API client utilities (base URL, headers, auth token wiring, timeouts, retries) | Server API implementation (belongs in `src/server/`) |
| Endpoint wrapper functions / hooks used by UI | Neo4j drivers, Cypher queries, or graph access from web code |
| Client-side typing and (optional) runtime validation for API payloads | Editing or defining API contracts (belongs in `src/server/contracts/`) |
| Guidance for Focus Mode / Story Node retrieval & rendering rules | Authoring Story Nodes (belongs in `docs/reports/story_nodes/`) |

### Audience

- UI maintainers and contributors working under `web/`
- API maintainers coordinating contract changes
- Reviewers enforcing governance/ethics/sovereignty requirements

### Definitions

- Glossary: `docs/glossary.md` *(not confirmed in repo — add or repair link if the glossary lives elsewhere)*
- Terms used here:
  - **API boundary**: the contracted interface surface (REST/GraphQL) exposed from `src/server/`.
  - **Contract artifact**: OpenAPI / GraphQL schema files (and related schemas) that must validate in CI.
  - **Context bundle**: an API response shaped for Focus Mode (entity + related entities + narrative + sources/provenance references).
  - **Provenance-linked**: all factual elements in narratives trace to a source ID (STAC/DCAT/PROV or other governed source identifiers).

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide v12 (draft) | `docs/MASTER_GUIDE_v12.md` | KFM Core | Canonical pipeline + invariants |
| v13 redesign blueprint (draft; if adopted) | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Arch | Canonical roots + “UI→API only” enforcement |
| API contracts | `src/server/contracts/**` | API maintainers | Contract-first boundary |
| API Contract Extension Template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | API maintainers | Used when contract changes |
| Story Node Template v3 | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Curators | Narrative + citation rules |
| Universal Doc Template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs | Govered Markdown structure |

### Definition of done (for this document)

- [ ] Front-matter complete + valid, and `path:` matches file location
- [ ] Directory responsibilities and placement rules documented (no UI→graph bypass)
- [ ] Example patterns documented without claiming unverified in-repo tooling
- [ ] Validation expectations are listed (contract + schema + lint)
- [ ] Governance + CARE/sovereignty considerations explicitly stated

---

## 🗂 Directory Layout

### This document

- `path`: `web/src/api/README.md` (must match front-matter)

### Related repository paths (orientation)

| Area | Path | What lives here |
|---|---|---|
| UI root | `web/` | React/map UI; consumes APIs only |
| UI API client (this area) | `web/src/api/` | API wrappers + typing/validation + client utilities |
| API boundary (server) | `src/server/` | REST/GraphQL implementation; redaction + policy enforcement |
| API contracts | `src/server/contracts/**` | OpenAPI/GraphQL + versioning; contract tests required |
| Graph subsystem | `src/graph/` | Ontology bindings + ingest/build tooling |
| Catalog outputs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | Evidence + provenance artifacts |
| Story Nodes | `docs/reports/story_nodes/` | Draft/published narrative artifacts + assets |
| Schemas | `schemas/` | JSON Schemas (STAC/DCAT/PROV/UI/telemetry) |

### Expected file tree for this sub-area

> Note: The specific filenames below are **illustrative** unless they already exist in-repo. If a file/path doesn’t exist, treat it as **not confirmed in repo** and either (a) create it intentionally, or (b) adjust this README to match actual structure.

~~~text
📁 web/
└── 📁 src/
    └── 📁 api/
        ├── 📄 README.md
        ├── 📁 client/                    # (not confirmed in repo) shared HTTP, auth, retries, error mapping
        ├── 📁 endpoints/                 # (not confirmed in repo) feature/domain endpoint wrappers
        ├── 📁 types/                     # (not confirmed in repo) TS types + optional runtime validators
        ├── 📁 __tests__/                 # (not confirmed in repo) client contract tests + mocked responses
        └── 📄 index.ts                   # (not confirmed in repo) public surface exports
~~~

---

## 🧭 Context

### Background

KFM’s architecture is **pipeline-ordered** and **boundary-governed**:

**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

The web UI is intentionally **not** the system-of-record for data semantics or provenance; it renders what the API delivers, and it must do so in a way that preserves contract + provenance guarantees.

### Assumptions

- The UI is a React-based web app with a map engine (e.g., MapLibre/Cesium is referenced in design docs; exact setup is repo-defined).
- The server API exposes contract-validated endpoints (REST and/or GraphQL).
- Focus Mode expects provenance-linked narrative artifacts (Story Nodes) and related evidence pointers.

### Constraints and invariants

Non-negotiables:

1. **No UI direct-to-graph reads**
   - `web/` code must never query Neo4j directly.
   - The UI must not import Neo4j drivers or run Cypher.
   - All graph access must go through the API boundary in `src/server/`.

2. **Contracts are canonical**
   - Client wrappers should be derived from / aligned to the server contracts in `src/server/contracts/**`.
   - Do not “silently” change response shapes in UI code.

3. **Focus Mode is provenance-only**
   - UI must not display unsourced narrative.
   - Citations/provenance must render from API-delivered sources.

4. **Governance is enforced at boundaries**
   - Assume the API applies redaction and access controls.
   - The UI must avoid logging/exposing sensitive content (including URLs/tokens, restricted coordinates) and must not attempt to reconstruct redacted data.

### Open questions (keep updated)

| Question | Owner | Target |
|---|---|---|
| Are API client types generated from OpenAPI/GraphQL (codegen), or authored manually? | UI/API | TBD |
| Is there a standard response “envelope” (e.g., `{ data, sources, provenance }`)? | API | TBD |
| What caching library is canonical (if any) for API calls (React Query/SWR/custom)? | UI | TBD |

### Future extensions

- Codegen pipeline for client types from `src/server/contracts/**`
- “Contract drift” CI check that compares client expectations to contract snapshots
- Offline-first caching for map layers (careful: must respect governance)

---

## 🗺️ Diagrams

### Where `web/src/api` sits in the canonical pipeline

~~~mermaid
flowchart LR
  A["UI components<br/>web/src/**"] --> B["API client wrappers<br/>web/src/api/**"]
  B --> C["API boundary<br/>src/server/**<br/>(contracted)"]
  C --> D["Graph services<br/>src/graph/**"]
  C --> E["Catalog evidence<br/>data/stac + data/catalog/dcat + data/prov"]
  C --> F["Story Nodes<br/>docs/reports/story_nodes/** or graph-backed"]
~~~

### Typical Focus Mode request sequence

~~~mermaid
sequenceDiagram
  participant UI as UI Component (web/)
  participant APIClient as API Client (web/src/api)
  participant Server as API Boundary (src/server)
  participant Graph as Graph Services (Neo4j via src/graph)
  participant Catalog as STAC/DCAT/PROV Evidence

  UI->>APIClient: loadFocus(entityId)
  APIClient->>Server: GET /focus?entityId=...
  Server->>Graph: fetch entity + related subgraph
  Server->>Catalog: attach evidence refs (STAC/DCAT/PROV IDs)
  Server-->>APIClient: context bundle (narrative + citations + refs)
  APIClient-->>UI: typed response (render-ready)
~~~

---

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode

- Focus Mode typically requires:
  - the focused entity (Place/Person/Event/Artifact),
  - related entities for context,
  - a Story Node narrative (stored/retrieved, not invented at render-time),
  - and a `sources[]`/provenance reference list that citations map to.

### UI-side enforcement checklist (client responsibilities)

Even when the server enforces provenance rules, the UI should still guard against accidental regression:

- [ ] Do not render narrative blocks if citations/sources references are missing or invalid.
- [ ] Render citations in a consistent, inspectable way (source IDs and links).
- [ ] If AI-assisted content is ever delivered (opt-in), clearly label it and keep it visually distinct from curated narrative.
- [ ] Never fabricate citations or merge “similar” sources client-side.
- [ ] Treat redacted values as final (do not attempt inference or reconstruction).

---

## 🧪 Validation & CI/CD

### Minimum CI gates (relevant to this area)

At minimum, changes touching API usage should remain compatible with expected repository gates:

- Markdown protocol validation (for docs)
- API contract tests (server side; client should track shape/version)
- UI schema checks (e.g., layer registry, if applicable)
- Security + sovereignty scanning (where applicable)

### Suggested local validation (examples only)

> Commands below are examples only (actual scripts are **not confirmed in repo**). Replace with repo-specific commands once known.

~~~bash
# Example: run UI typecheck / unit tests
# npm test
# npm run typecheck

# Example: run lint
# npm run lint
~~~

### Testing strategy (recommended)

- **Unit tests** for:
  - request builder (URL + query params),
  - error mapping,
  - runtime validation (if used).
- **Mocked integration tests** for:
  - endpoint wrappers returning expected typed objects,
  - failure scenarios (401/403, redaction responses, schema mismatch).
- **Contract drift detection** (ideal):
  - compare client expectations against `src/server/contracts/**` snapshots (implementation approach TBD).

---

## 📦 Data & Metadata

### What this folder should preserve

This folder is not just “HTTP glue.” It is where the UI should:
- preserve **stable IDs** from upstream (graph IDs, dataset IDs),
- preserve **provenance pointers** (STAC/DCAT/PROV identifiers, source references),
- preserve **policy state** (redacted flags, audit hints if provided by API),
- and preserve **version semantics** (API versioning if present).

### Example: “context bundle” response shape (illustrative)

> The exact response envelope is API-defined. The pattern below reflects common KFM guidance: the UI receives narrative plus a `sources` array that citations map to.

~~~json
{
  "entity": { "id": "place:ks:example", "label": "Example Place" },
  "storyNode": {
    "id": "story:example",
    "title": "Example Narrative",
    "body": [
      { "text": "A sourced claim.", "citations": ["source:stac:item:123"] }
    ]
  },
  "relatedEntities": [
    { "id": "event:example", "label": "Example Event" }
  ],
  "sources": [
    {
      "id": "source:stac:item:123",
      "kind": "stac-item",
      "ref": "data/stac/items/... (or external URL)",
      "license": "CC-BY-4.0"
    }
  ]
}
~~~

### Sensitivity & redaction (UI handling)

- Do not log raw API responses containing sensitive details.
- Never store sensitive payloads in long-lived client storage unless explicitly allowed by governance.
- If coordinates are generalized/redacted, treat them as canonical for UI rendering.
- Do not “guess” missing locations or fill in gaps with heuristics.

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- The UI may receive STAC Item/Collection identifiers or asset references.
- Client wrappers must preserve those IDs as-is (do not rewrite or “normalize” IDs unless required by contract).

### DCAT

- The UI may receive dataset-level descriptors/IDs for discovery and attribution.
- Ensure dataset license and attribution fields are surfaced where required.

### PROV-O

- Provenance bundles may be referenced by ID/run.
- The UI should expose provenance pointers in an inspectable way (e.g., “Data lineage” link/panel) when the UI design includes it.

---

## 🏛️ Architecture

### Design goal

Create a **small, predictable API surface** for the UI that is:
- typed,
- testable,
- contract-aligned,
- provenance-preserving,
- and governance-safe.

### Recommended layering (implementation-neutral)

1. **Transport/client layer**
   - base URL resolution
   - auth header injection (if applicable)
   - consistent timeout/cancel
   - error normalization

2. **Endpoint wrappers**
   - one module per feature/domain (e.g., `focus`, `layers`, `search`)
   - stable function signatures (prefer objects over positional params)

3. **Type + validation layer**
   - TypeScript types (and optional runtime validation)
   - explicit “unknown field” handling

4. **UI-facing helpers**
   - hooks/adapters (if present)
   - map-friendly transformations (only formatting, never semantic inference)

### Error handling conventions (recommended)

- Normalize errors into a small set of categories the UI can render:
  - network/timeout,
  - auth/permission (401/403),
  - not found (404),
  - contract mismatch (schema/type error),
  - server error (5xx).

~~~ts
// Example only — not confirmed in repo.
export type ApiErrorKind =
  | "network"
  | "timeout"
  | "auth"
  | "not_found"
  | "contract_mismatch"
  | "server";

export type ApiError = {
  kind: ApiErrorKind;
  message: string;
  status?: number;
  requestId?: string;
};
~~~

---

## ⚖️ FAIR+CARE & Governance

This folder is part of the **governed boundary** between “what exists in data/graph” and “what the user sees.”

- Favor “show the evidence” over “summarize the evidence.”
- Do not introduce UI behavior that reconstructs redacted content.
- Treat culturally sensitive or sovereignty-restricted content as high risk by default.
- If new UI features would surface new classes of data (e.g., restricted layers), require governance review.

---

## 🕰️ Version History

| Version | Date | Change | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-25 | Initial README for `web/src/api` | <author> |

---

## 🔗 Footer refs (do not remove)

- `docs/MASTER_GUIDE_v12.md`
- `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` *(if adopted)*
- `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- `src/server/contracts/**`
- `docs/governance/ROOT_GOVERNANCE.md`
- `docs/governance/ETHICS.md`
- `docs/governance/SOVEREIGNTY.md`
