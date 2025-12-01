---
title: "📝 Kansas Frontier Matrix — Shared Form Controls Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/components/shared/FormControls/README.md"
version: "v11.2.2"
last_updated: "2025-11-30"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/web-formcontrols-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/web-components-formcontrols-v2.json"
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
classification: "Public Document"
jurisdiction: "United States / Kansas"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

status: "Active / Enforced"
doc_kind: "Component Overview"
intent: "web-components-formcontrols"
semantic_intent:
  - "UI-primitive"
  - "form-controls"
  - "a11y-foundation"

fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk (UI-only)"
sensitivity_level: "None"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false

provenance_chain:
  - "web/src/components/shared/FormControls/README.md@v10.4.0"
  - "web/src/components/shared/FormControls/README.md@v10.3.2"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "WebPageElement"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"

json_schema_ref: "../../../../../schemas/json/web-components-formcontrols-readme-v11.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/web-components-formcontrols-readme-v11-shape.ttl"
doc_uuid: "urn:kfm:doc:web-components-formcontrols-readme-v11.2.2"
semantic_document_id: "kfm-doc-web-components-formcontrols-readme-v11"
event_source_id: "ledger:web/src/components/shared/FormControls/README.md"
immutability_status: "version-pinned"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "diagram-extraction"
ai_transform_prohibited:
  - "summaries"
  - "speculative-additions"
  - "unverified-historical-claims"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Structure"
    - "🧩 Component Responsibilities"
    - "🔐 FAIR+CARE & Governance Responsibilities"
    - "♿ Accessibility Requirements (WCAG 2.1 AA+)"
    - "📈 Telemetry Responsibilities"
    - "🧪 Testing Requirements"
    - "🕰 Version History"
    - "⚖️ Footer"
---

<div align="center">

# 📝 **Kansas Frontier Matrix — Shared Form Controls Overview**  
`web/src/components/shared/FormControls/README.md`

