---
title: "🔧 Kansas Frontier Matrix — Shared UI Components Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/components/shared/README.md"
version: "v10.4.0"
last_updated: "2025-11-15"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/web-components-shared-v1.json"
governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Component Overview"
intent: "web-components-shared"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk (component-level)"
sensitivity_level: "None"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false
provenance_chain:
  - "web/src/components/shared/README.md@v10.3.2"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E28 Conceptual Object"
  schema_org: "WebPageElement"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
json_schema_ref: "../../../../schemas/json/web-components-shared-readme.schema.json"
shape_schema_ref: "../../../../schemas/shacl/web-components-shared-readme-shape.ttl"
doc_uuid: "urn:kfm:doc:web-components-shared-readme-v10.4.0"
semantic_document_id: "kfm-doc-web-components-shared-readme"
event_source_id: "ledger:web/src/components/shared/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "summaries"
  - "unverified historical claims"
  - "speculative additions"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "United States / Kansas"
classification: "Public Document"
role: "overview"
lifecycle_stage: "stable"
ttl_policy: "Annual review"
sunset_policy: "Superseded on shared-component system redesign"
---

<div align="center">

# 🔧 **Kansas Frontier Matrix — Shared UI Components Overview**  
`web/src/components/shared/README.md`

**Purpose:**  
Define the shared, reusable UI primitives used across the entire KFM Web Platform.  
These components provide accessible, FAIR+CARE-aligned building blocks used by  
features, pipelines, pages, and layouts to ensure a consistent, ethical, and  
governance-compliant user interface.

</div>

---

# 📘 Overview

Shared UI components:

- Provide **fundamental UI building blocks**  
- Are used across all features (Focus Mode, Story Nodes, Timeline, STAC, Governance, Map, etc.)  
- Must be:
  - Deterministic  
  - Accessible  
  - Governance-aware where applicable  
  - Telemetry-enabled when interactive  
  - Free of business logic  
  - Consistent with the design system tokens  
- Must avoid speculative behavior, unsafe content rendering, or bypassing CARE masking rules  

Shared components form the common visual vocabulary for the entire KFM Web Platform.

---

# 🧱 Directory Structure

~~~text
web/src/components/shared/
├── Button.tsx                  # Accessible button with WCAG AA color tokens
├── IconButton.tsx              # Icon-only button with ARIA labels
├── Dropdown.tsx                # Keyboard-navigable dropdown menu
├── Tabs.tsx                    # Tabbed interface with focus management
├── Modal.tsx                   # Accessible modal with focus trapping
├── Tooltip.tsx                 # Accessible tooltip with semantic descriptions
├── Spinner.tsx                 # Loading indicators (reduced-motion safe)
├── Badge.tsx                   # Semantic label with A11y-safe contrast
├── Card.tsx                    # Standardized container with design tokens
└── FormControls/               # Shared form inputs
    ├── TextInput.tsx
    ├── Checkbox.tsx
    ├── RadioGroup.tsx
    └── Select.tsx
~~~

---

# 🧩 Component Responsibilities

## 🔘 **Button.tsx**
- Fully keyboard-accessible  
- WCAG AA color contrast  
- Clear disabled state  
- Telemetry: `"ui:button-click"`  
- Must allow CARE-aware labeling if used in governance contexts  

---

## 🖱️ **IconButton.tsx**
- Must include `aria-label`  
- No color-only distinctions  
- Supports high-contrast and reduced-motion  

---

## 🧭 **Dropdown.tsx**
- Keyboard-navigable  
- ESC-to-close  
- Arrow key traversal  
- Screen-reader role: `listbox` or `menu`  
- Telemetry: `"ui:dropdown-open"`, `"ui:dropdown-select"`  

---

## 🗂️ **Tabs.tsx**
- Renders semantic tablist  
- Arrow-key navigation  
- Focus indicator  
- Accessible labels  
- Telemetry: `"ui:tab-change"`  

---

