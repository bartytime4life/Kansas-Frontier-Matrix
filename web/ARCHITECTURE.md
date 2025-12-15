---
title: "🌐 Kansas Frontier Matrix — Web Application Architecture (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/ARCHITECTURE.md"
version: "v11.2.6"
last_updated: "2025-12-15"

review_cycle: "Quarterly · FAIR+CARE Council & Web Architecture Board"
release_stage: "Stable / Governed"
status: "Active / Enforced"
lifecycle_stage: "LTS"
backward_compatibility: "Aligned: v10.x → v11.x"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../releases/v11.2.6/manifest.zip"
telemetry_ref: "../releases/v11.2.6/focus-telemetry.json"
telemetry_schema: "../schemas/telemetry/web-architecture-v11.json"
energy_schema: "../schemas/telemetry/energy-v2.json"
carbon_schema: "../schemas/telemetry/carbon-v2.json"
signature_ref: "../releases/v11.2.6/signature.sig"
attestation_ref: "../releases/v11.2.6/slsa-attestation.json"

governance_ref: "../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

status_category: "Architecture"
doc_kind: "Architecture"
intent: "web-platform-architecture"
role: "architecture"
category: "Web · Architecture · UI"

fair_category: "F1-A1-I2-R3"
care_label: "Public · Low-Risk"
sensitivity_level: "Low"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false

provenance_chain:
  - "web/ARCHITECTURE.md@v11.2.2"
  - "web/ARCHITECTURE.md@v11.0.0"
  - "web/ARCHITECTURE.md@v10.4.0"
  - "web/ARCHITECTURE.md@v10.3.2"
  - "web/ARCHITECTURE.md@v10.0.0"

ontology_alignment:
  cidoc: "E31 Document"
  schema_org: "WebApplication"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../schemas/json/web-architecture-v11.schema.json"
shape_schema_ref: "../schemas/shacl/web-architecture-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:web-architecture-v11.2.6"
semantic_document_id: "kfm-doc-web-architecture"
event_source_id: "ledger:web/ARCHITECTURE.md"
immutability_status: "version-pinned"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "3d-context-render"
  - "a11y-adaptations"
  - "diagram-extraction"
  - "metadata-extraction"
  - "layout-normalization"
ai_transform_prohibited:
  - "speculative-additions"
  - "unverified-historical-claims"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"
  - "content-alteration"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
classification: "Public Document"
ttl_policy: "Review required every 12 months"
sunset_policy: "Superseded upon next major KFM web platform protocol release"
---

<div align="center">

# 🌐 **Kansas Frontier Matrix — Web Application Architecture (v11)**  
`web/ARCHITECTURE.md`

**Purpose**  
Define the **governed frontend architecture** for the Kansas Frontier Matrix (KFM) Web Platform:  
how the UI renders space/time, integrates **Story Nodes** and **Focus Mode**, surfaces **STAC/DCAT/PROV** metadata,  
and enforces **FAIR+CARE**, sovereignty, accessibility, and telemetry constraints.

<img src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Governance%20Aligned-orange" />
<img src="https://img.shields.io/badge/Accessibility-WCAG_2.1_AA%2B-blueviolet" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

</div>

---

## 📘 Overview

### 1. Scope and intent

The KFM Web Platform is the **primary spatial + narrative interface** for the system. It provides:

- 2D map exploration (MapLibre)
- 3D exploration (Cesium)
- Timeline-driven navigation and filtering
- Story Node v3 rendering and browsing
- Focus Mode v3 “deep dive” experiences with explainability surfaces
- Dataset discovery via STAC/DCAT explorers
- Governance overlays (CARE labels, sovereignty signals, masking)
- Telemetry emission (performance, a11y usage, Focus Mode behavior, energy/carbon summaries)

This file defines the **frontend architecture and behavioral contract** for code and assets under `web/**`.

### 2. Non-negotiable system invariants

The web client MUST:

1. **Stay behind governed APIs**  
   - No direct graph access from the frontend.  
   - No direct reads from raw lake/graph stores.

2. **Remain read-only for core knowledge**  
   - Client mutations are limited to local preferences and local caches.

3. **Treat governance as mandatory**  
   - The backend enforces policy; the UI must *display* and *respect* it.  
   - The UI must never “undo” masking or downgrade sensitivity labels.

4. **Be provenance-first**  
   - Every narrative summary, dataset preview, and derived output must be linkable back to source metadata (STAC/DCAT/PROV and/or governed ledgers).

5. **Be accessibility-first**  
   - WCAG 2.1 AA+ compliance is a baseline requirement, not a feature request.

