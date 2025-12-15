---
title: "🎨 Kansas Frontier Matrix — Web Styles & Design System Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/styles/README.md"
version: "v11.2.6"
last_updated: "2025-12-15"

review_cycle: "Quarterly · FAIR+CARE Council & Web Architecture Board"
release_stage: "Stable / Governed"
status: "Active / Enforced"
lifecycle: "Long-Term Support (LTS)"
lifecycle_stage: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.6/manifest.zip"
telemetry_ref: "../../../releases/v11.2.6/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/web-styles-readme-v11.json"
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

status_category: "Architecture"
doc_kind: "Overview"
intent: "web-styles-overview"
role: "overview"
category: "Web · Styles · Design System"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk (style-only)"
sensitivity_level: "None"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false

provenance_chain:
  - "web/src/styles/README.md@v10.3.1"
  - "web/src/styles/README.md@v10.3.2"
  - "web/src/styles/README.md@v10.4.0"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "WebPageElement"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"

json_schema_ref: "../../../schemas/json/web-styles-readme.schema.json"
shape_schema_ref: "../../../schemas/shacl/web-styles-readme-shape.ttl"

doc_uuid: "urn:kfm:doc:web-styles-readme:v11.2.6"
semantic_document_id: "kfm-doc-web-styles-readme"
event_source_id: "ledger:web/src/styles/README.md"
immutability_status: "version-pinned"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "a11y-adaptations"
  - "semantic-highlighting"
ai_transform_prohibited:
  - "summaries"
  - "speculative additions"
  - "unverified historical claims"
  - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
classification: "Public Document"
ttl_policy: "Review required every 12 months"
sunset_policy: "Superseded upon next style-system update"
---

<div align="center">

# 🎨 **Kansas Frontier Matrix — Web Styles & Design System Overview (v11)**  
`web/src/styles/README.md`

