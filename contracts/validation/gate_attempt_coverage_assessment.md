<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/validation/gate-attempt-coverage-assessment
title: GateAttemptCoverageAssessment Candidate Contract
type: semantic-contract
version: v1.1.0
status: proposed-inactive; fixture-only; no-network; non-authoritative
owners: OWNER_TBD — Validation steward · Runtime steward · Audit steward
created: 2026-08-28
updated: 2026-09-06
maturity: repository-grounded; fixture-packet-backed; hosted-currentness-unverified; non-authoritative
policy_label: internal; validation; gate-accounting; deterministic; fail-closed
owning_root: contracts/
responsibility: fixture-only verification that every guarded-action attempt is classified, terminal classes remain distinct, and reported metric denominators declare their complete class population
truth_posture: "CONFIRMED current repository packet, source-map provenance, and historical bounded receipt; PROPOSED inactive assessment contract and fixture matrix; UNKNOWN live receipt carrier, production adoption, gate consumer adoption, and current hosted acceptance; NEEDS VERIFICATION human review and exact-head CI"
related:
  - ../../schemas/contracts/v1/validation/gate_attempt_coverage_assessment.schema.json
  - ../../fixtures/contracts/v1/validation/gate_attempt_coverage_assessment/cases.json
  - ../../tools/generators/gate_attempt_coverage_assessment/build_gate_attempt_coverage_assessment.py
  - ../../tools/validators/validate_gate_attempt_coverage_assessment.py
  - ../../tests/validators/test_validate_gate_attempt_coverage_assessment.py
  - ../../.github/workflows/gate-attempt-coverage-assessment.yml
  - ../../docs/intake/exploratory/cairnwake-gate-attempt-coverage-source-map.md
  - ../../data/receipts/generated/genrec-cairnwake-gate-attempt-coverage-20260828.json
  - ../../control_plane/object_family_register.yaml
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 5efb430268fb59fccc0b1332d187615f5c063b10
  prior_contract_blob: 958ac4549042faff6b4e282990c21eb0826473db
  schema_blob: fe202c4fbcd2dfdca053cc06a28f68b3dd867382
  fixture_blob: 40310030aacc0222171edd1b493201c6fe6ae53a
  builder_blob: c5897bb1bc336fcf9efccd1bc5c5beeab6817949
  validator_blob: be914a29f6ba82f8ac14a9a3d371091485657a90
  focused_tests_blob: b7ca31a4d05438f5f87d73e5a5278141a678a081
  workflow_blob: 61a37cbe06150e4197b9a833b18a90779fbd7f04
  source_map_blob: 340a870076794b1f3967ea005a4b229f6720b529
  historical_receipt_blob: ebac8087209c93e89274310a01d07d9a40501afc
  validator_registry_blob: 72c8c53617aecebfa50cb89d7f8b40b0eeeb8992
  fixture_cases: 13
  focused_tests: 9
  attempt_classes: 4
  validator_registry_entry: "No matching gate-attempt-coverage entry observed; the dedicated workflow invokes the validator directly."
  current_main_workflow_readback: "No workflow runs or combined status results returned for main@5efb430268fb59fccc0b1332d187615f5c063b10 at readback"
tags: [kfm, validation, gate, attempts, refusals, coverage, denominator, fixture]
notes:
  - "Version v1.1.0 is a repository-evidence/currentness refresh; it does not select a live receipt carrier, register a validator, configure a gate, or authorize runtime feedback."
[/KFM_META_BLOCK_V2] -->

# GateAttemptCoverageAssessment Candidate Contract

GateAttemptCoverageAssessment is a fixture-only validation object for detecting survivorship bias in guarded-operation reporting. The repository now carries a closed schema, a 13-case fixture manifest, a deterministic builder and validator, a nine-test focused suite, a dedicated no-network workflow, and a historical authoring receipt; none is a live gate, receipt carrier, or release authority. It accounts for one bounded synthetic attempt population without retaining submitted payloads or sensitive values.

### Current implementation evidence

| Surface | Bounded readback |
|---|---|
| Fixture manifest | 13 cases: one valid accounted population and twelve invalid mutations with exact expected outcomes and finding codes. |
| Focused suite | Nine deterministic unittest methods cover schema validity, fixture polarity, population reconciliation, refusal semantics, signature domains, denominator partitions, no-network/no-write inspection, symlink rejection, and deterministic CLIs. |
| Builder and validator | The builder renders a selected synthetic case; the validator checks schema, counts, reference identity, signature domains, denominator completeness, refusal semantics, terminal coverage, window order, and spec identity. |
| Dedicated workflow | `KFM_NO_NETWORK=1` is set; the focused suite, representative builder case, fixture replay, and generated-receipt integrity check run with read-only contents permission. |
| Historical receipt | The receipt records PASS for the bounded shape, deterministic fixture suite, and focused tests; hosted exact-head CI was SKIPPED and human review remains pending. |
| Carrier and registry | The `run_receipt` family remains `CONFLICTED`; no matching validator-registry entry was observed, and the workflow invokes the validator directly. |
| Current main | `main@5efb430268fb59fccc0b1332d187615f5c063b10`; no workflow runs or combined status results were returned for that commit at readback. |

