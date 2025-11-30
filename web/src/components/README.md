---
title: "🧩 Kansas Frontier Matrix — Web Components Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/components/README.md"
version: "v11.2.2"
last_updated: "2025-11-30"

review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
release_stage: "Stable / Governed"
status: "Active / Enforced"
lifecycle_stage: "LTS"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../releases/v11.2.2/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/web-components-readme-v1.json"
energy_schema: "../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../schemas/telemetry/carbon-v2.json"
signature_ref: "../../releases/v11.2.2/signature.sig"
attestation_ref: "../../releases/v11.2.2/slsa-attestation.json"

governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"

status_category: "Overview"
doc_kind: "Overview"
intent: "web-components-overview"
role: "overview"

fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk (unless displaying CARE-masked data)"
sensitivity_level: "None"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false

provenance_chain:
  - "web/src/components/README.md@v10.3.1"
  - "web/src/components/README.md@v10.3.2"
  - "web/src/components/README.md@v10.4.0"
  - "web/src/components/README.md@v10.4.1"

ontology_alignment:
  cidoc: "E28 Conceptual Object"
  schema_org: "WebPageElement"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"

json_schema_ref: "../../schemas/json/web-components-readme-v11.schema.json"
shape_schema_ref: "../../schemas/shacl/web-components-readme-shape.ttl"

doc_uuid: "urn:kfm:doc:web-components-readme-v11.2.2"
semantic_document_id: "kfm-doc-web-components-readme"
event_source_id: "ledger:web/src/components/README.md"
immutability_status: "version-pinned"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "diagram-extraction"
  - "metadata-extraction"
ai_transform_prohibited:
  - "summaries"
  - "speculative-additions"
  - "unverified-historical-claims"
  - "governance-override"
  - "content-alteration"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "United States / Kansas"
classification: "Public Document"

ttl_policy: "Review each release"
sunset_policy: "Superseded upon next component-layer revision"
---

<div align="center">

# 🧩 **Kansas Frontier Matrix — Web Components Overview (v11.2.2)**  
`web/src/components/README.md`

**Purpose**  
Provide the authoritative, FAIR+CARE-aligned directory and structural overview for all UI components  
within the Kansas Frontier Matrix Web Platform.  
This document defines the **canonical component hierarchy**, **responsibilities**,  
**accessibility requirements**, **governance rules**, and **telemetry expectations** for  
every component within `web/src/components/**`.

</div>

---

## 📘 1. Overview

All UI components inside this directory:

- Are **presentation-layer** building blocks (no direct API calls or business logic).  
- Are deterministic, testable, and governed under KFM v11.2.2.  
- Integrate with:
  - 🗺️ **MapLibre** + 🌍 **Cesium**  
  - 📖 **Story Node v3**  
  - 🎯 **Focus Mode v3**  
  - 📦 **STAC/DCAT metadata**  
  - ⚖️ **Governance & CARE overlays**  
  - ♿ **A11y tokens + design system**  
  - 📈 **Telemetry hooks** (OpenTelemetry v11)  

Components must:

- Meet **WCAG 2.1 AA** accessibility requirements.  
- Follow **KFM-MDP v11.2.2** documentation and formatting standards.  
- Pass governance validation for:
  - CARE labeling  
  - Provenance visibility  
  - Sovereignty masking  
  - AI narrative restrictions (no speculative content)  

Components function as **atomic UI elements** used by pages, feature modules, and pipelines defined in  
`web/src/ARCHITECTURE.md` and `web/ARCHITECTURE.md`.

---

## 🗂 2. Directory Structure (Component Categories)

~~~text
web/src/components/
├── 🗺️ map/                 # MapLibre-based map views and controls
├── 🕒 timeline/            # Timeline tracks, ranges, and temporal controls
├── 🎯 focus/               # Focus Mode v3 panels and explainability views
├── 📖 story/               # Story Node v3 cards, details, and media shells
├── ⚖️ governance/          # CARE labels, provenance chips, masking indicators
├── 📦 stac/                # STAC/DCAT dataset cards, lists, previews
├── 🧩 layout/              # Layout shells, panels, page wrappers, split views
└── 🧱 shared/              # Low-level reusable UI primitives (buttons, forms, etc.)
~~~

Each subdirectory has its own internal organization, but the **top-level categories** above are stable and governed.  
Any new category must be approved in a web-src architecture review.

