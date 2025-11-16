---
title: "🔄 Kansas Frontier Matrix — Focus Mode Pipeline Specification (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/features/focus-mode/pipelines/README.md"
version: "v10.4.0"
last_updated: "2025-11-15"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/web-feature-focusmode-pipelines-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.1"
status: "Active / Enforced"
doc_kind: "Pipeline Layer"
intent: "focus-mode-pipelines"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Entity-Dependent"
sensitivity_level: "Medium"
public_exposure_risk: "Low–Medium"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"
risk_category: "Mixed"
redaction_required: true
provenance_chain:
  - "web/src/features/focus-mode/pipelines/README.md@v10.3.2"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E7 Activity"
  schema_org: "SoftwareApplication"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
json_schema_ref: "../../../../../schemas/json/web-feature-focusmode-pipelines.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/web-feature-focusmode-pipelines-shape.ttl"
doc_uuid: "urn:kfm:doc:web-feature-focusmode-pipelines-v10.4.0"
semantic_document_id: "kfm-doc-web-feature-focusmode-pipelines"
event_source_id: "ledger:web/src/features/focus-mode/pipelines/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "summaries"
  - "speculative additions"
  - "unverified historical claims"
  - "relationship inference"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "United States / Kansas"
classification: "Public Document"
role: "pipeline-layer"
lifecycle_stage: "stable"
ttl_policy: "Annual"
sunset_policy: "Superseded upon Focus Mode v3 pipeline refactor"
---

<div align="center">

# 🔄 **Kansas Frontier Matrix — Focus Mode Pipeline Specification**  
`web/src/features/focus-mode/pipelines/README.md`

**Purpose:**  
Describe the **feature-scoped pipeline wrappers** that interface Focus Mode’s logic  
(`focusPipeline.ts`) with feature-level hooks and state slices.  
These wrappers ensure deterministic, governance-safe execution of the  
Focus Mode v2.5 entity reasoning flow.

</div>

---

# 📘 Overview

The **Focus Mode pipeline layer** acts as a thin wrapper between:

- The **global pipeline orchestrator** (`web/src/pipelines/focusPipeline.ts`)
- The **feature hooks** (`useFocusEntity`, `useFocusExplainability`, etc.)
- The **feature state slices** (focusState, spatialState, timelineState)
- The **Focus Mode view-models** (FocusViewModel, RelationsViewModel, ExplainabilityVM, etc.)

It is responsible for:

- Executing the full pipeline  
- Normalizing and transforming the result  
- Applying governance gates  
- Updating feature state slices  
- Triggering downstream spatial/temporal sync  
- Emitting telemetry events  

This layer contains **no UI**, **no React components**, and **no direct MapLibre calls** —  
only data coordination and deterministic orchestration.

---

# 🧱 Directory Structure

~~~text
web/src/features/focus-mode/pipelines/
├── runFocusPipeline.ts       # Executes the global focusPipeline + updates feature state
└── README.md                 # This document
~~~

> Additional wrappers may be added in future versions if Focus Mode v3 introduces multi-entity workflows.

---

# 🧩 Module Responsibilities

---

## 🔹 `runFocusPipeline.ts`

This is the **single entrypoint** for Focus Mode v2.5 inside the feature layer.

It coordinates:

1. **Global Focus Pipeline Execution**
   - Calls `web/src/pipelines/focusPipeline.ts`
   - Receives full Focus DTO:  
     - entity  
     - narratives  
     - relations  
     - spatial footprints  
     - temporal ranges  
     - provenance  
     - CARE metadata  
     - explainability payloads  

2. **View-Model Conversion**
   - Converts pipeline output → Focus Mode ViewModels  
   - Uses:
     - `FocusViewModel.ts`
     - `RelationsViewModel.ts`
     - `ExplainabilityVM.ts`
     - `StoryNodeVM.ts`
     - `ProvenanceVM.ts`  

3. **Governance Enforcement**
   - Applies sovereignty/masking rules  
   - Applies CARE classification gating  
   - Rejects or obfuscates restricted fields  
   - Ensures provenance chain integrity  
   - Ensures AI narrative labeling  

