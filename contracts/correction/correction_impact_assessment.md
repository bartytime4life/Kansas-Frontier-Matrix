<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/correction/correction-impact-assessment
title: CorrectionImpactAssessment Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive
owners: OWNER_TBD — correction steward · release steward · validation steward
created: 2026-08-09
updated: 2026-09-07
policy_label: internal; fixture-only; non-authoritative; correction; rollback-aware
related:
  - ./correction_notice.md
  - ./correction_propagation_plan.md
  - ./supersession_notice.md
  - ../../schemas/contracts/v1/correction/correction_impact_assessment.schema.json
  - ../../fixtures/contracts/v1/correction/correction_impact_assessment/
  - ../../tools/validators/correction/validate_correction_impact_assessment.py
  - ../../tests/validators/correction/test_correction_impact_assessment.py
tags: [kfm, correction, impact, propagation, cache, map, search, ai, rollback]
[/KFM_META_BLOCK_V2] -->

# CorrectionImpactAssessment Contract

> **Profile:** `kfm.correction.impact-assessment.v1`  \
> **Schema:** `1.0.0`  \
> **Execution profile:** `FIXTURE_ONLY_NO_NETWORK`  \
> **Authority:** none

## Purpose and currentness

`CorrectionImpactAssessment` is a deterministic, read-only assessment of the
carriers that a named correction may affect. It records the proposed action,
reason codes, artifact references, review state, policy binding, and rollback
target needed for a later decision. It does not perform the action.

This README is documentation for the existing contract surface. It does not
change the JSON Schema, fixtures, validator, policy, release lane, or runtime
behavior. The implementation authority snapshot used for this refresh is
`main@daf554239d8f22b7825a7e8700b70ad71c14b3b0`, inspected on 2026-09-07.
The prior README blob was
`c397c83f558299388f9d5ca0a9c58deffb3f8c86`.

The requested `ccontracts/...` path does not exist in the repository; the
intended current path is `contracts/correction/correction_impact_assessment.md`.

## Non-authority boundary

An assessment is an inert contract record. Even a valid `COMPLETE` record:

- does not mutate the catalog, API payloads, maps, tiles, search indexes,
  graph projections, exports, AI answers, caches, or documentation;
- does not invalidate a cache, withdraw an export, repoint an alias, rebuild a
  derivative, or publish a replacement;
- does not create authority, approve policy, authorize a release, or grant
  public use; and
- does not replace a `CorrectionNotice`, `CorrectionPropagationPlan`,
  `SupersessionNotice`, policy decision, `ReleaseManifest`, or rollback card.

The five authority flags are schema-constrained to `false`:
`authority_created`, `repository_mutation_allowed`, `release_authorized`,
`publication_authorized`, and `public_use_allowed`.

## Record semantics

The schema requires these top-level fields:

| Field | Contract meaning |
| --- | --- |
| `profile` | Must be `kfm.correction.impact-assessment.v1`. |
| `schema_version` | Must be `1.0.0`. |
| `assessment_id` | `kfm:correction-impact:` plus the first 16 hex characters of the computed digest. |
| `correction_notice_ref` | Reference to the named correction being assessed. |
| `assessed_at` | Canonical UTC second: `YYYY-MM-DDTHH:MM:SSZ`. |
| `review_state` | `PENDING`, `APPROVED`, `CHANGES_REQUESTED`, or `REJECTED`. |
| `policy_decision_ref` | A reference or `null`; required for a `COMPLETE` result. |
| `rollback_target_ref` | A reference or `null`; required for a `COMPLETE` result. |
| `carriers` | Exactly ten carrier records in canonical order. |
| `outcome` | Record outcome: `COMPLETE` or `HOLD`. |
| `assessment_digest` | SHA-256 digest over the canonical payload excluding `assessment_id` and `assessment_digest`. |
| authority flags | All five are required and must be `false`. |

The record-level `outcome` enum is only `COMPLETE` or `HOLD`. The validator
uses `ERROR` as a fail-closed diagnostic result when input, schema, semantic,
identity, digest, or outcome checks fail. `ERROR` is therefore not a valid
persisted assessment outcome.

## Canonical carrier inventory

Every assessment has exactly one row for each carrier, in this order:

1. `CATALOG`
2. `API`
3. `MAP`
4. `TILE`
5. `SEARCH`
6. `GRAPH`
7. `EXPORT`
8. `AI`
9. `CACHE`
10. `DOCUMENTATION`

