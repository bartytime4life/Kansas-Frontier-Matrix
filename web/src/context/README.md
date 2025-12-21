---
title: "Kansas Frontier Matrix — Web Context Layer Overview"
path: "web/src/context/README.md"
version: "v12.0.0-draft"
last_updated: "2025-12-21"
status: "draft"
doc_kind: "Guide"
license: "MIT"

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
care_label: "Public / Medium (context-dependent)"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:web:context-readme:v12.0.0-draft"
semantic_document_id: "kfm-doc-web-context-readme-v12.0.0-draft"
event_source_id: "ledger:web/src/context/README.md"
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

# Kansas Frontier Matrix — Web Context Layer Overview
`web/src/context/`

This document governs how **shared UI state** is structured and accessed across the KFM Web UI using a **React Context layer** (providers + hooks), while preserving platform invariants: **API-first contracts**, **governance-aligned rendering**, and **no hidden data leakage**.

## 📘 Overview

### Purpose
- Define the role of `web/src/context/` as KFM’s **cross-cutting UI state boundary**.
- Establish invariants for **governance-aware state**, **provenance-preserving identifiers**, and **safe telemetry**.

### Scope
| In Scope | Out of Scope |
|---|---|
| Context provider patterns, state boundaries, and invariants | Backend graph queries, ETL logic, catalog generation |
| Rules for storing identifiers, redaction flags, and UI state | Defining new API endpoints (use API Contract template) |
| Guidance for Focus Mode + Story Node state handoff | Creating Story Nodes themselves (use Story Node template) |

### Audience
- Primary: Web UI developers, reviewers, and maintainers
- Secondary: Governance reviewers, QA, security/privacy reviewers

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc: Context Provider, Context Hook, Focus Mode, Story Node, Provenance, Redaction, Generalization

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This README | `web/src/context/README.md` | Web | Governed conventions + invariants |
| UI components | `web/src/components/` | Web | Consumers of context hooks |
| API contracts | `src/api/` + `docs/api/` | API | UI state should reflect API contract types |
| Telemetry schemas | `schemas/telemetry/` | Platform | Context-driven events must conform |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Invariants explicitly stated (API boundary, no leakage, governance flags honored)
- [ ] Clear examples of “store IDs, not secrets”
- [ ] Validation steps listed and repeatable
- [ ] Version history updated

## 🗂️ Directory Layout

### This document
- `path`: `web/src/context/README.md` (must match front-matter)

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Frontend | `web/` | React + map clients |
| Frontend context | `web/src/context/` | Providers + hooks for shared UI state |
| Frontend components | `web/src/components/` | UI building blocks that consume context |
| Schemas | `schemas/` | JSON schemas + telemetry schemas |
| Documentation | `docs/` | Canonical governed docs (Master Guide, templates, standards) |

### Expected file tree for this sub-area
> This is an **expected** layout. If your branch differs, update the tree to match actual filenames.

~~~text
📁 web/
└── 📁 src/
    ├── 📁 context/
    │   ├── 📄 README.md                  — This document
    │   ├── 📄 index.ts                   — Re-export providers/hooks (optional)
    │   ├── 📄 AppProviders.tsx           — Root provider composition (optional)
    │   ├── 📄 GovernanceContext.tsx      — Governance flags + redaction state (optional)
    │   ├── 📄 SelectionContext.tsx       — Selected entity/feature IDs (optional)
    │   ├── 📄 MapViewContext.tsx         — Viewport/layer toggles/time range (optional)
    │   ├── 📄 FocusModeContext.tsx       — Focus Mode lifecycle + focus entity (optional)
    │   ├── 📄 TelemetryContext.tsx       — Safe event emit helpers (optional)
    │   └── 📄 types.ts                   — Shared context types/interfaces (optional)
    ├── 📁 components/
    └── 📁 api/
~~~

## 🧭 Context

### Background
KFM’s web UI spans map, timeline, search, Story Nodes, and Focus Mode. Many interactions require **shared state** across multiple components (e.g., selected entity ID, active layer set, focus mode target, and governance/redaction hints).

The context layer exists to:
- reduce prop-drilling across complex layouts
- provide a consistent “state boundary” for governance and provenance rules
- centralize safe interaction signals (telemetry) without duplicating logic across components

### Assumptions
- The frontend is a React application, and `web/src/context/` provides the canonical location for shared state.
- The UI consumes **contracted API payloads** (not direct database/graph reads).
- Governance decisions (redaction/generalization) are computed and enforced upstream and surfaced to the UI as flags and display-safe values.

### Constraints / invariants
- Canonical ordering is preserved: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- The UI (and context layer) **does not** query Neo4j directly. All graph access must occur behind APIs.
- Context values must be **safe-by-construction**:
  - store stable IDs + display-safe fields
  - never store or emit sensitive raw values that should be redacted/generalized
- Context must not create “shadow data paths” that bypass governance checks.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Which contexts are authoritative vs. legacy (if multiple exist)? | Web | TBD |
| What is the canonical place for derived UI state (context vs. local component state)? | Web | TBD |
| Is any context persisted (URL, storage)? If yes, what governance constraints apply? | Web + Governance | TBD |

