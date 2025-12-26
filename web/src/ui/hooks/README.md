---
title: "🪝 KFM Web UI — Hooks"
path: "web/src/ui/hooks/README.md"
version: "v1.0.0"
last_updated: "2025-12-26"
status: "draft"
doc_kind: "Guide"
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
care_label: "CARE Screened (UI code)"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:web:ui:hooks:readme:v1.0.0"
semantic_document_id: "kfm-web-ui-hooks-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:ui:hooks:readme:v1.0.0"
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

<div align="center">

# 🪝 **KFM Web UI — Hooks**
`web/src/ui/hooks/`

_Modular UI logic for KFM’s React + Map UI, designed to respect the API boundary and support map + narrative workflows._

</div>

> **Purpose (required):** Define **conventions and guardrails** for React hooks in `web/src/ui/hooks/`, including:  
> (1) data fetching via **contracted APIs**, (2) map interaction patterns (e.g., MapLibre), and (3) Focus Mode / Story Node behaviors that keep **provenance visible** and avoid leakage of sensitive information.

---

## 📘 Overview

### Purpose

- Provide a shared, reviewable standard for React hooks used across the KFM web UI.
- Keep UI logic modular and testable while enforcing:
  - **No direct graph access from `web/`** (all graph reads go through `src/server/` contracts).
  - Provenance-first behavior for story and focus flows.
- Reduce duplication: common patterns (abort/cancel, caching, error states, map events) should be centralized.

### Scope

| In Scope | Out of Scope |
|---|---|
| Reusable React hooks under `web/src/ui/hooks/` | Implementing server endpoints / graph queries (`src/server/`, `src/graph/`) |
| Patterns for safe async requests (cancelation, stale data protection) | ETL, STAC/DCAT/PROV generation (`src/pipelines/`, `data/`) |
| Map UI integration hooks (e.g., MapLibre lifecycle, layer toggles) | Styling/UI components (unless a hook is required for shared logic) |
| Focus Mode / Story Node orchestration hooks | Story Node authoring content (`docs/reports/story_nodes/`) |

### Audience

- Primary: Frontend engineers working in `web/`.
- Secondary: API engineers reviewing UI consumption patterns; governance reviewers for anything that changes data exposure in UI.

### Definitions

- **Hook:** A React function named `useX…` encapsulating reusable state + effects.
- **API boundary:** UI reads data only through API contracts; no direct Neo4j/graph reads.
- **Provenance refs:** Identifiers/links returned by API that map UI-visible claims back to STAC/DCAT/PROV artifacts.
- **Focus Mode:** A deep-dive UI state/view that emphasizes one entity/story with provenance-linked content.

> Glossary reference: `docs/glossary.md` (not confirmed in repo — if absent, add or update the correct glossary location per Master Guide).

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This README | `web/src/ui/hooks/README.md` | UI | Conventions + patterns |
| Master Guide | `docs/MASTER_GUIDE_v12.md` | Platform | Canonical pipeline + invariants |
| API contracts | `src/server/contracts/**` (or legacy; not confirmed in repo) | API | UI must follow contracts |
| Governance | `docs/governance/ROOT_GOVERNANCE.md` | Governance | Review gates + sensitivity posture |

### Definition of done

- [ ] Front-matter complete + valid (`path` matches file location)
- [ ] Hooks described here match actual directory structure (no stale examples)
- [ ] Constraints/invariants explicitly stated (API boundary, provenance visibility)
- [ ] Validation steps listed and repeatable
- [ ] Governance considerations included (redaction, sovereignty, logging)

---

## 🗂️ Directory Layout

### This document

