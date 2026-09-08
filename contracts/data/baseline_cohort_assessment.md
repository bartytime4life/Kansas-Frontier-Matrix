<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/data/baseline-cohort-assessment
title: BaselineCohortAssessment Contract
type: contract
version: v0.2.0
status: proposed; fixture-first; local-only; non-authoritative
owners: OWNER_TBD — data steward; analysis steward; domain baseline steward; validation steward
created: 2026-08-10
updated: 2026-09-08
policy_label: repository-facing; baseline; cohort; discontinuity; fail-closed
owning_root: contracts/
responsibility: Bind a versioned baseline manifest, cohort eligibility, discontinuities, validation result, and rebuild provenance into one replayable review candidate.
truth_posture: cite-or-abstain
related:
  - ./README.md
  - ./material_change_assessment.md
  - ../../schemas/contracts/v1/data/baseline_cohort_assessment.schema.json
  - ../../tools/validators/data/validate_baseline_cohort_assessment.py
  - ../../fixtures/contracts/v1/data/baseline_cohort_assessment/cases.json
  - ../../tests/data/test_baseline_cohort_assessment.py
  - ../../.github/workflows/baseline-cohort-assessment.yml
  - ../../data/receipts/generated/genrec-baseline-cohort-assessment-20260810.json
  - ../../docs/intake/exploratory/new-ideas-4-16-source-map.md
  - ../../docs/kfm_full_atlas_seed_cards.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
notes:
  - "A coherent baseline is a review candidate, not a scientific threshold, anomaly decision, policy decision, or release object."
  - "The profile uses synthetic references and digests only; it does not fetch observations or prove the referenced bytes exist."
  - "Version v0.2.0 documents the existing v0.1.0 machine contract; it does not change its schema or finite-state behavior."
[/KFM_META_BLOCK_V2] -->

# BaselineCohortAssessment

> **Purpose.** Make a proposed baseline inspectable as a versioned, replayable evidence artifact whose cohort eligibility, exclusions, missingness, method identity, discontinuities, validation result, and rebuild provenance remain explicit.

## Status and evidence snapshot

This revision documents the implementation present at
`main@d58c91b5ca5efb915bb21bf8d6945c46faa41e47`. The pin is a review
snapshot, not a permanent current-state claim.

| Surface | Verified responsibility | Boundary |
|---|---|---|
| `schemas/contracts/v1/data/baseline_cohort_assessment.schema.json` | Closed Draft 2020-12 shape for profile `kfm.data.baseline-cohort.fixture.v1` and schema version `0.1.0`. | Shape only; it does not derive state or resolve references. |
| `tools/validators/data/validate_baseline_cohort_assessment.py` | Deterministic identity, accounting, temporal, discontinuity, lineage, and derived-state checks. | Local consistency only; coherent input returns `HOLD`, never `ALLOW`. |
| `fixtures/contracts/v1/data/baseline_cohort_assessment/cases.json` | Nineteen synthetic cases: nine coherent `HOLD` cases and ten fail-closed `DENY` cases. | Synthetic coverage is not domain adoption or scientific fitness. |
| `tests/data/test_baseline_cohort_assessment.py` | Ten focused tests covering schema validity, fixture polarity, state derivation, accounting, lineage, identity tamper, unsafe input forms, and no-network imports. | Does not fetch or recompute any referenced artifact. |
| `.github/workflows/baseline-cohort-assessment.yml` | Read-only, path-scoped fixture and focused-test execution with a generated-receipt integrity replay. | CI success is not review, policy, release, or publication authority. |
| `data/receipts/generated/genrec-baseline-cohort-assessment-20260810.json` | Immutable authoring receipt for the six-file introduction at `978cd53371014e9bd5c659787de0eba9b32094b7`. | Historical byte binding; it does not attest later documentation revisions. |

## Source basis and dependency readiness

Full Atlas triad `KFM-TRIAD-036`, especially programming card
`KFM-CAND-0108`, proposes `BaselineManifest`, `CohortEligibilityReport`,
`DiscontinuityRecord`, `BaselineValidationReport`, and
`BaselineRebuildReceipt` semantics. The reconciled April 16 intake calls for
stable cohort eligibility, explicit method and station discontinuities, and
reproducible baseline construction. Its example thresholds are design inputs,
not values adopted by this generic contract.

Stable structural diff and material-change semantics now exist separately as
`tools/diff/stable_diff.py` and `material_change_assessment.md`. This contract
binds a baseline review candidate; it neither computes a baseline nor decides
whether a later observation is anomalous or materially changed.

## Responsibility boundary

