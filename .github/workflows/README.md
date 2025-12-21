---
title: "KFM — GitHub Workflows (CI Gate Map)"
path: ".github/workflows/README.md"
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

doc_uuid: "urn:kfm:doc:github:workflows-readme:v1.0.0"
semantic_document_id: "kfm-github-workflows-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:github:workflows-readme:v1.0.0"
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

# KFM — GitHub Workflows (CI Gate Map)

## 📘 Overview

### Purpose
This folder documents **GitHub Actions workflows** under `.github/workflows/` and how they map to KFM’s CI gates and repository invariants.

KFM’s pipeline ordering is contract-driven, and CI is responsible for enforcing those contracts at each boundary so that downstream stages (API/UI/Story/Focus Mode) never consume invalid or unsourced artifacts.

### Scope

| In Scope | Out of Scope |
|---|---|
| Workflow intent, gate mapping, invariants, and “how to add/update workflows” | Detailed implementation of ETL/catalog/graph/API/UI jobs (belongs in subsystem docs/runbooks) |
| CI behavior rules (deterministic pass/fail/skip semantics) | Cloud deployment specifics (belongs under `tools/` and/or dedicated ops repos) |

### Audience
- Primary: repo maintainers and contributors adding or modifying workflows
- Secondary: reviewers who need a fast “what does CI enforce?” map

### Definitions (link to glossary)
- Link (expected): `docs/glossary.md`
- Terms used in this doc:
  - **Gate**: a required CI validation category (e.g., schema validation, story node validation).
  - **Repo lint**: structural and naming rules enforced in CI (see “Repo lint rules” below).
  - **Contract-first**: schemas and API contracts are treated as canonical artifacts and validated in CI.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide v12 | `docs/MASTER_GUIDE_v12.md` | Maintainers | Canonical pipeline order and repo inventory |
| v13 Redesign Blueprint | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Maintainers | Defines minimum CI gates and invariants |
| Workflows | `.github/workflows/*.yml` | Maintainers | CI implementations of gates |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Workflow list reflects what exists in `.github/workflows/`
- [ ] CI gates and repo lint rules are documented (including “skip vs fail” rules)
- [ ] Notes include “not confirmed in repo” where this README proposes future workflow names

---

## 🗂️ Directory Layout

