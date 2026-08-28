<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/release/api-contract-change-assessment
title: ApiContractChangeAssessmentCandidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; no-network; non-authoritative
owners: OWNER_TBD — API steward · Contracts steward · Release steward · Correction steward · Validation steward
created: 2026-08-10
updated: 2026-08-10
owning_root: contracts/
policy_label: internal; release; api-contract; compatibility; correction-aware
responsibility: Define a fixture-only assessment that binds one declared API contract change to version impact, compatibility evidence, client fixtures, notices, migration, review, release, correction, and rollback references without changing an API or authorizing release.
truth_posture: "CONFIRMED source-card traceability and repository gap; PROPOSED inactive contract; UNKNOWN actual compatibility and consumer adoption; NEEDS VERIFICATION API, release, and correction steward review plus hosted CI"
related:
  - ./release_manifest.md
  - ./rollback_card.md
  - ../correction/correction_notice.md
  - ../runtime/http_outcome_binding.md
  - ../../schemas/contracts/v1/release/api_contract_change_assessment.schema.json
  - ../../fixtures/contracts/v1/release/api_contract_change_assessment/cases.json
  - ../../tools/validators/release/validate_api_contract_change_assessment.py
  - ../../tests/validators/release/test_validate_api_contract_change_assessment.py
  - ../../docs/intake/exploratory/pass-18-api-contract-change-assessment-source-map.md
[/KFM_META_BLOCK_V2] -->

# ApiContractChangeAssessmentCandidate

`ApiContractChangeAssessmentCandidate` is an inactive declaration profile for
one proposed API contract transition. It implements the smallest
dependency-closed portion of Pass 18 card `KFM-P18-INV-413`.

## Boundary

A validator `PASS` proves only that declared before/after versions and digests,
impact labels, compatibility posture, test and client-fixture references,
change/migration/correction/deprecation notices, review, release, rollback,
limitations, deterministic identity, and fixed-false authority claims are
internally coherent under this synthetic profile.

It does not diff OpenAPI or runtime bytes, discover clients, run compatibility
tests, establish semantic-version policy, authenticate references, approve a
change, mutate a route or response, migrate a client, release, roll back, deploy,
publish, or authorize public use.

## Conservative declaration rules

- the before and candidate contract digests must differ;
- the candidate semantic version must advance and match the author's declared
  `PATCH`, `MINOR`, or `MAJOR` impact;
- an explicitly incompatible or breaking change requires a major-version
  declaration, a major-version advance, and a migration-guide reference;
- complete assessments require compatibility-test, client-fixture,
  compatibility-rationale, change-notice, release-manifest, rollback-card, and
  review references;
- correction or declared interpretation, client-behavior, or evidence-handling
  impact requires a correction-notice reference; and
- deprecation requires a deprecation-notice reference.

These are conservative fixture-profile checks, not an accepted exhaustive rule
for which individual response-field changes require a major version. Actual
compatibility remains a reviewer and runtime evidence question.

## Finite outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | The declared change-assessment packet is locally coherent and reviewable. |
| `ABSTAIN` | Compatibility or impact remains incomplete, unknown, or unresolved. |
| `DENY` | Version, digest, impact, compatibility, notice, migration, review, release, or rollback declarations are incoherent. |
| `ERROR` | Shape or input handling prevents safe evaluation, or the assessment records an error. |

These outcomes are not compatibility decisions, review approvals, release
decisions, or runtime status.

## Directory Rules basis

The card defines version/change notices as release duties. Accepted ADR-0029
therefore places semantic meaning under `contracts/release/`, machine shape
under `schemas/contracts/v1/release/`, synthetic replay under
`fixtures/contracts/v1/release/`, reusable validation under
`tools/validators/release/`, conformance proof under `tests/validators/release/`,
read-only orchestration under `.github/workflows/`, source reconciliation under
`docs/intake/exploratory/`, and authoring accountability under
`data/receipts/generated/`.

The profile references existing ReleaseManifest, CorrectionNotice, and
RollbackCard families without redefining them. It creates no API registry,
compatibility authority, client registry, release record, runtime route, or
publication path.

## Validation and rollback

```bash
python -m unittest tests.validators.release.test_validate_api_contract_change_assessment -v
python tools/validators/release/validate_api_contract_change_assessment.py --fixtures
```

Rollback is one additive commit revert. No API, client, release, correction,
rollback, deployment, cache, or public state requires operational restoration.
