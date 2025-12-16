---
title: "🧠 Kansas Frontier Matrix — Web Context System Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/context/README.md"
version: "v11.2.6"
last_updated: "2025-12-16"

release_stage: "Stable / Governed"
status: "Active / Enforced"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.6/manifest.zip"
telemetry_ref: "../../../releases/v11.2.6/web-context-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/web-context-readme-v2.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"
signature_ref: "../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../releases/v11.2.6/slsa-attestation.json"

governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

doc_kind: "Overview"
intent: "web-context-overview"
role: "overview"
category: "Web · Source · State Layer"

fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk (logic-only)"
sensitivity_level: "None"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "SoftwareSourceCode"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"

json_schema_ref: "../../../schemas/json/web-context-readme-v11.schema.json"
shape_schema_ref: "../../../schemas/shacl/web-context-readme-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:web-context-readme-v11.2.6"
semantic_document_id: "kfm-doc-web-context-readme-v11"
event_source_id: "ledger:web/src/context/README.md"
immutability_status: "version-pinned"

provenance_chain:
  - "web/src/context/README.md@v11.2.2"
  - "web/src/context/README.md@v10.4.0"
  - "web/src/context/README.md@v10.3.2"
  - "web/src/context/README.md@v10.3.1"

fencing_profile: "outer-backticks-inner-tildes-v1"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "summary"
  - "speculative-additions"
  - "unverified-historical-claims"
  - "governance-override"
  - "content-alteration"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "United States / Kansas"
classification: "Public Document"

ttl_policy: "Review each release"
sunset_policy: "Superseded upon next state-layer overhaul"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "🧭 Context"
    - "🗺️ Diagrams"
    - "🧠 Story Node & Focus Mode Integration"
    - "🧪 Validation & CI/CD"
    - "📦 Data & Metadata"
    - "🌐 STAC, DCAT & PROV Alignment"
    - "🧱 Architecture"
    - "⚖ FAIR+CARE & Governance"
    - "🕰️ Version History"
---

<div align="center">

# 🧠 **Kansas Frontier Matrix — Web Context System Overview**  
`web/src/context/README.md`

**Purpose**  
Define the governed, deterministic contract for the **React Context state layer** in the Kansas Frontier Matrix (KFM) Web Platform (`web/src/context/**`).  
Contexts coordinate **time**, **space**, **focus**, **governance**, **accessibility**, **theme**, and **UI shell** state—while keeping the frontend behind approved APIs and preventing unsafe disclosure of governed data.

