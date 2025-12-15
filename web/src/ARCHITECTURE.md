---
title: "💻 Kansas Frontier Matrix — Web Source Architecture Specification (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/ARCHITECTURE.md"
version: "v11.2.6"
last_updated: "2025-12-15"

review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
release_stage: "Stable / Governed"
status: "Active / Enforced"
lifecycle_stage: "LTS"
backward_compatibility: "Aligned: v10.x → v11.x"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../releases/v11.2.6/manifest.zip"
telemetry_ref: "../../releases/v11.2.6/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/web-src-architecture-v11.json"
energy_schema: "../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../schemas/telemetry/carbon-v2.json"
signature_ref: "../../releases/v11.2.6/signature.sig"
attestation_ref: "../../releases/v11.2.6/slsa-attestation.json"

governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

doc_kind: "Architecture"
intent: "web-src-architecture"
role: "architecture"
category: "Web · Source · Architecture · UI"

fair_category: "F1-A1-I2-R3"
care_label: "Public · Low-Risk"
sensitivity_level: "Low"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false

provenance_chain:
  - "web/src/ARCHITECTURE.md@v10.0.0"
  - "web/src/ARCHITECTURE.md@v10.3.2"
  - "web/src/ARCHITECTURE.md@v10.4.1"
  - "web/src/ARCHITECTURE.md@v11.0.0"
  - "web/src/ARCHITECTURE.md@v11.2.2"

ontology_alignment:
  cidoc: "E31 Document"
  schema_org: "SoftwareSourceCode"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
  geosparql: "N/A"

json_schema_ref: "../../schemas/json/web-src-architecture-v11.schema.json"
shape_schema_ref: "../../schemas/shacl/web-src-architecture-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:web-src-architecture-v11.2.6"
semantic_document_id: "kfm-doc-web-src-architecture"
event_source_id: "ledger:web/src/ARCHITECTURE.md"
immutability_status: "version-pinned"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "diagram-extraction"
  - "metadata-extraction"
  - "layout-normalization"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
classification: "Public Document"
ttl_policy: "Review required every 12 months"
sunset_policy: "Superseded upon next major web-src architecture update"
---

<div align="center">

# 💻 **Kansas Frontier Matrix — Web Source Architecture Specification (v11)**  
`web/src/ARCHITECTURE.md`

**Purpose**  
Define the **source-level, enforceable architecture** for `web/src/**` within the Kansas Frontier Matrix (KFM) Web Platform.

This spec governs:
UI composition, state management, Focus Mode v3 flows, Story Node v3 rendering, 2D/3D geovisualization,
accessibility-first patterns, FAIR+CARE + sovereignty visibility/enforcement hooks, typed DTO boundaries,
STAC/DCAT integration surfaces, and telemetry instrumentation.

<img src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Governance%20Aligned-orange" />
<img src="https://img.shields.io/badge/Accessibility-WCAG_2.1_AA%2B-blueviolet" />
<img src="https://img.shields.io/badge/License-CC--BY--4.0-green" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

</div>

---

## 📘 Overview

`web/src/**` is the governed frontend source layer for the KFM Web Application (`web/**`), which is described
as a React-based interface with 2D/3D visualization (MapLibre + Cesium) in the repo layout. It is responsible
for rendering, interaction orchestration, and policy-visible UI behaviors — **not** for core governance decisions,
graph writes, or pipeline execution.

### Scope (what this spec governs)

- **UI composition**: components, pages, layouts, and interaction patterns.
- **State architecture**: shared contexts and deterministic flows between map, timeline, Story, and Focus.
- **API integration boundary**: typed access to REST / GraphQL / JSON-LD / STAC / DCAT endpoints.
- **Rendering pipelines**: 2D (MapLibre) and 3D (Cesium) visual layers and their governance constraints.
- **Governance surfacing**: CARE labels, sovereignty flags, masking notices, licensing and provenance affordances.
- **Accessibility**: WCAG 2.1 AA+ compliance as a first-class architectural requirement.
- **Telemetry**: instrumented UX flows and performance signals (schema-constrained; no PII).

### Non-goals (explicitly out of scope)

- ETL/pipeline implementation (belongs under `src/pipelines/**` and `tools/**`).
- Knowledge-graph schema design (belongs under `src/graph/**` + ontology docs).
- Backend services implementation (FastAPI / GraphQL, Focus transformers, etc.).
- CI/CD workflow definitions (belongs under `.github/**` and governed workflow docs).

