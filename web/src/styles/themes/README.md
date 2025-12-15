---
title: "🌗 Kansas Frontier Matrix — Theme Configuration Specification (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/styles/themes/README.md"
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

sbom_ref: "../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.6/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.6/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/web-styles-themes-v1.json"
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
intent: "web-styles-themes"
role: "specification"
category: "Web · Styles · Themes"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk (style-only)"
sensitivity: "General (style-only; non-sensitive)"
sensitivity_level: "None"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false

provenance_chain:
  - "web/src/styles/themes/README.md@v10.4.0"
  - "web/src/styles/themes/README.md@v10.3.2"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "DefinedTermSet"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"

json_schema_ref: "../../../../schemas/json/web-styles-themes.schema.json"
shape_schema_ref: "../../../../schemas/shacl/web-styles-themes-shape.ttl"

doc_uuid: "urn:kfm:doc:web-styles-themes-v11.2.6"
semantic_document_id: "kfm-doc-web-styles-themes"
event_source_id: "ledger:web/src/styles/themes/README.md"
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
ttl_policy: "Review required every 12 months"
sunset_policy: "Superseded upon next theme-system update"
---

<div align="center">

# 🌗 **Kansas Frontier Matrix — Theme Configuration Specification (v11)**  
`web/src/styles/themes/README.md`