Each row requires `carrier`, `affected`, `action`, `reason_codes`, and
`artifact_refs`.

### Affected rows

An affected row uses an action other than `NO_ACTION` and includes at least
one reason code and one artifact reference. The assessment describes the
needed follow-up; it does not execute it.

Two carrier-specific safeguards are mandatory:

- An affected `CACHE` row uses `INVALIDATE` and includes
  `CACHE_INVALIDATION_REQUIRED`.
- An affected `AI` row uses `REVALIDATE`, `WITHDRAW`, or `SUPERSEDE` and
  includes `CITATIONS_REVALIDATE`.

### Unaffected rows

An unaffected row uses `NO_ACTION`, has no artifact references, and includes
`NOT_APPLICABLE_CONFIRMED` in `reason_codes`. This prevents an assessment from
collapsing an unexamined carrier into a silent omission.

## Outcome and review gates

The validator computes `COMPLETE` only when:

- the JSON is readable, finite, and duplicate-key free;
- the schema is valid;
- the carrier inventory and carrier-specific semantics are closed;
- `assessment_id` and `assessment_digest` match the canonical payload;
- `review_state` is `APPROVED`;
- `policy_decision_ref` is a non-empty string; and
- `rollback_target_ref` is a non-empty string.

Otherwise the validator returns a fail-closed diagnostic (`ERROR`) or a
schema-valid record with `HOLD`, depending on which boundary is reached. A
`HOLD` assessment is not an approval and cannot be treated as release,
publication, or public-use readiness.

## Relationship to adjacent correction artifacts

| Artifact | Responsibility | Boundary |
| --- | --- | --- |
| [CorrectionNotice](./correction_notice.md) | Names and describes the correction event. | Does not prove carrier closure or authorize execution. |
| [CorrectionPropagationPlan](./correction_propagation_plan.md) | Enumerates dependency and propagation planning. | Does not execute propagation or replace this assessment. |
| [SupersessionNotice](./supersession_notice.md) | Records old/new lineage and supersession intent. | Does not mutate public or derived surfaces. |
| `CorrectionImpactAssessment` | Assesses the ten carrier rows and binds review/policy/rollback references. | Fixture-only, no-network, non-executing. |
| Release correction lane | Reviews release and rollback artifacts. | Separate from contract semantics. |

An assessment may be evidence for a later release or policy review, but no
document in this lane grants that later authority by implication.

## Verified implementation surfaces

The following surfaces were present at the pinned main commit:

- **Schema:** [correction_impact_assessment.schema.json](../../schemas/contracts/v1/correction/correction_impact_assessment.schema.json), blob `f721aa7cd9c1b30cf63ab108f12c9b08927fd0bf`.
- **Schema index:** [schemas/contracts/v1/correction/README.md](../../schemas/contracts/v1/correction/README.md), blob `95ade6418f91db518d4813299b5c25ca05f20815`.
- **Valid fixtures:** [valid/](../../fixtures/contracts/v1/correction/correction_impact_assessment/valid/) contains `complete.json` (blob `f29dbf363d691ab26c5a9515c330fd2eb7f331e2`) and `hold.json` (blob `9ae88825c280844d4fccd1abf706858b5e8470da`).
- **Negative fixtures:** [invalid/](../../fixtures/contracts/v1/correction/correction_impact_assessment/invalid/) covers missing AI citation, invalid cache action, digest mismatch, and missing carrier. Their blobs are `114fcf629a110a0a1f147f04c80cfe9157e6b61f`, `f2bc3544c3e4abac723c9bf87759fb0c50ac9e0e`, `e39222c9b078e5af74c159df0932db1427efc0f7`, and `c08a5e714c47f68897019ff29d001aa9949fdb5d` respectively.
- **Validator:** [validate_correction_impact_assessment.py](../../tools/validators/correction/validate_correction_impact_assessment.py), blob `2d78540bb04a906fee7e86588fac71303511d787`.
- **Focused tests:** [test_correction_impact_assessment.py](../../tests/validators/correction/test_correction_impact_assessment.py), blob `e720222ec5d695a5e8db2be75048d4f07863eeb9`.

