<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake-new-ideas-3-16-26-webhook-ingress-source-map
title: New Ideas 3-16-26 — Webhook Ingress Source Map
type: exploratory-source-map; implementation-assay
version: v0.1.0
status: draft; PROPOSED; current-session-repo-assay
owners: OWNER_TBD — Docs steward · Source steward · Security steward
created: 2026-08-05
updated: 2026-08-05
policy_label: public; exploratory; source-map; webhook; no-live-source-authority
related:
  - ../../../contracts/source/webhook_ingress_decision.md
  - ../../../schemas/contracts/v1/source/webhook_ingress_decision.schema.json
  - ../../../tools/validators/validate_webhook_ingress_decision.py
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
notes:
  - "This source map records why one bounded idea was selected from New Ideas 3-16-26.pdf."
  - "The attached PDF is design evidence, not implementation authority."
[/KFM_META_BLOCK_V2] -->

# New Ideas 3-16-26 — Webhook Ingress Source Map

## Evidence checkpoint

| Field | Value |
|---|---|
| Repository | `bartytime4life/Kansas-Frontier-Matrix` |
| Base branch | `main` |
| Base commit | `2eb0291da99af02c0ea6eba60f5091319d0a7f7c` |
| Attached design source | `New Ideas 3-16-26.pdf` |
| Directory authority | Accepted `ADR-0029`; canonical rules at `docs/doctrine/directory-rules.md` |
| Selected implementation | Fixture-first `WebhookIngressDecision` profile |
| Network/source activation | None |

## Candidate assay

| Candidate mined from the packet | Current-session disposition | Reason |
|---|---|---|
| Privacy-safe reversible entity reconciliation | **ALREADY REPRESENTED** | Current `main` contains the shared reversible entity reconciliation contract, schema, validator, tests, workflow, and generated receipt. |
| PR-first promotion, PromotionReceipt, signed release/rollback concepts | **ALREADY REPRESENTED / BROADER AUTHORITY** | Current `main` already contains promotion, proof, catalog-closure, release, and rollback families. Extending signing or release authority would require a separate release/security review. |
| DNA/genealogy consent, re-identification, and overlays | **HOLD — SENSITIVE** | Living-person/genomic handling requires consent, privacy, stewardship, and public-safety decisions beyond this packet. |
| Biodiversity STAC/PMTiles publication | **HOLD — SOURCE/RIGHTS/GEOPRIVACY** | Source activation, terms, sensitive-taxa rules, release artifacts, and map delivery require their own governed slice. |
| Live webhook receiver, queue, dedupe store, DLQ, and conditional poller | **DEFERRED IMPLEMENTATION** | No live source or infrastructure is activated in a document-derived PR. The contract and deterministic negative tests must exist first. |
| Webhook signature/timestamp/nonce verification, replay-safe idempotency, and conditional-poll fallback decision | **SELECTED** | High-value shared pre-RAW trust boundary; no dedicated contract/schema/validator was found at the pinned base; implementable with synthetic no-network fixtures. |

## Selected scope

The selected change converts the packet's ingress rules into one reviewable object family:

- signature status and non-secret key reference;
- timestamp freshness and bounded skew;
- nonce digest and replay status;
- idempotency new/exact-duplicate/conflict states;
- deterministic event/body/spec references;
- explicit source activation posture;
- conditional polling only for declared fallback triggers;
- restricted DLQ semantics for verifier errors;
- finite `ACCEPT | DUPLICATE_NOOP | QUARANTINE | DENY | ERROR` outcomes; and
- hard denial of promotion, release, publication, and public-route authority.

## Non-goals

This slice does not:

- receive HTTP requests;
- verify a real provider key or secret;
- store raw headers, payloads, signatures, or nonces;
- create a connector, queue, database, cache, dedupe ledger, DLQ, Airflow DAG, or polling worker;
- activate a source or write any lifecycle state;
- create or evaluate OPA/Rego policy;
- generate or verify cosign/in-toto attestations;
- create a release, public API, MapLibre layer, or public claim.

## Directory Rules result

`PLACE` under existing responsibility roots:

- semantic meaning → `contracts/source/`;
- machine shape → `schemas/contracts/v1/source/`;
- synthetic examples → `fixtures/contracts/v1/source/`;
- validator → `tools/validators/`;
- tests → `tests/validators/`;
- workflow → `.github/workflows/`;
- source-map documentation → `docs/intake/exploratory/`;
- authoring provenance → `data/receipts/generated/`.

No new root or parallel authority is created.

## Next governed increment

After review of this profile, a separate PR may implement an adapter-specific receiver that consumes an admitted `SourceDescriptor`, keeps secrets outside event records, persists idempotency state transactionally, emits an ingest/run receipt, and routes failures to a restricted DLQ. That later change must name the provider, source terms, deployment boundary, secret management, retention, and operational rollback.
