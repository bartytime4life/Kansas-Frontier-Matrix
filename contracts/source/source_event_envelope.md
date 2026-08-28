<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/source/source-event-envelope
title: SourceEventEnvelopeCandidate Contract
type: semantic-contract; source-edge-candidate
version: v0.1.0
status: proposed; fixture-first; no-network; non-authoritative
owners: OWNER_TBD — Source steward · Contract steward · Evidence steward · Policy steward · Validation steward
created: 2026-08-06
updated: 2026-08-06
policy_label: internal; source-edge; fixture-only; no-authority
related:
  - ./README.md
  - ./source_descriptor.md
  - ./source_activation_decision.md
  - ./ingest_receipt.md
  - ../../schemas/contracts/v1/source/source_event_envelope.schema.json
  - ../../fixtures/contracts/v1/source/source_event_envelope/
  - ../../tools/validators/validate_source_event_envelope.py
  - ../../tests/validators/test_validate_source_event_envelope.py
  - ../../docs/intake/exploratory/new-ideas-3-11-26-source-event-envelope-source-map.md
tags: [kfm, source-event, cloudevents-shaped, deterministic-identity, idempotency, source-admission, quarantine, fixture-first]
notes:
  - "This is a bounded candidate profile inspired by the event-driven pattern in New Ideas 3-11-26.pdf."
  - "The profile carries CloudEvents-shaped core attributes but explicitly does not claim CloudEvents conformance."
  - "The current implementation admits only FIXTURE_ONLY records and creates no source, lifecycle, policy, review, release, or publication authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# SourceEventEnvelopeCandidate

> A `SourceEventEnvelopeCandidate` is a deterministic, fixture-only notification that describes a possible source-edge change and routes it toward source-admission review, quarantine review, or no action. It is not an admitted source event, source activation, RAW write, policy decision, proof, release record, or public fact.

## Status and boundary

| Field | Value |
|---|---|
| Status | `PROPOSED` / fixture-first / no-network |
| Contract home | `contracts/source/source_event_envelope.md` |
| Machine shape | `schemas/contracts/v1/source/source_event_envelope.schema.json` |
| Runtime authority | None |
| Execution mode | `FIXTURE_ONLY` |
| Public use | Denied |
| Network, queue, or orchestrator access | None |
| Source activation or RAW write | None |

The source packet recommends normalizing object-store notifications, webhooks, and feed changes into one event shape, computing a deterministic hash for idempotency, and handing the result to governed orchestration and attestation. This first repository slice implements only the bounded event shape, deterministic identity, finite routing, fixtures, and validation boundary.

It deliberately does **not** implement NATS, Pub/Sub, S3 or GCS notifications, webhooks, Temporal, Dagster, OCI, Sigstore, Cosign, in-toto, live connectors, source activation, or lifecycle mutation.

## Why this belongs to the source contract family

The envelope exists at the source edge and binds one `SourceDescriptor` reference and its declared source-role field. It does not define a new source registry, event bus, runtime service, or lifecycle root. Source meaning therefore remains under `contracts/source/`; machine shape remains under `schemas/contracts/v1/source/`; examples and enforcement remain under their existing fixture, validator, test, and workflow roots.

## CloudEvents-shaped adaptation

The profile carries the recognizable core concepts `specversion`, event identity, source, type, subject, and time. KFM-specific source, governance, and finite-routing fields are explicit.

The field `claims.cloudevents_conformance_claimed` is fixed to `false`. A passing KFM validator result must not be represented as full CloudEvents conformance. A later operational profile would require a separate standards review, compatibility contract, transport rules, and runtime evidence.

## Object shape

