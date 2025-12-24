---
title: "KFM GitHub Automation & Community Health"
path: ".github/README.md"
version: "v1.0.1-draft"
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

doc_uuid: "urn:kfm:doc:github:readme:v1.0.1-draft"
semantic_document_id: "kfm-github-readme-v1.0.1-draft"
event_source_id: "ledger:kfm:doc:github:readme:v1.0.1-draft"
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
- Treat CI as a **pipeline contract enforcement layer** (not just “unit tests”), so merges preserve:
  - the canonical pipeline ordering,
  - contract-first API boundaries,
  - provenance-first content rules,
  - schema-valid catalogs and story outputs.

### Scope

| In Scope | Out of Scope |
|---|---|
| GitHub Actions workflows and CI configuration under `.github/` (including reusable/composite actions, when used) | Application logic under `src/`, datasets under `data/`, and operational cloud infrastructure |
| Community health files (issue/PR templates, CODEOWNERS, SECURITY entrypoint) when required by GitHub conventions | Product docs that belong in `docs/` (except when GitHub requires/recognizes a `.github/` location) |
| Review and least-privilege expectations for workflows | Runtime telemetry dashboards and production observability plumbing |

### Audience

- Primary: repo maintainers and reviewers of CI/security changes.
- Secondary: contributors adding or updating workflows, templates, and automation.

### Definitions

- Glossary: `docs/glossary.md` (**not confirmed in repo** — update this link if the glossary lives elsewhere)
- Terms used in this doc: workflow, required check, gate, least privilege, provenance, community health files.

### Quick navigation

- Workflows overview: `.github/workflows/README.md` (**not confirmed in repo**)
- Local reusable actions: `.github/actions/README.md` (**not confirmed in repo**)
- Lineage gate notes: `.github/lineage/README.md` (**not confirmed in repo**)
- Releases and distribution bundles: `releases/README.md` (**not confirmed in repo**)
- Canonical pipeline ordering + invariants: `docs/MASTER_GUIDE_v12.md`
- Repo layout + CI gate mapping: `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` (**draft; not confirmed in repo**)
- Markdown work protocol: `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` (**not confirmed in repo**)
- Security standards: `docs/security/` (**not confirmed in repo**)

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide v12 | `docs/MASTER_GUIDE_v12.md` | Core maintainers | Canonical pipeline ordering + system inventory |
| Redesign Blueprint v13 | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Core maintainers | Target repo layout + CI gate mapping (draft) |
| Markdown work protocol | `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` | Docs maintainers | Template + lint rules for governed Markdown |
| Workflow gates index | `.github/workflows/README.md` | Repo maintainers | Required checks, gate intent, and debug pointers (**not confirmed in repo**) |
| Local actions index | `.github/actions/README.md` | Repo maintainers | Shared actions and security posture (**not confirmed in repo**) |
| Lineage gate notes | `.github/lineage/README.md` | Repo maintainers | Provenance + cross-link validation notes (**not confirmed in repo**) |
| Releases README | `releases/README.md` | Core maintainers | Release bundle conventions + required contents (**not confirmed in repo**) |
| Ownership routing | `.github/CODEOWNERS` | Core maintainers | Review routing for workflows/security (**not confirmed in repo**) |
| Security entrypoint | `.github/SECURITY.md` or `SECURITY.md` | Security owners | Disclosure + reporting (location varies; **not confirmed in repo**) |
| Templates | `docs/templates/` | Docs maintainers | Universal / Story Node / API contract templates |

### Definition of done

