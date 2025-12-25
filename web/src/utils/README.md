---
title: "KFM Web UI — Utils"
path: "web/src/utils/README.md"
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

doc_uuid: "urn:kfm:doc:web:src:utils:readme:v1.0.0"
semantic_document_id: "kfm-web-src-utils-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:src:utils:readme:v1.0.0"
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

# KFM Web UI — Utils

## 📘 Overview

### Purpose
`web/src/utils/` is the shared utility layer for the KFM web UI. Its job is to keep UI behavior consistent and testable by centralizing:

- small, reusable helper functions (formatting, parsing, validation helpers),
- “adapter” functions that translate **contract artifacts** (API responses, Story Node Markdown, UI registries) into UI-ready structures,
- safe-by-default helpers for citation rendering and provenance display.

This directory supports the project’s canonical architecture ordering:

**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

Utilities live on the **UI** side of the API boundary and must not “reach across” into server or graph internals.

### Scope

| In Scope | Out of Scope |
|---|---|
| Pure/mostly-pure helpers (string/date/number formatting, parsing, small transforms) | React components/hooks (belong in `web/src/components/**` or similar) |
| UI adapters for contract artifacts (API response normalization, citation parsing) | ETL/graph logic (belongs in `src/pipelines/**` / `src/graph/**`) |
| Map/client helpers (e.g., translating a layer registry entry into client config) | Direct Neo4j access (UI must not query the graph directly) |
| Guarded helpers for redaction-safe display (masking, generalization-ready formatting) | Secrets, keys, internal-only endpoints, or “hidden data leakage” patterns |

### Audience
- Primary: Web/UI maintainers and contributors
- Secondary: API maintainers (to understand how UI expects contracts to behave), narrative curators (how Story Nodes render)

### Definitions
- **Contract artifact**: a machine-validated schema/spec (JSON Schema, OpenAPI, GraphQL SDL, UI registry schema).
- **Evidence artifact**: validated STAC/DCAT/PROV outputs and derived evidence products.
- **Story Node**: provenance-linked narrative Markdown designed to be rendered in the UI.
- **Focus Mode**: immersive UI state that consumes provenance-linked context only.

> If `docs/glossary.md` exists, prefer linking definitions there; otherwise treat the glossary path as not confirmed in repo and repair links where needed.

### Key artifacts (what this README aligns to)
| Artifact | Path / Identifier | Notes |
|---|---|---|
| Master Guide v12 | `docs/MASTER_GUIDE_v12.md` | Canonical pipeline + invariants |
| Redesign blueprint v13 (draft; if adopted) | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Canonical roots + CI gates + contract-first rules |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Front-matter + citation rules used in Focus Mode |
| API contracts | `src/server/contracts/**` | UI must consume contracts through APIs |
| UI registry schemas | `schemas/ui/**` | Used to validate layer registry and other UI registries (if present) |

### Definition of done (for this directory/README)
- [ ] README path matches front-matter `path`
- [ ] This README does **not** enumerate files unless they exist in-repo (keep it truthful)
- [ ] Utility modules added under `web/src/utils/**` are:
  - [ ] deterministic and testable (minimal side effects),
  - [ ] documented at point-of-use (JSDoc/TSDoc or equivalent),
  - [ ] aligned with API/UI contract expectations,
  - [ ] reviewed for sensitive-location leakage / CARE constraints when applicable.

---

## 🗂️ Directory Layout

### This document
- `path`: `web/src/utils/README.md` (must match front-matter)

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| UI | `web/` | Web UI app + layer registries; consumes API boundary |
| UI source | `web/src/` | React/Map client code + UI state + view logic |
| Utils (this) | `web/src/utils/` | Shared UI helpers; no direct graph access |
| API boundary | `src/server/` | REST/GraphQL services; redaction + contract enforcement |
| API contracts | `src/server/contracts/**` | OpenAPI/GraphQL contracts, schemas, operation IDs |
| Graph | `src/graph/` | Ontology + ingest/migrations; not UI-consumable directly |
| Catalog outputs | `data/stac/**`, `data/catalog/dcat/**`, `data/prov/**` | Evidence artifacts that UI may display through API |
| Story Nodes | `docs/reports/story_nodes/**` | Governed narrative artifacts rendered in UI |
| Schemas | `schemas/**` | STAC/DCAT/PROV/storynodes/UI/telemetry schemas (if present) |

### Expected file tree for this sub-area
This is a **recommended** structure, not an assertion of what exists today:

