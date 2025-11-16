---
title: "🧩 Kansas Frontier Matrix — Focus Mode View-Models Specification (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/features/focus-mode/view-models/README.md"
version: "v10.4.0"
last_updated: "2025-11-15"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/web-feature-focusmode-viewmodels-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.1"
status: "Active / Enforced"
doc_kind: "Specification"
intent: "focus-mode-view-models"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Entity-Dependent"
sensitivity_level: "Medium"
public_exposure_risk: "Low–Medium"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"
risk_category: "Mixed"
redaction_required: true
provenance_chain:
  - "web/src/features/focus-mode/view-models/README.md@v10.3.2"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "DataModel"
  owl_time: "TemporalEntity"
  prov_o: "prov:Entity"
json_schema_ref: "../../../../../schemas/json/web-feature-focusmode-viewmodels.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/web-feature-focusmode-viewmodels-shape.ttl"
doc_uuid: "urn:kfm:doc:web-feature-focusmode-viewmodels-v10.4.0"
semantic_document_id: "kfm-doc-web-feature-focusmode-viewmodels"
event_source_id: "ledger:web/src/features/focus-mode/view-models/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative additions"
  - "relationship inference"
  - "unverified historical claims"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "United States / Kansas"
classification: "Public Document"
role: "view-model-layer"
lifecycle_stage: "stable"
ttl_policy: "Annual"
sunset_policy: "Superseded upon Focus Mode v3 refactor"
---

<div align="center">

# 🧩 **Kansas Frontier Matrix — Focus Mode View-Models Specification**  
`web/src/features/focus-mode/view-models/README.md`

**Purpose:**  
Define the **UI-ready data structures** (View-Models) for Focus Mode v2.5.  
View-models are **pure, typed, deterministic representations** of Focus Mode data, produced from  
DTO inputs and pipelines, and consumed by React components in `components/FocusMode/**`.

They ensure:
- consistent UI behavior,  
- full FAIR+CARE governance alignment,  
- spatial + temporal safety,  
- accessible and explainable outputs.

</div>

---

# 📘 Overview

The **view-model layer** converts raw data (DTOs, Story Nodes, provenance, explainability vectors, footprints) into:

- safe, normalized, UI-ready objects  
- masked / generalized geometry  
- fuzzy/open-ended temporal ranges  
- flattened provenance chains  
- grouped and typified relations  
- explainability metadata suitable for rendering  
- narrative structures with AI-labeling flags  

View-models **never** contain JSX, business logic, network calls, or speculation.

They are **the single source of truth** for Focus Mode rendering.

---

# 🧱 Directory Structure

~~~text
web/src/features/focus-mode/view-models/
├── FocusViewModel.ts            # Root model for Focus Mode v2.5
├── RelationsViewModel.ts        # Relation grouping & typed relation model
├── ExplainabilityVM.ts          # Explainability (SHAP/LIME) rendering model
├── StoryNodeVM.ts               # Light-weight Story Node projection for Focus Mode
├── ProvenanceVM.ts              # Flattened provenance chain for UI display
└── README.md
~~~

---

# 🧩 View-Model Modules

---

## 🎯 `FocusViewModel.ts` — Root Focus Mode View-Model

Represents the **full structured output** of Focus Mode v2.5.

Includes:

- `id`, `entityType`, `title`, `summary`  
- `narrative` (with `aiGenerated` + `provenanceSource` flags)  
- `spatial`:
  - masked geometry  
  - centroid  
  - bounding boxes  
  - sovereignty flags  
- `temporal`:  
  - start/end/fuzzy/open-ended  
  - OWL-Time compatible metadata  
- `relations`: relation groups from `RelationsViewModel`  
- `storyNodes`: projected Story Node subsets  
- `explainability`: SHAP/LIME vectors via `ExplainabilityVM`  
- `care`: CARE classification + sovereignty metadata  
- `provenance`: flattened chain from `ProvenanceVM`

Governance logic guarantees:

- No precise coordinates for sensitive entities  
- Clear AI labeling  
- Provenance integrity  

---

## 🔗 `RelationsViewModel.ts` — Entity Relationship Model

Represents:

