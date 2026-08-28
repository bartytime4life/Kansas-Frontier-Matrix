<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/worker-integrity-launch-readiness-source-map
title: Worker Integrity Launch Readiness Source Map
type: exploratory-source-map
version: v1.0.0
status: proposed; review-pending
owners: OWNER_TBD — Atlas steward · Runtime steward · Security steward · Evidence steward
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; exploratory; source-grounded; non-authoritative
owning_root: docs/
responsibility: Reconcile the Drive worker-integrity proposal to current runtime verification and verified-rendering contracts, retaining only a non-duplicative pre-launch readiness candidate.
truth_posture: CONFIRMED source transcription and repository comparison / PROPOSED bounded adaptation pending review / NEEDS VERIFICATION hosted exact-head execution
related:
  - ../../../contracts/runtime/worker_integrity_launch_readiness.md
  - ../../../contracts/runtime/runtime_verification.md
  - ../../../contracts/runtime/verified_rendering_resource_envelope.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, atlas, runtime, worker, integrity, isolation, source-map]
[/KFM_META_BLOCK_V2] -->

# Worker Integrity Launch Readiness Source Map

## Source lineage

| Source | Confirmed contribution | Boundary |
|---|---|---|
| Google Drive `New Ideas 4-12-26`, document `1iSqUHB-ktYXfc0HdKvQe7yJCzigS7YuZfZSOBdrALnc`, fetched 2026-08-10, sections “Runtime Proof — Worker Integrity,” “Runtime Verification Contract — Worker Integrity,” “Worker Integrity Schemas,” and “Runtime Verification Validator — Worker Integrity” | Proposes explicit worker identity, manifest-backed verification, isolation requirements, finite outcomes, deterministic fixtures, and a fail-closed validator. | Mutable research/working document; proposed paths and runtime behavior are not repository authority. |
| `contracts/runtime/runtime_verification.md` and its schema/fixture/validator family | Already owns streamed artifact digest declaration, observation, equality, receipts, and proof-ready finite outcomes. | Does not decide whether a worker may launch or whether runtime capabilities satisfy one launch proposal. |
| `contracts/runtime/verified_rendering_resource_envelope.md` | Already owns synthetic verify-before-decode trace ordering, chunk/resource budgets, cancellation, worker failure, and render-readiness composition. | Does not model worker asset identity or cross-origin-isolation launch prerequisites. |
| Directory Rules and ADR-0029 | Route semantic meaning, machine shape, fixtures, validators, tests, receipts, and execution to distinct responsibility roots. | Placement authority; no runtime or release authorization. |

## Repository and history reconciliation

Current `main@5f615a3b86332d55af7cb7e9c6c2e2427cf443d5` was inspected on
2026-08-10. No current contract, schema, validator, fixture, test, workflow, or
open pull request named for worker-integrity launch readiness was found.

Two adjacent historical implementations were explicitly separated:

- merged PR #2400 is present on current main as the fixture-only
  `VerifiedRenderingResourceEnvelopeCandidate`; it owns trace and resource
  composition and remains unchanged; and
- merged PR #484 once added an actual browser Sigstore worker under legacy
  `apps/web/` and `schemas/maps/` paths, but those named paths are absent on
  current main. This packet does not resurrect that worker, legacy path family,
  policy, or render gate.

The Drive source's proposed `contracts/runtime_verification/`,
`schemas/runtime_verification/`, `tests/e2e/`, and executable worker paths are
therefore not copied. The candidate composes existing proof vocabulary by
reference and declares all execution effects false.

## Bounded adaptation

| Source pressure | Retained behavior | Repository constraint |
|---|---|---|
| Worker identity must be explicit | Synthetic worker and asset URNs. | No URL, package coordinate, source, or executable byte. |
| Verification must precede launch | Nullable existing `RuntimeVerificationProof` ref plus declared finite outcome. | No digest comparison, proof resolution, or proof emission. |
| Isolation and capabilities matter | Explicit required and observed booleans for worker support, isolation, `SharedArrayBuffer`, and WASM. | No header inspection or capability probe. |
| Fail closed with finite outcomes | Deterministic `READY_CANDIDATE`, `ABSTAIN`, or `DENY` derivation. | Ready remains review-required and launch-authorized is fixed false. |
| Reviewer-visible follow-up | Canonical obligation for missing or unavailable prerequisites. | No retry, configuration change, or issue mutation. |

## Path decision

~~~yaml
path_decision:
  artifact: WorkerIntegrityLaunchReadinessCandidate
  proposed_path: contracts/runtime/worker_integrity_launch_readiness.md
  artifact_kind: semantic contract
  authority_owner: fixture-only worker pre-launch readiness composition
  lifecycle_stage: not_applicable
  execution_role: none
  scope_kind: runtime
  scope_id: worker-integrity-launch-readiness
  exposure: internal
  mutability: versioned
  evidence:
    - docs/doctrine/directory-rules.md
    - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
    - contracts/runtime/runtime_verification.md
    - contracts/runtime/verified_rendering_resource_envelope.md
  rules:
    - DIR-SIGNATURE-001
    - DIR-SIGNATURE-002
    - DIR-PLACE-001
    - DIR-DEP-001
  outcome: PLACE
~~~

Any proof resolver, browser capability probe, header configuration, worker
bootstrap, policy, release gate, renderer integration, deployment, or public
surface requires a separately reviewed change.

## Non-effects

This packet does not read or hash worker bytes, resolve a proof, authenticate a
manifest, inspect headers, start or stop a worker, enable isolation, execute a
render trace, evaluate policy, mutate configuration, approve review, release,
deploy, publish, or authorize public use.
