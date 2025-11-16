---
title: "🎨 Kansas Frontier Matrix — Focus Mode UI Components Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/features/focus-mode/components/README.md"
version: "v10.4.0"
last_updated: "2025-11-15"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/web-feature-focusmode-components-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.1"
status: "Active / Enforced"
doc_kind: "UI Components"
intent: "focus-mode-components"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Entity-Dependent"
sensitivity_level: "Medium"
public_exposure_risk: "Low–Medium"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"
risk_category: "Medium"
redaction_required: true
provenance_chain:
  - "web/src/features/focus-mode/components/README.md@v10.3.2"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E28 Conceptual Object"
  schema_org: "WebPageElement"
  owl_time: "TemporalEntity"
  prov_o: "prov:Entity"
json_schema_ref: "../../../../../schemas/json/web-feature-focusmode-components.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/web-feature-focusmode-components-shape.ttl"
doc_uuid: "urn:kfm:doc:web-feature-focusmode-components-v10.4.0"
semantic_document_id: "kfm-doc-web-feature-focusmode-components"
event_source_id: "ledger:web/src/features/focus-mode/components/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "a11y-adaptations"
  - "semantic-highlighting"
ai_transform_prohibited:
  - "speculative expansions"
  - "unverified historical claims"
  - "inferred relationships"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "United States / Kansas"
classification: "Public Document"
role: "components-index"
lifecycle_stage: "stable"
ttl_policy: "Annual Review"
sunset_policy: "Superseded upon Focus Mode v3 UI overhaul"
---

<div align="center">

# 🎨 **Kansas Frontier Matrix — Focus Mode UI Components Overview**  
`web/src/features/focus-mode/components/README.md`

**Purpose:**  
Document all **UI-level React components** used by Focus Mode v2.5.  
These UI components live in **`web/src/components/FocusMode/**`** and are imported here  
by the feature layer.  
This README functions as an **index + mapping layer**, describing how Focus Mode’s  
presentational components integrate with feature logic, pipelines, and view-models.

</div>

---

# 📘 Overview

Focus Mode UI components:

- Render the **visual interface** for entity-centric exploration  
- Display narrative, spatial, temporal, relational, and provenance information  
- Enforce presentation-level FAIR+CARE UI patterns  
- Consume view-models from `view-models/**`  
- Consume state from `state/**`  
- Are driven by hooks from `hooks/**`  
- Must remain **pure** (no pipeline logic, no data fetching)  
- Must remain **WCAG 2.1 AA compliant**  
- Must integrate with MapView/TimelineView highlight layers  

Focus Mode is one of the **heaviest governance surfaces** in the entire KFM UI —  
UI components here must never hide, distort, or imply meaning beyond what is provided  
by governance and pipeline layers.

---

# 🧱 Directory Structure (Feature Layer)

*Focus Mode UI components live in `web/src/components/FocusMode/**`.  
This directory contains the documentation and import surface.*

~~~text
web/src/features/focus-mode/components/
└── README.md   # This document
~~~

The actual UI logic lives here:

~~~text
web/src/components/FocusMode/
├── FocusContainer.tsx         # Top-level Focus UI shell
├── FocusHeader.tsx            # Entity title + CARE + provenance summary
├── FocusSummary.tsx           # Narrative summary block (AI-labeled)
├── FocusTabs.tsx              # Navigation tabs (Overview · Relations · Spatial · Provenance)
├── RelationsPanel.tsx         # Related-entity browser
├── RelationCard.tsx           # Inline related-entity card
├── NarrativeSection.tsx       # Full narrative region
├── ExplainabilitySection.tsx  # SHAP/LIME explainability UI
├── SpatialPanel.tsx           # Spatial preview + masking indicators
├── ProvenancePanel.tsx        # Provenance chain representation
├── WarningsPanel.tsx          # CARE/sovereignty warnings + ethics banner
└── primitives/                # Legacy primitives (FocusPanel, FocusNarrative, etc.)
~~~

This README references and documents all of the above.

---

# 🧩 Component Responsibilities (Canonical)

---

## 🟥 `FocusContainer.tsx` — *The Focus Mode root layout*

Responsible for:

