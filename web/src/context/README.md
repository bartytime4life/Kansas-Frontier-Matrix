---
title: "🧠 Kansas Frontier Matrix — Web Context System Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/context/README.md"
version: "v11.2.2"
last_updated: "2025-11-30"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../releases/v11.2.2/web-context-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/web-context-readme-v2.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

status: "Active / Enforced"
doc_kind: "Overview"
intent: "web-context-overview"
role: "overview"

fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk (logic-only)"
sensitivity_level: "None"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false

provenance_chain:
  - "web/src/context/README.md@v10.4.0"
  - "web/src/context/README.md@v10.3.2"
  - "web/src/context/README.md@v10.3.1"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "SoftwareSourceCode"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"

json_schema_ref: "../../../schemas/json/web-context-readme-v11.schema.json"
shape_schema_ref: "../../../schemas/shacl/web-context-readme-v11-shape.ttl"
doc_uuid: "urn:kfm:doc:web-context-readme-v11.2.2"
semantic_document_id: "kfm-doc-web-context-readme-v11"
event_source_id: "ledger:web/src/context/README.md"
immutability_status: "version-pinned"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "summaries"
  - "speculative-additions"
  - "unverified-historical-claims"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "United States / Kansas"
classification: "Public Document"

ttl_policy: "Review each release"
sunset_policy: "Superseded upon next state-layer overhaul"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Structure"
    - "🧩 Context Responsibilities"
    - "🔐 FAIR+CARE & Governance Integration"
    - "♿ Accessibility Requirements (WCAG 2.1 AA+)"
    - "📈 Telemetry Responsibilities"
    - "🧪 Testing Requirements"
    - "🕰 Version History"
    - "⚖️ Footer"
---

<div align="center">

# 🧠 **Kansas Frontier Matrix — Web Context System Overview**  
`web/src/context/README.md`

