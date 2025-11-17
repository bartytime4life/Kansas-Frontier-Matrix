---
title: "🔘 Kansas Frontier Matrix — Accessible Buttons & Toggles (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/accessibility/patterns/buttons.md"
version: "v10.4.1"
last_updated: "2025-11-16"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/a11y-buttons-v1.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.3"
status: "Active / Enforced"
doc_kind: "Pattern"
intent: "accessible-buttons"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Medium-Risk"
sensitivity_level: "Low"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM Accessibility Council"
risk_category: "Low"
redaction_required: false
provenance_chain:
  - "docs/accessibility/patterns/buttons.md@v10.0.0"
previous_version_hash: "<previous-hash>"
ontology_alignment:
  schema_org: "WebPage"
  cidoc: "E29 Design or Procedure"
  prov_o: "prov:Plan"
json_schema_ref: "../../../schemas/json/a11y-buttons.schema.json"
shape_schema_ref: "../../../schemas/shacl/a11y-buttons-shape.ttl"
doc_uuid: "urn:kfm:doc:a11y-buttons-v10.4.1"
semantic_document_id: "kfm-doc-a11y-buttons"
event_source_id: "ledger:docs/accessibility/patterns/buttons.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Restricted"
ai_transform_permissions:
  - "summaries"
  - "explanatory-modes"
  - "contrast-checks"
ai_transform_prohibited:
  - "modifying semantic roles"
  - "removing provenance"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
classification: "UI Controls & Interactions"
jurisdiction: "Kansas / United States"
role: "a11y-pattern-buttons"
lifecycle_stage: "stable"
ttl_policy: "Quarterly review"
sunset_policy: "Superseded on next update"
---

<div align="center">

# 🔘 **Kansas Frontier Matrix — Accessible Buttons & Toggles**  
`docs/accessibility/patterns/buttons.md`

**Purpose:**  
Establish inclusive, keyboard-first, ARIA-semantic, and ethically governed patterns for **buttons, toggles, and interactive controls** across the KFM ecosystem.  
Aligned with **WCAG 2.1 AA**, **WAI-ARIA 1.2**, **ISO 9241-210**, and **FAIR+CARE** Consent & Ethics Framework.

