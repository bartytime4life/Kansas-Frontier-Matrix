---
title: "🎯 Kansas Frontier Matrix — Focus Mode Feature Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/features/focus-mode/README.md"
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
telemetry_ref: "../../../../releases/v11.2.2/web-feature-focusmode-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/web-feature-focusmode-v2.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

status: "Active / Enforced"
doc_kind: "Feature Architecture Overview"
intent: "focus-mode-feature"
role: "feature"

fair_category: "F1-A1-I1-R1"
care_label: "Public / Entity-Dependent"
sensitivity_level: "Medium"
public_exposure_risk: "Low–Medium"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"
risk_category: "Mixed"
redaction_required: true

provenance_chain:
  - "web/src/features/focus-mode/README.md@v10.4.0"
  - "web/src/features/focus-mode/README.md@v10.3.2"

ontology_alignment:
  cidoc: "E7 Activity"
  schema_org: "AboutPage"
  owl_time: "TemporalEntity"
  prov_o: "prov:Activity"

json_schema_ref: "../../../../schemas/json/web-feature-focusmode.schema.json"
shape_schema_ref: "../../../../schemas/shacl/web-feature-focusmode-shape.ttl"

doc_uuid: "urn:kfm:doc:web-feature-focusmode-v11.2.2"
semantic_document_id: "kfm-doc-web-feature-focusmode"
event_source_id: "ledger:web/src/features/focus-mode/README.md"
immutability_status: "version-pinned"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "summaries"
ai_transform_prohibited:
  - "speculative-additions"
  - "unverified-historical-claims"
  - "inferred-relationships"
  - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "United States / Kansas"
classification: "Public Document"
lifecycle_stage: "stable"
ttl_policy: "Annual review"
sunset_policy: "Superseded upon Focus Mode v4 release"
---

<div align="center">

# 🎯 **Kansas Frontier Matrix — Focus Mode Feature Overview**  
`web/src/features/focus-mode/README.md`

**Purpose:**  
Document the **Focus Mode v3 feature layer**, which powers entity-centric reasoning,  
spatial + temporal synchronization, narrative explainability, and governance-aware  
data presentation within the Kansas Frontier Matrix Web Platform.

</div>

---

## 📘 Overview

**Focus Mode v3** is the entity-centric exploration surface of KFM. It provides users with:

- Narrative summaries (AI-labeled, provenance-aware)  
- Spatial footprints + map highlights  
- Timeline highlights + temporal relationships  
- Related entities and Story Node recommendations  
- Explainability overlays (SHAP/LIME-style integrations from the AI layer)  
- CARE + sovereignty governance notices  
- A unified, multimodal context for each selected entity  

Focus Mode integrates **data, narrative, provenance, space, time, and governance**  
into a single adaptive UI flow, orchestrated across the **graph**, **pipelines**, and **web** layers.

The `web/src/features/focus-mode/` feature module provides **logic, state, and view-models**  
only; all presentational UI components live in `web/src/components/FocusMode/**`.

---

## 🗂️ Directory Layout

~~~text
web/src/features/focus-mode/
│
├── 📦 index.ts                      # Public exports for the Focus Mode feature
│
├── 🪝 hooks/                        # Focus-specific hooks (logic only)
│   ├── 🧠 useFocusEntity.ts         # Active focused-entity orchestrator (entry point)
│   ├── 🔗 useFocusRelations.ts      # Fetch + normalize related entities from graph/API
│   ├── 🤖 useFocusExplainability.ts # Explainability integration (SHAP/LIME-style payloads)
│   ├── 📜 useFocusProvenance.ts     # Provenance pipeline for the focused entity
│   └── 🗺️ useFocusSpatial.ts        # Spatial highlight + masking logic (MapView integration)
│
├── 🧠 state/                        # State slices (Zustand/Context) for Focus Mode
│   ├── 🎯 focusState.ts             # Focus entity ID, loading, errors, payload
│   ├── 📊 explainabilityState.ts    # Derived explainability vectors + flags
│   ├── 🗺️ spatialState.ts           # Map highlight + layer toggles
│   └── ⏱️ timelineState.ts          # Local timeline window for Focus Mode
│
├── 🧬 view-models/                  # DTO → UI-ready view-model converters
│   ├── 🎯 FocusViewModel.ts         # Root Focus Mode entity view-model
│   ├── 🔗 RelationsViewModel.ts     # Relation grouping + typed relation VMs
│   ├── 🤖 ExplainabilityVM.ts       # Explainability UI model
│   ├── 📖 StoryNodeVM.ts            # Story Node v3 lightweight projections for Focus Mode
│   └── 🧾 ProvenanceVM.ts          # Flattened provenance + attribution structures
│
├── 🔗 pipelines/                    # Pipeline wrappers (thin orchestration layer)
│   └── 🚀 runFocusPipeline.ts       # Calls graph/API focus pipeline + dispatches state updates
│
├── 🎨 components/                   # UI wrappers for Focus Mode
│   └── README.md                   # Redirect note (UI lives in web/src/components/FocusMode)
│
└── 📘 README.md                    # This document
~~~

