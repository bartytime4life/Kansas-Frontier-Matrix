---
title: "🗃️ Kansas Frontier Matrix — DataCards Component Suite Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/components/DataCards/README.md"
version: "v11.2.2"
last_updated: "2025-12-15"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council Oversight"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.2/web-datacards-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/web-components-datacards-v2.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT / CC-BY 4.0"
classification: "Public / Dataset-Sensitive"
jurisdiction: "United States / Kansas"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

status: "Active / Enforced"
doc_kind: "Component Overview"
intent: "frontend-datacards"
semantic_intent:
  - "UI-component"
  - "dataset-metadata"
  - "governance-ui"
  - "provenance-ui"

fair_category: "F1-A1-I1-R1"
care_label: "CARE-Aware · Dataset Dependent"
sensitivity: "Variable"
public_exposure_risk: "Medium"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"
risk_category: "Mixed"
redaction_required: true

ttl_policy: "12 months"
sunset_policy: "Superseded upon next DataCards system upgrade"
immutability_status: "version-pinned"

json_schema_ref: "../../../../schemas/json/web-components-datacards-readme-v11.schema.json"
shape_schema_ref: "../../../../schemas/shacl/web-components-datacards-readme-v11-shape.ttl"
doc_uuid: "urn:kfm:doc:web-components-datacards-readme-v11.2.2"
semantic_document_id: "kfm-doc-web-components-datacards-readme-v11"
event_source_id: "ledger:web/src/components/DataCards/README.md"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with guardrails"
ai_transform_permissions:
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "diagram-extraction"
ai_transform_prohibited:
  - "speculative-content"
  - "hallucinated-metadata"
  - "unverified-claims"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

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

provenance_chain:
  - "web/src/components/DataCards/README.md@v10.4.0"
  - "web/src/components/DataCards/README.md@v10.3.2"
---

<div align="center">

# 🗃️ **Kansas Frontier Matrix — DataCards Component Suite Overview (v11.2.2)**
`web/src/components/DataCards/README.md`

**Purpose**  
The **DataCards Suite** provides FAIR+CARE-governed, metadata-rich, provenance-linked UI components used throughout the Kansas Frontier Matrix (KFM) Web Client.
DataCards render spatial/temporal previews, dataset classifications, licenses, CARE badges, and provenance details in a consistent, accessible, deterministic format — while enforcing masking/redaction rules for dataset-sensitive content.

<img src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Enforced-gold" />
<img src="https://img.shields.io/badge/A11y-WCAG_2.1_AA%2B-brightgreen" />
<img src="https://img.shields.io/badge/SLSA-Level_3-orange" />

</div>

---

## 📘 Overview

DataCards are a **governed metadata UI framework** used for:

- STAC/DCAT dataset browsing and search results
- Story Node asset previews (dataset and evidence attachments)
- Focus Mode contextual dataset lists and “supporting evidence” trails
- Map-adjacent dataset listings and layer browsers
- Provenance and governance details (license, rights-holder, CARE label, sovereignty notices)

**Core principles**

- **Deterministic rendering:** schema-driven display; no inferred/hallucinated fields
- **Governance-first:** CARE and sovereignty rules are enforced, never “optional”
- **Redaction-aware:** if metadata is incomplete or restricted, DataCards show safe placeholders and explanations
- **Accessibility:** WCAG 2.1 AA+ semantics for structure, focus order, and non-visual equivalents
- **Telemetry:** interactions emit non-PII, governance-safe events tied to component version

**Non-goals**

- DataCards do not fetch data (no API calls)
- DataCards do not compute policy (masking decisions come from upstream governance layers)
- DataCards do not “improve” metadata (no guessing, no enrichment inference)

---

## 🗂️ Directory Layout

KFM-MDP requires the directory tree to be box-safe, one-branch, and tildes-fenced.

~~~text
📁 web/src/components/DataCards/
├── 📄 README.md                     — This document (governed component overview)
├── 📄 DataCard.tsx                  — 🗃️ Universal governed dataset/narrative card container
├── 📄 DataCardHeader.tsx            — 🏷️ Title, dataset-type label, CARE badge, provenance chip
├── 📄 DataCardMetadata.tsx          — 🧾 Key fields: publisher, license, time, space, rights
├── 📄 DataCardPreview.tsx           — 🗺️ Spatial/temporal preview with masking/generalization
├── 📄 DataCardFooter.tsx            — 🦶 Actions: open/explore/provenance (policy-aware)
├── 📄 DataCardA11yHelpers.tsx       — ♿ ARIA scaffolding, focus order, SR-only helpers
└── 📄 DataCardSkeleton.tsx          — 🧱 Non-sensitive loading state (no leaked metadata)
~~~

**Optional adjacency pattern (if/when added)**  
If the suite expands, keep additions co-located and explicit (e.g., `types.ts`, `index.ts`, `*.test.tsx`, `*.stories.tsx`) and update this layout immediately.

---

## 🧭 Context

DataCards sit in the **presentation layer** and should receive:

- already-resolved dataset/story metadata (STAC/DCAT/Graph-derived)
- already-computed governance overlays (CARE label, sovereignty flags, redaction directives)
- already-normalized extents (temporal/spatial), with masking/generalization applied upstream

DataCards return:

- accessible, deterministic UI
- user actions via callbacks (e.g., `onOpen`, `onViewProvenance`, `onAddToMap`)
- telemetry events (non-PII, schema-valid)

**Boundary rule:** DataCards must never “undo” upstream generalization by recomputing precise geometry from bboxes, centroids, IDs, or map state.

---

## 🗺️ Diagrams

### DataCards data flow

~~~mermaid
flowchart LR
  A["STAC/DCAT/Graph Sources"] --> B["Upstream Normalizers + Governance Filters"]
  B --> C["DataCards Props: DisplayModel + Governance"]
  C --> D["Header / Metadata / Preview / Footer"]
  D --> E["User Interactions"]
  E --> F["Telemetry Events (non-PII)"]
~~~


### Component composition

~~~mermaid
flowchart TB
  Card[DataCard.tsx] --> Head[DataCardHeader.tsx]
  Card --> Meta[DataCardMetadata.tsx]
  Card --> Prev[DataCardPreview.tsx]
  Card --> Foot[DataCardFooter.tsx]
  Card --> A11y[DataCardA11yHelpers.tsx]
  Card --> Skel[DataCardSkeleton.tsx]
~~~

---

## 🧠 Story Node & Focus Mode Integration

### Focus Mode v3 usage

DataCards are commonly used to display:

- supporting datasets relevant to a focal entity
- evidence trails that justify a Focus narrative block
- related distributions/assets (when allowed by governance)

**Requirements for Focus Mode contexts**

- When the Focus context is sovereign-controlled, DataCards must:
  - show sovereignty notice components in the header region
  - suppress preview surfaces that could imply precision
  - route users to provenance/governance details rather than “open raw”

### Story Node v3 usage

DataCards may appear inside Story Node UI as:

- “Referenced Datasets”
- “Supporting Evidence”
- “Assets / Distributions”

**Story Node rule:** DataCards must not add narrative interpretation. They only display metadata and provenance already attached to the Story Node or dataset record.

---

## 🧪 Validation & CI/CD

DataCards are dataset-sensitive and must pass stricter validation gates:

- Markdown lint + schema lint for this README
- Component tests (unit + integration)
- A11y checks (structure, focus order, reduced-motion compliance)
- Governance tests (masking, redaction-required flows, sovereignty notices)
- Telemetry schema validation for emitted events

**Expected test locations**

~~~text
📁 tests/unit/web/components/DataCards/
📁 tests/integration/web/components/DataCards/
~~~

**CI blocking conditions (non-exhaustive)**

- A restricted/sovereign dataset renders a preview surface that implies precision
- License / CARE label / rights-holder is present upstream but not rendered
- A11y regressions for keyboard flow or missing textual equivalents
- Telemetry includes raw IDs or other sensitive fields instead of hashed/abstract identifiers

---

## 📦 Data & Metadata

### Display model inputs

DataCards should be fed by a “display model” produced upstream (hooks/services/pipelines). A common pattern is a single object that contains:

- stable display fields (title, summary, publisher)
- governance block (CARE label, redaction directives)
- normalized extents (temporal, spatial) that are already safe to show

Example (illustrative) shape:

~~~ts
type CareLabel =
  | "CARE-P"
  | "CARE-Aware"
  | "Public"
  | "Restricted"
  | "Sovereign-Controlled";

interface DataCardGovernance {
  careLabel: CareLabel;
  redactionRequired: boolean;
  indigenousRightsFlag?: boolean;
  sovereigntyNotice?: string; // UI-safe text, not a policy computation
  license?: string;           // SPDX or CC identifier when available
  rightsHolder?: string;
}

interface DataCardExtent {
  temporal?: { start?: string; end?: string; precision?: "day" | "month" | "year" | "range" };
  spatial?: { bbox?: [number, number, number, number]; generalized?: boolean; method?: "H3" | "bbox" | "none" };
}

interface DataCardDisplayModel {
  idHash: string;             // never raw dataset IDs in UI events/URLs unless policy allows
  title: string;
  subtitle?: string;
  publisher?: string;
  description?: string;
  extent?: DataCardExtent;
  governance: DataCardGovernance;
  provenance?: { summary?: string; link?: string };
}
~~~

### Redaction behavior

- If `redactionRequired === true`, DataCards must:
  - hide or generalize preview surfaces
  - replace sensitive fields with safe placeholders
  - provide an explanation (tooltips/inline text) referencing governance context
- If license/rights data is missing, DataCards must show “Unknown / Not provided” rather than guessing.

### Telemetry event guidance

Event names are stable and suite-scoped:

- `datacard:open`
- `datacard:hover`
- `datacard:action`
- `datacard:care-warning`
- `datacard:provenance-expand`

**Telemetry content rules**

