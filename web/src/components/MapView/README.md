---
title: "🗺️ Kansas Frontier Matrix — MapView Component Suite Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/components/MapView/README.md"
version: "v11.2.2"
last_updated: "2025-11-30"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/web-mapview-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/web-components-mapview-v2.json"
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
classification: "Public / Spatial Data"
jurisdiction: "United States / Kansas"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

status: "Active / Enforced"
doc_kind: "Component Overview"
intent: "frontend-mapview"
semantic_intent:
  - "map-ui"
  - "spatial-visualization"
  - "governance-aware-map"
  - "focus-timeline-sync"

fair_category: "F1-A1-I1-R1"
care_label: "Public / Mixed (dataset-dependent)"
sensitivity_level: "Variable (spatial data)"
public_exposure_risk: "Medium"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"
risk_category: "Mixed"
redaction_required: true

provenance_chain:
  - "web/src/components/MapView/README.md@v10.4.0"
  - "web/src/components/MapView/README.md@v10.3.2"

ontology_alignment:
  cidoc: "E34 Inscription"
  schema_org: "Map"
  owl_time: "TemporalEntity"
  geosparql: "geo:Feature"
  prov_o: "prov:Entity"

json_schema_ref: "../../../../../schemas/json/web-components-mapview-readme-v11.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/web-components-mapview-readme-v11-shape.ttl"
doc_uuid: "urn:kfm:doc:web-components-mapview-readme-v11.2.2"
semantic_document_id: "kfm-doc-web-components-mapview-readme-v11"
event_source_id: "ledger:web/src/components/MapView/README.md"
immutability_status: "version-pinned"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions (no invented geography)"
ai_transform_permissions:
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "diagram-extraction"
ai_transform_prohibited:
  - "coordinate-hallucination"
  - "speculative-spatial-inference"
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
    - "📈 Telemetry Responsibilities"
    - "🧪 Testing Requirements"
    - "🕰 Version History"
    - "⚖️ Footer"
---

<div align="center">

# 🗺️ **Kansas Frontier Matrix — MapView Component Suite Overview**  
`web/src/components/MapView/README.md`

**Purpose:**  
Define the architecture, responsibilities, accessibility, telemetry, and FAIR+CARE governance rules  
for the **MapView** component suite — the primary 2D map rendering layer in the  
Kansas Frontier Matrix (KFM) Web Platform.  

