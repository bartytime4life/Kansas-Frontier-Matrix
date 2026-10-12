# `tests/evidence/` — Evidence-assessment test lane

> Executable, fixture-backed checks for selected evidence assessment contracts
> and validators. This lane tests bounded behavior; it does not establish that
> evidence is adequate, a claim is true, policy permits use, or publication is
> authorized.

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-evidence-readme
title: tests/evidence/README.md — Evidence-assessment test lane
type: README; directory-readme; test-lane-index
version: v0.1
status: draft; repository-grounded; executable-partial; workflow-binding-partial; non-authoritative
owner: "@bartytime4life — CONFIRMED CODEOWNERS review route; evidence, test, policy, privacy, security, and release stewardship remain NEEDS VERIFICATION"
created: 2026-08-30
updated: 2026-08-30
policy_label: repository-facing; tests; evidence-assessment; deterministic; no-network; fail-closed; non-publisher
owning_root: tests/
responsibility: executable conformance checks for selected evidence assessment schemas, fixtures, validators, compatibility behavior, and safety boundaries
truth_posture: source and fixture evidence support only the named assertions at the checked revision; test success is not evidence closure, policy approval, review completion, release, deployment, or publication authority
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 1ea6593ede80d5ce10f561c7eec72135d6ccf806
  direct_modules: 9
  source_defined_tests: 66
  directly_workflow_bound_modules: 2
notes:
  - "This file is an authored lane README. It is not generated or mirrored."
  - "The module and test counts describe source at the pinned commit, not a durable coverage promise or a recorded test run."
  - "Only the EvidenceTemporalPostureAssessment and legacy evidence TemporalAuthorityEnvelope modules have a confirmed direct workflow command."
  - "No Make target or canonical root-wide full-suite command for tests/evidence was established."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

## Purpose and audience

This directory helps maintainers and reviewers locate the direct tests for nine
evidence-assessment families. The tests exercise declared schema shape,
positive and negative fixture polarity, deterministic identity, finite
outcomes, compatibility, correction posture, unsafe-input rejection, and
selected no-network boundaries.

The lane is subordinate to the responsibility roots that own meaning and
behavior:

| Concern | Authority home | Role of this lane |
|---|---|---|
| Evidence semantics | [`contracts/evidence/`](../../contracts/evidence/README.md) | Exercise named rules; do not redefine them. |
| Machine shape | [`schemas/contracts/v1/evidence/`](../../schemas/contracts/v1/evidence/README.md) | Check selected schemas and fixture polarity. |
| Reusable fixtures | [`fixtures/contracts/v1/evidence/`](../../fixtures/contracts/v1/evidence/README.md) | Consume deterministic examples; do not become fixture authority. |
| Validator implementation | [`tools/validators/evidence/`](../../tools/validators/evidence/README.md) | Exercise entrypoints, results, diagnostics, and side-effect boundaries. |
| Policy, proof, and release | `policy/`, `data/proofs/`, `data/receipts/`, and `release/` | Remain outside test authority. |

Placement under `tests/` follows the accepted
[Directory Rules decision](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md)
and the [test-root contract](../README.md). Adding this README creates no new
authority home or executable behavior.

## Confirmed inventory

At the pinned revision, the directory contains nine Python modules and 66
source-defined `test_*` functions or methods.

