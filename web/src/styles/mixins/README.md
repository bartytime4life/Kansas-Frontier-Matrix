---
title: "⚙️ Kansas Frontier Matrix — Style Mixins Specification (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/styles/mixins/README.md"
version: "v10.4.0"
last_updated: "2025-11-15"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/web-styles-mixins-v1.json"
governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.1"
status: "Active / Enforced"
doc_kind: "Specification"
intent: "web-styles-mixins"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
sensitivity_level: "None"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false
provenance_chain:
  - "web/src/styles/mixins/README.md@v10.3.2"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "DefinedTermSet"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
json_schema_ref: "../../../../schemas/json/web-styles-mixins.schema.json"
shape_schema_ref: "../../../../schemas/shacl/web-styles-mixins-shape.ttl"
doc_uuid: "urn:kfm:doc:web-styles-mixins-v10.4.0"
semantic_document_id: "kfm-doc-web-styles-mixins"
event_source_id: "ledger:web/src/styles/mixins/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "summaries"
  - "speculative additions"
  - "unverified visual semantics"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "United States / Kansas"
classification: "Public Document"
role: "specification"
lifecycle_stage: "stable"
ttl_policy: "Review every 12 months"
sunset_policy: "Superseded upon mixin system v11 update"
---

<div align="center">

# ⚙️ **Kansas Frontier Matrix — Style Mixins Specification**  
`web/src/styles/mixins/README.md`

**Purpose:**  
Define the **style mixins** used across the KFM Web Platform — reusable CSS/utility patterns built on  
top of design tokens.  
Mixins provide consistent **focus rings**, **cards**, **panels**, **transitions**, **layout primitives**,  
and other patterns that ensure visual consistency, WCAG 2.1 AA accessibility, and FAIR+CARE-aware styling.

</div>

---

## 📘 Overview

Mixins in `web/src/styles/mixins/` are **abstractions built on design tokens** that:

- Encapsulate common layout and component patterns  
- Standardize focus styles, cards, panels, transitions, and layout grids  
- Guarantee **WCAG 2.1 AA** compliance when used correctly  
- Respect **FAIR+CARE** constraints (governance indicators, masking hints, etc.)  
- Provide predictable behavior across light/dark/high-contrast themes  
- Reduce code duplication in `components/**` and feature layers  

Mixins **must not** define new raw colors or spacing — they must consume token values from  
`web/src/styles/tokens/**` and map them into reusable patterns.

---

## 🧱 Directory Structure

~~~text
web/src/styles/mixins/
├── focus-ring.ts        # Standardized focus outline styles (A11y)
├── card.ts             # Card layout/spacing/shadow mixins
├── panel.ts            # Panel container & chrome mixins
├── layout.ts           # Flex/grid layout primitives for pages & shells
├── transitions.ts      # Motion/transition helpers that respect prefers-reduced-motion
└── scrollbar.ts        # Accessible scrollbar styling (where platform allows)
~~~

> File names are illustrative; exact names should match the implementation in the repo.

---

## 🧩 Mixin Modules

### 🎯 `focus-ring.ts`

Provides a **single canonical focus style** for all interactive elements:

- Focus outline thickness  
- Focus color (WCAG AA-compliant)  
- Offset/padding to avoid clipping  
- Dark/light/high-contrast safe variants  

Rules:

- All interactive elements (buttons, cards, map controls, tabs, etc.) must consume this mixin for focus styling.  
- No component may define its own “custom” focus outline that deviates from accessibility specs.  
- Must respect `prefers-reduced-motion` (no pulsing or animated outlines by default).

---

### 🃏 `card.ts`

Defines card presentation patterns:

- Padding based on spacing tokens  
- Border/radius tokens  
- Shadow tokens for elevation  
- Optional header/footer patterns  

Used by:

- DataCards  
- StoryCard  
- Shared `Card` component  
- Focus Mode/Story Node detail sections  

Design constraints:

- Must be theme-neutral (works in light/dark/high-contrast)  
- Must maintain adequate contrast between card and background  
- Must be usable with or without additional borders.

---

### 🧱 `panel.ts`

