---
title: ".github — Automation & Community Health (KFM)"
path: ".github/README.md"
version: "v1.0.0"
last_updated: "2025-12-17"
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

# .github — Automation & Community Health

## 📘 Overview

### Purpose
This document defines what belongs in the `.github/` directory and how repository automation + community-health files support KFM’s governed pipeline and contributor workflow.

### Scope
| In Scope | Out of Scope |
|---|---|
| GitHub Actions workflows, status checks, CI/CD conventions | Application code (`src/**`) and data (`data/**`) |
| Community-health files (issue/PR templates, CODEOWNERS, SECURITY policy references) | End-user docs unrelated to GitHub processes |
| Security automation hooks (scanning gates, provenance/SBOM generation) | Operational secrets/credentials (never stored in-repo) |

### Audience
- Primary: Maintainers, release engineers, security reviewers
- Secondary: Contributors opening PRs and issues

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc: CI, CD, “status check”, “community-health file”, “governed doc”, “pipeline contract”

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Workflows | `.github/workflows/*.yml` | Maintainers | CI/CD + scanning gates |
| Security policy | `.github/SECURITY.md` | Security reviewers | Reporting + disclosure process |
| Issue templates | `.github/ISSUE_TEMPLATE/*` | Maintainers | Structured intake for issues |
| PR template | `.github/PULL_REQUEST_TEMPLATE.md` | Maintainers | Ensures required metadata/checks are addressed |
| Code owners | `.github/CODEOWNERS` | Maintainers | Review routing |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Statements avoid asserting repo contents that are *not confirmed in repo*
- [ ] Workflow expectations are stated as “must/should” only when backed by a governed contract (Master Guide / Security policy)
- [ ] File-tree section present and uses emoji + aligned tree

## 🗂️ Directory Layout

