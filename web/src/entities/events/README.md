---
title: "📅 Kansas Frontier Matrix — Events Entities Architecture (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/entities/events/README.md"
version: "v11.2.2"
last_updated: "2025-11-30"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../releases/v11.2.2/web-entities-events-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/web-entities-events-v2.json"
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
intent: "web-entities-events"
role: "overview"

fair_category: "F1-A1-I1-R1"
care_label: "Public / Mixed (event-dependent)"
sensitivity_level: "Event-dependent"
public_exposure_risk: "Medium"
indigenous_rights_flag: "Conditional"
data_steward: "KFM FAIR+CARE Council"
risk_category: "Mixed"
redaction_required: true

provenance_chain:
  - "web/src/entities/events/README.md@v10.3.2"

ontology_alignment:
  cidoc: "E5 Event / E52 Time-Span / E53 Place / E31 Document"
  schema_org: "Event"
  owl_time: "TemporalEntity"
  geosparql: "geo:Feature"
  prov_o: "prov:Entity"

json_schema_ref: "../../../schemas/json/web-entities-events-readme-v11.schema.json"
shape_schema_ref: "../../../schemas/shacl/web-entities-events-readme-v11-shape.ttl"
doc_uuid: "urn:kfm:doc:web-entities-events-readme-v11.2.2"
semantic_document_id: "kfm-doc-web-entities-events-readme-v11"
event_source_id: "ledger:web/src/entities/events/README.md"
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
classification: "Public (event semantics with CARE exceptions)"

ttl_policy: "Review each major release"
sunset_policy: "Superseded upon Events Entities v12 upgrade"
---

<div align="center">

# 📅 **Kansas Frontier Matrix — Events Entities Architecture**  
`web/src/entities/events/README.md`