Defines panel-level containers:

- Side panels (e.g., Focus Mode, Story, Data Explorer)  
- Drawers  
- Docked tool panels  

Mixins include:

- Background + border tokens  
- Padding and internal spacing  
- Scrollbar integration (with `scrollbar.ts`)  
- Panel header/footer alignment  

Governance:

- Panel mixins used in governance UI must not obscure CARE labels or warnings.  

---

### 🧭 `layout.ts`

Contains **layout primitives**:

- Flexbox/grid helpers for:
  - Page shells  
  - Split views (map + timeline, map + narrative)  
  - Column/row sections  
- Safe responsive breakpoints (no hard-coded pixel hacks)  
- Utilities to ensure:
  - Sidebar + content interplay  
  - Drawer overlays do not block essential map/timeline content  

Constraints:

- Must avoid fragile layouts that break with large text/A11y modes.  
- Must be symmetrical enough to support different content densities (dense map vs. text-heavy story).

---

### 🔄 `transitions.ts`

Defines reusable motion helpers:

- Fade-in/fade-out  
- Expand/collapse  
- Slide-in/out for drawers and modals  
- Map/Timeline UI transitions  

Rules:

- All transitions must respect `prefers-reduced-motion: reduce`.  
- No indefinite or hyperactive animations.  
- No motion-based context that encodes critical meaning (i.e., no “shake” as only error indicator).

---

### 📜 `scrollbar.ts`

Provides consistent, accessible scrollbar styling (where supported):

- Slightly thicker grab areas for A11y  
- Theme-aware colors  
- Unobtrusive but visible thumbs  

Constraints:

- Must remain legible in light and dark themes.  
- Must not reduce usability on OS-level theming.

---

## ♿ Accessibility Requirements

Mixins are part of the **A11y contract**:

- `focus-ring` must be used for all focusable components.  
- `card`, `panel`, and `layout` mixins must preserve text legibility and responsiveness.  
- `transitions` must respect `prefers-reduced-motion` and avoid unnecessary animation.  
- `scrollbar` mixins should improve, not diminish, usability.

Any mixin that causes an A11y regression **must be corrected before merge**.

---

## 🔐 FAIR+CARE & Governance Constraints

While mixins are primarily visual:

- They must support **governance-specific visual semantics** (e.g., border colors for CARE labels, masked regions).  
- They must never encode governance meaning in ways not approved by FAIR+CARE (e.g., color-only status with no text).  
- They must be flexible enough to display:
  - SovereigntyNotice  
  - MaskingIndicator  
  - CAREBadge components without layout clipping or collisions.

Governance regressions triggered by mixin changes → **CI BLOCKER**.

---

## 📈 Telemetry & Observability

Mixins themselves do not emit telemetry, but:

- Changes to mixins may **change perceived behavior** (e.g., focus visibility, motion).  
- Visual regressions can show up as changes in A11y telemetry (e.g., fewer keyboard users successfully focusing controls).

When mixins are updated, relevant A11y and UX tests should be inspected.

---

## 🧪 Testing Requirements

At minimum, tests should verify:

- Focus outlines remain visible across themes.  
- Layout mixins do not break important viewports (mobile, tablet, desktop).  
- Transitions honor `prefers-reduced-motion`.  
- Cards/panels preserve adequate padding and legibility.  
- Scrollbars remain usable in both light and dark themes.

Tests are typically indirect (component-level), but the mixin layer must **not** introduce regressions.

---

## 🕰 Version History

| Version | Date       | Summary                                                                 |
|--------:|------------|-------------------------------------------------------------------------|
| v10.4.0 | 2025-11-15 | Mixins spec aligned with KFM-MDP v10.4.1; focus ring, card, panel, layout, transitions, scrollbar |
| v10.3.2 | 2025-11-14 | Tightened alignment between mixins and design tokens                    |
| v10.3.1 | 2025-11-13 | Initial mixins & base layout patterns                                  |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
FAIR+CARE Certified · Public Document · Version-Pinned  
Validated under MCP-DL v6.3 & KFM-MDP v10.4.1  

</div>

