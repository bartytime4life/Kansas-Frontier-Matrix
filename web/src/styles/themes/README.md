---
title: "🌗 Kansas Frontier Matrix — Theme Configuration Specification (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/styles/themes/README.md"
version: "v10.4.0"
last_updated: "2025-11-15"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/web-styles-themes-v1.json"
governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.1"
status: "Active / Enforced"
doc_kind: "Specification"
intent: "web-styles-themes"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
sensitivity_level: "None"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false
provenance_chain:
  - "web/src/styles/themes/README.md@v10.3.2"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "DefinedTermSet"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
json_schema_ref: "../../../../schemas/json/web-styles-themes.schema.json"
shape_schema_ref: "../../../../schemas/shacl/web-styles-themes-shape.ttl"
doc_uuid: "urn:kfm:doc:web-styles-themes-v10.4.0"
semantic_document_id: "kfm-doc-web-styles-themes"
event_source_id: "ledger:web/src/styles/themes/README.md"
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
sunset_policy: "Superseded upon theme system v11 update"
---

<div align="center">

# 🌗 **Kansas Frontier Matrix — Theme Configuration Specification**  
`web/src/styles/themes/README.md`

**Purpose:**  
Define the **theme configuration layer** for the KFM Web Platform — mapping design tokens to  
light, dark, and high-contrast variants.  
Themes ensure that the UI is **visually consistent**, **WCAG 2.1 AA–compliant**, and  
**FAIR+CARE-aware** across all pages and components.

</div>

---

# 📘 Overview

Themes in `web/src/styles/themes/` are **token-to-CSS-variable maps** that:

- Bind `web/src/styles/tokens/**` to actual UI themes  
- Provide **light**, **dark**, and optional **high-contrast** experiences  
- Guarantee **WCAG 2.1 AA** contrast  
- Respect system preferences (`prefers-color-scheme`, `prefers-reduced-motion`)  
- Ensure CARE, governance, and masking colors are **consistent and readable**  
- Support all layout and component states (MapView, TimelineView, Focus Mode, Story Nodes, etc.)

Theme modules do **not** define new colors or spacing — they only **compose existing tokens**  
into usable themes.

---

# 🧱 Directory Structure

~~~text
web/src/styles/themes/
├── light.ts          # Light theme mapping of tokens → CSS variables
├── dark.ts           # Dark theme mapping of tokens → CSS variables
└── highContrast.ts   # Optional high-contrast theme for enhanced A11y
~~~

---

# 🧩 Theme Modules

---

## 🌞 `light.ts` — Light Theme

Defines:

- `:root[data-theme="light"]` CSS variable mappings  
- Primary text and background colors for light mode  
- Accessible colors for:
  - Focus rings  
  - Buttons and interactive states  
  - Map overlays and legends  
  - CARE badges and sovereignty indicators  
  - Errors, warnings, success, info  

Requirements:

- Must meet or exceed **WCAG 2.1 AA** contrast ratios  
- Must avoid excessively bright or harsh colors that cause fatigue  
- Must behave well on common monitors in typical lighting conditions  
- Must ensure governance and masking colors remain legible

---

## 🌙 `dark.ts` — Dark Theme

Defines:

- `:root[data-theme="dark"]` CSS variable mappings  
- Dark background and neutral text colors  
- Reduced-luminance palette for map overlays and panels  
- Complementary colors for CARE badges and governance overlays  

Requirements:

- Must meet **WCAG 2.1 AA** contrast ratios against dark backgrounds  
- Must not rely on neon-like or overly saturated accents  
- Must ensure map layers and overlays are clearly visible against dark maps  
- Must preserve the same **semantic hierarchy** as light theme  
  (same tokens, different values; no surprise meaning changes)

---

## ⚪ `highContrast.ts` — High-Contrast Theme (Optional / A11y)

Defines:

