---
title: "🌐 Kansas Frontier Matrix — Web Application Architecture (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/ARCHITECTURE.md"
version: "v10.4.0"
last_updated: "2025-11-15"
review_cycle: "Quarterly / Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../releases/v10.4.0/manifest.zip"
telemetry_ref: "../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../schemas/telemetry/web-architecture-v3.json"
governance_ref: "../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Architecture"
intent: "web-platform"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
sensitivity_level: "None"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false
provenance_chain:
  - "web/ARCHITECTURE.md@v10.0.0"
  - "web/ARCHITECTURE.md@v10.3.2"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E31 Document"
  schema_org: "WebApplication"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"
json_schema_ref: "../schemas/json/web-architecture.schema.json"
shape_schema_ref: "../schemas/shacl/web-architecture-shape.ttl"
doc_uuid: "urn:kfm:doc:web-architecture-v10.4.0"
semantic_document_id: "kfm-doc-web-architecture"
event_source_id: "ledger:web/ARCHITECTURE.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative additions"
  - "unverified historical claims"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Public Document"
role: "architecture"
lifecycle_stage: "stable"
ttl_policy: "Review required every 12 months"
sunset_policy: "Superseded upon next major KFM web platform protocol release"
---

<div align="center">

# 🌐 **Kansas Frontier Matrix — Web Application Architecture**  
`web/ARCHITECTURE.md`

