# Valid PM2.5-observation fixtures

`fixtures/domains/atmosphere/valid/pm25-observation/`

Status: draft / nested fixture lane.

This directory is for positive `PM25Observation` fixture examples used by bounded tests, validators, no-network checks, helpers, or documentation examples. These files are examples only and are not authoritative PM2.5 records.

## Scope

Use this lane for compact synthetic PM2.5-specific air-quality cases that are expected to pass a specific check while preserving KFM's PM2.5-observation boundary. A valid `PM25Observation` fixture may represent governed PM2.5 value identity, station context, source role, observed time, retrieval time, valid time, units, QA posture, freshness, low-cost caveats, correction/confidence/limitation fields, evidence references, or release dry-run fields required by the test.

A valid fixture here does not prove real-world PM2.5 concentration, AQI status, regulatory exceedance, exposure, health effect, advisory status, source-rights clearance, public release, or policy approval.

## Expected passes

Examples may include payloads that demonstrate:

- station or network context is present when required
- source identity and source role are explicit, including whether the case is concentration, public AQI/report, low-cost sensor, or archive-like context
- observed time, retrieved time, valid time, units, QA posture, freshness, caveats, correction, confidence, and limitations are represented when required
- PM2.5 remains distinct from generic `AirObservation`, ozone, AQI-only reports, model fields, AOD rasters, smoke context, and advisory context
- evidence references close within the fixture-only test boundary when required
- safe-render or release dry-run behavior is demonstrated without promoting anything to `data/published/`

## Related fixture lanes

- `../README.md`
- `../air-observation/README.md`
- `../ozone-observation/README.md`
- `../../golden/README.md`
- `../../invalid/README.md`
- `../../objects/README.md`
- `../../sources/README.md`

## Related references

- `../../../../../contracts/domains/atmosphere/PM25Observation.md`
- `../../../../../contracts/domains/atmosphere/OzoneObservation.md`
- `../../../../../contracts/domains/atmosphere/AirObservation.md`
- `../../../../../contracts/domains/atmosphere/AirStation.md`
- `../../../../../contracts/domains/atmosphere/AODRaster.md`
- `../../../../../docs/runbooks/atmosphere/NO_NETWORK_TEST_RUNBOOK.md`
- `../../../../../docs/domains/atmosphere/OBJECT_FAMILY_MAP.md`
- `../../../../../docs/domains/atmosphere/POLICY.md`
- `../../../../../schemas/contracts/v1/domains/atmosphere/PM25Observation.schema.json`
- `../../../../../docs/doctrine/directory-rules.md`

## Maintenance notes

- Keep examples synthetic, compact, deterministic, and reviewable.
- Keep each valid fixture tied to a known test, validator, no-network check, helper, or documentation example.
- Record what the fixture is expected to pass; avoid broad claims of real-world correctness.
- Keep `PM25Observation` distinct from generic air observations, ozone, AQI-only reports, low-cost uncaveated claims, model fields, AOD-as-PM2.5 claims, smoke context, advisory context, regulatory proof, health guidance, and public layer release unless the fixture is explicitly testing that boundary.
- Pair inputs with expected outputs when practical.
- Do not treat a fixture as evidence, source admission, rights approval, policy approval, release state, PM2.5 truth, regulatory proof, exposure proof, health guidance, advisory output, or a published artifact.
- Update this README when PM2.5-observation fixture payloads, validators, tests, or helper scripts are added.

## Verification status

- Target README: updated from placeholder content.
- Payload inventory: NEEDS VERIFICATION.
- Tests and validators: NOT RUN.
