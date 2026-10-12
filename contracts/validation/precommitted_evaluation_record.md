<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/validation/precommitted-evaluation-record
title: PrecommittedEvaluationRecord Candidate Contract
type: semantic-contract
version: v1.0.1
status: proposed-inactive; fixture-only; no-network; non-authoritative
owners: OWNER_TBD — Validation steward · Evidence steward · Review steward
created: 2026-08-25
updated: 2026-09-06
policy_label: internal; validation; preregistration; scoring; deterministic; fail-closed
owning_root: contracts/
responsibility: fixture-only verification of a sealed precommitment, evaluation timing, intervention disclosure, outcome coverage, and exact Brier scoring
truth_posture: "CONFIRMED synthetic fixture behavior, current repository bundle, and one successful historical exact-head workflow / PROPOSED semantic contract and evidence refresh / NEEDS VERIFICATION current-main hosted exact-head execution, independent steward review, and external evidence authentication"
related:
  - ../../schemas/contracts/v1/validation/precommitted_evaluation_record.schema.json
  - ../../fixtures/contracts/v1/validation/precommitted_evaluation_record/cases.json
  - ../../tools/generators/precommitted_evaluation_record/build_precommitted_evaluation_record.py
  - ../../tools/validators/validate_precommitted_evaluation_record.py
  - ../../tests/validators/test_validate_precommitted_evaluation_record.py
  - ../../docs/intake/exploratory/cairnwake-precommitted-evaluation-source-map.md
  - ../../.github/workflows/precommitted-evaluation-record.yml
  - ../../data/receipts/generated/genrec-cairnwake-precommitted-evaluation-20260825.json
  - ../../data/receipts/generated/genrec-contract-precommitted-evaluation-record-currentness-20260906.json
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 2b65cfdb6d4a8ce472a8c6a10cc0718c7d43ef3a
  prior_contract_blob: eecaa9b77c1d12af4f36747ad1a24f51d0b647be
  schema_blob: 2197c3a2adaa4c8a4364c236d233f63847c8e746
  fixture_blob: f952ac2cd63fcf1245455f1f0acaa70ce3c8b396
  builder_blob: a0427fd5ad934e800fa971f34df9ae82f45da1c4
  validator_blob: 5d134488ffb4b543d07257036632db5a5f9e237e
  focused_tests_blob: de388e7172ee881147cf9560925fac0993b14ddf
  workflow_blob: 16f8c8533853468c1944ee27f89d050051a160ab
  source_map_blob: 84e74b173c42855c6745a52740bc5f21ce9c8f48
  historical_receipt_blob: f3592629c832d277c080f8fc31c0e599231248a4
  bundle: "one schema, one eight-case fixture manifest, one deterministic builder, one validator, one focused test module, one no-network workflow, one source map, and one historical generated receipt"
  historical_workflow_run: "precommitted-evaluation-record run 32929740203 (workflow run number 3) on commit 6af91c7d4cc132b53a747736c2109e5561ff2c04 completed successfully; all seven job steps passed"
  current_main_workflow_readback: "No pull-request-triggered workflow run was returned for main@2b65cfdb6d4a8ce472a8c6a10cc0718c7d43ef3a at readback; current-main exact-head acceptance remains NEEDS VERIFICATION"
notes:
  - "v1.0.1 is a repository-evidence/currentness refresh only; no schema fields, canonicalization, exact Brier formula, denied authorities, execution mode, or activation posture changed."
  - "The 2026-08-25 receipt remains immutable historical provenance and is replayed against its exact originating commit; the currentness receipt binds this revision."
  - "A current-main hosted pass, independent steward review, and external observation authentication remain outside this evidence snapshot."
tags: [kfm, validation, preregistration, commitment, reveal, brier, fixture]
[/KFM_META_BLOCK_V2] -->

# PrecommittedEvaluationRecord Candidate Contract

PrecommittedEvaluationRecord verifies that a revealed synthetic evaluation payload matches a commitment published before its observation window, that interventions are disclosed, that every preregistered prediction has one observed outcome, and that exact Brier scoring is reproducible.

## Current repository evidence

PrecommittedEvaluationRecord remains a proposed, fixture-only, non-authoritative semantic contract. The repository bundle is bounded by a schema, an eight-case fixture manifest, a deterministic builder and validator, focused tests, a no-network workflow, a source map, and an immutable historical generated receipt. Those surfaces constrain validation; they do not authenticate external observations or authorize execution, review, release, or publication.

