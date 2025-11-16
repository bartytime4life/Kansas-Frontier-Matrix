---
title: "🧬 Kansas Frontier Matrix — Focus Mode State Architecture (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/features/focus-mode/state/README.md"
version: "v10.4.0"
last_updated: "2025-11-15"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/web-feature-focusmode-state-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.1"
status: "Active / Enforced"
doc_kind: "State Layer"
intent: "focus-mode-state"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Entity-Dependent"
sensitivity_level: "Medium"
public_exposure_risk: "Low–Medium"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"
risk_category: "Mixed"
redaction_required: true
provenance_chain:
  - "web/src/features/focus-mode/state/README.md@v10.3.2"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E7 Activity"
  schema_org: "SoftwareApplication"
  owl_time: "TemporalEntity"
  prov_o: "prov:Activity"
json_schema_ref: "../../../../../schemas/json/web-feature-focusmode-state.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/web-feature-focusmode-state-shape.ttl"
doc_uuid: "urn:kfm:doc:web-feature-focusmode-state-v10.4.0"
semantic_document_id: "kfm-doc-web-feature-focusmode-state"
event_source_id: "ledger:web/src/features/focus-mode/state/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "a11y-adaptations"
  - "semantic-highlighting"
ai_transform_prohibited:
  - "summaries"
  - "speculative additions"
  - "unverified historical claims"
  - "inferred relationships"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "United States / Kansas"
classification: "Public Document"
role: "state-management"
lifecycle_stage: "stable"
ttl_policy: "Annual review"
sunset_policy: "Superseded upon Focus Mode v3 state refactor"
---

<div align="center">

# 🧬 **Kansas Frontier Matrix — Focus Mode State Architecture**  
`web/src/features/focus-mode/state/README.md`

**Purpose:**  
Define the **state layer** that powers Focus Mode v2.5 — including entity state,  
explainability vectors, spatial highlight state, and local temporal state —  
deterministically, accessibly, and in full compliance with FAIR+CARE governance.

</div>

---

# 📘 Overview

The **state layer** for Focus Mode provides:

- Global + feature-scoped state slices  
- Deterministic state transitions  
- Shared, predictable access to Focus Mode data  
- Integration with the pipelines + hooks layer  
- Governance-aware redaction, gating, and masking  
- Rich telemetry integration  
- Zero JSX or UI concerns (pure logic)  

Focus Mode uses **Zustand (recommended)** or React Context-based reducers to maintain:

- what entity is in focus  
- how its narrative is represented  
- explainability metadata  
- map highlight geometry (masked/generalized)  
- time interval highlighting  
- provenance chains  
- loading/error lifecycle states  
- A11y indicators  

All state must be **serializable**, **stable**, and **testable**.

---

# 🧱 Directory Structure

~~~text
web/src/features/focus-mode/state/
├── focusState.ts              # Core Focus Mode state: entity, narrative, metadata, governance
├── explainabilityState.ts     # SHAP/LIME explainability vectors + metadata
├── spatialState.ts            # Spatial highlight state (masked geometry + centroids)
├── timelineState.ts           # Local temporal state (intervals/fuzzy/open-ended)
└── README.md                  # This document
~~~

> These files represent **state slices**, not full UI or pipelines.

---

# 🧩 State Slice Responsibilities

---

## 🔹 `focusState.ts`

Primary Focus Mode state manager.

Stores:

- Current focused entity (ID + type)
- Raw DTO (sanitized)
- Focus view-model
- Narrative summary (with AI flags)
- Governance metadata:
  - CARE classification  
  - sovereignty flags  
  - masking requirements  
- Provenance summaries
- Loading/error states

Rules:

- MUST use type guards before writing state  
- MUST mark AI-generated text as `aiGenerated: true`  
- MUST mask or generalize sensitive fields before storing  
- MUST store provenance chains intact (no truncation)  
- MUST reject DTOs missing governance metadata  

Telemetry emitted via hooks:

- `"focus:open"`
- `"focus:entity-load"`
- `"focus:entity-error"`

---

## 🔹 `explainabilityState.ts`

Stores:

- SHAP/LIME explanation arrays  
- feature attribution rankings  
- uncertainty weights  
- model identity (model name, version)  
- explainability visibility state  

