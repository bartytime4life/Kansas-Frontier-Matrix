<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/domains/people-dna-land/historical-person-place-event-resolution
title: Historical Person-Place-Event Resolution Candidate Contract
type: semantic-contract; fixture-first; no-network
version: v0.1.0
status: proposed; fixture-only; no-live-resolution; no-publication
owners: OWNER_TBD — People/DNA/Land steward · Evidence steward · Validation steward
created: 2026-08-06
updated: 2026-08-06
policy_label: restricted-review; historical; synthetic-fixture; no-publish
related:
  - ../../../docs/architecture/people-place-joins.md
  - ../../../docs/domains/people-dna-land/IDENTITY_MODEL.md
  - ../../../docs/intake/exploratory/new-ideas-3-11-26-historical-person-place-event-resolution-source-map.md
  - ../../../schemas/contracts/v1/domains/people-dna-land/historical_person_place_event_resolution.schema.json
  - ../../../fixtures/contracts/v1/domains/people-dna-land/historical_person_place_event_resolution/
  - ../../../tools/validators/validate_historical_person_place_event_resolution.py
[/KFM_META_BLOCK_V2] -->

# Historical Person-Place-Event Resolution Candidate Contract

> A deterministic, evidence-referenced scorecard for **synthetic historical candidate
> resolution only**. It never adjudicates identity, residence, migration, land ownership,
> patent validity, title, policy, release, or publication.

## Status and authority

| Field | Value |
|---|---|
| Status | **PROPOSED semantic contract**; executable fixture profile |
| Owning root | `contracts/` — semantic meaning |
| Paired schema | `schemas/contracts/v1/domains/people-dna-land/historical_person_place_event_resolution.schema.json` |
| Fixture profile | `fixtures/contracts/v1/domains/people-dna-land/historical_person_place_event_resolution/` |
| Validator | `tools/validators/validate_historical_person_place_event_resolution.py` |
| Public/release effect | None; `not_released`, `promotion_eligible=false`, `public_exposure=false` |

The attached idea packet proposes authority-ID matching, GLO township/range/section
anchoring, independent source co-mentions, negative evidence, and explicit confidence
bands. The source packet's concrete scoring is preserved here, but its paths and live-source
examples are not treated as repository authority. *New Ideas 3-11-26.pdf*, pp. 25–28.

Current repository doctrine is controlling where it differs. In particular, the existing
person-anchor ladder is LCNAF → VIAF → ISNI → Wikidata → local. SNAC may appear as
corroborative fixture evidence, but it does not become a primary authority or earn the
three-point authority signal by itself in this profile.

## Meaning

`HistoricalPersonPlaceEventResolutionCandidate` is a review candidate that says:

> A synthetic historical person assertion may be related to a time-scoped place/event with
> a reproducible score derived from explicitly enumerated evidence signals and
> contradictions.

It is an event-first relation, not a flat person attribute. Every source signal retains a
`source_ref`, rights label, and minimal scan identifier. Conflicting evidence is retained and
changes the score; it is never silently discarded.

## Deterministic score

| Signal | Points | Rule |
|---|---:|---|
| Authority match | `+3` | At least one exact LCNAF, VIAF, ISNI, or Wikidata match is independently supported by two or more distinct source refs. |
| Independent co-mentions | `+2` | At least three distinct source families support the same synthetic county and time slice. Duplicate records from one family count once. |
| Exact GLO place block | `+2` | A present GLO fixture anchor exactly matches the candidate township/range/section sentinel. |
| Strong contradiction | `-3` | One or more strong census, conflicting-patent, or equivalent negative records exist. |

The score is recomputed from the record; a declared mismatch is invalid.

| Score | Confidence | Required disposition |
|---:|---|---|
| `>= 5` | `high` | `candidate_review` |
| `2..4` | `medium` | `hold_for_review` |
| `< 2` | `low` | `abstain` |

Any strong contradiction requires `hold_for_review` even when the remaining score would
otherwise be high. No confidence band makes the candidate promotion-eligible.

## Required evidence posture

Each authority record, co-mention, GLO anchor, and negative record carries:

- a fixture-safe source reference;
- `rights_spdx` or a fixture license reference;
- one or more minimal `scan_ids` sufficient for a reviewer to locate the synthetic record;
- a role that remains distinct from person, event, place, title, policy, or release truth.

`evidence_refs` must be nonempty and unique. A receipt or fixture result does not become an
EvidenceBundle merely because it contains evidence references.

## Fail-closed boundaries

The validator denies or rejects:

- any `living_person=true` candidate;
- any public-release or public-exposure claim;
- raw DNA, genotype, sequence, DNA segment, or kit/vendor identifiers;
- private parcel identifiers, addresses, coordinates, or precise-location fields;
- score, confidence, disposition, primary-authority, or `spec_hash` drift;
- undeclared fields or malformed source/rights/scan metadata.

All fixtures use `county_fips=99999`, `Synthetic County`, and `T00S/R00W/S00`. Those are
sentinels, not spatial claims. A production resolver, live source adapter, AHCB crosswalk,
GLO connector, or public API is outside this change.

## Finite validation outcomes

- `VALID` — the synthetic candidate matches the bounded profile.
- `INVALID` — one or more deterministic findings exist.
- `ABSTAIN` — represented as a valid low-confidence candidate disposition, not as proof.
- `ERROR` — the validator cannot safely parse or evaluate the input.

## Lifecycle and publication boundary

This profile is repository fixture/test material only. It writes no RAW, WORK, QUARANTINE,
PROCESSED, CATALOG, TRIPLET, PUBLISHED, proof, release, graph, search, vector, cache, API,
map, or AI state. Watchers, workflows, and validators remain non-publishers.

## Rollback

Revert the PR commit to remove the contract, schema, fixtures, validator, tests, workflow,
and generated authoring receipt. No lifecycle or public state is created, so rollback requires
no data migration, cache invalidation, correction notice, or release withdrawal.