- Layout shell  
- Tabs → panels routing  
- High-level A11y & CARE warnings  
- Loading + error states  

Must:

- Always show CARE badges  
- Support reduced-motion mode  
- Provide semantic landmarks  

---

## 🟥 `FocusHeader.tsx`

Displays core identity:

- Title  
- Entity type  
- CARE classification  
- sovereignty or sensitive-site warnings  
- provenance summary  

Must:

- Never omit governance metadata  
- Use accessible heading structure  

---

## 🟦 `FocusSummary.tsx`

Shows:

- Brief narrative  
- AI-label flag  
- Relevant metadata  

Rules:

- Must clearly mark AI-generated material  
- Must preserve narrative provenance  

---

## 🟩 `FocusTabs.tsx`

Tab interface for navigating:

- Overview  
- Relations  
- Spatial  
- Provenance  

Requirements:

- Keyboard-navigable  
- ARIA tablist semantics  
- Support large text  

---

## 🟧 `RelationsPanel.tsx`

Renders relation groups:

- People  
- Places  
- Story Nodes  
- Datasets  
- Events  

Rules:

- Must visually mark restricted or sovereign relations  
- Must never fabricate relationships  
- Must use governed view-models  

---

## 🟧 `RelationCard.tsx`

Individual relation unit:

- Label  
- Secondary metadata  
- CARE badge  
- “Open in Focus Mode” link  

---

## 🟨 `NarrativeSection.tsx`

Displays detailed narrative.

Rules:

- Must visibly mark any sections derived from AI  
- Must not collapse provenance metadata  
- Must avoid textual speculation  

---

## 🟪 `ExplainabilitySection.tsx`

Renders:

- SHAP/LIME attributions  
- Ranked factors  
- Influence bars  
- Model identity  

Rules:

- Must be labeled as “Model-derived explanation”  
- Must use WCAG-safe color ramps  

---

## 🟫 `SpatialPanel.tsx`

Shows:

- Map footprint preview (generalized/masked)  
- Masking indicators  
- Sovereignty notices  
- Spatial metadata  

Must:

- Use masked geometry only  
- Never display raw sensitive coordinates  

---

## 🟫 `ProvenancePanel.tsx`

Displays:

- Full provenance chain  
- derived-from relationships  
- data sources  
- license metadata  

Requirements:

- No missing links  
- No reordering provenance  
- Show uncertainty explicitly  

---

## 🟥 `WarningsPanel.tsx`

Displays critical warnings:

- sovereignty restrictions  
- CARE red flags  
- speculative-content notices  
- AI disclaimers  
- incomplete provenance warnings  

Rules:

- Cannot be dismissed unless explicitly designed  
- Must always appear before sensitive content  

---

# 🔐 Governance Rules for UI Components

Focus Mode UI components must:

### ✔ Always surface CARE labels  
### ✔ Always surface sovereignty generalization  
### ✔ Always show provenance  
### ✔ Always mark AI-generated narrative  
### ✔ Never leak raw coordinates  
### ✔ Never flatten or hide governance metadata  
### ✔ Never imply historical claims not in data  
### ✔ Never infer relationships or motives  

Governance violations = **CI BLOCKER**.

---

# ♿ Accessibility Requirements

All components must:

- Fully support WCAG 2.1 AA  
- Use tokenized colors (high contrast)  
- Provide keyboard accessibility  
- Respect reduced-motion  
- Present ARIA roles correctly  
- Include SR-only narrative descriptors  

---

# 🧪 Testing Requirements

Tests must validate:

- A11y behaviors  
- governance surfacing  
- view-model rendering  
- spatial footnotes  
- tab switching  
- provenance visualization  
- explainability readability  

Test files live in:

```

tests/unit/web/components/FocusMode/**
tests/integration/web/features/focus-mode/**

```

---

# 🕰 Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v10.4.0 | 2025-11-15 | Complete Focus Mode UI component documentation |
| v10.3.2 | 2025-11-14 | Added governance + explainability UI rules     |
| v10.3.1 | 2025-11-13 | Initial migration to feature-component split   |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
FAIR+CARE Certified · Public Document · Version-Pinned  
Validated under MCP-DL v6.3 & KFM-MDP v10.4.1  

</div>
