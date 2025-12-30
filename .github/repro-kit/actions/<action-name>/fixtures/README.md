---
title: "KFM Reproducibility Kit — Action Fixtures"
path: ".github/repro-kit/actions/<action-name>/fixtures/README.md"
version: "v1.0.0"
last_updated: "2025-12-30"
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

doc_uuid: "urn:kfm:doc:github:repro-kit-action-fixtures-readme:<action-name>:v1.0.0"
semantic_document_id: "kfm-github-repro-kit-action-fixtures-readme-<action-name>-v1.0.0"
event_source_id: "ledger:kfm:doc:github:repro-kit-action-fixtures-readme:<action-name>:v1.0.0"
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

# KFM Reproducibility Kit — <action-name> Fixtures

## 📘 Overview

### Purpose

This directory contains **safe-to-publish test fixtures** used by the repro-kit action at:

- `.github/repro-kit/actions/<action-name>/`

Fixtures exist to keep **CI and local reproduction** aligned by providing:
- minimal, deterministic inputs,
- pinned “golden” expected outputs (hashes / manifests) where appropriate,
- negative cases that should reliably fail (contract/schema violations).

### Scope

| In scope | Out of scope |
|---|---|
| Small fixture inputs (synthetic or redacted) used to exercise action logic | Any restricted/sensitive datasets or privileged replays |
| Expected outputs used for deterministic regression checks (“golden” hashes) | Storing production secrets or tokens (never commit) |
| Fixtures that validate STAC/DCAT/PROV/contract handling *as artifacts* | Replacing canonical validators/tests owned in `tools/`, `schemas/`, or `tests/` |
| Documentation of fixture purpose, provenance, and licensing | Creating or redefining governance policy (see `docs/governance/*`) |

### Audience

- Contributors authoring or updating `.github/repro-kit/actions/<action-name>`
- Reviewers validating determinism, provenance packaging, and governance safety
- CI maintainers maintaining workflow parity

### Definitions

- **Fixture**: a small, versioned bundle of inputs/expected outputs used for repeatable testing.
- **Golden fixture**: a fixture with pinned expected outputs used for deterministic regression detection.
- **Negative fixture**: a fixture designed to fail validation (e.g., missing required schema field) so the action fails closed.
- **Redacted / generalized**: content modified so sensitive locations/identifiers cannot be reconstructed.

### Key artifacts

| Artifact | Path | Notes |
|---|---|---|
| Action README | `.github/repro-kit/actions/<action-name>/README.md` | Inputs/outputs contract for the action |
| Fixtures root (this doc) | `.github/repro-kit/actions/<action-name>/fixtures/README.md` | Fixture rules + inventory |
| Repro-kit actions index | `.github/repro-kit/actions/README.md` | High-level purpose + boundaries |
| Global repro-kit guidance | `.github/repro-kit/README.md` | *not confirmed in repo* — canonical repro-kit intent if present |
| Master Guide | `docs/MASTER_GUIDE_v12.md` | Canonical pipeline ordering + invariants |

### Definition of done

- [ ] Every fixture has a clear purpose and a stable fixture ID.
- [ ] Fixtures are **safe-to-publish** (no secrets, no PII, no restricted locations).
- [ ] Any external content includes license + attribution notes.
- [ ] Golden outputs are pinned via checksums and updated only with an explicit reason.
- [ ] Fixtures are small enough to run in CI quickly and consistently.
- [ ] Fixtures do not encourage bypass patterns (e.g., no guidance that would lead UI to read Neo4j directly).

---

## 🗂️ Directory Layout

### This document

| Artifact | Path |
|---|---|
| Fixtures README | `.github/repro-kit/actions/<action-name>/fixtures/README.md` |

### Related repository paths

| Area | Canonical path | Notes |
|---|---|---|
| Repro-kit root | `.github/repro-kit/README.md` | *not confirmed in repo* |
| Repro-kit actions index | `.github/repro-kit/actions/README.md` | |
| Merge-gating local actions | `.github/actions/` | Required CI gates typically live here |
| Workflows | `.github/workflows/` | |
| Schemas | `schemas/` | Optional root depending on repo state |
| Tests | `tests/` | Unit + integration tests |
| Pipelines | `src/pipelines/` | ETL + catalog builders |
| Catalogs | `data/{stac,catalog/dcat,prov}/` | Canonical STAC/DCAT/PROV homes |

### Expected file tree

