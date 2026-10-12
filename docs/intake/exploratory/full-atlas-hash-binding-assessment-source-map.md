<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://intake/exploratory/full-atlas-hash-binding-assessment-source-map
title: Full Atlas Hash Binding Assessment Source Map
type: source-map
version: v0.1.0
status: confirmed-source-map; proposed-implementation; NEEDS STEWARD REVIEW
owners: OWNER_TBD - Intake steward; Integrity steward; Contracts steward; Security reviewer
created: 2026-08-11
updated: 2026-08-11
policy_label: public-with-gates; provenance; hashing; no-policy-adoption
owning_root: docs/
responsibility: Record source identity, current-main overlap, placement, and non-effects for the bounded hash-binding assessment.
truth_posture: cite-or-abstain
[/KFM_META_BLOCK_V2] -->

# Full Atlas hash-binding assessment source map

## Selected idea and source identity

| Item | Evidence reference | Truth label |
|---|---|---|
| Connected Drive Full Atlas | `gdrive://1whGonKzHVBe5FOU5ovDBakNU4Nf-30tQr09R_UNeBho`; revision `3`; modified `2026-07-12T16:59:46.342Z` | `CONFIRMED` source carrier for KFM-TRIAD-042. |
| Repository mirror | `docs/kfm_full_atlas_seed_cards.md`; SHA-256 `07c7765576df1997e0be88141bd3cd213930e7281d490a8ae62afd78abe8f445`; section `KFM-TRIAD-042` | `CONFIRMED` wording and candidate keys KFM-CAND-0124 through KFM-CAND-0126. |
| Existing readiness matrix | `control_plane/hash_profile_readiness_matrix.json`; SHA-256 `a8963bfc7dcc4572827045e488c1137d0878708415f4198c9eed0c881aa24548` | `CONFIRMED` six current role/profile tuples and the sole executable `spec_hash` baseline. |
| Existing readiness semantics | `contracts/common/hash_profile_readiness_matrix.md`; SHA-256 `77fe801b1212736a8401bd4d078d151bf9550fdff7b66501bd14f8bc442b4deb` | `CONFIRMED` that field selection remains object-family-owned and the matrix cannot adopt policy. |
| Directory authority | `docs/doctrine/directory-rules.md`; SHA-256 `44f7e94344cb42b630008eb0bc03a13fcb97dbdfba6f3e56579693a272571e6e`; accepted by ADR-0029 | `CONFIRMED` responsibility-root placement. |

The Full Atlas is an exploratory carrier. It proposes distinct purpose-specific profiles and adversarial vectors; it does not itself adopt a profile, algorithm, equivalence rule, migration, signature, or release decision.

## Current-main overlap check

Reviewed base: `main@c4cb046829f72afd07e39d167c781fb7435a9ac4`. Connected GitHub inspection returned no open pull requests in the repository at review time.

Current main already provides the necessary readiness foundation:

- `packages/hashing/` implements only the current RFC 8785 JCS plus SHA-256 `spec_hash` baseline.
- `HashProfileReadinessMatrix` distinguishes `content_hash`, `descriptor_hash`, `range_hash`, `root_hash`, `signature_digest`, and `spec_hash`, but intentionally leaves object-family field selection unresolved.
- The readiness validator checks matrix tuple integrity and activation posture, not the safety of a declared digest subject.

The remaining bounded gap is an inspectable subject-binding declaration and deterministic vectors for the failure modes named by KFM-TRIAD-042.

## Gap decision

Status: `REPO_GAP`, accepted only as an inactive synthetic conformance slice.

The slice reuses all six existing readiness profiles without changing them. It adds checks for self-hashing, signature recursion, volatile fields, unordered collections, finite-number handling, same-profile comparison, and exact readiness-matrix closure. Normalized-geometry and receipt-payload identity are recorded as held gaps because current main has no dedicated readiness profiles for them.

It intentionally does not add a `CanonicalizationProfile` registry, implement a new algorithm, compute production digests, activate an inactive tuple, migrate stored hashes, alter signatures, admit evidence, decide policy, release, or publish.

## Placement and non-effects

Directory Rules place meaning in `contracts/common/`, shape in `schemas/contracts/v1/common/`, synthetic inputs in `fixtures/contracts/v1/common/`, deterministic checking in `tools/validators/`, proof in `tests/validators/`, CI under `.github/workflows/`, this source map under `docs/intake/exploratory/`, and authoring provenance under `data/receipts/generated/`.

No new root, parallel contract authority, control-plane instance, data lifecycle record, source, evidence, policy, review, release, or publication surface is created.

## Rollback

Revert the bounded feature commit. No digest store, signature, migration, source, evidence record, policy decision, release, or publication requires operational rollback.
