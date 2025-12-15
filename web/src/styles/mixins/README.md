---
title: "⚙️ Kansas Frontier Matrix — Style Mixins Specification (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/styles/mixins/README.md"
version: "v11.2.6"
last_updated: "2025-12-15"

review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
release_stage: "Stable / Governed"
status: "Active / Enforced"
lifecycle_stage: "LTS"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.6/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.6/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/web-styles-mixins-v1.json"
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

doc_kind: "Specification"
intent: "web-styles-mixins"
role: "specification"
category: "Web · Styles · Mixins"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (style-only)"
sensitivity_level: "None"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false

provenance_chain:
  - "web/src/styles/mixins/README.md@v10.3.2"
  - "web/src/styles/mixins/README.md@v10.4.0"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "DefinedTermSet"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"

json_schema_ref: "../../../../schemas/json/web-styles-mixins.schema.json"
shape_schema_ref: "../../../../schemas/shacl/web-styles-mixins-shape.ttl"

doc_uuid: "urn:kfm:doc:web-styles-mixins-v11.2.6"
semantic_document_id: "kfm-doc-web-styles-mixins"
event_source_id: "ledger:web/src/styles/mixins/README.md"
immutability_status: "version-pinned"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "summaries"
  - "speculative additions"
  - "unverified visual semantics"
  - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "United States / Kansas"
classification: "Public Document"
ttl_policy: "Review every 12 months"
sunset_policy: "Superseded upon mixin system v12 update"
---

<div align="center">

# ⚙️ **Kansas Frontier Matrix — Style Mixins Specification (v11)**  
`web/src/styles/mixins/README.md`

**Purpose**  
Define the **style mixins** used across the KFM Web Platform — reusable, token-driven styling
patterns that standardize **focus rings**, **cards**, **panels**, **layout primitives**, and
**motion behavior** for WCAG 2.1 AA+ accessibility and governance-safe UI rendering.

<img src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Accessibility-WCAG_2.1_AA%2B-blueviolet" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

</div>

---

## 📘 Overview

Mixins in `web/src/styles/mixins/` are **governed styling primitives** built on top of the
design-token and theming layers. They exist to:

- Prevent ad-hoc or inconsistent styling across `web/src/**`.
- Ensure **consistent accessibility** (keyboard focus visibility, reduced-motion compliance, target sizes).
- Provide **theme-safe** patterns (light/dark/high-contrast parity).
- Keep governance-critical UI (CARE labels, sovereignty notices, masking indicators) **visible and unobstructed**.

### Non-negotiable constraints

Mixins MUST:

- Consume **tokens and theme variables** (no hard-coded hex colors or magic spacing).
- Remain **side-effect-free** (pure helpers; no DOM writes, no telemetry, no runtime mutation).
- Be safe across UI density modes (map-heavy views vs text-heavy narrative views).
- Avoid encoding governance meaning without accompanying text/icons (color alone is never sufficient).

Mixins MUST NOT:

- Replace governance overlays or attempt to “style away” restrictions.
- Introduce new semantic color meanings that conflict with `styles/tokens/**`.

### Cross-repo consistency note

The KFM monorepo also maintains **shared** design token and theming utilities under
`src/design-tokens/` and `src/theming/` (shared with the frontend). Mixins must remain compatible
with those shared sources when they are consumed by the web build pipeline.

---

## 🗂️ Directory Layout

> Filenames must match the repo. If implementation differs, update this tree and the module contracts together.

~~~text
web/src/styles/mixins/
├── 📄 README.md                  # This specification (governed)
├── 🧩 focus-ring.ts              # Canonical focus outline utilities (A11y)
├── 🧩 card.ts                    # Card chrome: padding/border/radius/elevation
├── 🧩 panel.ts                   # Panels/drawers/sheets: container + header/footer patterns
├── 🧩 layout.ts                  # Shell + split-view layout primitives (responsive-safe)
├── 🧩 transitions.ts             # Motion helpers honoring prefers-reduced-motion
└── 🧩 scrollbar.ts               # Optional accessible scrollbar patterns (platform-permitting)
~~~

---

## 🧭 Context

### How mixins fit into the style stack

The KFM web style stack is layered intentionally:

1. **Tokens** (`web/src/styles/tokens/**`)  
   Define the raw primitives (color, spacing, typography, radii, elevation, z-index).

2. **Themes** (`web/src/styles/themes/**`)  
   Map tokens into theme-aware CSS variables and high-contrast variants.

3. **Mixins** (`web/src/styles/mixins/**`)  
   Compose tokens/themes into reusable, testable UI patterns.

4. **Components** (`web/src/components/**`)  
   Consume mixins (directly or via shared primitives) to render consistent UI.

### Where mixins are expected to be used

Mixins SHOULD be the default styling source for:

- Shared UI primitives (buttons, tabs, tooltips, modals, toasts).
- Panels used by Focus Mode and Story Node views.
- Map and timeline chrome (controls, HUD framing, legends) where “app UI” is styled.
- Governance UI elements (badges, notices, masking banners) to avoid clipping or poor contrast.

