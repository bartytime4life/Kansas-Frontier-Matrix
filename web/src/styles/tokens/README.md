---
title: "🎨 Kansas Frontier Matrix — Design Tokens Specification (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/styles/tokens/README.md"
version: "v11.2.6"
last_updated: "2025-12-15"

review_cycle: "Quarterly · FAIR+CARE Council & Web Architecture Board"
release_stage: "Stable / Governed"
status: "Active / Enforced"
lifecycle_stage: "LTS"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.6/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.6/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/web-styles-tokens-v1.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"
signature_ref: "../../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../../releases/v11.2.6/slsa-attestation.json"

governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"

status_category: "Design System"
doc_kind: "Specification"
intent: "web-styles-tokens"
role: "specification"
category: "Web · Styles · Tokens"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity_level: "None"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false

provenance_chain:
  - "web/src/styles/tokens/README.md@v10.3.2"
  - "web/src/styles/tokens/README.md@v10.4.0"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "DefinedTermSet"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"

json_schema_ref: "../../../../schemas/json/web-styles-tokens.schema.json"
shape_schema_ref: "../../../../schemas/shacl/web-styles-tokens-shape.ttl"

doc_uuid: "urn:kfm:doc:web-styles-tokens-v11.2.6"
semantic_document_id: "kfm-doc-web-styles-tokens"
event_source_id: "ledger:web/src/styles/tokens/README.md"
immutability_status: "version-pinned"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "summaries"
  - "speculative-additions"
  - "unverified-visual-semantics"
  - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "United States / Kansas"
classification: "Public Document"
ttl_policy: "Review required every 12 months"
sunset_policy: "Superseded upon next design token system major revision"
---

<div align="center">

# 🎨 **Kansas Frontier Matrix — Design Tokens Specification**  
`web/src/styles/tokens/README.md`

Design tokens are the **canonical visual primitives** for the KFM Web Platform (React + MapLibre + Cesium):  
**color, spacing, typography, radii, shadows, z-index**, and related semantics that enable a UI that is:

- **deterministic** (no ad-hoc styling drift),
- **accessible** (WCAG 2.1 AA+),
- **governance-aware** (supports CARE / sovereignty / masking indicators),
- **portable** (tokens can be consumed by themes, mixins, Tailwind utilities, and map UI styling).

<img src="https://img.shields.io/badge/Docs-MCP--DL_v6.3-blue" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-6A5ACD" />
<img src="https://img.shields.io/badge/Accessibility-WCAG_2.1_AA%2B-success" />
<img src="https://img.shields.io/badge/License-MIT-green" />

</div>

---

## 📘 Overview

Design tokens are the **lowest-level governed interface** between design intent and implementation. They exist to ensure that every surface in the KFM web UI (Story Node cards, Focus Mode panels, maps, timelines, explorers, overlays) can be rendered:

- **consistently** across features and releases,
- **safely** across accessibility modes and user preferences,
- **without bypassing governance semantics** (e.g., masking and sovereignty indicators remain readable and unambiguous),
- **without injecting raw, unreviewed styling decisions** into feature code.

### Scope

This specification governs:

- `web/src/styles/tokens/**` (this directory)
- how tokens are consumed by:
  - `web/src/styles/themes/**`
  - `web/src/styles/mixins/**`
  - `web/src/styles/maps/**` (map UI CSS, not the MapLibre style JSON itself)
  - UI components and pages via Tailwind utilities and/or CSS variables

### System alignment (shared token sources)

KFM maintains **shared token and theming assets** under the repository root `src/` tree:

- `src/design-tokens/` — design tokens shared with the frontend (style constants)
- `src/theming/` — theming utilities shared with the frontend (styles, themes)

`web/src/styles/tokens/**` MUST NOT drift from those shared sources. If the project uses an automated sync/build step, it MUST preserve this directory’s public surface and the rules in this document.

### Non-goals (explicit)

- Tokens do **not** define or override governance policy. They only provide **visual affordances** used by governance components.
- Tokens do **not** embed narrative meaning (e.g., “good/bad history”) beyond generic UI semantics (success/warn/error) and explicitly approved CARE/sovereignty indicators.
- Tokens do **not** replace themes; themes map tokens into runtime CSS variables.

### Hard invariants

