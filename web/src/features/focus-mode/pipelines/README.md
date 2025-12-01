---
title: "🔄 Kansas Frontier Matrix — Focus Mode Pipeline Specification (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/features/focus-mode/pipelines/README.md"
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
telemetry_ref: "../../../../../releases/v11.2.2/web-feature-focusmode-pipelines-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/web-feature-focusmode-pipelines-v2.json"
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
doc_kind: "Pipeline Layer"
intent: "focus-mode-pipelines"
role: "pipeline-layer"

fair_category: "F1-A1-I1-R1"
care_label: "Public / Entity-Dependent"
sensitivity_level: "Medium"
public_exposure_risk: "Low–Medium"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"
risk_category: "Mixed"
redaction_required: true

provenance_chain:
  - "web/src/features/focus-mode/pipelines/README.md@v10.4.0"
  - "web/src/features/focus-mode/pipelines/README.md@v10.3.2"

ontology_alignment:
  cidoc: "E7 Activity"
  schema_org: "SoftwareApplication"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"

json_schema_ref: "../../../../../schemas/json/web-feature-focusmode-pipelines.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/web-feature-focusmode-pipelines-shape.ttl"
doc_uuid: "urn:kfm:doc:web-feature-focusmode-pipelines-v11.2.2"
semantic_document_id: "kfm-doc-web-feature-focusmode-pipelines-v11"
event_source_id: "ledger:web/src/features/focus-mode/pipelines/README.md"
immutability_status: "version-pinned"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "summaries"
  - "speculative-additions"
  - "unverified-historical-claims"
  - "relationship-inference"
  - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "United States / Kansas"
classification: "Public Document"
lifecycle_stage: "stable"
ttl_policy: "Annual review"
sunset_policy: "Superseded upon Focus Mode v4 pipeline refactor"
---

<div align="center">

# 🔄 **Kansas Frontier Matrix — Focus Mode Pipeline Specification**  
`web/src/features/focus-mode/pipelines/README.md`

**Purpose:**  
Describe the **feature-scoped pipeline wrappers** that interface Focus Mode’s logic  
(`focusPipeline.ts`) with feature-level hooks and state slices.  
These wrappers ensure deterministic, governance-safe execution of the  
Focus Mode v3 entity reasoning flow.

</div>

---

## 📘 Overview

The **Focus Mode pipeline layer** acts as a thin wrapper between:

- The **global pipeline orchestrator** (`web/src/pipelines/focusPipeline.ts`)  
- The **feature hooks** (`useFocusEntity`, `useFocusExplainability`, etc.)  
- The **feature state slices** (`focusState`, `spatialState`, `timelineState`, `explainabilityState`)  
- The **Focus Mode view-models** (`FocusViewModel`, `RelationsViewModel`, `ExplainabilityVM`, etc.)

It is responsible for:

- Executing the full focus pipeline  
- Normalizing and transforming the result into Feature-layer view-models  
- Applying FAIR+CARE governance gates  
- Updating feature state slices in a deterministic way  
- Triggering downstream spatial/temporal synchronization  
- Exposing telemetry hooks for Focus Mode usage and performance  

This layer contains:

- ❌ no UI,  
- ❌ no React components,  
- ❌ no direct MapLibre/Cesium calls —  
only **data coordination and deterministic orchestration**.

---

## 🧱 Directory Structure

~~~text
web/src/features/focus-mode/pipelines/
│
├── 🚀 runFocusPipeline.ts   # Executes global focusPipeline + updates feature state
└── 📘 README.md             # This document
~~~

Future versions MAY add additional wrappers if Focus Mode introduces advanced workflows (e.g., multi-entity focus).

---

## 🧩 Module Responsibilities

---

### 🔹 `runFocusPipeline.ts` — Primary Wrapper

This is the **single entrypoint** for global Focus Mode pipeline execution inside the feature layer.

It coordinates:

#### 1️⃣ Global Focus Pipeline Execution

- Calls `web/src/pipelines/focusPipeline.ts` with:
  - `entityId`, `entityType`  
  - optional context (time window, map region)  