The focused test file covers deterministic valid profiles (`COMPLETE` and
`HOLD`), fail-closed invalid profiles, digest and ID recomputation, the
authority flags, and zero network calls. It does not claim hosted CI success
or repository-wide validation.

## Policy, release, and documentation boundaries

The repository has no dedicated `policy/correction/` directory at this
snapshot. General policy entry points are [policy/README.md](../../policy/README.md),
[policy/contract/README.md](../../policy/contract/README.md),
[policy/decision/README.md](../../policy/decision/README.md), and
[policy/review/README.md](../../policy/review/README.md). Correction rights
guidance, where applicable, is separately located at
[policy/rights/correction/README.md](../../policy/rights/correction/README.md).
Those locations are policy context, not an implicit approval binding for this
fixture-only record.

Release review is a separate lane:

- [release/correction/README.md](../../release/correction/README.md)
- [release/correction/rollback/README.md](../../release/correction/rollback/README.md)
- [policy/release/README.md](../../policy/release/README.md)

The correction doctrine and publication boundary are documented in
[docs/doctrine/corrections-first-class.md](../../docs/doctrine/corrections-first-class.md)
and [docs/architecture/publication/CORRECTION.md](../../docs/architecture/publication/CORRECTION.md).
Neither document is a substitute for the machine schema or for an accepted
release/policy decision.

The parent [contracts/correction/README.md](./README.md) and
[contracts/release/README.md](../../contracts/release/README.md) still contain
placement and maturity questions. This refresh records the verified current
paths without silently resolving those broader repository decisions.

## Validation profile

Run from the repository root with network disabled:

```bash
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python -m pytest -q tests/validators/correction/test_correction_impact_assessment.py

PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tools/validators/correction/validate_correction_impact_assessment.py \
  fixtures/contracts/v1/correction/correction_impact_assessment/valid/*.json
```

The first command exercises the focused `unittest` suite through pytest. The
second command validates the two positive fixtures and emits the validator's
canonical JSON report. Neither command performs network access, writes a
repository artifact, or authorizes a lifecycle transition.

## Evidence and coordination lineage

GitHub is the implementation authority. The pinned GitHub commit, exact blob
IDs, schema, fixtures, validator, and tests above are the authoritative
implementation evidence for this README.

Notion was consulted read-only for coordination context:

- [KFM Repository Workbench](https://app.notion.com/p/3c9a92021bf68195b8b1f3a8d694b447?pvs=204)
  reiterates that GitHub remains implementation authority and that coordination
  pages do not authorize merge, release, deployment, or publication.
- [KFM Issue #4228 — Frozen Catalog Correction-Mechanism Decision Package](https://app.notion.com/p/3cfa92021bf681eda2f7c8baa90217b5?pvs=204)
  records a separate correction-mechanism hold; it does not bind this contract
  or authorize a topology correction.

Google Drive was consulted read-only for durable chronology and lineage:

- [KFM System Chronicle](https://docs.google.com/document/d/1fBOUDqrcsHaPJiEfM5HmtJL7fBMKFr-rgoN2ge_uVrI/edit?usp=drivesdk)
  records the same GitHub-authority, append-only, rollback-aware, and
  no-publication-without-separate-review boundaries.

These Notion and Drive artifacts are coordination evidence only. They are not
editable masters for this file, do not supersede GitHub, and do not prove that
the assessment is approved, released, published, or usable by the public.

## Rollback

Before merge, close or abandon the draft PR and preserve the current main
history. After any separately authorized merge, use an ordinary reviewed
forward revert of the single documentation commit. The rollback target for
this README is the prior blob
`c397c83f558299388f9d5ca0a9c58deffb3f8c86`.

Do not delete the schema, fixtures, validator, tests, correction history, or
release evidence. Reverting this README does not roll back a correction
assessment, mutate a carrier, or restore any public surface.

## Definition of done for a future contract promotion

Promotion beyond this proposed-inactive, fixture-only state requires a
separate reviewed decision that establishes, at minimum:

- a named owner and steward responsibilities;
- an accepted policy decision path and review record;
- schema/fixture/validator/test parity for every changed rule;
- explicit separation of assessment outcome from execution authority;
- a resolved relationship between `contracts/correction/` and
  `release/correction/`; and
- a rollback target that is independently reviewable and does not depend on
  deleting history or silently replacing a public artifact.

Until those gates are met, this document remains a repository-grounded
semantic contract description, not an activation or release declaration.