### This document
- `path`: `.github/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Workflows | `.github/workflows/` | CI/CD and security automation definitions |
| Policies | `.github/SECURITY.md` | Vulnerability reporting and disclosure |
| Templates | `.github/ISSUE_TEMPLATE/` | Issue forms and templates |
| PR template | `.github/PULL_REQUEST_TEMPLATE.md` | PR checklist and metadata prompts |
| System contracts | `docs/` | Master Guide, governed templates, standards |
| Schemas | `schemas/` | JSON schema (STAC/DCAT/telemetry/etc.) |
| Pipelines | `src/pipelines/` | ETL + catalog build + graph ingest |
| Tests | `tests/` | Unit/integration/contract tests |

### Expected file tree for this sub-area
> Note: The exact filenames below are a **recommended baseline** and may need to be adjusted to match the current repo state (**not confirmed in repo**).

~~~text
📁 .github/
├── 📄 README.md
├── 📄 SECURITY.md
├── 📄 CODEOWNERS
├── 📁 workflows/
│   ├── 📄 ci.yml
│   ├── 📄 docs.yml
│   ├── 📄 security.yml
│   ├── 📄 stac-validate.yml
│   └── 📄 release.yml
├── 📁 ISSUE_TEMPLATE/
│   ├── 📄 bug_report.yml
│   ├── 📄 data_ingest_request.yml
│   ├── 📄 story_node_request.yml
│   └── 📄 config.yml
└── 📄 PULL_REQUEST_TEMPLATE.md
~~~

## 🧭 Context

### Why `.github/` matters in KFM
KFM is “documentation-first” and “contract-first”: automation should protect the canonical pipeline ordering (ETL → catalogs → graph → APIs → UI → Story Nodes → Focus Mode) and prevent changes that break provenance or sovereignty rules.

In KFM, `.github/` is treated as a **control plane**: workflows and templates encode the minimum checks required for safe, reproducible contributions.

### Constraints and invariants
- **Pipeline order is non-negotiable**: artifacts should be produced/validated in the canonical order.
- **Front-end stays behind APIs**: do not introduce direct graph access from the UI layer.
- **Focus Mode is provenance-only**: narrative content must be traceable to IDs (datasets/records/assets) and must not “hallucinate sources”.

### Change management expectations
Changes under `.github/` are high-impact because they affect contributor experience, merge safety, and supply-chain posture.
- Prefer small, reviewable changes.
- Pin third-party GitHub actions where feasible.
- Keep workflow steps deterministic and cache-safe.

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  A["Contributor Branch"] --> B["Pull Request"]
  B --> C["CI Status Checks<br/>(lint · tests · schema · contract · security)"]
  C -->|pass| D["Merge to default branch"]
  C -->|fail| E["Fix + re-run"]
  D --> F["Optional CD<br/>(docs site release · catalog publish · tagged release)"]
~~~

## 📦 Data & Metadata

### Inputs (events that trigger automation)
- Pull requests
- Pushes to protected branches
- Scheduled workflows (e.g., nightly validation / data refresh)
- Release tags

### Outputs (artifacts and signals)
- Required status checks (pass/fail)
- Test reports and coverage artifacts (if configured)
- Schema validation reports for STAC/DCAT/telemetry (if configured)
- SBOM/provenance artifacts for releases (if configured)
- Published docs site / Pages deploy (if configured)

### Sensitivity and secrets
- Never store secrets in the repo.
- Prefer GitHub environment protection rules and least-privilege tokens.
- Treat any dataset that may encode restricted locations or culturally sensitive information as “governance-triggering”; require explicit review.

## 🌐 STAC, DCAT & PROV Alignment

Workflows in `.github/workflows/` should help enforce:
- STAC collection/item generation and validation for new/updated assets.
- DCAT mappings for dataset-level metadata.
- PROV run identifiers for transformations (ETL runs, catalog builds, graph ingests).

If a PR changes data products:
- Require schema validation for the modified STAC/DCAT/telemetry documents.
- Require a reproducible run reference (run ID or run log path), when applicable.

## 🧱 Architecture

### CI checks mapped to the canonical pipeline layers
| Layer | Typical checks in CI | Notes |
|---|---|---|
| ETL | config validation, deterministic run / replayability checks | Avoid non-deterministic transforms |
| Catalogs (STAC/DCAT/PROV) | JSON schema validation; STAC validation tooling | Machine-validated metadata |
| Graph | integrity tests; ontology/constraint checks | Stable labels/edges |
| APIs | OpenAPI/GraphQL contract tests | Backward compat or version bump |
| UI | layer registry schema checks; a11y smoke tests | No hidden data leakage |
| Story Nodes | schema + provenance-link validation | Evidence-led only |
| Focus Mode | provenance-linked bundle checks | Predictive content must be opt-in + uncertainty |
| Security/Sovereignty | secret scanning; dependency checks; policy gates | Apply “where applicable” |

### Workflow design principles
- **Deterministic**: CI should produce consistent results for the same commit.
- **Least privilege**: default to read-only permissions unless write is required.
- **Auditable**: artifacts should record versions, run IDs, and checksums when possible.

### Extension points checklist (for future work)
- [ ] Data: new domain added under `data/<domain>/`
- [ ] STAC: new collection + item schema validation
- [ ] PROV: activity + agent identifiers recorded
- [ ] Graph: new labels/relations mapped + migration plan
- [ ] APIs: contract version bump + tests
- [ ] UI: layer registry entry + access rules
- [ ] Focus Mode: provenance references enforced
- [ ] Telemetry: new signals + schema version bump

## 🧠 Story Node & Focus Mode Integration

### How `.github/` work surfaces in Focus Mode
This directory does not add end-user features directly, but it ensures that:
- Story Nodes remain machine-ingestible and provenance-linked.
- Focus Mode only receives evidence bundles with traceable identifiers.

### Provenance-linked narrative rule
- Every claim must trace to a dataset / record / asset ID.

## 🧪 Validation & CI/CD

### Minimum CI gates for “v12-ready” contributions
- Markdown protocol validation
- JSON schema validation (STAC/DCAT/telemetry)
- Graph integrity tests
- API contract tests
- UI layer registry schema checks
- Security + sovereignty scanning gates (where applicable)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands

# 1) validate markdown/doc protocol
# make docs-lint

# 2) validate schemas (STAC/DCAT/telemetry)
# make schema-validate

# 3) run tests
# make test

# 4) run security scans (where applicable)
# make security-scan
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| CI status + runtimes | GitHub Actions | (repo-specific) |
| Validation reports | schema validators | `reports/` (recommended) |

## ⚖ FAIR+CARE & Governance

### Review gates
Changes may require elevated review when they introduce:
- New sensitive layers
- New AI narrative behaviors
- New external data sources
- New public-facing endpoints

### CARE / sovereignty considerations
- Document redaction/generalization rules for any restricted locations.
- Ensure CI does not publish restricted data artifacts to public endpoints.

### AI usage constraints
- Ensure this doc’s AI permissions/prohibitions match intended use.
- Avoid implying prohibited AI actions (e.g., inferring sensitive locations).

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-17 | Initial `.github/README.md` | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