**Purpose:**  
Describe the **shared, accessible, FAIR+CARE-compliant form controls** used across the  
KFM Web Platform.  
These controls provide the foundation for filters, inputs, search bars, configuration panels,  
and interaction surfaces within STAC/DCAT explorers, Focus Mode, Story Nodes, governance drawers,  
and map tools.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)]()  
[![KFM-MDP v11.2.2](https://img.shields.io/badge/KFM%E2%80%93MDP-v11.2.2-purple)]()  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Low%20Risk-gold)]()  
[![WCAG AA+](https://img.shields.io/badge/A11y-WCAG%202.1%20AA%2B-brightgreen)]()

</div>

---

## 📘 Overview

The **FormControls** directory contains the **universal input primitives** for the entire web platform:

- Fully accessible (WCAG 2.1 AA+)  
- Deterministic, prop-driven behavior  
- Governance-aware where needed (e.g., toggling masking, consent)  
- Integrated with telemetry via parent components  
- Designed with design tokens in `web/src/styles/tokens/**` for spacing, colors, motion  
- Stable and predictable across all features  

They MUST:

- Never bypass governance restrictions that parent components enforce  
- Never reveal sensitive dataset, coordinate, or internal ID information in labels/placeholders  
- Never produce speculative or unverified outputs (no content generation)  
- Always support keyboard + screen-reader workflows  
- Remain logic-light and presentation-focused (no hidden business logic)  

These components form the baseline interaction layer for the entire frontend.

---

## 🗂️ Directory Structure

~~~text
web/src/components/shared/FormControls/
│
├── ✏️ TextInput.tsx            # Accessible text field with labels, descriptions, and error states
├── ☑️ Checkbox.tsx             # Boolean toggle with clear A11y semantics
├── 🔘 RadioGroup.tsx           # Mutually exclusive option selection control
├── 🔽 Select.tsx               # Dropdown/select control (keyboard-first)
├── 🔀 ToggleSwitch.tsx         # A11y-safe toggle for binary feature flags
└── 🏷️ FieldLabel.tsx           # Standardized label + description + helper text container
~~~

Changes to this directory MUST be reflected here and in the responsibilities section.

---

## 🧩 Component Responsibilities

### ✏️ TextInput.tsx

**Role:**  
Core text entry primitive.

**Responsibilities:**

- Render input with:
  - Proper `<label>` association or `aria-label`  
  - `aria-describedby` for helper/error text where applicable  
- Provide:
  - Error state styles with SR announcements  
  - High contrast text and border colors  

**Governance:**

- When used for dataset or entity searches, must avoid displaying:
  - raw IDs  
  - restricted identifiers in placeholder or default values  
- Must accept governance hints (e.g., show warnings around certain fields) from parent components.

**Telemetry (parent-level wiring):**

- `"ui:input-change"`  

---

### ☑️ Checkbox.tsx

**Role:**  
Shared checkbox for boolean state.

**Responsibilities:**

- Large click target (~44×44px minimum)  
- Visible focus outline  
- Clear checked/unchecked/indeterminate states  
- Proper `<input type="checkbox">` semantics and labels  

**Governance:**

- May be used for consent or toggling governance features (e.g., “show masked geometries”)  
- Must not silently bypass consent semantics: parent components must wire any side effects explicitly.

**Telemetry:**

- `"ui:checkbox-toggle"`  

---

### 🔘 RadioGroup.tsx

**Role:**  
Grouping of radio buttons when exactly one option may be selected.

**Responsibilities:**

- Wrapped in `<fieldset>` with `<legend>` describing the choice set  
- Arrow-key navigation between radio options  
- Clear grouping semantics for screen readers  

**Governance:**

- May present different options depending on CARE/sovereignty context (via props)  
- In all cases, options themselves and any restrictions are determined by parent components.

**Telemetry:**

- `"ui:radio-select"`  

---

### 🔽 Select.tsx

**Role:**  
Shared select/dropdown control (list-like selection).

**Responsibilities:**

- ESC to close  
- Arrow keys to traverse list items  
- Enter/Space to select  
- Announce current selection via screen-reader text  

**Governance:**

- Parent components may disable/gray out restricted options; Select must:
  - visually indicate disabled items  
  - provide tooltips or helper text (if passed in) explaining why options are disabled  

**Telemetry:**

- `"ui:select-change"`  

---

### 🔀 ToggleSwitch.tsx

**Role:**  
Binary toggle styled as a switch.

**Responsibilities:**

- Implement ARIA `role="switch"` with:
  - `aria-checked` state  
  - full keyboard toggling via Space/Enter  
- Provide clear ON/OFF states through color + position (and text where necessary)  

**Governance:**

- Frequently used for feature flags like:
  - “Show generalized geometries only”  
  - “Enable advanced filters”  
- Parent components must ensure toggling is consistent with CARE policy.

**Telemetry:**

- `"ui:toggle-switch"`  

---

### 🏷️ FieldLabel.tsx

**Role:**  
Reusable container for label, description, and helper/error text for any control.

**Responsibilities:**

- Provide:
  - Visual label  
  - Optional description text (e.g., “Date range must not exceed 10 years”)  
  - Space for inline CARE/governance notices where appropriate  
- Ensure label and description connect to inputs via correct IDs / ARIA attributes.

**Governance:**

- When a control relates to governance or CARE (e.g., “Restrict to generalized view”), FieldLabel may carry the textual explanation given by parent components.

---

## 🔐 FAIR+CARE & Governance Responsibilities

Even though FormControls are **UI-only**, they are still used in contexts governing access to sensitive data.

They MUST:

- Respect any governance hints (props) from parent components, such as:
  - show a warning message in FieldLabel when a field affects sensitive behavior  
  - disable toggles that would violate CARE rules  
- Never:
  - Show raw coordinates or dataset IDs in placeholder or auto-complete text  
  - Display restricted metadata directly in UI scaffolding (labels, hints)  
- Provide surfaces for provenance or governance notes when used in such contexts (e.g., Modal + FieldLabel combination).

Governance-related issues cause wide-spread impact; any violation discovered at this level is a **CI-blocking** problem.

---

## ♿ Accessibility Requirements (WCAG 2.1 AA+)

FormControls are central to UI accessibility and MUST:

- Support full keyboard navigation and usage  
- Provide accessible names via `<label>` or ARIA attributes  
- Avoid placeholder-only labeling (placeholder is never the only label)  
- Maintain visible focus outlines for all focusable controls  
- Uphold WCAG 2.1 AA+ contrast requirements for text and input borders  
- Respect user preferences such as reduced-motion (for toggled states)  
- Work correctly with screen readers (announcing states, errors, and instructions)  

Accessibility regressions MUST block merges.

---

## 📈 Telemetry Responsibilities

FormControls themselves do not have to emit telemetry directly, but they are commonly wrapped in telemetry-aware contexts.

Typical events (wired by parent components) include:

- `"ui:input-change"`  
- `"ui:checkbox-toggle"`  
- `"ui:radio-select"`  
- `"ui:select-change"`  
- `"ui:toggle-switch"`  

Telemetry MUST:

- Be non-PII  
- Adhere to the shape defined in `telemetry_schema`  
- Include component and version metadata at the point of emission  

---

## 🧪 Testing Requirements

Tests MUST verify:

- **Unit level:**
  - Correct rendering of each control with minimal and full props  
  - Controlled/uncontrolled behavior as designed  

- **Accessibility:**
  - Correct ARIA usage  
  - Keyboard operability and focus management  
  - Label association and error announcements  

- **Telemetry (where parent wiring is provided in tests):**
  - Emission of expected events on interaction  
  - No extra or double emission  

- **Governance passthrough:**
  - Props used to indicate restrictions or warnings are rendered and not ignored  

Test locations:

~~~text
tests/unit/web/components/shared/FormControls/**
tests/integration/web/components/shared/FormControls/**
~~~

---

## 🕰 Version History

| Version | Date       | Summary                                                                 |
|--------:|------------|-------------------------------------------------------------------------|
| v11.2.2 | 2025-11-30 | Upgraded to v11.2.2; enriched metadata, governance + A11y clarifications, telemetry v2 |
| v10.4.0 | 2025-11-15 | Full WCAG + CARE-aligned rebuild; toggle + FieldLabel + telemetry rules |
| v10.3.2 | 2025-11-14 | Improved Select + Checkbox accessibility patterns                      |
| v10.3.1 | 2025-11-13 | Initial FormControls structure                                         |

---

## ⚖️ Footer

<div align="center">

**📚 Governance Links**  
[Docs Root](../../../../../README.md) •  
[Standards Index](../../../../../docs/standards/INDEX.md) •  
[Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

**🔐 Compliance:**  
FAIR+CARE · CIDOC-CRM · OWL-Time · PROV-O · WCAG 2.1 AA+ · SLSA Level 3

**End of Document**

</div>