---
title: "⏱️ Kansas Frontier Matrix — TimelineView Primitives Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/components/TimelineView/primitives/README.md"
version: "v11.2.2"
last_updated: "2025-11-30"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.2.2/web-timelineview-primitives-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/web-components-timelineview-primitives-v2.json"
energy_schema: "../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

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
intent: "frontend-timeline-primitives"
semantic_intent:
  - "UI-primitive"
  - "timeline-rendering"
  - "temporal-visualization"

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
  - "web/src/components/TimelineView/primitives/README.md@v10.4.0"

ontology_alignment:
  cidoc: "E52 Time-Span"
  schema_org: "WebPageElement"
  owl_time: "TemporalEntity"
  prov_o: "prov:Entity"

json_schema_ref: "../../../../../../schemas/json/web-components-timelineview-primitives-v11.schema.json"
shape_schema_ref: "../../../../../../schemas/shacl/web-components-timelineview-primitives-v11-shape.ttl"
doc_uuid: "urn:kfm:doc:web-components-timelineview-primitives-v11.2.2"
semantic_document_id: "kfm-doc-web-components-timelineview-primitives-v11"
event_source_id: "ledger:web/src/components/TimelineView/primitives/README.md"
immutability_status: "version-pinned"

ai_training_inclusion: false
ai_focusmode_usage: "Forbidden (logic-free primitives)"
ai_transform_permissions:
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "summaries"
  - "temporal-inference"
  - "speculative-chronology"
  - "unverified-historical-claims"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Structure"
    - "🧩 Component Responsibilities"
    - "🔐 Governance & FAIR+CARE Integration"
    - "♿ Accessibility Requirements (WCAG 2.1 AA+)"
    - "📈 Telemetry Expectations"
    - "🧪 Testing Expectations"
    - "🕰 Version History"
    - "⚖️ Footer"
---

<div align="center">

# ⏱️ **Kansas Frontier Matrix — TimelineView Primitives Overview**  
`web/src/components/TimelineView/primitives/README.md`

**Purpose:**  
Document the **Timeline UI primitives** that form the foundational elements of the  
KFM TimelineView system.  
These primitives were originally part of the old `timeline/` folder and now live  
under `TimelineView/primitives/` to support the fully orchestrated TimelineView v3 architecture.