Governance rules:

- Explainability must be labeled as **model-derived**  
- No inferred relationships stored in state  
- No speculative expansion of attributions  

Telemetry:

- `"focus:explanation-open"`
- `"focus:explanation-metric-view"`

---

## 🔹 `spatialState.ts`

Stores:

- spatial highlight geometry  
- masked geometry  
- generalized centroids  
- bounding boxes  
- layer IDs for MapView  
- highlight visibility toggles  

Governance constraints:

- Raw coordinates for sensitive locations must **never** be stored  
- Only generalized/masked geometry may enter state  
- Sovereignty flags must be stored alongside geometry  

Integration points:

- `geospatial/masking.ts`  
- `geospatial/footprint.ts`  
- `geospatial/layers.ts`  
- MapContext  

Telemetry:

- `"focus:highlight-on"`
- `"focus:highlight-off"`
- `"focus:masking-applied"`

---

## 🔹 `timelineState.ts`

Stores:

- time interval for the focused entity  
- fuzzy/open-ended intervals  
- state for timeline → focus synchronization  
- derived labels for UI (e.g., “early 1800s”, “~1850”, “unknown”)  

Rules:

- Must maintain OWL-Time compatible formatting  
- Fuzzy values must be marked with `fuzzy: true`  
- Missing dates must be represented as `"unknown"`  

Telemetry:

- `"focus:timeline-highlight-enabled"`
- `"focus:timeline-fuzzy-range"`

---

# 🔐 FAIR+CARE Governance Enforcement

The state layer is responsible for handling **the riskiest parts** of the Focus Mode feature  
— making governance here **mandatory and enforced**.

Focus Mode state **must enforce**:

### ✔ Masking of sensitive geometry  
No raw coordinates may reach UI state if CARE/sovereignty flags prohibit it.

### ✔ Preservation of CARE + sovereignty metadata  
State must store these early so UI cannot accidentally hide them.

### ✔ Provenance chain integrity  
No link may be removed, truncated, or overwritten.

### ✔ Labeling of AI-generated narrative  
State must store `aiGenerated: true` so UI can show banners.

### ✔ No speculative filling of missing data  
If backend did not provide it, state must not invent it.

### ✔ Timeline uncertainty and fuzzy precision  
Must store exact metadata so UI handles it correctly.

Governance violations here lead to **CI hard failures**, not soft warnings.

---

# ♿ Accessibility Requirements

State slices must enable A11y-compliant UI by providing:

- clear loading/error states  
- flags for fuzzy/uncertain data  
- textual alternatives to spatial/temporal content  
- boolean flags to show/hide complex visualization regions  
- props for keyboard-focused features (e.g., narrations, relations)  

The state layer **does not implement A11y** but **makes it possible**.

---

# 📈 Telemetry Integration

Focus Mode state slices must expose standardized telemetry hooks for:

- entity selection  
- relation expansion  
- explainability views  
- spatial highlight events  
- masking activation  
- sovereignty notices  
- temporal highlight events  

Events must match schemas in:

```

types/telemetry.ts
schemas/telemetry/web-feature-focusmode-hooks-v1.json

```

No PII or exact coordinates may enter telemetry.

---

# 🧪 Testing Requirements

State slices must include:

### ✔ Unit Tests
- default state  
- transitions  
- edge cases  
- governance-driven branches  

### ✔ Integration Tests
- run through pipeline → hooks → state transitions  
- verify masking logic  
- ensure fuzzy temporal definitions propagate correctly  
- ensure provenance stays intact  

### ✔ Negative Path Tests
- malformed DTOs  
- missing CARE metadata  
- invalid geometries  
- missing temporal bounds  

Tests live in:

```

tests/unit/web/features/focus-mode/state/**
tests/integration/web/features/focus-mode/**

```

---

# 🕰 Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v10.4.0 | 2025-11-15 | Added full Focus Mode state layer documentation; aligned with KFM pipelines |
| v10.3.2 | 2025-11-14 | Added governance-first state constraints |
| v10.3.1 | 2025-11-13 | Initial state scaffold added |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
FAIR+CARE Certified · Public Document · Version-Pinned  
Validated under MCP-DL v6.3 & KFM-MDP v10.4.1  

</div>
