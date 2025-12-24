---
title: "KFM — Lineage & Provenance (CI)"
path: ".github/lineage/README.md"
version: "v1.0.1"
last_updated: "2025-12-24"
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

doc_uuid: "urn:kfm:doc:github:lineage:readme:v1.0.1"
semantic_document_id: "kfm-github-lineage-readme-v1.0.1"
event_source_id: "ledger:kfm:doc:github:lineage:readme:v1.0.1"
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

# KFM Lineage & Provenance CI

This folder documents how KFM enforces provenance/lineage expectations in CI, and how contributors should wire new pipeline outputs into *traceable* evidence artifacts.

> Important: **This folder is not the canonical home of lineage data.**  
> Canonical lineage artifacts live in `data/prov/**` and are consumed downstream (audits, graph provenance, Focus Mode). This directory exists to keep the *CI and contribution rules* close to GitHub automation.

## 📘 Overview

### Purpose

- Define the CI “lineage gates” that keep KFM evidence-first and reproducible.
- Describe how provenance artifacts (PROV bundles) connect to STAC/DCAT outputs and downstream consumers (graph, API, Focus Mode).
- Provide contributor guidance for adding new data/evidence products without creating orphaned or uncitable content.

### Scope

| In Scope | Out of Scope |
|---|---|
| CI validation rules for lineage artifacts and cross-links | Implementing full ETL logic for every domain |
| Expected locations of PROV/STAC/DCAT artifacts and how CI discovers them | Cloud deployment / ops infrastructure |
| Minimal contribution checklist for provenance completeness | Writing/authoring Story Nodes (see Story Node template) |

### Audience

- Primary: pipeline + catalog maintainers; CI/automation maintainers
- Secondary: graph/API maintainers; curators reviewing evidence readiness

### Definitions

- Glossary: `docs/glossary.md` *(expected by governed templates; add if missing)*
- Terms used in this doc:
  - **Lineage**: the traceable chain from raw inputs → transforms → outputs (datasets/evidence products).
  - **Provenance**: the machine-readable record of activities/agents/derivations supporting lineage (W3C PROV‑O aligned).
  - **Contract artifact**: machine-validated schema/spec (JSON Schema, OpenAPI, GraphQL SDL, UI registry schema).
  - **Evidence artifact**: catalog + provenance outputs consumed downstream (STAC/DCAT/PROV and derived evidence products).
  - **Domain pack**: the minimal set that lets a domain participate in the pipeline (staging + mapping + tests + docs).
  - **PROV bundle**: a provenance record describing activities/agents/entities and their relationships.
  - **Lineage gate**: a CI check that validates provenance completeness + referential integrity.
  - **No orphan data**: any output lacking source/provenance is treated as invalid for Focus Mode and/or blocks promotion.

### Key artifacts

| Artifact | Path / Identifier | Notes |
|---|---|---|
| Universal governed doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Canonical doc structure + required front-matter keys |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Canonical Story Node structure + publication rules |
| Master Guide v12 | `docs/MASTER_GUIDE_v12.md` | Canonical pipeline ordering + invariants |
| v13 redesign blueprint | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Canonical “homes” per subsystem + CI gate expectations |
| Architecture vision (draft) | `docs/architecture/KFM_VISION_FULL_ARCHITECTURE.md` | *not confirmed in repo* (draft exists in project files) |
| Tests guide | `tests/README.md` | Minimum CI gates and test taxonomy *(path not confirmed in repo)* |
| Releases guide | `releases/README.md` | Release bundles link back to STAC/DCAT/PROV + PROV run IDs |
| MCP workspace guide | `mcp/README.md` | Run manifests should point to PROV bundles (do not duplicate provenance payloads) |
| PROV bundles | `data/prov/**` | Canonical lineage artifacts; consumed downstream |
| STAC catalogs | `data/stac/**` | Evidence artifacts referenced by graph/story |
| DCAT records | `data/catalog/dcat/**` | Dataset identifiers for export + APIs |
| API contracts | `src/server/contracts/**` | Contract-first boundary between UI and graph/catalogs |
| UI layer registry | `web/**/layers/**` | Layer metadata; must honor redaction + provenance surfacing |
| Example governed domain docs | `docs/data/**` | e.g., air-quality governance + land-treaties STAC submodule |

### Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] Clearly states canonical lineage artifact locations (`data/prov/**`)
- [ ] CI behavior documented (validate if present; fail if invalid; skip if not applicable)
- [ ] Validation steps listed and repeatable (placeholders allowed)
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document

- `path`: `.github/lineage/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| GitHub automation | `.github/workflows/` | CI workflows (schema lint, tests, lineage gates) |
| Lineage CI docs | `.github/lineage/` | This README + optional lineage helper scripts |
| Data domains | `data/<domain>/**` | `raw/`, `work/`, `processed/` per domain |
| STAC outputs | `data/stac/**` | STAC items/collections |
| DCAT outputs | `data/catalog/dcat/**` | DCAT dataset records |
| PROV outputs | `data/prov/**` | Provenance bundles (lineage) |
| Schemas | `schemas/**` | JSON Schemas + optional shapes |
| Pipelines | `src/pipelines/**` | Deterministic transforms producing outputs |
| Graph | `src/graph/**` + `data/graph/**` | Ontology + ingest fixtures |
| API boundary | `src/server/**` | Services + contracts + redaction + query orchestration |
| UI | `web/**` | Layer registry + Focus Mode UX |
| Releases | `releases/**` | Manifests/SBOMs/telemetry snapshots (distribution edge) |
| MCP workspace | `mcp/**` | Run manifests + experiments + model cards + SOPs |

### Expected file tree for this sub-area

~~~text
📁 .github/
├── 📁 workflows/
│   ├── 📄 kfm-ci.yml                         # CI entrypoint (not confirmed in repo)
│   └── 📄 <other-workflows>.yml
└── 📁 lineage/
    ├── 📄 README.md                          # (this file)
    └── 📁 scripts/                           # optional; not confirmed in repo
        └── 📄 validate_lineage.<ext>         # optional; not confirmed in repo
~~~

## 🧭 Context

### Background

KFM’s canonical flow is:

**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

Lineage and provenance are treated as first-class so that:

- Story Nodes and Focus Mode can only surface **provenance-linked content** (no uncited “floating” facts).
- Missing links (e.g., evidence IDs, entity references, provenance activities) are caught early via CI.
- Outputs remain **deterministic and diffable**, supporting audits and reproducible builds.

This `.github/lineage/` area exists so CI rules for provenance stay discoverable and consistent as domains expand.

### v13-aligned invariants (non‑negotiables)

- **No UI direct-to-graph reads**: `web/` must never query Neo4j directly; all graph access is via `src/server/`.
- **No unsourced narrative**: published Story Nodes must be provenance-linked and validate.
- **Contracts are canonical**: schemas live in `schemas/` and API contracts in `src/server/contracts/` and must validate in CI.
- **Data outputs are not code**: derived datasets belong under `data/<domain>/processed/`, not under `src/`.
- **Catalogs are not docs**: pipelines should not write STAC/DCAT/PROV into `docs/` (catalogs live under `data/`).

### Assumptions

- Canonical roots exist (or are being created) for `schemas/`, `data/stac/`, `data/catalog/dcat/`, `data/prov/`, `src/server/`, and `web/`.
- When schemas exist under `schemas/**`, CI validates artifacts against those schemas.
- PROV bundles are serialized in a machine-readable format (JSON‑LD / PROV‑JSON / Turtle): **format is implementation-defined**.

### Constraints / determinism requirements

- Canonical ordering is preserved: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- CI must be deterministic:
  - If an optional root is absent, jobs may skip.
  - If a required root is present but invalid, jobs fail.
- Prefer every meaningful run to produce (or link to) a PROV activity bundle under `data/prov/**`.
  - `mcp/runs/**` should contain pointers/IDs to PROV (not duplicate provenance payloads).

### Open questions

| Question | Owner | Target |
|---|---|---|
| What is the canonical PROV bundle serialization (JSON‑LD vs Turtle vs PROV‑JSON)? | Catalog owners | TBD |
| Do we adopt SHACL validation for JSON‑LD bundles now or later? | Catalog + graph owners | TBD |
| What is the minimum schema set required for “CI green” (stac/dcat/prov/storynodes/ui/telemetry)? | Contract owners | TBD |
| Do we standardize domains as `air-quality` vs `air_quality` and resolve naming inconsistencies? | Data governance | TBD |
| Governance refs vary across docs (`docs/governance/*` vs `docs/standards/governance/*` or `ROOT_GOVERNANCE.md` vs `ROOT_CHARTER.md`): what is canonical? | Governance owners | TBD |

### Future extensions

- Add a repo-standard validator under `.github/lineage/scripts/` that:
  - validates PROV bundles against `schemas/prov/**`
  - checks cross-links into STAC/DCAT
  - reports orphan references and missing evidence IDs
- Emit a machine-readable CI report (telemetry schema) for lineage health trends.

## 🗺️ Diagrams

### System / dataflow diagram

~~~mermaid
flowchart LR
  A[ETL runs] --> B[STAC/DCAT/PROV outputs]
  B --> C[Neo4j Graph]
  C --> D[APIs]
  D --> E[React/MapLibre UI]
  E --> F[Story Nodes]
  F --> G[Focus Mode]

  PR[Pull Request] --> CI[GitHub Actions CI]
  CI --> L[Lineage gates]
  L -->|pass| M[Merge allowed]
  L -->|fail| X[Block merge + report]

  B --> L
~~~

### CI gate flow on Pull Requests

~~~mermaid
flowchart TB
  PR[Pull Request] --> CI[GitHub Actions]

  CI --> MD[Markdown protocol validation]
  CI --> SC[Schema validation]
  CI --> SN[Story Node validation]
  CI --> API[API contract tests]
  CI --> SEC[Security + sovereignty scanning]

  MD --> OK[Merge allowed]
  SC --> OK
  SN --> OK
  API --> OK
  SEC --> OK
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| PROV bundle(s) | JSON‑LD / PROV‑JSON / Turtle (implementation-defined) | `data/prov/**` | `schemas/prov/**` (if present) |
| STAC collections/items | JSON | `data/stac/**` | `schemas/stac/**` (if present) |
| DCAT dataset records | RDF/JSON‑LD/Turtle (implementation-defined) | `data/catalog/dcat/**` | `schemas/dcat/**` (if present) |
| Story Node refs (optional) | Markdown + front-matter | `docs/reports/story_nodes/**` | `schemas/storynodes/**` (if present) |
| Release bundle refs (optional) | JSON/zip/SPDX/etc | `releases/**` | `schemas/telemetry/**` (if present) |

### Outputs

| Output | Format | Where | Notes |
|---|---|---|---|
| CI status | GitHub check | GitHub UI | Required |
| Validation report (optional) | JSON/Markdown | CI artifact (TBD) | Recommended for debugging |

### Sensitivity & redaction

- Provenance artifacts must not leak restricted locations or culturally sensitive knowledge.
- If a dataset is restricted, ensure provenance logs follow governance rules (redaction/generalization steps should be recorded as activities).

### Quality signals

- Schema validity for all present artifacts (STAC/DCAT/PROV).
- No orphan references:
  - evidence refs resolve (STAC/DCAT/PROV identifiers exist)
  - Story Node refs resolve (entity IDs exist; citations exist)
- Deterministic, diffable outputs (stable IDs + reproducible generation)
- Classification propagation:
  - no output is “less restricted” than any input in its lineage

## 🌐 STAC, DCAT & PROV Alignment

### STAC

**Lineage checks should confirm:**

- STAC IDs referenced by PROV (and by graph/story) exist and are unique.
- Any declared STAC assets referenced by provenance exist at the expected paths (or are resolvable via catalogs).
- If a STAC Item’s geometry is sensitive, geometry must be generalized/omitted according to governance (and that decision must be traceable in PROV).

> Observed pattern: KFM fixture/tooling notes reference STAC properties like `kfm:provenance_ref`, `kfm:lineage_sha`, and `kfm:telemetry_ref`. If your domain adopts these fields, CI should validate that they resolve and are stable.

### DCAT

**Lineage checks should confirm:**

- DCAT dataset IDs referenced by PROV (and by graph/story) exist and are stable.
- Minimum DCAT metadata required for sharing/export is present (title/description/license/keywords), subject to governance classification.

### PROV‑O

**Lineage checks should confirm:**

- `prov:wasDerivedFrom`: links outputs → inputs (source snapshots, upstream artifacts).
- `prov:wasGeneratedBy`: links outputs → the generating activity.
- Activity / Agent identities are stable identifiers for:
  - pipeline activities (runs)
  - agents (pipelines, maintainers, systems) as appropriate
- No public-facing evidence artifact exists without provenance metadata (**no orphan data**).

### Versioning and releases (optional)

Some domains are shipped as **versioned release bundles** (e.g., SBOM/manifest/telemetry snapshots and optional signatures/attestations).

If a PR changes `releases/**`, CI should validate:

- referenced artifacts exist (SBOM, manifest, telemetry, signatures/attestations if used)
- release manifests link back to:
  - STAC/DCAT/PROV snapshot paths (or pointers)
  - PROV run IDs / activities

## 🧪 Validation & CI/CD

### CI behavior contract

Lineage gates follow one deterministic contract:

- **Validate if present**:
  - when `data/prov/**` exists and changes, validate it
  - when `data/stac/**` or `data/catalog/dcat/**` changes, validate it and cross-link it to provenance
  - when Story Nodes change, validate evidence references and provenance annotations
- **Fail if invalid**: schema errors, missing links, or orphan refs fail the job deterministically.
- **Skip if not applicable**: optional roots absent → skip without failing the overall pipeline.

### Test profiles (documented patterns)

The following validator “profiles” appear in governed domain documentation and can be treated as a shared vocabulary for CI checks:

- `markdown-lint`
- `schema-lint`
- `footer-check`
- `accessibility-check`
- `diagram-check`
- `metadata-check`
- `provenance-check`
- `secret-scan`
- `pii-scan`

> Implementation note: profile names are a **contract for CI reporting**, not a requirement that tooling uses any particular engine.

### Lineage gate matrix (what should run when)

| Change surface | Gate | Profile(s) | Fail condition (examples) |
|---|---|---|---|
| `data/prov/**` | PROV validation | `schema-lint`, `provenance-check` | invalid serialization; missing required relations; dangling IDs |
| `data/stac/**` | STAC validation + link integrity | `schema-lint`, `provenance-check` | invalid STAC JSON; broken links; STAC IDs referenced by PROV missing |
| `data/catalog/dcat/**` | DCAT validation + link integrity | `schema-lint`, `provenance-check` | invalid DCAT record; dataset IDs drift; missing license metadata |
| `schemas/**` | Schema validation | `schema-lint` | schema invalid or breaks known fixtures |
| `docs/reports/story_nodes/**` | Story Node evidence gating | `metadata-check`, `provenance-check` | missing evidence IDs; refs to non-existent STAC/DCAT/PROV IDs |
| `src/pipelines/**` | Reproducibility + provenance hooks | `metadata-check`, `provenance-check` | outputs changed but provenance not updated |
| `src/server/contracts/**` | Contract + provenance fields | `schema-lint`, `metadata-check` | provenance fields removed/renamed without version bump |
| `web/**/layers/**` | UI registry validation | `schema-lint`, `accessibility-check` | layer metadata missing classification/redaction flags |
| `releases/**` | Release bundle integrity | `metadata-check`, `provenance-check`, `secret-scan` | manifest/SBOM refs broken; missing provenance pointers; signatures mismatched (if used) |

### Fixture-driven validation (recommended pattern)

Some KFM validation notes describe using a **fixture suite** to make lineage gates deterministic:

- Fixtures live under `.github/actions/fixtures/catalogs/stac/**` *(path not confirmed in repo)*
- Common jobs/checks:
  - `stac-validate`
  - `stac-invalid-assert` (a known-bad fixture must fail)
  - `stac-links` (link resolution)
  - `stac-asset-size` (keep example assets small and stable)

Why fixtures matter:

- They prevent “green by accident” validators.
- They ensure a PR that breaks schema or link integrity fails with an expected message.
- They give maintainers a stable baseline for cross-link rules (STAC ↔ PROV ↔ DCAT).

## 🧩 Domain patterns in governed docs

This guide is intentionally domain-agnostic, but several governed documents illustrate how lineage rules show up in practice.

### Land treaties module (historical, sovereignty-sensitive)

Documented patterns:

- Module root under `docs/data/historical/land-treaties/` with a STAC subfolder (module-local packaging).
- STAC Items may omit or generalize geometry for sensitive sites; provenance should record the generalization step as an activity.
- CI validation concepts include a FAIR+CARE check (e.g., “forbid raw sensitive geometries”) alongside schema + link validation.

### Air-quality domain (freshness-sensitive, API lifecycle)

Documented patterns:

- Domain root under `data/air-quality/` with `raw/`, `work/`, `processed/`, and `stac/` outputs plus domain governance docs.
- Freshness gates are evaluated at the ETL/catalog boundary and must be explainable via catalog + provenance metadata.
- Telemetry signals and exception registries can be recorded under `docs/telemetry/` and versioned via `schemas/telemetry/`.

> These are “patterns in docs,” not guarantees about the current repo state. If a referenced path does not exist, treat it as **not confirmed in repo** and follow the v13 blueprint’s canonical homes.

### Freshness gates (for dynamic sources)

Some domains (e.g., near-real-time APIs or incremental geospatial tiles) may declare **freshness windows**, API lifecycle rules, and schema-drift detection as part of governance.

Recommended CI pattern:

- PR checks: validate configuration + schema + provenance linkability.
- Scheduled checks (nightly/weekly): run freshness and drift detection that can open issues, but should not block unrelated PRs.

Example watcher pattern (documented in project files):

- Watcher kits under `tools/validate/watchers/**` may run on:
  - `schedule` (cron)
  - `repository_dispatch` (external trigger)
- A watcher can emit **incremental artifacts** into a dated run directory, for example:

~~~text
data/surficial-geology/increments/soilgrids/{yyyymmdd}/
  tiles/*.tif.cog
  vectors/*.parquet
  stac/*.json
  prov/*.jsonld
~~~

- Each watcher run should emit (or update pointers to):
  - STAC Item(s) (+ optional Collection updates)
  - a DCAT dataset record for the run date (domain-defined)
  - a PROV‑O activity/agent bundle referencing upstream checksums and headers (ETag / Last‑Modified / SHA256)

Determinism guidance (watchers):

- Pin core geospatial tooling (e.g., `gdal`, `rasterio`, `rio-cogeo`) and record versions in provenance.
- Use checksum gates to avoid re‑emission; date‑stamped run directories avoid collisions.
- Emit minimal run telemetry (example fields): `tile_count`, `changed_tiles`, `diff_area_m2`, `runtime_sec`, `cpu_ms`, `energy_joules`.

CI notes (scheduled workflows):

- Scheduled workflows should run the same schema + lineage validators used in PR gates.
- If a scheduled workflow commits artifacts back to the repository, treat it as a governed change:
  - do not bypass sovereignty/redaction review for classification-sensitive outputs.

### Local reproduction (placeholder)

~~~bash
# NOTE: commands are placeholders; replace with repo-approved tooling.
# Intent:
# 1) validate schemas
# 2) validate provenance bundles
# 3) check cross-links into STAC/DCAT

# make validate-schemas
# make validate-lineage
~~~

## 🧠 Story Node & Focus Mode Integration

### Story Nodes as “machine-ingestible storytelling”

- Story Nodes must carry provenance annotations and connect to graph entities.
- Story Nodes should link to evidence IDs (STAC/DCAT/PROV) wherever possible.

### Focus Mode rule

- Focus Mode only consumes provenance-linked content.
- Any predictive/AI-generated content must be opt-in and carry uncertainty / confidence metadata.
- Provenance should be surfaced to users via citations and “About this data” / audit affordances in the UI.

## ⚖ FAIR+CARE & Governance

### Review gates

- Changes that touch provenance rules, redaction behavior, or public-facing evidence exports require human review.
- Any change that could expose sensitive locations by interaction/zoom must be reviewed and tested against sovereignty policy.

### CARE / sovereignty considerations

- Identify impacted communities and protection rules for sensitive/restricted locations.
- Ensure provenance and audit logs don’t re-expose restricted geometry or identifiers.
- Prefer storing generalized public geometry and keeping exact geometry in restricted tiers (domain-defined).

### AI usage constraints

- Ensure this document’s AI permissions/prohibitions match intended use.
- No “generate policy” behavior should be derived from this README.
- If AI is used to propose classifications or redaction decisions, a human review must approve final labels (especially downgrades).

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.1 | 2025-12-24 | Align lineage CI doc with v13 invariants + releases/MCP + validator profiles | TBD |
| v1.0.0 | 2025-12-22 | Initial `.github/lineage/` README scaffold | TBD |

---

## Footer refs (do not remove)

- Master guide: `docs/MASTER_GUIDE_v12.md`
- v13 blueprint: `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Ethics: `docs/governance/ETHICS.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
