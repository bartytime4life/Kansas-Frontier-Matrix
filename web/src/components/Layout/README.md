---
title: "📐 Kansas Frontier Matrix — Layout Components Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/components/Layout/README.md"
version: "v11.2.6"
last_updated: "2025-12-16"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"
signature_ref: "<release-signature-or-attestation-ref>"

sbom_ref: "../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.6/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.6/web-layout-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/web-components-layout-v2.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
classification: "Public Document"
jurisdiction: "United States / Kansas"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

status: "Active / Enforced"
doc_kind: "Component Overview"
intent: "frontend-layout"
semantic_intent:
  - "UI-component"
  - "layout-system"
  - "a11y-scaffolding"
  - "governance-surface"

fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk (layout-only)"
sensitivity: "None"
sensitivity_level: "None"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false

provenance_chain:
  - "web/src/components/Layout/README.md@v10.4.0"
  - "web/src/components/Layout/README.md@v10.3.2"
  - "web/src/components/Layout/README.md@v10.3.1"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "WebPageElement"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"

json_schema_ref: "../../../../schemas/json/web-components-layout-readme-v11.schema.json"
shape_schema_ref: "../../../../schemas/shacl/web-components-layout-readme-v11-shape.ttl"
doc_uuid: "urn:kfm:doc:web-components-layout-readme-v11.2.6"
semantic_document_id: "kfm-doc-web-components-layout-readme-v11"
event_source_id: "ledger:web/src/components/Layout/README.md"
immutability_status: "version-pinned"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative-additions"
  - "unverified-historical-claims"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "🧩 Component Responsibilities"
    - "⚖ FAIR+CARE & Governance"
    - "♿ Accessibility Requirements (WCAG 2.1 AA+)"
    - "📈 Telemetry Responsibilities"
    - "🧪 Testing Requirements"
    - "🕰️ Version History"
---

<div align="center">

# 📐 **Kansas Frontier Matrix — Layout Components Overview**
`web/src/components/Layout/README.md`

**Purpose**  
Define the **layout system** used across the KFM Web Platform — shells, containers, panels, navigation regions,
and accessibility scaffolding that keep every view **coherent, responsive, and WCAG‑compliant**.

Layout components are **presentation-only**: they must not fetch data, query the graph, or embed domain business logic.
They exist to make feature surfaces (Map, Timeline, Story Nodes, Focus Mode, Dataset browsers) structurally consistent,
governance-visible, and accessible.

<img src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Governed-orange" />
<img src="https://img.shields.io/badge/Accessibility-WCAG_2.1_AA%2B-blueviolet" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

</div>

---

## 📘 Overview

Layout components provide the **structural foundation** for KFM’s web UI, which is described as a React-based,
map-centric interface with supporting panels such as a Timeline control, Layer Legend, and Search surface. The
platform also supports 2D/3D mapping engines (MapLibre / Cesium) at the view layer.

This README defines how layout code should be structured so that downstream features can:

- Present a map-first interface with consistent placement of navigation, tools, panels, and drawers.
- Maintain stable semantic landmarks across routes and modes (Map view, Timeline mode, Story Node reading,
  Focus Mode investigation).
- Keep governance surfaces (CARE labels, sovereignty notices, provenance links) reachable and non-optional.
- Support responsive composition (desktop, tablet, mobile) without breaking keyboard navigation or focus order.
- Consume shared theming and design tokens (defined upstream in the monorepo) without hard-coding UI “magic numbers.”

**Non-goals**

- Implementing data access (API clients, graph access, file downloads).
- Implementing feature logic (Map rendering, Timeline logic, Focus Mode reasoning).
- Implementing governance policy decisions (layout only renders governance state supplied by higher layers).

---

## 🗂️ Directory Layout

~~~text
web/src/components/Layout/
├── 📄 README.md — This document (governed layout contract for the web UI)
├── 🧱 PageContainer.tsx — Page shell + landmark regions + skip-to-content target
├── 🧭 Header.tsx — Global header (navigation, global actions, governance entry points)
├── 📚 Sidebar.tsx — Primary navigation / filters (collapsible, keyboard-first)
├── 🗂 Panel.tsx — Generic panel container (map-adjacent panels, narrative panels, inspector panels)
├── 🧩 Section.tsx — Accessible content section block (heading + spacing + reading width)
├── 🔀 SplitView.tsx — Split-pane scaffold (map + narrative, map + inspector, etc.)
├── 🛠 Toolbar.tsx — Layout-level tool strip (buttons, toggles, shortcut affordances)
└── 🪟 ModalLayout.tsx — Modal scaffold (focus trap, scroll lock, ARIA dialog semantics)
~~~

