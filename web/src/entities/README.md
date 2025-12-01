---
title: "👥 Kansas Frontier Matrix — Entities Architecture & Semantic View-Model Layer (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/entities/README.md"
version: "v11.2.2"
last_updated: "2025-11-30"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../releases/v11.2.2/web-entities-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/web-entities-v2.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

status: "Active / Enforced"
doc_kind: "Architecture Overview"
intent: "web-entities-architecture"
role: "overview"

fair_category: "F1-A1-I1-R1"
care_label: "Public / Mixed (entity-dependent)"
sensitivity_level: "Entity-dependent"
public_exposure_risk: "Medium"
indigenous_rights_flag: "Conditional"
data_steward: "KFM FAIR+CARE Council"
risk_category: "Mixed"
redaction_required: true

provenance_chain:
  - "web/src/entities/README.md@v10.3.2"
  - "web/src/entities/README.md@v10.3.1"

ontology_alignment:
  cidoc: "E21 Person / E53 Place / E5 Event / E31 Document"
  schema_org: "CreativeWork / Place / Dataset"
  owl_time: "TemporalEntity"
  geosparql: "geo:Feature"
  prov_o: "prov:Entity"

json_schema_ref: "../../../schemas/json/web-entities-readme-v11.schema.json"
shape_schema_ref: "../../../schemas/shacl/web-entities-readme-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:web-entities-readme-v11.2.2"
semantic_document_id: "kfm-doc-web-entities-readme-v11"
event_source_id: "ledger:web/src/entities/README.md"
immutability_status: "version-pinned"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with constraints"
ai_transform_permissions:
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "diagram-extraction"
  - "metadata-extraction"
ai_transform_prohibited:
  - "summaries"
  - "speculative-additions"
  - "unverified-historical-claims"
  - "governance-override"
  - "content-alteration"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "United States / Kansas"
classification: "Public (semantic layer; entity-sensitive)"

ttl_policy: "Review each major release"
sunset_policy: "Superseded upon Entities Layer v12 refactor"
---

<div align="center">

# 👥 **Kansas Frontier Matrix — Entities Architecture & Semantic View-Model Layer**  
`web/src/entities/README.md`