MapView components orchestrate MapLibre rendering, spatial overlays, time-sync, governance masking,  
and Focus Mode v3 / Story Node v3 integration.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)]()  
[![KFM-MDP v11.2.2](https://img.shields.io/badge/KFM%E2%80%93MDP-v11.2.2-purple)]()  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Enforced-gold)]()  
[![WCAG AA+](https://img.shields.io/badge/A11y-WCAG%202.1%20AA%2B-brightgreen)]()

</div>

---

## 📘 Overview

MapView components implement the **core spatial UI** for KFM.

They provide:

- MapLibre GL initialization and lifecycle management  
- Spatial layer rendering (STAC footprints, Story Nodes, Focus overlays, vector tiles)  
- CARE/sovereignty-aware masking overlays (H3 r7+ and above)  
- Visible governance indicators on sensitive spatial data  
- Timeline → Map synchronization (TimeContext → MapView)  
- Focus Mode spatial highlighting and adjacency exploration  
- Accessible map controls and overlays (WCAG 2.1 AA+)  
- Telemetry instrumentation for spatial interactions (pan, zoom, highlight, mask)  

MapView is a **high-governance**, **high-sensitivity** layer, since it touches all geospatial content, including potentially sensitive locations.

---

## 🗂️ Directory Structure

Emoji-enriched v11 layout:

~~~text
web/src/components/MapView/
│
├── 🧭 MapViewContainer.tsx        # Top-level orchestrator (map instance, contexts, sync)
├── 🗺️ MapCanvas.tsx               # MapLibre canvas mount + lifecycle hooks
├── 🗂️ LayerManager.tsx            # Dynamic loading/unloading and ordering of layers
├── 🎨 LegendPanel.tsx             # Accessible legend with CARE-aware color ramps
├── 🔧 MapControls.tsx             # Zoom, reset, rotate, layer toggles, etc.
├── 📚 StoryNodeLayer.tsx          # Story Node v3 footprints + temporal fading
├── 🎯 FocusHighlightLayer.tsx     # Focus Mode entity highlight rendering
├── 📦 DatasetFootprintLayer.tsx   # STAC dataset footprint preview layer
├── 🛡️ SovereigntyMaskLayer.tsx    # H3 masking grids + sovereignty overlays/notices
├── 📍 CursorHUD.tsx               # Coarse cursor readout + map state info
└── 🧾 AttributionBar.tsx          # Map metadata, licensing, and provenance surface
~~~

All files in this directory MUST be described here.

---

## 🧩 Component Responsibilities

### 🧭 MapViewContainer.tsx

**Role:**  
Top-level orchestrator for MapView, wiring contexts and MapLibre instance.

**Responsibilities:**

- Initialize MapLibre map instance with configuration defined by geospatial pipelines  
- Hydrate and propagate contexts:
  - TimeContext (timeline → map sync)  
  - FocusContext (Focus Mode highlighting)  
  - GovernanceContext (CARE + sovereignty flags)  
  - A11yContext (reduced motion, contrast, font scaling)  
- Compose child layers:
  - StoryNodeLayer, FocusHighlightLayer, DatasetFootprintLayer, SovereigntyMaskLayer, etc.  
- Coordinate timeline/map synchronization:
  - When TimeContext changes, adjust map overlays and temporal fading  

**Governance:**

- When GovernanceContext signals that a dataset cannot be shown:
  - do not render corresponding layers  
  - ensure SovereigntyMaskLayer and/or warnings are shown instead  

**Telemetry:**

- `"mapview:load"` when MapViewContainer first mounts with map active  
- `"mapview:context-sync"` when timeline/focus changes propagate to the map  

---

### 🗺️ MapCanvas.tsx

**Role:**  
Low-level MapLibre canvas mount and event subscription.

**Responsibilities:**

- Mount MapLibre `<canvas>` into the DOM  
- Attach sizing/resize observers  
- Respect A11y settings (reduced animation where applicable)  
- Ensure overlays remain legible at different zooms (contrast-aware)  

**Accessibility:**

- Provide ARIA labeling for map container (e.g., `aria-label="Kansas Frontier Matrix map"`)  
- Ensure map controls are reachable via keyboard, not buried inside the canvas alone  

---

### 🗂️ LayerManager.tsx

**Role:**  
Central router for layer ordering and visibility.

**Responsibilities:**

- Determine render ordering of:
  - Base map  
  - SovereigntyMaskLayer  
  - DatasetFootprintLayer  
  - StoryNodeLayer  
  - FocusHighlightLayer  
  - Additional overlays  
- Handle enabling/disabling layers based on:
  - User toggles  
  - Governance context  
  - TimeContext (temporal filtering)  

**Governance:**

- Must guarantee that SovereigntyMaskLayer renders **above** any sensitive geometries  
- Must prevent loading of prohibited layers based on governance flags  

---

### 🎨 LegendPanel.tsx

**Role:**  
Visual and textual legend for map symbology.

**Responsibilities:**

- Display categories and color ramps for:
  - Sovereignty masks  
  - Dataset footprints  
  - Story Node footprints  
  - Focus highlights  
- Show icons and labels for:
  - Masked/generalized layers  
  - CARE classification  

**A11y:**

- Keyboard accessible toggle for opening/closing legend  
- Provide SR-only descriptions for each symbol/color ramp  

**Telemetry:**

- `"mapview:legend-open"` when user opens legend  

---

### 🔧 MapControls.tsx

**Role:**  
Controller bar for standard map controls.

**Controls:**

- Zoom in/out  
- Reset view  
- Rotate map (if applicable)  
- Layer visibility toggles (high-level)  

**Accessibility:**

- Buttons with clear ARIA labels (e.g., `"Zoom in"`, `"Reset view"`)  
- Keyboard shortcuts:
  - `+` / `-` for zoom (when focused)  
  - Additional shortcuts documented where used  

**Telemetry:**

- `"mapview:control-interact"` with action name  

---

### 📚 StoryNodeLayer.tsx

**Role:**  
Render Story Node v3 footprints as geospatial overlays.

**Responsibilities:**

- Draw generalized polygons or markers representing Story Node spatial extents  
- Apply temporal fading based on TimeContext (past vs. current vs. future segments)  
- Attach tooltips/click handling for:
  - Opening Story Node detail view  
  - Jumping to associated timeline slice  

**Governance:**

- Must **never** render raw coordinates for sensitive or archaeological sites  
- Must obey generalized footprints (H3 or similar) and avoid leaking site precision  

**Telemetry:**

- `"mapview:storynode-hover"` / `"mapview:storynode-click"` for interactions  

---

### 🎯 FocusHighlightLayer.tsx

**Role:**  
Highlight the spatial footprint of the Focus Mode entity (and optionally its immediate neighbors).

**Responsibilities:**

- Render an outline or halo around focus entity geometry  
- Optionally show edges or adjacency rings for related locations  
- Provide simple, visually clear highlight styling  

**Governance:**

- H3 generalization for sensitive focus entities (tribal, cultural sites, etc.)  
- No invented geometry; shapes must come from the backend/graph or derived pipelines  

**Telemetry:**

- `"mapview:focus-highlight"` when new entity highlight is rendered  

---

### 📦 DatasetFootprintLayer.tsx

**Role:**  
Display footprints of STAC datasets and other spatial layers.

**Responsibilities:**

- Render bounding polygons or simplified geometry for each dataset  
- Visualize temporal coverage (e.g., shading or line styles over time slices)  
- Indicate dataset CARE classification via color/outline style  

**Governance:**

- Apply masking/generalization to sensitive dataset footprints  
- Provide clear connection to LicenseTag/ProvenanceChip via shared dataset IDs  

**Telemetry:**

- `"mapview:dataset-footprint"` for dataset hover/click interactions  

---

### 🛡️ SovereigntyMaskLayer.tsx

**Role:**  
Core sovereignty and masking layer.

**Responsibilities:**

- Render H3-grid cells (r7+ or coarser) over areas requiring obfuscation  
- Show sovereign territories or culturally sensitive regions, generalized appropriately  
- Display slight overlays or hatch patterns to indicate masked regions  

**Governance:**

- Intended to be ALWAYS above base data for restricted regions  
- Must respect Indigeneous Data Protection policy and mask coordinates for sensitive zones  

**Telemetry:**

- `"mapview:masking-applied"` when mask is active or updated  

---

### 📍 CursorHUD.tsx

**Role:**  
Display coarse state information under the cursor or map center.

**Responsibilities:**

- Show coarse coordinates (rounded, H3-based or truncated) where allowed  
- Indicate active layer or dataset where cursor is hovering  
- Show temporal slice or year when relevant  

**Governance:**

- MUST generalize coordinates over masked or sensitive areas  
- MUST avoid showing full precision lat/lon anywhere flagged as sensitive  

**Telemetry:**

- `"mapview:cursor-move"`—aggregated, non-PII, where enabled  

---

### 🧾 AttributionBar.tsx

**Role:**  
Mandatory licensing and attribution bar for map content.

**Responsibilities:**

- Display:
  - Base map source and license  
  - Spatial dataset attributions  
  - STAC/metadata references where applicable  
- Provide:
  - Links to license text  
  - Optional inline ProvenanceChip for main map sources  

**Governance:**

- Must always be visible or easily accessibly via UI controls  
- Must not be hidden by layout changes  

---

## 🔐 Governance & FAIR+CARE Integration

Because spatial data can be highly sensitive, MapView must strictly enforce:

- **CARE and sovereignty rules:**
  - Mask or generalize positions of sacred/indigenous sites  
  - Hide or coarsen details for protected locations  
- **No fabricated spatial content:**
  - All geometry MUST come from validated backend sources or deterministic pipelines  
  - No front-end inference of paths, boundaries, or extents  

- **Clear governance surfaces:**
  - Indicate masked regions via SovereigntyMaskLayer and MaskingIndicator (from Governance)  
  - Display warnings or hints when map views include sensitive areas  

MapView must never:

- Show raw coordinates for data flagged as sensitive or sovereignty-controlled  
- Render unapproved geometry or “fill in” missing spatial information by guesswork  

Any governance failure is a **CI-blocking condition**.

---

## ♿ Accessibility Requirements (WCAG 2.1 AA+)

MapView v11.2.2 MUST:

- Provide keyboard navigation to:
  - Map controls  
  - LegendPanel  
  - Layer toggles  
- Use proper semantics:
  - Map container labeled (`role="region"` / `aria-label`)  
  - Controls as buttons with accessible names  
- Respect user preferences:
  - `prefers-reduced-motion` → toned-down panning/zoom animations where controllable  
- Avoid color-only semantics for:
  - CARE categories  
  - Sovereignty vs. non-sovereignty overlays  
  - Focus vs. non-focus highlights  

Accessibility test failures MUST block merges.

---

## 📈 Telemetry Responsibilities

MapView components feed spatial usage and governance telemetry.

Events include (at minimum):

- `"mapview:load"` — map initialized  
- `"mapview:pan"` / `"mapview:zoom"` — panning/zoom operations  
- `"mapview:layer-toggle"` — layer visibility toggled  
- `"mapview:legend-open"` — LegendPanel opened  
- `"mapview:masking-applied"` — sovereignty masking active/updated  
- `"mapview:dataset-footprint"` — dataset footprint interacted with  
- `"mapview:storynode-hover"` — Story Node feature hovered  
- `"mapview:focus-highlight"` — new focus highlight active  

Telemetry MUST:

- Conform to `telemetry_schema` above  
- Avoid PII (aggregate counts only)  
- Include environment + component version tags  

---

## 🧪 Testing Requirements

MapView tests MUST cover:

- **Unit tests:**
  - Each subcomponent (MapCanvas, LayerManager, LegendPanel, etc.)  
  - Guard-rail behaviors (e.g., not rendering sensitive layer when flagged)  

- **Integration tests:**
  - MapView + timeline synchronization  
  - Focus Mode spatial highlighting  
  - Governance and masking interplay with map layers  

- **Accessibility tests:**
  - Keyboard navigation to controls and legend  
  - ARIA labels and roles on map regions and controls  
  - Contrast checks for overlays and legends  

- **Telemetry tests:**
  - Events emitted with correct payload shapes and timing  

Test layout:

~~~text
tests/unit/web/components/MapView/**
tests/integration/web/components/MapView/**
~~~

---

## 🕰 Version History

| Version | Date       | Summary                                                                 |
|--------:|------------|-------------------------------------------------------------------------|
| v11.2.2 | 2025-11-30 | Upgraded to v11.2.2; telemetry v2, governance & A11y clarifications, H3 masking rules |
| v10.4.0 | 2025-11-15 | Complete rewrite under KFM-MDP v10.4; full spatial governance, A11y, and telemetry |
| v10.3.2 | 2025-11-14 | Improved footprint rendering + CARE masking                            |
| v10.3.1 | 2025-11-13 | Initial MapView architecture overview                                  |

---

## ⚖️ Footer

<div align="center">

**📚 Governance Links**  
[Docs Root](../../../../../README.md) •  
[Standards Index](../../../../../docs/standards/INDEX.md) •  
[Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

**🔐 Compliance:**  
FAIR+CARE · CIDOC-CRM · OWL-Time · GeoSPARQL · PROV-O · WCAG 2.1 AA+ · SLSA Level 3

**End of Document**

</div>