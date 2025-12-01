---
title: "📐 Kansas Frontier Matrix — Layout Components Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/components/Layout/README.md"
version: "v11.2.2"
last_updated: "2025-11-30"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.2/web-layout-telemetry.json"
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
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
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
doc_uuid: "urn:kfm:doc:web-components-layout-readme-v11.2.2"
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
    - "🗂️ Directory Structure"
    - "🧩 Component Responsibilities"
    - "🔐 FAIR+CARE & Governance Integration"
    - "♿ Accessibility Requirements (WCAG 2.1 AA+)"
    - "📈 Telemetry Responsibilities"
    - "🧪 Testing Requirements"
    - "🕰 Version History"
    - "⚖️ Footer"
---

<div align="center">

# 📐 **Kansas Frontier Matrix — Layout Components Overview**  
`web/src/components/Layout/README.md`

**Purpose:**  
Define the layout system used across the KFM Web Platform — including containers, shells, panels, navigation  
structures, and accessibility scaffolding that ensures every page and feature is presented in a coherent,  
WCAG-compliant, FAIR+CARE-aware UI architecture.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)]()  
[![KFM-MDP v11.2.2](https://img.shields.io/badge/KFM%E2%80%93MDP-v11.2.2-purple)]()  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Low%20Risk-gold)]()  
[![WCAG AA+](https://img.shields.io/badge/A11y-WCAG%202.1%20AA%2B-brightgreen)]()

</div>

---

## 📘 Overview

Layout components define **the structural foundation** of the KFM Web Platform UI.  
They ensure:

- Consistent page scaffolding across all views  
- Accessible navigation and region semantics  
- Always-on visibility for governance surfaces (CARE + provenance when needed)  
- Predictable responsive behavior on desktop, tablet, mobile  
- Integration with global contexts (theme, governance, A11y, time, focus)  
- A clean separation between **layout** and **feature/business logic** components  
- Deterministic rendering with no hidden side effects  

**Layout components must:**

- Be **pure presentation** (no data fetching, no business logic)  
- Use appropriate **semantic HTML** landmarks and regions  
- Propagate **A11y tokens** and theme tokens from global providers  
- Defer all data-processing to hooks, context providers, or higher-level containers  

---

## 🗂️ Directory Structure

Emoji-enriched v11 layout:

~~~text
web/src/components/Layout/
│
├── 🧭 Header.tsx              # Global top bar with navigation + governance links
├── 📚 Sidebar.tsx             # Left/right navigation sidebar (collapsible, accessible)
├── 🧱 PageContainer.tsx       # Top-level page wrapper with theme + A11y + contexts
├── 🗂 Panel.tsx               # Generic panel container (story, focus, datasets, governance)
├── 🧩 Section.tsx             # Accessible sectional content block
├── 🔀 SplitView.tsx           # Horizontal/vertical split panes (e.g., map + narrative)
├── 🛠 Toolbar.tsx             # Tool/action bar with icons + keyboard shortcuts
└── 🪟 ModalLayout.tsx         # Accessible modal scaffolding (focus trapping, scroll control)
~~~

Any additions MUST be reflected here and documented in the responsibilities section.

---

## 🧩 Component Responsibilities

### 🧭 Header.tsx

**Role:**  
Global top bar used across major views.

**Responsibilities:**

- Provides primary navigation (e.g., links to Map, Timeline, Datasets, Docs)  
- Surfaces governance affordances:
  - Link to governance docs  
  - CARE/sovereignty info entry points  
- Hosts global search (if enabled) and app-level utilities (theme toggle, a11y toggle)

**A11y:**

- `<header>` landmark  
- Skip-to-content link anchored into `<main>`/PageContainer  
- High-contrast color tokens; no color-only semantics for active states  

---

### 📚 Sidebar.tsx

**Role:**  
Persistent or collapsible navigation sidebar.

**Responsibilities:**

- Render navigation tree (sections, view links)  
- Support collapsible sections with ARIA attributes (`aria-expanded`)  
- Provide optional area for filters or dataset layer lists when used in map context  

**A11y:**

- Use `<nav>` landmark with `aria-label` (e.g., `"Primary navigation"`)  
- Keyboard navigation support (arrow keys for tree, tab for actions)  

---

### 🧱 PageContainer.tsx

**Role:**  
Top-level page wrapper and context host.

**Responsibilities:**

- Wrap page-level content in `<main>` region with correct `role="main"`  
- Apply theming and layout tokens (spacing, typography)  
- Connect global contexts:
  - ThemeContext  
  - GovernanceContext (CARE, sovereignty flags)  
  - A11yContext (reduced motion, contrast preferences)  
  - TimeContext / FocusContext (where appropriate)  
- Manage scroll behavior and overflow  

**Rules:**

- MUST not fetch data; only read from contexts and render children  
- MUST ensure that Skip-to-content link and focus management land here  

---

### 🗂 Panel.tsx

**Role:**  
Reusable container for high-level panels.

**Typical uses:**

- Story Node detail panel  
- Focus Mode side panel  
- Dataset detail or governance panel  
- Timeline explanation panel  

**A11y:**

- Provide appropriate region semantics (e.g., `<section>` with headings)  
- Support optional `aria-label` for panel context  

---

### 🧩 Section.tsx

**Role:**  
Structured content block for within panels/pages.

**Responsibilities:**

- Encapsulate a discrete unit of content with its heading  
- Maintain heading order (H2/H3/etc.) consistent with parent layout  
- Provide appropriate spacing, background, and reading width  

**Context:**

- Used for narrative blocks, governance notices, timeline descriptions, etc.  

---

### 🔀 SplitView.tsx

**Role:**  
Layout for side-by-side or top-bottom panes (e.g., Map + Narrative).

**Responsibilities:**

- Arrange two (or more) child regions with adjustable sizes  
- Optionally allow keyboard-resizable split (using ARIA `separator` patterns)  
- Respect reduced-motion and avoid over-animated transitions  

**A11y:**

- Use ARIA `role="separator"` when panes are user-resizable  
- Provide keyboard controls (e.g., arrow keys with modifier) for resizing when enabled  

---

### 🛠 Toolbar.tsx

**Role:**  
Tool/action bar for layout-level actions.

**Typical contents:**

- Map tools (zoom, basemap, layer toggles)  
- Timeline tools (granularity, play/pause)  
- Focus Mode actions (switch entity, filter relations)  

**Requirements:**

- Every tool must have:
  - Visible text label or ARIA label  
  - Clear icon semantics for screen readers  
- Should expose hooks/events for telemetry (e.g., `"ui:tool-activated"`)  

---

### 🪟 ModalLayout.tsx

**Role:**  
Scaffolding for modals and drawers (layout-level concern).

**Responsibilities:**

- Provide correct `role="dialog"` or `role="alertdialog"` semantics  
- Implement focus trapping and return focus to invoker on close  
- Prevent scroll bleed behind the modal  
- Respect reduced-motion for open/close animations  

**Used for:**

- GovernanceDrawer  
- Story Node media viewer  
- Dataset metadata modals  
- System-level prompts  

---

## 🔐 FAIR+CARE & Governance Integration

Although primarily visual/structural, the layout system must:

- Ensure governance and CARE surfaces remain **reachable and visible**, not hidden by layout decisions  
- Reserve clear, consistent regions for:
  - CAREBadge / governance widgets  
  - Provenance chips or trails in places where sensitive data is shown  
- Avoid layout patterns that:
  - Make warnings easy to miss (e.g., burying them below endlessly scrolling panels)  
  - Confuse which section a warning applies to  

Layout components **must not**:

- Suppress or conditionally hide governance components provided as children  
- Obscure sovereignty notices behind non-obvious gestures or off-screen areas  

---

## ♿ Accessibility Requirements (WCAG 2.1 AA+)

Layout components are **foundational** for accessibility.

They MUST:

- Use semantic landmarks:
  - `<header>`, `<nav>`, `<main>`, `<aside>`, `<footer>` where appropriate  
- Maintain a logical heading hierarchy (no skipping levels arbitrarily)  
- Provide:
  - Skip-to-content links (from Header to PageContainer)  
  - Visible focus indicators for all interactive layout controls (Sidebar, SplitView, Toolbar, ModalLayout)  
- Respect user preferences:
  - `prefers-reduced-motion`  
  - High-contrast mode  
- Avoid:
  - Hidden focus traps  
  - Off-screen content that becomes keyboard focusable without context  

Any layout-related A11y regression MUST block CI.

---

## 📈 Telemetry Responsibilities

The layout system participates in UI-level telemetry. Through higher-level wiring, it should enable:

- `"layout:page-enter"` / `"layout:page-exit"` events  
- `"layout:sidebar-toggle"` when Sidebar is opened/closed  
- `"layout:modal-open"` / `"layout:modal-close"` for ModalLayout usage  
- `"layout:splitview-adjust"` when SplitView is resized (if user-controllable)  
- `"layout:toolbar-tool-activated"` when Toolbar tools are invoked  

**Constraints:**

- No PII in telemetry payloads  
- Events MUST conform to `telemetry_schema`  
- Events should be stable across versions or version-tagged for analysis  

---

## 🧪 Testing Requirements

Testing scope for layout components:

- **Unit tests:**
  - Render correctness (smoke tests)  
  - Proper classnames / tokens for layout  
  - Prop-driven variants (e.g., sidebar positions, modal states)  

- **Integration tests:**
  - Combined layout with main views (map + panel, story + map, etc.)  
  - Skip-to-content jumps and focus movement  
  - Governance components placed in Header/Sidebar show correctly  

- **Accessibility tests:**
  - Landmark roles present and unique where needed  
  - Keyboard navigation across Header, Sidebar, Panel, ModalLayout  
  - Focus trap behavior in modals  

- **Telemetry tests:**
  - Events triggered on key interactions (sidebar toggle, modal open/close…)  

Test locations:

~~~text
tests/unit/web/components/Layout/**
tests/integration/web/components/Layout/**
~~~

---

## 🕰 Version History

| Version | Date       | Summary                                                                 |
|--------:|------------|-------------------------------------------------------------------------|
| v11.2.2 | 2025-11-30 | Upgraded to v11.2.2; enriched metadata, A11y, governance & telemetry   |
| v10.4.0 | 2025-11-15 | Complete layout overview per KFM-MDP v10.4; added A11y, governance rules |
| v10.3.2 | 2025-11-14 | Improved SplitView + Header governance patterns                        |
| v10.3.1 | 2025-11-13 | Initial layout documentation                                          |

---

## ⚖️ Footer

<div align="center">

**📚 Governance Links**  
[Docs Root](../../../../README.md) •  
[Standards Index](../../../../docs/standards/INDEX.md) •  
[Governance Charter](../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

**🔐 Compliance:**  
FAIR+CARE · CIDOC-CRM · OWL-Time · PROV-O · WCAG 2.1 AA+ · SLSA Level 3

**End of Document**

</div>