---
title: "KFM Web Map Hooks — README"
path: "web/src/map/hooks/README.md"
version: "v1.0.0"
last_updated: "2025-12-25"
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
care_label: "TBD"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:web:map:hooks:readme:v1.0.0"
semantic_document_id: "kfm-web-map-hooks-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:map:hooks:readme:v1.0.0"
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

# KFM Web Map Hooks — README

## 📘 Overview

### Purpose
- Define conventions and responsibilities for React hooks in `web/src/map/hooks/`.
- Keep map behavior consistent with KFM architecture invariants: **API boundary**, **provenance-first Focus Mode**, and **no hidden data leakage**.

### Scope
| In Scope | Out of Scope |
|---|---|
| Hook patterns for map lifecycle, event wiring, layer/source management, selection, and UI state synchronization | Implementing specific endpoints, graph queries, or ETL logic |
| Focus Mode “controls → map state” integration points (center/time/layers) | Story authoring guidelines (see Story Node template) |
| Test + validation expectations for hooks (cleanup, determinism, schema checks) | Picking a specific toolchain if the repo already has one (**not confirmed in repo**) |

### Audience
- **Primary:** Frontend contributors working in `web/`.
- **Secondary:** Reviewers validating UI contract rules (layer registry, a11y, audit affordances, redaction).

### Definitions
- Link: `docs/glossary.md` (**not confirmed in repo** — create if missing)
- Terms used in this doc include: **MapLibre**, **hook**, **layer registry**, **Focus Mode**, **Story Node**, **provenance**, **redaction**, **audit affordances**.

### Key artifacts
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master pipeline ordering + invariants | `docs/MASTER_GUIDE_v12.md` | KFM Core | Canonical pipeline + invariants |
| Universal governed doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | KFM Core | Template used for this README |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | KFM Core | Defines optional Focus Mode controls |
| v13 redesign blueprint | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | KFM Core | Use if adopted (**not confirmed in repo**) |
| API contracts | `src/server/contracts/**` | API Eng | Contract-first boundary (**not confirmed in repo**) |
| UI registry schemas | `schemas/ui/**` | Frontend/Platform | Layer registry schema validation (**not confirmed in repo**) |

### Definition of done
- [ ] Front-matter complete + valid
- [ ] Hook responsibilities and boundaries are explicit
- [ ] Architecture invariants are stated (API boundary, provenance-first Focus Mode, no hidden data leakage)
- [ ] Validation steps are listed and repeatable (or clearly marked **not confirmed in repo**)
- [ ] Governance + CARE/sovereignty constraints are explicitly stated

## 🗂️ Directory Layout

### This document
- `path`: `web/src/map/hooks/README.md` (must match front-matter)

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Frontend | `web/` | React UI, map clients, Focus Mode UI |
| Map module | `web/src/map/` | Map components, contexts, engine adapters (**not confirmed in repo**) |
| Map hooks | `web/src/map/hooks/` | Hooks that wrap map-engine imperative APIs and UI state sync |
| Layer registry | `web/**/layers/**` | Layer registry/config(s) consumed by UI (**not confirmed in repo**) |
| UI schemas | `schemas/ui/` | Layer registry schemas validated in CI (**not confirmed in repo**) |
| API boundary | `src/server/` | Contracted endpoints + redaction/generalization (**not confirmed in repo**) |

### Expected file tree for this sub-area
> This is the **recommended** structure. Some files may not exist yet (**not confirmed in repo**).

~~~text
📁 web/
└── 📁 src/
    └── 📁 map/
        └── 📁 hooks/
            ├── 📄 README.md
            ├── 📄 index.ts                    # barrel exports (recommended; not confirmed)
            ├── 📄 useMapInstance.ts           # create/own map instance (example; not confirmed)
            ├── 📄 useMapEvent.ts              # subscribe/unsubscribe helpers (example; not confirmed)
            ├── 📄 useLayerRegistry.ts         # resolve layer definitions (example; not confirmed)
            ├── 📄 useLayerLifecycle.ts        # add/update/remove sources & layers (example; not confirmed)
            ├── 📄 useViewportSync.ts          # URL/app state ↔ camera (example; not confirmed)
            ├── 📄 useSelectionSync.ts         # click/hover selection ↔ app state (example; not confirmed)
            └── 📄 useFocusModeMapSync.ts      # Focus Mode controls → map state (example; not confirmed)
