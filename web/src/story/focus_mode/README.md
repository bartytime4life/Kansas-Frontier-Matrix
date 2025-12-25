---
title: "Focus Mode — UI README"
path: "web/src/story/focus_mode/README.md"
version: "v0.1.0-draft"
last_updated: "2025-12-25"
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

doc_uuid: "urn:kfm:doc:web:story:focus-mode:readme:v0.1.0-draft"
semantic_document_id: "kfm-web-story-focus-mode-readme-v0.1.0-draft"
event_source_id: "ledger:kfm:doc:web:story:focus-mode:readme:v0.1.0-draft"
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

# Focus Mode — UI README

## 📘 Overview

### Purpose

Focus Mode is the **deep-dive narrative + map + timeline** experience in KFM’s UI. It “immerses the user in a specific story or analysis, showing the narrative alongside maps/timelines.” In **Focus Mode v3**, the UI must enforce two rules:

- **Provenance-linked only:** everything displayed must be traceable to a dataset/record/asset identifier (no orphan facts).
- **AI labeling:** any AI-generated elements must be clearly indicated as such.

These requirements are treated as **system invariants**, not optional UX features.

### Scope

| In Scope | Out of Scope |
|---|---|
| Focus Mode UI composition and routing | ETL, catalog generation, graph ingest |
| Consuming **contracted APIs** to retrieve Focus Mode context | Direct queries to Neo4j from the browser |
| Rendering story narrative, citations, and provenance panels | Writing or publishing Story Nodes |
| Applying story-provided “focus hints” to map/time/layers | Defining new API endpoints (belongs under `src/server/`) |
| Respecting redaction / generalization flags from APIs | Circumventing governance or sovereignty rules |

### Audience

- **Primary:** Frontend contributors working in `web/` (map UI, narrative UI, Focus Mode UX).
- **Secondary:** Narrative curators validating Story Nodes; API engineers owning the Focus Mode context endpoint; reviewers enforcing governance constraints.

### Definitions

- Glossary: `docs/glossary.md` (not confirmed in repo).
- Terms used here:
  - **Story Node:** curated narrative document that must include citations and evidence IDs.
  - **Focus Mode:** UI view that renders a Story Node and its context in map/timeline form.
  - **Context bundle:** API payload that packages narrative + evidence + entity references for Focus Mode.
  - **Provenance:** traceable linkage to STAC/DCAT/PROV and other governed artifacts.
  - **Redaction:** intentional suppression or generalization of sensitive data.

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Canonical pipeline ordering + invariants | `docs/MASTER_GUIDE_v12.md` | KFM Core | Pipeline ends in Story Nodes → Focus Mode |
| Focus Mode requirements and v13 roadmap | `docs/architecture/KFM_NEXT_STAGES_BLUEPRINT.md` | Arch | Defines Focus Mode v3 rule set |
| Contract-first canonical homes and story node location | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Arch | UI is `web/`, Story Nodes are `docs/reports/story_nodes/` |
| Story Node authoring standard | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Narrative | Includes optional Focus Mode controls |
| Governed doc template baseline | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs | This README follows the universal structure |
| API contracts | `src/server/contracts/**` (or repo-defined equivalent) | API | Focus Mode must consume contracts, not ad-hoc JSON |
| UI schemas | `schemas/ui/**` (v13 target; not confirmed in repo) | Frontend/Platform | Layer registry and other UI contracts |
| Story Nodes canonical home | `docs/reports/story_nodes/` | Narrative | Draft/published workflow; may require migration if drift exists |

### Definition of done

- [ ] Front-matter complete and `path` matches file location
- [ ] Focus Mode invariants are explicit (no direct graph reads, provenance-only narrative, AI labeling)
- [ ] Cross-links point to canonical docs/contracts (or marked “not confirmed in repo”)
- [ ] Validation steps are actionable and repeatable

## 🗂️ Directory Layout

### This document

