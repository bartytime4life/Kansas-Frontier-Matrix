---
title: "🗺️ Kansas Frontier Matrix — Map Components Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/components/map/README.md"
version: "v11.2.2"
last_updated: "2025-11-30"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.2/web-map-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/web-components-map-v2.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
classification: "Public / Geospatial"
jurisdiction: "Kansas / United States"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

status: "Active / Enforced"
doc_kind: "Component Overview"
intent: "frontend-map-components-overview"
semantic_intent:
  - "map-ui"
  - "spatial-rendering"
  - "governed-geospatial"

fair_category: "F1-A1-I1-R1"
care_label: "Public / Mixed (dataset-dependent)"
sensitivity_level: "Varies (geospatial)"
public_exposure_risk: "Medium"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"
risk_category: "Mixed"
redaction_required: true

provenance_chain:
  - "web/src/components/map/README.md@v10.4.0"
  - "web/src/components/map/README.md@v10.3.2"

ontology_alignment:
  cidoc: "E34 Inscription"
  schema_org: "Map"
  owl_time: "TemporalEntity"
  geosparql: "geo:Feature"
  prov_o: "prov:Entity"

json_schema_ref: "../../../../schemas/json/web-components-map-readme-v11.schema.json"
shape_schema_ref: "../../../../schemas/shacl/web-components-map-readme-v11-shape.ttl"
doc_uuid: "urn:kfm:doc:web-components-map-readme-v11.2.2"
semantic_document_id: "kfm-doc-web-components-map-readme-v11"
event_source_id: "ledger:web/src/components/map/README.md"
immutability_status: "version-pinned"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with strict constraints"
ai_transform_permissions:
  - "a11y-adaptations"
  - "semantic-highlighting"
  - "diagram-extraction"
ai_transform_prohibited:
  - "speculative-additions"
  - "unverified-historical-claims"
  - "coordinate-hallucination"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Structure"
    - "🧩 Component Responsibilities"
    - "🔐 FAIR+CARE & Governance Requirements"
    - "♿ Accessibility Requirements (WCAG 2.1 AA+)"
    - "📈 Telemetry Responsibilities"
    - "🧪 Testing Requirements"
    - "🕰 Version History"
    - "⚖️ Footer"
---

<div align="center">

# 🗺️ **Kansas Frontier Matrix — Map Components Overview**  
`web/src/components/map/README.md`

**Purpose:**  
Document the structure, responsibilities, FAIR+CARE obligations, geospatial governance,  
accessibility rules, and telemetry requirements for all **MapLibre-based map components**  
implemented in `web/src/components/map/**` within the KFM Web Platform.

