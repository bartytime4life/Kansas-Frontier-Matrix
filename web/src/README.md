---
title: "KFM Web UI Source README"
path: "web/src/README.md"
version: "v1.0.0"
last_updated: "2025-12-21"
status: "draft"
doc_kind: "Guide"
license: "CC-BY-4.0"

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
care_label: "TBD"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:web:src:readme:v1.0.0"
semantic_document_id: "kfm-web-src-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:src:readme:v1.0.0"
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

# KFM Web UI Source README

## 📘 Overview

### Purpose
- This README documents what belongs in `web/src/` and how frontend work stays architecture-synced to KFM’s pipeline: **API boundary → UI → Story Nodes → Focus Mode**.
- It defines the frontend-side invariants for:
  - contract-bound data access
  - provenance and citation rendering
  - Focus Mode behavior expectations

### Scope
| In Scope | Out of Scope |
|---|---|
| Runtime UI code under `web/src/` (React components, map UI, state, API clients, Story Node rendering, Focus Mode UX, frontend tests) | ETL/pipelines, catalog generation, graph ingest, server implementation, infrastructure/deployments |
| UI layer registry consumption and validation behavior | Authoring Story Nodes themselves (lives under `docs/reports/story_nodes/`) |

### Audience
- Primary: Frontend engineers working in `web/` and `web/src/`.
- Secondary: API engineers validating contracts, reviewers checking audit/provenance UX, and governance/security reviewers.

### Definitions
- Glossary link: `docs/glossary.md` (not confirmed in repo)

Terms used in this doc:
- **API boundary**: server layer under `src/server/` that enforces redaction/generalization and exposes contracted data to the UI.
- **Story Node**: a governed narrative bundle (Markdown + assets + citations), canonical home `docs/reports/story_nodes/`.
- **Focus Mode**: an immersive view over a single story/entity that must remain provenance-linked only.
- **Provenance**: links back to STAC/DCAT/PROV identifiers (and/or document IDs) supporting claims.
- **Layer registry**: declarative map layer catalog used by the UI (schema-validated if `schemas/ui/` exists).

### Key artifacts
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide v12 | `docs/MASTER_GUIDE_v12.md` | Docs | Canonical pipeline ordering + UI invariants |
| Redesign Blueprint v13 | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Docs | Canonical homes for stages; drift notes |
| Story Node Template v3 | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Docs | Story Node structure; optional Focus controls |
| Universal Doc Template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs | Governing Markdown template used here |
| API code + contracts | `src/server/` + `src/server/contracts/` | API | UI must stay contract-bound |
| UI schemas | `schemas/ui/` | Schemas | Layer registry validation (not confirmed in repo) |
| Story Nodes | `docs/reports/story_nodes/` | Content | Draft/published story bundles + assets |

### Definition of done
- [ ] Front-matter complete + valid; `path` matches actual file path
- [ ] README aligns with Master Guide + Blueprint stage boundaries
- [ ] UI work described here honors API boundary and redaction/generalization rules
- [ ] Story Node citations in `【…】` syntax are renderable + auditable in UI
- [ ] Focus Mode rules are stated and enforceable from UI behavior
- [ ] Validation steps are repeatable (replace placeholders with repo commands)

## 🗂️ Directory Layout