6. **Emit telemetry safely**  
   - Telemetry is schema-validated, aggregated, and must exclude PII.

### 3. Audience

This document is written for:

- Frontend engineers maintaining `web/**`
- Backend/API engineers owning the contracts the UI consumes
- FAIR+CARE and sovereignty reviewers verifying UI enforcement patterns
- QA/a11y reviewers validating user journeys
- Observability/sustainability reviewers validating telemetry integrity

---

## 🗂️ Directory Layout

The directory layout below is treated as the **public contract** for `web/**`.  
Any structural change must be reflected here **and** in `web/README.md`.

~~~text
web/
├── 📄 README.md                      # Web platform overview (behavioral contract)
├── 📄 ARCHITECTURE.md                # This architecture spec (governed)
├── 📦 package.json                   # Frontend dependencies & scripts
├── 📦 package-lock.json              # Deterministic dependency lock
├── ⚙️ vite.config.ts                 # Build configuration (Vite)
│
├── 📁 public/                        # Static assets (publicly served)
│   ├── 📄 index.html                 # HTML entrypoint
│   ├── 🧾 manifest.json              # PWA manifest (if enabled)
│   ├── 📁 icons/                     # Favicons/app icons
│   └── 📁 images/                    # Screenshots, logos, non-sensitive imagery
│
└── 📁 src/                           # React/TypeScript SPA
    ├── 📄 main.tsx                   # SPA bootstrap
    ├── 📄 App.tsx                    # Root router/layout composition
    ├── 📁 components/                # UI components (map/timeline/focus/story/governance)
    ├── 📁 pages/                     # Route-level containers (Explore/Focus/About/etc.)
    ├── 📁 hooks/                     # Shared hooks (time/map/focus/catalog/telemetry)
    ├── 📁 context/                   # State providers (Time/Focus/Governance/A11y/Theme)
    ├── 📁 services/                  # API clients (REST/GraphQL/JSON-LD/STAC/DCAT/OTel)
    ├── 📁 utils/                     # Helpers (formatting, schema helpers, adapters)
    └── 📁 styles/                    # CSS + design-token consumption (themes, map styles)
~~~

Cross-repo dependencies that the web architecture expects to remain stable include:

- `schemas/**` for JSON/SHACL/telemetry validation (consumed by CI and tooling)
- `src/design-tokens/**` and `src/theming/**` for shared tokens/themes (single source of truth)
- `releases/**` for SBOM/manifests/telemetry/attestations for certified releases

---

## 🧭 Context

### 1. Pipeline alignment

The web application is the final presentation layer in the KFM flow:

ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/MapLibre/Cesium UI → Story Nodes / Focus Mode

The frontend must assume that:

- **catalogs and APIs are the contract surface**, not raw stores
- **governance is enforced upstream**, and must be rendered faithfully downstream

### 2. Deployment and trust model

The web frontend is typically deployed as static assets served by a web server or static host, and loads data via:

- Approved API endpoints (REST/GraphQL/JSON-LD)
- Governed catalogs (STAC/DCAT), either via catalog traversal or an API façade

Because the web app is a **public entrypoint**, it must be designed so that:

- sensitive content is already generalized/redacted by the time it reaches the browser
- any sensitive behavior is blocked server-side, and explained UI-side

### 3. Governance boundaries

The UI is responsible for **showing**:

- CARE labels and risk categories
- sovereignty indicators (when present)
- masking/generalization notices (when enforced)
- provenance links (dataset/story/entity/source chains)
- clear differentiation between:
  - archival/human-curated narrative
  - derived/model output
  - AI-generated summaries

The UI is *not* responsible for deciding policy outcomes. It consumes them.

---

## 🗺️ Diagrams

### 1. System integration overview (frontend perspective)

~~~mermaid
flowchart TD
  UI["Web UI (React/TS)"] --> R2D["2D Map (MapLibre)"]
  UI --> R3D["3D View (Cesium)"]
  UI --> TL["Timeline + Filters"]
  UI --> SN["Story Nodes"]
  UI --> FM["Focus Mode UI"]

  UI --> CL["Catalog Clients (STAC/DCAT/JSON-LD)"]
  UI --> API["API Clients (REST/GraphQL)"]
  UI --> TEL["Telemetry Client (OTel)"]

  CL --> CAT["Catalog Services (STAC/DCAT)"]
  API --> SVC["Backend Services (Governed)"]
  SVC --> KG["Knowledge Graph (Neo4j)"]
  SVC --> LED["Governance Ledgers (FAIR+CARE / SBOM / SLSA)"]
  TEL --> TELSVC["Telemetry Backend (Aggregated)"]