- No feature code may introduce raw hex colors, raw z-index numbers, or ad-hoc spacing scales when an equivalent token exists.
- Tokens MUST be:
  - **theme-safe** (usable across light/dark/high-contrast),
  - **A11y-safe** (contrast and focus visibility),
  - **machine-extractable** (stable exports; no runtime randomness),
  - **reviewable** (changes are small, justified, and tested).

---

## 🗂️ Directory Layout

~~~text
web/src/styles/tokens/
├── 📄 README.md                 # This specification (KFM-MDP v11.2.6)
├── 🎨 color.tokens.ts           # Color primitives + semantic colors + governance affordance colors
├── 📏 spacing.tokens.ts         # Spacing + sizing primitives (includes min target sizes)
├── 🔤 typography.tokens.ts      # Type scale, font stacks, narrative presets, A11y multipliers
├── 🟦 radii.tokens.ts           # Border radius scale for shells, cards, controls, overlays
├── 🌫 shadow.tokens.ts          # Elevation system (motion-safe; theme-aware)
└── 🗂 zindex.tokens.ts          # Global stacking order (no ad-hoc z-index values)
~~~

---

## 🧭 Context

### How tokens flow through the web UI

Tokens are not consumed directly by most feature components. The intended path is:

1. **Tokens** (`web/src/styles/tokens/**`) define canonical primitives and semantic groupings.
2. **Themes** (`web/src/styles/themes/**`) map token values → runtime CSS variables.
3. **Mixins** (`web/src/styles/mixins/**`) compose theme variables into reusable patterns (focus rings, cards, panels).
4. **Consumers**:
   - Tailwind utilities and design primitives
   - map UI CSS (`web/src/styles/maps/**`)
   - cross-cutting overlays (governance, A11y affordances)
   - component styles (only via mixins / theme variables / Tailwind)

This layering prevents:
- hidden styling drift,
- duplication of semantic meaning,
- inaccessible one-off UI patterns.

### What “tokenized” means in KFM

A style decision is “tokenized” when it is:

- defined once (in tokens),
- applied consistently (via theme/mixins/utilities),
- validated (contrast, completeness, regressions),
- governance-safe (does not reduce clarity of warnings/masking).

### Compatibility expectations

- Token additions are typically **non-breaking**.
- Token removals or semantic changes are **breaking** and MUST be versioned and migrated.
- Every token used by production UI MUST be available in every supported theme.

---

## 🧱 Architecture

### Token layers

KFM tokens SHOULD be organized into three conceptual layers (even if physically stored together):

1. **Primitives**  
   Raw “design materials” such as palette steps, spacing units, font weights.

2. **Semantic tokens**  
   Meaningful UI intents such as `text.primary`, `surface.panel`, `border.muted`, `focus.ring`.

3. **Governance affordance tokens**  
   Colors and emphasis helpers used by governance components:
   - CARE label badges
   - sovereignty notices
   - masking / generalization indicators
   - provenance chips

Governance tokens MUST NOT be interpreted as governance decisions; they are visual affordances used after policy decisions are made elsewhere.

### Export conventions

Each token file MUST export:

- a stable `const` token object (`as const`) for machine extraction,
- a derived type (`typeof tokens[keyof ...]`) for safe consumption,
- optional helper selectors (e.g., “semantic” subsets) that remain deterministic.

Example (shape only; not canonical values):

~~~ts
// color.tokens.ts (illustrative shape; values in repo define the canonical palette)
export const colorTokens = {
  primitive: {
    neutral: {
      0: "#FFFFFF",
      900: "#0B0B0C",
    },
  },
  semantic: {
    text: {
      primary: "var(--kfm-color-text-primary)",
      muted: "var(--kfm-color-text-muted)",
    },
    surface: {
      page: "var(--kfm-color-surface-page)",
      panel: "var(--kfm-color-surface-panel)",
    },
    focus: {
      ring: "var(--kfm-color-focus-ring)",
    },
  },
  governance: {
    care: {
      public: "var(--kfm-color-care-public)",
      restricted: "var(--kfm-color-care-restricted)",
      sovereign: "var(--kfm-color-care-sovereign)",
      masked: "var(--kfm-color-care-masked)",
    },
  },
} as const;

export type ColorTokens = typeof colorTokens;
~~~

### Naming conventions (normative)

Token naming MUST be:

- **semantic**, not descriptive by appearance  
  Prefer `text.primary` over `text.blue`.
