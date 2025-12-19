---
title: ".github — GitHub Automation & Repo Entry Points"
path: ".github/README.md"
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

# .github — GitHub Automation & Repo Entry Points

## 📘 Overview

### Purpose
- This document describes what belongs in the repo’s `.github/` area: GitHub Actions workflows, contribution templates, and security entry points.
- It also documents the intended CI “gates” that protect the Kansas Frontier Matrix (KFM) pipeline invariants (provenance-first, deterministic runs, and API-boundary access).

### Scope
| In Scope | Out of Scope |
|---|---|
| GitHub Actions workflows (`.github/workflows/`) | Implementing ETL, catalog, graph, API, or UI logic (lives outside `.github/`) |
| Repo contribution entry points (issue/PR templates, CODEOWNERS) | Writing governance policy (lives under `docs/governance/` and `.github/SECURITY.md`) |
| CI gate expectations (what must be validated) | Infra provisioning / cloud resources (not governed here) |

### Audience
- Primary: repo maintainers, CI/CD owners, security reviewers
- Secondary: contributors, data curators, reviewers for Story Nodes / Focus Mode content

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc:
  - **CI gate**: a required validation step that must pass before merge.
  - **Provenance-first**: artifacts must trace to STAC/DCAT/PROV + graph lineage.
  - **Sovereignty**: special handling (generalization/redaction/review) for restricted/sensitive locations or community-governed data.

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| GitHub workflows | `.github/workflows/` | Repo maintainers | CI gates, validation, release automation |
| Security policy | `.github/SECURITY.md` | Security owners | Canonical entry point for reporting + standards |
| Issue templates | `.github/ISSUE_TEMPLATE/` | Maintainers | Bug reports, data requests, etc. |
| PR template | `.github/PULL_REQUEST_TEMPLATE.md` | Maintainers | “Definition of done” checklist for PRs |
| Code ownership | `.github/CODEOWNERS` | Maintainers | Review routing; required approvals |
| Dependency updates | `.github/dependabot.yml` | Maintainers | Optional; if present, keep scoped and safe |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Links point to canonical KFM references (Master Guide, governance, security)
- [ ] CI gate expectations align with `docs/MASTER_GUIDE_v12.md`
- [ ] No workflow implies bypassing provenance/security/sovereignty checks
- [ ] No secrets/credentials documented or embedded

## 🗂️ Directory Layout

