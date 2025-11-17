---
title: "💬 Kansas Frontier Matrix — Accessible Tooltip, Helper Text, and Inline Hint Standards (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/accessibility/patterns/tooltips.md"
version: "v10.4.1"
last_updated: "2025-11-16"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/a11y-tooltips-v1.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.3"
status: "Active / Enforced"
doc_kind: "Pattern"
intent: "a11y-tooltips-and-helper-text"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
sensitivity_level: "Low"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM Accessibility Council + FAIR+CARE Council"
risk_category: "Low"
redaction_required: false
provenance_chain: []
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "CreativeWork"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
json_schema_ref: "../../../schemas/json/a11y-tooltips.schema.json"
shape_schema_ref: "../../../schemas/shacl/a11y-tooltips-shape.ttl"
doc_uuid: "urn:kfm:doc:a11y-tooltips-v10.4.1"
semantic_document_id: "kfm-doc-a11y-tooltips"
event_source_id: "ledger:docs/accessibility/patterns/tooltips.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
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
accessibility_compliance: "WCAG 2.1 AA"
classification: "Public Document"
jurisdiction: "United States / Kansas"
role: "a11y-pattern-tooltips"
lifecycle_stage: "stable"
ttl_policy: "Quarterly review"
sunset_policy: "Superseded upon next tooltip/inline-hint pattern update"
---

<div align="center">

# 💬 **Kansas Frontier Matrix — Accessible Tooltip, Helper Text, and Inline Hint Standards**  
`docs/accessibility/patterns/tooltips.md`

**Purpose:**  
Define accessible, predictable, and ethically neutral patterns for tooltips, helper text, and inline hints used across Kansas Frontier Matrix (KFM) applications.  
Ensures all contextual help mechanisms are keyboard operable, screen-reader compatible, culturally respectful, and aligned with **WCAG 2.1 AA**, **FAIR+CARE**, and **Master Coder Protocol v6.3**.