### Architectural invariants (normative)

1. **Frontend is behind APIs**  
   `web/src/**` MUST NOT access Neo4j or internal storage directly. All data access occurs via approved
   REST/GraphQL/JSON-LD endpoints and catalog services.

2. **Read-only for governed content**  
   The client MUST NOT mutate “core truth” datasets. Permitted writes are limited to local preferences
   and client-side caches.

3. **Governance decisions are enforced server-side and surfaced client-side**  
   The frontend MUST render governance signals (CARE, sovereignty, masking) and MUST NOT provide
   toggles that bypass enforced restrictions.

4. **Deterministic UX flows**  
   Given identical API responses and identical user actions, the resulting UI state must be reproducible.

5. **No secrets / no PII**  
   UI telemetry and UI storage MUST exclude PII and secrets. Logs and errors must be non-leaky.

### Related documents

- `web/README.md` — Web platform behavioral contract.
- `web/ARCHITECTURE.md` — Web subsystem architecture.
- `../ARCHITECTURE.md` — Monorepo system architecture.
- `.github/ARCHITECTURE.md` — CI/CD architecture & governance infrastructure.

---

## 🗂️ Directory Layout

Directory layouts are normative and must remain stable. Structural changes require architecture review.

~~~text
📁 web/src/                                              — Web app source (React/TypeScript; governed)
├── 📄 main.tsx                                          — SPA bootstrap (root render + provider stack)
├── 📄 App.tsx                                           — Top-level routing shell + global layout
│
├── 📁 components/                                       — UI components (JSX/presentation + interaction)
│   ├── 📁 map/                                          — MapLibre view(s), controls, layer rendering
│   ├── 📁 cesium/                                       — Cesium view(s), camera controls, 3D overlays
│   ├── 📁 timeline/                                     — Timeline controls, brushes, time affordances
│   ├── 📁 story/                                        — Story Node v3 cards, details, media renderers
│   ├── 📁 focus/                                        — Focus Mode v3 panels, explainability widgets
│   ├── 📁 stac/                                         — STAC/DCAT explorer widgets + dataset previews
│   ├── 📁 governance/                                   — CARE labels, sovereignty chips, masking notices
│   └── 📁 layout/                                       — App shell, split panes, responsive scaffolding
│
├── 📁 pages/                                            — Route containers (compose features + contexts)
├── 📁 context/                                          — Shared state providers (time, focus, map, etc.)
├── 📁 hooks/                                            — Hooks (logic/effects; call pipelines/services)
├── 📁 pipelines/                                        — Multi-step orchestrators (focus/story/stac/time)
├── 📁 services/                                         — Typed clients (REST/GraphQL/JSON-LD/STAC/DCAT)
├── 📁 types/                                            — DTOs + domain types + telemetry payload shapes
├── 📁 utils/                                            — Stateless helpers (guards, formatting, geometry)
└── 📁 styles/                                           — Design tokens adapters, global styles, map styles
~~~

### Placement rules (enforced)

- `components/**` MUST NOT call APIs directly.
- `services/**` MUST contain all network access and external IO calls.
- `pipelines/**` MAY coordinate multi-step flows, but MUST not render UI.
- `types/**` MUST define inbound/outbound DTOs and internal domain types.
- `utils/**` MUST be stateless (no network, no storage, no side effects).

---

## 🧭 Context

Shared state must be explicit, testable, and traceable. Context providers are the authoritative
cross-feature coordination mechanism.

### Core contexts (minimum set)

- **TimeContext**
  - owns active interval(s), brush selections, and temporal granularity.
  - drives timeline → map/layer filtering and story/focus sync.

- **FocusContext**
  - owns the current focus target (entity/story/dataset), Focus Mode UI state, and panel mode.
  - drives focus → map highlighting and related Story Node selection.

- **MapContext**
  - owns map viewport, layer toggles, selection/hover state, and map-mode preferences.
  - provides a controlled API to set highlighted features and active layers.

- **GovernanceContext**
  - owns governance-visible metadata that affects rendering:
    CARE label, sovereignty flags, masking requirements, license display rules.
  - provides helpers for “why masked?” and “show provenance” affordances.

- **ThemeContext**
  - owns theme and contrast mode preferences.

- **A11yContext**
  - owns reduced motion, font scale, keyboard-first flags, and accessible alternates for complex widgets.