### This document
- `path`: `.github/workflows/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| GitHub meta | `.github/` | Repo-level policies and automation |
| Workflows | `.github/workflows/` | GitHub Actions YAML workflows (CI/CD) |
| Schemas | `schemas/` | JSON Schemas (STAC/DCAT/PROV/story nodes/UI/telemetry) |
| Pipelines | `src/pipelines/` | ETL + transforms (deterministic, idempotent) |
| Graph | `src/graph/` + `data/graph/` | Ontology bindings + import artifacts |
| API boundary | `src/server/` + `src/server/contracts/` | API implementation + versioned contracts |
| UI | `web/` | React + map UI that consumes APIs/catalogs (not Neo4j directly) |
| Story Nodes | `docs/reports/story_nodes/` | Draft/published narratives with provenance |

### Folder snapshot (illustrative)
> Keep this tree current as workflows are added/renamed.

~~~text
📁 .github/
├── 📁 workflows/
│   ├── 📄 README.md
│   └── 📄 <workflow-files>.yml
└── 📄 README.md
~~~

---

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Repository content | Git refs | GitHub Actions runner | Gate-specific validation |
| Schemas/contracts | JSON / YAML / GraphQL | `schemas/`, `src/server/contracts/` | Schema/contract tests |
| Story Nodes | Markdown + front-matter | `docs/reports/story_nodes/` | Story node validators |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| CI status checks | GitHub check runs | PR / commit status | Deterministic pass/fail/skip rules |
| Validation reports (optional) | text/json | workflow artifacts | *Not confirmed in repo* (depends on implementation) |

### Sensitivity & redaction
- CI should treat logs as potentially public; never print restricted values.
- If a gate inspects sensitive content (e.g., sovereignty-flagged assets), it must enforce redaction/generalization rules before artifacts are surfaced.

### Quality signals
- “Green CI” indicates required gates passed.
- Gates that depend on optional roots must **skip** when the root is absent and **fail** when present but invalid.

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Validate `data/stac/collections/` and `data/stac/items/` against STAC + KFM profiles (when those artifacts exist).

### DCAT
- Validate `data/catalog/dcat/` outputs (JSON-LD) against DCAT + KFM mappings (when present).

### PROV-O
- Validate `data/prov/` bundles for pipeline run provenance (when present).

### Versioning
- Prefer versioned catalogs and contract artifacts; when version lineage is used, link predecessor/successor consistently across catalogs and graph (policy details live in standards docs).

---

## 🧱 Architecture

### Components (pipeline context)
| Component | Responsibility | Interface |
|---|---|---|
| ETL | Ingest + normalize | Config + run logs |
| Catalogs | STAC/DCAT/PROV | JSON + validator |
| Graph | Neo4j | Cypher + API layer |
| APIs | Serve contracts | REST/GraphQL |
| UI | Map + narrative | API calls |
| Story Nodes | Curated narrative | Graph + docs |
| Focus Mode | Contextual synthesis | Provenance-linked only |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas | `schemas/` | Semver + changelog (recommended) |
| API contracts | `src/server/contracts/` | Contract tests required |
| UI registries | `web/...` | Schema-validated |

### Extension points checklist (for future work)
- [ ] Add a new CI gate as a standalone workflow (or job) with a clear mapping back to a pipeline contract
- [ ] Ensure “skip if absent; fail if invalid” semantics for optional roots
- [ ] Update this README’s workflow list and gate map

---

## 🧠 Story Node & Focus Mode Integration

### Provenance-linked narrative rule
- CI must protect the invariant: **no unsourced narrative** in published Story Nodes and Focus Mode contexts.

### How this surfaces in Focus Mode
- Story nodes and focus contexts must render citations/provenance links; CI validation should ensure required references resolve (where validators exist).

---

## 🧪 Validation & CI/CD

### Minimum CI gates (v13 readiness)
- Markdown protocol validation
- Schema validation
- Story Node validation
- API contract tests
- Security and sovereignty scanning gates

> Exact job/tooling names live in the workflow YAML files and supporting scripts.

### Repo lint rules
Enforce:
- no YAML front-matter in code files
- no `README.me`
- no duplicate canonical homes without explicit deprecation markers

### Workflow behavior contract (determinism)
CI workflows that reference canonical roots must have deterministic behavior:
- validate if present
- fail if invalid
- skip if not applicable

### Workflow-to-gate map
> Update this table whenever workflows are added/renamed.

| Gate | What it protects | Expected workflow file(s) | Notes |
|---|---|---|---|
| Markdown protocol validation | Governed markdown compliance | *not confirmed in repo* | Add when validator exists |
| Schema validation | STAC/DCAT/PROV/UI/telemetry schema integrity | *not confirmed in repo* | Add per schema family |
| Story Node validation | Provenance + front-matter + entity refs | *not confirmed in repo* | Must protect “no unsourced narrative” invariant |
| API contract tests | Contract-first API boundary | `ci__api_contract_tests.yml` | Name assumes convention; adjust to actual file name |
| Security/sovereignty scanning | Prevent harmful disclosure + enforce gating | *not confirmed in repo* | Must align with governance docs |

### Reproduction
~~~bash
# Repo-specific commands are not defined here.
# Prefer running the same scripts the CI workflows call (if present),
# and keep them deterministic and pinned to tool versions.

# Examples (placeholders):
# 1) validate schemas
# 2) run unit/integration tests
# 3) run doc lint
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| CI gate results | GitHub Actions | PR checks / workflow logs (and optional artifacts) |

---

## ⚖ FAIR+CARE & Governance

### Review gates
- Workflow changes that affect sovereignty checks, redaction/generalization rules, or AI narrative behavior should trigger governance review.

### CARE / sovereignty considerations
- If a workflow processes sensitive datasets or locations, ensure any required generalization/redaction rules are applied before publishing artifacts.

### AI usage constraints
- This README is safe for summarization/structure extraction; it must not be used to invent policies or infer sensitive locations.

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-21 | Initial `.github/workflows/README.md` | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
