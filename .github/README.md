---
title: "KFM GitHub Automation & Community Health"
path: ".github/README.md"
version: "v1.0.4-draft"
last_updated: "2025-12-28"
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

doc_uuid: "urn:kfm:doc:github:readme:v1.0.4-draft"
semantic_document_id: "kfm-github-readme-v1.0.4-draft"
event_source_id: "ledger:kfm:doc:github:readme:v1.0.4-draft"
commit_sha: "<latest-commit-hash>"

ai_transform_permissions:
  - "summarize"
  - "structure_extract"
  - "translate"
  - "keyword_index"
ai_transform_prohibited:
  - "generate_policy"
  - "infer_sensitive_locations"

doc_integrity_checksum: "sha256:<calculated-in-ci>"
---

# KFM GitHub Automation & Community Health

This README defines what belongs in `.github/`, how CI is expected to behave, and how community health files and automation support KFM’s end-to-end pipeline contract.

> **Governed document notice:** This file uses KFM governed front-matter. Do not remove it. Keep `path:` synchronized with the repository location.

> **Design intent:** `.github/` is a *mechanism surface* (automation + gates). It must **enforce** governance and contracts defined elsewhere; it must not silently *invent* new policy.

---

## 📘 Overview

### Purpose

- Establish a single, repo-local source of truth for:
  - what belongs in `.github/`,
  - how GitHub Actions gates are expected to behave,
  - how community health files are located and maintained.
- Treat CI as a **pipeline contract enforcement layer**, not only “unit tests,” so merges preserve:
  - canonical pipeline ordering,
  - contract-first API boundaries,
  - provenance-first narrative rules,
  - schema-valid catalogs and governed narrative artifacts.

### Scope

| In Scope | Out of Scope |
|---|---|
| GitHub Actions workflows under `.github/workflows/**` | Application logic under `src/**` |
| Local reusable/composite actions under `.github/actions/**` (if used) | Cloud/infra operations (belongs under `tools/**` or separate ops repos) |
| Community health files recognized by GitHub (issue/PR templates, CODEOWNERS, SECURITY entrypoint) | Full policy bodies (belongs under `docs/governance/**`, `docs/security/**`) |
| CI gate design: “validate if present; fail if invalid; skip if not applicable” | Any attempt to bypass governance review, reduce sensitivity/classification, or publish restricted artifacts via automation |
| Workflow security posture (least privilege, secrets hygiene, fork safety) | Production observability dashboards (CI may emit reports; ops dashboards are separate) |

### Audience

- **Primary:** maintainers and reviewers approving workflow/security/automation changes.
- **Secondary:** contributors adding or updating workflows, templates, and automation helpers.

### Definitions

#### Canonical pipeline ordering (non-negotiable)

KFM pipeline ordering (canonical), with “Catalogs” commonly understood as STAC/DCAT/PROV outputs:

**ETL → Catalogs (STAC/DCAT/PROV) → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**

> Some documents and diagrams break “Catalogs” into explicit steps: STAC → DCAT → PROV. Treat that as an *implementation detail* of the Catalogs stage, not a license to reorder stages.

#### Definitions (link to glossary)

- Link: `docs/glossary.md` (**recommended; not confirmed in repo**)
- Terms used here:
  - **Gate**: a CI check that enforces a contract (schema, policy boundary, reproducibility rule).
  - **Required check**: a gate configured in branch protection as mandatory for merge.
  - **Baseline root**: a directory/file required by an adopted repo baseline (e.g., “v13-ready” posture).
  - **Trusted context**: CI execution path that is allowed to use secrets/write permissions (typically `push` to protected branches, manual approvals, or trusted workflows).
  - **Untrusted context**: CI execution path that must **not** use secrets or write permissions (typically `pull_request` from forks).
  - **Least privilege**: minimal GitHub token permissions and minimal secret exposure.
  - **Idempotent / deterministic**: same inputs → same outputs; stable IDs/ordering where applicable.

### Quick navigation

> Some entries are **recommended structure** and may not exist yet (**not confirmed in repo**). If a link is missing, prefer creating the file rather than deleting references.