- `:root[data-theme="high-contrast"]` mapping  
- Increased contrast beyond AA where possible (approaching AAA in key areas)  
- Simplified colors that maximize legibility for:
  - Text  
  - Icons  
  - Focus rings  
  - Form fields  
  - Governance signals  

Requirements:

- Designed for users requiring maximum contrast or A11y support  
- Must work with both `prefers-contrast` and manual user toggles  
- Must emphasize clarity over brand aesthetic  
- Must be fully compatible with CARE + governance palettes  
  (e.g., sovereignty warnings must stand out clearly)

---

# 🔄 Theme Switching Architecture

Themes are selected via:

- A theme context (e.g., `ThemeContext`)  
- System preference detection:
  - `prefers-color-scheme: dark` / `light`  
  - Optional `prefers-contrast`  

Switching mechanism:

- Generally via a `data-theme` attribute on `<html>` or `<body>`  
  - `data-theme="light"`  
  - `data-theme="dark"`  
  - `data-theme="high-contrast"`  

Rules:

- No inline style overrides for theming (must use variables)  
- No component should hardcode hex colors; always resolve via tokens → theme → CSS variable  
- Theme switches must respect `prefers-reduced-motion` (no heavy animation)

---

# ♿ Accessibility Requirements

Theme configurations MUST:

- Guarantee **WCAG 2.1 AA** contrast for all text and interactive elements  
- Provide adequate focus outlines (visible, not purely color-based)  
- Respect:
  - `prefers-color-scheme`  
  - `prefers-reduced-motion`  
  - user-chosen theme overrides  

Dark and high-contrast themes must be tested for:

- Legibility of:
  - Text and headings  
  - Map legends  
  - Governance labels  
  - CARE badges  
- Clarity of states:
  - Hover  
  - Focus  
  - Disabled  

Accessibility test failures → **CI-blocking**.

---

# 🔐 FAIR+CARE & Governance Constraints

Themes are **not purely aesthetic**; they are part of governance:

- CARE labels must be visibly distinguishable in all themes  
- Masked/blurred content must still be clearly indicated as such  
- Sovereignty warnings must be prominent and legible in all themes  
- Provenance tags must remain visible and readable across light/dark/high-contrast modes  
- No theme may downplay or hide governance-related warnings or badges  

FAIR+CARE failures → **CI BLOCKER**.

---

# 📈 Telemetry & Observability

Theme-related telemetry may include:

- Theme selection changes (`light`, `dark`, `high-contrast`)  
- A11y-related toggles (large text, reduced motion, high contrast)  
- Any theme-specific errors (invalid variable resolution, etc.)  

This is handled by hooks (`useTelemetry`) and services (`telemetryService`), not by the theme modules themselves,  
but themes must expose:

- Stable, predictable variable names  
- No breaking changes without versioning  

---

# 🧪 Testing Requirements

Tests MUST verify:

- Light and Dark themes satisfy:
  - WCAG 2.1 AA for core UI  
  - CARE & sovereignty label visibility  
  - Focus state visibility  
- High-contrast theme increases legibility and conforms to A11y expectations  
- All `var(--token-name)` are defined and not orphaned  
- No theme introduces new colors outside token sets  

Recommended tests:

- Automated contrast checks  
- Snapshot tests of critical layouts under each theme  
- Visual regression checks for key governance components (CAREBadge, SovereigntyNotice, MaskingIndicator)

---

# 🕰 Version History

| Version | Date       | Summary                                                                 |
|--------:|------------|-------------------------------------------------------------------------|
| v10.4.0 | 2025-11-15 | Theme system aligned with KFM-MDP v10.4.1; added light, dark, high-contrast specs |
| v10.3.2 | 2025-11-14 | Strengthened dark-mode and governance color rules                       |
| v10.3.1 | 2025-11-13 | Initial theme mapping for light and dark                               |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
FAIR+CARE Certified · Public Document · Version-Pinned  
Validated under MCP-DL v6.3 & KFM-MDP v10.4.1  

</div>