---

## 🧱 3. Component Responsibilities

### 3.1 Rendering & Composition

Components:

- Render UI, handle local interactions, and implement A11y semantics.  
- Compose other components (e.g., MapView + Legend + Controls).  
- **Must not**:
  - Call backend APIs directly.  
  - Implement cross-cutting state logic (use hooks/contexts instead).  
  - Override governance or masking flags.

### 3.2 Integration Boundaries

Components receive:

- Data via props from **hooks**, **context**, or **pipelines**, not directly from services.  
- Governance flags, CARE labels, and sovereignty indicators **already resolved** by upstream layers.  

They return:

- Pure visual output + user interactions (callbacks) to the calling layer.

---

## 🧭 4. Category-by-Category Overview

### 4.1 `map/` — Map & Spatial UI

Typical components:

- `MapViewContainer` / `MapCanvas` — MapLibre GL mounting and layout.  
- `LayerManager` — toggling STAC/Story layers (driven by state, not services).  
- `LegendPanel` — CARE-aware legend; indicates masking/generalization.  
- `MapControls` — zoom, rotate, reset; fully keyboard-accessible.  
- Spatial overlays:
  - Story Node geometries.  
  - Focus highlights.  
  - Dataset footprints.  
  - Sovereignty masking grids (H3 generalization).  

**Requirements:**

- Respect generalized/ masked geometries provided by backend.  
- Display sovereignty notices supplied via governance contexts.  
- Provide screen-reader-friendly summaries where possible (e.g., “3 Story Nodes visible in view”).

---

### 4.2 `timeline/` — Temporal UI

Typical components:

- `TimelineView` or `TimelinePrimary` — main axis and active range.  
- `TimelineMarkersLayer` — Story Nodes, events, STAC items, and datasets as markers.  
- `TimelineControls` — granularity switches, zoom, filter toggles.  
- `TimelineA11yHelpers` — screen reader text and keyboard overlays.

**Requirements:**

- Use keyboard-accessible handles and controls.  
- Expose ARIA descriptions for the current temporal range and selection.  
- Display CARE-related temporal warnings (e.g., restricted visibility windows).

---

### 4.3 `focus/` — Focus Mode v3 Components

Typical components:

- `FocusContainer` — high-level layout for Focus Mode panels.  
- `FocusHeader` — focal entity name, CARE labels, provenance summary.  
- `FocusSummary` — short narrative summary (AI-generated label when present).  
- `FocusTabs` — navigation between summary, relations, explainability, etc.  
- `RelationsPanel` / `RelationCard` — graph neighbors and related entities.  
- `NarrativeSection` — rich textual narrative, governance-filtered.  
- `ExplainabilitySection` — SHAP/LIME summary plots, if available.  

**Requirements:**

- Clearly label AI-generated content and show provenance.  
- Respect `ai_transform_prohibited` restrictions.  
- Provide explicit “Why am I seeing this?” and “Show supporting data” controls.  

---

### 4.4 `story/` — Story Node v3 UI

Typical components:

- `StoryCard` — compact narrative preview.  
- `StoryDetail` — full narrative, relations, media slots.  
- `StoryMapPreview` — **generalized** spatial preview.  
- `StoryRelations` — related entities/datasets lists.  

**Requirements:**

- Always render CARE labels / sovereignty warnings if provided.  
- Never show precise coordinates for sensitive/sovereign Story Nodes (masking handled upstream, but UI must not imply precision).  
- Provide consistent card layouts with clear headings, summaries, and accessible structure.

---

### 4.5 `governance/` — Governance & CARE Presentation

Typical components:

- `CAREBadge` — CARE classification.  
- `LicenseTag` — SPDX-style license indicator.  
- `ProvenanceChip` / `ProvenanceTrail` — inline chips and full chain views.  
- `SovereigntyNotice` — prominent banner for sovereign or sensitive content.  
- `MaskingIndicator` — explicit label when locations are generalized/masked.  

**Requirements:**

- Governance overlays are **non-optional** and cannot be suppressed by user preference where policy requires them.  
- Components must be visually prominent enough to satisfy governance guidelines.  

---

### 4.6 `stac/` — STAC/DCAT Dataset Exploration

Typical components:

