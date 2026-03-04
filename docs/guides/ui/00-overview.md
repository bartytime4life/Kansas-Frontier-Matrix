<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/7cdd1c2f-3c6c-4f69-8e5a-51ed4bf2c1c4
title: UI Guide Overview
type: standard
version: v1
status: draft
owners: [KFM UI Working Group]
created: 2026-03-04
updated: 2026-03-04
policy_label: public
related: [docs/guides/ui/, docs/governance/, contracts/openapi/]
tags: [kfm, ui, map, timeline, story, focus-mode, governance]
notes: [Overview entrypoint for UI docs; defines invariants and navigation]
[/KFM_META_BLOCK_V2] -->

# UI Guide Overview
One-page orientation for KFM’s UI surfaces (Map, Timeline, Story, Focus Mode) and the non-negotiable governance boundaries they must respect.

---

## Impact
**Status:** draft  
**Owners:** KFM UI Working Group (**PROPOSED**)  
**Applies to:** Map Explorer, Timeline, Story, Focus Mode UI clients  
**Last updated:** 2026-03-04

**Badges (TODO):** build · tests · a11y · policy-gate · provenance

---

## Quick navigation
- [Scope](#scope)
- [Where the UI fits](#where-the-ui-fits)
- [UI surfaces](#ui-surfaces)
- [Non-negotiable UI invariants](#non-negotiable-ui-invariants)
- [Evidence-first UX patterns](#evidence-first-ux-patterns)
- [Contracts the UI should depend on](#contracts-the-ui-should-depend-on)
- [Common user flows](#common-user-flows)
- [Testing and CI gates](#testing-and-ci-gates)
- [Security and privacy notes](#security-and-privacy-notes)
- [Next guides to write](#next-guides-to-write)
- [Claims status legend](#claims-status-legend)

---

## Scope
This file is the entrypoint for UI documentation.

**In scope**
- UI surfaces and responsibilities
- Evidence-first UX requirements (citations, provenance, “abstain” behavior)
- Hard boundaries (UI must not bypass governed APIs)
- High-level contracts (what the UI asks for, what it shows)
- Testing expectations for UI correctness and governance compliance

**Out of scope**
- Implementing ingestion pipelines (RAW → WORK → PROCESSED → PUBLISHED)
- Policy authoring details (OPA/Rego specifics)
- Storage layer details (PostGIS/Neo4j/search index schema internals)
- Dataset onboarding procedures and catalog authoring

---

## Where the UI fits
The UI is a **presentation layer**. It renders maps and narratives but **does not** decide what data is allowed, and it **does not** synthesize facts from raw stores.

### Architecture boundary
- **CONFIRMED:** UI clients talk only to a **governed API layer** (policy enforcement point).
- **CONFIRMED:** The governed API orchestrates retrieval from knowledge stores (graph, spatial DB, search).
- **CONFIRMED:** The LLM (Focus Mode) is invoked only by the backend orchestrator; the UI never calls models directly.

~~~mermaid
flowchart LR
  subgraph UI["UI clients"]
    Map["Map Explorer"]
    Time["Timeline"]
    Story["Story Reader"]
    Focus["Focus Mode Chat"]
    ThreeD["3D Story Node Mode"]
  end

  subgraph API["Governed API layer"]
    PEP["Policy Enforcement Point"]
    Retrieve["Retrieval Planner"]
    Evidence["Evidence Resolver"]
    Synthesize["LLM Orchestrator"]
  end

  subgraph Stores["Knowledge stores"]
    PostGIS["Spatial store"]
    Graph["Graph store"]
    Search["Document / Vector index"]
    Catalogs["STAC DCAT PROV catalogs"]
  end

  UI --> PEP
  PEP --> Retrieve
  Retrieve --> PostGIS
  Retrieve --> Graph
  Retrieve --> Search
  Retrieve --> Catalogs
  Retrieve --> Evidence
  Evidence --> Synthesize
  Synthesize --> PEP
~~~

---

## UI surfaces
These are the UI “products” we document. The names may be implemented as routes, tabs, or applications; the responsibilities are what matter.

| Surface | Purpose | Primary interactions | Evidence UX requirement | Status |
|---|---|---|---|---|
| Map Explorer | Browse layers and features spatially | pan/zoom, layer toggle, feature inspect | every displayed fact has a source link or “unknown” | **CONFIRMED** (concept) |
| Timeline | Filter by time, scrub periods, animate change | time slider, date range filter | time claims show explicit dates + citations | **CONFIRMED** (concept) |
| Story | Read narrative nodes tied to evidence | step through nodes, jump to map context | narrative sentences cite EvidenceBundles | **CONFIRMED** (concept) |
| Focus Mode | Ask questions and get cited answers | query, refine, follow-ups | answers must include citations or abstain | **CONFIRMED** (concept) |
| 3D Story Node Mode | Optional 3D context for certain stories | 2D → 3D transition, camera path | 3D overlays still cite evidence | **PROPOSED** (implementation detail) |

---

## Non-negotiable UI invariants
These are “musts.” Violations are bugs, not preferences.

### Trust membrane
- **CONFIRMED:** UI MUST NOT access storage (object stores, PostGIS, Neo4j, indexes) directly.
- **CONFIRMED:** UI MUST NOT call the LLM runtime directly.
- **CONFIRMED:** All reads MUST cross the governed API boundary.

### Fail-closed behavior
- **CONFIRMED:** If the API response cannot be verified (missing citations, policy denies, invalid provenance), the UI MUST:
  - render an **abstain state** (not a “best guess”), and
  - provide a user-actionable reason (e.g., “insufficient evidence” / “restricted by policy”) without leaking sensitive details.

### Evidence visibility
- **CONFIRMED:** Any user-visible claim (map popup fact, story sentence, focus-mode answer) MUST link to:
  - an EvidenceBundle or equivalent evidence object, and
  - dataset/run provenance (run receipt / catalogs) when available.
- **UNKNOWN:** The exact EvidenceBundle schema and UI component(s) are not pinned in this file.
  - Verification step: point this guide at `contracts/openapi` endpoints and/or `packages/evidence` types once available.

### Accessibility
- **PROPOSED:** Target WCAG 2.1 AA minimum for interactive UI (map controls, drawers, dialogs).
  - Verification step: add automated a11y checks in CI (Playwright + axe).

### Observability
- **PROPOSED:** Emit UI telemetry events (PII-free) for:
  - evidence panel opened
  - citation clicked
  - layer enabled/disabled
  - focus query submitted
  - focus answer accepted/abstained
  - provenance drawer opened
  - errors and policy denials (redacted)
  - Verification step: confirm schema path for UI telemetry and add a contract test.

---

## Evidence-first UX patterns
### The “citation drawer” pattern
When a user sees *any* claim, they should be able to open a consistent evidence UI:

- **What the UI shows**
  - Citation list (datasets, documents, assets)
  - Coverage (time range, bbox)
  - Provenance pointers (run receipt, STAC/DCAT/PROV references)
  - Redaction markers (what was withheld)

- **What the UI must not show**
  - Restricted coordinates at disallowed precision
  - Raw secrets, tokens, or internal URLs
  - “Model said so” as a source

### Explicit dates, not relative time
- **CONFIRMED (principle):** Prefer precise dates (YYYY-MM-DD or full timestamp) over “recently / last year / today” in UI labels.
- **PROPOSED:** In the Timeline UI, render both:
  - human readable (“Mar 4, 2026”), and
  - machine (“2026-03-04”) in tooltips for clarity and auditability.

---

## Contracts the UI should depend on
This is a lightweight contract sketch so UI code stays stable while backend evolves.

### UI reads
- **CONFIRMED (concept):**
  - Dataset discovery (catalog browsing)
  - Map layers / features (spatial query)
  - Timeline events (time-bounded query)
  - Story nodes (narrative + evidence)
  - Focus Mode answers (answer + citations + policy outcomes)
  - Provenance (run receipts, attestations, SBOM links)

### DTO sketch
**PROPOSED:** Canonical DTO shapes (actual schemas should be generated from OpenAPI/GraphQL).

~~~ts
// PROPOSED: minimal types that the UI needs to render evidence-first UX.
// Replace with generated types from contracts once available.

export type Citation = {
  label: string;                 // short name shown to users
  kind: "dataset" | "document" | "asset" | "run_receipt";
  ref: string;                   // stable identifier (not a raw bucket path)
  href?: string;                 // API URL to fetch details
};

export type EvidenceBundle = {
  id: string;
  claims: Array<{ text: string; citations: Citation[] }>;
  redactions?: Array<{ reason: string; policy_ref?: string }>;
};

export type FocusAnswer = {
  answer_markdown: string;
  evidence: EvidenceBundle;
  policy: { decision: "allow" | "deny" | "abstain"; reason?: string };
};

export type MapFeaturePopup = {
  title: string;
  properties: Record<string, unknown>;
  evidence: EvidenceBundle;
};
~~~

---

## Common user flows
### Flow A: Map explore → inspect → evidence
~~~mermaid
sequenceDiagram
  participant U as User
  participant UI as UI
  participant API as Governed API
  U->>UI: Click feature
  UI->>API: GET feature + evidence refs
  API-->>UI: Feature + EvidenceBundle (or policy deny)
  alt allow
    UI-->>U: Popup + Evidence drawer
  else deny or abstain
    UI-->>U: Redacted/abstain state + reason
  end
~~~

### Flow B: Focus Mode question → cited answer (or abstain)
~~~mermaid
sequenceDiagram
  participant U as User
  participant UI as Focus UI
  participant API as Governed API
  U->>UI: Ask question
  UI->>API: POST focus ask
  API-->>UI: Answer + citations OR abstain
  alt answer has citations
    UI-->>U: Render answer + citations drawer
  else abstain
    UI-->>U: Abstain UI + next-step guidance
  end
~~~

### Flow C: Story Node → optional 2D to 3D transition
- **PROPOSED:** Use MapLibre for baseline interaction and Cesium for 3D “story moments,” with a controlled handoff.
- **PROPOSED:** The 3D view must still be evidence-first: overlays and callouts link to the same EvidenceBundle UX.

~~~mermaid
sequenceDiagram
  participant U as User
  participant UI2D as 2D Viewer
  participant UI3D as 3D Viewer
  participant API as Governed API
  U->>UI2D: Open story node
  UI2D->>API: GET story node + evidence + camera path
  API-->>UI2D: Story node payload
  UI2D-->>U: Read node, click "View in 3D"
  UI2D->>UI3D: Handoff state (bbox, time, evidence refs)
  UI3D-->>U: 3D scene + evidence drawer
~~~

---

## Testing and CI gates
**PROPOSED** minimum gates for UI PRs (fail-closed):
- Typecheck + lint (no implicit any in contracts)
- Contract tests against API schemas (OpenAPI/GraphQL)
- Unit tests for evidence rendering and policy-deny UI states
- E2E tests:
  - map load
  - layer toggle
  - feature inspect and citation click
  - focus query returns citations or abstains
  - story node renders citations
- Accessibility checks for major surfaces (drawers, dialogs, focus input)

**UNKNOWN:** exact repo commands and CI workflow names.
- Verification step: align with existing monorepo tooling once `apps/ui` and workflows are present.

---

## Security and privacy notes
- **CONFIRMED (principle):** Do not fetch provenance/attestation artifacts directly from untrusted origins in the browser; use a governed server proxy.
- **PROPOSED:** For on-map automation/provenance “badges,” only render:
  - status and timestamp
  - safe links to API endpoints that verify signatures server-side
  - never raw registry URLs unless they are explicitly policy-approved.

---

## Next guides to write
These are suggested follow-on docs under `docs/guides/ui/` (**PROPOSED** list).
- `01-map-explorer.md` — MapLibre layer model, styling, feature inspect UX
- `02-timeline.md` — timeline semantics, time filtering, animation, date handling
- `03-story.md` — story node schema, rendering rules, evidence embedding
- `04-focus-mode.md` — chat UX, citations, abstain patterns, follow-up UX
- `05-3d-story-nodes.md` — Cesium integration, 2D/3D transitions, 3D assets
- `06-ui-telemetry.md` — event taxonomy, privacy rules, dashboards
- `07-accessibility.md` — keyboard map controls, screen reader strategy
- `08-testing.md` — unit/e2e patterns, golden images, contract tests
- `09-component-registry.md` — reusable UI components and design tokens

---

## Claims status legend
KFM docs and guides should label meaningful claims using:

- **CONFIRMED:** backed by an authoritative KFM source (spec, contract, or adopted standard)
- **PROPOSED:** a recommended design not yet ratified or implemented
- **UNKNOWN:** missing evidence; list the smallest step to confirm

---

### Back to top
Back to [Quick navigation](#quick-navigation).
