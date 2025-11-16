---
title: "🧠 Kansas Frontier Matrix — Web Context System Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/context/README.md"
version: "v10.4.0"
last_updated: "2025-11-15"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/web-context-readme-v1.json"
governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Overview"
intent: "web-context-overview"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk (logic-only)"
sensitivity_level: "None"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false
provenance_chain:
  - "web/src/context/README.md@v10.3.2"
  - "web/src/context/README.md@v10.3.1"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "SoftwareSourceCode"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
json_schema_ref: "../../../schemas/json/web-context-readme.schema.json"
shape_schema_ref: "../../../schemas/shacl/web-context-readme-shape.ttl"
doc_uuid: "urn:kfm:doc:web-context-readme-v10.4.0"
semantic_document_id: "kfm-doc-web-context-readme"
event_source_id: "ledger:web/src/context/README.md"
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
ttl_policy: "Review each release"
sunset_policy: "Superseded upon next state-layer overhaul"
---

<div align="center">

# 🧠 **Kansas Frontier Matrix — Web Context System Overview**  
`web/src/context/README.md`

**Purpose:**  
Document the **state management layer** of the Kansas Frontier Matrix Web Platform — including  
the contexts that manage time, focus, governance, accessibility, theming, and spatial/narrative  
synchronization across the entire frontend application.  
React Contexts in this directory serve as the *global, ethical, and deterministic state backbone*  
for all features, components, and pipelines.

</div>

---

# 📘 Overview

Contexts in `web/src/context/` provide:

- **Global state containers** shared across the Web Platform  
- Deterministic, typed state transitions  
- Mandatory governance (CARE/provenance) checks  
- Accessibility-first system settings  
- Synchronization for:
  - Timeline → Map  
  - Focus Mode → Story Nodes  
  - Governance → UI visibility  
  - Theme → Design system tokens  
- Centralized, predictable state orchestration  
- Telemetry-aware updates (non-PII)  

Contexts must remain:

- Pure  
- Type-safe  
- Predictable  
- Immutable state where possible  
- FAIR+CARE compliant  
- A11y aligned  
- Non-speculative  
- Free from UI logic  

---

# 🧱 Directory Structure

~~~text
web/src/context/
├── TimeContext.tsx             # Controls global timeline range + fuzzy intervals
├── FocusContext.tsx            # Entity in focus + narrative bundle + geometry
├── ThemeContext.tsx            # Light/dark + high-contrast-aware theme state
├── A11yContext.tsx             # Reduced-motion, high-contrast, large-text modes
├── GovernanceContext.tsx       # CARE, provenance, sovereignty flags + warnings
├── MapContext.tsx              # MapLibre + Cesium viewport + camera state
└── UIContext.tsx               # UI toggles (sidebars, panels, modals)
~~~

---

# 🧩 Context Responsibilities

## ⏱️ **TimeContext**
Responsible for:

- Current timeline window  
- OWL-Time interval normalization  
- Granularity (year/decade/century)  
- Temporal filters for:
  - Story Nodes  
  - STAC Items  
  - Map layers  
  - Focus Mode ranges  

Guarantees:

- No inconsistent temporal state  
- Fuzzy/uncertain dates handled ethically  
- Telemetry events: `"timeline:update"`  

---

## 🎯 **FocusContext**
Responsible for:

- Focus Mode v2.5 state  
- Selected entity + type  
- Narrative metadata (AI-labeled)  
- Graph neighbors  
- Story Node suggestions  
- Map highlight geometry  

Governance:

- CARE labeling  
- Provenance chips  
- Sovereignty-safe footprint handling  

Telemetry: `"focus:activate"`, `"focus:relation-select"`

---

## 🎨 **ThemeContext**
Controls:

- Light/dark modes  
- High-contrast variants  
- Design tokens for color/spacing/typography  
- Tailwind variable hydration  

A11y:

- Must respect `prefers-color-scheme`  
- Must ensure WCAG AA contrast  

---

## ♿ **A11yContext**
Tracks:

- Reduced-motion  
- High-contrast preference  
- Large-text mode  
- Screen-reader flags  

Context triggers A11y-safe component updates.

Telemetry: `"a11y:preference-change"`

---

## 🛡 **GovernanceContext**
Responsible for:

- CARE metadata  
- Sovereignty rules  
- Masking flags (H3 generalization)  
- Provenance display state  
- AI generation warnings  
- Data classification (Public / Restricted / Indigenous-controlled)

GovernanceContext MUST:

- Never expose restricted coordinates  
- Always propagate CARE flags to UI components  
- Block unsafe render flows  

Telemetry: `"governance:warning-shown"`

---

## 🗺️ **MapContext**
Stores:

- MapLibre viewport  
- Cesium camera position/time slice  
- Active layers  
- Highlight geometries  
- Map interaction state  

Used by:

- useMap  
- focusPipeline  
- storyPipeline  
- stacPipeline  

Telemetry: `"map:pan"`, `"map:zoom"`, `"map:layer-toggle"`

---

## 🖥️ **UIContext**
Controls:

- Sidebar open/close  
- Drawer states  
- Modal visibility  
- Toolbars  
- Panel layouts (e.g., SplitView)  

Ensures consistent UI transitions and predictable accessibility behavior.

---

# 🔐 FAIR+CARE & Governance Integration

Every context must:

- Enforce CARE flags  
- Respect sovereignty restrictions  
- Annotate AI-generated narrative sections  
- Prevent improper spatial or narrative exposure  
- Emit governance metadata for downstream UI layers  

Governance failures **block merges**.

---

# ♿ Accessibility Requirements

Contexts must:

- Respect system-level preferences  
- Guarantee predictable keyboard focus paths  
- Centralize accessibility preferences for all components  
- Not break screen-reader interactions  

A11y regressions fail CI.

---

# 📈 Telemetry Responsibilities

Each context must generate telemetry when:

- Global state changes  
- User interacts with time/focus/map/theme  
- Governance warnings are shown  
- A11y preferences updated  

Telemetry rules:

- Must follow schema  
- Must be non-PII  
- Must carry no sensitive coordinates  
- Stored in `focus-telemetry.json`

---

# 🧪 Testing Requirements

Each context requires:

- Unit tests for state transitions  
- Integration tests for cross-context sync  
- Telemetry correctness tests  
- Governance compliance  
- A11y preference propagation tests  
- Map/time/focus consistency tests  

Location:

~~~text
tests/unit/web/context/**
tests/integration/web/context/**
~~~

---

# 🕰 Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v10.4.0 | 2025-11-15 | Fully rewritten for KFM-MDP v10.4; added governance, A11y, telemetry, Focus Mode v2.5 alignment |
| v10.3.2 | 2025-11-14 | Added sovereignty + provenance integration |
| v10.3.1 | 2025-11-13 | Initial context layer documentation |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
Validated under MCP-DL v6.3 and KFM-MDP v10.4  
FAIR+CARE Certified · Public Document · Version-Pinned  

</div>