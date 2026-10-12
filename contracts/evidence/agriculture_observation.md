# AgricultureObservation contract

Status: proposed, fixture-only  
Contract profile: `kfm.agriculture-observation.fixture.v1`

## Purpose

`AgricultureObservation` records one aggregate agricultural measure for one
version-bound Kansas county and one calendar year. It gives `CountyYearPanel`
an explicit, evidence-bearing object for farms, acreage, sales, crop production,
or livestock inventory without embedding source rows in the panel.

The object is an evidence profile. It does not replace the agriculture domain's
`DomainObservation`, resolve a farm or producer, classify a county as frontier,
or authorize publication.

## Ownership and placement

| Concern | Authoritative path |
| --- | --- |
| Meaning and invariants | `contracts/evidence/agriculture_observation.md` |
| Machine shape | `schemas/contracts/v1/evidence/agriculture_observation.schema.json` |
| Conformance examples | `fixtures/contracts/v1/evidence/agriculture_observation/cases.json` |
| Deterministic checks | `tools/validators/evidence/validate_agriculture_observation.py` |
| Executable proof | `tests/validators/evidence/test_validate_agriculture_observation.py` |

This placement follows the accepted directory-governance rule that a path is an
authority claim. The agriculture domain may consume this object by digest; it
does not gain a second definition of the object.

## Required semantics

Each record binds:

- one digest-bound `GeographyVersion` and one five-digit county feature key;
- one calendar-year reference period and explicit source release, retrieval,
  and optional correction instants;
- one declared measure family, unit, result state, and value or missingness;
- optional source-defined unit and classification references, never inline
  classification authority;
- one official aggregate source role with digest-bound descriptor, dataset,
  table, variable, and evidence references;
- correction lineage, fixed interpretation limits, governance non-effects, and
  deterministic content identity.

`OBSERVED` requires a nonnegative value and `NOT_APPLICABLE` missingness.
`SUPPRESSED` and `MISSING` prohibit a value. Suppression is never represented as
zero. A real zero remains an observed value.

## Measure compatibility

| Measure family | Required unit | Monetary basis |
| --- | --- | --- |
| `FARM_COUNT` | `COUNT` | not applicable |
| `LAND_IN_FARMS` | `ACRES` | not applicable |
| `HARVESTED_CROPLAND` | `ACRES` | not applicable |
| `IMPROVED_ACRES` | `ACRES` | not applicable |
| `MARKET_VALUE_SALES` | `USD` | current or constant dollars |
| `CROP_PRODUCTION` | `SOURCE_DEFINED` | not applicable |
| `LIVESTOCK_INVENTORY` | `HEAD` | not applicable |

`SOURCE_DEFINED` requires a digest-bound unit definition. A constant-dollar
measure requires a price year. All other combinations prohibit those fields.

`ALL_AGRICULTURE` prohibits classification details. `SOURCE_CLASSIFIED`
requires a classification kind, scheme reference, and code. The record
preserves the source classification; it does not interpret, reconcile, or
promote it.

## Time and lineage invariants

The reference period must cover exactly the declared calendar year. Source
release cannot precede the period end, retrieval cannot precede release, and a
correction cannot precede release. `ORIGINAL` prohibits correction metadata;
`CORRECTED` requires the correction instant, predecessor digest, and correction
record digest.

## Deterministic identity

Remove `observation_id` and `spec_hash`, canonicalize the remaining JSON using
the repository JCS profile, and compute SHA-256. Store the full digest in
`spec_hash` and derive `observation_id` as
`kfm:agriculture-observation:` plus the first 24 digest hex characters.

## Fixed interpretation limits

The sorted limit set is exactly:

- `AGGREGATE_ONLY`
- `NO_CAUSAL_CLAIM`
- `NO_FARM_OR_PRODUCER_INFERENCE`
- `NO_PUBLICATION_AUTHORITY`
- `SOURCE_ROLE_PRESERVED`
- `SUPPRESSION_PRESERVED`
- `UNIT_AND_CLASSIFICATION_DECLARED`
- `VERSION_BOUND`

## Non-effects

Validation is local and fixture-only. It performs no network request, source
download, geography or evidence resolution, farm or producer identification,
source classification resolution, frontier classification, policy evaluation,
review approval, promotion, release, public-use authorization, publication, or
deployment.

