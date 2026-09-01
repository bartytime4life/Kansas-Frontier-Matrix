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

| Source family | Direct claim scope | Authority/cadence | Spatial support and resolution | Revision/correction posture | Rights posture |
| --- | --- | --- | --- | --- | --- |
| `USDM` | Drought classification at the source polygon/version | Official weekly category release | Polygon support with source-native scale preserved | Weekly versions and any corrections remain explicit lineage | Public discovery does not equal KFM source admission |
| `USGS_STREAMFLOW` | Streamflow condition at the station and observation time | Official station observations and daily comparisons | Station support with source-native unit/statistic | Provisional/final and correction/supersession status remain explicit | Rights/admission unresolved until separately approved |
| `KGS_GROUNDWATER` | Groundwater condition at the admitted well/aquifer support | KGS well/aquifer observation cadence | Point/well/aquifer support with source-native scale | Correction/supersession references required when present | Rights and water-right boundaries remain source-specific |
| `PRECIP_EDDI` | Precipitation or evaporative-demand condition at the source grid/support | Product-specific cadence for precip/EDDI products | Grid support with source-native resolution preserved | Product revision identity and corrections remain explicit | Admission and rights are independent of other families |
| `SOIL_MOISTURE` | Soil-moisture condition at the source grid/support | Product-specific soil-moisture cadence | Grid support with source-native resolution preserved | Product revision identity and corrections remain explicit | Admission and rights are independent of other families |
| `AGRICULTURE_CONTEXT` | Crop/rangeland context only | Context publication cadence only | Source-native context support; no loss inference | Corrections remain explicit and independent | Context does not inherit hydrology claim authority |
| `WATER_MANAGEMENT_BOUNDARY` | Join/reference boundary context only | Boundary publication cadence only | Management-area or boundary support only | Boundary updates are lineage-tracked reference changes | Boundaries are join context, not condition/cause authority |

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
- `observation_id`, `method`, `unit`, `statistic`, `threshold`, and `uncertainty`;
- correction or supersession links where applicable.

The validator requires:

`observation_start <= observation_end <= publication_time <= retrieval_time <= analysis_time`.

A recent publication cannot make an older observation fresh. Freshness is
computed from `observation_end`, `analysis_time`, and `max_age_days`.

## Spatial and join rules

Every source records support kind (`STATION`, `POINT`, `POLYGON`, `GRID_CELL`,
`BASIN`, `COUNTY`, `MANAGEMENT_AREA`, or `OTHER`), support identifier, CRS,
method, unit, statistic, threshold, uncertainty, and resolution where
meaningful. A claim records its requested support separately.

The profile denies:

- county-wide uniformity inferred only from polygon/county intersection;
- resampling that erases source support or resolution;
- management boundaries treated as condition or cause;
- direct claims from a source family outside its admitted role; and
- cross-source derivation without a transformation reference and complete
  tuple-level evidence from at least two joined source observations.

## Prohibited inference shortcuts

The exact synthetic matrix proves fail-closed handling for:

- USDM to groundwater condition;
- streamflow to groundwater condition;
- soil moisture or contextual evidence to agricultural loss;
- evaporative-demand indicators to agricultural loss;
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

Rollback is an ordinary revert of the additive contract, schema, fixtures,
validator, tests, workflow, and receipt. No live source, data store, release, or
public system requires cleanup.
