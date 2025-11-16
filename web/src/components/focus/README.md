---
title: "🎯 Kansas Frontier Matrix — Focus Mode UI Components Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/components/focus/README.md"
version: "v10.4.0"
last_updated: "2025-11-15"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/web-components-focus-v1.json"
governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Component Overview"
intent: "web-components-focus"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Medium (entity-dependent)"
sensitivity_level: "Dataset-dependent"
public_exposure_risk: "Medium"
indigenous_rights_flag: "Conditional"
data_steward: "KFM FAIR+CARE Council"
risk_category: "Mixed"
redaction_required: true
provenance_chain:
  - "web/src/components/focus/README.md@v10.3.2"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E21 Person / E53 Place / E31 Document"
  schema_org: "WebPageElement"
  owl_time: "TemporalEntity"
  prov_o: "prov:Entity"
json_schema_ref: "../../../../schemas/json/web-components-focus-readme.schema.json"
shape_schema_ref: "../../../../schemas/shacl/web-components-focus-readme-shape.ttl"
doc_uuid: "urn:kfm:doc:web-components-focus-readme-v10.4.0"
semantic_document_id: "kfm-doc-web-components-focus-readme"
event_source_id: "ledger:web/src/components/focus/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions (UI-side)"
ai_transform_permissions:
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "summaries"
  - "unverified historical claims"
  - "speculative additions"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "United States / Kansas"
classification: "Public UI Components (governance-aware)"
role: "overview"
lifecycle_stage: "stable"
ttl_policy: "Review each release cycle"
sunset_policy: "Superseded upon next Focus Mode system update"
---

<div align="center">

# 🎯 **Kansas Frontier Matrix — Focus Mode UI Components Overview**  
`web/src/components/focus/README.md`

**Purpose:**  
Document all UI components powering **Focus Mode v2.5**, the entity-centric reasoning system of the  
KFM Web Platform.  
These components display entity narratives, relationships, spatial overlays, provenance, CARE metadata,  
explainability insights, and ethical notices.  
Focus Mode is one of the **highest-governance** areas of the frontend and must be fully FAIR+CARE-aligned.

</div>

---

# 📘 Overview

Focus Mode components:

- Render **entity profiles**  
- Show **narrative explanations** (AI-augmented + clearly labeled)  
- Visualize **entity relationships**  
- Provide **geospatial highlights** on the map  
- Integrate with Story Node v3  
- Display **full governance metadata** (CARE, provenance, licensing)  
- Include explainability (SHAP/LIME) for AI-derived content  
- Trigger telemetry for reasoning journeys  
- Respect all restrictions in `ai_transform_prohibited`  
- Comply with WCAG 2.1 AA for accessible reasoning flows  

Focus Mode is deeply integrated with:

- `focusPipeline.ts`  
- `useFocus.ts`  
- `GovernanceContext.tsx`  
- Story Node & STAC systems  
- Spatial pipelines (highlights, masked geometry)  

---

# 🧱 Directory Structure

~~~text
web/src/components/focus/
├── FocusPanel.tsx                 # Main container for entity-focused reasoning
├── FocusHeader.tsx                # Entity title, type, CARE tag, provenance link
├── FocusSummary.tsx               # Summary section (AI-labeled if applicable)
├── RelatedEntityCard.tsx          # Cards for neighbors in the knowledge graph
├── RelatedEntityList.tsx          # Grouped relations by type (places, events, docs)
├── ExplanationBlock.tsx           # Explainability (SHAP/LIME) representation
├── RelationGraphPreview.tsx       # Mini-graph visualization (non-speculative)
├── StoryNodeSuggestions.tsx       # Story Node v3 recommendations
├── CARENotices.tsx                # Sensitive/sovereignty warnings
├── ProvenanceBar.tsx              # Provenance chain preview
├── SpatialHighlightToggle.tsx     # Toggle to emphasize spatial footprint on map
└── AIGeneratedDisclaimer.tsx      # Banner marking AI-generated segments
~~~

---

# 🧩 Component Responsibilities

## 🧠 **FocusPanel.tsx**
The core of Focus Mode.

Handles:

- Rendering all sub-sections  
- Integrating governance messages  
- Accessible layout & keyboard focus  
- AI narrative labeling  

Telemetry:

- `"focus:open"`  
- `"focus:tab-change"`  
- `"focus:entity-view"`  

Governance:

- Blocks rendering if CARE flags prohibit viewing full detail  
- Triggers masking logic for spatial footprints  

---

## 🏷️ **FocusHeader.tsx**
Displays:

- Entity name & type  
- CAREBadge  
- ProvenanceChip  
- Category icon with A11y labels  
- AI indicator if summary is AI-generated  