- `path`: `web/src/ui/hooks/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Frontend root | `web/` | React + map clients |
| Hooks | `web/src/ui/hooks/` | Reusable UI hooks (this directory) |
| UI components | `web/src/ui/components/` (not confirmed in repo) | Presentational + composed UI |
| UI state | `web/src/ui/state/` (not confirmed in repo) | Shared state container / reducers |
| API layer | `src/server/` | Contracted API boundary to graph/data |
| Schemas | `schemas/` | JSON schemas (contracts, telemetry, etc.) |
| Governance docs | `docs/governance/` | Governance/ethics/sovereignty references |

### Expected file tree for this sub-area

> Update this tree to match the real directory whenever hooks are added/removed.

~~~text
📁 web/
└── 📁 src/
    └── 📁 ui/
        └── 📁 hooks/
            ├── 📄 README.md
            ├── 📄 index.ts                       (optional; barrel exports)
            ├── 📄 useFocusContext.ts             (example; update to match repo)
            ├── 📄 useStoryNodes.ts               (example; update to match repo)
            ├── 📄 useMapInstance.ts              (example; update to match repo)
            └── 📁 __tests__/                     (optional; update to match repo)
                └── 📄 useFocusContext.test.tsx   (example; update to match repo)
~~~

---

## 🧭 Context

### Background

KFM’s frontend is a React SPA that integrates mapping (e.g., MapLibre GL) and narrative exploration (Story Nodes + Focus Mode). Hooks are the primary mechanism to:

- Keep map and narrative state synchronized.
- Encapsulate data fetching behind API contracts.
- Enforce consistent patterns for provenance display, error handling, and redaction-safe behavior.

### Assumptions

- This UI is React-based and uses a mapping library (e.g., MapLibre GL JS).
- The UI does not query Neo4j directly; it calls APIs that enforce governance and provenance rules.
- Data returned from APIs may include provenance references and sensitivity flags, which must be surfaced or honored in UI.

### Constraints and invariants

- Preserve the canonical pipeline ordering: **ETL → catalogs → graph → APIs → UI → Story Nodes → Focus Mode**.
- **No UI direct-to-graph reads:** `web/` must never query Neo4j directly.
- Hooks must not fabricate facts or citations; they only render/transform what the API contract returns.
- Sensitive content handling:
  - If a response indicates redaction/generalization, hooks must not “reconstruct” hidden details.
  - Never log raw sensitive payloads or exact coordinates when sensitivity is non-public.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| What is the standard data-fetch layer (native `fetch`, GraphQL client, React Query/SWR, etc.)? | TBD | TBD |
| Where is the canonical API client module located under `web/`? | TBD | TBD |
| What is the standard telemetry event schema for UI interactions? | TBD | TBD |

### Future extensions

- A standardized “Focus bundle” hook that returns:
  - core entity data,
  - map extents/layers,
  - provenance refs,
  - sensitivity flags,
  - uncertainty/confidence metadata (when enabled).
- A unified caching policy for map-driven queries (viewport/time filters) that remains deterministic and testable.

---

## 🗺️ Diagrams

### System and dataflow

~~~mermaid
flowchart LR
  ETL["ETL (src/pipelines)"] --> CAT["STAC/DCAT/PROV (data/stac + data/catalog/dcat + data/prov)"]
  CAT --> GR["Graph (Neo4j)"]
  GR --> API["API boundary (src/server)"]
  API --> UI["React/Map UI (web/)"]
  UI --> SN["Story Nodes (docs/reports/story_nodes)"]
  SN --> FM["Focus Mode"]
~~~

### Hook-centric sequence

~~~mermaid
sequenceDiagram
  participant C as Component
  participant H as Hook (web/src/ui/hooks)
  participant A as API Client (web/)
  participant S as Server (src/server)
  participant G as Graph (Neo4j)

  C->>H: select entityId + timeRange + viewport
  H->>A: request focus bundle (contracted)
  A->>S: HTTP/GraphQL request
  S->>G: query + provenance refs + redaction rules
  G-->>S: result set
  S-->>A: payload (data + provenance + sensitivity)
  A-->>H: JSON
  H-->>C: { loading, error, data, provenanceRefs }
~~~

---

## 🧠 Story Node & Focus Mode Integration

Hooks that power Story Node markers, story panels, and Focus Mode should:

- Prefer APIs that return **provenance-linked** content (dataset IDs, document IDs, citations).
- Treat provenance references as **first-class UI data**:
  - expose them to components so they can render “Sources” / “Evidence” affordances,
  - do not strip them in mapping-to-view-model steps.
- Respect Focus Mode rules:
  - display only provenance-backed content by default,
  - clearly label any AI-generated/predicted content and keep it **opt-in**,
  - propagate uncertainty/confidence metadata when present.
- Keep map and narrative in sync:
  - Focus selection updates viewport/time filters,
  - map click selection updates focus entity (if supported).

---

## 🧪 Validation & CI/CD

### Validation steps (recommended)

- Typecheck passes for hooks and their consumers (TS build).
- Lint passes (React hooks rules, unused deps, etc.) if configured.
- Unit tests exist for hooks that contain non-trivial logic (mock API client, verify cancelation behavior).
- No direct graph/Neo4j usage from `web/` (review + automated grep rule if available).

### Review checklist for new hooks

- [ ] Name starts with `use…`
- [ ] Single responsibility
- [ ] Cancelation/stale-data protection for async work
- [ ] Errors are surfaced as typed states (not thrown in render)
- [ ] Provenance refs preserved (if returned)
- [ ] Sensitivity/redaction respected
- [ ] Tests added for non-trivial behavior

---

## 📦 Data & Metadata

### Inputs

| Input | Source | Notes |
|---|---|---|
| User interactions | UI events | clicks, hover, selection, timeline changes |
| Map events | MapLibre instance (or wrapper) | zoom, move, layer toggle |
| API responses | `src/server` contracts | may include provenance + sensitivity flags |
| UI config | layer registry JSON (not confirmed in repo path) | used to define layers, attribution, sensitivity |

### Outputs

| Output | Where | Notes |
|---|---|---|
| View models | Hook return values | `{data, loading, error, provenanceRefs}` patterns |
| Map state | Component props / state | viewport, active layers, selection |
| Telemetry events | telemetry subsystem (if present) | must align with schemas; avoid sensitive logs |

---

## 🌐 STAC, DCAT & PROV Alignment

Hooks generally do **not** create STAC/DCAT/PROV artifacts. However, hooks must support KFM’s evidence-first posture by:

- Passing through provenance references returned by APIs (do not “simplify away” evidence fields).
- Rendering dataset/document identifiers in UI as clickable/inspectable metadata where supported.
- Avoiding inference:
  - do not guess dataset IDs,
  - do not synthesize citations client-side.

If an API payload contains links/IDs referencing:
- STAC Items/Collections
- DCAT dataset/distributions
- PROV activities/runs

…hooks must preserve these fields and make them available to components.

---

## 🧱 Architecture

### Hook categories

> Use categories as a mental model; actual file names and grouping should match the repo.

- **Data hooks:** contract-first fetch, caching, pagination, abort/cancel patterns.
- **Map hooks:** map lifecycle, event subscriptions, layer visibility, feature selection.
- **Narrative hooks:** story node lists, focus entity bundle, citations/provenance display logic.
- **Utility hooks:** debounced values, media queries, reduced-motion preferences.

### Design rules

- **API boundary first:** hooks fetch only via the UI’s API client layer (location not confirmed in repo).
- **Abort/cancel by default:** any hook that fetches must handle:
  - abort on unmount,
  - abort on param changes,
  - stale result suppression.
- **Deterministic behavior:** given the same inputs, hooks should behave predictably (avoid hidden global state).
- **Minimal side effects:** map event listeners, telemetry emits, and network calls must be explicit and cleaned up.

### Example hook skeleton

~~~ts
import { useEffect, useMemo, useState } from "react";

type UseFocusBundleParams = {
  entityId: string | null;
  timeRange: { start: string; end: string } | null;
};

type FocusBundle = {
  entity: unknown;
  narrative: unknown;
  provenanceRefs: Array<{ id: string; kind: string }>;
  sensitivity?: { classification: "open" | "restricted" | "redacted"; notes?: string };
};

type UseFocusBundleState =
  | { status: "idle"; data: null; error: null }
  | { status: "loading"; data: null; error: null }
  | { status: "error"; data: null; error: Error }
  | { status: "success"; data: FocusBundle; error: null };

export function useFocusBundle(params: UseFocusBundleParams): UseFocusBundleState {
  const [state, setState] = useState<UseFocusBundleState>({ status: "idle", data: null, error: null });

  const requestKey = useMemo(() => {
    if (!params.entityId || !params.timeRange) return null;
    return `${params.entityId}:${params.timeRange.start}:${params.timeRange.end}`;
  }, [params.entityId, params.timeRange]);

  useEffect(() => {
    if (!requestKey) {
      setState({ status: "idle", data: null, error: null });
      return;
    }

    const controller = new AbortController();
    setState({ status: "loading", data: null, error: null });

    // NOTE: Replace with the repo’s canonical API client + contract type (not confirmed in repo).
    fetch(`/api/focus?key=${encodeURIComponent(requestKey)}`, { signal: controller.signal })
      .then(async (r) => {
        if (!r.ok) throw new Error(`Focus bundle request failed: ${r.status}`);
        return (await r.json()) as FocusBundle;
      })
      .then((data) => setState({ status: "success", data, error: null }))
      .catch((err) => {
        if (controller.signal.aborted) return;
        setState({ status: "error", data: null, error: err instanceof Error ? err : new Error("Unknown error") });
      });

    return () => controller.abort();
  }, [requestKey]);

  return state;
}
~~~

### Hook inventory

> Keep this table updated as hooks are added.

| Hook | Responsibility | Side effects | API contract used | Tests |
|---|---|---|---|---|
| `useFocusBundle` (example) | Fetch + normalize focus payload | network | TBD | TBD |

---

## ⚖ FAIR+CARE & Governance

### Review gates

Changes to hooks require governance review when they:

- introduce new data surfaces in UI (new fields rendered, new endpoints called),
- change how sensitivity/redaction is displayed or enforced,
- add telemetry that could record sensitive content,
- enable AI-generated/predicted content in Focus Mode without clear opt-in + uncertainty.

### CARE and sovereignty considerations

- Treat culturally sensitive knowledge and restricted locations as high-risk.
- If the API indicates generalized/redacted geometry or narrative, do not attempt to reconstruct or “approximate” it client-side.
- Prefer safe defaults:
  - do not log raw payloads,
  - do not persist sensitive values in localStorage/sessionStorage unless explicitly governed.

### AI usage constraints

- This document permits: summarization/structure extraction/translation/keyword indexing.
- This document prohibits: generating policy, inferring sensitive locations.
- Hooks that surface any AI-derived content must:
  - clearly label it,
  - expose uncertainty/confidence when provided,
  - default to off unless explicitly enabled by the product spec.

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-26 | Initial hooks README establishing conventions and invariants | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Universal template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`

