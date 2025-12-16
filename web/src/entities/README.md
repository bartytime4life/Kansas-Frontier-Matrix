---
title: "👥 Kansas Frontier Matrix — Entities Architecture & Semantic View-Model Layer (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/entities/README.md"

version: "v11.2.6"
last_updated: "2025-12-16"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.6/manifest.zip"
signature_ref: "../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../releases/v11.2.6/slsa-attestation.json"

telemetry_ref: "../../../releases/v11.2.6/web-entities-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/web-entities-v2.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

status: "Active / Enforced"
doc_kind: "Architecture Overview"
intent: "web-entities-architecture"
role: "overview"
category: "Web · Entities · Architecture"

fair_category: "F1-A1-I1-R1"
care_label: "Public / Mixed (entity-dependent)"
sensitivity: "Entity-dependent"
sensitivity_level: "Entity-dependent"
public_exposure_risk: "Medium"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"
risk_category: "Mixed"
redaction_required: true

provenance_chain:
  - "web/src/entities/README.md@v11.2.2"
  - "web/src/entities/README.md@v10.3.2"
  - "web/src/entities/README.md@v10.3.1"
provenance_requirements:
  versions_required: true
  newest_first: true

ontology_alignment:
  cidoc: "E21 Person / E53 Place / E5 Event / E31 Document"
  schema_org: "CreativeWork / Place / Dataset"
  owl_time: "TemporalEntity"
  geosparql: "geo:Feature"
  prov_o: "prov:Entity"

json_schema_ref: "../../../schemas/json/web-entities-readme-v11.schema.json"
shape_schema_ref: "../../../schemas/shacl/web-entities-readme-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:web-entities-readme:v11.2.6"
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

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "🧭 Context"
    - "🗺️ Diagrams"
    - "🧠 Story Node & Focus Mode Integration"
    - "🧪 Validation & CI/CD"
    - "📦 Data & Metadata"
    - "🌐 STAC, DCAT & PROV Alignment"
    - "🧱 Architecture"
    - "⚖ FAIR+CARE & Governance"
    - "🕰️ Version History"
---

<div align="center">

# 👥 **Kansas Frontier Matrix — Entities Architecture & Semantic View-Model Layer (v11.2.6)**  
`web/src/entities/README.md`

**Purpose:**  
Define the **Entities Layer** (semantic view‑model layer) for KFM Web — the governed transformation
that turns heterogeneous sources (graph/API DTOs + STAC/DCAT metadata + provenance/gov overlays)
into **UI‑ready, accessibility‑ready, FAIR+CARE‑constrained Entity View Models (EVMs)**.

<img src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Governed-orange" />
<img src="https://img.shields.io/badge/Accessibility-WCAG_2.1_AA%2B-blueviolet" />

</div>

---

## 📘 Overview

The **Entities Layer** is the Web Platform’s **semantic adapter** between:

- **Backend & pipeline outputs**
  - Knowledge‑graph query responses (REST/GraphQL or static exports)
  - STAC‑like catalogs for geospatial assets (layers/items/collections)
  - DCAT‑like dataset registries (dataset‑level metadata)
  - Provenance records (PROV‑O aligned) and governance decisions

…and…

- **Frontend consumers**
  - Map UI (MapLibre / Cesium view layers, highlights, selection)
  - Timeline filtering and navigation
  - Detail drawers / modals / cards (summary + metadata)
  - Focus Mode (entity‑centric context + explainability)
  - Story Nodes (narrative objects referencing entities by stable IDs)

**Entity View Models (EVMs)** produced by this layer are designed to be:

- **Deterministic:** same inputs → same outputs (no hidden global mutation)
- **Typed:** compile‑time safety (TypeScript) + runtime guards (schema/guards)
- **Governance‑preserving:** CARE + sovereignty + redaction metadata cannot be “dropped”
- **A11y‑ready:** consistent fields for screen‑reader friendly labels and summaries
- **Non‑speculative:** do not invent relationships, dates, places, or coverage

### What the Entities Layer is *not*

- Not a renderer (no React components)
- Not a network layer (no fetch/axios calls inside mappers)
- Not an inference engine (no synthetic relationship creation)
- Not an authorization bypass (frontend may be stricter than backend, never looser)

---

## 🗂️ Directory Layout

> **Repository note:** This section defines the **canonical pattern** expected for `web/src/entities/**`.
> If filenames differ in the repo, update this layout to match the implementation (do not “paper over” drift).

