# Valid forecast-context fixtures

`fixtures/domains/atmosphere/valid/forecast-context/`

Status: draft / nested fixture lane.

This directory is for positive `ForecastContext` fixture examples used by bounded tests, validators, no-network checks, helpers, or documentation examples. These files are examples only and are not authoritative forecast records.

## Scope

Use this lane for compact synthetic forecast or modeled-atmospheric-field cases that are expected to pass a specific check while preserving KFM's forecast boundary. A valid `ForecastContext` fixture may represent governed model-run identity, source role, initialization time, valid time, forecast horizon, product lineage, spatial scope, uncertainty, model-run receipt reference, evidence reference, or release dry-run field required by the test.

A valid fixture here does not prove the forecast is correct, authorize model-as-observation claims, substitute for an official forecast or advisory source, provide emergency guidance, or approve release of controlled Atmosphere/Air forecast products.

## Expected passes

Examples may include payloads that demonstrate:

- model-run source, initialization time, valid time, forecast horizon, product lineage, and uncertainty are represented when required
- source role identifies forecast/model context rather than observed-sensor truth
- source, valid, retrieval, release, and correction times remain distinct where material
- `ForecastContext` remains distinct from observations, station records, AOD rasters, smoke context, climate context, and advisory context
- model-run receipt, evidence reference, or citation references close within the fixture-only test boundary when required
- safe-render or release dry-run behavior is demonstrated without promoting anything to `data/published/`

## Related fixture lanes

- `../README.md`
- `../advisory-context/README.md`
- `../../golden/README.md`
- `../../invalid/README.md`
- `../../objects/README.md`
- `../../sources/README.md`

## Related references

- `../../../../../contracts/domains/atmosphere/ForecastContext.md`
- `../../../../../contracts/domains/atmosphere/AdvisoryContext.md`
- `../../../../../contracts/domains/atmosphere/WindField.md`
- `../../../../../contracts/domains/atmosphere/SmokeContext.md`
- `../../../../../docs/runbooks/atmosphere/NO_NETWORK_TEST_RUNBOOK.md`
- `../../../../../docs/domains/atmosphere/OBJECT_FAMILY_MAP.md`
- `../../../../../docs/domains/atmosphere/PUBLICATION_POSTURE.md`
- `../../../../../schemas/contracts/v1/domains/atmosphere/ForecastContext.schema.json`
- `../../../../../docs/doctrine/directory-rules.md`

## Maintenance notes

- Keep examples synthetic, compact, deterministic, and reviewable.
- Keep each valid fixture tied to a known test, validator, no-network check, helper, or documentation example.
- Record what the fixture is expected to pass; avoid broad claims of real-world correctness.
- Keep `ForecastContext` distinct from observations, advisory instructions, station records, remote-sensing masks, climate context, evidence proof, health guidance, life-safety guidance, and public layer release unless the fixture is explicitly testing that boundary.
- Pair inputs with expected outputs when practical.
- Do not treat a fixture as evidence, source admission, rights approval, policy approval, release state, forecast truth, official advisory output, emergency guidance, health guidance, or a published artifact.
- Update this README when forecast-context fixture payloads, validators, tests, or helper scripts are added.

## Verification status

- Target README: updated from placeholder content.
- Payload inventory: NEEDS VERIFICATION.
- Tests and validators: NOT RUN.
