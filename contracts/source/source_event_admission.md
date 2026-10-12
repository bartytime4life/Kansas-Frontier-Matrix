<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/source/source-event-admission
title: Source Event Admission Contract Family
type: semantic-contract
version: v0.1.0
status: proposed; fixture-first; no-network; non-authoritative
owners:
  - OWNER_TBD - Source steward
  - OWNER_TBD - Contract steward
  - OWNER_TBD - Evidence steward
  - OWNER_TBD - Policy steward
  - OWNER_TBD - Validation steward
created: 2026-08-08
updated: 2026-08-08
policy_label: internal; source-edge; fixture-only; no-authority
owning_root: contracts/
responsibility: Define the semantic boundary for deterministic source-event prefilter output and fixture-only event run receipt candidates extending the existing SourceEventEnvelopeCandidate profile.
truth_posture: CONFIRMED existing SourceEventEnvelopeCandidate family and accepted placement authority; PROPOSED prefilter and run-receipt realization; NEEDS VERIFICATION production signing, policy execution, source activation, and operational admission
related:
  - ./README.md
  - ./source_event_envelope.md
  - ./source_descriptor.md
  - ../../schemas/contracts/v1/source/source_event_prefilter_output.schema.json
  - ../../schemas/contracts/v1/source/source_event_run_receipt.schema.json
  - ../../fixtures/contracts/v1/source/source_event_admission/
  - ../../tools/validators/validate_source_event_admission.py
  - ../../tests/validators/test_validate_source_event_admission.py
  - ../../.github/workflows/source-event-admission.yml
tags: [kfm, source-event, prefilter-output, event-run-receipt, deterministic-triage, pre-raw, fixture-first, no-authority]
notes:
  - "Realizes Pass 3 carry-forward candidate KFM-P1-PROG-0008 without creating a second event envelope or a new repository root."
  - "The existing SourceEventEnvelopeCandidate remains the canonical source-edge event wrapper for this bounded slice."
  - "The fixture signature profile is deterministic test evidence only; it is not DSSE, Cosign, key custody, or production cryptographic attestation."
  - "No live source, queue, watcher, model, policy engine, lifecycle write, release, deployment, or publication is activated."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Source Event Admission Contract Family

> This family extends the existing `SourceEventEnvelopeCandidate` with a deterministic prefilter output and a fixture-only signed-shape event run receipt. It owns the typed decision seam before any operational RAW admission; it does not execute that admission.

## Goal and status

| Field | Value |
|---|---|
| Source candidate | Pass 3 carry-forward `KFM-P1-PROG-0008` |
| Existing event contract | `contracts/source/source_event_envelope.md` |
| New machine shapes | `source_event_prefilter_output.schema.json` and `source_event_run_receipt.schema.json` |
| Execution mode | `FIXTURE_ONLY` |
| Network/model/policy/signing services | none |
| Operational authority | none |
| Public use | denied |

Pass 3 says watchers should produce pre-RAW or WORK-candidate events with receipts rather than direct published records. The candidate depends on an event envelope, bounded prefilter output, and event run receipt. This slice closes the two missing companion shapes around the existing envelope while preserving the repository's current `contracts/source/` and `schemas/contracts/v1/source/` responsibility lanes.

## Directory Rules basis

The accepted Directory Rules place:

- semantic object meaning under `contracts/`;
- machine shape under `schemas/contracts/v1/<family>/`;
- executable validation under `tools/validators/`;
- examples under `fixtures/`;
- enforceability under `tests/`;
- platform CI integration under `.github/workflows/`; and
- process memory under `data/receipts/`.

The repository already owns the source-edge envelope under the singular `source` family. Creating a second generic `events` authority would duplicate responsibility, so this slice extends the existing source family instead.

## Typed flow

```text
SourceEventEnvelopeCandidate
        |
        v
SourceEventPrefilterOutputCandidate
        |
        v
SourceEventRunReceiptCandidate
        |
        +--> ALLOW       -> target_lane RAW          (no write executed)
        +--> HOLD        -> target_lane WORK         (no write executed)
        +--> QUARANTINE  -> target_lane QUARANTINE   (no write executed)
        +--> REJECT      -> target_lane NONE
        +--> NO_ACTION   -> target_lane NONE
```

The receipt is a reviewable candidate record. Even `ALLOW` has `operational_effect: NONE_FIXTURE_ONLY`, `raw_write_allowed: false`, and `raw_write_performed: false`.

## `SourceEventPrefilterOutputCandidate`

The prefilter output binds one existing event and records only bounded triage data:

```text
SourceEventPrefilterOutputCandidate
├── prefilter_id
├── spec_hash
├── event_ref
├── event_payload_spec_hash
├── evaluated_at
├── evaluator
│   ├── evaluator_id
│   ├── kind = RULE_SET | MODEL
│   ├── version
│   ├── configuration_hash
│   ├── deterministic = true
│   ├── temperature
│   └── seed
├── classification
├── significance_score [0, 1]
├── uncertainty [0, 1]
├── explanation_digest
├── candidate_destination
├── reason_codes
└── all-false/no-authority claims
```

