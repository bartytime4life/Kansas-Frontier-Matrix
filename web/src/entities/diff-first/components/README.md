---
title: "🧩 Kansas Frontier Matrix — Diff-First Entity Components Architecture (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/entities/diff-first/components/README.md"
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
telemetry_ref: "../../../../../releases/v11.2.2/web-entity-diff-components-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/web-entity-diff-components-v2.json"
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
doc_kind: "Component Overview"
intent: "web-entity-diff-components"
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
  - "web/src/entities/diff-first/components/README.md@v10.3.2"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "WebPageElement"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"

json_schema_ref: "../../../../../schemas/json/web-entity-diff-components-readme-v11.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/web-entity-diff-components-readme-v11-shape.ttl"
doc_uuid: "urn:kfm:doc:web-entity-diff-components-readme-v11.2.2"
semantic_document_id: "kfm-doc-web-entity-diff-components-readme-v11"
event_source_id: "ledger:web/src/entities/diff-first/components/README.md"
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
classification: "Public Components (diff-UI · governance-sensitive)"

ttl_policy: "Review each major release"
sunset_policy: "Superseded upon Diff-First Entity Components v12 refactor"
---

<div align="center">

# 🧩 **Kansas Frontier Matrix — Diff-First Entity Components Architecture**  
`web/src/entities/diff-first/components/README.md`

