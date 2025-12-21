---
title: "🗃️ Kansas Frontier Matrix — DataCards Component Suite Overview"
path: "web/src/components/DataCards/README.md"
version: "v12.0.0"
last_updated: "2025-12-21"
status: "active"
doc_kind: "Component Overview"
license: "MIT / CC-BY-4.0"

markdown_protocol_version: "KFM-MDP v11.2.6"
mcp_version: "MCP-DL v6.3"
ontology_protocol_version: "KFM-ONTO v4.1.0"
pipeline_contract_version: "KFM-PPC v11.0.0"
stac_profile: "KFM-STAC v11.0.0"
dcat_profile: "KFM-DCAT v11.0.0"
prov_profile: "KFM-PROV v11.0.0"

governance_ref: "docs/governance/ROOT_GOVERNANCE.md"
ethics_ref: "docs/governance/ETHICS.md"
sovereignty_policy: "docs/governance/SOVEREIGNTY.md"
fair_category: "FAIR+CARE"
care_label: "CARE-Aware"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:web:components:datacards:readme:v12.0.0"
semantic_document_id: "kfm-web-components-datacards-readme-v12.0.0"
event_source_id: "ledger:web/src/components/DataCards/README.md"
commit_sha: "<latest-commit-hash>"

ai_transform_permissions:
  - "summarize"
  - "structure_extract"
  - "translate"
  - "keyword_index"
ai_transform_prohibited:
  - "generate_policy"
  - "infer_sensitive_locations"

doc_integrity_checksum: "sha256:<calculate-and-fill>"
---

# 🗃️ Kansas Frontier Matrix — DataCards Component Suite Overview

`web/src/components/DataCards/README.md`

The **DataCards** component suite provides FAIR+CARE-aware, provenance-linked UI components used throughout the KFM Web Client to render dataset and evidence metadata in a **deterministic**, **accessible**, and **redaction-safe** way.

DataCards are a **presentation-layer** suite:
- They **render** already-normalized metadata and governance overlays.
- They **never fetch** data (no API calls inside the suite).
- They **never compute** governance policy (masking decisions must be upstream).

---

## 📘 Overview

### Purpose
- Define the **responsibilities, boundaries, and invariants** for the DataCards UI suite.
- Provide a governed reference for:
  - metadata rendering rules (no guessing / no enrichment inference)
  - redaction + sovereignty-safe behavior
  - provenance affordances
  - telemetry constraints (non-PII)

### Scope

| In Scope | Out of Scope |
|---|---|
| DataCards suite structure + component responsibilities | API calls, data fetching, caching |
| Rendering rules for metadata + governance overlays | Computing governance policy / permissions |
| Redaction-safe UI behavior + placeholder rules | Metadata enrichment / inference / “fixups” |
| A11y requirements for composite card UIs | Graph queries, Neo4j access, ontology changes |
| Telemetry emission constraints + event naming | Telemetry pipeline implementation details |

### Audience
- Primary: Web/React engineers building KFM UI surfaces (search, map-adjacent panels, Focus Mode)
- Secondary: Governance reviewers (FAIR+CARE), a11y reviewers, API/schema maintainers

### Definitions
- Link: `docs/glossary.md`
- Terms used in this doc:
  - **Display model**: A UI-safe object produced upstream (API/hooks) containing display-ready fields.
  - **Governance overlay**: Policy outputs attached upstream (CARE label, redaction flags, sovereignty notices).
  - **Redaction-required**: A state where sensitive fields and/or previews must be omitted or generalized.
  - **Provenance affordance**: UI control to view provenance (PROV trail, manifest references, “derived from”).

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| DataCards suite | `web/src/components/DataCards/` | Web UI | Governed UI components; no data fetch |
| This document | `web/src/components/DataCards/README.md` | Web UI | Component suite overview |
| Telemetry schema | `schemas/telemetry/web-components-datacards-v2.json` | Telemetry | Event validation (non-PII) |
| Energy schema | `schemas/telemetry/energy-v2.json` | Telemetry | Optional sustainability telemetry |
| Carbon schema | `schemas/telemetry/carbon-v2.json` | Telemetry | Optional sustainability telemetry |
| Governance docs | `docs/governance/` | Governance | ROOT + ethics + sovereignty |
| Master guide | `docs/MASTER_GUIDE_v12.md` | Program | Canonical pipeline + v12 invariants |
| Prior release SBOM | `releases/v11.2.2/sbom.spdx.json` | Release Eng | Historical reference (if present) |
| Prior release manifest | `releases/v11.2.2/manifest.zip` | Release Eng | Historical reference (if present) |
| Prior DataCards telemetry | `releases/v11.2.2/web-datacards-telemetry.json` | Telemetry | Historical reference (if present) |