Allowed evaluator metadata is identity, version, configuration hash, finite scores, and an explanation digest. Long free-form reasoning and hidden chain-of-thought fields are excluded by the closed schema.

### Finite classifications

| Classification | Required destination |
|---|---|
| `MATERIAL_CHANGE` | `RAW_REVIEW` |
| `REVIEW_REQUIRED` | `WORK_REVIEW` |
| `RIGHTS_UNRESOLVED` | `QUARANTINE_REVIEW` |
| `SENSITIVITY_UNRESOLVED` | `QUARANTINE_REVIEW` |
| `NON_MATERIAL_CHANGE` | `NO_ACTION` |
| `DUPLICATE_REPLAY` | `NO_ACTION` |

A model evaluator is admissible only with `temperature: 0`, a finite integer seed, and `deterministic: true`. This proves a bounded fixture configuration, not model truth or reproducibility across unpinned external runtimes.

## `SourceEventRunReceiptCandidate`

The run receipt binds one event, one prefilter output, one finite disposition, one policy summary, and one fixture-only signature shape.

```text
SourceEventRunReceiptCandidate
├── receipt_id
├── spec_hash
├── event_ref + event_payload_spec_hash
├── prefilter_ref + prefilter_spec_hash
├── recorded_at
├── decision
├── target_lane
├── policy_summary
├── review_required
├── reason_codes
├── signature
└── no-authority claims
```

### Decision coherence

| Decision | Target lane | Policy summary | Review required |
|---|---|---|---:|
| `ALLOW` | `RAW` | `ALLOW`; rights and sensitivity both `KNOWN` | yes |
| `HOLD` | `WORK` | `HOLD` | yes |
| `QUARANTINE` | `QUARANTINE` | `HOLD`; rights or sensitivity unresolved/conflicted | yes |
| `REJECT` | `NONE` | `DENY` | yes |
| `NO_ACTION` | `NONE` | `NOT_EVALUATED` | no |

This mapping prevents the receipt from concealing destination or policy posture behind a generic pass/fail field.

## Identity and fixture attestation

`prefilter_id` and `receipt_id` are deterministic RFC 8785 JCS plus SHA-256 identifiers over declared identity projections. Each object also carries a full `spec_hash`.

The receipt signature profile is:

```text
kfm.fixture.sha256-attestation.v1
```

It deterministically binds a fixture signer reference to the receipt `spec_hash`, allowing negative tests for missing, drifted, or mismatched signatures. It is explicitly not:

- a production digital signature;
- DSSE;
- Cosign or Sigstore verification;
- key custody or identity proof;
- human approval;
- policy authority; or
- release authority.

Production signing remains `NEEDS VERIFICATION` and requires a separate reviewed implementation with key management, signature verification, retention, incident response, and rollback.

## Invariants

- The event reference and payload hash match the companion `SourceEventEnvelopeCandidate`.
- The prefilter reference and spec hash match the companion prefilter.
- Prefilter evaluation does not predate event receipt.
- Receipt recording does not predate the event or prefilter.
- Classification and candidate destination are coherent.
- Decision, target lane, policy outcome, and review flag are coherent.
- `ALLOW` requires known rights and sensitivity.
- `QUARANTINE` requires an unresolved or conflicted rights/sensitivity reason.
- Reason codes and policy references are canonical and duplicate-free.
- Deterministic IDs, spec hashes, and fixture signatures are recomputed.
- Every operational, evidence, proof, policy, review, promotion, release, publication, network, and lifecycle-write claim remains false.

## What validation proves

The validator proves only:

- closed Draft 2020-12 shape;
- bounded, duplicate-free UTF-8 JSON parsing;
- deterministic identity and spec hashes;
- bounded deterministic evaluator configuration;
- score ranges and finite classifications;
- event/prefilter/receipt reference binding;
- finite decision and target coherence;
- time ordering;
- fixture signature integrity; and
- exact fixture polarity.

It does not run a model, retrieve a source, resolve `EvidenceRef`, evaluate a policy bundle, authenticate a signer, perform a lifecycle write, or grant source admission.

## Fixture profile

The fixture suite reuses three existing valid envelope fixtures and adds:

- three valid prefilter outputs;
- three valid run receipts;
- three invalid prefilter cases; and
- four invalid receipt cases.

The valid receipt outcomes cover `ALLOW`, `QUARANTINE`, and `NO_ACTION`, while every fixture remains synthetic, no-network, nonpublic, and operationally inert.

## Rollback

Before merge, close the draft pull request and delete its feature branch.

After an authorized merge, revert the dependency-closed packet. No source, queue, model, policy service, signing service, lifecycle record, API route, cache, release, deployment, or public artifact requires migration or correction.

[Back to top](#top)