- [ ] Front-matter complete + valid
- [ ] Directory layout reflects current `.github/` contents (no stale references)
- [ ] CI “behavior contract” is explicit (validate if present, fail if invalid, skip when not applicable)
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
| Workflows | `.github/workflows/` | GitHub Actions workflows (CI/CD gates) |
| Lineage kits | `.github/lineage/` | Optional: provenance + cross-link validators/docs |
| Local reusable actions | `.github/actions/` | Optional: reusable/composite actions used by workflows |
| Data domains | `data/` | Raw/work/processed + STAC/DCAT/PROV outputs |
| Documentation | `docs/` | Canonical governed docs |
| Pipelines | `src/pipelines/` | ETL, transforms, catalog build |
| Catalog tooling | `src/catalog/` | Catalog tooling (STAC/DCAT/PROV) (**not confirmed in repo**) |
| Graph | `src/graph/` | Graph build + ontology bindings |
| APIs | `src/server/` | API layer + contracts (UI must not read Neo4j directly) |
| Web UI | `web/` | React + map UI, layer registries |
| Schemas | `schemas/` | JSON schemas + constraints for CI validation |
| Tests | `tests/` | Unit + integration tests |
| Tools | `tools/` | Validators + CLI wrappers (must not create new canonical roots) |
| Runs / experiments | `mcp/` | Run logs and experiment artifacts |
| Releases | `releases/` | Versioned distribution bundles (**not confirmed in repo**) |

### Expected file tree for this sub-area

~~~text
📁 .github/
├── 📄 README.md                         # (this document)
├── 📁 workflows/                        # GitHub Actions workflows (CI gates)
│   ├── 📄 README.md                     # gate index + required checks (recommended)
│   └── 📄 *.yml                         # workflow files (do not list here unless present in-repo)
├── 📁 lineage/                          # optional: provenance + cross-link CI kits
│   ├── 📄 README.md
│   └── 📁 scripts/                      # optional; not confirmed in repo
│       └── 📄 validate_lineage.<ext>    # optional; not confirmed in repo
├── 📁 actions/                          # optional: reusable/composite actions
│   ├── 📄 README.md                     # shared action inventory (recommended)
│   └── 📁 <action-name>/
│       └── 📄 action.yml
├── 📁 apps/                             # optional: GitHub Apps / automation notes
│   └── 📄 README.md
├── 📁 ISSUE_TEMPLATE/                   # optional: issue templates
│   └── 📄 <template>.yml
├── 📄 pull_request_template.md          # optional: PR template
├── 📄 CODEOWNERS                        # optional: ownership + review routing
├── 📄 dependabot.yml                    # optional: dependency update config
└── 📄 SECURITY.md                       # optional: security policy entrypoint (GitHub-recognized location)
~~~

> Note: Specific workflow filenames and job layouts should not be enumerated here unless they exist in-repo. Keep this README synchronized with the actual `.yml` files present.

## 🧭 Context

### Background

- `.github/` is reserved for repository-level automation (CI) and community health files.
- In KFM, CI gates exist to keep contributions aligned to:
  - canonical pipeline ordering and invariants,
  - contract-first API boundaries,
  - provenance-first content rules,
  - schema-valid catalogs and story outputs.

### Assumptions

- `.github/workflows/` changes can affect all pipeline stages (ETL → Catalog → Graph → API → UI → Story Nodes → Focus Mode).
- Workflow security is least-privilege by default (minimal `permissions:`; secrets come from GitHub secrets/vars, not committed text).
- CI runs should be deterministic and auditable (diffable outputs, stable IDs where applicable).

### Constraints / invariants

Non-negotiables this directory must not violate:

1. **Canonical pipeline ordering**
   - ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode.
2. **No UI direct-to-graph reads**
   - UI code must not query Neo4j directly; all access is via the API layer (`src/server/`).
3. **No unsourced narrative**
   - Published Story Nodes and Focus Mode content must be provenance-linked; CI should never “green” changes that add uncited facts to governed narrative artifacts.
4. **Contracts are canonical**
   - Schemas/specs live in `schemas/` and API contracts under the API layer; they must validate in CI.
5. **Data outputs are not code**
   - Derived datasets live under `data/<domain>/processed/`, not under `src/` (and not under `tools/`).