~~~text
📁 web/
└── 📁 src/
    └── 📁 utils/
        ├── 📄 README.md
        ├── 📁 format/          (recommended: date/number/text formatting)
        ├── 📁 parse/           (recommended: URL/querystring/citation parsing)
        ├── 📁 geo/             (recommended: bbox/center/extent helpers for map focus)
        ├── 📁 contracts/       (recommended: UI-side helpers for working with contract shapes)
        ├── 📁 security/        (recommended: sanitization, safe-link helpers, redaction-safe display)
        └── 📄 index.*          (recommended: exports barrel; extension depends on language/tooling)
~~~

> Keep this tree synced with the repo. If the directory evolves, update the tree and the “what goes where” guidance below.

---

## 🧭 Context

### Where `utils/` sits in the canonical pipeline
Utilities operate in the **UI stage**, downstream of:

- API responses (which already applied redaction rules),
- Story Node Markdown content (validated before publish),
- UI layer registries (schema-validated config, if present).

Utilities must not:
- query Neo4j directly,
- bypass API-level redaction,
- fabricate provenance/citations, or
- convert uncited narrative into “facts.”

### Hard invariants (do not break)
- **UI must consume through contracted APIs** (no direct graph reads).
- **Focus Mode consumes provenance-linked content only**.
- **Predictive/AI content must be opt-in and clearly labeled with uncertainty metadata**.

### What belongs in `utils/` (decision rules)
Put a function here if it is:
- used by multiple components/features, **and**
- small and deterministic (or at least side-effect-minimized), **and**
- not tied to a specific React component lifecycle.

Prefer `utils/` for:
- formatting/parsing,
- contract-shape normalization (UI-side),
- citation parsing + rendering helpers,
- small map-focus computations (center/bbox normalization),
- safe-link/sanitization helpers.

Avoid `utils/` for:
- stateful services with hidden caches,
- “god modules” that accumulate unrelated helpers,
- business logic that belongs to domain packs, server services, or pipelines.

### Conventions
- Keep modules narrow: one concept per file.
- Prefer explicit inputs/outputs (no reliance on global mutable state).
- Treat inbound data as untrusted: validate or defensive-parse.
- Where a utility depends on a contract artifact (schema/OpenAPI), link it in code comments.

---

## 🗺️ Diagrams

