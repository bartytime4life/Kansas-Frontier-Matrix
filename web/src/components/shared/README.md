---
title: "🔧 Kansas Frontier Matrix — Shared UI Components Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/components/shared/README.md"
version: "v11.2.2"
last_updated: "2025-11-30"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.2/web-shared-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/web-components-shared-v2.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

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
intent: "web-components-shared"
semantic_intent:
  - "UI-primitive"
  - "design-system"
  - "a11y-foundation"

fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk (component-level)"
sensitivity_level: "None"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false

provenance_chain:
  - "web/src/components/shared/README.md@v10.4.0"
  - "web/src/components/shared/README.md@v10.3.2"

ontology_alignment:
  cidoc: "E28 Conceptual Object"
  schema_org: "WebPageElement"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"

json_schema_ref: "../../../../schemas/json/web-components-shared-readme-v11.schema.json"
shape_schema_ref: "../../../../schemas/shacl/web-components-shared-readme-v11-shape.ttl"
doc_uuid: "urn:kfm:doc:web-components-shared-readme-v11.2.2"
semantic_document_id: "kfm-doc-web-components-shared-readme-v11"
event_source_id: "ledger:web/src/components/shared/README.md"
immutability_status: "version-pinned"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "diagram-extraction"
ai_transform_prohibited:
  - "summaries"
  - "unverified-historical-claims"
  - "speculative-additions"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Structure"
    - "🧩 Component Responsibilities"
    - "🔐 Governance & FAIR+CARE Responsibilities"
    - "♿ Accessibility Requirements (WCAG 2.1 AA+)"
    - "📈 Telemetry Responsibilities"
    - "🧪 Testing Requirements"
    - "🕰 Version History"
    - "⚖️ Footer"
---

<div align="center">

# 🔧 **Kansas Frontier Matrix — Shared UI Components Overview**  
`web/src/components/shared/README.md`