~~~

Key interpretation:

- The web UI aggregates *multiple governed sources* (APIs + catalogs) into a single experience.
- Governance and redaction decisions are treated as authoritative, and shown in-context.

### 2. UI synchronization (time, story, focus, map)

~~~mermaid
flowchart LR
  Time["TimeContext"] -->|filters| Map["MapView"]
  Time -->|filters| Cesium["CesiumView"]
  Time -->|filters| Story["StoryNodeBrowser"]
  Time -->|filters| Layers["LayerExplorer (STAC/DCAT)"]
  Time -->|filters| Focus["FocusPanel"]

  Story -->|select| Time
  Story -->|select| Map
  Story -->|select| Focus

  Map -->|select feature| Focus
  Map -->|select feature| Story

  Focus -->|highlight| Map
  Focus -->|highlight| Story
  Focus -->|highlight| Layers
~~~

Key interpretation:

- Synchronization MUST occur through state providers (contexts/stores), not ad-hoc cross-component coupling.
- Governance can constrain the propagation (e.g., selection allowed, but coordinates generalized).

---

## 🧱 Architecture

### 1. Layered frontend architecture

The web application is organized into explicitly bounded layers:

1. **Rendering layer**  
   - MapLibre (2D), Cesium (3D), timeline widgets, charts, overlays

2. **Narrative layer**  
   - Story Node cards and detail views; narrative layouts synchronized to map/time

3. **Focus layer**  
   - Focus Mode entry/exit flows; explainability controls; evidence previews (where allowed)

4. **State layer**  
   - Predictable, testable state containers:
     - `TimeContext` (time filters, brushes)
     - `FocusContext` (focused entity/story, focus state)
     - `GovernanceContext` (labels, masking flags, allowed views)
     - `A11yContext` (reduced motion, contrast, font scaling)
     - `ThemeContext` (tokens/themes, map styles)

5. **Integration layer**  
   - Typed clients for REST/GraphQL/JSON-LD/STAC/DCAT
   - Request lifecycle control (cancellation, retry rules, backoff)

6. **Governance layer**  
   - UI overlays and interaction constraints that reflect the policy state returned by backend/catalogs

7. **Telemetry layer**  
   - OpenTelemetry spans and event emission with schema constraints

### 2. Declarative configuration over imperative wiring

Architectural preference order:

1. **Declarative registries** (layers, modes, feature flags, policy surfaces)
2. **Schema-validated configuration** (JSON/YAML validated in CI)
3. **Typed adapters** (normalize API/cat data into UI models)
4. **Components that render models** (pure UI logic)

Avoid:

- hand-wiring map layers directly inside UI components without registry/config
- “magic” UI behavior that is not driven by state + configuration

### 3. Rendering pipelines

#### 3.1 2D (MapLibre) rendering responsibilities

- Render base cartography and dataset overlays
- Render Story Node geometries (Point/Line/Polygon/Multi*)
- Render generalized geometry / H3-style aggregation when required
- Reflect time filtering via shared `TimeContext`
- Provide accessible alternatives (keyboard navigation, focus cues, textual summaries)

#### 3.2 3D (Cesium) rendering responsibilities

- Render terrain and time-aware features
- Support “deep-time” narratives that combine camera motion + timeline context
- Respect reduced motion preferences (disable or minimize camera fly-throughs)
- Obey governance constraints (do not show restricted detail even in 3D)

### 4. Reliability and error isolation

- Use error boundaries at route and major subsystem levels (Map/3D/Focus/Catalog)
- Prefer graceful degradation:
  - “map available but focus unavailable” must remain functional
  - “catalog offline” must preserve core navigation and explain the failure
- All errors that could affect governance interpretation must have:
  - a user-facing safe message
  - a telemetry record (aggregated, non-PII)

### 5. URL state and shareable views

Where implemented, URL state is the preferred mechanism for reproducible views:

- time range(s)
- map camera (center/zoom/bearing/pitch where allowed)
- selected story node / focus entity ID
- selected layer set (governed)

URL state MUST not encode sensitive coordinates, restricted identifiers, or anything disallowed by policy.

---

## 🧠 Story Node & Focus Mode Integration

### 1. Story Node v3 rendering contract

Story Nodes are the primary narrative unit. The UI must treat Story Nodes as:

- **schema-validated content**
- **governance-bearing objects** (labels, masking flags, permissions)
- **linkable across time and space** (geometry + time range)

