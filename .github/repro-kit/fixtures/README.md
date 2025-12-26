---
title: "KFM Repro Kit — Fixtures"
path: ".github/repro-kit/fixtures/README.md"
version: "v1.0.0"
last_updated: "2025-12-26"
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

doc_uuid: "urn:kfm:doc:github:repro-kit-fixtures-readme:v1.0.0"
semantic_document_id: "kfm-github-repro-kit-fixtures-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:github:repro-kit-fixtures-readme:v1.0.0"
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

# KFM Repro Kit — Fixtures

## 📘 Overview

### Purpose

This directory holds **small, public-safe fixture packages** used to run **deterministic regression checks** across the KFM pipeline (ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode).

Fixtures exist to make PR review and CI checks repeatable by providing:

- **minimal inputs** (synthetic / redacted / public-domain only),
- **expected outputs** (or output hashes),
- a **portable manifest** that documents how the fixture should be executed and validated.

### Scope

| In Scope | Out of Scope |
|---|---|
| Small “golden” datasets suitable for committing to git | Raw source snapshots of real domains (belongs under `data/<domain>/raw/`) |
| Expected outputs and/or canonical hashes for deterministic comparisons | Large datasets, restricted datasets, or anything requiring secrets/privileged access |
| Minimal metadata to reproduce and validate a fixture run | Defining new governance policy (use `docs/governance/*` instead) |
| CI-friendly artifacts that exercise STAC/DCAT/PROV, graph imports, and API contracts | Production-scale replays or full-pipeline backfills |

### Audience

- **Primary:** contributors adding/changing ETL, catalogs, graph ingest, API endpoints/contracts, UI layers, or Story Nodes.
- **Secondary:** maintainers reviewing CI failures and reproducibility claims.

### Definitions (link to glossary)

- Link: `docs/glossary.md` *(not confirmed in repo)*
- Terms used in this doc include: **fixture**, **golden dataset**, **expected output**, **hash comparison**, **deterministic**, **idempotent**, **run manifest**, **PROV bundle**, **stable identifier**.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Repro-kit root README | `.github/repro-kit/README.md` | TBD | Defines repro-kit purpose and subfolders |
| Fixture packages | `.github/repro-kit/fixtures/<fixture_id>/` | TBD | One folder per fixture; contains manifest + inputs + expected |
| Schemas | `schemas/` | TBD | STAC/DCAT/PROV + any fixture-manifest schema (if added) |
| Catalog outputs | `data/stac/` + `data/catalog/dcat/` | TBD | Canonical production catalogs (fixtures may mirror micro versions) |
| PROV bundles | `data/prov/` | TBD | Canonical provenance outputs; fixtures may validate PROV profile on micro runs |
| Tests | `tests/` | TBD | Unit/integration/contract tests may consume fixtures |
| Workflows | `.github/workflows/` | TBD | CI may execute fixture runs and attach diff reports |

### Definition of done (for this document)

- [ ] Front-matter complete + `path` matches file location
- [ ] Fixture package conventions are explicit (layout, naming, required metadata)
- [ ] Safety rules are explicit (no secrets/PII, no sensitive locations, public-safe only)
- [ ] Validation expectations are explicit (schema checks, hash comparisons, provenance expectations)
- [ ] Open questions captured (schema/tooling decisions not yet standardized)
- [ ] Version history present

## 🗂️ Directory Layout

### This document