~~~text
📁 .github/
└── 📁 repro-kit/
    └── 📁 actions/
        └── 📁 <action-name>/
            ├── 📄 action.yml
            ├── 📄 README.md
            └── 📁 fixtures/
                ├── 📄 README.md
                ├── 📄 fixtures.manifest.yml        # optional, recommended (not confirmed in repo)
                ├── 📁 <fixture-id-1>/
                │   ├── 📄 README.md                # fixture-level “protocol”
                │   ├── 📁 input/                   # minimal inputs for the action
                │   ├── 📁 expected/                # pinned expected outputs (if golden)
                │   └── 📁 meta/                    # optional provenance/license notes
                └── 📁 <fixture-id-2>/
                    └── ...
~~~

---

## 🧭 Context

### Why fixtures matter in KFM

KFM’s “v12-ready” posture treats validation and provenance as first-class build gates. Fixtures are how we:
- keep **repro steps deterministic** across local runs and CI runners,
- verify that provenance packaging stays stable across refactors,
- exercise failure modes for schema/contract checks (fail-closed),
- support graph integrity tests that load small, known datasets (when the action is used by graph-related workflows).

### Constraints / invariants

Fixtures must not violate KFM’s hard invariants:

- **No sensitive location leakage** (including via logs, manifests, and “expected output” files).
- **Classification propagation** must not be downgraded in fixtures (if fixture meta includes classification).
- **Provenance-first order preserved**: fixtures that include multi-stage artifacts should reflect the canonical pipeline sequence (ETL → STAC/DCAT/PROV → Graph → API → UI → Story → Focus Mode).

> If you need restricted fixtures to test restricted paths, do **not** commit them here.
> Use synthetic or generalized equivalents, or a private fixture channel (repo-specific approach: *not confirmed in repo*).

---

## 🗺️ Diagrams

### Fixture usage overview

~~~mermaid
flowchart LR
  FX["Fixtures<br/>.github/repro-kit/actions/<action-name>/fixtures/"] --> ACT["Action<br/>.github/repro-kit/actions/<action-name>"]

  ACT --> OUT["Workspace outputs / CI artifacts<br/>(manifests, hashes, packaged prov)"]
  OUT --> DIFF["Optional golden diff<br/>(expected vs actual)"]
~~~

---

## 🧾 Fixture inventory

List fixtures added for this action here so reviewers can quickly see what exists and why.

| Fixture ID | Type | Purpose | Golden? | Notes |
|---|---|---|---|---|
| *(none yet)* |  |  |  | Add entries as fixtures land |

### Fixture ID guidance

Recommended pattern (replace with repo standards if different):

- `fx-<short-purpose>-v<major>`  
  Examples: `fx-manifest-min-v1`, `fx-stac-invalid-missing-id-v1`, `fx-hash-golden-small-v1`

Rules of thumb:
- keep IDs stable; do not rename fixtures just to “tidy”
- if semantics change, add a new fixture ID or bump the `v<major>`

---

## 📦 Data & Metadata

### Fixture types

A fixture should be explicitly categorized in its fixture-level README:

- **Positive**: action should succeed and produce deterministic outputs.
- **Golden**: positive + expected outputs are checked in under `expected/`.
- **Negative**: action should fail (and should fail *consistently*).

### What a fixture may include

Depending on the action’s purpose, fixtures may include:

- **Inputs**
  - sample run manifest inputs (YAML/JSON)
  - small directory trees to hash
  - minimal STAC/DCAT/PROV artifacts to package/validate
  - config snippets used by the action

- **Expected outputs** (golden fixtures only)
  - hash reports (text/JSON)
  - packaged provenance bundles (e.g., zipped outputs)
  - normalized manifests

### What a fixture must include

At minimum, each fixture directory must include a fixture-level README acting as a “protocol”:

- objective (what this fixture proves)
- input summary + any assumptions (including pinned versions)
- expected outcome (success/failure; artifacts produced; hashes)
- safety notes (why it is safe-to-publish)
- license/attribution notes (if any external content is embedded)

> This mirrors the project’s broader preference for protocol-style, reproducible documentation.

### Determinism traps and how fixtures should avoid them

Golden fixtures are only useful if the action output is stable. Common traps:

- **Timestamps**: default “generated_at: now()” fields change every run.
  - Prefer allowing a fixed timestamp input or omitting timestamps from golden outputs.
