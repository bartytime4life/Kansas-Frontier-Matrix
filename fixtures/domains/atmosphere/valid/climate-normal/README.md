# Valid climate-normal fixtures

`fixtures/domains/atmosphere/valid/climate-normal/`

Status: draft / nested fixture lane.

This directory is for positive `ClimateNormal` fixture examples used by bounded tests, validators, no-network checks, helpers, or documentation examples. These files are examples only and are not authoritative climate records.

## Scope

Use this lane for compact synthetic reference-period climate baseline cases that are expected to pass a specific check while preserving KFM's climate-normal boundary. A valid `ClimateNormal` fixture may represent governed baseline identity, reference period, aggregation method, variable, units, spatial scope, source role, valid time, retrieval time, uncertainty, aggregation receipt reference, evidence reference, or release dry-run field required by the test.

A valid fixture here does not prove raw observation truth, climate anomaly truth, attribution, trend significance, causal impact, source-rights clearance, public release, or health/safety guidance.

## Expected passes

Examples may include payloads that demonstrate:

- a declared reference period, baseline scope, aggregation method, variable, and units are present when required
- source role, spatial scope, uncertainty, and aggregation receipt fields are represented when required
- source, valid, retrieval, release, and correction times remain distinct where material
- `ClimateNormal` remains distinct from raw observations, `ClimateAnomaly`, forecasts, model fields, event claims, and attribution claims
- aggregation receipt, evidence reference, or citation references close within the fixture-only test boundary when required
- safe-render or release dry-run behavior is demonstrated without promoting anything to `data/published/`

## Related fixture lanes

- `../README.md`
- `../climate-anomaly/README.md`
- `../../golden/README.md`
- `../../invalid/README.md`
- `../../objects/README.md`
- `../../sources/README.md`

## Related references

- `../../../../../contracts/domains/atmosphere/ClimateNormal.md`
- `../../../../../contracts/domains/atmosphere/ClimateAnomaly.md`
- `../../../../../contracts/domains/atmosphere/TemperatureObservation.md`
- `../../../../../contracts/domains/atmosphere/PrecipitationObservation.md`
- `../../../../../docs/runbooks/atmosphere/NO_NETWORK_TEST_RUNBOOK.md`
- `../../../../../docs/domains/atmosphere/OBJECT_FAMILY_MAP.md`
- `../../../../../docs/domains/atmosphere/PUBLICATION_POSTURE.md`
- `../../../../../schemas/contracts/v1/domains/atmosphere/ClimateNormal.schema.json`
- `../../../../../docs/doctrine/directory-rules.md`

## Maintenance notes

- Keep examples synthetic, compact, deterministic, and reviewable.
- Keep each valid fixture tied to a known test, validator, no-network check, helper, or documentation example.
- Record what the fixture is expected to pass; avoid broad claims of real-world correctness.
- Keep `ClimateNormal` distinct from raw observations, climate anomalies, forecasts, model fields, event claims, attribution claims, evidence proof, health guidance, and public layer release unless the fixture is explicitly testing that boundary.
- Pair inputs with expected outputs when practical.
- Do not treat a fixture as evidence, source admission, rights approval, policy approval, release state, attribution proof, trend proof, impact proof, health guidance, or a published artifact.
- Update this README when climate-normal fixture payloads, validators, tests, or helper scripts are added.

## Verification status

- Target README: updated from placeholder content.
- Payload inventory: NEEDS VERIFICATION.
- Tests and validators: NOT RUN.