- `DatasetCard` / `DatasetList` — dataset summaries and lists.  
- `ItemPreview` — STAC Item preview (map thumbnail, date/time).  
- `AssetMetadata` — per-asset key metadata and licensing.  
- `ExtentPreview` — bounding box and temporal extent visualization.  

**Requirements:**

- Always show license and FAIR+CARE labels when available.  
- Respect dataset-level masking rules (e.g., aggregated footprints for sensitive layers).  

---

### 4.7 `layout/` — Layout & Shell Components

Typical components:

- `Header` — top navigation, governance links, project identity.  
- `Sidebar` — navigation tree and quick filters.  
- `PageContainer` — semantic `<main>` regions per route.  
- `SplitView` — resizable pane layouts for map + panels.  

**Requirements:**

- Provide landmark roles (`header`, `nav`, `main`, `complementary`).  
- Work cleanly with screen readers and keyboard navigation.

---

### 4.8 `shared/` — Low-Level UI Primitives

Typical components:

- Buttons, icon buttons, dropdowns, tabs, modals, tooltips, spinners, badges.  
- `FormControls/` — accessible text inputs, checkboxes, radio groups, selects, toggles.  

**Requirements:**

- All primitives are A11y-compliant and reused across higher-level components.  
- No direct service calls; they are pure UI and small state only.

---

## ⚖ 5. Governance & AI Behavior

Components that **render data or narratives** must:

- Display CARE classification and sovereignty indicators, when provided.  
- Show provenance chips for datasets, Story Nodes, and Focus narratives.  
- Never invent content or unverified claims.  
- Clearly label AI-generated segments as such, when they appear.  

AI-related behavior:

- **Allowed transforms:** semantic highlighting, A11y adaptations, metadata/diagram extraction.  
- **Prohibited:** speculative additions, summaries that alter governance meaning, unverified historical claims, governance override, content alteration.

---

## ♿ 6. Accessibility (WCAG 2.1 AA)

All components must:

- Support **keyboard navigation** (tab/focus order, ARIA roles).  
- Provide visible focus states.  
- Use color only in combination with other cues (icon, label, shape).  
- Support reduced motion when OS/user preferences indicate.  
- Expose accessible names, roles, and descriptions for interactive elements.  

Accessibility failures in core components result in **CI block** for dependent features.

---

## 📈 7. Telemetry Expectations

Components emitting user interactions should:

- Use shared telemetry hooks (e.g., `useTelemetry`) rather than ad-hoc logging.  
- Emit events that:
  - Conform to `web-components-readme-v1` schema.  
  - Contain no PII or sensitive fields.  
  - Include high-level context labels (component area, route, interaction type).  

Example events:

- Map layer toggles, timeline range changes, focus tab switches, Story Node expansions, dataset previews.

---

## 🔗 8. Interaction With Other Layers

Components interact with:

- **Hooks** — to obtain data and perform actions.  
- **Context providers** — to read/update shared state.  
- **Pipelines** — as visual endpoints of orchestration flows.  

They **do not**:

- Call services directly.  
- Maintain their own global state.  
- Apply governance logic independently of provided flags and metadata.

---

## 🧪 9. Testing Expectations

Each component (or group of related components) must be covered by:

- Unit tests (render and interaction).  
- A11y checks for core controls and flows.  
- Governance tests (when relevant) to ensure CARE labels and masking indicators appear.  
- Snapshot tests for stable visual primitives, where appropriate.  

Testing requirements follow the patterns defined in:

- `web/src/ARCHITECTURE.md`  
- `.github/ARCHITECTURE.md`  

---

## 🕰 10. Version History

| Version | Date       | Summary                                                                                                  |
|--------:|------------|----------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-30 | Upgraded to KFM-MDP v11.2.2; added telemetry v11 alignment, energy/carbon v2, governance + AI constraints. |
| v10.4.1 | 2025-11-15 | Updated directory structure with labels; aligned MapView, TimelineView, and Focus components.           |
| v10.4.0 | 2025-11-15 | KFM-MDP v10.4 documentation overhaul; expanded governance & A11y requirements.                          |
| v10.3.2 | 2025-11-14 | Map + Story Node + governance updates.                                                                  |
| v10.3.1 | 2025-11-13 | Initial components overview.                                                                            |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
[⬅️ Back to web/src Architecture](../ARCHITECTURE.md) · [🌐 Web Platform Overview](../README.md) · [🛡 Governance](../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
