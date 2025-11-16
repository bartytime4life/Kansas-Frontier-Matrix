---
title: "📐 Kansas Frontier Matrix — Layout Components Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/components/Layout/README.md"
version: "v10.4.0"
last_updated: "2025-11-15"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/web-components-layout-v1.json"
governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Component Overview"
intent: "web-components-layout"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk (layout-only)"
sensitivity_level: "None"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false
provenance_chain:
  - "web/src/components/Layout/README.md@v10.3.2"
  - "web/src/components/Layout/README.md@v10.3.1"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "WebPageElement"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
json_schema_ref: "../../../../schemas/json/web-components-layout-readme.schema.json"
shape_schema_ref: "../../../../schemas/shacl/web-components-layout-readme-shape.ttl"
doc_uuid: "urn:kfm:doc:web-components-layout-readme-v10.4.0"
semantic_document_id: "kfm-doc-web-components-layout-readme"
event_source_id: "ledger:web/src/components/Layout/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative additions"
  - "unverified historical claims"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "United States / Kansas"
classification: "Public Document"
role: "overview"
lifecycle_stage: "stable"
ttl_policy: "Review each release"
sunset_policy: "Superseded on next layout-system revision"
---

<div align="center">

# 📐 **Kansas Frontier Matrix — Layout Components Overview**  
`web/src/components/Layout/README.md`

**Purpose:**  
Define the layout system used across the KFM Web Platform — including containers, shells, panels, navigation  
structures, and accessibility scaffolding that ensures every page and feature is presented in a coherent,  
WCAG-compliant, FAIR+CARE-aware UI architecture.

</div>

---

# 📘 Overview

Layout components define **the structural foundation** of the Web Platform UI.  
They ensure:

- Consistent page scaffolding  
- Accessible navigation patterns  
- FAIR+CARE metadata visibility  
- Predictable responsive behavior  
- Integration with global contexts (theme, governance, A11y, time, focus)  
- A clean separation between layout and feature components  
- Deterministic rendering with no business logic  

Layout components must:

- Be **pure presentation**  
- Use **semantic HTML regions**  
- Propagate **A11y tokens**  
- Leave data-processing to hooks/pipelines  

---

# 🧱 Directory Structure

~~~text
web/src/components/Layout/
├── Header.tsx                # Global top bar w/ navigation + governance links
├── Sidebar.tsx               # Left/right navigation sidebar (collapsible, accessible)
├── Panel.tsx                 # Generic panel container (story, focus, datasets)
├── PageContainer.tsx         # Top-level page wrapper w/ theming + A11y roles
├── Section.tsx               # Accessible sectional content block
├── SplitView.tsx             # Horiz/vertical split panes (map + narrative layout)
├── Toolbar.tsx               # Tool/action bar w/ icons + keyboard shortcuts
└── ModalLayout.tsx           # Accessible modal scaffolding (focus trapping)
~~~

---

# 🧩 Component Responsibilities

## 🧭 Header.tsx  
- Provides site-wide navigation  
- Displays governance links (CARE, provenance, license)  
- Houses global search (if enabled)  
- A11y:
  - Semantic `<header>` landmark  
  - High-contrast color usage  
  - Skip-to-content link  

---

## 📚 Sidebar.tsx  
- Contains navigation tree  
- Collapsible  
- Must support:
  - Keyboard navigation  
  - Screen-reader labels  
- CARE-specific sections must be clearly labeled  

---

## 🧱 PageContainer.tsx  
Defines the global content frame:

- Applies theme + A11y tokens  
- Wraps FocusContext, TimeContext, GovernanceContext  
- Provides semantic `<main>` region  
- Ensures proper scrolling + `tabIndex` behavior  

---

## 🗂 Panel.tsx  
Reusable container for:

- Story Node detail  
- Focus Mode panel  
- Dataset details  
- Governance drawers  

A11y rules:

- Accessible headers  
- Focus trapping for modal-like behaviors  
- Skip links if scrollable  

---

## 🧩 Section.tsx  
Used for document-like content areas:

- Story Node narrative blocks  
- Timeline explanations  
- Governance notices  

Sections must:

- Maintain accessible heading order  
- Provide logical reading flow  
- Use WCAG AA color/spacing tokens  

---

## 🔀 SplitView.tsx  
Manages side-by-side layouts:

- Map + Narrative  
- Map + Timeline  
- Focus Mode + Map  

Requirements:

- Keyboard-resizable panes  
- ARIA roles for `separator`  
- Respect reduced-motion  

---

## 🛠 Toolbar.tsx  
Provides:

- Feature tool buttons  
- Map tools  
- Timeline granularity controls  
- Focus Mode actions  

Rules:

- Every tool must have:
  - Visible label or ARIA-label  
  - Keyboard shortcut annotation  
  - Telemetry event (`ui:tool-activated`)  

---

## 🪟 ModalLayout.tsx  
For all modal/drawer-based layout elements:

- Ensures focus trapping  
- Prevents scroll bleed  
- Ensures escape/close via keyboard  
- Provides high-contrast dimming layers  

Used for:

- GovernanceDrawer  
- Story Node media viewer  
- Dataset metadata view  

---

# 🔐 FAIR+CARE Integration

Layout components must always expose:

- CARE classification when the page displays sensitive material  
- Warnings for sovereignty-controlled content  
- Ethical context blocks when AI narratives appear  
- Provenance chips in persistent layout regions (e.g., header/footer)  

Layout must **never hide** governance information through scrolling or navigation omission.

---

# ♿ Accessibility Requirements

All layout components must:

- Use semantic landmarks (`header`, `nav`, `main`, `aside`, `footer`)  
- Maintain heading structure  
- Offer predictable keyboard behavior  
- Respect high-contrast and reduced-motion settings  
- Provide clear focus outlines  
- Offer skip-to-content behavior  

Accessibility violations block CI.

---

# 📈 Telemetry Responsibilities

Layout generates telemetry for:

- Page enters/leaves  
- Sidebar open/close  
- Modal open/close  
- Tool activation via toolbar  
- SplitView interactions  
- Scroll-depth (non-PII)  
- Theme/A11y toggles  

Telemetry flows into:

`releases/<version>/focus-telemetry.json`

All telemetry must be non-PII and schema-valid.

---

# 🧪 Testing Requirements

Each layout component requires:

- Unit tests  
- Integration tests (layout + features)  
- A11y tests  
- Telemetry tests  
- Governance visibility checks  

Tests stored under:

~~~text
tests/unit/web/components/layout/**
tests/integration/web/components/layout/**
~~~

---

# 🕰 Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v10.4.0 | 2025-11-15 | Complete layout overview per KFM-MDP v10.4; added A11y, governance, telemetry rules |
| v10.3.2 | 2025-11-14 | Improved SplitView + Header governance patterns |
| v10.3.1 | 2025-11-13 | Initial layout documentation |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
Reviewed under MCP-DL v6.3 and KFM-MDP v10.4  
FAIR+CARE Certified · Public Document · Version-Pinned  

</div>