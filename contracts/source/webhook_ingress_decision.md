<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-source-webhook-ingress-decision
title: Webhook Ingress Decision Contract
type: semantic-contract; source-intake; pre-raw; replay-protection; idempotency
version: v0.1.0
status: draft; PROPOSED; fixture-first; no-live-source-or-publication-authority
owners: OWNER_TBD — Source steward · Security steward · Contracts steward · Schema steward · Validation steward
created: 2026-08-05
updated: 2026-08-05
policy_label: public; contracts; source; webhook; pre-raw; security; non-authoritative
related:
  - ./README.md
  - ./source_activation_decision.md
  - ../../schemas/contracts/v1/source/webhook_ingress_decision.schema.json
  - ../../fixtures/contracts/v1/source/webhook_ingress_decision/
  - ../../tools/validators/validate_webhook_ingress_decision.py
  - ../../tests/validators/test_validate_webhook_ingress_decision.py
  - ../../docs/intake/exploratory/new-ideas-3-16-26-webhook-ingress-source-map.md
notes:
  - "Implements the bounded webhook verification, replay-safety, idempotency, and conditional-poll fallback pattern mined from New Ideas 3-16-26.pdf."
  - "The contract records decisions only; it does not host a webhook service, persist secrets, activate a source, admit bytes to RAW, or publish."
[/KFM_META_BLOCK_V2] -->

# Webhook Ingress Decision

`WebhookIngressDecision` is a fixture-first pre-RAW decision object for determining whether a signed source-update event may be admitted to the controlled ingest path, treated as an exact duplicate no-op, held in quarantine, rejected, or retried.

## Purpose

The object separates six concerns that must not be collapsed:

1. **Source posture** fixes the `SourceDescriptor` and source-activation decision used for the evaluation.
2. **Event identity** preserves the provider event ID, resource ID, event/receipt times, body digest, declared content hash, and sequence state.
3. **Verification** records signature, timestamp-skew, and nonce-replay results without storing raw secrets, raw signatures, or raw nonces.
4. **Idempotency** distinguishes a new request, an exact duplicate, a digest conflict, and an unverifiable state before any side effect.
5. **Fallback** allows conditional polling only for an explicit gap or provider/runtime failure and requires ETag or Last-Modified state.
6. **Decision** returns one finite outcome and one compatible next action while keeping promotion, release, publication, and public routes denied.

## Directory Rules basis

The accepted Directory Rules v2 decision in ADR-0029 makes path ownership a responsibility decision. This slice uses existing roots only:

| Responsibility | Home |
|---|---|
| Source-intake meaning | `contracts/source/` |
| Machine shape | `schemas/contracts/v1/source/` |
| Synthetic examples | `fixtures/contracts/v1/source/webhook_ingress_decision/` |
| Deterministic validation | `tools/validators/` |
| Enforceability | `tests/validators/` |
| Focused CI orchestration | `.github/workflows/` |
| Exploratory source mapping | `docs/intake/exploratory/` |
| AI authoring provenance | `data/receipts/generated/` |

No new root, connector, queue, secret store, dedupe database, DLQ service, source registry record, lifecycle record, policy authority, release object, or public route is introduced.

## Finite outcomes

| Outcome | Required meaning | Compatible next action |
|---|---|---|
| `ACCEPT` | Signature is valid, timestamp is fresh, nonce is unseen, idempotency state is new, and source activation is active. | `ADMIT_TO_RAW` |
| `DUPLICATE_NOOP` | The provider event was already accepted and the prior body digest exactly matches. | `NOOP` |
| `QUARANTINE` | Identity, activation, sequence, or verification is unresolved but may be reviewable. | `HOLD_IN_QUARANTINE` |
| `DENY` | Signature, timestamp, nonce, source posture, or digest consistency fails. | `REJECT` |
| `ERROR` | The verifier or intake runtime could not evaluate safely. | `RETRY` with a restricted steward DLQ |

## Required invariants

- A webhook is not accepted unless signature, timestamp, nonce, idempotency, and source-activation checks all pass.
- An exact duplicate is a no-op only when its digest matches the previously accepted digest.
- A duplicate with a different digest is never silently accepted or treated as a no-op.
- Raw signing secrets, raw signature values, and raw nonces are never persisted in this decision object.
- A conditional-poll fallback requires an explicit trigger, a deterministic request key, and at least one conditional validator (`ETag` or `Last-Modified`).
- Conditional polling cannot bypass the decision into RAW or PUBLISHED state.
- Side effects have not been applied when this decision object is emitted.
- A materialization attestation remains required before any later publish transition.
- Promotion, release, publication, and public-route authority remain false in every fixture.
- Findings contain stable codes and JSON pointers only; candidate values are not echoed.

## Deterministic fixture identity

The synthetic fixtures use `kfm-fixture-json-v1`: remove the top-level `spec_hash`, serialize UTF-8 JSON with sorted keys and no insignificant whitespace, preserve array order, compute SHA-256, and prefix `sha256:`.

This local test profile is not a repository-wide RFC 8785/JCS decision. Production canonicalization remains subject to the adopted hash policy, schema/version compatibility, and release controls.

## Trust boundary

A green result proves only the proposed JSON shape, fixture identity profile, finite routing rules, replay/idempotency polarity, and no-secret/no-public-authority guardrails. It does **not** verify a provider signature, inspect a secret, activate a source, persist an event, write RAW, enqueue materialization, operate a DLQ, evaluate OPA, sign an attestation, promote, release, deploy, publish, or authorize public use.

## Validation

```bash
python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_webhook_ingress_decision.py' \
  --verbose

python tools/validators/validate_webhook_ingress_decision.py --fixtures
```

## Rollback

Before merge, close the draft pull request and delete its feature branch. After an authorized merge, revert the dependency-closed contract, schema, fixtures, validator, tests, workflow, source map, and authoring receipt. No live source state or published artifact is created by this slice.
