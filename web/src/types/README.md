---
title: "🧾 Kansas Frontier Matrix — Web Types Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/types/README.md"
version: "v10.4.0"
last_updated: "2025-11-15"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/web-types-readme-v1.json"
governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.1"
status: "Active / Enforced"
doc_kind: "Overview"
intent: "web-types-overview"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk (unless typing redacted CARE fields)"
sensitivity_level: "None"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false
provenance_chain:
  - "web/src/types/README.md@v10.3.2"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E28 Conceptual Object"
  schema_org: "DefinedTerm"
  owl_time: "TemporalEntity"
  prov_o: "prov:Entity"
json_schema_ref: "../../../schemas/json/web-types-readme.schema.json"
shape_schema_ref: "../../../schemas/shacl/web-types-readme-shape.ttl"
doc_uuid: "urn:kfm:doc:web-types-readme-v10.4.0"
semantic_document_id: "kfm-doc-web-types-readme"
event_source_id: "ledger:web/src/types/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative typing"
  - "synthetic type inference"
  - "unverified historical claims"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "United States / Kansas"
classification: "Public Document"
role: "overview"
lifecycle_stage: "stable"
ttl_policy: "Annual review"
sunset_policy: "Superseded upon next type-system revision"
---

<div align="center">

# 🧾 **Kansas Frontier Matrix — Web Types Overview**  
`web/src/types/README.md`

**Purpose:**  
Define the type system that underpins all TypeScript-powered behavior in the  
Kansas Frontier Matrix Web Platform (`web/src/types/**`).  
Types ensure deterministic, FAIR+CARE-governed, and semantically correct modeling  
of data exchanged between UI components, hooks, pipelines, backend APIs, and the  
knowledge graph.

</div>

---

# 📘 Overview

The `types/` directory provides:

- **Shared TypeScript interfaces, enums, and type aliases**
- **Canonical data modeling** for STAC, DCAT, Story Nodes, Focus Mode payloads, UI state, and spatial metadata
- **Strict typing for governance and CARE metadata**
- **Typed DTOs** used by `services/` to communicate with backend APIs
- **Schema-derived types** mapped from JSON schemas and SHACL shapes
- **Non-speculative modeling** (no invented fields, no assumed relationships)
- **Machine-extractable, stable definitions** that drive:
  - component props
  - pipeline orchestration
  - context state
  - telemetry schemas
  - provenance modeling

Everything in this directory exists to **guarantee correctness, safety, and predictability**  
across the entire Web Platform.

---

# 🧱 Directory Structure (Labeled)

~~~text
web/src/types/
├── api.ts                    # DTOs for REST/GraphQL/STAC/DCAT backend responses
├── domain.ts                # Domain entities (StoryNode, Dataset, Place, Event)
├── governance.ts            # CARE labels, sovereignty flags, provenance shapes
├── spatial.ts               # Bounding boxes, GeoJSON shapes, H3 masks
├── temporal.ts              # OWL-Time aligned temporal types
├── ui.ts                    # UI-level component props shared across systems
├── telemetry.ts             # Telemetry event shapes (schema-derived)
├── focus.ts                # Focus Mode v2.5 narrative + relational payload types
├── story.ts                 # Story Node v3 narrative + spatial + temporal types
├── stac.ts                  # STAC v1.0 Collection, Item, Asset, Link types
├── dcat.ts                  # DCAT v3 Dataset, Distribution, Catalog types
└── index.ts                 # Re-export barrel (central type surface)
~~~

---

# 🧩 Module Responsibilities

## 📡 **api.ts**
Defines typed backend responses:

- REST DTOs  
- GraphQL fragments  
- STAC item/collection shapes  
- DCAT v3 responses  
- Provenance/bibliographic metadata  

Guarantees:

- No untyped API calls  
- No implicit fields  
- All types derived from backend schemas  

---

## 🧬 **domain.ts**
Provides shared domain models, including:

- `StoryNode`  
- `Dataset`  
- `Place`  
- `Event`  
- `Person`  
- `GraphRelation`  

