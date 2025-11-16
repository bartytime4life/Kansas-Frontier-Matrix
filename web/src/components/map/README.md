---
title: "🗺️ Kansas Frontier Matrix — Map Components Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/components/map/README.md"
version: "v10.4.0"
last_updated: "2025-11-15"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/web-components-map-v1.json"
governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Component Overview"
intent: "map-components-overview"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Mixed (dataset-dependent)"
sensitivity_level: "Varies (geospatial)"
public_exposure_risk: "Medium"
indigenous_rights_flag: "Conditional"
data_steward: "KFM FAIR+CARE Council"
risk_category: "Mixed"
redaction_required: true
provenance_chain:
  - "web/src/components/map/README.md@v10.3.2"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E34 Inscription"
  schema_org: "Map"
  owl_time: "TemporalEntity"
  geosparql: "geo:Feature"
  prov_o: "prov:Entity"
json_schema_ref: "../../../../schemas/json/web-components-map-readme.schema.json"
shape_schema_ref: "../../../../schemas/shacl/web-components-map-readme-shape.ttl"
doc_uuid: "urn:kfm:doc:web-components-map-readme-v10.4.0"
semantic_document_id: "kfm-doc-web-components-map-readme"
event_source_id: "ledger:web/src/components/map/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with strict constraints"
ai_transform_permissions:
  - "a11y-adaptations"
  - "semantic-highlighting"
ai_transform_prohibited:
  - "speculative additions"
  - "unverified historical claims"
  - "coordinate hallucination"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Public / Geospatial"
role: "overview"
lifecycle_stage: "stable"
ttl_policy: "Review each KFM release"
sunset_policy: "Superseded upon map system refactor"
---

<div align="center">

# 🗺️ **Kansas Frontier Matrix — Map Components Overview**  
`web/src/components/map/README.md`

**Purpose:**  
Document the structure, responsibilities, FAIR+CARE obligations, geospatial governance,  
accessibility rules, and telemetry requirements for all **MapLibre-based map components**  
implemented in `web/src/components/map/**` within the KFM Web Platform.

These components form the **primary 2D spatial interface** for the Kansas Frontier Matrix.

</div>

---

# 📘 Overview

Map components in this directory:

- Render MapLibre GL's 2D map instance  
- Handle all spatial overlays (STAC footprints, Story Nodes, Focus Mode highlights)  
- Enforce CARE masking + sovereignty redaction rules  
- Display governance metadata inline on the map  
- Sync with timeline, Focus Mode, and Story Node v3 contexts  
- Emit structured telemetry for spatial interactions  
- Follow strict A11y design constraints for map controls  
- Integrate with geospatial pipelines and context providers  
- Maintain deterministic, ethics-safe rendering behavior  

These components **must never** perform speculative spatial inference  
and **must not** bypass masking/generalization settings.

---

# 🧱 Directory Structure

~~~text
web/src/components/map/
├── MapContainer.tsx              # Initializes MapLibre instance, binds contexts
├── LayerToggle.tsx               # Accessible control for enabling/disabling map layers
├── Legend.tsx                    # CARE-aware, WCAG-AA accessible legend UI
├── FeatureHighlight.tsx          # Focus Mode + Story Node highlight renderer
├── ProvenanceOverlay.tsx         # Inline map overlay for license, CARE, provenance chips
├── MaskedArea.tsx                # Shows H3 r7+ masking generalization visually
├── StoryNodeMarkers.tsx          # Story Node v3 spatial markers + time-aware fading
└── MapInteractionHUD.tsx         # HUD for spatial info, measurements, cursor position
~~~

---

# 🧩 Component Responsibilities

## 🌍 MapContainer.tsx  
The root of all map interactions.

Responsibilities:

- Create MapLibre GL map instance  
- Register pan/zoom/rotate event listeners  
- Hydrate layers from:
  - STAC footprints  
  - Story Node geometries  
  - Focus Mode spatial context  
  - Governance overlays  
- Bind to:
  - TimeContext  
  - FocusContext  
  - GovernanceContext  
  - A11yContext  

Telemetry:

- `"map:load"`  
- `"map:pan"` / `"map:zoom"`  
- `"map:layer-toggle"`

Governance enforcement:

- Apply masking overlays  
- Hide restricted geometry  
- Display sovereignty banners  

---

## 🧩 LayerToggle.tsx  
Accessible toggle control for map layers.

Must:

