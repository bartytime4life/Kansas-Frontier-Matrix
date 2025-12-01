---
title: "👤 Kansas Frontier Matrix — People Entities Architecture (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/entities/people/README.md"
version: "v11.2.2"
last_updated: "2025-11-30"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Autonomous + FAIR+CARE Council"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../releases/v11.2.2/web-entities-people-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/web-entities-people-v2.json"
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
intent: "web-entities-people"
role: "overview"

fair_category: "F1-A1-I1-R1"
care_label: "Public / Mixed (person-dependent)"
sensitivity_level: "Person-dependent"
public_exposure_risk: "Medium"
indigenous_rights_flag: "Conditional"
data_steward: "KFM FAIR+CARE Council"
risk_category: "Mixed"
redaction_required: true

provenance_chain:
  - "web/src/entities/people/README.md@v10.3.2"

ontology_alignment:
  cidoc: "E21 Person / E39 Actor"
  schema_org: "Person"
  owl_time: "TemporalEntity"
  geosparql: "geo:Feature"
  prov_o: "prov:Entity"

json_schema_ref: "../../../schemas/json/web-entities-people-readme-v11.schema.json"
shape_schema_ref: "../../../schemas/shacl/web-entities-people-readme-v11-shape.ttl"
doc_uuid: "urn:kfm:doc:web-entities-people-readme-v11.2.2"
semantic_document_id: "kfm-doc-web-entities-people-readme-v11"
event_source_id: "ledger:web/src/entities/people/README.md"
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
classification: "Public (People entities, CARE-governed)"

ttl_policy: "Review each major release"
sunset_policy: "Superseded upon People Entities v12 upgrade"
---

<div align="center">

# 👤 **Kansas Frontier Matrix — People Entities Architecture**  
`web/src/entities/people/README.md`

