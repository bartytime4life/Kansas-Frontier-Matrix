# Atmosphere valid fixtures

`fixtures/domains/atmosphere/valid/`

Status: draft / fixture lane.

This directory is for positive Atmosphere fixture examples used by bounded tests, validators, no-network checks, helpers, or documentation examples. These files are examples only and are not authoritative project records.

## Scope

Use this lane for compact synthetic cases that are expected to pass a specific check. A valid fixture may prove that an example satisfies a schema, validator, source-role rule, policy helper, evidence-closure check, release dry-run check, finite-outcome envelope, renderer check, or documentation example.

A valid fixture does not prove that the represented source, object, observation, station, model field, advisory context, rights posture, or release state is true in the real world.

## Expected passes

Examples may include:

- object-shaped payloads that preserve Atmosphere object-family boundaries
- source-shaped payloads with fixed source role, freshness, rights, and caveat fields required by the test
- bundle-shaped payloads that close the expected fixture-only evidence references
- safe-render payloads that avoid live advisory output, health guidance, or unsupported public claims
- release dry-run examples that demonstrate gating behavior without promoting anything to `data/published/`

## Related fixture lanes

- `../bundles/README.md`
- `../golden/README.md`
- `../invalid/README.md`
- `../objects/README.md`
- `../sources/README.md`

## Related references

- `../../../../docs/runbooks/atmosphere/NO_NETWORK_TEST_RUNBOOK.md`
- `../../../../docs/domains/atmosphere/OBJECT_FAMILY_MAP.md`
- `../../../../docs/domains/atmosphere/SOURCES.md`
- `../../../../docs/domains/atmosphere/MISSING_OR_PLANNED_FILES.md`
- `../../../../contracts/domains/atmosphere/`
- `../../../../schemas/contracts/v1/domains/atmosphere/`
- `../../../../docs/doctrine/directory-rules.md`

## Maintenance notes

- Keep examples synthetic, compact, deterministic, and reviewable.
- Keep each valid fixture tied to a known test, validator, no-network check, helper, or documentation example.
- Record what the fixture is expected to pass; avoid broad claims of real-world correctness.
- Pair inputs with expected outputs when practical.
- Do not treat a fixture as evidence, source admission, rights approval, sensitivity approval, release state, health guidance, live advisory output, or a published artifact.
- Update this README when valid payloads, validators, tests, or helper scripts are added.

## Verification status

- Target README: updated from placeholder content.
- Payload inventory: NEEDS VERIFICATION.
- Tests and validators: NOT RUN.
