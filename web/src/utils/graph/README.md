---
title: "🧠 Kansas Frontier Matrix — Graph & Entity Utilities (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/utils/graph/README.md"
version: "v11.2.6"
last_updated: "2025-12-15"
review_cycle: "Quarterly · FAIR+CARE Council & Web Architecture Board"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.6/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.6/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/web-utils-graph-v11.json"

governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11.0"

status: "Active / Enforced"
doc_kind: "Architecture"
intent: "web-graph-utilities"
role: "frontend-graph-normalization"
category: "Web · Graph · Utilities · Focus Mode · Story Nodes"

classification: "Public"
fair_category: "F1-A2-I2-R3"
care_label: "Public · Governed"
sensitivity_level: "Low"
public_exposure_risk: "Low"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

risk_category: "Low"
redaction_required: false

provenance_chain:
  - "web/src/utils/graph/README.md@v11.2.2"
  - "web/src/utils/graph/README.md@v11.0.0"
  - "web/src/utils/graph/README.md@v10.4.1"
  - "web/src/utils/graph/README.md@v10.3.2"
  - "web/src/utils/graph/README.md@v10.3.1"
provenance_requirements:
  versions_required: true
  newest_first: true

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "SoftwareSourceCode"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../schemas/json/web-utils-graph-readme-v11.schema.json"
shape_schema_ref: "../../../../schemas/shacl/web-utils-graph-readme-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:web-utils-graph-readme:v11.2.6"
semantic_document_id: "kfm-doc-web-utils-graph-readme"
event_source_id: "ledger:web/src/utils/graph/README.md"
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
  - "relationship-fabrication"
  - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "Annual review"
sunset_policy: "Superseded upon next graph-utils revision"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🧠 **Kansas Frontier Matrix — Graph & Entity Utilities (v11.2.6)**  
`web/src/utils/graph/README.md`

**Purpose**  
Define the **frontend-side normalization, relationship flattening, subgraph extraction, entity merging, provenance propagation, and Focus Mode v3 bindings** used by the KFM Web Platform to transform Neo4j + API graph responses into **stable, deterministic, governance-safe UI structures**.

These utilities are:
- deterministic
- typed (TypeScript strict)
- FAIR+CARE-governed
- sovereignty-safe
- aligned with Story Node v3 + Focus Mode v3
- essential to map/timeline/focus synchronization

</div>

## 📘 Overview

`web/src/utils/graph/**` contains **pure functional TypeScript modules** responsible for turning *graph-shaped API payloads* into **predictable, UI-ready models** that can be rendered safely in:

- Focus Mode v3 (focal entity → context → narrative panels)
- Story Node v3 (cards, relations, evidence trails)
- Map layers and overlays (spatial extents, masked geometries)
- Timeline engine (temporal extents and ordering)
- Entity detail panels (typed properties + provenance)

Core responsibilities:

- 🔄 Normalize raw nodes into canonical entities (type-safe, schema-guarded)
- 🪢 Flatten nested subgraphs into stable arrays (nodes + edges)
- 🧊 Deterministically order nodes/edges for stable rendering and caching
- 🧾 Preserve and propagate provenance (PROV-O) and rights/license metadata
- 🔐 Enforce governance filters (CARE labels, sovereignty rules, masking/generalization)
- 🧠 Provide Focus Mode binding helpers (context windows, “related entities”, evidence lists)

Hard constraints (non-negotiable):

- No network calls, no IO, no global mutation
- No DOM / `window` / browser-global usage
- No relationship invention or “best guess” linking
- No sharpening of uncertain time or generalized/masked geometry into precise values
- Governance metadata must not be dropped silently

## 🗂️ Directory Layout

~~~text
📁 web/
  📁 src/
    📁 utils/
      📁 graph/
        📄 README.md                 # This document (architecture + contracts)
        📄 entityNormalize.ts        # Canonical entity normalization (typed + governed)
        📄 relationFlatten.ts        # Nested subgraph → flat nodes/edges (dedupe + stable sort)
        📄 focusBindings.ts          # Focus Mode v3 bindings (entity → FocusContext)
        📄 idUtils.ts                # Stable ID helpers (canonicalization, merge keys, dedupe)
        📄 groupByType.ts            # Split heterogeneous nodes into typed buckets