**Purpose**  
Define the **theme configuration layer** for the KFM Web Platform — mapping design tokens to  
theme-scoped CSS variables for **light**, **dark**, and **high-contrast** experiences.  
Themes are required to be **WCAG 2.1 AA+ compliant**, **token-driven**, and **governance-safe**  
so CARE/sensitivity indicators, sovereignty notices, masking cues, and provenance badges remain  
clear and consistent across the platform.

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/MCP--DL-v6.3-blueviolet)](../../../../mcp/MCP-README.md)
· [![KFM-MDP v11.2.6](https://img.shields.io/badge/KFM--MDP-v11.2.6-purple)](../../../../docs/standards/kfm_markdown_protocol_v11.2.6.md)
· [![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Aligned-orange)](../../../../docs/standards/faircare/FAIRCARE-GUIDE.md)
· [![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../../LICENSE)

</div>

---

## 📘 Overview

Themes in `web/src/styles/themes/` provide **token-to-theme mappings** that:

- Bind design primitives from `web/src/styles/tokens/**` into runtime CSS variables.
- Support **light** and **dark** experiences as first-class requirements.
- Provide **high-contrast** support where configured (user toggle and/or system preference).
- Keep governance-visible UI (CARE badges, sovereignty notices, masking indicators, provenance chips)
  **legible and semantically consistent** across all themes.
- Enable consistent styling in:
  - narrative surfaces (Story Node views, Focus Mode panels),
  - exploration surfaces (MapView, CesiumView, timeline),
  - and shell UI (drawers, modals, toolbars).

Themes are **configuration**, not artistry: they MUST NOT introduce ad-hoc hex colors or spacing.
All values must be derived from tokens and expressed through CSS variables.

---

## 🗂️ Directory Layout

~~~text
web/src/styles/
├── 📁 tokens/                         # Design primitives (color, spacing, type, etc.)
├── 📁 themes/                         # Token → CSS-variable theme maps (this folder)
│   ├── 📄 light.ts                    # Light theme variable mapping
│   ├── 📄 dark.ts                     # Dark theme variable mapping
│   └── 📄 highContrast.ts             # Optional high-contrast mapping (if implemented)
├── 📁 mixins/                         # Reusable styling patterns consuming CSS variables
└── 📁 maps/                           # Map-specific CSS consuming the same variables
~~~

If the theme folder diverges (additional themes, renamed files, or generated outputs), this
layout MUST be updated in the same PR.

---

## 🧭 Context

### Relationship to the shared repo theme/tokens layer

The repository includes shared directories for cross-cutting UI semantics (e.g., `src/design-tokens/`
and `src/theming/`). The web theme system MUST remain consistent with the shared conventions
so “governance colors” and “meaning by styling” do not drift between documentation, pipelines,
and UI surfaces.  

If a conflict emerges, the safe default is:

1. Treat **web UI tokens/themes** as the authoritative runtime source for the browser.
2. Raise a governance/architecture review to reconcile shared vs web-specific naming.

### Relationship to UI state

Theme application is controlled by the Web UI state layer (commonly a `ThemeContext` plus A11y
preferences). The theme system MUST support:

- System preference detection (`prefers-color-scheme`).
- A11y preference accommodation (reduced motion, high contrast, large text), without breaking
  token semantics.
- Deterministic application (same inputs → same CSS variable map).

### Relationship to map styling

MapLibre/Cesium styling must consume the same theme variables as the rest of the UI:

- Legends and map UI chrome MUST remain readable in all themes.
- Masking and sovereignty styling MUST not be weakened in dark/high-contrast modes.
- No map stylesheet may “hardcode around” a theme problem; the fix belongs in tokens/themes.

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  TOK["Design Tokens\n(web/src/styles/tokens)"] --> THEME["Theme Maps\n(web/src/styles/themes)"]
  THEME --> VARS["CSS Variables\n(html/body data-theme)"]
  VARS --> MIX["Mixins + Components\n(web/src/styles/mixins + components)"]
  VARS --> MAPS["Map CSS + Legends\n(web/src/styles/maps)"]
  MIX --> UI["Rendered UI\n(Focus / Story / Explore)"]
  MAPS --> UI
~~~

---

## 🧱 Architecture

### 1) Theme contract

Themes MUST be treated as an **API surface**:

- Variable names are stable and version-pinned (breaking renames require review + coordinated refactors).
- Theme maps only **assign values**; they do not define new token categories.
- Theme maps must cover:
  - core UI surfaces,
  - governance surfaces,
  - and map/legend surfaces.

### 2) Theme application mechanism

A compliant implementation uses a single, inspectable theme selector (e.g., a `data-theme`
attribute on `<html>` or `<body>`). All styling must flow from:

`tokens → theme map → CSS variables → components/mixins/maps`

and NOT from inline styles or ad-hoc per-component color decisions.

### 3) High-contrast behavior

If a high-contrast theme is implemented, it MUST:

- Prioritize legibility over aesthetic subtlety.
- Preserve governance semantics (warnings, masking, sovereignty) without relying on color alone.
- Avoid introducing “new meaning” compared to light/dark (contrast can increase, meaning cannot change).

### 4) Interaction states

Themes MUST define consistent values for interaction states:

- default / hover / active / focus / disabled
- success / warning / error / info
- map selection / highlight / hover
- governance emphasis tiers (e.g., sovereignty notice prominence)

Focus styling must remain visible and not be “washed out” in dark mode.

### 5) Telemetry linkage

Theme modules do not emit telemetry, but they MUST support telemetry correctness by ensuring
theme state is unambiguous (e.g., `light | dark | high-contrast`) so the telemetry layer can
safely record aggregate usage without inferring anything user-identifying.

---

## ⚖ FAIR+CARE & Governance

Themes are governance-sensitive because they change how restrictions and warnings are perceived.

Requirements:

- **Governance overlays cannot be visually muted** by theme choices.
- Meaning must not be encoded by color alone:
  - All governance statuses must also have labels/icons/textual cues.
- Masked/generalized content MUST remain clearly indicated:
  - themes must not reduce the perceptual distinction between “masked” and “unmasked”.
- Sovereignty/heritage notices MUST remain prominent and readable across themes.

Any theme change that reduces governance clarity is a governance defect and must not merge.

---

## 🧪 Validation & CI/CD

Theme changes MUST be validated with:

- **Contrast checks** for core text, controls, and key governance UI (AA+ baseline).
- **Variable completeness checks**:
  - no orphaned `var(--*)` references,
  - no partially-defined themes (light has variables that dark lacks).
- **Map legend/readability checks** across themes.
- **A11y checks** on key flows (Focus, Story Node, Explorer, Map controls):
  - keyboard navigation,
  - visible focus,
  - reduced-motion behavior.

If theme variables or semantics change, update the corresponding telemetry schema references
and any style/visual regression baselines in the same PR.

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-15 | Documentation update: aligned to KFM-MDP v11.2.6 heading/fencing rules; clarified theme contract, governance-safe semantics, and validation expectations. |
| v10.4.0 | 2025-11-15 | Theme system aligned with KFM-MDP v10.4.1; added light/dark/high-contrast specs. |
| v10.3.2 | 2025-11-14 | Strengthened dark-mode and governance color rules. |
| v10.3.1 | 2025-11-13 | Initial theme mapping for light and dark. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
FAIR+CARE Certified · Public Document · Version-Pinned  

[⬅️ Back to Styles Overview](../README.md) · [💻 Back to Web Source Overview](../../README.md) · [🛡 Governance Charter](../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
