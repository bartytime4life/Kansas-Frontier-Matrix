<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/validation/validator-assurance-report
title: ValidatorAssuranceReport Contract
type: semantic-contract; validation; mutation-assurance; adversarial-testing
version: v0.1.0
status: draft; PROPOSED; fixture-first; workflow-defined; human-review-hold; no-universal-threshold
owners: OWNER_TBD — Validation steward · QA steward · Policy-test steward · Contracts steward · Security reviewer
created: 2026-08-05
updated: 2026-09-06
policy_label: public; contracts; validation; mutation-assurance; non-authoritative
owning_root: contracts/
responsibility: "Define semantic meaning for bounded validator-assurance evidence without executing a mutation campaign or granting authority."
truth_posture: "CONFIRMED companion paths and synthetic validator behavior / PROPOSED contract and report profile / NEEDS VERIFICATION current hosted exact-head execution, human review, and live campaign evidence"
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  commit: eaae135d8f4508c0712e3c6e151d7168a46f54ab
  tree: af2819f1f32c99970ba87c77b0219a8ecef99b4c
related:
  - ./README.md
  - ../../schemas/contracts/v1/validation/validator_assurance_report.schema.json
  - ../../fixtures/contracts/v1/validation/validator_assurance_report/
  - ../../tools/validators/validate_validator_assurance_report.py
  - ../../tests/validators/test_validate_validator_assurance_report.py
  - ../../.github/workflows/validator-assurance-report.yml
  - ../../data/receipts/generated/genrec-validator-assurance-report-20260805.json
  - ../../tools/validators/validator_registry.json
  - ../../tests/policy/README.md
  - ../../docs/intake/exploratory/new-ideas-4-25-source-map.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
notes:
  - "Implements the bounded KFM-TRIAD-063 gap."
  - "The report records bounded assurance evidence; it does not approve a validator or establish a universal mutation score threshold."
  - "The dedicated workflow is a read-only synthetic profile, not a mutation engine or aggregate-registry entry."
  - "The 2026-08-05 generated receipt is an authoring/integrity receipt, not evidence that a live mutation campaign ran."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `ValidatorAssuranceReport`

> A deterministic, reviewable record showing whether a bounded adversarial or mutation campaign detected semantically dangerous validator changes—and which mutants survived.

## Purpose

Positive fixtures and line coverage show that selected paths execute. They do not prove that a validator detects fail-open changes, removed reference checks, reversed time comparisons, identity collapse, or policy-boundary bypasses.

`ValidatorAssuranceReport` records:

- the exact validator target and digest;
- the test command and versioned assurance profile;
- deterministic campaign identity and seed;
- a sorted, explicit mutation-operator set;
- a manifest digest for generated mutants;
- killed, survived, invalid, and timed-out counts;
- an exact survivor inventory;
- semantic-gap and risk classifications;
- review/fix disposition and issue references;
- a finite assurance outcome; and
- explicit non-authority declarations.

The first slice models and validates assurance evidence. It deliberately does not introduce or select a mutation engine.

## Current repository posture

The following readback is pinned to `main@eaae135d8f4508c0712e3c6e151d7168a46f54ab`, immediately before this contract-only refresh. File presence and blob identity establish repository content, not a successful hosted run, human review, or real mutation campaign.