| This contract owns | It does not own |
|---|---|
| Meaning and relationship of the five composite parts | Domain eligibility rules, scientific thresholds, or statistical estimators |
| Deterministic assessment identity | Existence, admissibility, or integrity of referenced bytes |
| Count closure and declared missingness semantics | Imputation, weighting, smoothing, or bias correction |
| Explicit discontinuity records and resolution declarations | Evidence review or scientific acceptance of a resolution |
| Rebuild and predecessor bindings | Source admission, lifecycle writes, correction approval, or rollback execution |
| Finite local validation states | Policy, review, release, deployment, or publication decisions |

## Top-level object

The schema is closed: undeclared fields are rejected. Every field below is
required, including nullable lineage fields inside nested objects.

| Field | Meaning | Required rule |
|---|---|---|
| `object_type` | Object-family discriminator. | Exactly `BaselineCohortAssessment`. |
| `schema_version` | Machine-contract version. | Exactly `0.1.0`; this document's `v0.2.0` is a prose revision only. |
| `profile` | Safety and execution profile. | Exactly `kfm.data.baseline-cohort.fixture.v1`. |
| `assessment_id` | Content-derived stable identity. | `kfm:baseline-cohort:` plus the 64 lowercase hexadecimal digest. |
| `subject_ref` | Repository-safe reference to the baseline subject. | Reference only; the validator does not dereference it. |
| `baseline_manifest` | Inputs, time window, method, profiles, cadence, and tool versions. | Complete manifest defined below. |
| `cohort_eligibility_report` | Candidate, eligible, excluded, and missing population accounting. | Counts and missingness must reconcile. |
| `discontinuity_records` | Declared changes that may break comparability. | Canonical references, chronological order, and bounded resolutions. |
| `baseline_validation_report` | Claimed state plus required decision, reason, and obligation. | Re-derived by the validator; self-promotion is rejected. |
| `baseline_rebuild_receipt` | Rebuild output/toolchain digests and predecessor/correction lineage. | Process memory only. |
| `governance` | Fixed non-authority and no-network assertions. | All constants must match the fixture-only profile. |
| `spec_hash` | RFC 8785 JCS plus SHA-256 identity digest. | Must match the identity projection. |

## Composite semantics

### Baseline manifest

The manifest binds at least one input artifact and one source reference. It
also records a semantic baseline version, predecessor reference, aggregate
input digest, source-role profile, inclusive lookback scope, seasonal,
eligibility, parameter, and uncertainty profile references, recalculation
cadence, method identity/version, and tool versions.

- `baseline_version` and `method_version` are semantic versions of the form
  `MAJOR.MINOR.PATCH`.
- `recalculation_cadence` uses the bounded form `P<number>D`, `P<number>W`,
  `P<number>M`, or `P<number>Y`; it is a declaration, not scheduler authority.
- `input_artifact_refs` and `source_refs` must be sorted and duplicate-free.
- Digests bind declared bytes but do not prove those bytes are available,
  rights-cleared, sensitive-safe, or scientifically appropriate.

### Cohort eligibility and missingness

The following identities are mandatory:

\[
\texttt{candidate\_count} = \texttt{eligible\_count} +
\texttt{excluded\_count} + \texttt{missing\_count}
\]

\[
\sum \texttt{exclusion\_reason\_counts} = \texttt{excluded\_count}
\]

Missingness is derived independently of exclusions:

| Condition | Required `missingness_state` |
|---|---|
| No candidates or no eligible members | `INSUFFICIENT` |
| At least one eligible member and `missing_count > 0` | `PARTIAL` |
| At least one eligible member and `missing_count = 0` | `COMPLETE` |

`known_blind_spots` must be sorted and duplicate-free. Counts describe the
declared cohort only; they do not establish representativeness, minimum sample
size, spatial coverage, temporal coverage, or fitness for inference.

### Discontinuities

Allowed kinds are `METHOD_CHANGE`, `SENSOR_RELOCATION`,
`INSTRUMENT_CHANGE`, and `SOURCE_CHANGE`. Allowed resolutions are
`SEGMENT_BASELINE`, `EXCLUDE_AFTER`, `INCLUDE_WITH_QUALIFICATION`, and
`UNRESOLVED`.

- Every effective time must fall within the declared lookback interval.
- References must be unique and canonically sorted; records must also be
  chronological by effective time and reference.
- `SEGMENT_BASELINE` requires both predecessor and successor segment refs.
- Nullable segment fields remain present for other resolutions.
- A resolution declaration records treatment; it is not evidence that the
  treatment is scientifically acceptable.

### Rebuild lineage

