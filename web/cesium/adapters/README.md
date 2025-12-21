---
title: "Cesium Adapter Layer — README"
path: "web/cesium/adapters/README.md"
version: "v0.1.0"
last_updated: "2025-12-21"
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

doc_uuid: "urn:kfm:doc:web:cesium:adapters:readme:v0.1.0"
semantic_document_id: "kfm-web-cesium-adapters-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:web:cesium:adapters:readme:v0.1.0"
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

# Cesium Adapter Layer

## 📘 Overview

### Purpose
This directory defines the **adapter layer** between KFM’s frontend features and Cesium’s rendering APIs.

Adapters exist to:
- centralize Cesium-specific code and lifecycle handling
- translate KFM layer configs and API payloads into Cesium primitives
- keep UI features stable when Cesium versions or implementation details change
- enforce KFM invariants in the UI layer (no direct graph access; provenance-first UX)

### Scope
| In Scope | Out of Scope |
|---|---|
| Conventions for Cesium adapter modules, lifecycle, and error handling | Defining API endpoints or changing server contracts |
| Mapping KFM layer descriptors to Cesium constructs | Adding new datasets or catalog entries |
| Provenance passthrough to UI audit surfaces | Direct Neo4j access from the frontend |

### Audience
- Primary: Frontend engineers working in `web/` on Cesium layers and Focus Mode behaviors.
- Secondary: API engineers verifying UI consumption patterns; curators validating provenance UX.

### Definitions
- Glossary link: `docs/glossary.md` (not confirmed in repo)
- Terms used in this doc:
  - **Adapter**: a module that creates, updates, and disposes Cesium objects for a single “thing” (layer, overlay, tileset, entity collection).
  - **Handle**: the runtime object(s) returned by an adapter that must be disposed/detached on unload.
  - **Provenance refs**: identifiers returned by APIs that point to STAC/DCAT/PROV sources (IDs, asset refs, run IDs).

### Key artifacts
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This README | `web/cesium/adapters/README.md` | Frontend | Adapter conventions and invariants |
| Layer registry | `web/cesium/layers/` | Frontend | Registry patterns are referenced; exact files not confirmed in repo |
| API client wrapper | `web/**/api/` | Frontend | Naming varies; use DI so adapters don’t own auth/session |

### Definition of done
- [ ] Adapters do not read Neo4j directly and do not embed Cypher or graph drivers
- [ ] Adapters call only contracted API endpoints (REST/GraphQL), respecting auth and redaction
- [ ] Every rendered layer can surface provenance refs to the audit UI (when available)
- [ ] All adapter resources are disposed on unload to prevent memory leaks
- [ ] Adapter inputs and outputs are typed and unit-testable

## 🗂️ Directory Layout