These components form a **legacy-compatible 2D spatial interface** that still underpins parts  
of the Kansas Frontier Matrix, especially during migration to the full v3 `MapView/` subsystem.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)]()  
[![KFM-MDP v11.2.2](https://img.shields.io/badge/KFM%E2%80%93MDP-v11.2.2-purple)]()  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Enforced-gold)]()  
[![WCAG AA+](https://img.shields.io/badge/A11y-WCAG%202.1%20AA%2B-brightgreen)]()

</div>

---

## 📘 Overview

Map components in this directory:

- Render or assist rendering of MapLibre GL’s 2D map instance  
- Provide low-level layer toggling, legend, highlighting, and masking UI  
- Enforce H3 r7+ masking for sensitive geospatial content (through parent governance props)  
- Display inline governance metadata (via overlays) when configured  
- Sync with timeline, Focus Mode, and Story Node v3 via shared contexts (in legacy paths)  
- Emit or support emission of spatial telemetry (via higher-level wrappers)  
- Follow strict A11y design constraints for map controls and overlays  
- Integrate with v11 geospatial pipelines and governance contexts  
- Maintain deterministic and ethics-safe rendering behavior  

These components must **never** perform speculative spatial inference or bypass masking/generalization rules.  
Where v3 `MapView/` exists, these components act as compatibility glue and primitives only.

---

## 🗂️ Directory Structure

~~~text
web/src/components/map/
│
├── 🗺️ MapContainer.tsx              # Legacy MapLibre instance initialization & context binding
├── 🔘 LayerToggle.tsx               # Accessible per-layer toggle control
├── 🎨 Legend.tsx                    # CARE-aware, WCAG AA+ accessible legend UI
├── ✨ FeatureHighlight.tsx          # Focus/Story Node highlight renderer (coarse only)
├── 🛡️ ProvenanceOverlay.tsx         # Inline overlay for license, CARE, provenance chips
├── 🔳 MaskedArea.tsx                # H3 r7+ masking/generalization visualization
├── 📍 StoryNodeMarkers.tsx          # Story Node v3 spatial markers + time-aware fading
└── 🖥️ MapInteractionHUD.tsx         # HUD for spatial info, coarse cursor position, measurements
~~~

New files in this directory MUST be documented here.

---

## 🧩 Component Responsibilities

### 🗺️ MapContainer.tsx

**Role:**  
Legacy root wrapper for MapLibre GL maps.

**Responsibilities:**

- Initialize MapLibre instance using configuration passed in from parent (no direct pipeline calls)  
- Register pan/zoom/rotate events and forward them to higher-level orchestrators  
- Provide a predictable map mount and reference for layers and overlays  
- Bind to:
  - TimeContext  
  - FocusContext  
  - GovernanceContext  
  - A11yContext  

**Governance:**

- MUST NOT add ungoverned layers on its own  
- MUST respect flags from GovernanceContext (`redaction_required`, `indigenous_rights_flag`, etc.)  
- MUST allow SovereigntyMaskLayer/MaskedArea or equivalent overlays to sit above base layers  

**Telemetry (via parent wiring):**

- `"map:load"`  
- `"map:pan"` / `"map:zoom"`  
- `"map:layer-toggle"`  

---

### 🔘 LayerToggle.tsx

**Role:**  
Accessible toggle control for individual map layers.

**Responsibilities:**

- Render toggles with:
  - Clear layer names / icons  
  - ARIA roles and labels (e.g., `role="switch"` or `checkbox` semantics)  
- Forward user interactions to parent map controller (no layer logic inside)  

**Governance:**

- MUST disable or hide toggles for layers disallowed by governance/CARE flags  
- MUST support reason hints (via tooltip/label) for disabled layers (e.g., “Sovereignty-restricted dataset”)  

**A11y:**

- Keyboard-operable toggle (Space/Enter)  
- Focus-visible styling and high color contrast  

---

### 🎨 Legend.tsx

**Role:**  
Legacy accessible legend UI.

**Responsibilities:**

- Display color ramps and symbols for:
  - Sovereignty masks  
  - Story Node overlays  
  - Dataset footprints  
  - Environmental/historical layers  
- Provide textual descriptions or SR-only equivalents for each legend element  

**Governance:**

- CARE-aware labeling (Public, Restricted, Sovereignty-controlled, etc.)  
- Clear indication where masking/generalization is applied  

**A11y:**

- WCAG AA+ contrast for all legend elements  
- Screen-reader descriptive text for color-coded symbology  

---

### ✨ FeatureHighlight.tsx

**Role:**  
Feature highlighting primitive for focus and selection.

**Responsibilities:**

- Render simple highlight outlines or halos for selected map features  
- Support hover and selection visual states (via props)  

**Governance:**

- NEVER render precise geometry for sensitive features (only generalized shapes provided by parent)  
- Defer to masking overlays for sovereignty-sensitive zones  
- No geometry computation or inference inside the component  

---

### 🛡️ ProvenanceOverlay.tsx

**Role:**  
Inline map overlay for governance metadata.

**Responsibilities:**

- Show:
  - CARE badges  
  - License tags  
  - Provenance chips  
  - Warnings where appropriate  
- Provide quick “at a glance” governance context atop the map  

**A11y:**

- Keyboard reachable (tab into overlay)  
- ARIA labels for small badges/icons  

**Governance:**

- MUST reflect metadata supplied from GovernanceContext  
- Must never contradict or override backend governance decisions  

---

### 🔳 MaskedArea.tsx

**Role:**  
Visual representation of masked or generalized spatial areas.

**Responsibilities:**

- Render H3 r7+ (or coarser) grid cells, blur overlays, or patterns over masked regions  
- Provide tooltip/explanation such as:
  - “Location generalized due to CARE/sovereignty rules.”  

**Governance:**

- MUST not show original geometry or allow easy inverse inference  
- Must distinguish masked vs non-masked zones clearly  

---

### 📍 StoryNodeMarkers.tsx

**Role:**  
Display Story Node v3 spatial markers, coordinated with TimeContext.

**Responsibilities:**

- Render marker positions based strictly on generalized coordinates passed in from parent  
- Apply visual fading or emphasis based on temporal position (e.g., older vs newer Story Nodes)  
- Provide hooks for opening Story Node detail views / Focus Mode when clicked  

**Governance:**

- Must never reveal high-precision coordinates for archaeological/sacred sites  
- Must integrate with masked regions (e.g., marker only appears as a generalized location)  

---

### 🖥️ MapInteractionHUD.tsx

**Role:**  
Heads-up display for map interactions.

**Responsibilities:**

- Coarsely show cursor position (rounded or snapped to grid) when allowed  
- Show active layer info, scale, or measurement hints when parent instructs  
- Provide keyboard shortcut hints for map controls  

**Governance:**

- MUST generalize or hide coordinates when the cursor is over restricted regions  
- MUST not display any raw coordinates from restricted datasets  

---

## 🔐 FAIR+CARE & Governance Requirements

Even though these are legacy-level map components, they are still **governance-critical**.

They MUST:

- Respect all sovereignty and CARE flags from contexts/props  
- Mask or generalize sensitive spatial info as instructed by parent components  
- Never produce or manipulate coordinates on their own (no spatial inference)  
- Cooperate with SovereigntyMask/MapView overlays by not drawing over them in a way that hides governance cues  
- Never create or adjust geometry without explicit, deterministic instructions from higher-level geospatial code  

Any violation of these principles is a **CI-blocking governance failure**.

---

## ♿ Accessibility Requirements (WCAG 2.1 AA+)

Map primitives MUST:

- Provide keyboard navigation for interactive controls (LayerToggle, HUD actions)  
- Use ARIA roles appropriately:
  - toggles: `button`, `checkbox` or `switch` semantics  
  - overlays/HUD: `role="status"` or `role="region"` with labels  
- Maintain visible focus indicators  
- Use high-contrast color tokens for icons and text  
- Respect `prefers-reduced-motion` for highlight animations or layer transitions  

A11y issues uncovered in tests MUST block merges.

---

## 📈 Telemetry Responsibilities

Primitives themselves:

- SHOULD NOT emit telemetry directly but must expose stable event/prop APIs so that:
  - v3 `MapView/` and other orchestration layers can emit:
    - `"map:load"`  
    - `"map:pan"` / `"map:zoom"`  
    - `"map:layer-toggle"`  
    - `"map:masking-applied"`  
    - `"map:storynode-hover"`  

Constraints:

- No PII in any bubbled event  
- No coordinate detail added to telemetry from this level beyond what orchestrators explicitly request  

---

## 🧪 Testing Requirements

Each map primitive MUST be covered by:

- **Unit tests:**
  - Rendering with normal and edge-case props  
  - Visual states for toggles, markers, highlights  

- **A11y tests:**
  - ARIA roles and accessible names present  
  - Keyboard interactions performing as expected  

- **Governance tests:**
  - Masks applied correctly when flags set  
  - Raw coordinates not rendered for restricted states  

- **Snapshot tests (optional)** for stable visual structure  

Test layout:

~~~text
tests/unit/web/components/map/**
tests/integration/web/components/map/**   # when combined with orchestration layers
~~~

---

## 🕰 Version History

| Version | Date       | Summary                                                                 |
|--------:|------------|-------------------------------------------------------------------------|
| v11.2.2 | 2025-11-30 | Upgraded to v11.2.2; clarified primitive/legacy role, governance & A11y |
| v10.4.0 | 2025-11-15 | Full KFM-MDP v10.4 rewrite; governance, masking, A11y, STAC/StoryNode   |
| v10.3.2 | 2025-11-14 | Expanded Focus Mode + Story Node integration                            |
| v10.3.1 | 2025-11-13 | Initial map component documentation                                    |

---

## ⚖️ Footer

<div align="center">

**📚 Governance Links**  
[Docs Root](../../../../README.md) •  
[Standards Index](../../../../docs/standards/INDEX.md) •  
[Governance Charter](../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

**🔐 Compliance:**  
FAIR+CARE · GeoSPARQL · CIDOC-CRM · OWL-Time · PROV-O · WCAG 2.1 AA+ · SLSA Level 3

**End of Document**

</div>