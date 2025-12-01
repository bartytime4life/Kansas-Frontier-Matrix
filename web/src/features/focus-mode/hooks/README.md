---
title: "🎯 Kansas Frontier Matrix — Focus Mode Hooks Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/features/focus-mode/hooks/README.md"
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
telemetry_ref: "../../../../../releases/v11.2.2/web-feature-focusmode-hooks-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/web-feature-focusmode-hooks-v2.json"
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

status: "Active / Enforced"
doc_kind: "Feature Hooks Overview"
intent: "focus-mode-hooks"
role: "feature-hooks"

fair_category: "F1-A1-I1-R1"
care_label: "Public / Entity-Dependent"
sensitivity_level: "Medium"
public_exposure_risk: "Low–Medium"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"
risk_category: "Mixed"
redaction_required: true

provenance_chain:
  - "web/src/features/focus-mode/hooks/README.md@v10.4.0"
  - "web/src/features/focus-mode/hooks/README.md@v10.3.2"

ontology_alignment:
  cidoc: "E7 Activity"
  schema_org: "SoftwareSourceCode"
  owl_time: "TemporalEntity"
  prov_o: "prov:Activity"

json_schema_ref: "../../../../../schemas/json/web-feature-focusmode-hooks.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/web-feature-focusmode-hooks-shape.ttl"
doc_uuid: "urn:kfm:doc:web-feature-focusmode-hooks-v11.2.2"
semantic_document_id: "kfm-doc-web-feature-focusmode-hooks-v11"
event_source_id: "ledger:web/src/features/focus-mode/hooks/README.md"
immutability_status: "version-pinned"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative-additions"
  - "unverified-historical-claims"
  - "relationship-inference"
  - "governance-override"
  - "content-alteration"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "United States / Kansas"
classification: "Public Document"
lifecycle_stage: "stable"
ttl_policy: "Annual review"
sunset_policy: "Superseded upon Focus Mode v4 hooks refactor"
---

<div align="center">

# 🎯 **Kansas Frontier Matrix — Focus Mode Hooks Overview**  
`web/src/features/focus-mode/hooks/README.md`

**Purpose:**  
Describe the **Focus Mode feature-level hooks** that orchestrate entity-centric flows for the  
Kansas Frontier Matrix Web Platform.  
These hooks provide all **logic**, **data fetching**, **governance enforcement**, and **state wiring**  
required by Focus Mode v3 – while keeping React components in `components/FocusMode/**` purely presentational.

</div>

---

## 📘 Overview

Hooks in this folder implement the **feature logic** for Focus Mode:

- Fetching & normalizing focus payloads  
- Resolving related entities from the graph  
- Building explainability view-models (SHAP/LIME-style payloads)  
- Propagating provenance chains (PROV-O aligned)  
- Coordinating spatial highlights and masking with MapView  
- Emitting telemetry and enforcing FAIR+CARE rules  

They are **logic-only**:

- No JSX  
- No styling  
- No direct DOM manipulation  
- No direct MapLibre/Cesium editing (they call pipelines, services, and state instead)  

---

## 🧱 Directory Structure (Emoji-Enhanced)

~~~text
web/src/features/focus-mode/hooks/
│
├── 🧠 useFocusEntity.ts          # Main focus entity controller (payload + governance)
├── 🔗 useFocusRelations.ts       # Fetch & normalize related entities for the focused entity
├── 🤖 useFocusExplainability.ts  # Load & assemble explainability metadata
├── 📜 useFocusProvenance.ts      # Compose provenance chain for the focused entity
└── 🗺️ useFocusSpatial.ts         # Manage spatial highlight + masking orchestration
~~~

> File names may differ slightly in implementation, but the **responsibilities MUST remain**.

---

## 🧩 Hook Responsibilities

---

### 🔹 `useFocusEntity.ts` — Core Controller Hook

**Responsibilities:**