**Purpose:**  
Define the **Entities Layer** for KFM v11.2.2 — the semantic model that unifies graph data,  
geospatial metadata, temporal ranges, AI reasoning signals, provenance lineage, and  
FAIR+CARE governance into coherent, UI-ready **Entity View Models (EVMs)** used across the Web Platform.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)]()  
[![KFM-MDP v11.2.2](https://img.shields.io/badge/KFM%E2%80%93MDP-v11.2.2-purple)]()  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Entities-orange)]()  
[![License: MIT](https://img.shields.io/badge/License-MIT-green)]()

</div>

---

## 📘 Overview

The **Entities Layer** is the semantic foundation of the Kansas Frontier Matrix.

It transforms heterogeneous backend sources into predictable, typed, FAIR+CARE-certified  
**Entity View Models (EVMs)** that are consumed consistently by:

- **MapView** (2D + 3D highlights, layer filtering)  
- **TimelineView** (temporal ranges, predictive projections)  
- **DetailDrawer** (contextual narratives, metadata, governance)  
- **Focus Mode v3** (entity-centric reasoning + explainability)  
- **Story Nodes** (graph-linked event chains & narratives)  
- **DataCards** (dataset/person/place/event summaries)  
- **Governance UI** (CARE labels, sovereignty flags, provenance lineage)  

The Entities Layer ensures:

- semantic consistency  
- governance correctness  
- provenance completeness  
- accessibility readiness  
- sustainability + telemetry integration  
- deterministic behavior across the UI  

It is **pure semantic/view-model logic** — no React rendering, minimal side effects, no direct network calls.

---

## 🗂️ Directory Layout

~~~text
web/src/entities/
│
├── 📘 README.md
│
├── 👤 people/
│   ├── 🧬 personViewModel.ts      # Person EVM type + factory
│   ├── 🧭 personMapper.ts         # Neo4j/STAC/DCAT → PersonVM mapping logic
│   └── 📝 metadata.json           # Person semantic metadata / schema hints
│
├── 📍 places/
│   ├── 🧬 placeViewModel.ts       # Place EVM type + factory
│   ├── 🧭 placeMapper.ts          # Graph/STAC → PlaceVM + geometry governance
│   └── 📝 metadata.json
│
├── 📅 events/
│   ├── 🧬 eventViewModel.ts       # Event EVM type + factory
│   ├── 🧭 eventMapper.ts          # Graph → EventVM + Story Node alignment
│   └── 📝 metadata.json
│
└── 📦 datasets/
    ├── 🧬 datasetViewModel.ts     # Dataset EVM type + FAIR+CARE licensing model
    ├── 🧭 datasetMapper.ts        # STAC/DCAT → DatasetVM + provenance binding
    └── 📝 metadata.json
~~~

Each subdirectory implements a clear **mapper → view-model → metadata** pattern.

---

## 🧬 Entity View-Model Architecture

> (In-repo, use a real ```mermaid``` block; here we use tildes to keep this one-fence output intact.)

~~~mermaid
flowchart TD
    RAW[Raw Metadata<br/>Neo4j · GraphQL · STAC · DCAT · AI signals] --> MAP[Entity Mappers]
    MAP --> VM[Entity View Models<br/>canonical, FAIR+CARE-certified]
    VM --> UI[UI Systems<br/>Map · Timeline · Drawer · Focus · StoryNodes · DataCards]
    VM --> GOV[Governance Engine<br/>provenance · sovereignty · CARE]
    VM --> TEL[Telemetry Layer<br/>usage · energy · a11y]
~~~

### Core EVM requirements

All EVMs MUST provide:

- **Identity**
  - `id` — global, stable, unique  
  - `label` — human-readable name  
  - `type` — `"person" | "place" | "event" | "dataset"`  

- **Provenance**
  - STAC/DCAT references where applicable  
  - Graph node references (e.g., `neo4j://Person/123`)  
  - PROV-O compatible lineage (entities, activities, agents)  
  - Governance ledger references for decisions applied to this entity  

- **FAIR+CARE**
  - CARE label: `public | sensitive | restricted | sovereignty-controlled`  
  - Sovereignty tags (tribal governance, protected areas)  
  - Redaction/generalization rules for spatial and temporal data  
  - Dataset licensing and usage constraints  

- **Spatiotemporal**
  - Temporal extents (start/end, ISO 8601 strings)  
  - Precision & uncertainty labels (`year`, `approximate`, etc.)  
  - Spatial extents (bbox, centroid) and generalization flags (`h3-r7`, `county`, `region`)  
  - Explicit marking of predictive vs historical intervals  

- **Explainability**
  - Relevance scores (for Focus Mode ranking)  
  - Evidence sets (IDs of Story Nodes, documents, datasets that justify inclusion)  

- **Accessibility**
  - Long descriptions / alt-text style summaries for narrative-heavy entities  
  - Short labels for simple read-out in lists  
  - Structured fields for accessible ordering (e.g., date, place, summary separated)

### Conceptual EVM Type (TypeScript)

~~~ts
export type EntityVMType = "person" | "place" | "event" | "dataset";

export interface EntityVM {
  id: string;
  label: string;
  type: EntityVMType;

  description?: string;

  temporal?: {
    start?: string;         // ISO 8601
    end?: string;           // ISO 8601
    precision?: "year" | "month" | "day" | "approximate";
    originalLabel?: string; // e.g. "late 19th century"
  };

  spatial?: {
    bbox?: [number, number, number, number];
    centroid?: [number, number];
    generalizationLevel?: "h3-r7" | "county" | "region" | "none";
  };

  provenance: {
    stacIds?: string[];
    dcatIds?: string[];
    graphRefs?: string[];     // neo4j://…
    lineage?: string[];       // IDs or human-readable lineage markers
    ledgerRefs?: string[];    // governance ledger IDs
    checksumVerified?: boolean;
  };

  care: {
    label: "public" | "sensitive" | "restricted" | "sovereignty-controlled";
    sovereignty?: string;     // e.g., "Kaw Nation", "Osage"
  };

  explainability?: {
    relevance?: number;
    evidence?: string[];      // IDs of related Story Nodes / sources
  };

  accessibility?: {
    longDescription?: string;
    shortLabel?: string;
  };
}
~~~

All concrete `personViewModel.ts`, `placeViewModel.ts`, etc. MUST conform to the canonical EVM schema.

---

## 👤 People Entities

**Domain:** `E21 Person` / `E39 Actor` in CIDOC-CRM.

People EVMs unify:

- Biographical metadata (names, roles, life ranges)  
- Cultural and sovereignty-sensitive labels (e.g., roles in colonial systems, tribal leadership)  
- Linkages to events, places, and datasets  
- Provenance for biographical claims (letters, census data, archival records)  
- CARE & sovereignty markers (especially for Indigenous individuals or groups)

Conceptual mapping flow:

~~~mermaid
flowchart LR
    P1[Person Node (Neo4j)] --> P2[personMapper]
    P2 --> P3[personViewModel]
    P3 --> UI[Focus · Drawer · StoryNodes · DataCards]
~~~

Rules:

- No inference of new relationships or attributes beyond validated graph edges and metadata.  
- When multiple person nodes are merged (e.g., due to curation), that decision must be recorded in provenance.  

---

## 📍 Places Entities

**Domain:** `E53 Place`.

Place EVMs encode:

- Generalized spatial extent:
  - Bbox, centroid, and generalization level only  
- Sovereignty and jurisdictional context:
  - tribal lands, county/state boundaries, etc.  
- Linked datasets and map layers (STAC items/collections, topographic or thematic layers)  
- Environment/geomorphology hints where available (non-essential but helpful)

Conceptual flow:

~~~mermaid
flowchart LR
    PL1[Place Node (Neo4j/STAC)] --> PL2[placeMapper]
    PL2 --> PL3[placeViewModel]
    PL3 --> MAP[MapView Integration · StoryNodes · Focus]
~~~

Rules:

- Raw geometry stays in geospatial pipelines; EVMs only store safe generalizations.  
- Sovereignty tags must be present when Places intersect protected/tribal domains.  

---

## 📅 Events Entities

**Domain:** `E5 Event`.

Event EVMs model:

- Temporal intervals (start/end, with precision and uncertainty)  
- Participants (linked Person and Group EVM references)  
- Spatial context (linked Place EVMs, not raw geometry)  
- Story Node associations (events as structural backbone of narratives)  
- Timeline alignment and focusing hints (which TimelineView slice to highlight)

Conceptual flow:

~~~mermaid
flowchart LR
    E1[Event Node (Neo4j)] --> E2[eventMapper]
    E2 --> E3[eventViewModel]
    E3 --> TL[TimelineView · StoryNodes · Focus Mode]
~~~

Rules:

- No invented start/end dates. If unknown, use `originalLabel` and/or open-ended temporal intervals.  
- All participants must be resolvable to People/Group/Place EVMs or be omitted (no “phantom” participants).  

---

## 📦 Dataset Entities

**Domain:** STAC/DCAT `Dataset` / `Collection` (mapped to `E31 Document` + `E73 Information Object` in CIDOC terms).

Dataset EVMs:

- Normalize STAC/DCAT metadata for frontend use  
- Harvest:
  - license, rights, creator/publisher  
  - spatial and temporal coverage  
  - additional STAC extensions (where relevant)  
- Encode CARE visibility:
  - data-level sensitivity  
  - usage constraints for maps and timelines  
- Provide explicit references to underlying STAC/DCAT IDs and data services

Conceptual flow:

~~~mermaid
flowchart LR
    D1[STAC/DCAT Dataset] --> D2[datasetMapper]
    D2 --> D3[datasetViewModel]
    D3 --> UI[DataCards · MapView · Timeline · Governance UI]
~~~

Rules:

- No inference of dataset coverage beyond what is defined (e.g., do not expand coverage to entire Kansas unless metadata says so).  
- Licensing and rights must never be “assumed”; unknown must remain unknown (and flagged as such in UI).  

---

## ⚖️ Governance & FAIR+CARE Integration

Governance is enforced at the EVM level in coordination with the backend.

The Entities Layer MUST:

- Propagate governance metadata:
  - CARE label and sovereignty tags  
  - Redaction flags (`redaction_required`)  
  - Spatial/temporal generalization rules  
- Ensure that EVMs **never**:
  - contain precise coordinates for sensitive entities  
  - remove or obscure governance-related fields  
  - claim higher licensing permissions than the source  

FAIR:

- EVMs are Findable via `id`, `label`, and `type`.  
- Accessible through typed interfaces and documented schema.  
- Interoperable via CIDOC/OWL-Time/GeoSPARQL/PROV-O alignment.  
- Reusable thanks to explicit provenance, licensing, and CARE metadata.

Any EVM that contradicts backend governance decisions or strips CARE/sovereignty tags must be treated as a **CI-blocking** error.

---

## ♿ Accessibility & A11y-Ready Content

Entities are designed to support accessible UI construction.

EVMs MUST provide:

- Human-readable labels and descriptions, separate from internal IDs.  
- Structured temporal data that UI can transform into friendly phrases (e.g. “winter 1864”).  
- Clear spatiotemporal descriptions for non-visual contexts (via `accessibility.longDescription`).  

Conceptual flow:

~~~mermaid
flowchart TD
    VM[Entity VM] --> ALT[Accessible Text Blocks<br/>SR / alt-text friendly]
    ALT --> UI[Story · Focus · Drawer · Map HUD]
~~~

UI components consume those fields; the Entities Layer ensures there is a consistent, central source of truth for A11y text.

---

## 📈 Telemetry & Sustainability Integration

Entity-level usage is observable via telemetry (hook-based, not inside pure mappers).

Typical events keyed off EVM usage:

- `entity:select` — when user explicitly opens an entity in Focus or DetailDrawer  
- `entity:sensitive-view` — aggregated count when a sensitive entity is displayed (no PII)  
- `entity:public-view` — aggregated count for public entities  
- `entity:explainability-view` — use of EVM-backed explainability features  

Telemetry is:

- stored in `../../../releases/v11.2.2/web-entities-telemetry.json`  
- version-tagged and schema-validated  
- used to support energy/carbon accounting by cross-linking with pipeline metrics (but not guessed at entity-level)

The Entities Layer provides typed hooks/events; telemetry emission logic should be in service/observer code, not inside mappers/view-models.

---

## 🧪 CI / Validation Requirements

**Validation surfaces:**

| Area         | Validation Mechanism                                    |
|--------------|---------------------------------------------------------|
| Schema       | `schemaGuards.ts` + JSON Schema for EVM structures      |
| Governance   | `faircare-validate.yml` (ensures CARE flags are present)|
| Accessibility| A11y tests using EVM fields in test harnesses           |
| Provenance   | lineage + checksum checks in ETL → EVM pipeline tests   |
| Telemetry    | `telemetry-export.yml` ensuring event schemas are valid |
| Docs         | `docs-lint.yml` for this README and related docs        |

All new or modified EVMs MUST be validated by:

- Type-level compile checks (TS)  
- Runtime schema validation in dev/test as configured  
- Governance audit pipelines (spot-checks for sensitive entities)  

---

## 🕰 Version History

| Version | Date       | Summary                                                                                          |
|--------:|------------|--------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-30 | Upgraded to KFM-MDP v11.2.2; aligned with KFM-OP v11, telemetry v2, FAIR+CARE v11 semantics, energy/carbon v2. |
| v10.3.2 | 2025-11-14 | Deep-architecture rebuild — CARE, provenance, STAC/DCAT linkage, Focus v2.5, and telemetry pipelines.         |
| v10.3.1 | 2025-11-13 | Initial Entities Layer documentation                                                             |

---

## ⚖️ Footer

<div align="center">

**👥 Kansas Frontier Matrix — Entities Architecture**  
Semantic Integrity · FAIR+CARE Governance · Provenance Fidelity · A11y-Ready · AI-Constrained  

[Docs Root](../../../README.md) •  
[Standards Index](../../../docs/standards/INDEX.md) •  
[Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

© 2025 Kansas Frontier Matrix — MIT License  

**End of Document**

</div>