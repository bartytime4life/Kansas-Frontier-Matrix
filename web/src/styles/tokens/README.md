---
title: "🎨 Kansas Frontier Matrix — Design Tokens Specification (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/styles/tokens/README.md"
version: "v10.4.0"
last_updated: "2025-11-15"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/web-styles-tokens-v1.json"
governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.1"
status: "Active / Enforced"
doc_kind: "Specification"
intent: "web-styles-tokens"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
sensitivity_level: "None"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false
provenance_chain:
  - "web/src/styles/tokens/README.md@v10.3.2"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "DefinedTermSet"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
json_schema_ref: "../../../../schemas/json/web-styles-tokens.schema.json"
shape_schema_ref: "../../../../schemas/shacl/web-styles-tokens-shape.ttl"
doc_uuid: "urn:kfm:doc:web-styles-tokens-v10.4.0"
semantic_document_id: "kfm-doc-web-styles-tokens"
event_source_id: "ledger:web/src/styles/tokens/README.md"
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
sunset_policy: "Superseded upon token system v11 update"
---

<div align="center">

# 🎨 **Kansas Frontier Matrix — Design Tokens Specification**  
`web/src/styles/tokens/README.md`

**Purpose:**  
Define the **design tokens** that power the KFM Web Platform: color, spacing, typography, radii, shadows, z-index,
and other visual primitives.  
These tokens enforce **visual consistency, accessibility (WCAG 2.1 AA)**, governance marking, and reproducibility
across all UI components.

</div>

---

# 📘 Overview

Design tokens are **the lowest-level design primitives** used throughout the KFM interface.  
They provide:

- Predictable cross-application styling  
- Consistent spacing + typography  
- Accessible color choices  
- Governance-aware color semantics (CARE, sovereignty, masking)  
- A11y-friendly motion rules  
- Deterministic theming for dark/light modes  
- Complete auditability by FAIR+CARE governance reviewers

These tokens are used by:

- `components/**`
- `styles/mixins/**`
- `styles/themes/**`
- Tailwind configuration

---

# 🧱 Directory Structure

~~~text
web/src/styles/tokens/
├── color.tokens.ts        # WCAG AA color palettes + CARE/sovereignty/masking colors
├── spacing.tokens.ts      # 4px modular spacing scale
├── typography.tokens.ts   # Type scale, line-height, weights, and accessibility rules
├── radii.tokens.ts        # Border radius scale for components and shells
├── shadow.tokens.ts       # Shadow elevation system (reduced-motion safe)
└── zindex.tokens.ts       # Global z-layer hierarchy (map, HUD, panels, modals)
~~~

---

# 🧩 Token Categories

---

## 🎨 **Color Tokens (`color.tokens.ts`)**

Color tokens include:

- **Primary palette** (brand-aligned, high contrast)
- **Secondary palette** (neutral, background, and text colors)
- **CARE palette**  
  - Public  
  - Low-risk  
  - Restricted  
  - Sovereignty  
  - Masked (generalized location)
- **Governance palette** (provenance, license, warnings)
- **A11y palette** (error, warning, success, info—WCAG AA compliant)
- **Map layers palette** (visibility-safe for basemaps, boundaries, highlights)

Rules:

- All colors must meet **WCAG 2.1 AA contrast minimums**  
- Motion-related artifacts (like shimmer) must use reduced-motion variants  
- No token may imply cultural meaning or classification not approved by FAIR+CARE

---

## 📏 **Spacing Tokens (`spacing.tokens.ts`)**

Defines a **4px modular scale**:

- `s0` = 0px  
- `s1` = 4px  
- `s2` = 8px  
- …  
- `s10` = 40px  
- etc.

Rules:

- All component padding/margins must use spacing tokens  
- Interactive elements must satisfy **44×44px minimum target size**  
- Spacing tokens cannot encode visual meaning (pure geometry)

---

## 🔡 **Typography Tokens (`typography.tokens.ts`)**

Defines:

- Type scale (e.g., `t0` to `t6`)  
- Font weights (400–700)  
- Line heights tailored for long-form Story Node reading  
- Large-text mode multipliers  
- Narrative modes for ADA compliance  

Typography must:

- Support long geographic and Indigenous terms  
- Use readable minimum sizes  
- Honor OS/browser font preferences

---

## 🟦 **Radii Tokens (`radii.tokens.ts`)**

Defines radii used across components:

- `r-none`  
- `r-sm`  
- `r-md`  
- `r-lg`  
- `r-xl`  
- `r-2xl`

Applied to:

- Cards  
- Panels  
- Buttons  
- Modals  
- Map UI shells  

Radii must be consistent across UI components.

---

## 🌫 **Shadow Tokens (`shadow.tokens.ts`)**

Defines shadow layers such as:

- `shadow-0` (none)  
- `shadow-1` (very subtle)  
- `shadow-2` (panels)  
- `shadow-3` (drawers, dialogs)  
- `shadow-4` (modals)  

Rules:

- Must be **reduced-motion-safe**  
- Must avoid excessive depth (ethical/neutral design)  
- Must maintain readability in dark mode

---

## 🗂 **Z-Index Tokens (`zindex.tokens.ts`)**

Defines the entire visual stacking order:

- `z-map` — Map canvas base  
- `z-map-hud` — Cursor HUD  
- `z-panels` — Side panels  
- `z-drawers` — DetailDrawer  
- `z-modals` — Modal dialogs  
- `z-tooltips` — Tooltip overlays  
- `z-top` — Emergency overlays + CARE warnings

Rules:

- No ad-hoc z-index declarations allowed  
- Components must use these tokens exclusively  

---

# ♿ Accessibility Requirements

Design tokens must:

- Guarantee **WCAG AA contrast**  
- Provide predictable scale changes in large-text mode  
- Use safe motion paths for reduced-motion users  
- Maintain semantic neutrality (no color tokens with cultural meaning unless CARE-approved)

---

# 🔐 FAIR+CARE Requirements

All tokens must:

- Avoid culturally inappropriate color semantics  
- Use CARE-specific colors only for CARE labeling UI  
- Support sovereign data masking (explicit masked colors)  
- Align with governance metadata (provenance, license, sovereignty)  
- Avoid reinforcing bias via color or typography

Failures → **CI BLOCKER**

---

# 🧪 Testing Requirements

Token tests must validate:

- WCAG contrast compliance  
- Token uniqueness  
- Proper dark/light theme accessibility  
- No unused or dangling token definitions  
- Correct integration with mixins + themes  

Tests live in:

~~~text
tests/unit/web/styles/tokens/**
tests/integration/web/styles/tokens/**
~~~

---

# 🕰 Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v10.4.0 | 2025-11-15 | Fully refactored token system to KFM-MDP v10.4.1; added CARE-aware palettes |
| v10.3.2 | 2025-11-14 | Added A11y-safe typography + spacing enforcement |
| v10.3.1 | 2025-11-13 | Initial design token baseline |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
FAIR+CARE Certified · Public Document · Version-Pinned  
Validated under MCP-DL v6.3 & KFM-MDP v10.4.1  

</div>

