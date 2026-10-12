<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/new-ideas-3-16-26-temporal-slice-source-map
title: New Ideas 3-16-26 — Temporal Slice Source Map
type: exploratory-source-map; implementation-assay
version: v0.1.0
status: draft; PROPOSED; current-session-repo-assay
owners: OWNER_TBD — Docs steward · Data steward · Temporal steward · Evidence steward
created: 2026-08-06
updated: 2026-08-06
policy_label: public; exploratory; source-map; temporal-slice; no-release-authority
related:
  - ../../../contracts/data/temporal_slice.md
  - ../../../schemas/contracts/v1/data/temporal_slice.schema.json
  - ../../../tools/validators/validate_temporal_slice.py
  - ./new-ideas-3-16-26-webhook-ingress-source-map.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
notes:
  - "Records the second bounded implementation selected from New Ideas 3-16-26.pdf."
  - "The attached PDF is design evidence, not repository or publication authority."
[/KFM_META_BLOCK_V2] -->

# New Ideas 3-16-26 — Temporal Slice Source Map

## Evidence checkpoint

| Field | Value |
|---|---|
| Repository | `bartytime4life/Kansas-Frontier-Matrix` |
| Assayed base | `main@9960a2e22fb78cd6d6cf9bedb2379c09c8d5239c` |
| Source | `New Ideas 3-16-26.pdf` |
| Directory authority | Accepted ADR-0029 and `docs/doctrine/directory-rules.md` |
| Prior packet slice | `WebhookIngressDecision`, landed through PR #2031 |
| Selected slice | Fixture-first `TemporalSlice` metadata profile |
| Network, database, release, or source activation | None |

## Candidate assay

| Packet candidate | Disposition | Reason |
|---|---|---|
| Webhook signature, replay, and idempotency decision | Implemented on current main | The full contract/schema/fixture/validator/test/workflow family is already present. |
| Reversible entity reconciliation | Already represented | Current main contains the shared reconciliation family. |
| PR-first spec promotion, signing, rollback, and OCI attestation | Already represented / higher authority | Release, promotion, rollback, proof, receipt, tile-artifact, and attestation surfaces already exist; operational signing or publication requires separate release/security authority. |
| Pulse suppression denylist | Deferred | Product ownership, input corpus, false-positive budget, appeal path, and policy home were not verified strongly enough for enforcement work. |
| Live SQL time/change indexes | Deferred | Database ownership, migration framework, retention, correction behavior, and runtime consumers remain unverified. |
| Persistent-observation Temporal Slice MetaBlock | **Selected** | The source defines a compact time-first, evidence- and receipt-bound object. Current main had adjacent temporal, dataset-version, materiality, evidence, receipt, and artifact families but no dedicated `TemporalSlice` profile. |

## Bounded implementation

The selected change adds a `TemporalSlice` semantic contract, Draft 2020-12 schema, two valid and eight exact-negative synthetic fixtures, a deterministic no-network validator, focused tests, CI, this source map, and a generated authoring receipt.

The source’s “deterministic ULID” is adapted to `kfm:temporal-slice:sha256:<digest>` over dataset version, exact temporal window, footprint hash, grid system/key, and `spec_hash`. This avoids timestamp-entropy ambiguity while preserving the source’s identity inputs.

The source’s time/change SQL indexes are documented as stable key projections only. No database or migration is created. The schema allows `PROCESSED` and `CATALOG` candidates only; it cannot authorize `PUBLISHED`, public rendering, or a public claim.

## Directory Rules result

The object has one data-semantic owner and is split across existing responsibility roots: meaning in `contracts/data/`, shape in `schemas/contracts/v1/data/`, examples in `fixtures/`, validation in `tools/validators/`, tests in `tests/validators/`, CI in `.github/workflows/`, source assay in `docs/intake/exploratory/`, and authoring provenance in `data/receipts/generated/`. `TemporalWindow` remains in `common`; release and artifact meanings remain in `contracts/release/`.

## Deferred governed increments

A storage adapter may be proposed only after database and migration conventions, reference integrity, retention, correction semantics, and rollback are verified. A release-facing adapter may be proposed only after real evidence resolution, policy evaluation, review, proof closure, release-manifest closure, and rollback targets exist.
