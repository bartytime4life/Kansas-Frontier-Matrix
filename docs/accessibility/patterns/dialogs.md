---
title: "💬 Kansas Frontier Matrix — Accessible Dialogs & Modals (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/accessibility/patterns/dialogs.md"
version: "v10.4.1"
last_updated: "2025-11-16"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/a11y-dialogs-v1.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.3"
status: "Active / Enforced"
doc_kind: "Pattern"
intent: "accessible-dialogs"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
sensitivity_level: "Low"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM Accessibility Council"
risk_category: "Low"
redaction_required: false
provenance_chain:
  - "docs/accessibility/patterns/dialogs.md@v10.0.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  schema_org: "CreativeWork"
  cidoc: "E31 Document"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
json_schema_ref: "../../../schemas/json/a11y-dialogs.schema.json"
shape_schema_ref: "../../../schemas/shacl/a11y-dialogs-shape.ttl"
doc_uuid: "urn:kfm:doc:a11y-dialogs-v10.4.1"
semantic_document_id: "kfm-doc-a11y-dialogs"
event_source_id: "ledger:docs/accessibility/patterns/dialogs.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "policy-altering paraphrase"
  - "removal of FAIR+CARE constraints"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
classification: "A11y Pattern"
jurisdiction: "Kansas / United States"
role: "a11y-dialog-pattern"
lifecycle_stage: "stable"
ttl_policy: "Quarterly review"
sunset_policy: "Superseded upon next pattern update"
---

<div align="center">

# 💬 **Kansas Frontier Matrix — Accessible Dialogs & Modals**  
`docs/accessibility/patterns/dialogs.md`

**Purpose:**  
Define strict, FAIR+CARE-aligned interaction patterns for all dialogs, modals, consent prompts, system alerts, and multi-step overlays within the Kansas Frontier Matrix — ensuring universal accessibility, predictable focus flows, culturally safe consent workflows, and fully compliant WCAG 2.1 AA modal semantics.

