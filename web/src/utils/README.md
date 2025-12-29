---
title: "KFM Web UI — Utils"
path: "web/src/utils/README.md"
version: "v1.0.1"
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

doc_uuid: "urn:kfm:doc:web:src:utils:readme:v1.0.1"
semantic_document_id: "kfm-web-src-utils-readme-v1.0.1"
event_source_id: "ledger:kfm:doc:web:src:utils:readme:v1.0.1"
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
`web/src/utils/` is the shared **utility layer** for the KFM Web UI. Its job is to keep UI behavior **consistent, testable, and governance-aware** by centralizing:

- small, reusable helper functions (formatting, parsing, defensive validation),
- UI-side “adapter” functions that translate **contract artifacts** (API responses, Story Node Markdown, UI registries) into UI-ready view models,
- safe-by-default helpers for **citation rendering** and **provenance display** (including redaction-aware formatting).

This directory supports the project’s canonical architecture ordering:

**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

Utilities live on the **UI side** of the API boundary and must not “reach across” into server or graph internals.

### Non‑negotiables (UI invariants)
These are project-level invariants expressed in a `utils/`-friendly way:

- **No direct graph/DB access.** UI (and utilities) only consume data through the API boundary.
- **Contract-first consumption.** Utilities may normalize/guard shapes, but must not “invent” fields that aren’t in the API contract.
- **Provenance-first rendering.** In provenance-linked contexts (especially Focus Mode), do not promote uncited narrative into “facts.”
- **Redaction awareness.** Do not reverse/undo generalization. Never attempt to reconstruct sensitive locations from partial hints.
- **Sensitivity metadata preservation.** If inputs carry sensitivity/classification/redaction flags, utilities must preserve them and must not widen access or downgrade classification.
- **No hidden data leakage.** No “Easter eggs,” secret debug panels, or backdoors that expose raw or restricted data.

### Scope

| In Scope | Out of Scope |
|---|---|
| Pure/mostly-pure helpers (string/date/number formatting, parsing, defensive validation) | React components/hooks (belong in `web/src/components/**` or feature folders) |
| UI adapters for contract artifacts (API response normalization, citation parsing, layer registry transforms) | ETL/graph logic (belongs in `src/pipelines/**` / `src/graph/**`) |
| Map/client helpers (bbox/center/extent normalization; projection-safe helpers) | Direct Neo4j access (UI must not query the graph directly) |
| Safe rendering helpers (sanitization, safe-link building, redaction-safe display) | Secrets, keys, internal-only endpoints, or “hidden data leakage” patterns |
| Deterministic utilities with unit tests | Stateful services with hidden caches or network fetching (put in a dedicated data/API layer instead) |

### Audience
- Primary: Web/UI maintainers and contributors
- Secondary: API maintainers (to understand UI contract expectations), narrative curators (Story Node rendering + Focus Mode rules)

### Definitions (link to glossary)
- Link (if present): `docs/glossary.md` *(not confirmed in repo)*
- **Contract artifact**: a machine-validated schema/spec (JSON Schema, OpenAPI, GraphQL SDL, UI registry schema).
- **Evidence artifact**: validated STAC/DCAT/PROV outputs and derived evidence products.
- **Story Node**: provenance-linked narrative Markdown designed to be rendered in the UI.
- **Focus Mode**: immersive UI state that consumes provenance-linked context bundles only.

> If `docs/glossary.md` is missing, treat this as a documentation gap and either (a) add the missing glossary entry, or (b) keep definitions local in the relevant README.

### Key artifacts (what this README aligns to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide v12 (draft) | `docs/MASTER_GUIDE_v12.md` | Docs/Architecture | Canonical pipeline + invariants |
| v13 redesign blueprint (draft; if adopted) | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Architecture | “One canonical home”, contract-first, evidence-first |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Docs/Story | Front-matter + citation rules used in Focus Mode |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs | Base structure used by this README |
| API contract extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | API | Contract changes and versioning expectations |
| API contracts | `src/server/contracts/**` | API | UI consumes contracts through API only |
| UI registry schemas | `schemas/ui/**` | Schemas/UI | Validate layer registry and other UI registries *(if present)* |
| Markdown work protocol | `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` | Docs | *not confirmed in repo* |

### Definition of done (for this directory/README)
- [ ] README path matches front-matter `path`
- [ ] This README does **not** enumerate files unless they exist in-repo (keep it truthful)
- [ ] Guidance is architecture-synced (ETL → Catalog → Graph → API → UI → Story → Focus)
- [ ] Utility modules added under `web/src/utils/**` are:
  - [ ] deterministic and testable (minimal side effects),
  - [ ] defensive against malformed/untrusted inputs,
  - [ ] documented at point-of-use (JSDoc/TSDoc or equivalent),
  - [ ] aligned with API/UI contract expectations,
  - [ ] reviewed for sensitive-location leakage / CARE constraints when applicable.

