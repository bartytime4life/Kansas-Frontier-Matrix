# Kansas Transportation Geometry Source Assessment

Status: `PROPOSED_INACTIVE`

Profile: `kfm.source.kansas-transportation-geometry-source-assessment.fixture.v1`

`KansasTransportationGeometrySourceAssessmentCandidate` is a synthetic, no-network profile that converts the reviewed transportation source-admission assessment into deterministic, testable source-role and hold-state rules. It does not create a `SourceDescriptor`, admit a source, fetch a service, store source bytes, decide a canonical road network, or authorize public use.

## Purpose

The profile preserves four separate source lanes:

| Lane | Permitted role | Fixture disposition |
| --- | --- | --- |
| `DASC_NG911_ROAD_CENTERLINE` | Candidate primary road geometry for non-KDOT-maintained roads and NG911 addressing context | `ADMIT_REFERENCE_CANDIDATE` |
| `KDOT_KHUB_LRS` | Candidate state/public-highway route, event, and measure reference | `ADMIT_REFERENCE_CANDIDATE` |
| `KDOT_MOBILE_LIDAR` | Candidate transportation observation or derived-asset source, never road-network authority | `HOLD` |
| `DASC_SUPPORTING_PRODUCTS` | Catalog, stewardship, boundary, and discovery support only | `ADMIT_REFERENCE_CANDIDATE` |

No lane inherits another lane's geometry, attribute, observation, catalog, rights, or correction authority.

## Finite validator outcomes

- `PASS` means the synthetic profile is internally coherent and ready for human review. It does not admit a source.
- `DENY` means endpoint identity, role separation, CRS, pagination, authentication, identifier semantics, crosswalk safeguards, blockers, or declared dispositions are inconsistent.
- `ERROR` means the candidate is malformed, non-canonical, identity-tampered, or claims a governance effect that the profile forbids.

Every successful candidate remains `review_state: HOLD` and `status: PROPOSED_INACTIVE`.

## Endpoint and protocol declarations

The profile pins only safe repository-local interface identities, not live URLs or source payloads:

- NG911 road centerline: `kfm://source-interface/dasc/ng911-road-centerline/mapserver/1`, layer `1`, EPSG:3395, maximum response `1000`, JSON/GeoJSON.
- KDOT K-Hub/LRS: `kfm://source-interface/kdot/state-system-kups/mapserver/0`, layer `0`, ESRI:6923, maximum response `2000`, JSON/GeoJSON/PBF.
- KDOT mobile LiDAR: `kfm://source-interface/kdot/mobile-lidar/project-portal`, account-required metadata/download posture, product identity unresolved.
- DASC supporting products: `kfm://source-interface/dasc/supporting-products/catalog`, product-specific authority and rights unresolved.

A later live snapshot must separately pin the exact URL, source metadata digest, query, pagination, response digest, record count, rights, sensitivity, and correction behavior.

## Identifier-role separation

The profile distinguishes:

- `NGSEGID` as an NG911 segment identifier;
- `LRSKEY` as a crosswalk candidate only;
- `RouteID` as a K-Hub route identifier;
- `EventID` as a K-Hub event identifier; and
- `GlobalID` as an object-store identifier, not a cross-system semantic key.

Identifier labels must not collapse into one role. Matching values do not prove a stable one-to-one crosswalk.

## Crosswalk safeguards

The synthetic crosswalk declaration requires temporal overlap, explicit split/merge modeling, and a hold state. Proximity-only matching is denied. Geometry disagreement cannot be accepted until a reviewed tolerance and supporting evidence exist. The profile models uncertainty; it does not choose a winner.

## Rights, sensitivity, and precision

Official service availability does not establish redistribution or public-use authority. The fixture packet keeps rights unresolved, precision unreviewed, and source snapshots unpinned. Mobile LiDAR remains on hold because account access, product rights, derivative methodology, exact precision, and stable collection identity are unresolved.

An `APPROVED` or `GENERALIZED` precision state requires a non-null policy reference. A prohibited rights state is denied. Credentials, tokens, session material, raw queries, and source payloads are outside this profile.

## Deterministic identity

The validator computes `spec_hash` as SHA-256 over canonical JSON for the complete candidate excluding only `assessment_id` and `spec_hash`. `assessment_id` is `ks-transport-geometry-assessment:` plus the first 24 hexadecimal characters of that digest.

## Authority boundary

All governance effects are fixed `false`, including network access, credential resolution, source admission, connector or schedule creation, lifecycle mutation, road-authority or crosswalk decisions, evidence or policy decisions, release, publication, and public-use authorization.

## Directory Rules basis

- `contracts/source/` owns source-assessment semantics.
- `schemas/contracts/v1/source/` owns machine shape.
- `fixtures/contracts/v1/source/` owns synthetic cases.
- `tools/validators/source/` owns reusable validation.
- `tests/source/` owns executable proof.
- `.github/workflows/` owns read-only CI orchestration.
- `data/receipts/generated/` owns the authoring receipt.

These are existing responsibility roots adopted through ADR-0029. The profile creates no new root and no parallel source, evidence, policy, lifecycle, release, or publication authority.

## Rollback

Before merge, close the draft pull request and remove its task branch. After a separately authorized merge, revert this additive packet and rerun the focused workflow. No live source, credential, data store, release, deployment, cache, or public surface requires cleanup.