- Related entities grouped by category (people, places, events, datasets, story nodes)  
- Each relation entry includes:
  - `id`, `label`, `entityType`  
  - CARE flags  
  - sovereignty status (if place)  
  - fuzzy/uncertain time flags (if event)  
  - minimal spatial hint (if needed)  

Rules:

- No inferred relationships  
- All relations **must come from backend**  
- Groups must be typed + labeled deterministically  

---

## 🧠 `ExplainabilityVM.ts` — Explainability View-Model

Converts backend explainability payload into:

- simplified vectors  
- ranked contributing attributes  
- human-friendly labels  
- scaled influence weights  
- color-safe values for UI heatmaps (WCAG AA compliant)

Governance:

- All explainability must be labeled as **model-derived**  
- No speculative rewrite of the model’s attribution scores  

---

## 📚 `StoryNodeVM.ts` — Story Node Projection View-Model

Provides a **lightweight projection** of Story Node v3 for Focus Mode.

Includes:

- `id`, `title`, `summary`  
- temporal range (fuzzy/open accepted)  
- masked/generalized footprint  
- provenance summary  
- CARE classification  
- map preview hints  

Used for:

- relation recommendations  
- timeline highlights  
- Focus Mode narrative context panel  

---

## 🧬 `ProvenanceVM.ts` — Provenance Chain View-Model

Represents the entire provenance chain in a flattened structure.

Includes:

- source entities  
- licenses  
- transformations  
- responsible organizations or data stewards  
- derived-from links  
- uncertainty flags  
- evidence metadata  

Governance requirements:

- No provenance link may be removed  
- Unverified provenance must be labeled  
- Provenance source identities must NOT map to real individuals unless public/legal  

Displayed in:

- `ProvenancePanel.tsx`  
- `ProvenanceChip.tsx`  

---

# 🔐 Governance & FAIR+CARE Requirements

The view-model layer is **one of the core governance enforcement checkpoints**.

All view-models must ensure:

### ✔ Sensitive geometry is masked / generalized  
### ✔ CARE labels are preserved and surfaced  
### ✔ Sovereignty flags are carried through  
### ✔ Provenance metadata is preserved + visible  
### ✔ AI narrative content is clearly labeled  
### ✔ No unverified history is invented  
### ✔ No inferred relationships or coordinates  
### ✔ No raw coordinates for sensitive entities  
### ✔ All uncertain temporal data is tagged  

Failing to enforce these rules → CI BLOCK.

---

# ♿ Accessibility Requirements

View-models provide metadata required by UI to meet WCAG 2.1 AA:

- flags for fuzzy time  
- textual equivalents for spatial previews  
- labels for explainability vectors  
- assisted navigation hints for Focus Mode panels  
- states for SR-only descriptions  

View-models must ensure that every UI component has what it needs to be accessible.

---

# 📈 Telemetry Integration

View-models feed telemetry by:

- indicating when certain views are shown (explainability, story nodes, relations)  
- exposing governance metadata used in telemetry analysis  
- enabling `"focus:*"` event generation in hooks  

They must:

- NEVER include PII  
- NEVER include precise sensitive coordinates  
- ALWAYS work with schemas in `types/telemetry.ts`  

---

# 🧪 Testing Requirements

Each view-model requires:

### ✔ Unit tests
- DTO → VM transforms  
- governance enforcement  
- masking behavior  
- temporal normalization  
- provenance flattening  

### ✔ Integration tests
- pipeline → view-model → UI behavior  
- spatial masking  
- timeline sync  
- explainability mapping  

Tests live in:

```

tests/unit/web/features/focus-mode/view-models/**
tests/integration/web/features/focus-mode/**

```

---

# 🕰 Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v10.4.0 | 2025-11-15 | Fully defined Focus Mode v2.5 view-model architecture; enforce CARE + provenance | 
| v10.3.2 | 2025-11-14 | Added explainability + provenance support |
| v10.3.1 | 2025-11-13 | Initial view-model scaffolding |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
FAIR+CARE Certified · Public Document · Version-Pinned  
Validated under MCP-DL v6.3 & KFM-MDP v10.4.1  

</div>