---

## 🗂️ Directory Layout

### This document
- `path`: `web/src/utils/README.md` *(must match front-matter)*

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| UI root | `web/` | Web UI app; consumes API boundary only |
| UI source | `web/src/` | UI code + state + view logic |
| Utils (this) | `web/src/utils/` | Shared helpers; no direct graph/DB access |
| Map engine (if present) | `web/src/map/engine/` | Map engine + adapters (MapLibre/Cesium, time, layers) |
| Story / Focus Mode (if present) | `web/src/story/focus_mode/` | Focus Mode UI; provenance-only rendering rules |
| API boundary | `src/server/` | REST/GraphQL services; redaction + contract enforcement |
| API contracts | `src/server/contracts/**` | OpenAPI/GraphQL contracts, schemas, operation IDs |
| Graph | `src/graph/` | Ontology + ingest/migrations; not UI-consumable directly |
| Catalog outputs | `data/stac/**`, `data/catalog/dcat/**`, `data/prov/**` | Evidence artifacts (UI displays through API) |
| Story Nodes | `docs/reports/story_nodes/**` | Governed narrative artifacts rendered in UI |
| Schemas | `schemas/**` | STAC/DCAT/PROV/storynodes/UI/telemetry schemas *(if present)* |

### Expected file tree for this sub-area
This is a **recommended** structure (aligned to contract-first + testability); it is not an assertion of what exists today:

~~~text
📁 web/
└── 📁 src/
    └── 📁 utils/
        ├── 📄 README.md
        ├── 📁 format/          (dates/numbers/text; locale/timezone-safe)
        ├── 📁 parse/           (citations, markdown-safe parsing, querystring)
        ├── 📁 geo/             (bbox/center/extent helpers; projection-safe)
        ├── 📁 contracts/       (UI-side normalizers for API contract shapes)
        ├── 📁 security/        (sanitization, safe-link helpers, redaction-safe display)
        ├── 📁 testkit/         (fixtures + helpers for unit tests; optional)
        └── 📄 index.*          (exports barrel; extension depends on language/tooling)
~~~

> Keep this tree synced with the repo. If structure changes, update the tree and the “what goes where” guidance below.

---

## 🧭 Context

### Where `utils/` sits in the canonical pipeline
Utilities operate in the **UI stage**, downstream of:

- API responses (which should already apply redaction and policy rules),
- Story Node Markdown content (validated before publish),
- UI registries (schema-validated config, if present).

Utilities must not:
- query Neo4j directly,
- bypass API-level redaction,
- fabricate provenance/citations, or
- convert uncited narrative into “facts.”

### Hard invariants (do not break)
- **Pipeline ordering is non‑negotiable:** ETL → Catalogs → Graph → API → UI → Story Nodes → Focus Mode
- **API boundary is a hard boundary:** UI never reads Neo4j/DB directly
- **Focus Mode is provenance‑only:** uncited narrative must not appear as fact; AI/predictive content must be opt‑in and labeled with uncertainty metadata
- **Redaction/generalization must survive to the UI:** do not “add precision back” (e.g., by geocoding names or over-zooming restricted layers)

### Boundary & dependency rules (UI)
- Do not import runtime code from `src/server/**`, `src/graph/**`, or `src/pipelines/**` into the UI bundle.
- Do not bypass the API boundary (no direct DB reads; no “secret” internal endpoints in client code).
- Prefer browser-safe dependencies; avoid Node-only APIs (`fs`, `path`, etc.) in `web/src/utils/**`.
- If logic must be shared across subsystems, prefer **schemas/contracts** (and versioned artifacts) over copy-pasted code.

### What belongs in `utils/` (decision rules)
Put a function here if it is:
- used by multiple components/features, **and**
- small and deterministic (or side effects are explicit and unit-testable), **and**
- not tied to a specific React component lifecycle.

Prefer `utils/` for:
- formatting/parsing,
- contract-shape normalization (UI-side),
- citation parsing + rendering helpers,
- small map-focus computations (center/bbox normalization),
- safe-link/sanitization helpers.

Avoid `utils/` for:
- stateful services with implicit caches,
- long-running workers without clear ownership,
- business logic that belongs to domain packs, server services, or pipelines,
- network fetching (keep fetch in an API/data client layer).

### Conventions (recommended)
- One concept per file; avoid “god modules.”
- Prefer explicit inputs/outputs (no global mutable state).
- Treat inbound data as **untrusted**: defensive parse + safe defaults.
- If a utility depends on a contract artifact, link it in the file header comment.
- If a utility touches **locations/people**, include a short comment noting sensitivity assumptions and redaction expectations.

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
  API-->>UI: Narrative + citations + redaction flags + audit metadata
  UI->>U: Render citations + build UI-safe links + enforce UI redaction guards
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
  - generate safe hyperlinks/popovers to the evidence viewer.