**Purpose:**  
Define the *complete, FAIR+CARE-governed* web application architecture for the Kansas Frontier Matrix (KFM) — covering 2D/3D rendering pipelines, React UI composition, Focus Mode v2.5 interfaces, Story Node v3 rendering, STAC/DCAT metadata exploration, provenance surfaces, governance overlays, WCAG 2.1 AA accessibility, telemetry instrumentation, and integration with the KFM API, Knowledge Graph, and Ops Plane.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../docs/README.md)  
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../LICENSE)  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../docs/standards/faircare.md)  
[![Status: Enforced](https://img.shields.io/badge/Status-Enforced-success)](../docs/standards/governance/ROOT-GOVERNANCE.md)  
[![A11y](https://img.shields.io/badge/Accessibility-WCAG%202.1%20AA-blueviolet)]()

</div>

---

# 📘 Overview

The **KFM Web Platform** is the primary **cognitive and narrative surface** of Kansas Frontier Matrix. It binds:

- React + TypeScript + Tailwind for component layout and theming  
- MapLibre GL for 2D cartography  
- CesiumJS for 3D terrain and deep-time/future overlays  
- Focus Mode v2.5 for AI-assisted, entity-centric reasoning  
- Story Node v3 for synchronized narrative units  
- STAC/DCAT explorers for dataset discovery and previews  
- REST/GraphQL/JSON-LD clients for talking to the KFM backend and knowledge graph  
- Governance and A11y layers enforcing FAIR+CARE and WCAG 2.1 AA  

This document defines what the web app owns, which contracts it consumes, and how it cooperates with backend services described in `src/ARCHITECTURE.md`.

---

# 🎯 Purpose & Scope

## ✅ Purpose

- Serve as the **canonical architecture reference** for `web/**`.  
- Ensure the web platform remains aligned with:
  - Global architecture (`src/ARCHITECTURE.md`),
  - Reliable pipeline patterns,
  - Observability specifications,
  - KFM Markdown rules and governance policies.  
- Guide implementation of:
  - Map + timeline synchronization (2D/3D),
  - Focus Mode v2.5 flows,
  - Story Node rendering,
  - STAC/DCAT exploration,
  - Governance overlays,
  - Telemetry and accessibility.

## 📍 Scope

### In Scope

- All React SPA code under `web/src/**`:
  - Components, hooks, context, services, styles.  
- Web integration with:
  - MapLibre, Cesium, D3/Recharts, etc.  
- Client-side handling of:
  - Focus Mode payloads,
  - Story Node payloads,
  - STAC/DCAT responses,
  - Governance metadata,
  - Telemetry signals.

### Out of Scope

- ETL/AI pipeline implementation (`src/pipelines/**`).  
- Neo4j schema design and backend data modeling.  
- Cloud infrastructure and deployment primitives (Kubernetes, Terraform, etc.).

---

# 📚 Key Terms

- **Web Platform** – The React SPA built from `web/`, delivered as static assets.  
- **MapView** – Component cluster around MapLibre GL for 2D mapping.  
- **CesiumView** – Component cluster around CesiumJS for 3D globe/terrain.  
- **TimelineView** – Temporal slider plus event/Story Node markers.  
- **Focus Panel** – UI container for Focus Mode v2.5 narratives and context.  
- **Story Node Card** – Visual representation of a Story Node v3 instance.  
- **STAC Explorer** – UI for browsing STAC Collections/Items.  
- **DCAT Explorer** – UI for browsing DCAT v3 Datasets/Distributions.  
- **Governance Overlay** – Layer showing CARE labels, licenses, and provenance chips.  

---

# 🏗 High-Level Web Architecture

## 🧱 Layered Web Stack (Style B)

```mermaid
flowchart TD
  WEB[React SPA<br/>TypeScript · Tailwind]:::client
  MAP[MapView<br/>MapLibre GL]:::client
  CES[CesiumView<br/>CesiumJS 3D]:::client
  TIME[TimelineView]:::client
  FOCUS[FocusPanel<br/>Focus Mode v2 5]:::client
  STORY[StoryNodeView<br/>Story Node v3]:::client
  STACX[STAC/DCAT Explorer]:::client
  GOVUI[Governance & CARE Overlays]:::client
  A11Y[A11y Layer<br/>WCAG 2 1 AA]:::client

  API[API Client<br/>REST · GraphQL · STAC]:::client

  SVC[Backend Services<br/>FastAPI · GraphQL]:::server
  KG[Knowledge Graph<br/>Neo4j]:::server
  STACC[STAC/DCAT Catalogs]:::server
  GOVSYS[Governance Ledger]:::server
  TEL[Telemetry Ingest]:::server
  OPS[Ops Plane<br/>WAL · Retry · Rollback · Lineage]:::server

  WEB --> MAP
  WEB --> CES
  WEB --> TIME
  WEB --> FOCUS
  WEB --> STORY
  WEB --> STACX
  WEB --> GOVUI
  WEB --> A11Y

  WEB --> API
  MAP --> API
  CES --> API
  TIME --> API
  FOCUS --> API
  STORY --> API
  STACX --> API
  GOVUI --> API

  API --> SVC
  SVC --> KG
  SVC --> STACC
  SVC --> GOVSYS
  SVC --> TEL
  SVC --> OPS

  classDef client fill:#f5fbff,stroke:#2b6cb0,stroke-width:1px,color:#1a202c;
  classDef server fill:#fff7f7,stroke:#c53030,stroke-width:1px,color:#1a202c;

The web layer is pure client-side logic and visuals. It never manipulates the knowledge graph directly — only via backend APIs.

⸻

🧱 Internal Web Structure

A conventional, modular React layout is used:

web/
  README.md
  ARCHITECTURE.md
  package.json
  vite.config.ts
  public/
    index.html
    icons/
    images/
    manifest.json
  src/
    main.tsx
    App.tsx
    components/
      map/
      timeline/
      focus/
      story/
      governance/
      stac/
      layout/
    pages/
    hooks/
    context/
    services/
    utils/
    styles/

	•	components/** – presentational and container components.
	•	hooks/** – custom hooks (useMap, useTimeline, useFocus, useStac, useA11y).
	•	context/** – React Context providers (theme, time, focus, auth).
	•	services/** – HTTP, GraphQL, STAC/DCAT, telemetry clients.
	•	utils/** – formatting, guards, JSON-LD helpers, URL builders.

⸻

🔄 Map + Timeline Synchronization

🌍 MapView (2D)

Responsibilities
	•	Render basemap and overlay layers:
	•	Historical COG rasters via STAC,
	•	Vector features (places, events, Story Node footprints),
	•	Governance masks (H3-based generalization for sensitive sites).
	•	Handle panning/zooming, layer toggling, feature selection.
	•	React to:
	•	Time filter changes,
	•	Focus Mode context changes,
	•	Dataset/layer selection in the explorers.

Data Flow
	1.	MapView subscribes to TimeContext and FocusContext.
	2.	It pulls layer definitions and feature collections via hooks (useLayers, useFeatures).
	3.	When time changes, features outside the interval are dimmed or hidden.
	4.	When focus changes, relevant features are highlighted or brought to front.

⏱ TimelineView

Responsibilities
	•	Display a continuous time axis (year-based, zoom levels).
	•	Show events and Story Nodes as marks or ranges on the axis.
	•	Expose a draggable time window and scrubbing handle.

Data Flow
	1.	TimelineView receives aggregated event/Story Node metadata (start, end, weight).
	2.	User actions update TimeContext.
	3.	MapView, FocusPanel, Story Node lists rerender based on TimeContext.

⸻

📖 Story Node v3 Integration

Story Nodes are obtained via GraphQL (e.g. storyNode(id: ID!)):
	•	Each Story Node Card shows:
	•	Title and short summary.
	•	Date range and a small temporal indicator.
	•	Human-readable place labels and a micro-map preview.
	•	Chips for related entities (clickable to change focus).
	•	Optional media carousel.

Interactions
	•	Click on Story Node icon in Timeline → highlight geometry in MapView, optionally open Story detail.
	•	Click on Story Node in a Focus Panel → treat as curated narrative for the focused entity.

Requirements
	•	Story Node payloads must pass JSON Schema validation before rendering.
	•	Narrative text must be sanitized and accessible.
	•	CARE/provenance chips must be visible and clickable.

⸻

🎯 Focus Mode v2.5 (Web Side)

Focus Mode is a cross-cutting feature implemented via hooks and context.

Flow
	1.	User clicks an entity (map, list, Story Node, etc.).
	2.	useFocus sets FocusContext with target ID + type.
	3.	Focus controller calls:
	•	/api/focus/{id} (REST), or
	•	focusEntity(id: ID!) (GraphQL).
	4.	Backend returns:
	•	Core entity fields,
	•	Graph neighborhood,
	•	AI narrative and insights,
	•	CARE/provenance metadata.
	5.	FocusPanel renders:
	•	Summary,
	•	Related entities grouped by kind,
	•	Story Node suggestions,
	•	Data/asset links,
	•	Provenance overlays.

flowchart LR
  CLICK[User selects entity] --> CTRL[Focus Controller Hook]
  CTRL --> REQ[Focus API Call]
  REQ --> PAY[Focus Payload]
  PAY --> PANEL[FocusPanel UI]
  PANEL --> MAPHL[Map Highlights]
  PANEL --> TIMEHL[Timeline Highlights]
  PANEL --> STORIES[StoryNode Suggestions]

AI Transform Controls

Per front-matter:
	•	Allowed: summaries, semantic highlighting, a11y adaptations.
	•	Prohibited: speculative additions, unverified historical claims.

Web behavior:
	•	Mark low-confidence or inferred sections explicitly.
	•	Display evidence sources on hover/click (provenance chips).
	•	Avoid generating claims not grounded in returned data.

If AI fails, FocusPanel falls back to graph-derived descriptions only.

⸻

🛰 STAC/DCAT Explorer

The web app exposes:
	•	STAC Explorer
	•	Collections and Items with filters (time, area, collection ID).
	•	Footprints previewed on MapView.
	•	Asset metadata and quick links (COGs, GeoJSON, etc.).
	•	DCAT Explorer
	•	DCAT v3 Datasets with summary information.
	•	Per-dataset view showing:
	•	Title, description, publisher,
	•	Spatial/temporal extent,
	•	Distributions (often linking into STAC).

STAC/DCAT requests are handled via services in src/services/; license and provenance are rendered through Governance overlays.

⸻

🧬 Ontology & JSON-LD Alignment

The web layer supports emitting JSON-LD for:
	•	Page-level metadata (web app, section).
	•	Focused entities (as schema.org or CIDOC types).
	•	Visible datasets (as dcat:Dataset).
	•	Visible Story Nodes (as schema:CreativeWork / cidoc:E31_Document).

Utilities in src/utils/jsonld.ts build JSON-LD blocks that can be injected into <script type="application/ld+json"> tags.

⸻

🔐 Governance & CARE Overlays

Governance overlays show:
	•	CARE label (e.g. “Public / Low-Risk”).
	•	License (MIT, CC-BY, public domain).
	•	Data steward and provenance trail.

Mechanism:
	•	Info icons open a governance drawer for the currently viewed entity/dataset.
	•	The drawer reads metadata from API responses or manifests and shows:
	•	Data steward, license, source, pipeline, CARE notes.

Sensitive sites:
	•	Must be generalized (e.g. H3 r7).
	•	Must show explicit notices about generalization and rights.
	•	May require confirmation before showing any additional detail.

The web layer must not suppress or bypass CARE labels under any circumstances.

⸻

♿ Accessibility (WCAG 2.1 AA)

Accessibility is validated in CI.

Key rules:
	•	All interactive UI must be keyboard-operable and visibly focused.
	•	Text and icons must satisfy contrast requirements.
	•	ARIA roles/attributes must be correct and minimal.
	•	Motion effects must respect prefers-reduced-motion.
	•	Map and 3D components must provide textual summaries for screen readers.

Plain-language summary:

The KFM web app is designed so people with different abilities can explore Kansas history. It supports keyboard navigation, readable text, high-contrast colors, and screen readers.

⸻

📈 Telemetry & Observability

Client telemetry:
	•	Performance: WebVitals (LCP, FID, CLS, TTI).
	•	Usage: Focus activations, Story Node opens, STAC previews, layer toggles.
	•	Reliability: error events (rendering, network, narrative, A11y).

Telemetry flows:
	•	Collected via useTelemetry hook.
	•	Sent to backend endpoints that validate payloads against telemetry_schema.
	•	Aggregated by backend into release-specific JSON and observability dashboards.

Constraints:
	•	No PII is collected.
	•	Telemetry behavior must follow privacy and policy rules.

⸻

🧪 Testing & CI Integration

Required commands:
	•	npm run lint – lint/format checks.
	•	npm run test – unit/integration tests.
	•	npm run typecheck – TypeScript strict type checks.
	•	Optional: npm run test:a11y – automated a11y tests.
	•	npm run build – production build.

GitHub Actions (.github/workflows/web.yml) must:
	•	Execute these commands on PRs touching web/**.
	•	Block merges on failure (tests, types, lint, a11y, docs schema).

⸻

🧩 Error Taxonomy & Handling

Error categories:
	•	RenderingError – component-level rendering issues.
	•	DataLoadError – network/request/response problems.
	•	NarrativeError – Focus narrative fetch/generation errors.
	•	GovernanceError – missing or inconsistent CARE/provenance.
	•	A11yError – accessibility regressions.
	•	TelemetryError – telemetry send/validation issues.

Handling:
	•	Use React error boundaries for RenderingErrors.
	•	Show clear, contextual messages instead of blank views.
	•	Log errors with non-PII context to telemetry.
	•	Provide fallbacks where possible (simpler views).

⸻

🕰 Version History — Web Architecture

Version	Date	Summary
v10.4.0	2025-11-15	Upgraded to KFM-MDP v10.4; complex but safe mermaid diagram, Story Node v3 + Focus v2.5 flows, CARE/A11y/telemetry wiring.
v10.3.2	2025-11-14	Deep web architecture rebuild; Cesium integration, STAC/DCAT explorers, Focus Mode v2.5 behavior documented.
v10.3.1	2025-11-13	A11y and STAC improvements; robust map–timeline synchronization; refined component boundaries.
v10.0.0	2025-11-09	Initial v10 web subsystem; baseline React/MapLibre architecture and Focus Mode v2 introduction.


⸻


<div align="center">


© 2025 Kansas Frontier Matrix — MIT License
Validated under Master Coder Protocol (MCP-DL v6.3) · Markdown Protocol KFM-MDP v10.4
FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified
Back to Web README￼ · Root Governance Charter￼

</div>
```
