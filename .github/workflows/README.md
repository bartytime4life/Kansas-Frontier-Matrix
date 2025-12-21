---
title: ".github/workflows — CI/CD Workflows Guide (GitHub Actions)"
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

doc_uuid: "urn:kfm:doc:github:workflows:readme:v1.0.0"
semantic_document_id: "kfm-github-workflows-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:github:workflows:readme:v1.0.0"
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

# .github/workflows — CI/CD Workflows Guide (GitHub Actions)

## 📘 Overview

### Purpose
- Document what GitHub Actions workflows exist (or are expected to exist) under `.github/workflows/`, what each one validates, and which checks are considered merge-blocking.
- Keep CI behavior aligned with KFM’s canonical pipeline ordering:
  **ETL → STAC/DCAT/PROV → Graph → APIs → React/Map UI → Story Nodes → Focus Mode**.
- Provide a single place to update when workflows are added/renamed, so contributors can quickly discover “what runs when” and “how to reproduce locally.”

> Note: This README includes **recommended defaults** aligned with KFM v12/v13 docs.  
> Workflow names and local commands are **not confirmed in repo** unless you update the inventory table below to match the actual `.github/workflows/*.yml` files.

### Scope

| In Scope | Out of Scope |
|---|---|
| Workflow inventory + intent, triggers, and required checks | Full workflow YAML contents (live in `.yml` files) |
| CI design invariants (determinism, skip-vs-fail rules, permissions) | Cloud deploy / runtime infra (belongs under `tools/` or ops repos) |
| How CI maps to KFM pipeline stages | Implementing ETL / API / UI features themselves |

### Audience
- Primary: maintainers and contributors who modify workflows or need to understand CI gates.
- Secondary: reviewers (governance/security/historian/editor) who rely on CI signals.

### Definitions (link to glossary)
- Link: `docs/glossary.md` (not confirmed in repo)
- Terms used in this doc:
  - **Workflow**: a GitHub Actions automation defined in `.github/workflows/*.yml`.
  - **Gate**: a required check that must pass before merge/release.
  - **Contract artifact**: a machine-validated schema/spec (e.g., JSON Schema, OpenAPI, GraphQL SDL, UI registry schema).
  - **Evidence artifact**: STAC/DCAT/PROV outputs and derived evidence products consumed downstream.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide v12 | `docs/MASTER_GUIDE_v12.md` | Core maintainers | Canonical pipeline ordering + canonical homes |
| v13 Redesign Blueprint | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Core maintainers | CI gate alignment + repo lint rules |
| Markdown Work Protocol | `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` | Docs governance | Not confirmed in repo |
| Schemas root | `schemas/` | Contract maintainers | Not confirmed in repo |
| Security policy | `.github/SECURITY.md` | Security owners | Not confirmed in repo |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Workflow inventory table matches `.github/workflows/*.yml`
- [ ] Required checks (merge gates) are explicitly identified
- [ ] “Skip vs fail” behavior is documented for optional roots (see CI rules below)
- [ ] Governance + CARE/sovereignty considerations explicitly stated

---

## 🗂️ Directory Layout

