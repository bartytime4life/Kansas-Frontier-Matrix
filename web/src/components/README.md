---
title: "🧩 Kansas Frontier Matrix — Web Components Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/components/README.md"
version: "v10.4.1"
last_updated: "2025-11-15"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/web-components-readme-v1.json"
governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.1"
status: "Active / Enforced"
doc_kind: "Overview"
intent: "web-components-overview"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk (unless displaying CARE-masked data)"
sensitivity_level: "None"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false
provenance_chain:
  - "web/src/components/README.md@v10.3.2"
  - "web/src/components/README.md@v10.3.1"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E28 Conceptual Object"
  schema_org: "WebPageElement"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
json_schema_ref: "../../../schemas/json/web-components-readme.schema.json"
shape_schema_ref: "../../../schemas/shacl/web-components-readme-shape.ttl"
doc_uuid: "urn:kfm:doc:web-components-readme-v10.4.1"
semantic_document_id: "kfm-doc-web-components-readme"
event_source_id: "ledger:web/src/components/README.md"
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
sunset_policy: "Superseded upon next component-layer revision"
---

<div align="center">

# 🧩 **Kansas Frontier Matrix — Web Components Overview**  
`web/src/components/README.md`

**Purpose:**  
Provide the authoritative, FAIR+CARE-aligned directory and structural overview for all UI components  
within the Kansas Frontier Matrix Web Platform.  
This document defines the **canonical component hierarchy**, **responsibilities**,  
**accessibility requirements**, **governance rules**, and **telemetry expectations** for  
every component within `web/src/components/**`.

</div>

---

# 📘 Overview

All UI components inside this directory:

- Are **presentation-only**, containing no business logic  
- Are deterministic, testable, and governed  
- Integrate with:
  - **MapLibre + Cesium**
  - **Story Node v3**
  - **Focus Mode v2.5**
  - **STAC/DCAT metadata**
  - **Governance & CARE layers**
  - **A11y tokens + design system**
  - **Telemetry hooks**
- Must meet **WCAG 2.1 AA** accessibility  
- Must follow **KFM-MDP v10.4.1** documentation, formatting & metadata standards  
- Must pass governance validation for:
  - CARE labeling  
  - Provenance chain visibility  
  - Sovereignty masking  
  - AI narrative restrictions

Components serve as **atomic UI building blocks** used by features, pipelines, pages, and maps.

---

# 🧱 Directory Structure (with labeled component purposes)

~~~text
web/src/components/