- never include raw dataset identifiers if they are not explicitly public-safe
- prefer hashed IDs (already in the display model)
- include the minimum governance context needed for analysis (e.g., care label bucket)

Illustrative event payload:

~~~json
{
  "event": "datacard:open",
  "component": "DataCards",
  "version": "v11.2.2",
  "id_hash": "sha256:…",
  "care_label": "CARE-Aware",
  "redaction_required": true,
  "interaction": { "source": "FocusMode", "action": "open" }
}
~~~

---

## 🌐 STAC, DCAT & PROV Alignment

DataCards must remain interoperable with KFM’s public-facing metadata standards:

### STAC alignment (KFM-STAC v11)

Commonly displayed (when present and allowed):

- `id`, `collection`
- `assets` (summarized, not exhaustive dumping)
- `license`
- `bbox` / `geometry` (only if already generalized)
- `datetime` or `start_datetime`/`end_datetime`

### DCAT alignment (KFM-DCAT v11)

Commonly displayed (when present and allowed):

- dataset title and publisher
- license and access rights
- distributions (safe-to-list; action gating may be required)
- temporal and spatial coverage summaries

### PROV alignment (KFM-PROV v11 / PROV-O)

DataCards should provide at least one “provenance affordance”:

- short provenance summary (“Source: … / Derived from: …”)
- expandable provenance trail
- link to dataset record provenance or manifest entry

**Rule:** provenance UI must reflect what is supplied. If provenance is absent, do not invent a chain.

---

## 🧱 Architecture

### DataCard.tsx

The suite orchestrator. Responsibilities:

- composes header/metadata/preview/footer
- applies redaction directives (hide/disable components as needed)
- ensures semantic HTML structure (`<article>` wrapper)
- triggers telemetry events (suite-scoped)

### DataCardHeader.tsx

- renders title + optional type label
- always displays CARE badge / classification when provided
- includes provenance chip affordance (expand/open)

### DataCardMetadata.tsx

- renders key fields (publisher, license, rights-holder, temporal coverage, spatial coverage)
- enforces masking/generalization (never implies precision)
- uses “explicit unknown” placeholders for missing fields

### DataCardPreview.tsx

- renders spatial/temporal preview only when allowed
- requires text equivalents (SR text, captions)
- if generalized: must label as generalized (method + no-precision notice)

### DataCardFooter.tsx

- presents actions, all policy-aware:
  - open details
  - open in map (if allowed)
  - view provenance (always safe)
- restricted datasets: disable actions with explanation (not silent)

### DataCardA11yHelpers.tsx

- provides shared ARIA scaffolding and screen-reader summaries
- centralizes focus order management for composite card layouts
- enforces reduced-motion alternatives for any animated placeholders

### DataCardSkeleton.tsx

- renders safe loading state
- must never reveal sensitive strings while loading
- must respect reduced motion preference

---

## ⚖ FAIR+CARE & Governance

DataCards operate under dataset-sensitive governance constraints.

**Non-negotiables**

- Display CARE and sovereignty indicators when provided
- Never show precise coordinates for restricted datasets
- Never display or emit sensitive identifiers in telemetry
- Never “upgrade” or “sharpen” uncertain coverage (temporal or spatial)
- Never replace missing metadata with inferred values

**Sovereignty-aware behavior (indigenous_rights_flag: true)**

- If sovereign-control indicators are present, DataCards must:
  - elevate notices to header-level prominence
  - default to safer displays (generalized extents, disabled preview)
  - route users to rights/provenance rather than raw export actions

**Redaction-required mode**

When `redaction_required: true` at the doc level, this suite must maintain conservative defaults:

- previews are opt-in and policy-gated
- metadata fields must be whitelisted by governance layer
- user-facing explanations are required when data is hidden

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-12-15 | KFM-MDP v11.2.6 compliance refresh: standardized headings, fencing, and directory layout; corrected relative refs; expanded STAC/DCAT/PROV + telemetry guidance; clarified redaction and sovereignty behavior. |
| v11.2.2 | 2025-11-30 | Full v11 upgrade: governance, metadata, A11y, telemetry, masking. |
| v10.4.0 | 2025-11-15 | Previous major update (pre-v11 standards). |
| v10.3.2 | 2025-11-14 | CARE disclosure refinements. |
| v10.3.1 | 2025-11-13 | Initial DataCards overview. |

---

<div align="center">

**📚 Governance Links**  
[Docs Root](../../../../README.md) ·
[Standards Index](../../../../docs/standards/INDEX.md) ·
[Governance Charter](../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[FAIR+CARE Guide](../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[Sovereignty Policy](../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

**🔐 Compliance**  
FAIR+CARE · CIDOC-CRM · OWL-Time · GeoSPARQL · STAC/DCAT · PROV-O · SLSA Level 3

**♻️ Sustainability**  
Energy & Carbon Telemetry Enabled (ISO 50001 / ISO 14064)

© 2025 Kansas Frontier Matrix — MIT / CC-BY 4.0 · Public / Dataset-Sensitive · Version-Pinned

</div>