### This document
- `path`: `web/src/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Frontend root | `web/` | Web app root (tooling/config + static assets) |
| Frontend source | `web/src/` | React/map UI source code |
| API boundary | `src/server/` | Query + redaction/generalization + contracted responses |
| Contracts | `src/server/contracts/` | OpenAPI/GraphQL contracts + tests |
| Story Nodes | `docs/reports/story_nodes/` | Story templates, drafts, published stories, assets |
| UI schemas | `schemas/ui/` | UI registry schemas (not confirmed in repo) |
| Evidence catalogs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | Evidence artifacts consumed by API/UI |
| Governance | `docs/governance/` | Ethics + sovereignty + review gates |

### Expected tree for `web/src`
This tree is a recommended shape. Update it to match the actual repository layout.

~~~text
📁 web/
├── 📁 src/
│   ├── 📁 app/                  # app shell, routing, providers (not confirmed in repo)
│   ├── 📁 components/           # shared UI components
│   ├── 📁 features/             # feature bundles (Focus Mode, Search, Layers)
│   ├── 📁 map/                  # MapLibre/Cesium wrappers + layer adapters
│   ├── 📁 services/             # API clients (contract-bound)
│   ├── 📁 state/                # state management (not confirmed in repo)
│   ├── 📁 styles/               # design tokens + globals
│   ├── 📁 utils/                # helpers (e.g., citation parsing)
│   ├── 📁 test/                 # fixtures + test helpers
│   └── 📄 README.md             # this file
└── 📄 package.json              # not confirmed in repo
~~~

## 🧱 Frontend invariants

### API boundary is mandatory
- The UI **must not** read Neo4j (or any graph DB) directly.
- The UI **must** consume graph and evidence through API endpoints under `src/server/` and/or catalog endpoints surfaced by the API.

### Provenance and citation rendering
- Story Nodes are Markdown and include citations in the `【…】` family of syntax.
- The UI must render citations as “audit affordances”:
  - clickable/hoverable citation chips, footnotes, or a Sources panel
  - a clear way to view “what evidence supports this claim”
- If content lacks required provenance, the UI should show a warning and avoid presenting it as fact.

### Focus Mode rules
- Focus Mode is an immersive view over one story/entity:
  - map zooms to relevant region
  - timeline narrows to relevant time window
  - side panel shows narrative + sources
- Focus Mode must only present provenance-linked content.
- Any AI-generated or predictive content must be:
  - clearly labeled
  - opt-in
  - accompanied by uncertainty/confidence metadata

### Layer registry driven UI
- Layers shown in the UI should come from a registry configuration, not ad-hoc hardcoding inside components.
- Registry entries should validate against `schemas/ui/` if schemas exist.

### Sensitivity and sovereignty
- Never infer or “complete” sensitive locations in the UI.
- Respect redaction and generalization behaviors from the API boundary.
- Avoid UI affordances that help users triangulate restricted knowledge.

### Accessibility
- Focus Mode and map controls should be keyboard accessible and screen-reader friendly.
- Ensure citation interactions (tooltips/popovers/panels) are accessible.

## ✅ Extension points checklist

- [ ] UI: add/modify a layer registry entry and validate it
- [ ] UI: add/modify Story Node renderer and citation handling
- [ ] UI: add Focus Mode behavior for a new entity type
- [ ] API: add/extend an endpoint and update contracts (required if UI needs new fields)
- [ ] Security: confirm redaction/generalization and “no leakage” behavior
- [ ] Focus Mode: provenance rules enforced and AI content remains opt-in
- [ ] Telemetry: add signals + schema version bump if telemetry is governed (not confirmed in repo)

## 🧠 Story Node and Focus Mode integration

### How this work surfaces in Focus Mode
- Map markers, search results, and entity pages can trigger Focus Mode.
- Focus Mode should load:
  - Story Node Markdown
  - referenced assets (images/audio/video if present)
  - a structured provenance bundle (if provided by API)

### Provenance-linked narrative rule
- Every factual claim shown to the user must trace to a dataset / record / asset ID.

### Optional structured controls
These hints may be returned by the API or embedded in Story Node content.

~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation and CI/CD

### Validation steps
- [ ] Frontend lint and type checks (not confirmed in repo)
- [ ] Unit tests for:
  - citation parsing/rendering
  - Focus Mode state transitions
  - layer registry parsing
- [ ] Contract alignment checks:
  - UI requests match OpenAPI/GraphQL
  - required provenance fields present
- [ ] UI schema checks for layer registry (if `schemas/ui/` exists)
- [ ] Accessibility checks for Focus Mode and citation interactions
- [ ] Security and sovereignty checks for restricted layers and generalization behavior

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands from web/package.json

# install dependencies
# (npm|pnpm|yarn) install

# run dev server
# (npm|pnpm|yarn) run dev

# run unit tests
# (npm|pnpm|yarn) test

# lint / typecheck
# (npm|pnpm|yarn) run lint
# (npm|pnpm|yarn) run typecheck

# build
# (npm|pnpm|yarn) run build
~~~

### Telemetry signals
| Signal | Source | Where recorded |
|---|---|---|
| focus_mode_entered | UI | `schemas/telemetry/` + telemetry pipeline (not confirmed in repo) |
| citation_opened | UI | `schemas/telemetry/` + telemetry pipeline (not confirmed in repo) |
| layer_toggled | UI | `schemas/telemetry/` + telemetry pipeline (not confirmed in repo) |
| api_error | UI error boundary | `schemas/telemetry/` + telemetry pipeline (not confirmed in repo) |

## ⚖ FAIR+CARE and governance

### Review gates
- Any change that can expose new data in the UI requires review, especially:
  - adding new layers
  - changing redaction/generalization handling
  - adding new story node rendering modes (e.g., richer excerpts)
  - adding AI explanation content surfaces

### CARE and sovereignty considerations
- Identify communities impacted by new UI features or content surfaces.
- Do not add UI affordances that encourage discovery of restricted or culturally sensitive locations.

### AI usage constraints
- This document prohibits:
  - `generate_policy`
  - `infer_sensitive_locations`
- Any AI-facing UI features must remain opt-in and clearly labeled.

## 🕰️ Version history
| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-21 | Initial README for `web/src` | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