- `path`: `.github/repro-kit/fixtures/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Repro kit root | `.github/repro-kit/` | Repro helpers (actions/scripts/env/fixtures) |
| CI workflows | `.github/workflows/` | CI gates that may run fixtures |
| Tests | `tests/` | Test runners that may consume fixtures |
| Pipelines | `src/pipelines/` | Deterministic ETL + catalog builders |
| Catalog outputs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | Canonical STAC/DCAT/PROV artifacts |
| Graph | `src/graph/` | Ontology bindings + graph build / ingest |
| API boundary | `src/server/` *(or legacy path — not confirmed in repo)* | API contracts, redaction, access controls |
| UI | `web/` | React/Map UI (never reads Neo4j directly) |
| Story Nodes | `docs/reports/story_nodes/` | Narrative artifacts (provenance-linked) |

### Expected file tree for this sub-area

~~~text
📁 .github/
└── 📁 repro-kit/
    └── 📁 fixtures/
        ├── 📄 README.md
        ├── 📁 <fixture_id>/                     # one fixture package (repeat per fixture)
        │   ├── 🧾 manifest.yaml                 # required: fixture metadata + reproduction contract
        │   ├── 📁 input/                        # required: small inputs (synthetic/redacted/public)
        │   ├── 📁 expected/                     # required: expected outputs and/or expected hashes
        │   ├── 🔐 checksums.sha256              # optional: checksums for input + expected artifacts
        │   └── 📝 NOTES.md                      # optional: governance/safety notes + rationale
        └── 📁 _shared/                          # optional: shared docs/schemas/examples
            └── 📄 (optional files)
~~~

## 🧭 Context

### Background

KFM emphasizes **deterministic, auditable processing**. Fixtures are the lightweight, CI-safe mechanism for making that guarantee testable:

- contributors can run “the same” miniature job and compare results,
- reviewers can validate that a change doesn’t break governed contracts,
- CI can produce reproducibility evidence (hash comparison, schema validation summaries) without requiring production data access.

### Assumptions

- The canonical pipeline ordering is preserved: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- The UI does not read Neo4j directly; the API boundary mediates access and enforces redaction/generalization.
- Schema validation and contract tests are first-class build gates.

### Constraints / invariants

- **Determinism:** same fixture inputs + same config + same code revision ⇒ same outputs (byte-for-byte when practical).
- **Idempotence:** running a fixture twice does not duplicate records or generate inconsistent outputs.
- **No hidden I/O:** fixtures must not require untracked downloads, secrets, or privileged infrastructure.
- **Stable IDs:** fixture data must use stable identifiers suitable for linking into catalogs/graph/API payloads.
- **Safety-first:** fixtures must not contain PII or sensitive/restricted location data.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| What is the canonical fixture manifest schema (YAML vs JSON, required fields, validation)? | TBD | TBD |
| Should expected comparisons be file-hash based, semantic-diff based, or both? | TBD | TBD |
| Where should fixture run reports live long-term: CI artifacts vs `mcp/runs/` pointers? | TBD | TBD |
| What is the standard environment locking approach used by fixture runs? | TBD | TBD |

### Future extensions

- Add a JSON Schema for `manifest.yaml` under `schemas/` and enforce it in CI.
- Add composite actions under `.github/repro-kit/actions/` that:
  - validate fixture manifests,
  - run fixtures,
  - compare hashes,
  - attach a diff report to CI artifacts.
- Add “fixture catalog index” (a single list of available fixtures + purpose + safety notes).

## 🗺️ Diagrams

### System / dataflow diagram

~~~mermaid
flowchart LR

  subgraph Fixtures[".github/repro-kit/fixtures/<fixture_id>"]
    M[manifest.yaml]
    I[input/]
    E[expected/]
  end

  M --> R[Fixture runner]
  I --> R
  R --> O[actual outputs]
  O --> V[validators<br/>schema + contract + integrity]
  E --> H[hash/semantic comparator]
  O --> H
  V --> P{pass/fail}
  H --> P
  P --> REP[diff report + summary]
~~~

### Optional: sequence diagram

~~~mermaid
sequenceDiagram
  participant Dev as Contributor/CI
  participant Runner as Fixture Runner
  participant Validators as Validators
  participant Report as Report/Artifacts

  Dev->>Runner: run fixture(<fixture_id>)
  Runner->>Validators: validate outputs (STAC/DCAT/PROV, contracts)
  Validators-->>Runner: validation summary
  Runner->>Runner: compare outputs vs expected (hash/diff)
  Runner-->>Report: publish report + hashes
  Report-->>Dev: pass/fail + diagnostics
~~~

## 📦 Data & Metadata

### Data lifecycle (required staging)

Fixtures are **not** a substitute for canonical data lifecycle staging.

- Production datasets follow: `data/raw/` → `data/work/` → `data/processed/` → `data/stac/` (+ `data/catalog/dcat/` + `data/prov/`).
- Fixtures live under `.github/repro-kit/fixtures/` and must remain:
  - **tiny**, **portable**, and **public-safe**,
  - usable without privileged access.

### Fixture package minimum metadata

Each fixture package should include a manifest with (at minimum):

- `fixture_id` (stable slug; directory name matches)
- `purpose` (what subsystem behavior it exercises)
- `inputs` (what files are used; whether they are synthetic/redacted)
- `expected` (what outputs/hashes are compared)
- `validation` (what schemas/contract checks apply)
- `determinism_notes` (seed, ordering, canonicalization expectations)
- `governance_notes` (why it is safe to include publicly)

#### Example manifest skeleton (illustrative)

~~~yaml
fixture_id: "<fixture_id>"
purpose: "<what behavior this fixture tests>"
inputs:
  - path: "input/<file-or-folder>"
    description: "<synthetic/redacted/public-safe>"
expected:
  - path: "expected/<file-or-folder>"
    compare: "sha256"   # or "semantic" (not confirmed in repo)
validation:
  stac: true
  dcat: false
  prov: true
determinism_notes:
  seed: 0
  canonicalization: "<how outputs are normalized before hashing (not confirmed in repo)>"
governance_notes:
  sensitivity: "public"
  pii_present: false
  restricted_locations_present: false
~~~

## 🌐 STAC, DCAT & PROV Alignment

### STAC/DCAT/PROV alignment policy (how to document)

If a fixture exercises catalog outputs:

- Include minimal “golden” STAC Collection/Item JSON under `expected/` (or expected hashes).
- Include minimal DCAT artifacts under `expected/` when relevant.
- Include minimal PROV bundle(s) under `expected/` when relevant.
- Ensure fixture outputs validate against the repo’s `schemas/` and declared profiles.

### Versioning expectations

- Fixtures are versioned by directory naming + manifest fields (recommended):
  - either `fixture_id` embeds version (e.g., `place-mini-v1`),
  - or `manifest.yaml` includes a `version` field (schema TBD).
- Any breaking change to expected outputs should be:
  - justified in `NOTES.md`,
  - paired with a clear PR description,
  - reviewed for governance impact.

## 🧱 Architecture

### Subsystem contracts (what must exist for each subsystem)

| Subsystem | Contract artifacts (fixture-oriented) | “Do not break” rule |
|---|---|---|
| ETL | input + expected normalized outputs/hashes | deterministic, replayable |
| Catalogs | expected STAC/DCAT/PROV snapshots/hashes | machine-validated |
| Graph | expected import artifacts or graph assertions | stable labels/edges |
| APIs | contract tests with deterministic responses | backward compat or version bump |
| UI | optional snapshot tests driven by API responses | no direct graph calls |
| Focus Mode | provenance-linked context bundle assertions | no unsourced claims |

### Next-evolution extension points

- Add fixture coverage for new domains as they appear (keep fixtures synthetic/public-safe).
- Add fixture coverage for redaction/generalization behavior at the API boundary.
- Add fixture coverage for Story Node ingestion and provenance requirements.

## 🧠 Story Node & Focus Mode Integration

### Story Nodes as “machine-ingestible storytelling”

- Fixtures may include micro Story Nodes strictly for validating:
  - provenance references,
  - schema conformance,
  - safe rendering constraints.
- Any narrative text in fixtures must remain **evidence-linked** and **non-sensitive**.

### Focus Mode rule

- Focus Mode must only consume provenance-linked content.
- Fixtures that exercise Focus Mode behaviors should include provenance references as first-class test artifacts.

### Optional structured controls

~~~yaml
focus_layers:
  - "fixture:<fixture_id>"
focus_time: "<TBD-iso8601>"
focus_center: [-98.0000, 38.0000]
~~~

## 🧪 Validation & CI/CD

### Minimum CI gates for “v12-ready” contributions

- [ ] Markdown protocol validation
- [ ] JSON schema validation (STAC/DCAT/telemetry if present)
- [ ] Graph integrity tests (if graph is exercised)
- [ ] API contract tests (if APIs are exercised)
- [ ] UI registry/schema checks (if UI is exercised)
- [ ] Security + sovereignty scanning gates (as applicable)
- [ ] Fixture run + compare (if fixtures are present)

### Reproduction

~~~bash
# Replace with repo-specific commands as they are added.

# 1) Validate fixture manifests (schema TBD)
# <TBD>

# 2) Run fixture(s) deterministically
# <TBD>

# 3) Validate outputs (STAC/DCAT/PROV schemas, contracts)
# <TBD>

# 4) Compare outputs vs expected (hash/diff)
# <TBD>
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| fixture_id + run_id | fixture runner | CI logs/artifacts and/or `mcp/runs/` pointers (TBD) |
| schema validation summary | validators | CI logs |
| hash comparison report | fixture runner | CI artifacts |

## ⚖ FAIR+CARE & Governance

### Governance review triggers

Review is required when fixtures introduce:

- any **location-bearing** datasets above previously used precision,
- any content that could reveal **restricted/sensitive locations** by reconstruction,
- any personal data or identifiable metadata (PII),
- any new public-facing behavior in APIs/UI supported by fixtures.

### CARE / sovereignty considerations

- Fixtures must not encode culturally sensitive knowledge or restricted site locations.
- Prefer:
  - synthetic coordinates,
  - coarse geometry,
  - redacted identifiers,
  - “toy” examples that validate behavior without leaking sensitive facts.

### AI usage constraints

- Ensure the front-matter AI permissions/prohibitions match intended use.
- Do not use fixtures as a basis for “generate policy” behavior.
- Do not use AI to infer sensitive locations from fixture data (directly or indirectly).

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-26 | Initial fixtures README scaffold (layout + safety + validation conventions) | TBD |

---

Footer refs:

- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

