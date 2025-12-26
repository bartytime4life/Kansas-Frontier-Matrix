---
title: "KFM Lineage — Scripts"
path: ".github/lineage/scripts/README.md"
version: "v1.0.0"
last_updated: "2025-12-26"
status: "draft"
doc_kind: "README"
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

doc_uuid: "urn:kfm:doc:ci:lineage:scripts-readme:v1.0.0"
semantic_document_id: "kfm-ci-lineage-scripts-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:ci:lineage:scripts-readme:v1.0.0"
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

# KFM Lineage — Scripts

## 📘 Overview

### Purpose

- Provide a **single, discoverable home** for optional scripts used to validate KFM lineage artifacts (PROV) and catalog cross-links (STAC/DCAT) during local development and CI.
- Keep lineage enforcement **deterministic, diffable, and auditable** as the project expands to new domains and new story/evidence products.

### Scope

| In Scope | Out of Scope |
|---|---|
| Running/authoring validation scripts for lineage + cross-link rules | Implementing ETL jobs or domain transforms (see `src/pipelines/`) |
| Producing machine-readable reports for CI annotations / artifacts | Writing governance policy (see `docs/governance/`) |
| Read-only validation against repo-local files and schemas | Fetching remote data (network I/O) |
| Checks that support the canonical pipeline ordering and API boundary | UI/UX features (see `web/`) |

### Audience

- Primary: CI/pipeline maintainers; contributors adding/refreshing data domains.
- Secondary: governance/security reviewers; graph/API/UI contributors who rely on provenance completeness.

### Definitions (link to glossary)

- Link: `docs/glossary.md` *(not confirmed in repo)*
- Terms used in this doc:
  - **lineage gate**: the minimum set of validations that must pass before publishing/merging lineage-bearing artifacts.
  - **PROV bundle**: W3C PROV(-O) serialized provenance for derivations/activities.
  - **OpenLineage event**: an optional event-format lineage record emitted by pipelines *(not confirmed in repo)*.
  - **cross-link**: an explicit reference from one artifact to another (e.g., STAC → PROV, DCAT → STAC, graph/story → STAC IDs).

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Lineage overview + invariants | `.github/lineage/README.md` | CI/Pipeline maintainers | Parent rules and expectations |
| Canonical pipeline ordering | `docs/MASTER_GUIDE_v12.md` | Docs team | Non-negotiable system flow |
| Next stages blueprint | `docs/architecture/KFM_NEXT_STAGES_BLUEPRINT.md` | Architecture | Roadmap + repo gap inventory *(may be a planned path)* |
| STAC outputs | `data/stac/` | Data domains | Collections + Items (by domain) |
| DCAT outputs | `data/catalog/dcat/` | Catalog builders | Dataset/distribution discovery metadata |
| PROV outputs | `data/prov/` | Pipelines | Lineage bundles (derivations, activities) |
| Validation schemas | `schemas/` | Schema maintainers | JSON Schemas (and optional SHACL) |
| CI entrypoints | `.github/workflows/` | CI maintainers | Workflows call these scripts |

> Note: Some canonical directories (e.g., `schemas/`, `data/catalog/dcat/`, `data/prov/`) are referenced by standards but may be absent in some repo states. This README assumes **skip-if-absent / fail-if-invalid** behavior.

### Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] Script interface expectations documented (inputs/outputs/exit codes)
- [ ] Minimum lineage gate defined (required vs advisory checks)
- [ ] CI integration pattern documented (skip/fail semantics)
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document