**Purpose:**  
Define the **Diamond⁹ Ω–grade UI component architecture** for the Diff-First Entity subsystem in KFM v11.2.2.  
These components present **release-to-release diffs** (properties, relations, text, governance, explainability) in a  
**FAIR+CARE-certified**, **accessible**, and **sustainability-aware** interface, tightly integrated with **Focus Mode v3**,  
**MapView**, **TimelineView**, and **Governance UIs**.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)]()  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-UI_Compliant-orange)]()  
[![Status](https://img.shields.io/badge/Status-Stable-success)]()  
[![License: MIT](https://img.shields.io/badge/License-MIT-green)]()

</div>

---

## 📘 Overview

The **Diff-First Entity Components** are responsible for:

- Rendering **diff summaries** across releases (`R_prev → R_curr`)  
- Displaying **property, relation, and text changes** with clear severity encodings  
- Surfacing **governance & CARE deltas** (consent, license, sovereignty, restrictions)  
- Exposing **explainability deltas** from Focus Mode v3  
- Maintaining **WCAG 2.1 AA+** visual and interaction standards  
- Emitting **telemetry events** for performance, energy, and ethical usage  
- Integrating with Diff-First features such as **ReleasePicker**, **Legend**, and governance-specific drawers  

They consume **EntityDiff models** from `web/src/features/entities/diff-first` and render them as  
**interpretable, ethical, and accessible UX**.

---

## 🗂️ Directory Layout

~~~text
web/src/entities/diff-first/components/
│
├── 📘 README.md
├── 🧾 DiffHeader.tsx        # Summary bar & severity overview
├── 🔡 PropertyDelta.tsx     # Scalar & categorical property changes
├── 🔗 RelationDelta.tsx     # Graph relation changes
├── 📝 TextDelta.tsx         # Textual change visualization
├── 🕰️ ReleasePicker.tsx     # Release navigation UI
└── 🎨 Legend.tsx            # Diff symbology & semantic tokens
~~~

---

## 🧩 High-Level Component Architecture

*(In repo, use ```mermaid```; here we use `~~~mermaid` to keep this single-fence block intact.)*

~~~mermaid
flowchart TD
    DIFF[EntityDiff model] --> HEAD[DiffHeader]
    DIFF --> PROP[PropertyDelta]
    DIFF --> REL[RelationDelta]
    DIFF --> TXT[TextDelta]
    TAGS[Release tags] --> RP[ReleasePicker]
    TOK[Design tokens] --> LEG[Legend]
    HEAD --> LEG
    PROP --> LEG
    REL --> LEG
    TXT --> LEG
~~~

---

## 🧱 DiffHeader.tsx — Summary Bar & Severity Overview

**Responsibilities**

- Display top-level diff summary:
  - total counts (`added`, `removed`, `changed`)  
  - overall severity (`low` | `med` | `high`)  
- Foreground governance-impacting changes:
  - CARE label changes  
  - license / consent transitions  
  - sovereignty or jurisdiction changes  
- Provide a **quick-glance** understanding of entity evolution between releases  

**Props**

~~~ts
type DiffHeaderProps = {
  summary: DiffSummary;
  governance: GovernanceChange;
};
~~~

Flow:

~~~mermaid
flowchart LR
    SUM[DiffSummary] --> HEAD[DiffHeader]
    GOV[GovernanceChange] --> HEAD
~~~

---

## 🔡 PropertyDelta.tsx — Scalar & Categorical Changes

**Responsibilities**

- Render numeric deltas with:
  - units (e.g., km², gCO₂e, persons)  
  - percent changes  
  - severity (low/med/high)  
- Render categorical changes:
  - enum swaps, label transitions, classification changes  

**UI Rules**

- Severity and meaning must be expressed via **shape + icon + text**, NOT color alone.  
- Tooltips and/or SR text MUST describe the change in plain language.

**Props**

~~~ts
type PropertyDeltaProps = {
  properties: PropertyChange[];
};
~~~

Flow:

~~~mermaid
flowchart LR
    PC[PropertyChange list] --> PUI[PropertyDelta]
~~~

---

## 🔗 RelationDelta.tsx — Graph Relation Changes

**Responsibilities**

- Show graph relation changes, including:
  - added relations (new links)  
  - removed relations (dropped links)  
  - relation types (e.g., `LOCATED_IN`, `PARTICIPATED_IN`)  
  - confidence scores / flags  
  - minimal provenance references  

**Governance**

- CARE/sovereignty masking rules may:
  - hide or anonymize certain relation targets  
  - group sensitive relations into generalized buckets  

**Props**

~~~ts
type RelationDeltaProps = {
  relations: RelationChange[];
};
~~~

Flow:

~~~mermaid
flowchart LR
    RC[RelationChange list] --> RUI[RelationDelta]
~~~

---

## 📝 TextDelta.tsx — Textual Change Visualization

**Responsibilities**

- Render unified or split text diffs for:
  - descriptions  
  - narrative summaries  
  - label/label-description pairs  
- Use outlines/underline/weight to indicate changes (not color-only).  
- Provide scroll-safe, wrap-safe views for long text.

**Props**

~~~ts
type TextDeltaProps = {
  textChanges: TextChange[];
};
~~~

Flow:

~~~mermaid
flowchart LR
    TC[TextChange list] --> TUI[TextDelta]
~~~

**A11y**

- Screen readers must be able to access both “before” and “after” forms.  
- Provide textual summaries of changes where possible (e.g., “4 words removed, 7 words added”).

---

## 🕰️ ReleasePicker.tsx — Release Navigation UI

**Responsibilities**

- Allow users to:
  - select previous and current releases (R_prev, R_curr)  
  - navigate across all available tags for an entity  
- Provide keyboard-first navigation and accessible labeling.

**Props**

~~~ts
type ReleasePickerProps = {
  tags: string[];                  // available release tags
  selectedPrev: string;            // current previous tag
  selectedCurr: string;            // current current tag
  onChange(prev: string, curr: string): void;
};
~~~

Flow:

~~~mermaid
flowchart TD
    TAGS2[Release tags] --> RP[ReleasePicker]
    RP --> EVT[Release change event]
~~~

**Governance**

- Release metadata must be sourced from a provenance-aware ledger; ReleasePicker is responsible only for UI.

---

## 🎨 Legend.tsx — Symbology & Semantic Tokens

**Responsibilities**

- Explain the meaning of:
  - severity encodings  
  - CARE icons and governance markers  
  - explainability indicators  
  - predictive vs historical diff markers  
- Show mapping from:
  - shapes/colors/icons → semantics (‘added’, ‘removed’, ‘changed’, ‘governance change’)  

**Props**

~~~ts
type LegendProps = {
  tokens: DiffLegendTokens;
};
~~~

Flow:

~~~mermaid
flowchart LR
    TOK2[Design tokens] --> LEG[Legend]
~~~

**A11y**

- Provide text labels for each legend entry.  
- Ensure each symbol has a corresponding SR description.

---

## ♿ Accessibility & Interaction

All components MUST:

- Provide **ARIA labels** and appropriate roles (`region`, `button`, `list`, etc.)  
- Support full keyboard navigation and tab order:
  - header → summary → property deltas → relation deltas → text deltas → legend → release picker  
- Describe severity and CARE flags with **text** and **shapes**, not solely color.  
- Preserve heading hierarchy consistent with parent views.  

Conceptual A11y flow:

~~~mermaid
flowchart TD
    EVM[EntityDiff model] --> A11Y[a11y prop builder]
    A11Y --> UI[Accessible diff components]
~~~

---

## 📡 Telemetry Integration

Components must support telemetry by calling callback props or hooks that emit events into:

~~~text
../../../../../releases/v11.2.2/web-entity-diff-components-telemetry.json
~~~

Tracked events:

- `diff_header:view`  
- `diff_property:expand`  
- `diff_relation:expand`  
- `diff_text:expand`  
- `diff_release:change`  
- `diff_legend:hover`  

Telemetry payloads SHOULD include:

- `entityId`  
- `releasePrev` / `releaseCurr`  
- `careImpact` (e.g., number of governance changes in view)  
- `latencyMs` (where available)  

All telemetry MUST remain non-PII and schema-valid.

---

## 🔐 Governance & FAIR+CARE Responsibilities

At the component layer, governance requires:

- Clear labeling of CARE-impacted changes (e.g., badges or icons + text on DiffHeader)  
- Layout that foregrounds governance changes in DiffHeader and relevant sections  
- No display of restricted details without gating or masking (for example, hiding sensitive relation targets)  
- Visual alerts for license/consent/sovereignty changes (Legend + header)  

A separate governance audit log can be written to:

~~~text
../../../../../docs/reports/audit/web-entity-diff-components-governance.json
~~~

Any UI component that misrepresents or hides governance changes MUST be treated as a CI-blocking defect.

---

## 🧪 CI & Validation Requirements

**Component validation must cover:**

| Layer        | Check / Job                         |
|-------------:|-------------------------------------|
| A11y         | `accessibility_scan.yml` (axe + Lighthouse) |
| Governance   | `faircare-validate.yml`             |
| Telemetry    | `telemetry-export.yml`              |
| Types        | TypeScript strict mode              |
| Security     | CodeQL + Trivy                      |
| Docs         | `docs-lint.yml`                     |

Before merging, any modifications to these components MUST pass:

- Unit tests  
- Integration tests with the Diff-First module  
- A11y and governance checks  

---

## 🧾 Example Component Metadata Record

~~~json
{
  "id": "entity_diff_components_v11.2.2",
  "components": [
    "DiffHeader",
    "PropertyDelta",
    "RelationDelta",
    "TextDelta",
    "ReleasePicker",
    "Legend"
  ],
  "a11y_score": 99.2,
  "fair_status": "certified",
  "care_flags_visible": true,
  "telemetry_synced": true,
  "checksum_verified": true,
  "timestamp": "2025-11-30T23:15:00Z"
}
~~~

This is an example **meta-report** for the component suite, not a runtime artifact.

---

## 🕰 Version History

| Version | Date       | Summary                                                                                                                                                    |
|--------:|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-30 | Upgraded to KFM-MDP v11.2.2; telemetry v2, FAIR+CARE v11 alignment, A11y clarifications, and improved governance highlight in DiffHeader/Legend.          |
| v10.3.2 | 2025-11-14 | Deep-architecture rewrite: integrated governance badges, explainability visuals, WCAG-compliant diff renderings, and telemetry-aware interactions.        |

---

## ⚖️ Footer

<div align="center">

**Kansas Frontier Matrix — Diff-First Entity Components Architecture**  
🧩 Change Transparency · 🔐 FAIR+CARE UI · 🔗 Provenance Surfacing · 🧠 Explainable UX  

[Back to Diff-First Module](../README.md) •  
[Docs Root](../../../../README.md) •  
[Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

© 2025 Kansas Frontier Matrix — MIT License  

**End of Document**

</div>