Guarantees:

- Non-speculative fields only  
- Strong typing used by components, pipelines, and features  

---

## 🛡 **governance.ts**
Defines:

- CARE labels  
- Sovereignty restrictions  
- Redaction flags  
- Provenance chain structures  
- Data stewardship attribution  

Guarantees:

- No component can ignore governance metadata  
- All data surfaces properly reflect FAIR+CARE requirements  

---

## 🌍 **spatial.ts**
Contains:

- GeoJSON types  
- Feature/FeatureCollection  
- BBox, CRS structures  
- H3 masking metadata  
- Map layer metadata  

Governance:

- Any type involving location must declare:
  - masking allowance
  - sovereignty flags
  - provenance tokens  

---

## ⏳ **temporal.ts**
Defines:

- OWL-Time compatible intervals  
- Temporal extents  
- Uncertainty/fuzziness flags  
- Story Node temporal bundling  

Guarantees:

- Correct alignment across timeline, map, and narrative systems  

---

## 🧩 **ui.ts**
Shared component-agnostic UI types:

- Panel states  
- Drawer states  
- Keyboard/mouse event wrappers  
- A11y state flags  
- Component prop primitives  

---

## 📈 **telemetry.ts**
Defines telemetry event structures:

- `"ui:*"`  
- `"map:*"`  
- `"timeline:*"`  
- `"story:*"`  
- `"focus:*"`  
- `"stac:*"`  

All telemetry types are:

- Non-PII  
- Schema-validated  
- CARE-aware  

---

## 🎯 **focus.ts**
Types for Focus Mode v2.5:

- Narrative bundles  
- Graph neighbors  
- Provenance summaries  
- Spatial highlight descriptors  

Ensures deterministic Focus Mode orchestration.

---

## 📖 **story.ts**
Typed Story Node v3 definitions:

- Narrative  
- Temporal ranges  
- Spatial footprints  
- Relations  
- Provenance metadata  

Focused on correctness & ethical narrative representation.

---

## 🗂 **stac.ts**
STAC v1.0 specification mapped to TypeScript:

- STAC Item  
- Collection  
- Asset  
- Link  
- Extent  

Including KFM-specific governance wrappers.

---

## 📦 **dcat.ts**
DCAT v3 mappings:

- Dataset  
- Distribution  
- Catalog  
- Keyword and thematic roles  

---

## 🔗 **index.ts**
Single export surface for all type modules.

Used by the rest of the Web Platform to maintain strong modular boundaries.

---

# 🔐 Governance & FAIR+CARE Requirements

All types must:

- Represent only verified, non-speculative fields  
- Include governance metadata when modeling sensitive entities  
- Declare masking/sovereignty requirements for spatial/temporal data  
- Maintain provenance type associations  
- Align with backend JSON Schemas and GraphQL SDL  
- Avoid modeling hypothetical or inferred relationships  

Governance violations by the type layer create **system-wide CI failures**.

---

# ♿ Accessibility Requirements

Type definitions must enable components to:

- Convey semantic information  
- Support ARIA labeling  
- Express visible & non-visible UI semantics  
- Avoid ambiguous or overloaded meaning  

Types should support both visual and nonvisual representations.

---

# 🧪 Testing Expectations

Testing must ensure:

- All exported types compile under strict TypeScript  
- No circular imports  
- No unused or deprecated domain types  
- API DTOs match backend schema snapshots  
- Telemetry types match telemetry schemas  

Tools involved:

- TypeScript compiler  
- JSON schema validators  
- CI schema diffing tools  

---

# 🕰 Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v10.4.0 | 2025-11-15 | Full KFM-MDP v10.4.1-compliant types overview; labeled modules; governance-aligned typing rules |
| v10.3.2 | 2025-11-14 | Added STAC/DCAT + Focus Mode v2.5 types |
| v10.3.1 | 2025-11-13 | Base type directory established |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
FAIR+CARE Certified · Public Document · Version-Pinned  
Validated under MCP-DL v6.3 & KFM-MDP v10.4.1  

</div>

