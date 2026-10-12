# Valid air-observation fixtures

`fixtures/domains/atmosphere/valid/air-observation/`

Status: draft / nested fixture lane.

This directory is for positive `AirObservation` fixture examples used by bounded tests, validators, no-network checks, helpers, or documentation examples. These files are examples only and are not authoritative observation records.

## Scope

Use this lane for compact synthetic air-observation cases that are expected to pass a specific check while preserving KFM's observation boundary. A valid `AirObservation` fixture may represent a governed general air-quality observation tied to station, source, observed time, retrieval time, units, QA posture, and source-role context required by the test.

A valid fixture here does not prove the represented air value is true in the real world and does not authorize publication, health guidance, regulatory claims, exposure claims, or release of controlled Atmosphere/Air products.

## Expected passes

Examples may include payloads that demonstrate:

- station or network context is present when required
- source identity and source role are explicit
- observed time, retrieved time, units, and QA posture are represented when required
- freshness, rights, caveat, or low-cost-sensor fields are present when the test requires them
- `AirObservation` remains distinct from PM2.5, ozone, AQI, model output, smoke context, and advisory context
- evidence references close within the fixture-only test boundary when required
- safe-render or release dry-run behavior is demonstrated without promoting anything to `data/published/`

## Related fixture lanes

- `../README.md`
- `../../invalid/air-observation/README.md`
- `../../golden/README.md`
- `../../invalid/README.md`
- `../../objects/README.md`
- `../../sources/README.md`

## Related references

- `../../../../../contracts/domains/atmosphere/AirObservation.md`
- `../../../../../contracts/domains/atmosphere/air-observation.md`
- `../../../../../docs/runbooks/atmosphere/NO_NETWORK_TEST_RUNBOOK.md`
- `../../../../../docs/domains/atmosphere/OBJECT_FAMILY_MAP.md`
- `../../../../../docs/domains/atmosphere/POLICY.md`
- `../../../../../schemas/contracts/v1/domains/atmosphere/AirObservation.schema.json`
- `../../../../../docs/doctrine/directory-rules.md`

## Maintenance notes

- Keep examples synthetic, compact, deterministic, and reviewable.
- Keep each valid fixture tied to a known test, validator, no-network check, helper, or documentation example.
- Record what the fixture is expected to pass; avoid broad claims of real-world correctness.
- Keep `AirObservation` distinct from pollutant-specific observations, AQI reports, model fields, smoke/AOD context, advisory context, health guidance, and regulatory proof unless the fixture is explicitly testing that boundary.
- Pair inputs with expected outputs when practical.
- Do not treat a fixture as evidence, source admission, rights approval, policy approval, release state, health guidance, regulatory proof, live advisory output, or a published artifact.
- Update this README when air-observation fixture payloads, validators, tests, or helper scripts are added.

## Verification status

- Target README: updated from placeholder content.
- Payload inventory: NEEDS VERIFICATION.
- Tests and validators: NOT RUN.
