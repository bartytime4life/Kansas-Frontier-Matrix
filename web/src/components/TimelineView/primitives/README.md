---
title: "⏱️ Kansas Frontier Matrix — TimelineView Primitives Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/components/TimelineView/primitives/README.md"
version: "v10.4.0"
last_updated: "2025-11-15"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/web-components-timelineview-primitives-v1.json"
governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.1"
status: "Active / Enforced"
doc_kind: "Component Overview"
intent: "web-components-timeline-primitives"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Temporal-Dependent"
sensitivity_level: "Low"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false
provenance_chain:
  - "web/src/components/timeline/README.md@v10.3.1"
  - "web/src/components/TimelineView/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E52 Time-Span"
  schema_org: "WebPageElement"
  owl_time: "TemporalEntity"
  prov_o: "prov:Entity"
json_schema_ref: "../../../../../../schemas/json/web-components-timelineview-primitives.schema.json"
shape_schema_ref: "../../../../../../schemas/shacl/web-components-timelineview-primitives-shape.ttl"
doc_uuid: "urn:kfm:doc:web-components-timelineview-primitives-v10.4.0"
semantic_document_id: "kfm-doc-web-components-timelineview-primitives"
event_source_id: "ledger:web/src/components/TimelineView/primitives/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Forbidden (logic-free primitives)"
ai_transform_permissions:
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "summaries"
  - "temporal inference"
  - "speculative chronology"
  - "unverified historical claims"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "United States / Kansas"
classification: "Public Document"
role: "overview"
lifecycle_stage: "stable"
ttl_policy: "Review each release"
sunset_policy: "Superseded upon TimelineView v3 primitive upgrade"
---

<div align="center">

# ⏱️ **Kansas Frontier Matrix — TimelineView Primitives Overview**  
`web/src/components/TimelineView/primitives/README.md`

**Purpose:**  
Document the **Timeline UI primitives** that form the foundational elements of the  
KFM TimelineView system.  
These primitives were originally part of the old `timeline/` folder and now live  
under `TimelineView/primitives/` to support the fully orchestrated TimelineView v2 architecture.

They remain FAIR+CARE-governed, WCAG-compliant, deterministic, and non-speculative.

</div>

---

# 📘 Overview

Timeline primitives are:

- Low-level UI building blocks  
- Used strictly **inside** TimelineView  
- Wrapped by higher-order components such as:
  - `TimelinePrimary`
  - `TimelineControls`
  - `TimelineMarkersLayer`
  - `TimelineA11yHelpers`
- Not imported outside the TimelineView domain  
- Designed to produce stable, predictable visual behaviors  
- Fully FAIR+CARE-governed  
- Fully WCAG AA compliant  

They must not:

- Create timeline logic  
- Perform timeline filtering  
- Alter temporal ranges or derive temporal meaning  
- Display speculative or uncertain temporal narrative  
- Handle sensitive temporal metadata outside governance rules  

---

# 🧱 Directory Structure (Labeled)

~~~text
web/src/components/TimelineView/primitives/
├── TimelineBar.tsx            # Core time-axis visual renderer
├── TimelineHandle.tsx         # Draggable time-window handle UI
├── TimelineMarkers.tsx        # Low-level marker renderer (StoryNodes, datasets, events)
└── GranularityControls.tsx    # Basic temporal granularity switcher (year/decade/century)
~~~

---

# 🧩 Component Responsibilities

## 📊 **TimelineBar.tsx**
Renders:

- Base horizontal timeline axis  
- Tick marks, intervals, and divisions  
- Faded inactive zones  

Must:

- Respect reduced-motion and accessibility preferences  
- Provide screen-reader equivalents via TimelineA11yHelpers  
- Never infer date ranges—pure rendering only  

---

## 🎚️ **TimelineHandle.tsx**
Renders and manages:

- Visual handle for selecting the active time range  
- Draggable UI element (mouse/keyboard)  

Requirements:

- Full keyboard operability  
- ARIA `slider` role  
- Must not apply timeline logic—only emit UI interaction  

Governance:

- Must not allow selecting restricted date windows (higher-level components enforce this)  

---

## 🏷️ **TimelineMarkers.tsx**
Responsible for drawing temporal markers representing:

- Story Node v3 occurrences  
- Events  
- Dataset footprints  
- Focus Mode hints (if present)  

Requirements:

- Pure position rendering—no filtering or inference  
- Must provide tooltips or ARIA labels for accessibility  
- CARE-protected markers must defer to governance wrappers  

---

## 📏 **GranularityControls.tsx**
Displays simple controls for switching between:

- Year  
- Decade  
- Century  
- Coarse granularity for sovereignty requirements  

Rules:

- ARIA tablist or button group  
- Keyboard accessible  
- Granularity logic is implemented in higher-level components  

Governance:

- Must visually denote when coarse granularity is required due to CARE or sovereignty  

---

# 🔐 Governance & FAIR+CARE Compliance

All primitives must:

- Honor CARE metadata passed from TimelineView parent  
- Avoid unmasked temporal detail for sensitive datasets  
- Avoid drawing markers with unverified or incomplete provenance  
- Trigger sovereignty notices through parent components if needed  
- Never display:
  - Cultural-sensitive date ranges  
  - Temporal claims not derived from backend  
  - Uncertain or manufactured chronology  

Violations → **CI BLOCK**.

---

# ♿ Accessibility Requirements (WCAG 2.1 AA)

Timeline primitives **must**:

- Provide focus-visible elements  
- Use high-contrast color tokens  
- Respect reduced-motion  
- Provide ARIA roles (`slider`, `tablist`, `button`, etc.)  
- Delegate screen-reader equivalents to TimelineA11yHelpers  
- Avoid color-only communication  

A11y regressions → **merge blocked**.

---

# 📈 Telemetry Expectations

Primitives do not send telemetry directly  
but must ensure:

- Stable event/pass-through structure  
- No PII is produced  
- No speculative or derived metadata is emitted  
- Upstream TimelineView components can record:
  - `"timeline:drag-start"`
  - `"timeline:drag-end"`
  - `"timeline:marker-hover"`
  - `"timeline:marker-click"`
  - `"timeline:granularity-change"`

---

# 🧪 Testing Expectations

Every primitive must include:

- Unit rendering tests  
- A11y tests (ARIA, contrast, keyboard)  
- Snapshot tests (when stable)  
- Governance masking tests when applicable  
- No timeline/temporal logic tests (handled by TimelineView)  

Test locations:

~~~text
tests/unit/web/components/TimelineView/primitives/**
tests/integration/web/components/TimelineView/primitives/**
~~~

---

# 🕰 Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v10.4.0 | 2025-11-15 | Created primitives overview; aligned with TimelineView v2 architecture |
| v10.3.2 | 2025-11-14 | Migrated legacy timeline UI into primitives |
| v10.3.1 | 2025-11-13 | Initial timeline primitives under old `timeline/` folder |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
FAIR+CARE Certified · Public Document · Version-Pinned  
Validated under MCP-DL v6.3 & KFM-MDP v10.4.1  

</div>

