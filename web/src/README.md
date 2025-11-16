---
title: "💻 Kansas Frontier Matrix — Web Source Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/README.md"
version: "v10.4.1"
last_updated: "2025-11-15"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../releases/v10.4.1/sbom.spdx.json"
manifest_ref: "../../releases/v10.4.1/manifest.zip"
telemetry_ref: "../../releases/v10.4.1/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/web-src-readme-v1.json"
governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.1"
status: "Active / Enforced"
doc_kind: "Overview"
intent: "web-src-overview"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
sensitivity_level: "None"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false
provenance_chain:
  - "web/src/README.md@v10.0.0"
  - "web/src/README.md@v10.3.2"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E31 Document"
  schema_org: "SoftwareSourceCode"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
json_schema_ref: "../../schemas/json/web-src-readme.schema.json"
shape_schema_ref: "../../schemas/shacl/web-src-readme-shape.ttl"
doc_uuid: "urn:kfm:doc:web-src-readme-v10.4.1"
semantic_document_id: "kfm-doc-web-src-readme"
event_source_id: "ledger:web/src/README.md"
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
jurisdiction: "Kansas / United States"
classification: "Public Document"
role: "overview"
lifecycle_stage: "stable"
ttl_policy: "Review required every 12 months"
sunset_policy: "Superseded upon next web/src overhaul"
---

<div align="center">

# 💻 **Kansas Frontier Matrix — Web Source Overview**  
`web/src/README.md`

**Purpose:**  
Provide a complete, FAIR+CARE-governed, WCAG-compliant architectural overview of  
`web/src/**`, the full frontend application layer of the Kansas Frontier Matrix (KFM).  
All React components, state systems, pipelines, governance layers, services, styling,  
and utilities live here.

</div>

---

# 📘 Overview

`web/src/` contains:

- React 18 + TypeScript strict mode  
- Tailwind design system + WCAG tokens  
- MapLibre (2D) & Cesium (3D)  
- Story Node v3 system  
- Focus Mode v2.5  
- TimelineView v2  
- STAC/DCAT dataset explorers  
- Governance/CARE overlays  
- Telemetry capture (WebVitals, A11y, Focus Mode usage, energy/carbon)  
- Context/state management, pipelines, services, and utilities  

It is the **core application logic** for the entire KFM frontend.

---

# 🧱 Directory Structure (inline-labeled, compact)