| Surface | Current evidence | Posture |
|---|---|---|
| Semantic contract | `contracts/validation/validator_assurance_report.md`, blob `be109d6c3ae39f2c473096b8304cda6e6451d4a9` | This document; `PROPOSED` |
| Machine shape | `schemas/contracts/v1/validation/validator_assurance_report.schema.json`, blob `155cbc392d8a97e83ec2eba0301c562b1a9246cb` | Draft 2020-12 schema; `PROPOSED` |
| Synthetic fixtures | Four valid and nine invalid JSON fixtures under `fixtures/contracts/v1/validation/validator_assurance_report/` | Exact fixture polarity and reviewed finding-code inventory; no mutant is executed |
| Executable validator | `tools/validators/validate_validator_assurance_report.py`, blob `ce5681effe37e28b1553ad37049e1d59e478c874` | No-network, fail-closed schema and semantic checks |
| Focused tests | `tests/validators/test_validate_validator_assurance_report.py`, blob `20d59106251f216ae2b657db4e7c9bb4a6506d3b` | Covers schema validity, fixture polarity, unsafe JSON, diagnostic non-echo, and deterministic replay |
| Dedicated workflow | `.github/workflows/validator-assurance-report.yml`, blob `d266c4bcdf045dfda00becea5df435641b230753` | Read-only profile on matching pull requests, `main` pushes, and manual dispatch; no live source or mutation execution |
| Generated authoring receipt | `data/receipts/generated/genrec-validator-assurance-report-20260805.json`, blob `3d10fa4d978af63121ae190955655b8e6019f6c0` | Records historical local focused-test and receipt-integrity passes; hosted exact-head CI and human review were skipped in that receipt |
| Aggregate validator registry | `tools/validators/validator_registry.json`, blob `72c8c53617aecebfa50cb89d7f8b40b0eeeb8992` | No `validator-assurance` profile or validator entry; this slice is not wired into the registry-driven aggregate profile |
| Current hosted readback | `main@eaae135d8f4508c0712e3c6e151d7168a46f54ab` | The commit readback returned no associated pull-request workflow runs or combined status entries; no current exact-head result is claimed |

The companion artifacts remain `PROPOSED`. The generated receipt's `contract_version` field (`3.0.0`) belongs to that receipt artifact; the report object continues to require `schema_version: 1.0.0`.

## Directory Rules basis

Semantic meaning belongs under `contracts/validation/`. Machine shape belongs under `schemas/contracts/v1/validation/`. Synthetic examples, executable validation, tests, CI, and authoring provenance remain in their established roots. The dedicated workflow and receipt are linked implementation and lineage surfaces, not additional semantic authorities. This change creates no new repository root, policy bundle, test runner, release family, or public path.

The placement follows the accepted Directory Rules decision recorded by ADR-0029: `contracts/` defines meaning, `schemas/` defines machine shape, `tests/` provides executable conformance evidence, and `tools/` owns validators. A control-plane or validator registry projection cannot self-authorize a new rule or an assurance result.

## Machine shape and authority boundary

The v1 report object requires:

- `object_type: ValidatorAssuranceReport`;
- `schema_version: 1.0.0`;
- a deterministic `assurance_id`, `hash_profile`, and `spec_hash`;
- `target`, `campaign`, `results`, `survivors`, `adequacy`, and `provenance`; and
- `governance` with every authority flag `false` and `release_ref: null`.

The campaign fixes `network_used` to `false`. The `provenance.run_receipt_ref` and `input_refs` fields identify the evidence that a real report would need; synthetic fixtures use synthetic references and do not substitute for a real run receipt.

## Counts and rate representation

`total` must equal:

```text
killed + survived + invalid + timed_out
```

`survived` must equal the survivor inventory length.

The kill rate is represented as the exact rational pair:

```text
kill_rate_numerator   = killed
kill_rate_denominator = killed + survived
```

This avoids float-rounding disputes and keeps invalid/time-out operational failures separate from assessable mutants.

## Survivor semantics

Every survivor records:

- a stable mutant ID;
- mutation operator;
- a location reference that does not echo source code;
- semantic-gap class;
- risk class;
- disposition;
- reason codes; and
- an optional issue/review reference.

High-risk survivors are visible even when an issue already exists. A medium or low survivor remains unreviewed when its disposition is `FIX_REQUIRED` or `REVIEW_REQUIRED` and no issue reference exists.

## Finite outcomes

| Outcome | Required meaning |
|---|---|
| `PASS` | No high-risk survivor, no unreviewed survivor, no invalid/time-out result, and no further review required. Equivalent or explicitly out-of-scope survivors may remain only when disposition is already reviewed. |
| `HOLD` | One or more non-high-risk survivors require review; review is required. |
| `FAIL` | At least one `HIGH` or `CRITICAL` survivor exists; review is required. |
| `ERROR` | Campaign execution produced invalid or timed-out mutants; review is required. |

