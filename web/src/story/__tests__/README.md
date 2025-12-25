---
title: "KFM Web — Story Subsystem Tests"
path: "web/src/story/__tests__/README.md"
version: "v1.0.0"
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

doc_uuid: "urn:kfm:doc:web:story:tests:readme:v1.0.0"
semantic_document_id: "kfm-web-story-tests-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:story:tests:readme:v1.0.0"
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

<div align="center">

# 🧪 **Story Subsystem Tests**

`web/src/story/__tests__/`

Evidence-first UI tests for Story Nodes + Focus Mode rendering.

</div>

---

> **Purpose (required):** Define how we test the **web Story subsystem** so it remains **contract-bound** (UI → API only), **provenance-safe** (Focus Mode shows provenance-linked content only), and **validator-friendly** (Story Nodes can be rendered without unsourced narrative).

---

## 📘 Overview

### Purpose

This README governs how tests in `web/src/story/__tests__/` should be written and organized to protect the KFM invariants:

- UI consumes **graph + catalog content through APIs** (no direct Neo4j reads).
- Focus Mode displays **provenance-linked only** narrative/context (no “orphan facts”).
- Story Node rendering respects citation syntax and (where present) Focus Mode hints.

### Scope

| In Scope | Out of Scope |
|---|---|
| Unit tests for Story Node Markdown rendering (including citation rendering) | Back-end API contract tests (live under `src/server/**`) |
| Focus Mode UI state tests (enter/exit, context bundle rendering) | Neo4j/ontology integrity tests (live under `src/graph/**` / graph test harnesses) |
| “Audit/provenance panel” expectations (presence, wiring, non-leakage) | STAC/DCAT/PROV schema validation (live under `schemas/**` + CI validators) |
| UI boundary mocking: API responses, redaction-safe fixtures | ETL determinism/provenance emission tests (live under `src/pipelines/**`) |

### Audience

- Primary: Front-end engineers working in `web/**`
- Secondary: Narrative curators validating Story Node behavior; reviewers auditing provenance/CARE risks

### Definitions

- Link: `docs/glossary.md` (**not confirmed in repo**)
- Terms used here:
  - **Story Node**: governed Markdown narrative artifact for Focus Mode.
  - **Focus Mode**: a UI view over provenance-linked context bundles.
  - **Context bundle**: the API payload that packages narrative + evidence references for Focus Mode.
  - **Provenance-linked**: every factual element maps to an evidence identifier (STAC/DCAT/PROV/Document IDs).

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide v12 | `docs/MASTER_GUIDE_v12.md` | KFM Core | Canonical pipeline + invariants |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs Team | Governed Markdown structure |
| Story Node template v3 | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Narrative Curators | Required story structure + citation rules |
| v13 redesign blueprint | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` (**not confirmed in repo**) | Arch Team | “UI → API only”; Focus Mode rules |
| Focus Mode UI guidance | `docs/...` (**not confirmed in repo**) | Web Team | Implementation expectations (audit panel, citations, map/timeline sync) |

### Definition of done (for this document)

- [ ] Front-matter complete + valid (`path` matches repo location)
- [ ] Directory layout described with canonical paths and “not confirmed in repo” markings where needed
- [ ] Test boundaries reflect the canonical pipeline (ETL → catalogs → graph → API → UI → Story Nodes → Focus Mode)
- [ ] Validation/CI expectations are actionable (placeholders clearly labeled)
- [ ] Governance/CARE/sovereignty risks for fixtures are explicitly addressed

---

## 🗂️ Directory Layout

### This document

- `path`: `web/src/story/__tests__/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| UI root | `web/` | Web application (React/Map UI, layer registry, Focus Mode) |
| Story UI code | `web/src/story/` | Story/Focus Mode components and helpers (**not confirmed in repo**) |
| API boundary | `src/server/` | API implementation (**not confirmed in repo**) |
| API contracts | `src/server/contracts/` | OpenAPI/GraphQL contracts + contract tests (**not confirmed in repo**) |
| Story Nodes | `docs/reports/story_nodes/` | Draft/published narrative artifacts |
| Schemas | `schemas/` | JSON schemas for catalogs/story/UI (**not confirmed in repo**) |

### Expected test folder shape (adjust to match the actual repo)

~~~text
📁 web/
└─ 📁 src/
   └─ 📁 story/
      └─ 📁 __tests__/
         ├─ 📄 README.md
         ├─ 📁 fixtures/                    # not confirmed in repo — recommended
         │  ├─ 📄 story-node.minimal.md     # recommended: valid citations + front-matter
         │  ├─ 📄 story-node.invalid.md     # recommended: missing/invalid citation cases
         │  └─ 📄 focus-bundle.sample.json  # recommended: mock API payloads
         ├─ 📁 helpers/                     # not confirmed in repo — recommended
         └─ 🧪 *.test.*                     # not confirmed in repo — actual pattern may differ
~~~

---

## 🧭 Context

### Why these tests exist

The KFM architecture is contract-first and provenance-bound:

- Canonical flow: **ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**.
- UI must not “invent” evidence: Focus Mode should only display provenance-linked narrative/context.
- The API boundary is responsible for enforcement (including redaction/generalization), but UI tests must ensure the UI does not bypass or weaken those guarantees.

### Guardrails this test suite should enforce

1. **No UI direct-to-graph behavior**
   - Tests should mock the API boundary (or adapters) rather than reaching into any graph client.
2. **No unsourced narrative in Focus Mode**
   - Any story rendering test should include citations in the expected syntax, and/or verify that “missing citation” warnings render (if the UI has that affordance).
3. **Deterministic, reproducible tests**
   - No reliance on wall-clock time, network, or non-versioned external sources.