- **ExplorerContext** (STAC/DCAT)
  - owns filters (time/space/license), pagination state, and current selection.

### State ownership rules

- Only the owning context may define the canonical value for that domain state.
- Cross-feature updates must occur via context actions/reducers — no “side-channel” globals.
- Local component state is allowed only for ephemeral UI state (open/closed, hover, transient input).

### Synchronization rules (must remain consistent)

- **Timeline → Map/Story/Focus**
  - Time selection filters visible layers and Story Node lists.
- **Map → Story/Focus**
  - Selecting a feature updates either Story selection or Focus selection, subject to governance.
- **Story → Map/Timeline**
  - Selecting a Story Node MUST update both spatial focus (map) and temporal focus (timeline).
- **Focus → Map/Timeline/Story**
  - Focus Mode selection may highlight layers, clamp time ranges, and suggest related Story Nodes;
    any changes MUST be explicit and reversible.

### Persistence rules

- Only preferences MAY persist locally (e.g., theme, reduced motion, last view mode).
- Persisted values MUST be non-identifying and MUST NOT include sensitive coordinates or restricted IDs.

---

## 🧱 Architecture

This section defines the source-level architectural contracts and dependency rules.

### Layer boundaries and dependency direction

`web/src/**` uses a layered model with strict dependency flow:

- **Pages** compose feature views and route-level orchestration.
- **Components** render UI and handle local interactions.
- **Contexts** expose shared state and controlled mutations.
- **Hooks** encapsulate effects/logic and connect contexts to pipelines/services.
- **Pipelines** coordinate multi-step flows (fetch → validate → update contexts → emit telemetry).
- **Services** perform network IO, schema validation, error normalization, and tracing.
- **Types/Utils** are pure helpers and contracts.

**Dependency rule:** higher layers may depend on lower layers; lower layers MUST NOT import higher layers.

~~~text
Allowed:
pages → components, hooks, context, types, utils
components → hooks, context, types, utils, styles
hooks → pipelines, services, context, types, utils
pipelines → services, context, types, utils
services → types, utils
types → (no imports except other types)
utils → types (optional)

Forbidden:
components → services (direct)
services → components/pages/context
utils → services/pipelines
~~~

### API integration and DTO boundary

The frontend consumes data through:

- **Catalog + static artifacts** (preferred): generated JSON catalogs, tiles, and STAC items/collections.
- **Dynamic APIs** (when needed): REST / GraphQL / JSON-LD endpoints for search and graph-backed queries.

**Service responsibilities (normative):**

- Validate all inbound payloads before they reach UI (schema-based runtime validation).
- Normalize errors into stable typed shapes (network vs validation vs governance-denial).
- Attach telemetry context (trace/span IDs where applicable) without leaking identifiers.
- Enforce “no PII / no secrets” in any log output.

### Rendering architecture (2D + 3D)

#### 2D rendering (MapLibre)

- Loads basemaps and overlay layers from declarative config + catalogs.
- Renders Story Node footprints (GeoJSON) and dataset previews (tiles/COGs where supported).
- Honors governance flags:
  - generalized/masked geometry MUST be visually labeled,
  - restricted layers MUST not be renderable without explicit backend allowance.

#### 3D rendering (Cesium)

- Provides deep-time / terrain / camera-driven exploration views.
- Must honor:
  - time filters (TimeContext),
  - reduced motion settings (A11yContext),
  - governance masking requirements (GovernanceContext).

#### Declarative layer configuration (governed)

Layer availability and defaults MUST be defined in declarative registries (JSON/YAML),
so that:
- governance metadata can be attached per layer,
- layers can be audited and validated in CI,
- UI does not introduce “ad-hoc” untracked layers.

### Accessibility architecture (WCAG 2.1 AA+)

Accessibility is not optional — it is a source-level contract.

- All interactive elements must be keyboard reachable with visible focus states.
- Complex widgets (map/3D) MUST provide accessible alternates:
  - textual summaries and a navigable feature list,
  - reduced motion and simplified interaction modes.
- A11y settings must be centralized in A11yContext and applied consistently across features.

### Telemetry architecture (schema-constrained)

Telemetry must be centralized and schema-validated:

- Route changes, major UI interactions, focus/story/stac workflows:
  - emitted via telemetry services/hooks only (not ad-hoc console logs).