- Workflows overview + required check index: `.github/workflows/README.md` (**recommended; not confirmed in repo**)
- Local reusable actions inventory: `.github/actions/README.md` (**recommended; not confirmed in repo**)
- Lineage gate notes (provenance + cross-link rules): `.github/lineage/README.md` (**recommended; not confirmed in repo**)
- Reproducibility helpers: `.github/repro-kit/README.md` (**recommended; not confirmed in repo**)
- GitHub Apps / automation notes: `.github/apps/README.md` (**recommended; not confirmed in repo**)
- Ownership routing: `.github/CODEOWNERS` (**recommended; not confirmed in repo**)
- Security entrypoint: `.github/SECURITY.md` (preferred for KFM) or repo-root `SECURITY.md` (fallback; location varies)

Core KFM anchors:

- Canonical pipeline ordering + invariants: `docs/MASTER_GUIDE_v12.md`
- v13 repo layout + CI alignment: `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Markdown governance/work protocol: `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` (**recommended; not confirmed in repo**)
- Repo structure standard: `docs/standards/KFM_REPO_STRUCTURE_STANDARD.md` (**recommended; not confirmed in repo**)
- Governed doc template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- API contract extension template: `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide v12 (draft) | `docs/MASTER_GUIDE_v12.md` | Core maintainers | Canonical pipeline ordering + subsystem homes |
| Redesign Blueprint v13 (draft) | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Core maintainers | “One canonical home per subsystem” + CI alignment |
| Markdown Work Protocol | `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` | Standards owners | Markdown/front-matter rules (**not confirmed in repo**) |
| Repo Structure Standard | `docs/standards/KFM_REPO_STRUCTURE_STANDARD.md` | Standards owners | Canonical roots + anti-drift posture (**not confirmed in repo**) |
| Workflow gates index | `.github/workflows/README.md` | Repo maintainers | Names, intent, required checks (**recommended; not confirmed in repo**) |
| Local actions index | `.github/actions/README.md` | Repo maintainers | Shared actions + security posture (**recommended; not confirmed in repo**) |
| Security entrypoint | `.github/SECURITY.md` | Security owners | Disclosure/reporting + routing into `docs/security/**` (**not confirmed in repo**) |
| Governance anchors | `docs/governance/**` | Governance owners | Root governance, ethics, sovereignty (**not confirmed in repo**) |

### Definition of done (for this document)

- [ ] Front-matter complete + valid (`path/version/last_updated` updated; checksum computed in CI)
- [ ] Directory layout reflects the repo’s **actual** `.github/` contents (no stale references)
- [ ] CI “behavior contract” is explicit and consistent with KFM: validate → fail → skip
- [ ] Diagrams render correctly on GitHub
- [ ] Validation steps are listed and repeatable (commands may be placeholders, but intent is explicit)
- [ ] Governance + CARE/sovereignty expectations are stated and linked (no new policy invented here)
- [ ] No secrets, tokens, or sensitive locations are embedded
- [ ] Footer refs include governance + template anchors

---

## 🗂️ Directory Layout

### This document

