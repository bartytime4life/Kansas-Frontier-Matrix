---
title: "🧾 Kansas Frontier Matrix — Web Types Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/types/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"
review_cycle: "Quarterly · FAIR+CARE Council & Web Architecture Board"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../releases/v11.2.2/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/web-types-readme-v11.json"
governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"

status: "Active / Enforced"
doc_kind: "Overview"
intent: "web-types-overview"
role: "type-system"
category: "Web · Types · Architecture"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk (unless typing redacted CARE fields)"
sensitivity_level: "None"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false

provenance_chain:
  - "web/src/types/README.md@v10.4.0"
  - "web/src/types/README.md@v10.3.2"
provenance_requirements:
  versions_required: true
  newest_first: true

ontology_alignment:
  cidoc: "E28 Conceptual Object"
  schema_org: "DefinedTerm"
  owl_time: "TemporalEntity"
  prov_o: "prov:Entity"

json_schema_ref: "../../../schemas/json/web-types-readme.schema.json"
shape_schema_ref: "../../../schemas/shacl/web-types-readme-shape.ttl"

doc_uuid: "urn:kfm:doc:web-types-readme:v11.2.2"
semantic_document_id: "kfm-doc-web-types-readme"
event_source_id: "ledger:web/src/types/README.md"
immutability_status: "version-pinned"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative typing"
  - "synthetic type inference"
  - "unverified historical claims"
  - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "United States / Kansas"
classification: "Public Document"
lifecycle_stage: "stable"
ttl_policy: "Annual review"
sunset_policy: "Superseded upon next type-system revision"
---

<div align="center">

# 🧾 **Kansas Frontier Matrix — Web Types Overview (v11.2.2)**  
`web/src/types/README.md`

**Purpose:**  
Define the **type system** that underpins all TypeScript-powered behavior in the  
Kansas Frontier Matrix Web Platform (`web/src/types/**`).  
Types ensure **deterministic, FAIR+CARE-governed, semantically correct modeling**  
of data exchanged between UI components, hooks, pipelines, backend APIs, and the  
knowledge graph — including Story Node v3, Focus Mode v3, STAC/DCAT, and governance overlays.

</div>

---

# 📘 Overview

The `types/` directory provides:

- 🧾 **Shared TypeScript interfaces, enums, and type aliases**  
- 🧬 **Canonical data modeling** for:
  - Story Node v3
  - Focus Mode v3 payloads
  - STAC v1.x and DCAT v3
  - UI state, spatial/temporal metadata
- 🛡️ **Strict typing for governance & CARE metadata**
- 🌐 **Typed DTOs** used by `services/` and `pipelines/` to communicate with backend APIs
- 📐 **Schema-derived types** mapped from JSON Schemas and SHACL shapes
- 🚫 **Non-speculative modeling** (no invented fields, no assumed relationships)
- 🧺 **Machine-extractable, stable definitions** driving:
  - Component props
  - Pipeline orchestration
  - Context state
  - Telemetry schemas
  - Provenance models

Everything in this directory exists to **guarantee correctness, safety, and predictability**  
across the entire Web Platform.

---

# 🧱 Directory Structure (Emoji-Rich · v11.2.2)

~~~text
web/src/types/
├── 🌐 api.ts          # DTOs for REST/GraphQL/STAC/DCAT backend responses
├── 🧬 domain.ts       # Domain entities (StoryNode, Dataset, Place, Event, Person, etc.)
├── 🛡 governance.ts   # CARE labels, sovereignty flags, provenance & restriction shapes
├── 🌍 spatial.ts      # Bounding boxes, GeoJSON, Feature/Collection, H3 masks, CRS
├── ⏳ temporal.ts     # OWL-Time aligned temporal types & fuzzy intervals
├── 🖥 ui.ts           # UI-level types (props, panel states, A11y flags, layout primitives)
├── 📈 telemetry.ts    # Telemetry event shapes (schema-derived, non-PII)
├── 🎯 focus.ts        # Focus Mode v3 focal payloads, related entities, context windows
├── 📖 story.ts        # Story Node v3 narrative + spatial + temporal + provenance types
├── 📦 stac.ts         # STAC v1.x Collection, Item, Asset, Link, Extent mappings
├── 🗂 dcat.ts         # DCAT v3 Dataset, Distribution, Catalog, Theme mappings
└── 🔗 index.ts        # Re-export barrel (central type surface)
~~~

