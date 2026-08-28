<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass-18-api-contract-change-assessment-source-map
title: Pass 18 API Contract Change Assessment Source Map
type: source-map
version: v1.0.0
status: exploratory; implementation-mapped; non-authoritative
owners: OWNER_TBD — Intake steward · API steward · Contracts steward · Release steward · Correction steward
created: 2026-08-10
updated: 2026-08-10
owning_root: docs/
policy_label: internal; exploratory; source-reconciliation; api-contract; compatibility; release
responsibility: Reconcile the supplied API contract-change idea with current release, correction, and rollback seams without promoting source prose or fixture declarations into compatibility, review, release, or publication authority.
truth_posture: "CONFIRMED source card and repository gap; PROPOSED inactive implementation profile; UNKNOWN actual compatibility and consumer adoption; NEEDS VERIFICATION API, release, correction, and rollback steward review plus hosted CI"
related:
  - ../../../contracts/release/api_contract_change_assessment.md
  - ../../../contracts/release/release_manifest.md
  - ../../../contracts/release/rollback_card.md
  - ../../../contracts/correction/correction_notice.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
[/KFM_META_BLOCK_V2] -->

# Pass 18 API Contract Change Assessment Source Map

## Source and gap

| Evidence | Observation | Status |
|---|---|---|
| Supplied Pass 18 card `KFM-P18-INV-413` | API contract changes should be versioned, documented, compatibility-tested with client fixtures, and linked to release/correction notices and rollback when interpretation or client behavior changes. | `CONFIRMED` source statement |
| `contracts/release/release_manifest.md` | Existing release semantics identify versioning and compatibility policy as a remaining maturity need while keeping release authority separate. | `CONFIRMED` adjacent contract and gap |
| `contracts/release/rollback_card.md` | Existing rollback semantics provide the referenced rollback family without assessing API compatibility. | `CONFIRMED` adjacent contract |
| `contracts/correction/correction_notice.md` | Existing correction semantics provide the notice family without binding one API contract transition to tests, client fixtures, and version impact. | `CONFIRMED` adjacent contract |
| Current `main@97b9cb77bf57b1d1cf75c2768f8e550e399a1345` plus branch/PR search | No exact `KFM-P18-INV-413` contract, schema, fixture family, validator, workflow, branch, or pull request was found before implementation. | `CONFIRMED` bounded gap |

## Adaptation

The implementation adds one closed synthetic assessment. It verifies that the
candidate version advances and agrees with the author's declared version impact;
requires conservative major-version and migration declarations for explicitly
breaking or incompatible changes; and requires compatibility tests, client
fixtures, rationale, change notice, review, ReleaseManifest, RollbackCard, and
conditional correction or deprecation notice references.

The validator does not decide whether a real field change is compatible or which
specific field changes universally require a major version. It does not inspect
OpenAPI, runtime, client, release, correction, or rollback bytes.

## Directory Rules basis

Because the source card defines the change notice as a release duty, semantic
meaning belongs in `contracts/release/`. Shape, fixtures, validation, tests,
orchestration, source reconciliation, and authoring accountability remain in
their established schema, fixture, tool, test, workflow, documentation, and
generated-receipt roots. Existing ReleaseManifest, CorrectionNotice, and
RollbackCard authorities remain separate and unchanged.

No API registry, compatibility authority, client registry, policy rule, review
approval, release record, runtime route, or publication surface is created.

## Non-effects and rollback

A local `PASS` authenticates no contract, version, client, compatibility result,
notice, review, release, correction, rollback, deployment, or public state.
Rollback is a single additive commit revert with no external cleanup.