- All telemetry payloads MUST validate against `telemetry_schema`.
- PII is prohibited:
  - no raw coordinates when masked,
  - no user identifiers,
  - no free-text fields that can leak secrets.

### Error handling and resilience

- Feature flows MUST use consistent loading/error/empty states.
- Errors MUST be classified:
  - `network_error` / `validation_error` / `governance_denial` / `render_error`.
- Error boundaries MUST prevent hard crashes and provide a safe fallback view.
- User-facing messages must be non-leaky and governance-safe.

---

## 🗺️ Diagrams

### Source-layer dependency and dataflow

~~~mermaid
flowchart TD
  P[Pages] --> C[Components]
  C --> X[Contexts]
  C --> H[Hooks]
  H --> PL[Pipelines]
  PL --> S[Services]
  S --> API[REST / GraphQL / JSON-LD]
  S --> CAT[STAC / DCAT / Catalog Services]
  S --> TEL[Telemetry Backend]

  X --> H
  X --> C
~~~

### Interaction synchronization (map · timeline · story · focus)

~~~mermaid
sequenceDiagram
  autonumber
  actor U as User
  participant TL as TimelineView
  participant MV as MapView
  participant SN as StoryNode UI
  participant FP as FocusPanel
  participant CTX as Context Providers
  participant SVC as Services

  U->>TL: Adjust time brush
  TL->>CTX: TimeContext.setInterval()
  CTX-->>MV: time filter update
  CTX-->>SN: story list filter update
  MV->>SVC: (optional) fetch filtered layers
  SVC-->>MV: validated layer data

  U->>SN: Select Story Node
  SN->>CTX: FocusContext.setStory(storyId)
  SN->>CTX: TimeContext.jumpTo(storyTime)
  CTX-->>MV: highlight geometry
  CTX-->>FP: update focus target

  U->>MV: Click governed feature
  MV->>CTX: attempt selection
  CTX-->>FP: open focus (if allowed)
  FP->>SVC: request focus payload
  SVC-->>FP: validated focus response + governance flags
~~~

---

## 🧠 Story Node & Focus Mode Integration

Story Node v3 and Focus Mode v3 are the primary narrative/intelligence surfaces in the web UI.

### Story Node v3 (frontend responsibilities)

- Render Story Nodes as:
  - cards (summary),
  - detail panels (full narrative),
  - map footprints (2D/3D),
  - timeline anchors (time range / instants).
- Show governance metadata with every story:
  - CARE label, sovereignty flag, license, provenance.
- Enforce masking:
  - if a story’s geometry is generalized/masked, the UI MUST label the display as generalized
    and MUST NOT provide precision reveal affordances.

### Focus Mode v3 (frontend responsibilities)

- Focus Mode is displayed, not generated, in the frontend:
  - AI reasoning and filtering happens server-side.
- The UI must:
  - present “why am I seeing this?” affordances,
  - display provenance chips for narrative claims,
  - display governance limitations as first-class UI elements (not footnotes).
- Focus Mode panels must remain deterministic:
  - the UI does not invent content, and must not “fill in” missing facts.

### Visual evidence and governed media

If the Focus payload or Story Node references images/plots/reports:

- UI MUST show provenance per asset (caption/link back to metadata).
- UI MUST gate sensitive media with explicit warnings/denials as required.
- UI SHOULD lazy-load media to avoid UI stalls and to support low-power devices.

---

## 📦 Data & Metadata

### Data sources consumed by `web/src/**`

The frontend may consume:

- **Static catalogs** (JSON) generated by pipelines (preferred).
- **STAC collections/items** for dataset discovery and spatial/temporal filtering.
- **Vector/raster tiles and COG-like assets** (where the hosting system supports range requests).
- **API responses** for dynamic graph-backed queries (search, related entities, Focus payloads).

### Metadata surfacing requirements (normative)

- Every dataset preview must show:
  - license/attribution,
  - provenance entry points,
  - temporal and spatial extents,
  - governance indicators (CARE + sovereignty + masking).
- Every map layer must expose:
  - a readable legend,
  - provenance link(s),
  - “masked/generalized” status when applicable.

### Local-only data (allowed)

`web/src/**` may store:

- theme and a11y preferences,
- last selected view mode (2D/3D),
- cached responses that contain no restricted content and no PII.

It must not store:

- secret tokens,
- user identifiers,
- restricted coordinates or unmasked sensitive geometries.