![Docs](https://img.shields.io/badge/Docs-MCP_v6.3-blue)
![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)
![License](https://img.shields.io/badge/License-CC--BY%204.0-green)
![Status](https://img.shields.io/badge/Status-Active-success)

</div>

---

## 📘 Overview

Buttons and toggles drive nearly every form of interaction in the **Kansas Frontier Matrix**:

- Navigating Focus Mode  
- Toggling layers on MapLibre / Cesium  
- Triggering AI-assisted workflows  
- Approving FAIR+CARE consent dialogs  
- Submitting data or filtering dashboards  

This pattern defines **semantic**, **visual**, **behavioral**, and **ethical** requirements ensuring all interactions remain **equitable, predictable, and culturally safe**.

---

## 🧩 Accessibility Foundations

| Requirement | Description | WCAG / Standard |
|--------------|--------------|------------------|
| **Keyboard Operability** | Must activate via `Enter` or `Space`. | WCAG 2.1.1 |
| **Focusable** | Must appear in the tab order (`tabindex="0"` if custom). | WCAG 2.4.3 |
| **Visible Focus** | ≥ 3px outline, ≥ 3:1 contrast. | WCAG 2.4.7 |
| **Semantic Role** | Use `<button>` or `role="button"`. | WAI-ARIA 1.2 |
| **Descriptive Labels** | Icon-only controls require `aria-label`. | WCAG 2.4.6 |
| **Toggle Semantics** | Toggle states require `aria-pressed="true/false"`. | ARIA |
| **Motion Safety** | Must honor `prefers-reduced-motion`. | WCAG 2.3.3 |
| **Neutral Tone** | No harmful metaphors; plain-language phrasing. | FAIR+CARE Ethics |

---

## 🧭 Semantic Structure Examples

### Primary Action Button  
```html
<button type="button" class="btn-primary">
  Save Changes
</button>
```

### Toggle Button  
```html
<button type="button" aria-pressed="false" class="btn-toggle">
  <span aria-hidden="true">🌞</span>
  Light Mode
</button>
```

### Icon-Only Button  
```html
<button type="button" aria-label="Open navigation menu" class="btn-icon">
  <svg role="img" aria-hidden="true">...</svg>
</button>
```

### Disclosure / Menu Trigger  
```html
<button
  aria-haspopup="true"
  aria-expanded="false"
  aria-controls="menu-resources"
>
  Resources
</button>
```

**Implementation Notes**

- Never rely on `<div>` / `<span>` as buttons.  
- Custom button components must implement **role**, **tabindex**, **keyboard handlers**, and **ARIA states**.  
- Icon-only cases must *always* provide a human-language visible or ARIA label.

---

## 🎨 Design Tokens (A11y-First)

| Token | Purpose | Example |
|--------|----------|---------|
| `button.primary.bg` | Primary button background | `#0053A0` |
| `button.primary.text` | Primary label text | `#FFFFFF` |
| `a11y.focus.color` | Universal focus outline color | `#FFD54F` |
| `a11y.focus.width` | Focus outline width | `3px` |
| `button.toggle.on.bg` | Toggle “on” state background | `#4CAF50` |
| `button.toggle.off.bg` | Toggle “off” state background | `#B0BEC5` |
| `motion.reduced` | Reduced-motion token | `true` |

---

## 🧠 Behavior Matrix

| Interaction | Expected Behavior | A11y Requirement |
|--------------|------------------|------------------|
| `Tab` / `Shift+Tab` | Move sequentially among controls | Must be predictable |
| `Enter` / `Space` | Activate / toggle | Must fire `click()` |
| `Esc` | Close related overlays | Restore focus to opener |
| `aria-pressed` | Stateful toggles | Must update on click / keypress |
| `aria-expanded` | Menu/disclosure controls | Reflect open/closed state |
| `aria-controls` | Links control to region | Required for menus & details |

---

## 🧾 Ethical & Inclusive Rules

| Category | Guideline |
|-----------|-----------|
| **Language** | Avoid metaphors implying violence, dominance, harm. |
| **Imagery** | Avoid culturally sensitive symbols unless approved. |
| **Consent** | Buttons initiating data sharing must link to consent text via `aria-describedby`. |
| **Equity** | No color-only state changes; always pair with text, icons, or shape. |
| **Localization** | All labels must be translatable and support `lang` attributes. |

---

## 🔁 Testing & CI Validation

| Tool | Scope | Output |
|-------|--------|---------|
| **axe-core** | ARIA roles, focus order, keyboard activation | `a11y_buttons.json` |
| **Cypress** | End-to-end keyboard tab flow | `button_focus_tests.json` |
| **Lighthouse** | Contrast, semantics, motion | `lighthouse_buttons.json` |
| **jest-axe** | React/KFM UI Kit component tests | `a11y_button_components.json` |
| **Manual Review** | NVDA / VoiceOver audit | FAIR+CARE logs |

Validation must confirm:

- Keyboard operation works across browsers  
- Focus ring visible on all backgrounds  
- `aria-pressed` & `aria-expanded` update correctly  
- No color-only communication  
- Plain-language labels present  

---

## 🧩 Focus Mode Toggle — Reference Pattern

```html
<button
  type="button"
  class="btn-focus"
  aria-pressed="false"
  aria-label="Enable Focus Mode"
  data-telemetry="focus-toggle"
>
  <span class="icon" aria-hidden="true">🧠</span>
  <span class="label">Focus Mode</span>
</button>
```

**Notes**

- `aria-pressed` controls toggle state.  
- Icon hidden from screen readers to prevent duplicate announcements.  
- Telemetry token logs focus-mode usage ethically.

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|--------|---------|---------|
| v10.4.1 | 2025-11-16 | KFM Accessibility Council | Updated to KFM-MDP v10.4.3; added extended YAML, governance metadata, SHACL schema links, and improved ethics guidance. |
| v10.0.0 | 2025-11-10 | FAIR+CARE A11y Council | Initial creation; defined semantic, ARIA, and inclusive button spec. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
Master Coder Protocol v6.3 · FAIR+CARE Council Verified  
[⬅ Back to Patterns Index](README.md) · [Next → Dialogs](dialogs.md)

</div>