6. **CI behavior is predictable**
   - If a governed root exists (schemas, catalogs, story nodes), workflows validate it and fail deterministically on invalid artifacts.
   - If an optional canonical root is absent, workflows skip that validation gate rather than failing the entire PR.
7. **No leakage via automation**
   - Workflow logs and artifacts must not disclose secrets or sensitive/restricted locations.

### Open questions

| Question | Owner | Target |
|---|---|---|
| Which workflows are “required checks” for the default branch? | Repo maintainers | TBD |
| Do we standardize workflow naming + shared actions for schema validation? | Contracts owners | TBD |
| Do we adopt a release bundle convention under `releases/<version>/` with SBOM + manifest + telemetry? | Core maintainers | TBD |
| What is the repo’s “minimum CI gates” list for v12/v13 readiness? | Repo maintainers | TBD |

### Future extensions

- Add reusable composite actions for:
  - schema validation (STAC/DCAT/PROV + story nodes + UI registry + telemetry),
  - Markdown protocol validation,
  - provenance/link integrity checks (STAC/DCAT/PROV ↔ story node evidence IDs).
- Add supply-chain hygiene:
  - third-party actions pinned to immutable SHAs,
  - dependency scanning (Dependabot or equivalent),
  - optional SBOM + artifact provenance attestations for release bundles.
- Use `.github/lineage/` as the canonical home for provenance + cross-link gate documentation and (optionally) shared validator scripts.

## 🗺️ Diagrams

### CI gates over the canonical pipeline

~~~mermaid
flowchart LR
  PR[Pull Request] --> CI[GitHub Actions<br/>.github/workflows]

  CI --> LINT[Repo lint<br/>roots + conventions]
  CI --> DOCS[Docs & Markdown protocol]
  CI --> SCHEMA[Schemas<br/>STAC/DCAT/PROV/UI/Telemetry]
  CI --> PIPE[ETL/Catalog unit + integration tests]
  CI --> GRAPH[Graph integrity tests]
  CI --> API[API contract tests]
  CI --> UI[UI layer registry + a11y checks]
  CI --> STORY[Story Node validation]
  CI --> SEC[Security posture gates<br/>secrets + permissions]

  ETL[ETL] --> CATS[STAC/DCAT/PROV] --> N4J[Neo4j Graph] --> APIS[APIs] --> WEB[React/Map UI] --> SN[Story Nodes] --> FM[Focus Mode]

  DOCS --> OK[Merge eligible]
  LINT --> OK
  SCHEMA --> OK
  PIPE --> OK
  GRAPH --> OK
  API --> OK
  UI --> OK
  STORY --> OK
  SEC --> OK
~~~

### Optional sequence view

~~~mermaid
sequenceDiagram
  participant Dev as Contributor
  participant GH as GitHub
  participant CI as GitHub Actions
  Dev->>GH: Open PR / push commits
  GH->>CI: Trigger workflows
  CI->>CI: Validate docs + schemas + contracts (+ security posture)
  CI-->>GH: Report status checks
  GH-->>Dev: Required checks pass/fail
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| PR and push events | GitHub event payload | GitHub | GitHub event schema |
| Workflow definitions | YAML | `.github/workflows/**` | YAML parse + action linting (if configured) |
| Lineage gate docs/scripts | Markdown + scripts | `.github/lineage/**` | Markdown protocol + script lint/tests (if present) |
| Local reusable actions | YAML + scripts | `.github/actions/**` | YAML parse + code review |
| Community health files | Markdown/YAML | `.github/**` | Markdown protocol checks (when governed) |
| Pipeline contract artifacts | Mixed | `schemas/**`, `docs/**`, `src/**`, `data/**` | Schema + contract + test gates |

### Outputs

| Output | Format | Where | Contract / Schema |
|---|---|---|---|
| CI status checks | Check runs | GitHub UI | Required-check policy (repo settings) |
| Validation reports | Logs / artifacts | GitHub Actions artifacts | Retention + redaction rules |
| Optional release bundles | Files | `releases/<version>/` | Manifest + SBOM + telemetry (if adopted; **not confirmed in repo**) |

