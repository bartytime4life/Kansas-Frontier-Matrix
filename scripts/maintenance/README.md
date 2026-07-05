# `scripts/maintenance/` — Maintenance Script Lane

Maintenance CLIs for doctrine-artifact preflight, registry hygiene, normalized-summary readiness, and bounded repository maintenance tasks.

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/scripts-maintenance-readme
title: scripts/maintenance/README.md — Maintenance Script Lane
type: readme; directory-readme; maintenance-script-index; governance-guardrail
version: v0.2
status: draft; operational-maintenance-lane; doctrine-preflight-tools-present; mixed-maturity; NEEDS VERIFICATION
owners: OWNER_TBD — Maintenance tooling steward · Doctrine steward · Registry steward · QA steward · Release steward · Docs steward
created: NEEDS VERIFICATION — README existed before v0.2 expansion
updated: 2026-07-04
policy_label: public; maintenance-scripts; doctrine-preflight; registry-hygiene; local-and-ci-helper
tags: [kfm, scripts, maintenance, doctrine-artifacts, registry, provenance, preflight, receipts, readiness, release-gates]
related:
  - ../README.md
  - ../dev/README.md
  - ../../tools/README.md
  - ../../tools/validators/
  - ../../control_plane/
  - ../../docs/runbooks/DOCTRINE_ARTIFACT_PREFLIGHT.md
  - ../../docs/adr/NORMALIZED_SUMMARY_CONSUMER_READINESS_CHECKLIST.md
  - ../../tests/policy/
  - ../../tests/source/
  - ../../receipts/doctrine_artifacts/
notes:
  - "Expanded from an existing maintenance README that already listed doctrine artifact preflight scripts and normalized-summary migration notes."
  - "Current-session search confirms maintenance helper modules, doctrine preflight CLIs, sync/check scripts, readiness checks, a test-suite wrapper, and one published-alias audit placeholder."
  - "This README documents script lane boundaries; it does not prove release readiness, CI wiring, runtime deployment, or policy approval by itself."
[/KFM_META_BLOCK_V2] -->

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: scripts/maintenance" src="https://img.shields.io/badge/root-scripts%2Fmaintenance-blue">
  <img alt="Authority: maintenance helpers" src="https://img.shields.io/badge/authority-maintenance__helpers-purple">
  <img alt="Maturity: mixed" src="https://img.shields.io/badge/maturity-mixed-orange">
  <img alt="Boundary: not release authority" src="https://img.shields.io/badge/boundary-not__release__authority-critical">
</p>

**Status:** draft / maintenance helper lane / mixed maturity  
**Path:** `scripts/maintenance/`  
**Primary lane:** doctrine-artifact preflight and registry hygiene  
**Truth posture:** CONFIRMED current script files by repository search; CONFIRMED selected behavior for the preflight runner, required-artifact checker, consumer-readiness checker, test-suite wrapper, and published-alias placeholder; NEEDS VERIFICATION for CI wiring, full command coverage, release integration, and operational ownership.

## Quick jumps

