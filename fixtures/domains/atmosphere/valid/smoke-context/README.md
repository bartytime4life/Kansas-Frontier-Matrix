# Valid smoke-context fixtures

`fixtures/domains/atmosphere/valid/smoke-context/`

Status: draft / nested fixture lane.

This directory is for positive `SmokeContext` fixture examples used by bounded tests, validators, no-network checks, helpers, or documentation examples. These files are examples only and are not authoritative smoke records.

## Scope

Use this lane for compact synthetic smoke-context cases that are expected to pass a specific check while preserving KFM's smoke-context boundary. A valid `SmokeContext` fixture may represent governed smoke mask, plume, analysis context, modeled smoke forecast context, source role, source time, analysis time, forecast time, retrieval time, geometry or raster reference, uncertainty, sensitivity posture, evidence references, or release dry-run fields required by the test.

A valid fixture here does not prove PM2.5 concentration, AOD truth, fire or hazards event truth, exposure, health impact, damage, evacuation need, advisory status, source-rights clearance, public release, or policy approval.

## Expected passes

Examples may include payloads that demonstrate:

- source identity and source role are explicit, including whether the case is a remote-sensing mask/proxy or atmospheric model field
- source time, analysis time, forecast time, retrieval time, valid time, uncertainty, and sensitivity fields are represented when required
- smoke context remains distinct from PM2.5 observations, AOD rasters, generic air observations, model forecasts, advisory context, and Hazards-domain event or impact truth
- sensitive joins are absent, generalized, denied, or represented with an expected safe fallback when required by the test
- evidence references close within the fixture-only test boundary when required
- safe-render or release dry-run behavior is demonstrated without promoting anything to `data/published/`

## Related fixture lanes

- `../README.md`
- `../aod-raster/README.md`
- `../pm25-observation/README.md`
- `../forecast-context/README.md`
- `../advisory-context/README.md`
- `../../golden/README.md`
- `../../invalid/README.md`
- `../../objects/README.md`
- `../../sources/README.md`

## Related references

- `../../../../../contracts/domains/atmosphere/SmokeContext.md`
- `../../../../../contracts/domains/atmosphere/AODRaster.md`
- `../../../../../contracts/domains/atmosphere/PM25Observation.md`
- `../../../../../contracts/domains/atmosphere/AirObservation.md`
- `../../../../../contracts/domains/atmosphere/ForecastContext.md`
- `../../../../../contracts/domains/atmosphere/AdvisoryContext.md`
- `../../../../../docs/runbooks/atmosphere/NO_NETWORK_TEST_RUNBOOK.md`
- `../../../../../docs/domains/atmosphere/OBJECT_FAMILY_MAP.md`
- `../../../../../docs/domains/atmosphere/POLICY.md`
- `../../../../../schemas/contracts/v1/domains/atmosphere/SmokeContext.schema.json`
- `../../../../../docs/doctrine/directory-rules.md`

## Maintenance notes

- Keep examples synthetic, compact, deterministic, and reviewable.
- Keep each valid fixture tied to a known test, validator, no-network check, helper, or documentation example.
- Record what the fixture is expected to pass; avoid broad claims of real-world correctness.
- Keep `SmokeContext` distinct from PM2.5 measurements, AOD rasters, observed sensors, model forecasts, advisory instructions, Hazards-domain event truth, impact claims, evidence proof, health guidance, life-safety guidance, and public layer release unless the fixture is explicitly testing that boundary.
- Pair inputs with expected outputs when practical.
- Do not treat a fixture as evidence, source admission, rights approval, policy approval, release state, smoke truth, PM2.5 proof, hazards proof, impact proof, exposure proof, health guidance, advisory output, or a published artifact.
- Update this README when smoke-context fixture payloads, validators, tests, or helper scripts are added.

## Verification status

- Target README: updated from placeholder content.
- Payload inventory: NEEDS VERIFICATION.
- Tests and validators: NOT RUN.