![Badge Docs](https://img.shields.io/badge/Docs-MCP_v6.3-blue)
![Badge FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)
![Badge License](https://img.shields.io/badge/License-CC--BY%204.0-green)
![Badge Status](https://img.shields.io/badge/Status-Active-success)

</div>

---

## 📘 Overview

Tooltips and helper text are critical for:

- Explaining complex geospatial controls  
- Clarifying AI narrative context  
- Presenting data provenance and consent hints  
- Guiding users through map, timeline, and Focus Mode interactions  

This pattern:

- Standardizes when and how KFM uses tooltips vs inline text  
- Prevents inaccessible hover-only help  
- Integrates FAIR+CARE consent and provenance indicators  
- Ensures information is available to both visual and non-visual users  

---

## 🧩 Tooltip & Helper Text Principles

| Principle           | Description                                                        | Standard Reference |
|---------------------|--------------------------------------------------------------------|--------------------|
| Non-Hover Dependency| Information must not be hover-only; keyboard and touch must work. | WCAG 1.4.13        |
| Keyboard Focusable  | Tooltip toggles and icons must be in the tab order.               | WCAG 2.1.1         |
| Persistent Option   | Critical info must be available inline or on-demand, not transient.| WCAG 3.2.4         |
| Screen Reader Safe  | ARIA attributes expose tooltip content clearly.                    | WAI-ARIA 1.2       |
| Ethical Context     | Provenance / consent information shown in clear, neutral language. | FAIR+CARE          |
| Low Cognitive Load  | Short, plain-language tooltip content with no jargon.             | WCAG 3.1.5         |

---

## 🗂️ File Context

```text
docs/accessibility/
│
├── README.md
├── testing-guide.md
├── tokens.md
└── patterns/
    │
    ├── tooltips.md                  # This file (tooltip and helper text patterns)
    ├── wildlife-tracking.md
    ├── wayfinding.md
    ├── vehicle-logistics.md
    └── urban-planning.md
```

---

## 🧭 Example Implementation: Icon Tooltip With Button Trigger

~~~html
<label for="year-input">
  Year of Observation
  <button
    type="button"
    class="tooltip-trigger"
    aria-describedby="year-help"
  >
    ⓘ
    <span class="sr-only">More information about year of observation</span>
  </button>
</label>

<input id="year-input" name="year" type="number" />

<div
  id="year-help"
  class="tooltip"
  role="tooltip"
>
  Use the year when the data was collected, not the publication date.
</div>
~~~

### Implementation Notes

- Tooltip trigger is a `button`, not a bare `span` or `i` element.  
- A visually hidden (`sr-only`) label describes the button’s purpose.  
- `aria-describedby` ties the trigger to `role="tooltip"` content.  
- Tooltip content is short, specific, and free of unexplained jargon.  

---

## 🧭 Example Implementation: Provenance / Consent Tooltip

~~~html
<span class="provenance-chip" aria-describedby="prov-tooltip-1">
  Provenance
</span>

<div id="prov-tooltip-1" role="tooltip" class="tooltip">
  Dataset: Tribal Territories (USFS, 1840–1890).  
  Display approved via Kaw Nation consultation (2025).
</div>
~~~

### Ethical Notes

- Use neutral language describing data source, validation, and consent.  
- Avoid implying ownership over cultural/heritage data; emphasize stewardship.  
- Indicate when display has been community-approved and when further consent is pending.  

---

## 🎨 Tooltip Design Tokens

| Token                          | Description                       | Example Value |
|--------------------------------|-----------------------------------|---------------|
| tooltip.bg.color               | Tooltip background color          | #263238       |
| tooltip.text.color             | Tooltip text color                | #FAFAFA       |
| tooltip.border.color           | Tooltip border                    | #B0BEC5       |
| tooltip.shadow                 | Drop shadow for tooltip           | 0 2px 4px rgba(0,0,0,0.25) |
| tooltip.max.width              | Max width for tooltip content     | 260px         |
| tooltip.zIndex                 | Stacking order                    | 1000          |
| tooltip.focus.outline.color    | Outline color when focused        | #FFD54F       |

---

## ⚙️ Keyboard & ARIA Behavior Matrix

| Interaction | Expected Behavior | A11y Requirement |
|-------------|-------------------|------------------|
| Tab to icon | Focus ring visible; hint about more info via SR text | WCAG 2.4.7 |
| Enter/Space on icon | Tooltip toggles open/closed | WCAG 2.1.1 |
| Escape      | Dismisses open tooltip and returns focus to trigger | Consistent UX |
| aria-expanded| Used when tooltip is persistently toggled | WAI-ARIA 1.2 |
| aria-describedby| Links input or icon to explanatory tooltip text | WCAG 1.3.1 |

---

## 🧪 Testing & Validation

| Tool       | Scope                          | Output                                       |
|------------|--------------------------------|----------------------------------------------|
| jest-axe   | Component-level tooltip tests  | a11y_tooltips_components.json                |
| axe-core   | Page-level ARIA + focus checks | a11y_tooltips.json                           |
| Cypress    | End-to-end keyboard tests      | a11y_tooltips_e2e.json                       |
| Manual SR  | NVDA / VoiceOver reading order | FAIR+CARE review notes                       |

Tests validate:

- Tooltip content is reachable and dismissible by keyboard only.  
- No hover-only tooltips for critical information.  
- Screen readers announce tooltip content once, clearly, and without repetition loops.  

---

## ⚖️ FAIR+CARE Integration

| Principle          | Implementation                                                |
|--------------------|--------------------------------------------------------------|
| Collective Benefit | Tooltips explain data and AI behavior for all user groups.   |
| Authority to Control | Consent and provenance tooltips show who approved what.   |
| Responsibility     | Critical ethical implications never hidden only in tooltips. |
| Ethics             | No manipulative, shaming, or biased language in helper text. |

---

## 🧩 When to Use Tooltips vs Inline Text

- Use **inline text** when:
  - The information is critical for task completion.  
  - The user must read it to avoid errors or harm.  

- Use **tooltips/helper icons** when:
  - The information is helpful but not strictly required.  
  - It clarifies terminology, acronyms, or edge cases.  

- Never rely on **color alone** in tooltips to convey meaning.  

---

## 🧾 Example: React Tooltip Wrapper (Conceptual)

~~~tsx
type TooltipProps = {
  id: string;
  label: string;
  children: React.ReactNode;
};

export function Tooltip({ id, label, children }: TooltipProps) {
  return (
    <span className="tooltip-wrapper">
      <button
        type="button"
        className="tooltip-trigger"
        aria-describedby={id}
      >
        ⓘ
        <span className="sr-only">{label}</span>
      </button>
      <span id={id} role="tooltip" className="tooltip">
        {children}
      </span>
    </span>
  );
}
~~~

---

## 🕰️ Version History

| Version | Date       | Author               | Summary                                                                 |
|--------:|------------|----------------------|-------------------------------------------------------------------------|
| v10.4.1 | 2025-11-16 | Accessibility Council | Created tooltip/helper-text accessibility standard; aligned with KFM-MDP v10.4.3 and FAIR+CARE. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Developed under **Master Coder Protocol v6.3** · Verified by **FAIR+CARE Council**  
[⬅ Back to Accessibility Index](../README.md)

</div>