[Purpose](#purpose) · [Boundary](#boundary) · [Current inventory](#current-inventory) · [Doctrine artifact tooling](#doctrine-artifact-tooling) · [Repo fit](#repo-fit) · [Quick start](#quick-start) · [Test bundle](#test-bundle) · [Normalized summary migration](#normalized-summary-migration) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Promotion rules](#promotion-rules) · [Validation](#validation) · [Open questions](#open-questions)

---

## Purpose

`scripts/maintenance/` contains bounded repository-maintenance CLIs and wrappers.

The current confirmed focus is doctrine-artifact preflight: checking required doctrine artifacts, provenance registries, registry alignment, normalized summary readiness, and the receipt/summary payloads used by policy or release-adjacent consumers.

The parent `scripts/README.md` says `scripts/` is for small operational scripts and that long-lived trust-bearing scripts graduate to `tools/`, `pipelines/`, or `packages/`. This lane therefore stays narrow: maintenance scripts may help operators inspect and reconcile repository state, but they do not become canonical schema, policy, release, proof, or lifecycle authority.

## Boundary

This directory is not the doctrine source of truth, policy engine, validator authority, release authority, proof root, receipt root, source registry root, data lifecycle root, or CI proof by itself.

Maintenance scripts may emit JSON summaries or receipts, but emitted objects must still land in accepted receipt, proof, artifact, or release-support locations and remain subject to schemas, validators, tests, policy, review, and rollback rules.

> [!IMPORTANT]
> A successful maintenance command is not publication. It may support a gate, but it does not replace EvidenceBundle resolution, policy decisions, steward review, release manifests, correction records, rollback targets, or public-client trust boundaries.

## Current inventory

| File | Current status | Notes |
|---|---|---|
| `README.md` | present | This directory index. |
| `_cli_errors.py` | present by search | Shared structured-error helper; not inspected in this pass. |
| `_doctrine_registry.py` | present by search | Shared doctrine-registry helper; not inspected in this pass. |
| `audit_published_aliases.py` | placeholder confirmed | Contains only a greenfield placeholder comment for auditing `data/published/<domain>/current` aliases. |
| `check_required_doctrine_artifacts.py` | inspected | Checks required artifact presence, status mismatches, minimum size, duplicate hashes, and optional JSON receipt output. |
| `check_doctrine_artifact_provenance.py` | present by search | Provenance checker; summarized by existing README, not reopened in this pass. |
| `check_doctrine_registry_alignment.py` | present by search | Registry-alignment checker invoked by preflight runner. |
| `check_normalized_summary_consumer_readiness.py` | inspected | Validates normalized-summary consumer registry fields and optional all-validated gate. |
| `render_doctrine_presence_input.py` | present by search | Renders presence input from checker receipt; summarized by existing README. |
| `run_doctrine_artifact_preflight.py` | inspected | Orchestrates required-artifact check, provenance check, provenance sync, registry alignment, readiness check, presence rendering, summary schema validation, and strict gates. |
| `enforce_doctrine_preflight_gates.sh` | present by search | Strict shell wrapper for preflight gates; summarized by existing README. |
| `sync_doctrine_artifact_registry_status.py` | present by search | Reconciles required registry status against artifact files; summarized by existing README. |
| `sync_doctrine_artifact_provenance_status.py` | present by search | Reconciles provenance status when required artifacts are present; summarized by existing README. |
| `run_doctrine_artifact_test_suite.sh` | inspected | Runs preflight summary validators, normalized-only shadow checks, readiness checks, and related policy/source pytest bundle. |

## Doctrine artifact tooling

| Script | Purpose | Exit codes |
|---|---|---|
| `check_required_doctrine_artifacts.py` | Validate required doctrine artifacts against registry + filesystem and emit JSON receipt (`present`, `status_mismatches`, integrity checks). | `0=pass`, `1=fail`, `2=registry/error path via structured error` |
| `check_doctrine_artifact_provenance.py` | Validate canonical source-link provenance registry shape for required doctrine artifacts. | `0=pass`, `1=fail`, `2=registry error` |
| `render_doctrine_presence_input.py` | Render `{ "present": ... }` from a checker receipt for policy consumers. | `0=success`, `1=invalid receipt` |
| `sync_doctrine_artifact_registry_status.py` | Reconcile registry `status:` fields (`present`/`missing`) against artifact files and emit sync receipt. | `0=success`, `1=changes needed (with --fail-on-change)`, `2=registry error` |
| `sync_doctrine_artifact_provenance_status.py` | Reconcile provenance `status` (`pending` → `verified`) when required artifact files are present; optional in-place write. | `0=success` |
| `check_doctrine_registry_alignment.py` | Check alignment between required doctrine artifact registry and provenance registry. | NEEDS VERIFICATION from script help/tests |
| `check_normalized_summary_consumer_readiness.py` | Validate normalized-summary consumer readiness registry and optionally require all consumers to be validated. | `0=pass`, `1=fail` |
| `run_doctrine_artifact_preflight.py` | Orchestrate checker + provenance + sync + alignment + readiness + renderer and print a single summary payload for CI/operator use. Supports timestamped receipts by default, `--stable-filenames`, `--presence-output`, `--strict`, `--strict-provenance`, `--emit-normalized-only`, and `--require-consumer-readiness`. | `0=preflight executed/pass under selected gates`, `1=strict missing/provenance/readiness fail`, `2=execution/validation error` |
| `enforce_doctrine_preflight_gates.sh` | Strict wrapper for release/promotion automation (`--strict`, `--strict-provenance`, `--require-consumer-readiness`); forwards additional CLI args to preflight unchanged. | mirrors underlying preflight exit code |

## Repo fit

```text
scripts/
├── README.md
└── maintenance/
    ├── README.md
    ├── _cli_errors.py
    ├── _doctrine_registry.py
    ├── audit_published_aliases.py
    ├── check_required_doctrine_artifacts.py
    ├── check_doctrine_artifact_provenance.py
    ├── check_doctrine_registry_alignment.py
    ├── check_normalized_summary_consumer_readiness.py
    ├── render_doctrine_presence_input.py
    ├── run_doctrine_artifact_preflight.py
    ├── enforce_doctrine_preflight_gates.sh
    ├── sync_doctrine_artifact_registry_status.py
    ├── sync_doctrine_artifact_provenance_status.py
    └── run_doctrine_artifact_test_suite.sh

control_plane/                         # doctrine artifact registries and readiness registries
docs/doctrine/artifacts/                # doctrine artifact files checked by preflight
receipts/doctrine_artifacts/            # default preflight receipt output path
tools/validators/source/                # validators invoked by the test-suite wrapper
tests/policy/ and tests/source/         # pytest coverage invoked by test-suite wrapper
release/                                # release authority; not owned by scripts/maintenance
```

## Quick start

Run the doctrine artifact preflight:

```bash
python scripts/maintenance/run_doctrine_artifact_preflight.py
```

Run strict preflight gates through the wrapper when release/promotion automation needs fail-closed behavior:

```bash
bash scripts/maintenance/enforce_doctrine_preflight_gates.sh
```

Detailed operator flow: `docs/runbooks/DOCTRINE_ARTIFACT_PREFLIGHT.md`.

## Test bundle

Run the maintenance test bundle:

```bash
bash scripts/maintenance/run_doctrine_artifact_test_suite.sh
```

The current wrapper runs source validators, a normalized-only preflight shadow summary, normalized-summary consistency validation, consumer-readiness validation, and a policy/source pytest bundle.

## Normalized summary migration

- **Current compatibility mode:** preflight emits both standalone fields and normalized maps (`artifact_paths`, `artifact_digests`).
- **Shadow validation mode:** run preflight with `--emit-normalized-only` and validate with:

```bash
python tools/validators/source/validate_doctrine_preflight_summary_consistency.py <summary.json> --require-normalized-only
```

- **Cutover gate:** only enable normalized-only by default after all consumers read from normalized maps and CI shadow checks are green over time.
- **Readiness checklist:** `docs/adr/NORMALIZED_SUMMARY_CONSUMER_READINESS_CHECKLIST.md`.

## What belongs here

- Bounded maintenance CLIs that inspect, reconcile, or summarize repo maintenance state.
- Doctrine-artifact preflight helpers and wrappers.
- Registry hygiene scripts for required doctrine artifacts, provenance records, alignment checks, and readiness ledgers.
- Local or CI-invoked wrappers that support, but do not replace, governed release/promotion gates.
- Shared helper modules used only by this maintenance lane.

## What does not belong here

| Do not put this in `scripts/maintenance/` | Correct home |
|---|---|
| Long-lived validators, generators, builders, proof-pack tools, release tools, or QA tools | `tools/` |
| Pipeline orchestration | `pipelines/` |
| Reusable libraries imported by multiple systems | `packages/` |
| Policy rules, sensitivity decisions, rights approvals, or release approvals | `policy/`, review, and release roots |
| Source records, lifecycle data, emitted receipts, proofs, catalogs, or published payloads | accepted `data/` lifecycle, receipt, proof, catalog, or published roots |
| Release manifests, rollback cards, correction notices, or publication decisions | `release/` |
| Fixtures, golden outputs, or generated examples | `fixtures/` unless an accepted migration says otherwise |
| Secrets, credentials, signing keys, tokens, or local `.env` contents | not in repo |
| Runtime/API/UI implementation | accepted package, app, service, or UI roots |

## Promotion rules

Move or redesign a maintenance script when any of the following become true:

| Signal | Required action |
|---|---|
| The script becomes a long-lived validator or gate implementation | Promote to `tools/validators/` or another accepted `tools/` lane with tests. |
| The script orchestrates multi-step production flow | Promote orchestration to `pipelines/`; keep this script as a wrapper only if useful. |
| The script emits trust-bearing receipts or proof packs | Confirm schema, validator, receipt/proof home, tests, and rollback notes. |
| The script changes registries in-place | Require dry-run/default-safe behavior, review notes, and rollback instructions. |
| The script becomes release-critical | Add release steward review, CI evidence, strict exit-code contract, and rollback target. |

## Validation

```bash
find scripts/maintenance -maxdepth 2 -type f | sort
python -m py_compile scripts/maintenance/*.py
bash -n scripts/maintenance/*.sh
python scripts/maintenance/run_doctrine_artifact_preflight.py --stable-filenames
bash scripts/maintenance/run_doctrine_artifact_test_suite.sh
```

> [!WARNING]
> Commands that reconcile registry status or write receipts may create or update files depending on options. Review command help, output paths, and git diff before committing generated changes.

## Open questions

| Question | Status |
|---|---|
| Which CI workflow invokes `run_doctrine_artifact_preflight.py`, `enforce_doctrine_preflight_gates.sh`, or `run_doctrine_artifact_test_suite.sh`? | NEEDS VERIFICATION |
| Should doctrine-artifact preflight become a `tools/validators/` or `tools/release/` command if it is release-critical? | NEEDS VERIFICATION |
| What is the accepted home for emitted doctrine-artifact receipts: `receipts/doctrine_artifacts/`, `data/receipts/`, or another governed receipt lane? | NEEDS VERIFICATION |
| Should `audit_published_aliases.py` remain a placeholder, be implemented here, or move to `tools/validators/release/`? | NEEDS VERIFICATION |
| Which owner signs off on normalized-summary consumer readiness cutover? | NEEDS VERIFICATION |
