# Agriculture Public-Safe Map Feature Candidate

Status: **PROPOSED_INACTIVE** / synthetic-fixture-only domain interface.

This contract defines `AgricultureMapFeatureCandidate`, an Agriculture-owned,
non-released carrier shape for later Catalog/Discovery and Explorer integration.
It is intentionally **not** an Explorer layer, renderer source, publication
record, source-admission path, or release authorization.

## Purpose

The carrier preserves the Agriculture semantics a downstream map consumer needs
without exposing farm/operator truth or taking authority from adjacent domains:

- Agriculture object family and semantic role remain explicit.
- Spatial support is generalized to county, region, or generalized grid support;
  exact field geometry, parcel/owner joins, private addresses, well/right IDs,
  operator identity, proprietary yield/input detail, and transform parameters
  are forbidden.
- Crop/calendar/reporting/valid-period semantics remain explicit.
- Freshness is explicit and deterministic: downstream consumers can distinguish
  current from stale candidates without treating source vintage as a claim of
  present-day currency.
- Observed, modeled/derived, and context-only values cannot collapse into one
  another.
- Soil, Hydrology, Habitat, Geology, Atmosphere, and Hazards authority is never
  created by this carrier.
- Evidence references remain explicit and sorted.
- A shape can be public-safe in precision while still being unreleased:
  policy, review, release, public-use, and publication effects remain false.

## Responsibility roots

- Semantic contract: `contracts/domains/agriculture/public_safe_map_feature.md`
- Machine shape: `schemas/contracts/v1/domains/agriculture/public_safe_map_feature.schema.json`
- Deterministic validator: `tools/validators/domains/agriculture/validate_public_safe_map_feature.py`
- Synthetic fixtures: `fixtures/domains/agriculture/public_safe_map_feature/cases.json`
- Regression proof: `tests/domains/agriculture/test_public_safe_map_feature.py`

These homes follow KFM's responsibility-root model: Agriculture is a segment
inside contract, schema, validator, fixture, and test roots rather than a new
repository root.

## Supported Agriculture families

The first bounded profile admits only map-relevant Agriculture families whose
meaning can be expressed without exact farm/operator geometry:

- `CropObservation`
- `CropRotation`
- `YieldObservation`
- `IrrigationLink`
- `ConservationPractice`
- `SoilCropSuitability`
- `AgriculturalEconomyObservation`
- `SupplyChainNode`
- `DroughtStressIndicator`
- `PestStressIndicator`

`FieldCandidate` is deliberately excluded from this first public-safe carrier
because field-candidate geometry can be reverse-engineerable. `AggregationReceipt`
remains a receipt, not a map feature.

## Semantic roles

- `OBSERVED_AGGREGATE` — released-source meaning is observational aggregate, not
  a modeled result.
- `DERIVED_CONTEXT` — derived Agriculture context such as rotation context.
- `IRRIGATION_CONTEXT` — Agriculture irrigation-use context only; never a
  Hydrology observation or water-right statement.
- `PRACTICE_CONTEXT` — generalized practice context only; never stewardship,
  participation, or legal-status authority.
- `MODELED_SUITABILITY` — Agriculture-owned suitability derivative consuming
  governed Soil evidence without redefining Soil truth.
- `ECONOMIC_AGGREGATE` — generalized Agriculture economic observation.
- `INFRASTRUCTURE_CONTEXT` — generalized infrastructure context; no precise
  private facility location.
- `DERIVED_INDICATOR` — derived stress/production context; never Hazards or
  Atmosphere emergency/forecast authority.

## Spatial support

`support.kind` is limited to `COUNTY`, `REGION`, or `GENERALIZED_GRID`.
`support.generalized` is always `true` and `precision_class` is always
`AGGREGATE_PUBLIC_SAFE` or `GENERALIZED_PUBLIC_SAFE`.

The declared support kind and support key are inseparable. Canonical keys are
restricted to these public-safe namespaces:

- `COUNTY` -> `US-KS-20NNN` Kansas county FIPS form;
- `REGION` -> `KS-AG-<NAME>-REGION-NN` Agriculture-owned generalized region;
- `GENERALIZED_GRID` -> `KS-GRID-<SIZE>KM-NNN-NNN` generalized grid cell.

Precision class is likewise kind-bound: county support requires
`AGGREGATE_PUBLIC_SAFE`, while region and generalized-grid support require
`GENERALIZED_PUBLIC_SAFE`. A candidate cannot select the broader-sounding label
independently of its declared support kind.

A coordinate literal, field/farm identifier, private label, or key from another
support namespace is invalid even when its characters satisfy the generic key
shape.

