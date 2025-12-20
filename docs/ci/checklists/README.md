---
title: "CI — Checklists (README)"
path: "docs/ci/checklists/README.md"
version: "v1.0.0"
last_updated: "2025-12-19"
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

doc_uuid: "urn:kfm:doc:ci:checklists:readme:v1.0.0"
semantic_document_id: "kfm-ci-checklists-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:ci:checklists:readme:v1.0.0"
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

# CI Checklists

## 📘 Overview

### Purpose
This directory contains **human review checklists** that complement automated CI gates. Checklists help reviewers and contributors consistently verify that a change preserves KFM’s **pipeline invariants**, **contracts**, and **governance constraints**, especially where automation cannot fully validate intent or context.

**Related docs**
- CI overview: `docs/ci/README.md`
- Canonical pipeline + invariants: `docs/MASTER_GUIDE_v12.md`
- Governed doc templates: `docs/templates/`

### Scope

| In Scope | Out of Scope |
|---|---|
| PR review checklists (data/catalog/graph/api/ui/story) | Defining new governance policy (belongs under `docs/governance/`) |
| Release readiness checklists (if present) | Deep runbooks / ops playbooks (place under `docs/runbooks/` if/when introduced) |
| “Manual checks” that are hard to automate (sensitivity, provenance completeness, UX audit) | Replacing CI automation (these docs **supplement**, not substitute for tests) |

### Audience
- Primary: Maintainers and reviewers
- Secondary: Contributors preparing PRs

### Definitions (link to glossary)
- Link: `docs/glossary.md` (if present)
- Terms used in this doc: CI gate, contract test, schema validation, provenance, redaction/generalization, deterministic pipeline.

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This directory index | `docs/ci/checklists/README.md` | Maintainers | Entry point for checklist usage |
| CI overview | `docs/ci/README.md` | Maintainers | Where CI gates are described (high-level) |
| Pipeline invariants | `docs/MASTER_GUIDE_v12.md` | Maintainers | Canonical ordering + “do not break” rules |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Checklist usage is described (how to apply in PR/review)
- [ ] Links to governing docs/templates are present
- [ ] No claims about enforcement that can’t be verified in-repo (only “intended use” + “must” when anchored to governing docs)

## 🗂️ Directory Layout

