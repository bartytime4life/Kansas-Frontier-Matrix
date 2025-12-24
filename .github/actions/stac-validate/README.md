---
title: "GitHub Action — STAC Validate"
path: ".github/actions/stac-validate/README.md"
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

doc_uuid: "urn:kfm:doc:github-actions:stac-validate:v1.0.1"
semantic_document_id: "kfm-github-action-stac-validate-v1.0.1"
event_source_id: "ledger:kfm:doc:github-actions:stac-validate:v1.0.1"
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

<div align="center">

# GitHub Action — STAC Validate

**Path:** `.github/actions/stac-validate/README.md`  
**KFM role:** Catalog validation gate for **STAC Collections + Items** (prevents downstream breakage)

<img alt="doc_kind" src="https://img.shields.io/badge/doc_kind-Guide-0ea5e9" />
<img alt="status" src="https://img.shields.io/badge/status-draft-f59e0b" />
<img alt="KFM-MDP" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-64748b" />
<img alt="KFM-STAC" src="https://img.shields.io/badge/KFM--STAC-v11.0.0-64748b" />

</div>

> **Purpose (required):** Provide a deterministic CI gate that validates KFM STAC artifacts (Collections + Items) against **STAC core + KFM-STAC profile expectations**, so broken metadata cannot merge and cascade into Graph/API/UI/Story failures.

## 📘 Overview

### Purpose

- Provide a **CI gate** that validates KFM STAC artifacts (Collections + Items) before merge.
- Enforce that STAC outputs remain **machine-valid**, **profile-consistent**, and **safe to consume downstream** (Graph, API boundary, UI, Story Nodes, Focus Mode).

### Scope

| In Scope | Out of Scope |
|---|---|
| Validate STAC JSON under `data/stac/**` | Generating STAC or modifying STAC outputs |
| Validate STAC “fixture catalogs” under `.github/actions/fixtures/catalogs/stac/**` *(if adopted; not confirmed in repo)* | Validating DCAT/PROV (separate gates/actions) |
| Validate against KFM constraints in `schemas/stac/**` *(not confirmed in repo)* | Loading Neo4j / API/UI testing |
| Fail CI on schema/profile errors | Story Node validation (separate gate) |
| Optional: “changed files only” validation *(if implemented in the action)* | External network link checking unless explicitly implemented + allowed |
| Optional: cross-file integrity checks (e.g., Item `collection` exists) *(if implemented)* | “Fixups”, enrichment, or inference of sensitive locations |

### Audience

- Primary: Contributors who modify `data/stac/**`, `schemas/stac/**`, or catalog-generation pipelines.
- Secondary: CI maintainers and reviewers/maintainers who need fast feedback that **catalog contracts** are preserved.

### Definitions

- Glossary: `docs/glossary.md` *(not confirmed in repo — add/repair link if the glossary lives elsewhere)*
- Terms used in this doc:
  - **STAC**: SpatioTemporal Asset Catalog
  - **Collection**: STAC Collection JSON under `data/stac/collections/`
  - **Item**: STAC Item JSON under `data/stac/items/`
  - **Gate**: A CI validation step that fails PRs if a required contract/invariant is violated
  - **Fixture catalogs**: small “golden” STAC examples used to test the validator gate itself *(not confirmed in repo)*

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This README | `.github/actions/stac-validate/README.md` | Repo maintainers | Usage + contract expectations |
| Action definition | `.github/actions/stac-validate/action.yml` | CI maintainers | Inputs/outputs + implementation *(not validated by this doc)* |
| Workflows calling this action | `.github/workflows/` | CI maintainers | PR/push/scheduled gates |
| Canonical STAC outputs | `data/stac/collections/**` + `data/stac/items/**` | Catalog stage | Canonical paths |
| STAC schemas + profile constraints | `schemas/stac/**` | Schema owners | KFM constraints + schema bundles *(not confirmed in repo)* |
| Fixture catalogs (recommended) | `.github/actions/fixtures/catalogs/stac/{minimal_valid,edge_cases,invalid}/**.json` | CI maintainers | Gate regression suite *(not confirmed in repo)* |
| Companion validators (optional) | `tools/validate/check_links.py`, `tools/validate/assert_asset_size.py` | Repo maintainers | Link + asset-size checks *(not confirmed in repo)* |
| Master Guide | `docs/MASTER_GUIDE_v12.md` | KFM maintainers | Canonical ordering + invariants |
| v13 redesign blueprint (draft) | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | KFM maintainers | Canonical roots + CI readiness gates *(draft; if adopted)* |