- Use ARIA-compliant toggle roles  
- Provide clear layer names  
- Mark layers with CARE labels  
- Emit telemetry: `"map:layer-toggle"`  
- Respect color contrast & keyboard navigation  

---

## 🎨 Legend.tsx  
Accessible legend UI.

Must:

- Render WCAG-compliant color ramps  
- Represent governance layers distinctly  
- Show H3-masked vs real geometries  
- Include icons for:
  - Story Nodes  
  - Focus Mode  
  - STAC footprints  
  - Environmental layers  

Governance:

- Must visually convey masking, sovereignty, and CARE classifications  

---

## ✨ FeatureHighlight.tsx  
Renders highlighted features from:

- Focus Mode entities  
- Story Node selections  
- Timeline-filtered features  

Must:

- Avoid precise localization of restricted entities  
- Use generalization or blur when required  
- Respect theme + reduced-motion preferences  

---

## 🛡️ ProvenanceOverlay.tsx  
Renders translated governance metadata directly on map:

- CARE badges  
- License chips  
- Provenance steps  
- Warning banners for sensitive datasets  

All overlays must be:

- Non-obstructive  
- Keyboard reachable  
- WCAG AA compliant  

---

## 🔳 MaskedArea.tsx  
Visual representation of masked or generalized spatial areas.

Rules:

- Must use H3 r7 or coarser  
- Never show original geometry  
- Provide tooltip:  
  “Location generalized for CARE/sensitivity reasons.”

---

## 🗺️ StoryNodeMarkers.tsx  
Displays Story Node v3 markers:

- Geometry centroids or generalized footprints  
- Time-aware fading (based on TimeContext)  
- Interaction handlers for Focus Mode  
- Governance labels encoded in marker style  

Governance:

- Must not reveal sensitive archaeological sites  
- Must merge with geospatial masking rules  

---

## 🖥️ MapInteractionHUD.tsx  
Contextual HUD with:

- Cursor readout (coarse-rounded if necessary)  
- Layer debug info (synthetic-only)  
- Keyboard shortcuts (via `useKeybinds`)  

Governance:

- Cursor longitude/latitude must be generalized  
  when hovering over restricted regions.

---

# 🔐 FAIR+CARE & Governance Requirements

Map components are the **highest-risk layer** for governance violations.

They MUST:

- Enforce H3 r7+ masking  
- Respect sovereignty boundaries  
- Display CARE classification prominently  
- Remove or generalize coordinates for flagged datasets  
- Label AI-generated graphics or inferred geometries  
- Provide provenance & rights-holder metadata  

FAILURE → CI BLOCK.

---

# ♿ Accessibility Requirements (WCAG 2.1 AA)

All map components must:

- Provide keyboard navigation for all interactive elements  
- Expose ARIA roles for map HUD, toggles, and legend  
- Provide zoom/rotation through keyboard equivalents  
- Respect reduced-motion for animations  
- Use accessible focus rings  
- Avoid color-only distinctions  

Accessibility regressions → PR BLOCK.

---

# 📈 Telemetry Responsibilities

Map components emit:

- `"map:load"`  
- `"map:interaction"`  
- `"map:layer-toggle"`  
- `"map:highlight"`  
- `"map:storynode-hover"`  
- `"map:masking-applied"`  

Telemetry MUST be:

- Non-PII  
- Schema-valid  
- Stored via telemetry service  
- Included in release:  
  `releases/<version>/focus-telemetry.json`

---

# 🧪 Testing Requirements

Testing MUST include:

- Unit tests for each map component  
- Integration tests with geospatial pipelines  
- Governance tests (masking, sovereignty, CARE tags)  
- Telemetry output validation  
- A11y tests (keyboard, ARIA, contrast)  
- Regression tests for:
  - Layer toggling  
  - Timeline syncing  
  - Focus Mode highlighting  

Tests live in:

~~~text
tests/unit/web/components/map/**
tests/integration/web/components/map/**
~~~

---

# 🕰 Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v10.4.0 | 2025-11-15 | Full KFM-MDP v10.4 rewrite; added governance, masking, A11y, STAC, Story Node, telemetry rules |
| v10.3.2 | 2025-11-14 | Expanded Focus Mode + Story Node integration |
| v10.3.1 | 2025-11-13 | Initial map component documentation |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
Validated under MCP-DL v6.3 & KFM-MDP v10.4  
FAIR+CARE Certified · Public Document · Version-Pinned  

</div>