---

## 🌐 STAC, DCAT & PROV Alignment

The web source layer must align metadata and lineage surfaces to KFM’s profiles:

- **STAC (1.0)**: collections/items for spatiotemporal assets.
- **DCAT**: dataset-level catalog views for governance/FAIR surfacing.
- **PROV-O**: provenance relationships used to power “show sources” and audit navigation.

### UI mapping guidelines

- STAC `id` → stable dataset/item identifier in UI.
- STAC `geometry`/`bbox` → map preview footprint (subject to governance masking).
- STAC `datetime`/temporal properties → timeline placement and filtering.
- STAC `assets` → previewable resources (tiles, images, reports), each with provenance links.
- PROV relationships → “generated by / derived from / used” disclosure in UI.

### Validation expectations

- STAC and DCAT payloads consumed by services MUST be validated against pinned validators
  (deterministic CI and reproducible behavior).
- Schema violations must fail safe:
  - no partial rendering of unvalidated content,
  - clear user-safe error states.

---

## ⚖ FAIR+CARE & Governance

The frontend must surface governance — not obscure it.

### Required governance UI elements

- CARE label and sovereignty indicator must appear on:
  - Story Nodes,
  - dataset cards and previews,
  - Focus Mode narratives,
  - map layer inspector panels.
- Masking/generalization must be explicit:
  - show a “generalized location” indicator,
  - provide “why masked?” explanation entry points,
  - prevent “precision reconstruction” via UI affordances.

### Prohibited behaviors

- Disabling or hiding governance overlays when policy requires them.
- Presenting AI summaries as archival fact.
- “Helpful” auto-completions that invent missing attribution or provenance.
- UI switches that attempt to bypass backend denials.

### AI transform guardrails (client-side)

The UI may format, summarize, and adapt presentation when allowed — but must not generate
new factual claims or override governance.

Allowed client transforms are limited to `ai_transform_permissions` in front-matter.
Prohibited transforms must not be implemented in any UI module.

---

## 🧪 Validation & CI/CD

`web/src/**` changes must be CI-clean and schema-valid.

### CI profiles (minimum)

- Markdown linting and protocol checks (for docs under `web/**`)
- Schema linting (telemetry payloads and DTO validation code)
- Footer and governance link checks (docs)
- Accessibility checks (automated + targeted manual)
- Diagram checks (mermaid renderability)
- Provenance checks (no orphan assets)
- Secret scanning and PII scanning

### Frontend test expectations

- **Unit tests**: components, hooks, services, utils.
- **Integration tests**: map↔timeline↔story↔focus synchronization.
- **E2E tests**: canonical journeys (Explore → Story → Focus → Dataset).
- **A11y tests**: Axe/Lighthouse audits and keyboard-only key flows.
- **Telemetry tests**: event payload schema conformance.

### Release and governance expectations

- Release artifacts referenced in front-matter (SBOM, manifest, signature, attestation)
  must be produced by governed release workflows and must remain version-pinned.
- Any change that affects governed presentation (masking rules, sovereignty surfacing,
  Focus Mode disclosure) requires FAIR+CARE review in the PR.

---

## 🕰️ Version History

| Version  | Date       | Summary |
|---------:|------------|---------|
| v11.2.6  | 2025-12-15 | Aligned with KFM-MDP v11.2.6: approved H2 registry, tilde-only internal fences, strengthened dependency rules, expanded governance + CI validation expectations, clarified STAC/DCAT/PROV UI mapping. |
| v11.2.2  | 2025-11-30 | v11.2.2 baseline: source layout, layer boundaries, Focus/Story/STAC integration, telemetry hooks. |
| v11.0.1  | 2025-11-27 | Clarified layer boundaries and context/service patterns; aligned with v11 web architecture. |
| v11.0.0  | 2025-11-24 | Initial v11 source architecture; aligned with Focus v3, Story Node v3, STAC/DCAT, and telemetry. |
| v10.4.1  | 2025-11-15 | Improved mapping between features, contexts, and services; clarified A11y responsibilities. |
| v10.3.2  | 2025-11-14 | Refined source structure; separated layout, map, and story components. |
| v10.0.0  | 2025-11-09 | Initial source architecture specification for `web/src/`. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
[⬅️ Back to Web Architecture](../ARCHITECTURE.md) · [🌐 Web Platform Overview](../README.md) · [🛡 Governance Charter](../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>