~~~text
📁 web/src/entities/                               — Semantic view‑model layer (pure TS; no React; no network)
├── 📄 README.md                                   — This document
├── 📄 index.ts                                    — Public surface (barrel exports)
│
├── 📁 core/                                       — Cross‑entity contracts + shared utilities
│   ├── 📄 entityKinds.ts                           — Canonical entity kinds (Person/Place/Event/Dataset…)
│   ├── 📄 entityRef.ts                             — Stable entity references (IDs only; safe for storage)
│   ├── 📄 evmBase.ts                               — Base EVM contracts + invariants
│   ├── 📄 evmGuards.ts                             — Runtime guards (schema/shape checks)
│   ├── 📄 governanceFragments.ts                   — CARE/sovereignty/redaction fragments (UI‑safe)
│   └── 📄 provenanceFragments.ts                   — PROV‑O aligned provenance fragments (UI‑safe)
│
├── 📁 people/                                     — Person EVMs (CIDOC E21 / E39)
│   ├── 📄 mapper.ts                                — DTO → PersonEvm mapping
│   ├── 📄 viewModel.ts                             — PersonEvm type + factory
│   └── 📄 metadata.json                            — Machine hints (optional; must be non‑sensitive)
│
├── 📁 places/                                     — Place EVMs (CIDOC E53)
│   ├── 📄 mapper.ts                                — DTO/STAC → PlaceEvm mapping
│   ├── 📄 viewModel.ts                             — PlaceEvm type + factory
│   └── 📄 metadata.json                            — Machine hints (optional; must be non‑sensitive)
│
├── 📁 events/                                     — Event EVMs (CIDOC E5)
│   ├── 📄 mapper.ts                                — DTO → EventEvm mapping
│   ├── 📄 viewModel.ts                             — EventEvm type + factory
│   └── 📄 metadata.json                            — Machine hints (optional; must be non‑sensitive)
│
└── 📁 datasets/                                   — Dataset EVMs (STAC/DCAT mapped; CIDOC E31/E73)
    ├── 📄 mapper.ts                                — STAC/DCAT → DatasetEvm mapping
    ├── 📄 viewModel.ts                             — DatasetEvm type + factory
    └── 📄 metadata.json                            — Machine hints (optional; must be non‑sensitive)
~~~

---

## 🧭 Context

The Entities Layer sits **between** the type system, services/pipelines, and global state:

- `web/src/types/**`
  - Defines canonical *shapes* for API DTOs, domain models, STAC/DCAT, governance, spatial, temporal, telemetry.
- `web/src/services/**` and/or `web/src/pipelines/**`
  - Fetch or load static artifacts produced by pipeline runs.
  - Normalize transport format (DTOs) and hand them to entity mappers.
- `web/src/entities/**` (this layer)
  - Converts DTOs → EVMs.
  - Normalizes uncertainty, provenance, governance, and accessibility fields.
- `web/src/context/**`
  - Stores selected EVMs or EVM references (IDs) as global state.
- `web/src/components/**` and/or `web/src/features/**`
  - Render map/timeline/drawers/cards using EVM fields.

### Inputs the Entities Layer must support

- Graph/query DTOs that represent:
  - entities (people, places, events)
  - relationships (links between entities)
  - evidence pointers (document IDs, story node IDs, dataset IDs)
- STAC‑like records describing geospatial assets (bbox + temporal coverage + license/source)
- DCAT‑like dataset registry records (dataset‑level metadata and publisher/source fields)
- Governance overlays (CARE labels, sovereignty flags, redaction requirement)
- Provenance fragments (sources, transformations, checksums where available)

### Outputs the Entities Layer must guarantee

- Stable `id` + human `label`
- Safe spatiotemporal representation (generalized where required)
- Governance + redaction preserved (never silently omitted)
- Provenance pointers sufficient for drill‑down / audit UI
- Accessibility text fields (long/short labels, SR‑friendly summaries)

---

## 🗺️ Diagrams

### End‑to‑end flow (pipeline → web)

~~~mermaid
flowchart LR
  P[Pipeline Outputs<br/>STAC/DCAT catalogs · graph exports · tiles] --> S[Static Hosting<br/>JSON · tiles · COG/VT]
  A[Query API<br/>Graph search · entity context] --> SV[web/src/services]
  S --> SV
  SV --> E[web/src/entities<br/>DTO → EVM]
  E --> C[web/src/context<br/>global state]
  C --> UI[UI Surfaces<br/>Map · Timeline · Focus · Story · Drawer]
~~~

### Governance gating (non‑negotiable)

~~~mermaid
flowchart TD
  IN[Incoming DTOs<br/>graph · STAC/DCAT] --> MAP[Entity Mapper]
  GOV[Governance Inputs<br/>CARE · sovereignty · redaction] --> MAP
  MAP --> OUT[EVM Output<br/>UI‑safe fields only]
  OUT --> R[Renderers<br/>Map/Timeline/Drawer]
  OUT --> T[Telemetry Hooks<br/>non‑PII aggregates]
