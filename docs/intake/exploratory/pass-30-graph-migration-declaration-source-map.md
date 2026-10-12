<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/pass-30-graph-migration-declaration-source-map
title: Pass 30 graph migration declaration — source adaptation map
type: exploratory-source-map
status: proposed; non-authoritative; non-release; non-publication
created: 2026-08-09
updated: 2026-08-09
source_card: KFM-P30-PROG-0008
source_spec_hash: sha256:517810192f27527381aca4b4ce448b2409f26e47932fddb1954d30ceab7d4b14
[/KFM_META_BLOCK_V2] -->

# Pass 30 graph migration declaration — source adaptation map

## Decision

**PROPOSED:** admit one dependency-closed, fixture-only `GraphMigrationDeclaration` contract packet. It defines a pre-execution declaration and does not implement graph migration mechanics.

## Source evidence

| Evidence | Status | Supports | Limit |
|---|---|---|---|
| `KFM-P30-PROG-0008` in the Pass 23–32 consolidated atlas | CONFIRMED | “Define a migration declaration contract with intent, invariants, scope, blast radius, telemetry, reversibility, and governance constraints.” | Idea card is not accepted architecture or implementation proof. |
| Card spec hash `sha256:517810192f27527381aca4b4ce448b2409f26e47932fddb1954d30ceab7d4b14` | CONFIRMED | Exact source-card identity. | Does not hash this implementation. |
| Consolidated atlas PDF SHA-256 `020a1207c2a6d193dc23defca40d24d429acd1273da17c2494582116ec8e9639` | CONFIRMED | Local attachment bytes inspected; card remains active and unchanged through Pass 32. | PDF is source material, not repository authority. |
| Repository base `76da0a048590710bd927891d43075d989568bf7d` | CONFIRMED | Exact-path and exact-card duplicate assay; accepted Directory Rules and current ownership READMEs. | Bounded snapshot; later changes require rebase/recheck. |

Drive evidence reference: `google-drive:1w7Qrf5Na7PSvwdTuplZnFbyueToPtQaa#KFM-P30-PROG-0008`.

## Directory Rules placement

| Responsibility | Path | Basis |
|---|---|---|
| Semantic pre-execution governance meaning | `contracts/governance/` | The object records intent, review burden, constraints, and hold posture. |
| Machine shape | `schemas/contracts/v1/governance/` | Schema is shape, not meaning or policy. |
| Synthetic cases | `fixtures/contracts/v1/governance/` | No real graph, environment, endpoint, or migration payload. |
| Executable validation | `tools/validators/governance/` | Offline bounded checks only. |
| Proof | `tests/validators/governance/` and `.github/workflows/` | Fixture polarity, identity replay, and receipt integrity. |
| Mechanics | `migrations/graph/` | Existing owner remains unchanged; no parallel runner or migration format is created. |

## Admitted, deferred, rejected

- **Admitted:** intent, non-destructive migration class, bounded scope, complete invariants, conservative blast radius, expected telemetry references, paired recovery design, pending governance posture, deterministic identity, and non-effects.
- **Deferred:** graph store, query language, runner, executable payloads, environment bindings, authenticated review, policy enforcement, dry-run evidence, post-run evidence, recovery rehearsal, release integration, and activation.
- **Rejected:** real graph data, credentials, endpoints, production claims, applied-state claims, destructive fixtures, authority inflation, automatic approval, release, and publication.

## Failure and rollback

Malformed, incomplete, non-canonical, authority-bearing, destructive, or identity-inconsistent records fail closed. Rollback is deletion of the eight files in this proposal; the profile cannot alter graph state.