Recommended UI surfaces:

- **StoryNodeCard**  
  - title, summary, time range, place(s), governance badges

- **StoryNodeDetail**  
  - full narrative sections, referenced entities, dataset links
  - map/timeline synchronization controls
  - provenance panel (sources, dataset IDs, lineage references)

Selection effects (subject to governance):

- StoryNode selection updates:
  - Map highlight (generalized if required)
  - Timeline focus/brush
  - Optional Focus Mode entry context (if the workflow enables it)

### 2. Focus Mode v3 interaction sequence

Focus Mode is the governed “deep dive” surface. A canonical Focus Mode session typically:

1. The user activates Focus Mode from a Story Node, map selection, or entity search.
2. The backend returns a **governed context bundle**:
   - entity neighborhood (graph context, bounded)
   - linked story nodes
   - relevant datasets (STAC/DCAT links)
   - governance metadata and masking flags
   - AI-generated narrative (when permitted), including provenance references
3. The UI updates multiple surfaces:
   - map zoom/highlight to relevant region (generalized if required)
   - timeline jumps to relevant interval(s)
   - relevant layers toggle on/off (via declarative registry rules)
   - narrative panel shows summary with citations and an “AI explanation” affordance
   - audit/governance panel shows masking notices when applicable

Focus Mode may temporarily constrain certain interactions to preserve context (e.g., limiting layer toggles or map exploration when a locked narrative sequence is active).

### 3. Provenance and evidence surfaces

The UI must provide a consistent way to answer:

- “Where did this come from?”
- “Why am I seeing this?”
- “What is masked, and why?”

Recommended standard components:

- **ProvenanceChip**: compact references to STAC/DCAT/PROV/ledger IDs
- **GovernanceBadge**: CARE label + sensitivity/masking state
- **ExplainabilityToggle**: separates human narrative vs AI summary vs derived/model output
- **EvidencePanel** (when allowed): renders linked assets from catalog items (images, plots, documents) with captions and provenance

Evidence rendering must be opt-in when content sensitivity requires it, and must never bypass policy controls.

### 4. AI transform guardrails in the UI

The web app must enforce and communicate AI constraints:

- The UI displays AI output as “AI-generated” and keeps human-curated content visually distinct.
- The UI must not rewrite narrative text locally.
- The UI must not “fill in gaps” or expand claims beyond what the backend returns.
- Allowed transforms in this document context are restricted to:
  - summaries, timeline generation, semantic highlighting, 3D context render, a11y adaptations, diagram/metadata extraction, layout normalization

---

## 📦 Data & Metadata

### 1. Web-consumed data sources

The web architecture assumes the UI will consume:

- **Catalog metadata**
  - STAC Collections/Items (spatiotemporal assets)
  - DCAT Dataset records (dataset-level metadata views)
  - PROV-aligned lineage references (where exposed)

- **API responses**
  - entity search results and entity detail payloads
  - story node indexes and story node details
  - Focus Mode context bundles and narratives
  - governance policy state (labels, masking, access rules)

- **Telemetry**
  - client-side performance and interaction summaries (OTel)
  - schema-validated aggregated export into versioned release telemetry artifacts

### 2. Schema validation and adapters

UI integration must be schema-first:

- Normalize and validate inputs at the edge of the app (service/adapters), not inside rendering components.
- Reject or quarantine invalid payloads:
  - fail safely in UI
  - emit a telemetry error event (non-PII)
  - never render partial payloads that could misrepresent governance state

### 3. Caching and pagination

Data-heavy surfaces (catalog browsing, entity exploration) should:

- paginate in the API layer (cursor/page tokens)
- cache responses cautiously (time-bounded, invalidation-aware)
- cancel in-flight requests on route/filter changes to protect the browser main thread

### 4. Sensitive-data handling

The UI must assume that:

- sensitive coordinates are generalized/redacted upstream
- any “precise location” rendering must be explicitly permitted by policy

UI must also:

- display masking notices when geometry has been generalized
- avoid exposing raw coordinates in the DOM when masking is active (including tooltips, debug overlays, URL state)

---

## 🌐 STAC, DCAT & PROV Alignment

### 1. STAC (KFM-STAC v11) alignment

The web client should support:

- browsing collections and items
- filtering by:
  - time (datetime / range)
  - space (bbox / map viewport)
  - keywords/themes (where present)
  - license/access constraints (surfaced from metadata)
- previewing assets in map/3D where allowed (tiles, vectors, rasters, derived artifacts)

UI expectations for STAC-driven previews:

- every preview must show:
  - a provenance pointer (collection/item ID)
  - licensing/attribution surfaces
  - governance badges when applicable

### 2. DCAT (KFM-DCAT v11) alignment

DCAT views are dataset-centric and must make it easy to answer:

- What is this dataset?
- Who published/stewards it?
- Under what license can it be used?
- What is its temporal/spatial coverage?
- Where are its distributions / access methods?
- What governance labels apply?

### 3. PROV-O alignment

Where lineage is exposed (directly or via references), the UI should present:

- upstream source chain (prov:Entity)
- processing steps (prov:Activity)
- responsible agents/systems (prov:Agent)
- versioning identifiers (run IDs, dataset IDs, release IDs) where present

Lineage should be readable at multiple depths:

- a compact summary for most users
- an expandable detailed view for auditors/researchers

---

## ⚖ FAIR+CARE & Governance

### 1. Governance overlay requirements

The web UI must render governance information as a first-class layer:

- CARE label and sensitivity level
- sovereignty indicators (when present)
- masking/generalization notices
- “why is this limited?” explanations
- separation of human vs AI vs derived/model outputs

Governance overlays must be:

- visible on Story Nodes
- visible on dataset previews (STAC/DCAT)
- visible on Focus Mode narratives and evidence panels
- visible (where relevant) on map/3D features

### 2. Sovereignty and cultural sensitivity

When sovereignty policy applies:

- do not expose restricted detail
- prefer generalization (region/county/aggregation) over precise points
- provide clear notices without revealing the protected information
- ensure UI patterns are consistent across map, narrative, and metadata views

### 3. Accessibility as governance

Accessibility is an enforced requirement:

- full keyboard navigation across the app
- map/3D affordances that have accessible alternatives (textual summaries, landmark structure)
- reduced motion support for 3D camera transitions and timeline animations
- no color-only encodings for governance states (use iconography and text)

### 4. Telemetry governance

Telemetry MUST:

- exclude PII and identifiers that can re-identify users
- avoid capturing raw map coordinates when masking is active
- validate against the declared telemetry schema
- remain aggregated at export time into release artifacts

---

## 🧪 Validation & CI/CD

### 1. CI-enforced checks

Changes under `web/**` are expected to pass:

- Type checks and build validation
- Unit tests (components, hooks, reducers, adapters)
- Integration tests (map–timeline–story–focus synchronization)
- E2E tests (canonical user journeys)
- Accessibility audits (automated + targeted manual verification)
- Schema validation (telemetry and configuration)
- Diagram checks (Mermaid validity)
- Secret scanning and PII scanning
- Provenance and metadata checks for governed content surfaces

### 2. Branching and release expectations

- Development work integrates on `develop`, then merges to `main` after CI and review.
- Certified artifacts are stored under `releases/<version>/` (SBOM, manifests, telemetry exports, signatures/attestations).
- Architecture changes that affect governance surfaces require FAIR+CARE review in addition to engineering review.

### 3. PR checklist (web architecture changes)

Before requesting review:

- Update `web/README.md` if user-visible behavior changes.
- Update `web/ARCHITECTURE.md` if architectural boundaries or contracts change.
- Confirm schema validation for any new/changed registries or telemetry events.
- Confirm A11y checks for modified user flows (Explore → Focus → Story Node → Catalog).
- Confirm no UI path bypasses backend governance.

---

## 🕰️ Version History

| Version  | Date       | Summary |
|---------:|------------|---------|
| v11.2.6  | 2025-12-15 | Aligned to KFM-MDP v11.2.6 (approved H2 registry, purpose block, governance footer links, fencing profile). Expanded architectural detail for state synchronization, declarative configuration, Focus Mode/Story Node flows, and CI validation expectations. |
| v11.2.2  | 2025-11-30 | Upgraded to KFM-MDP v11.2.2; added signature/attestation, energy/carbon v2, AI transform constraints, alignment with web/README.md. |
| v11.0.0  | 2025-11-24 | Initial v11 web architecture; Focus Mode v3, Story Node v3, STAC/DCAT explorer introduced. |
| v10.4.0  | 2025-11-15 | v10.4 upgrades; rendering and narrative pipeline improvements. |
| v10.3.2  | 2025-11-14 | Cesium integration; STAC/DCAT explorer refinements. |
| v10.0.0  | 2025-11-09 | Initial web architecture baseline. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
[⬅️ Back to Web README](README.md) · [⬅️ Repo Root](../README.md) · [🧭 System Architecture](../ARCHITECTURE.md) · [🛡 Governance](../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>