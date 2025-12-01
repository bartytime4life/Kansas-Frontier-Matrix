---
title: "📍 Kansas Frontier Matrix — Places Entities Architecture (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/entities/places/README.md"
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
telemetry_ref: "../../../releases/v11.2.2/web-entities-places-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/web-entities-places-v2.json"
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
intent: "web-entities-places"
role: "overview"

fair_category: "F1-A1-I1-R1"
care_label: "Public / Mixed (place-dependent)"
sensitivity_level: "Place-dependent"
public_exposure_risk: "Medium"
indigenous_rights_flag: "Conditional"
data_steward: "KFM FAIR+CARE Council"
risk_category: "Mixed"
redaction_required: true

provenance_chain:
  - "web/src/entities/places/README.md@v10.3.2"

ontology_alignment:
  cidoc: "E53 Place / E28 Conceptual Object"
  schema_org: "Place"
  owl_time: "TemporalEntity"
  geosparql: "geo:Feature"
  prov_o: "prov:Entity"

json_schema_ref: "../../../schemas/json/web-entities-places-readme-v11.schema.json"
shape_schema_ref: "../../../schemas/shacl/web-entities-places-readme-v11-shape.ttl"
doc_uuid: "urn:kfm:doc:web-entities-places-readme-v11.2.2"
semantic_document_id: "kfm-doc-web-entities-places-readme-v11"
event_source_id: "ledger:web/src/entities/places/README.md"
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
classification: "Public (Places entities; CARE-governed)"

ttl_policy: "Review each major release"
sunset_policy: "Superseded upon Places Entities v12 upgrade"
---

<div align="center">

# 📍 **Kansas Frontier Matrix — Places Entities Architecture**  
`web/src/entities/places/README.md`