They remain FAIR+CARE-governed, WCAG-compliant, deterministic, and non-speculative.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)]()  
[![KFM-MDP v11.2.2](https://img.shields.io/badge/KFM%E2%80%93MDP-v11.2.2-purple)]()  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Low%20Risk-gold)]()  
[![WCAG AA+](https://img.shields.io/badge/A11y-WCAG%202.1%20AA%2B-brightgreen)]()

</div>

---

## 📘 Overview

TimelineView **primitives** are:

- Low-level, **logic-free** UI building blocks  
- Used strictly **inside** `TimelineView/`  
- Wrapped by higher-order components such as:
  - `TimelinePrimary`
  - `TimelineControls`
  - `TimelineMarkersLayer`
  - `TimelineA11yHelpers`  
- Never imported outside the TimelineView domain  
- Designed to produce **stable, predictable visual behavior**  
- Fully FAIR+CARE-governed and WCAG 2.1 AA+ compliant  

They **must not**:

- Implement or modify TimeContext logic  
- Perform timeline filtering or range computations  
- Infer temporal relationships or “fill in” missing dates  
- Display speculative or uncertain temporal narrative  
- Handle sensitive temporal metadata outside of higher-level governance rules  

These primitives serve **only** as deterministic, safe presentation utilities.

---

## 🗂️ Directory Structure

~~~text
web/src/components/TimelineView/primitives/
│
├── 📊 TimelineBar.tsx            # Core time-axis visual renderer
├── 🎚️ TimelineHandle.tsx         # Draggable/keyboard time-window handle UI
├── 🏷️ TimelineMarkers.tsx        # Marker renderer for StoryNodes/datasets/events
└── 📏 GranularityControls.tsx    # Basic temporal granularity switcher (year/decade/century)
~~~

Any new primitive MUST be added here and documented in the responsibilities section.

---

## 🧩 Component Responsibilities

### 📊 TimelineBar.tsx

**Role:**  
Render the base horizontal time axis.

**Responsibilities:**

- Draw axis line, tick marks, labels for intervals  
- Present faded inactive regions vs. active range area  
- Take display configuration (labels, ticks, range) strictly via props  

**Constraints:**

- **No temporal logic**: cannot compute ranges, only render them  
- Must respect reduced-motion preferences for animated visual tweaks  
- Must cooperate with `TimelineA11yHelpers` to expose SR equivalents (e.g., “Timeline from 1700 to 2025, current range 1850–1900”)  

---

### 🎚️ TimelineHandle.tsx

**Role:**  
Interactive visual handle for selecting the active time range (drag/keyboard).

**Responsibilities:**

- Render one or more handles representing temporal boundaries  
- Support mouse drag and keyboard adjustment (e.g., arrow keys to move handle)  
- Emit events (via props) describing pointer/keyboard movement, leaving logic to higher layers  

**Accessibility:**

- Use `role="slider"` and appropriate ARIA attributes:
  - `aria-valuemin`, `aria-valuemax`, `aria-valuenow`, `aria-valuetext`  
- Ensure focus-visible states and keyboard operability  

**Governance:**

- Must not implement any rule about forbidden periods; higher-level TimelineView and GovernanceContext enforce blocked ranges  
- If parent flags a handle as disabled (e.g., restricted window), it must visually and SR-wise indicate that  

---

### 🏷️ TimelineMarkers.tsx

**Role:**  
Draw individual time markers at positions along the timeline.

**Responsibilities:**

- Render markers for:
  - Story Node v3 occurrences  
  - Events (e.g., battles, treaties)  
  - Dataset temporal entries (e.g., dataset coverage start/end)  
  - Focus hints when present  
- Place markers strictly from props (positions, colors, shapes)  

**Constraints:**

- No filtering, clustering, inference; markers appear exactly where given  
- Provide ARIA labels or hook into `TimelineA11yHelpers` to describe markers (e.g., “Event: Treaty of 1867, October 1867”)  

**Governance:**

- CARE-protected markers must be flagged via props and styled appropriately (e.g., generalized or anonymized position), but the primitive itself does not decide what is sensitive  

---

### 📏 GranularityControls.tsx

**Role:**  
Simple control set for selecting temporal granularity.

**Granularities (typical):**

- Year  
- Decade  
- Century  
- Coarse modes used for sovereignty/CARE constraints  

**Responsibilities:**

- Render a button group or tablist to switch between granularities  
- Emit events indicating user’s desired granularity; actual time bucket logic lives in TimelineViewContainer/TimelinePrimary  

**Accessibility:**

- Use ARIA `tablist`/`tab` or button group semantics  
- Fully keyboard operable (arrow keys / tab)  
- Provide SR-only text explaining each granularity (e.g., “decade view”)  

**Governance:**

- When parents require coarse granularity (due to CARE), the control must visually reflect that (e.g., “coarse mode enforced”) based on props  

---

## 🔐 Governance & FAIR+CARE Integration

Even as UI primitives, these components are part of a **governed temporal surface**.

They MUST:

- Honor governance and CARE props passed down from TimelineView (e.g., flags for restricted markers or coarse-only mode)  
- Avoid:
  - Rendering extra markers beyond what is provided  
  - Guessing dates or interpolating missing values  
  - Providing narrative text or interpretive labels beyond props and A11y helper outputs  

All temporal decisions (e.g., which range is allowed, which markers can show) are made in higher layers; primitives are **pure renderers**.

If a primitive starts embedding logic that violates CARE or inference rules, that is a **CI-blocking governance failure**.

---

## ♿ Accessibility Requirements (WCAG 2.1 AA+)

Timeline primitives MUST:

- Provide focus-visible interactive elements (handles, controls)  
- Use appropriate ARIA roles:
  - `slider` for handles  
  - `button`/`tab` for granularity controls  
- Use high-contrast color tokens for axis, markers, handles  
- Respect `prefers-reduced-motion` and allow static alternatives for timeline animations  
- Rely on `TimelineA11yHelpers` for SR descriptions and instructions  

Accessibility regressions MUST block merges.

---

## 📈 Telemetry Expectations

Primitives themselves:

- DO NOT emit telemetry directly, but **must** provide stable prop/event APIs so higher-level TimelineView components can emit telemetry like:
  - `"timeline:drag-start"`  
  - `"timeline:drag-end"`  
  - `"timeline:marker-hover"`  
  - `"timeline:marker-click"`  
  - `"timeline:granularity-change"`  

Constraints:

- No PII (no user IDs, only action categories)  
- No direct injection of temporal metadata into telemetry beyond what is requested by parent components  

---

## 🧪 Testing Expectations

Each primitive MUST be covered by:

- **Unit tests:**
  - Rendering with typical & edge props  
  - Visual states (selected/unselected, focused, disabled)  

- **A11y tests:**
  - ARIA roles, labels, and properties correct  
  - Keyboard operations across all interactive elements  
  - Focus outlines and high contrast  

- **Governance masking tests (where relevant):**
  - When parent sets flags for “restricted/blocked” markers, ensure the primitive renders appropriate visual states but does not override logic  

- **Snapshot tests (optional):**
  - For stable visual structure  

Test structure:

~~~text
tests/unit/web/components/TimelineView/primitives/**
tests/integration/web/components/TimelineView/primitives/**   # only for combined use with TimelineView
~~~

---

## 🕰 Version History

| Version | Date       | Summary                                                                 |
|--------:|------------|-------------------------------------------------------------------------|
| v11.2.2 | 2025-11-30 | Upgraded to v11.2.2; clarified primitive-only role, governance & A11y  |
| v10.4.0 | 2025-11-15 | Created primitives overview; aligned with TimelineView v2 architecture |
| v10.3.2 | 2025-11-14 | Migrated legacy timeline UI into primitives                            |
| v10.3.1 | 2025-11-13 | Initial timeline primitives under old `timeline/` folder               |

---

## ⚖️ Footer

<div align="center">

**📚 Governance Links**  
[Docs Root](../../../../../../README.md) •  
[Standards Index](../../../../../../docs/standards/INDEX.md) •  
[Governance Charter](../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

**🔐 Compliance:**  
FAIR+CARE · OWL-Time · CIDOC-CRM · PROV-O · WCAG 2.1 AA+ · SLSA Level 3

**End of Document**

</div>