### Definition of done (for this document)

- [ ] Front-matter complete + valid (KFM-MDP v11.2.6)
- [ ] Mermaid diagram renders (no parse errors)
- [ ] Usage examples match the action’s real `action.yml` inputs
- [ ] Validation steps are repeatable locally and align with minimum CI gates
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document

- `path`: `.github/actions/stac-validate/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Local actions | `.github/actions/` | Composite/local actions used by workflows |
| Workflows | `.github/workflows/` | CI entrypoints calling local actions |
| STAC outputs | `data/stac/` | Collections + Items produced by catalog stage |
| Schemas | `schemas/stac/` | STAC schemas + KFM constraints *(not confirmed in repo)* |
| Tooling | `tools/` | validators/utilities *(not confirmed in repo)* |
| Pipelines | `src/pipelines/` | ETL + catalog build producing `data/stac/**` |
| Governance | `docs/governance/` | FAIR+CARE + sovereignty rules |

### Expected file tree for this sub-area

~~~text
📁 .github/
└── 📁 actions/
    └── 📁 stac-validate/
        ├── 📄 README.md
        ├── 📄 action.yml
        └── 📁 scripts/                      # optional: helper entrypoints
            └── 📄 validate-stac.(sh|py|js)   # optional: local runner wrapper
~~~

### Recommended fixture tree (gate self-test)

*(Recommended pattern; not confirmed in repo.)*

~~~text
📁 .github/
└── 📁 actions/
    └── 📁 fixtures/
        └── 📁 catalogs/
            └── 📁 stac/
                ├── 📁 minimal_valid/
                ├── 📁 edge_cases/
                └── 📁 invalid/
~~~

## 🧭 Context

### Background

KFM uses a governed pipeline where catalogs (STAC/DCAT/PROV) sit between ETL outputs and graph/API/UI/Story consumers. If STAC JSON breaks, it can cascade into ingestion failures, broken UI layers, or missing provenance.

**Canonical ordering (non-negotiable):**  
**ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**

This action exists to make “STAC must validate” a repeatable, automated CI gate.

### Assumptions

- STAC artifacts are committed under `data/stac/collections/` and `data/stac/items/`.
- KFM schema constraints are expected under `schemas/stac/` *(not confirmed in repo)*.
- Validation should be deterministic and not depend on external services by default.

### Constraints / invariants

- Preserve canonical pipeline ordering (see above).
- Validation must not mutate repository data (read-only check).
- No inference of sensitive locations; no enrichment; no “fixups” inside CI.
- Avoid leaking sensitive geometry details in logs when sovereignty rules apply.

### Contract expectations (what “pass” means)

At minimum, a passing run should indicate:

- JSON parses and files match expected STAC types (Collection / Item).
- STAC core schema validation succeeds for the STAC version used by the project.
- KFM-STAC profile expectations hold (see “📦 Data & Metadata”).

If the action currently validates a smaller subset, update this README so “pass” is not overstated.

## 🗺️ Diagrams

### System / dataflow diagram

~~~mermaid
flowchart LR
  A[ETL outputs<br/>data/&lt;domain&gt;/processed/] --> B[Catalog build]
  B --> C[STAC JSON<br/>data/stac/**]
  C --> D[CI Gate: stac-validate]
  D -->|pass| E[Graph ingest + API + UI consume]
  D -->|fail| F[Fix STAC JSON / schema / pipeline]
~~~

### Optional: sequence diagram

~~~mermaid
sequenceDiagram
  participant Dev as Contributor
  participant CI as GitHub Actions
  participant Repo as Repository

  Dev->>Repo: Push/PR changes (data/stac/**, schemas/stac/**, action)
  CI->>Repo: Checkout
  CI->>CI: Run stac-validate (local action)
  CI-->>Dev: Pass/Fail + logs (+ optional report)
~~~

### Mermaid rendering note

If you include glob patterns in Mermaid labels (e.g., `data/stac/**/*`), quote or escape special characters to avoid Mermaid parse errors.

## 📦 Data & Metadata

### What this action validates

**Canonical catalog roots (expected):**
- STAC Collections: `data/stac/collections/**/*.json`
- STAC Items: `data/stac/items/**/*.json`

**Recommended fixture roots (optional; not confirmed in repo):**
- `.github/actions/fixtures/catalogs/stac/minimal_valid/**.json`
- `.github/actions/fixtures/catalogs/stac/edge_cases/**.json`
- `.github/actions/fixtures/catalogs/stac/invalid/**.json`

### Validation layers (recommended contract)

This action is intended to be a “catalog contract gate” with layered checks:

1) **Schema/type checks**
- Valid JSON
- Correct STAC object type (Collection vs Item)

2) **STAC core checks**
- STAC version pinned (e.g., `stac_version: "1.0.0"`) and consistent

3) **KFM lineage hooks (required for valid artifacts)**
All *valid* Collections and Items should include the following `properties` fields:

- `kfm:provenance_ref` — path/identifier for provenance activity/entity (PROV bundle)
- `kfm:lineage_sha` — commit SHA that produced the artifact
- `kfm:telemetry_ref` — telemetry identifier (e.g., CI/run telemetry)

4) **Spatial/temporal coherence (KFM profile expectations)**
- Collection `extent.spatial.bbox` is coherent and Kansas-scoped (no inverted min/max; 2D vs 3D consistent)
- Item `bbox` covers `geometry`; geometry is valid; CRS assumptions are explicit/consistent
- Temporal logic: if `datetime` present, do not also provide `start_datetime/end_datetime`; otherwise ensure `start <= end`

5) **Optional companion checks (separate gates unless bundled)**
- Link hygiene (self/parent/root/collection resolve; no 404s)
- Asset size + checksum rules for deterministic CI (tiny, fetchable assets; include checksum when possible)

If you implement (4) or (5) inside this action, document the exact rules and failure modes here.

### Fixture semantics (recommended)

If a fixture suite is adopted:

- **Minimal examples**: MUST pass validation
- **Edge cases**: MUST pass while exercising rare/optional fields
- **Invalids**: MUST fail with expected error class (CI asserts regressions)

### Telemetry signals (if emitted)

| Signal | Source | Where recorded |
|---|---|---|
| `catalog_validation_result` | CI | CI logs + artifacts; optionally `mcp/runs/` |
| `lineage_sha` | CI / pipelines | STAC `properties.kfm:lineage_sha` |
| `telemetry_ref` | CI / telemetry | STAC `properties.kfm:telemetry_ref` |

## 🌐 STAC, DCAT & PROV Alignment

### Alignment policy

- STAC artifacts are a **contract**: downstream consumers rely on them to be valid.
- This action is the STAC gate only. DCAT and PROV have separate validators/gates.
- Stable identifiers and lineage hooks should align across:
  - STAC IDs / collection references
  - DCAT dataset records
  - PROV bundles (activities/entities/agents)

### Versioning expectations

- Schema/profile changes should be versioned and paired with:
  - updated pipelines that emit compliant STAC
  - updated fixtures (minimal/edge/invalid)
  - updated CI gate behavior docs

## 🧱 Architecture

### How to use in a workflow

~~~yaml
name: Validate STAC

on:
  pull_request:
    paths:
      - "data/stac/**"
      - "schemas/stac/**"
      - ".github/actions/stac-validate/**"

jobs:
  stac-validate:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      pull-requests: read
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Validate STAC artifacts
        uses: ./.github/actions/stac-validate
        with:
          stac_root: "data/stac"          # update to match action.yml
          schemas_root: "schemas/stac"    # update to match action.yml
          fail_on_warning: "true"         # update to match action.yml
~~~

> **Important:** `with:` input names above are placeholders until verified against `.github/actions/stac-validate/action.yml`.

### Fixture-gate workflow pattern (recommended)

If you adopt a fixture suite, consider separate jobs so failures are easy to interpret:

- `stac-validate` (minimal + edge cases must pass)
- `stac-invalid-assert` (invalid fixtures must fail as expected)
- `stac-links` (optional; checks link resolution)
- `stac-asset-size` (optional; checks asset size/checksum rules)

The repo may implement these as:
- additional workflows, or
- separate local actions, or
- a single action with feature flags.

### Local validation (developer workflow)

Use the same validator/toolchain that the action uses so results match CI.

Recommended “fast targets” (pattern; not confirmed in repo):

~~~text
make stac/validate:minimal   # validate minimal + edge cases
make stac/validate:invalid   # assert invalid fixtures fail
make stac/links              # link checker
make stac/assets:tiny        # asset size + checksum rules
~~~

If the action provides a script entrypoint, run that locally:

~~~text
# Example patterns (update to match the action):
# - ./.github/actions/stac-validate/scripts/validate-stac.sh
# - python .github/actions/stac-validate/scripts/validate_stac.py --stac-root data/stac --schemas-root schemas/stac
~~~

## 🧠 Story Node & Focus Mode Integration

- This action does **not** validate Story Nodes.
- Story Node validation is a separate CI gate (front-matter, citations, entity references, redaction compliance).
- However, STAC validity matters for Focus Mode because:
  - Story Nodes must be provenance-linked (claims trace to dataset/record/asset IDs).
  - STAC provides discoverable, stable identifiers that Story Nodes and UI layers can reference.

## 🧪 Validation & CI/CD

### Validation checklist

- [ ] All targeted STAC files validate (Collections + Items)
- [ ] Required lineage hooks present on valid artifacts:
  - [ ] `properties.kfm:provenance_ref`
  - [ ] `properties.kfm:lineage_sha`
  - [ ] `properties.kfm:telemetry_ref`
- [ ] Schema/profile changes are compatible with intended outputs
- [ ] No CI step writes back to `data/stac/**` (validation is read-only)
- [ ] Action logs do not expose restricted geometries (when sovereignty rules apply)

### CI gate alignment (recommended minimum)

This action is one of the “repo lint / contract gates” expected by the Master Guide / redesign blueprint. Other gates typically include:

- Markdown protocol checks (KFM-MDP)
- DCAT validation gate
- PROV validation gate
- Story Node validation gate
- API contract tests
- UI schema checks
- Security/sovereignty scans

See `.github/workflows/README.md` for the canonical CI gate list *(not confirmed in repo)*.

## ⚖ FAIR+CARE & Governance

### Review gates

- Changes to `schemas/stac/**` *(if present)* require maintainer review.
- Changes impacting sensitivity/redaction handling require governance review per:
  - `docs/governance/ROOT_GOVERNANCE.md`
  - `docs/governance/SOVEREIGNTY.md`
  - `docs/governance/ETHICS.md`

### CARE / sovereignty considerations

- This action must not attempt to infer or “repair” sensitive geometries.
- Avoid leaking restricted coordinates in logs (prefer summary errors over raw geometry dumps).
- If catalogs are public, ensure restricted-location protections are enforced earlier in the pipeline and at the API boundary.

### AI usage constraints

- This action performs deterministic validation only; no AI generation.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial README for STAC validation action | TBD |
| v1.0.1 | 2025-12-24 | Align README to KFM-MDP v11.2.6 patterns; add fixture + lineage-hook expectations; tighten gate boundaries | TBD |

---

Footer refs:
- Local actions index: `.github/actions/README.md`
- Workflows index: `.github/workflows/README.md`
- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