![Docs](https://img.shields.io/badge/Docs-MCP_v6.3-blue)
![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)
![License](https://img.shields.io/badge/License-CC--BY%204.0-green)
![Status](https://img.shields.io/badge/Status-Stable-success)

</div>

---

## 📘 Overview

Dialogs are used across KFM for:

- Consent confirmation  
- Dataset visibility approval  
- Governance actions  
- AI Focus Mode explanations  
- Sensitive metadata disclosure  
- Multi-step workflows  

This pattern ensures every modal interaction is:

- **Accessible** — fully keyboard operable, labeled, and screen-reader compatible  
- **Ethical** — consent-driven, transparent, reversible  
- **Predictable** — no hidden state changes, no unexpected focus jumps  
- **Aligned** — compliant with FAIR+CARE and KFM-MDP v10.4.3

---

## 🧩 Accessibility Principles

| Principle | Description | Standard |
|----------|-------------|----------|
| **Focus Containment** | Focus must not leave modal once opened; loop with Tab/Shift+Tab. | WCAG 2.4.3 |
| **Return Focus** | On close, return focus to triggering element. | WAI-ARIA Authoring 1.2 |
| **Keyboard Shortcuts** | Escape closes modal; Enter/Space activate primary action. | WCAG 2.1.1 |
| **ARIA Roles** | Use `role="dialog"` or `role="alertdialog"` depending on urgency. | WAI-ARIA 1.2 |
| **Semantic Labels** | Must include `aria-labelledby` + `aria-describedby`. | WCAG 2.4.6 |
| **Reduced Motion** | Respect `prefers-reduced-motion` for transitions. | WCAG 2.3.3 |
| **Consent Context** | All sensitive dialogs require cultural & ethical disclosure. | FAIR+CARE A2 / E1 |

---

## 🧭 Example Implementation

```html
<div
  id="consent-dialog"
  role="dialog"
  aria-modal="true"
  aria-labelledby="dialog-title"
  aria-describedby="dialog-body"
  class="kfm-modal"
  tabindex="-1"
>
  <h2 id="dialog-title">Data Usage Consent</h2>

  <p id="dialog-body">
    You are asked to consent to data processing under KFM’s FAIR+CARE governance.
    No sensitive or cultural data will be collected without explicit approval.
  </p>

  <div class="dialog-actions">
    <button id="btn-accept">Agree</button>
    <button id="btn-decline">Decline</button>
  </div>
</div>
```

**Rules Applied**

- Modal traps focus via JS focus loop.  
- Elements behind modal get `aria-hidden="true"`.  
- ESC closes modal → restores focus to original trigger.  
- Buttons have visible focus ring per KFM design tokens.  

---

## ⚙️ Keyboard & ARIA Matrix

| Key / Attribute | Behavior | Requirement |
|-----------------|----------|-------------|
| `Tab`           | Cycle forward through focusable elements | Must wrap within dialog |
| `Shift+Tab`     | Cycle backward | Must wrap within dialog |
| `Esc`           | Close modal | Mandatory |
| `Enter/Space`   | Activate currently focused button | Mandatory |
| `aria-modal="true"` | Locks background for AT users | Required |
| `aria-labelledby` | References dialog heading | Required |
| `aria-describedby` | References body/explanatory text | Strongly recommended |
| `role="alertdialog"` | For urgent/time-sensitive events | Only when appropriate |

---

## 🎨 Design Tokens (Dialogs)

| Token | Use | Example |
|--------|------|---------|
| `dialog.backdrop.bg` | Modal scrim/background | `#00000099` |
| `dialog.panel.bg` | Modal surface background | `#FFFFFF` |
| `dialog.focus.color` | Focus outline | `#FFD54F` |
| `dialog.transition.speed` | Animation duration | `0.25s` |
| `dialog.elevation` | z-index stack | `1100` |

---

## 🧾 FAIR+CARE Consent Integration

**All modals requesting user permission must include:**

- ✓ **Plain-language explanation**  
- ✓ **Data purpose disclosure**  
- ✓ **Retention & usage statement**  
- ✓ **Revocation method** (link or button)  
- ✓ **Cultural/heritage consent indicator** when applicable  
- ✓ **Persistent provenance record** stored in governance ledger  

Example annotation:

```html
<div
  data-faircare-consent="required"
  data-provenance-ref="governance-ledger.json#entry-482"
>
```

---

## 🧪 Validation Workflow

| Tool | Purpose | Output |
|-------|---------|--------|
| **axe-core** | Dialog role, label, focus trap validation | `reports/self-validation/web/a11y_dialogs.json` |
| **Lighthouse CI** | Modal focus order + reduced motion compliance | `reports/ui/lighthouse_dialogs.json` |
| **jest-axe** | Component-level ARIA compliance | `reports/ui/a11y_dialog_components.json` |
| **Manual FAIR+CARE Review** | Consent clarity & ethical framing | Governance Council log |

---

## ⚖️ FAIR+CARE Alignment

| Principle | Implementation |
|------------|----------------|
| **Collective Benefit** | Dialogs disclose governance and empower user autonomy. |
| **Authority to Control** | Users retain opt-in/opt-out control for all sensitive actions. |
| **Responsibility** | Audit trails captured for all modal interactions. |
| **Ethics** | Tone is neutral, non-coercive, avoiding urgency language unless truly required. |

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|-------|--------|---------|
| v10.4.1 | 2025-11-16 | Accessibility Council | Updated to KFM-MDP v10.4.3; added provenance annotations + extended ethics cues. |
| v10.0.0 | 2025-11-10 | FAIR+CARE A11y Council | Initial accessible modal standard. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Maintained under **Master Coder Protocol v6.3** · Verified by **FAIR+CARE Council**  
[⬅ Back to Patterns Index](README.md) · [Next → Forms](forms.md)

</div>