---
title: "💻 Kansas Frontier Matrix — Web Source Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/README.md"
version: "v10.4.2"
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
doc_uuid: "urn:kfm:doc:web-src-readme-v10.4.2"
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
Provide a comprehensive, FAIR+CARE-governed overview of `web/src/**`, the **entire frontend  
application layer** of the Kansas Frontier Matrix (KFM) Web Platform.  
All React components, contexts, services, pipelines, styles, and utilities live here.

</div>

---

# 📘 Overview

`web/src/` contains:

- **React 18 + TypeScript strict mode** application code  
- **Tailwind + design tokens** for accessible styling  
- **MapLibre (2D) + Cesium (3D)** map and globe rendering  
- **Focus Mode v2.5** entity-centric reasoning UI  
- **Story Node v3** narrative visualizations  
- **TimelineView v2** temporal navigation  
- **STAC/DCAT** dataset explorers  
- **Governance overlays** (CARE, sovereignty, provenance, licensing)  
- **Accessibility systems** (contexts, hooks, A11y tokens, patterns)  
- **Telemetry and sustainability** instrumentation  
- **Pipelines, services, and utilities** that orchestrate data flow between UI and backend

All logic in this directory must be **deterministic, testable, FAIR+CARE-compliant,  
and WCAG 2.1 AA accessible**.

---

# 🧱 Directory Structure (all entries labeled)