Notes:

- Keep **layout** components small and composable; prefer composition over deep inheritance.
- If a component introduces a new landmark or navigational region, it must be documented here.
- If filenames differ in-repo, update this tree (the directory layout is CI-linted).

---

## 🧩 Component Responsibilities

### 🧱 PageContainer.tsx

**Role**  
Top-level page wrapper that defines the *stable landmarks* and layout grid used by all routes.

**Responsibilities**

- Provide consistent semantic regions (typically: `header`, `nav`, `main`, `footer`, optional `aside`).
- Host the skip-to-content target and ensure focus lands in the correct region after route changes.
- Apply layout tokens (spacing, max widths, responsive breakpoints) via the theming layer.

**Must not**

- Fetch data or call APIs.
- Make governance decisions (it only renders what governance state providers supply).

---

### 🧭 Header.tsx

**Role**  
Global top bar / app header.

**Responsibilities**

- Provide primary navigation links (e.g., Map, Timeline, Datasets, Docs).
- Provide globally-relevant controls (theme/a11y toggles, help entry points).
- Provide consistent entry points to governance documentation and explanations.

**Accessibility baseline**

- Must render as a `<header>` landmark.
- Must include (or support) a skip-to-content link.

---

### 📚 Sidebar.tsx

**Role**  
Primary navigation and (optionally) filter surface.

**Responsibilities**

- Render a keyboard-friendly navigation list/tree.
- Support collapsible sections with correct ARIA state (`aria-expanded`, `aria-controls`).
- Provide consistent placement for view-local navigational content (e.g., map layers list, filters).

**Accessibility baseline**

- Must render as a `<nav>` landmark with a clear `aria-label`.
- Must avoid hidden-focus scenarios when collapsed (collapsed sidebar content must not be tabbable).

---

### 🗂 Panel.tsx

**Role**  
A layout container for secondary surfaces adjacent to the main content area.

**Responsibilities**

- Provide consistent padding/spacing and a stable section header pattern.
- Support scroll behavior inside a panel without breaking page-level scroll semantics.
- Support “map-adjacent” and “narrative-adjacent” panel placement.

**Examples of consumers (feature-owned, not layout-owned)**

- Story Node reading panel
- Focus Mode investigation panel
- Dataset inspector panel
- Timeline explanation panel

---

### 🧩 Section.tsx

**Role**  
A semantic content wrapper for structuring panel/page content.

**Responsibilities**

- Provide consistent heading spacing and reading width.
- Enforce heading order within a container (no skipping levels).
- Provide a predictable content boundary for screen readers (use `<section>` + heading).

---

### 🔀 SplitView.tsx

**Role**  
A split-pane scaffold for multi-surface views (common in map-first UIs).

**Responsibilities**

- Provide stable composition for:
  - Map + panel
  - Map + narrative
  - Map + inspector
- Optionally support user resizing (if supported by the current UI design).
- Respect reduced motion and avoid “animated layout thrash.”

**If resizable is enabled**

- Use an ARIA separator pattern for the resize handle (`role="separator"` and keyboard controls).

---

### 🛠 Toolbar.tsx

**Role**  
A consistent location for view-level tools.

**Responsibilities**

- Provide consistent spacing/alignment for tool buttons and toggles.
- Ensure every tool is keyboard-accessible and has a visible name or an accessible name.
- Support stable integration points for telemetry (tool activation events are emitted by the wiring layer).

---

### 🪟 ModalLayout.tsx

**Role**  
The governed scaffolding for modals and modal-adjacent surfaces (including drawers).

**Responsibilities**

- Provide correct dialog semantics (`role="dialog"` / `aria-modal="true"` when appropriate).
- Trap focus within the modal while open and restore focus to the invoking control on close.
- Prevent background scroll bleed while open.
- Respect reduced motion for open/close transitions.

**Notes**

- Feature components such as DetailDrawer must be compatible with ModalLayout’s focus and scroll rules.

