# Valid advisory-context fixtures

`fixtures/domains/atmosphere/valid/advisory-context/`

Status: draft / nested fixture lane.

This directory is for positive `AdvisoryContext` fixture examples used by bounded tests, validators, no-network checks, helpers, or documentation examples. These files are examples only and are not authoritative advisory records.

## Scope

Use this lane for compact synthetic advisory-context cases that are expected to pass a specific check while preserving KFM's advisory boundary. A valid `AdvisoryContext` fixture may represent a governed referral to an authoritative advisory, alert, bulletin, watch, warning, statement, notice, or public-information product.

A valid fixture here does not make KFM the advisory issuer and does not provide emergency response guidance, health guidance, evacuation guidance, operational direction, or live alerting.

## Expected passes

Examples may include payloads that demonstrate:

- source identity and advisory source role are explicit
- valid time, retrieval time, expiration, supersession, or withdrawal fields are represented when required by the test
- advisory text is summarized or referenced without replacing the authoritative source
- official-source redirection is present when required
- related atmosphere objects remain contextual and do not become advisory instructions
- stale, transformed, or rights-limited advisory material is handled through expected safe display, abstention, or release-gate behavior
- release dry-run behavior is demonstrated without promoting anything to `data/published/`

## Related fixture lanes

- `../README.md`
- `../../golden/README.md`
- `../../invalid/README.md`
- `../../objects/README.md`
- `../../sources/README.md`

## Related references

- `../../../../../contracts/domains/atmosphere/AdvisoryContext.md`
- `../../../../../docs/runbooks/atmosphere/NO_NETWORK_TEST_RUNBOOK.md`
- `../../../../../docs/domains/atmosphere/OBJECT_FAMILY_MAP.md`
- `../../../../../docs/domains/atmosphere/POLICY.md`
- `../../../../../schemas/contracts/v1/domains/atmosphere/AdvisoryContext.schema.json`
- `../../../../../docs/doctrine/directory-rules.md`

## Maintenance notes

- Keep examples synthetic, compact, deterministic, and reviewable.
- Keep each valid fixture tied to a known test, validator, no-network check, helper, or documentation example.
- Record what the fixture is expected to pass; avoid broad claims of real-world correctness.
- Keep advisory context distinct from forecast fields, observations, concentration measurements, smoke context, hazard proof, health guidance, and official alert issuance.
- Pair inputs with expected outputs when practical.
- Do not treat a fixture as evidence, source admission, rights approval, policy approval, release state, emergency guidance, health guidance, live advisory output, or a published artifact.
- Update this README when advisory-context fixture payloads, validators, tests, or helper scripts are added.

## Verification status

- Target README: updated from placeholder content.
- Payload inventory: NEEDS VERIFICATION.
- Tests and validators: NOT RUN.