Protected detail is denied whether it appears as an object member name or is
embedded in an otherwise permitted scalar string such as an indicator value or
evidence reference. Protected identifiers remain denied with punctuation or
plain whitespace separators, and coordinate literals remain denied whether
integer or fractional and whether coordinate pairs use commas or whitespace.
Protected identifier values are denied at every length. A complete scalar that
is shaped as a private identity label remains denied with one or more identity
tokens, regardless of capitalization or Unicode letter width, even when it
omits an ID suffix or uses whitespace, colon, equals, or hash delimiters.
Compatibility-equivalent Unicode forms are normalized before scalar scanning,
so full-width labels, delimiters, and identifiers cannot bypass the same rules.
Descriptive aggregate prose may mention field, farm,
parcel, operator, well, permit, or water-right concepts without being recast as
an identity label; explicit protected identifiers and coordinate literals
remain denied anywhere in a scalar. JSON decoding is strict: malformed documents, duplicate
object members, and non-finite numeric literals receive machine-readable
denials; programmatic candidates receive the same finite-number check before
schema validation or identity hashing.

Every EvidenceRef is carrier-local and synthetic-only. Its canonical form is
`evidence:synthetic:agriculture:<slug>:vN`, where the slug is lowercase
kebab-case and `N` is a positive integer. Foreign-domain, live-source, URL,
parcel, operator, or unversioned references are not admitted by this carrier.

The carrier must never contain exact/reconstructable:

- field boundaries or coordinates;
- parcel IDs or parcel-owner joins;
- operator/farm identities or private addresses;
- well IDs, permits, or water-right identifiers;
- precise sensitive infrastructure;
- proprietary yield/input/application detail;
- transform parameters capable of reconstructing protected detail.

## Temporal semantics

`temporal.kind` is one of `CROP_YEAR`, `CALENDAR_YEAR`, `REPORTING_PERIOD`, or
`VALID_INTERVAL`. `year`, `start`, `end`, and `source_vintage` remain distinct.
`CALENDAR_YEAR` must be January 1 through December 31. A `CROP_YEAR` may
cross calendar boundaries; its explicit interval is authoritative and its year
label must fall within that interval. Reporting/valid intervals likewise keep
their declared year label inside the interval. All intervals require
`start <= end`, and `source_vintage` cannot precede the interval end.

## Freshness semantics

`freshness` separates source vintage from downstream currency. It contains:

- `evaluated_at` — the deterministic date at which currency is assessed;
- `max_age_days` — the Agriculture-specific maximum age accepted as current;
- `state` — exactly `CURRENT` or `STALE`.

`evaluated_at` cannot precede `temporal.source_vintage`. The validator computes
`evaluated_at - source_vintage` in whole days. `state` must be `CURRENT` when
that age is less than or equal to `max_age_days`, otherwise it must be `STALE`.

This is presentation truth only. A `CURRENT` candidate is not automatically
released, authoritative, or approved; a `STALE` candidate remains explicitly
stale for downstream Catalog/Explorer presentation rather than being silently
treated as current.

## Role separation

`indicator.value_role` must agree with `semantic_role`:

- observed/economic aggregates -> `OBSERVED`;
- derived/model roles -> `MODELED_OR_DERIVED`;
- irrigation/practice/infrastructure context -> `CONTEXT_ONLY`.

A map carrier cannot upgrade modeled context to observed truth.

Each supported object family also has one admitted indicator key:

| Object family | Indicator key |
|---|---|
| `CropObservation` | `cropland_class` |
| `CropRotation` | `crop_rotation_class` |
| `YieldObservation` | `yield_rate` |
| `IrrigationLink` | `irrigation_context_class` |
| `ConservationPractice` | `conservation_practice_context_class` |
| `SoilCropSuitability` | `soil_crop_suitability_index` |
| `AgriculturalEconomyObservation` | `agricultural_receipts` |
| `SupplyChainNode` | `supply_chain_context_class` |
| `DroughtStressIndicator` | `drought_stress_index` |
| `PestStressIndicator` | `pest_stress_index` |

Indicator keys cannot carry operator, address, proprietary-value, or another
family's semantics through an otherwise valid candidate.

## Authority and release effects

All adjacent-domain authority flags are fixed false:

- `hydrology_observation`
- `water_right`
- `habitat_occurrence`
- `geology_truth`
- `atmosphere_forecast`
- `hazard_alert`

The synthetic v1 profile is intentionally unreleased. `policy_evaluated`,
`review_approved`, `release_authorized`, `public_use_allowed`, and `published`
must all remain false. This preserves `RAW -> WORK/QUARANTINE -> PROCESSED ->
CATALOG/TRIPLET -> PUBLISHED`; the carrier does not skip lifecycle gates.

## Deterministic identity

The validator removes `id` and `spec_hash`, serializes the remaining candidate
with sorted JSON keys and compact separators, and computes SHA-256.

- `spec_hash = "sha256:" + digest`
- `id = "ag-map-feature:" + digest[:24]`

Changing semantic role, temporal scope, freshness evaluation, spatial support,
evidence binding, sensitivity declaration, or non-effects therefore changes
identity.

## Validation outcomes

- `PASS` — the synthetic candidate satisfies schema and semantic invariants.
- `DENY` — trust, structure, authority, precision, role, temporal, freshness, or identity constraints fail.

No successful validation implies source admission, evidence resolution, policy
approval, release, publication, or truth beyond the candidate fixture.