### Sensitivity & redaction

- Treat workflow logs as potentially public. Never print secrets, tokens, or sensitive location details.
- If workflows touch restricted layers or culturally sensitive knowledge, ensure redaction/generalization is applied at the API and Story Node layers, and that CI artifacts do not leak restricted details.

### Quality signals

Target quality signals for `.github` assets:

- Minimal workflow permissions (`permissions:` scoped to the job; add write scopes only when required).
- Third-party actions pinned to immutable versions (prefer commit SHAs).
- Deterministic outcomes (avoid flaky checks; stable ordering; fixed seeds where applicable).
- CI failures are actionable (clear logs; links to the subsystem owner and where to debug).
- Gates validate canonical outputs in canonical locations (no “shadow” output roots).

## 🌐 STAC, DCAT & PROV Alignment

This README does not define datasets directly, but CI workflows should validate standards outputs in their canonical locations when present.

### STAC

- Collections: `data/stac/collections/**`
- Items: `data/stac/items/**`
- Constraints: `schemas/stac/**` (and any KFM extensions)

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
| Repo lint | Enforce canonical roots + naming + “no duplicates” posture | Lint reports + CI failure |
| Lineage gate | Provenance + cross-link validation | `.github/lineage/**` + CI checks |
| ETL | Ingest + normalize | Config + run logs |
| Catalogs | STAC/DCAT/PROV generation + validation | JSON + validator |
| Graph | Neo4j build + integrity | Server-side graph scripts + API boundary |
| APIs | Serve contracted access | REST/GraphQL |
| UI | Map + narrative | API calls |
| Story Nodes | Curated narrative artifacts | Governed Markdown + provenance links |
| Focus Mode | Contextual synthesis | Provenance-linked bundles |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| Workflow definitions | `.github/workflows/` | Changes reviewed; breaking gate changes require governance review |
| Lineage gate docs/scripts | `.github/lineage/` | Keep docs + scripts in sync with workflow behavior |
| Local actions | `.github/actions/` | Treat like code: tests + review; pin dependencies |
| JSON schemas | `schemas/` | SemVer + changelog |
| API contracts | API layer (e.g., `src/server/contracts/`) | Contract tests required |
| Layer registry | `web/**/layers/**` | Schema-validated |
| Release bundles | `releases/<version>/` | Version-pinned; include manifest + checksums (**not confirmed in repo**) |

### Canonical roots CI may depend on

When a gate validates a subsystem, it should reference these canonical roots (and skip if the root is absent):

- Docs: `docs/`
- Schemas: `schemas/`
- Data + catalogs: `data/` (including `data/stac/`, `data/catalog/dcat/`, `data/prov/`)
- Pipelines: `src/pipelines/`
- Graph: `src/graph/` and (optionally) `data/graph/`
- API: `src/server/`
- UI: `web/`
- Tests: `tests/`
- Tools: `tools/`
- Runs/experiments: `mcp/`
- Releases: `releases/`

### Extension points checklist

- [ ] CI: add a new gate/workflow with minimal permissions and clear ownership
- [ ] Docs: governed Markdown validates + links resolve
- [ ] Schemas: new schema files are referenced and validated
- [ ] Data: new domain added under `data/<domain>/...` (raw/work/processed)
- [ ] STAC/DCAT/PROV: outputs validate and remain deterministic
- [ ] Graph: new labels/relations mapped + migration plan
- [ ] APIs: contract version bump + tests
- [ ] UI: layer registry entry + access rules
- [ ] Story/Focus: provenance references enforced
- [ ] Telemetry: new signals + schema version bump

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode

- CI gates here protect Focus Mode quality indirectly by ensuring:
  - Story Nodes validate (front-matter, citations/evidence refs, entity references, redaction compliance).
  - Evidence artifacts (STAC/DCAT/PROV) remain consistent and traceable.
  - The UI only consumes data through the API boundary (no direct graph access).