### Definition of done

- [ ] Front-matter complete + valid (no extra keys)
- [ ] Directory tree matches repo reality and is tilde-fenced
- [ ] Boundaries are explicit: DataCards render only (no fetch, no policy compute)
- [ ] Redaction + sovereignty behavior is defined and testable
- [ ] Telemetry constraints documented (no raw sensitive IDs; no PII)
- [ ] Validation steps and expected test locations listed
- [ ] Version history updated for this rewrite

---

## 🗂️ Directory Layout

### This document
- `path`: `web/src/components/DataCards/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Raw/work/processed + catalog outputs |
| Documentation | `docs/` | Canonical governed docs |
| Graph | `src/graph/` | Ontology bindings + graph build |
| Pipelines | `src/pipelines/` | ETL + catalog build + transforms |
| Schemas | `schemas/` | JSON schemas + telemetry schemas |
| Frontend | `web/` | React + map UI |
| MCP | `mcp/` | Experiments, model cards, SOPs |

### Expected file tree for this sub-area

~~~text
📁 web/
└── 📁 src/
    └── 📁 components/
        └── 📁 DataCards/
            ├── 📄 README.md                   — This document (suite overview)
            ├── 📄 DataCard.tsx                — Suite orchestrator / container
            ├── 📄 DataCardHeader.tsx          — Title, classification, badges, provenance affordance
            ├── 📄 DataCardMetadata.tsx        — Key metadata fields (publisher/license/time/space/rights)
            ├── 📄 DataCardPreview.tsx         — Redaction-safe preview surface (only if allowed)
            ├── 📄 DataCardFooter.tsx          — Policy-aware actions (open/map/provenance)
            ├── 📄 DataCardA11yHelpers.tsx     — Shared ARIA + focus-order helpers
            └── 📄 DataCardSkeleton.tsx        — Safe loading state (no leaked metadata)
~~~

Optional adjacency pattern (if/when added): `types.ts`, `index.ts`, `*.test.tsx`, `*.stories.tsx`

---

## 🧭 Context

### Background
KFM requires consistent, governed UI rendering for:
- STAC/DCAT dataset browsing and search results
- Map-adjacent layer lists and dataset side panels
- Focus Mode “supporting evidence” and contextual dataset lists
- Story Node attachments (datasets, evidence artifacts, distributions)

### Assumptions
- DataCards receive **UI-safe** props produced upstream:
  - normalized metadata fields
  - governance overlay (CARE label, sovereignty flags, redaction directives)
  - already-generalized spatial/temporal extents (if needed)
- Any “open”, “download”, or “view raw” action is **policy-gated** by upstream decisions and/or parent context.

### Constraints and invariants
- The canonical pipeline ordering is preserved: DataCards sit in **UI**, downstream of APIs.
- DataCards never query Neo4j or catalogs directly: **frontend consumes contracts via APIs**.
- DataCards must never “sharpen” generalized extents (no recomputing precision from bboxes, IDs, or map state).
- Missing metadata must be rendered as **explicit unknown** (never guessed).
- Telemetry must be **non-PII** and must not leak sensitive identifiers.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Where is the canonical “DataCard display model” schema defined (API schema vs UI types)? | Web + API | TBD |
| Which telemetry schema version is current for DataCards (v2 vs newer)? | Telemetry | TBD |
| What is the preferred sovereignty notice component pattern (shared UI component vs DataCards-local)? | Governance + Web | TBD |

### Future extensions
- Support for “analysis products” (AI evidence artifacts) as first-class card types, linked as STAC assets.
- Card variants for distributions (download gates, access rights badges).
- A shared UI library for sovereignty + CARE badges to keep consistent across components.

---

## 🗺️ Diagrams

### Canonical KFM placement

~~~mermaid
flowchart LR
  A[ETL] --> B[STAC/DCAT/PROV Catalogs]
  B --> C[Neo4j Graph]
  C --> D[APIs]
  D --> E[React/Map UI]
  E --> F[Story Nodes]
  F --> G[Focus Mode]
  E --> H[DataCards Suite]
~~~

### DataCards data flow

~~~mermaid
flowchart LR
  API[API contract payload] --> N[Normalizer / UI display model]
  N --> G[Governance overlay already computed]
  G --> P[DataCards props]
  P --> R[Render: Header / Metadata / Preview / Footer]
  R --> U[User actions via callbacks]
  U --> T[Telemetry events (non-PII)]
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

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Display model | TS object / JSON | API response → UI normalizer | Type checks + snapshot tests |
| Governance overlay | TS object / JSON | API/governance layer | Governance tests |
| Action callbacks | Functions | Parent container / router | Unit tests |
| Telemetry context | Minimal object | Telemetry wrapper | Schema validation |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Rendered card | DOM/React | `web/` | A11y + visual regression |
| Telemetry events | JSON | Telemetry pipeline | `schemas/telemetry/...` |
| User intents | Callback invocations | Parent container | Integration tests |

### Display model guidance
DataCards should be driven by a single UI-safe “display model” object produced upstream. If fields are absent, render “Unknown / Not provided” rather than inferring.

Illustrative example shape:

~~~ts
type CareLabel =
  | "Public"
  | "CARE-Aware"
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
  temporal?: {
    start?: string;
    end?: string;
    precision?: "day" | "month" | "year" | "range";
  };
  spatial?: {
    bbox?: [number, number, number, number];
    generalized?: boolean;
    method?: "H3" | "bbox" | "none";
  };
}

interface DataCardDisplayModel {
  idHash: string; // prefer hashed IDs for telemetry + URLs unless explicitly public-safe
  title: string;
  subtitle?: string;
  publisher?: string;
  description?: string;
  extent?: DataCardExtent;
  governance: DataCardGovernance;
  provenance?: { summary?: string; link?: string };
}
~~~

### Sensitivity and redaction
- If `redactionRequired === true`:
  - hide or generalize preview surfaces
  - suppress sensitive fields
  - show safe placeholders + an explanation (“Restricted by governance”)
- Never show precise coordinates for restricted/sovereign datasets.
- Never emit raw dataset identifiers in telemetry unless policy explicitly marks them public-safe.

### Telemetry guidance
- Stable suite-scoped event names (examples):
  - `datacard:open`
  - `datacard:action`
  - `datacard:provenance_expand`
  - `datacard:care_warning`
- Payload must include only minimum fields needed for analysis:
  - component version
  - care label bucket
  - redaction flag
  - hashed identifier

Illustrative payload:

~~~json
{
  "event": "datacard:open",
  "component": "DataCards",
  "version": "v12.0.0",
  "id_hash": "sha256:…",
  "care_label": "CARE-Aware",
  "redaction_required": true,
  "interaction": { "source": "FocusMode", "action": "open" }
}
~~~

---

## 🌐 STAC, DCAT & PROV Alignment

DataCards must remain interoperable with the metadata standards used upstream.

### STAC
Commonly displayed (when present and allowed):
- `id`, `collection`
- `license`
- `datetime` or `start_datetime`/`end_datetime`
- spatial coverage summaries (only if already generalized)
- selected `assets` summaries (do not dump all assets by default)

### DCAT
Commonly displayed (when present and allowed):
- dataset title + description
- publisher / contact (if provided)
- license + access rights
- distributions (safe listing; action gating may apply)
- temporal + spatial coverage summaries

### PROV-O
DataCards should provide at least one provenance affordance:
- short provenance summary
- expandable provenance trail
- link to a provenance/manifest view (when provided)

Rule: if provenance is absent upstream, do not invent a chain.

### Versioning
- If upstream includes predecessor/successor references, DataCards may display “Supersedes / Superseded by” links.
- DataCards must never imply that a version relationship exists unless supplied upstream.

---

## 🧱 Architecture

### DataCard.tsx
Suite orchestrator:
- composes header/metadata/preview/footer
- applies redaction directives (hide/disable as needed)
- provides semantic HTML wrapper (`<article>` + labeled regions)
- triggers telemetry hooks (suite-scoped)

### DataCardHeader.tsx
- title, subtitle/type label
- CARE/classification badges when provided
- sovereignty notice placement (header prominence when present)
- provenance affordance (expand/open)

### DataCardMetadata.tsx
- key metadata fields (publisher, license, rights-holder, temporal/spatial summaries)
- explicit unknown placeholders
- no precision leaks

### DataCardPreview.tsx
- only renders when allowed by governance
- requires textual equivalents (caption / SR summary)
- if generalized: explicitly label as generalized and avoid precision language

### DataCardFooter.tsx
- action buttons, policy-aware:
  - open details
  - open in map (if allowed)
  - view provenance (generally safe)
- restricted datasets: disable actions with an explanation (not silently)

### DataCardA11yHelpers.tsx
- shared ARIA helpers and screen-reader summaries
- focus order management for composite layouts
- reduced-motion-friendly patterns for loading/animation

### DataCardSkeleton.tsx
- safe loading state
- must never reveal sensitive strings while loading
- must respect reduced motion preferences

---

## 🧠 Story Node & Focus Mode Integration

### Focus Mode usage
DataCards commonly display:
- supporting datasets relevant to a focal entity
- evidence trails backing a narrative block
- related distributions/assets (when allowed)

Requirements:
- sovereign-controlled contexts elevate sovereignty notices and suppress precision-implying previews
- prefer routing users to provenance/governance details over “open raw” actions

### Story Node usage
DataCards may appear as:
- referenced datasets
- supporting evidence
- assets/distributions

Rule: DataCards must not add narrative interpretation. They only display metadata and provenance already attached to the Story Node or dataset record.

---

## 🧪 Validation and CI/CD

Expected gates for DataCards changes:
- markdown protocol validation for this README
- unit + integration tests for DataCards components
- a11y checks (keyboard flow, focus order, SR equivalents, reduced motion)
- governance tests (redaction-required flows, sovereignty notices, action gating)
- telemetry schema validation for emitted events

Expected test locations:

~~~text
📁 tests/unit/web/components/DataCards/
📁 tests/integration/web/components/DataCards/
~~~

CI blocking examples:
- restricted dataset shows preview surface implying precision
- license/CARE/rights-holder present upstream but missing in UI
- telemetry includes raw IDs or sensitive fields
- keyboard focus traps / missing SR equivalents

---

## ⚖ FAIR+CARE and Governance

### Non-negotiables
- Display CARE + sovereignty indicators when provided upstream
- Never show precise coordinates for restricted datasets
- Never emit sensitive identifiers in telemetry
- Never “upgrade” uncertain coverage (temporal/spatial)
- Never infer missing metadata

### Sovereignty-aware behavior
If sovereign-control indicators are present:
- elevate notices to header prominence
- default to safer displays (generalized extents, disabled previews)
- route users to rights/provenance rather than raw export actions

### Redaction-required posture
When a dataset’s governance overlay indicates redaction is required:
- previews are opt-in and policy-gated
- metadata fields are whitelisted by governance layer
- user-facing explanations are required when data is hidden

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v12.0.0 | 2025-12-21 | Rebuilt from scratch to be v12-ready using the Universal Governed Doc structure; moved non-template YAML fields into body artifacts; clarified UI/API boundary and redaction invariants. | TBD |
| v11.2.2 | 2025-12-15 | Prior governed suite overview (pre-v12 doc structure). | TBD |
| v10.4.0 | 2025-11-15 | Earlier major update (pre-v11 standards). | TBD |

---

## 📎 References

- Repo root: `../../../../README.md`
- Master guide: `../../../../docs/MASTER_GUIDE_v12.md`
- Governance: `../../../../docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `../../../../docs/governance/ETHICS.md`
- Sovereignty: `../../../../docs/governance/SOVEREIGNTY.md`
- Telemetry schemas: `../../../../schemas/telemetry/`
---