- **stable**, not feature-specific  
  Prefer `surface.panel` over `focusPanelBackground`.
- **explicit about function**, especially for governance affordances  
  Prefer `governance.masked.*` over `hexMask*`.

CSS variable names SHOULD:

- be prefixed (e.g., `--kfm-*`) to prevent collisions,
- use stable nouns (`text`, `surface`, `border`, `focus`, `care`, `sovereignty`, `masking`),
- avoid embedding app version numbers (versioning is handled at doc/release level).

### Color tokens

Color tokens MUST support:

- **Text and surface hierarchy** (page → panel → card → overlay)
- **Interactive states** (hover, active, disabled, selected)
- **Status semantics** (info/success/warning/error)
- **Focus visibility** (focus ring and focus background must remain clear in every theme)
- **Governance affordances**:
  - CARE badges and severity cues
  - sovereignty notices and warning banners
  - masking/generalization indicators and legends
  - provenance chips and attribution links

Color constraints:

- All text colors used on surfaces MUST meet WCAG AA+ contrast targets.
- Tokens that are used to convey meaning MUST be paired with non-color affordances (iconography and/or text) at the component level.
- Map-related colors MUST avoid ramps that mislead interpretation (e.g., “hotter means worse” unless explicitly labeled).

### Spacing tokens

Spacing tokens MUST:

- follow a modular scale (commonly 4px base),
- include explicit minimum tap/target sizes to enforce accessibility,
- remain purely geometric (spacing tokens do not encode meaning).

Example (shape only):

~~~ts
export const spacingTokens = {
  px: {
    0: 0,
    1: 4,
    2: 8,
    3: 12,
    4: 16,
    5: 20,
    6: 24,
  },
  a11y: {
    minTarget: 44,
    minFocusOffset: 2,
  },
} as const;
~~~

### Typography tokens

Typography tokens MUST:

- provide a consistent type scale suitable for:
  - dense UI controls (map, timeline),
  - long-form narratives (Story Nodes),
  - structured reasoning panels (Focus Mode),
- support large-text modes without layout collapse,
- avoid hard-coded, culturally specific “display fonts” unless explicitly approved and documented.

Typography tokens SHOULD include:

- font stack definitions (system-safe defaults),
- font weights and line-heights,
- narrative presets (reading mode, condensed mode, caption mode).

### Radii tokens

Radii tokens MUST:

- define a small set of consistent radii values,
- avoid per-component bespoke radii when a token exists,
- keep interactive controls comfortably touchable and visually stable.

### Shadow tokens

Shadow tokens MUST:

- define a small elevation model aligned with panels/drawers/modals,
- be theme-safe (dark mode shadows must not appear as “glow” unless explicitly intended),
- avoid motion illusion or depth cues that imply meaning.

### Z-index tokens

Z-index tokens MUST:

- define a single global stacking order used across the app,
- prevent ad-hoc z-index usage,
- ensure governance and safety overlays can always be placed above content when required.

Recommended conceptual stack (exact numbers are implementation-defined and tokenized):

- map canvas
- map HUD
- side panels / drawers
- modals
- tooltips / toasts
- emergency overlays / required governance overlays

### Change management (normative)

Token changes MUST follow this sequence:

1. Define or adjust token(s) in `web/src/styles/tokens/**`.
2. Map token(s) in all relevant themes under `web/src/styles/themes/**`.
3. Ensure mixins/utilities reference the token(s) (no raw values).
4. Update any dependent map UI CSS, if relevant.
5. Add or update validation/tests (contrast, completeness, regressions).
6. Update this document and version history.

Breaking changes MUST include:
- migration guidance (what token to use instead),
- a deprecation period when feasible (aliases + JSDoc `@deprecated`),
- validation that no production components depend on removed tokens.

---

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  TOK["Tokens<br/>web/src/styles/tokens/**"] --> THM["Themes<br/>web/src/styles/themes/**<br/>token→CSS var maps"]
  THM --> CSSV["CSS Variables<br/>:root[data-theme=…]"]
  CSSV --> MIX["Mixins<br/>web/src/styles/mixins/**<br/>reusable patterns"]
  CSSV --> TW["Tailwind Utilities<br/>(via vars)"]
  MIX --> UI["Components & Pages<br/>web/src/components/**<br/>web/src/pages/**"]
  TW --> UI
  CSSV --> MAPCSS["Map UI CSS<br/>web/src/styles/maps/**"]
  MAPCSS --> UI
