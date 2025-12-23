---
title: "KFM GitHub Automation & Community Health"
path: ".github/README.md"
version: "v1.0.0-draft"
last_updated: "2025-12-23"
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

doc_uuid: "urn:kfm:doc:github:readme:v1.0.0-draft"
semantic_document_id: "kfm-github-readme-v1.0.0-draft"
event_source_id: "ledger:kfm:doc:github:readme:v1.0.0-draft"
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

# KFM GitHub Automation & Community Health

## 📘 Overview

### Purpose

- Document what belongs in `.github/` and how to change it safely.
- Govern expectations for CI/validation workflows and community health files so they reinforce KFM’s canonical, contract-first pipeline.

### Scope

| In Scope | Out of Scope |
|---|---|
| GitHub Actions workflows, reusable/composite actions, and CI-related configuration under `.github/` | Application logic under `src/`, datasets under `data/`, and operational cloud infrastructure |
| Community health files (issue/PR templates, CODEOWNERS, SECURITY entrypoint) | Product docs that belong in `docs/` (except when a file is required by GitHub conventions) |
| Review and least-privilege expectations for workflows | Runtime telemetry dashboards and observability plumbing |

### Audience

- Primary: repo maintainers and reviewers of CI/security changes.
- Secondary: contributors adding or updating workflows, templates, and automation.

### Definitions (link to glossary)

- Link: `docs/glossary.md`
- Terms used in this doc: workflow, required check, gate, least privilege, provenance, community health files.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide v12 | `docs/MASTER_GUIDE_v12.md` | Core maintainers | Canonical pipeline ordering + system inventory |
| Redesign Blueprint v13 | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Core maintainers | Repo layout + CI gate mapping |
| Markdown work protocol | `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` | Docs maintainers | Template + lint rules for governed Markdown |
| Security policy | `.github/SECURITY.md` + `docs/security/` | Security owners | Disclosure, reporting, and security standards |
| Templates | `docs/templates/` | Docs maintainers | Universal / Story Node / API contract templates |

### Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] Directory layout reflects the current `.github/` contents (no stale references)
- [ ] Validation steps are listed and repeatable (even if commands are placeholders)
- [ ] Governance + CARE/sovereignty considerations explicitly stated
- [ ] No secrets, tokens, or sensitive locations are embedded in this README

## 🗂️ Directory Layout

### This document