**Purpose:**  
Define the shared, reusable UI primitives used across the entire KFM Web Platform.  
These components provide accessible, FAIR+CARE-aligned building blocks used by  
features, pipelines, pages, and layouts to ensure a consistent, ethical, and  
governance-compliant user interface.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)]()  
[![KFM-MDP v11.2.2](https://img.shields.io/badge/KFM%E2%80%93MDP-v11.2.2-purple)]()  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Low%20Risk-gold)]()  
[![WCAG AA+](https://img.shields.io/badge/A11y-WCAG%202.1%20AA%2B-brightgreen)]()

</div>

---

## 📘 Overview

Shared UI components:

- Provide **fundamental UI building blocks**  
- Are used across all features (Focus Mode, Story Nodes, Timeline, STAC, Governance, Map, etc.)  
- Must be:
  - Deterministic  
  - Accessible (WCAG 2.1 AA+)  
  - Governance-aware where applicable  
  - Telemetry-enabled when interactive  
  - Free of business logic and data fetching  
  - Consistent with the design system tokens (spacing, typography, color, motion)  
- Must avoid speculative behavior, unsafe content rendering, or bypassing CARE masking rules  

Shared components form the **common visual vocabulary** for the entire KFM Web Platform.

---

## 🗂️ Directory Structure

~~~text
web/src/components/shared/
│
├── 🔘 Button.tsx                 # Accessible button with WCAG AA+ color tokens
├── 🖱️ IconButton.tsx             # Icon-only button with ARIA labels
├── 🧭 Dropdown.tsx               # Keyboard-navigable dropdown menu
├── 🗂️ Tabs.tsx                   # Tabbed interface with focus management
├── 🪟 Modal.tsx                  # Accessible modal with focus trapping & ARIA
├── 💬 Tooltip.tsx                # Accessible tooltip with semantic descriptions
├── 🔄 Spinner.tsx                # Loading indicator (reduced-motion safe)
├── 🏷️ Badge.tsx                  # Semantic label with A11y-safe contrast
├── 🗃️ Card.tsx                   # Standardized container with design tokens
└── 📝 FormControls/              # Shared form inputs
    ├── TextInput.tsx
    ├── Checkbox.tsx
    ├── RadioGroup.tsx
    └── Select.tsx
~~~

---

## 🧩 Component Responsibilities

### 🔘 Button.tsx

**Role:**  
Primary clickable action primitive.

**Responsibilities:**

- Fully keyboard-accessible  
- WCAG 2.1 AA+ contrast compliant  
- Clear disabled states and focus-visible outlines  
- Never performs side effects (logic lives in handlers passed as props)  

**Telemetry (via parent wiring):**

- `"ui:button-click"` (prop-driven; this component only calls handler props)  

---

### 🖱️ IconButton.tsx

**Role:**  
Icon-only button with strong accessibility guarantees.

**Requirements:**

- MUST provide `aria-label` or nested visible label  
- MUST have clear focus indicator  
- MUST not rely on color alone to indicate state  
- Respect theme and high-contrast tokens  

---

### 🧭 Dropdown.tsx

**Role:**  
Reusable dropdown / select menu.

**Responsibilities:**

- Keyboard navigation:
  - Arrow keys to move between options  
  - ESC to close  
  - Enter/Space to select  
- Expose roles/apps as:
  - `role="listbox"` or `role="menu"` depending on usage pattern  

**Telemetry:**

- `"ui:dropdown-open"`  
- `"ui:dropdown-select"`  

---

### 🗂️ Tabs.tsx

**Role:**  
Shared tab system for top-level and nested tabbed interfaces.

**Responsibilities:**

- Implement ARIA `tablist`, `tab`, `tabpanel` semantics  
- Ensure:
  - Arrow-key navigation between tabs  
  - Proper focus management  
  - Association via `aria-controls` / `aria-labelledby`  

**Telemetry:**

- `"ui:tab-change"`  

---

### 🪟 Modal.tsx

**Role:**  
Generic modal layout and behavior.

**Responsibilities:**

- Focus trapping inside modal content  
- `aria-modal="true"` and `role="dialog"`/`"alertdialog"` as needed  
- Close on:
  - ESC key  
  - designated close button  
- Prevent scroll bleed behind overlay  

**Governance (when used for sensitive content):**

- Must allow injection of governance warnings/CARE labels in the header/body from parent components  

**Telemetry:**

- `"ui:modal-open"`  
- `"ui:modal-close"`  

---

### 💬 Tooltip.tsx

**Role:**  
Shared tooltip for hover/focus hints.

**Requirements:**

- Non-hover-only access (keyboard focus triggers)  
- Descriptive, concise content (NO speculative or sensitive text)  
- WCAG AA+ contrast for text and background  
- Dismissible via ESC or blur  

---

### 🔄 Spinner.tsx

**Role:**  
Loading indicator primitive.

**Requirements:**

- Honor `prefers-reduced-motion` (static or minimal motion variant)  
- High-contrast and visible against backgrounds  
- No telemetry (unless explicitly wrapped by parent monitoring)  

---

### 🏷️ Badge.tsx

**Role:**  
Generic label for statuses, small tags, and category indicators.

**Usage:**

- Status indication (e.g., “Beta”, “Draft”, “Synced”)  
- Dataset type or view tags  
- A11y hints (e.g., “Keyboard shortcut available”)  

**Requirements:**

- WCAG AA+ contrast  
- No misuse for CARE or sovereignty classification (that is handled by Governance components)  

---

### 🗃️ Card.tsx

**Role:**  
Generic layout container with standardized padding and style tokens.

**Responsibilities:**

- Provide:
  - header/body/footer slots (via children or composition)  
  - consistent padding, border radius, shadows  
- Semantics:
  - typically `role="group"` or `<section>` with heading, depending on usage  

Card is frequently used across:

- Story Node lists  
- Focus Mode sidebars  
- Governance panels  
- Dataset lists  

---

### 📝 FormControls/

**Role:**  
Shared form primitives for text input and selection.

**Includes:**

- `TextInput.tsx`  
- `Checkbox.tsx`  
- `RadioGroup.tsx`  
- `Select.tsx`  

**Requirements:**

- Correct ARIA attributes:
  - `aria-labelledby`, `aria-describedby` as needed  
- Label association via `<label>` or `aria-label`  
- Visible focus ring  
- High-contrast text/borders  

**Telemetry (via parent wiring):**

- `"ui:input-change"`  
- `"ui:checkbox-toggle"`  
- `"ui:select-change"`  

---

## 🔐 Governance & FAIR+CARE Responsibilities

Shared UI components are low-risk but still part of the **governance surface**.

They MUST:

- Respect CARE and sovereignty flags passed down from parent components (e.g., to show/hide specific actions)  
- Never themselves:
  - Render restricted coordinates or other sensitive data  
  - Inject speculative or unverified text (no content generation)  
- Provide clear surfaces where parent components can mount CARE or governance-specific elements (e.g., warnings inside Modal header/body)  
- Avoid color usage that may conflict with governance color coding (e.g., reserved colors for CARE statuses)

Breaking these patterns at the shared component level has system-wide impact; if governance policies are violated via shared components, that is a **CI-blocking** issue.

---

## ♿ Accessibility Requirements (WCAG 2.1 AA+)

Shared components are the **foundation of UI accessibility**.

They MUST:

- Provide correct ARIA roles and attributes:
  - `button`, `dialog`, `tablist`/`tab`, `listbox`, etc.  
- Guarantee keyboard operability:
  - Tab-order support  
  - Key-specific behaviors (arrows in menus/tabs, ESC to close modals)  
- Maintain:
  - Visible focus outlines  
  - 4.5:1 contrast ratio for text and critical UI elements  
- Respect user preferences (reduced-motion, high contrast modes)  
- Work correctly with screen readers (labels, announcements, and region semantics)

Any A11y regression MUST block merges.

---

## 📈 Telemetry Responsibilities

Shared components support telemetry, but they should **not hardcode analytics**; instead, they:

- Provide optional callbacks/hooks so higher-level components can emit events such as:
  - `"ui:button-click"`  
  - `"ui:dropdown-open"` / `"ui:dropdown-select"`  
  - `"ui:tab-change"`  
  - `"ui:modal-open"` / `"ui:modal-close"`  
  - `"ui:input-change"` / `"ui:checkbox-toggle"` / `"ui:select-change"`  

Telemetry MUST:

- Be non-PII  
- Match the schema defined in `telemetry_schema`  
- Include component/version metadata so we can track behavior over releases  

---

## 🧪 Testing Requirements

Each shared component MUST have:

- **Unit tests**:
  - Rendering with typical and edge props  
  - State/prop changes reflected in DOM  

- **Accessibility tests**:
  - Keyboard navigation and focus handling  
  - ARIA roles and labels  
  - Color contrast checks where applicable  

- **Telemetry tests** (for interactive components):
  - Events fired when triggers (click, open, change) happen  
  - Event payloads conform to expected shape (through parent wrappers)  

- **Optional snapshot tests**:
  - For visual regression guarding on stable components  

Test directory:

~~~text
tests/unit/web/components/shared/**
tests/integration/web/components/shared/**
~~~

---

## 🕰 Version History

| Version | Date       | Summary                                                                 |
|--------:|------------|-------------------------------------------------------------------------|
| v11.2.2 | 2025-11-30 | Upgraded to v11.2.2; enriched metadata, A11y requirements, telemetry v2 |
| v10.4.0 | 2025-11-15 | KFM-MDP v10.4 rewrite; governance, A11y, telemetry updates               |
| v10.3.2 | 2025-11-14 | Added Dropdown + FormControls refinements                               |
| v10.3.1 | 2025-11-13 | Initial shared components overview                                     |

---

## ⚖️ Footer

<div align="center">

**📚 Governance Links**  
[Docs Root](../../../../README.md) •  
[Standards Index](../../../../docs/standards/INDEX.md) •  
[Governance Charter](../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

**🔐 Compliance:**  
FAIR+CARE · CIDOC-CRM · OWL-Time · PROV-O · WCAG 2.1 AA+ · SLSA Level 3

**End of Document**

</div>