| Module | Tests | Direct subject and bounded assertion |
|---|---:|---|
| [`test_distribution_coverage_assessment.py`](test_distribution_coverage_assessment.py) | 8 | [Distribution-coverage validator](../../tools/validators/evidence/validate_distribution_coverage_assessment.py): 20-case finite-state matrix, no inferred absence, deterministic identity, no-network execution, deterministic CLI replay, and unsafe JSON denial. |
| [`test_evidence_temporal_posture_assessment.py`](test_evidence_temporal_posture_assessment.py) | 10 | [Canonical temporal-posture validator](../../tools/validators/evidence/validate_evidence_temporal_posture_assessment.py): schema separation, fixture polarity, legacy byte/diagnostic compatibility, chronology, source-role distinction, and reference-family checks. |
| [`test_geometry_quality_scope_assessment.py`](test_geometry_quality_scope_assessment.py) | 17 | [Geometry-quality validator](../../tools/validators/evidence/validate_geometry_quality_scope_assessment.py): four-way result polarity, identity binding, precision/accuracy separation, attachment modes, abstention, derived-quality limits, no-coordinate and no-network boundaries, safe input handling, CLI behavior, and diagnostic non-disclosure. |
| [`test_non_detection_support_assessment.py`](test_non_detection_support_assessment.py) | 8 | [Non-detection validator](../../tools/validators/evidence/validate_non_detection_support_assessment.py): 12-case polarity, scoped non-detection, abstention, privacy-transform hold, identity integrity, safe input handling, and absence of network-client imports. |
| [`test_observation_fitness_assessment.py`](test_observation_fitness_assessment.py) | 9 | [Observation-fitness validator](../../tools/validators/evidence/validate_observation_fitness_assessment.py): 14-case polarity, retain-and-exclude behavior, qualified single-observation handling, contradiction denial, append-only correction lineage, identity integrity, safe input handling, and absence of network-client imports. |
| [`test_reality_boundary_note.py`](test_reality_boundary_note.py) | 2 | [Reality-boundary validator](../../tools/validators/evidence/validate_reality_boundary_note.py): synthetic material remains illustrative and cannot claim direct-evidence status. |
| [`test_representation_fitness_assessment.py`](test_representation_fitness_assessment.py) | 4 | [Representation-fitness validator](../../tools/validators/evidence/validate_representation_fitness_assessment.py): schema validity, fixture polarity, false-precision denial, and obligation requirements for conditional results. |
| [`test_temporal_authority_envelope.py`](test_temporal_authority_envelope.py) | 4 | [Legacy evidence temporal wrapper](../../tools/validators/evidence/validate_temporal_authority_envelope.py): valid/invalid temporal behavior and explicit compatibility with the canonical EvidenceTemporalPostureAssessment family. |
| [`test_temporal_support_assessment.py`](test_temporal_support_assessment.py) | 4 | [Temporal-support validator](../../tools/validators/evidence/validate_temporal_support_assessment.py): schema validity, fixture polarity, stale/support mismatch denial, and correction-reference requirements. |

The matching schema and fixture families live under
[`schemas/contracts/v1/evidence/`](../../schemas/contracts/v1/evidence/README.md)
and [`fixtures/contracts/v1/evidence/`](../../fixtures/contracts/v1/evidence/README.md).
The table is a direct-lane inventory, not a claim of complete evidence-contract
coverage.

## Running the lane

From the repository root, the focused collection command is:

```bash
KFM_NO_NETWORK=1 \
PYTHONDONTWRITEBYTECODE=1 \
PYTHONHASHSEED=0 \
PYTHONUNBUFFERED=1 \
TZ=UTC \
python -m pytest -q tests/evidence
```

This is a focused maintainer command derived from the current Python test
layout. It is not exposed as a dedicated Make target, is not identified as a
required check, and does not establish a canonical repository-wide test
command.

For the two directly workflow-bound temporal modules, the current hosted
workflow uses `unittest`:

```bash
KFM_NO_NETWORK=1 \
KFM_VALIDATION_NOW=2026-08-17T00:00:00Z \
PYTHONDONTWRITEBYTECODE=1 \
PYTHONHASHSEED=0 \
TZ=UTC \
python -m unittest \
  tests.evidence.test_evidence_temporal_posture_assessment \
  tests.evidence.test_temporal_authority_envelope \
  --verbose
```

Do not substitute that 14-test temporal command for the full 66-test source
inventory.

## Workflow boundary

[`evidence-temporal-posture-assessment.yml`](../../.github/workflows/evidence-temporal-posture-assessment.yml)
directly names the canonical and legacy temporal modules. It also watches their
tests, validators, schemas, fixtures, contracts, and related compatibility
surfaces.