**Purpose**  
Define the **governed styling + design system contract** for the KFM Web Platform’s frontend (`web/src/styles/**`):  
design tokens, themes, map/3D styling primitives, accessibility-first constraints, and governance-safe visual semantics.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../mcp/MCP-README.md)
· [![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Aligned-orange)](../../../docs/standards/faircare/FAIRCARE-GUIDE.md)
· [![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../LICENSE)

</div>

---

## 📘 Overview

`web/src/styles/**` is the **single styling authority** for the KFM Web Platform UI layer. It exists to ensure that:

- **Tokens** (color, spacing, typography, radii, elevation, z-index, motion) are deterministic and reusable.
- **Themes** (light/dark/high-contrast behaviors) are consistent and accessibility-safe.
- **Map and 3D styling** (MapLibre / Cesium-related visual primitives) follows the same semantic rules as the rest of the UI.
- **Governance visualization semantics** (CARE labels, masking indicators, provenance affordances) are consistent and cannot be “styled away.”
- UI remains **WCAG 2.1 AA+** compliant by construction (contrast, focus, reduced motion, readable typography).

### Alignment with shared monorepo styling assets

The monorepo also contains:
- `src/design-tokens/` — design tokens intended to be shared with the frontend
- `src/theming/` — theming utilities intended to be shared with the frontend

`web/src/styles/**` MUST remain aligned with those shared sources when present and approved for use. If local tokens/themes exist in `web/src/styles/**`, they are treated as **frontend bindings** (or a generated mirror) rather than a competing source-of-truth.

### Non-negotiable constraints

- **No ad-hoc styling** in features: avoid “random hex codes,” one-off spacing, and inline overrides.
- **No governance-erasing styles**: warnings, masking banners, provenance chips must remain readable and prominent.
- **No accessibility regressions**: contrast + focus states are mandatory and enforced in CI.

---

## 🗂️ Directory Layout

~~~text
web/src/styles/
├── 📄 README.md                         # This document (styles & design system contract)
├── 📄 global.css                        # Global CSS entry: resets + Tailwind layers + CSS vars mount
│
├── 📁 tokens/                           # Design primitives (typed)
│   ├── 📄 color.tokens.ts               # Color palette + semantic colors (incl. governance semantics)
│   ├── 📄 spacing.tokens.ts             # Spacing scale and rhythm rules
│   ├── 📄 typography.tokens.ts          # Type scale, weights, line-height, reading presets
│   ├── 📄 radii.tokens.ts               # Radius scale (cards, panels, controls)
│   ├── 📄 shadow.tokens.ts              # Elevation system (shadows), reduced-motion safe
│   └── 📄 zindex.tokens.ts              # Z-layer ordering (map, HUD, modal, overlay, tooltip)
│
├── 📁 themes/                           # Theme definitions (CSS variable maps)
│   ├── 📄 light.ts                      # Light theme variable map
│   └── 📄 dark.ts                       # Dark theme variable map
│
├── 📁 mixins/                           # Reusable styling helpers (typed)
│   ├── 📄 focus-ring.ts                 # Visible focus indicators (A11y)
│   ├── 📄 card.ts                       # Standard card + reading surfaces
│   ├── 📄 panel.ts                      # Panel shells (Focus, Explorer, Story)
│   └── 📄 transitions.ts                # Reduced-motion-safe transitions
│
├── 📁 maps/                             # Map/3D related style primitives
│   ├── 📄 maplibre.css                  # MapLibre controls, popups, container styling
│   ├── 📄 layers.css                    # Layer outlines/highlights + selection styling
│   └── 📄 legend.css                    # Accessible legends + ramp presentation rules
│
└── 📁 (optional)/                       # Additional governed style assets (only if approved)
    └── 📄 <reserved>                    # Keep additions reviewed and documented here
~~~

### Related shared sources (outside `web/`)

These are repo-level shared assets (do not duplicate without an explicit reason):

- `src/design-tokens/` — shared token definitions for consistent styling across subsystems.
- `src/theming/` — shared theming utilities (e.g., variable-map builders, contrast helpers).
- `src/icons/` — shared icon assets (avoid bespoke icon sets unless reviewed).

---

## 🧱 Architecture

### 1) Token model

Tokens encode the **visual language** of KFM and must be:

- **Semantic-first**: encode meaning (status, governance, emphasis) rather than aesthetics.
- **Deterministic**: token outputs do not depend on runtime randomness or device quirks.
- **Theme-safe**: tokens must function in light/dark and with high-contrast usage modes.
- **Map-safe**: token semantics must remain interpretable in both “UI surfaces” and “map surfaces.”

#### Token classes

- **Color tokens**
  - Brand neutrals, reading surfaces, interactive states, warnings/errors.
  - Governance semantics (CARE label palettes, masking/generalization indicators).
  - Map highlight + selection colors with sufficient contrast against basemaps.

- **Typography tokens**
  - Narrative readability (Story Nodes, Focus Mode summaries, document previews).
  - Accessible line-height defaults and long-text wrapping behaviors.

- **Spacing + sizing tokens**
  - A consistent grid (layout rhythm).
  - Minimum interactive target sizes (A11y-friendly tap/click targets).

- **Radii / elevation / z-index**
  - Stable “surface hierarchy” so overlays (governance, tooltips, dialogs) remain predictable.
  - Z-index order is treated as a *contract* to prevent “invisible overlays” or unreadable dialogs.

### 2) Theme architecture

Themes are **variable maps**, not alternate CSS forks.

- Themes should be implemented using CSS variables mounted by `global.css`.
- Components should use tokens (or token-bound utilities), not direct theme values.
- Theme switching must respect:
  - `prefers-color-scheme`
  - reduced motion
  - readability constraints for long-form narrative content

**Theme parity rule:** all critical semantics (errors, warnings, governance, focus highlight) must be preserved across themes. “Dark mode” is not allowed to hide or de-emphasize governance signals.

### 3) Styling contract for components

To keep layering clean:

- Components should:
  - use Tailwind utility classes that bind to tokenized values, OR
  - use small style helpers in `mixins/`, OR
  - use CSS variables surfaced in `global.css`.

- Components must **not**:
  - introduce unreviewed color hex values,
  - introduce arbitrary spacing “just this once,”
  - override governance overlay visibility/contrast.

### 4) Map & 3D styling primitives

Map styling is a high-risk area for misinterpretation and must follow additional constraints:

- Legends must be accessible and present when ramps encode meaning.
- Selection/highlight states must be visible in both light/dark themes.
- Masked/generalized layers must use **clear** visual indicators and accompanying labels (color alone is insufficient).

If a dataset’s governance requires masking/generalization, map styling MUST support a presentation that:
- does not imply false precision,
- does not leak precise boundaries,
- remains interpretable to users.

### 5) Accessibility architecture (styles layer responsibilities)

`web/src/styles/**` must provide primitives that make accessible UI the default:

- Focus rings are always visible (keyboard navigation).
- Contrast is enforced by token selection (not left to “component taste”).
- Reduced-motion-safe transitions live in `mixins/transitions.ts`.
- Reading surfaces prioritize long-form comprehension (Story Nodes / Focus Mode).

---

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  A["src/design-tokens/ (shared)"] --> B["web/src/styles/tokens/ (bindings or mirror)"]
  C["src/theming/ (shared)"] --> D["web/src/styles/themes/ (variable maps)"]
  B --> E["Tailwind config + CSS variables"]
  D --> E
  E --> F["Components + Pages + Map/3D UI"]
  F --> G["Governance Overlay Surfaces (CARE / masking / provenance)"]
~~~

~~~mermaid
flowchart TD
  Z["zindex.tokens.ts (contract)"] --> MAP["Map surface"]
  Z --> HUD["HUD + panels (Focus/Story/Explorer)"]
  Z --> MODAL["Dialogs / modals"]
  Z --> TIP["Tooltips / transient UI"]
  Z --> GOV["Governance overlays (cannot be hidden)"]
~~~

---

## ⚖ FAIR+CARE & Governance

This document is “style-only,” but styling is not neutral: it encodes meaning.

### Governance-safe visualization rules

- Governance semantics (CARE labels, sovereignty notices, masking indicators) must have:
  - consistent placement patterns,
  - readable contrast across themes,
  - non-color redundant cues (icons, text labels, patterns).

- Styling MUST NOT:
  - visually minimize restricted or masked content,
  - imply precision when data is generalized,
  - use culturally insensitive iconography or decorative motifs to represent sovereignty.

### Review triggers (must go through governance review)

Any of the following changes require FAIR+CARE review:

- Changing the mapping between CARE labels and visual semantics.
- Introducing new “status colors” that users may interpret as risk/permission.
- Modifying masking/generalization representation for sensitive spatial layers.

---

## 🧪 Validation & CI/CD

The styles layer is expected to be CI-safe and regression-resistant.

### Required validations

- **Contrast checks** for key token pairs (text vs surface, warning vs background, etc.).
- **Focus visibility checks** (keyboard-only navigation must remain usable).
- **Reduced motion checks** (transitions should honor reduced-motion preference).
- **Token integrity checks**
  - no duplicate keys,
  - no missing semantic tokens,
  - stable exports for consumers.
- **Map styling checks**
  - legend readability,
  - selection/highlight visibility on common basemaps,
  - masking indicators remain visible and explained.

### CI expectations

CI must fail if:

- token changes introduce contrast regressions,
- governance overlays become unreadable in any supported theme,
- styling introduces arbitrary unreviewed values that bypass token usage.

(Exact commands/scripts are defined in repo CI workflows and `web/package.json`; this document defines the contract, not the invocation.)

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-15 | Upgraded to KFM-MDP v11.2.6; normalized section structure + directory layout; aligned `web/src/styles/**` with shared `src/design-tokens/` and `src/theming/`; raised accessibility posture to WCAG 2.1 AA+; added release artifact refs (SBOM/attestation/energy/carbon). |
| v10.4.0 | 2025-11-15 | Full KFM-MDP v10.4 rewrite; introduced CARE/A11y theming rules, map style architecture, token system. |
| v10.3.2 | 2025-11-14 | Updated color tokens + Story Node typography presets. |
| v10.3.1 | 2025-11-13 | Initial styles overview. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
FAIR+CARE Certified · Public Document · Version-Pinned  

[⬅️ Back to Web Source Overview](../README.md) ·
[🧱 Web Source Architecture](../ARCHITECTURE.md) ·
[🌐 Web Platform Overview](../../README.md) ·
[🛡 Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
