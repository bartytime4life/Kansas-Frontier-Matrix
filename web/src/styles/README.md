---
title: "🎨 Kansas Frontier Matrix — Web Styles & Design System Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/styles/README.md"
version: "v11.2.6"
last_updated: "2025-12-15"

review_cycle: "Quarterly · FAIR+CARE Council & Web Architecture Board"
release_stage: "Stable / Governed"
status: "Active / Enforced"
lifecycle_stage: "LTS"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.6/manifest.zip"
telemetry_ref: "../../../releases/v11.2.6/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/web-styles-readme-v1.json"
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

doc_kind: "Overview"
intent: "web-styles-overview"
role: "overview"
category: "Web · Styles · Design System · UI"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk (style-only)"
sensitivity: "Style-only (non-sensitive)"
sensitivity_level: "None"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false
classification: "Public Document"
jurisdiction: "Kansas / United States"

provenance_chain:
  - "web/src/styles/README.md@v10.4.0"
  - "web/src/styles/README.md@v10.3.2"
  - "web/src/styles/README.md@v10.3.1"

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
  - "content-alteration"
  - "speculative-additions"
  - "unverified-historical-claims"
  - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "Review required every 12 months"
sunset_policy: "Superseded upon next style-system update"
---

<div align="center">

# 🎨 **Kansas Frontier Matrix — Web Styles & Design System Overview (v11.2.6)**  
`web/src/styles/README.md`

**Purpose**  
Define the **governed design system** for the Kansas Frontier Matrix Web Platform: tokens, themes, map UI styling, and accessibility-first visual constraints that keep UI behavior **consistent**, **testable**, and **FAIR+CARE-aligned**.

<img src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/License-MIT-green" />
<img src="https://img.shields.io/badge/Accessibility-WCAG_2.1_AA%2B-blueviolet" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

</div>

---

## 📘 Overview

The **Styles Layer** (`web/src/styles/**`) provides the governed foundation for all UI rendering:

- **Design tokens** (color, spacing, typography, radii, elevation, z-index)
- **Theme maps** (light / dark / high-contrast) built from tokens
- **A11y-first styling primitives** (focus rings, reduced-motion safe transitions)
- **Governance-aware visual semantics** (CARE labels, sovereignty indicators, masking/generalization cues)
- **Map UI styling** (MapLibre/Cesium controls, popups, legends, HUD)
- **Deterministic theming integration** with the web UI (no ad-hoc inline “magic”)

This layer is treated as **infrastructure**:

- It must be **stable** (changes require review)
- It must be **machine-extractable** (tokens/themes can be validated in CI)
- It must be **accessible** (WCAG 2.1 AA+)
- It must not encode policy decisions—only **render** them consistently

---

## 🗂️ Directory Layout

~~~text
📁 web/
└── 📁 src/
    └── 📁 styles/                                 — Web design system (tokens, themes, mixins, map UI)
        ├── 📁 tokens/                             — Design primitives (color, spacing, type, radii, etc.)
        │   ├── 📄 color.tokens.ts                 — WCAG-safe palette + governance semantic tokens
        │   ├── 📄 spacing.tokens.ts               — Spacing scale and layout rhythm
        │   ├── 📄 typography.tokens.ts            — Type scale, reading presets, narrative text rules
        │   ├── 📄 radii.tokens.ts                 — Corner rounding system
        │   ├── 📄 shadow.tokens.ts                — Elevation system
        │   └── 📄 zindex.tokens.ts                — Layering contract (map/hud/modals/tooltips/etc.)
        │
        ├── 📁 themes/                             — Theme variable maps
        │   ├── 📄 light.ts                        — Light theme variables
        │   └── 📄 dark.ts                         — Dark theme variables
        │
        ├── 📁 mixins/                             — Reusable styling patterns (A11y-safe)
        │   ├── 📄 focus-ring.ts                   — Visible focus treatment
        │   ├── 📄 card.ts                         — Card/panel primitives
        │   ├── 📄 panel.ts                        — Pane shells + split-layout helpers
        │   └── 📄 transitions.ts                  — Reduced-motion safe transitions
        │
        ├── 📁 maps/                               — Map UI CSS primitives (MapLibre/Cesium)
        │   ├── 📄 README.md                       — Map styling spec (governance + masking rules)
        │   ├── 📄 maplibre.css                    — Controls, popups, attribution, overlays
        │   ├── 📄 cesium.css                      — Cesium canvas + overlays
        │   ├── 📄 layers.css                      — Layer styling helpers (non-policy; token-driven)
        │   ├── 📄 legends.css                     — Legend layout + a11y hooks
        │   ├── 📄 masking.css                     — Masking/generalization visualization primitives
        │   └── 📄 hud.css                         — HUD layout + readability rules
        │
        └── 📄 global.css                          — Base reset + Tailwind layers + variable mounts
