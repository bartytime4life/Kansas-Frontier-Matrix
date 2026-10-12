# Valid AOD-raster fixtures

`fixtures/domains/atmosphere/valid/aod-raster/`

Status: draft / nested fixture lane.

This directory is for positive `AODRaster` fixture examples used by bounded tests, validators, no-network checks, helpers, or documentation examples. These files are examples only and are not authoritative raster records.

## Scope

Use this lane for compact synthetic aerosol optical depth raster or remote-sensing proxy cases that are expected to pass a specific check while preserving KFM's raster boundary. A valid `AODRaster` fixture may represent governed raster identity, source role, product lineage, spatial extent, retrieval time, valid time, quality flags, processing level, caveats, evidence references, or release dry-run fields required by the test.

A valid fixture here does not prove ground-level PM2.5, AQI, smoke exposure, health impact, visibility impact, regulatory status, or release approval.

## Expected passes

Examples may include payloads that demonstrate:

- source identity, product lineage, raster extent, retrieval time, valid time, and QA posture are represented when required
- `AODRaster` is tagged or interpreted as remote-sensing context, not a ground sensor observation
- AOD remains distinct from PM2.5, AQI, AirObservation, SmokeContext, ForecastContext, and AdvisoryContext
- rights, freshness, caveat, or source-role fields are present when required by the test
- evidence references close within the fixture-only test boundary when required
- safe-render or release dry-run behavior is demonstrated without promoting anything to `data/published/`

## Related fixture lanes

- `../README.md`
- `../../golden/README.md`
- `../../invalid/README.md`
- `../../objects/README.md`
- `../../sources/README.md`

## Related references

- `../../../../../contracts/domains/atmosphere/AODRaster.md`
- `../../../../../contracts/domains/atmosphere/SmokeContext.md`
- `../../../../../contracts/domains/atmosphere/AirObservation.md`
- `../../../../../contracts/domains/atmosphere/PM25Observation.md`
- `../../../../../docs/runbooks/atmosphere/NO_NETWORK_TEST_RUNBOOK.md`
- `../../../../../docs/domains/atmosphere/OBJECT_FAMILY_MAP.md`
- `../../../../../docs/domains/atmosphere/POLICY.md`
- `../../../../../schemas/contracts/v1/domains/atmosphere/AODRaster.schema.json`
- `../../../../../docs/doctrine/directory-rules.md`

## Maintenance notes

- Keep examples synthetic, compact, deterministic, and reviewable.
- Keep each valid fixture tied to a known test, validator, no-network check, helper, or documentation example.
- Record what the fixture is expected to pass; avoid broad claims of real-world correctness.
- Keep `AODRaster` distinct from PM2.5 concentration, AQI reports, ground observations, forecast/model fields, smoke context, advisory context, health guidance, exposure proof, and public tile release unless the fixture is explicitly testing that boundary.
- Pair inputs with expected outputs when practical.
- Do not treat a fixture as evidence, source admission, rights approval, policy approval, release state, PM2.5 proof, exposure proof, health guidance, public tile approval, or a published artifact.
- Update this README when AOD-raster fixture payloads, validators, tests, or helper scripts are added.

## Verification status

- Target README: updated from placeholder content.
- Payload inventory: NEEDS VERIFICATION.
- Tests and validators: NOT RUN.
