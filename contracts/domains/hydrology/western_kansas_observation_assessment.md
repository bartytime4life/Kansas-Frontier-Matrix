# Western Kansas Observation Assessment

Status: `PROPOSED_INACTIVE`

Profile: `kfm.western-kansas-observation-assessment.v1`

This profile is a synthetic, no-network claim-assessment layer over KFM's existing Hydrology `domain_observation` contract. It does not replace that contract, create a second observation authority, admit a source, or publish a drought product.

## Purpose

The profile evaluates whether a bounded western-Kansas observation/forecast/join/claim packet preserves:

- source-family authority and source role;
- observation, validity, forecast, publication, retrieval, and revision time;
- source spatial support, CRS, method, unit, and resolution;
- tuple-level evidence references and payload digests;
- predecessor, correction, and supersession lineage;
- material-change declarations; and
- finite `OBSERVED`, `FORECAST`, `DERIVED`, `CONFLICT`, `STALE`, or `ABSTAIN` states.

Malformed, contradictory, support-erasing, governance-changing, or declared-outcome-mismatched packets return `ERROR`.

## Source families

The profile keeps these source roles separate:

| Source family | Required role | Direct claim scope |
| --- | --- | --- |
| `USDM` | optional legacy role | Drought classification at the source polygon/version |
| `CPC_DROUGHT_OUTLOOK` | `FORECAST` | Drought outlook at the declared issue time, forecast horizon, and native source support |
| `USGS_STREAMFLOW` | optional legacy role | Streamflow condition at the station and observation time |
| `KGS_GROUNDWATER` | optional legacy role | Groundwater condition at the admitted well/aquifer support |
| `PRECIP_EDDI` | optional legacy role | Precipitation or evaporative-demand condition at the source grid/support |
| `SOIL_MOISTURE` | optional legacy role | Soil-moisture condition at the source grid/support |
| `AGRICULTURE_CONTEXT` | optional legacy role | Crop/rangeland context only |
| `WATER_MANAGEMENT_BOUNDARY` | optional legacy role | Join/reference boundary context only |

Existing synthetic v1 observation fixtures remain backward-compatible and may omit `source_role`. New CPC drought-outlook candidates must declare `source_role: FORECAST` and the forecast-specific time fields below.

No family inherits another family's authority, cadence, method, support, uncertainty, or temporal semantics.

## Finite outcomes

- `OBSERVED` — one directly supporting observation/classification family backs the claim at its recorded support and time.
- `FORECAST` — a forecast family backs an outlook claim at an explicit issue time and forecast-validity horizon. It is not an observed current condition.
- `DERIVED` — an explicit transformation combines multiple admitted observation candidates while preserving source support and tuple evidence.
- `CONFLICT` — relevant sources disagree and the packet does not force a winner.
- `STALE` — a relied-on observation exceeds its freshness envelope or a forecast horizon has expired.
- `ABSTAIN` — evidence is missing, superseded, not yet forecast-valid, spatially overgeneralized, or cannot support the requested claim.
- `ERROR` — the packet is malformed, temporally contradictory, loses source support, misdeclares material change, collapses forecast/observation roles, claims governance effects, or disagrees with the computed outcome.

## Temporal rules

Every source object carries distinct fields for:

- `observation_start` and `observation_end`;
- optional `valid_start` and `valid_end`;
- `publication_time`;
- `retrieval_time`;
- `revision_status`; and
- correction or supersession links where applicable.

The general validator requires:

`observation_start <= observation_end <= publication_time <= retrieval_time <= analysis_time`.

A recent publication cannot make an older observation fresh. Observation freshness is computed from `observation_end`, `analysis_time`, and `max_age_days`.

### Forecast successor rules

A `CPC_DROUGHT_OUTLOOK` source additionally requires:

- `source_role: FORECAST`;
- `forecast_issue_time`;
- `forecast_valid_start`;
- `forecast_valid_end`; and
- explicit predecessor identity when `predecessor_relation: SUCCESSOR` is declared.

The additional ordering is:

`observation_end <= forecast_issue_time <= publication_time <= retrieval_time <= analysis_time`

and:

`forecast_issue_time <= forecast_valid_start <= forecast_valid_end`.

The observation window records the source-reported input/initial-condition basis. It is not inferred from publication time or forecast validity.

A successor forecast is not a correction or supersession by default. `predecessor_relation: SUCCESSOR` preserves the prior forecast as a distinct historical artifact. Correction and supersession remain separate relations and must not be inferred from byte changes or a later issue date.

A forecast before `forecast_valid_start` returns `ABSTAIN`; after `forecast_valid_end` it returns `STALE`. A valid forecast claim returns `FORECAST`.

## Spatial and join rules

Every source records support kind, support identifier, CRS, method, unit, and resolution where meaningful. A claim records its requested support separately.

The profile denies:

- county-wide uniformity inferred only from polygon/county intersection;
- resampling that erases source support or resolution;
- management boundaries treated as condition or cause;
- direct claims from a source family outside its admitted role;
- a drought outlook used as proof of an observed drought classification or other current observed condition; and
- cross-source derivation without a transformation reference and complete tuple-level evidence.

## Prohibited inference shortcuts

The exact synthetic matrix and focused tests prove fail-closed handling for:

- USDM to groundwater condition;
- streamflow to groundwater condition;
- soil moisture or contextual evidence to agricultural loss;
- management boundary to condition;
- county intersection to county-wide uniformity;
- recent publication with stale observation time;
- resampling that erases support;
- missing observation as normal or zero;
- superseded source as current truth;
- forecast artifact as observed current condition;
- future or expired forecast horizon misrepresented as current; and
- material-change declarations that do not match claim digests.

## Corrections, successors, and material change

`CORRECTED` observations require both a correction reference and the superseded observation reference. `SUPERSEDED` observations cannot support a current claim.

Forecast succession is deliberately different. A later CPC outlook can be a material `SUCCESSOR` while leaving the earlier outlook historically valid for its own issue and forecast horizon. A successor does not rewrite the predecessor's issue time, valid interval, source bytes, or conclusion.

A packet records prior and current claim digests. The declared material-change flag must equal whether the digests differ. This prevents a source revision or successor forecast from silently rewriting a prior briefing conclusion.

## Authority boundary

All governance effects are fixed false. A green result is not a `SourceDescriptor`, `EvidenceBundle`, `PolicyDecision`, `ValidationReport`, promotion, release, deployment, publication, emergency alert, groundwater declaration, agricultural-loss finding, forecast endorsement, or public-use authorization.

The profile uses only synthetic fixtures. Live observations and forecasts remain gated by source admission, rights, sensitivity, evidence, policy, correction, and release review.

## Validation and rollback

The focused workflow runs the validator's exact legacy case matrix, focused unit tests including forecast-successor anti-collapse cases, schema meta-validation through validator construction, and generated-receipt integrity with networking disabled.

Rollback is an ordinary revert of this additive contract/schema/validator/test extension. The existing observation fixture matrix remains valid, and no live source, data store, release, or public system requires cleanup.
