---
title: "⏱️ Kansas Frontier Matrix — Timeline UI Components Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/components/timeline/README.md"
version: "v10.4.0"
last_updated: "2025-11-15"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/web-components-timeline-v1.json"
governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Component Overview"
intent: "web-components-timeline"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Temporal-Data Dependent"
sensitivity_level: "Low"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false
provenance_chain:
  - "web/src/components/timeline/README.md@v10.3.2"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E52 Time-Span"
  schema_org: "WebPageElement"
  owl_time: "TemporalEntity"
  prov_o: "prov:Entity"
json_schema_ref: "../../../../schemas/json/web-components-timeline-readme.schema.json"
shape_schema_ref: "../../../../schemas/shacl/web-components-timeline-readme-shape.ttl"
doc_uuid: "urn:kfm:doc:web-components-timeline-readme-v10.4.0"
semantic_document_id: "kfm-doc-web-components-timeline-readme"
event_source_id: "ledger:web/src/components/timeline/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "a11y-adaptations"
  - "semantic-highlighting"
ai_transform_prohibited:
  - "summaries"
  - "unverified historical claims"
  - "speculative additions"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Public Document"
role: "overview"
lifecycle_stage: "stable"
ttl_policy: "Review each release cycle"
sunset_policy: "Superseded upon next timeline system update"
---

<div align="center">

# ⏱️ **Kansas Frontier Matrix — Timeline UI Components Overview**  
`web/src/components/timeline/README.md`

**Purpose:**  
Define the UI components used to render the timeline experience in the Kansas Frontier Matrix Web Platform —  
including temporal navigation, markers, granularity controls, A11y support, governance integration, and  
telemetry instrumentation.  
Timeline components synchronize time → map → story → focus flows and must comply with FAIR+CARE rules.

</div>

---

# 📘 Overview

Timeline UI components render:

- The main temporal axis  
- Story Node v3 markers  
- Dataset markers from STAC/DCAT  
- Timeline handles for selecting intervals  
- Granularity controls (year/decade/century)  
- Accessibility overlays and keyboard navigation  
- CARE-aware temporal warnings  
- Telemetry for all timeline interactions  

They connect tightly to:

- `useTimeline.ts`  
- `timelinePipeline.ts`  
- TimeContext  
- MapContext  
- FocusContext  
- Story Node v3 metadata  

Timeline UI is a **data-critical control surface**, so all components must be deterministic, accessible,  
governance-safe, and fully tested.

---

# 🧱 Directory Structure

~~~text
web/src/components/timeline/
├── TimelineBar.tsx              # Main timeline axis visualization
├── TimelineHandle.tsx           # Draggable time selector handle
├── TimelineMarkers.tsx          # Story Nodes, datasets, events displayed along timeline
├── GranularityControls.tsx      # Year/decade/century switcher
├── TemporalTooltip.tsx          # Accessible tooltip for time-ranges
└── TimelineA11y.tsx             # Accessibility helpers for screen readers + keyboard
~~~

---

# 🧩 Component Responsibilities

## 📊 **TimelineBar.tsx**
Renders:

- Visual time axis  
- Time window boundaries  
- Temporal shading to represent active range  
- CARE-sensitive warnings for restricted periods  

Must:

- Support keyboard navigation  
- Provide text equivalents for screen readers  
- Avoid motion unless reduced-motion is off  

Telemetry:

- `"timeline:range-change"`  
- `"timeline:interaction"`

---

## 🎚️ **TimelineHandle.tsx**
Enables users to change active time ranges.

Must:

- Use ARIA `slider` role  
- Provide keyboard controls (← → for movement)  
- Snap to appropriate granularity  
- Respect fuzzy intervals for Story Nodes  

Governance:

- If a temporal range is sovereignty-controlled, show contextual warning  

Telemetry:

- `"timeline:drag-start"`  
- `"timeline:drag-end"`

---

## 🏷️ **TimelineMarkers.tsx**
Displays markers for:

- Story Nodes  
- Historical events  
- STAC datasets  
- Focus Mode event hints  

Must:

- Use WCAG AA compliant colors  
- Provide tooltip text  
- Use click/keyboard activation  

Governance:

- Mask or generalize markers tied to sensitive sites  
- Provide reason codes via CARE metadata  

Telemetry:

- `"timeline:marker-hover"`  
- `"timeline:marker-click"`

---

## 📏 **GranularityControls.tsx**
Switches between:

- Year-level  
- Decade-level  
- Century-level  
- Coarse-grain options for generalization  

Accessibility:

- Keyboard-navigation  
- ARIA tablist role  
- Screen-reader announcements  

Governance:

- Enforce coarse granularity for sensitive cultural periods  

Telemetry:

- `"timeline:granularity-change"`

---

## 💬 **TemporalTooltip.tsx**
Accessible, plain-language timeline tooltip.

Contents include:

- Start/end  
- Uncertainty ranges  
- Provenance of temporal metadata  
- CARE-sensitive notices  

Must:

- Use semantic roles  
- Be fully screen-reader accessible  
- Not rely solely on hover  

---

## ♿ **TimelineA11y.tsx**
Provides A11y helpers:

- SR-only descriptions  
- Keyboard shortcut overlays  
- Textual equivalents for temporal markers  
- Improved focus management  

Required for WCAG 2.1 AA compliance.

---

# 🔐 Governance & FAIR+CARE Integration

Timeline components must:

- Surface CARE metadata for sensitive historical periods  
- Warn users when entering sovereignty-restricted intervals  
- Apply generalization rules (temporal smoothing)  
- Label any AI-derived narrative or temporal inferences  
- Provide provenance sources for event ranges  

Governance failures → **CI BLOCK**.

---

# ♿ Accessibility Requirements (WCAG 2.1 AA)

All timeline components must:

- Use ARIA roles  
- Provide keyboard operability  
- Respect reduced-motion  
- Provide alternative labels for visuals  
- Maintain ≥ 4.5:1 contrast  
- Announce interactive changes to screen readers  

A11y violations → **PR BLOCKED**.

---

# 📈 Telemetry Responsibilities

Timeline components emit:

- `"timeline:range-change"`  
- `"timeline:marker-hover"`  
- `"timeline:marker-click"`  
- `"timeline:granularity-change"`  
- `"timeline:drag-start"`  
- `"timeline:drag-end"`  

Telemetry must be:

- Schema-valid  
- Non-PII  
- Governance-aware  
- Included in the release bundle  
  (`releases/<version>/focus-telemetry.json`)

---

# 🧪 Testing Requirements

Tests must validate:

- Proper rendering  
- Governance-based temporal restrictions  
- Interaction with TimeContext  
- Integration with MapContext + FocusContext  
- A11y behavior (screen readers, keyboard controls)  
- Telemetry accuracy  
- Correct display of fuzzy intervals  

Locations:

~~~text
tests/unit/web/components/timeline/**
tests/integration/web/components/timeline/**
~~~

---

# 🕰 Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v10.4.0 | 2025-11-15 | Full rewrite aligned with KFM-MDP v10.4; added governance, A11y, STAC/Story Node integration |
| v10.3.2 | 2025-11-14 | Improved marker rendering + temporal logic |
| v10.3.1 | 2025-11-13 | Initial timeline component overview |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
FAIR+CARE Certified · Public Document · Version-Pinned  
Validated under MCP-DL v6.3 & KFM-MDP v10.4  

</div>