| Surface | Current bounded evidence |
|---|---|
| Machine shape | The JSON Schema fixes profile version `1.0.0`, `PROPOSED_INACTIVE`, `FIXTURE_ONLY_NO_EXTERNAL_EFFECT`, `authority: NONE`, exact permissions, non-effects, and the commit/reveal, intervention, outcome, score, and identity fields. |
| Fixture polarity | The manifest contains eight cases: one valid scored record plus seven deterministic `DENY` mutations covering seal, late registration, early reveal, outcome coverage, score, intervention ordering, and identity. |
| Deterministic implementation | The builder derives the RFC 8785 JCS + SHA-256 commitment, exact Brier fraction, specification hash, and evaluation ID; the validator checks schema, canonical inventories, timing, intervention bounds, score, and identity. |
| Focused proof surface | The focused test module covers schema validity, fixture polarity, fail-closed timing, exact Brier scoring, missing outcomes, no-network/no-write imports, symlink rejection, and deterministic CLI output. |
| Hosted historical result | Workflow run [32929740203](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/runs/32929740203) tested the unchanged bundle at exact commit `6af91c7d4cc132b53a747736c2109e5561ff2c04` and passed all seven job steps, including historical receipt integrity. |
| Current main | The current `main@2b65cfdb6d4a8ce472a8c6a10cc0718c7d43ef3a` contains the same pre-update bundle blobs listed in the evidence snapshot. No pull-request-triggered run was returned for this exact merge head at readback. |

The successful historical run is bounded evidence for the bundle at its exact head. It is not a current-main pass, external observation authentication, calibration result, review approval, release decision, or publication authorization.
## Commit and reveal

The commitment is SHA-256 over the repository RFC 8785 JCS encoding of sealed_payload. The declared publication time must precede the evaluation window. Reveal may not occur before the window closes. The candidate carries both the revealed payload and commitment so a validator can reproduce the check without network access.

## Predictions and scoring

Predictions are sorted and unique by prediction_id. Each declares an event definition, an explicit falsifier, and confidence_basis_points from 0 through 10000. Outcomes are sorted, unique, and cover the prediction set exactly.

For prediction confidence p in basis points and observed value y in {0, 10000}, squared_error_basis_points_2 is (p - y)^2. The mean Brier score is stored as an exact fraction with numerator equal to the sum of squared errors and denominator equal to prediction_count multiplied by 100000000. No floating-point rounding or curve adjustment is permitted.

## Interventions

Every disclosed intervention is ordered by timestamp and must fall between commitment publication and reveal. The record does not claim the list is complete; validator PASS means only that the declared list is canonical and internally bounded. A real evaluation would require independent evidence and review.

## Validator outcomes

PASS means schema, seal, temporal order, inventories, score, identity, and non-authority fields agree. DENY identifies an incoherent candidate. ERROR identifies unsafe JSON input. PASS does not make a prediction true, establish calibration, authenticate an observation, approve an intervention, or authorize publication.

## Validation and currentness

The repository-native workflow runs the focused unittest module, the deterministic builder, the fixture suite, and generated-receipt integrity checks under `KFM_NO_NETWORK=1`. The historical exact-head run above is the latest confirmed hosted result for this unchanged bundle.

The currentness packet preserves the historical receipt as immutable provenance by replaying its artifact bytes against `6af91c7d4cc132b53a747736c2109e5561ff2c04`; a separate currentness receipt binds this contract and the workflow revision. A future current-head run must be read back from GitHub before operational reliance. Absence of that run remains an explicit `NEEDS VERIFICATION` hold.
## Authority boundary and rollback

The profile is fixture-only, no-network, and non-mutating. It does not publish a commitment, collect observations, authenticate evidence, run an experiment, update a scoreboard, approve review, or create release, deployment, publication, or public-use authority. Before merge, close the draft pull request and delete its branch. After an authorized merge, revert the additive commit; no external state requires correction.

### Currentness refresh and rollback

The version `v1.0.1` records repository implementation evidence only. It preserves the v1.0 field meaning, canonicalization profile, exact Brier scoring rule, denied execution authorities, fixture-only posture, and repository-only rollback boundary. The prior contract blob is `eecaa9b77c1d12af4f36747ad1a24f51d0b647be`; restoring that blob is the documentation rollback target if this evidence refresh is rejected.

Rollback of the additive currentness packet is limited to reverting the contract, workflow, and currentness-receipt commits. It does not mutate external sources, observations, scoreboards, lifecycle stores, Drive, Notion, release records, or public surfaces.
