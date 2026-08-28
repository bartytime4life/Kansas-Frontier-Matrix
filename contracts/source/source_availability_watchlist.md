<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/source/source-availability-watchlist
title: SourceAvailabilityWatchlist Contract
type: semantic-contract; aggregate-projection; review-routing
version: v0.1.0
status: proposed; fixture-first; no-network; non-authoritative
owners: OWNER_TBD — Source steward · Data steward · Contract steward · Validation steward
created: 2026-08-08
updated: 2026-08-08
policy_label: public; source; watchlist; review-candidate; non-publisher
related:
  - ./source_health_assessment.md
  - ../data/material_change_assessment.md
  - ../../schemas/contracts/v1/source/source_availability_watchlist.schema.json
  - ../../fixtures/contracts/v1/source/source_availability_watchlist/
  - ../../tools/validators/source/validate_source_availability_watchlist.py
  - ../../tests/validators/test_validate_source_availability_watchlist.py
  - ../../docs/intake/exploratory/pass-32-source-availability-watchlist-source-map.md
tags: [kfm, source-health, material-change, watchlist, candidate-work, deterministic, fixture-first]
notes:
  - "This aggregate references existing SourceHealthAssessment and MaterialChangeAssessment records; it does not replace either family."
  - "A REVIEW_CANDIDATE route is review metadata only and cannot execute work or authorize promotion."
[/KFM_META_BLOCK_V2] -->

# SourceAvailabilityWatchlist

> `SourceAvailabilityWatchlist` is a deterministic, fixture-only aggregate projection that separates source availability from schema/content materiality and routes only proven material changes to a referenced proposed-work record. It does not probe a source, create work, admit RAW data, evaluate policy, promote, release, publish, or authorize public use.

## Source basis

Pass 32 candidate `KFM-P32-FEAT-0016` proposes a watchlist that distinguishes stable availability from material schema or content changes requiring a candidate work record. This contract adapts that idea through existing repository object families instead of creating a parallel health or materiality model:

```text
SourceHealthAssessment reference
  + MaterialChangeAssessment reference
  -> SourceAvailabilityWatchlist entry
  -> NO_ACTION | REVIEW_CANDIDATE | HOLD | ERROR
```

The source material is a downstream design carrier. It does not by itself adopt this contract or prove implementation.

## Responsibility boundary

| This contract owns | It does not own |
|---|---|
| Aggregate source-review projection | Source probing or network transport |
| Separation of availability from materiality | `SourceHealthAssessment` semantics |
| Binding to `MaterialChangeAssessment` outcome | Domain materiality thresholds |
| Candidate-work reference requirement | Candidate-work creation or execution |
| Deterministic counts, ordering, and identity | Policy, review approval, promotion, or release |
| Finite review-routing result | RAW writes, catalog mutation, or publication |

Existing dependencies remain authoritative for their responsibilities:

- `SourceHealthAssessment` records bounded source freshness and retrieval health.
- `MaterialChangeAssessment` records `NON_EVENT`, `PROMOTION_CANDIDATE`, `HOLD`, or `ERROR`.
- `packages/hashing` owns RFC 8785 JCS plus SHA-256 `spec_hash` computation.
- policy, review, promotion, release, correction, and rollback remain separate object families.

## Entry model

Each entry binds:

- one stable `source_id` and exact `kfm://source/{source_id}` reference;
- one `SourceHealthAssessment` reference;
- one `MaterialChangeAssessment` reference;
- one availability state;
- one material-change class, kind, and finite outcome;
- optional schema/content digest pairs;
- one routing result;
- a candidate-work reference only for a proven material change; and
- exact finite reason codes.

Entries are ordered by `source_id`. Duplicate sources or health assessments fail closed.

## Coherent routing

| Change class | Material kind | Material outcome | Watchlist route | Candidate work |
|---|---|---|---|---|
| `UNCHANGED` | `NONE` | `NON_EVENT` | `NO_ACTION` | forbidden |
| `BYTE_ONLY` | `NONE` | `NON_EVENT` | `NO_ACTION` | forbidden |
| `SEMANTIC_NON_MATERIAL` | `NONE` | `NON_EVENT` | `NO_ACTION` | forbidden |
| `MATERIAL` | `SCHEMA`, `CONTENT`, or `BOTH` | `PROMOTION_CANDIDATE` | `REVIEW_CANDIDATE` | required reference |
| `UNDETERMINED` | `UNDETERMINED` | `HOLD` | `HOLD` | forbidden |
| `ERROR` | `ERROR` | `ERROR` | `ERROR` | forbidden |

`REVIEW_CANDIDATE` means only that a separately identified proposed-work record is ready for steward review. The watchlist never creates or executes that record.

## Availability is independent

Availability uses the existing finite health vocabulary:

```text
HEALTHY | DEGRADED | STALE | UNAVAILABLE | UNKNOWN
```

A healthy source can still have a material change. A degraded or stale source can still yield a review candidate when the referenced assessments support it. `UNAVAILABLE` or `UNKNOWN` cannot claim a material change because no trustworthy current comparison is established; they route to `HOLD` or `ERROR`.

## Deterministic identity

The validator computes RFC 8785 JCS plus SHA-256 over the top-level object excluding only `watchlist_id` and `spec_hash`.

```text
spec_hash    = SHA-256(JCS(identity subject))
watchlist_id = "kfm:source-availability-watchlist:" + digest_hex[0:24]
```

Source order, assessment references, digest pairs, routing, counts, observation time, and fixed governance flags all participate in identity.

## Finite validation outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | A coherent `STABLE` or `REVIEW_REQUIRED` projection was validated. |
| `ABSTAIN` | A coherent `HOLD` projection contains unresolved availability or materiality. |
| `DENY` | Shape, identity, binding, routing, ordering, digest, summary, or authority invariants failed. |
| `ERROR` | A coherent entry records an assessment error, or the validator cannot safely read the input. |

A `PASS` with `REVIEW_REQUIRED` does not approve the referenced candidate. It proves only local aggregate consistency.

## Governance posture

Every instance is fixed to:

- `FIXTURE_ONLY`;
- no network attempt;
- no source activation;
- no RAW or lifecycle write;
- no candidate creation or execution;
- no policy evaluation or authority creation;
- no promotion, release, publication, or public use.

## Validation

```bash
python -m unittest tests.validators.test_validate_source_availability_watchlist -v
python tools/validators/source/validate_source_availability_watchlist.py <watchlist.json>
```

The fixture set covers stable, material schema, material content, unresolved, and error states plus exact negative cases for candidate binding, digest evidence, summaries, references, timestamps, availability conflicts, identity, and authority overreach.

## Directory Rules basis

Semantic meaning is owned by `contracts/source/`; machine shape by `schemas/contracts/v1/source/`; deterministic samples by `fixtures/contracts/v1/source/`; executable validation by `tools/validators/source/`; enforceability by `tests/validators/`; CI orchestration by `.github/workflows/`; source adaptation notes by `docs/intake/exploratory/`; and AI-authoring provenance by `data/receipts/generated/`. No new root or parallel source, schema, policy, receipt, proof, release, or publication authority is introduced.

## Rollback

Before merge, close the draft pull request and retire its branch. After an authorized merge, revert the additive packet. No live source, queue, candidate execution, lifecycle state, cache, release, or public artifact requires operational rollback.