---

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  A[Story Node (Markdown)] --> B[Story Parser/Renderer]
  C[Focus API Context Bundle] --> D[Focus Mode UI]
  B --> D
  D --> E[Audit / Provenance Panel (UI)]
  subgraph Tests[web/src/story/__tests__/]
    T1[Fixture story nodes] --> B
    T2[Mock context bundles] --> D
    T3[Assertions: citations, provenance, redaction-safe UI] --> D
  end
~~~

---

## 🧠 Story Node & Focus Mode Integration

### What to test about Story Nodes

Story Nodes are “machine-ingestible storytelling”:

- They should be renderable as Markdown with citation tokens.
- They may include optional Focus Mode hints (layers/time/center) that should be reflected in the UI state when present.

Recommended test categories:

| Category | What to assert | Fixture pattern |
|---|---|---|
| Citation rendering | `【source†Lx-Ly】` is rendered consistently (link, popover, footnote, etc.) | Minimal story node with 1–2 citations |
| Missing/invalid citations | UI surfaces warnings or fails safely (no silent acceptance) | “invalid” story node fixture |
| Focus hints | `focus_layers`, `focus_time`, `focus_center` (if supported) update map/timeline state | Story node fixture with Focus hints |
| Entity links | Entity anchors in narrative trigger Focus Mode navigation correctly | Story node fixture with entity refs |
| Audit panel wiring | Evidence IDs appear in audit panel; user can inspect provenance | Mock context bundle with evidence list |

### What to test about Focus Mode

Focus Mode is a specialized UI state:

- Entering Focus Mode should request a context bundle from the API boundary (mocked).
- The rendered view should clearly separate:
  - the narrative,
  - the evidence / provenance panel,
  - any AI-generated sections (if present) with explicit labeling and opt-in behavior.

> If the repository includes a “Story Node validator” that runs in CI, UI tests should complement it by verifying that **the renderer and UI behaviors** match the validator’s expectations (especially for citations and redaction-safe displays).

---

## 🧪 Validation & CI/CD

### Local reproduction (placeholder)

~~~bash
# NOTE: commands are placeholders — replace with repo-approved tooling.
# Goal: run ONLY the Story subsystem tests (or the full web test suite).

# e.g. npm test
# e.g. pnpm test
# e.g. yarn test
# e.g. npm run test:story
~~~

### Test writing checklist (UI)

- [ ] Tests do not fetch real network resources (mock API calls)
- [ ] Tests do not hardcode sensitive coordinates or PII in fixtures
- [ ] Assertions include at least one “provenance behavior” check for Focus Mode screens
- [ ] Accessibility checks are included where the repo supports them (**not confirmed in repo**)
- [ ] Snapshots (if used) are stable and minimal (avoid snapshotting huge HTML trees)

### CI expectations (if configured)

- These tests should be runnable headlessly.
- Failures must be deterministic (no flaky timeouts, no random data).
- If UI schemas exist (e.g., layer registry), tests should not bypass schema constraints.

---

## 📦 Data & Metadata

### Fixtures policy

Fixtures in this folder must be:

- **Small**: minimal payload to demonstrate behavior
- **Synthetic**: do not copy raw datasets into `web/`
- **Redaction-safe**: no restricted coordinates or sensitive locations unless already generalized and explicitly approved

Recommended fixture types:

- `story-node.minimal.md`: valid citations + neutral narrative
- `story-node.invalid.md`: missing citations / malformed citation token
- `focus-bundle.sample.json`: mock API response (context bundle)

---

## 🌐 STAC, DCAT & PROV Alignment

This UI test folder does not produce STAC/DCAT/PROV artifacts, but tests can still enforce alignment by:

- Verifying that evidence references in UI payloads are treated as **identifiers**, not as raw embedded datasets.
- Ensuring “evidence IDs” displayed in the audit panel match expected formats (if a format is defined in schemas/contracts — **not confirmed in repo**).
- Confirming the UI does not imply provenance that is absent (“no orphan facts”).

---

## 🧱 Architecture

### Architectural invariants relevant to these tests

- **API boundary is canonical:** UI should only consume graph/catalog content through API endpoints.
- **Focus Mode is provenance-linked only:** narrative and context must trace back to evidence identifiers.
- **Contracts are canonical:** any shape assumptions about Focus Mode payloads must come from API contracts/schemas (or be marked as “not confirmed in repo” and treated as placeholders).

### Recommended mocking boundary

- Mock the Focus Mode API request at the HTTP boundary (or at an injected client adapter), rather than mocking deep internal components.
- Prefer “contract-shaped” mock payloads:
  - minimal fields,
  - stable IDs,
  - explicit evidence references.

---

## ⚖ FAIR+CARE & Governance

### Review gates

- Changes that add new fixtures with:
  - sensitive/restricted locations,
  - culturally sensitive narrative content,
  - or AI-generated narrative behaviors
  require governance review per:
  - `docs/governance/ROOT_GOVERNANCE.md`
  - `docs/governance/SOVEREIGNTY.md`
  - `docs/governance/ETHICS.md`

### CARE / sovereignty considerations

- Do not include exact coordinates for sensitive sites in public test fixtures.
- Prefer coarse geometries and generalized locations if any spatial values are required at all.

### AI usage constraints (in UI tests)

- If tests cover AI-labeled sections, verify:
  - AI output is explicitly labeled,
  - user opt-in behavior is respected,
  - AI text does not appear as “authoritative evidence.”

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-25 | Initial Story subsystem tests README (structure + invariants + fixture policy) | (you) |

---

### Footer refs (do not remove)

- Master guide: `docs/MASTER_GUIDE_v12.md`
- Universal template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Ethics: `docs/governance/ETHICS.md`