### This document
- `path`: `web/cesium/adapters/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Frontend root | `web/` | UI app code, map clients, layer registry, Focus Mode UX |
| Cesium client | `web/cesium/` | Cesium viewer wiring, scene config, adapter implementations |
| APIs | `src/server/` | Contracted access layer (REST/GraphQL) |
| Schemas | `schemas/` | JSON schemas (STAC/DCAT/PROV, telemetry, UI registries) |
| Story Nodes | `docs/reports/.../story_nodes/` | Provenance-linked narrative artifacts |

### Expected file tree for this sub-area
~~~text
📁 web/
└── 📁 cesium/
    └── 📁 adapters/
        ├── 📄 README.md
        ├── 📄 index.ts              — recommended public exports
        ├── 📄 types.ts              — adapter context and type contracts
        ├── 📄 telemetry.ts          — adapter-level telemetry helpers
        ├── 📄 imageryAdapter.ts     — imagery/overlay adapter example
        ├── 📄 tilesetAdapter.ts     — 3D Tiles adapter example
        └── 📄 entityAdapter.ts      — entity/primitive adapter example
~~~

Notes:
- The non-README filenames above are **recommended** conventions; the exact contents of this directory are not confirmed in repo.

## 🧭 Context

### Background
KFM’s canonical pipeline is:

ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React map UI → Story Nodes → Focus Mode.

The adapter layer lives in the **UI stage**. Its job is to render what the API provides (layers, tiles, entity bundles) while preserving provenance and sensitivity rules.

### Assumptions
- The frontend consumes data only via API contracts.
- API responses can include provenance references (STAC item IDs, PROV activity IDs, dataset identifiers).
- Cesium objects require explicit teardown to avoid GPU and memory leaks.

### Constraints and invariants
- **API boundary**: UI never queries Neo4j directly.
- **Provenance-first**: adapters should pass through provenance refs for audit rendering.
- **Sensitivity**: adapters must respect redaction/generalization flags from the API payload.
- **Deterministic behavior**: given the same adapter inputs, rendering should be stable and repeatable.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| What is the canonical “layer descriptor” type used across MapLibre and Cesium clients? | TBD | TBD |
| Where is the layer registry schema validated in CI? | TBD | TBD |
| What telemetry schema should adapters emit for load failures and timings? | TBD | TBD |

### Future extensions
- Add adapter-level provenance “bundles” that can be shown in an audit panel without extra API round trips.
- Add “capability negotiation” so adapters can declare Cesium feature requirements.

## 🗺️ Diagrams

### UI dataflow
~~~mermaid
flowchart LR
  A[API contracts] --> B[Layer descriptors]
  B --> C[Cesium adapters]
  C --> D[Cesium Viewer]
  B --> E[Audit panel]
  A --> E
~~~

### Adapter lifecycle
~~~mermaid
sequenceDiagram
  participant Feature as UI Feature
  participant Adapter as Cesium Adapter
  participant Viewer as Cesium Viewer
  participant API as KFM API

  Feature->>API: fetch layer descriptor + provenance refs
  API-->>Feature: payload
  Feature->>Adapter: attach(ctx, payload)
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
| Layer descriptor | JSON | API or layer registry | Contract tests and runtime parsing |
| Focus context | Object | Focus Mode state | Type-checked |
| Time controls | ISO string, range | UI state / API response | Validate parseable timestamps |
| Provenance refs | IDs/URIs | API response | Must be renderable in audit UI |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Cesium runtime handle | Object | In-memory | Adapter type contract |
| Audit metadata | JSON | In-memory | UI audit component contract |

### Sensitivity and redaction
- Adapters must honor API-provided redaction/generalization rules.
- Adapters must not infer or reconstruct sensitive locations.

### Quality signals
- Load timing (start/end), tile/asset counts, and failure types.
- Deterministic teardown: no leaked primitives after detach.

## 🌐 STAC, DCAT and PROV Alignment

### STAC
Adapters should treat STAC identifiers and asset links as **read-only inputs**:
- If the API returns STAC item IDs or asset refs, pass them through to the audit UI.
- Do not “fix up” STAC metadata in the client.

### DCAT
If a layer is sourced from a DCAT dataset identifier, the adapter should preserve that ID in its audit bundle.

### PROV-O
If a payload includes PROV activity or agent refs:
- surface them in audit UI
- include them in telemetry events to support traceability

## 🧱 Architecture

### Responsibilities
Adapters are responsible for:
- creating Cesium objects (imagery layers, tilesets, primitives, entities)
- updating Cesium objects when UI state changes (visibility, styling, time filters)
- disposing Cesium objects on unload
- emitting telemetry and surfacing provenance

Adapters are not responsible for:
- authentication and session management
- API schema evolution
- data enrichment, entity inference, or narrative generation

### Adapter contracts
The types below are reference patterns, not a mandated implementation.

~~~ts
// Recommended shape for adapter context.
export type CesiumAdapterContext = {
  viewer: unknown; // Cesium.Viewer in concrete code

  // Contracted API access. The adapter should not own auth/session concerns.
  api: {
    get: <T>(path: string, opts?: { signal?: AbortSignal }) => Promise<T>;
  };

  // Centralized telemetry hook.
  telemetry: {
    emit: (event: string, props: Record<string, unknown>) => void;
  };

  // Optional: audit sink for provenance bundles.
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
  attach: (ctx: CesiumAdapterContext, input: TIn) => Promise<AdapterAttachResult<THandle>>;
  update?: (ctx: CesiumAdapterContext, handle: THandle, patch: Partial<TIn>) => Promise<void>;
  detach: (ctx: CesiumAdapterContext, handle: THandle) => Promise<void>;
}
~~~

### Error handling
- Prefer failing a single adapter cleanly over failing the whole viewer.
- Emit telemetry on:
  - attach start/success/failure
  - detach start/success/failure
  - update failure
- If an adapter fails, surface a user-visible error state that includes provenance context when possible.

### Performance notes
- Avoid per-frame allocations in adapters.
- Debounce updates from UI state when safe.
- Use AbortSignals for cancellable fetches during attach.

## 🧠 Story Node and Focus Mode Integration

Adapters may be driven by Focus Mode controls:
- layer toggles
- time window selection
- camera focus and “zoom-to” actions

Optional structured controls pattern (mirrors Story Node conventions):

~~~yaml
focus_layers:
  - "example-layer-id"
focus_time: "1854-01-01/1854-12-31"
focus_center: [ -98.0000, 38.0000 ]
~~~

Rules:
- Focus Mode must remain provenance-linked.
- If Focus Mode asks for predictive or inferred overlays, they must be opt-in and include uncertainty metadata.

## 🧪 Validation and CI

### Validation steps
- [ ] Typecheck and lint adapter modules
- [ ] Unit test adapter attach/update/detach behaviors with mocked Cesium objects
- [ ] Contract test API payload parsing used by adapters
- [ ] Validate any UI layer registry entries against schema (if applicable)
- [ ] Ensure sensitive-location prohibitions are not violated in adapter logic

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# 1) typecheck
# 2) lint
# 3) unit tests
# 4) UI registry schema validation
~~~

## ⚖ FAIR+CARE and Governance

### Review gates
- Changes to adapter behavior that impact:
  - provenance rendering
  - redaction/generalization
  - new telemetry fields
  require human review.

### CARE and sovereignty considerations
- Do not add client-side logic that increases the precision of restricted locations.
- Prefer server-side generalization where policy can be audited.

### AI usage constraints
- Adapters must not generate narrative claims.
- Adapters must not infer sensitive locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v0.1.0 | 2025-12-21 | Initial Cesium adapters README | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
