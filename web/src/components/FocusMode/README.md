---
title: "🎯 Kansas Frontier Matrix — FocusMode Component Suite Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/components/FocusMode/README.md"
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
telemetry_ref: "../../../../../releases/v11.2.2/web-focusmode-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/web-components-focusmode-v2.json"
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
classification: "Public (governance-restricted content)"
jurisdiction: "United States / Kansas"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

status: "Active / Enforced"
doc_kind: "Component Overview"
intent: "frontend-focusmode"
semantic_intent:
  - "UI-component"
  - "focus-mode"
  - "contextual-exploration"
  - "governance-ui"
  - "provenance-ui"

fair_category: "F1-A1-I1-R1"
care_label: "Public / Medium (entity-dependent)"
sensitivity_level: "Dataset-dependent"
public_exposure_risk: "Medium"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"
risk_category: "Mixed"
redaction_required: true

provenance_chain:
  - "web/src/components/FocusMode/README.md@v10.4.0"
  - "web/src/components/FocusMode/README.md@v10.3.2"

ontology_alignment:
  cidoc: "E21 Person / E53 Place / E31 Document"
  schema_org: "CreativeWork"
  owl_time: "TemporalEntity"
  prov_o: "prov:Entity"

json_schema_ref: "../../../../../schemas/json/web-components-focusmode-readme-v11.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/web-components-focusmode-readme-v11-shape.ttl"
doc_uuid: "urn:kfm:doc:web-components-focusmode-readme-v11.2.2"
semantic_document_id: "kfm-doc-web-components-focusmode-readme-v11"
event_source_id: "ledger:web/src/components/FocusMode/README.md"
immutability_status: "version-pinned"

ai_training_inclusion: false
ai_focusmode_usage: "Core feature with hard ethical boundaries"
ai_transform_permissions:
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "diagram-extraction"
ai_transform_prohibited:
  - "unverified-historical-claims"
  - "speculative-additions"
  - "narrative-inventions"

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

# 🎯 **Kansas Frontier Matrix — FocusMode Component Suite Overview**  
`web/src/components/FocusMode/README.md`

