---
title: "Kansas Frontier Matrix — .github Directory Guide"
path: ".github/README.md"
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

doc_uuid: "urn:kfm:doc:github:readme:v1.0.0"
semantic_document_id: "kfm-github-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:github:readme:v1.0.0"
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

# Kansas Frontier Matrix — .github

## 📘 Overview

### What this folder is

This directory hosts GitHub-specific configuration:

- CI/CD workflows (GitHub Actions) for validation and automation
- Community health files such as issue and pull request templates that guide contributors to follow KFM documentation + validation requirements

### Purpose

- Make CI expectations explicit and discoverable for contributors
- Keep the repo’s governed architecture enforceable at the pull request boundary

### Scope

In scope:

- Workflows that validate KFM’s contract artifacts and invariants across the pipeline
- Contributor-facing templates that capture required metadata (sources, licenses, validation steps, governance flags)

Out of scope:

- Pipeline implementations (live under `src/` and `tools/`)
- Generated datasets, catalogs, provenance bundles, or releases (live under `data/` and `releases/`)

### Audience

- Maintainers editing GitHub Actions workflows and repository automation
- Contributors opening issues or pull requests who need checklists and required fields

### Definitions

- See `docs/glossary.md` for shared terms (STAC, DCAT, PROV-O, Story Nodes, Focus Mode, etc.)

### Key artifacts

| Artifact | Path | Status | Notes |
|---|---|---|---|
| Master Guide v12 | `docs/MASTER_GUIDE_v12.md` | present | Canonical pipeline ordering + minimum CI gates |
| Universal Doc Template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | present | Governs markdown structure and front-matter requirements |
| Story Node Template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | present | Governs narrative docs that CI should validate |
| v13 Redesign Blueprint | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | not confirmed in repo | Defines invariants such as the API boundary and “no UI direct-to-graph reads” |

### Definition of done

- [ ] Required CI gates run (or explicitly skip) based on what changed
- [ ] Workflows follow the rule: validate if present; fail if invalid; skip if not applicable
- [ ] Workflows do not violate system invariants (e.g., UI never reads Neo4j directly; all graph access via API layer)
- [ ] Contributor templates capture required metadata for reviews (sources/licensing, validation steps, governance flags)

## 🗂 Directory Layout

### This document

- `path`: `.github/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Actions workflows | `.github/workflows/` | CI checks, scheduled jobs, deploy pipelines (if used) |
| Issue templates | `.github/ISSUE_TEMPLATE/` | Issue forms/templates (data addition requests, bug reports, etc.) |
| PR template | `.github/PULL_REQUEST_TEMPLATE.md` | PR checklist reminding contributors to update docs and run validation |

### File tree

~~~text
📁 .github/
├── 📄 README.md
├── 📁 workflows/                 # GitHub Actions workflows (CI/CD)
├── 📁 ISSUE_TEMPLATE/            # Issue forms/templates
└── 📄 PULL_REQUEST_TEMPLATE.md   # PR checklist template
~~~

## 📦 Data & Metadata

### Data lifecycle

This folder does not store datasets. Workflows here should enforce that data moves through the required staging pattern:

- `data/raw/` → `data/work/` → `data/processed/` → `data/stac/` (and optional report outputs)

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Pull request changes | Git diff | GitHub PR | Run the relevant gates for changed areas |
| Schemas | JSON Schema | `schemas/**` | Schema validation |
| Docs | Markdown | `docs/**` | Markdown protocol validation |
| UI registries | JSON | `web/**` | Schema validation |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| CI results | GitHub Actions checks | PR status | Must be reproducible and explain failures |
| Validation artifacts | logs/reports | CI artifacts | Job-defined |

### Sensitivity and redaction

- Identify any fields requiring generalization or omission for public outputs.
- Apply redaction/generalization rules from `docs/governance/SOVEREIGNTY.md` when applicable.

### Quality signals

- CI should provide clear, actionable failures:
  - what failed, why, where to reproduce, and the file path(s) involved

## 🌐 STAC, DCAT & PROV Alignment

### Policy for datasets

Workflows should enforce that new/updated datasets have:

- STAC Collection + Item(s)
- DCAT mapping record
- PROV activity bundle describing lineage

### Paths validated by CI

- STAC: `data/stac/collections/**`, `data/stac/items/**`
- DCAT: `data/catalog/dcat/**`
- PROV: `data/prov/**`
- Schemas: `schemas/stac/**`, `schemas/dcat/**`, `schemas/prov/**`

### Versioning expectations

- New versions should link predecessor/successor where applicable
- Graph lineage should mirror catalog lineage

## 🧱 Architecture

### How this folder supports the pipeline

KFM’s canonical ordering is enforced by CI gates configured here:

**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

Workflows should detect changes by area and run the corresponding gate(s).

### Components

| Component | Responsibility | Interface |
|---|---|---|
| ETL | Ingest + normalize | Config + run logs |
| Catalogs | STAC/DCAT/PROV | JSON + validator |
| Graph | Neo4j | Cypher + API layer |
| APIs | Serve contracts | REST/GraphQL |
| UI | Map + narrative | API calls |
| Story Nodes | Curated narrative | Graph + docs |
| Focus Mode | Contextual synthesis | Provenance-linked |

### Interfaces and contracts

| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas | `schemas/` | SemVer + changelog |
| API schemas | `src/server/` + docs | Contract tests required |
| Layer registry | `web/**` | Schema-validated |

### Invariants CI must protect

- UI must never query Neo4j directly; all graph access is via `src/server/`
- Contract artifacts are canonical (schemas and API contracts must validate)
- Derived datasets live under `data/<domain>/processed/`, not under `src/`

## 🧠 Story Node & Focus Mode Integration

### Story Nodes as machine-ingestible storytelling

- Published Story Nodes must be provenance-linked and validate (front-matter, citations, entity references, redaction compliance).

### Focus Mode rule

- Focus Mode consumes provenance-linked content only.
- Predictive or AI-generated content must be opt-in and include uncertainty metadata.

## 🧪 Validation & CI/CD

### Minimum CI gates

- Markdown protocol validation
- JSON schema validation (STAC/DCAT/telemetry)
- Graph integrity tests
- API contract tests
- UI layer registry schema checks
- Security + sovereignty scanning gates (where applicable)

### Validation steps

- [ ] Markdown protocol checks
- [ ] Schema validation (STAC/DCAT/PROV)
- [ ] Graph integrity checks
- [ ] API contract tests
- [ ] UI schema checks (layer registry)
- [ ] Security and sovereignty checks (as applicable)

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands
# 1) validate schemas
# 2) run unit/integration tests
# 3) run doc lint
~~~

### Telemetry signals

| Signal | Source | Where recorded |
|---|---|---|
| CI run logs | GitHub Actions | Actions UI + artifacts |

## ⚖ FAIR+CARE & Governance

### Review gates

Workflow changes require additional review when they:

- alter enforcement of sensitive-layer handling
- change sovereignty scanning/redaction gates
- relax required checks for contracts and provenance

### CARE and sovereignty considerations

- When a workflow change could expose restricted location detail, require governance review and ensure redaction/generalization rules are applied before any output is published.

### AI usage constraints

- Ensure automation does not generate new policy and does not infer sensitive locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-21 | Initial `.github/README.md` | TBD |

---

Footer refs:

- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
