---
title: "Web UI — API Client (web/src/api) README"
path: "web/src/api/README.md"
version: "v1.0.0"
last_updated: "2025-12-28"
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

# Web UI — API Client

`web/src/api/` is the **canonical home for Web UI API consumption code**: request helpers, endpoint wrappers, client-side response typing/validation, and **policy-aligned** handling of provenance/citations.

This folder exists to prevent:

- ad-hoc `fetch()` scattered across components,
- accidental drift from server contracts,
- and violations of the KFM invariant: **UI → API only** (no direct graph access).

## Non-negotiables

1. **UI never connects to Neo4j directly**
   - No Neo4j drivers in `web/`.
   - No Cypher in the browser.
   - Graph access happens only through contracted APIs.

2. **Focus Mode consumes only provenance-linked content**
   - The UI must not display unsourced narrative.
   - Citations/sources must be rendered from API-delivered provenance pointers.

3. **Contracts are canonical**
   - Do not “patch around” server contract changes in UI components.
   - Fix/update: contract → client wrapper/types → UI feature.

---

## 📘 Overview

### Purpose

- Provide a **single, consistent** place for the React/map UI to call KFM backend services.
- Enforce KFM boundary constraints at the UI edge:
  - **UI → API only** (no direct graph access).
  - **Provenance-first**: render citations/provenance references that come from the API; do not invent or guess sources.
- Make endpoint evolution predictable:
  - contract update (server) → client wrapper update (here) → UI feature update.

### Scope

| In Scope | Out of Scope |
|---|---|
| Base client utilities (base URL, headers, auth token wiring, timeouts, retries, cancellation) | Server API implementation (belongs in `src/server/`) |
| Endpoint wrapper functions (and optional UI hooks/adapters) used by UI | Neo4j drivers, Cypher queries, or graph access from web code |
| Client-side typing and (optional) runtime validation for API payloads | Authoring/defining contracts (belongs in `src/server/contracts/**` if present) |
| Provenance-preserving request/response handling for Focus Mode + Story Node retrieval | Authoring Story Nodes (belongs in `docs/reports/story_nodes/`) |

### Audience

- Primary: UI maintainers and contributors working under `web/`
- Secondary: API maintainers coordinating contract changes; reviewers enforcing governance/ethics/sovereignty constraints

### Definitions

- Glossary: `docs/glossary.md` *(not confirmed in repo — add or repair link if the glossary lives elsewhere)*

Terms used here:

- **API boundary**: the contracted interface surface (REST/GraphQL) exposed from `src/server/`.
- **Contract artifact**: machine-validated schema/spec (OpenAPI, GraphQL SDL, JSON Schema).
- **Context bundle**: a Focus Mode payload shaped as: entity + related entities + narrative + sources/provenance references.
- **Provenance-linked**: factual elements trace to source IDs (STAC/DCAT/PROV or other governed identifiers).
- **Redaction/generalization**: server-enforced transformation for sensitive content; the UI treats redacted outputs as final.

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide v12 | `docs/MASTER_GUIDE_v12.md` | KFM Core | Canonical pipeline + invariants |
| v13 redesign blueprint | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Architecture | “one canonical home”, contract-first, evidence-first |
| API contracts | `src/server/contracts/**` *(if present)* | API maintainers | Contract-first boundary |
| API Contract Extension Template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | API maintainers | Used for contract changes |
| Story Node Template v3 | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Curators | Narrative + citation rules |
| Universal Doc Template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs | Governs structure |

### Definition of done

- [ ] Front-matter complete + valid, and `path:` matches file location.
- [ ] Responsibilities + boundaries stated (UI→API only).
- [ ] Contract + provenance expectations documented (no unsourced narrative).
- [ ] Validation expectations listed (lint/typecheck/tests + contract drift strategy).
- [ ] Governance + CARE/sovereignty considerations explicitly stated.

---

## 🗂️ Directory Layout

### This document

