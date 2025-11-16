---
title: "🎨 Kansas Frontier Matrix — Web Styles & Design System Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/styles/README.md"
version: "v10.4.0"
last_updated: "2025-11-15"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/web-styles-readme-v1.json"
governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Overview"
intent: "web-styles-overview"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk (style-only)"
sensitivity_level: "None"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false
provenance_chain:
  - "web/src/styles/README.md@v10.3.2"
  - "web/src/styles/README.md@v10.3.1"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "WebPageElement"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
json_schema_ref: "../../../schemas/json/web-styles-readme.schema.json"
shape_schema_ref: "../../../schemas/shacl/web-styles-readme-shape.ttl"
doc_uuid: "urn:kfm:doc:web-styles-readme-v10.4.0"
semantic_document_id: "kfm-doc-web-styles-readme"
event_source_id: "ledger:web/src/styles/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "a11y-adaptations"
  - "semantic-highlighting"
ai_transform_prohibited:
  - "summaries"
  - "speculative additions"
  - "unverified historical claims"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Public Document"
role: "overview"
lifecycle_stage: "stable"
ttl_policy: "Review every 12 months"
sunset_policy: "Superseded upon next style-system update"
---

<div align="center">

# 🎨 **Kansas Frontier Matrix — Web Styles & Design System Overview**  
`web/src/styles/README.md`

**Purpose:**  
Document the **design system architecture** for the Kansas Frontier Matrix Web Platform—defining  
tokens, themes, maps styling, accessibility layers, layout rules, and governance-aware visual  
constraints that ensure a consistent, ethical, accessible, and FAIR+CARE-aligned UI.

</div>

---

# 📘 Overview

The **Styles Layer** provides:

- Design tokens (color, spacing, typography, radii, shadows)  
- Light/dark theme configuration  
- Accessibility-first color choices  
- CARE-compliant color semantics (sovereignty, masking, provenance)  
- MapLibre styling rules  
- Layout spacing & grid rules  
- Component-level visual patterns  
- WCAG 2.1 AA guaranteed palettes  
- Deterministic theming utilities integrated with Tailwind  

This layer **must be stable**, **machine-extractable**, and **fully testable**, with no inline  
magic or ad-hoc styles across the codebase.

---

# 🧱 Directory Structure

~~~text
web/src/styles/
├── tokens/                     # Base design primitives for KFM UI
│   ├── color.tokens.ts         # WCAG AA palette + CARE colors
│   ├── spacing.tokens.ts       # Spacing scale (4px/8px grid)
│   ├── typography.tokens.ts    # Type scale, font weights, line-height rules
│   ├── radii.tokens.ts         # Border radius scale
│   ├── shadow.tokens.ts        # Shadow elevation system
│   └── zindex.tokens.ts        # Z-layer mapping (map > modal > drawer > HUD)
│
├── themes/                     # Light/dark mode themes
│   ├── light.ts                # Light mode CSS variables
│   └── dark.ts                 # Dark mode CSS variables
│
├── mixins/                     # Reusable patterns for CSS/Tailwind
│   ├── focus-ring.ts           # Visible focus indicators (A11y)
│   ├── card.ts                 # Standardized card layout
│   ├── panel.ts                # Panel shell mixins
│   └── transitions.ts          # Reduced-motion-safe transitions
│
├── maps/                       # MapLibre & Cesium styles
│   ├── maplibre.css            # Map UI, controls, popup styling
│   ├── layers.css              # Layer coloring, outlines, highlights
│   └── legend.css              # Accessible legend color ramps
│
└── globals.css                 # Base resets, Tailwind layers, variable mounts
~~~

---

# 🎨 Design System Philosophy

The design system is based on:

- **Functional consistency** across all features  
- **Accessibility-first design** (WCAG 2.1 AA)  
- **Ethical visualization**  
- **Semantic meaning through color**  
- **Predictable spacing + grids**  
- **Dark/light parity**  
- **Governance-aware theming**  

Color and shape are not merely aesthetic—they convey governance, focus, and data-quality meaning.

---

# 🎨 Tokens

Tokens define the **visual language** of the platform.

## 🎨 Color Tokens (`color.tokens.ts`)

Includes:

- Primary + secondary brand palette  
- High-contrast variants  
- CARE colors:
  - Public  
  - Low-Risk  
  - Restricted  
  - Sovereignty-Controlled  
  - Masked (H3)  
