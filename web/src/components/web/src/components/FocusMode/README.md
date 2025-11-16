---
title: "🎯 Kansas Frontier Matrix — FocusMode Component Suite Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/components/FocusMode/README.md"
version: "v10.4.0"
last_updated: "2025-11-15"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/web-components-focusmode-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Component Overview"
intent: "web-components-focusmode"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Medium (entity-dependent)"
sensitivity_level: "Dataset-dependent"
public_exposure_risk: "Medium"
indigenous_rights_flag: "Conditional"
data_steward: "KFM FAIR+CARE Council"
risk_category: "Mixed"
redaction_required: true
provenance_chain:
  - "web/src/components/FocusMode/README.md@v10.3.2"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E21 Person / E53 Place / E31 Document"
  schema_org: "CreativeWork"
  owl_time: "TemporalEntity"
  prov_o: "prov:Entity"
json_schema_ref: "../../../../../schemas/json/web-components-focusmode-readme.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/web-components-focusmode-readme-shape.ttl"
doc_uuid: "urn:kfm:doc:web-components-focusmode-readme-v10.4.0"
semantic_document_id: "kfm-doc-web-components-focusmode-readme"
event_source_id: "ledger:web/src/components/FocusMode/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with hard ethical boundaries"
ai_transform_permissions:
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "unverified historical claims"
  - "speculative additions"
  - "narrative inventions"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "United States / Kansas"
classification: "Public (governance-restricted content)"
role: "overview"
lifecycle_stage: "stable"
ttl_policy: "Review each release cycle"
sunset_policy: "Superseded upon Focus Mode v3 release"
---

<div align="center">

# 🎯 **Kansas Frontier Matrix — FocusMode Component Suite Overview**  
`web/src/components/FocusMode/README.md`

**Purpose:**  
Provide a comprehensive, standard-aligned overview of the **FocusMode component suite** — the UI engine that powers  
entity-centric reasoning in the Kansas Frontier Matrix (KFM).  
FocusMode integrates AI-labeled narratives, Story Node v3 context, geospatial highlights, governance metadata,  
provenance lineage, and timeline/map synchronization.

</div>

---

# 📘 Overview

Components in this directory implement the **full Focus Mode v2.5 UI experience**, enabling users to:

- Explore an entity in depth  
- Read narrative + contextual information  
- Understand entity relationships  
- View explainability (SHAP/LIME) blocks  
- Access provenance & CARE indicators  
- Highlight entity footprints on maps  
- Navigate related Story Nodes  
- Receive ethical warnings and sovereignty notices  

These components must be:

- **FAIR+CARE-governed**  
- **WCAG AA accessible**  
- **Provenance-correct**  
- **Generalization-safe** (H3 masking for spatial info)  
- **Deterministic + schema-validated**  
- **Non-speculative**  

---

# 🧱 Directory Structure

~~~text
web/src/components/FocusMode/
├── FocusContainer.tsx            # Top-level region for Focus Mode UI
├── FocusHeader.tsx               # Entity header w/ CARE + provenance labels
├── FocusSummary.tsx              # Summary section (AI-labeled when applicable)
├── FocusTabs.tsx                 # Tabbed navigation (Overview / Relations / Spatial / Provenance)
├── RelationsPanel.tsx            # Related entity list (places, events, artifacts)
├── RelationCard.tsx              # Single related entity card
├── NarrativeSection.tsx          # Narrative + AI disclaimers + CARE filtering
├── ExplainabilitySection.tsx     # SHAP/LIME blocks
├── SpatialPanel.tsx              # Spatial footprint preview + highlight controls
├── ProvenancePanel.tsx           # Full provenance chain
└── WarningsPanel.tsx             # CARE, sovereignty, redaction, ethical notices
~~~

---

# 🧩 Component Responsibilities

## 🧠 **FocusContainer.tsx**
- Manages layout + top-level interactions  
- Orchestrates tab switching  
- Propagates governance warnings  
- Triggers telemetry: `"focus:open"`  

Governance:
- MUST NOT render if CARE prohibits viewing detail  
- Must display redaction/sovereignty notices up front  

---

## 🏷️ **FocusHeader.tsx**
Displays:

- Entity name, type  
- CAREBadge  
- ProvenanceChip  
- AIGeneratedTag if summary includes AI text  

A11y:
- `<header>` landmark  
- Screen-reader summary  

