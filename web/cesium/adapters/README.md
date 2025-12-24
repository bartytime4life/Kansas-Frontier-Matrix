---
title: "Cesium Adapter Layer — README"
path: "web/cesium/adapters/README.md"
version: "v0.1.1"
last_updated: "2025-12-24"
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

doc_uuid: "urn:kfm:doc:web:cesium:adapters:readme:v0.1.1"
semantic_document_id: "kfm-web-cesium-adapters-readme-v0.1.1"
event_source_id: "ledger:kfm:doc:web:cesium:adapters:readme:v0.1.1"
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

# Cesium Adapter Layer (`web/cesium/adapters/`)

## 📘 Overview

### Purpose

This directory defines the **adapter layer** between KFM’s frontend features and Cesium’s rendering APIs.

Adapters exist to:

- **Centralize Cesium-specific implementation details** (lifecycle, primitives, performance, quirks).
- **Translate KFM layer descriptors and API payloads** into Cesium primitives/entities/tilesets.
- **Keep UI features stable** when Cesium versions or Cesium-facing implementation details change.
- **Enforce KFM invariants in the UI stage**:
  - no direct-to-graph access
  - contract-bound data access via APIs
  - provenance-first UX
  - sensitivity/redaction compliance

KFM canonical ordering remains unchanged:

**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

### Scope

| In Scope | Out of Scope |
|---|---|
| Adapter conventions, lifecycle management, and error handling | Defining API endpoints or changing server contracts (`src/server/`) |
| Mapping layer descriptors into Cesium imagery, terrain, entities, primitives, and 3D Tiles | Authoring datasets/caches/catalog outputs (belongs in `data/**` + catalogs) |
| Provenance passthrough to UI audit surfaces (sources panels, citation affordances) | Neo4j access from the frontend (no drivers, no Cypher, no “direct graph” paths) |
| Adapter-level telemetry hooks (if implemented) | Policy creation (governance lives under `docs/governance/`) |

### Audience

- Primary: Frontend engineers implementing Cesium layers and Focus Mode map behaviors.
- Secondary: API/contract owners validating UI consumption; governance reviewers checking provenance + sensitivity UX.

### Definitions

- Glossary: `docs/glossary.md` *(not confirmed in repo — repair link if glossary lives elsewhere)*

Terms used in this doc:

- **Adapter**: A module that creates, updates, and disposes Cesium objects for one “renderable unit” (layer, overlay, tileset, entity collection).
- **Handle**: The runtime object(s) returned by an adapter that must be disposed/detached on unload.
- **Layer descriptor**: A contract-bound config/payload describing a layer and its sources, attribution, sensitivity flags, and parameters.
- **Provenance refs**: Identifiers pointing to evidence (STAC Item/Collection IDs, DCAT dataset IDs, PROV activity IDs, document IDs).
- **Audit bundle**: A structured object the UI can render as “Sources / Evidence / Lineage” for a given layer/feature.

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This README | `web/cesium/adapters/README.md` | UI | Adapter conventions + invariants |
| Cesium area README | `web/cesium/README.md` | UI | Cesium integration overview + layer registry expectations |
| Layer registry | `web/cesium/layers/` | UI + Governance | Registry patterns referenced here; exact filenames vary |
| UI schemas | `schemas/ui/` | Schemas owners | Layer registry schema validation (not confirmed in repo) |
| API boundary | `src/server/` | API | Contracted access + redaction/generalization enforcement |
| API contracts | `src/server/contracts/` | API | UI must remain contract-bound |
| Story Nodes (canonical) | `docs/reports/story_nodes/` | Curators | Narrative artifacts consumed via API context bundles |

### Definition of done

- [ ] Adapters do **not** read Neo4j directly and do not embed Cypher, Bolt drivers, or graph credentials.
- [ ] Adapters consume only **contracted** inputs:
  - layer registry descriptors (schema-validated if schemas exist)
  - API payloads (REST/GraphQL contract-bound)