- **Zip archives**: file ordering, mtimes, and permissions can differ across runners.
  - Prefer deterministic zip creation (sorted file list, normalized metadata) or hash the unzipped normalized content.
- **JSON/YAML ordering**: key order may differ depending on serializer.
  - Prefer canonicalization (stable key ordering) before hashing/comparison.
- **Filesystem ordering**: directory traversal order is not guaranteed.
  - Always sort before hashing/comparison.

If the action cannot reasonably be byte-for-byte deterministic, fixtures should:
- compare **normalized** outputs, or
- compare **semantic invariants** (e.g., same set of filenames + same per-file hashes), with the comparison rule documented.

### Optional fixture manifest

If you maintain many fixtures, consider an inventory file:

~~~yaml
# fixtures.manifest.yml (example only — not confirmed in repo)
fixtures:
  - id: "fx-manifest-min-v1"
    type: "positive"
    purpose: "Validate manifest packaging produces stable hash output"
    golden: true
    inputs:
      - "input/manifest.json"
    expected:
      - "expected/hash-report.json"
    classification: "open"
    sensitivity: "public"
    license: "CC-BY-4.0"
~~~

---

## 🌐 STAC, DCAT & PROV Alignment

### When fixtures include catalogs/provenance artifacts

Fixtures may embed minimal STAC/DCAT/PROV examples to test packaging/validation behavior.

If so:

- keep identifiers stable and consistent across STAC/DCAT/PROV
- keep geometry **non-sensitive** (use synthetic extents or generalized bounding boxes)
- avoid “real” restricted site coordinates even if publicly available elsewhere
- do **not** treat fixture catalogs as canonical published catalogs
  - canonical STAC/DCAT/PROV outputs live under `data/` (fixtures are test-only)

### Linking rules inside fixtures

If a fixture includes STAC/DCAT/PROV:

- A STAC Item should reference its Collection ID (if included).
- A DCAT Dataset (if included) should list distributions that correspond to the fixture artifacts.
- A PROV bundle (if included) should reference:
  - the activity/run that produced the artifact
  - inputs and outputs as entities
  - the software agent (repo commit SHA or tool version) when practical

> Keep fixtures minimal: include only what the action needs to validate/package.

---

## 🧱 Architecture

### How the action should consume fixtures

Fixtures are intended to be referenced by the action as a **path input** (pattern depends on the action contract).

Example (illustrative only):

~~~yaml
- name: Run repro-kit action with fixture
  uses: ./.github/repro-kit/actions/<action-name>
  with:
    fixture_path: ".github/repro-kit/actions/<action-name>/fixtures/fx-manifest-min-v1"
~~~

### Artifact handling

- Prefer writing generated artifacts into the runner workspace (or GitHub Actions artifact upload), not back into the fixture directory.
- Golden comparisons should compare normalized outputs against files under `expected/`.
- If the action emits “expected output” files, only commit them intentionally as **test fixtures** (not as pipeline outputs).

---

## 🧠 Story Node & Focus Mode Integration

Fixtures may include Story Node examples *only* if the action’s responsibility includes validating Story Nodes.

If Story Node fixtures exist:

- they must follow `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- every factual claim must remain evidence-led and provenance-linked
- fixtures must not contain personal data or sensitive locations

---

## 🧪 Validation & CI/CD

### Fixture validation expectations

Fixtures should be structured so that CI jobs can:

- run quickly and deterministically,
- validate schema/contract behavior,
- emit actionable diffs when a golden fixture changes.

### Suggested checks

Examples only; replace with repo commands:

~~~bash
# Validate fixtures are safe-to-publish (no secrets/PII; no sensitive coordinates)
# <TBD>

# Run the repro-kit action against all fixtures
# <TBD>

# If golden fixtures exist: compare expected vs actual hashes
# <TBD>
~~~

---

## ⚖ FAIR+CARE & Governance

### Safety requirements

Fixtures must be safe for a public repository:

- No secrets/tokens/keys (ever).
- No PII.
- No restricted locations or culturally sensitive information.
- If the fixture references real places, use generalized extents and avoid attributing sensitive context.

### Licensing

If any fixture content is derived from external sources:

- ensure the license allows redistribution in this repository,
- include attribution notes in the fixture-level README,
- prefer capturing a minimal DCAT-style snippet in `meta/` when appropriate.

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-30 | Initial fixtures README scaffold for repro-kit action fixtures | TBD |