├── MapView/                                   # Full MapLibre 2D map system
│   ├── MapViewContainer.tsx                   # Assembles map + contexts + lifecycle
│   ├── MapCanvas.tsx                          # MapLibre canvas mount + rendering surface
│   ├── LayerManager.tsx                       # Dynamically loads/unloads map layers
│   ├── LegendPanel.tsx                        # CARE-aware legend UI
│   ├── MapControls.tsx                        # Zoom/rotate/reset controls (A11y-compliant)
│   ├── StoryNodeLayer.tsx                     # Story Node v3 spatial overlays
│   ├── FocusHighlightLayer.tsx                # Focus Mode highlight geometry
│   ├── DatasetFootprintLayer.tsx              # STAC footprint visualizations
│   ├── SovereigntyMaskLayer.tsx               # H3-based sensitivity masking grids
│   ├── CursorHUD.tsx                          # Coarse readout for coords + state
│   │
│   └── primitives/                            # Legacy map primitives (still supported)
│       ├── MapContainer.tsx                   # Legacy base map wrapper
│       ├── LayerToggle.tsx                    # Per-layer toggle primitive
│       ├── Legend.tsx                         # Legacy legend rendering
│       └── FeatureHighlight.tsx               # Legacy highlight visualization
│
├── TimelineView/                              # Full-page timeline feature
│   ├── TimelineViewContainer.tsx              # Top-level timeline page wrapper
│   ├── TimelinePrimary.tsx                    # Main visual timeline axis + active range
│   ├── TimelineMarkersLayer.tsx               # Events + STAC + Story Node markers
│   ├── TimelineControls.tsx                   # Granularity, zoom, generalization controls
│   ├── TimelineA11yHelpers.tsx                # SR descriptions + keyboard overlays
│   ├── TimelineCallouts.tsx                   # CARE warnings for temporal restrictions
│   │
│   └── primitives/                            # Legacy timeline primitives
│       ├── TimelineBar.tsx                    # Core axis renderer
│       ├── TimelineHandle.tsx                 # Draggable timeline select handle
│       ├── TimelineMarkers.tsx                # Low-level marker renderer
│       └── GranularityControls.tsx            # Base granularity switcher
│
├── FocusMode/                                 # Focus Mode v2.5 UI suite
│   ├── FocusContainer.tsx                     # Full Focus Mode workspace container
│   ├── FocusHeader.tsx                        # CARE, provenance, entity header
│   ├── FocusSummary.tsx                       # Narrative summary (AI-labeled when present)
│   ├── FocusTabs.tsx                          # Navigation tabs between focus modules
│   ├── RelationsPanel.tsx                     # Related entities grouped by type
│   ├── RelationCard.tsx                       # Individual related-entity card
│   ├── NarrativeSection.tsx                   # Detailed narrative + governance checks
│   ├── ExplainabilitySection.tsx              # SHAP/LIME explainability visual block
│   ├── SpatialPanel.tsx                       # Map footprint preview + highlight toggle
│   ├── ProvenancePanel.tsx                    # Full provenance chain viewer
│   ├── WarningsPanel.tsx                      # CARE + sovereignty + ethics notices
│   │
│   └── primitives/                            # Legacy focus primitives
│       ├── FocusPanel.tsx                     # Old unified focus panel block
│       ├── RelatedEntityCard.tsx              # Pre-refactor relation card
│       ├── FocusNarrative.tsx                 # Legacy narrative renderer
│       ├── ExplanationBlock.tsx               # Legacy explainability block
│       └── CARENotices.tsx                    # Legacy care/ethics banner
│
├── DetailDrawer/                              # General-purpose slide-out drawer system
│   ├── DetailDrawer.tsx                       # Drawer container (focus-trapping dialog)
│   ├── DrawerHeader.tsx                       # Title + CARE + provenance
│   ├── DrawerSection.tsx                      # A11y-friendly section wrapper
│   ├── DrawerMetadata.tsx                     # Metadata list block
│   ├── DrawerProvenance.tsx                   # Provenance graph + lineage
│   ├── DrawerCAREBlock.tsx                    # Cultural + sovereign data warnings
│   ├── DrawerFooter.tsx                       # Actions / navigation
│   └── DrawerA11yHelpers.tsx                  # SR text + ARIA attributes
│
├── DataCards/                                 # Dataset/asset summary card framework
│   ├── DataCard.tsx                           # Full card wrapper
│   ├── DataCardHeader.tsx                     # Title + CARE + provenance chip
│   ├── DataCardMetadata.tsx                   # Key-value metadata list
│   ├── DataCardPreview.tsx                    # Spatial or temporal miniature preview
│   ├── DataCardFooter.tsx                     # Actions (open / preview / map)
│   ├── DataCardA11yHelpers.tsx                # ARIA labels + SR descriptions
│   └── DataCardSkeleton.tsx                   # Low-motion loading placeholder
│
├── story/                                     # Story Node v3 UI components
│   ├── StoryCard.tsx                          # Compact narrative preview
│   ├── StoryDetail.tsx                        # Full narrative + provenance
│   ├── StoryMedia.tsx                         # Media carousel (maps, documents)
│   ├── StoryMapPreview.tsx                    # Generalized spatial preview
│   └── StoryRelations.tsx                     # Related entities list
│
├── governance/                                # Governance & CARE presentation
│   ├── CAREBadge.tsx                          # CARE classification badge
│   ├── LicenseTag.tsx                         # SPDX license label
│   ├── ProvenanceChip.tsx                     # Inline provenance tag
│   ├── ProvenanceTrail.tsx                    # Full provenance chain visualization
│   ├── SovereigntyNotice.tsx                  # Sovereignty governance banner
│   ├── MaskingIndicator.tsx                   # Masking/generalization applied indicator
│   └── GovernanceDrawer.tsx                   # Complete governance detail drawer
│
├── stac/                                      # STAC/DCAT dataset exploration suite
│   ├── DatasetCard.tsx                        # Top-level dataset summary
│   ├── DatasetList.tsx                        # Paginated dataset list
│   ├── ItemPreview.tsx                        # STAC Item preview (spatial/temporal)
│   ├── AssetMetadata.tsx                      # Asset-level metadata
│   └── ExtentPreview.tsx                      # Spatiotemporal extent visualization
│
├── layout/                                    # Global application layout components
│   ├── Header.tsx                             # Top navigation + governance link
│   ├── Sidebar.tsx                            # Collapsible navigation sidebar
│   ├── Panel.tsx                              # Panel wrapper used across UI
│   ├── PageContainer.tsx                      # Semantic page wrapper
│   └── SplitView.tsx                          # Resizable split-pane layout
│
└── shared/                                    # Reusable low-level UI primitives
    ├── Button.tsx                             # Accessible button component
    ├── IconButton.tsx                         # Icon-only button with ARIA labels
    ├── Dropdown.tsx                           # Menu / listbox pattern
    ├── Tabs.tsx                               # Accessible tab interface
    ├── Modal.tsx                              # Focus-trapped modal
    ├── Tooltip.tsx                            # ARIA-compliant tooltip
    ├── Spinner.tsx                            # Reduced-motion loading indicator
    ├── Badge.tsx                              # General-purpose tag
    ├── Card.tsx                               # Generic card wrapper
    └── FormControls/                          
        ├── TextInput.tsx                      # Accessible text input
        ├── Checkbox.tsx                       # WCAG AA checkbox control
        ├── RadioGroup.tsx                     # Mutually exclusive options
        ├── Select.tsx                         # Keyboard navigable dropdown
        ├── ToggleSwitch.tsx                   # ARIA switch component
        └── FieldLabel.tsx                     # Label + description wrapper