---

## 🧱 Architecture

### Architectural invariants

- **Single-source focus styling:** all focusable UI uses the same focus-ring rules.
- **Theme parity:** every mixin must render legibly in light/dark/high-contrast.
- **A11y-first motion:** transitions must degrade gracefully under `prefers-reduced-motion`.
- **Composable primitives:** mixins may compose other mixins (e.g., `panel` composing `scrollbar`),
  but must not import from `components/**`.

### Module contracts

#### 🎯 `focus-ring.ts`

Responsibilities:

- Provide a single, canonical focus-visible style:
  - consistent outline thickness and offset
  - token-driven colors for each theme
  - safe behavior for dense controls (map buttons) and large interactive regions (cards)

Non-goals:

- Animated focus effects by default (avoid pulsing/flash).
- Per-component “bespoke” focus styling.

#### 🃏 `card.ts`

Responsibilities:

- Standardize card chrome used throughout the UI:
  - padding and spacing rhythm
  - border/radius
  - elevation/shadow (if used)
  - safe separation between card background and page background

Non-goals:

- Encoding governance state (e.g., “restricted” = red border) inside the base card mixin.
  Governance framing must be done by governance components using approved semantics.

#### 🧱 `panel.ts`

Responsibilities:

- Provide consistent containers for:
  - docked panels (Focus, Story, Explorer)
  - drawers/sheets
  - panel headers/footers
  - scroll containment without content clipping (especially governance notices)

Non-goals:

- Overriding the z-index stacking model defined by tokens.
- Obscuring map/timeline safety overlays.

#### 🧭 `layout.ts`

Responsibilities:

- Provide layout primitives for page shells and split views:
  - responsive-safe, large-text-safe patterns
  - predictable spacing and gutters from tokens
  - safe constraints for map + narrative + timeline compositions

Non-goals:

- Pixel-perfect hacks or fixed heights that break under A11y modes.

#### 🔄 `transitions.ts`

Responsibilities:

- Provide motion utilities for:
  - modal/drawer transitions
  - expand/collapse sections
  - opacity/translate transitions for UI chrome

Hard requirement:

- MUST honor `prefers-reduced-motion: reduce` by disabling or shortening non-essential motion.

Non-goals:

- Motion as the only signal (errors, warnings, or governance restrictions must not be motion-only).

#### 📜 `scrollbar.ts`

Responsibilities:

- Optional, theme-aware scrollbar affordances where supported:
  - usable thumb size
  - sufficient contrast
  - non-destructive overrides (don’t fight OS accessibility settings)

Non-goals:

- “Custom scroll” UI that interferes with platform conventions.

---

## ⚖ FAIR+CARE & Governance

Mixins are a style layer, but they are still governance-relevant because they can
accidentally hide or downplay governed UI signals.

Mixins MUST support (and never clip/obscure):

- CARE labels and risk chips
- sovereignty notices
- masking indicators and “why masked?” banners
- attribution/license blocks

Mixins MUST NOT:

- Reduce warning salience below normal content in any theme.
- Make governance indicators “optional” by styling them into invisibility.

Any mixin change that makes governed content less legible or less discoverable is a
governance regression and must be treated as a release blocker.

---

## 🧪 Validation & CI/CD

### Expected validations

At minimum, changes to mixins SHOULD be covered by:

- Contrast checks for focus rings and critical chrome in all themes (AA+ targets).
- Reduced-motion behavior checks (`prefers-reduced-motion`).
- Layout resilience checks (small screens, large text, dense UI).
- Visual regression snapshots for:
  - panel headers/footers
  - cards in list views
  - focus ring appearance on common controls

### Documentation compliance

This file is governed by KFM‑MDP and must remain:

- front‑matter complete,
- H2 headings registry‑compliant,
- directory layout boxed (`~~~text`),
- version history present and updated when behavior changes.

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-15 | Upgraded to KFM‑MDP v11.2.6; normalized approved H2 headings + ordering; added required governance/ethics/sovereignty refs; added release signature/attestation refs; clarified mixin contracts and cross-repo token/theming alignment. |
| v10.4.0 | 2025-11-15 | Mixins spec aligned with KFM‑MDP v10.4.1; documented focus ring, card, panel, layout, transitions, scrollbar. |
| v10.3.2 | 2025-11-14 | Tightened alignment between mixins and design tokens. |
| v10.3.1 | 2025-11-13 | Initial mixins & base layout patterns. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
FAIR+CARE Certified · Public Document · Version-Pinned  

[⬅️ Back to Styles Overview](../README.md) · [💻 Web Source Overview](../../README.md) · [🛡 Governance](../../../../docs/standards/governance/ROOT-GOVERNANCE.md) · [🧾 FAIR+CARE](../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) · [🪶 Sovereignty](../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

</div>
