---
title: "🎯 Kansas Frontier Matrix — Focus Mode Hooks Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/features/focus-mode/hooks/README.md"
version: "v10.4.0"
last_updated: "2025-11-15"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/web-feature-focusmode-hooks-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.1"
status: "Active / Enforced"
doc_kind: "Feature Hooks"
intent: "focus-mode-hooks"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Entity-Dependent"
sensitivity_level: "Medium"
public_exposure_risk: "Low–Medium"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"
risk_category: "Mixed"
redaction_required: true
provenance_chain:
  - "web/src/features/focus-mode/hooks/README.md@v10.3.2"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E7 Activity"
  schema_org: "SoftwareSourceCode"
  owl_time: "TemporalEntity"
  prov_o: "prov:Activity"
json_schema_ref: "../../../../../schemas/json/web-feature-focusmode-hooks.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/web-feature-focusmode-hooks-shape.ttl"
doc_uuid: "urn:kfm:doc:web-feature-focusmode-hooks-v10.4.0"
semantic_document_id: "kfm-doc-web-feature-focusmode-hooks"
event_source_id: "ledger:web/src/features/focus-mode/hooks/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative additions"
  - "unverified historical claims"
  - "relationship inference"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "United States / Kansas"
classification: "Public Document"
role: "feature-hooks"
lifecycle_stage: "stable"
ttl_policy: "Annual"
sunset_policy: "Superseded upon Focus Mode v3 refactor"
---

<div align="center">

# 🎯 **Kansas Frontier Matrix — Focus Mode Hooks Overview**  
`web/src/features/focus-mode/hooks/README.md`

**Purpose:**  
Describe the **Focus Mode feature-level hooks** that orchestrate entity-centric flows for the  
Kansas Frontier Matrix Web Platform.  
These hooks provide all **logic**, **data fetching**, **governance enforcement**, and **state wiring**  
required by Focus Mode v2.5 – while keeping React components in `components/FocusMode/**` purely presentational.

</div>

---

## 📘 Overview

Hooks in this folder implement the **feature logic** for Focus Mode:

- Fetching & normalizing focus payloads  
- Resolving related entities  
- Building explainability view-models (SHAP/LIME)  
- Propagating provenance chains  
- Coordinating spatial highlights and masking  
- Emitting telemetry and enforcing governance rules  

They are **logic-only**:

- No JSX  
- No styling  
- No direct DOM manipulation  
- No direct MapLibre/Cesium editing (they call pipelines & services instead)  

---

## 🧱 Directory Structure

~~~text
web/src/features/focus-mode/hooks/
├── useFocusEntity.ts         # Main focus entity controller (payload + governance)
├── useFocusRelations.ts      # Fetch & normalize related entities for the focused entity
├── useFocusExplainability.ts # Load & assemble explainability (SHAP/LIME) metadata
├── useFocusProvenance.ts     # Compose provenance chain for the focused entity
└── useFocusSpatial.ts        # Manage spatial highlight + masking orchestration
~~~

> File names can be adjusted to your actual implementation, but the responsibilities must remain.

---

## 🧩 Hook Responsibilities

---

### 🔹 `useFocusEntity.ts`

Central controller hook for Focus Mode.

Responsibilities:

- Accept an **entity ID + type** as input  
- Call the **`focusPipeline.ts`** orchestrator  
- Validate the returned DTO via type guards  
- Populate:
  - narrative summary  
  - key attributes  
  - governance metadata (CARE, sovereignty, license)  
- Manage loading / error / empty states  
- Emit telemetry:
  - `"focus:open"`  
  - `"focus:entity-load"`  

Governance:

- Must block entity display if CARE rules or sovereignty config forbid it  
- Must surface appropriate warnings for restricted entities  

---

### 🔹 `useFocusRelations.ts`

Manages the focused entity’s **relation graph**.

Responsibilities:

- Fetch related entities (places, events, Story Nodes, datasets, people)  
- Normalize them into typed relation groups  
- Sort by relevance / domain rules  
- Provide convenience derived values for UI (counts, group labels)  

Governance:

- Must mark any relation with restricted CARE status  
- Must avoid displaying relations that backend labeled as suppressed  

Telemetry:

- `"focus:relation-fetch"`  
- `"focus:relation-select"` (via callbacks passed to components)  

---

### 🔹 `useFocusExplainability.ts`

Handles **Explainability** for the focused entity.

