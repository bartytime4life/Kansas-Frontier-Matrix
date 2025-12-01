---
title: "📖 Kansas Frontier Matrix — Story Node UI Components Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/components/story/README.md"
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
telemetry_ref: "../../../../releases/v11.2.2/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/web-components-story-v1.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

status: "Active / Enforced"
status_category: "Overview"
doc_kind: "Component Overview"
intent: "web-components-story"
role: "overview"

fair_category: "F1-A1-I1-R1"
care_label: "Public / Variable (Story-dependent)"
sensitivity_level: "Dataset-dependent"
public_exposure_risk: "Medium"
indigenous_rights_flag: "Conditional"
data_steward: "KFM FAIR+CARE Council"
risk_category: "Mixed"
redaction_required: true

provenance_chain:
  - "web/src/components/story/README.md@v10.3.2"
  - "web/src/components/story/README.md@v10.4.0"

ontology_alignment:
  cidoc: "E31 Document / E53 Place / E52 Time-Span"
  schema_org: "CreativeWork"
  owl_time: "TemporalEntity"
  geosparql: "geo:Feature"
  prov_o: "prov:Entity"

json_schema_ref: "../../../../schemas/json/web-components-story-readme.schema.json"
shape_schema_ref: "../../../../schemas/shacl/web-components-story-readme-shape.ttl"

doc_uuid: "urn:kfm:doc:web-components-story-readme-v11.2.2"
semantic_document_id: "kfm-doc-web-components-story-readme"
event_source_id: "ledger:web/src/components/story/README.md"
immutability_status: "version-pinned"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with constraints"
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
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "United States / Kansas"
classification: "Public UI Components (with CARE exceptions)"

ttl_policy: "Review every major release"
sunset_policy: "Superseded upon Story Node v4 upgrade"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Structure"
    - "🧩 Component Responsibilities"
    - "⚖️ Governance & FAIR+CARE Integration"
    - "♿ Accessibility Requirements (WCAG 2.1 AA+)"
    - "📈 Telemetry Responsibilities"
    - "🧪 Testing Requirements"
    - "🕰 Version History"
    - "⚖️ Footer"
---

<div align="center">

# 📖 **Kansas Frontier Matrix — Story Node UI Components Overview (v11.2.2)**  
`web/src/components/story/README.md`