- Receives a full **Focus DTO** containing:  
  - core entity details  
  - narratives & summaries  
  - relations graph  
  - spatial footprints & hints  
  - temporal ranges  
  - provenance metadata  
  - CARE & sovereignty metadata  
  - explainability payloads  

#### 2️⃣ View-Model Conversion

- Converts pipeline output → Focus Mode view-models using:
  - `FocusViewModel.ts`  
  - `RelationsViewModel.ts`  
  - `ExplainabilityVM.ts`  
  - `StoryNodeVM.ts`  
  - `ProvenanceVM.ts`  

Mapping rules MUST:

- Preserve semantics from the global pipeline (no speculation).  
- Represent uncertainty (temporal/spatial) explicitly via VM fields.  
- Carry through all governance metadata.

#### 3️⃣ Governance Enforcement (FAIR+CARE)

The wrapper ensures:

- CARE labels and sovereignty flags are propagated into feature state.  
- Sensitive attributes (e.g., raw coordinates, unredacted sacred-site narratives) are **removed or masked** before state update.  
- AI narratives are flagged as `aiGenerated`, `confidenceLevel`, etc., for UI to render correctly.  
- Any failure in governance validation results in:
  - safe error state  
  - telemetry event  
  - no unsafe state updates.

#### 4️⃣ State Slice Updates

Writes results into Focus Mode feature state:

- `focusState`:
  - focus entity metadata  
  - VMs for narrative & core entity data  
  - governance flags (CARE, sovereignty)  

- `spatialState`:
  - masked geometry  
  - centroids  
  - layer configuration for MapView  

- `timelineState`:
  - normalized OWL-Time temporal ranges  
  - flags for uncertainty and predictive vs historical  

- `explainabilityState`:
  - explainability vectors  
  - top contributing signals  
  - evidence references  

All updates MUST be immutable and traceable.

#### 5️⃣ Spatial Integration

Integrates with geospatial pipeline primitives:

- `masking.ts` (H3-based + sovereignty masks)  
- `footprint.ts` (footprint generalization & classification)  
- `layers.ts` (overlay/layer configuration)  
- `bounds.ts` (viewport fitting)  

Spatial outputs are consumed by `MapContext` and `MapView`.

#### 6️⃣ Timeline Integration

- Identifies relevant temporal intervals from Focus DTO.  
- Normalizes to OWL-Time friendly forms.  
- Updates `timelineState` & interacts with global `TimeContext`  
  to highlight:
  - event intervals  
  - lifespan spans  
  - dataset coverage windows  

#### 7️⃣ Provenance Integration

- Flattens complex provenance graphs into UI-readable structures.  
- Maintains full PROV-O semantics (`Entity`, `Activity`, `Agent`).  
- Populates provenance view-models for:
  - FocusMode provenance panel  
  - Governance dashboards.

#### 8️⃣ Telemetry Emission

The wrapper is expected to collaborate with telemetry utilities to emit events such as:

- `"focus:pipeline-start"`  
- `"focus:pipeline-success"`  
- `"focus:pipeline-error"`  
- `"focus:highlight-generated"`  
- `"focus:explainability-available"`  
- `"focus:governance-blocked"`  

Telemetry MUST:

- Conform to schemas in:
  - `types/telemetry.ts`  
  - `schemas/telemetry/web-feature-focusmode-pipelines-v2.json`  
- Never contain PII or raw sensitive coordinates.  
- Encode governance context in non-sensitive forms (e.g., CARE label enums, not raw narrative text).

---

## 🔐 Governance (FAIR+CARE) Requirements

The pipeline wrapper **MUST** enforce governance rules *before* state update:

### Mandatory

- CARE classification propagation from DTO → state & VM.  
- Sovereignty masking using policies defined in Governance layer.  
- Masking or coarse generalization of precise coordinates for sensitive sites.  
- AI narrative labeling:
  - denote AI-generated vs archival vs mixed sources.  
- Provenance visibility (no silent loss of provenance).  
- Strict rejection of DTOs missing required governance fields.  

### Forbidden

- Creating or linking entities that the backend did not explicitly mark as related.  
- Inferring temporal ranges (e.g., “probably earlier/later”) without explicit metadata.  
- Storing raw sensitive coordinates in state or VMs.  
- Dropping required provenance or governance attributes for convenience.  
- Overriding CARE classification or sovereignty flags.  