~~~text
web/src/
├── README.md                          # This document
├── ARCHITECTURE.md                    # Full system architecture specification
│
├── components/                        # All React UI components (presentational only)
│   ├── MapView/                       # Canonical 2D map system (MapLibre)
│   │   ├── MapViewContainer.tsx       # Map orchestration + contexts
│   │   ├── MapCanvas.tsx              # MapLibre mount + render surface
│   │   ├── LayerManager.tsx           # Loads/unloads layers deterministically
│   │   ├── LegendPanel.tsx            # CARE-aware legend panel
│   │   ├── MapControls.tsx            # Zoom/rotate/reset controls
│   │   ├── StoryNodeLayer.tsx         # Story Node v3 footprint rendering
│   │   ├── FocusHighlightLayer.tsx    # Focus Mode spatial highlight
│   │   ├── DatasetFootprintLayer.tsx  # STAC/DCAT footprint overlays
│   │   ├── SovereigntyMaskLayer.tsx   # H3 r7+ masking for sensitive sites
│   │   └── primitives/                # Map primitives (legacy-compatible)
│   │       ├── MapContainer.tsx       # Legacy map wrapper
│   │       ├── LayerToggle.tsx        # Legacy layer toggle
│   │       ├── Legend.tsx             # Legacy legend component
│   │       └── FeatureHighlight.tsx   # Legacy highlight implementation
│   │
│   ├── TimelineView/                  # Full timeline navigation system
│   │   ├── TimelineViewContainer.tsx  # Top-level timeline shell
│   │   ├── TimelinePrimary.tsx        # Core timeline axis renderer
│   │   ├── TimelineMarkersLayer.tsx   # StoryNode/STAC markers
│   │   ├── TimelineControls.tsx       # Granularity + zoom
│   │   ├── TimelineA11yHelpers.tsx    # Screen-reader labeling
│   │   ├── TimelineCallouts.tsx       # CARE temporal warnings
│   │   └── primitives/                # Timeline primitives (legacy-compatible)
│   │       ├── TimelineBar.tsx        # Base axis visuals
│   │       ├── TimelineHandle.tsx     # Adjustable handle
│   │       ├── TimelineMarkers.tsx    # Marker renderer
│   │       └── GranularityControls.tsx# Base granularity component
│   │
│   ├── FocusMode/                     # Focus Mode v2.5 advanced reasoning UI
│   │   ├── FocusContainer.tsx         # Primary focus viewport
│   │   ├── FocusHeader.tsx            # Entity header + CARE/provenance
│   │   ├── FocusSummary.tsx           # Summary (AI-labeled if applicable)
│   │   ├── FocusTabs.tsx              # Overview/Relations/Spatial/Prov tabs
│   │   ├── RelationsPanel.tsx         # Related entity groups
│   │   ├── RelationCard.tsx           # Individual relation card
│   │   ├── NarrativeSection.tsx       # Narrative + governance text
│   │   ├── ExplainabilitySection.tsx  # SHAP/LIME explainability
│   │   ├── SpatialPanel.tsx           # Map footprint preview
│   │   ├── ProvenancePanel.tsx        # Full provenance chain
│   │   ├── WarningsPanel.tsx          # CARE/sovereignty warnings
│   │   └── primitives/                # Focus primitives (legacy-compatible)
│   │       ├── FocusPanel.tsx
│   │       ├── RelatedEntityCard.tsx
│   │       ├── FocusNarrative.tsx
│   │       ├── ExplanationBlock.tsx
│   │       └── CARENotices.tsx
│   │
│   ├── DetailDrawer/                  # Universal slide-out detail drawer
│   │   ├── DetailDrawer.tsx
│   │   ├── DrawerHeader.tsx
│   │   ├── DrawerSection.tsx
│   │   ├── DrawerMetadata.tsx
│   │   ├── DrawerProvenance.tsx
│   │   ├── DrawerCAREBlock.tsx
│   │   ├── DrawerFooter.tsx
│   │   └── DrawerA11yHelpers.tsx
│   │
│   ├── DataCards/                     # Dataset/asset metadata cards
│   │   ├── DataCard.tsx
│   │   ├── DataCardHeader.tsx
│   │   ├── DataCardMetadata.tsx
│   │   ├── DataCardPreview.tsx
│   │   ├── DataCardFooter.tsx
│   │   ├── DataCardA11yHelpers.tsx
│   │   └── DataCardSkeleton.tsx
│   │
│   ├── story/                         # Story Node v3 narrative components
│   │   ├── StoryCard.tsx
│   │   ├── StoryDetail.tsx
│   │   ├── StoryMedia.tsx
│   │   ├── StoryMapPreview.tsx
│   │   └── StoryRelations.tsx
│   │
│   ├── governance/                    # Governance & CARE UI
│   │   ├── CAREBadge.tsx
│   │   ├── LicenseTag.tsx
│   │   ├── ProvenanceChip.tsx
│   │   ├── ProvenanceTrail.tsx
│   │   ├── SovereigntyNotice.tsx
│   │   ├── MaskingIndicator.tsx
│   │   └── GovernanceDrawer.tsx
│   │
│   ├── stac/                          # STAC/DCAT UI suite
│   │   ├── DatasetCard.tsx
│   │   ├── DatasetList.tsx
│   │   ├── ItemPreview.tsx
│   │   ├── AssetMetadata.tsx
│   │   └── ExtentPreview.tsx
│   │
│   ├── layout/                        # Page shells & navigation
│   │   ├── Header.tsx
│   │   ├── Sidebar.tsx
│   │   ├── Panel.tsx
│   │   ├── PageContainer.tsx
│   │   └── SplitView.tsx
│   │
│   └── shared/                        # Low-level UI primitives
│       ├── Button.tsx
│       ├── IconButton.tsx
│       ├── Dropdown.tsx
│       ├── Tabs.tsx
│       ├── Modal.tsx
│       ├── Tooltip.tsx
│       ├── Spinner.tsx
│       ├── Badge.tsx
│       ├── Card.tsx
│       └── FormControls/
│           ├── TextInput.tsx
│           ├── Checkbox.tsx
│           ├── RadioGroup.tsx
│           ├── Select.tsx
│           ├── ToggleSwitch.tsx
│           └── FieldLabel.tsx
│
├── pages/                             # SPA route views (Map, Timeline, Focus, Story)
│
├── hooks/                             # Reusable logic (cross-feature)
│   ├── useMap.ts
│   ├── useTimeline.ts
│   ├── useFocus.ts
│   ├── useStac.ts
│   └── useTelemetry.ts
│
├── context/                           # Global React state containers
│   ├── TimeContext.tsx
│   ├── FocusContext.tsx
│   ├── ThemeContext.tsx
│   ├── A11yContext.tsx
│   ├── GovernanceContext.tsx
│   ├── MapContext.tsx
│   └── UIContext.tsx
│
├── services/                          # Backend & metadata communication
│   ├── apiClient.ts
│   ├── stacService.ts
│   ├── dcatService.ts
│   ├── telemetryService.ts
│   └── governanceService.ts
│
├── pipelines/                         # Client-side orchestration systems
│   ├── focusPipeline.ts
│   ├── stacPipeline.ts
│   ├── storyPipeline.ts
│   └── timelinePipeline.ts
│
├── utils/                             # Pure helper modules
│   ├── formatters.ts
│   ├── jsonld.ts
│   ├── guards.ts
│   ├── bbox.ts
│   ├── a11y.ts
│   ├── color.ts
│   └── temporal.ts
│
├── styles/                            # Design tokens + global styling
│   ├── tokens/
│   ├── themes/
│   ├── mixins/
│   └── maps/
│
├── types/                             # Shared TS types (DTOs + domain models)
│   ├── api.ts
│   ├── domain.ts
│   ├── governance.ts
│   ├── spatial.ts
│   ├── temporal.ts
│   ├── ui.ts
│   ├── telemetry.ts
│   ├── focus.ts
│   ├── story.ts
│   ├── stac.ts
│   ├── dcat.ts
│   └── index.ts
│
├── main.tsx                           # React entrypoint
└── App.tsx                            # Root shell, routing, context providers
~~~

