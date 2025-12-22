~~~text
📁 .github/
├── 📄 dependabot.yml
├── 📄 PULL_REQUEST_TEMPLATE.md
└── 📁 workflows/
    └── 📄 README.md
~~~

---

~~~text
FILE: .github/workflows/README.md
~~~

~~~markdown
---
title: "GitHub Actions — Workflows (README)"
path: ".github/workflows/README.md"
version: "v1.0.0"
last_updated: "2025-12-22"
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

# GitHub Actions — Workflows (README)

## 📘 Overview

### Purpose

- Provide conventions for GitHub Actions workflows under `.github/workflows/`.
- Make CI expectations explicit so PRs remain **CI-clean** and architecture-synced.

### Scope

| In Scope | Out of Scope |
|---|---|
| CI workflows for validation, tests, and security checks | Production deployments (unless explicitly added later) |
| Workflow naming + organization conventions | Runtime infrastructure operations (databases, cloud resources) |

### Audience

- Primary: maintainers who add/modify workflows.
- Secondary: contributors who need to understand required checks.

### Definitions (link to glossary)

- Glossary (if present): `docs/glossary.md`
- Terms used here:
  - **CI**: continuous integration checks that gate merges
  - **Catalog validation**: STAC/DCAT/PROV schema + integrity validation
  - **Least privilege**: minimal GitHub token permissions in workflows

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Workflows folder | `.github/workflows/` | Maintainers | GitHub Actions YAML files live here |
| Dependabot config | `.github/dependabot.yml` | Maintainers | Automated dependency updates |
| PR template | `.github/PULL_REQUEST_TEMPLATE.md` | Maintainers | Ensures PR descriptions capture required info |
| Governance refs | `docs/governance/*` | Governance leads | Referenced by governed docs |

### Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] Workflow conventions documented clearly
- [ ] No hard-coded secrets or org-specific assumptions
- [ ] Validation steps described are repeatable

## 🗂️ Directory Layout

### This document