**Purpose:**  
Define the **FocusMode v3** UI component suite — the entity-centric exploration engine of Kansas Frontier Matrix v11.  
FocusMode binds AI-assisted narratives, Story Node v3 context, geospatial highlights, governance metadata,  
provenance lineage, and timeline/map synchronization into a single, governed experience.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)]()  
[![KFM-MDP v11.2.2](https://img.shields.io/badge/KFM%E2%80%93MDP-v11.2.2-purple)]()  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Enforced-gold)]()  
[![WCAG AA+](https://img.shields.io/badge/A11y-WCAG%202.1%20AA%2B-brightgreen)]()

</div>

---

## 📘 Overview

FocusMode v3 enables users to:

- Explore a **focus entity** (Person, Place, Event, Story Node, Dataset) in depth  
- Read curated + AI-labeled narratives (clearly tagged and provenance-backed)  
- Inspect relationships (related places, events, documents, Story Nodes)  
- See explainability (SHAP/LIME-like summary blocks) for AI-driven views  
- View governance context, CARE labels, sovereignty markers, and redaction reasons  
- Highlight focus footprints on the map and align the timeline to relevant intervals  
- Navigate to related entities without losing focus context  

Every FocusMode component must be:

- **FAIR+CARE-governed**  
- **WCAG 2.1 AA+ accessible**  
- **Provenance-correct** (no invented lineage)  
- **Generalization-safe** (H3 masking for spatial info where required)  
- **Deterministic & schema-validated**  
- **Non-speculative** — no narrative or relationship beyond what the backend provides  

---

## 🗂️ Directory Structure

~~~text
web/src/components/FocusMode/
│
├── 🎯 FocusContainer.tsx            # Top-level Focus Mode UI container (layout + orchestration)
├── 🏷️ FocusHeader.tsx               # Entity header with CARE + provenance labels
├── 📘 FocusSummary.tsx              # Overview summary (AI-labeled where applicable)
├── 🗂️ FocusTabs.tsx                 # Tabbed navigation (Overview / Relations / Spatial / Provenance / Explainability)
├── 🔗 RelationsPanel.tsx            # Related entities (people, events, places, docs, Story Nodes)
├── 📇 RelationCard.tsx              # Single related entity card component
├── 📜 NarrativeSection.tsx          # Narrative text section with AI disclaimers & CARE filtering
├── 🤖 ExplainabilitySection.tsx     # SHAP/LIME-like blocks and explanation UI
├── 🗺️ SpatialPanel.tsx              # Spatial footprint preview + “highlight on map” controls
├── 🧬 ProvenancePanel.tsx           # Full PROV-O lineage and dataset/document provenance
├── ⚠️ WarningsPanel.tsx             # CARE, sovereignty, redaction, and AI disclaimers
└── ♿ FocusA11yHelpers.tsx          # A11y helpers (ARIA, focus management, announcements)
~~~

Any additions/renames MUST be reflected here.

---

## 🧩 Component Responsibilities

### 🎯 FocusContainer.tsx

**Role:**  
Top-level orchestrator for Focus Mode UI.

**Responsibilities:**

- Layout and composition of header, summary, tabs, and panels  
- open/close lifecycle handling (if presented as a distinct region/drawer)  
- Manage selected focus entity + tab state  
- Inject governance, CARE, and A11y context into children  
- Synchronize with:
  - timeline (scroll/zoom around entity interval)  
  - map (highlight focus geometry when allowed)  

**Governance:**

- MUST NOT render full Focus UI if CARE/sovereignty rules prohibit showing details  
- MUST show WarningsPanel before sensitive content when `redaction_required = true`  

**Telemetry:**

- `"focus:open"` when FocusMode is activated  
- `"focus:entity-select"` when focus target changes  

---

### 🏷️ FocusHeader.tsx

**Role:**  
Top header region for the focus entity.

**Displays:**

- Entity name (preferred label)  
- Entity type (Person / Place / Event / Story Node / Dataset / Other)  
- CAREBadge (classification)  
- Provenance chip (summary of roots of entity)  
- Optional AIGeneratedTag if summary includes AI text  

**Accessibility:**

- Uses `<header>` in focus context  
- Provides title used by `aria-labelledby` on surrounding container  
- Close/back controls are keyboard reachable and labeled  

---

### 📘 FocusSummary.tsx

**Role:**  
High-level summary and narrative entry point.

**Content:**

- Overview description (from graph + Story Nodes)  
- AI-generated text clearly labeled as AI and constrained to backend-provided facts  
- CARE-filtered fields (no sensitive details shown here)

**Governance:**

- No invented historical claims; only uses data already in graph / Story Nodes / backend  
- Sensitive content must be elided or generalized with note/tooltip  

**Telemetry:**

- `"focus:summary-expand"` when user expands or interacts with extended summary text  

---

### 🗂️ FocusTabs.tsx

**Role:**  
Tabbed navigation for Focus Mode.

**Tabs (typical):**

- Overview  
- Relations  
- Spatial  
- Provenance  
- Explainability  

**Accessibility:**

- Uses ARIA `tablist`, `tab`, `tabpanel` roles  
- Keyboard controls: arrow keys move between tabs; tab/shift-tab interacts with panels  

**Telemetry:**

- `"focus:tab-change"` with tab identifier  

---

### 🔗 RelationsPanel.tsx & 📇 RelationCard.tsx

**Role:**  
Surfacing nearby graph context for the focus entity.

**RelationsPanel.tsx:**

- Lists graph neighbors grouped by type:
  - People (E21)  
  - Places (E53)  
  - Events (E5)  
  - Documents (E31)  
  - Story Nodes (story-node entities)  
- Provides filtering and sorting (e.g., by time, type, distance)

**RelationCard.tsx:**

- Displays single related entity summary:
  - title  
  - type  
  - short description  
  - CARE classification  

**Governance:**

- Sensitive relations (e.g., to restricted sacred places) must be masked or hidden  
- Sovereignty-controlled relations labeled clearly  

**Telemetry:**

- `"focus:relation-select"` when user selects a related entity  

---

### 📜 NarrativeSection.tsx

**Role:**  
Longer narrative and contextual text region.

**Content:**

- Story Node excerpts  
- AI-augmented narrative, **clearly marked** as AI-derived  
- Inline provenance chips referencing documents/events used  

**Rules:**

- No inference beyond backend outputs: strictly render given narrative content  
- CARE filtering and sovereignty warnings must appear above any sensitive narrative  

**Accessibility:**

- Structured headings and paragraphs; no giant unlabeled wall of text  
- SR-only context for each major narrative block  

---

### 🤖 ExplainabilitySection.tsx

**Role:**  
Explainability UI for Focus Mode AI behavior.

**Displays (depending on backend payload):**

- SHAP/LIME summary bars for features influencing ranking/selection  
- Signature of model used (ID/version)  
- Text explanation of how the AI combined evidence  
- Link to model card and experiment logs (MCP)

**Governance:**

- All values MUST come from validated backend payloads; nothing fabricated in UI  
- Make clear that this is an *explanation of model behavior*, not additional historical evidence  

**Telemetry:**

- `"focus:explanation-view"` when user opens/expands explainability UI  

---

### 🗺️ SpatialPanel.tsx

**Role:**  
Spatial view for the focus entity.

**Functions:**

- Show generalized location (H3-based) for Places and Events  
- Provide “Highlight on map” toggle, integrated with main MapView  
- Display textual explanation of any generalization/masking  

**Governance:**

- H3 r7+ (or coarser) generalization enforced for sensitive / sovereignty-controlled features  
- No direct rendering of raw WKT/GeoJSON from protected layers  
- Must show masking/generalization notices when applied  

**Telemetry:**

- `"focus:spatial-highlight-toggle"` when user toggles map highlight  

---

### 🧬 ProvenancePanel.tsx

**Role:**  
Entity provenance and lineage front-end.

**Displays:**

- PROV-O chain:
  - source entities (archives, sensors, datasets)  
  - activities (ETL, AI transforms)  
  - agents (institutions, pipeline code)  
- Links to:
  - SBOM references  
  - manifest references  
  - dataset-level STAC/DCAT records  

**Rules:**

- No invented lineage; all entries must map to known graph/metadata nodes  
- Provide JSON-LD/PROV download for auditing  

**Telemetry:**

- `"focus:provenance-expand"` when user opens/expands provenance panel  

---

### ⚠️ WarningsPanel.tsx

**Role:**  
Ethical, CARE, and sovereignty warnings.

**Responsibilities:**

- Present:
  - Indigenous sovereignty statements  
  - Cultural sensitivity and sacred site warnings  
  - Explanation of redaction and generalization  
  - AI-narrative disclaimers and limitations  

- MUST appear *before* or alongside any sensitive content panel.

**Telemetry:**

- `"focus:care-warning"` when accessed or acknowledged  

---

### ♿ FocusA11yHelpers.tsx

**Role:**  
Centralized accessibility utilities for Focus Mode.

**Provides:**

- ARIA role/label helpers for Focus container, tabs, panels  
- Focus management utilities for multi-panel environment  
- Screen-reader announcements for focus changes, warnings, and explainability toggles  
- Reduced-motion behavior toggles  

**Requirement:**  
All FocusMode components must rely on this helper module for consistent A11y behaviors.

---

## 🔐 Governance & FAIR+CARE Integration

FocusMode v3 is one of the most sensitive UI surfaces; it MUST:

- Enforce CARE and sovereignty constraints on:
  - narratives  
  - relations  
  - spatial previews  
  - temporal details  
- Provide visible and SR-accessible warnings when content is:
  - generalized  
  - masked  
  - unavailable due to governance  
- Label any AI-generated content as such with link(s) to underlying data and models  
- Avoid speculation / “filling in blanks” — front-end **only** renders facts and narrative supplied by backend/graph  

No governance shortcutting. Violations are **hard CI blockers**.

---

## ♿ Accessibility Requirements (WCAG 2.1 AA+)

FocusMode v3 MUST:

- Use semantic regions (`<header>`, `<main>`, `<section>`, `<aside>`)  
- Provide ARIA-compliant tabs and panels  
- Allow full keyboard-only operation:
  - Accessing all tabs and sections  
  - Activating actions in each panel  
- Maintain visible focus indicators  
- Respect `prefers-reduced-motion` (no forced animations)  
- Avoid color-only semantics; pair color with icons or text  
- Provide adequate labels and descriptions for:
  - explainability charts  
  - spatial previews  
  - warnings  

Accessibility regressions block merges.

---

## 📈 Telemetry Responsibilities

FocusMode components MUST emit:

- `"focus:open"`  
- `"focus:entity-select"`  
- `"focus:summary-expand"`  
- `"focus:tab-change"`  
- `"focus:relation-select"`  
- `"focus:explanation-view"`  
- `"focus:spatial-highlight-toggle"`  
- `"focus:provenance-expand"`  
- `"focus:care-warning"`  

Telemetry MUST:

- Conform to `telemetry_schema`  
- Exclude PII  
- Include governance context where relevant (e.g., which CARE state triggered warnings)  
- Be versioned along with component version for auditability  

---

## 🧪 Testing Requirements

Tests MUST cover:

- **Unit**:
  - Each subcomponent renders with expected props and governance flags  
  - AI-labeling state toggles (e.g., AIGeneratedTag visibility)  

- **Integration**:
  - FocusContainer with Story Nodes and dataset contexts  
  - Tab navigation + content loading  
  - Map + timeline integration (when focus selects or toggles SpatialPanel)  

- **Governance**:
  - Sovereignty + CARE enforcement  
  - Redaction & generalization in spatial/temporal views  
  - AI narrative labeling present and correct  

- **Accessibility**:
  - Keyboard-only navigation through tabs and panels  
  - Correct ARIA attributes on tablist/tabpanel  
  - Screen-reader readability of warnings & narratives  

- **Telemetry**:
  - All events emitted with expected structure and values  

Test directory layout:

~~~text
tests/unit/web/components/FocusMode/**
tests/integration/web/components/FocusMode/**
~~~

---

## 🕰 Version History

| Version | Date       | Summary                                                       |
|--------:|------------|---------------------------------------------------------------|
| v11.2.2 | 2025-11-30 | Upgraded to v11.2.2 standards; governance, A11y, telemetry v2 |
| v10.4.0 | 2025-11-15 | Full FocusMode v2.5 documentation; governance + A11y + expl. |
| v10.3.2 | 2025-11-14 | Added explainability + sovereignty warnings                   |
| v10.3.1 | 2025-11-13 | Initial FocusMode component overview                         |

---

## ⚖️ Footer

<div align="center">

**📚 Governance Links**  
[Docs Root](../../../../../README.md) •  
[Standards Index](../../../../../docs/standards/INDEX.md) •  
[Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

**🔐 Compliance:**  
FAIR+CARE · CIDOC-CRM · OWL-Time · STAC/DCAT · PROV-O · WCAG 2.1 AA+ · SLSA Level 3

**End of Document**

</div>