~~~

---

## 🧭 Context

### What “governance-aware styling” means

The styles system does **not** decide governance. It renders governance decisions emitted by APIs and metadata:

- **CARE labels**: visible, consistent, and not suppressible when required
- **Sovereignty notices**: visually prioritized and readable across themes
- **Masking/generalization**: unambiguous distinction between precise vs. generalized geometry
- **Provenance visibility**: styling supports “chips/badges/overlays” patterns used elsewhere

### Relationship to shared tokens outside `web/`

If the monorepo provides shared token sources (for example under `src/design-tokens/**` or `src/theming/**`), the web styles layer must remain **1:1 consistent** by either:
- importing them directly, or
- generating/deriving web tokens via a deterministic build step that is version-pinned and CI-validated.

(Do not duplicate token logic in multiple locations without an explicit synchronization contract.)

---

## 🧱 Architecture

### Token-driven styling is mandatory

Rules:

- No “new colors” appear directly in components or CSS.
- All color semantics come from **tokens** and theme variables.
- Layout rhythm comes from **spacing tokens** and shared mixins.

### A11y constraints are encoded in primitives

- Focus visibility is enforced via a dedicated focus-ring mixin/pattern.
- Reduced motion is enforced via transition mixins that honor user preferences.
- Target sizes and spacing should satisfy common accessibility guidance (e.g., touch targets).

### Map UI styling is treated as a governed subsystem

MapLibre/Cesium UI styling is scoped under `styles/maps/**` and must:
- respect theme variables,
- preserve legibility in all modes,
- never visually undermine masking, sovereignty, or warnings.

---

## ⚖ FAIR+CARE & Governance

Non-negotiable requirements:

- Styles must not reduce the visibility of sovereignty and masking indicators.
- High-risk warnings must remain readable under all themes.
- Governance overlays cannot be made “optional” by visual design choices.
- Styling must avoid culturally inappropriate iconography or color semantics.

---

## 🧪 Validation & CI/CD

Minimum expectations (implemented via CI checks and/or unit tests):

- **Token integrity**: no missing variables, no duplicates, stable names
- **Contrast checks**: WCAG contrast validation for critical text/UI states
- **Theme parity**: light/dark/high-contrast produce equivalent hierarchy
- **Reduced-motion compliance**: transitions respect preferences
- **Map legend readability**: legends remain readable on small viewports

Suggested test locations (repo conventions):

~~~text
📁 tests/
├── 📁 unit/
│   └── 📁 web/
│       └── 📁 styles/
└── 📁 integration/
    └── 📁 web/
        └── 📁 styles/
~~~

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-15 | KFM‑MDP v11.2.6 compliance pass: approved H2 set, tilde fences, standardized directory layout, required governance footer links. |
| v10.4.0 | 2025-11-15 | Added CARE/A11y theming rules, map style architecture, token system. |
| v10.3.2 | 2025-11-14 | Updated color tokens + Story Node typography presets. |
| v10.3.1 | 2025-11-13 | Initial styles overview. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
FAIR+CARE Certified · Public Document · Version-Pinned  

[⬅️ Back to Web Source Overview](../README.md) · [🧭 Web Source Architecture](../ARCHITECTURE.md) · [🛡 Governance](../../../docs/standards/governance/ROOT-GOVERNANCE.md) · [🧡 FAIR+CARE](../../../docs/standards/faircare/FAIRCARE-GUIDE.md) · [🪶 Sovereignty Policy](../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

</div>