> **Important:** Feature folders contain **logic, state, hooks, and view-models — NOT React UI.**  
> All UI surfaces live under: `web/src/components/FocusMode/**`.

---

## 🧩 Feature Responsibilities

Focus Mode unifies 6 independent domains into a single synchronized experience:

1. **Entity Reasoning**  
2. **Narrative Rendering (AI-labeled)**  
3. **Spatial Integration**  
4. **Temporal Integration**  
5. **Explainability & Transparency**  
6. **Governance Enforcement (FAIR+CARE)**  

Each responsibility is implemented via **hooks + state + view-models**, not via UI components.

---

### 1️⃣ Entity Reasoning

- Fetch entity details from `/api/focus/{id}` (REST) or equivalent GraphQL query.  
- Validate schema + type mappings against Focus DTO and graph contracts.  
- Construct a `FocusViewModel` representing:
  - core identity (type, label, IDs)  
  - typed relations (people, places, events, documents, datasets)  
  - CARE + sovereignty metadata  
- Guard against incomplete/ambiguous data:
  - entity must be resolvable in the graph  
  - missing critical fields → safe fallbacks + error surfaces (never silent failures)

`useFocusEntity.ts` is the **primary controller hook**, orchestrating the full focus lifecycle.

---

### 2️⃣ Narrative Rendering (AI-Labeled)

- Accept narratives from backend LLM pipelines (precomputed or on-demand).  
- Clearly label speculative or AI-generated text (UI surfaces show “AI-generated” badges).  
- Apply governance rules:
  - mark low-confidence segments  
  - require source-backed factual claims  
- Attach provenance overlays:
  - link narrative segments to entities and source documents via IDs  
  - ensure Story Node–compatible structure for later insertion into the narrative graph.

Narrative content is treated as **data**, not free-form text.

---

### 3️⃣ Spatial Integration

Uses shared geospatial utilities:

- `geospatial/footprint.ts`  
- `geospatial/masking.ts`  
- `geospatial/layers.ts`  

Focus Mode spatial responsibilities:

- Build highlight geometries (Points, Lines, Polygons) for the Focus entity & neighbors.  
- Apply H3 generalization/masking for sensitive places (archaeology, tribal lands, etc.).  
- Integrate sovereignty overlays (tribal boundaries, treaty polygons).  
- Push derived spatial overlays to `MapView` via `spatialState` and `useFocusSpatial`.

Map-facing outputs must be **GeoJSON-safe** and aligned with MapLibre layer schema.

---

### 4️⃣ Temporal Integration

Via `timelineState` and time utilities:

- Highlight relevant intervals:
  - event dates, person lifespans, treaty effective periods, dataset validity.  
- Map fuzzy/open-ended spans:
  - approximate ranges (e.g., “ca. 1850s”) modeled using precision flags.  
- Propagate temporal uncertainty to UI:
  - timeline labels + styling show approximate vs exact periods.  

Focus Mode time logic is OWL-Time–compatible and integrates with global `TimeContext`.

---

### 5️⃣ Explainability & Transparency

Powered by:

- `useFocusExplainability.ts`  
- explainability payloads (SHAP/LIME-style vectors) from the AI pipelines  

Focus Mode explainability:

- Surfaces **why** an entity or relation is highlighted:
  - which features or data points drive relevance.  
- Exposes per-field or per-entity contribution scores to the UI.  
- Provides structured models (`ExplainabilityVM`) suitable for:
  - charts, badges, and textual explanations without leaking model internals unsafely.  

Explainability outputs must never override governance or CARE rules.

---

### 6️⃣ Governance Enforcement (FAIR+CARE)

Focus Mode is one of the **highest-governance** surfaces in KFM.

It must:

- Display CARE labels prominently for focused entities.  
- Apply H3 generalization and masking for sensitive sites (especially archaeology & sovereignty).  
- Never show raw coordinates for sovereignty-protected places.  
- Label any AI-derived text clearly (“AI-generated”, “low confidence”, etc.).  
- Indicate missing or uncertain provenance.  
- Warn when narratives contain low-confidence or contested material.  
- Ensure Story Node suggestions and relation graphs obey governance metadata.

**Strictly prohibited:**

- Invented relationships  
- Unverified historical claims  
- Coordinate inference for masked sites  
- Speculative narrative reconstruction  
- Any “governance-override” behavior  

Governance failures → **hard CI BLOCKER** for Focus Mode feature changes.

---

