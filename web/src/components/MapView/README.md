---
title: "🗺️ Kansas Frontier Matrix — MapView Component Suite Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/components/MapView/README.md"
version: "v10.4.0"
last_updated: "2025-11-15"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/web-components-mapview-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Component Overview"
intent: "web-components-mapview"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Mixed (dataset-dependent)"
sensitivity_level: "Variable (spatial data)"
public_exposure_risk: "Medium"
indigenous_rights_flag: "Conditional"
data_steward: "KFM FAIR+CARE Council"
risk_category: "Mixed"
redaction_required: true
provenance_chain:
  - "web/src/components/MapView/README.md@v10.3.2"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E34 Inscription"
  schema_org: "Map"
  owl_time: "TemporalEntity"
  geosparql: "geo:Feature"
  prov_o: "prov:Entity"
json_schema_ref: "../../../../../schemas/json/web-components-mapview-readme.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/web-components-mapview-readme-shape.ttl"
doc_uuid: "urn:kfm:doc:web-components-mapview-readme-v10.4.0"
semantic_document_id: "kfm-doc-web-components-mapview-readme"
event_source_id: "ledger:web/src/components/MapView/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions (no invented geography)"
ai_transform_permissions:
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "coordinate hallucination"
  - "speculative spatial inference"
  - "unverified historical claims"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "United States / Kansas"
classification: "Public / Spatial Data"
role: "overview"
lifecycle_stage: "stable"
ttl_policy: "Review with each KFM release"
sunset_policy: "Superseded upon next MapView system update"
---

<div align="center">

# 🗺️ **Kansas Frontier Matrix — MapView Component Suite Overview**  
`web/src/components/MapView/README.md`

**Purpose:**  
Define the architecture, responsibilities, accessibility, telemetry, and FAIR+CARE governance rules  
for the **MapView** component suite — the primary 2D map rendering layer in the  
Kansas Frontier Matrix (KFM) Web Platform.  
MapView components orchestrate MapLibre rendering, spatial overlays, time-sync, governance masking,  
and Focus Mode v2.5 / Story Node v3 integration.

</div>

---

# 📘 Overview

MapView components are the **core spatial UI** for KFM.

They provide:

- MapLibre GL initialization  
- Spatial layer rendering (STAC footprints, Story Nodes, vector tiles)  
- Generalized masking overlays (H3 r7+)  
- CARE/sovereignty governance indicators  
- Timeline → Map synchronization  
- Focus Mode spatial highlights  
- Accessible map controls  
- Telemetry instrumentation for spatial usage  
- Integration with:
  - `useMap.ts`
  - `mapPipeline.ts`
  - `geospatial pipelines`
  - Governance + A11y contexts

MapView is a *high-governance*, *high-sensitivity* layer.

---

# 🧱 Directory Structure

~~~text
web/src/components/MapView/
├── MapViewContainer.tsx        # Top-level orchestrator (map instance, contexts)
├── MapCanvas.tsx               # MapLibre canvas mount + lifecycle
├── LayerManager.tsx            # Dynamically loads/unloads spatial layers
├── LegendPanel.tsx             # Accessible legend w/ CARE-aware color ramps
├── MapControls.tsx             # Zoom, reset, rotate, toggle controls
├── StoryNodeLayer.tsx          # Story Node v3 footprints + temporal fading
├── FocusHighlightLayer.tsx     # Focus Mode entity highlight rendering
├── DatasetFootprintLayer.tsx   # STAC footprint preview layer
├── SovereigntyMaskLayer.tsx    # H3 masking grids + sovereignty notices
├── CursorHUD.tsx               # Coarse cursor readout + map state information
└── AttributionBar.tsx          # Map metadata, licensing, provenance
~~~

---

# 🧩 Component Responsibilities

---

## 🧭 **MapViewContainer.tsx**
Provides:

- Context hydration (Time, Focus, Governance, A11y)
- MapLibre initialization
- Layer assembly pipeline
- Spatial orchestration with geospatial pipelines

Governance:

- Blocks rendering when data is prohibited  
- Loads masking overlays first  
- Displays governance banners

Telemetry:

- `"mapview:load"`  
- `"mapview:context-sync"`  

---

## 🗺️ **MapCanvas.tsx**
Renders the actual MapLibre canvas.

Requirements:

- Respect reduced-motion for transitions  
- Provide appropriate ARIA roles  
- Guarantee 4.5:1 contrast for overlays  
- Handle resize + accessibility scaling  

---

## 🗂️ **LayerManager.tsx**
Handles:

- Layer ordering  
- Rendering STAC footprints  
- Loading line, polygon, raster layers  
- Conflict resolution among overlapping layers  

Governance:

- Ensures sensitive layers are masked  
- Applies CARE label–based styling  