- `path`: `web/src/api/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| UI root | `web/` | React/map UI; consumes APIs only |
| UI API client (this area) | `web/src/api/` | API wrappers + typing/validation + client utilities |
| API boundary (server) | `src/server/` | REST/GraphQL implementation; redaction + policy enforcement |
| API contracts | `src/server/contracts/**` *(if present)* | OpenAPI/GraphQL + versioning; contract tests required |
| Graph subsystem | `src/graph/` | Ontology bindings + ingest/build tooling |
| Catalog outputs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | Evidence + provenance artifacts |
| Story Nodes | `docs/reports/story_nodes/` | Draft/published narrative artifacts + assets |
| Schemas | `schemas/` | JSON Schemas (STAC/DCAT/PROV/story/ui/telemetry) |

### Expected local layout for `web/src/api`

> The structure below is a recommended, contract-first layout. If a file/path does not exist, treat it as **not confirmed in repo** and either (a) create intentionally, or (b) adjust this README to match the actual structure.

~~~text
📁 web/
└── 📁 src/
    └── 📁 api/
        ├── 📄 README.md
        ├── 📄 index.ts                         # (not confirmed in repo) public surface exports
        ├── 📁 client/                          # (not confirmed in repo) base HTTP + auth + retries + error mapping
        │   ├── 📄 http.ts
        │   ├── 📄 auth.ts
        │   └── 📄 errors.ts
        ├── 📁 endpoints/                       # (not confirmed in repo) endpoint wrappers grouped by feature/domain
        │   ├── 📄 focus.ts
        │   ├── 📄 search.ts
        │   └── 📄 layers.ts
        ├── 📁 types/                           # (not confirmed in repo) TS types + optional runtime validators
        │   ├── 📄 focus.ts
        │   └── 📄 provenance.ts
        └── 📁 __tests__/                       # (not confirmed in repo) unit + mocked integration tests
            ├── 📄 focus.test.ts
            └── 📄 http-errors.test.ts
~~~

---

## 🧭 Context

### Background

KFM is pipeline-ordered and boundary-governed. The canonical ordering is:

**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

The UI is not a system-of-record for semantics/provenance. It **renders contract-delivered payloads** and preserves provenance guarantees.

### Boundary constraints and invariants

1. **UI only reads from API endpoints and catalog endpoints**
   - No direct DB/Neo4j access.
   - If STAC/DCAT/PROV artifacts are accessed directly, they must be served as governed “catalog endpoints” (deployment-specific).

2. **Focus Mode rule is a hard gate**
   - Focus Mode consumes only provenance-linked context bundles.
   - Predictive/suggestive content (if any) must be opt-in, carry uncertainty metadata, and must not infer sensitive locations.

3. **Governance is enforced at boundaries**
   - Assume the server applies redaction + access controls.
   - UI must not reconstruct, infer, or “fill in” redacted content.

### Extension points

This folder participates primarily in two “where to add capability” extension points:

- (D) **API**: new endpoints with contract tests + redaction rules (server-side work).
- (E) **UI**: new features/layers that reference provenance pointers + CARE gating (this repo’s web work).

If you are trying to “add capability” but you are in the wrong stage:

- New dataset/evidence → start at `data/**` + STAC/DCAT/PROV + PROV (not here).
- New entity/relationship semantics → start at `src/graph/` + ontology mapping (not here).
- New endpoint behavior/shape → start at `src/server/` + contracts (not here).

### Open questions

| Question | Owner | Target |
|---|---|---|
| Are client types generated from OpenAPI/GraphQL (codegen), or authored manually? | UI/API | TBD |
| Is there a standard response “envelope” (e.g., `{ data, sources, provenance }`)? | API | TBD |
| What caching library is canonical (if any) for API calls (React Query/SWR/custom)? | UI | TBD |
| Are STAC/DCAT/PROV served via the API, or via dedicated static catalog endpoints? | API/UI | TBD |

---

## 🗺️ Diagrams

### Where `web/src/api` sits in the pipeline

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

## 📦 Data & Metadata

### What this folder must preserve

This folder is not “just HTTP glue.” It preserves:

- **Stable IDs** (graph IDs, dataset IDs, story node IDs).
- **Evidence pointers** (STAC/DCAT identifiers, licenses, attributions).
- **Lineage pointers** (PROV activity/run IDs if included by the API).
- **Policy state** (redaction flags, access/permission hints if provided by API).
- **Version semantics** (API versioning if present; explicit compatibility strategies for breaking changes).

### Example “context bundle” envelope

> API-defined; illustrative only.

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
      "ref": "data/stac/items/... (or served catalog URL)",
      "license": "CC-BY-4.0"
    }
  ],
  "provenance": {
    "prov_activity_id": "prov:activity:run:2025-12-01T12:00:00Z",
    "prov_bundle_ref": "data/prov/... (or served provenance URL)"
  }
}
~~~

### Sensitivity and redaction

- Do not log raw API responses that may contain sensitive details.
- Never store sensitive payloads in long-lived client storage unless explicitly allowed by governance.
- If coordinates are generalized/redacted, treat them as canonical for UI rendering.
- Do not guess missing locations or infer sensitive locations from related fields.

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- The UI may receive STAC Item/Collection identifiers or asset references.
- Client wrappers must preserve those IDs as-is (do not rewrite or “normalize” IDs unless required by contract).

### DCAT

- The UI may receive dataset-level descriptors/IDs for discovery and attribution.
- Ensure dataset license and attribution fields are surfaced where required (UI design-dependent).

### PROV-O

- Provenance bundles may be referenced by run/activity IDs and/or artifact refs.
- If the UI includes a “lineage” affordance, it should point to PROV references delivered by the API (inspectable, not inferred).

---

## 🧱 Architecture

### Design goal

Create a small, predictable API surface for the UI that is:

- typed,
- testable,
- contract-aligned,
- provenance-preserving,
- and governance-safe.

### Recommended layering

1. **Transport/client layer**
   - base URL resolution
   - auth header injection (if applicable)
   - timeout/cancellation
   - retries (careful: do not retry non-idempotent operations)
   - error normalization

2. **Endpoint wrappers**
   - one module per feature/domain (e.g., `focus`, `layers`, `search`)
   - stable function signatures (prefer object params over positional params)

3. **Types and optional runtime validation**
   - TypeScript types (and optional runtime validation)
   - explicit “unknown field” and “contract mismatch” handling

4. **UI-facing helpers**
   - hooks/adapters (if present)
   - map-friendly transformations that only format (never infer new facts)

### Error normalization conventions

Normalize errors into categories the UI can render consistently:

- network/timeout
- auth/permission (401/403)
- not found (404)
- contract mismatch (schema/type error)
- server error (5xx)

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
  requestId?: string; // if server returns one
};
~~~

### Adding or changing endpoints

If the API contract changes (new endpoint, new fields, deprecations, breaking changes):

1. Update/author a governed contract change doc using:
   - `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
2. Update server contracts and tests under:
   - `src/server/contracts/**` *(if present)* and associated server-side test suites
3. Update client wrappers + types here (`web/src/api/**`)
4. Update UI features/components to consume the wrapper (not raw `fetch()`)

---

## 🧠 Story Node and Focus Mode Integration

### How this work surfaces in Focus Mode

Focus Mode typically needs:

- the focused entity (Place/Person/Event/Artifact),
- related entities for context,
- a governed narrative artifact (Story Node),
- and a `sources[]`/provenance reference list that citations map to.

### UI-side enforcement checklist

- [ ] Do not render narrative blocks if citations/sources references are missing or invalid.
- [ ] Render citations in a consistent, inspectable way (IDs + resolvable refs).
- [ ] If AI-assisted content is ever delivered (opt-in), clearly label it and keep it visually distinct from curated narrative.
- [ ] Never fabricate citations or merge “similar” sources client-side.
- [ ] Treat redacted values as final (no reconstruction/inference).

---

## 🧪 Validation & CI/CD

### Minimum CI gates relevant to this area

- Markdown protocol validation (front-matter + required sections)
- Typecheck/lint/unit tests for `web/`
- API contract tests (server side; client must track shape/version)
- Security + sovereignty scanning gates (as applicable):
  - secret scan
  - PII scan
  - sensitive-location leakage checks
  - classification propagation checks (no downgrades without review)

### Suggested local validation

> Commands below are examples only (actual scripts are not confirmed in repo). Replace with repo-specific commands once known.

~~~bash
# Example placeholders — replace with repo-specific commands
# 1) run UI typecheck/tests
# npm test
# npm run typecheck
#
# 2) run lint
# npm run lint
~~~

### Testing strategy

- Unit tests for:
  - request builder (URL + query params),
  - error mapping,
  - runtime validation (if used).
- Mocked integration tests for:
  - endpoint wrappers returning expected typed objects,
  - failure scenarios (401/403, redaction responses, schema mismatch).
- Contract drift detection (ideal):
  - compare client expectations against `src/server/contracts/**` snapshots (approach TBD).

---

## ⚖ FAIR+CARE & Governance

This folder is part of the governed boundary between “what exists in data/graph” and “what the user sees.”

- Favor “show the evidence” over “summarize the evidence.”
- Do not introduce UI behavior that reconstructs redacted content.
- Treat culturally sensitive or sovereignty-restricted content as high risk by default.
- If new UI features would surface new classes of data (e.g., restricted layers), require governance review.

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-25 | Initial README for `web/src/api` | <author> |
| v1.0.0 | 2025-12-28 | Restructured to match Universal template; clarified invariants, extension points, and governance | <author> |

---

Footer refs:
- Master Guide: `docs/MASTER_GUIDE_v12.md`
- v13 redesign blueprint: `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Universal Doc Template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- API Contract Extension Template: `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- Story Node Template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- API contracts: `src/server/contracts/**` *(if present)*
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