~~~text
web/src/
├── README.md                          # Web source overview and entry documentation
├── ARCHITECTURE.md                    # High-level web architecture specification (v10.x)
│
├── components/                        # All React UI components (presentational layer)
│   ├── MapView/                       # Canonical 2D MapLibre system for maps
│   │   ├── MapViewContainer.tsx       # Assembles map, contexts, and child layers
│   │   ├── MapCanvas.tsx              # MapLibre canvas mount + lifecycle wrapper
│   │   ├── LayerManager.tsx           # Manages layer registration, order, and visibility
│   │   ├── LegendPanel.tsx            # Accessible legend panel (CARE-aware colors)
│   │   ├── MapControls.tsx            # Zoom/rotate/reset control cluster
│   │   ├── StoryNodeLayer.tsx         # Story Node v3 footprint layer renderer
│   │   ├── FocusHighlightLayer.tsx    # Entity highlight overlay for Focus Mode
│   │   ├── DatasetFootprintLayer.tsx  # STAC/DCAT footprint overlay rendering
│   │   ├── SovereigntyMaskLayer.tsx   # H3-based masking layer for sensitive sites
│   │   └── primitives/                # Legacy map primitives reused internally
│   │       ├── MapContainer.tsx       # Legacy MapLibre base wrapper
│   │       ├── LayerToggle.tsx        # Legacy per-layer toggle component
│   │       ├── Legend.tsx             # Legacy legend UI component
│   │       └── FeatureHighlight.tsx   # Legacy highlight drawing primitive
│   │
│   ├── TimelineView/                  # Full temporal navigation view (timeline)
│   │   ├── TimelineViewContainer.tsx  # Page-level container for the timeline feature
│   │   ├── TimelinePrimary.tsx        # Main axis + active interval visualization
│   │   ├── TimelineMarkersLayer.tsx   # Renders StoryNode/dataset/event markers
│   │   ├── TimelineControls.tsx       # Zoom & granularity controls (year/decade/etc.)
│   │   ├── TimelineA11yHelpers.tsx    # Screen-reader text + keyboard help overlays
│   │   ├── TimelineCallouts.tsx       # CARE temporal warning banners
│   │   └── primitives/                # Low-level timeline primitives
│   │       ├── TimelineBar.tsx        # Raw axis graphic (ticks + labels)
│   │       ├── TimelineHandle.tsx     # Draggable handle for interval selection
│   │       ├── TimelineMarkers.tsx    # Marker list primitive for nodes/events
│   │       └── GranularityControls.tsx# Base UI for granularity switching
│   │
│   ├── FocusMode/                     # Focus Mode v2.5 entity reasoning components
│   │   ├── FocusContainer.tsx         # Main container for Focus Mode layout
│   │   ├── FocusHeader.tsx            # Entity header with CARE + provenance chips
│   │   ├── FocusSummary.tsx           # Summary block; clearly labels AI text
│   │   ├── FocusTabs.tsx              # Tab navigation (Overview/Relations/Spatial/Prov)
│   │   ├── RelationsPanel.tsx         # Grouped related-entity lists
│   │   ├── RelationCard.tsx           # Single related-entity card UI
│   │   ├── NarrativeSection.tsx       # Detailed narrative content region
│   │   ├── ExplainabilitySection.tsx  # SHAP/LIME explanation UI
│   │   ├── SpatialPanel.tsx           # Shows generalized spatial footprint + controls
│   │   ├── ProvenancePanel.tsx        # Full provenance chain visual/ textual view
│   │   ├── WarningsPanel.tsx          # CARE, sovereignty, and ethics notices
│   │   └── primitives/                # Legacy Focus Mode primitives (internal use)
│   │       ├── FocusPanel.tsx         # Older composite focus panel
│   │       ├── RelatedEntityCard.tsx  # Legacy related-entity card primitive
│   │       ├── FocusNarrative.tsx     # Legacy narrative region component
│   │       ├── ExplanationBlock.tsx   # Legacy explainability layout
│   │       └── CARENotices.tsx        # Legacy ethics/CARE notice block
│   │
│   ├── DetailDrawer/                  # Reusable slide-out drawer system
│   │   ├── DetailDrawer.tsx           # Drawer container with focus-trapping dialog
│   │   ├── DrawerHeader.tsx           # Drawer title + CARE + provenance summary
│   │   ├── DrawerSection.tsx          # Semantic section wrapper for drawer content
│   │   ├── DrawerMetadata.tsx         # Key metadata display within a drawer
│   │   ├── DrawerProvenance.tsx       # Provenance and lineage panel
│   │   ├── DrawerCAREBlock.tsx        # CARE + sovereignty explanation region
│   │   ├── DrawerFooter.tsx           # Footer with actions/links
│   │   └── DrawerA11yHelpers.tsx      # A11y helpers (ARIA, SR-only messaging)
│   │
│   ├── DataCards/                     # Dataset/asset summary card components
│   │   ├── DataCard.tsx               # Root card wrapper for dataset previews
│   │   ├── DataCardHeader.tsx         # Title + CARE + provenance for a card
│   │   ├── DataCardMetadata.tsx       # Summarized key metadata rows
│   │   ├── DataCardPreview.tsx        # Spatial/temporal mini preview
│   │   ├── DataCardFooter.tsx         # Card actions (open, explore, view in map)
│   │   ├── DataCardA11yHelpers.tsx    # ARIA labels + SR descriptions
│   │   └── DataCardSkeleton.tsx       # Loading skeleton for card layout
│   │
│   ├── story/                         # Story Node v3 narrative components
│   │   ├── StoryCard.tsx              # Compact card for Story Node preview
│   │   ├── StoryDetail.tsx            # Full narrative + metadata view
│   │   ├── StoryMedia.tsx             # Media carousel (scans, maps, images)
│   │   ├── StoryMapPreview.tsx        # Generalized mini map showing footprint
│   │   └── StoryRelations.tsx         # Related entities/Story Nodes list
│   │
│   ├── governance/                    # Governance/CARE-specific UI elements
│   │   ├── CAREBadge.tsx              # CARE classification badge
│   │   ├── LicenseTag.tsx             # SPDX license label
│   │   ├── ProvenanceChip.tsx         # Inline provenance status chip
│   │   ├── ProvenanceTrail.tsx        # Detailed provenance graph representation
│   │   ├── SovereigntyNotice.tsx      # Notice for Indigenous/sovereignty-governed data
│   │   ├── MaskingIndicator.tsx       # Indicator that data has been generalized/masked
│   │   └── GovernanceDrawer.tsx       # Governance-only drawer view
│   │
│   ├── stac/                          # STAC/DCAT dataset exploration components
│   │   ├── DatasetCard.tsx            # Basic card summarizing a dataset
│   │   ├── DatasetList.tsx            # Paginated list of dataset cards
│   │   ├── ItemPreview.tsx            # Preview panel for a single STAC Item
│   │   ├── AssetMetadata.tsx          # Asset-level metadata display
│   │   └── ExtentPreview.tsx          # Spatiotemporal extent visualization
│   │
│   ├── layout/                        # Page-level layout and navigation
│   │   ├── Header.tsx                 # Application header with nav + branding
│   │   ├── Sidebar.tsx                # Collapsible navigation sidebar
│   │   ├── Panel.tsx                  # Generic panel wrapper
│   │   ├── PageContainer.tsx          # Page shell with semantic regions
│   │   └── SplitView.tsx              # Resizable split-pane layout (map + narrative)
│   │
│   └── shared/                        # Reusable low-level UI primitives
│       ├── Button.tsx                 # Accessible button component
│       ├── IconButton.tsx             # Icon-only button with ARIA labels
│       ├── Dropdown.tsx               # Keyboard-navigable dropdown/menu
│       ├── Tabs.tsx                   # Accessible tablist/tab panels
│       ├── Modal.tsx                  # Focus-trapped modal dialog
│       ├── Tooltip.tsx                # ARIA-compliant tooltip
│       ├── Spinner.tsx                # Reduced-motion loading indicator
│       ├── Badge.tsx                  # General-purpose label/badge
│       ├── Card.tsx                   # Neutral card wrapper
│       └── FormControls/              # Shared form controls
│           ├── TextInput.tsx          # Text input with label + error messaging
│           ├── Checkbox.tsx           # Accessible checkbox control
│           ├── RadioGroup.tsx         # Mutually exclusive option group
│           ├── Select.tsx             # Select/dropdown control
│           ├── ToggleSwitch.tsx       # Binary toggle with switch semantics
│           └── FieldLabel.tsx         # Label + description wrapper
│
├── pages/                             # Top-level SPA route views (Map, Timeline, Focus, Story, etc.)
│   # Each page wires contexts + features into route-level layout.
│
├── hooks/                             # Shared React hooks (logic, not UI)
│   ├── useMap.ts                      # Map state + interaction sync with MapContext
│   ├── useTimeline.ts                 # Timeline → Map → Focus synchronization
│   ├── useFocus.ts                    # Focus Mode v2.5 orchestration logic
│   ├── useStac.ts                     # STAC/DCAT search and retrieval logic
│   └── useTelemetry.ts                # WebVitals + usage metrics emission
│
├── context/                           # Global React Context providers
│   ├── TimeContext.tsx                # Current time window and granularity
│   ├── FocusContext.tsx               # Current focused entity and payload
│   ├── ThemeContext.tsx               # Light/dark/high-contrast theme state
│   ├── A11yContext.tsx                # Reduced-motion, large-text, etc.
│   ├── GovernanceContext.tsx          # CARE, sovereignty, license, and provenance flags
│   ├── MapContext.tsx                 # Map viewport, layers, and basemap state
│   └── UIContext.tsx                  # Shell UI state (drawers, sidebars, modals)
│
├── services/                          # External communication layer (APIs, STAC, telemetry)
│   ├── apiClient.ts                   # Shared REST/GraphQL client wrapper
│   ├── stacService.ts                 # STAC 1.0 catalog & item API integration
│   ├── dcatService.ts                 # DCAT v3 dataset/distribution integration
│   ├── telemetryService.ts            # Telemetry event submission to backend
│   └── governanceService.ts           # Governance metadata lookup (CARE, license)
│
├── pipelines/                         # Client-side orchestration pipelines
│   ├── focusPipeline.ts               # Focus Mode v2.5 data + context coordination
│   ├── stacPipeline.ts                # STAC/DCAT dataset browsing flow
│   ├── storyPipeline.ts               # Story Node v3 + Focus Mode coordination
│   └── timelinePipeline.ts            # Time-context pipeline (timeline + map + story)
│
├── utils/                             # Pure utility modules (no side effects)
│   ├── formatters.ts                  # Date/number/text formatting helpers
│   ├── jsonld.ts                      # JSON-LD builders for entities and datasets
│   ├── guards.ts                      # Runtime type/schema guard helpers
│   ├── bbox.ts                        # Bounding-box math and geometry checks
│   ├── a11y.ts                        # Accessibility-related helper functions
│   ├── color.ts                       # WCAG-compliant color calculations
│   └── temporal.ts                    # Temporal utilities aligned with OWL-Time
│
├── styles/                            # Styling & theme system (design tokens)
│   ├── tokens/                        # Color, spacing, typography, radii, etc.
│   ├── themes/                        # Light/dark theme variable mappings
│   ├── mixins/                        # Shared CSS/utility classes and patterns
│   └── maps/                          # MapLibre/Cesium-specific style sheets
│
├── types/                             # Shared TypeScript type definitions
│   ├── api.ts                         # Typed DTOs for API responses
│   ├── domain.ts                      # Core domain entities (StoryNode, Dataset, Place...)
│   ├── governance.ts                  # CARE/sovereignty/provenance type shapes
│   ├── spatial.ts                     # GeoJSON, BBox, H3 masking types
│   ├── temporal.ts                    # OWL-Time compatible temporal types
│   ├── ui.ts                          # Generic UI and component prop types
│   ├── telemetry.ts                   # Telemetry event and payload types
│   ├── focus.ts                       # Focus Mode-specific types
│   ├── story.ts                       # Story Node-specific types
│   ├── stac.ts                        # STAC v1.0 typed structures
│   ├── dcat.ts                        # DCAT v3 typed structures
│   └── index.ts                       # Barrel file exporting all shared types
│
├── main.tsx                           # React application entrypoint (bootstrap)
└── App.tsx                            # Root component: routing + context providers
~~~

