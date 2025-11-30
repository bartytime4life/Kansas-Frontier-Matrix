---
title: "🎨 KFM v11 — Accessibility Design Tokens (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/accessibility/tokens.md"
version: "v11.2.3"
last_updated: "2025-11-29"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"
backward_compatibility: "Aligned with v10.x → v11.x governance rules"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../releases/v11.2.3/a11y-tokens-telemetry.json"
telemetry_schema: "../../schemas/telemetry/a11y-tokens-v2.json"
energy_schema: "../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../schemas/telemetry/carbon-v2.json"

governance_ref: "../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"

doc_kind: "Guide"
intent: "accessibility-design-tokens"
fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"

classification: "Public (Governed)"
sensitivity_level: "Low"
public_exposure_risk: "Low"
indigenous_rights_flag: false
risk_category: "Low"
redaction_required: false
data_steward: "KFM Accessibility Council · FAIR+CARE Council"

provenance_chain:
  - "docs/accessibility/tokens.md@v10.0.0"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "DefinedTermSet"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"

json_schema_ref: "../../schemas/json/accessibility-tokens.schema.json"
shape_schema_ref: "../../schemas/shacl/accessibility-tokens-shape.ttl"

doc_uuid: "urn:kfm:doc:accessibility-tokens-v11.2.3"
semantic_document_id: "kfm-doc-accessibility-tokens"
event_source_id: "ledger:docs/accessibility/tokens.md"
immutability_status: "version-pinned"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative additions"
  - "unverified historical claims"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "United States · Kansas"
lifecycle_stage: "stable"
ttl_policy: "Continuous"
sunset_policy: "Replaced upon next token revision"
---

<div align="center">

# 🎨 **Kansas Frontier Matrix — Accessibility Design Tokens**  
`docs/accessibility/tokens.md`

**Purpose**  
Define the **reusable accessibility design tokens** used across the Kansas Frontier Matrix (KFM).  
Ensure consistent, measurable compliance with **WCAG 2.1 AA**, **FAIR+CARE**, **ISO 9241-210**, and **MCP-DL v6.3**.

</div>

---

## 📘 Overview

Accessibility tokens are the **atomic building blocks** of the KFM design system.  
They guarantee **consistent and inclusive UI/UX patterns** across:

- Focus Mode  
- Timeline/map controls  
- Narrative interfaces  
- Documentation UI  
- Accessibility overlays  
- Interactive data visualizations  

All tokens are:

- **Machine-extractable**  
- **Validated in CI**  
- **WCAG 2.1 AA-compliant**  
- **FAIR+CARE-annotated** (where applicable)

This file extends the global design token set defined under:

`docs/design/tokens/`

---

## 🗂️ Directory Layout (Emoji-Prefix Standard)

~~~text
docs/accessibility/
│
├── 📄 README.md                     # Accessibility guidelines
├── 🎨 tokens.md                     # Accessibility token specification (this file)
│
├── 📁 patterns/                     # Inclusive UI component guidelines
│   ├── 📄 buttons.md
│   ├── 📄 dialogs.md
│   └── 📄 map-controls.md
│
└── 📁 audits/                       # axe-core, Lighthouse, CI audit outputs
    ├── 📄 2025-Q1_a11y_report.json
    └── 📄 2025-Q2_a11y_report.json
~~~

---

## 🗂️ Token Categories

| Category             | Description                                              |
|----------------------|----------------------------------------------------------|
| **Color Tokens**     | Ensure legible contrast ratios and non-harmful palettes. |
| **Typography Tokens**| Maintain readable and scalable text.                     |
| **Motion Tokens**    | Respect OS reduce-motion settings and avoid disorientation. |
| **Focus Tokens**     | Define visible, high-contrast focus states.              |
| **ARIA Tokens**      | Standardize semantic labeling & announcements.           |
| **Ethical Tokens**   | Support FAIR+CARE representation & provenance signaling. |

---

## 🎨 Color Tokens

| Token                     | Example Value | Description                     | WCAG Ratio |
|---------------------------|---------------|---------------------------------|------------|
| color.text.primary        | #1A1A1A       | Primary readable text           | 15.0:1     |
| color.text.secondary      | #404040       | Metadata labels                 | 9.0:1      |
| color.text.inverse        | #FFFFFF       | Text on dark backgrounds        | 12.0:1     |
| color.bg.surface          | #FFFFFF       | Main application background     | N/A        |
| color.bg.alt              | #F6F6F6       | Alternating row backgrounds     | N/A        |
| color.button.primary.bg   | #0053A0       | Primary action button background| 4.6:1      |
| color.button.primary.text | #FFFFFF       | Primary button label            | 4.6:1      |
| color.link.default        | #004FC6       | Default link color              | 5.2:1      |
| color.link.focus          | #FFCA28       | Focused link                   | 7.1:1      |
| color.error               | #C62828       | Error states                    | 5.0:1      |

---

## 🔠 Typography Tokens