**Purpose:**  
Document the **state management layer** of the Kansas Frontier Matrix Web Platform — including  
the contexts that manage time, focus, governance, accessibility, theming, and spatial/narrative  
synchronization across the entire frontend application.  
React Contexts in this directory serve as the *global, ethical, and deterministic state backbone*  
for all features, components, and pipelines.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)]()  
[![KFM-MDP v11.2.2](https://img.shields.io/badge/KFM%E2%80%93MDP-v11.2.2-purple)]()  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Low%20Risk-gold)]()  
[![WCAG AA+](https://img.shields.io/badge/A11y-WCAG%202.1%20AA%2B-brightgreen)]()

</div>

---

## 📘 Overview

Contexts in `web/src/context/` provide:

- **Global state containers** shared across the Web Platform  
- Deterministic, typed state transitions  
- Mandatory governance (CARE/provenance) checks at the state layer  
- Accessibility-first system settings and preferences  
- Synchronization for:
  - Timeline → Map  
  - Focus Mode → Story Nodes  
  - Governance → UI visibility / masking  
  - Theme → design-system tokens  
- Centralized, predictable state orchestration  
- Telemetry-aware updates (non-PII)  

Contexts must remain:

- Pure (no rendering, no direct side effects beyond controlled telemetry)  
- Type-safe (TS types/guards for all state shapes)  
- Predictable (no hidden global mutation)  
- FAIR+CARE compliant (respecting governance flags)  
- A11y aligned (propagating user preferences to UI)  
- Non-speculative (no inferred facts about time, place, or entities)  

---

## 🗂️ Directory Structure

~~~text
web/src/context/
│
├── ⏱️ TimeContext.tsx         # Controls global timeline range + fuzzy intervals
├── 🎯 FocusContext.tsx        # Entity in focus + narrative bundle + geometry refs
├── 🎨 ThemeContext.tsx        # Light/dark + high-contrast-aware theme state
├── ♿ A11yContext.tsx          # Reduced-motion, high-contrast, large-text preferences
├── 🛡 GovernanceContext.tsx    # CARE, provenance, sovereignty flags + warnings
├── 🗺️ MapContext.tsx          # MapLibre + Cesium viewport + camera state
└── 🖥️ UIContext.tsx           # UI toggles (sidebars, panels, modals, layouts)
~~~

Each context file must be documented in the responsibilities section below.

---

## 🧩 Context Responsibilities

### ⏱️ TimeContext.tsx

**Role:**  
Global controller for time-related state.

**Responsibilities:**

- Maintain the current timeline window (start/end)  
- Normalize and store time spans in OWL-Time-friendly shapes  
- Track granularity (e.g., year/decade/century)  
- Expose filters for:
  - Story Nodes  
  - STAC/DCAT datasets  
  - Map layers  
  - Focus Mode ranges  

**Guarantees:**

- No inconsistent temporal state (e.g., end < start)  
- Fuzzy/uncertain dates handled ethically (e.g., storing ranges and labels like “ca. 1850”)  
- Changes propagated deterministically via reducer/actions or equivalent pattern  

**Telemetry (via helper/wrapper):**

- `"timeline:update"` when the global time window or granularity changes  

---

### 🎯 FocusContext.tsx

**Role:**  
Global state for Focus Mode and focus-like views.

**Responsibilities:**

- Track the current focus entity:
  - ID, type (Person, Place, Event, Dataset, Story Node, etc.)  
- Store summary/narrative metadata (e.g., AI-labeled or archival)  
- Maintain a small neighborhood of graph neighbors and related Story Nodes  
- Provide references for map highlight geometry (IDs, not raw coordinates)  
- Provide states for “focus is active/inactive”  

**Governance:**

- CARE labels must be tracked alongside focus entity  
- Must carry flags for “sovereignty-controlled” or “sensitive” focus targets  
- Must never embed raw geometry or coordinates — only IDs/handles  

**Telemetry:**

- `"focus:activate"` (focus set)  
- `"focus:relation-select"` (user follows relation from focus context)  

---

### 🎨 ThemeContext.tsx

**Role:**  
Platform theming controller.

**Responsibilities:**

- Manage:
  - Light/dark modes  
  - High-contrast variants  
  - Color token preferences consistent with A11y rules  
- Provide a unified set of design tokens to components (via CSS variables / Tailwind config)

**Accessibility:**

- Must respect `prefers-color-scheme` and user overrides  
- Must ensure that all theme combinations maintain WCAG AA+ contrast for core tokens  

---

### ♿ A11yContext.tsx

**Role:**  
Accessibility preferences context.

**Responsibilities:**

- Track:
  - `reducedMotion` preference  
  - `highContrast` preference  
  - `largeText` or font scaling factors  
  - Optional flags for screen-reader “mode” or other assistive indicators  
- Provide hooks for components to subscribe to and respond to preference changes  

**Telemetry:**

- `"a11y:preference-change"` when user changes any of these preferences  

Components should not guess; they should read preferences from this context.

---

### 🛡 GovernanceContext.tsx

**Role:**  
Global governance and CARE state hub.

**Responsibilities:**

- Track:
  - CARE labels at application-scope (e.g., default classification)  
  - Sovereignty rules relevant to the current view/region  
  - Masking flags (H3 generalization, temporal generalization, redaction status)  
  - Current warnings that must be shown (e.g., for sensitive pages)  
  - AI generation flags / disclaimers  

- Provide:
  - Derived, read-only governance state to mapping, timeline, story, and dataset views  

**Rules:**

- Must not compute or store raw coordinates; only flags and rules  
- Must not circumvent backend/graph governance decisions; only surface and propagate  

**Telemetry:**

- `"governance:warning-shown"` when a global governance warning becomes active  

---

### 🗺️ MapContext.tsx

**Role:**  
Global view state for 2D/3D maps.

**Responsibilities:**

- Track:
  - MapLibre viewport (center, zoom, bearing, pitch)  
  - Cesium camera position/time slice for 3D (if used)  
  - Active layers and layer visibility state  
  - Selected map entity IDs (not raw coordinates)  
- Provide:
  - A stable interface for MapView to read+update camera/viewport state  

**Governance:**

- Must interact with GovernanceContext to determine which layers are viewable  
- Must signal when restricted layers would be visible so UI can mask or block  

**Telemetry:**

- `"map:pan"`  
- `"map:zoom"`  
- `"map:layer-toggle"`  

(Events are emitted by map-layer code using MapContext values.)

---

### 🖥️ UIContext.tsx

**Role:**  
Global UI toggles and layout state.

**Responsibilities:**

- Manage:
  - Sidebar open/close  
  - Drawer visibility (e.g., DetailDrawer, GovernanceDrawer)  
  - Modal open/close  
  - Layout modes (e.g., split view vs stacked)  
- Ensure:
  - Consistent transitions and animation flags  
  - Controlled focus management when panels open/close (in collaboration with A11y helpers)  

**Rules:**

- No business or data logic; only UI-level toggles and transient state  
- Must be consistent and deterministic across reloads (where appropriate; may be persisted in local storage with user consent)  

---

## 🔐 FAIR+CARE & Governance Integration

The context layer is where governance flags and preferences first become **globally visible**.

All contexts MUST:

- Respect CARE and sovereignty flags from backend/graph:
  - GovernanceContext must hold the canonical “frontend view” of these flags  
  - TimeContext and MapContext must use these to prevent unsafe state combinations (e.g., non-generalized view on restricted data)  
- Avoid storing:
  - Raw coordinates  
  - Sensitive text or media content (only IDs, references, and flags)  
- Provide:
  - Clean, typed interfaces for UI layers to read governance metadata and respond accordingly  

Governance logic in contexts:

- Determines **whether** something is allowed to be shown, but not **how** it is visually rendered (that’s the component layer).  
- MUST not override stricter backend governance decisions; “frontend can be stricter, never looser.”

Governance violations at the context layer (e.g., exposing restricted state or ignoring redaction_required flags) are **CI-blocking**.

---

## ♿ Accessibility Requirements (WCAG 2.1 AA+)

Although contexts are non-visual, they are **critical** for accessibility:

- A11yContext:
  - Must reliably propagate user preferences so components can adapt correctly  
- ThemeContext:
  - Must ensure theme choices do not break contrast or readability  
- UIContext:
  - Must support predictable focus behavior on open/close actions (via layout components)

Requirements:

- No context may create “hidden” states that trap focus or disable essential features without UI components being aware  
- State transitions triggered by user preferences must be:
  - Deterministic  
  - Announced (where needed) to assistive technologies via UI/ARIA integration  

Accessibility regressions in context usage must block merges.

---

## 📈 Telemetry Responsibilities

Each context participates in telemetry by providing semantic “change points” that can be recorded by wrapper hooks or side-effect layers.

Typical events (wired by hooks, not emitted inside contexts):

- `timeline:update` (from TimeContext updates)  
- `focus:activate` / `focus:clear` (from FocusContext)  
- `map:pan` / `map:zoom` / `map:layer-toggle` (from MapContext-driven interactions)  
- `governance:warning-shown` (from GovernanceContext state)  
- `a11y:preference-change` (from A11yContext updates)  

Telemetry MUST:

- Be non-PII  
- Follow the schemas in `telemetry_schema`  
- Include context version and environment tags to support time-series analysis and debugging  

Context code itself should remain side-effect-light; telemetry is best handled by effect hooks at the boundary.

---

## 🧪 Testing Requirements

Each context MUST have:

- **Unit tests**:
  - State initialization  
  - Reducer/transition function tests  
  - Edge case transitions (boundary conditions for time, focus, map, governance)  

- **Integration tests**:
  - Cross-context synchronization:
    - TimeContext ↔ MapContext ↔ FocusContext  
    - GovernanceContext ↔ MapContext / TimelineView / Story components  
  - Combined behavior with UI components (e.g., map/timeline reacting to TimeContext)  

- **Governance tests**:
  - Redaction and sovereignty flags propagate properly and are not dropped  
  - Prohibited states (e.g., “sensitive geometry in a non-masked view”) cannot occur via context alone  

- **A11y preference propagation tests**:
  - A11yContext updates cause expected downstream behavior in test harnesses  

Test file layout:

~~~text
tests/unit/web/context/**
tests/integration/web/context/**
~~~

---

## 🕰 Version History

| Version | Date       | Summary                                                                                  |
|--------:|------------|------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-30 | Upgraded to KFM-MDP v11.2.2; added telemetry v2, energy/carbon schemas, clearer governance contracts |
| v10.4.0 | 2025-11-15 | Rewritten for KFM-MDP v10.4; added governance, A11y, telemetry, Focus Mode v2.5 alignment |
| v10.3.2 | 2025-11-14 | Added sovereignty + provenance integration                                              |
| v10.3.1 | 2025-11-13 | Initial context layer documentation                                                    |

---

## ⚖️ Footer

<div align="center">

**📚 Governance Links**  
[Docs Root](../../../README.md) •  
[Standards Index](../../../docs/standards/INDEX.md) •  
[Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

**🔐 Compliance:**  
FAIR+CARE · CIDOC-CRM · OWL-Time · PROV-O · WCAG 2.1 AA+ · SLSA Level 3

**End of Document**

</div>