---
title: "🎯 Kansas Frontier Matrix — Focus Mode Feature Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/features/focus-mode/README.md"
version: "v10.4.0"
last_updated: "2025-11-15"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/web-feature-focusmode-v1.json"
governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.1"
status: "Active / Enforced"
doc_kind: "Feature"
intent: "focus-mode-feature"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Entity-Dependent"
sensitivity_level: "Medium"
public_exposure_risk: "Low–Medium"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"
risk_category: "Mixed"
redaction_required: true
provenance_chain:
  - "web/src/features/focus-mode/README.md@v10.3.2"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E7 Activity"
  schema_org: "AboutPage"
  owl_time: "TemporalEntity"
  prov_o: "prov:Activity"
json_schema_ref: "../../../../schemas/json/web-feature-focusmode.schema.json"
shape_schema_ref: "../../../../schemas/shacl/web-feature-focusmode-shape.ttl"
doc_uuid: "urn:kfm:doc:web-feature-focusmode-v10.4.0"
semantic_document_id: "kfm-doc-web-feature-focusmode"
event_source_id: "ledger:web/src/features/focus-mode/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "summaries"
ai_transform_prohibited:
  - "speculative additions"
  - "unverified historical claims"
  - "inferred relationships"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "United States / Kansas"
classification: "Public Document"
role: "feature"
lifecycle_stage: "stable"
ttl_policy: "Annual"
sunset_policy: "Superseded upon Focus Mode v3 release"
---

<div align="center">

# 🎯 **Kansas Frontier Matrix — Focus Mode Feature Overview**  
`web/src/features/focus-mode/README.md`

**Purpose:**  
Document the **Focus Mode v2.5 feature layer**, which powers entity-centric reasoning,  
spatial + temporal synchronization, narrative explainability, and governance-aware  
data presentation within the Kansas Frontier Matrix Web Platform.

</div>

---

# 📘 What Is Focus Mode?

**Focus Mode v2.5** is an entity-centric exploration surface that provides users with:

- Narrative summaries (AI-labeled, provenance-aware)  
- Spatial footprints + map highlights  
- Timeline highlights + temporal relationships  
- Related entities and Story Node recommendations  
- Explainability overlays (SHAP/LIME)  
- CARE + sovereignty governance notices  
- A unified, multimodal context for each selected entity  

Focus Mode integrates **data, narrative, provenance, space, time, and governance**  
into a single adaptive UI flow.

---

# 🧱 Directory Structure

~~~text
web/src/features/focus-mode/
├── index.ts                     # Public exports for the Focus Mode feature
├── hooks/                       # Focus-specific hooks (logic only)
│   ├── useFocusEntity.ts        # Active focused entity orchestrator
│   ├── useFocusRelations.ts     # Fetch + normalize related entities
│   ├── useFocusExplainability.ts# SHAP/LIME explainability integration
│   ├── useFocusProvenance.ts    # Provenance pipeline for the focused entity
│   └── useFocusSpatial.ts       # Spatial highlight + masking logic
│
├── state/                       # Zustand/Context state slices for Focus Mode
│   ├── focusState.ts            # Entity ID, loading, errors, payload
│   ├── explainabilityState.ts   # Derived explainability vectors
│   ├── spatialState.ts          # Map highlight state
│   └── timelineState.ts         # Local timeline context for Focus Mode
│
├── view-models/                 # DTO → UI-ready view-model converters
│   ├── FocusViewModel.ts        # Root Focus Mode view-model
│   ├── RelationsViewModel.ts    # Relation grouping + types
│   ├── ExplainabilityVM.ts      # Explainability UI model
│   ├── StoryNodeVM.ts           # Story Node v3 lightweight projection for Focus Mode
│   └── ProvenanceVM.ts          # Flattened provenance + attribution structure
│
├── pipelines/                   # Pipeline wrappers (thin layer)
│   └── runFocusPipeline.ts      # Calls focusPipeline + assigns state updates
│
├── components/                  # UI wrappers for Focus Mode (imported from components/FocusMode)
│   └── README.md                # Redirect note (explains UI lives in components/)
│
└── README.md                    # This document
~~~

> **Feature folders contain logic, state, hooks, and view-models —  
> NOT React components.**  
>
> All UI surfaces live in:  
> `web/src/components/FocusMode/**`

