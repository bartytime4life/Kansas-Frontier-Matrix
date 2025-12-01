---
title: "🧬 Kansas Frontier Matrix — Diff-First Entity Model Architecture (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/entities/diff-first/model/README.md"
version: "v11.2.2"
last_updated: "2025-11-30"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Autonomous + FAIR+CARE Council"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/web-entity-diff-model-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/web-entity-diff-model-v2.json"
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

status: "Active / Enforced"
doc_kind: "Architecture Overview"
intent: "web-entity-diff-model"
role: "overview"

fair_category: "F1-A1-I1-R1"
care_label: "Public / Mixed (entity- and dataset-dependent)"
sensitivity_level: "Entity-dependent"
public_exposure_risk: "Medium"
indigenous_rights_flag: "Conditional"
data_steward: "KFM FAIR+CARE Council"
risk_category: "Mixed"
redaction_required: true

provenance_chain:
  - "web/src/entities/diff-first/model/README.md@v10.3.2"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "SoftwareSourceCode"
  owl_time: "TemporalEntity"
  geosparql: "geo:Feature"
  prov_o: "prov:Entity"

json_schema_ref: "../../../../../schemas/json/web-entity-diff-model-readme-v11.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/web-entity-diff-model-readme-v11-shape.ttl"
doc_uuid: "urn:kfm:doc:web-entity-diff-model-readme-v11.2.2"
semantic_document_id: "kfm-doc-web-entity-diff-model-readme-v11"
event_source_id: "ledger:web/src/entities/diff-first/model/README.md"
immutability_status: "version-pinned"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with strict constraints"
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
classification: "Public Model Layer (content-sensitive)"

ttl_policy: "Review each major release"
sunset_policy: "Superseded upon next Diff-First model refactor"
---

<div align="center">

# 🧬 **Kansas Frontier Matrix — Diff-First Entity Model Architecture**  
`web/src/entities/diff-first/model/README.md`