- Map highlight colors  
- A11y-safe gradients  
- Semantic statuses (error, warning, info)

All tokens must:

- Meet 4.5:1 minimum contrast  
- Work in dark/light themes  
- Avoid cultural misappropriation  
- Be accessible for color-blind users  

---

## 🔡 Typography Tokens (`typography.tokens.ts`)

Defines:

- Heading scale  
- Body text size  
- Line-height  
- Letter spacing  
- Narrative text presets for Story Nodes  

Requirements:

- Maintain readable text size across DPI  
- Support long historical names/labels  
- Provide large text mode for A11y  

---

## 📏 Spacing Tokens (`spacing.tokens.ts`)

- 4px modular scale  
- Consistent vertical rhythm  
- Accessible target sizes (min 44×44px)  

---

## 🧩 Shape & Layout Tokens

### Radii (`radii.tokens.ts`)
- Soft round corners for cards/panels  
- Accessible tap/drag zones  

### Shadows (`shadow.tokens.ts`)
- Shallow elevation scheme  
- No excessive parallax  
- Reduced-motion friendly  

### Z-index (`zindex.tokens.ts`)
Defines:

- Map  
- HUD  
- Modal  
- Governance drawer  
- Tooltips  

Order enforced consistently.

---

# 🌗 Themes

Themes are **CSS variable maps** for light/dark modes.

## 🌞 Light Mode (`light.ts`)
- High contrast  
- Low visual noise  
- Soft neutrals for long reading sessions  

## 🌙 Dark Mode (`dark.ts`)
- WCAG-safe dark backgrounds  
- Desaturated neutrals  
- Careful highlight colors (avoid neon/harsh colors)  

Theme switching must:

- Respect `prefers-color-scheme`  
- Transition with reduced-motion patterns  
- Maintain same information hierarchy  

---

# 🗺️ Map Styling

Styles under `maps/` govern MapLibre + Cesium:

- Layer outlines  
- Highlight states  
- Sovereignty/masking indicators  
- Story Node footprints  
- Raster preview frames  
- Accessible map controls  
- Color ramps for environmental layers  

All maps must avoid:

- Misleading visual interpretations  
- Overly saturated colors  
- Confusing color ramps  
- Indistinguishable boundaries  

Governance colors must remain **consistent** with CARE tokens.

---

# ♿ Accessibility Requirements

The Styles Layer must:

- Enforce visible focus rings  
- Guarantee accessible color contrast  
- Support reduced-motion  
- Use predictable spacing  
- Avoid text embedded in images  
- Provide alternative color tokens for:
  - Color-blind users  
  - High-contrast mode  

A11y failures → CI block.

---

# 🛡 Governance & FAIR+CARE Integration

Visual layers must:

- Clearly identify masked areas  
- Use CARE-compliant coloring  
- Avoid representing sensitive spatial features precisely  
- Mark AI-generated graphics  
- Provide sovereignty warnings  
- Avoid cultural misuse in icons or color choices  

All visual patterns undergo FAIR+CARE review.

---

# 📈 Telemetry Responsibilities

Styles influence telemetry through:

- Theme change events  
- High-contrast mode activations  
- Reduced-motion toggles  
- Map layer/legend interactions  

Telemetry must be:

- Non-PII  
- Schema-valid  
- Logged by `useTelemetry.ts`  
- Stored in `focus-telemetry.json`

---

# 🧪 Testing Requirements

Tests for the Styles Layer must include:

- WCAG contrast checks  
- Reduced-motion validation  
- Token integrity tests (no duplicates, no broken variables)  
- CSS snapshot tests (optional)  
- Governance color mapping tests  
- Map style consistency checks  

Location:

~~~text
tests/unit/web/styles/**
tests/integration/web/styles/**
~~~

---

# 🕰 Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v10.4.0 | 2025-11-15 | Full KFM-MDP v10.4 rewrite; added CARE/A11y theming rules, map style architecture, token system |
| v10.3.2 | 2025-11-14 | Updated color tokens + Story Node typography presets |
| v10.3.1 | 2025-11-13 | Initial styles overview |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
Reviewed under MCP-DL v6.3 and KFM-MDP v10.4  
FAIR+CARE Certified · Public Document · Version-Pinned  

</div>