- `path`: `.github/workflows/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| GitHub meta | `.github/` | PR templates, automation configs |
| Workflows | `.github/workflows/` | GitHub Actions workflows |
| Data | `data/` | Raw/work/processed, catalog outputs |
| Catalog outputs | `data/stac/` / `data/catalog/dcat/` / `data/prov/` | STAC/DCAT/PROV outputs |
| Pipelines | `src/pipelines/` | ETL + catalog build code |
| Graph | `src/graph/` | Ontology bindings, ingest, migrations |
| API | `src/api/` or `src/server/` | API layer (UI must not read Neo4j directly) |
| UI | `web/` or `src/web/` | React/Map UI + Story/Focus Mode UX |

## 🧭 Context

### Why workflows matter in KFM

Workflows provide automated enforcement for:
- deterministic + idempotent pipeline expectations
- standards alignment (STAC/DCAT/PROV)
- API boundary invariants (UI never queries Neo4j directly)
- doc/template consistency (Markdown protocol validation)

### Minimal security posture

- Prefer least-privilege `permissions:` per workflow.
- Avoid running untrusted code with write tokens on `pull_request` from forks unless explicitly designed.

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  A[Developer pushes branch / opens PR] --> B[GitHub Actions triggers]
  B --> C[Validation jobs]
  C --> D{All required checks pass?}
  D -- yes --> E[Merge eligible]
  D -- no --> F[Fix issues / update PR]
~~~

## 📦 Data & Metadata

### Typical workflow artifacts

| Artifact | Where produced | Notes |
|---|---|---|
| Test logs | workflow job output | Keep logs readable + deterministic |
| Lint results | job annotations | Prefer annotation output for fast review |
| Build artifacts (optional) | workflow artifacts | Use only when needed; avoid leaking sensitive data |

## 🌐 STAC, DCAT & PROV Alignment

If the repo includes catalog outputs or generation steps, workflows should (when applicable):
- validate STAC Items/Collections against schema
- validate DCAT catalog structure
- validate PROV bundles for required identifiers
- run broken-link checks on catalog references (items ↔ assets ↔ collections)

## 🧱 Architecture

### Guiding architecture constraint

- The canonical KFM flow is: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- Workflows should validate each stage **without** bypassing layer boundaries.

### Suggested workflow families (may not exist yet)

- **repo-lint**: formatting, markdown protocol validation, link checks
- **data-catalog-validate**: STAC/DCAT/PROV validation
- **graph-validate**: schema/ontology validation, migration checks
- **api-contract**: OpenAPI/GraphQL schema lint + contract tests
- **web-ui**: build + unit tests + a11y checks (as applicable)
- **security**: dependency review, CodeQL (if configured)

## 🧠 Story Node & Focus Mode Integration

If Story Nodes or Focus Mode docs are changed in a PR, workflows should (when applicable):
- validate Story Node format against template expectations
- ensure referenced entity IDs resolve (or are explicitly marked as TODO with tracked tickets)
- enforce provenance linking for narrative claims

## 🧪 Validation & CI/CD

### Workflow authoring checklist

- [ ] Workflow names are descriptive and consistent
- [ ] `permissions:` is set and minimal
- [ ] Secrets are not echoed to logs
- [ ] Jobs are deterministic (pinned versions, stable tooling, fixed seeds where applicable)
- [ ] CI gates match the scope of changes (docs/data/graph/api/ui/story)

### Troubleshooting

- If a workflow is noisy or flaky, treat it as a defect:
  - reduce nondeterminism
  - improve caching strategy
  - add clearer output annotations
  - split large workflows into focused jobs

## ⚖ FAIR+CARE & Governance

### Review gates

- Sensitive data layers, sovereignty concerns, and narrative AI features should trigger explicit review per governance docs (if present).

### CARE / sovereignty considerations

- Avoid publishing exact sensitive locations, raw PII, or culturally sensitive details in logs/artifacts.
- When in doubt: generalize/redact and require human review.

### AI usage constraints

- Do not introduce workflows that automatically generate policy or infer sensitive locations from restricted datasets.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial workflows README | TBD |
~~~

---

~~~text
FILE: .github/dependabot.yml
~~~

~~~yaml
# Dependabot configuration for dependency hygiene.
# Minimal, CI-safe defaults: keep GitHub Actions up to date.
#
# If/when the repo has language package managers (pip/npm/etc),
# add additional "updates" blocks with correct directories.

version: 2

updates:
  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      interval: "weekly"
    open-pull-requests-limit: 5
    commit-message:
      prefix: "deps"
      include: "scope"
    groups:
      github-actions:
        patterns:
          - "*"
~~~

---

~~~text
FILE: .github/PULL_REQUEST_TEMPLATE.md
~~~

~~~markdown
<!--
---
title: "Pull Request Template"
path: ".github/PULL_REQUEST_TEMPLATE.md"
version: "v1.0.0"
last_updated: "2025-12-22"
status: "active"
doc_kind: "Template"
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

doc_uuid: "urn:kfm:doc:github:pull-request-template:v1.0.0"
semantic_document_id: "kfm-github-pull-request-template-v1.0.0"
event_source_id: "ledger:kfm:doc:github:pull-request-template:v1.0.0"
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
-->

## 📘 Summary

### What changed?

<!-- 1–5 sentences. Link issues/tickets if applicable. -->

### Why?

<!-- Motivation + user impact. -->

### What areas does this touch? (check all that apply)

- [ ] ETL / pipelines
- [ ] Catalogs (STAC / DCAT / PROV)
- [ ] Graph (ontology, ingest, migrations)
- [ ] AI (models, prompts, evidence products)
- [ ] API (REST/GraphQL contracts)
- [ ] UI (React/Map UI, MapLibre, a11y)
- [ ] Story Nodes / Focus Mode narrative
- [ ] Docs / templates / standards
- [ ] CI / tooling / GitHub configuration

## 🧭 Architecture + invariants (must remain true)

- [ ] Canonical pipeline ordering preserved: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**
- [ ] API boundary preserved: **UI does not read Neo4j directly**
- [ ] Stable IDs / deterministic transforms (idempotent ETL where applicable)
- [ ] No secrets or sensitive locations/PII introduced in code, data, logs, or artifacts

## 🌐 STAC / DCAT / PROV (if applicable)

- [ ] STAC: Items/Collections updated and schema-valid
- [ ] DCAT: Dataset catalog updated and consistent
- [ ] PROV: Provenance recorded (source IDs + run/activity IDs)

Evidence/paths:
- STAC: `data/stac/...`
- DCAT: `data/catalog/dcat/...`
- PROV: `data/prov/...`

## 🧱 Graph (if applicable)

- [ ] Ontology/schema changes documented and versioned (if required)
- [ ] Migrations included for non-backwards-compatible changes
- [ ] Graph tests/constraints updated (if present)

Evidence/paths:
- Ontology/docs: `docs/graph/...` (if present)
- Migrations: `src/graph/migrations/...` (if present)

## 📦 API (if applicable)

- [ ] Contract change documented (use `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` for governed contract updates)
- [ ] Contract tests updated/added (OpenAPI/GraphQL lint + resolver/integration tests)

## 🧪 Validation & CI/CD

### What did you validate? (check all that apply)

- [ ] CI is green
- [ ] Unit/integration tests updated (if applicable)
- [ ] Schema validation updated/passing (if applicable)
- [ ] Docs/templates updated in the same PR (if applicable)

### Notes for reviewers

<!-- Call out anything risky, non-obvious, or needing special attention. -->

## ⚖ FAIR+CARE & Governance

- [ ] Governance review required? (mark and explain)
- [ ] CARE/sovereignty considerations documented (if applicable)
- [ ] Sensitive data handling / generalization confirmed (if applicable)

## 🕰️ Version History (optional)

- Summary of notable changes if this PR is part of an incremental rollout.
~~~