`previous_baseline_ref` must equal `supersedes_baseline_ref`, and a baseline
cannot supersede itself. A non-null `correction_ref` requires a predecessor.
The rebuild receipt records generation time plus output and toolchain digests;
it does not confer proof, correction, catalog, release, or rollback authority.

## State derivation and precedence

The validator ignores self-asserted promotion and derives state in this order:

1. Any unresolved discontinuity yields `DISCONTINUITY_UNRESOLVED`.
2. Otherwise, zero candidates or zero eligible members yields `INSUFFICIENT`.
3. Otherwise, any exclusion, missing member, or declared discontinuity yields
   `QUALIFIED`.
4. Otherwise, the state is `REPLAYABLE`.

| Derived state | Required decision | Required reason | Required obligation |
|---|---|---|---|
| `REPLAYABLE` | `REVIEW_CANDIDATE` | `BASELINE_REPLAYABLE` | `HUMAN_REVIEW_REQUIRED` |
| `QUALIFIED` | `REVIEW_CANDIDATE` | `BASELINE_QUALIFIED` | `REVIEW_EXCLUSIONS_AND_DISCONTINUITIES` |
| `INSUFFICIENT` | `HOLD` | `INSUFFICIENT_ELIGIBLE_COHORT` | `REBUILD_COHORT_BEFORE_USE` |
| `DISCONTINUITY_UNRESOLVED` | `HOLD` | `BASELINE_DISCONTINUITY_UNRESOLVED` | `RESOLVE_DISCONTINUITY_BEFORE_USE` |

The required reason and obligation may appear with additional bounded codes,
but their presence does not bypass schema, identity, or semantic checks.

## Temporal, identity, and diagnostic invariants

The complete temporal order is:

```text
lookback_started_at < lookback_ended_at <= generated_at <= evaluated_at
```

All timestamps must be timezone-aware. `spec_hash` is SHA-256 over the RFC
8785 canonical form of the complete assessment with only `assessment_id` and
`spec_hash` omitted. `assessment_id` is reconstructed from that digest. Any
content edit without resealing is denied.

The validator returns:

- `HOLD` with no findings for a coherent fixture-only assessment;
- `DENY` with bounded finding codes and JSON Pointers for schema, identity,
  count, time, ordering, lineage, state, reason, obligation, or unsafe-input
  failures.

Diagnostics do not echo candidate values. Duplicate-key JSON, symbolic-link
inputs, malformed JSON, and canonicalization failures are rejected. The
validator contains no network-client imports and performs no network access.

## Validation and replay

```bash
python tools/validators/data/validate_baseline_cohort_assessment.py --fixtures

python -m pytest tests/data/test_baseline_cohort_assessment.py \
  -q --strict-config --strict-markers

python tools/validators/validate_generated_receipt.py \
  data/receipts/generated/genrec-baseline-cohort-assessment-20260810.json \
  --repo-root . \
  --artifact-git-ref 978cd53371014e9bd5c659787de0eba9b32094b7
```

The first two commands validate current executable behavior. The third replays
the immutable introduction receipt against its exact ancestor commit. That
historical receipt must not be rewritten to claim later documentation bytes.
Hosted workflow results belong to the exact commit that ran them and do not
transfer review or authority to a later head.

## Consumer and lifecycle boundary

A coherent object may proceed only as a review input:

```text
BaselineCohortAssessment(HOLD)
  -> domain and scientific review
  -> candidate-versus-baseline comparison
  -> MaterialChangeAssessment
  -> evidence, rights, sensitivity, policy, review, and release gates
```

This contract does not advance `RAW`, `WORK`, `QUARANTINE`, `PROCESSED`,
`CATALOG`, `TRIPLET`, or `PUBLISHED` state. It does not authorize a scheduler,
watcher, anomaly emitter, UI claim, AI answer, export, source activation,
deployment, promotion, or publication.

## Directory Rules basis

Meaning belongs in `contracts/data/`; machine shape in
`schemas/contracts/v1/data/`; validation in `tools/validators/data/`; synthetic
cases in `fixtures/contracts/v1/data/`; tests in `tests/data/`; provenance in
`data/receipts/generated/`. No new responsibility root, policy home, lifecycle
stage, catalog, proof, release, or publication authority is added.

## Change control and rollback

Changes to prose must be checked against the schema, validator, fixtures,
tests, workflow, and historical receipt boundary. Machine-behavior changes
require a dependency-closed schema/validator/fixture/test revision rather than
documentation drift.

Before integration, close the draft pull request and delete its feature branch
to abandon this documentation revision. After integration, revert the bounded
documentation/workflow commit. Reverting the prose does not delete historical
receipts or roll back any data because this profile performs no data or
lifecycle write.