**Purpose:**  
Define the **deep-architecture, FAIR+CARE-certified semantic model** for **Places** entities in the Kansas Frontier Matrix (KFM) v11.2.2 web platform.  
This module converts Neo4j spatial nodes, STAC/DCAT metadata, lineage references, governance constraints, and Focus Mode v3 insights into  
a **canonical Places view-model** suitable for map rendering, story navigation, timeline alignment, and provenance auditing.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)]()  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Places-orange)]()  
[![Status](https://img.shields.io/badge/Status-Stable-success)]()  
[![License: MIT](https://img.shields.io/badge/License-MIT-green)]()

</div>

---

## 📘 Overview

The **Places Entities Layer** models every place represented in KFM:

- Historical, cultural, administrative, ecological, or geospatial sites  
- GNIS features, archival map references, tribal lands, settlements, hydrologic units  
- Spatial geometries (points, polygons, multipolygons) governed by CARE + sovereignty rules  
- Temporal changes (boundary shifts, settlement phases, renaming, jurisdictional changes)  
- Provenance chains: STAC → DCAT → dataset → document → graph nodes  
- CARE governance rules for sensitive & sovereignty-limited locations  
- Explainability integration for Focus Mode v3 (e.g., why a place is highlighted for a focus entity)  
- Accessibility & sustainability metadata for map and story UIs  

This results in a **trusted, explainable, governed spatial model** for all KFM interface layers.

---

## 🗂️ Directory Layout

~~~text
web/src/entities/places/
│
├── 📘 README.md           # This file
├── 🧬 placeViewModel.ts   # TypeScript contract + builder for PlaceVM
├── 🧭 placeMapper.ts      # Graph/STAC/DCAT → PlaceVM transformation logic
└── 📝 metadata.json       # Provenance, governance, and telemetry metadata
~~~

- `placeViewModel.ts` → TypeScript contract and helpers for Places entities.  
- `placeMapper.ts` → deterministic mapper from Neo4j + external data to canonical PlaceVM.  
- `metadata.json` → domain metadata, governance notes, and test coverage hints.

---

## 🧩 High-Level Places Entity Flow

*(Use ```mermaid``` in repo; `~~~mermaid` here to keep a single safe fence.)*

~~~mermaid
flowchart TD
    RAW[Neo4j Place Node<br/>+ STAC/DCAT Assets + Story Nodes] --> MAP[placeMapper]
    MAP --> VM[placeViewModel<br/>canonical PlaceVM]
    VM --> UI[MapView · DetailDrawer · TimelineView · StoryNodes · FocusMode]
    VM --> GOV[Governance Layer<br/>CARE · sovereignty · masking]
    VM --> TEL[Telemetry Layer]
~~~

---

## 🧬 Places View-Model Specification

### `PlaceVM` (conceptual)

~~~ts
export type PlaceVM = {
  id: string;
  type: "place";

  label: string;                    // display name
  alternateNames?: string[];        // historic or variant names
  description?: string;             // accessible narrative description

  geometry?: {
    type: "Point" | "Polygon" | "MultiPolygon" | string;
    centroid?: [number, number];    // [lon, lat] generalized
    bbox?: [number, number, number, number]; // [minX,minY,maxX,maxY]
    masked?: boolean;               // CARE-enforced masking toggle
    generalizationLevel?: "h3-r7" | "h3-r6" | "county" | "region" | "none";
  };

  temporal?: {
    validFrom?: string;             // ISO date or datetime
    validTo?: string;               // ISO date or datetime
    historicalPeriod?: string;      // label (e.g., "Territorial Kansas", "Dust Bowl")
    originalLabel?: string;         // raw temporal label (e.g., "ca. 1870s")
  };

  categories?: string[];            // settlement, hydrology, tribal land, hazard zone, etc.

  provenance: {
    sourceIds: string[];            // dataset/document IDs
    stacRefs?: string[];            // STAC collection/item identifiers
    lineage?: string[];             // pipeline step IDs or URIs
    ledgerRefs?: string[];          // governance ledger entries
    checksumVerified?: boolean;
  };

  care: {
    label: "public" | "sensitive" | "restricted" | "sovereignty-controlled";
    sovereignty?: string;           // tribal governance domain or other sovereignty regime
  };

  explainability?: {
    relevanceScore?: number;        // Focus Mode ranking
    evidenceSources?: string[];     // dataset, event, or Story Node IDs that explain emphasis on this place
  };

  accessibility?: {
    longDescription?: string;       // full narrative description for SR/drawer
    shortLabel?: string;            // compact label for map tooltips, legends
  };
};
~~~

PlaceVMs MUST be validated using TS strict mode + JSON Schema guards (`schemaGuards.ts`).

---

## 🗺️ Spatial Handling & Governance

### Geometry Treatment

The Places layer **never** exposes raw, high-resolution geometry directly into PlaceVM where it would be unsafe. Instead:

- Computes accurate-but-generalized **centroids** for anchoring map markers.  
- Extracts **bounding boxes** for 2D/3D zoom and framing.  
- Uses **masking strategies** for sensitive or sovereignty-limited geometry, e.g.:

  - H3 r7/r6 generalization for maskable areas  
  - County/region-level generalization for protected sites  
  - Complete omission of geometry (with explicit `masked = true`) where required  

### Spatial Governance Flow

~~~mermaid
flowchart TD
    META[Place Metadata<br/>geometry + CARE + sovereignty] --> MASK[Masking Engine]
    MASK --> SVM[Governed Spatial Block<br/>PlaceVM.geometry]
~~~

Sensitive locations (burial sites, archaeological areas, protected tribal lands) MUST be masked or generalized per governance policy.

---

## 📑 Provenance Integration

Places require **full provenance visibility**, including:

- STAC Items & Collections referencing the place  
- DCAT dataset records with spatial coverage including the place  
- Document lineage (archival maps, surveys, gazetteers)  
- Dataset & checksum verification for spatial layers  

Conceptual flow:

~~~mermaid
flowchart LR
    GEO[Place Node] --> STACREF[STAC/DCAT Provenance]
    STACREF --> PROV[Lineage Builder]
    PROV --> PVM[PlaceVM<br/>provenance block]
~~~

Provenance fields help users and systems answer:

- *Why does KFM know about this place?*  
- *Which datasets and documents support the geometry and label?*  

---

## 🧠 Explainability Integration

Focus Mode v3 and other reasoning layers may surface a place because:

- It appears in many relevant events or Story Nodes.  
- It overlaps with high-importance datasets (e.g., hazard zones, treaty lands).  
- It is central to an entity’s narrative (e.g., key battle site, major river confluence).

Explainability in `PlaceVM.explainability` must:

- Record `relevanceScore` as a numeric summary (no hidden semantics).  
- Provide `evidenceSources` listing related entities/datasets used for emphasis.  
- NOT generate new reasoning; only encode what upstream explainability pipelines produce.

---

## ♿ Accessibility Requirements

PlaceVM must provide **A11y-ready** fields:

- `label` and `shortLabel` for concise announcements (map hover, card titles).  
- `accessibility.longDescription` for rich textual descriptions used in DetailDrawer or fully narrated views.  
- Structured category labels (e.g., “historic settlement”, “tribal land”, “flood-prone reach”) to be converted to screenreader text.

Accessibility flow:

~~~mermaid
flowchart TD
    PVM[PlaceVM] --> A11Y[A11y Text Builder]
    A11Y --> UI[Accessible Components<br/>Map tooltips · Drawers · StoryNodes]
~~~

Descriptions MUST avoid stigmatizing language and acknowledge uncertainty where applicable.

---

## 📡 Telemetry Integration

Place-entity interactions emit telemetry such as:

- `place:select`                — user opens a place detail  
- `place:focus-used`            — place is used as a Focus Mode context  
- `place:mask-applied`          — masking/generalization applied in map or story view  
- `place:relation-navigate`     — navigation to related events/people/datasets  

Telemetry is aggregated in:

~~~text
../../../releases/v11.2.2/web-entities-places-telemetry.json
~~~

Telemetry MUST:

- Conform to `telemetry_schema`.  
- Avoid PII (use internal IDs, not names).  
- Respect CARE labels; counts for sensitive/restricted places should only be reported in aggregate.

---

## 🔐 FAIR+CARE Governance Integration

Places may require:

- **Sovereignty markers** (tribal lands, co-managed territories).  
- **Restricted-view redactions** for highly sensitive locations.  
- **Consent-dependent visibility** for certain kinds of Indigenous data or community contributions.  
- Preservation of Indigenous knowledge protocols (e.g., some place knowledge not visible or generalized publicly).

Governance decisions and audits are logged at:

~~~text
../../../docs/reports/audit/web-entities-places-governance.json
~~~

Governance rules MUST:

- Never downgrade protections (e.g., from restricted → public) without explicit governance approval and ledger entry.  
- Ensure `PlaceVM.care` matches the strictest known rules for that place.

---

## ⚙️ CI / Validation Requirements

**Contracts and validators:**

| Contract      | Validator / Workflow       |
|---------------|----------------------------|
| Schema        | `schemaGuards.ts` + JSON Schema for PlaceVM |
| Governance    | `faircare-validate.yml`    |
| Telemetry     | `telemetry-export.yml`     |
| Accessibility | `accessibility_scan.yml` (via consuming components) |
| Security      | CodeQL + Trivy             |
| Documentation | `docs-lint.yml`            |

Any change in Places Entities MUST pass all of the above before merge.

---

## 🧾 Example Places Metadata Record

~~~json
{
  "id": "places_entities_v11.2.2",
  "entities_indexed": 10340,
  "care_public": 9600,
  "care_sensitive": 580,
  "care_restricted": 160,
  "sovereignty_flags": 260,
  "provenance_complete": true,
  "telemetry_linked": true,
  "a11y_ready": true,
  "timestamp": "2025-11-30T23:59:00Z"
}
~~~

This record summarizes the Places index status for a given release; it is not part of PlaceVM itself.

---

## 🕰 Version History

| Version | Date       | Summary                                                                                                                                                                      |
|--------:|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-30 | Upgraded to v11.2.2; strengthened geometry governance, CARE & sovereignty semantics, telemetry v2, energy/carbon tracking, and alignment with KFM-OP v11 + KFM-MDP v11.2.2. |
| v10.3.2 | 2025-11-14 | Deep-architecture creation: geometry governance, provenance lineage, explainability integration, accessibility + sustainability hooks.                                       |

---

<div align="center">

**Kansas Frontier Matrix — Places Entities Architecture**  
📍 Ethical Spatial Modeling · 🔗 Provenance Fidelity · 🔐 Sovereignty-Aware Governance  

[Back to Entities Index](../README.md) •  
[Docs Root](../../../README.md) •  
[Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

© 2025 Kansas Frontier Matrix — MIT License  

**End of Document**

</div>