```text
SourceEventEnvelopeCandidate
├── schema_version = 1.0.0
├── profile = kfm.source_event_envelope_candidate.v1
├── execution_mode = FIXTURE_ONLY
├── specversion = 1.0
├── event_id
├── source_descriptor_ref
├── source_role_ref
├── event_type
├── subject
│   ├── subject_ref
│   ├── native_id
│   ├── media_type
│   ├── content_digest
│   ├── byte_count
│   ├── etag
│   └── last_modified
├── occurred_at
├── received_at
├── producer
│   ├── producer_id
│   ├── kind
│   └── version
├── payload
│   ├── payload_spec_hash
│   └── attributes
├── routing
│   ├── disposition
│   ├── reason_codes
│   ├── review_required
│   ├── source_activation_allowed = false
│   ├── raw_write_allowed = false
│   └── publication_allowed = false
├── governance
│   ├── rights_state
│   ├── sensitivity_state
│   ├── evidence_refs
│   └── policy_refs
└── claims
    ├── deterministic_identity = true
    ├── idempotent_replay = true
    ├── cloudevents_core_attributes_present = true
    ├── cloudevents_conformance_claimed = false
    ├── network_access_performed = false
    ├── authority_created = false
    ├── source_activated = false
    ├── lifecycle_write_performed = false
    ├── released = false
    └── published = false
```

## Identity and hashing

`payload.payload_spec_hash` is:

```text
SHA-256(RFC 8785 JCS(payload.attributes))
```

`event_id` is:

```text
"kfm:source-event:" + SHA-256(RFC 8785 JCS(identity_projection))
```

The identity projection contains:

- schema version and profile;
- source descriptor reference;
- event type;
- bounded subject identity and source-head fields;
- occurrence time;
- producer identity, kind, and version; and
- the declared payload specification hash.

Routing, evidence references, policy references, receipt time, and no-authority flags do not change event identity. This permits the same source notification to be re-evaluated without multiplying the underlying event identity. A payload-hash mismatch remains a separate validation failure.

## Finite routing

| Disposition | Meaning | Required posture |
|---|---|---|
| `PROPOSE_SOURCE_ADMISSION` | The event may be reviewed by the existing source-admission process. | Rights and sensitivity are `KNOWN`; evidence and policy references are present; review remains required. |
| `PROPOSE_QUARANTINE` | The event requires review because rights, sensitivity, deletion, identity, or another material condition is unresolved. | Review required; unresolved rights or sensitivity has an explicit reason code. |
| `NO_ACTION` | The event is an idempotent redelivery or non-material change. | No review required; reason identifies duplicate redelivery or no material change. |

No routing result authorizes source activation, RAW admission, promotion, release, or publication.

## Invariants

- `source_role_ref` equals `source_descriptor_ref + "#/source_role"`.
- `received_at` does not precede `occurred_at`.
- A represented source `last_modified` time does not occur after `received_at`.
- Non-deletion events carry a content digest and positive byte count.
- Deletion events carry no content digest and a zero byte count.
- Payload hash and event identity are recomputed deterministically.
- Evidence references, policy references, and reason codes use deterministic ordering.
- Unknown or conflicted rights or sensitivity cannot route to source-admission review.
- Manual replay routes only to `NO_ACTION`.
- All authority, lifecycle-write, release, publication, and network claims remain false.

## What validation proves

The validator proves only:

- closed Draft 2020-12 shape;
- bounded, duplicate-free UTF-8 JSON parsing;
- deterministic payload and event identity;
- source-role reference binding;
- time ordering;
- source-content state coherence;
- deterministic reference and reason-code ordering;
- finite routing coherence; and
- exact fixture polarity.

It does not authenticate the producer, resolve the referenced source or evidence, evaluate the referenced policy, verify a queue message, prove full CloudEvents conformance, or authorize any operational transition.

## Compatibility and future profiles

This is the initial fixture-only profile. A future operational profile must be introduced as a separately reviewed compatibility change. It must define transport binding, replay storage, source activation integration, retention, sensitivity handling, policy execution, receipts, signing, observability, and rollback without weakening the candidate profile's no-authority guarantees.

## Rollback

Before merge, close the draft pull request and delete its branch. After an authorized merge, revert the dependency-closed source-event-envelope commit or merge commit. The slice creates no live event, queue, source activation, lifecycle state, release, deployment, cache, or public route, so rollback requires no migration or public correction.

[Back to top](#top)