~~~

---

## 🧠 Story Node & Focus Mode Integration

Entities are foundational to **storytelling and reasoning** features, but the Entities Layer remains **semantic, not narrative**.

### Story Nodes

- Story Nodes reference entities by **stable IDs** (EVM `id` and/or `EntityRef`).
- Story rendering should not “guess” entity facts; it should consume:
  - `label`, `description`, `temporal`, `spatial` (generalized), `provenance`, `care`.
- Story Nodes may contain narrative prose, but entities provide the **auditable factual spine**
  (what the story is “about”, what it references, and where those references came from).

### Focus Mode

- Focus Mode state should be built on EVMs:
  - A focused entity EVM
  - Related entity refs/EVMs
  - Evidence pointers (documents/story nodes/datasets)
- Any AI‑derived signals (ranking, relevance, “why this matters”) must be:
  - provenance‑linked (IDs to evidence, not free‑floating claims)
  - clearly labeled as derived (not archival fact)
  - suppressible/redactable based on governance rules

---

## 🧪 Validation & CI/CD

The Entities Layer is a high‑risk correctness boundary: it is where data becomes UI‑ready.

### CI checks expected for this layer

- **Type safety**
  - `tsc --noEmit` and strict linting must pass for all mappers and EVM types.
- **Schema/guard validation**
  - EVM guards must reject malformed DTOs or missing governance fields.
- **Governance safety checks**
  - If `redaction_required: true`, EVMs must not contain precise coordinates for sensitive entities.
  - CARE and sovereignty tags must not disappear during mapping.
- **Docs + protocol compliance**
  - README must pass KFM‑MDP checks (headings, directory layout, version history, footer links).
- **Security / privacy**
  - No PII leakage in logs, errors, or telemetry events.

> Note: The Entities Layer should remain **side‑effect‑light**; telemetry emission belongs to hooks/services
> that observe entity usage, not inside mappers.

---

## 📦 Data & Metadata

### Identity and external identifiers (non‑negotiable)

- Every EVM MUST have a stable, unique `id`.
- When available, EVMs SHOULD carry **external IDs** (e.g., Wikidata, archival catalog IDs, GIS IDs),
  but EVMs MUST NOT invent external IDs.
- If duplicate entities are merged upstream (curation/ETL), that merge MUST be traceable in provenance.

### Temporal representation

- Use ISO‑8601 strings for machine‑readable dates when possible.
- Preserve uncertainty:
  - keep an `originalLabel` (e.g., “late 19th century”, “ca. 1850”)
  - represent fuzziness as ranges instead of forcing a single instant

### Spatial representation

- Prefer **bbox/centroid** and a **generalizationLevel** over raw geometry.
- For sovereignty‑controlled or otherwise sensitive entities:
  - omit precise coordinates, or
  - provide generalized geometry references (e.g., H3 cell resolution, county, region)

### Conceptual EVM contract (TypeScript — illustrative)

~~~ts
export type EntityKind = "person" | "place" | "event" | "dataset";

export type TemporalPrecision = "year" | "month" | "day" | "approximate" | "unknown";
export type SpatialGeneralization = "none" | "h3" | "county" | "region" | "unknown";

export interface EntityRef {
  id: string;
  kind: EntityKind;
}

export interface GovernanceFragment {
  careLabel: "public" | "low-risk" | "sensitive" | "restricted" | "sovereignty-controlled";
  redactionRequired: boolean;
  sovereigntyTags?: string[]; // e.g., Nation/Tribe names (when approved to surface)
  warnings?: string[];        // UI-safe short codes/messages (no sensitive specifics)
}

export interface ProvenanceFragment {
  sources?: string[];         // IDs/refs to source records (not raw URLs if restricted)
  stacIds?: string[];
  dcatIds?: string[];
  graphRefs?: string[];       // e.g., stable graph node IDs/URIs
  lineageRefs?: string[];     // PROV-aligned IDs: entities/activities/agents
  checksumVerified?: boolean; // whether referenced artifacts checksums were validated
}

export interface EntityViewModel {
  id: string;
  kind: EntityKind;

  label: string;
  description?: string;

  temporal?: {
    start?: string;          // ISO 8601
    end?: string;            // ISO 8601
    precision?: TemporalPrecision;
    originalLabel?: string;  // preserves uncertainty wording
  };

  spatial?: {
    bbox?: [number, number, number, number];
    centroid?: [number, number];
    generalizationLevel?: SpatialGeneralization;
  };

  governance: GovernanceFragment;
  provenance: ProvenanceFragment;