- `path`: `web/src/story/focus_mode/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| UI | `web/` | Map UI, Focus Mode UI, citation rendering |
| API boundary | `src/server/` | Contract-first APIs, redaction, query services |
| Story Nodes | `docs/reports/story_nodes/` | Draft and published Story Nodes consumed by Focus Mode |
| Schemas | `schemas/` | Validation schemas for story nodes + UI registries (v13 target) |
| Catalog outputs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | Evidence and provenance consumed downstream |

### Suggested subtree

This is a **recommended** organization for this folder. Some paths may be **not confirmed in repo** yet and should be aligned to the actual `web/` structure when implemented.

~~~text
📁 web/
└─ 📁 src/
   └─ 📁 story/
      └─ 📁 focus_mode/
         ├─ 📄 README.md
         ├─ 📄 FocusMode.tsx                 (not confirmed in repo)
         ├─ 📁 components/                   (not confirmed in repo)
         │  ├─ 📄 NarrativePanel.tsx
         │  ├─ 📄 ProvenancePanel.tsx
         │  ├─ 📄 TimelinePanel.tsx
         │  ├─ 📄 LayerControls.tsx
         │  └─ 📄 AiInsightsPanel.tsx
         ├─ 📁 api/                          (not confirmed in repo)
         │  ├─ 📄 focusModeClient.ts
         │  └─ 📄 types.generated.ts         (from API contracts)
         ├─ 📁 state/                        (not confirmed in repo)
         │  ├─ 📄 focusModeStore.ts
         │  └─ 📄 selectors.ts
         ├─ 📁 utils/                        (not confirmed in repo)
         │  ├─ 📄 citations.ts
         │  └─ 📄 redaction.ts
         └─ 📁 __tests__/                    (not confirmed in repo)
            └─ 📄 FocusMode.test.tsx
~~~

## 🔒 Core invariants

### API boundary is mandatory

The UI must **not** connect to Neo4j directly. All graph access must be mediated by contracted APIs.

### Provenance-linked narrative only

In Focus Mode v3, **all content displayed must be provenance-linked** (no unverified or orphan facts). The UI should assume the Story Node publish workflow enforces this, and it should surface provenance and citation structure prominently.

### AI output must be labeled and scoped

If AI-derived elements are presented, they must be:

- clearly labeled as AI-generated,
- linked to evidence,
- shown with uncertainty metadata when applicable,
- never presented as unqualified fact.

### Respect redaction and sovereignty controls

Focus Mode must respect sensitivity and redaction decisions enforced by upstream governance and API services. The UI should treat redaction flags as non-negotiable.

## 🧠 How Focus Mode fits the pipeline

KFM’s canonical pipeline ends in Focus Mode.

~~~mermaid
flowchart LR
  A[ETL\nsrc/pipelines/] --> B[Catalogs\nSTAC/DCAT/PROV\n data/stac/ data/catalog/dcat/ data/prov/]
  B --> C[Graph\nNeo4j\nsrc/graph/]
  C --> D[API Boundary\nsrc/server/]
  D --> E[UI\nweb/]
  E --> F[Story Nodes\n docs/reports/story_nodes/]
  F --> G[Focus Mode\nweb/src/story/focus_mode/]
~~~

## 📦 Inputs to Focus Mode

Focus Mode should be treated as a **consumer** of a single “context bundle” returned by the API boundary. The exact payload shape must be defined in API contracts.

Conceptually, a Focus Mode context bundle should include:

- **Story Node content** (renderable narrative, typically Markdown)
- **Citations** and evidence references (dataset IDs, STAC item IDs, document IDs)
- **Entity references** (stable IDs usable to fetch more context)
- **Focus hints** that the UI can apply immediately:
  - layer suggestions
  - timeline window or “focus time”
  - map center/extent
- **Redaction flags** and sensitivity labels
- **Optional AI insights** as a clearly labeled add-on

## 🎛️ Story Node Focus Mode controls

Story Nodes may include optional structured controls that Focus Mode can interpret.

Example pattern:

~~~yaml
focus_layers:
  - "example_layer:<layer-id>"
focus_time: "1861-01-01T00:00:00Z"
focus_center: [-98.0000, 38.0000]
~~~

If these fields are absent, Focus Mode should fall back to a safe default behavior:

- default map viewport (Kansas-wide)
- default timeline window (story-wide or evidence-wide)
- no forced layers beyond baseline

## 🧩 Rendering responsibilities

### Narrative rendering

- Render Story Node narrative as **readable, accessible text**.
- Citations must be rendered in a way that supports:
  - quick “open evidence” actions,
  - provenance inspection,
  - user trust (don’t hide references).

### Provenance panel

Provide a dedicated panel that surfaces:

- evidence IDs,
- dataset IDs,
- provenance lineage pointers (STAC/DCAT/PROV),
- any validation warnings provided by upstream services.

### Map and timeline coordination

- Timeline interactions should update map layers and filters when supported by contracts.
- Map interactions should never bypass narrative provenance controls.

## ✅ Validation and testing

Recommended checks for changes in this folder:

- Markdown protocol check for this README
- No secrets in client code or docs
- No client dependencies that connect directly to Neo4j
- Contract typing: Focus Mode uses generated/validated types, not ad-hoc JSON
- If Story Node rendering changes: ensure citation rendering remains correct
- If layer controls change: ensure UI registry schema validation remains satisfied

Example placeholders:

~~~bash
# Replace with repo tooling (not confirmed in repo)

# 1) Lint / typecheck UI
# npm run lint
# npm run typecheck

# 2) Run tests
# npm test

# 3) Validate story nodes / UI schemas (if validators exist)
# make validate-story-nodes
# make validate-ui-schemas
~~~

## ⚖ FAIR+CARE and governance

Changes to Focus Mode should trigger extra review when they involve:

- new UI features that could reveal sensitive locations via interaction/zoom
- changes to citation/provenance handling
- introduction or expansion of AI-generated narrative behaviors
- changes that affect how redaction/generalization is displayed

AI usage constraints for this document are defined in front-matter:
- Allowed: summarize, structure extraction, translation, keyword indexing
- Prohibited: generating new policy, inferring sensitive locations

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v0.1.0-draft | 2025-12-25 | Initial Focus Mode README scaffold | (you) |

---

## Footer refs

- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Next Stages Blueprint: `docs/architecture/KFM_NEXT_STAGES_BLUEPRINT.md`
- v13 Redesign Blueprint: `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Universal template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
---

