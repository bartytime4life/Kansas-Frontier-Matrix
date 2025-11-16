---
title: "⏱️ Kansas Frontier Matrix — Timeline Feature Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/features/timeline/README.md"
version: "v10.4.0"
last_updated: "2025-11-15"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/web-feature-timeline-v1.json"
governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Feature Overview"
intent: "timeline-feature"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
sensitivity_level: "None"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false
provenance_chain:
  - "web/src/features/timeline/README.md@v10.3.2"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E52 Time-Span"
  schema_org: "WebApplication"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
json_schema_ref: "../../../../schemas/json/web-feature-timeline.schema.json"
shape_schema_ref: "../../../../schemas/shacl/web-feature-timeline-shape.ttl"
doc_uuid: "urn:kfm:doc:web-feature-timeline-v10.4.0"
semantic_document_id: "kfm-doc-web-feature-timeline"
event_source_id: "ledger:web/src/features/timeline/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "a11y-adaptations"
  - "semantic-highlighting"
ai_transform_prohibited:
  - "speculative additions"
  - "unverified historical claims"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Public Document"
role: "feature-overview"
lifecycle_stage: "stable"
ttl_policy: "Review each release cycle"
sunset_policy: "Superseded upon next timeline feature revision"
---

<div align="center">

# ⏱️ **Kansas Frontier Matrix — Timeline Feature Overview**  
`web/src/features/timeline/README.md`

**Purpose:**  
Document the architecture, responsibilities, accessibility rules, governance interactions,  
data flows, and telemetry expectations for the **Timeline Feature** of the  
KFM Web Platform — responsible for temporal navigation, time-window filtering,  
map synchronization, Story Node alignment, and Focus Mode v2.5 integrations.

</div>

---

# 📘 Overview

The **Timeline Feature** is one of the core interaction surfaces of the  
Kansas Frontier Matrix Web Platform. It powers:

- Time-range selection  
- Temporal navigation  
- Synchronization of narrative + spatial layers  
- Filtering of Story Nodes, STAC assets, and vector layers  
- OWL-Time–aligned interpretation of dataset intervals  
- Temporal slices for 2D maps and 3D Cesium views  
- Integration with Focus Mode timelines  
- Telemetry for time-based exploration  
- Accessibility-compliant controls and keyboard interactions  

The timeline is tightly connected to:

- `TimeContext`  
- `useTimeline.ts`  
- `timelinePipeline.ts`  
- Story Node v3 metadata  
- STAC/DCAT temporal extents  
- Governance metadata (for sensitive temporal ranges)

---

# 🧱 Directory Structure

~~~text
web/src/features/timeline/
├── components/                    # Timeline UI components
│   ├── TimelineBar.tsx            # Main temporal axis
│   ├── TimelineHandle.tsx         # Drag/select handle
│   ├── TimelineMarkers.tsx        # Story Node + dataset markers
│   ├── GranularityControls.tsx    # Year/decade/century zoom levels
│   └── TimelineA11y.tsx           # Accessibility-specific timeline helpers
│
├── hooks/                         # Feature-specific logic
│   ├── useTimelineFeature.ts      # Timeline state + pipeline integration
│   └── useTemporalZoom.ts         # Controls temporal granularity
│
├── pipelines/                     # Timeline orchestration logic
│   └── timelinePipeline.ts        # Timeline → Map → Focus Mode sync
│
└── telemetry/                     # Timeline telemetry signals
    ├── timelineEvents.ts          # Event taxonomy ("timeline:range-change", etc.)
    └── timelinePerformance.ts     # FPS/interaction stats (non-PII)
~~~

---

# 🧩 Responsibilities

The Timeline Feature coordinates several interacting systems:

## 1. **Temporal Navigation**
- Users select a time window.  
- Supports:
  - Year-level  
  - Decade-level  
  - Century-level  
  - Custom intervals  
- Provides smooth scrubbing interactions.  

## 2. **Map Synchronization**
All spatial layers update automatically:

- STAC footprints  
- Story Node footprints  
- Environmental layers  
- Archaeological layers  
- Focus Mode entity highlights  

MapLibre & Cesium views receive deterministic updates from `TimeContext`.

## 3. **Story Node v3 Alignment**
Timeline determines:

- Active Story Nodes  
- Narrative boundaries  
- Temporal overlays  
- Visual Highlights (range bands, markers)

## 4. **Focus Mode v2.5 Integration**
Timeline modifies:

- Which events/entities are highlighted  
- Which narratives appear in Focus Mode  
- Which Story Nodes are suggested  
- How temporal clusters are grouped  

## 5. **Governance & CARE Controls**
Timeline must:

- Respect CARE-sensitive temporal ranges  
- Show warnings when data is restricted  
- Provide provenance metadata for datasets bound to time  

---

# ♿ Accessibility Requirements (WCAG 2.1 AA)

Timeline UI MUST:

- Support full keyboard navigation  
- Provide visible focus states  
- Offer high-contrast, accessible color ramps  
- Respect `prefers-reduced-motion`  
- Offer textual descriptions for Story Node markers  
- Expose ARIA labels for handles + temporal controls  

Accessibility regressions block CI merges.

---

# 🔐 Governance Integration

Timeline components must surface:

- CARE labels for sensitive narratives  
- Provenance for historical ranges  
- Warnings for culturally sensitive periods  
- Masks or reduced granularity when required  

If temporal data is restricted:

- H3 masking rules may apply to spatial overlays  
- Timeline defaults to “generalized” bands  
- UI reveals the reason (CARE notice)

---

# 📈 Telemetry Responsibilities

Timeline generates telemetry for:

- `"timeline:range-change"`  
- `"timeline:granularity-change"`  
- `"timeline:focus-sync"`  
- `"timeline:storynode-highlight"`  
- `"timeline:drag-start"` / `"drag-end"`  

Telemetry must:

- Be non-PII  
- Follow schemas in telemetry config  
- Record sustainability metrics when expensive operations occur  
- Include governance metadata when masking occurs

Telemetry flows to:

`releases/<version>/focus-telemetry.json`

---

# 🧪 Testing Requirements

Timeline Feature MUST include:

- Unit tests (`TimelineBar`, `Markers`, accessibility helpers)  
- Integration tests (timeline → map → focus sync)  
- Schema tests for temporal metadata  
- Governance tests for sensitive period handling  
- A11y tests (keyboard, reduced-motion, labels)  
- Telemetry correctness tests  
- State propagation tests (TimeContext interactions)

Test directories:

~~~text
tests/unit/web/features/timeline/**
tests/integration/web/features/timeline/**
tests/e2e/web/features/timeline/**
~~~

---

# 🧠 Pipeline Flow (Conceptual)

~~~text
User Adjusts Timeline Handle
        │
        ▼
useTimelineFeature.ts
        │
        ▼
timelinePipeline.ts
        │
        ├──► MapLibre layers filtered
        ├──► Cesium time slices updated
        ├──► Story Node v3 list filtered
        └──► Focus Mode narrative recalculated
        │
        ▼
Telemetry + governance + provenance recording
~~~

---

# 🕰 Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v10.4.0 | 2025-11-15 | Full rewrite for KFM-MDP v10.4; added governance, A11y, STAC, Story Node, Focus Mode sync |
| v10.3.2 | 2025-11-14 | Improved granularity logic + temporal sync |
| v10.3.1 | 2025-11-13 | Initial timeline feature overview |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
FAIR+CARE Certified · Public Document · Version-Pinned  
Validated under MCP-DL v6.3 and KFM-MDP v10.4  

</div>