Current repository evidence does **not** establish:

- a workflow command that directly names the other seven modules;
- indirect wildcard collection of all nine modules;
- a Make target for this directory;
- required-check or branch-protection status for this lane; or
- a path filter that causes the temporal workflow to run when only this README
  changes.

Treat those items as `UNKNOWN` until the relevant workflow or repository
settings provide direct evidence. Documentation checks may validate this file
without exercising the underlying evidence-assessment tests.

## Interpreting failures

| Failure area | Investigate first | Do not infer |
|---|---|---|
| Schema or fixture polarity | Matching schema, contract, fixture family, validator, and expected finding codes | That the schema or contract should be weakened to make a fixture pass |
| Identity or tamper checks | Canonical serialization, `spec_hash`, `assessment_id`, and correction lineage | That a changed identity is harmless |
| Finite outcome mismatch | Validator derivation, fixture expectation, and obligation/reason codes | That `PASS`, `HOLD`, `ABSTAIN`, `DENY`, and `ERROR` are interchangeable |
| Network, symlink, duplicate-key, or non-finite input checks | Input loader, import boundary, diagnostics, and fail-closed handling | That a harness error is an expected denial |
| Temporal compatibility | Canonical and legacy validator bytes, fixture parity, schema identity, and downstream references | That the legacy surface may be removed or renamed |
| Reality or representation boundary | Synthetic/direct-evidence role, precision claims, qualifications, and obligations | That plausible output is direct evidence or sovereign truth |

A test failure is a review signal for the checked revision. A test success does
not admit a source, resolve an EvidenceRef, create an EvidenceBundle, approve
rights or sensitivity handling, authorize policy, complete review, move data
through the lifecycle, or authorize release, deployment, promotion, or
publication.

## Fixture and safety requirements

- Keep fixtures synthetic or otherwise explicitly approved for public
  repository use.
- Do not add personal, restricted, culturally sensitive, precise protected
  location, credential, secret, or externally retrieved payload data.
- Preserve deterministic time, hashing, ordering, locale, and network
  assumptions where the subject depends on them.
- Keep positive, negative, abstention, hold, denial, error, correction, stale,
  and compatibility outcomes explicit.
- Diagnostics must identify a safe path and finding code without echoing
  protected values.
- A map, dashboard, generated answer, model output, or test result never
  becomes evidence authority.

## Maintenance checklist

When this directory changes:

1. Update the module and source-defined test counts in this README.
2. Link each new module to its actual validator, schema, fixture, contract, or
   compatibility dependency; label missing bindings `UNKNOWN`.
3. Add negative and failure-path cases for consequential behavior, not only
   happy-path shape checks.
4. Keep reusable fixture data under the accepted fixture root.
5. Verify network, unsafe-input, sensitivity, deterministic-identity, and
   diagnostic boundaries where relevant.
6. Update workflow commands and path filters in the same reviewed change when
   hosted collection is intentionally expanded.
7. Reconcile canonical and compatibility consumers before changing a legacy
   temporal identifier or entrypoint.
8. Record what was actually run; do not convert command presence or a green
   workflow into broader maturity.

## Open verification

| Question | Status |
|---|---|
| Who provides accountable evidence, QA, policy, privacy, security, and release review beyond the confirmed CODEOWNERS route? | `NEEDS VERIFICATION` |
| Are the seven modules outside the temporal workflow collected by another hosted command? | `UNKNOWN` |
| Should this README be added to a focused workflow path filter? | `OPEN` |
| Is this lane a required check under current repository rules? | `UNKNOWN` |
| What complete evidence-contract and validator coverage remains outside this directory? | `UNKNOWN` |
| What operational correction, rollback, and public-surface tests are required before release use? | `NEEDS VERIFICATION` |

## Rollback

This README changes documentation only. Before merge, close the draft pull
request to abandon it. After merge, revert the documentation commit. Neither
action changes validators, fixtures, evidence, policy, lifecycle state,
runtime behavior, release state, deployment, or publication.

[Back to top](#top)