- Accept an **entity ID + type** as input.  
- Call the **focus pipeline** (e.g., `runFocusPipeline.ts`) or `/api/focus/{id}` endpoints.  
- Validate the returned DTO via type guards + JSON Schema.  
- Build and expose a **FocusViewModel**:
  - core entity identity & type  
  - resolved governance metadata (CARE, sovereignty, license)  
  - minimal narrative and attribute summary (non-speculative)  
- Maintain local React state:
  - `loading`, `error`, `data` (FocusViewModel)  

**Governance:**

- MUST block or gate entity display if CARE rules or sovereignty configuration forbid showing details in this context.  
- MUST surface appropriate warnings and metadata flags for restricted or sovereign entities.  

**Telemetry:**

- Ensure callers can emit:
  - `"focus:open"`  
  - `"focus:entity-load"`  
  - `"focus:entity-error"`  

---

### 🔹 `useFocusRelations.ts` — Relations Logic

**Responsibilities:**

- Fetch related entities (people, places, events, Story Nodes, datasets) from the graph/API.  
- Normalize them into **typed relation groups** (e.g., by relationship type).  
- Sort relations by relevance or feature rules (e.g., story relevance, graph distance).  
- Provide derived values for UI:
  - counts  
  - group labels  
  - top-N lists  

**Governance:**

- MUST mark any relation with restricted CARE status for UI to respect.  
- MUST avoid sending relations that backend marked as suppressed or blocked (the backend is source of truth).  

**Telemetry:**

- Expose hooks/callbacks so callers can emit:
  - `"focus:relation-fetch"`  
  - `"focus:relation-select"`  

---

### 🔹 `useFocusExplainability.ts` — Explainability Logic

**Responsibilities:**

- Fetch explainability payloads (SHAP/LIME-style or Focus-specific) for the focused entity.  
- Convert DTO → `ExplainabilityVM` (ranked feature contributions, evidence sets).  
- Filter to an interpretable subset of features (e.g., top K signals).  
- Provide structured metadata for:
  - charts  
  - textual explanations  
  - story-level overlays  

**Governance:**

- MUST clearly mark outputs as **model-derived**, not factual assertions.  
- MUST NOT alter weights or invent new explanations; any transformation must be purely structural (e.g., sorting, filtering).  

**Telemetry:**

- Allow callers to emit:
  - `"focus:explanation-view"`  
  - `"focus:explanation-error"` (if payload fails validations)  

---

### 🔹 `useFocusProvenance.ts` — Provenance Chain Builder

**Responsibilities:**

- Aggregate provenance from:
  - Focus API  
  - Entity graph (Neo4j node relationships)  
  - STAC/DCAT metadata  
  - Story Node references  
- Normalize into:
  - flattened lists of sources & agents  
  - optional graph-like structures for visualizing lineage  

**Governance:**

- MUST maintain PROV-O semantics (`Entity`, `Activity`, `Agent`).  
- MUST NOT drop provenance links silently; missing links should be flagged as such.  
- MUST surface incomplete provenance as a first-class status (e.g., “source unknown”).  

**Telemetry:**

- Expose patterns so callers can emit:
  - `"focus:provenance-expand"`  
  - `"focus:provenance-missing"`  

---

### 🔹 `useFocusSpatial.ts` — Spatial Orchestration

**Responsibilities:**

- Connect Focus Mode to geospatial utilities:
  - `geospatial/footprint.ts`  
  - `geospatial/masking.ts`  
  - `geospatial/layers.ts`  
- Compute:
  - focus entity highlight geometry  
  - masked geometry (H3 generalized)  
  - derived centroids and extents for MapView  
- Push results into:
  - MapContext / MapView state  
  - TimelineView (for temporal-spatial linking)  

**Governance:**

- MUST mask all sensitive footprints according to CARE + sovereignty policy.  
- MUST ensure coordinates surfaced to UI are **generalized**; no raw coordinates for protected sites.  
- MUST coordinate with `SovereigntyMaskLayer`, `MaskingIndicator`, and other governance components.  

**Telemetry:**

- Support emission of:
  - `"focus:spatial-highlight-toggle"`  
  - `"focus:spatial-computed"`  
  - `"focus:spatial-mask-applied"`  

