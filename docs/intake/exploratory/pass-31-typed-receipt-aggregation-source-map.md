<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://intake/exploratory/pass-31-typed-receipt-aggregation-source-map
title: Pass 31 typed receipt aggregation source map
type: source-adaptation-map
version: v1.0.0
status: proposed; implementation-support; non-authoritative
owners: OWNER_TBD — Intake steward · Data steward · Receipt steward · Directory Rules reviewer
created: 2026-08-09
updated: 2026-08-09
policy_label: internal; intake; data; receipt; provenance
source_card: KFM-P31-PROG-0013
source_spec_hash: sha256:fa365992bb1c2f8569fd070249dea29aa05442be2a032b33922aed4318317a4a
[/KFM_META_BLOCK_V2] -->

# Pass 31 typed receipt aggregation source map

## Evidence basis

| Evidence | Confirmed use |
|---|---|
| Drive `KFM_Pass23_Pass32_Consolidated_Deduplicated_Atlas.pdf` (`1w7Qrf5Na7PSvwdTuplZnFbyueToPtQaa`) | Card `KFM-P31-PROG-0013`; specification hash `sha256:fa365992bb1c2f8569fd070249dea29aa05442be2a032b33922aed4318317a4a`. |
| Supplied `KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas.pdf` | Byte digest `sha256:020a1207c2a6d193dc23defca40d24d429acd1273da17c2494582116ec8e9639`; extracted card text checked locally. |
| Drive `Directory Rules` (`1uTqdIEFZE2cq3gyISetoRYM6LIlnKqTc3FobtEx7Cbs`) | Responsibility-root placement and receipt-instance separation. |
| Repository `main@7335ed9ea0f81342ae0b1c7828a21ac74711c78b` | Gap and collision assay across existing RunReceipt, PromotionReceipt, generated-receipt, artifact-delta, and receipt documentation surfaces. |

## Adaptation decision

The source asks for dataset, run, specification, input digest, Rekor identifier, produced artifacts, materiality delta, and publish-candidate fields in a typed receipt aggregation shape. The packet models only a candidate aggregation over typed receipt references. It deliberately does not create a new canonical receipt family or receipt instance and does not resolve referenced bytes.

`publish_candidate` is treated as a declaration that is coherent only with `PROMOTION_CANDIDATE`; it never implies policy approval, promotion eligibility, release, or publication. The aggregation posture remains `HOLD_FOR_SEPARATE_REVIEW`.

## Collision check

Exact card-ID, exact-title, repository-field, and PR searches found no implementation of `KFM-P31-PROG-0013`. Existing receipt families remain distinct authorities and are referenced, not merged or superseded.

## Truth and authority boundary

`CONFIRMED`: source card, specification hash, Directory Rules authority, repository base, and existing receipt-family boundaries were inspected. `PROPOSED`: this profile and every authored path. `UNKNOWN`: referenced receipt validity, artifact validity, Rekor inclusion, signature state, policy, human review, promotion, release, and publication.

## Rollback

Delete the eight additive packet files. Existing receipt schemas, instances, verification state, lifecycle state, release state, and public state are unchanged.