- `path`: `.github/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Repo automation + community health | `.github/` | CI workflows, templates, security entrypoints |
| Data domains | `data/` | Raw/work/processed + STAC/DCAT/PROV outputs |
| Documentation | `docs/` | Canonical governed docs |
| Pipelines | `src/pipelines/` | ETL, transforms, catalog build |
| Graph | `src/graph/` | Graph build + ontology bindings |
| APIs | `src/server/` | API layer + contracts (UI must not read Neo4j directly) |
| Web UI | `web/` | React + map UI, layer registries |
| Schemas | `schemas/` | JSON schemas + constraints for CI validation |
| Runs / experiments | `mcp/` | Run logs and experiment artifacts |

### Expected file tree for this sub-area

~~~text
📁 .github/
├── 📄 README.md                         # (this document)
├── 📁 workflows/                        # GitHub Actions workflows (CI/CD gates)
│   └── 📄 <workflow>.yml                # naming varies by repo conventions
├── 📁 actions/                          # optional: reusable/composite actions
│   └── 📁 <action-name>/
│       └── 📄 action.yml
├── 📁 ISSUE_TEMPLATE/                   # optional: issue templates
│   └── 📄 <template>.yml
├── 📄 pull_request_template.md          # optional: PR template
├── 📄 CODEOWNERS                        # optional: ownership + review routing
├── 📄 dependabot.yml                    # optional: dependency update config
└── 📄 SECURITY.md                       # security policy entrypoint
~~~

## 🧭 Context

### Background

- `.github/` is reserved for repository-level automation (CI) and community health files.
- In KFM, CI gates are expected to protect the canonical pipeline ordering and the “no unsourced narrative” rule by validating documents, schemas, and contracts before merge.

### Assumptions

- `.github/workflows/` changes can affect all pipeline stages (ETL → Catalog → Graph → API → UI → Story Nodes → Focus Mode).
- Workflow security is least-privilege by default (minimal `permissions:`; secrets must come from GitHub secrets, not committed text).
- CI runs should be deterministic and auditable (diffable outputs, stable IDs where applicable).

### Constraints / invariants

Non-negotiables this directory must not violate:

1. **No UI direct-to-graph reads**
   - UI code must not query Neo4j directly; all access is via the API layer (`src/server/`).
2. **No unsourced narrative**
   - Published Story Nodes and Focus Mode content must be provenance-linked; CI should never “green” a change that adds uncited facts.
3. **Contracts are canonical**
   - Schemas/specs live in `schemas/` and API contracts under `src/server/contracts/` and must validate in CI.
4. **Data outputs are not code**
   - Derived datasets live under `data/<domain>/processed/`, not under `src/`.

### Open questions

| Question | Owner | Target |
|---|---|---|
| Which workflows are “required checks” for the default branch? | Repo maintainers | TBD |
| Do we standardize workflow naming + shared actions for schema validation? | Contracts owners | TBD |

### Future extensions

- Add reusable composite actions for schema validation and Story Node linting (to reduce duplication across workflows).
- Add supply-chain hygiene (dependency scanning, pinned action SHAs) consistent with governance and sovereignty constraints.

## 🗺️ Diagrams

### CI gates over the canonical pipeline

~~~mermaid
flowchart LR
  PR[Pull Request] --> CI[GitHub Actions<br/>.github/workflows]

  CI --> DOCS[Docs & Markdown protocol]
  CI --> SCHEMA[Schemas<br/>STAC/DCAT/PROV/UI/Telemetry]
  CI --> PIPE[ETL/Catalog unit + integration tests]
  CI --> GRAPH[Graph integrity tests]
  CI --> API[API contract tests]
  CI --> UI[UI layer registry + a11y checks]
  CI --> STORY[Story Node validation]

  ETL[ETL] --> CATS[STAC/DCAT/PROV] --> N4J[Neo4j Graph] --> APIS[APIs] --> WEB[React/Map UI] --> SN[Story Nodes] --> FM[Focus Mode]

  STORY --> SN
  DOCS --> OK[Merge eligible]
  SCHEMA --> OK
  PIPE --> OK
  GRAPH --> OK
  API --> OK
  UI --> OK
  STORY --> OK
~~~

### Optional sequence view

~~~mermaid
sequenceDiagram
  participant Dev as Contributor
  participant GH as GitHub
  participant CI as GitHub Actions
  Dev->>GH: Open PR / push commits
  GH->>CI: Trigger workflows
  CI->>CI: Validate docs + schemas + contracts
  CI-->>GH: Report status checks
  GH-->>Dev: Required checks pass/fail
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| PR and push events | GitHub event payload | GitHub | GitHub event schema |
| Workflow definitions | YAML | `.github/workflows/**` | YAML parse + action linting (if configured) |
| Shared action definitions | YAML + scripts | `.github/actions/**` | YAML parse + code review |
| Repo policy docs | Markdown | `.github/**` + `docs/**` | Markdown protocol checks |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| CI status checks | Check runs | GitHub UI | Required-check policy (repo settings) |
| Validation reports | Logs / artifacts | GitHub Actions artifacts | Retention + redaction rules |
| Optional generated artifacts | Files | (repo-specific) | Must be diffable + deterministic |

### Sensitivity & redaction

- Treat workflow logs as potentially public. Never print secrets, tokens, or sensitive location details.
- If workflows handle restricted layers or culturally sensitive knowledge, enforce redaction/generalization at the API and Story Node layers (do not “leak” via CI artifacts).

### Quality signals

Target quality signals for `.github` assets:

- Minimal workflow permissions (`permissions:` scoped to the job).
- Third-party actions pinned to immutable versions (prefer SHAs).
- No network egress beyond what is required for validation (principle of least surprise).
- CI failures are actionable (clear logs; no flaky checks).

## 🌐 STAC, DCAT & PROV Alignment

This README does not define datasets directly, but CI workflows under `.github/workflows/` should validate standards outputs in their canonical locations.

### STAC

- Collections: `data/stac/collections/**`
- Items: `data/stac/items/**`
- Extension(s): per `schemas/stac/**` and KFM constraints

### DCAT

- Dataset records: `data/catalog/dcat/**`
- Constraints/shapes (as applicable): `schemas/dcat/**`

### PROV-O

- Bundles: `data/prov/**`
- Constraints/profiles: `schemas/prov/**`

### Versioning

- Schema versions: SemVer + changelog; changes that break validation require coordinated contract bumps.
- Catalog outputs should be deterministic and diffable (same inputs → same outputs).

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| CI (GitHub) | Gatekeeping + validation orchestration | GitHub checks + artifacts |
| ETL | Ingest + normalize | Config + run logs |
| Catalogs | STAC/DCAT/PROV | JSON + validator |
| Graph | Neo4j | Cypher (server-side) + API layer |
| APIs | Serve contracts | REST/GraphQL |
| UI | Map + narrative | API calls |
| Story Nodes | Curated narrative | Graph + docs |
| Focus Mode | Contextual synthesis | Provenance-linked |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| Workflow definitions | `.github/workflows/` | Changes reviewed; breaking gate changes require governance review |
| JSON schemas | `schemas/` | SemVer + changelog |
| API contracts | `src/server/contracts/` | Contract tests required |
| Layer registry | `web/**/layers/**` | Schema-validated |

### Extension points checklist (for future work)

- [ ] CI: add a new gate/workflow with minimal permissions and clear ownership
- [ ] Data: new domain added under `data/<domain>/...`
- [ ] STAC: new collection + item schema validation
- [ ] PROV: activity + agent identifiers recorded
- [ ] Graph: new labels/relations mapped + migration plan
- [ ] APIs: contract version bump + tests
- [ ] UI: layer registry entry + access rules
- [ ] Focus Mode: provenance references enforced
- [ ] Telemetry: new signals + schema version bump

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode

- CI gates here protect Focus Mode quality indirectly by ensuring:
  - Story Nodes validate (front-matter, citations, entity references, redaction compliance).
  - Evidence artifacts (STAC/DCAT/PROV) remain consistent and traceable.

### Provenance-linked narrative rule

- Every factual claim shown to users must trace to a dataset / record / asset ID.
- Predictive or AI-generated content must be opt-in and carry uncertainty/confidence metadata.

### Optional structured controls

_N/A for `.github/` docs._ Focus Mode controls live in Story Node front-matter under `docs/reports/story_nodes/**`.

## 🧪 Validation & CI/CD

### Validation steps

When modifying `.github/` assets (especially workflows):

- [ ] Markdown protocol checks
- [ ] Schema validation (STAC/DCAT/PROV + storynodes + UI + telemetry)
- [ ] Graph integrity checks
- [ ] API contract tests
- [ ] UI schema checks (layer registry)
- [ ] Security and sovereignty checks (as applicable)
- [ ] Workflow linting/sanity checks (YAML + action linting, if configured)

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands

# 1) validate schemas
#    (e.g., schemas/stac + schemas/dcat + schemas/prov + schemas/storynodes + schemas/ui)

# 2) run unit/integration tests
#    (e.g., ETL/Catalog/Graph/API tests)

# 3) run doc lint / markdown protocol validation
#    (governed markdown checks)
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| CI run logs + artifacts | GitHub Actions | GitHub Actions UI / artifacts |
| Pipeline telemetry (schema-defined) | Pipelines + CI | `docs/telemetry/` + `schemas/telemetry/` |

## ⚖ FAIR+CARE & Governance

### Review gates

- Changes to `.github/workflows/**` should require maintainer review.
- Any change that relaxes validation, increases workflow permissions, or touches security/sovereignty gates should be treated as **requires human review**.

### CARE / sovereignty considerations

- If workflows affect restricted locations or culturally sensitive knowledge:
  - enforce generalization/redaction rules at the API + Story Node layers,
  - prevent sensitive artifacts from being uploaded as CI artifacts,
  - document the review gate that approves publication.

### AI usage constraints

- Ensure this document’s AI permissions/prohibitions in front-matter match intended use.
- Do not use automation to introduce new policy text without governance review.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0-draft | 2025-12-23 | Initial `.github/` README scaffolding | TBD |

---

Footer refs:

- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
