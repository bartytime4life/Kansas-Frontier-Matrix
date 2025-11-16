---
title: "🔄 Kansas Frontier Matrix — Pipeline Converters Specification (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/pipelines/converters/README.md"
version: "v10.4.0"
last_updated: "2025-11-15"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/web-pipelines-converters-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.1"
status: "Active / Enforced"
doc_kind: "Specification"
intent: "web-pipelines-converters"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Dataset-Dependent"
sensitivity_level: "Low–Medium (depending on source)"
public_exposure_risk: "Low"
indigenous_rights_flag: "Conditional"
data_steward: "KFM FAIR+CARE Council"
risk_category: "Mixed"
redaction_required: false
provenance_chain:
  - "web/src/pipelines/converters/README.md@v10.3.1"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "DataTransformation"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
json_schema_ref: "../../../../../schemas/json/web-pipelines-converters.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/web-pipelines-converters-shape.ttl"
doc_uuid: "urn:kfm:doc:web-pipelines-converters-v10.4.0"
semantic_document_id: "kfm-doc-web-pipelines-converters"
event_source_id: "ledger:web/src/pipelines/converters/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Forbidden (no AI inference allowed)"
ai_transform_permissions:
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "summaries"
  - "speculative additions"
  - "entity inference"
  - "relationship inference"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "United States / Kansas"
classification: "Public Document"
role: "specification"
lifecycle_stage: "stable"
ttl_policy: "Annual review"
sunset_policy: "Superseded when pipeline v11 lands"
---

<div align="center">

# 🔄 **Kansas Frontier Matrix — Pipeline Converters Specification**  
`web/src/pipelines/converters/README.md`

**Purpose:**  
Define the **data transformation layer** that converts raw backend DTOs (REST/GraphQL/STAC/DCAT/Focus Mode/Story Node)  
into **typed, normalized, UI-ready domain objects** used by pipelines and components across the KFM Web Platform.  
Converters ensure that **no untyped, unsafe, or non-governed data** enters the UI.

</div>

---

# 📘 Overview

The `converters/` directory provides **pure, deterministic transformation modules** that:

- Map backend responses → strongly typed domain objects  
- Apply governance metadata (CARE, sovereignty, licensing, provenance)  
- Perform spatial generalization (via `geospatial/` pipelines)  
- Normalize temporal extents (OWL-Time–aligned)  
- Construct UI view-models for components  
- Guarantee consistency across:
  - Focus Mode  
  - Story Nodes  
  - Timeline  
  - Map layers  
  - Dataset lists  
  - Governance UI  
- Prevent components from knowing API-layer details  

Converters **must not**:

- Perform API calls  
- Render UI  
- Produce side effects  
- Invent or infer relationships  
- Generate speculative or fabricated metadata  

---

# 🧱 Directory Structure (Labeled)

~~~text
web/src/pipelines/converters/
├── dtoToDomain.ts           # Core mapping: API DTO → internal domain entity
├── stacToLayer.ts           # Convert STAC Items → MapView layer defs + metadata
├── storyToTimeline.ts       # Convert Story Nodes → timeline markers/events
├── focusToView.ts           # Focus Mode DTO → UI-ready view-model for renderer
├── entityResolver.ts        # Normalize entity references across systems (Story/Focus/Map)
└── README.md                # This document
~~~

---

# 🧩 Converter Modules

---

## 🔄 `dtoToDomain.ts`
**Purpose:** Convert raw API DTOs into normalized domain objects.

Handles:

- Dataset DTOs  
- Story Node DTOs  
- Entity DTOs (Place/Person/Event)  
- Provenance chains  
- Licensing metadata  

Ensures:

- Only schema-valid data proceeds  
- CARE flags are maintained  
- Spatial + temporal fields normalized  
- No speculative fields added  

---

## 🗺️ `stacToLayer.ts`
**Purpose:** Convert STAC Items → Map layers for MapView.

Produces:

- Layer definitions  
- Footprint geometries  
- Temporal coverage  
- Provenance chips  
- CARE-safe geometry generalization (using `geospatial/masking.ts`)  

Ensures:

- Sensitive footprints are generalized  
- Sovereignty boundaries are honored  
- Licensing displayed correctly  
- UI gets deterministic layer metadata  

---

## 📅 `storyToTimeline.ts`
**Purpose:** Convert Story Node v3 → Timeline markers.

Produces:

- Start/end temporal extents  
- Fuzzy/uncertain time ranges  
- CARE-aware event markers  
- Timeline label text  
- Provenance summary  

Guarantees:

- Timeline markers match backend-vetted time metadata  
- No inferred chronology  
- Temporal uncertainty is visible in UI  

---

## 🎯 `focusToView.ts`
**Purpose:** Convert Focus Mode DTO → UI-ready view-model.

Produces:

- Entity summary  
- Story Node recommendations  
- Explainability metadata (SHAP/LIME)  
- Provenance view-model  
- Highlight geometry for map + timeline  

Ensures:

- Sensitive geometry → generalized  
- CARE flags → visible  
- AI-generated text → labeled  
- No hallucinated relationships or invented attributes  

---

## 🧭 `entityResolver.ts`
**Purpose:** Normalize and unify entity references across systems.

Examples:

- Story Node → Entity ID → Focus Mode entity  
- STAC dataset → Place → Timeline event  
- Provenance → Entity → UI card  

Guarantees:

- Singular source-of-truth entity identity  
- Fully typed entity structure  
- No collisions or inconsistent linking  

No inference allowed — relationships must come directly from backend data.

---

# 🔐 FAIR+CARE Governance Rules

Converters must:

- Preserve CARE labels from backend DTOs  
- Apply appropriate spatial generalization (r7+, depending on sensitivity)  
- Maintain provenance chains intact  
- Not hide or downplay sovereignty warnings  
- Surface necessary warnings in the downstream data structures  

Converters **MAY NOT**:

- Infer missing fields  
- Change CARE classifications  
- Modify historical chronology  
- Create relationships not explicitly in backend data  

---

# ♿ Accessibility Requirements

Converters must:

- Output view-models that allow components to meet WCAG 2.1 AA  
- Preserve alt-text or descriptive text payloads when included in narrative  
- Provide accessible fallback text when values are missing (e.g., “No date available”)  

Converters must not break A11y flows caused by missing or malformed fields.

---

# 📈 Telemetry Considerations

Converters do not send telemetry themselves, but:

- Pipeline-level telemetry relies on stable converted types  
- Errors in conversion may generate telemetry events (schema mismatch, governance block)  
- Changes to view-model structure must be reflected in `types/telemetry.ts` when needed  

---

# 🧪 Testing Expectations

Converters **must** include:

- Unit tests for every conversion path  
- CARE/sovereignty masking tests  
- Temporal normalization tests  
- Provenance chain reconstruction tests  
- Schema guard tests  
- Cross-system entity resolution tests  

Test locations:

~~~text
tests/unit/web/pipelines/converters/**
tests/integration/web/pipelines/converters/**
~~~

---

# 🕰 Version History

| Version | Date       | Summary                                                                |
|--------:|------------|------------------------------------------------------------------------|
| v10.4.0 | 2025-11-15 | Complete converter-layer specification added for KFM-MDP v10.4         |
| v10.3.2 | 2025-11-14 | Stabilized mapping between Story, STAC, and Focus entities             |
| v10.3.1 | 2025-11-13 | Initial converter definitions under old pipeline structure             |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
FAIR+CARE Certified · Public Document · Version-Pinned  
Validated under MCP-DL v6.3 & KFM-MDP v10.4.1  

</div>

