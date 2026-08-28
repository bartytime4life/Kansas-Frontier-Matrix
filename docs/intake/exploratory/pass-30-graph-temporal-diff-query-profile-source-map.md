<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/pass-30-graph-temporal-diff-query-profile-source-map
title: Pass 30 graph temporal-diff query profile - source adaptation map
type: exploratory-source-map
status: proposed; non-authoritative; non-release; non-publication
created: 2026-08-09
updated: 2026-08-09
source_card: KFM-P30-PROG-0010
source_spec_hash: sha256:b40876ab01dbd8f6262288674846060542ee79a7e75d0ac202cd04febb64f5ba
[/KFM_META_BLOCK_V2] -->

# Pass 30 graph temporal-diff query profile - source adaptation map

## Decision

**PROPOSED:** admit one dependency-closed, fixture-only `GraphTemporalDiffQueryProfileCandidate` packet. It declares three read-only parameterized query templates and does not implement graph migration mechanics or query execution.

## Source evidence

| Evidence | Status | Supports | Limit |
|---|---|---|---|
| `KFM-P30-PROG-0010` in the Pass 23-32 consolidated atlas | CONFIRMED | "Create standard Cypher queries for migration-window diffs, label-scoped diffs, and relationship-scoped diffs." | The idea card is not accepted architecture or runtime proof. |
| Card spec hash `sha256:b40876ab01dbd8f6262288674846060542ee79a7e75d0ac202cd04febb64f5ba` | CONFIRMED | Exact source-card identity. | Does not hash this implementation. |
| Consolidated atlas PDF SHA-256 `020a1207c2a6d193dc23defca40d24d429acd1273da17c2494582116ec8e9639` | CONFIRMED | Attachment bytes and rendered card page inspected; the card remains active and unchanged through Pass 32. | Source material, not repository authority. |
| Repository base `1ab34018d7fb13ad41cfe8a79aed5d4763e58bf8` | CONFIRMED | Exact-ID, semantic, branch, and PR duplicate assay; accepted ADR-0029 and adjacent graph authorities inspected. | Bounded snapshot; later changes require recheck. |

Drive evidence reference: `google-drive:1w7Qrf5Na7PSvwdTuplZnFbyueToPtQaa#KFM-P30-PROG-0010`.

## Directory Rules placement

| Responsibility | Path | Basis |
|---|---|---|
| Proposed declaration meaning | `contracts/governance/` | The packet defines reviewable pre-execution constraints and a mandatory hold posture. |
| Machine shape | `schemas/contracts/v1/governance/` | Schema owns shape, not query execution or policy. |
| Synthetic query cases | `fixtures/contracts/v1/governance/` | Templates, refs, windows, and expected outcomes are fictional and reusable. |
| Executable validation | `tools/validators/governance/` | Offline structural and conservative lexical checks only. |
| Proof | `tests/validators/governance/` and `.github/workflows/` | Exact polarity, parser hardening, identity replay, and receipt integrity. |
| Migration mechanics | `migrations/graph/` | Existing owner remains unchanged; no executable `.cypher`, runner, or rollback implementation is created. |

## Dependency and authority boundaries

The candidate is subordinate to `GraphMigrationDeclaration` and complementary to `GraphInvariantArtifactCandidate`. It does not become a migration declaration, invariant artifact, execution receipt, graph result, policy decision, review record, release record, or publication artifact.

## Admitted, deferred, rejected

- **Admitted:** exact three-query set, parameter closure, synthetic snapshot window, read-only and bounded declarations, deterministic result columns, fixed pending review, deterministic identity, and non-effects.
- **Deferred:** graph platform/version compatibility, complete Cypher parsing, query planning, authenticated parameter binding, graph fixtures, execution, observed results, performance evidence, migration/rollback mechanics, policy integration, and activation.
- **Rejected:** endpoints, credentials, real graph data, procedure calls, external loads, write clauses, chained statements, runtime claims, automatic approval, release, and publication.

## Failure and rollback

Malformed, incomplete, write-capable, unbounded, parameter-inconsistent, temporally invalid, authority-bearing, or identity-inconsistent records fail closed. Rollback is deletion of the eight additive files; the profile cannot alter graph state.
