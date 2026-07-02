# Atmosphere fixtures

`fixtures/domains/atmosphere/`

Status: draft / fixture index.

This directory groups Atmosphere-domain fixture lanes used by bounded tests, validators, no-network checks, helpers, renderer checks, release dry-runs, and documentation examples. Files here are examples only. They are not authoritative project records, source records, evidence, policy decisions, source admissions, rights approvals, release state, live advisory output, health guidance, emergency guidance, public API material, public map material, or published artifacts.

## Scope

Atmosphere fixtures are for offline, deterministic checks. They may exercise schemas, contracts, source descriptors, source-role handling, policy gates, evidence closure, finite-outcome envelopes, safe rendering, and release dry-run behavior before live connectors or public publication are considered.

## Child lanes

| Lane | Purpose | Status |
|---|---|---|
| `bundles/` | Bundle-shaped examples for fixture-only evidence or grouped payload checks. | README present; payload inventory NEEDS VERIFICATION. |
| `golden/` | Stable expected-output examples. | README present; payload inventory NEEDS VERIFICATION. |
| `invalid/` | Negative examples and expected failures. | README present; payload inventory NEEDS VERIFICATION. |
| `invalid/air-observation/` | Negative `AirObservation` examples. | README present; payload inventory NEEDS VERIFICATION. |
| `invalid/air-station/` | Negative `AirStation` examples. | README present; payload inventory NEEDS VERIFICATION. |
| `objects/` | Object-shaped examples across the Atmosphere roster. | README present; payload inventory NEEDS VERIFICATION. |
| `sources/` | Source-shaped examples for source-role, rights, sensitivity, freshness, and admission behavior. | README present; payload inventory NEEDS VERIFICATION. |
| `valid/` | Positive examples for bounded checks. | README present; payload inventory NEEDS VERIFICATION. |

## Valid object lanes

| Lane | Object boundary |
|---|---|
| `valid/advisory-context/` | Advisory referral context; not emergency guidance or live alerting. |
| `valid/air-observation/` | General air-quality observation; not PM2.5, ozone, AQI, model output, or advisory guidance by itself. |
| `valid/air-station/` | Air station/site context; not observation truth or exact public siting approval. |
| `valid/aod-raster/` | Remote-sensing proxy/raster; not PM2.5, AQI, ground observation, or exposure proof. |
| `valid/climate-anomaly/` | Baseline-relative anomaly context; not raw observation, forecast, attribution, or trend proof. |
| `valid/climate-normal/` | Reference-period baseline; not raw observation, anomaly claim, attribution, or trend proof. |
| `valid/forecast-context/` | Modeled atmospheric field; not observation, advisory instruction, or forecast truth proof. |
| `valid/ozone-observation/` | Ozone-specific observation/report context; not generic air observation, PM2.5, or health proof. |
| `valid/pm25-observation/` | PM2.5-specific observation/report context; not AQI collapse, AOD-as-PM2.5, or health proof. |
| `valid/precipitation-observation/` | Precipitation-specific observation/context; not climate claim, forecast truth, or hazards impact proof. |
| `valid/smoke-context/` | Smoke remote-sensing/model context; not PM2.5 proof, hazards truth, impact proof, or advisory output. |
| `valid/temperature-observation/` | Temperature-specific observation/context; not climate claim, hazard proof, or health guidance. |
| `valid/weather-observation/` | General meteorological observation/context; not specialized weather variables, forecast, climate, or hazard truth. |
| `valid/weather-station/` | Weather station/site context; not weather truth, exact public siting approval, or release authority. |
| `valid/wind-field/` | Wind observed/model field; observed and model roles must remain distinct. |

## Related references

- `../../../docs/runbooks/atmosphere/NO_NETWORK_TEST_RUNBOOK.md`
- `../../../docs/domains/atmosphere/OBJECT_FAMILY_MAP.md`
- `../../../docs/domains/atmosphere/SOURCES.md`
- `../../../docs/domains/atmosphere/MISSING_OR_PLANNED_FILES.md`
- `../../../contracts/domains/atmosphere/`
- `../../../schemas/contracts/v1/domains/atmosphere/`
- `../../../policy/domains/atmosphere/`
- `../../../data/registry/sources/atmosphere/README.md`
- `../../../docs/doctrine/directory-rules.md`

## Accepted material

This fixture root may contain:

- small synthetic `*.input.json` examples
- small `*.expected.json` examples
- expected-error text for invalid cases
- object-shaped examples tied to Atmosphere contracts
- source-shaped examples tied to source-descriptor and source-role checks
- bundle-shaped examples for fixture-only evidence closure checks
- README files explaining fixture intent and boundaries

## Exclusions

Do not use this fixture root for:

- authoritative records
- source-system exports
- live upstream fetch results
- EvidenceBundles, proof packs, or receipt storage
- policy rules or policy decisions
- source admissions, rights approvals, or sensitivity approvals
- connector, pipeline, validator, package, or schema implementation code
- release manifests, release candidates, public API material, public map material, public tiles, or published artifacts
- health guidance, emergency guidance, live alerting, or advisory issuance

## Maintenance notes

- Keep examples synthetic, compact, deterministic, and reviewable.
- Keep each fixture tied to a known test, validator, no-network check, helper, renderer check, release dry-run, or documentation example.
- Keep object-family, source-role, rights, freshness, sensitivity, evidence, and release boundaries explicit.
- Pair inputs with expected outputs, expected errors, expected denials, expected abstentions, or expected safe fallbacks when practical.
- Update this parent index when child lanes are added, removed, renamed, or promoted.
- Run relevant tests before claiming fixture validity.

## Verification status

- Parent README: updated from a greenfield stub.
- Child README coverage: PARTIAL; based on current fetches and recent updates.
- Payload inventory: NEEDS VERIFICATION.
- Tests and validators: NOT RUN.