---

## 📘 **FocusSummary.tsx**
Includes:

- Overview text  
- AI-labeled narrative (with a disclaimer)  
- CARE-filtered fields  

Governance:
- Must remove sensitive content  
- No invented historical claims  

Telemetry:
- `"focus:summary-expand"`  

---

## 🗂️ **FocusTabs.tsx**
Sections:

- Overview  
- Relationships  
- Spatial  
- Provenance  

Accessibility:

- ARIA tablist  
- Keyboard navigation  

Telemetry:
- `"focus:tab-change"`  

---

## 🔗 **RelationsPanel.tsx + RelationCard.tsx**
Displays related entities:

- People  
- Events  
- Locations  
- Documents  
- Story Nodes  

Governance:

- Mask or hide sensitive relations  
- Label sovereignty-controlled connections  

Telemetry:

- `"focus:relation-select"`  

---

## 📜 **NarrativeSection.tsx**
Renders longer narrative text:

- AI-generated elements clearly marked  
- Provenance chips in-line  
- CARE warnings where data is sensitive  

Must:

- Avoid any inference not returned from backend  
- Be screen-reader friendly  

---

## 🤖 **ExplainabilitySection.tsx**
Shows:

- SHAP values  
- Influence features  
- Narrative explanation generation metadata  

Rules:

- Values MUST come from validated payloads  
- No fabricated explanations  

Telemetry:
- `"focus:explanation-view"`  

---

## 🗺️ **SpatialPanel.tsx**
Displays spatial context:

- Generalized footprints  
- Masking indicators  
- “Highlight on map” toggle  

Governance:

- H3 r7+ mandatory masking  
- Never expose raw geometry  
- Always show sovereignty + CARE labels  

Telemetry:

- `"focus:spatial-highlight-toggle"`  

---

## 🧬 **ProvenancePanel.tsx**
Renders:

- Full PROV-O lineage  
- Source → transformation → derived entity  
- License + rights-holder metadata  
- SBOM + manifest links  

---

## ⚠️ **WarningsPanel.tsx**
Shows required ethical content:

- Cultural sensitivity warnings  
- Indigenous sovereignty statements  
- Redaction reasons  
- AI content disclaimers  

This panel **must appear before** sensitive content.

---

# 🔐 Governance Requirements

FocusMode components must:

- Enforce CARE classification  
- Display sovereignty warnings prominently  
- Mask sensitive spatial/temporal content  
- Label AI-generated text  
- Show provenance chips consistently  
- Block rendering when governance restrictions apply  
- Avoid speculative or unverified content  

Governance failure = **CI BLOCK**.

---

# ♿ Accessibility Requirements (WCAG 2.1 AA)

FocusMode UI must:

- Provide structured headings  
- Use semantic regions (`<header>`, `<main>`, `<aside>`)  
- Support keyboard-only use  
- Include strong focus indicators  
- Respect reduced-motion  
- Provide alt-text + ARIA labels  
- Avoid color-only distinctions  

A11y issues block merges.

---

# 📈 Telemetry Responsibilities

Components emit:

- `"focus:open"`  
- `"focus:entity-select"`  
- `"focus:summary-expand"`  
- `"focus:relation-select"`  
- `"focus:explanation-view"`  
- `"focus:spatial-highlight-toggle"`  
- `"focus:provenance-expand"`  
- `"focus:care-warning"`  

Telemetry MUST be:

- Schema-valid  
- Non-PII  
- CARE-aware  
- Added to release bundle  

---

# 🧪 Testing Requirements

Tests must validate:

- A11y  
- Governance enforcement  
- Provenance correctness  
- Masking & spatial generalization  
- AI labeling  
- Telemetry emission  
- Timeline/map sync  

Location:

~~~text
tests/unit/web/components/FocusMode/**
tests/integration/web/components/FocusMode/**
~~~

---

# 🕰 Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v10.4.0 | 2025-11-15 | Full FocusMode v2.5 UI documentation; governance, A11y, temporal + spatial integration |
| v10.3.2 | 2025-11-14 | Added explainability + sovereignty warnings |
| v10.3.1 | 2025-11-13 | Initial FocusMode component overview |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
FAIR+CARE Certified · Public Document · Version-Pinned  
Validated under MCP-DL v6.3 & KFM-MDP v10.4  

</div>