- [ ] Every rendered layer can surface **provenance refs** to the audit UI (when available).
- [ ] All Cesium resources are disposed on detach to prevent memory/GPU leaks.
- [ ] Adapter inputs/outputs are typed, and adapters are unit-testable with mocked Cesium primitives.
- [ ] Sensitivity and redaction flags in payloads/descriptors are respected (no client-side reconstruction).

## 🗂️ Directory Layout

### This document

- `path`: `web/cesium/adapters/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Frontend root | `web/` | UI app root (React/Map runtimes, configs, tests) |
| Cesium integration | `web/cesium/` | Cesium viewer wiring, scene config, registry adapters |
| Cesium adapter layer | `web/cesium/adapters/` | This directory: translation + lifecycle + resource management |
| Layer registries | `web/**/layers/**` | Declarative layer configs *(exact location not confirmed in repo)* |
| UI schemas | `schemas/ui/` | JSON Schemas for UI registries *(not confirmed in repo)* |
| API boundary | `src/server/` | Contracted access layer + redaction/provenance |
| API contracts | `src/server/contracts/` | OpenAPI/GraphQL + tests |
| Evidence catalogs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | Evidence artifacts referenced in provenance |
| Story Nodes | `docs/reports/story_nodes/` | Governed narratives + assets (served via API) |

### Expected file tree for this sub-area

> The non-README filenames below are **recommended conventions**. The actual contents of this directory are not confirmed in repo; keep this section synchronized with reality.

~~~text
📁 web/
└── 📁 cesium/
    └── 📁 adapters/
        ├── 📄 README.md
        ├── 📄 index.ts                 # public adapter exports + registry
        ├── 📄 types.ts                 # adapter context + contracts
        ├── 📄 resources.ts             # resource tracker / disposables
        ├── 📄 errors.ts                # normalized adapter error types
        ├── 📄 audit.ts                 # audit bundle helpers (provenance passthrough)
        ├── 📄 imageryAdapter.ts        # imagery/overlay adapter example
        ├── 📄 tileset3dAdapter.ts      # 3D Tiles adapter example
        └── 📄 entitiesAdapter.ts       # entities/primitives adapter example
~~~

## 🧭 Context

### Background

Adapters operate strictly in the **UI stage**. Their job is to render what contracts provide (layers, tiles, entity bundles), while preserving provenance, sensitivity, and the API boundary rule.

### Assumptions

- The frontend consumes data only via API contracts and/or schema-validated registries.
- API responses can include provenance identifiers (STAC/DCAT/PROV IDs, document IDs).
- Cesium objects require explicit teardown to avoid GPU and memory leaks.
- The UI may support switching between 2D and 3D without losing state (MapLibre ↔ Cesium) *(toggle behavior not confirmed in repo)*.

### Constraints and invariants

Non-negotiables:

- **API boundary**: UI never queries Neo4j directly; graph access is via `src/server/`.
- **Contracts are canonical**:
  - UI registry schemas live under `schemas/` (if present)
  - API contracts live under `src/server/contracts/` (if present)
- **Provenance-first UX**:
  - adapters pass through provenance refs to audit UI
  - do not show uncited narrative or “mystery layers” without attribution
- **Sensitivity enforcement**:
  - respect API-provided redaction/generalization flags
  - do not reconstruct “more precise” locations client-side (including via snapping, triangulation, reverse-geocoding, or implicit inference)

### Open questions

| Question | Owner | Target date |
|---|---|---|
| What is the canonical layer descriptor type shared across 2D/3D map runtimes? | TBD | TBD |
| Where is the layer registry schema validated in CI? | TBD | TBD |
| What telemetry schema should adapters emit for timings and failures? | TBD | TBD |

### Future extensions

- Adapter “capability negotiation” (declare what an adapter supports: time-dynamic, terrain, clipping planes, etc.).
- Shared layer descriptor translation across map engines (MapLibre ↔ Cesium) without diverging semantics.

## 🗺️ Diagrams

### UI dataflow

~~~mermaid
flowchart LR
  A["API contracts + registry descriptors"] --> B["Layer descriptors"]
  B --> C["Cesium adapters"]
  C --> D["Cesium Viewer / Scene"]
  B --> E["Audit UI (sources/provenance)"]
  A --> E
~~~

### Adapter lifecycle

~~~mermaid
sequenceDiagram
  participant Feature as UI Feature
  participant Adapter as Cesium Adapter
  participant Viewer as Cesium Viewer
  participant API as KFM API (src/server)

  Feature->>API: fetch layer descriptor + provenance refs
  API-->>Feature: payload
  Feature->>Adapter: attach(ctx, input)
  Adapter->>Viewer: create Cesium primitives
  Feature->>Adapter: update(ctx, patch)
  Adapter->>Viewer: update primitives
  Feature->>Adapter: detach(ctx)
  Adapter->>Viewer: destroy primitives
~~~

## 📦 Data and Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Layer descriptor | JSON / typed object | API response or layer registry | Contract tests + runtime parsing |
| Focus context | object | Focus Mode UI state | Type-checked |
| Time controls | ISO strings / ranges | UI state / API response | Validate parseable timestamps |
| Provenance refs | IDs/URIs | API response | Must be renderable in audit UI |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Cesium runtime handle | object | In-memory | Adapter type contract |
| Audit bundle | JSON-ish object | In-memory | UI audit component contract (repo-specific) |
| Telemetry events (optional) | JSON-ish | In-memory / emitter | `schemas/telemetry/` *(not confirmed in repo)* |

### Sensitivity and redaction

- Treat redaction/generalization flags as **authoritative**.
- Do not infer sensitive locations or increase precision in the client.
- Do not log precise coordinates or sensitive identifiers to client telemetry (unless explicitly permitted and reviewed).

### Quality signals

- Deterministic teardown: no leaked primitives after detach.
- Adapter attach/update/detach timing and failure types (when telemetry exists).
- No orphan layer references (descriptor references reachable endpoints/assets).

## 🌐 STAC, DCAT and PROV Alignment

Adapters **do not author** catalogs. They only consume evidence/provenance identifiers surfaced by APIs.

- **STAC**: pass through STAC Item/Collection IDs and asset refs if provided.
- **DCAT**: preserve dataset IDs and attribution metadata if provided.
- **PROV-O**: surface activity/run IDs in audit UI and (optionally) in telemetry to support traceability.

## 🧱 Architecture

### Responsibilities

Adapters are responsible for:

- creating Cesium objects (imagery layers, tilesets, primitives, entities)
- updating Cesium objects when UI state changes (visibility, styling, time filters)
- disposing Cesium objects on unload
- surfacing provenance/audit bundles to the UI
- isolating Cesium-specific code so feature code stays engine-agnostic

Adapters are not responsible for:

- authentication/session management
- API schema evolution or compatibility (that is a contract + server concern)
- data enrichment, entity inference, or narrative generation
- policy creation (governance lives in `docs/governance/`)

### Adapter contract pattern

Reference shape (not mandated implementation):

~~~ts
export type CesiumAdapterContext = {
  viewer: unknown; // Cesium.Viewer in concrete code

  // Contracted API access. Adapters do not own auth/session concerns.
  api: {
    get: <T>(path: string, opts?: { signal?: AbortSignal }) => Promise<T>;
    post?: <T>(path: string, body: unknown, opts?: { signal?: AbortSignal }) => Promise<T>;
  };

  // Centralized telemetry hook (optional).
  telemetry?: {
    emit: (event: string, props: Record<string, unknown>) => void;
  };

  // Optional audit sink for provenance bundles.
  audit?: {
    publish: (bundle: Record<string, unknown>) => void;
  };
};

export type AdapterAttachResult<THandle> = {
  handle: THandle;
  auditBundle?: Record<string, unknown>;
};

export interface KfmCesiumAdapter<TIn, THandle> {
  id: string;

  // Idempotent expectation: attach creates everything needed and returns a handle.
  attach: (ctx: CesiumAdapterContext, input: TIn) => Promise<AdapterAttachResult<THandle>>;

  // Optional incremental update.
  update?: (ctx: CesiumAdapterContext, handle: THandle, patch: Partial<TIn>) => Promise<void>;

  // Deterministic teardown: remove/destroy all created Cesium resources.
  detach: (ctx: CesiumAdapterContext, handle: THandle) => Promise<void>;
}
~~~

### Resource management

- Track all created Cesium resources via a single “resource tracker” so detach is deterministic.
- Support cancellation during attach:
  - use `AbortController` for any fetches
  - if attach is cancelled or fails, ensure partial resources are disposed
- Avoid “hidden global singletons” inside adapters (prefer dependency injection).

### Error handling

- Prefer failing a **single adapter** cleanly over failing the whole viewer.
- Normalize errors into stable, inspectable types (timeout, schema mismatch, forbidden, source unavailable, etc.).
- Emit telemetry (if present) on:
  - attach start/success/failure
  - update failure
  - detach start/success/failure
- Surface a user-visible error state that includes attribution and provenance context when possible.

### Performance notes

- Avoid per-frame allocations inside adapters.
- Debounce/throttle UI-driven updates where safe.
- Prefer “one-time construction + incremental updates” over teardown/rebuild on every interaction.

### Security notes

- Do not commit secrets (Cesium/Ion tokens, API keys, private endpoints).
- Any sensitive access must be mediated server-side; the client should not learn restricted URLs or credentials.

## 🧠 Story Node and Focus Mode Integration

Adapters may be driven by Focus Mode controls:

- layer toggles
- time window selection
- camera focus / zoom-to actions

Optional structured controls (mirrors Story Node conventions):

~~~yaml
focus_layers:
  - "example-layer-id"
focus_time: "1854-01-01/1854-12-31"
focus_center: [ -98.0000, 38.0000 ]
~~~

Rules:

- Focus Mode must remain provenance-linked.
- If Focus Mode requests any predictive overlays, they must be opt-in and include uncertainty metadata (if supported by the API contract).

## 🧪 Validation and CI

### Validation steps

- [ ] Lint and typecheck adapter modules (tooling repo-specific).
- [ ] Unit tests for attach/update/detach with mocked Cesium primitives.
- [ ] Contract alignment tests for adapter-consumed payloads (API/client typing).
- [ ] UI registry schema validation (if `schemas/ui/` exists).
- [ ] Governance review for any change that affects provenance surfaces or sensitivity handling.

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands
# cd web
# (npm|pnpm|yarn) install
# (npm|pnpm|yarn) run lint
# (npm|pnpm|yarn) run typecheck
# (npm|pnpm|yarn) test
~~~

## ⚖ FAIR+CARE and Governance

### Review gates

Human review is required for changes that impact:

- provenance rendering / audit surfaces
- redaction/generalization behavior
- exposure of new source URLs in descriptors
- telemetry payload fields (especially anything location-revealing)

### CARE and sovereignty considerations

- Do not add client-side logic that increases the precision of restricted locations.
- Prefer server-side generalization where policy can be audited and enforced.

### AI usage constraints

- Adapters must not generate narrative claims.
- Adapters must not infer sensitive locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v0.1.0 | 2025-12-21 | Initial Cesium adapters README | TBD |
| v0.1.1 | 2025-12-24 | Clarified adapter boundaries, provenance/audit bundle expectations, fixed Story Nodes path, expanded lifecycle/resource rules | TBD |

---

Footer refs:
- Cesium area: `web/cesium/README.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Story Nodes: `docs/reports/story_nodes/`