Accessibility:

- `<header>` landmark  
- Screen-reader contextual summary  

---

## 📘 **FocusSummary.tsx**
Contains:

- Core entity summary  
- AI output clearly labeled (banner + icon + tooltip)  
- CARE-filtered text (no sensitive claims)  

Rules:

- MUST NOT display unverified historical information  
- Must use plain-language reductions if sensitive fields masked  

---

## 🧩 **RelatedEntityCard/List**
Displays graph neighbors:

- Places  
- Documents  
- Events  
- People  
- Datasets  

Governance:

- May hide or generalize entities if restricted  
- Must annotate sovereign/cultural relationships  

A11y:

- Keyboard-navigable scrolling lists  
- Semantic list structures  

---

## 🤖 **ExplanationBlock.tsx**
Displays explainability insights produced upstream:

- SHAP values  
- Influence features  
- Confidence grades  

Rules:

- Never fabricate explanations  
- Only display values present in validated payloads  
- Use accessible charts (WCAG-compliant colors)  

---

## 🕸️ **RelationGraphPreview.tsx**
Small preview of entity relationships.

Constraints:

- NEVER extrapolate new relationships  
- Only show graph edges returned from API  
- H3-generalized nodes for sensitive areas  

---

## 🧭 **StoryNodeSuggestions.tsx**
Provides:

- List of relevant Story Nodes  
- Previews with time & location  
- Accessible indicators for narrative richness  

Governance:

- Handles Story Node generalization  
- Must show provenance chips  

---

## ⚠️ **CARENotices.tsx**
Displays mandatory notices:

- Sovereignty warnings  
- Cultural protocol notices  
- Ethical usage guidelines  

Must:

- Use readable text  
- Include links to relevant governance docs  
- Appear before sensitive content is shown  

---

## 🧬 **ProvenanceBar.tsx**
Inline bar summarizing:

- Dataset lineage  
- Source → transformation → publication  
- License + rights-holder information  

Connected to `GovernanceContext`.

---

## 🎯 **SpatialHighlightToggle.tsx**
Provides UI switch for turning spatial highlight on/off.

Must:

- Generalize geometry when needed  
- Push telemetry: `"focus:spatial-highlight-toggle"`  
- Use A11y-compliant toggle roles  

---

## 🤖 **AIGeneratedDisclaimer.tsx**
Required banner when:

- Summary  
- Explanation  
- Any content segment  
is derived using AI.

Contains:

- Icon + tool name  
- Confidence note (if provided)  
- Link to provenance sources  

---

# 🔐 Governance Requirements

Focus Mode components MUST:

- Display CARE labels immediately  
- Enforce sovereignty masking  
- Label all AI-generated text  
- Provide provenance trail  
- Remove or generalize sensitive spatial footprints  
- Sound ethical warnings for contextual risk  
- Block rendering if data is not validated  

Governance violations = **CI blocker**.

---

# ♿ Accessibility Requirements (WCAG 2.1 AA)

All components must:

- Use correct landmarks  
- Provide keyboard navigation  
- Include alt text + ARIA  
- Respect reduced-motion  
- Meet color-contrast requirements  
- Announce content changes via screen-reader mechanisms  

A11y violations = **merge blocked**.

---

# 📈 Telemetry Responsibilities

Focus components emit:

- `"focus:open"`  
- `"focus:entity-select"`  
- `"focus:summary-expand"`  
- `"focus:related-click"`  
- `"focus:graph-preview"`  
- `"focus:explanation-view"`  
- `"focus:storynode-suggest"`  
- `"focus:spatial-highlight-toggle"`  

Telemetry must be:

- Non-PII  
- Schema-valid  
- CARE-aware  
- Included in release bundles  

---

# 🧪 Testing Requirements

Tests must cover:

- Component rendering  
- Governance enforcement (CARE/masking)  
- AI-label propagation  
- Story Node + Focus Mode sync  
- Spatial highlight toggling  
- A11y checks  
- Telemetry correctness  
- Narrative segmentation  
- Provenance display  

Locations:

~~~text
tests/unit/web/components/focus/**
tests/integration/web/components/focus/**
~~~

---

# 🕰 Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v10.4.0 | 2025-11-15 | Full rewrite with governance, A11y, Story Node v3, SHAP/LIME explainability integration |
| v10.3.2 | 2025-11-14 | Added Story Node relations + governance UI improvements |
| v10.3.1 | 2025-11-13 | Initial Focus Mode component overview |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
FAIR+CARE Certified · Public Document · Version-Pinned  
Validated under MCP-DL v6.3 & KFM-MDP v10.4  

</div>