---

## ⚖ FAIR+CARE & Governance

Even though layout components are “low-risk” by themselves, they are responsible for ensuring that governance
surfaces remain **structurally visible** and **reachable**.

Layout must support:

- A stable region for CARE/sovereignty labels and notices (especially in header/panel patterns).
- A stable region for provenance links and “why is this hidden/generalized?” explanations when sensitive content is present.
- Predictable placement of warnings so they are not buried below fold or hidden behind non-obvious interactions.

Layout must not:

- Obscure governance warnings behind overlay-only interactions without accessible alternatives.
- Render feature surfaces that bypass platform contracts (frontend stays behind APIs; no direct graph access).

---

## ♿ Accessibility Requirements (WCAG 2.1 AA+)

Layout components are accessibility-critical because they define navigation order and semantic landmarks.

Minimum requirements:

- Provide semantic landmarks (`header`, `nav`, `main`, optional `aside`, `footer`) and ensure they are not duplicated in ways
  that confuse assistive technology.
- Provide a skip-to-content link pattern (Header → PageContainer main region).
- Ensure focus order matches reading order for both:
  - map-first layouts (map in `main`, panels in `aside` or adjacent sections)
  - narrative-first layouts (panel or narrative in `main`, map secondary)
- Respect user preferences:
  - `prefers-reduced-motion`
  - high-contrast modes (avoid color-only affordances)

Hard constraints:

- No invisible tabbable UI when hidden/collapsed.
- No focus traps outside ModalLayout; modal/drawer focus behavior must be centralized.

---

## 📈 Telemetry Responsibilities

Layout participates in UI-level telemetry by providing stable, predictable interaction points.

Common event families (names are illustrative; payloads must follow `telemetry_schema`):

- `layout:page-enter` / `layout:page-exit`
- `layout:sidebar-toggle`
- `layout:modal-open` / `layout:modal-close`
- `layout:splitview-adjust` (only if user-driven resizing exists)
- `layout:toolbar-tool-activated`

Telemetry constraints:

- No PII in payloads.
- No raw user-entered content in telemetry.
- Include component version/environment tags (handled by the telemetry client/wiring layer).

---

## 🧪 Testing Requirements

Layout tests must validate structure, accessibility, and regressions that would affect every page.

Minimum coverage:

- **Unit**
  - renders without errors across supported variants (collapsed sidebar, no header actions, etc.)
  - landmark structure is present and stable

- **Accessibility**
  - skip-to-content works and lands focus in the correct region
  - keyboard-only navigation across header/sidebar/toolbar is functional
  - modal focus trap and focus restoration works

- **Integration**
  - map + panel compositions (SplitView) do not break scroll/focus
  - governance surfaces render in expected regions when provided by feature layers

Suggested test locations (align to the repo’s chosen web test harness):

~~~text
tests/unit/web/components/Layout/**
tests/integration/web/components/Layout/**
~~~

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-16 | Aligned to KFM‑MDP v11.2.6; normalized headings (Directory Layout, governance, version history ordering); strengthened layout non-goals and web UI context; improved directory tree style and footer governance links. |
| v11.2.2 | 2025-11-30 | Upgraded to v11.2.2; enriched metadata, A11y, governance & telemetry. |
| v10.4.0 | 2025-11-15 | Complete layout overview per KFM-MDP v10.4; added A11y and governance guidance. |
| v10.3.2 | 2025-11-14 | Improved SplitView + Header governance patterns. |
| v10.3.1 | 2025-11-13 | Initial layout documentation. |

---

<div align="center">

**📚 Reference Links**  
[Web Architecture](../../../ARCHITECTURE.md) · [Web README](../../../README.md) · [Docs Root](../../../../README.md)

**🧭 Governance & Standards**  
[Standards Index](../../../../docs/standards/INDEX.md) · [Governance Charter](../../../../docs/standards/governance/ROOT-GOVERNANCE.md) · [FAIR+CARE Guide](../../../../docs/standards/faircare/FAIRCARE-GUIDE.md)

**🔐 Compliance (layout-level)**  
FAIR+CARE · PROV‑O aware surfaces · WCAG 2.1 AA+ · KFM‑MDP v11.2.6

© 2025 Kansas Frontier Matrix — MIT License

</div>
