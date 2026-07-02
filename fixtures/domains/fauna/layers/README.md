# Fauna layer fixtures

`fixtures/domains/fauna/layers/`

Status: draft / fixture lane.

This directory is for small layer-shaped Fauna fixture examples used by bounded tests, validators, renderer checks, helpers, release dry-runs, or documentation examples. These files are examples only. They are not authoritative project records, source records, evidence, policy decisions, sensitivity decisions, layer registry entries, release state, public API material, public map material, public tiles, or published artifacts.

## Placement basis

Directory rules place golden, valid, and invalid sample data under the `fixtures/` responsibility root, with domain fixtures under `fixtures/domains/<domain>/`. This lane is therefore a Fauna fixture lane for layer-shaped examples. Published layer artifacts belong under `data/published/layers/fauna/`, and release decisions belong under `release/`.

## Related fixture lanes

- `../README.md`
- `../golden/README.md`
- `../invalid/README.md`
- `../valid/README.md`

## Related references

- `../../../../docs/domains/fauna/MAP_UI_CONTRACTS.md`
- `../../../../docs/domains/fauna/OBJECT_FAMILIES.md`
- `../../../../docs/domains/fauna/MISSING_OR_PLANNED_FILES.md`
- `../../../../contracts/domains/fauna/`
- `../../../../schemas/contracts/v1/domains/fauna/`
- `../../../../policy/domains/fauna/`
- `../../../../data/published/layers/fauna/`
- `../../../../docs/doctrine/directory-rules.md`

## Accepted material

This lane may contain:

- small synthetic layer descriptor or layer-manifest-shaped examples
- small expected renderer payloads for bounded tests
- public-safe redaction, generalization, denial, or abstention examples
- examples for trust-visible layer states, freshness states, or policy-gated rendering
- README files explaining fixture intent and boundaries

## Exclusions

Do not use this lane for:

- authoritative taxon, occurrence, monitoring, mortality, disease, invasive-species, or sensitive-site records
- source-system exports or live upstream fetch results
- EvidenceBundles, proof packs, receipts, or release manifests
- policy rules, policy decisions, sensitivity approvals, or rights approvals
- exact sensitive locations or reconstructive geoprivacy clues
- connector, pipeline, validator, package, or schema implementation code
- layer registry entries, public API material, public map material, public tiles, or published artifacts

## Maintenance notes

- Keep examples synthetic, compact, deterministic, and reviewable.
- Keep each layer fixture tied to a known test, validator, helper, renderer check, release dry-run, or documentation example.
- Keep source role, evidence, time, sensitivity, rights, geoprivacy, release, and renderer boundaries explicit.
- Pair inputs with expected outputs, expected denials, expected abstentions, or safe fallback outputs when practical.
- Do not treat a fixture as evidence, approval, release state, or a published artifact.
- Update this README when payload files, validators, tests, or helper scripts are added.

## Verification status

- Target README: updated from one-character placeholder content.
- Payload inventory: NEEDS VERIFICATION.
- Tests and validators: NOT RUN.
