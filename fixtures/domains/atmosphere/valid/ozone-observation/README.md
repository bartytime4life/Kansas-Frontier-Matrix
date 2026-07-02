# Valid ozone-observation fixtures

`fixtures/domains/atmosphere/valid/ozone-observation/`

Status: draft / nested fixture lane.

This directory is for positive `OzoneObservation` fixture examples used by bounded tests, validators, no-network checks, helpers, or documentation examples. These files are examples only and are not authoritative ozone records.

## Scope

Use this lane for compact synthetic ozone-specific air-quality cases that are expected to pass a specific check while preserving KFM's ozone-observation boundary. A valid `OzoneObservation` fixture may represent governed ozone value identity, station context, source role, observed time, retrieval time, valid time, units, QA posture, freshness, caveats, evidence references, or release dry-run fields required by the test.

A valid fixture here does not prove real-world ozone concentration, AQI status, regulatory exceedance, exposure, health effect, advisory status, source-rights clearance, public release, or policy approval.

## Expected passes

Examples may include payloads that demonstrate:

- station or network context is present when required
- source identity and source role are explicit, including whether the case is concentration, public AQI/report, or archive-like context
- observed time, retrieved time, valid time, units, QA posture, freshness, and caveats are represented when required
- ozone remains distinct from generic `AirObservation`, PM2.5, AQI-only reports, model fields, AOD rasters, smoke context, and advisory context
- evidence references close within the fixture-only test boundary when required
- safe-render or release dry-run behavior is demonstrated without promoting anything to `data/published/`

## Related fixture lanes

- `../README.md`
- `../air-observation/README.md`
- `../../golden/README.md`
- `../../invalid/README.md`
- `../../objects/README.md`
- `../../sources/README.md`

## Related references

- `../../../../../contracts/domains/atmosphere/OzoneObservation.md`
- `../../../../../contracts/domains/atmosphere/AirObservation.md`
- `../../../../../contracts/domains/atmosphere/AirStation.md`
- `../../../../../contracts/domains/atmosphere/PM25Observation.md`
- `../../../../../docs/runbooks/atmosphere/NO_NETWORK_TEST_RUNBOOK.md`
- `../../../../../docs/domains/atmosphere/OBJECT_FAMILY_MAP.md`
- `../../../../../docs/domains/atmosphere/POLICY.md`
- `../../../../../schemas/contracts/v1/domains/atmosphere/OzoneObservation.schema.json`
- `../../../../../docs/doctrine/directory-rules.md`

## Maintenance notes

- Keep examples synthetic, compact, deterministic, and reviewable.
- Keep each valid fixture tied to a known test, validator, no-network check, helper, or documentation example.
- Record what the fixture is expected to pass; avoid broad claims of real-world correctness.
- Keep `OzoneObservation` distinct from generic air observations, PM2.5, AQI-only reports, model fields, remote-sensing masks, smoke context, advisory context, regulatory proof, health guidance, and public layer release unless the fixture is explicitly testing that boundary.
- Pair inputs with expected outputs when practical.
- Do not treat a fixture as evidence, source admission, rights approval, policy approval, release state, ozone truth, regulatory proof, exposure proof, health guidance, advisory output, or a published artifact.
- Update this README when ozone-observation fixture payloads, validators, tests, or helper scripts are added.

## Verification status

- Target README: updated from placeholder content.
- Payload inventory: NEEDS VERIFICATION.
- Tests and validators: NOT RUN.
