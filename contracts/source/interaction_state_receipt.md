<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/source/interaction-state-receipt
title: InteractionStateReceiptCandidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; no-network; non-authoritative
owners: OWNER_TBD — Source steward · Connector steward · Security steward · Validation steward
created: 2026-08-10
updated: 2026-08-10
owning_root: contracts/
policy_label: internal; source; connector; dynamic-interaction; redacted-receipt
responsibility: Define a fixture-only, redacted interaction-state receipt for dynamic source acquisition without retaining sensitive values or creating source admission, evidence, lifecycle, release, or publication authority.
truth_posture: "CONFIRMED supplied-card traceability and repository placement; PROPOSED inactive contract; UNKNOWN connector adoption; NEEDS VERIFICATION human review and hosted CI"
related:
  - ./source_artifact.md
  - ./retrieval_artifact_handoff.md
  - ./ingest_receipt.md
  - ../../schemas/contracts/v1/source/interaction_state_receipt.schema.json
  - ../../fixtures/contracts/v1/source/interaction_state_receipt/cases.json
  - ../../tools/validators/source/validate_interaction_state_receipt.py
  - ../../tests/validators/test_validate_interaction_state_receipt.py
  - ../../docs/intake/exploratory/pass-18-interaction-state-receipt-source-map.md
[/KFM_META_BLOCK_V2] -->

# InteractionStateReceiptCandidate

`InteractionStateReceiptCandidate` records a synthetic, digest-only trace of a dynamic source interaction involving form submission, browser-like script execution, redirects, or a composite flow. It implements the smallest reviewable portion of supplied Pass 18 card `KFM-P18-INV-373`.

## Boundary

A validator `PASS` proves only closed shape, deterministic identity, contiguous step order, declared state-digest continuity, result coherence, redaction coverage, obligations, and fixed-false authority effects.

It does not open a browser, execute JavaScript, submit a form, follow a redirect, read a source, authenticate an endpoint, admit a source, create a canonical `SourceArtifact`, resolve evidence, write RAW or QUARANTINE data, evaluate policy or review, release, deploy, or publish.

## Safe receipt shape

The receipt carries opaque references, counts, finite actions, and SHA-256 digests. It intentionally has no field for URLs, query strings, headers, cookies, tokens, session identifiers, hidden-field values, form values, response bodies, coordinates, or captured source payloads.

Sensitive state is represented only by a finite class label and must be covered by an explicit redaction declaration. `retained_sensitive_values` is fixed to `false`. A captured result remains `SOURCE_CAPTURE_CANDIDATE` or `QUARANTINE_CANDIDATE` and requires a separate source-artifact handoff obligation.

## Result semantics

| Result | Required local posture |
|---|---|
| `CAPTURED` | Final successful `CAPTURE` step, digest-bound candidate reference, no failure reasons, and source-artifact handoff obligation. |
| `FAILED` | Final failed step, no capture reference, and one or more finite failure reason codes. |
| `BLOCKED` | Final blocked step, no capture reference, and one or more finite failure reason codes. |

A coherent failure receipt may pass validation because the receipt preserves process memory; it does not make the failed acquisition successful or evidentiary.

## Finite validator outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | The declared interaction trace, redaction posture, and result are locally coherent. |
| `ABSTAIN` | Assessment or non-sensitive redaction-profile declaration remains incomplete or unresolved. |
| `DENY` | Step, state, result, redaction, obligation, or identity semantics are contradictory. |
| `ERROR` | The candidate cannot be evaluated under the closed schema. |

These outcomes are not source, evidence, policy, review, lifecycle, release, or publication decisions.

## Directory Rules basis

The object belongs to the source acquisition responsibility lane: meaning under `contracts/source/`; shape under `schemas/contracts/v1/source/`; synthetic cases under `fixtures/contracts/v1/source/`; validation under `tools/validators/source/`; executable evidence under `tests/validators/`; orchestration under `.github/workflows/`; reconciliation under `docs/intake/exploratory/`; and authoring accountability under `data/receipts/generated/`.

The profile composes existing source-artifact and retrieval-handoff boundaries without replacing or extending their authority.

## Validation

```bash
python -m unittest tests.validators.test_validate_interaction_state_receipt -v
python tools/validators/source/validate_interaction_state_receipt.py --fixtures
```

## Rollback

Revert the additive packet. It has no connector or runtime consumer and creates no live interaction, retained secret, source capture, lifecycle write, release, deployment, or publication side effect.
