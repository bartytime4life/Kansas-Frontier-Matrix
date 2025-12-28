---
title: "Kansas Frontier Matrix — Changelog"
path: "CHANGELOG.md"
version: "v12.0.1-draft"
last_updated: "2025-12-28"
status: "draft"
doc_kind: "Changelog"
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

doc_uuid: "urn:kfm:doc:changelog:v12.0.1-draft"
semantic_document_id: "kfm-changelog-v12.0.1-draft"
event_source_id: "ledger:kfm:doc:changelog:v12.0.1-draft"
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

# Changelog

All notable changes to the **Kansas Frontier Matrix (KFM)** repository are documented in this file.

This changelog is intended to support traceability across the canonical KFM pipeline:

**ETL → STAC/DCAT/PROV catalogs → Graph → API → UI → Story Nodes → Focus Mode**  
*(Pipeline ordering is non-negotiable; see `docs/MASTER_GUIDE_v12.md`.)*

The format is based on *Keep a Changelog*, and the project aims to follow *Semantic Versioning* (SemVer).

## 📘 Overview

### Purpose

- Provide a single, repo-level ledger of notable changes across **all** pipeline stages.
- Preserve provenance and auditability by recording identifiers (STAC/DCAT/PROV IDs, run IDs, schema/contract versions, release manifests).
- Support v13 readiness/compliance expectations by ensuring repository-wide changes are traceable and reviewable.

### Scope

| In scope | Out of scope |
| --- | --- |
| Any change that affects pipeline outputs, contracts, schemas, stable identifiers, or user-visible behavior | Local dev environment notes that do not land in the repo |
| New/updated datasets with catalog + provenance artifacts | Personal TODOs (track as issues instead) |
| Governance/security changes, redaction rules, or sovereignty handling | Private incident details (use SECURITY processes) |
| Focus Mode behavior changes (citation rendering, evidence bundling) | Raw research notes not tied to a governed artifact |

### Audience

- Maintainers (DataOps / Catalog / Graph / API / UI / Story)
- Contributors submitting PRs
- Reviewers validating provenance, standards, and governance compliance

### Definitions

- **Contract baseline**: pinned protocol/profile versions that define validation requirements across the pipeline.
- **Stable identifier**: a long-lived ID intended to survive refactors (dataset IDs, STAC collection IDs, ontology IDs, etc.).
- **Run ID**: a deterministic identifier for an ETL/catalog/graph activity recorded in PROV and/or MCP run manifests.
- **Story Node**: a governed narrative artifact that is machine-ingestible and provenance-linked.
- **Focus Mode**: an experience that consumes only provenance-linked context bundles (no unsourced narrative).

### Key artifacts

