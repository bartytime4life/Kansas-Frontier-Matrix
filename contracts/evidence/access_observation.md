# AccessObservation contract

Status: proposed, fixture-only  
Contract profile: `kfm.access-observation.fixture.v1`

## Purpose

`AccessObservation` records one aggregate service-access measure for one
version-bound Kansas county and one calendar year. It gives `CountyYearPanel`
an explicit, evidence-bearing object for travel time, distance, provider
presence, or service coverage without embedding source-specific rows or method
results in the panel.

The object is an evidence profile. It does not replace the roads, rail, and
trade domain's `AccessRestriction`, calculate a route, identify a provider,
guarantee eligibility or availability, issue emergency guidance, classify a
county as frontier, or authorize publication.

## Ownership and placement

| Concern | Authoritative path |
| --- | --- |
| Meaning and invariants | `contracts/evidence/access_observation.md` |
| Machine shape | `schemas/contracts/v1/evidence/access_observation.schema.json` |
| Conformance examples | `fixtures/contracts/v1/evidence/access_observation/cases.json` |
| Deterministic checks | `tools/validators/evidence/validate_access_observation.py` |
| Executable proof | `tests/validators/evidence/test_validate_access_observation.py` |

This placement follows the accepted directory-governance rule that a path is an
authority claim. Domains and applications may consume the object by digest;
they do not gain a second definition of its meaning.

## Required semantics

Each record binds:

- one digest-bound `GeographyVersion` and one five-digit county feature key;
- one calendar-year reference period and explicit source release, retrieval,
  and optional correction instants;
- one service domain, declared measure family, compatible unit, result state,
  and value or missingness;
- one digest-bound method with declared method family, origin, destination,
  aggregation, and any required threshold or network/model reference;
- one official aggregate source role with digest-bound descriptor, dataset,
  table, variable, and evidence references;
- correction lineage, fixed interpretation limits, governance non-effects, and
  deterministic content identity.

`OBSERVED` requires a nonnegative value and `NOT_APPLICABLE` missingness.
`SUPPRESSED` and `MISSING` prohibit a value. Suppression is never represented as
zero. A real zero remains an observed value.

## Measure and method compatibility

| Measure family | Unit | Method family | Aggregation |
| --- | --- | --- | --- |
| `TRAVEL_TIME` | `MINUTES` | `NETWORK_TRAVEL_TIME` | mean, median, minimum, or maximum |
| `DISTANCE` | `KILOMETRES` | `STRAIGHT_LINE_DISTANCE` | mean, median, minimum, or maximum |
| `PROVIDER_COUNT` | `COUNT` | `PROVIDER_INVENTORY` | count |
| `SERVICE_COVERAGE` | `PERCENT` | `COVERAGE_ESTIMATE` | percent |

Travel time and service coverage require a digest-bound network or model.
Service coverage also requires a digest-bound threshold definition and must be
between zero and 100. Distance and provider count prohibit those fields.

`SOURCE_DEFINED` service domains require a digest-bound source service
definition. Named service domains prohibit that extra reference. The object
preserves the declared method and service definition; it does not execute,
resolve, or validate either one.

## Time and lineage invariants

The reference period must cover exactly the declared calendar year. Source
release cannot precede the period end, retrieval cannot precede release, and a
correction cannot precede release. `ORIGINAL` prohibits correction metadata;
`CORRECTED` requires the correction instant, predecessor digest, and correction
record digest.

## Deterministic identity

Remove `observation_id` and `spec_hash`, canonicalize the remaining JSON using
the repository JCS profile, and compute SHA-256. Store the full digest in
`spec_hash` and derive `observation_id` as `kfm:access-observation:` plus the
first 24 digest hex characters.

## Fixed interpretation limits

The sorted limit set is exactly:

- `AGGREGATE_ONLY`
- `METHOD_BOUND`
- `NO_CAUSAL_CLAIM`
- `NO_PROVIDER_ELIGIBILITY_GUARANTEE`
- `NO_PUBLICATION_AUTHORITY`
- `NO_ROUTING_OR_EMERGENCY_GUIDANCE`
- `SOURCE_ROLE_PRESERVED`
- `VERSION_BOUND`

## Non-effects

Validation is local and fixture-only. It performs no network request, source
download, geography, evidence, service, method, or provider resolution, route
calculation, eligibility determination, emergency dispatch, frontier
classification, policy evaluation, review approval, promotion, release,
public-use authorization, publication, or deployment.