~~~

---

## 📦 Data & Metadata

### Machine-extractable requirements

This token system MUST remain machine-extractable:

- Token exports MUST be deterministic (`as const`, stable names).
- Token files MUST avoid runtime environment dependence.
- Token surfaces SHOULD be analyzable by:
  - schema checks (presence/shape),
  - lint rules (no raw colors in components),
  - accessibility validators (contrast checks).

### Release and provenance alignment

This specification is release-pinned and points to:

- SBOM (`sbom_ref`)
- release manifest (`manifest_ref`)
- signature (`signature_ref`)
- SLSA attestation (`attestation_ref`)

Token changes are part of the governed release surface and MUST be reviewable in the same way as code.

---

## 🌐 STAC, DCAT & PROV Alignment

This document is a governed specification and can be represented in the platform’s metadata stack:

- **DCAT**: treat as a documentation `dcat:Dataset` or `dcat:CatalogRecord`
  - `semantic_document_id` → `dct:identifier`
  - Markdown is a `dcat:Distribution` (`mediaType: text/markdown`)
- **STAC**: may be represented as a non-spatial STAC Item
  - `geometry: null`
  - `properties.datetime = last_updated`
- **PROV-O**: treat as `prov:Plan`
  - updates and validations are `prov:Activity`
  - reviewers and CI agents are `prov:Agent`

---

## 🧪 Validation & CI/CD

### Documentation compliance (KFM-MDP)

This file MUST pass documentation compliance profiles (CI enforced), including:

- `markdown-lint` (H1/H2 rules, formatting constraints)
- `schema-lint` (front-matter schema compliance)
- `metadata-check` (required keys present and consistent)
- `footer-check` (governance links + footer ordering)
- `provenance-check` (provenance chain + version history coherence)

### Token-specific validation (normative)

Token changes MUST be validated for:

- **Contrast safety**
  - text-on-surface combinations used by core UI
  - focus ring visibility on all supported surfaces
  - legend/swatches readability in all themes
- **Theme completeness**
  - every semantic token used in UI is mapped in every theme
  - no orphan CSS variables
- **Uniqueness / determinism**
  - no duplicate token keys with divergent meaning
  - stable exports for machine extraction
- **Governance visibility**
  - masking indicators remain unmistakable
  - sovereignty notices remain prominent
  - CARE badges remain legible and not color-only

Recommended test locations (project-conventional):

~~~text
tests/unit/web/styles/tokens/**
tests/integration/web/styles/tokens/**
~~~

---

## ⚖ FAIR+CARE & Governance

Tokens must enable governance UI to be **clear, non-deceptive, and accessible**.

### Governance-safe semantics

- CARE and sovereignty colors MUST be used only by approved governance components (badges/notices/overlays).
- Tokens MUST NOT encode governance decisions. They only provide visual affordances for already-computed policy outcomes.
- No governance indicator may rely on color alone:
  - include labels, icons, or patterns at the component level
  - ensure screen-reader equivalents exist where appropriate

### Masking and sensitive visualization

Where masking/generalization is required:

- Tokens used for masked regions MUST make masking visually obvious.
- Masking affordances MUST remain distinguishable across themes.
- Token changes that reduce the clarity of masking are considered governance regressions and MUST be rejected.

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-15 | Upgraded to KFM-MDP v11.2.6; enforced H1/H2 registry compliance; clarified shared token alignment with `src/design-tokens/` and theming alignment with `src/theming/`; expanded architecture, validation, and governance constraints. |
| v10.4.0 | 2025-11-15 | Refactored token system to KFM-MDP v10.4.1; strengthened CARE-aware palettes and accessibility rules. |
| v10.3.2 | 2025-11-14 | Added A11y-safe typography and spacing enforcement; tightened governance semantics. |
| v10.3.1 | 2025-11-13 | Initial design token baseline. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
FAIR+CARE Certified · Public Document · Version-Pinned

[⬅️ Back to Styles Overview](../README.md) · [🌗 Themes](../themes/README.md) · [⚙️ Mixins](../mixins/README.md) · [🗺️ Map Styling](../maps/README.md) · [🛡 Governance Charter](../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
