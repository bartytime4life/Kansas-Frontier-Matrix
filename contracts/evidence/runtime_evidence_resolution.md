<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/evidence/runtime-evidence-resolution/v1alpha1
title: RuntimeEvidenceResolution Candidate Contract
type: semantic-contract
version: v1alpha1
status: PROPOSED; internal-candidate-profile; non-authoritative; no-network; non-publisher
owners: OWNER_TBD — Evidence steward · Runtime steward · Contract steward · Schema steward · Validation steward
created: 2026-08-05
updated: 2026-08-05
policy_label: internal; evidence-resolution; cite-or-abstain; fail-closed; no-release-authority
related:
  - ./README.md
  - ./evidence_ref.md
  - ./evidence_bundle.md
  - ./verification_state_history.md
  - ../../schemas/contracts/v1/evidence/runtime_evidence_resolution.schema.json
  - ../../fixtures/contracts/v1/evidence/runtime_evidence_resolution/README.md
  - ../../packages/evidence-resolver/
  - ../../tools/validators/evidence_resolver/
  - ../../tests/packages/evidence_resolver/test_result_schema.py
[/KFM_META_BLOCK_V2] -->

# RuntimeEvidenceResolution candidate contract

> **One-line purpose.** Define the deterministic, machine-checkable result emitted by the internal `kfm/evidence-ref-bundle-candidate/v1alpha1` resolver profile without turning that result into evidence truth, a public runtime answer, policy clearance, review approval, release authority, or publication state.

## Status and boundary

This contract is **PROPOSED** and deliberately narrow. It describes the existing internal candidate evaluator under `packages/evidence-resolver/`. The evaluator performs bounded, no-network checks over caller-supplied data. It does not query a registry, verify a signature, execute policy, authenticate a reviewer, resolve release state, or authorize rendering.

The contract preserves the KFM rule:

```text
unresolved evidence cannot become renderable evidence
```

A `RESOLVED` result means only that the supplied candidate passed the checks named in `checks_performed`. Downstream code must still resolve evidence authority, rights, sensitivity, policy, review, release, correction, and public-surface obligations before producing an authoritative `ANSWER`.

## Object fields

| Field | Meaning | Required rule |
|---|---|---|
| `profile` | Pinned evaluator profile identifier. | Exactly `kfm/evidence-ref-bundle-candidate/v1alpha1`. |
| `status` | Finite candidate outcome. | One of `RESOLVED`, `UNRESOLVED`, `DENIED`, or `ERROR`. |
| `authoritative` | Explicit authority guard. | Always `false`. |
| `bundle_id` | Candidate bundle identity when closure succeeds. | Required string only for `RESOLVED`; `null` for every other status. |
| `checks_performed` | Stable names of checks actually executed. | Non-empty and unique. |
| `issues` | Safe reason-code records. | Empty for `RESOLVED`; non-empty for every other status. Raw input values are not carried. |
| `limitations` | Fixed profile limitations. | Exact ordered list defined by the paired schema. |

## Finite outcomes

| Status | Meaning | Downstream posture |
|---|---|---|
| `RESOLVED` | The explicit candidate passed the bounded profile. | Continue to governed policy, review, release, and citation checks; do not render solely from this result. |
| `UNRESOLVED` | Evidence closure or current-state support is incomplete, stale, corrected, superseded, withdrawn, or otherwise insufficient. | Abstain or hold; preserve the reason codes. |
| `DENIED` | Caller-supplied policy context explicitly blocks the candidate. | Deny; do not expose the bundle identity. |
| `ERROR` | Input or caller-supplied policy context could not be evaluated safely. | Fail closed; do not infer truth or fall back to allow. |

Precedence remains:

```text
ERROR > DENIED > UNRESOLVED > RESOLVED
```

## Negative-state preservation

Non-resolved outcomes must remain inspectable. The result must not erase why a candidate was blocked, corrected, superseded, revoked, withdrawn, stale, missing, or inconsistent. At the same time, non-resolved results must not carry `bundle_id`, which prevents downstream code from accidentally treating a blocked candidate as usable evidence.

## Authority separation

This object is not:

- an `EvidenceBundle` or proof pack;
- a `PolicyDecision` or policy evaluation;
- a `ReviewRecord`;
- a `PromotionDecision`, `PromotionReceipt`, or `ReleaseManifest`;
- an API `DecisionEnvelope` or public `RuntimeResponseEnvelope`;
- permission to render, cite, publish, release, deploy, or expose a claim.

## Validation

The paired schema is:

```text
schemas/contracts/v1/evidence/runtime_evidence_resolution.schema.json
```

Static positive and negative fixtures live under:

```text
fixtures/contracts/v1/evidence/runtime_evidence_resolution/
```

The evidence-resolver test suite validates both the static examples and every checked-in v1alpha1 resolver output:

```bash
make evidence-resolver
```

## Rollback

Revert this contract, schema, fixtures, conformance test, and generated receipt together. No lifecycle data, release record, public artifact, runtime route, or external source is changed by this slice.