**Purpose:**  
Define the **deep, FAIR+CARE-certified semantic View-Model architecture** for **Events** in the Kansas Frontier Matrix (KFM) v11.2.2 web platform.  
Events represent **time-bounded happenings** (historical, cultural, environmental, administrative), linking people, places, datasets,  
Story Nodes, and predictive timelines into a unified, governed semantic structure.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)]()  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Events-orange)]()  
[![Status: Stable](https://img.shields.io/badge/Status-Stable-success)]()  
[![License: MIT](https://img.shields.io/badge/License-MIT-green)]()

</div>

---

## 📘 Overview

The **Events Entities Layer** harmonizes all event-based knowledge across Kansas Frontier Matrix:

- Historical events (treaties, settlements, conflicts, migrations)  
- Cultural and tribal events (ceremonies, displacements, boundary changes)  
- Environmental events (floods, droughts, wildfires, storms)  
- Administrative & institutional events (county formation, land patents, resource extraction, policy changes)  
- Predictive scenario events (future drought windows, hazard projections 2030–2100, climate scenarios)  

Events serve as **temporal anchors** for Focus Mode v3, TimelineView, MapView overlays, Story Nodes, and Diff-First change logs.  
They provide the core “when + where + who + what happened” semantics for the KFM graph.

---

## 🗂️ Directory Layout

~~~text
web/src/entities/events/
│
├── 📘 README.md            # This file (architecture + governance spec)
├── 🧬 eventViewModel.ts    # Typed EventVM contract + builder helpers
├── 🧭 eventMapper.ts       # Raw graph/data → EventVM normalization
└── 📝 metadata.json        # CARE + provenance validations + telemetry lineage
~~~

- `eventViewModel.ts` — defines the EventVM TypeScript type + construction helpers.  
- `eventMapper.ts` — maps Neo4j/ETL outputs, STAC/DCAT links, and Story Nodes into canonical EventVM.  
- `metadata.json` — contains domain-level notes (schemas, governance flags, and test coverage metadata).

---

## 🧩 High-Level Events Flow

*(Use ```mermaid``` in repo; `~~~mermaid` here to keep this one-fence block safe.)*

~~~mermaid
flowchart TD
    RAW[Neo4j Event Node<br/>+ STAC/DCAT + Story Nodes] --> MAP[eventMapper]
    MAP --> VM[eventViewModel<br/>canonical EventVM]
    VM --> UI[UI Systems<br/>TimelineView · MapView · DetailDrawer · FocusMode · StoryNodes]
    VM --> GOV[Governance Layer<br/>CARE · sovereignty · provenance]
    VM --> TEL[Telemetry Layer]
~~~

---

## 🧬 Event View-Model Specification

### `EventVM` (conceptual)

~~~ts
export type EventVM = {
  id: string;
  type: "event";
  label: string;                       // event name/title
  description?: string;                // accessible narrative summary

  temporal: {
    start?: string;                    // ISO datetime or date (start)
    end?: string;                      // ISO datetime or date (end)
    durationDays?: number;             // computed if applicable
    periodLabel?: string;              // e.g. "Bleeding Kansas", "Dust Bowl"
    precision?: "year" | "month" | "day" | "approximate";
    predictive?: boolean;              // future scenario indicator
    originalLabel?: string;            // e.g. "late 19th century", "winter 1863–64"
  };

  spatial?: {
    centroid?: [number, number];       // [lon, lat] generalized
    bbox?: [number, number, number, number];
    geometryMasked?: boolean;          // CARE protection applied to geometry
    generalizationLevel?: "h3-r7" | "county" | "region" | "none";
  };

  participants?: string[];             // Person IDs (EntityVM IDs)
  placesInvolved?: string[];           // Place IDs
  datasets?: string[];                 // Dataset IDs (STAC/DCAT)
  storyNodes?: string[];               // Story Node IDs (narrative wrappers)

  provenance: {
    sourceIds: string[];               // primary sources (documents, datasets)
    stacRefs?: string[];               // STAC collection/item IDs or URIs
    lineage?: string[];                // transformation chain references
    ledgerRefs?: string[];             // governance ledger entries
    checksumVerified?: boolean;        // integrity check result
  };

  care: {
    label: "public" | "sensitive" | "restricted" | "sovereignty-controlled";
    sovereignty?: string;              // e.g., "Kaw Nation", "Osage", etc.
  };

  explainability?: {
    relevanceScore?: number;          // used for Focus Mode ranking
    evidenceSources?: string[];       // dataset/story/evidence IDs supporting the event
  };

  accessibility?: {
    longDescription?: string;         // rich narrative for screen readers
    shortLabel?: string;              // condensed label for timelines/lists
  };
};
~~~

EventVMs MUST be validated via TypeScript + JSON Schema guards.

---

## ⏳ Temporal Semantics

Event temporal information must support:

- **Rigid time spans** (explicit `start` and `end` dates/times)  
- **Fuzzy dates** (decade, season, approximate ranges) with `precision` and `originalLabel`  
- **Multi-era alignment** for historical/archival events (e.g., event spanning multiple years/periods)  
- **Predictive future periods** (2030–2050, 2050–2100, etc.) clearly marked with `predictive = true`  
- **Timeline “density bins”** for aggregated visualizations (handled in TimelineView but driven by EventVM)  

### Temporal Mapping Pipeline

~~~mermaid
flowchart TD
    TRaw[Raw Temporal Fields<br/>Neo4j · ETL] --> TNorm[Temporal Normalizer]
    TNorm --> TInfer[Derivation Layer<br/>durationDays · fuzzy ranges]
    TInfer --> TEVM[Event Temporal Block<br/>EventVM.temporal]
~~~

Rules:

- Unknown bounds must not be guessed; use open-ended intervals or `precision = "approximate"`.  
- Period labels (`periodLabel`) must come from curated sources (e.g., recognized historical eras), not heuristics.

---

## 🗺️ Spatial Semantics

Spatial data must include:

- `centroid` for geographic anchoring in MapView/Focus Mode  
- `bbox` for map auto-zoom and frame selection  
- Optional geometry linking (via Place EVMs, hydrologic regions, etc.)  
- **Masking rules** for CARE-sensitive locations:
  - geometry not in EventVM, only generalized fields  
  - `geometryMasked = true` + `generalizationLevel` specifying coarseness  
- Sovereignty overlays for tribal territories (applied via Governance & Place layers)

Spatial governance flow:

~~~mermaid
flowchart TD
    GEO[Raw Event Geometry] --> MASK[CARE Mask Handler]
    MASK --> GEOOUT[Governed Spatial Block<br/>spatial.* fields]
~~~

---

## 🔗 Relationship Semantics

Events unify multiple entity classes:

| Relationship    | Direction        | Notes                                      |
|-----------------|------------------|--------------------------------------------|
| Participants    | event → people   | may include implicit relevance weighting   |
| Places Involved | event → places   | must support governance masking            |
| Linked Datasets | event ↔ datasets | provenance + evidence for event claims     |
| Story Nodes     | event ↔ story    | narrative contextualization and grouping   |
| Event Clusters  | event ↔ event    | historical phases, thematic or causal ties |

All relationships must be:

- **Graph-derived** (from Neo4j or curated sources)  
- Explicit in provenance (which sources support which edges)  

---

## 🧱 Event Mapper — `eventMapper.ts`

### Responsibilities

- Coerce raw graph nodes into strict, canonical EventVM.  
- Normalize temporal formats (ISO 8601, precision semantics).  
- Extract and govern spatial metadata using Place EVM & governance rules.  
- Apply CARE and sovereignty rules:  
  - mark events as `sensitive` or `sovereignty-controlled` when appropriate  
- Connect EventVM to Story Node lineage (narrative overlays).  
- Validate provenance integrity (must have clear sources for key claims).  
- Produce accessible summaries where textual metadata is available (no speculation).

### Mapping Architecture

~~~mermaid
flowchart TD
    EN["Raw Event Node"] --> CLEAN["Field Normalization"]
    CLEAN --> CAREPROC["CARE Processor<br/>sovereignty + sensitivity"]
    CAREPROC --> PROV["Provenance Enricher"]
    PROV --> TEMP["Temporal Formatter"]
    TEMP --> SPAT["Spatial Formatter"]
    SPAT --> FINAL["EventVM<br/>canonical, governed, a11y-ready"]
~~~

---

## 🔐 FAIR+CARE Governance

Governance concerns for events include:

- Politically sensitive periods (e.g., conflict or contested history)  
- Tribal or Indigenous sovereignty (events on/related to Indigenous lands)  
- Private/restricted archival material (e.g., personal diaries, restricted collections)  
- Sensitive environmental hazard data (e.g., locations of at-risk infrastructure)  
- Events relating to trauma or violence (must be handled with care, disclaimers, and masking)

Governance output and audit trails for events are stored in:

~~~text
../../../docs/reports/audit/web-entities-events-governance.json
~~~

Rules:

- Events tagged as restricted/sensitive must propagate those flags through EventVM.care.  
- Events associated with protected sites must rely on generalized spatial semantics; no raw coordinates are exposed through EventVM.

---

## 🧠 Explainability Integration (Focus Mode v3)

EventVM supports:

- `relevanceScore` for Focus Mode ranking and evidence weighting.  
- `evidenceSources` linking to datasets/Story Nodes/documents that justify the event’s inclusion or prominence.  
- Consistent semantics for Focus Mode explanation deltas:
  - when relevance changes between releases  
  - when evidence sources are added/removed  

Focus Mode uses EventVM as a **semantic anchor**, not as a place to compute new explanations.

---

## ♿ Accessibility & Narrative Integrity

EventVM must include:

- Screenreader-ready labels (shortLabel + label).  
- Long narrative summaries (`accessibility.longDescription`) when available and permitted by governance.  
- Clear and unambiguous date descriptions from `temporal` data (UI can derive human-readable versions).  
- Relationship descriptions that avoid conflating correlation and causation (no speculative statements).

Accessibility flow:

~~~mermaid
flowchart TD
    EVM[EventVM] --> A11Y[a11y Summary Builder]
    A11Y --> UI[Accessible UI Components]
~~~

---

## 📡 Telemetry Integration

Event usage emits telemetry via UI/hooks, which is tied back to EventVM:

Common events:

- `event:select`              — user opens an event detail  
- `event:focus-used`          — event is set as Focus entity  
- `event:mask-applied`        — spatial or narrative masking triggered  
- `timeline:jump-triggered`   — user jumps to event’s time range via timeline  

Telemetry target for v11.2.2:

~~~text
../../../releases/v11.2.2/web-entities-events-telemetry.json
~~~

Telemetry MUST:

- be non-PII  
- respect CARE flags (aggregated for sensitive events)  
- follow the schema in `telemetry_schema`.

---

## ⚙️ CI / Validation Requirements

**Validation layers:**

| Layer         | Validator / Job                |
|--------------:|--------------------------------|
| Type safety   | TS strict mode                 |
| Schema        | `schemaGuards.ts` for EventVM  |
| Governance    | `faircare-validate.yml`        |
| Telemetry     | `telemetry-export.yml`         |
| Accessibility | `accessibility_scan.yml` (via consuming UI) |
| Security      | CodeQL + Trivy                 |
| Documentation | `docs-lint.yml`                |

No event-related changes may be merged if governance or schema validation fails.

---

## 🧾 Example Events Metadata Record

~~~json
{
  "id": "events_entities_v11.2.2",
  "entities_indexed": 20340,
  "care_public": 18220,
  "care_sensitive": 1660,
  "care_restricted": 460,
  "provenance_complete": true,
  "timeline_visible": true,
  "telemetry_linked": true,
  "timestamp": "2025-11-30T23:59:00Z"
}
~~~

This metadata record summarizes an index state for a release; it is not part of EventVM.

---

## 🕰 Version History

| Version | Date       | Summary                                                                                                                                                                            |
|--------:|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-30 | Upgraded to v11.2.2; strengthened CARE/sovereignty semantics, telemetry v2 integration, energy/carbon schemas, and alignment with KFM-OP v11 + KFM-MDP v11.2.2 across all events. |
| v10.3.2 | 2025-11-14 | Deep-architecture build: canonical EventVM, sovereignty masking, predictive-period handling, explainability linking, provenance expansions, a11y + telemetry hooks.               |

---

<div align="center">

**Kansas Frontier Matrix — Events Entities Architecture**  
📅 Temporal Semantics · 🌐 FAIR+CARE Governance · 🔗 Provenance Integrity · 🧠 Explainable Event Modeling  

[Back to Entities Index](../README.md) •  
[Docs Root](../../../README.md) •  
[Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

© 2025 Kansas Frontier Matrix — MIT License  

**End of Document**

</div>