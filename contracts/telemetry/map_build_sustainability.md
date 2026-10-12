<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/telemetry/map-build-sustainability
title: Map Build Sustainability Telemetry Fixture Profile
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; no-network; non-authoritative
owners: OWNER_TBD — Map artifact steward · Observability steward · Sustainability owner · Validation steward
created: 2026-08-11
updated: 2026-08-11
owning_root: contracts/
policy_label: internal; telemetry; map-build; energy; carbon; review-signal
responsibility: Define a closed fixture-only meaning for map-build energy and carbon estimates as internal operational review evidence without creating mapped-phenomenon truth, thresholds, release authority, or telemetry collection.
truth_posture: "CONFIRMED supplied-card and repository traceability / PROPOSED inactive fixture profile / UNKNOWN production methodology thresholds and runtime integration / NEEDS VERIFICATION human review and hosted CI"
related:
  - ./README.md
  - ../../schemas/contracts/v1/telemetry/map_build_sustainability.schema.json
  - ../../fixtures/contracts/v1/telemetry/map_build_sustainability/README.md
  - ../../fixtures/contracts/v1/telemetry/map_build_sustainability/cases.json
  - ../../tools/validators/telemetry/validate_map_build_sustainability.py
  - ../../tests/validators/telemetry/test_map_build_sustainability.py
  - ../../docs/dashboards/observability/energy-carbon-footprint.md
  - ../../docs/standards/TELEMETRY_MINIMUMS.md
  - ../../docs/intake/exploratory/pass-18-map-build-sustainability-source-map.md
[/KFM_META_BLOCK_V2] -->

# Map Build Sustainability Telemetry Fixture Profile

This contract implements the smallest reviewable portion of supplied Pass 18 card `KFM-P18-INV-424`: a map artifact build may carry energy and carbon telemetry as operational evidence, but those values are not claims about the mapped phenomenon.

The profile is `PROPOSED_INACTIVE_FIXTURE_ONLY`. It validates synthetic candidate records and demonstrates three finite postures:

- `PASS` when energy and carbon estimates are present, bounded, internally consistent, explicitly uncertain, and non-authoritative;
- `ABSTAIN` when measurement or factor evidence is unavailable; and
- `DENY` when shape, time, arithmetic, uncertainty, or authority boundaries fail.

## What the candidate binds

| Surface | Meaning | Boundary |
|---|---|---|
| `build_binding` | A synthetic map-build reference, artifact digest, and UTC measurement window. | Does not prove that the build or artifact exists. |
| `energy` | A measured or estimated joule value, method reference/version, and relative uncertainty; or a bounded unavailable reason. | Does not collect energy telemetry or certify a tool. |
| `carbon` | A gCO2e estimate, regional factor metadata, uncertainty, and rounding tolerance; or a bounded unavailable reason. | Does not select or approve an accounting methodology. |
| `review_posture` | Fixes purpose to `REVIEW_SIGNAL_ONLY` and threshold status to `UNRESOLVED_NO_AUTOMATIC_DENIAL`. | Cannot decide policy, promotion, or release. |
| `sensitivity` | Keeps per-build and per-workflow details internal and public rollup unauthorized. | Does not approve any public dashboard or report. |
| `authority_claims` | Fixes environmental-truth, evidence, policy, review, promotion, release, publication, and public-use authority to `false`. | A passing fixture remains non-authoritative. |

Numeric values are decimal strings rather than binary floating-point values. When both measurements are available, the validator checks:

$$
\text{expected gCO2e} = \frac{\text{joules}}{3{,}600{,}000} \times \text{factor gCO2e/kWh}
$$

The declared carbon value must fall within the candidate's explicit rounding tolerance, and the fixture profile caps that arithmetic tolerance at `0.001 gCO2e` so a caller cannot hide an inconsistent calculation behind an unbounded tolerance. This is an internal-consistency rule, not a sustainability policy threshold; it does not establish that the energy reading, factor, region, method, or resulting estimate is accurate.

## Authority and threshold boundary

The source card asks which thresholds should trigger review rather than automatic denial. The repository also leaves accounting methodology and carbon budgets unresolved. This slice does not answer those governance questions.

A validator result cannot:

- measure a live build, contact a telemetry sink, fetch a regional factor, or certify a provider;
- amend `RunReceipt`, `ReleaseManifest`, policy, dashboard, lifecycle, or artifact bytes;
- establish environmental truth about any mapped layer, place, source, or phenomenon;
- set a carbon budget, threshold, alert, policy outcome, or automatic release denial;
- approve a review, promotion, release, deployment, publication, public rollup, or public use; or
- replace evidence, release, correction, or rollback objects.

`ABSTAIN` is a valid safe outcome. Missing telemetry remains visible without inventing a zero, silently selecting a factor, or weakening the authority boundary.

## Directory Rules basis

Accepted Directory Rules place semantic meaning under `contracts/`, machine shape under `schemas/`, reusable synthetic candidates under `fixtures/`, repository validation under `tools/`, executable conformance under `tests/`, read-only orchestration under `.github/`, and source reconciliation under `docs/intake/exploratory/`.

No policy file is added because methodology, budgets, thresholds, and release effects remain unresolved. No runtime adapter is added because this slice does not collect telemetry.

## Validation

```bash
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python -m unittest discover \
  --start-directory tests/validators/telemetry \
  --pattern 'test_map_build_sustainability.py' \
  --verbose

PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tools/validators/telemetry/validate_map_build_sustainability.py \
  --fixtures
```

## Activation and rollback

Production activation remains `HOLD` until stewards choose and version a methodology, define factor provenance and acceptable uncertainty, classify sensitivity and retention, decide review thresholds, bind an accepted receipt/release object, implement source-side minimization, and add runtime and release evidence.

Rollback is a single additive revert. The profile has no runtime consumer and mutates no build, artifact, receipt, policy, release, deployment, dashboard, or public surface.