~~~

If the codebase includes additional graph utility modules in this directory, they MUST be documented here with:
- inputs/outputs
- governance behavior
- determinism guarantees
- test coverage location

## 🧭 Context

KFM’s web application does not query Neo4j directly. It consumes **API responses** (REST and/or GraphQL) that may include:

- a focal entity payload (Place/Event/Person/Group/Document/Dataset/StoryNode)
- a compact subgraph for context (typically within limited hops)
- evidence and provenance attachments
- governance overlays (CARE label, sovereignty flags, license, sensitivity)

These utilities sit between:

- `web/src/utils/api/**` (fetch, response guards, schema checks)
and
- `web/src/components/**` + Focus Mode panels + timeline/map views

Pipeline fit (frontend perspective):

~~~text
API response (graph-shaped)
  → relationFlatten (structure & dedupe)
    → entityNormalize (typed canonical entities)
      → groupByType (UI bucketization)
        → focusBindings (Focus Mode context assembly)
          → UI render (map + timeline + narrative + provenance)
~~~

Design goal:

- Make graph consumption **boring**: deterministic, validated, auditable.
- Make governance **visible**: if something is masked or suppressed, the UI should be able to explain why.
- Make failures **safe**: invalid payloads are rejected early; no partial rendering that can leak restricted details.

## 🧱 Architecture

### Canonical inputs

Graph utilities are designed around a minimal set of input expectations:

- **Nodes** have:
  - stable identifier (prefer `urn:kfm:...` or API-stable id)
  - type/label information (entity category)
  - properties payload (names, dates, geometry, evidence links, etc.)
  - governance/provenance metadata (when available)

- **Edges** have:
  - stable source/target ids
  - relationship type label
  - optional properties (confidence, evidence, temporal qualifiers)
  - governance qualifiers (when required)

Graph utilities MUST tolerate:
- partial nodes (missing optional props)
- missing edges
- unknown node labels (must be handled as “unknown type”, not crashed)
- mixed precision temporal/spatial data

Graph utilities MUST NOT tolerate:
- payloads that cannot be validated by upstream response guards
- payloads that attempt to bypass governance requirements (e.g., missing required CARE metadata for sensitive classes)

### Canonical outputs

The output of these utilities is intended to be:

- stable (same input → same output)
- serializable (no `Date` objects unless explicitly isolated)
- safe (masked/generalized where required)
- explainable (provenance and governance preserved)

Recommended core shapes (illustrative; align to actual project types/contracts):

~~~ts
export type CanonicalId = string;

export interface GovernanceMeta {
  careLabel?: string;
  sovereignty?: string;
  sensitivity?: "none" | "low" | "moderate" | "high";
  indigenousRightsFlag?: boolean;
  license?: string;
  restrictions?: string[];
  masked?: boolean;
  maskMethod?: "h3" | "bbox-generalization" | "redaction" | "none";
}

export interface ProvenanceMeta {
  prov?: {
    used?: string[];
    wasDerivedFrom?: string[];
    wasGeneratedBy?: string[];
    wasAssociatedWith?: string[];
  };
  evidence?: Array<{ id: string; href?: string; label?: string }>;
}

export interface CanonicalEntity {
  id: CanonicalId;
  kind:
    | "Place"
    | "Event"
    | "Person"
    | "Group"
    | "Organization"
    | "Document"
    | "Dataset"
    | "StoryNode"
    | "Unknown";
  label?: string;
  description?: string;
  when?: { start?: string; end?: string; precision?: string; approx?: boolean };
  where?: { geometry?: unknown; bbox?: [number, number, number, number] | null };
  confidence?: number;
  __governance?: GovernanceMeta;
  __provenance?: ProvenanceMeta;
  __raw?: unknown; // optional passthrough for debugging (must be safe/redacted)
}