**Rules:**
- Preserve citation text exactly (do not rewrite IDs or line ranges).
- Do not generate new citations or infer sources (“no hallucinated sources”).
- Do not fetch raw GitHub links in the browser to “resolve” citations; rely on API-provided evidence viewers/endpoints.

2) **Focus hints parsing (structured story controls)**
Story Node front-matter may include fields like:
- `focus_center` (map center),
- `focus_time` (timeline window),
- `focus_layers` (layer toggles).

Utilities should parse these hints defensively and treat them as **UI suggestions**, not authoritative facts.

Example (optional structured controls):

~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [-98.0000, 38.0000]
~~~

3) **Redaction awareness and “precision control”**
Even when upstream validation exists, utilities should fail safe:
- enforce maximum zoom or geometry generalization for restricted layers (if the API flags it),
- avoid displaying precise coordinates when generalized geometry is intended,
- do not geocode narrative text or entity names to “find” a location (this can re-identify sensitive sites).

4) **Provenance-only enforcement (UI-side guardrails)**
When a view claims provenance-linked mode:
- do not render “facts” without citations (or surface as “uncited / audit gap” if the UI has an audit view),
- do not show AI/predictive blocks unless explicitly enabled and clearly labeled (uncertainty + provenance).

---

## 🧪 Validation & CI/CD

### Validation steps (expected)
Align these checks with repo-defined tooling and the Master Guide’s minimum gates:

- [ ] UI lint + type checks
- [ ] Accessibility checks (a11y) for UI surfaces touched by utilities *(if enforced)*
- [ ] Unit tests for non-trivial utilities (especially parsers/formatters)
- [ ] Schema validation for any UI registries consumed *(if present)*
- [ ] Markdown protocol checks (front-matter + required sections) *(if enforced on `web/**`)*
- [ ] Link/reference checks (no orphan pointers; mark “not confirmed in repo” where appropriate)
- [ ] Security + sovereignty scanning gates as applicable:
  - [ ] secret scan / credential scan
  - [ ] PII scan (if configured)
  - [ ] sensitive-location leakage checks
  - [ ] classification propagation checks (no downgrades without review)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands (not confirmed in repo)

# 1) UI lint/typecheck
# <command>

# 2) UI unit tests
# <command>

# 3) (Optional) validate UI schemas / registries
# <command>

# 4) (Optional) doc lint / markdown protocol validation
# <command>
~~~

### Telemetry signals (optional; align with `schemas/telemetry/**` if present)
| Signal | Source | Where recorded |
|---|---|---|
| `ui_render_error` | client runtime | telemetry pipeline *(if present)* |
| `focus_mode_fetch_failed` | network layer | telemetry pipeline *(if present)* |
| `focus_mode_redaction_notice_shown` | Focus Mode UI | telemetry pipeline *(if present)* |
| `external_link_blocked` | safe-link helper | telemetry pipeline *(if present)* |

---

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Focus context bundle | JSON | API boundary | Contract tests + runtime validation (recommended) |
| Story Node Markdown | Markdown + front-matter | API or docs export | Story Node schema validation (upstream) |
| Layer registry entries | JSON | `web/**/layers/**` *(if present)* | UI registry schema *(if present)* |
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
- Do not fabricate lineage. If a PROV reference is missing, treat it as missing and surface it as an audit gap (if supported).

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
| UI | no hidden data leakage; no direct DB reads |
| Focus Mode | provenance-linked only; no hallucinated/unsourced claims |
| Utils | defensive parsing; no secret material; respect redaction/generalization |

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
- New external link rendering behaviors (tracking/leakage risk)
- New AI/predictive UI rendering behavior (must be opt-in and labeled)
- Any change that weakens citation/provenance enforcement in Focus Mode

### Security and ethics posture (UI)
- Sanitize/allowlist Markdown features where appropriate
- Avoid rendering raw HTML from untrusted sources
- Avoid embedding secrets or internal endpoints in client-side code
- Prefer API-level redaction; UI must not bypass or “undo” redactions

---

## 🕰️ Version History

| Version | Date | Change | Author |
|---|---:|---|---|
| v1.0.0 | 2025-12-25 | Initial README for `web/src/utils/` | TBD |
| v1.0.1 | 2025-12-28 | Clarify UI invariants, redaction-aware utilities, and CI gate alignment | TBD |

---

Footer refs (do not remove):
- `docs/MASTER_GUIDE_v12.md`
- `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` *(draft; if adopted)*
- `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- `src/server/contracts/**` *(API contract artifacts)*
- `schemas/ui/**` *(UI registry schemas; not confirmed in repo)*