**Purpose**  
Describe the complete suite of **Story Node v3 UI components**, which render narrative units  
combining text, time, place, provenance, media, geospatial footprints, and governance metadata.  
Story Node components must be **ethically governed**, **WCAG-compliant**, and fully integrated  
with Focus Mode v3, Timeline, STAC/DCAT data, and mapping pipelines.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)]()  
[![KFM-MDP v11.2.2](https://img.shields.io/badge/KFM%E2%80%93MDP-v11.2.2-purple)]()  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Story%20Dependent-gold)]()  
[![WCAG AA+](https://img.shields.io/badge/A11y-WCAG%202.1%20AA%2B-brightgreen)]()

</div>

---

## 📘 Overview

Story Node components:

- Render structured narratives (Story Node v3).  
- Display spatial footprints (generalized / masked when required).  
- Integrate with Focus Mode v3 and Timeline.  
- Surface provenance metadata (source → rights-holder → transformation).  
- Show CARE labels and sovereignty warnings.  
- Provide accessible, ethical UI for historical/cultural content.  
- Annotate any AI-generated text clearly and visibly.  
- Sync with map highlight layers (2D + 3D).  
- Emit telemetry for narrative engagement and governance events.  

These components must **never**:

- Invent historical claims or entities.  
- Show exact restricted coordinates.  
- Collapse or hide governance metadata.  
- Display unmasked archaeological/sacred sites.  
- Override backend governance / sovereignty rules.

---

## 🗂️ Directory Structure

~~~text
web/src/components/story/
│
├── 📘 StoryCard.tsx           # Compact Story Node summary card
├── 📖 StoryDetail.tsx         # Full narrative view with media + provenance
├── 🖼️ StoryMedia.tsx          # Media carousel (images, scans, maps)
├── 🗺️ StoryMapPreview.tsx     # Mini-map with generalized footprint
├── 🔗 StoryRelations.tsx      # Related entities (places, events, docs, datasets)
├── 🕰️ StoryTimeline.tsx       # Optional temporal visualization block
├── 🧬 StoryProvenance.tsx     # PROV-O aligned provenance information
└── ⚠️ StoryCareBlock.tsx      # CARE + sovereignty + ethics warning section
~~~

All new Story Node UI components must be added under this directory, with this README updated accordingly.

---

## 🧩 Component Responsibilities

### 📘 StoryCard.tsx

**Purpose**

- Display a concise, clickable summary of a Story Node.

**Content**

- Title + short summary.  
- CARE badge / sovereignty indicator (if present).  
- Time span label (e.g., “ca. 1450–1650 CE”).  
- Generalized location label (region, watershed, county, etc.).  
- ProvenanceChip (e.g., archive / collection / dataset).  

**Accessibility**

- Proper heading level within card grid/list.  
- Keyboard-selectable card (Enter/Space).  
- High-contrast tokens; no color-only state.  

**Telemetry**

- `story:card-open` (via parent wiring) when activated (non-PII, schema-compliant).

---

### 📖 StoryDetail.tsx

**Purpose**

- Render a full, scrollable Story Node view.

**Contains**

- Narrative sections (archival text + AI summaries, clearly labeled).  
- `StoryProvenance` section.  
- `StoryCareBlock` section (when required).  
- `StoryMapPreview` (generalized geometry).  
- `StoryRelations` (related entities).  
- `StoryMedia` (if safe and allowed).  
- Optional `StoryTimeline` mini-view.  

**Governance**

- MUST label AI-generated narrative segments.  
- MUST show provenance for major claims (source references).  
- MUST omit, blur, or generalize sensitive content per governance metadata.  

**Accessibility**

- Semantic headings and section landmarks.  
- Focusable headings/sections for keyboard navigation.  

---

### 🖼️ StoryMedia.tsx

**Purpose**

- Present media assets attached to a Story Node.

**Supported Media**

- Scans (documents, maps).  
- Photos.  
- Historical map tiles or thumbnails.  

**Rules**

- Must display metadata + rights-holder/licensing.  
- Sensitive or sacred content must be masked or replaced with a redaction message.  
- Zoom and carousel behavior must respect reduced-motion and A11y settings.  

**Telemetry**

- `story:media-view` with media-type + Story Node identifier (non-PII).

---

### 🗺️ StoryMapPreview.tsx

**Purpose**

- Display a **safe**, **generalized** spatial preview of the Story Node.

**Behavior**

- Uses generalized geometry when required (H3, county, region).  
- Shows “location generalized / masking applied” indicators.  
- Optionally animates footprint highlight in sync with Timeline & MapContext.  

**Governance**

- Must **never** expose precise coordinates for sensitive/sovereign nodes.  
- Must read masking flags from governance metadata and display appropriate UI.  

**Telemetry**

- `story:map-preview` interaction events (e.g., hover, click through).

---

### 🔗 StoryRelations.tsx

**Purpose**

- Render related entities and resources:

  - Places  
  - Events  
  - People  
  - Datasets  
  - Other Story Nodes  

**Rules**

- Relations MUST reflect the knowledge graph; no client-side guesses.  
- Sensitive entities must be flagged or masked according to governance metadata.  
- All relation items must be keyboard-accessible and screen-reader-friendly.  

**Telemetry**

- `story:relation-click` when users navigate via relations.

---

### 🕰️ StoryTimeline.tsx

**Purpose**

- Display a mini-timeline for the Story Node’s temporal span.

**Behavior**

- OWL-Time-aligned representation of time span / fuzzy dates.  
- Indicates uncertainty explicitly (“ca.”, “before”, “after”).  
- Uses high-contrast visuals and respects reduced-motion settings.  

**Telemetry**

- `story:timeline-hover` / `story:timeline-scrub` for engagement metrics.

---

### 🧬 StoryProvenance.tsx

**Purpose**

- Provide a clear, visual view into the Story Node’s provenance chain.

**Content**

- Sources (documents, datasets, archives).  
- Transformations (e.g., digitization, georeferencing, modeling).  
- Rights-holders and licenses.  
- Links to SBOM/manifests when relevant.  

**Requirements**

- Map to PROV-O (`prov:Entity`, `prov:Activity`, `prov:Agent`).  
- Offer optional JSON-LD export/download triggers (via parent wiring).  

**Telemetry**

- `story:provenance-expanded` when the user opens or expands provenance.

---

### ⚠️ StoryCareBlock.tsx

**Purpose**

- Render mandatory ethical and governance context **before** sensitive content.

**Content**

- CARE label + explanation.  
- Sovereignty warnings and data ownership notes.  
- Cultural sensitivity and usage guidance.  
- Explanation of masking/generalization choices.  
- Links to FAIR+CARE and sovereignty policies.  

**Behavior**

- Must be displayed prominently for Story Nodes flagged as sensitive or sovereign.  

**Telemetry**

- `story:care-warning-shown` when displayed.

---

## ⚖️ Governance & FAIR+CARE Integration

All Story Node UI components must:

- Enforce CARE and sovereignty flags passed from upstream.  
- Display provenance chips/trails in all relevant views.  
- Correctly generalize or omit sensitive spatial and media content.  
- Label AI-generated text and never fabricate or speculate beyond data.  
- Respect backend decisions on what may or may not be publicly rendered.  

They must **never**:

- Show unmasked coordinates for protected sites.  
- Remove or hide governance metadata (CARE, sovereignty, lineage).  
- Merge or split Story Nodes in the UI in a way that contradicts the underlying graph.

Governance regressions are treated as **CI hard failures** and must block merges.

---

## ♿ Accessibility Requirements (WCAG 2.1 AA+)

Each Story Node component must:

- Use semantic HTML elements and headings.  
- Provide alt text / SR descriptions for images and maps.  
- Support keyboard navigation and logical focus order.  
- Respect reduced-motion settings for animations.  
- Provide descriptive labels for temporal and spatial information.  
- Ensure visible focus indicators and color-contrast ≥ AA thresholds.  

WCAG 2.1 AA+ conformance is mandatory for all Story UI components; any regression blocks merges.

---

## 📈 Telemetry Responsibilities

Story Node components must support emission of (via parent wiring):

- `story:open`  
- `story:card-open`  
- `story:media-view`  
- `story:relation-click`  
- `story:timeline-hover` / `story:timeline-scrub`  
- `story:map-preview`  
- `story:care-warning-shown`  
- `story:provenance-expanded`  

Telemetry MUST:

- Be non-PII and aggregated where possible.  
- Conform to `telemetry_schema`.  
- Be CARE-aware (e.g., mark interactions with sensitive Story Nodes).  
- Be included in release telemetry bundles referenced by `telemetry_ref`.

---

## 🧪 Testing Requirements

Each Story Node component MUST be covered by:

- **Unit tests**  
  - Rendering states and prop combinations  
  - Governance flags (e.g., redaction_required, sovereignty)  

- **Integration tests**  
  - Interactions with MapView and TimelineView where applicable  
  - Focus Mode integration (Story-focused views)  

- **Accessibility tests**  
  - ARIA roles / labels  
  - Keyboard navigation across sections and media  
  - Contrast and reduced-motion behavior  

- **Governance tests**  
  - Masking behavior for sensitive spatial or media content  
  - CARE block visibility when expected  

- **Telemetry tests**  
  - Event emission for key user actions  

Recommended test locations:

~~~text
tests/unit/web/components/story/**
tests/integration/web/components/story/**
~~~

---

## 🕰 Version History

| Version | Date       | Summary                                                                                              |
|--------:|------------|------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-30 | Upgraded to KFM-MDP v11.2.2; aligned AI constraints, telemetry v11, energy/carbon v2, governance hooks. |
| v10.4.0 | 2025-11-15 | Full Story Node v3 UI rewrite under KFM-MDP v10.4; added CARE, provenance, AI labeling rules.       |
| v10.3.2 | 2025-11-14 | Improved spatial previews + relations layout.                                                        |

---

## ⚖️ Footer

<div align="center">

**📚 Governance Links**  
[Docs Root](../../../../README.md) •  
[Standards Index](../../../../docs/standards/INDEX.md) •  
[Governance Charter](../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

**🔐 Compliance:**  
FAIR+CARE · CIDOC-CRM · OWL-Time · GeoSPARQL · PROV-O · WCAG 2.1 AA+ · SLSA Level 3

**End of Document**

</div>