**Purpose:**  
Define the **deep-architecture, FAIR+CARE-certified view-model layer** for **People** entities in the KFM v11.2.2 web platform.  
This module translates Neo4j graph nodes, STAC/DCAT metadata, Story Nodes, and Focus Mode v3 outputs into **canonical People view models**  
that are governance-safe, explainable, accessible, and telemetry-aware.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)]()  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-People-orange)]()  
[![Status](https://img.shields.io/badge/Status-Stable-success)]()  
[![License: MIT](https://img.shields.io/badge/License-MIT-green)]()

</div>

---

## 📘 Overview

The **People Entities Layer** models individuals (historic, contemporary, and synthetic personas) in KFM:

- Biographical & role metadata  
- Relationships to places, events, datasets, Story Nodes  
- Sovereignty and CARE-sensitive status (where appropriate)  
- Temporal presence (lifespans, active periods)  
- Provenance & lineage paths (archives, censuses, treaties, oral histories)  
- Explainability & Focus Mode v3 relevance  
- Accessibility-ready descriptions  
- Telemetry annotations for entity-centric interactions  

This layer ensures People entities are **semantically consistent, ethically represented, and technically reproducible** across the UI.

---

## 🗂️ Directory Layout

~~~text
web/src/entities/people/
│
├── 📘 README.md           # This file
├── 🧬 personViewModel.ts  # People EVM type + builder helpers
├── 🧭 personMapper.ts     # Raw graph/API → PersonVM normalization
└── 📝 metadata.json       # Governance + provenance + telemetry metadata
~~~

- `personMapper.ts` — converts raw graph/API responses into normalized PersonVMs.  
- `personViewModel.ts` — exports typed People view-model contracts and helpers.  
- `metadata.json` — governance, CARE, and telemetry metadata for People entities.

---

## 🧩 High-Level People Entity Flow

*(Use ```mermaid``` in-repo; `~~~mermaid` here avoids nested fences.)*

~~~mermaid
flowchart TD
    RAW[Neo4j Person Node<br/>+ STAC/DCAT + StoryNodes] --> MAP[personMapper]
    MAP --> VM[personViewModel<br/>canonical PersonVM]
    VM --> UI[UI Systems<br/>DetailDrawer · FocusMode · MapView · TimelineView · DataCards]
    VM --> GOV[Governance Layer<br/>CARE · sovereignty · provenance]
    VM --> TEL[Telemetry Layer]
~~~

---

## 🧬 People View-Model Specification

### `PersonVM` (conceptual)

~~~ts
export type PersonVM = {
  id: string;
  type: "person";

  label: string;                    // primary display name
  alternateNames?: string[];        // aliases / historic names
  description?: string;             // short bio, SR-friendly

  temporal?: {
    birthYear?: number;
    deathYear?: number;
    activeStartYear?: number;
    activeEndYear?: number;
    originalLabel?: string;         // e.g. "fl. 1860s", "early 20th century"
  };

  affiliations?: string[];          // organizations, groups, tribes
  roles?: string[];                 // e.g. "historian", "soldier", "trader"

  spatial?: {
    homeRegions?: string[];         // region/place labels or encoded IDs
    keyPlaces?: string[];           // PlaceVM IDs for major events
  };

  provenance: {
    sourceIds: string[];            // archive IDs, document IDs, dataset IDs
    stacRefs?: string[];            // STAC collections/items referencing this person
    ledgerRefs?: string[];          // governance ledger entries
    checksumVerified?: boolean;
  };

  care: {
    label: "public" | "sensitive" | "restricted" | "sovereignty-controlled";
    sovereignty?: string;           // tribal or sovereignty domain when applicable
  };

  explainability?: {
    relevanceScore?: number;        // Focus Mode v3 ranking
    evidenceSources?: string[];     // dataset or node IDs used as evidence
  };

  accessibility?: {
    longDescription?: string;       // fuller narrative for SR and accessible drawers
    shortLabel?: string;            // shorter label for lists/cards
  };
};
~~~

PersonVMs MUST be validated via TS types + JSON Schema guards (`schemaGuards.ts`).

---

## 🔁 Mapping Pipeline — `personMapper.ts`

The mapping pipeline implements canonicalization and governance:

~~~mermaid
flowchart TD
    PRAW[Raw Person Node<br/>graph/API payloads] --> CLEAN[Normalizer<br/>strip unknowns]
    CLEAN --> CAREPROC[CARE Processor<br/>sovereignty · consent · sensitivity]
    CAREPROC --> PROV[Provenance Enricher]
    PROV --> VM[PersonVM Builder<br/>type-safe construction]
~~~

`personMapper.ts` MUST:

- Coerce raw fields into strict `PersonVM`, discarding or flagging unknown/unsafe fields.  
- Apply CARE governance (masking or redacting non-public data fields as configured).  
- Attach provenance and ledger references for key attributes (e.g., life dates, roles, affiliations).  
- Produce consistent temporal & spatial information (no ad hoc heuristics).  
- Provide a11y-ready textual fields (no speculation; only data-backed narrative).

---

## 🔐 FAIR+CARE Governance Integration

People entities often require **special handling** for:

- Indigenous individuals and communities  
- Minors or vulnerable persons  
- Potentially living persons represented in data  
- Sensitive historical roles (e.g., victims, perpetrators, marginalized groups)

The mapping layer MUST:

- Propagate CARE labels from graph/metadata into `PersonVM.care`.  
- Mask or generalize restricted individuals for public-facing UIs:
  - e.g., hide detailed biography, show only high-level references  
- Attach sovereignty flags where relevant (tribal affiliation, governance context).  
- Route all governance decisions to `metadata.json` + ledger entries.

Governance pipeline:

~~~mermaid
flowchart TD
    META[Person Metadata<br/>CARE + sovereignty] --> GPROC[Governance Processor]
    GPROC --> PVM[PersonVM<br/>governed]
    PVM --> LEDGER[Governance Ledger<br/>audit entries]
~~~

Governance log path:

~~~text
../../../docs/reports/audit/web-entities-people-governance.json
~~~

Any mislabeling or mis-propagation of CARE/sovereignty metadata is **CI-blocking**.

---

## 📡 Telemetry Integration

People entity usage contributes to telemetry such as:

- `person:select` — user opens person detail  
- `person:focus-used` — person used as Focus Mode entity  
- `person:care-gated` — person view restricted by CARE rules  
- `person:relation-navigate` — navigation via Person relations  

Telemetry target for v11.2.2:

~~~text
../../../releases/v11.2.2/web-entities-people-telemetry.json
~~~

Telemetry MUST:

- Conform to `telemetry_schema`.  
- Avoid PII beyond internal entity IDs (no names in telemetry data).  
- Respect CARE labels — e.g., aggregated reporting for sensitive/restricted persons.

---

## ♿ Accessibility & Inclusive Representation

People entity models MUST support:

- Screenreader-friendly naming & descriptions:
  - Distinguish between label/shortLabel/longDescription.  
- Clear indication of tribal affiliations & sovereignty (if present) in ways that respect community guidance.  
- Inclusive, non-stigmatizing language in descriptions (no speculation or editorializing).  
- Explicit labeling for cases where details are removed or generalized due to CARE rules:
  - e.g., “Details removed due to privacy and governance rules” instead of silent omission.  

Accessibility flow:

~~~mermaid
flowchart TD
    PVM[PersonVM] --> A11Y[a11y Text Generator]
    A11Y --> UI[Accessible UI Components]
~~~

Components must map PersonVM fields into SR-friendly text consistently across the UI.

---

## ⚙️ CI / Validation Requirements

**Contracts and validations:**

| Contract           | Validator / Workflow     |
|--------------------|--------------------------|
| Type safety        | TS strict mode           |
| Schema correctness | `schemaGuards.ts`        |
| Governance fields  | `faircare-validate.yml`  |
| Accessibility meta | `accessibility_scan.yml` (via consumers) |
| Telemetry logs     | `telemetry-export.yml`   |
| Docs compliance    | `docs-lint.yml`          |
| Security           | CodeQL + Trivy           |

No People VM–related change can be merged if **any** of these checks fail.

---

## 🧾 Example People Metadata Record

~~~json
{
  "id": "people_entities_v11.2.2",
  "entities_indexed": 38210,
  "care_public": 34450,
  "care_sensitive": 3460,
  "care_restricted": 300,
  "a11y_ready": true,
  "provenance_complete": true,
  "telemetry_linked": true,
  "timestamp": "2025-11-30T23:59:00Z"
}
~~~

This record summarizes the People Entities index state for a release; it is **not** part of the PersonVM itself.

---

## 🕰 Version History

| Version | Date       | Summary                                                                                                                                                       |
|--------:|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-30 | Upgraded to v11.2.2; aligned PersonVM with KFM-OP v11, FAIR+CARE v11 semantics, telemetry v2, and strengthened CARE/sovereignty & A11y semantics.            |
| v10.3.2 | 2025-11-14 | Deep-architecture creation: canonical PersonVM, CARE + sovereignty integration, provenance linkages, A11y + telemetry hooks.                                 |

---

<div align="center">

**Kansas Frontier Matrix — People Entities Architecture**  
👤 Semantic People Models · 🌐 FAIR+CARE Governance · 🔗 Provenance Integrity · 🧠 AI-Aligned Context  

[Back to Entities Index](../README.md) •  
[Docs Root](../../../README.md) •  
[Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

© 2025 Kansas Frontier Matrix — MIT License  

**End of Document**

</div>