Responsibilities:

- Fetch SHAP/LIME or custom explainability payloads from API  
- Map DTO → Explainability view-model (via converters)  
- Filter to a safe, human-comprehensible subset  
- Ensure correct linking to data attributes shown in the UI  

Governance:

- Must label explainability output as **model-derived**  
- Must not fabricate or extrapolate new explanations  
- Must never adjust weights without backend authority  

Telemetry:

- `"focus:explanation-view"`  

---

### 🔹 `useFocusProvenance.ts`

Builds the **provenance view** underlying `ProvenancePanel` and `ProvenanceChip`.

Responsibilities:

- Aggregate provenance metadata from:
  - focus API  
  - Story Node references  
  - STAC/DCAT metadata  
- Normalize them into:
  - a flattened list  
  - a graph-like structure suited for visualization  

Governance:

- Must maintain PROV-O semantics  
- Must keep **full chain integrity** (no dropped links)  
- Must expose missing provenance as a first-class condition (e.g., “unknown source”)  

Telemetry:

- `"focus:provenance-expand"`  

---

### 🔹 `useFocusSpatial.ts`

Provides **spatial orchestration** for Focus Mode.

Responsibilities:

- Use `geospatial/masking.ts`, `geospatial/footprint.ts`, and `geospatial/layers.ts`  
- Compute:
  - highlight geometry  
  - masked geometry (H3)  
  - derived centroids and extents  
- Sync with:
  - MapContext / MapView  
  - TimelineView (via timeline pipeline)  

Governance:

- Must mask all sensitive footprints according to CARE/sovereignty config  
- Must ensure coordinates surfaced to UI are **generalized**  
- Must coordinate with `SovereigntyMaskLayer` and `MaskingIndicator`  

Telemetry:

- `"focus:spatial-highlight-toggle"`  
- `"focus:spatial-computed"`  

---

## 🔐 Governance & FAIR+CARE Rules

Hooks in this folder must:

- Respect CARE metadata and sovereignty rules in **every branch**  
- Never expose precise, sensitive coordinates  
- Never fabricate or infer relationships not provided by the backend  
- Always label AI-generated narrative & explanations via view-model fields  
- Surface provenance metadata to UI layers via stable contracts  

Any governance oversight here is **critical**, because these hooks sit at the core of Focus Mode.

---

## ♿ Accessibility Requirements

Hooks must **enable** WCAG 2.1 AA-friendly UIs by:

- Exposing clear loading + error states (for components to render text equivalents)  
- Supplying flags for:
  - fuzzy time  
  - masked spatial content  
  - low confidence narrative  
- Supporting keyboard-friendly state transitions in Focus Mode components  

Hooks themselves do not handle ARIA roles, but they must provide the **data and flags** needed  
for components to do so.

---

## 📈 Telemetry Responsibilities

All telemetry from Focus Mode is expected to route through these hooks (directly or via `useTelemetry`):

- entity selection/open/close  
- relation exploration  
- explainability viewing  
- provenance expansion  
- spatial highlight toggles  

Hooks must guarantee that:

- No PII is sent  
- Events conform to `types/telemetry.ts` schemas  
- Governance context (CARE, sovereignty) is available for analysis where appropriate  

---

## 🧪 Testing Expectations

For each hook:

- **Unit tests**  
  - happy-path data  
  - error state  
  - governance edge cases  

- **Mocked pipeline + service interactions**  
  - focusPipeline returns expected structures  
  - errors propagate cleanly  

- **Governance tests**  
  - restricted entity behavior  
  - masking enforcement flags  

- **Telemetry tests**  
  - correct events emitted when major hook actions occur  

Tests typically live in:

```text
tests/unit/web/features/focus-mode/hooks/**
tests/integration/web/features/focus-mode/**
````

---

## 🕰 Version History

| Version | Date       | Summary                                                                 |
| ------: | ---------- | ----------------------------------------------------------------------- |
| v10.4.0 | 2025-11-15 | Defined complete Focus Mode feature hook responsibilities and contracts |
| v10.3.2 | 2025-11-14 | Added governance-aware relation + explainability hooks                  |
| v10.3.1 | 2025-11-13 | Initial creation of focus-mode hook layer                               |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License
FAIR+CARE Certified · Public Document · Version-Pinned
Validated under MCP-DL v6.3 & KFM-MDP v10.4.1

</div>