---

# 🧩 Module Responsibilities

## 🌐 `api.ts` — Backend DTOs

Defines typed backend response shapes for:

- REST endpoints (JSON)  
- GraphQL queries/mutations  
- Focus/Story orchestrator endpoints  
- STAC Collections/Items metadata  
- DCAT v3 datasets/distributions  
- Provenance & bibliographic metadata  

**Guarantees**

- All external API calls have strongly-typed DTOs  
- No “any” usage for backend payloads  
- DTOs track **exact** schema fields (no speculation)  

---

## 🧬 `domain.ts` — Core Domain Models

Provides shared domain models including:

- `StoryNode`  
- `Dataset`  
- `Place`  
- `Event`  
- `Person`  
- `GraphRelation`  
- `HazardLayer`  
- `TemporalCluster`  

Used by:

- Focus Mode v3  
- Story Node components & pipelines  
- Timeline & map overlays  
- Graph utilities in `web/src/utils/graph/**`  

---

## 🛡 `governance.ts` — Governance & CARE Typing

Defines types for:

- CARE labels (`Public`, `Restricted`, `Indigenous-governed`, etc.)  
- Sovereignty flags and heritage metadata  
- Redaction & masking flags  
- Provenance chain structures (PROV-O aligned)  
- Data stewardship tags  

**Guarantees**

- All governance metadata is explicitly typed, never “just a string”  
- Higher layers cannot silently omit governance fields without TypeScript errors  

---

## 🌍 `spatial.ts` — Spatial & CRS Types

Contains types for:

- GeoJSON `Geometry`, `Feature`, `FeatureCollection`  
- `BBox` and `LatLng` primitives  
- CRS descriptors (EPSG codes, vertical datum hints)  
- H3 masks & resolution-level descriptors  
- Map layer spatial configs (extent, zoom, mask metadata)  

Governance:

- Spatial types for sensitive datasets **must** carry:
  - Masking configuration  
  - CARE & sovereignty flags  
  - Provenance tokens  

---

## ⏳ `temporal.ts` — Temporal & OWL-Time Types

Defines:

- OWL-Time-compatible intervals (`TimeInstant`, `TimeInterval`)  
- Temporal extents and coverage info  
- Approximation/fuzziness flags (`approx`, `precision`)  
- Story Node temporal bundles (`StoryTimeSpan`)  
- Timeline band descriptors  

Guarantees:

- UI & backend share a single source-of-truth for temporal semantics  
- Fuzzy ranges are never silently converted to precise instants  

---

## 🖥 `ui.ts` — UI-Level Types

Shared component-agnostic UI primitives:

- Panel states & layout modes  
- Drawer, modal, sheet, and overlay states  
- A11y flags (high contrast, reduced motion, large text)  
- Input and navigation event wrappers  
- Generic prop types for cross-cutting UI patterns  

---

## 📈 `telemetry.ts` — Telemetry Event Types

Defines structured telemetry events:

- `"ui:*"` — interactions, navigation, A11y usage  
- `"map:*"` — pan/zoom patterns, layer toggles (non-PII)  
- `"timeline:*"` — range changes, zoom levels, selection patterns  
- `"story:*"` — Story Node view events  
- `"focus:*"` — Focus Mode context loads  
- `"stac:*"` — dataset preview & selection events  

All telemetry types:

- Are **non-PII**  
- Match telemetry schemas under `schemas/telemetry/**`  
- Respect FAIR+CARE requirements  

---

## 🎯 `focus.ts` — Focus Mode v3 Types

