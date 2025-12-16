---
title: "✨ Kansas Frontier Matrix — Web Features Layer Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/features/README.md"
version: "v11.2.6"
last_updated: "2025-12-16"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.6/manifest.zip"
telemetry_ref: "../../../releases/v11.2.6/web-features-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/web-features-readme-v2.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"
signature_ref: "../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../releases/v11.2.6/slsa-attestation.json"

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
doc_kind: "Overview"
intent: "web-features-overview"
role: "overview"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Mixed (feature-dependent)"
sensitivity_level: "Feature-dependent"
public_exposure_risk: "Low · Medium"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low · Medium"
redaction_required: false

provenance_chain:
  - "web/src/features/README.md@v11.2.2"
  - "web/src/features/README.md@v10.4.1"
  - "web/src/features/README.md@v10.3.2"
  - "web/src/features/README.md@v10.3.1"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "SoftwareApplication"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"

json_schema_ref: "../../../schemas/json/web-features-readme-v11.schema.json"
shape_schema_ref: "../../../schemas/shacl/web-features-readme-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:web-features-readme-v11.2.6"
semantic_document_id: "kfm-doc-web-features-readme-v11"
event_source_id: "ledger:web/src/features/README.md"
immutability_status: "version-pinned"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative-additions"
  - "unverified-historical-claims"
  - "governance-override"
  - "content-alteration"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
classification: "Public Document"
lifecycle_stage: "stable"
ttl_policy: "Review annually"
sunset_policy: "Superseded on next feature-architecture revision"

fencing_profile: "outer-backticks-inner-tildes-v1"
directory_layout_profile: "immediate-one-branch-with-descriptions-and-emojis"
badge_profile: "standard-four-badges"

test_profiles:
  - "markdown-lint-v1"
  - "schema-lint-v1"
  - "link-check-v1"
  - "heading-registry-check-v1"
  - "a11y-lint-v1"

ci_integration:
  required_checks:
    - "markdown-lint"
    - "schema-lint"
    - "link-check"
    - "footer-check"
    - "accessibility-check"
    - "diagram-check"
    - "metadata-check"
    - "provenance-check"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "🧱 Architecture"
    - "🧭 Context"
    - "🗺️ Diagrams"
    - "🧠 Story Node & Focus Mode Integration"
    - "🌐 STAC, DCAT & PROV Alignment"
    - "📦 Data & Metadata"
    - "🧪 Validation & CI/CD"
    - "⚖ FAIR+CARE & Governance"
    - "🕰️ Version History"
---

<div align="center">

# ✨ **Kansas Frontier Matrix — Web Features Layer Overview (v11.2.6)**
`web/src/features/README.md`