## 🧠 Focus Mode Data Flow & Architecture

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
    REL --> UI[FocusMode UI Components]
    EXPL --> UI
    GOV --> UI
~~~

This flow describes **Focus Mode v3** orchestration between:

- **Feature layer** (`web/src/features/focus-mode/**`)  
- **Graph/API** (Neo4j + FastAPI/GraphQL)  
- **UI components** (`web/src/components/FocusMode/**`)  

---

## 🔐 Governance Requirements

Focus Mode MUST:

- Always surface CARE labels for the focal entity and sensitive neighbors.  
- Apply H3 masking / generalization for:
  - sacred/archaeological sites  
  - sovereignty-controlled territories  
- Avoid exposing raw coordinates where masking is required.  
- Propagate sovereignty notices into the Focus Detail view.  
- Ensure all suggestions (related entities, Story Nodes) respect:
  - CARE tags  
  - license constraints  
  - indigenous data sovereignty policies  

Any governance regression in Focus Mode triggers:

- **CI failure** in governance-validation jobs.  
- Blocked merges until remediation and governance review.

---

## ♿ Accessibility Requirements

Focus Mode feature logic supports A11y-compliant UI by ensuring:

- All Focus entities have:
  - clear labels, summaries, and types for ARIA usage.  
- Explainability sections have:
  - text equivalents, not only visualizations.  
- Temporal and spatial uncertainty are surfaced in structured metadata:
  - enabling screen readers to convey approximate vs exact.  

Consuming components in `web/src/components/FocusMode/**` must:

- Provide keyboard navigation across tabs/panels.  
- Use ARIA roles for dialog, tablist, tabpanel, etc.  
- Respect high-contrast and reduced-motion preferences from `A11yContext`.  

Accessibility regressions in Focus Mode flows → **CI BLOCKER**.

---

## 📈 Telemetry Responsibilities

Focus Mode feature MUST cooperate with telemetry by:

- Emitting/forwarding event hooks for:
  - `"focus:open"` / `"focus:close"`  
  - `"focus:entity-select"`  
  - `"focus:summary-expand"`  
  - `"focus:relation-select"`  
  - `"focus:explanation-view"`  
  - `"focus:spatial-highlight"`  
  - `"focus:care-warning"`  

Telemetry requirements:

- All events are **non-PII** and schema-valid (`web-feature-focusmode-v2.json`).  
- CARE-sensitive interactions may be aggregated or anonymized as needed.  
- Telemetry is recorded in:
  - `releases/<version>/web-feature-focusmode-telemetry.json`  

Telemetry events must never leak raw coordinates for masked entities or sensitive IDs.

---

## 🧪 Testing Requirements

Tests MUST validate:

- Focus pipeline orchestration:
  - `runFocusPipeline.ts` behavior for success/error cases.  
- View-model generation:
  - correctness of `FocusViewModel`, `RelationsViewModel`, `ExplainabilityVM`, etc.  
- Governance propagation:
  - CARE/sovereignty flags present on Focus entities and relations.  
- Narrative safety:
  - no speculative/inferred relationships emitted by feature logic.  
- Spatial highlight generation:
  - correct masking/generalization behavior.  
- Temporal normalization:
  - proper modeling of fuzzy dates and precision levels.  
- Explainability integrity:
  - explainability payloads correspond to underlying data features.  
- A11y integration:
  - feature outputs supply adequate metadata for consuming components.

Test locations:

~~~text
tests/unit/web/features/focus-mode/**
tests/integration/web/features/focus-mode/**
tests/e2e/web/features/focus-mode/**      # where applicable, for full-stack flows
~~~

CI must run these suites on every PR touching `web/src/features/focus-mode/**`.

---

## 🕰️ Version History

| Version  | Date       | Summary                                                                                         |
|---------:|------------|-------------------------------------------------------------------------------------------------|
| v11.2.2  | 2025-11-30 | Upgraded to KFM-MDP v11.2.2; aligned with v11 Focus Mode v3 design, telemetry v2, and governance. |
| v10.4.0  | 2025-11-15 | Complete Focus Mode v2.5 feature documentation; aligned with full KFM pipeline architecture.    |
| v10.3.2  | 2025-11-14 | Added explainability + provenance enforcement.                                                  |
| v10.3.1  | 2025-11-13 | Initial feature-scoped Focus Mode folder added.                                                 |

---

## ⚖️ Footer

<div align="center">

**Kansas Frontier Matrix — Focus Mode Feature**  
🎯 Entity-Centric Exploration · 🛡️ FAIR+CARE Governance · 🧠 Explainable Narratives  

[← Back to Web Features](../README.md) •  
[📚 Docs Root](../../../../README.md) •  
[🛡 Governance Charter](../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

© 2025 Kansas Frontier Matrix — MIT License  

**End of Document**

</div>