### Future extensions
- Standardize “context boundary contracts” (types + runtime checks) to prevent accidental leakage.
- Add explicit “governance gate” helpers for actions that depend on redaction state.

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[ETL] --> B[STAC/DCAT/PROV Catalogs]
  B --> C[Neo4j Graph]
  C --> D[APIs]
  D --> E[React/Map UI]
  E --> F[Story Nodes]
  F --> G[Focus Mode]
~~~

### Optional: sequence diagram (context-driven UI update)
~~~mermaid
sequenceDiagram
  participant User
  participant UI as React UI
  participant Ctx as Context Provider
  participant API
  participant G as Governance Rules (API-side)

  User->>UI: Select entity / feature
  UI->>Ctx: setSelectedEntityId(id)
  Ctx->>API: fetchContextBundle(id)
  API->>G: apply redaction/generalization rules
  G-->>API: display-safe payload + governance flags + provenance refs
  API-->>Ctx: context bundle (contracted)
  Ctx-->>UI: updated state -> re-render
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| User interactions (selection, navigation) | events | UI components | Type-safe handler signatures |
| Contracted API payloads (context bundle) | JSON | API layer | Schema/Type validation at boundary |
| Governance flags (redaction/generalization) | booleans/enums | API payload | Treat as authoritative |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Shared UI state | TS objects | `web/src/context/*` | Type-checked (TS) |
| Telemetry events (non-PII) | JSON | emitters | `schemas/telemetry/*` (as applicable) |

### Sensitivity & redaction
Context is a **high-risk accidental leakage surface** because it’s widely consumed.
Rules:
- Store **stable identifiers** and **display-safe fields** only.
- If the API indicates redaction/generalization:
  - store the redaction flag + safe display value
  - do not store raw sensitive values “just in case”
- Never put sensitive fields into:
  - telemetry payloads
  - console logs
  - DOM attributes

### Quality signals
- Context boundary types should be explicit and composable.
- Avoid “any” / untyped state; prefer narrow interfaces.
- Prefer derived selectors/hooks over duplicating computed state across components.

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Context should store **STAC item/collection identifiers** as opaque IDs (if used by UI), not duplicate full catalogs in memory.

### DCAT
- Context may store **dataset identifiers** and key display-safe metadata fields (title, license, attribution) as provided by APIs.

### PROV-O
- Context should preserve provenance references returned by APIs (e.g., run/activity IDs), and pass them through to:
  - Detail panels
  - Story Node views
  - Focus Mode audit/provenance surfaces

### Versioning
- Context state should prefer stable IDs and versioned references (predecessor/successor links) over mutable “latest only” semantics.

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| Context Providers | Own shared state + boundary validation | Provider props + typed values |
| Context Hooks | Read/derive state + enforce access patterns | `useXyz()` hooks |
| API adapters | Fetch contracted payloads | typed request/response |
| Governance gating helpers | Enforce UI-safe decisions | `canShowX`, `canExportY` |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| API payload types | `src/api/` + docs | Contract tests required |
| Telemetry schemas | `schemas/telemetry/` | Semver + schema validation |
| UI governance invariants | `docs/governance/*` | Requires review on change |

### Extension points checklist (for future work)
- [ ] Add a new provider only when state is truly cross-cutting
- [ ] Ensure new state preserves provenance references
- [ ] Ensure new state does not introduce leakage paths
- [ ] Add tests for redaction/gating behaviors
- [ ] Add telemetry only if schema-backed and non-PII

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Context should store:
  - the focused entity ID
  - the focus bundle payload (contracted)
  - governance flags required to render the focus bundle safely
- Focus Mode must only consume provenance-linked content and must not introduce uncited claims.

### Provenance-linked narrative rule
- Any narrative rendered in Focus Mode must preserve links to:
  - dataset/document IDs
  - STAC asset references (when relevant)
  - PROV activity/run references (when available)

## 🧪 Validation & CI/CD

Minimum checks for the context layer:
- Type checking (context values, hooks, provider props)
- Unit tests:
  - default state + reducers (if used)
  - redaction/gating helpers
  - telemetry emit helpers (shape + non-PII)
- Integration tests:
  - selection → context update → detail panel render
  - focus entry/exit behavior (state reset, safe caching)
- Security/privacy checks:
  - ensure no secrets/PII in state snapshots or telemetry fixtures
  - ensure no sensitive values logged during errors

## ⚖ FAIR+CARE & Governance

Context must:
- treat governance/redaction flags from APIs as **authoritative**
- ensure UI actions respect governance (export/share/precision controls)
- avoid “copy-through” of sensitive raw values even if present upstream

Context must not:
- reconstruct sensitive locations from partial data
- provide hidden toggles to reveal redacted fields
- bypass the API boundary by embedding direct graph logic in the UI

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v12.0.0-draft | 2025-12-21 | Initial v12-governed README for `web/src/context/` | TBD |
---

Footer refs:
- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Universal template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`