Any violation is classified as a **CI BLOCKER** and MUST be remediated before merge.

---

## ♿ Accessibility Requirements

The pipeline wrapper must ensure that the outputs it produces:

- Contain all semantic cues needed for accessible UI:
  - flags for fuzzy temporal ranges  
  - flags for masked spatial content  
  - summary-level provenance for explanatory text  
- Are structured for screenreader-friendly components:
  - narrative blocks broken into manageable segments  
  - clearly labeled relation groups  
  - clarity of “what changed” between Focus contexts (if diffed).  

Actual ARIA roles and screenreader text belong to components, but pipeline outputs drive A11y design.

---

## 📈 Telemetry Requirements

The pipelines layer feeds telemetry by:

- Timing pipeline execution (e.g., `focus_pipeline_ms`).  
- Counting:
  - governance gates triggered  
  - masked/blocked entities  
  - successful vs error states.  
- Supporting energy/carbon annotations based on STAC/DCAT + infra metrics.

Events MUST:

- Be non-PII.  
- Be schema-valid.  
- Be included in `web-feature-focusmode-pipelines-telemetry.json`.  

Telemetry is used to:

- Monitor performance & UX.  
- Track reliability & reproducibility.  
- Provide quantitative evidence for FAIR+CARE compliance.

---

## 🧪 Testing Requirements

Tests MUST cover:

### Unit Tests (using mocks)

- Correct invocation of `focusPipeline.ts`.  
- Correct mapping from DTO → VMs.  
- Governance gating logic (restricted entities, masked geometry).  
- Error handling (network failures, schema violations).  

### Integration Tests

- End-to-end: entity ID → pipeline → state → Focus Mode UI (through integration harness).  
- Spatial highlight generation & masking correctness.  
- Timeline highlight synchronization for events and ranges.  
- Explainability & provenance UI states (in test harness).  

### Negative Tests

- DTO missing required governance fields.  
- Inconsistent temporal data.  
- Malformed geometry.  
- Missing or broken provenance.

Test locations:

~~~text
tests/unit/web/features/focus-mode/pipelines/**
tests/integration/web/features/focus-mode/**
~~~

All pipeline changes MUST pass full pipeline test suites.

---

## 🧠 Data Flow Diagram (Pipeline Wrapper Context)

*(Use ```mermaid``` in repo; `~~~mermaid` here preserves the top-level fence.)*

~~~mermaid
flowchart LR
    ID[Entity ID] --> RUN[runFocusPipeline]
    RUN --> GP[Global focusPipeline.ts]
    GP --> DTO[Focus DTO<br/>Narrative · Spatial · Temporal · Relations · Governance]
    DTO --> VM[View-Model Transformation]
    VM --> GOV[Governance Guard]
    GOV --> STATE[Focus Mode State Slices]
    STATE --> UI[Focus Mode UI Components]
    GOV --> TEL[Telemetry Events]
~~~

---

## 🕰 Version History

| Version | Date       | Summary                                                                                                                   |
|--------:|------------|---------------------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-30 | Upgraded to KFM-MDP v11.2.2; aligned with Focus Mode v3, telemetry v2, FAIR+CARE v11, and energy/carbon pipeline metrics. |
| v10.4.0 | 2025-11-15 | Created full Focus Mode pipeline wrapper specification for v2.5.                                                          |
| v10.3.2 | 2025-11-14 | Added governance + provenance enforcement requirements.                                                                   |
| v10.3.1 | 2025-11-13 | Initial feature-level pipeline wrapper scaffold.                                                                          |

---

## ⚖️ Footer

<div align="center">

**Kansas Frontier Matrix — Focus Mode Pipelines**  
🔄 Deterministic Orchestration · 🛡️ FAIR+CARE Enforcement · 🧠 Explainable Focus Flows  

[← Back to Focus Mode Feature](../README.md) •  
[✨ Web Features Index](../../README.md) •  
[🛡 Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

© 2025 Kansas Frontier Matrix — MIT License  

**End of Document**

</div>