4. **State Slice Updates**
   Writes results to:
   - `focusState` → entity, narrative, governance  
   - `spatialState` → masked geometry, centroids, layer IDs  
   - `timelineState` → OWL-Time normalized ranges  
   - `explainabilityState` → SHAP/LIME vectors + metadata  

5. **Spatial Integration**
   Integrates with geospatial pipeline:
   - `masking.ts`
   - `footprint.ts`
   - `layers.ts`
   - `bounds.ts`

6. **Timeline Integration**
   - Updates timeline highlight  
   - Ensures fuzzy/open-ended intervals are properly propagated  

7. **Provenance Integration**
   - Flattens provenance chain  
   - Normalizes PROV-O semantics  

8. **Telemetry Emission**
   Emits:
   - `"focus:open"`
   - `"focus:entity-load"`
   - `"focus:highlight-generated"`
   - `"focus:explainability-available"`
   - `"focus:governance-blocked"` (when gating occurs)

Telemetry must match schemas in:
```

types/telemetry.ts
schemas/telemetry/web-feature-focusmode-hooks-v1.json

```

---

# 🔐 Governance (FAIR+CARE) Requirements

The pipeline wrapper **must enforce** governance rules before updating state:

### Mandatory
- CARE classification propagation  
- Sovereignty masking (H3)  
- Masking of precise coordinates  
- AI narrative labeling  
- Provenance visibility  
- No speculative or inferred history  
- Enforcement of content restrictions from backend  

### Forbidden
- Linking entities not explicitly related  
- Inference of temporal ranges  
- Storage of raw sensitive coordinates  
- Drop of required provenance metadata  
- Alteration of CARE classification  

Any governance failure → **CI BLOCKER**.

---

# ♿ Accessibility Requirements

The wrapper must ensure:

- view-models include A11y metadata required for UI  
- fuzzy/open-ended intervals include descriptive labels  
- masked geometries include textual equivalents  
- explainability vectors include human-readable names  
- provenance chain exposes ARIA-friendly metadata  

---

# 📈 Telemetry Requirements

Pipeline wrappers must:

- emit well-formed telemetry events  
- include governance metadata when relevant  
- avoid PII  
- avoid precise sensitive spatial data  
- ensure consistent event naming across all Focus Mode flows  

Telemetry drives:

- A11y dashboards  
- Sustainability/energy metrics  
- FAIR+CARE compliance logs  
- Focus Mode engagement analytics  

---

# 🧪 Testing Requirements

Tests must cover:

### ✔ Unit Testing (using mocks)
- correct invocation of global `focusPipeline`  
- view-model transformation  
- state updates  
- governance gating  
- telemetry emission  

### ✔ Integration Testing
- full end-to-end: entity → pipeline → state → UI  
- masked geometry correctness  
- timeline highlight synchronization  
- explainability integration  
- Story Node recommendation flows  
- provenance chain correctness  

### ✔ Negative Path Testing
- malformed DTO  
- missing governance fields  
- restricted entity  
- broken geometry  
- broken provenance  

Tests should live in:

```

tests/unit/web/features/focus-mode/pipelines/**
tests/integration/web/features/focus-mode/**

```

---

# 🧠 Data Flow Diagram (Pipeline Wrapper Context)

~~~mermaid
flowchart LR
    ID[Entity ID] --> RUN[runFocusPipeline]
    RUN --> GP[Global focusPipeline.ts]
    GP --> DTO[Focus DTO<br/>Narrative · Spatial · Temporal · Relations]
    DTO --> VM[View-Model Transformation]
    VM --> GOV[Governance Guard]
    GOV --> STATE[Focus Mode State Slices]
    STATE --> UI[Focus Mode UI Components]
    GOV --> TEL["Telemetry Events"]
~~~

---

# 🕰 Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v10.4.0 | 2025-11-15 | Created full Focus Mode pipeline wrapper specification for v2.5 |
| v10.3.2 | 2025-11-14 | Added governance + provenance enforcement requirements |
| v10.3.1 | 2025-11-13 | Initial feature-level pipeline wrapper scaffold |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
FAIR+CARE Certified · Public Document · Version-Pinned  
Validated under MCP-DL v6.3 & KFM-MDP v10.4.1  

</div>
