# Atmosphere source fixtures

`fixtures/domains/atmosphere/sources/`

Status: draft / fixture lane.

This directory is for source-shaped Atmosphere fixture examples used by bounded tests, validators, no-network checks, helpers, or documentation examples. These files are examples only and are not authoritative source records.

## Scope

Use this lane for compact synthetic source fixtures that exercise source-role, rights, sensitivity, freshness, evidence-closure, and admission behavior without reaching live upstream systems.

Examples may model source-family or `SourceDescriptor`-like cases for:

- OpenAQ-like aggregators
- EPA AQS-like archives
- AirNow or agency reporting
- CAMS / ECMWF-family model fields
- HRRR-Smoke or NOAA smoke forecasts
- HMS smoke products
- GOES / ABI AOD products
- VIIRS fire or hotspot products
- weather, climate, forecast, or advisory-context source cases when needed by tests

## Boundary

This fixture lane is not the source registry. Authoritative source descriptor routing and admission-control records belong under:

```text
data/registry/sources/atmosphere/
```

Fixtures here may imitate source records for tests, but they do not admit a source, prove rights, decide sensitivity, close evidence, authorize a connector, publish a layer, or provide live advisory output.

## Related fixture lanes

- `../bundles/README.md`
- `../golden/README.md`
- `../invalid/README.md`
- `../objects/README.md`

## Related references

- `../../../../docs/domains/atmosphere/SOURCES.md`
- `../../../../docs/domains/atmosphere/SOURCE_FAMILIES.md`
- `../../../../data/registry/sources/atmosphere/README.md`
- `../../../../docs/runbooks/atmosphere/NO_NETWORK_TEST_RUNBOOK.md`
- `../../../../schemas/contracts/v1/source/`
- `../../../../docs/doctrine/directory-rules.md`

## Maintenance notes

- Keep examples synthetic, compact, deterministic, and reviewable.
- Keep each source fixture tied to a known test, validator, no-network check, helper, or documentation example.
- Keep source role fixed in each example; do not let promotion or downstream transformation silently upgrade source authority.
- Pair inputs with expected outputs, expected errors, expected denials, expected abstentions, or expected safe fallbacks when practical.
- Do not treat a fixture as evidence, source admission, rights approval, sensitivity approval, release state, connector authorization, live advisory output, or a published artifact.
- Update this README when source fixture payloads, validators, tests, or helper scripts are added.

## Verification status

- Target README: updated from placeholder content.
- Payload inventory: NEEDS VERIFICATION.
- Tests and validators: NOT RUN.