**Purpose:**  
Define the **canonical, deeply-governed diff model architecture** for release-to-release entity comparison in the Kansas Frontier Matrix (KFM).  
This subsystem produces deterministic, FAIR+CARE-certified diffs used by UI components, telemetry, governance ledgers, explainability engines,  
and sustainability workflows under **MCP-DL v6.3** and KFM-MDP v11.2.2.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)]()  
[![License: MIT](https://img.shields.io/badge/License-MIT-green)]()  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Model-orange)]()  
[![Status: Stable](https://img.shields.io/badge/Status-Stable-success)]()

</div>

---

## 📘 Overview

The **Diff-First Entity Model Layer** is the **semantic core** of KFM’s entity-evolution workflow.  
It transforms raw diff responses into **normalized, CARE-aware, provenance-complete, accessibility-ready, telemetry-annotated** `EntityDiff` objects.

It guarantees:

- ✔ Stable & deterministic schema across releases  
- ✔ Provenance continuity (STAC · DCAT · PROV-O · Story Nodes)  
- ✔ CARE-governed masking & sovereignty flags  
- ✔ Explainability deltas for Focus Mode v3  
- ✔ WCAG 2.1 AA+ compatible metadata (via downstream components)  
- ✔ Temporal + spatial change representation  
- ✔ Sustainability metrics for energy + latency (via telemetry hooks)  
- ✔ Strict MCP-DL v6.3 + KFM-OP v11 compliance  

This document is the **authoritative specification** for the diff model.

---

## 🗂️ Directory Layout

~~~text
web/src/entities/diff-first/model/
│
├── 📘 README.md         # This file
├── 📑 diffTypes.ts      # Type definitions and core model types (EntityDiff, PropertyChange, etc.)
└── 📐 normalize.ts      # Normalization pipeline (raw → guarded → governed EntityDiff)
~~~

---

## 🧩 High-Level Architecture

*(Use ```mermaid``` in-repo; we use `~~~mermaid` here to avoid nested-fence issues.)*

~~~mermaid
flowchart TD
    RAW[Raw Diff Response] --> GUARD[Schema Guards]
    GUARD --> CARE[CARE & Sovereignty Enforcement]
    CARE --> NORM[normalize.ts<br/>canonical conversion]
    NORM --> MODEL[EntityDiff Model]
    MODEL --> UI[UI Components]
    MODEL --> TESTS[Test Suite]
    MODEL --> GOV[Governance Engine]
    MODEL --> TEL[Telemetry Pipeline]
~~~

---

## 🧬 Canonical Diff Model

### `EntityDiff`

~~~ts
export type EntityDiff = {
  entityId: string;
  entityType: "person" | "place" | "event" | "dataset";
  releasePrev: string;
  releaseCurr: string;
  summary: DiffSummary;
  properties: PropertyChange[];
  relations: RelationChange[];
  text: TextChange[];
  governance: GovernanceChange;
  explainability?: ExplainabilityDelta[];
};
~~~

### `DiffSummary`

~~~ts
export type DiffSummary = {
  added: number;
  removed: number;
  changed: number;
  severity: "low" | "med" | "high";
};
~~~

`severity` SHOULD be influenced by governance changes (CARE, license, sovereignty) as well as structural/property diffs.

---

## 🔡 Property-Level Diff Types

~~~ts
export type ScalarChange = {
  kind: "scalar";
  key: string;
  from: number | null;
  to: number | null;
  pct?: number | null;
  unit?: string;
  severity: "low" | "med" | "high";
};

export type CategoricalChange = {
  kind: "categorical";
  key: string;
  from: string | null;
  to: string | null;
  severity: "low" | "med" | "high";
};

export type PropertyChange = ScalarChange | CategoricalChange;
~~~

**Notes:**

- `pct` is a convenience for front-end display; must be mathematically consistent with `from`/`to` when present.  
- `unit` MUST be human-readable and aligned with domain standards (e.g., `"km²"`, `"gCO₂e"`, `"persons"`).

---

## 📝 Text Diff Model

~~~ts
export type TextChange = {
  key: string;
  from?: string;
  to?: string;
  mode: "unified" | "split";
  changed: boolean;
  tokens?: number; // approximate affected token count
};
~~~

Text diffs must support:

- Unified & split diff modes (front-end decides how to display)  
- Screenreader-safe segmentation (no raw ANSI diff output)  
- No color-only semantics (UI uses shapes/icons/labels)  

---

## 🔗 Relation Diff Model

~~~ts
export type RelationChange = {
  kind: "added" | "removed";
  relType: string;         // e.g., "LOCATED_IN", "PARTICIPATED_IN"
  targetId: string;        // entity ID of the target
  label: string;           // human-readable label of the target
  confidence?: number;     // 0–1 or similar
  provenance?: string[];   // IDs/URIs of sources that support this relation
};
~~~

Relation diffs must reflect:

- Provenance lineage (which docs/data support relation)  
- Potentially restricted/sensitive targets (to be masked by UI as needed)  
- Story Node and Focus Mode linkages (through consistent IDs)  

---

## 🔐 Governance Diff Model

~~~ts
export type GovernanceChange = {
  careLabelPrev?: string;
  careLabelCurr?: string;
  consentChanged?: boolean;
  sovereigntyDomainChanged?: boolean;
  licenseChanged?: boolean;
  lineageRefs?: string[];     // references in governance ledger or provenance
};
~~~

Governance diffs MUST be considered when:

- Computing `DiffSummary.severity`  
- Surface-level governance callouts in UI (e.g., DiffHeader)  

Changes in CARE or sovereignty status often indicate **high** severity.

---

## 🧠 Explainability Delta Model

~~~ts
export type ExplainabilityDelta = {
  evidenceAdded?: string[];      // IDs of new evidence nodes
  evidenceRemoved?: string[];    // IDs of removed evidence nodes
  relevancePrev?: number;        // previous relevance score
  relevanceCurr?: number;        // current relevance score
  driftDetected?: boolean;       // boolean flag for explanation drift
};
~~~

Tracks reasoning drift between releases for Focus Mode, without recomputing the explanations — ONLY comparing provided values.

---

## 🧪 Normalization Pipeline (`normalize.ts`)

The normalization pipeline enforces:

- Strict type coercion  
- Deterministic ordering of arrays and objects  
- Removal of extraneous or unknown fields  
- CARE/sovereignty protection where applicable  
- Consistency of null/undefined handling across runs  

Pipeline flow:

~~~mermaid
flowchart TD
    RAW["RawDiffResponse"] --> GUARD["schemaGuards<br/>TS + JSON Schema"]
    GUARD --> GOVPROC["Governance Coercion<br/>CARE/Sovereignty application"]
    GOVPROC --> NORM["normalize.ts<br/>canonicalization"]
    NORM --> OUT["EntityDiff (final)<br/>ready for UI + telemetry"]
~~~

If schema or governance coercion fails, `normalize` MUST:

- produce a clear, structured error;  
- NOT silently truncate or reshape unknown fields.

---

## ♿ Accessibility Metadata

The model layer supports accessibility by providing:

- Consistent keys and labels for diff categories (`key` fields)  
- Structured numeric + unit fields for SR-friendly summaries  
- Clear separation of severity classification for potential SR announcements  
- Metadata that allows UI to:

  - announce “X properties added, Y removed, Z changed”  
  - indicate significance (e.g., “high severity governance change”)  

Conceptual flow:

~~~mermaid
flowchart TD
    DIFF[EntityDiff] --> A11Y[a11y Metadata Builder]
    A11Y --> UI[Accessible Diff Components]
~~~

The model does not embed ARIA text, but the structure MUST enable accessible components.

---

## 📡 Telemetry Integration

`normalize.ts` may collaborate with telemetry-oriented utilities to attach:

- `diff_compute_ms`       — time required for diff normalization  
- `governance_deltas`     — count of governance changes  
- `explainability_drift`  — boolean/metric indicating drift  
- `a11y_diff_complexity`  — simple numeric complexity estimate (e.g., number of changed elements)  
- `energy_estimate_wh`    — derived from pipeline metrics, not guessed ad hoc  

Telemetry is appended via services to:

~~~text
../../../../../releases/v11.2.2/web-entity-diff-model-telemetry.json
~~~

Rules:

- Telemetry MUST NOT include PII or raw coordinates or sensitive text.  
- Telemetry schema MUST match `telemetry_schema`.

---

## 🔐 FAIR+CARE Governance Integration

The model layer enforces:

- CARE label propagation from raw diff to `GovernanceChange`  
- Sovereignty boundary change detection (`sovereigntyDomainChanged`)  
- Consent-change detection (`consentChanged`)  
- License transition detection (`licenseChanged`)  
- Lineage continuity via `GovernanceChange.lineageRefs` & provenance fields  

Governance diffs recorded in audit logs (downstream) such as:

~~~text
../../../../../docs/reports/audit/web-entity-diff-model-governance.json
~~~

If the model cannot faithfully represent governance diffs from raw metadata, the error MUST be surfaced (not hidden).

---

## ⚙️ CI & Validation Requirements

**Mandatory checks:**

| Layer         | Validator / Job                |
|--------------:|--------------------------------|
| Type safety   | TypeScript strict mode         |
| Runtime schema| `schemaGuards.ts` JSON guards  |
| Governance    | `faircare-validate.yml`        |
| Accessibility | `accessibility_scan.yml` (for consumers) |
| Telemetry     | `telemetry-export.yml`         |
| Security      | CodeQL + Trivy                 |
| Docs          | `docs-lint.yml`                |

The model must **never** regress schema stability or governance semantics without corresponding schema + UI + telemetry updates.

---

## 🧾 Metadata Record (Example)

~~~json
{
  "id": "entity_diff_model_v11.2.2",
  "normalized_models_generated": 31240,
  "governance_deltas_detected": 2310,
  "explainability_drift_cases": 79,
  "checksum_verified": true,
  "telemetry_linked": true,
  "timestamp": "2025-11-30T22:50:00Z"
}
~~~

This example shows a summarized, release-level statistics record (not a runtime EntityDiff).

---

## 🕰 Version History

| Version | Date       | Summary                                                                                                                         |
|--------:|------------|---------------------------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-30 | Upgraded to v11.2.2; added telemetry v2, FAIR+CARE v11 semantics, energy/carbon tracking, and stricter governance diff handling. |
| v10.3.2 | 2025-11-14 | Deep-architecture rebuild: governance diff system, explainability deltas, provenance continuity, a11y metadata, sustainability telemetry. |

---

## ⚖️ Footer

<div align="center">

**Kansas Frontier Matrix — Diff-First Entity Model Architecture**  
🧬 Deterministic Semantics · 🔐 FAIR+CARE Governance · 🔗 Provenance Fidelity · 🧠 Explainable AI  

[Back to Diff-First](../README.md) •  
[Docs Root](../../../../README.md) •  
[Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

© 2025 Kansas Frontier Matrix — MIT License  

**End of Document**

</div>