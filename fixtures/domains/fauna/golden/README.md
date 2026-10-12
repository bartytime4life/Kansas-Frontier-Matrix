# Fauna golden fixtures

`fixtures/domains/fauna/golden/`

Status: draft / fixture lane.

This directory is for stable expected-output Fauna fixture examples used by bounded tests, validators, renderer checks, helpers, release dry-runs, or documentation examples. These files are examples only. They are not authoritative project records, source records, evidence, policy decisions, sensitivity decisions, release state, public API material, public map material, or published artifacts.

## Placement basis

Directory rules place golden, valid, and invalid sample data under the `fixtures/` responsibility root, with domain fixtures under `fixtures/domains/<domain>/`. This lane is therefore the Fauna-domain golden fixture lane, not a data lifecycle, policy, source, release, or publication root.

## Related fixture lanes

- `../README.md`
- `../valid/README.md`
- `../invalid/README.md`

## Related references

- `../../../docs/domains/fauna/OBJECT_FAMILIES.md`
- `../../../docs/domains/fauna/MISSING_OR_PLANNED_FILES.md`
- `../../../contracts/domains/fauna/`
- `../../../schemas/contracts/v1/domains/fauna/`
- `../../../policy/domains/fauna/`
- `../../../docs/doctrine/directory-rules.md`

## Accepted material

This lane may contain:

- small synthetic `*.input.json` examples
- small `*.expected.json` examples
- stable snapshots for bounded tests
- expected public-safe outputs for redaction, generalization, or denial checks
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
- Keep each golden fixture tied to a known test, validator, helper, renderer check, release dry-run, or documentation example.
- Pair inputs with expected outputs when practical.
- Keep source role, evidence, time, sensitivity, and release boundaries explicit.
- Do not treat a fixture as evidence, approval, release state, or a published artifact.
- Update this README when payload files, validators, tests, or helper scripts are added.

## Verification status

- Target README: updated from one-character placeholder content.
- Payload inventory: NEEDS VERIFICATION.
- Tests and validators: NOT RUN.
