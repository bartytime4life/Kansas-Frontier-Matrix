<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/validation/validator-assurance-report
title: ValidatorAssuranceReport Contract
type: semantic-contract; validation; mutation-assurance; adversarial-testing
version: v0.1.0
status: draft; PROPOSED; fixture-first; no-universal-threshold
owners: OWNER_TBD — Validation steward · QA steward · Policy-test steward · Contracts steward · Security reviewer
created: 2026-08-05
updated: 2026-08-05
policy_label: public; contracts; validation; mutation-assurance; non-authoritative
related:
  - ./README.md
  - ../../schemas/contracts/v1/validation/validator_assurance_report.schema.json
  - ../../fixtures/contracts/v1/validation/validator_assurance_report/
  - ../../tools/validators/validate_validator_assurance_report.py
  - ../../tests/validators/test_validate_validator_assurance_report.py
  - ../../tests/policy/README.md
  - ../../docs/intake/exploratory/new-ideas-4-25-source-map.md
notes:
  - "Implements the bounded KFM-TRIAD-063 gap."
  - "The report records assurance evidence; it does not approve a validator or establish a universal mutation score threshold."
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

## Directory Rules basis

Semantic meaning belongs under `contracts/validation/`. Machine shape belongs under `schemas/contracts/v1/validation/`. Synthetic examples, executable validation, tests, CI, and authoring provenance remain in their established roots. The change creates no new repository root, policy bundle, test runner, release family, or public path.

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

`kfm-fixture-json-v1` removes top-level `spec_hash`, serializes sorted-key UTF-8 JSON without insignificant whitespace, preserves array order, and computes SHA-256. It is a local replay profile only.

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

A green result does not prove that mutants were actually generated or executed; that proof must come from the campaign runner, logs, mutant manifest, test output, and run receipt referenced by a real report.

## Correction and rollback

The slice is additive. Rollback removes the contract lane, schema, fixtures, validator, tests, workflow, and generated authoring receipt. It changes no existing validator, policy evaluator, test aggregate, branch protection, release gate, or published artifact.