~~~

---

# 🧩 Component Responsibilities

## 1. Rendering
- Deterministic  
- Presentation-only  
- No business logic  
- No global state mutation  

## 2. Accessibility (WCAG 2.1 AA)
All components **must** provide:
- Proper ARIA roles  
- Focus indicators  
- High-contrast colors  
- Reduced-motion support  
- Full keyboard navigation  
- Alt text or SR equivalents  

## 3. Governance
Every component handling content or data must:
- Display CARE classification  
- Show provenance chips  
- Respect sovereignty restrictions  
- Mask sensitive spatial/temporal data  
- Label AI-generated segments  

## 4. Telemetry
Components must trigger:
- Interaction telemetry  
- Navigation telemetry  
- Focus Mode events  
- Map events  
- Story Node events  
- Dataset browsing events  

Telemetry must be **schema-valid, non-PII, CARE-aware**.

---

# 🔐 Governance Enforcement

Rendering unsafe content is prohibited:
- Sensitive coordinates  
- Unmasked sovereignty sites  
- Unverified historical claims  
- Unlabeled AI narratives  

Violations → **CI BLOCK**

---

# ♿ Accessibility Enforcement

Fails if:
- Keyboard navigation breaks  
- SR labels missing  
- Color contrast < AA  
- Motion not respecting preferences  

Accessibility failures → **CI BLOCK**

---

# 🔗 Interaction With Other Layers

Components interact **indirectly** via:
- Hooks  
- Pipeline outputs  
- Context providers  
- Services  

They **never** directly hit APIs.

---

# 🧪 Testing Expectations

Every component must include:
- Unit tests  
- A11y tests  
- Governance tests  
- Telemetry tests  
- Snapshot tests (when appropriate)  

---

# 🕰 Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v10.4.1 | 2025-11-15 | Updated directory structure with labels; added primitives alignment for MapView, TimelineView, and FocusMode |
| v10.4.0 | 2025-11-15 | Full KFM-MDP v10.4 documentation overhaul |
| v10.3.2 | 2025-11-14 | Map + Story Node + governance updates |
| v10.3.1 | 2025-11-13 | Initial components overview |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
FAIR+CARE Certified · Public Document · Version-Pinned  
Validated under MCP-DL v6.3 & KFM-MDP v10.4.1  

</div>