- `path`: `.github/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Repo automation + community health | `.github/` | CI workflows, templates, security entrypoint |
| Workflows | `.github/workflows/` | GitHub Actions workflows (CI gates) |
| Local reusable actions | `.github/actions/` | Optional: reusable/composite actions used by workflows |
| Lineage kits | `.github/lineage/` | Optional: provenance + cross-link validators/docs |
| Repro kit | `.github/repro-kit/` | Optional: reproduction helpers for reviewers |
| GitHub Apps notes | `.github/apps/` | Optional: GitHub Apps / automation notes |
| Standards | `docs/standards/` | Markdown protocol, repo structure standard, STAC/DCAT/PROV profiles (**not confirmed in repo**) |
| Data domains | `data/` | Raw/work/processed + STAC/DCAT/PROV outputs |
| STAC outputs | `data/stac/` | STAC collections/items (catalog stage output) |
| DCAT outputs | `data/catalog/dcat/` | DCAT dataset/distribution metadata (catalog stage output) |
| PROV outputs | `data/prov/` | PROV bundles (lineage) |
| Pipelines | `src/pipelines/` | ETL, transforms, catalog build (canonical home) |
| Graph | `src/graph/` (+ optional `data/graph/`) | Ontology + ingest + import artifacts |
| APIs | `src/server/` | API layer + contracts (UI must not read Neo4j directly) |
| Web UI | `web/` | React + map UI, layer registries |
| Schemas | `schemas/` | JSON schemas + constraints for CI validation |
| Tests | `tests/` | Unit + integration + contract tests |
| Tools | `tools/` | Validators + CLI wrappers (no new canonical roots) |
| Runs / experiments | `mcp/` | Run logs and experiment artifacts |
| Telemetry (docs) | `docs/telemetry/` | Governance/ops metrics & reports (**not confirmed in repo**) |
| Security (docs) | `docs/security/` | Threat models, standards (**not confirmed in repo**) |
| Releases | `releases/` | Manifests, SBOMs, checksums (v13 target; may be placeholder until adopted) |

### Expected file tree for this sub-area

~~~text
📁 .github/
├── 📄 README.md                         # (this document)
├── 📁 workflows/                        # GitHub Actions workflows (CI gates)
│   ├── 📄 README.md                     # gate index + required checks (recommended)
│   └── 📄 *.yml                         # workflow files (list only if present in-repo)
├── 📁 actions/                          # optional: reusable/composite actions
│   ├── 📄 README.md                     # shared action inventory (recommended)
│   └── 📁 <action-name>/
│       └── 📄 action.yml
├── 📁 lineage/                          # optional: provenance + cross-link CI kits
│   ├── 📄 README.md
│   └── 📁 scripts/                      # optional
│       └── 📄 validate_lineage.<ext>
├── 📁 repro-kit/                        # optional: reproducibility helpers
│   └── 📄 README.md
├── 📁 apps/                             # optional: GitHub Apps / automation notes
│   └── 📄 README.md
├── 📁 ISSUE_TEMPLATE/                   # optional: issue templates
│   └── 📄 <template>.yml
├── 📄 pull_request_template.md          # optional: PR template
├── 📄 CODEOWNERS                        # optional: ownership + review routing
├── 📄 dependabot.yml                    # optional: dependency update config
├── 📄 FUNDING.yml                       # optional: funding config
└── 📄 SECURITY.md                       # recommended: security entrypoint (pairs with docs/security/**)
~~~

> GitHub-recognized community health files can also live at repo root (e.g., `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`, `SUPPORT.md`). Keep the canonical location consistent and documented.

### Compatibility note: v12 vs v13 catalog roots

KFM documents may differ on *how* the Catalogs stage is represented in file paths during migration:

- v13 blueprint (target): `data/stac/` + `data/catalog/dcat/` + `data/prov/`
- Some v12-era references include supporting mapping/docs under `docs/data/**` in addition to `data/stac/**`

**CI guidance:** validate the canonical outputs where they exist; avoid introducing *duplicate* catalog roots unless explicitly declared as migration targets and marked clearly as deprecated.

---

## 🧭 Context

### Background

- `.github/` is reserved for repository-level automation (CI) and community health files.
- In KFM, CI gates exist to keep contributions aligned to:
  - canonical pipeline ordering and invariants,
  - contract-first API boundaries,
  - provenance-first content rules,
  - schema-valid catalogs and governed story outputs.

### Operating assumptions

- `.github/workflows/**` changes can affect all pipeline stages (ETL → Catalogs → Graph → API → UI → Story Nodes → Focus Mode).
- Workflow security is **least-privilege by default**:
  - minimal `permissions:`,
  - secrets come from GitHub secrets/vars — never committed.
- CI runs should be **deterministic and auditable**:
  - diffable outputs,
  - stable IDs where applicable,
  - clear logs with ownership routing.

### Constraints / invariants (non-negotiable)

1. **Canonical pipeline ordering must hold**  
   ETL → Catalogs (STAC/DCAT/PROV) → Graph → API → UI → Story Nodes → Focus Mode.
2. **No UI direct-to-graph reads**  
   UI code in `web/` must not query Neo4j directly; all graph access is via `src/server/`.
3. **No unsourced narrative**  
   Published Story Nodes and Focus Mode outputs must be provenance-linked and must validate.
4. **Contracts are canonical**  
   Schemas belong in `schemas/`; API contracts belong under `src/server/` (e.g., `src/server/contracts/`), and must validate in CI.
5. **One canonical home per subsystem**  
   Avoid “shadow” duplicates (second API root, second UI root, extra data output roots). If legacy duplicates exist, treat them as migration targets.
6. **Data outputs are not code**  
   Derived datasets belong under `data/<domain>/processed/` and catalog outputs under canonical catalog roots — not under `src/` or `tools/`.
7. **CI behavior is predictable**  
   If a governed root exists, workflows validate it and fail deterministically on invalid artifacts. If an optional root is absent, skip rather than fail unless a baseline branch rule requires presence.
8. **No leakage via automation**  
   Workflow logs and artifacts must not disclose secrets or sensitive/restricted locations.
9. **Repo lint should prevent drift** (recommended baseline)  
   Lint gates should detect common drift signals such as:
   - YAML front-matter accidentally added to non-doc code files,
   - misnamed docs (e.g., `README.me`),
   - duplicate canonical roots without an explicit deprecation/migration marker.

### Change risk tiers (review expectations)

> Use this to decide when changes require heightened review and/or governance sign-off.

| Tier | Examples | Required review posture |
|---|---|---|
| Low | README/template text changes; issue templates; docs-only gates | Maintainer review recommended |
| Medium | New/modified validation gates; new composite action; dependency update workflows | Maintainer review required; consider security owner |
| High | Permission increases; use of `pull_request_target`; publishing releases; writing to repo; OIDC/attestations | Security owner + governance review; explicit rationale required |

### Repo drift vs v13-ready posture

The v13 blueprint expects top-level canonical folders and “one home per subsystem,” and calls out that CI must remain deterministic and use “validate if present; fail if invalid; skip if not applicable.” If the repo is not yet v13-ready (missing canonical roots), workflows must either:

- skip gates for absent optional roots (default), or
- enforce a declared baseline (e.g., a dedicated baseline branch or branch rules) that requires those roots to exist.

### Open questions

| Question | Owner | Target |
|---|---|---|
| Which workflows are configured as **required checks** for the default branch? | Repo maintainers | TBD |
| Do we standardize workflow naming + shared actions for schema validation? | Contracts owners | TBD |
| Do we adopt a release bundle convention under `releases/<version>/` (manifest + checksums + SBOM)? | Core maintainers | TBD |
| Where is the canonical “CI debug guide” documented? (`.github/workflows/README.md` vs `docs/`) | Repo maintainers | TBD |
| Do we require `schemas/` + `data/catalog/dcat/` + `data/prov/` as baseline roots for “v13-ready”? | Maintainers + governance | TBD |

### Future extensions (optional)

- Reusable composite actions for:
  - Markdown/front-matter validation,
  - schema validation (STAC/DCAT/PROV/storynodes/ui/telemetry),
  - provenance/link integrity checks (catalog ↔ Story Node evidence IDs).
- Supply-chain hygiene:
  - third-party actions pinned to commit SHAs,
  - dependency scanning,
  - SBOM + provenance attestations for release bundles.
- `.github/lineage/` as canonical home for provenance + cross-link gate documentation and shared validator scripts.
- `.github/repro-kit/` as canonical home for local reproduction ergonomics.

---

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
  CI --> UI[UI registry + build + a11y checks]
  CI --> STORY[Story Node validation]
  CI --> SEC[Security posture gates<br/>secrets + permissions]

  ETL[ETL] --> STAC[STAC] --> DCAT[DCAT] --> PROV[PROV] --> N4J[Neo4j Graph] --> APIS[APIs] --> WEB[React/Map UI] --> SN[Story Nodes] --> FM[Focus Mode]

  LINT --> OK[Merge eligible]
  DOCS --> OK
  SCHEMA --> OK
  PIPE --> OK
  GRAPH --> OK
  API --> OK
  UI --> OK
  STORY --> OK
  SEC --> OK
~~~

### Workflow composition (recommended pattern)

~~~mermaid
flowchart TD
  WF["Workflow\n.github/workflows/*.yml"] --> A["Local action(s)\n.github/actions/*"]
  A --> C1["Check: Markdown protocol + front-matter"]
  A --> C2["Check: Schemas (STAC/DCAT/PROV/storynodes/ui/telemetry)"]
  A --> C3["Check: Tests (pipelines/graph/api/ui)"]
  A --> C4["Check: Security posture (permissions/secrets/pinning)"]
~~~

---

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| PR/push/workflow events | GitHub event payload | GitHub | GitHub event schema |
| Workflow definitions | YAML | `.github/workflows/**` | YAML parse + action linting (if configured) |
| Local actions | YAML + scripts | `.github/actions/**` | YAML parse + code review + tests (if present) |
| Community health files | Markdown/YAML | `.github/**` | Markdown protocol checks (when governed) |
| Contract artifacts | Mixed | `schemas/**`, `docs/**`, `src/**`, `data/**` | Schema + contract + test gates |

### Outputs

| Output | Format | Where | Contract / Schema |
|---|---|---|---|
| CI status checks | Check runs | GitHub UI | Required-check policy (repo settings) |
| Validation reports | Logs/artifacts | GitHub Actions artifacts | Retention + redaction rules |
| Optional release bundles | Files | `releases/<version>/` | Manifest + checksums (+ SBOM if adopted) |

### Sensitivity & redaction

- Treat workflow logs and artifacts as potentially public.
- Never print:
  - secrets/tokens,
  - raw sensitive locations,
  - restricted cultural knowledge details.
- If CI touches restricted layers, ensure redaction/generalization is applied at the API + Story Node layers, and CI artifacts do not leak restricted details.

### Quality signals (what “good” looks like)

- Minimal workflow permissions (`permissions:` scoped to each job).
- Third-party actions pinned to immutable versions (prefer commit SHAs).
- Deterministic outcomes (avoid flakey checks; stable ordering; fixed seeds where applicable).
- Failures are actionable (clear error, subsystem owner pointer, reproducible steps).
- Gates validate canonical outputs in canonical locations (no “shadow roots”).

---

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

- Schema versions: SemVer + changelog; breaking changes require coordinated contract bumps.
- Catalog outputs should be deterministic and diffable (same inputs → same outputs).

---

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| CI (GitHub) | Gate orchestration | GitHub checks + artifacts |
| Repo lint | Enforce canonical roots + “no duplicates” posture | Lint reports + CI failure |
| Pipelines | Ingest/transform/build catalogs | `src/pipelines/**` outputs to `data/**` |
| Catalogs | STAC/DCAT/PROV generation + validation | JSON + validators |
| Graph | Neo4j build + integrity | `src/graph/**` (+ optional `data/graph/**`) |
| APIs | Contracted access layer | REST/GraphQL (contract-first) |
| UI | Map + narrative UX | API calls only (no direct graph calls) |
| Story Nodes | Governed narrative artifacts | `docs/reports/story_nodes/**` |
| Telemetry | Observability + governance signals | `docs/telemetry/**` + `schemas/telemetry/**` |
| Security | Policy + technical standards | `.github/SECURITY.md` + `docs/security/**` |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| Workflows | `.github/workflows/` | Reviewed; breaking gate changes require governance/security review |
| Local actions | `.github/actions/` | Treat like code: tests + review; pin dependencies |
| Lineage gate docs/scripts | `.github/lineage/` | Keep docs + scripts aligned with workflow behavior |
| JSON schemas | `schemas/` | SemVer + changelog |
| API contracts | `src/server/contracts/` | Contract tests required |
| UI registry | `web/**` | Schema-validated |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Governed narrative structure |
| Release bundles | `releases/<version>/` | Version-pinned; include manifest + checksums (+ SBOM if adopted) |

### Canonical roots CI may depend on

When a gate validates a subsystem, it should reference these canonical roots (skip if absent unless baseline rules require it):

- `.github/`
- `docs/`
- `schemas/`
- `data/` (including `data/stac/`, `data/catalog/dcat/`, `data/prov/`)
- `src/pipelines/`
- `src/graph/` (+ optional `data/graph/`)
- `src/server/`
- `web/`
- `tests/`
- `tools/`
- `mcp/`
- `releases/`

### Extension points checklist

- [ ] CI: add a new gate/workflow with minimal permissions and clear ownership
- [ ] Docs: governed Markdown validates + links resolve
- [ ] Schemas: new schema files are referenced and validated
- [ ] Data: new domain added under `data/<domain>/...` (raw/work/processed)
- [ ] STAC/DCAT/PROV: outputs validate and remain deterministic
- [ ] Graph: new labels/relations mapped + migration plan
- [ ] APIs: contract version bump + tests
- [ ] UI: registry entry + access rules
- [ ] Story/Focus: provenance references enforced
- [ ] Telemetry: new signals + schema version bump

---

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode

CI gates here protect Focus Mode quality by ensuring:

- Story Nodes validate (front-matter, evidence refs, entity references, redaction compliance).
- Evidence artifacts (STAC/DCAT/PROV + PROV bundles) remain consistent and traceable.
- The UI only consumes data through the API boundary (no direct graph access).

### Provenance-linked narrative rule

- Every factual claim shown to users must trace to a dataset/record/asset ID.
- Predictive or AI-generated content must be opt-in and carry uncertainty/confidence metadata.

### Optional structured controls

N/A for `.github/` docs. Focus Mode controls live in Story Node front-matter under `docs/reports/story_nodes/**`.

---

## 🧪 Validation & CI/CD

### CI behavior contract

When writing or modifying workflows, each gate must be predictable:

- **Validate if present:** if a canonical root exists (or changes), validate its artifacts.
- **Fail if invalid:** schema errors, broken links, orphan references fail deterministically.
- **Skip if not applicable:** optional roots absent → skip without failing the overall pipeline (unless baseline rules require the root).

### Event context & fork safety (recommended)

> Treat “untrusted” code as any code coming from outside the protected branch context.

| Trigger type | Typical use | Trust level | Secrets allowed | Write operations allowed | Notes |
|---|---|---|---|---|---|
| `pull_request` (fork) | Validate contributions | Untrusted | **No** | **No** | Preferred for PR validation; keep checks deterministic and read-only |
| `pull_request` (same repo branch) | Validate contributions | Usually untrusted-by-default | Prefer “no” unless explicitly approved | Prefer “no” | Still run as untrusted unless you have a strong reason otherwise |
| `push` to protected branches | Build/publish from reviewed code | Trusted | Yes (scoped) | Yes (scoped) | Keep privileged tasks here (releases, publishing) |
| Manual approvals / Environments | Publish/deploy | Trusted w/ approvals | Yes (scoped) | Yes (scoped) | Prefer for any publication step |
| `pull_request_target` | Special cases only | High risk | Yes (dangerous) | Yes (dangerous) | Avoid unless explicitly threat-modeled and approved |

### Minimum checks (recommended baseline)

> Exact workflow names/commands belong in `.github/workflows/README.md` (**recommended; not confirmed in repo**).

- [ ] Markdown protocol checks (governed docs + front-matter)
- [ ] Link integrity checks for governed docs (if tooling exists)
- [ ] Schema validation (when present):
  - STAC/DCAT/PROV outputs
  - Story Nodes
  - UI registry schemas
  - Telemetry schemas
- [ ] ETL/Catalog unit + integration tests (when present)
- [ ] Graph integrity checks (when present)
- [ ] API contract tests (when present)
- [ ] UI checks (registry + build + a11y) (when present)
- [ ] Security posture checks (secrets handling, minimal permissions, dependency scanning)

### Recommended permissions pattern (least privilege)

~~~yaml
# Example pattern (adjust to what the job actually needs)
permissions:
  contents: read

jobs:
  validate:
    permissions:
      contents: read
      actions: read
    steps:
      - uses: actions/checkout@<PINNED-REF>
~~~

### Recommended action pinning posture

- Prefer pinning third-party actions to immutable refs (commit SHA) for supply-chain resilience.
- Prefer local composite actions in `.github/actions/**` for shared logic; treat them like code:
  - tests where possible,
  - version pinning for any dependencies they invoke,
  - documented inputs/outputs in `.github/actions/README.md` (recommended).

~~~yaml
# Example only: pin to a commit SHA once selected
- uses: actions/checkout@<COMMIT-SHA>
~~~

### Artifacts & logging posture

- Minimize artifact uploads; prefer uploading only:
  - machine-readable validation reports,
  - redacted logs,
  - small diffable summaries.
- Never upload:
  - raw secrets,
  - raw restricted/sensitive geospatial layers,
  - unredacted “sensitive location” outputs.
- Prefer short retention unless otherwise required by governance/ops policy.

### Reproduction (local)

~~~bash
# Placeholders — replace with repo-specific commands and keep them in sync with workflows.

# 1) validate governed markdown + front-matter
# 2) validate schemas (STAC/DCAT/PROV + story nodes + UI + telemetry)
# 3) validate lineage bundles + cross-links (if lineage gate exists)
# 4) run unit/integration tests (pipelines/graph/api/ui)
# 5) run security checks (secrets scan, dependency scan, action lint)
~~~

### Workflow security hardening checklist

- [ ] Use minimal `permissions:` (prefer job-level permissions; default to read-only).
- [ ] Do not expose secrets to untrusted PR code (especially from forks).
- [ ] Pin third-party actions to immutable versions (prefer commit SHAs).
- [ ] Avoid `pull_request_target` unless explicitly approved and threat-modeled (baseline: avoid).
- [ ] Prefer reproducible toolchains (pinned language/runtime versions; lockfiles).
- [ ] Keep artifacts redacted and minimize retention of sensitive outputs.
- [ ] Treat any write operations (releases, tags, publishing) as privileged workflows with explicit approvals.

### Telemetry signals (canonical homes)

| Signal | Source | Where recorded |
|---|---|---|
| CI run logs + artifacts | GitHub Actions | GitHub Actions UI / artifacts |
| Gate health reports | CI | GitHub artifacts; optionally mirrored into `docs/telemetry/` (**not confirmed in repo**) |
| Pipeline telemetry | Pipelines + CI | `docs/telemetry/` + `schemas/telemetry/` (**not confirmed in repo**) |
| Release telemetry | Release workflows | `releases/<version>/telemetry.json` (if adopted) |

---

## ⚖ FAIR+CARE & Governance

### Review gates

- Changes to `.github/workflows/**` should require maintainer review.
- Any change that relaxes validation, increases permissions, alters publication behavior, or touches security/sovereignty gates **requires human review**.
- Workflow changes must not introduce new policy text; policy belongs in governance/security docs.

### CARE / sovereignty considerations

If workflows affect restricted locations or culturally sensitive knowledge:

- enforce generalization/redaction rules at the API + Story Node layers,
- prevent sensitive artifacts from being uploaded as CI artifacts,
- document the review gate that approves publication.

### Recommended automated sovereignty/sensitivity checks (where feasible)

These are examples of the kinds of checks KFM may encode as CI gates (without redefining policy in CI):

- **Sensitive location leakage** checks: prevent publication/artifacts if restricted/sensitive locations are present without redaction.
- **Classification propagation** checks: prevent “higher classification → lower classification output” without review.

> The policy thresholds and decision rules must remain defined in `docs/governance/**` (or `docs/security/**`)—CI should only enforce what those documents declare.

### AI usage constraints

- Ensure this document’s AI permissions/prohibitions in front-matter match intended use.
- Do not use automation to introduce new policy text without governance review.
- Do not use AI to infer sensitive locations.

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0-draft | 2025-12-23 | Initial `.github/` README scaffolding | TBD |
| v1.0.1-draft | 2025-12-23 | Align with Master Guide v12; add CI behavior contract; expand directory layout | TBD |
| v1.0.2-draft | 2025-12-26 | Normalize `.github/` pointers; clarify “one canonical home” invariant; expand security posture + baseline checks | TBD |
| v1.0.3-draft | 2025-12-27 | Tighten alignment to v13 blueprint + Master Guide; add change risk tiers; clarify security entrypoint + canonical roots; reduce ambiguity around optional vs baseline gates | TBD |
| v1.0.4-draft | 2025-12-28 | Align more tightly to Universal Doc template; add glossary linkage; expand fork-safety/permissions patterns; clarify v12 vs v13 catalog-root compatibility; add recommended sovereignty/sensitivity checks without inventing policy | TBD |

---

Footer refs:

- Master guide: `docs/MASTER_GUIDE_v12.md`
- v13 redesign blueprint: `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Markdown work protocol: `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` (**not confirmed in repo**)
- Repo structure standard: `docs/standards/KFM_REPO_STRUCTURE_STANDARD.md` (**not confirmed in repo**)
- Template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- API contract extension template: `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`