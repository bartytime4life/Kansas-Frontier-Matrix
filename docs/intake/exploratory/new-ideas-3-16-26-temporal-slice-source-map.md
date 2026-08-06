<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake-new-ideas-3-16-26-temporal-slice-source-map
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
  - "This source map records the second bounded implementation selected from New Ideas 3-16-26.pdf."
  - "The attached PDF is design evidence, not repository or publication authority."
[/KFM_META_BLOCK_V2] -->

# New Ideas 3-16-26 — Temporal Slice Source Map

## Evidence checkpoint

| Field | Value |
|---|---|
| Repository | `bartytime4life/Kansas-Frontier-Matrix` |
| Base branch | `main` |
| Assayed base commit | `9960a2e22fb78cd6d6cf9bedb2379c09c8d5239c` |
| Attached design source | `New Ideas 3-16-26.pdf` |
| Directory authority | Accepted `ADR-0029`; canonical rules at `docs/doctrine/directory-rules.md` |
| Prior packet-derived slice | `WebhookIngressDecision`, landed through PR #2031 |
| Selected implementation | Fixture-first `TemporalSlice` data metadata profile |
| Network, database, release, or source activation | None |

## Candidate assay

| Candidate mined from the packet | Current-session disposition | Evidence-based reason |
|---|---|---|
| Webhook signature/replay/idempotency decision | **IMPLEMENTED ON CURRENT MAIN** | Current main contains the contract, schema, fixtures, validator, tests, workflow, source map, and authoring receipt from PR #2031. |
| Reversible entity reconciliation | **ALREADY REPRESENTED** | Current main contains the shared reconciliation contract, schema, fixtures, validator, tests, and workflow. |
| PR-first spec promotion, signing, rollback, and OCI attestation | **ALREADY REPRESENTED / HIGHER RELEASE AUTHORITY** | ReleaseManifest, PromotionDecision, PromotionReceipt, RollbackCard, tile-artifact, proof, receipt, and attestation surfaces already exist. Operational signing or publication would require separate release/security authority. |
| Pulse suppression denylist | **DEFERRED — PRODUCT-SCOPE DECISION** | The packet names product-specific noise classes. Current Pulse ownership, input corpus, false-positive budget, appeal path, and policy home were not sufficiently verified for a safe enforcement PR. |
| Live SQL indices for temporal slices | **DEFERRED — STORAGE CONVENTIONS UNKNOWN** | The source proposes time/change indices, but current production database, migration framework, retention, and runtime consumers were not verified. Stable index keys are documented without creating a migration. |
| Persistent-observation `Temporal Slice MetaBlock` | **SELECTED** | The packet defines a compact time-first, evidence- and receipt-bound metadata object. Current main has TemporalWindow, TemporalAuthorityEnvelope, DatasetVersion, MaterialChangeAssessment, EvidenceBundle, RunReceipt, and artifact/release families, but no dedicated TemporalSlice contract/schema/validator was found. |

## Selected scope

The selected change converts the packet's persistent-observation idea into one bounded object family:

- one deterministic `slice_id` derived from dataset version, temporal window, footprint, grid key, and governing `spec_hash`;
- explicit `TemporalWindow` reuse rather than a second temporal vocabulary;
- one spatial support and footprint digest;
- mandatory EvidenceBundle and run-receipt references;
- declared checks, policy labels, obligations, and gate references;
- optional prior-slice, materiality-assessment, and delta-proof lineage;
- referenced map/story/Focus/API/export materializations;
- stable time-index and change-index key projections; and
- hard denial of evidence-closure, policy, promotion, release, publication, and public-use authority.

## Source-to-repository adaptations

| Source suggestion | Bounded implementation adaptation |
|---|---|
| Deterministic ULID over dataset, footprint, time, and spec | Content-derived `kfm:temporal-slice:sha256:<digest>` using the same identity inputs. This avoids timestamp-entropy ambiguity and matches existing deterministic hash practice. |
| One record per publishable view | First profile records `PROCESSED` or `CATALOG` candidates only. A release object must later authorize any public surface. |
| `source_bundle` and `run_receipt` | Mandatory EvidenceBundle-reference array and one run-receipt reference. References remain unresolved by this local validator. |
| Promotion Gate F | Generic `promotion_gate_ref` rather than hard-coding gate numbering that may change. CATALOG candidates require a gate reference. |
| SQL tables and indices | Stable index projections documented; no DB technology, migration, or runtime is created. |
| OPA policy | Policy labels, decision refs, and obligations are shape-checked, but policy is not evaluated or authored in this slice. |

## Non-goals

This slice does not:

- ingest an observation or remote-sensing source;
- create a live watcher, connector, scheduler, or API;
- select PostgreSQL, SQLite, DuckDB, Elasticsearch, or another index implementation;
- add a migration or production table;
- create or resolve EvidenceBundle, RunReceipt, PolicyDecision, or proof instances;
- build PMTiles, COGs, feature sets, or story artifacts;
- run OPA/Conftest;
- assign a universal processing-level vocabulary;
- authorize CATALOG-to-PUBLISHED promotion;
- expose a MapLibre layer, Focus Mode answer, story, API response, or expose a MapLibre layer, Focus Mode answer, story, API response, or public claim.

## Directory Rules result

The artifact has one data-semantic owner and is split across existing responsibility roots:

- semantic meaning → `contracts/data/`;
- machine shape → `schemas/contracts/v1/data/`;
- synthetic examples → `fixtures/contracts/v1/data/`;
- validator → `tools/validators/`;
- tests → `tests/validators/`;
- focused CI → `.github/workflows/`;
- source assay → `docs/intake/exploratory/`;
- authoring provenance → `data/receipts/generated/`.

`TemporalWindow` remains in `contracts/common/`; release and tile-artifact meanings remain in `contracts/release/`. No new root, parallel schema home, lifecycle stage, catalog authority, release object, proof home, or public route is introduced.

## Next governed increment

A later PR may add a storage adapter for the documented time/change index keys only after current migration conventions, database/runtime ownership, retention, correction semantics, and rollback are verified. A separate release-facing increment may bind TemporalSlice candidates to ReleaseManifest and public-safe artifact manifests after evidence resolution, policy evaluation, review, proof closure, and rollback targets exist.