- `path`: `.github/lineage/scripts/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| GitHub automation | `.github/` | Workflows, lineage checks, (optional) validators |
| Lineage rules | `.github/lineage/` | High-level lineage policy + invariants |
| Lineage scripts | `.github/lineage/scripts/` | Executable validators (this folder) |
| Data domains | `data/` | Raw/work/processed + published STAC outputs |
| STAC catalog | `data/stac/` | STAC Collections + Items |
| DCAT catalog | `data/catalog/dcat/` | DCAT JSON-LD datasets + distributions |
| Provenance | `data/prov/` | PROV bundles |
| Schemas | `schemas/` | Schemas for STAC/DCAT/PROV/story/UI/telemetry |
| Pipelines | `src/pipelines/` | Deterministic ETL + catalog generation |
| Graph | `src/graph/` | Ontology bindings + graph ingest tooling |
| API boundary | `src/server/` | API contracts + redaction + query services |
| Story Nodes | `docs/reports/story_nodes/` | Draft/published story content *(expected)* |

### Expected file tree for this sub-area

~~~text
📁 .github/
└── 📁 lineage/
    ├── 📄 README.md                          # Lineage overview + invariants
    └── 📁 scripts/
        ├── 📄 README.md                      # (this file)
        ├── 📄 validate_lineage.<ext>         # optional; not confirmed in repo
        ├── 📄 validate_prov.<ext>            # optional; not confirmed in repo
        ├── 📄 validate_catalog_links.<ext>   # optional; not confirmed in repo
        └── 📁 lib/                           # optional; not confirmed in repo
~~~

## 🧭 Context

### Background

KFM’s canonical flow is:

**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

Lineage and provenance are treated as first-class so that:

- Story Nodes / Focus Mode can only surface **provenance-linked content**.
- Missing evidence IDs and broken cross-links are caught early via CI.
- Outputs remain deterministic and diffable for audits and reproducible builds.

This folder exists to keep validator code close to the CI entrypoints while remaining discoverable and governed.

### Assumptions

- Canonical roots exist (or are being created) for `schemas/`, `data/catalog/dcat/`, and `data/prov/`.
- PROV bundle serialization and validation toolchain are selected and pinned by maintainers *(tooling not specified here)*.

### Constraints / invariants

- Canonical ordering is preserved: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- **API boundary is mandatory**: the UI never queries Neo4j directly; it consumes contracted API responses.
- CI behavior must be deterministic:
  - If an optional root is absent, jobs may **skip** with a clear message.
  - If a required root is present but invalid, jobs **fail** with actionable errors.
- Scripts must be safe-by-default:
  - no network calls,
  - no secrets,
  - no leaking sensitive locations via logs/reports.

## 🗺️ Diagrams

### Lineage gate in the canonical pipeline

~~~mermaid
flowchart LR
  A[ETL] --> B[STAC/DCAT/PROV outputs]
  B --> C[Graph (Neo4j)]
  C --> D[API layer]
  D --> E[UI + Story Nodes + Focus Mode]

  P[PR / local change] --> CI[CI job]
  CI --> S[Lineage scripts]
  S --> R[Report + exit code]
  R -->|pass| M[Merge OK]
  R -->|fail| F[Fix required]
~~~

## 🧱 Architecture

### Script inventory

This table is the “contract surface” for scripts that live here.

| Script | Purpose | Inputs | Output | Status |
|---|---|---|---|---|
| `validate_lineage.<ext>` | End-to-end lineage gate (PROV + cross-links) | repo paths | JSON report + summary | optional; not confirmed in repo |
| `validate_prov.<ext>` | Validate PROV bundles | `data/prov/` + schemas | report | optional; not confirmed in repo |
| `validate_catalog_links.<ext>` | Validate STAC/DCAT references and links to PROV | `data/stac/`, `data/catalog/dcat/` | report | optional; not confirmed in repo |

### Script contract (recommended)

These scripts are intended to be called from CI and locally. To keep them composable:

- **Inputs**: repo-local paths only (no network calls)
- **Outputs**: machine-readable report + human summary
- **Side effects**: none (read-only); write reports only to an explicit output path
- **Determinism**: stable ordering; stable identifiers in reports; no timestamps unless passed in

#### CLI shape

*(Examples are placeholders — not confirmed in repo.)*

~~~bash
# Example: end-to-end lineage gate
# (validate PROV + validate cross-links into STAC/DCAT + report orphans)
./.github/lineage/scripts/validate_lineage.<ext> \
  --repo-root . \
  --prov-dir data/prov \
  --stac-dir data/stac \
  --dcat-dir data/catalog/dcat \
  --schemas-dir schemas \
  --report-out mcp/runs/<run-id>/lineage_report.json
~~~

#### Exit codes (recommended)

| Code | Meaning |
|---:|---|
| 0 | All required checks passed |
| 1 | Validation failure (action required) |
| 2 | Configuration error (bad args / missing required paths) |
| 3 | Internal error (bug) |

### Report format (recommended)

- Emit JSON with at least:
  - `run_id` (caller supplied)
  - `checked_paths`
  - `schema_versions` (if applicable)
  - `errors[]` and `warnings[]` with stable identifiers
  - `summary` counts for dashboards

## 🌐 STAC, DCAT & PROV Alignment

### Minimal “lineage gate” (MVP)

The default gate should stay small and strict; additional checks can be advisory.

**Required (fail CI):**

- PROV bundles parse and conform to the chosen PROV profile (format TBD).
- Any artifact claiming a PROV link actually resolves to an existing file.
- No orphan evidence IDs in “published” outputs (definition owned by maintainers).

**Advisory (warn CI):**

- Missing optional catalogs (e.g., DCAT) when a domain is still onboarding.
- Missing schema pins (until `schemas/` is populated).

### Cross-link checks (examples)

| Check | What it prevents |
|---|---|
| STAC item references missing assets | Broken map layers / missing downloads |
| DCAT dataset references missing distributions | Catalog discoverability drift |
| PROV derivation points to non-existent input/output | Un-auditable transformations |
| Story references missing evidence IDs | Unsourced narrative |

## 🧪 Validation & CI/CD

### Local run

*(Placeholders — replace with repo-specific commands.)*

~~~bash
# Run the lineage gate locally (if scripts exist)
./.github/lineage/scripts/validate_lineage.<ext> --help
~~~

### CI integration pattern

- Workflows under `.github/workflows/` call these scripts as a job step when PRs touch:
  - `data/**`, `schemas/**`, `docs/reports/story_nodes/**`, `src/pipelines/**`, `src/graph/**`
- Deterministic rules:
  - **Skip** if the relevant catalog/prov directories do not exist yet.
  - **Fail** if they exist but do not validate.

### Telemetry signals

| Signal | Source | Where recorded |
|---|---|---|
| lineage_run_id | CI workflow | CI logs + artifacts |
| lineage_report_json | lineage scripts | CI artifacts or `mcp/runs/` |
| schema_validation_result | validators | CI logs |
| orphan_reference_count | lineage report | dashboards / trends *(optional)* |

## ⚖ FAIR+CARE & Governance

### Review gates

Governance/security review is required when changes introduce:

- new checks that could reveal sensitive locations through logs/reports,
- changes that affect “published” vs “draft” lineage gate behavior,
- new external data sources or new public-facing endpoints.

### CARE / sovereignty considerations

- Do not print or export sensitive coordinates, restricted locations, or raw identifiers in logs unless governance-approved.
- Prefer aggregated reporting (counts + stable IDs) over dumping full records.

### AI usage constraints

- Allowed: structural extraction, summarization, translation, keyword indexing.
- Prohibited: generating new policy text or inferring sensitive locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---:|---|---|
| v1.0.0 | 2025-12-26 | Initial lineage scripts README scaffold | TBD |

---

Footer refs (do not remove)

- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Lineage (parent): `.github/lineage/README.md`
- Template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