### UI boundary and utility role
~~~mermaid
flowchart LR
  A[API Contracts<br/>src/server/contracts/**] --> B[API Boundary<br/>src/server/**]
  C[Story Nodes<br/>docs/reports/story_nodes/**] --> B
  D[Catalog Evidence<br/>data/stac + data/catalog/dcat + data/prov] --> B

  B --> E[Web UI<br/>web/**]
  E --> F[Shared Utils<br/>web/src/utils/**]
  F --> G[Components/Views<br/>web/src/**]
  G --> H[Focus Mode UI]
~~~

### Focus Mode request flow (where utils commonly assist)
~~~mermaid
sequenceDiagram
  participant UI as UI (Focus Mode)
  participant U as utils/*
  participant API as API boundary
  participant Graph as Graph (Neo4j)

  UI->>U: Parse entity ref + focus hints<br/>(center/time/layers)
  UI->>API: GET /focus/{entityId}<br/>(contracted)
  API->>Graph: Fetch subgraph + provenance refs
  Graph-->>API: Context bundle
  API-->>UI: Narrative + citations + audit flags
  UI->>U: Render citations + build UI-safe links
~~~

---

## 🧠 Story Node & Focus Mode Integration

### How this directory supports Focus Mode
Utilities commonly support Focus Mode by providing:

1) **Citation parsing + rendering helpers**
- Story Nodes use inline citation patterns (e.g., `【source†Lx-Ly】` style).
- Utilities may:
  - locate citation tokens,
  - map tokens to a “sources” panel or API-provided source registry,
  - generate safe hyperlinks/popovers.

2) **Focus hints parsing**
Story Node front-matter may include fields like:
- `focus_center` (map center),
- `focus_time` (timeline window),
- `focus_layers` (layer toggles).

Utilities should parse these hints defensively and treat them as **UI suggestions**, not authoritative facts.

3) **Provenance-only content enforcement (UI-side guardrails)**
Even when upstream validation exists, UI utilities should fail safe:
- do not render “facts” without citations when a view claims provenance-linked mode,
- do not show AI/predictive blocks unless explicitly enabled and labeled.

### Practical guidance (utility responsibilities)
- **Do** keep citation parsing isolated and unit-testable.
- **Do** keep link generation safe (no javascript: URLs; sanitize/allowlist).
- **Do** preserve citation text exactly (don’t rewrite references).
- **Do not** generate new citations or infer sources (“no hallucinated sources”).

---

## 🧪 Validation & CI/CD

### Validation steps (expected)
- [ ] Lint/type checks for UI code (repo-defined tooling)
- [ ] Unit tests for non-trivial utilities (especially parsers/formatters)
- [ ] Schema validation for any UI registries consumed (if present)
- [ ] Security/sovereignty scanning gates as required by governance
- [ ] Markdown protocol checks for governed docs (including this README, if included in doc lint scope)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands (not confirmed in repo)
# 1) run UI lint/typecheck
# 2) run UI unit tests
# 3) run schema validation (if UI registries exist)
# 4) run doc lint / markdown protocol validation (if enforced on web/**)
~~~

### Telemetry signals (optional; align with schemas/telemetry if present)
| Signal | Source | Where recorded |
|---|---|---|
| UI render errors (citations/markdown) | client logs | TBD |
| Focus Mode fetch failures | network layer | TBD |
| Sensitive-layer access attempts | UI + API | TBD |

---

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Focus context bundle | JSON | API boundary | Contract tests + runtime validation (recommended) |
| Story Node Markdown | Markdown + front-matter | API or docs export | Story Node schema validation (upstream) |
| Layer registry entries | JSON | `web/**/layers/**` (if present) | UI registry schema (if present) |
| Evidence references | IDs/URIs | API response | Must resolve to STAC/DCAT/PROV identifiers |

### Outputs
| Output | Format | Used by | Contract / Schema |
|---|---|---|---|
| UI-ready view models | JS/TS objects | Components | UI-internal (keep stable within major versions) |
| Citation render model | tokens + refs | Story renderer | Must preserve source IDs and line ranges |
| Map focus model | center/bbox/time | Map + timeline | Must not invent locations |

### Sensitivity & redaction
- Utilities must assume some inputs may be sensitive even if partially redacted.
- Never “reconstruct” restricted locations from partial hints.
- Prefer API-provided generalized geometry over UI-derived precision.

### Quality signals
- Deterministic outputs for deterministic inputs
- Parsing is defensive (no crashes on malformed citations/metadata)
- Stable handling of versioned contract fields (forward-compatible where practical)

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- UI utilities may display or link to STAC **Collection/Item IDs** and assets.
- Treat STAC identifiers as immutable references; do not rewrite IDs.
- If utilities compute derived display (e.g., human-readable titles), keep it presentation-only.

### DCAT
- Utilities may render dataset-level metadata (license, keywords, publisher) if provided.
- Do not guess missing licensing or attribution fields; display “unknown” or omit.

### PROV-O
- Utilities may display provenance chains (activity/agent IDs) when present.
- Do not fabricate lineage. If a PROV reference is missing, treat it as missing and surface it as an audit gap (if the UI supports audit views).

### Versioning
- Prefer contract-driven compatibility:
  - when API versions change, update normalization utilities with explicit mapping,
  - keep backward compatibility within a major UI version where feasible.

---

## 🧱 Architecture

### Components (UI perspective)
| Component | Responsibility | Interface |
|---|---|---|
| Web UI | Render map + narrative | Uses API contracts only |
| Utils (this) | Shared helpers + adapters | Pure functions + small modules |
| Story renderer | Markdown → UI | Uses citation utilities + sanitization |
| Map client | Render layers + focus | Uses map focus utilities + layer registry |

### “Do not break” rules
| Subsystem | “Do not break” rule |
|---|---|
| UI | no hidden data leakage |
| Focus Mode | no hallucinated sources; provenance-linked only |
| Utils | no direct graph access; no secret material; defensive parsing |

### Extension points checklist (when adding new utilities)
- [ ] Utility belongs to a clear category (`format/`, `parse/`, `geo/`, etc.)
- [ ] Unit tests added for parsers and any non-trivial logic
- [ ] Any contract-shape assumptions are documented and linked to a contract artifact
- [ ] Sensitive-data handling reviewed if geometry, locations, or people are involved
- [ ] No new “global singleton” state introduced without justification

---

## ⚖ FAIR+CARE & Governance

### Governance review triggers (examples)
- New utilities that could expose or re-identify sensitive locations
- New external link rendering behaviors (risk of tracking/leakage)
- Any new AI/predictive UI rendering behavior (must be opt-in and labeled)
- Any change that weakens citation/provenance enforcement in Focus Mode

### Security and ethics posture (UI)
- Sanitize/allowlist markdown features where appropriate
- Avoid rendering raw HTML from untrusted sources
- Avoid embedding secrets or internal endpoints in client-side code
- Prefer API-level redaction; UI must not bypass or “undo” redactions

---

## 🕰️ Version History

| Version | Date | Change | Author |
|---|---:|---|---|
| v1.0.0 | 2025-12-25 | Initial README for `web/src/utils/` | TBD |

Footer refs (do not remove):
- `docs/MASTER_GUIDE_v12.md`
- `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` *(draft; if adopted)*
- `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- `src/server/contracts/**` *(API contract artifacts)*
- `schemas/ui/**` *(UI registry schemas; not confirmed in repo)*