---

## 🎨 **LegendPanel.tsx**
Displays:

- CARE-aware legend categories  
- Accessible color ramps  
- Layer descriptions  
- Masking indicators  

Must:

- Be accessible via keyboard  
- Contain SR-only descriptions of map categories  

Telemetry: `"mapview:legend-open"`

---

## 🔧 **MapControls.tsx**
Controls include:

- Zoom  
- Rotate  
- Reset view  
- Toggle markers/layers  

A11y:

- ARIA-compliant button roles  
- Keyboard shortcuts (`+`, `-`, `r`)  

Telemetry: `"mapview:control-interact"`

---

## 🗺️ **StoryNodeLayer.tsx**
Renders Story Node v3 footprints:

- Generalized polygons  
- Temporal fading based on TimeContext  
- CARE labels + provenance chips  

Governance:

- Never expose original archaeological/sacred site coordinates  
- Always display ethical context  

Telemetry: `"mapview:storynode-hover"`

---

## 🎯 **FocusHighlightLayer.tsx**
Highlights:

- Focus Mode entity geometry  
- Related entities  
- Spatial neighborhood  

Requirements:

- H3 generalization  
- No speculative shapes  
- Accurate but privacy-preserving representation  

Telemetry: `"mapview:focus-highlight"`

---

## 📦 **DatasetFootprintLayer.tsx**
Displays STAC footprints:

- COG boundary polygons  
- Dataset temporal extent shading  
- CARE overlays  

Governance:

- Apply masking to sensitive datasets  
- Show sovereignty notices  

Telemetry: `"mapview:dataset-footprint"`

---

## 🛡️ **SovereigntyMaskLayer.tsx**
Displays:

- H3 r7+ masking cells  
- Sovereignty boundaries  
- Cultural protection overlays  

Governance:

- Mandatory for any culturally restricted data  
- Always displayed ABOVE base layers  

Telemetry: `"mapview:masking-applied"`

---

## 📍 **CursorHUD.tsx**
Shows:

- Mouse position (coarse-rounded if sensitive)  
- Active layer name  
- Temporal slice  

Governance:

- MUST generalize coordinates over sensitive areas  

Telemetry: `"mapview:cursor-move"`

---

## 📝 **AttributionBar.tsx**
Displays:

- Map tile licenses  
- Dataset rights-holder metadata  
- Provenance chips  
- FAIR+CARE documentation links  

Governance:

- Must always be visible  
- Must include machine-readable licensing metadata  

---

# 🔐 Governance & FAIR+CARE Integration

MapView components MUST:

- Enforce all CARE classifications  
- Apply sovereignty-based masking (H3 r7 minimum)  
- Generalize coordinates  
- Display ethical warnings  
- Label AI-generated overlays  
- Blur/remove sensitive geometry  
- Expose provenance metadata consistently  

Governance violations = **CI BLOCK**.

---

# ♿ Accessibility Requirements (WCAG 2.1 AA)

MapView MUST:

- Provide keyboard navigation for map controls  
- Avoid color-only information  
- Respect motion-reduction preferences  
- Provide text equivalents for layers + legends  
- Use strong, visible focus rings  
- Ensure readable contrast  

A11y violations block merges.

---

# 📈 Telemetry Responsibilities

Telemetry events include:

- `"mapview:load"`  
- `"mapview:pan"` / `"mapview:zoom"`  
- `"mapview:layer-toggle"`  
- `"mapview:legend-open"`  
- `"mapview:masking-applied"`  
- `"mapview:dataset-footprint"`  
- `"mapview:storynode-hover"`  
- `"mapview:focus-highlight"`

Telemetry must:

- Be non-PII  
- Follow schema  
- Be FAIR+CARE-aware  
- Flow to:  
  `releases/<version>/focus-telemetry.json`

---

# 🧪 Testing Requirements

Tests MUST cover:

- Rendering correctness  
- Timeline synchronization  
- Governance enforcement  
- Coordinate generalization  
- Accessibility (ARIA, keyboard, contrast)  
- Telemetry events  
- Integration with STAC, Focus Mode, Story Nodes  

Tests located at:

~~~text
tests/unit/web/components/MapView/**
tests/integration/web/components/MapView/**
~~~

---

# 🕰 Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v10.4.0 | 2025-11-15 | Complete rewrite under KFM-MDP v10.4; full spatial governance, A11y, and telemetry integration |
| v10.3.2 | 2025-11-14 | Improved footprint rendering + CARE masking |
| v10.3.1 | 2025-11-13 | Initial MapView architecture overview |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
FAIR+CARE Certified · Public Document · Version-Pinned  
Validated under MCP-DL v6.3 & KFM-MDP v10.4  

</div>