[![Web Source Overview](https://img.shields.io/badge/web%2Fsrc-README-blue)](../README.md)
· [![Web Source Architecture](https://img.shields.io/badge/web%2Fsrc-ARCHITECTURE-blueviolet)](../ARCHITECTURE.md)
· [![KFM‑MDP v11.2.6](https://img.shields.io/badge/KFM--MDP-v11.2.6-purple)](../../../docs/standards/kfm_markdown_protocol_v11.2.6.md)
· [![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Governance%20Aligned-orange)](../../../docs/standards/faircare/FAIRCARE-GUIDE.md)
· [![Governance](https://img.shields.io/badge/Governance-ROOT--GOVERNANCE-brightgreen)](../../../docs/standards/governance/ROOT-GOVERNANCE.md)
· [![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../LICENSE)

</div>

---

## 📘 Overview

`web/src/context/**` is the **global state backbone** for the web client. It exists to make the UI:

- **Deterministic** (repeatable state transitions; predictable cross-feature sync)
- **Governable** (CARE/sovereignty/masking status is carried as explicit state—not inferred)
- **Accessible** (user A11y preferences propagate consistently and immediately)
- **Composable** (map, timeline, story, focus, and explorer features can coordinate without ad-hoc wiring)
- **Safe by design** (no “direct graph access,” no bypassing API governance, no accidental exposure of sensitive geometries)

### What contexts are for

Contexts are responsible for:

- Storing **small, shared, app-wide state** (time window, active focus, map camera, panel visibility)
- Exposing **typed, bounded update surfaces** (reducers/actions or equivalent)
- Coordinating synchronization between major UI subsystems:
  - Timeline ↔ Map (2D/3D)
  - Story Node selection ↔ Time focus ↔ Map highlight
  - Focus selection ↔ narrative panes ↔ provenance/governance overlays
  - Theme/A11y ↔ design system tokens ↔ reduced-motion behavior

### What contexts are not for

Contexts MUST NOT:

- Perform network calls (REST/GraphQL/STAC/DCAT). Those belong in `services/**`, `hooks/**`, and/or `pipelines/**`.
- Store large data payloads (full Story Node bodies, large feature collections, imagery tiles).
- Store or recompute authoritative governance decisions. The backend remains the source of truth; the frontend may be stricter, never looser.

---

## 🗂️ Directory Layout

~~~text
📁 web/
└── 📁 src/
    └── 📁 context/
        ├── 📄 README.md                 — This document (state-layer overview + contracts)
        ├── 📄 TimeContext.tsx           — Global temporal window + granularity + fuzzy ranges
        ├── 📄 FocusContext.tsx          — Active focus target + selection + narrative handles
        ├── 📄 GovernanceContext.tsx     — CARE/sovereignty flags + masking + required notices
        ├── 📄 MapContext.tsx            — MapLibre/Cesium camera + layer visibility + selection IDs
        ├── 📄 ThemeContext.tsx          — Theme selection (token-backed light/dark/high-contrast)
        ├── 📄 A11yContext.tsx           — Reduced motion + large text + keyboard/SR preferences
        └── 📄 UIContext.tsx             — Shell state (panes, drawers, modals, focus management)
~~~

---

## 🧭 Context

### Implementation contract (applies to every context)

Each context module SHOULD present a consistent surface:

- `XxxContext` (React context)
- `XxxProvider` (provider component)
- `useXxx()` (hook for consuming context safely)
- Typed `State` and `Action` (or `State` and bounded setters)
- Reducer/action transitions that are:
  - deterministic
  - serializable (where practical)
  - testable without rendering

#### Shared non-negotiables

- **No network I/O** inside context modules.
- **No raw governed geometries** inside context state.
  - Storing a *map camera viewport* is allowed.
  - Storing *dataset feature geometry* or *precise sensitive coordinates* is not allowed.
- **No secret-bearing values** (tokens, credentials), and no obvious PII.
- **No “hidden global mutation”** (no module-level mutable singletons controlling app state).

---

### ⏱️ TimeContext

**Role**  
Canonical controller for temporal state: the active time window, granularity, and uncertainty-safe ranges.

**Owns (typical state, names may vary)**

- Active interval(s) for filtering: `start`, `end` (or multi-range brushes)
- Granularity (year / decade / century / “deep time bands”)
- “Fuzzy time” descriptors (approximation flags, original labels)
- Timeline interaction state (brush handles, pinned instants, hover window)

**Hard invariants**

- `start <= end` (or valid ordered bounds for multi-range models)
- Uncertain dates are preserved as **ranges + labels**, never silently coerced to precise instants
- Time is stored in a form that can be mapped to OWL-Time-friendly representations

**Cross-context interactions**

- Timeline updates TimeContext → downstream filters update MapContext-visible layers, Story lists, dataset explorers
- Story Node selection may propose a time window update (TimeContext remains the canonical store)

**Persistence policy**

- Optional: persist user “default time band” preference locally
- Never persist sensitive content-derived time claims as if they were facts (store user UI preference only)

---

### 🎯 FocusContext

**Role**  
Canonical “what am I looking at?” state: current focus target, active selection mode, and focus-driven UI coordination.

**Owns (typical state, names may vary)**

- `focusTarget`: `{ id, type }` where `type` is constrained (Place / Event / Person / Dataset / StoryNode / etc.)
- `activeStoryNodeId` (when focus is driven by a Story Node)
- Focus UI mode: panel state, tab selection, expand/collapse
- Highlight handles (IDs), not geometries: related entity IDs, dataset IDs, layer keys

**Hard invariants**

- FocusContext stores **identifiers and handles**, not raw governed payloads
- Any narrative content stored locally must be treated as:
  - UI-cached, non-authoritative display data, and
  - labeled/segmented by origin (archival vs derived vs AI-generated)
- Must carry or reference governance metadata required to render disclaimers safely (via GovernanceContext or embedded minimal flags)

**Cross-context interactions**

- Setting focus may:
  - request a map highlight (via IDs into MapContext)
  - request a time window alignment (via TimeContext)
  - activate governance notices (via GovernanceContext)

**Persistence policy**

- Do not persist Focus targets by default (prevents “sticky” focus on sensitive topics across sessions)
- If share-links exist, share only safe identifiers (no coordinates; no governed payload excerpts)

---

### 🛡 GovernanceContext

**Role**  
Frontend-wide governance visibility hub: CARE labels, sovereignty flags, masking requirements, and required notices that must be rendered.

**Owns (typical state, names may vary)**

- Active governance profile for the current view (CARE label, risk category)
- Sovereignty and protection flags relevant to currently-viewed items
- Masking requirements (H3/generalization requirements, “redaction required” toggles)
- Required notices (e.g., “locations generalized”, “restricted media hidden”)
- AI disclosure settings and disclaimers that must be shown in Focus/Story surfaces

**Hard invariants**

- GovernanceContext does **not** invent governance status; it surfaces backend decisions and applies frontend-safe tightening only.
- Governance notices required by policy are not user-dismissable when policy requires persistent display.
- GovernanceContext must be available to Map/Story/Focus surfaces without duplication.

**Cross-context interactions**

- Governance flags gate what MapContext can render (layer enablement, masking mode)
- FocusContext and Story surfaces must reference governance flags for labeling and safe disclosure behavior

**Persistence policy**

- Never persist governance decisions as “user preferences.”
- Persist only user UI preferences that do not loosen governance (e.g., “show governance drawer by default” is OK).

---

### 🗺️ MapContext

**Role**  
2D/3D view controller for global map state, including camera/viewport, active layers, and selection handles.

**Owns (typical state, names may vary)**

- MapLibre viewport (center, zoom, bearing, pitch)
- Cesium camera equivalents (position/orientation) if 3D is enabled
- Active layer keys and visibility flags
- Selected feature handles:
  - feature IDs
  - Story Node IDs
  - dataset/layer IDs
  - (avoid raw feature geometry storage)

**Hard invariants**

- MapContext may store **camera coordinates**, but must not store **governed feature coordinates** unless explicitly authorized and non-sensitive.
- Layer visibility must obey GovernanceContext:
  - restricted layers cannot become visible through client-only state changes
  - masking mode must apply when required

**Cross-context interactions**

- Map selection may activate FocusContext (via IDs)
- Map camera changes may be tagged for telemetry (without leaking user identifiers)

**Persistence policy**

- Optional: persist non-sensitive map UI preferences (basemap choice, last zoom)
- Never persist restricted-layer visibility as a user preference if policy forbids it

---

### 🎨 ThemeContext

**Role**  
Theme selection (light/dark/high-contrast), implemented via tokens and CSS variables.

**Owns (typical state, names may vary)**

- Active theme key: `light | dark | high-contrast`
- System preference detection and user override
- Token mode hooks for design system integration

**Hard invariants**

- Components must not bypass theme tokens with raw hex colors
- Theme changes must not reduce accessibility contrast for core UI affordances

**Cross-context interactions**

- Reads A11yContext (e.g., high-contrast preference)
- Coordinates with UIContext for safe transitions respecting reduced motion

**Persistence policy**

- Safe to persist theme preference locally

---

### ♿ A11yContext

**Role**  
Centralized accessibility preference state.

**Owns (typical state, names may vary)**

- `reducedMotion`
- `highContrast`
- `fontScale` / `largeText`
- Optional keyboard-navigation preference flags (if implemented)

**Hard invariants**

- A11yContext is authoritative for preference propagation; components do not “guess”
- Preference changes must be safe to apply at runtime without breaking focus behavior

**Cross-context interactions**

- Informs ThemeContext, UIContext, and map/3D transition behavior
- Supports “reduced-motion-safe” camera changes and panel animations

**Persistence policy**

- Safe to persist A11y preferences locally

---

### 🖥️ UIContext

**Role**  
Global shell state: which panels are open, which drawers/modals are active, and layout mode.

**Owns (typical state, names may vary)**

- Pane visibility: left/right panels, focus panel, story panel, explorer panel
- Modal/drawer open states
- Layout mode: split/stacked/docked
- Focus-management coordination flags (when opening/closing panels)

**Hard invariants**

- UIContext contains UI-only state (no domain data, no governance decisions)
- Must coordinate focus management to avoid keyboard traps and silent focus jumps

**Cross-context interactions**

- Reads A11yContext for reduced-motion behavior
- Works with FocusContext (e.g., “open focus panel when focus activated”)

**Persistence policy**

- Safe to persist non-sensitive UI preferences (panel default open/closed), with user consent

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  subgraph Providers["Context Providers"]
    Time["TimeContext"]
    Focus["FocusContext"]
    Gov["GovernanceContext"]
    Map["MapContext"]
    Theme["ThemeContext"]
    A11y["A11yContext"]
    UI["UIContext"]
  end

  subgraph Surfaces["Major UI Surfaces"]
    Timeline["TimelineView"]
    Map2D3D["MapView / CesiumView"]
    FocusPanel["FocusPanel"]
    StoryUI["Story Node UI"]
    Explorer["STAC/DCAT Explorer UI"]
    Overlay["Governance Overlay UI"]
  end

  Timeline --> Time
  Map2D3D --> Map
  FocusPanel --> Focus
  StoryUI --> Focus
  StoryUI --> Time
  Explorer --> Time
  Explorer --> Gov
  Overlay --> Gov

  Map --> Gov
  Focus --> Gov
  Theme --> A11y
  UI --> A11y
  UI --> Focus
~~~

---

## 🧠 Story Node & Focus Mode Integration

Contexts are the coordination plane that keeps **Story Node** and **Focus Mode** interactions coherent.

### Canonical interaction sequences

#### Story Node selection → synchronized UI

1. User selects a Story Node card (or a map footprint associated with a Story Node).
2. The app sets:
   - `FocusContext.activeStoryNodeId` (and/or focus target)  
   - `TimeContext` window aligned to the Story Node temporal span (range-safe)
   - `MapContext` highlight handles (IDs)
3. Governance overlays render:
   - CARE label and sovereignty indicators (from GovernanceContext)
   - masking/generalization notices where required

#### Focus target selection → governed explanation surface

1. User selects an entity (place/event/person/dataset) through search, map click, or Story relations.
2. The app sets `FocusContext.focusTarget = { id, type }`.
3. Data retrieval and narrative generation occur **outside** contexts (hooks/pipelines/services), and any returned content must:
   - preserve provenance references
   - label AI-generated segments vs archival text
   - honor backend governance restrictions
4. GovernanceContext drives required disclosures and any masking requirements for map/story previews.

### Non-negotiable constraints

- Frontend contexts coordinate state; they do not perform reasoning or governance decisions.
- All sensitive redaction and access control remains enforced by backend services; the frontend may add additional safety constraints but must never loosen them.

---

## 🧪 Validation & CI/CD

### Minimum CI expectations (context layer)

- Unit tests for:
  - initial state
  - reducers / bounded setters
  - invariants and edge cases (time ordering, focus clearing, layer gating)
- Integration tests for cross-context synchronization:
  - Time ↔ Map ↔ Story ↔ Focus
  - Governance ↔ Map layer visibility and masking state
  - A11y ↔ Theme ↔ UI focus management
- Type checks:
  - strict TypeScript compilation for context state and action types
- Security checks:
  - no secrets
  - no obvious PII in documentation or state snapshots

### Markdown governance checks (documentation CI)

This document is expected to pass the standard KFM Markdown validation profiles:

| Profile | What it protects |
|---|---|
| `markdown-lint` | heading structure + formatting constraints |
| `schema-lint` | YAML front-matter schema compliance |
| `metadata-check` | required keys present and consistent |
| `diagram-check` | Mermaid parse + allowed diagram profiles |
| `footer-check` | governance links present and ordered |
| `accessibility-check` | heading order + list semantics + basic a11y checks |
| `provenance-check` | provenance chain and version history coherence |
| `secret-scan` | blocks secrets/tokens/credentials |
| `pii-scan` | blocks obvious PII leakage |

---

## 📦 Data & Metadata

### Telemetry boundaries

Contexts should be **telemetry-aware** but remain side-effect light.

**Recommended pattern**

- Contexts expose stable “change points” (state transitions).
- Hooks at the boundary (e.g., `useTelemetry`) emit events based on transitions.
- Telemetry payloads are validated against `telemetry_schema` and MUST be non-PII.

### Suggested event families (non-exhaustive)

- `timeline:*` — global time window changes, granularity changes
- `focus:*` — focus activate/clear, relation navigation
- `map:*` — pan/zoom, layer toggle, safe selection events (IDs only)
- `governance:*` — required notice shown, masking mode activated
- `a11y:*` — preference changes (high-contrast, reduced-motion, font scale)
- `ui:*` — drawer/panel open/close (aggregated)

### State snapshot policy (debugging)

If state snapshots are captured (e.g., for error reports):

- Remove or hash any potentially sensitive identifiers if policy requires it.
- Never include raw governed geometries, restricted media URLs, or user identifiers.

---

## 🌐 STAC, DCAT & PROV Alignment

Contexts interact with standards-aligned metadata **by reference**:

- **STAC**
  - Dataset/asset selections should be represented in context state as stable identifiers or catalog handles.
  - Spatial previews obey masking rules; contexts should not carry raw asset geometries when restricted.
- **DCAT**
  - Catalog browsing state should reference dataset identifiers and filters (keywords, license classes) without embedding full distributions unless explicitly safe.
- **PROV-O**
  - Provenance is surfaced in UI via provenance chips and references.
  - Contexts store provenance handles/IDs needed to request provenance details from APIs, not reconstructed provenance graphs.

This keeps the state layer lightweight and ensures governance enforcement remains centralized and auditable.

---

## 🧱 Architecture

### Context boundaries vs other layers

- **Contexts**: shared state + deterministic transitions  
- **Hooks/Pipelines**: orchestration and side effects (fetching, telemetry emission, derived computation)  
- **Services**: API clients + schema validation + error normalization  
- **Components/Pages**: rendering and interaction

### Performance expectations

- Avoid storing large objects in context state (prevents unnecessary rerenders).
- Prefer stable identifiers and small structs over large payloads.
- If a context grows too broad, consider splitting into sub-contexts (without breaking the “approved API surface” contract).

### Accessibility (WCAG 2.1 AA+)

Contexts are non-visual, but they must support accessible UX:

- A11yContext must propagate preferences reliably.
- UIContext must support predictable focus behavior when panels open/close.
- ThemeContext must support contrast-safe modes and never require raw color usage in components.

---

## ⚖ FAIR+CARE & Governance

The context layer is the earliest point where governance becomes **globally visible** in the frontend.

### Required governance behaviors

- GovernanceContext is a single source of truth for:
  - CARE label visibility
  - sovereignty notices
  - masking/generalization requirements
  - required disclaimers (including AI disclosure)
- MapContext and FocusContext must consume governance flags and must not allow “unsafe states” such as:
  - restricted layers becoming visible via client-only toggles
  - unmasked sensitive features being rendered due to a stale state transition

### Prohibited behaviors

- Storing raw sensitive feature geometry in context state
- Creating feature flags that disable governance overlays for governed content
- Treating user preferences as authority to override policy

### Principle

**Frontend can be stricter, never looser.**  
If backend denies or masks, contexts must carry and respect that decision.

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-16 | Aligned to KFM-MDP v11.2.6: normalized approved H2 headings, directory layout format, fencing profile, and footer governance links; expanded context contracts, invariants, and cross-context sync rules. |
| v11.2.2 | 2025-11-30 | Added telemetry v2 references and clarified governance and A11y responsibilities across contexts. |
| v10.4.0 | 2025-11-15 | Rewritten for KFM-MDP v10.4; added governance + A11y + telemetry alignment. |
| v10.3.2 | 2025-11-14 | Added sovereignty + provenance integration notes. |
| v10.3.1 | 2025-11-13 | Initial context layer documentation. |

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
FAIR+CARE Certified · Public Document · Version-Pinned  

[⬅️ Back to Web Source Overview](../README.md) ·
[🧱 Web Source Architecture](../ARCHITECTURE.md) ·
[🌐 Web Platform Overview](../../README.md) ·
[🛡 Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🪶 FAIR+CARE Guide](../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🧿 Sovereignty Policy](../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

</div>