---

# 🔐 Governance (FAIR+CARE)

All modules in `web/src/**` must:

- Respect CARE classification and sovereignty rules  
- Apply H3 r7+ generalization for sensitive locations  
- Never display precise coordinates for protected sites  
- Mark AI-generated narrative content and respect `ai_transform_prohibited`  
- Surface provenance metadata (source, rights-holder, transformations)  
- Avoid speculative or unverified historical claims  

Violations are treated as **CI-blocking** issues.

---

# ♿ Accessibility (WCAG 2.1 AA)

Across the entire web source:

- All interactive elements must be keyboard-operable  
- Focus must always be visible  
- ARIA roles/labels must be correct and minimal  
- Reduced-motion preferences must be honored  
- Color contrast must meet or exceed AA thresholds  
- Non-text content must have text alternatives  

Accessibility regressions **block merges**.

---

# 📈 Telemetry Requirements

`web/src/**` is responsible for emitting telemetry for:

- Map interactions (pan, zoom, layer toggles)  
- Timeline interactions (range changes, granularity changes)  
- Focus Mode activations and relations exploration  
- Story Node viewing and media engagement  
- STAC/DCAT dataset browsing actions  
- Accessibility preference usage (reduced motion, high contrast)  
- Performance metrics (WebVitals)  
- Sustainability metrics (energy / CO₂ estimates where available)  