These are repository and historical-receipt facts, not live gate evidence. They do not establish that a real guarded action occurred, that refusals or errors were captured in production, that a live carrier is selected, that a gate consumes the assessment, or that any review, lifecycle, release, deployment, publication, or public-use transition is authorized.

## Attempt population

Every attempted guarded action is assigned to exactly one class:

- `ADMITTED` — the gate admitted the guarded action and the action occurred within the declared synthetic record;
- `REFUSED` — the gate refused the action; the refusal does not prove the guarded action occurred;
- `ERROR` — processing failed without confirming the guarded action occurred;
- `UNOBSERVED` — an attempt reference exists but no terminal record was observed.

The declared invariant is:

`attempted_count = admitted_count + refused_count + error_count + unobserved_count`

Each class count must equal its reference-row count. Attempt references are unique across the population. Terminal record references are unique across admitted, refused, and error classes. The four classes use distinct signature domains so a refusal or error cannot be reinterpreted as an admission record.

## Denominators and feedback

Every reported metric denominator declares both included and excluded attempt classes. Those sets must be disjoint, canonical, and together cover all four classes. The declared denominator count is reproduced from the included class counts.

A refusal record has `guarded_action_occurrence = DID_NOT_OCCUR` and `same_gate_feedback_allowed = false`. A refusal may be counted as a refusal, but it must not serve as evidence that the guarded action occurred or feed the same gate in a way that manufactures later refusals. Error and unobserved classes likewise cannot confirm the guarded action.

The current packet tests this rule only over synthetic references and declared counts. It does not infer an attempt from a missing row, convert an `ERROR` or `UNOBSERVED` state into a refusal, or establish that any external gate emitted a complete class population.

## References and carrier boundary

Rows carry opaque KFM references and signature-domain labels only. Rejected payloads, addresses, messages, credentials, personal data, and sensitive values are prohibited from this candidate surface.

The repository currently records the `run_receipt` family as `CONFLICTED` across runtime, source, source-event, and release-bound variants. This candidate therefore selects no live receipt carrier and creates no parallel receipt authority. Its references are synthetic fixtures. The generated authoring receipt is historical provenance for this packet, not a runtime carrier. Any live integration requires a separately reviewed carrier decision, producer and consumer mapping, retention policy, rights and sensitivity review, and migration or compatibility plan.

## Validator outcomes

`PASS` means the candidate is schema-valid, its attempt population reconciles, reference roles and signature domains remain distinct, denominator declarations are complete, refusal semantics are fail-closed, terminal coverage state is truthful, and deterministic identity reproduces. `DENY` identifies an incoherent candidate. `ERROR` identifies unsafe JSON input.

`PASS` does not prove delivery, authenticate a real attempt or terminal record, configure a gate, permit feedback, admit a source, approve review, or authorize merge, lifecycle mutation, release, deployment, publication, or public use.

### Reproduction command set

The dedicated workflow runs:

    python -m unittest tests.validators.test_validate_gate_attempt_coverage_assessment --verbose
    python tools/generators/gate_attempt_coverage_assessment/build_gate_attempt_coverage_assessment.py --case valid-accounted-with-refusal-and-unobserved
    python tools/validators/validate_gate_attempt_coverage_assessment.py --fixtures
    python tools/validators/validate_generated_receipt.py data/receipts/generated/genrec-cairnwake-gate-attempt-coverage-20260828.json --repo-root .

The historical receipt records PASS for JSON shape and Python compilation, all 13 fixture polarities, and the nine focused tests. It records hosted exact-head CI as SKIPPED and human review as pending. Because that historical receipt binds the pre-update contract bytes, a currentness-only edit to this document is expected to make the receipt-integrity step report `ARTIFACT_DIGEST_MISMATCH` until a separately reviewed receipt rebinding is produced; this document-only update does not rewrite the historical receipt. No current hosted pass or production-readiness claim is made.

## Authority boundary and rollback

The profile is `PROPOSED_INACTIVE`, fixture-only, no-network, and non-mutating. The dedicated workflow is read-only packet enforcement, not validator-registry admission, live-gate configuration, runtime feedback, or receipt-carrier selection. Before merge, close the draft pull request and delete its branch. After an authorized merge, revert this contract currentness update to prior blob `958ac4549042faff6b4e282990c21eb0826473db`; preserve the historical receipt and its original artifact hashes. No source, gate, lifecycle, data, release, deployment, or public state requires correction.