~~~

## 🧭 Context

### Background
KFM’s UI sits downstream of the pipeline and must preserve the canonical flow:

**ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.

This directory exists to make map behavior predictable and reviewable by:
- Centralizing map-engine imperative calls behind React-safe hooks.
- Enforcing the **API boundary** (no direct graph access).
- Supporting Focus Mode requirements (provenance-linked context only).
- Preventing “hidden data leakage” through interaction patterns (layer toggles, zoom, hover, tooltips).

### Assumptions
- The map UI is React-based and uses a MapLibre-style map engine (exact engine/package **not confirmed in repo**).
- Layer configuration exists as a “registry” that can be schema-validated (exact location **not confirmed in repo**).
- Focus Mode is implemented as a UI view that consumes Story Nodes and API-provided context bundles.

### Constraints and invariants
- **API boundary:** hooks in `web/` must not connect to Neo4j or import server/graph drivers.
- **UI contract:** layer registry + a11y + audit affordances; **no hidden data leakage**.
- **Provenance-first:** map interactions that surface facts should carry dataset/evidence identifiers through selection state so the UI can render audit/citation affordances.
- **Deterministic behavior:** avoid random IDs and time-dependent behavior unless explicitly required and tested.
- **Clean lifecycles:** all event listeners, timers, and subscriptions must be cleaned up on unmount and on dependency changes.

## 🗺️ Diagrams

### Where map hooks sit in the system
~~~mermaid
flowchart LR

  subgraph Data["Data products"]
    STAC["STAC/DCAT/PROV"]
    GRAPH["Graph (Neo4j)"]
  end

  subgraph API["API boundary (src/server/)"]
    CONTRACTS["Contracts + redaction + provenance mediation"]
  end

  subgraph UI["UI (web/)"]
    MAP["Map UI (React/MapLibre)"]
    HOOKS["Map hooks (web/src/map/hooks)"]
    REG["Layer registry (web/**/layers/**)"]
    MAP --> HOOKS
    HOOKS --> REG
  end

  STAC --> GRAPH
  GRAPH --> CONTRACTS
  CONTRACTS --> HOOKS
~~~

## 🧠 Story Node & Focus Mode Integration

### Focus Mode rule
Focus Mode consumes **provenance-linked** content only. Any predictive/AI-generated content must be opt-in and clearly labeled with uncertainty metadata (handled at the API/Story layer, not by hooks).

### Optional structured controls from Story Nodes
Story Nodes may provide optional controls that the UI can treat as “suggested map state”:

~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

Hook responsibilities related to these controls:
- Apply **focus_center** to the map camera in a bounded way (respect min/max zoom; avoid revealing sensitive detail).
- Apply **focus_time** to timeline/temporal filters (through app state, not direct data fetch logic embedded in the hook).
- Apply **focus_layers** by toggling layers that exist in the UI layer registry (and that are allowed by access rules).

### Evidence and audit affordances
When a Focus Mode action results in map changes (layers on/off, filtered features), hooks should preserve enough identifiers in state so UI panels can show:
- “what am I looking at?” (layer metadata),
- “where did it come from?” (dataset/evidence IDs),
- “what was redacted/generalized?” (redaction notice flags, if supplied by the API).

## 🧱 Architecture

### What belongs in `web/src/map/hooks/`
Hooks in this directory should be **map-centric** and reusable across domains:
- Map instance lifecycle (create once, expose stable ref)
- Event wiring with cleanup (click, hover, move, zoom, style load)
- Layer/source lifecycle helpers (add/update/remove in response to app state)
- Synchronization between map state and app state (URL, store, Focus Mode state)
- Selection/hover helpers that produce stable, provenance-carrying selection objects

If a hook is **domain-specific** (e.g., “treaty polygons styling rules”), consider placing it under a domain-owned UI module and keeping this directory for engine- and UI-infrastructure hooks (**domain module paths not confirmed in repo**).