### This document
- `path`: `.github/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Master guide | `docs/MASTER_GUIDE_v12.md` | Canonical pipeline ordering + “v12-ready” gates |
| Workflows | `.github/workflows/` | CI jobs, validators, deployment pipelines |
| Security | `.github/SECURITY.md` + `docs/security/` | Policy + technical standards |
| Standards | `docs/standards/` | Governed standards, including markdown protocol |
| Templates | `docs/templates/` | Governed doc templates (Universal, Story Node, API Contract Extension) |
| Schemas | `schemas/` | JSON schemas (STAC/DCAT/telemetry/etc.) |
| Catalog outputs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | STAC/DCAT/PROV artifacts validated by CI |
| Pipelines | `src/pipelines/` | ETL + catalog build logic (workflows call into this) |
| Graph | `src/graph/` | Neo4j schema/migrations/ingestion (validated by CI) |
| APIs | `src/server/` | Contracted access layer (validated by CI) |
| UI | `web/` | React/map UI, layer registry checks, a11y gates |

### Expected file tree for this sub-area
~~~text
🗂️ .github/                                  GitHub automation and repo entry points
├── 📄 README.md                              Overview of this .github/ area (what lives where)
├── 🔐 SECURITY.md                            Security policy + reporting instructions
├── 📁 workflows/                             GitHub Actions workflows (CI, validation, release)
│   └── 📄 <ci-and-validation-workflows>.yml  CI + validation gates (lint/tests/schema/security)
├── 📁 ISSUE_TEMPLATE/                        Issue templates + forms
│   └── 📄 <issue-forms>.yml                  Structured issue form definitions
├── 📄 PULL_REQUEST_TEMPLATE.md               PR checklist + required change notes
├── 👥 CODEOWNERS                             Review ownership + required approvers routing
└── 🤖 dependabot.yml                         Automated dependency update configuration
~~~

## 🧭 Context

### Background
KFM’s pipeline is intentionally contract-driven: data is processed into standards-based catalogs (STAC/DCAT/PROV), then loaded into the graph, then served via APIs to the UI and Story/Focus experiences. `.github/` is where we enforce those contracts through automated validation gates and reviewer routing.

### Assumptions
- GitHub Actions is the CI runner for this repository.
- Required checks exist (or will exist) to validate:
  - governed Markdown documents,
  - STAC/DCAT/PROV schema validity,
  - graph integrity,
  - API contract compatibility,
  - UI layer registry structure,
  - security/sovereignty safeguards where applicable.

### Constraints / invariants
- Canonical ordering is preserved: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- **Frontend never reads Neo4j directly**; UI depends on API contracts only.
- Focus Mode must only consume provenance-linked content; unsourced narrative is not acceptable.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Which workflow files are “required checks” on the default branch? | TBD | TBD |
| Where are CI reports stored (artifacts vs `docs/telemetry/` vs `mcp/runs/`)? | TBD | TBD |
| Who are CODEOWNERS for workflows, security, and sovereignty-sensitive areas? | TBD | TBD |

### Future extensions
- Add/expand “sovereignty scanning gates” for changes touching sensitive layers or restricted locations.
- Add telemetry reporting for CI gate trends (pass rates, runtimes, security findings).

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  PR["Pull Request"] --> CI["GitHub Actions: CI Gates"]

  subgraph Gates["Gates"]
    M["Markdown protocol validation"]
    S["Schema validation: STAC/DCAT/PROV/telemetry"]
    G["Graph integrity tests"]
    A["API contract tests"]
    U["UI schema checks (layer registry and a11y hooks)"]
    Sec["Security and sovereignty checks (as applicable)"]
  end

  CI --> M
  CI --> S
  CI --> G
  CI --> A
  CI --> U
  CI --> Sec

  M --> Status["Required checks pass"]
  S --> Status
  G --> Status
  A --> Status
  U --> Status
  Sec --> Status
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
  participant Dev as Contributor
  participant GH as GitHub
  participant CI as Actions Runner
  participant Repo as Repo Artifacts

  Dev->>GH: Open PR
  GH->>CI: Trigger workflows
  CI->>Repo: Run validators + tests
  Repo-->>CI: Results + reports
  CI-->>GH: Status checks (pass/fail)
  GH-->>Dev: Review + merge eligibility
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Code changes | git diff | Pull request | unit/integration tests, lint |
| Catalog changes | JSON / TTL / JSON-LD | Pull request | schema validation (STAC/DCAT/PROV) |
| Docs changes | Markdown | Pull request | markdown protocol validation |
| Workflow changes | YAML | Pull request | workflow lint + least-privilege review |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| CI status checks | GitHub status | GitHub UI | Required checks configured in repo |
| Validation reports | artifacts/logs | GitHub Actions artifacts (typical) | Schema + test logs |
| Telemetry summaries (optional) | Markdown/JSON | `docs/telemetry/` | `schemas/telemetry/` |

### Sensitivity & redaction
- Workflows may require credentials for protected operations (publishing, deployments, private data pulls). Never store secrets in-repo; never echo secrets to logs.
- If CI touches sovereignty-restricted data or locations, enforce generalization/redaction rules and required reviewers before merge.

### Quality signals
- All required CI gates pass.
- Schema-validated catalogs remain consistent with the pipeline contracts.
- No regressions in API/UI/story validations when those areas are touched.

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- CI should validate STAC collections and items under `data/stac/` whenever they change.
- If new assets are added, ensure they remain link-consistent (items ↔ collections) and schema-valid.

### DCAT
- CI should validate DCAT dataset records under `data/catalog/dcat/` when changed.
- Minimum expected metadata fields (title/description/license/keywords) should be present per the Master Guide guidance.

### PROV-O
- CI should validate provenance bundles under `data/prov/` when changed.
- Provenance should reference stable run/activity identifiers where applicable.

### Versioning
- New versions should link predecessor/successor (catalog + graph lineage) when versioning is used.

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- When Story Nodes or Focus Mode artifacts change, CI should enforce that narrative claims trace to provenance-linked evidence (dataset/document/asset identifiers).

### Provenance-linked narrative rule
- Every claim must trace to a dataset / record / asset ID.

### Optional structured controls
~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks
- [ ] Schema validation (STAC/DCAT/PROV/telemetry)
- [ ] Graph integrity checks
- [ ] API contract tests
- [ ] UI schema checks (layer registry)
- [ ] Security and sovereignty checks (as applicable)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# 1) validate docs / markdown protocol
# 2) validate STAC/DCAT/PROV schemas
# 3) run unit/integration tests
# 4) run graph integrity checks
# 5) run API contract tests
# 6) run UI schema checks
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| CI pass/fail trend | GitHub Actions | `docs/telemetry/` + `schemas/telemetry/` |
| Security scan findings | Workflow job | `docs/telemetry/` + `schemas/telemetry/` |
| Sovereignty gate triggers | Workflow job | `docs/telemetry/` + `schemas/telemetry/` |

## ⚖ FAIR+CARE & Governance

### Review gates
- Workflow changes: require maintainer review; security reviewers when secrets/permissions or scanning rules change.
- Changes that affect public-facing content, sensitive layers, sovereignty rules, or AI narrative behaviors should trigger governance review per the Master Guide.

### CARE / sovereignty considerations
- Identify communities impacted and protection rules before exposing restricted locations or culturally sensitive content.

### AI usage constraints
- Ensure this document’s AI permissions/prohibitions match intended use.
- Do not treat AI-generated outputs as authoritative without provenance links and human review.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-19 | Initial `.github/README.md` scaffold | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
