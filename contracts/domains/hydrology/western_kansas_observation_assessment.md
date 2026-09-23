# Western Kansas Observation Assessment

Status: `PROPOSED_INACTIVE`

Profile: `kfm.western-kansas-observation-assessment.v1`

This profile is a synthetic, no-network claim-assessment layer over KFM's
existing Hydrology `domain_observation` contract. It does not replace that
contract, create a second observation authority, admit a source, or publish a
drought product.

## Purpose

The profile evaluates whether a bounded western-Kansas observation/join/claim
packet preserves:

- source-family authority;
- observation, validity, publication, retrieval, and revision time;
- source spatial support, CRS, method, unit, and resolution;
- tuple-level evidence references and payload digests;
- correction and supersession lineage;
- material-change declarations; and
- finite `OBSERVED`, `DERIVED`, `CONFLICT`, `STALE`, or `ABSTAIN` states.

Malformed, contradictory, support-erasing, governance-changing, or
declared-outcome-mismatched packets return `ERROR`.

## Source families

The profile keeps these source roles separate:

| Source family | Direct claim scope |
| --- | --- |
| `USDM` | Drought classification at the source polygon/version |
| `USGS_STREAMFLOW` | Streamflow condition at the station and observation time |
| `KGS_GROUNDWATER` | Groundwater condition at the admitted well/aquifer support |
| `PRECIP_EDDI` | Precipitation or evaporative-demand condition at the source grid/support |
| `SOIL_MOISTURE` | Soil-moisture condition at the source grid/support |
| `AGRICULTURE_CONTEXT` | Crop/rangeland context only |
| `WATER_MANAGEMENT_BOUNDARY` | Join/reference boundary context only |

No family inherits another family's authority, cadence, method, support, or
uncertainty.

## Finite outcomes

- `OBSERVED` — one directly supporting source family backs the claim at its
  recorded support and time.
- `DERIVED` — an explicit transformation combines multiple admitted observation
  candidates while preserving source support and tuple evidence.
- `CONFLICT` — relevant sources disagree and the packet does not force a winner.
- `STALE` — one or more relied-on observations exceed the declared freshness
  envelope, even when publication or retrieval is recent.
- `ABSTAIN` — evidence is missing, superseded, spatially overgeneralized, or
  cannot support the requested claim.
- `ERROR` — the packet is malformed, temporally contradictory, loses source
  support, misdeclares material change, claims governance effects, or disagrees
  with the computed outcome.

## Temporal rules

Every source object carries distinct fields for:

- `observation_start` and `observation_end`;
- optional `valid_start` and `valid_end`;
- `publication_time`;
- `retrieval_time`;
- `revision_status`; and
- correction or supersession links where applicable.

The validator requires:

`observation_start <= observation_end <= publication_time <= retrieval_time <= analysis_time`.

A recent publication cannot make an older observation fresh. Freshness is
computed from `observation_end`, `analysis_time`, and `max_age_days`.

The validator parses every declared instant defensively. A malformed or
timezone-less value remains inside the finite result boundary as `ERROR` with
`TEMPORAL_ORDER_INVALID`; parser exceptions are not exposed as execution
failures.

## Spatial and join rules

Every source records support kind, support identifier, CRS, method, unit, and
resolution where meaningful. A claim records its requested support separately.

For a directly supporting source family, every source's `support_kind` and
`support_id` must exactly match the direct claim's recorded support. An otherwise
eligible direct claim at a different support returns `ABSTAIN` with
`SOURCE_SUPPORT_MISMATCH`. Caller declarations of preserved support, resampling,
or a transformation reference do not override that identity check. A packet that
still declares `OBSERVED` additionally receives `DECLARED_OUTCOME_MISMATCH` and
returns `ERROR` under the existing outcome-consistency rule.

This check does not apply direct-observation identity rules to
`CROSS_SOURCE_STRESS`: its explicit transformation may combine differing source
supports under the existing derived-claim rules. Existing family-role,
county-intersection and support-erasure failures keep their specific reasons;
the support mismatch is reported only when those earlier claim checks permit a
direct claim. Finite precedence remains `ERROR` before `ABSTAIN`, then `STALE`,
`CONFLICT`, and the supported result.

The profile denies:

- county-wide uniformity inferred only from polygon/county intersection;
- resampling that erases source support or resolution;
- management boundaries treated as condition or cause;
- direct claims from a source family outside its admitted role; and
- cross-source derivation without a transformation reference and complete
  tuple-level evidence.

## Prohibited inference shortcuts

The exact synthetic matrix proves fail-closed handling for:

- USDM to groundwater condition;
- streamflow to groundwater condition;
- soil moisture or contextual evidence to agricultural loss;
- management boundary to condition;
- county intersection to county-wide uniformity;
- recent publication with stale observation time;
- resampling that erases support;
- missing observation as normal or zero;
- superseded source as current truth; and
- material-change declarations that do not match claim digests.

## Corrections and material change

`CORRECTED` observations require both a correction reference and the superseded
observation reference. `SUPERSEDED` observations cannot support a current claim.

A packet records prior and current claim digests. The declared material-change
flag must equal whether the digests differ. This prevents a source revision from
silently rewriting a prior briefing conclusion.

## Authority boundary

All governance effects are fixed false. A green result is not a
`SourceDescriptor`, `EvidenceBundle`, `PolicyDecision`, `ValidationReport`,
promotion, release, deployment, publication, emergency alert, groundwater
declaration, agricultural-loss finding, or public-use authorization.

The profile uses only synthetic fixtures. Live observations remain gated by
source admission, rights, sensitivity, evidence, policy, correction, and release
review.

## Validation and rollback

The focused workflow runs the validator's exact case matrix, focused unit tests,
schema meta-validation, and generated-receipt integrity with networking disabled.

The support-identity repair retains the historical fixture matrix and receipts
unchanged. Its added tests cover all direct source families, same-kind/different-ID
and different-kind claims, caller flags, corrected and stale observations,
multiple source supports, declared outcomes, and unchanged explicit derivation.
The new receipt binds current changed bytes; prior receipts remain evidence of
their pinned historical revisions. Packets previously accepted as `OBSERVED`
despite mismatched direct support must now narrow the claim to the recorded
support or abstain. No existing matching direct claim or fixture outcome is
reclassified, and no source, schema, seam or public-join authority is introduced.

Rollback of the support-identity repair is a focused revert of its validator,
tests, contract clarification, workflow receipt binding, and successor receipt.
That revert would restore the unsupported-observation gap; prefer a same-family
forward fix. Historical receipts and fixtures must remain intact in either case.

Rollback is an ordinary revert of the additive contract, schema, fixtures,
validator, tests, workflow, and receipt. No live source, data store, release, or
public system requires cleanup.