---

# 🧩 Feature Responsibilities

Focus Mode unifies 6 independent domains into a single synchronized experience:

---

## 1. **Entity Reasoning**
- Fetch entity details from `/api/focus/{id}`
- Validate schema + type mappings
- Construct Focus ViewModel
- Guard against incomplete/ambiguous data

---

## 2. **Narrative Rendering (AI-labeled)**
- Accepts narratives from backend LLM pipelines
- Clearly labels speculative or AI-generated text
- Applies governance rules:
  - “AI-generated”
  - “Low confidence”
  - “Sources required”
- Applies provenance overlays

---

## 3. **Spatial Integration**
Uses:

- `geospatial/footprint.ts`
- `geospatial/masking.ts`
- `geospatial/layers.ts`

To construct:

- highlight geometry  
- generalization  
- masking  
- sovereignty overlays  

---

## 4. **Temporal Integration**
Uses Timeline pipeline to:

- highlight relevant intervals  
- map fuzzy/open-ended temporal spans  
- propagate temporal uncertainty to UI  

---

## 5. **Explainability & Transparency**
Powered by:

- `useFocusExplainability.ts`
- SHAP vectors
- LIME explanations
- CARE governance rules

Displayed via:

- `ExplainabilitySection.tsx`

---

## 6. **Governance Enforcement (FAIR+CARE)**
Focus Mode is one of the *highest-governance* surfaces in KFM.

It must:

- Display sovereignty notices  
- Mask sensitive locations  
- Apply CARE labels  
- Preserve provenance chains  
- Prevent speculative expansion  
- Suppress unverified historical claims  

Governance failures → CI BLOCKER.

---

# 🧠 Focus Mode Data Flow

~~~mermaid
flowchart LR
    U[User selects entity] --> C["useFocusEntity() Controller"]
    C --> API["/api/focus/{id} (REST/GraphQL)"]
    API --> DTO[Focus DTO]
    DTO --> VM[Focus ViewModel Builder]
    VM --> GOV[CARE + Sovereignty Guard]
    VM --> SPATIAL[Spatial Highlight Builder]
    VM --> TIME[Temporal Range Normalizer]
    VM --> REL[Relations Builder]
    VM --> EXPL[Explainability Formatter]
    SPATIAL --> MAP[MapView Highlight]
    TIME --> TL[Timeline Highlight]
    REL --> UI[FocusMode Components]
    EXPL --> UI
    GOV --> UI
~~~

This matches the **Focus Mode v2.5 architecture contract**.

---

# 🔐 Governance Requirements

Focus Mode must:

- Always show CARE labels  
- Apply H3 generalization for sensitive sites  
- Never show raw coordinates for sovereignty-protected places  
- Label any AI-derived text  
- Indicate missing or uncertain provenance  
- Warn when narratives contain low-confidence material  
- Ensure Story Node suggestions obey governance metadata  

Prohibited:

- invented relationships  
- unverified historical claims  
- coordinate inference  
- speculative narrative reconstruction  

---

# ♿ Accessibility Requirements

Focus Mode must:

- Follow WCAG 2.1 AA  
- Use theme + token + mixins for color, spacing, focus rings  
- Provide keyboard navigation across tabs/panels  
- Provide SR-only summaries for:
  - explainability blocks  
  - temporal uncertainty  
  - masked spatial areas  

---

# 🧪 Testing Requirements

Tests must cover:

- Focus pipeline + converters  
- View-model generation  
- Governance metadata propagation  
- Narrative safety enforcement  
- Spatial highlight generation  
- Temporal normalization  
- Explainability correctness  
- A11y compliance  

Located in:

```

tests/unit/web/features/focus-mode/**
tests/integration/web/features/focus-mode/**

```

---

# 🕰 Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v10.4.0 | 2025-11-15 | Complete Focus Mode v2.5 feature documentation; aligned with full KFM pipeline architecture |
| v10.3.2 | 2025-11-14 | Added explainability + provenance enforcement |
| v10.3.1 | 2025-11-13 | Initial feature-scoped Focus Mode folder added |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
FAIR+CARE Certified · Public Document · Version-Pinned  
Validated under MCP-DL v6.3 & KFM-MDP v10.4.1  

</div>
