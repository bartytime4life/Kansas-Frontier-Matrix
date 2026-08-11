<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/joins/historical-network-proximity-assessment
title: Historical Network Proximity Assessment Contract
type: semantic-contract
version: v0.1.0
status: proposed; inactive; synthetic-fixture-only; non-authoritative
owners: OWNER_TBD - Join steward; Settlements/Infrastructure steward; Roads/Rail/Trade steward; Evidence steward; Validation steward
created: 2026-08-11
updated: 2026-08-11
policy_label: public-with-gates; historical; uncertainty; temporal; proximity; no-inference
owning_root: contracts/
responsibility: Define a bounded assessment of a historical place assertion and route assertion as a qualified proximity candidate while preserving source role, valid time, spatial uncertainty, and non-authority boundaries.
truth_posture: cite-or-abstain
related:
  - ./README.md
  - ./cross_lane_join_assessment.md
  - ../domains/settlements-infrastructure/historical_place_resolution.md
  - ../domains/settlements-infrastructure/roads-rail-crosswalk.md
  - ../../schemas/contracts/v1/joins/historical_network_proximity_assessment.schema.json
  - ../../fixtures/contracts/v1/joins/historical_network_proximity_assessment/
  - ../../tools/joins/historical_network_proximity.py
  - ../../tests/joins/test_historical_network_proximity.py
  - ../../docs/intake/exploratory/full-atlas-historical-network-proximity-source-map.md
  - ../../data/receipts/generated/genrec-full-atlas-historical-network-proximity-20260811.json
tags: [kfm, joins, historical-place, historical-route, proximity, uncertainty, valid-time, non-publisher]
notes:
  - "Implements the bounded offline-proof seam proposed by Full Atlas KFM-TRIAD-041."
  - "A CANDIDATE conclusion means qualified proximity only; it never asserts route use, service, causality, network membership, historical truth, or publication readiness."
[/KFM_META_BLOCK_V2] -->

# Historical Network Proximity Assessment

> [!CAUTION]
> **PROPOSED / INACTIVE / SYNTHETIC-ONLY.** This assessment contains no coordinates or real locations. It does not establish place truth, route truth, a historical relationship, source admission, policy, review, release, or publication authority.

`HistoricalNetworkProximityAssessmentCandidate` evaluates one already-declared place assertion and one already-declared route assertion without absorbing either domain's authority. It preserves each assertion's valid-time interval, source role, resolution state, geometry/alignment method, uncertainty, and evidence references, then records a synthetic distance band and temporal-overlap result.

## Directory Rules basis

| Responsibility | Home | Role in this slice |
|---|---|---|
| Join meaning | `contracts/joins/` | This qualified relationship contract. |
| Machine shape | `schemas/contracts/v1/joins/` | Closed Draft 2020-12 candidate shape. |
| Synthetic examples | `fixtures/contracts/v1/joins/` | Exact, approximate, non-overlapping, ambiguous, unsupported, and invalid cases. |
| Deterministic helper | `tools/joins/` | No-network, no-write assessment validation. |
| Behavioral proof | `tests/joins/` | Exact finite outcomes and anti-collapse checks. |
| Source mapping | `docs/intake/exploratory/` | Evidence chain, repository gap, and non-effects. |
| Authoring provenance | `data/receipts/generated/` | Artifact-byte hashes and pending human review. |

No new domain, schema, source, policy, receipt, lifecycle, release, or publication root is created.

## Preserved dimensions

| Dimension | Required separation |
|---|---|
| Place assertion | Own ref, source role, valid time, resolution, coordinate method, uncertainty, and evidence refs. |
| Route assertion | Own ref, source role, valid time, resolution, route vintage/alignment method, uncertainty, and evidence refs. |
| Temporal relation | Half-open interval overlap is calculated independently of spatial proximity. |
| Spatial relation | A synthetic minimum/maximum distance band remains distinct from combined uncertainty. |
| Interpretation | Proximity, non-overlap, ambiguity, and unsupported context are finite, explicit states. |

The fixture profile never stores coordinates, geometry, real names, route names, addresses, parcels, people, or sensitive locations.

## Derived conclusion

| Declared outcome | Required interpretation | Bounded meaning |
|---|---|---|
| `CANDIDATE` | `PROXIMITY_CANDIDATE` | Both assertions resolve, use historical roles, overlap in valid time, and preserve coherent distance/uncertainty declarations. Eligible only for independent review. |
| `ABSTAIN` | `NO_TEMPORAL_OVERLAP`, `AMBIGUOUS`, or `UNSUPPORTED` | The intervals do not overlap, an assertion is ambiguous/unresolved, or a modern reference/alignment is context only. |
| `DENY` | none in valid fixtures | Reserved for a validator finding such as collapsed time, invalid uncertainty, distance reversal, or stored/derived mismatch. |
| `ERROR` | none in valid fixtures | Reserved for malformed input, schema failure, unsafe JSON, or forbidden authority overclaim. |

The validator itself returns `PASS` only when the stored interpretation and conclusion agree with the bounded derivation. A stored `ABSTAIN` can therefore validate successfully without becoming a relationship claim.

## Fail-closed rules

- Place and route valid-time intervals use `[start, end)` and require `start < end`.
- `temporal_overlap` must equal the deterministic half-open interval calculation.
- `distance_min_m <= distance_max_m`.
- `combined_uncertainty_m` must equal the declared place plus route uncertainty; it is not hidden inside the distance band.
- Approximate centroids, uncertainty envelopes, and reconstructed historical routes require non-zero uncertainty.
- A modern designated alignment must retain the matching modern source role and can yield only `ABSTAIN`/`UNSUPPORTED`.
- Ambiguous or unresolved assertions cannot yield a proximity candidate.
- Evidence and reason references are canonical sorted unique lists.
- Causal relationship, service relationship, route use, network membership, and historical relationship claims are schema-fixed to `false`.
- Every authority claim is schema-fixed to `false`.

## Non-authority boundary

The profile does not resolve an EvidenceRef, authenticate a source, decide place identity, decide route identity, calculate geometry, query a spatial database, create a join receipt, activate a source, evaluate sensitivity or rights, make a PolicyDecision or ReviewRecord, issue a ReleaseManifest, render a tile, or publish.

## Validation

```bash
python tests/joins/test_historical_network_proximity.py --verbose
python tools/joins/historical_network_proximity.py --fixtures
python tools/validators/validate_generated_receipt.py \
  data/receipts/generated/genrec-full-atlas-historical-network-proximity-20260811.json \
  --repo-root .
```

Green validation proves only closed shape, deterministic fixture materialization, temporal/uncertainty coherence, stored-versus-derived parity, and non-authority declarations for synthetic values.

## Rollback

Before merge, close the draft pull request and delete its branch. After an authorized merge, revert the dependency-closed contract, schema, fixtures, helper, tests, workflow, source map, README entry, and generated receipt. No source, real location, geometry, database row, lifecycle state, tile, release, or publication requires operational rollback.
