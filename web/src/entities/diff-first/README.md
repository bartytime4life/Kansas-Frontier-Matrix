---
title: "🧾 Kansas Frontier Matrix — Diff-First Entity Detail Architecture (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/features/entities/diff-first/README.md"
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
telemetry_ref: "../../../../../releases/v11.2.2/web-entity-diff-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/web-entity-diff-v3.json"
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
doc_kind: "Feature Architecture Overview"
intent: "web-features-entities-diff-first"
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
  - "web/src/features/entities/diff-first/README.md@v10.3.2"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "SoftwareSourceCode"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"

json_schema_ref: "../../../../../schemas/json/web-features-entities-diff-first-readme-v11.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/web-features-entities-diff-first-readme-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:web-features-entities-diff-first-readme-v11.2.2"
semantic_document_id: "kfm-doc-web-features-entities-diff-first-readme-v11"
event_source_id: "ledger:web/src/features/entities/diff-first/README.md"
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
classification: "Public (diff & governance engine; content-sensitive)"

ttl_policy: "Review each major release"
sunset_policy: "Superseded upon next Diff-First module overhaul"

heading_registry:
  approved_h2:
    - "📘 Deep Overview"
    - "🗂️ Directory Layout"
    - "🧭 High-Level Architecture"
    - "🧬 Canonical Diff Model"
    - "🧩 Diff Types Architecture"
    - "🧠 Explainability Deltas & Focus Mode Integration"
    - "🧭 Release Picker Architecture"
    - "🧱 Normalization Pipeline"
    - "📡 Telemetry & Sustainability"
    - "🔐 Governance & CARE Enforcement"
    - "♿ Accessibility Architecture (WCAG 2.1 AA)"
    - "🧪 CI & Validation Requirements"
    - "🧾 Example Metadata Record"
    - "🕰 Version History"
    - "⚖️ Footer"
---

<div align="center">

# 🧾 **Kansas Frontier Matrix — Diff-First Entity Detail Architecture**  
`web/src/features/entities/diff-first/README.md`