| Token                    | Value  | Description                      |
|--------------------------|--------|----------------------------------|
| font.base.size           | 16px   | Base text size                   |
| font.scale.ratio         | 1.25   | Modular type scale               |
| font.lineheight.normal   | 1.6    | Line-height for readability      |
| font.weight.bold         | 700    | Emphasis for headings            |
| text.spacing.letter      | 0.02em | Readability for long paragraphs  |
| text.decoration.links    | underline | Reinforces link identification |
| text.align.readableWidth | 70ch   | Max readable line width          |

---

## 💫 Motion Tokens

| Token                    | Value    | Behavior                                 |
|--------------------------|----------|-------------------------------------------|
| motion.duration.short    | 100ms    | Micro-interactions                        |
| motion.duration.medium   | 250ms    | Standard transitions                      |
| motion.duration.long     | 500ms    | Large layout transitions                  |
| motion.easing.default    | ease-in-out | Smooth easing pattern                  |
| motion.prefersReduced    | true (system) | Automatically respects OS settings   |

---

## 🔲 Focus Tokens

| Token                     | Value                    | Purpose                                |
|---------------------------|--------------------------|----------------------------------------|
| focus.outline.color       | #FFB300                  | High-visibility focus outline          |
| focus.outline.width       | 3px                      | Focus outline width                    |
| focus.outline.offset      | 2px                      | Separation for visibility              |
| focus.transition.duration | 100ms                    | Accessible animation duration          |
| focus.shadow.color        | rgba(255,179,0,0.25)     | Optional glow for enhanced visibility  |

---

## 🔖 ARIA Tokens

| Token                   | Description                       | Example                      |
|-------------------------|-----------------------------------|------------------------------|
| aria.label.primaryNav   | Main navigation label             | "Main navigation"            |
| aria.label.focusToggle  | Focus Mode toggle                 | "Enable Focus Mode"          |
| aria.status.loading     | Live-region loading message       | "Loading timeline data"      |
| aria.status.ready       | Live-region readiness message     | "Timeline ready"             |
| aria.live.polite        | Non-critical updates              | "map status update"          |
| aria.live.assertive     | Critical updates                  | "Error loading data"         |

---

## 🧭 Ethical Tokens (FAIR+CARE)

| Token                         | Function                                 | Example                | Standard |
|-------------------------------|-------------------------------------------|------------------------|----------|
| care.provenance.chip.color   | Color for provenance badges               | #FFCA28                | FAIR+CARE |
| care.consent.indicator.icon  | Indicator for consented data              | 🟢                     | CARE     |
| care.ethics.alert.bg         | Sensitive-content background marker       | #FFF3E0                | ISO 26000 |
| care.inclusive.iconset       | Ensures culturally neutral iconography    | true                   | CARE C3  |
| care.altText.default         | Default alt-text template                 | "Image of [subject]"   | WCAG 1.1.1 |

---

## ⚙️ CI Validation Workflows

| Workflow                | Purpose                               | Output                        |
|-------------------------|----------------------------------------|-------------------------------|
| `color-contrast.yml`    | Validate WCAG AA/AAA contrast targets | `color-contrast.json`         |
| `accessibility_scan.yml`| Validate focus, motion, ARIA patterns | `a11y_summary.json`           |
| `faircare-audit.yml`    | Validate ethical tokens & labeling    | `faircare-validation.json`    |
| `build-and-deploy.yml`  | Publish validated tokens bundle       | `manifest.zip`                |

All tokens MUST pass these workflows before promotion to `kfm-prod`.

---

## 🧾 Usage Example (React + CSS Variables)

~~~tsx
<button
  className="
    focus-visible:outline-none
    focus-visible:ring-[var(--focus-outline-width)]
    focus-visible:ring-[var(--focus-outline-color)]
    focus-visible:ring-offset-[var(--focus-outline-offset)]
  "
  aria-label="Activate Focus Mode"
>
  Enable Focus Mode
</button>
~~~

~~~css
:root {
  --focus-outline-color: #FFB300;
  --focus-outline-width: 3px;
  --focus-outline-offset: 2px;
  --focus-shadow-color: rgba(255,179,0,0.25);
}

button:focus-visible {
  outline: none;
  box-shadow: 0 0 0 var(--focus-outline-width)
              var(--focus-outline-color),
              0 0 0 calc(var(--focus-outline-width) * 2)
              var(--focus-shadow-color);
}
~~~

---

## 🕰️ Version History

| Version | Date       | Author                | Summary |
|--------:|------------|-----------------------|---------|
| v11.2.3 | 2025-11-29 | Accessibility Council | Upgraded to v11.2.3; emoji-prefix directory layout; telemetry v2 alignment; tightened WCAG + FAIR+CARE standards. |
| v10.4.1 | 2025-11-16 | Accessibility Council | Updated to KFM-MDP v10.4.3; ensured Apple-safe codeblocks; cleaned separators. |
| v10.0.0 | 2025-11-10 | FAIR+CARE A11y Council| Initial token specification & CI integration. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Validated by **FAIR+CARE Accessibility Council**  
Built under **Master Coder Protocol v6.3**

[⬅ Back to Accessibility Index](README.md) · [📘 Design Tokens](../design/tokens.md) · [🛡 Governance](../standards/governance/ROOT-GOVERNANCE.md)

</div>