---

## 🔐 Governance & FAIR+CARE Rules

Hooks in this folder are at the **governance-critical core** of Focus Mode.

They MUST:

- Respect CARE metadata and sovereignty rules in **all branches**, not just “happy path.”  
- Never expose precise coordinates for sensitive or sovereignty-controlled entities.  
- Never fabricate or infer relationships beyond what the backend returns.  
- Always label AI-generated narrative & explainability as such via view-model flags.  
- Always surface provenance metadata when available; missing provenance must be explicit.  

Any governance oversight here is **critical** and can propagate system-wide.  
Governance regressions → **CI BLOCKER** for any Focus Mode–related change.

---

## ♿ Accessibility Requirements

Hooks must **enable** WCAG 2.1 AA+–compliant UIs by providing:

- Clear, typed loading/error/data states for accessible messaging.  
- Flags for:
  - fuzzy time (`precision`, approximate events)  
  - masked spatial content (for alternative map descriptions)  
  - low-confidence narrative / explainability segments.  
- Stable IDs and type tags so components can:
  - provide headings, landmark regions, ARIA attributes, and descriptive text.  

Hooks themselves do not manage ARIA roles or DOM,  
but their data shape MUST allow accessible React components to be easily built.

---

## 📈 Telemetry Responsibilities

Focus Mode telemetry is expected to be orchestrated via these hooks (directly or via shared telemetry utilities):

- Entity-level events:
  - `focus:open`, `focus:close`, `focus:entity-load`, `focus:entity-error`  
- Relation events:
  - `focus:relation-fetch`, `focus:relation-select`  
- Explainability events:
  - `focus:explanation-view`, `focus:explanation-error`  
- Provenance events:
  - `focus:provenance-expand`, `focus:provenance-missing`  
- Spatial events:
  - `focus:spatial-highlight-toggle`, `focus:spatial-mask-applied`  

Telemetry MUST:

- Be non-PII (no names, no raw coordinates, no direct personal identifiers).  
- Be schema-valid (see `web-feature-focusmode-hooks-v2.json`).  
- Annotate CARE context where appropriate (e.g., included in event payload as a label, not raw sensitive details).

---

## 🧪 Testing Expectations

For each hook:

- **Unit tests**:
  - happy-path data  
  - error states  
  - governance edge cases (restricted entities, missing provenance)  

- **Mocked pipeline & service interactions**:
  - e.g., `focusPipeline` returns expected DTO shapes  
  - network errors & schema validation failures are handled gracefully  

- **Governance tests**:
  - restricted entity behavior is correct (gated/masked)  
  - relation masking for sovereignty rules taken into account  

- **Telemetry tests**:
  - correct events emitted when main actions occur  
  - invalid events are not sent or are blocked by guards  

Canonical locations:

~~~text
tests/unit/web/features/focus-mode/hooks/**
tests/integration/web/features/focus-mode/**
~~~

Hook-level tests are required for any functional change in this folder.

---

## 🕰 Version History

| Version | Date       | Summary                                                                                         |
|--------:|------------|-------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-30 | Upgraded to v11.2.2; aligned hooks with Focus Mode v3 architecture, telemetry v2, FAIR+CARE v11. |
| v10.4.0 | 2025-11-15 | Defined complete Focus Mode v2.5 hook responsibilities and contracts.                           |
| v10.3.2 | 2025-11-14 | Added governance-aware relation + explainability hooks.                                         |
| v10.3.1 | 2025-11-13 | Initial creation of focus-mode hook layer.                                                      |

---

## ⚖️ Footer

<div align="center">

**Kansas Frontier Matrix — Focus Mode Hooks**  
🎯 Entity Logic · 🧠 Explainable State · 🛡️ FAIR+CARE Enforcement  

[← Back to Focus Mode Feature](../README.md) •  
[✨ Web Features Index](../../README.md) •  
[🛡 Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

© 2025 Kansas Frontier Matrix — MIT License  

**End of Document**

</div>