### This document
- `path`: `docs/ci/checklists/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| CI overview | `docs/ci/README.md` | CI concepts, gates, how docs relate to workflows |
| Workflows | `.github/workflows/` | Automation entry points (not documented here unless linked) |
| Standards & templates | `docs/templates/` + `docs/standards/` | Governing formats and protocols |
| Schemas | `schemas/` | JSON schemas (STAC/DCAT/telemetry/etc.) |
| Tests | `tests/` | Contract + unit/integration tests |
| Source | `src/` + `web/` | Pipeline code, API, and UI |

### Expected file tree for this sub-area
~~~text
📁 docs/
├── 📁 ci/
│   ├── 📄 README.md
│   └── 📁 checklists/
│       └── 📄 README.md
~~~

> Note: Additional checklist files may be added under `docs/ci/checklists/`. If they do not exist yet, create them as needed and update this index.

## 🧭 Context

### Background
KFM spans multiple subsystems (ETL, catalogs, graph, APIs, UI, story artifacts). Automated CI is necessary but not sufficient: some requirements are **contextual** (e.g., sensitivity handling, provenance adequacy, “did we break the API boundary?”, narrative claim traceability). Checklists capture these repeatable manual checks.

### Assumptions
- Reviewers will verify changes against the canonical pipeline and invariants documented in `docs/MASTER_GUIDE_v12.md`.
- Contributors will attach evidence (links, logs, IDs) when a checklist item asks for it.

### Constraints / invariants
- Preserve canonical ordering: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- UI must not read the graph directly; all access is via API contracts.
- Provenance is first-class; narrative content must be provenance-linked.

### How to use checklists (workflow)
1. **Select the checklist** that matches the change type (data ingest, schema/catalog updates, graph work, API changes, UI changes, story/narrative changes).
2. **Copy the checklist into the PR description** (or link to it) and mark items complete.
3. Where the checklist asks for evidence, provide it as:
   - schema validation output (or CI job link)
   - IDs (STAC item/collection IDs, dataset IDs, run IDs)
   - screenshots for UI changes (as appropriate)
4. Reviewers use the same checklist as a consistent “definition of done”.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Which checklists are mandatory for which change categories? | TBD | TBD |
| Where is checklist completion enforced (if at all)? | TBD | TBD |
| Do we need subfolders (e.g., `data/`, `api/`, `ui/`) under `docs/ci/checklists/`? | TBD | TBD |

### Future extensions
- Add category-specific checklists (Data, Catalogs, Graph, API, UI, Story Nodes).
- Add a release checklist if the repo adopts a versioned release process.

## 🗺️ Diagrams

### CI + checklist intent (human + automated gates)
~~~mermaid
flowchart LR
  A["Change proposed - PR"] --> B["Automated CI gates"]
  A --> C["Human checklist"]

  B --> D{CI passes}
  C --> E{Checklist done}

  D -->|Yes| F["Review and approval"]
  E -->|Yes| F

  F --> G["Merge and release"]

  D -->|No| H["Fix issues"]
  E -->|No| H

  H --> A
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| PR change set | git diff | Git hosting | Code review + CI |
| CI logs | job output | CI provider | Must be linkable/traceable |
| Catalog artifacts | JSON/JSON-LD | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | Schema validation + integrity checks |
| Story content | Markdown | `docs/` | Provenance linkage review |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Completed checklist (review evidence) | Markdown (copied into PR) | PR description/comments | N/A (process artifact) |
| Updated checklist docs (if needed) | Markdown | `docs/ci/checklists/` | KFM Markdown protocol |

### Sensitivity & redaction
- If a checklist touches location data, sources, or cultural materials that could be sensitive, the checklist must require:
  - confirmation of redaction/generalization rules
  - governance review triggers (as documented in governance docs)
- Do not include sensitive locations or PII in checklists or PR evidence.

### Quality signals
Examples of what checklists may require (as applicable):
- Completeness: required fields present (IDs, licenses, provenance).
- Validity: schema checks pass (STAC/DCAT/PROV).
- Integrity: no broken references (STAC links, dataset IDs).
- Determinism: runs are reproducible with pinned configs.

## 🌐 STAC, DCAT & PROV Alignment

### STAC
Checklist items should typically ask:
- Are new/changed STAC Items valid against the project profile?
- Are item ↔ collection references consistent?
- Are spatial/temporal extents present and reasonable?

### DCAT
Checklist items should typically ask:
- Does the dataset metadata have minimal required fields (title/description/license/keywords)?
- Are distribution links correct and stable?

### PROV-O
Checklist items should typically ask:
- Is `prov:wasDerivedFrom` present for new derived artifacts?
- Is `prov:wasGeneratedBy` present with a pipeline activity/run ID?

### Versioning
- If a change introduces a new version of an artifact, checklists should require predecessor/successor linkage as applicable.

## 🧱 Architecture

### Components (what checklists commonly span)
| Component | Responsibility | Interface |
|---|---|---|
| ETL | Ingest + normalize | Configs + run logs |
| Catalogs | STAC/DCAT/PROV | JSON + validators |
| Graph | Neo4j | Accessed only via API layer |
| APIs | Serve contracts | REST/GraphQL + tests |
| UI | Map + narrative | API calls only |
| Story Nodes | Curated narrative | Provenance-linked docs |
| Focus Mode | Context synthesis | Evidence + citations |

### Interfaces / contracts
Checklists must not imply bypassing the API boundary. If UI requires new data, the checklist should require an API contract update and tests.

## 🧠 Story Node & Focus Mode Integration

### How this area supports Focus Mode
When story content changes or new story nodes are added, checklist items should require:
- Every factual claim maps to a dataset/document ID (or equivalent evidence ref)
- Sensitivity handling is explicitly documented
- API routes (if any) can fetch the story node without direct graph access from UI

## 🧪 Validation & CI/CD

### Validation steps (typical)
- [ ] Markdown protocol checks (formatting/front-matter conventions)
- [ ] Schema validation (STAC/DCAT/PROV when touched)
- [ ] Graph integrity checks (when graph mappings change)
- [ ] API contract tests (when API changes)
- [ ] UI schema checks (when layer registry/UI config changes)
- [ ] Security and sovereignty checks (when sensitive content could be exposed)

### Reproduction
~~~bash
# Replace with repo-specific commands once confirmed in-repo.
# 1) run schema validators (STAC/DCAT/PROV)
# 2) run unit/integration tests
# 3) run doc lint / markdown checks
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| CI run link / job ID | CI provider | PR evidence |
| Pipeline run ID | ETL/catalog build | `data/prov/` (if generated) |

## ⚖ FAIR+CARE & Governance

### Review gates
Use governance docs as the source of truth for when extra review is required. Checklists should reference:
- `docs/governance/ROOT_GOVERNANCE.md`
- `docs/governance/ETHICS.md`
- `docs/governance/SOVEREIGNTY.md`

### CARE / sovereignty considerations
- If the change affects culturally sensitive materials or locations, require a governance review gate and ensure generalization/redaction rules are applied.

### AI usage constraints
- Checklists must not request prohibited AI actions (e.g., inferring sensitive locations).
- Any AI-assisted summaries must remain provenance-linked and non-speculative.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-19 | Initial `docs/ci/checklists/` README | TBD |

---
Footer refs:
- Master guide: `docs/MASTER_GUIDE_v12.md`
- Templates: `docs/templates/`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