### Provenance-linked narrative rule

- Every factual claim shown to users must trace to a dataset / record / asset ID.
- Predictive or AI-generated content must be opt-in and carry uncertainty/confidence metadata.

### Optional structured controls

_N/A for `.github/` docs._ Focus Mode controls live in Story Node front-matter under `docs/reports/story_nodes/**`.

## 🧪 Validation & CI/CD

### CI behavior contract

When writing or modifying workflows, ensure each gate is predictable:

- **Validate if present:** if a canonical root exists (or changes), validate its artifacts.
- **Fail if invalid:** schema errors, missing links, or orphan references fail deterministically.
- **Skip if not applicable:** optional roots absent → skip without failing the overall pipeline.

### Validation steps

When modifying `.github/` assets (especially workflows):

- [ ] Repo lint (canonical roots + no duplicate “shadow” directories)
- [ ] Markdown protocol checks
- [ ] Schema validation (STAC/DCAT/PROV + story nodes + UI + telemetry)
- [ ] Unit/integration tests (ETL/Catalog/Graph/API as applicable)
- [ ] Graph integrity checks
- [ ] API contract tests
- [ ] UI schema checks (layer registry) + a11y checks
- [ ] Security posture checks (secrets handling, minimal permissions, dependency scanning)
- [ ] Sovereignty checks (as applicable for restricted domains)

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands

# 1) validate governed markdown + front-matter
# 2) validate schemas (STAC/DCAT/PROV + story nodes + UI + telemetry)
# 3) validate lineage bundles + cross-links (if .github/lineage exists)
# 4) run unit/integration tests (pipelines/graph/api/ui)
# 5) run security checks (secrets scan, dependency scan, action lint)
~~~

### Workflow security hardening checklist

- [ ] Use minimal `permissions:` (prefer job-level permissions; default to read-only).
- [ ] Do not expose secrets to untrusted PR code (especially from forks).
- [ ] Pin third-party actions to commit SHAs.
- [ ] Avoid `pull_request_target` unless you fully understand the security implications (**not confirmed in repo** — recommended baseline).
- [ ] Prefer reproducible toolchains (pinned language/runtime versions; lockfiles where applicable).
- [ ] Keep artifacts redacted and minimize retention of sensitive outputs.

### Telemetry signals

| Signal | Source | Where recorded |
|---|---|---|
| CI run logs + artifacts | GitHub Actions | GitHub Actions UI / artifacts |
| Lineage health reports | CI | GitHub artifacts or `docs/telemetry/` (**not confirmed in repo**) |
| Pipeline telemetry | Pipelines + CI | `docs/telemetry/` + `schemas/telemetry/` (**not confirmed in repo**) |
| Release telemetry | Release workflows | `releases/<version>/telemetry.json` (**not confirmed in repo**) |

## ⚖ FAIR+CARE & Governance

### Review gates

- Changes to `.github/workflows/**` should require maintainer review.
- Any change that relaxes validation, increases workflow permissions, or touches security/sovereignty gates should be treated as **requires human review**.
- If a workflow change impacts public distribution (e.g., release bundles), route through governance review as defined by `docs/governance/ROOT_GOVERNANCE.md`.

### CARE / sovereignty considerations

- If workflows affect restricted locations or culturally sensitive knowledge:
  - enforce generalization/redaction rules at the API + Story Node layers,
  - prevent sensitive artifacts from being uploaded as CI artifacts,
  - document the review gate that approves publication.

### AI usage constraints

- Ensure this document’s AI permissions/prohibitions in front-matter match intended use.
- Do not use automation to introduce new policy text without governance review.
- Do not use AI to infer sensitive locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0-draft | 2025-12-23 | Initial `.github/` README scaffolding | TBD |
| v1.0.1-draft | 2025-12-23 | Align with Master Guide v12 + add CI behavior contract + expand directory layout + lineage/release pointers | TBD |

---

Footer refs:

- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