## 🪟 **Modal.tsx**
- Full A11y support:
  - Focus trapping  
  - ARIA labeling  
  - Escape key close  
  - Screen-reader announcements  
- Must show governance warnings if invoked for CARE-sensitive content  
- Telemetry: `"ui:modal-open"`, `"ui:modal-close"`  

---

## 💬 **Tooltip.tsx**
- Non-hover-only access (keyboard + touch friendly)  
- Descriptive content  
- WCAG AA contrast  
- Must be dismissible  
- Never show speculative or sensitive info  

---

## 🔄 **Spinner.tsx**
- Must respect `prefers-reduced-motion`  
- High-contrast mode safe  
- Telemetry-free (unless part of performance tracing)  

---

## 🏷️ **Badge.tsx**
General-purpose labeling component.

- High-contrast WCAG AA compliant  
- May be used for:
  - Status indicators  
  - Dataset categories  
  - Accessibility hints  
- NOT used for CARE labels (those live in Governance components)  

---

## 🗃️ **Card.tsx**
A structured container with:

- Standard padding (design tokens)  
- Shadow + radius tokens  
- Header/content/footer slots  
- Accessible heading baseline  

Used across Story Nodes, Focus Mode, STAC, governance views, and dashboards.

---

## 📝 **FormControls/**
Shared form inputs must:

- Support ARIA attributes  
- Use visible focus rings  
- Provide proper labels  
- Respect high-contrast + reduced-motion  
- Emit telemetry:
  - `"ui:input-change"`  
  - `"ui:checkbox-toggle"`  
  - `"ui:select-change"`  

---

# 🔐 Governance & FAIR+CARE Responsibilities

Even though shared components are generic, they MUST:

- Respect CARE visibility signals passed via props  
- Display masking/generalization banners when required (e.g., inside modal)  
- Never render:
  - Precise restricted coordinates  
  - Sensitive images  
  - Unverified historical claims  
- Avoid color misuse (no culturally inappropriate or misleading colors)  
- Preserve provenance metadata display where required  

Shared components act as **trusted primitives**—any governance slip here propagates across the entire platform.

---

# ♿ Accessibility Requirements

Shared components are **foundation A11y primitives** and therefore must:

- Use semantic roles  
- Guarantee keyboard operability  
- Show strong focus indicators  
- Maintain color contrast ≥ 4.5:1  
- Provide ARIA-compliant labels  
- Respect reduced-motion preferences  
- Be compatible with screen-readers  

Accessibility failures → **hard CI block**.

---

# 📈 Telemetry Responsibilities

Shared interactive components (Button, Dropdown, Modal, Tabs, FormControls) must emit standardized telemetry events:

- `"ui:button-click"`  
- `"ui:dropdown-open"`  
- `"ui:dropdown-select"`  
- `"ui:tab-change"`  
- `"ui:modal-open"` / `"ui:modal-close"`  
- `"ui:input-change"`  
- `"ui:checkbox-toggle"`  
- `"ui:select-change"`  

Telemetry must be:

- Non-PII  
- Schema-valid  
- Included in release-level telemetry bundles  

---

# 🧪 Testing Requirements

Each shared component MUST include:

- Unit tests  
- Accessibility tests (ARIA + keyboard)  
- Telemetry correctness tests  
- Snapshot tests (optional for visual baselines)  
- Governance passthrough tests (props honored)  

Tests located at:

~~~text
tests/unit/web/components/shared/**
tests/integration/web/components/shared/**
~~~

---

# 🕰 Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v10.4.0 | 2025-11-15 | Full KFM-MDP v10.4 rewrite; added A11y, governance, telemetry rules; expanded global primitive set |
| v10.3.2 | 2025-11-14 | Added Dropdown + FormControls refinements |
| v10.3.1 | 2025-11-13 | Initial shared components overview |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
FAIR+CARE Certified · Public Document · Version-Pinned  
Validated under MCP-DL v6.3 & KFM-MDP v10.4  

</div>

