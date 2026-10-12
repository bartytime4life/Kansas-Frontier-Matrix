<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://intake/exploratory/full-atlas-historical-network-proximity-source-map
title: Full Atlas Historical Network Proximity Source Map
type: source-map
version: v0.1.0
status: confirmed-source-map; proposed-implementation; NEEDS STEWARD REVIEW
owners: OWNER_TBD - Intake steward; Join steward; Settlements/Infrastructure steward; Roads/Rail/Trade steward
created: 2026-08-11
updated: 2026-08-11
policy_label: public-with-gates; provenance; historical; uncertainty; no-source-activation
owning_root: docs/
responsibility: Record the source chain, current-main overlap analysis, placement, and non-effects for the bounded historical network proximity assessment.
truth_posture: cite-or-abstain
[/KFM_META_BLOCK_V2] -->

# Full Atlas historical network proximity source map

## Selected idea and source identity

| Item | Evidence reference | Truth label |
|---|---|---|
| Connected Drive Full Atlas | `gdrive://1whGonKzHVBe5FOU5ovDBakNU4Nf-30tQr09R_UNeBho`; revision `3`; modified `2026-07-12T16:59:46.342Z` | `CONFIRMED` source carrier for KFM-TRIAD-041. |
| Repository mirror | `docs/kfm_full_atlas_seed_cards.md`; SHA-256 `07c7765576df1997e0be88141bd3cd213930e7281d490a8ae62afd78abe8f445`; lines headed `KFM-TRIAD-041` | `CONFIRMED` local wording and candidate keys KFM-CAND-0121 through KFM-CAND-0123. |
| Intake reconciliation | `docs/intake/exploratory/new-ideas-4-16-source-map.md` | `CONFIRMED` warning that proximity is not a historical relationship and recommendation for an offline uncertainty/valid-time fixture slice. |
| Directory authority | `docs/doctrine/directory-rules.md`; SHA-256 `44f7e94344cb42b630008eb0bc03a13fcb97dbdfba6f3e56579693a272571e6e`; accepted by ADR-0029 | `CONFIRMED` responsibility-root placement. |

The atlas is an exploratory carrier. It proposes work but does not admit a source, authorize a historical assertion, or approve release.

## Current-main overlap check

Reviewed base: `main@f2ef6741430f93270eb38a4ee9170f8a3726e5b3`. Connected GitHub searches returned no open pull request for `KFM-TRIAD-041` or historical-network temporal proximity at review time.

Current main already contains useful but non-equivalent surfaces:

- `contracts/joins/cross_lane_join_assessment.md` and `tools/joins/join_candidates.py` provide a generic synthetic spatial-temporal candidate lane, but do not represent separate coordinate/alignment methods, per-side uncertainty, route vintage, a distance band, or the historical no-inference interpretation.
- `contracts/domains/settlements-infrastructure/historical_place_resolution.md` resolves synthetic name-and-year candidates while deliberately forbidding coordinates and geometry.
- `contracts/domains/settlements-infrastructure/roads-rail-crosswalk.md` documents proposed temporal, historical-route, source-role, limitation, and review fields, but states that its serialized shape is not field-complete until a paired schema and validators exist.
- `docs/intake/exploratory/new-ideas-4-16-source-map.md` explicitly lists historical place/route proximity fixtures with uncertainty and valid-time checks as a later bounded offline-proof option.

## Gap decision

Status: `REPO_GAP`, accepted only as an inactive join-assessment profile.

The slice adds one qualified relationship carrier. It references place and route assertion candidates but does not define their domain truth. It derives only:

- half-open valid-time overlap;
- a declared synthetic distance band;
- combined declared uncertainty;
- modern-context, ambiguity, and unresolved abstentions; and
- a qualified proximity-candidate interpretation with all relationship and authority claims fixed to false.

It intentionally does not implement `HistoricalPlaceAssertion`, `HistoricalRouteSegment`, a live `TemporalSpatialJoinReceipt`, source descriptors, ingestion, spatial SQL, public-safe tiles, map UI, policy, release, or publication.

## Placement and non-effects

Directory Rules place join meaning in `contracts/joins/`, shape in `schemas/contracts/v1/joins/`, synthetic examples in `fixtures/contracts/v1/joins/`, the deterministic helper in `tools/joins/`, proof in `tests/joins/`, this source map in `docs/intake/exploratory/`, and authoring provenance in `data/receipts/generated/`.

No new root or parallel domain, schema, source, policy, evidence, receipt, lifecycle, release, proof, or publication authority is created. The artifacts process no real place, route, coordinate, geometry, person, parcel, infrastructure, or sensitive-location data.

## Rollback

Revert the bounded feature commit. No source state, database, real geometry, join record, map layer, tile, policy decision, review record, release, or publication requires operational rollback.