### Recommended responsibilities and anti-patterns
| Concern | Do | Avoid |
|---|---|---|
| Map instance ownership | Create the map once; store it in a ref; expose a stable API | Recreating map instances on every render |
| Events | Register/unregister listeners inside `useEffect` with strict cleanup | Attaching listeners without cleanup (memory leaks) |
| Layers/sources | Derive layer state from registry + app state; perform idempotent add/update/remove | Hardcoding domain facts in generic hooks |
| Data access | Use contracted API clients outside the hook or behind a clearly bounded interface | Fetching directly from graph/DB; bypassing API redaction |
| Selection | Return stable selection objects that include IDs/evidence refs | Returning raw engine objects or dropping provenance |
| Performance | Throttle high-frequency callbacks; avoid setState storms | Triggering heavy work on every mousemove/zoom frame |

### Minimal hook patterns

#### Event subscription with cleanup
~~~tsx
// Pseudocode — adjust to actual hook names and map engine types (not confirmed in repo)
import { useEffect } from "react";

export function useMapEvent(map: unknown, event: string, handler: (...args: any[]) => void) {
  useEffect(() => {
    if (!map) return;

    // map.on(event, handler)
    // return () => map.off(event, handler)

    return () => {
      // cleanup
    };
  }, [map, event, handler]);
}
~~~

#### Focus Mode controls → map state
~~~tsx
// Pseudocode — map state application should be bounded and testable (not confirmed in repo)
type FocusControls = {
  focus_center?: [number, number];
  focus_time?: string;
  focus_layers?: string[];
};

export function useFocusModeMapSync(map: unknown, controls: FocusControls) {
  // 1) validate/normalize controls
  // 2) apply camera changes (center/zoom constraints)
  // 3) toggle layers via registry-resolved IDs
  // 4) update app state for focus_time (do not embed fetch logic here)
}
~~~

### Hook index
> Keep this table updated as hooks are added/removed. If a hook is internal-only, do not list it here.

| Hook | Responsibility | Inputs | Outputs | Side effects | Notes |
|---|---|---|---|---|---|
| TBD | TBD | TBD | TBD | TBD | Update as hooks stabilize |

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks (front-matter, required sections)
- [ ] Web typecheck + lint (tooling **not confirmed in repo**)
- [ ] Unit tests for hook behavior (cleanup, idempotence, determinism)
- [ ] UI schema checks when the layer registry changes (**not confirmed in repo**)
- [ ] Security and sovereignty scanning (no secrets; no sensitive-coordinate leakage)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands (not confirmed in repo)

# 1) typecheck / lint
# npm run lint
# npm run typecheck

# 2) run hook tests
# npm test

# 3) validate UI registry schema (if applicable)
# python tools/validate_ui_registry.py web/**/layers/** schemas/ui/**
~~~

### Telemetry signals
If map interaction telemetry is implemented, keep signals schema-versioned and documented (locations **not confirmed in repo**):
- `ui.map.layer_toggled`
- `ui.map.feature_selected`
- `ui.focus_mode.applied_controls`

## ⚖ FAIR+CARE & Governance

### Review gates
Escalate for elevated review when changes include:
- Adding a new UI layer or interaction pattern that could reveal sensitive locations by zoom/hover/filter.
- Adding new external map services (tiles, geocoders) that could leak user queries/coordinates.
- Adding any AI-driven narrative behavior in the UI (must remain provenance-linked and clearly labeled).

### CARE and sovereignty considerations
- Follow `docs/governance/SOVEREIGNTY.md` for any data tied to sovereignty-controlled knowledge or culturally sensitive locations.
- Prefer coarse/aggregate public products when appropriate.
- Never attempt to reconstruct or infer restricted locations from redacted/generalized outputs.

### AI usage constraints
- Allowed: summarization, structure extraction, translation, keyword indexing.
- Prohibited: generating new policy, inferring sensitive locations (directly or indirectly).

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-25 | Initial README for map hook conventions | TBD |

---

Footer refs:
- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Universal template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Ethics: `docs/governance/ETHICS.md`