---

# 🔐 Governance (FAIR+CARE)

All modules must:

- Display CARE labels  
- Respect sovereignty boundaries  
- Apply H3 r7+ generalization for sensitive coordinates  
- Annotate AI-generated content  
- Surface provenance metadata  
- Avoid speculative or unverified historical claims  

Governance violations = **CI BLOCKER**.

---

# ♿ Accessibility (WCAG 2.1 AA)

Requirements across all code:

- Keyboard operability  
- ARIA roles & labels  
- High-contrast tokens  
- Reduced-motion support  
- Semantic HTML structure  
- Screen-reader-safe content  

Accessibility regressions = **merge blocked**.

---

# 📈 Telemetry Requirements

Telemetry captured here includes:

- Map interactions  
- Timeline scrubs  
- Focus Mode activity  
- Story Node interactions  
- A11y usage  
- Energy & carbon metrics  
- Performance (WebVitals)  

Exported to:

```

releases/<version>/focus-telemetry.json

```

---

# 🧪 Testing Requirements

Every feature must implement:

- Unit tests  
- Integration tests  
- A11y tests  
- Governance tests  
- Telemetry tests  
- Schema/type guard tests  
- Timeline ↔ Map ↔ Focus sync tests  

Testing failures block merges under CI/CD.

---

# 🕰 Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v10.4.1 | 2025-11-15 | Fully aligned + polished to reflect new MapView, TimelineView, FocusMode, primitives structure |
| v10.4.0 | 2025-11-15 | Rewritten to match v10.4 architecture |
| v10.3.2 | 2025-11-14 | Added governance & accessibility enhancements |
| v10.3.1 | 2025-11-13 | Initial baseline README |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
FAIR+CARE Certified · Public Document · Version-Pinned  
Validated under MCP-DL v6.3 & KFM-MDP v10.4.1  

</div>