**Purpose**  
Define the canonical structure, responsibilities, boundaries, governance rules, and telemetry expectations for the
**Features Layer** in the KFM Web Platform. Each feature is a **self-contained user-facing capability** that integrates
pipelines, hooks, view-models, governance, accessibility, and telemetry — while keeping rendering concerns in
`web/src/components/**` and routing concerns in `web/src/pages/**`.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../mcp/MCP-README.md)
· [![KFM–MDP v11.2.6](https://img.shields.io/badge/KFM%E2%80%93MDP-v11.2.6-purple)](../../../docs/standards/kfm_markdown_protocol_v11.2.6.md)
· [![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Aligned-orange)](../../../docs/standards/faircare/FAIRCARE-GUIDE.md)
· [![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../LICENSE)

</div>

---

## 📘 Overview

`web/src/features/**` is where KFM groups **domain-driven capabilities** that span multiple architectural layers
without becoming UI components themselves.

A feature is responsible for:

- Orchestrating feature flows (user intent → validated inputs → pipeline/service calls → view-models → UI wiring).
- Providing **typed, deterministic** “feature APIs” that can be consumed by `pages/`, hooks, and pipeline wrappers.
- Applying **FAIR+CARE** and sovereignty constraints *at the feature boundary* (never later, never optionally).
- Producing UI-ready view models and state slices **without embedding React rendering**.

A feature is *not* responsible for:

- Rendering UI (belongs in `web/src/components/**`).
- Owning global application state (belongs in `web/src/context/**`).
- Calling backend endpoints ad hoc (belongs in `web/src/services/**`, often coordinated via `web/src/pipelines/**`).
- Inventing types or relationships not present in governed schemas (`web/src/types/**`).

**Design intent:** Features are the “capability layer” between architectural primitives (types, services, pipelines, entities)
and UI assembly (components, pages).

---

## 🗂️ Directory Layout

~~~text
📁 web/src/features/
├── 📄 README.md                — This document (feature-layer contract)
├── 📁 accessibility/           — Cross-cutting A11y capability helpers (feature-scoped)
├── 📁 admin/                   — Governed admin capabilities (restricted routes; governance tooling)
├── 📁 focus-mode/              — Focus Mode v3 feature module (logic + VMs + orchestration)
├── 📁 map/                     — Map feature module (layer toggles, map interactions, workflows)
├── 📁 search/                  — Search feature module (entity/dataset search; query parsing; results shaping)
├── 📁 story/                   — Story Node v3 feature module (narrative flows; relation navigation)
├── 📁 telemetry/               — Telemetry feature module (event builders, Vitals adapters, error taxonomy helpers)
└── 📁 timeline/                — Timeline feature module (range/brush/zoom flows; TimeContext coupling)
~~~

**Naming conventions**

- Directories are lowercase and hyphen-separated (e.g., `focus-mode/`, `ar-mode/`).
- Each feature directory should include its own `README.md` when the module is non-trivial.

---

## 🧱 Architecture

### Feature module contract

Each feature should expose a **stable public surface** and keep internal details private.

Recommended pattern:

- `web/src/features/<feature>/index.ts` exports the feature’s intended API surface.
- Internals remain under `hooks/`, `pipelines/`, `state/`, `view-models/`, `telemetry/`, etc.

A typical (non-normative) feature module shape:

~~~text
📁 web/src/features/<feature>/
├── 📄 README.md                — Feature contract, workflows, governance notes
├── 📄 index.ts                 — Public export surface (barrel)
├── 📁 hooks/                   — Feature hooks (no JSX; effect boundaries)
├── 📁 pipelines/               — Orchestration wrappers (multi-step flows)
├── 📁 state/                   — Feature-local state machines/slices (not global contexts)
├── 📁 view-models/             — UI-ready derived models (typed, governance-carrying)
├── 📁 telemetry/               — Event builders + attribute mappers (non-PII)
└── 📁 __tests__/               — Feature-level unit/integration tests (if co-located)
~~~

### Import boundaries

To preserve layered architecture, feature code:

**May import from (down-layer and peer utilities):**

- `web/src/types/**` (DTOs and domain typing)
- `web/src/entities/**` (entity view-models and mappers/factories)
- `web/src/utils/**` (pure helpers and guards)
- `web/src/services/**` and/or `web/src/pipelines/**` (governed data access and orchestration)
- `web/src/context/**` (consume and update shared state through approved APIs)

**Must not import from (up-layer composition):**

- `web/src/pages/**` (routes compose features; features do not know routes)
- `web/src/App.tsx` or `web/src/main.tsx`
- UI components directly as implementation details

If a feature needs to “expose” UI components, do so as an **import surface** only (re-export),
without co-locating rendering logic inside the feature module.

### Determinism and side-effect boundaries

Feature logic must remain deterministic given the same inputs and governed backend responses:

- Validation occurs at the edge (guards/schemas) before view-model creation.
- Side effects are isolated to hooks and pipeline/service boundaries.
- Feature modules must not mutate global state outside context APIs.

---

## 🧭 Context

Features integrate with the global state layer via `web/src/context/**`.

Core expectations:

- Features **read/write** shared state only through context APIs.
- Features must not invent “shadow global state” in module singletons.
- Feature-local state is allowed, but must remain *feature-scoped* and must not conflict with contexts.

Typical context usage by feature:

- `timeline/` uses `TimeContext` as the canonical temporal source of truth.
- `map/` uses `MapContext` for camera/layers/selection and must respect `GovernanceContext`.
- `focus-mode/` uses `FocusContext` and coordinates with `TimeContext` and `MapContext`.
- `story/` updates `FocusContext` and `TimeContext` when navigating narrative relations.
- Cross-cutting `telemetry/` observes context transitions (non-PII) to emit events.

Suggested rule of thumb:

- **Contexts own state**; **features own workflows**.

---

## 🗺️ Diagrams

### Feature layering relative to the rest of `web/src/`

~~~mermaid
flowchart TD
  P[Pages · Route Containers] --> C[Components · UI Rendering]
  P --> F[Features · Capability Modules]
  C --> F

  F --> E[Entities · View Models]
  F --> H[Hooks · Effect Boundaries]
  H --> S[Services · API Clients]
  H --> PL[Pipelines · Orchestration]
  F --> X[Contexts · Shared State]

  PL --> S
  S --> API[Backend APIs · REST · GraphQL · STAC · DCAT]
  E --> X
~~~

### Canonical journey wiring (example)

~~~mermaid
flowchart LR
  Search[search/] --> Select[entity:select]
  Select --> Focus[focus-mode/]
  Focus --> Story[story/]
  Focus --> Map[map/]
  Story --> Timeline[timeline/]
  Timeline --> Map
  Focus --> Tel[telemetry/]
  Story --> Tel
  Map --> Tel
  Timeline --> Tel
~~~

---

## 🧠 Story Node & Focus Mode Integration

Two feature modules are structurally central to KFM’s v11 UX:

### `focus-mode/` (Focus Mode v3)

Feature responsibilities include:

- Orchestrating Focus requests (validated inputs → pipeline/service calls → view-model shaping).
- Maintaining feature-local state for loading/error/retry states (global focus selection remains in `FocusContext`).
- Producing view models for:
  - focus target summaries
  - relations and ranked neighbors
  - explainability/evidence sets
- Enforcing governance display obligations:
  - provenance references must be present
  - CARE labels and sovereignty flags must be available to the UI
  - no client-side speculative additions

### `story/` (Story Node v3)

Feature responsibilities include:

- Validating Story Node payloads before they reach UI layers.
- Producing view models for list/detail display and relationship navigation.
- Coordinating synchronization:
  - selecting a Story Node updates `FocusContext`
  - Story Node temporal spans update `TimeContext` (when appropriate)
  - Story Node spatial references update map highlight state (through `MapContext`)

**Shared contract:** Both features must keep map, timeline, and focus views coherent by updating shared contexts,
not by maintaining hidden global state.

---

## 🌐 STAC, DCAT & PROV Alignment

Feature modules must treat catalog and provenance systems as first-class constraints.

### STAC (KFM-STAC v11)

- Features may browse STAC collections/items through services/pipelines.
- Any derived view model must preserve:
  - STAC identifiers
  - license/rights fields
  - spatial/temporal extent fields (as provided; no expansion by assumption)

### DCAT (KFM-DCAT v11)

- Search and dataset-related features may expose DCAT datasets/distributions.
- View models must surface:
  - publisher/creator where present
  - distribution access links (when allowed)
  - rights and licensing constraints

### PROV-O (KFM-PROV v11)

- Features that render narratives or derived summaries must carry provenance references:
  - source datasets/documents
  - transformation activities (when available)
  - agents (systems/councils/bots) where applicable

---

## 📦 Data & Metadata

### Telemetry

Feature modules participate in telemetry through the shared telemetry system:

- Feature events should be non-PII, schema-valid, and aggregatable.
- Recommended patterns:
  - `feature:<featureKey>:open`
  - `feature:<featureKey>:close`
  - `feature:<featureKey>:action` (with typed attributes describing outcome)

Release storage:

~~~text
../../../releases/<version>/web-features-telemetry.json
~~~

### Sustainability instrumentation

Feature workflows should support energy and carbon accounting by:

- emitting stable, low-cardinality signals (e.g., “focus-run”, “stac-search”, “timeline-scrub”)
- avoiding per-entity unique identifiers in telemetry payloads (aggregate instead)

### Feature documentation metadata

When a feature introduces a new capability with governance implications (e.g., new visualization mode),
the feature README should include:

- governance notes (risk, masking expectations)
- A11y notes (keyboard/screen-reader expectations)
- telemetry notes (events and error taxonomy)

---

## 🧪 Validation & CI/CD

This README and the features layer are validated as part of governed CI.

### Documentation validation (README)

Expected checks include:

- Markdown linting and formatting validation
- Schema/metadata validation
- Heading registry validation (H2 headings must match `heading_registry`)
- Link checks
- Footer and governance-link checks
- Diagram validation (Mermaid hygiene)

### Code validation (features layer)

Feature modules should be covered by:

- **Unit tests** for:
  - view-model builders
  - guards and parsers
  - state reducers/machines
- **Integration tests** for:
  - feature flows that coordinate multiple contexts
  - pipeline/service orchestration wrappers
- **Governance tests** for:
  - masking and redaction behavior (feature-dependent)
  - sovereignty flags and CARE labels propagation
- **Accessibility tests** for:
  - feature-driven workflows that affect keyboard/screen-reader flows
- **Telemetry tests** for:
  - schema-valid event shapes
  - correct aggregation behavior for sensitive content

Suggested test locations:

~~~text
tests/unit/web/features/<feature>/**
tests/integration/web/features/<feature>/**
tests/e2e/web/features/<feature>/**
~~~

---

## ⚖ FAIR+CARE & Governance

Features are a governance-critical layer because they:

- translate user intent into data access patterns,
- shape view-models that UI components render,
- coordinate interactions across map/time/story/focus.

Therefore, every feature must:

- Respect backend governance decisions (frontend may be stricter; never looser).
- Enforce masking/generalization rules before view-models reach UI.
- Keep governance metadata attached:
  - CARE labels
  - sovereignty flags
  - provenance references
  - license/rights
- Avoid speculative relationships, inferred facts, or unverified historical claims.
- Ensure warnings and disclosure signals remain available to governance UI components.

Governance failures introduced at the feature layer are treated as **CI-blocking defects**.

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v11.2.6** | 2025-12-16 | Updated to KFM-MDP v11.2.6 formatting and metadata; normalized H2 headings via `heading_registry`; clarified feature boundaries, import surfaces, and CI expectations. |
| v11.2.2     | 2025-11-30 | Updated to KFM-MDP v11.2.2; improved governance, telemetry v2, A11y rules, and feature schema alignment. |
| v10.4.1     | 2025-11-15 | Polished v10.4.1 structure; removed deprecated `focus/` folder. |
| v10.4.0     | 2025-11-15 | Feature architecture rewrite aligned with pipelines & governance. |
| v10.3.2     | 2025-11-14 | Added governance + dataset explorer alignment. |
| v10.3.1     | 2025-11-13 | Initial baseline structure. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
FAIR+CARE Certified · Public Document · Version-Pinned

[⬅️ Back to Web Source Overview](../README.md) ·
[🧱 Web Source Architecture](../ARCHITECTURE.md) ·
[👥 Entities Layer](../entities/README.md) ·
[🧠 Context System](../context/README.md) ·
[🛡 Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
