<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/pass-30-paleoenvironmental-proxy-provenance-source-map
title: Pass 30 paleoenvironmental proxy provenance — source adaptation map
type: exploratory-source-map
status: proposed; non-authoritative; non-release; non-publication
created: 2026-08-09
updated: 2026-08-09
source_card: KFM-P30-PROG-0029
source_spec_hash: sha256:cd77280751f0bc76d55a2ecddff911b0b9f022b79bcad4ad90500320fdffc295
[/KFM_META_BLOCK_V2] -->

# Pass 30 paleoenvironmental proxy provenance — source adaptation map

## Decision

**PROPOSED:** admit one dependency-closed, fixture-only `PaleoenvironmentalProxyProvenanceRecord` packet. It preserves proxy-source, reconstruction, temporal, and spatial-generalization provenance without admitting real records or asserting environmental truth.

## Source evidence

| Evidence | Status | Supports | Limit |
|---|---|---|---|
| `KFM-P30-PROG-0029` in the Pass 23–32 consolidated atlas | CONFIRMED | “Define proxy-source, reconstruction, temporal, and spatial-generalization provenance records for paleoenvironmental outputs.” | Idea card is not accepted architecture, scientific validation, or implementation proof. |
| Card spec hash `sha256:cd77280751f0bc76d55a2ecddff911b0b9f022b79bcad4ad90500320fdffc295` | CONFIRMED | Exact source-card identity. | Does not hash this implementation. |
| Consolidated atlas PDF SHA-256 `020a1207c2a6d193dc23defca40d24d429acd1273da17c2494582116ec8e9639` | CONFIRMED | Local attachment bytes inspected; card remains active and unchanged through Pass 32. | PDF is source material, not repository authority. |
| Repository base `76da0a048590710bd927891d43075d989568bf7d` | CONFIRMED | Exact-path and exact-card duplicate assay; accepted Directory Rules and evidence ownership README. | Bounded snapshot; later changes require rebase/recheck. |

Drive evidence reference: `google-drive:1w7Qrf5Na7PSvwdTuplZnFbyueToPtQaa#KFM-P30-PROG-0029`.

## Directory Rules placement

| Responsibility | Path | Basis |
|---|---|---|
| Semantic provenance meaning | `contracts/evidence/` | The object explains evidence roles and anti-collapse rules. |
| Machine shape | `schemas/contracts/v1/evidence/` | Schema is shape, not scientific or policy authority. |
| Synthetic cases | `fixtures/contracts/v1/evidence/` | Opaque references only; no coordinates, people, sites, or real samples. |
| Executable validation | `tools/validators/evidence/` | Offline bounded checks only. |
| Proof | `tests/validators/evidence/` and `.github/workflows/` | Fixture polarity, identity replay, evidence closure, precision monotonicity, and receipt integrity. |

## Admitted, deferred, rejected

- **Admitted:** explicit proxy and reconstruction roles, opaque source/sample/method/output references, parameter and output hashes, transform receipts, timescale and uncertainty, monotone spatial generalization, sensitivity posture, evidence closure, deterministic identity, and non-effects.
- **Deferred:** real proxy vocabularies, actual chronology and calibration models, scientific method review, geographic authorities, rights resolution, sensitivity policy, source ingestion, reconstruction execution, lifecycle integration, release gates, and activation.
- **Rejected:** coordinates, real sensitive locations or samples, present-condition equivalence, predictive authority, scientific validation claims, policy authority, source fetching, evidence mutation, release, and publication.

## Failure and rollback

Malformed, incomplete, role-collapsing, temporally reversed, spatially upcast, sensitivity-leaking, evidence-incomplete, non-canonical, authority-bearing, or identity-inconsistent records fail closed. Rollback is deletion of the eight files in this proposal; no evidence or source data is changed.