Typed shapes for Focus Mode v3:

- Focal entity descriptor (`FocusTarget`)  
- Related entities (Places, Events, StoryNodes, Datasets)  
- Context windows (temporal + spatial)  
- Governance overlays (CARE, sovereignty, risk flags)  

Used by:

- `FocusContext`  
- `focusPipeline`  
- `focusClient` and `focusBindings`  

Ensures deterministic Focus Mode state and safe integration with the UI.

---

## 📖 `story.ts` — Story Node v3 Types

Defines:

- `StoryNode` core shape (title, summary, narrative body)  
- Temporal structures (time spans, fuzziness, original labels)  
- Spatial structures (geometry, bbox, H3 mask references)  
- Relations (linked entities, datasets, events)  
- Provenance metadata (sources, rights, model references if AI is used)  

Guarantees:

- Story Nodes have explicit and auditable fields  
- Narrative rendering is bounded by well-typed structures  

---

## 📦 `stac.ts` — STAC v1.x Types

Maps STAC concepts to TypeScript:

- `StacCollection`  
- `StacItem`  
- `StacAsset`  
- `StacLink`  
- `StacExtent`  

Includes:

- KFM-specific governance wrappers (licenses, CARE labels)  
- Spatial/temporal extent fields with typed constraints  

---

## 🗂 `dcat.ts` — DCAT v3 Types

Models DCAT v3 constructs:

- `DcatDataset`  
- `DcatDistribution`  
- `DcatCatalog`  
- Thematic & keyword tags  

DCAT types must align with `KFM-DCAT v11` profile.

---

## 🔗 `index.ts` — Barrel Exports

Exports all type modules:

- Ensures a single **stable import point** for the rest of the web codebase  
- Allows downstream code to treat the type system as a **coherent surface**  

---

# 🔐 Governance & FAIR+CARE Requirements

All types MUST:

- Represent only **verified, non-speculative fields**  
- Include governance metadata for sensitive entities (or be explicit about its absence)  
- Distinguish:
  - archival vs. derived vs. AI-generated content  
- Support sovereignty/masking flows by design (`governance.ts`, `spatial.ts`)  
- Align with backend JSON Schemas, GraphQL SDL, and ontology profiles (CIDOC, OWL-Time, STAC/DCAT)  

If a type attempts to model something that is:

- unsupported by backend schema, or  
- a speculative relationship,  

→ it must be rejected in review and never merged.

---

# ♿ Accessibility Expectations

Type definitions must allow components to:

- Express semantics to assistive technologies (ARIA-driven props, state)  
- Distinguish visible vs. non-visible UI semantics  
- Represent A11y modes (e.g., high contrast, reduced motion, large text) clearly  

Types must not:

- Conflate visual-only concepts with structural semantics  
- Make it impossible to build accessible components (e.g., missing fields for labels or roles)  

---

# 🧪 Testing Expectations

The type system is primarily validated via:

- TypeScript strict compilation (`tsc --noEmit`)  
- Schema compatibility checks (JSON Schema ↔ TS types)  
- Telemetry schema alignment tests  
- Linting for unused/dead types  

CI will:

- Fail if new API payloads don’t have corresponding types  
- Fail if schema snapshots and TS types drift  

---

# 🕰 Version History

| Version | Date       | Summary                                                                                          |
|--------:|------------|--------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-28 | Upgraded to KFM-MDP v11.2.2; emoji directory; added Focus v3, Story v3, STAC/DCAT v11 alignment; strengthened governance typing. |
| v10.4.0 | 2025-11-15 | KFM-MDP v10.4.1 types overview; labeled modules; governance-aligned typing rules.               |
| v10.3.2 | 2025-11-14 | Added STAC/DCAT + Focus Mode v2.5 types.                                                         |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
FAIR+CARE Certified · Public Document · Version-Pinned  

[⬅️ Back to Web Source Overview](../README.md) · [🌐 Web Platform Overview](../../README.md) · [🛡 Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>