Telemetry is collected, validated, and exported into:

```text
releases/<version>/focus-telemetry.json
````

---

# 🧪 Testing Expectations

All web source layers must be covered by:

* Unit tests (components, hooks, utilities)
* Integration tests (pipelines, context interactions, map + timeline sync)
* A11y tests (keyboard, ARIA, contrast, motion)
* Governance tests (CARE, sovereignty, provenance masking)
* Telemetry tests (schema + emission)
* Type/schema guard tests (for `types/` + `guards.ts`)

Testing failures must block PR merges via CI.

---

# 🕰 Version History

| Version | Date       | Summary                                                                                        |
| ------: | ---------- | ---------------------------------------------------------------------------------------------- |
| v10.4.2 | 2025-11-15 | Expanded directory descriptions; labeled every file inline; aligned with new primitives layout |
| v10.4.1 | 2025-11-15 | First v10.4.1-aligned overview (MapView/TimelineView/FocusMode refactor)                       |
| v10.4.0 | 2025-11-15 | v10.4 architecture rewrite for web/src                                                         |
| v10.3.2 | 2025-11-14 | Added governance & accessibility enhancements                                                  |
| v10.3.1 | 2025-11-13 | Initial baseline README                                                                        |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License
FAIR+CARE Certified · Public Document · Version-Pinned
Validated under MCP-DL v6.3 & KFM-MDP v10.4.1

</div>