The report does not convert `PASS` into validator approval, merge permission, policy authority, promotion, or release.

## No universal threshold

`universal_threshold_applied` is fixed to `false`. Mutation adequacy is contextual. A low aggregate score can be acceptable when surviving mutants are reviewed equivalents; a high score can still hide one dangerous fail-open survivor. The semantic survivor inventory outranks one percentage.

Any later threshold profile must be independently versioned, reviewed, and bound to consequence, validator role, and risk. This contract does not invent one.

## Deterministic fixture hash

`kfm-fixture-json-v1` removes top-level `spec_hash`, serializes sorted-key UTF-8 JSON without insignificant whitespace, preserves array order, and computes SHA-256. It is a local replay profile only. It does not bind a live campaign, generated mutant bytes, or a real validator run.

## Execution profile and evidence boundary

The dedicated workflow is the current repository execution declaration for this slice. It checks out the tested revision without persisted credentials, installs declared test dependencies, and runs the following bounded commands:

```bash
python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_validator_assurance_report.py' \
  --verbose

python tools/validators/validate_validator_assurance_report.py --fixtures

python tools/validators/validate_generated_receipt.py \
  data/receipts/generated/genrec-validator-assurance-report-20260805.json \
  --repo-root .
```

It also checks Draft 2020-12 schema validity and parses every fixture JSON file. The workflow advertises `KFM_NO_NETWORK=1`, grants `contents: read`, and records its result as a bounded step summary. A workflow definition is not a current workflow result.

This profile is intentionally separate from the aggregate `tools/validators/validator_registry.json`. Adding it to the aggregate registry, changing its trigger scope, or introducing a mutation runner requires a separate reviewed change that updates the registry, tests, receipt, and rollback evidence together.

## Real campaign evidence required

A future real campaign report must bind, at minimum:

1. the exact validator target digest and test command;
2. a versioned assurance profile and profile digest;
3. a deterministic campaign ID, seed, sorted operator set, and mutant-manifest digest;
4. killed, survived, invalid, and timed-out results whose arithmetic matches the survivor inventory;
5. semantic-gap, risk, disposition, and review/issue references for survivors;
6. an actual run receipt and input references; and
7. the finite outcome and all-false governance fields.

The current synthetic fixtures and the `genrec-validator-assurance-report-20260805` authoring receipt do not establish any of those facts for a live mutation campaign. In particular, no mutation engine, mutant manifest, generated mutant execution, survivor set, or live campaign result is claimed by this contract refresh.

## Validation boundary

The validator fails closed on unsafe JSON and enforces:

- non-placeholder digests and exact `spec_hash`;
- canonical operator, survivor, reference, and reason-code ordering;
- mutant-count and survivor-inventory arithmetic;
- exact rational rate fields;
- high-risk and unreviewed survivor counts;
- finite-outcome consistency;
- prohibition of a universal threshold;
- campaign/provenance time order; and
- non-authority governance fields.

The focused test file additionally covers duplicate-key rejection, non-finite-number rejection, missing-file errors, non-echoing diagnostics, and deterministic serialization. The `--fixtures` profile expects four valid fixtures and nine invalid fixtures with exact reviewed finding codes.

A green result proves only the bounded schema and semantic invariants implemented by the repository validator. It does not prove that mutants were generated or executed, that a validator is adequate in production, that a policy was evaluated, or that review, merge, promotion, release, deployment, publication, or public use is authorized. No new exact-head hosted result or human review is claimed by this documentation update.

## Correction and rollback

This refresh changes only the semantic Markdown at `contracts/validation/validator_assurance_report.md`; it does not change the schema, fixtures, validator, focused tests, workflow, registry, or generated receipt. Before merge, rollback is the reversible restoration of the prior contract blob `be109d6c3ae39f2c473096b8304cda6e6451d4a9` or closure of the draft pull request and deletion of its branch. After an authorized merge, revert the documentation commit.

Retiring the full profile, wiring it into the aggregate registry, selecting a mutation engine, or changing any authority boundary requires a separate reviewed change with refreshed companion artifacts and explicit rollback evidence.
