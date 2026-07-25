# Fauna invalid fixtures

`fixtures/domains/fauna/invalid/`

Status: draft fixture lane with four accepted bounded negative fixtures.

This directory is for negative Fauna fixture examples used by bounded tests, validators, renderer checks, helpers, release dry-runs, or documentation examples. These files are examples only. They are not authoritative project records, source records, evidence, policy decisions, sensitivity decisions, release state, public API material, public map material, or published artifacts.

## Placement basis

Directory rules place golden, valid, and invalid sample data under the `fixtures/` responsibility root, with domain fixtures under `fixtures/domains/<domain>/`. This lane is therefore the Fauna-domain invalid fixture lane, not a data lifecycle, policy, source, release, or publication root.

## Related fixture lanes

- `../README.md`
- `../golden/README.md`
- `../valid/README.md`

## Related references

- `../../../../docs/domains/fauna/OBJECT_FAMILIES.md`
- `../../../../docs/domains/fauna/MISSING_OR_PLANNED_FILES.md`
- `../../../../contracts/domains/fauna/`
- `../../../../schemas/contracts/v1/domains/fauna/`
- `../../../../policy/domains/fauna/`
- `../../../../docs/doctrine/directory-rules.md`
- `../../../../tools/validators/domains/fauna/validate_public_safe_fixture.py`
- `../../../../tests/domains/fauna/test_fauna_smoke.py`
- `../../../../.github/workflows/domain-fauna.yml`

## Accepted bounded payloads

| File | Expected deterministic findings |
|---|---|
| `missing_source_descriptor.json` | Missing synthetic source descriptor reference. |
| `unresolved_governance.json` | Unresolved evidence, rights, policy, geoprivacy, review, correction, and rollback states. Release remains not released and promotion remains ineligible. |
| `unresolved_taxonomy.json` | Unresolved synthetic taxonomy state. |
| `over_precise_sensitive.json` | Unresolved sensitivity, unsafe spatial kind, and non-numeric `SYNTHETIC-ONLY` location-shaped fields. No real location is present. |

Acceptance applies only to the synthetic fixture-safety validator. These files do not execute policy, model an actual species occurrence, or establish a release, promotion, correction, rollback, or publication path.

## Accepted material

This lane may contain:

- small synthetic invalid `*.input.json` examples
- expected error text or expected validation diagnostics
- examples for expected denial, abstention, quarantine, or safe fallback behavior
- negative cases for identity, source role, evidence, time, sensitivity, rights, geoprivacy, or release boundaries
- README files explaining fixture intent and boundaries

## Exclusions

Do not use this lane for:

- authoritative taxon, occurrence, monitoring, mortality, disease, invasive-species, or sensitive-site records
- source-system exports or live upstream fetch results
- EvidenceBundles, proof packs, receipts, or release manifests
- policy rules, policy decisions, sensitivity approvals, or rights approvals
- exact sensitive locations or reconstructive geoprivacy clues
- connector, pipeline, validator, package, or schema implementation code
- public API material, public map material, public tiles, or published artifacts

## Maintenance notes

- Keep examples synthetic, compact, deterministic, and reviewable.
- Keep each invalid fixture tied to a known test, validator, helper, renderer check, release dry-run, or documentation example.
- Pair invalid inputs with expected errors, expected denials, expected abstentions, quarantine decisions, or safe fallback outputs when practical.
- Keep source role, evidence, time, sensitivity, rights, geoprivacy, and release boundaries explicit.
- Do not treat a fixture as evidence, approval, release state, or a published artifact.
- Update this README when payload files, validators, tests, or helper scripts are added.

## Verification status

- Target README: updated from one-character placeholder content.
- Payload inventory: PARTIALLY VERIFIED — the four JSON fixtures above are accepted only for the bounded fixture-safety slice; other lane maturity remains NEEDS VERIFICATION.
- Consumer alignment: CONFIRMED only for `validate_public_safe_fixture.py`, `test_fauna_smoke.py`, and `validate-fauna`.
- Tests and validator: the accepted five-test standard-library suite passed locally on 2026-07-25; CI execution remains subject to the focused pull request.