**Purpose:**  
Define the **deep-architecture specification** of the Diff-First Entity Detail Module — the KFM v11.2.2 subsystem that compares  
**release-to-release entity states**, surfaces **governance changes**, exposes **lineage evidence**, and synchronizes with **Map**,  
**Timeline**, **Focus Mode v3**, and **Story Node** systems.  
This module enforces **FAIR+CARE**, **provenance integrity**, **WCAG 2.1 AA+**, and **MCP-DL v6.3** reproducibility.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)]()  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Diff_Integrity-orange)]()  
[![Status](https://img.shields.io/badge/Status-Stable-success)]()  
[![License](https://img.shields.io/badge/License-MIT-green)]()

</div>

---

## 📘 Deep Overview

Most systems show entity details as **static snapshots**.  
**KFM Diff-First** shows **history before state**, answering:

- *What changed?*  
- *Why did it change?*  
- *What is the evidence?*  
- *What is the governance/CARE impact?*  
- *What is the lineage from previous releases?*

The Diff-First module surfaces:

### 🔍 Structural Differences

- Added / removed relationships  
- New or removed datasets  
- Geometry changes  
- Temporal refinements  
- CARE label shifts  

### 🧩 Property Differences

- Numeric deltas (with units and % changes)  
- Text diffs (unified & split)  
- Enum / categorical changes  
- Severity classifications (low / med / high)  

### 🔐 Governance & Provenance Changes

- Consent modifications  
- License changes  
- Provenance lineage updates  
- STAC/DCAT metadata updates  
- CARE label changes + sovereignty warnings  

### 🧠 Explainability & Focus Mode Integration

- Evidence deltas (added/removed evidence nodes)  
- `relevanceScore` changes  
- Degraded or improved explainability reliability  

All of the above must be rendered in a **non-speculative, provenance-backed** manner.

---

## 🗂️ Directory Layout

~~~text
web/src/features/entities/diff-first/
│
├── 📘 README.md
│
├── 🧩 components/
│   ├── 🧾 DiffHeader.tsx         # Summary banner for entity diff (what changed, severity)
│   ├── 𝛥 PropertyDelta.tsx       # Renders single property change (scalar/categorical)
│   ├── 🔗 RelationDelta.tsx      # Renders relationship-level changes
│   ├── ✍️ TextDelta.tsx          # Text diff renderer with A11y support
│   ├── 🕰️ ReleasePicker.tsx      # Release range picker (prev/curr)
│   └── 🎨 Legend.tsx             # Legend for diff symbols, severity, governance
│
├── 🪝 hooks/
│   ├── 🔍 useEntityDiff.ts       # Hook for fetching + normalizing diff model
│   └── 🏷️ useReleaseTags.ts     # Hook for retrieving available releases/tags
│
├── 🧬 model/
│   ├── 📑 diffTypes.ts           # Types for EntityDiff, PropertyChange, etc.
│   └── 📐 normalize.ts           # Normalization + schema guard logic
│
├── 🌐 services/
│   └── 📡 diffClient.ts          # API client for diff endpoint(s)
│
├── 🎨 styles/
│   └── 🎯 tokens.css             # Visual tokens for diff colors, severity, etc.
│
└── 🧪 tests/
    └── ✅ diff-first.spec.tsx    # Core integration + unit tests for diff UI
~~~

---

## 🧭 High-Level Architecture

*(Rendered here as text-friendly mermaid; in-repo you can switch to a native ```mermaid``` block.)*

~~~mermaid
flowchart TD
    REL["Release Metadata<br/>R_prev · R_curr"] --> API["diffClient"]
    API --> NORM["normalize<br/>schema guards + governance coercion"]
    NORM --> DIFF["EntityDiff Model<br/>canonical, governed"]
    DIFF --> UI["Diff Components<br/>header · properties · relations · text"]
    UI --> GOV["Governance Engine<br/>CARE · consent · lineage"]
    GOV --> TEL["Telemetry Export<br/>energy · ethics · provenance"]
~~~

---

## 🧬 Canonical Diff Model

### Base Model — `EntityDiff`

Represents the full diff for a single entity across two releases:

~~~ts
type EntityDiff = {
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

### Summary

~~~ts
type DiffSummary = {
  added: number;     // count of new properties/relations/text blocks
  removed: number;   // count of removed elements
  changed: number;   // count of modified items
  severity: "low" | "med" | "high";
};
~~~

---

## 🧩 Diff Types Architecture

~~~mermaid
flowchart TD
    P["PropertyChange"] --> NUM["ScalarChange"]
    P --> CAT["CategoricalChange"]
    P --> TXT["TextualChange"]
    R["RelationChange"] --> ADD["Added"]
    R --> REM["Removed"]
~~~

### `PropertyChange` (Scalar)

Numeric deltas with units, percentage changes, and severity:

- `prevValue` / `currValue`  
- `delta`  
- `percentChange`  
- `unit` (e.g., km², persons, gCO₂e)  
- `severity`  

### `PropertyChange` (Categorical)

Enum/label changes:

- `prevLabel` / `currLabel`  
- Differences flagged as benign/important/critical via `severity`  

### `TextChange`

Represents text diffs for narrative/description fields:

- Unified/split diff representation  
- Token-level changes counted  
- A11y-friendly representation (highlighted terms with SR equivalents)

### `RelationChange`

Graph edge additions/removals, including:

- referenced entity ID and type  
- relationship type (e.g., “located_in”, “participated_in”)  
- direction (if relevant)  
- provenance to show why relation exists/changed  
- sovereignty or CARE dependence (e.g., relation only visible if CARE permits)

---

## 🧠 Explainability Deltas & Focus Mode Integration

Focus Mode v3 returns:

- `relevanceScore`  
- evidence node IDs (Story Nodes, datasets, places, people)  
- dataset lineage references  
- CARE and governance warnings  

The Diff-First module compares:

- **explanation loss** (e.g., fewer evidence sources, lower relevance score)  
- **new evidence** (e.g., new Story Node or dataset used)  
- **removed evidence**  
- **reasoning drift** (e.g., shift in types of evidence used)

High-level flow:

~~~mermaid
flowchart LR
    XAI_prev["R_prev Explainability"] --> CMP["Explainability Comparator"]
    XAI_curr["R_curr Explainability"] --> CMP
    CMP --> XDEL["ExplainabilityDelta<br/>relevance + evidence changes"]
~~~

Explainability deltas MUST be surfaced with clear provenance and NEVER as speculation.

---

## 🧭 Release Picker Architecture

~~~mermaid
flowchart TD
    TAGS["Release Tags List"] --> PICK["ReleasePicker"]
    PICK --> UPDATE["Diff Recompute"]
    UPDATE --> UI["Diff Components"]
~~~

**ReleasePicker.tsx** MUST:

- Support complete history navigation (all releases present in the ledger)  
- Provide keyboard-first release cycling (`[` previous, `]` next in keybinds)  
- Display release metadata (timestamp, tag, ledger ID)  
- Wire to hooks (`useReleaseTags`, `useEntityDiff`) to recompute diffs deterministically  

---

## 🧱 Normalization Pipeline

Ensures all release-to-release comparisons follow:

- Strict schema guards  
- FAIR+CARE coercion for governance fields  
- Provenance retention across transformations  
- Stability across versions (consistent shapes over time)

~~~mermaid
flowchart LR
    RAW["Raw Diff Response"] --> GUARD["Schema Guards<br/>Type + JSON Schema"]
    GUARD --> COERCE["Governance Coercion<br/>CARE/Sovereignty application"]
    COERCE --> READY["UI-Ready Diff Model<br/>EntityDiff"]
~~~

If schema or governance coercion fails, the pipeline MUST raise an explicit error (not silently degrade).

---

## 📡 Telemetry & Sustainability

Telemetry events include, at minimum:

- `entity_diff:view`               — user opens a diff view  
- `entity_diff:expand_property`    — expand a property delta  
- `entity_diff:expand_relation`    — expand a relation delta  
- `entity_diff:copy`               — copy diff snippet (for research/audit)  
- `entity_diff:governance_change`  — governance section expanded or interacted with  

Telemetry is written into release bundles, e.g.:

~~~text
../../../../../releases/v11.2.2/web-entity-diff-telemetry.json
~~~

Telemetry payloads SHOULD include:

- latency for diff computation  
- counts of governance changes (CARE label changes, sovereignty shifts, license changes)  
- A11y path coverage (whether user navigated via keyboard, presence of SR features)  
- aggregated energy/carbon metrics (from pipeline-level metrics, NOT guessed in UI)  

All telemetry MUST be non-PII and schema-valid.

---

## 🔐 Governance & CARE Enforcement

Governance-related diffs are **first-class** outputs.

The module MUST:

- Highlight changes in:
  - CARE labels  
  - consent flags  
  - sovereignty domains  
  - licenses  
  - dataset lineage (e.g., new upstream dataset or removal of a trusted source)  

Governance comparator flow:

~~~mermaid
flowchart TD
    META["Governance Metadata<br/>prev · curr"] --> COMP["Governance Comparator"]
    COMP --> OUT["GovernanceChange<br/>CARE · license · consent · sovereignty"]
~~~

**Governance impact MUST appear prominently** (top of diff UI), not buried behind minor property changes.

Any governance-related regression (e.g., marking a restricted dataset as public) MUST fail CI.

---

## ♿ Accessibility Architecture (WCAG 2.1 AA)

Diff-First UI MUST:

- Label all deltas with icon **and** text (no color-only encodings)  
- Maintain valid, logical heading hierarchy  
- Provide a “skip-to-changes” link for keyboard users  
- Offer keyboard shortcuts (where supported), with clear documentation:
  - `[` = previous release  
  - `]` = next release  
  - `/` = search within diff  
  - `g` = jump to governance section  

Conceptual flow:

~~~mermaid
flowchart TD
    TOK["A11y Tokens"] --> DIFF["Diff Components"]
    DIFF --> TEL_A11Y["A11y Telemetry<br/>(non-PII)"]
~~~

All A11y behaviors MUST be covered by automated and manual tests.

---

## 🧪 CI & Validation Requirements

**Mandatory checks:**

| Category     | Validator / Job                       |
|--------------|---------------------------------------|
| Schema       | TypeScript strict + runtime JSON guards |
| Governance   | `faircare-validate.yml`               |
| Accessibility| axe-core + Lighthouse + custom tests |
| Provenance   | lineage continuity checks in pipeline |
| Telemetry    | `telemetry-export.yml` (event schema) |
| Security     | CodeQL + Trivy                        |
| Documentation| `docs-lint.yml`                       |

No diff feature may ship if:

- Governance comparators fail or produce inconsistent results  
- A11y tests fail or regress  
- Telemetry schemas drift without coordinated schema updates  

---

## 🧾 Example Metadata Record

~~~json
{
  "id": "entity_diff_first_v11.2.2",
  "total_entities_diffed": 19540,
  "governance_changes": 1042,
  "care_label_changes": 63,
  "avg_diff_compute_ms": 20.4,
  "energy_use_wh": 0.88,
  "telemetry_synced": true,
  "checksum_verified": true,
  "timestamp": "2025-11-30T22:42:00Z"
}
~~~

This represents a **Diff-First feature-level summary** for a release, not a specific entity diff.

---

## 🕰 Version History

| Version | Date       | Summary                                                                                                                                                                    |
|--------:|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-30 | Upgraded to v11.2.2; aligned with KFM-OP v11, FAIR+CARE v11, telemetry v2, energy/carbon tracking, strengthened governance/comparator semantics and A11y keybindings.     |
| v10.3.2 | 2025-11-14 | Deep-architecture rewrite: governance diff engine, explainability deltas, provenance lineage continuity, predictive support, A11y shortcuts.                               |

---

## ⚖️ Footer

<div align="center">

**Kansas Frontier Matrix — Diff-First Entity Architecture**  
🧾 Change Transparency · 🔐 FAIR+CARE Integrity · 🔗 Provenance Fidelity · 🧠 Explainable AI  

[Back to Web Features](../../README.md) •  
[Docs Root](../../../../README.md) •  
[Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

© 2025 Kansas Frontier Matrix — MIT License  

**End of Document**

</div>