export interface CanonicalEdge {
  id: CanonicalId;
  source: CanonicalId;
  target: CanonicalId;
  type: string;
  confidence?: number;
  __governance?: GovernanceMeta;
  __provenance?: ProvenanceMeta;
}
~~~

### Determinism rules

All transformations must be deterministic. At minimum:

- dedupe keys:
  - entities: `id`
  - edges: `(source, type, target, qualifiers)` canonicalized into a stable id

- stable ordering:
  - entities sorted by `(kind, label || "", id)`
  - edges sorted by `(type, source, target, id)`

- merge policy:
  - never overwrite “more governed” values with “less governed” values
  - never discard provenance or governance blocks unless explicitly configured and logged at a higher layer

### Governance filtering model

Graph utilities are a **secondary enforcement layer** (API and backend should already enforce). Their job is to prevent frontend-side leakage when:

- the API returns generalized geometry and a client tries to “reconstruct” precision
- the API returns mixed-precision temporal metadata and UI wants to display a more precise date
- edges imply relationships that should be suppressed at public risk levels

Graph utilities must implement “deny by default” behavior for:
- restricted geometry
- restricted identifiers for deep-linking
- restricted relationship types (where policy requires suppression)
- missing governance metadata when policy requires it

## 📦 Data & Metadata

### Stable identifiers

The system uses stable ids for cross-linking and caching. Graph utilities must:

- treat ids as opaque
- avoid encoding sensitive meaning into derived ids
- avoid exposing internal ids in URLs without governance checks

### Confidence and evidence

Graph/entity payloads may include confidence-like signals:

- entity confidence (identity/linking strength)
- relationship confidence (evidence strength)
- evidence count / citations list

Graph utilities must:
- preserve confidence values, never invent them
- never treat confidence as proof; it is a UI hint
- ensure evidence lists are preserved and can be rendered as provenance trails

### Temporal + spatial metadata

Graph utilities commonly depend on:

- `web/src/utils/date/**` for OWL-Time aligned temporal normalization
- `web/src/utils/bbox/**` for safe bounding box computation and clamping
- `web/src/utils/url/**` for governance-safe deep links

Rules:

- If temporal precision is “year” (or fuzzier), do not render as day-level
- If geometry is masked/generalized, do not compute derived geometry that increases precision
- If only a bbox exists, treat it as authoritative and do not infer a centroid unless explicitly allowed

## 🌐 STAC, DCAT & PROV Alignment

Graph utilities must remain compatible with KFM’s catalog and provenance outputs:

- **Datasets** may be represented as:
  - DCAT dataset identifiers (URNs)
  - references to STAC Collections/Items (repo paths or API hrefs)
  - distributions/assets (STAC assets) that should be displayed without leaking restricted details

- **Provenance** (PROV-O):
  - Entities: raw/processed artifacts, documents, datasets, story nodes
  - Activities: ETL runs, curation, inference, validation
  - Agents: people, services, scripts (as allowed by governance rules)

Graph utilities must preserve:
- `prov:used`
- `prov:wasGeneratedBy`
- `prov:wasDerivedFrom`
- `prov:wasAssociatedWith`

When provenance is missing:
- do not fabricate
- surface the absence as a UI-visible “provenance incomplete” condition (for governance review)

## 🧠 Story Node & Focus Mode Integration

Focus Mode is a “deep exploration session” centered on a focal entity. Graph utilities support this by producing stable, governed Focus Mode inputs:

### Focus bindings

`focusBindings.ts` should compute a stable Focus Context:

- focal entity id + kind
- related entity ids (places/events/documents/story nodes/datasets)
- safe temporal window (no sharpening)
- safe bbox (clamped/generalized as required)
- governance overlay (CARE label + sovereignty flags + any masking notices)
- evidence/provenance lists to support “why am I seeing this?” panels

Illustrative shape:

~~~ts
export interface FocusContext {
  focusId: string;
  focusKind: CanonicalEntity["kind"];
  related: {
    places: string[];
    events: string[];
    documents: string[];
    storyNodes: string[];
    datasets: string[];
    people: string[];
    groups: string[];
    organizations: string[];
    unknown: string[];
  };
  timelineWindow: { start?: string; end?: string; precision?: string; approx?: boolean };
  bbox: [number, number, number, number] | null;
  governance: {
    careLabel?: string;
    sovereignty?: string;
    sensitivity?: string;
    masked?: boolean;
    maskMethod?: string;
    notices?: string[];
  };
  provenance?: ProvenanceMeta;
}
~~~

### Story Node alignment

Graph utilities must support Story Node v3 expectations:

- Story Nodes are structured entities with:
  - title + narrative text
  - spatial extent
  - temporal extent
  - linked entities
  - evidence links / provenance

Graph utilities must:
- preserve the separation of facts vs interpretation vs speculation flags if present
- ensure evidence links remain attached through normalization
- ensure story node relations do not imply unverified facts (no relationship invention)

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["API response\n(nodes + relationships + metadata)"] --> B["relationFlatten.ts\n- dedupe\n- stable sort\n- suppress restricted edges"]
  B --> C["entityNormalize.ts\n- typed entities\n- temporal/spatial normalize\n- governance masking"]
  C --> D["groupByType.ts\n- buckets for UI"]
  D --> E["focusBindings.ts\n- FocusContext\n- timeline window\n- safe bbox\n- related sets"]
  E --> F["UI render\n(Focus Mode + Story Nodes + Map + Timeline)\n+ provenance + governance overlays"]
~~~

## 🧪 Validation & CI/CD

Graph utilities are high-impact and must be continuously validated.

Required test coverage:

~~~text
tests/unit/web/utils/graph/**
tests/integration/web/utils/graph/**
~~~

Minimum test categories:

- Normalization correctness (entity types, required fields, fallbacks)
- Deterministic ordering (stable sort and stable dedupe)
- Governance filtering:
  - masked geometry stays masked
  - restricted ids do not appear in URL-oriented outputs
  - suppressed relationship types remain suppressed
- Provenance retention (PROV fields and evidence trails survive transforms)
- Temporal safety:
  - fuzzy/approx dates remain fuzzy/approx
  - no precision sharpening
- FocusContext stability (same input → same context result)

CI expectations (see `.github/workflows/**`):

- TypeScript checks (strict)
- Unit/integration tests
- Schema validation where applicable
- Governance and security gating aligned with repository standards and policies

## ⚖ FAIR+CARE & Governance

This layer is explicitly governed.

It MUST:

- Respect CARE labels and sovereignty flags attached to entities/edges
- Prevent precision leakage for protected locations (do not derive fine geometry)
- Prevent narrative leakage through “implied” edges (no relationship fabrication)
- Preserve license/rights-holder metadata on datasets/documents
- Allow the UI to present governance notices (“coordinates blurred due to policy”)

It MUST NOT:

- reconstruct restricted coordinates from generalized forms
- infer relationships that are not present in the graph/API payload
- silently drop governance metadata
- bypass upstream policy failures (if something is missing, fail safe)

Indigenous rights flag behavior:

- When `indigenous_rights_flag: true` is relevant for a returned entity:
  - masking/generalization is the default posture
  - any override requires explicit policy and must not be performed by frontend utilities

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-15 | KFM-MDP v11.2.6 compliance pass (single H1, approved H2 registry, fence profile). Expanded contracts, governance filtering model, provenance retention rules, and Focus Mode integration guidance. |
| v11.2.2 | 2025-11-28 | Emoji layout refresh; aligned with Focus Mode v3, Story Node v3, CARE masking, and CI/schema expectations. |
| v11.0.0 | 2025-11-24 | v11 alignment for graph-to-UI normalization, provenance propagation, and deterministic relationship flattening. |
| v10.4.1 | 2025-11-15 | Initial v10.4 graph-utils documentation. |
| v10.3.2 | 2025-11-14 | Early graph extraction logic. |
| v10.3.1 | 2025-11-13 | Initial utilities overview. |

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
FAIR+CARE Certified · Public · Version-Pinned  

[⬅️ Back to Web Utils](../README.md) · [🧭 Web Source Overview](../../README.md) · [🛡 Governance Charter](../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