  relations?: Array<{
    type: string;            // relationship label (must be defined upstream)
    to: EntityRef;
    evidence?: string[];     // IDs of documents/story nodes/datasets supporting the link
  }>;

  accessibility?: {
    shortLabel?: string;
    longDescription?: string;
  };
}
~~~

### Mapper invariants (must hold for every entity kind)

- **No speculation:** do not add inferred relationships or fill missing dates/places.
- **No silent drops:** governance/provenance fields can be empty/unknown, but not silently removed.
- **Safe defaults:** unknown remains unknown; do not “assume” permissions or coverage.
- **Serializable outputs:** EVMs must be JSON‑safe and safe to cache in memory/state.

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC (asset-level, geospatial)

The platform uses a STAC‑like approach where geospatial layers/assets are indexed with:

- name + description
- bbox (spatial extent)
- time range/date (temporal extent)
- format, source, license

EVM dataset mappings SHOULD:

- preserve STAC IDs (items/collections)
- normalize bbox/temporal coverage into EVM fields
- preserve licensing + rights for UI display and governance gating

### DCAT (dataset-level, catalog/registry)

DCAT‑like registry structures provide higher‑level dataset metadata (title, description, publisher/source,
temporal/spatial coverage). Dataset EVMs should carry DCAT IDs/refs when applicable.

### PROV‑O (provenance)

Provenance must be UI‑addressable:

- entities and relationships should link back to source records
- transformations should be traceable (pipeline steps, model versions where applicable)
- evidence pointers should allow “drill‑down” without exposing restricted details

The Entities Layer should not fabricate provenance; it should bind what exists and surface “unknown” explicitly.

---

## 🧱 Architecture

### Core pattern: DTO → Mapper → EVM

For each entity kind:

1. **Input DTOs** are defined in the shared type system (`web/src/types/**`).
2. **Mapper** normalizes:
   - labels, aliases, display strings
   - temporal ranges (with uncertainty preserved)
   - spatial extents (generalized as required)
   - governance + provenance fragments
3. **EVM** becomes the single, UI‑ready source for:
   - cards and lists
   - map highlights and selections
   - timeline markers and range filtering
   - focus context payloads

### Query alignment (time + place + topic)

The backend query layer can retrieve entities by:

- time windows (date range filtering)
- map viewport / region
- topic/keyword and relevance scoring

The Entities Layer must preserve enough structure to support:
- timeline sorting and grouping
- map filtering and selection by ID
- explainability linkages to evidence nodes (documents, datasets, story nodes)

### Error handling (UI-safe)

Mapper failures must be:
- non‑PII
- non‑sensitive
- actionable (which field is missing/invalid, which guard failed)

Prefer typed error codes over dumping raw payloads.

---

## ⚖ FAIR+CARE & Governance

This document and layer are **entity‑sensitive**:

- Some entities may reference sovereignty‑controlled or culturally sensitive contexts.
- Some entities may require spatial/temporal generalization.
- Some entities may be visible only under specific governance conditions.

### Non‑negotiable governance rules

- **Frontend can be stricter, never looser** than backend governance.
- If `redaction_required` applies:
  - EVMs must not contain precise coordinates
  - EVMs must carry explicit generalization metadata or omit spatial fields
- CARE labels and sovereignty tags must remain visible to UI systems:
  - masking indicators
  - sovereignty notices
  - dataset licensing/rights warnings

### Accessibility and governance together

Do not encode governance meaning using **color only**:
- always provide text labels and SR‑friendly descriptions
- ensure warnings are readable in all themes

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-16 | Updated to KFM‑MDP v11.2.6 structure (approved H2s, outer-backticks/inner-tildes, footer governance links); refreshed release refs to v11.2.6; strengthened identity/temporal/spatial invariants and STAC/DCAT/PROV alignment notes. |
| v11.2.2 | 2025-11-30 | Upgraded to KFM‑MDP v11.2.2; aligned with KFM‑OP v11, telemetry v2, FAIR+CARE semantics, energy/carbon v2. |
| v10.3.2 | 2025-11-14 | Deep-architecture rebuild — CARE, provenance, STAC/DCAT linkage, Focus alignment, telemetry pipelines. |
| v10.3.1 | 2025-11-13 | Initial Entities Layer documentation. |

<div align="center">

**👥 Kansas Frontier Matrix — Entities Layer**  
Designed for Longevity · Governed for Integrity · Provenance Fidelity · A11y‑Ready · AI‑Constrained

[Docs Root](../../../README.md) •
[Web Source Overview](../README.md) •
[Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md) •
[FAIR+CARE Guide](../../../docs/standards/faircare/FAIRCARE-GUIDE.md) •
[Sovereignty Policy](../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License

</div>
