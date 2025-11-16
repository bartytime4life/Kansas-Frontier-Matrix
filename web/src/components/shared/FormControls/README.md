---
title: "📝 Kansas Frontier Matrix — Shared Form Controls Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/components/shared/FormControls/README.md"
version: "v10.4.0"
last_updated: "2025-11-15"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/web-components-formcontrols-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Component Overview"
intent: "web-components-formcontrols"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk (UI-only)"
sensitivity_level: "None"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false
provenance_chain:
  - "web/src/components/shared/FormControls/README.md@v10.3.2"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "WebPageElement"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
json_schema_ref: "../../../../../schemas/json/web-components-formcontrols-readme.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/web-components-formcontrols-readme-shape.ttl"
doc_uuid: "urn:kfm:doc:web-components-formcontrols-readme-v10.4.0"
semantic_document_id: "kfm-doc-web-components-formcontrols-readme"
event_source_id: "ledger:web/src/components/shared/FormControls/README.md"
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
  - "unverified historical claims"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "United States / Kansas"
classification: "Public Document"
role: "overview"
lifecycle_stage: "stable"
ttl_policy: "Annual review"
sunset_policy: "Superseded upon next FormControls system update"
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

</div>

---

# 📘 Overview

The **FormControls** directory contains the **universal input primitives** for the entire web platform:

- Fully accessible  
- Deterministic behavior  
- Governance-aware where needed  
- Integrated with the telemetry system  
- Designed with WCAG 2.1 AA and reduced-motion constraints  
- Stable and predictable across all features  

They MUST:

- Never bypass governance restrictions  
- Never reveal sensitive dataset information  
- Never produce speculative or unsafe outputs  
- Always support keyboard + screen-reader workflows  
- Use design tokens defined in `web/src/styles/tokens/**`  

These components form the baseline interaction layer for the entire frontend.

---

# 🧱 Directory Structure

~~~text
web/src/components/shared/FormControls/
├── TextInput.tsx            # Accessible text field w/ validation
├── Checkbox.tsx             # Boolean toggle w/ CARE-aware labeling
├── RadioGroup.tsx           # Mutually exclusive option selection
├── Select.tsx               # Dropdown/select control (keyboard-friendly)
├── ToggleSwitch.tsx         # A11y-safe toggle for binary feature flags
└── FieldLabel.tsx           # Standardized label + description container
~~~

---

# 🧩 Component Responsibilities

## ✏️ **TextInput.tsx**
Provides:

- Clear, accessible text entry  
- ARIA-labeled structure  
- Error states with screen-reader support  
- High-contrast color rules  

Governance:

- Must sanitize text when used for dataset searches  
- Must avoid leaking internal IDs or sensitive metadata  

Telemetry:

- `"ui:input-change"`  

---

## ☑️ **Checkbox.tsx**
Accessible checkbox component.

Requirements:

- Clickable area ≥ 44×44px  
- Visible focus ring  
- AC-compliant contrast palette  
- Indeterminate state support  

Governance:

- CARE warnings may appear as contextual tooltips  

Telemetry:

- `"ui:checkbox-toggle"`  

---

## 🔘 **RadioGroup.tsx**
Used when only one option may be selected.

Requirements:

- Arrow key navigation  
- Semantic `<fieldset>` + `<legend>`  
- Clear grouping  

Governance:

- May expose alternative views depending on sovereignty restrictions  

Telemetry:

- `"ui:radio-select"`  

---

## 🔽 **Select.tsx**
Keyboard-friendly dropdown.

Requirements:

- ESC to close  
- Arrow keys traverse options  
- Screen-reader announcements of selection  
- High-contrast mode support  

Governance:

- Restricted options must be disabled + explained  
- Tooltip may show rights-holder or CARE notes  

Telemetry:

- `"ui:select-change"`  

---

## 🔀 **ToggleSwitch.tsx**
Binary state toggle.

Requirements:

- ARIA-compliant switch role  
- Keyboard-triggered (`Space` + `Enter`)  
- Reduced-motion-compliant transitions  

Governance:

- Used to toggle spatial masks or consent-based features  

Telemetry:

- `"ui:toggle-switch"`  

---

## 🏷️ **FieldLabel.tsx**
Standardized wrapper for labels, descriptions, and helper text.

Rules:

- Every input must be associated with a FieldLabel  
- Descriptions must be concise and non-speculative  
- Must support CARE warnings (e.g., “Generalized for sovereignty reasons”)  

---

# 🔐 FAIR+CARE & Governance Responsibilities

Form Controls must:

- Prevent unsafe user input paths  
- Display warnings near sensitive fields  
- Respect sovereignty boundaries (e.g., disabling certain map tools)  
- Ensure privacy of sensitive entries  
- Never leak raw coordinates or dataset IDs in placeholder text  
- Support provenance display when interacting with dataset metadata  

Governance failures → **hard CI failure**.

---

# ♿ Accessibility Requirements

All FormControls MUST:

- Support full keyboard operation  
- Provide semantic labeling  
- Respect extended contrast profiles  
- Support large-text mode  
- Avoid placeholder-only labeling  
- Maintain visible focus indicators  
- Validate input for A11y warnings (e.g., ambiguous date ranges)  

Accessibility regressions → **merge blocked**.

---

# 📈 Telemetry Responsibilities

FormControls must generate:

- `"ui:input-change"`  
- `"ui:checkbox-toggle"`  
- `"ui:radio-select"`  
- `"ui:select-change"`  
- `"ui:toggle-switch"`  

All telemetry must:

- Be schema-valid  
- Exclude PII  
- Include governance context when present  
- Flow to release bundles (`focus-telemetry.json`)  

---

# 🧪 Testing Requirements

Test coverage MUST include:

- Unit tests for each control  
- A11y tests (keyboard, ARIA, contrast)  
- Telemetry validation  
- Governance passthrough tests  
- Error-state visibility tests  
- RTL (React Testing Library) interaction checks  

Tests located at:

~~~text
tests/unit/web/components/shared/FormControls/**
tests/integration/web/components/shared/FormControls/**
~~~

---

# 🕰 Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v10.4.0 | 2025-11-15 | Full WCAG + CARE-aligned rebuild; added toggle + FieldLabel + extensive telemetry rules |
| v10.3.2 | 2025-11-14 | Improved Select + Checkbox accessibility patterns |
| v10.3.1 | 2025-11-13 | Initial FormControls structure |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
FAIR+CARE Certified · Public Document · Version-Pinned  
Validated under MCP-DL v6.3 & KFM-MDP v10.4  

</div>

