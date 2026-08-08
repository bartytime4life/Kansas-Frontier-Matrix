<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass-32-source-availability-watchlist
title: Pass 32 Source Availability Watchlist Adaptation
type: exploratory-intake; source-map; implementation-record
version: v0.1.0
status: proposed adaptation; fixture-only
owners: OWNER_TBD — Source steward · Architecture steward · Validation steward
created: 2026-08-08
updated: 2026-08-08
policy_label: public; exploratory; pass-32; non-authoritative
related:
  - ../../../contracts/source/source_availability_watchlist.md
  - ../../../contracts/source/source_health_assessment.md
  - ../../../contracts/data/material_change_assessment.md
  - ../../../schemas/contracts/v1/source/source_availability_watchlist.schema.json
tags: [kfm, pass-32, source-watchlist, material-change, candidate-work]
[/KFM_META_BLOCK_V2] -->

# Pass 32 Source Availability Watchlist Adaptation

## Goal

Adapt candidate `KFM-P32-FEAT-0016` into the smallest inactive repository slice that distinguishes source availability from material schema/content change and requires a separately referenced proposed-work record only when the existing material-change family reports `PROMOTION_CANDIDATE`.

## Evidence basis

**CONFIRMED source statement:** Pass 32 proposes that a source availability watchlist distinguish stable source availability from material schema or content changes requiring a candidate work record.

**CONFIRMED repository dependencies at the delivery base:**

- `contracts/source/source_health_assessment.md` defines source health outcomes.
- `schemas/contracts/v1/source/source_health_assessment.schema.json` and its validator provide the existing bounded health family.
- `contracts/data/material_change_assessment.md` defines byte, semantic, and material change with `NON_EVENT`, `PROMOTION_CANDIDATE`, `HOLD`, and `ERROR`.
- `packages/hashing` owns RFC 8785 JCS plus SHA-256 identity.
- accepted ADR-0029 and Directory Governance Standard v2 govern responsibility-root placement.

## Adaptation decision

The watchlist is an **aggregate projection**, not a replacement contract:

```text
health assessment ref
  + material-change assessment ref
  + digest evidence and finite routing
  -> stable / review-required / hold / error watchlist
```

This avoids parallel health or materiality authority and keeps the proposed-work record outside the watchlist.

## Added packet

- semantic aggregate contract;
- strict Draft 2020-12 schema;
- fifteen deterministic fixture cases;
- no-network validator with repository hashing;
- eight focused tests;
- read-only path-scoped workflow; and
- generated authoring receipt.

## Non-effects

This packet does not:

- perform a network request or activate a source;
- create a `SourceHealthAssessment` or `MaterialChangeAssessment`;
- create or execute candidate work;
- admit or write RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED state;
- resolve evidence or evaluate policy;
- approve review, promotion, release, deployment, publication, or public use.

## Validation boundary

A green result proves strict machine shape, deterministic identity, source/assessment reference binding, canonical ordering, digest evidence for material schema/content change, candidate-reference polarity, recomputed summary counts, exact finite outcomes, no-network behavior, and fixed false authority flags.

## Rollback

The slice is additive. Before merge, close the draft and abandon the branch. After an authorized merge, revert the bounded commit. No external or public state is created.