### This document
- `path`: `.github/workflows/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Workflows | `.github/workflows/` | GitHub Actions workflow YAML + this README |
| Composite actions | `.github/actions/` | Optional: shared CI steps (not confirmed in repo) |
| Docs | `docs/` | Governed docs + templates + standards |
| Schemas | `schemas/` | JSON Schemas + validation shapes (not confirmed in repo) |
| Data outputs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | Evidence outputs (may be absent early) |
| Server/API | `src/server/` | OpenAPI/GraphQL contracts + services (not confirmed in repo) |
| UI | `web/` | React/MapLibre UI + registries (not confirmed in repo) |
| Story Nodes | `docs/reports/story_nodes/` | Draft/published narratives + assets (not confirmed in repo) |

### Expected file tree for this sub-area

~~~text
📁 .github/
├── 📁 workflows/
│   ├── 📄 README.md
│   ├── 📄 ci__repo_lint.yml                     # not confirmed in repo
│   ├── 📄 ci__markdown_protocol.yml             # not confirmed in repo
│   ├── 📄 ci__schemas_validate.yml              # not confirmed in repo
│   ├── 📄 ci__catalogs_validate.yml             # not confirmed in repo
│   ├── 📄 ci__graph_checks.yml                  # not confirmed in repo
│   ├── 📄 ci__api_contract_tests.yml            # not confirmed in repo
│   ├── 📄 ci__ui_checks.yml                     # not confirmed in repo
│   ├── 📄 ci__story_nodes_validate.yml          # not confirmed in repo
│   └── 📄 ci__security_and_sovereignty.yml      # not confirmed in repo
└── 📄 SECURITY.md                               # not confirmed in repo
~~~

---

## 🧭 Context

### Background
KFM treats documentation, contracts, and provenance as first-class artifacts. CI is the enforcement layer that ensures:
- canonical homes stay canonical (no “mystery duplicates”),
- schema/contract artifacts remain valid,
- narrative artifacts (Story Nodes) remain sourced and auditable.

### Assumptions
- GitHub Actions is enabled for the repository.
- Workflows are designed to be deterministic and reproducible (no hidden state).
- Some canonical roots may be optional in early phases; CI must handle that cleanly.

### Constraints / invariants
- **Canonical pipeline ordering is preserved**: ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode.
- **API boundary is enforced**: the UI consumes Neo4j-derived data via the API layer only (no direct graph access).
- **Repo lint rules are enforced** (recommended):
  - no YAML front-matter in code files,
  - no `README.me`,
  - no duplicate canonical homes without explicit deprecation markers.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Which checks are required to merge to `main`? | TBD | TBD |
| What is the canonical validation command set (`make`, `npm`, `poetry`, etc.)? | TBD | TBD |
| Do we publish artifacts (SBOM, schema bundles, reports) into `releases/`? | TBD | TBD |

### Future extensions
- Add scheduled workflows for nightly catalog integrity checks.
- Add “release” workflows that build signed bundles and SBOMs into `releases/` (not confirmed in repo).
- Add provenance integrity workflows that cross-check STAC/DCAT/PROV linkage.

---

## 🗺️ Diagrams

### System / dataflow diagram

~~~mermaid
flowchart LR
  PR[Pull Request] --> CI[GitHub Actions CI]

  CI --> LINT[Repo lint + docs lint]
  CI --> SCHEMAS[Schema validation]
  CI --> CONTRACTS[API contract tests]
  CI --> UI[UI checks]
  CI --> STORY[Story Node validation]
  CI --> SEC[Security + sovereignty gates]

  LINT --> MERGE[Merge Gate]
  SCHEMAS --> MERGE
  CONTRACTS --> MERGE
  UI --> MERGE
  STORY --> MERGE
  SEC --> MERGE
~~~

### Optional: sequence diagram

~~~mermaid
sequenceDiagram
  participant Dev as Contributor
  participant GH as GitHub Actions
  participant Repo as Repo Contents

  Dev->>Repo: Push / Open PR
  Repo->>GH: workflow triggers
  GH->>Repo: checkout + run validators
  GH-->>Dev: status checks + artifacts
~~~

---

## 📦 Data & Metadata

### Inputs / triggers

| Input | Source | Notes |
|---|---|---|
| `pull_request` | GitHub | Main CI trigger for gates |
| `push` | GitHub | Often for branch checks; configure as needed |
| `workflow_dispatch` | GitHub UI | Manual reruns / ad-hoc validations |
| `schedule` | GitHub | Nightly/weekly integrity checks (optional) |

### Outputs

| Output | Where | Notes |
|---|---|---|
| Check results | PR “Checks” tab | Merge gating decisions |
| Logs | GitHub Actions run | Should avoid leaking secrets |
| Artifacts | GitHub run artifacts | Optional: reports, SARIF, schema bundles |
| Release bundles | `releases/` | Not confirmed in repo |

---

## 🌐 STAC, DCAT & PROV Alignment

### CI expectations for evidence artifacts
When these canonical roots exist, CI should validate them:
- `data/stac/` (STAC collections/items)
- `data/catalog/dcat/` (DCAT outputs, typically JSON-LD)
- `data/prov/` (PROV bundles per run/dataset)

### “Validate if present; fail if invalid; skip if not applicable”
CI workflows that reference optional roots MUST behave deterministically:
- If a root is **absent** (early repo phase), the workflow should **skip** related checks with a clear message.
- If a root is **present**, the workflow should **validate**.
- If present but **invalid**, the workflow should **fail**.

---

## 🧱 Architecture

### CI component placement
CI spans all pipeline stages but does not replace them. It enforces contracts at boundaries.

| Component | Canonical path | CI responsibility |
|---|---|---|
| ETL/pipelines | `src/pipelines/` | Test + lint + deterministic run rules |
| Evidence catalogs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | Validate schemas and linkage |
| Graph | `src/graph/` + `data/graph/` | Integrity checks + migrations sanity |
| APIs | `src/server/` | Contract tests + redaction checks |
| UI | `web/` | Build/lint/a11y + registry schema validation |
| Story Nodes | `docs/reports/story_nodes/` | Template + provenance validation |
| CI/CD | `.github/workflows/` | Enforce gates + report status |

### Interfaces / contracts enforced by CI

| Interface | Location | What to validate |
|---|---|---|
| Markdown protocol | `docs/` + repo-wide `.md` | Front-matter rules, links, structure |
| JSON Schema bundles | `schemas/` | Schema lint + resolver tests |
| STAC/DCAT/PROV outputs | `data/**` | Conformance + linkage |
| API schemas | `src/server/` + docs | Contract tests required |
| UI registries | `web/**` | Schema-validated registries (paths TBD) |

### Extension points checklist (for future workflow work)
- [ ] Repo lint: canonical home rules + file naming rules
- [ ] Docs: markdown protocol validation
- [ ] Schemas: validate JSON Schemas + version pinning
- [ ] Catalogs: validate STAC/DCAT/PROV outputs when present
- [ ] Graph: optional constraints checks (labels/relations)
- [ ] APIs: OpenAPI/GraphQL contract tests
- [ ] UI: build/lint/a11y + registry schema checks
- [ ] Story Nodes: provenance-linked narrative validation
- [ ] Security: dependency/secret scanning, sovereignty gates (as applicable)

---

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
CI ensures downstream UX can trust inputs:
- Story Nodes render with citations/provenance without “unsourced narrative.”
- Focus Mode can display audit flags when evidence or provenance is missing/invalid.

### Provenance-linked narrative rule
- Every claim must trace to a dataset / record / asset ID (enforced by Story Node validation gate).

---

## 🧪 Validation & CI/CD

### Minimum CI gates (recommended)
- Markdown protocol validation
- Schema validation
- Story Node validation
- API contract tests
- Security and sovereignty scanning gates

### Workflow inventory (update to match actual workflow YAML files)

| Workflow file | Trigger(s) | Purpose | Merge gate? | Notes |
|---|---|---:|:---:|---|
| `ci__repo_lint.yml` | PR | Enforce canonical homes, naming rules | TBD | not confirmed in repo |
| `ci__markdown_protocol.yml` | PR | Validate doc structure + front-matter | TBD | not confirmed in repo |
| `ci__schemas_validate.yml` | PR | Validate JSON schemas | TBD | not confirmed in repo |
| `ci__catalogs_validate.yml` | PR | Validate STAC/DCAT/PROV outputs (if present) | TBD | not confirmed in repo |
| `ci__api_contract_tests.yml` | PR | OpenAPI/GraphQL contract tests | TBD | not confirmed in repo |
| `ci__ui_checks.yml` | PR | UI lint/build/a11y (as configured) | TBD | not confirmed in repo |
| `ci__story_nodes_validate.yml` | PR | Validate Story Nodes + provenance | TBD | not confirmed in repo |
| `ci__security_and_sovereignty.yml` | PR + schedule | Dependency/secret scanning + sovereignty checks | TBD | not confirmed in repo |

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands

# 1) markdown protocol validation (TBD)
# ./tools/validate_markdown_protocol.sh

# 2) schema validation (TBD)
# python -m tools.validate_schemas

# 3) story node validation (TBD)
# python -m tools.validate_story_nodes docs/reports/story_nodes/

# 4) API contract tests (TBD)
# cd src/server && ./run_contract_tests.sh

# 5) UI checks (TBD)
# cd web && npm test && npm run build
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| CI run ID + conclusion | GitHub Actions | GitHub checks UI |
| Artifact digests | Workflow job | `releases/` (not confirmed in repo) |
| Schema version coverage | Schema validator | `docs/telemetry/` + `schemas/telemetry/` (not confirmed in repo) |

---

## ⚖ FAIR+CARE & Governance

### Review gates
- Workflow changes that relax or remove gates should require maintainer review (and security review if secrets/permissions change).
- Changes affecting Story Node validation rules should require historian/editor review (as applicable).

### CARE / sovereignty considerations
- Workflows must not leak sensitive locations, restricted datasets, or protected community information in logs/artifacts.
- If sovereignty rules apply to a dataset/domain, CI should enforce redaction/generalization gates as designed.

### AI usage constraints
- Ensure this doc’s AI permissions/prohibitions match intended use (no policy generation; no inference of sensitive locations).

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-21 | Initial `.github/workflows/README.md` scaffold | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