| Artifact | Purpose | Canonical path |
| --- | --- | --- |
| Master Guide v12 | Pipeline order, invariants, and system inventory | `docs/MASTER_GUIDE_v12.md` |
| v13 Redesign Blueprint | Canonical homes per subsystem + v13 readiness gates | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` |
| Universal doc template | Default governed documentation structure | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` |
| Story Node template | Evidence-linked narrative structure | `docs/templates/TEMPLATE__STORY_NODE_V3.md` |
| API contract extension template | Contract-first API change proposals | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` |

### Definition of done

A changelog update is considered complete when:

- [ ] Each bullet is tagged with at least one stage tag (`[ETL]`, `[Catalog]`, `[Graph]`, `[AI]`, `[API]`, `[UI]`, `[Story]`, `[Focus]`, `[Docs]`, `[Governance/Security]`).
- [ ] Entries include required identifiers when applicable:
  - STAC: `collection/<id>` and/or `item/<id>`
  - DCAT: `<dataset-id>`
  - PROV: `activity/<id>` and/or `run/<id>`
  - MCP: `mcp/runs/<run_id>/…` (manifest/evals) when applicable
  - Schemas/contracts: name + version
- [ ] Any breaking change includes migration notes and a downstream impact summary.
- [ ] Any sensitive-content change includes redaction/scope notes and references the governance review artifact (no restricted details in the changelog).
- [ ] If a release is cut, `releases/<x.y.z>/` contains a manifest + checksums (and SBOM/attestations if used).

## 🔁 Baselines to keep in sync

When any item below changes, add a bullet under **[Unreleased]** and update the baseline table(s).

### Minimum contract set

The following are the minimum contract artifacts expected to stay aligned:

- `KFM-MDP` (Markdown protocol)
- `KFM-PPC` (Pipeline contract)
- `KFM-STAC` / `KFM-DCAT` / `KFM-PROV` (catalog profiles)
- `KFM-ONTO` (ontology protocol)
- `MCP-DL` (delivery layer / runs & evidence products)

### Protocol and contract baselines

| Baseline | Current | Source of truth | Change triggers |
| --- | --- | --- | --- |
| Markdown protocol | `KFM-MDP v11.2.6` | Master Guide / Blueprint | Rules for headings/fences/metadata |
| MCP delivery layer | `MCP-DL v6.3` | Master Guide / Blueprint | Run manifests, evidence products, eval harness |
| Ontology protocol | `KFM-ONTO v4.1.0` | Master Guide / Blueprint | Graph label/relation standards |
| Pipeline contract | `KFM-PPC v11.0.0` | Master Guide / Blueprint | Boundary/invariants (ETL→Catalog→Graph→API→UI→Story→Focus) |
| STAC profile | `KFM-STAC v11.0.0` | Master Guide / Blueprint | STAC schema/profile changes |
| DCAT profile | `KFM-DCAT v11.0.0` | Master Guide / Blueprint | DCAT mapping/schema changes |
| PROV profile | `KFM-PROV v11.0.0` | Master Guide / Blueprint | Provenance schema/profile changes |

### Documentation baselines

| Document | Version | Last updated | Notes |
| --- | --- | --- | --- |
| Master Guide | `v12.0.1-draft` | `2025-12-27` | Canonical pipeline + invariants |
| v13 Redesign Blueprint | `v13.0.0-draft` | `2025-12-21` | Canonical roots + v13 readiness gates |

## 🗂️ Directory layout reference

This changelog expects changes to land in canonical homes (one home per subsystem).

### Canonical homes by stage

| Pipeline stage | Canonical paths (examples) | Notes |
| --- | --- | --- |
| ETL | `src/pipelines/**`, `data/raw/**`, `data/work/**`, `data/processed/**` | Deterministic, idempotent runs |
| Catalog | `data/stac/**`, `data/catalog/dcat/**`, `data/prov/**` | Schema-validated STAC/DCAT/PROV |
| Graph | `src/graph/**`, `data/graph/csv/**`, `data/graph/cypher/**` | Ontology-governed ingest + import artifacts |
| API | `src/server/**` | UI must not read Neo4j directly |
| UI | `web/**` | Map/UI rendering + layer registry + Focus Mode UI |
| Story | `docs/reports/story_nodes/**` | Story Nodes (draft/published split if defined) |
| Docs | `docs/**` | Governed documentation (templates, architecture, guides) |
| Governance/Security | `docs/governance/**`, `.github/**`, `SECURITY.md` | Review gates, scanning, redaction |

### Repo top-levels expected

~~~text
📁 .github/
├── 📁 workflows/
└── 📄 SECURITY.md                         # if present

📁 data/
├── 📁 raw/
│   └── 📁 <domain>/
├── 📁 work/
│   └── 📁 <domain>/
├── 📁 processed/
│   └── 📁 <domain>/
├── 📁 stac/
│   ├── 📁 collections/
│   └── 📁 items/
├── 📁 catalog/
│   └── 📁 dcat/
├── 📁 prov/
├── 📁 graph/
│   ├── 📁 csv/
│   └── 📁 cypher/
└── 📄 README.md

📁 docs/
├── 📄 MASTER_GUIDE_v12.md
├── 📁 templates/
│   ├── 📄 TEMPLATE__KFM_UNIVERSAL_DOC.md
│   ├── 📄 TEMPLATE__STORY_NODE_V3.md
│   └── 📄 TEMPLATE__API_CONTRACT_EXTENSION.md
├── 📁 architecture/
│   ├── 📄 KFM_REDESIGN_BLUEPRINT_v13.md
│   ├── 📄 KFM_NEXT_STAGES_BLUEPRINT.md
│   └── 📄 KFM_VISION_FULL_ARCHITECTURE.md
└── 📁 reports/
    └── 📁 story_nodes/

📁 mcp/
├── 📁 runs/
└── 📁 experiments/

📁 schemas/
├── 📁 stac/
├── 📁 dcat/
├── 📁 prov/
├── 📁 story_nodes/
├── 📁 ui/
└── 📁 telemetry/

📁 src/
├── 📁 pipelines/
├── 📁 graph/
└── 📁 server/

📁 web/
📁 tests/
📁 tools/
📁 releases/
~~~

## 🧪 Validation and CI expectations

If your change impacts these areas, note it in the changelog and ensure the corresponding checks stay green:

- Markdown protocol checks (KFM-MDP)
- Schema validation (STAC/DCAT/PROV + any domain schemas in `schemas/`)
- Graph integrity checks (ontology + ingest fixtures)
- API contract tests (REST/OpenAPI and/or GraphQL)
- UI schema checks (layer registry, accessibility, citation rendering)
- Security + sovereignty checks (as applicable)

Repository hygiene expectations:

- No YAML front-matter in **code files** (docs are allowed).
- One canonical home per subsystem; duplicates require explicit deprecation markers.
- CI workflows should be deterministic: validate if present; fail if invalid; skip if not applicable.

## [Unreleased]

### Added
- **[Docs][Governance/Security]** Upgraded `CHANGELOG.md` into a pipeline-synced, contract-aware changelog (baseline tables, stage tags, release metadata checklist).
- **[Docs][Governance/Security]** Added explicit “sync points” so changes to contracts/schemas/templates trigger a changelog entry.
- **[Docs]** Added `[Focus]` and `[Docs]` stage tags to reflect Focus Mode and documentation changes explicitly.

### Changed
- **[Docs]** Updated directory layout references to match the Master Guide and v13 blueprint canonical homes (including `data/graph/csv/` + `data/graph/cypher/`).
- **[Docs]** Corrected SemVer bump examples to use `X.Y.Z` notation (instead of `0.Y.0` / `0.0.Z`).
- **[Docs]** Expanded “Definition of done” to include MCP run/evidence references and release manifests.

### Deprecated

### Removed

### Fixed

### Security

---

## Changelog entry guidance

### Stage tags

Every bullet MUST start with at least one stage tag:

- `[ETL]`
- `[Catalog]`
- `[Graph]`
- `[AI]`
- `[API]`
- `[UI]`
- `[Story]`
- `[Focus]`
- `[Docs]`
- `[Governance/Security]`

If multiple stages are impacted, use multiple tags (example: `[ETL][Catalog]`).

### Identifier conventions

Prefer stable identifiers with explicit prefixes:

- `DOC:` `<semantic_document_id>` (for governed docs)
- `STAC:` `collection/<id>` and/or `item/<id>`
- `DCAT:` `<dataset-id>`
- `PROV:` `activity/<id>` and/or `run/<id>`
- `MCP:` `run/<id>` (and/or `mcp/runs/<id>/manifest.json`)
- `SCHEMA:` `<schema-name>@<semver>`
- `API:` `<contract-name>@<semver>` + endpoint(s)
- `ADR:` `ADR-####-<slug>`

### Entry anatomy

A good changelog bullet is:

- short, user-meaningful, and stage-tagged
- stable-ID aware (IDs that downstream code depends on are explicit)
- provenance-aware (mentions run/prov artifacts when outputs changed)
- contract-aware (calls out API/schema changes explicitly)

Recommended additional refs (when available):

- `PR:` `<number>`  
- `ISSUE:` `<number>`  
- `COMMIT:` `<sha>`

### Release entry template

Use this skeleton when cutting a new version:

~~~markdown
## [x.y.z] - YYYY-MM-DD

### Release meta
- Repo version: `x.y.z`
- Contract baseline: `KFM-PPC …` | `KFM-STAC …` | `KFM-DCAT …` | `KFM-PROV …`
- Release artifacts: `releases/x.y.z/**` (manifest, checksums, optional SBOM/attestations)
- Breaking changes: yes/no

### Added
- **[Stage]** …

### Changed
- **[Stage]** …

### Deprecated
- **[Stage]** …

### Removed
- **[Stage]** …

### Fixed
- **[Stage]** …

### Security
- **[Stage]** …
~~~

### SemVer bump rules

- **MAJOR** (`X.0.0`): breaking change to stable identifiers, schemas, API contracts, or ontology/graph migrations that require downstream changes.
- **MINOR** (`X.Y.0`): additive features (new datasets, new endpoints, new Story Nodes, backwards-compatible schema additions).
- **PATCH** (`X.Y.Z`): fixes and refactors that do not change contracts or published outputs.

### What requires a changelog entry

Add a changelog bullet when any of the following change:

- `docs/MASTER_GUIDE_v12.md` or `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` (contract/protocol/version changes)
- Anything under `docs/templates/**` (template changes that affect governed docs)
- Anything under `schemas/**` (schema additions/changes/removals)
- Any published STAC/DCAT/PROV artifacts under `data/stac/**`, `data/catalog/dcat/**`, `data/prov/**`
- Graph ingest artifacts under `src/graph/**` and/or `data/graph/**`
- API contract or behavior changes under `src/server/**`
- UI layer registry or user-visible behavior changes under `web/**` (including Focus Mode)
- New/updated Story Nodes under `docs/reports/story_nodes/**`
- Any MCP runs/evals that are referenced as evidence products under `mcp/runs/**`
- Any release packaging changes under `releases/**`
- Any redaction/sensitivity handling change (record under **Security** and/or **Governance/Security**)

### Governance and sensitive content

When changes involve culturally sensitive knowledge or restricted locations:

- Record the redaction/generalization approach and the affected artifacts (API redaction + Story Node review gates).
- Do not include restricted location details in the changelog; reference the internal governance review artifact instead.

## 🕰️ Document version history

| Version | Date | Summary |
| --- | --- | --- |
| `v12.0.0-draft` | `2025-12-27` | Upgraded the changelog to align with KFM pipeline stages and contract baselines. |
| `v12.0.1-draft` | `2025-12-28` | Aligned directory layout + tags with Master Guide/v13 blueprint; corrected SemVer examples; expanded DoD + identifiers. |
