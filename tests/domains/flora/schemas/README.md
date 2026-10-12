# Flora Schemas Tests

> Test-lane README for `tests/domains/flora/schemas/`.

This directory is for Flora schema-related tests under the `tests/` responsibility root. It should verify required fields, versions, machine-shape conformance, reference shape, and schema-family behavior by calling canonical schema and validator code from their owning roots.

## Authority boundary

This directory is a test lane only. It is not a schema home, contract home, fixture inventory, evidence store, receipt, proof, release decision, or public artifact home.

## Directory fit

```text
tests/domains/flora/schemas/
```

Directory Rules place domain-specific tests under `tests/domains/<domain>/`, with the domain as a segment inside the responsibility root.

## Relationship to `schema/`

The repository also has a singular schema-test lane path in progress:

```text
tests/domains/flora/schema/
```

Whether `schema/` and `schemas/` should both remain, or whether one should become the canonical lane and the other an alias/compatibility lane, is **NEEDS VERIFICATION**. Until resolved, this directory must not duplicate authority or create a second schema-testing standard.

## Expected proof

- Valid Flora fixtures pass the canonical schema family.
- Invalid Flora fixtures fail for missing required fields, invalid values, invalid versions, invalid references, or wrong family shape.
- Schema shape remains separate from contract meaning.
- Schema validation does not equal evidence approval, policy approval, or release approval.
- Tests use deterministic local fixtures and do not require live network access by default.

## Suggested commands

```bash
pytest tests/domains/flora/schemas
pytest tests/domains/flora
python tools/validate_all.py
```

Command names and validators are **NEEDS VERIFICATION** until checked against repository configuration.

## Open questions

| Question | Status |
|---|---|
| Is `schemas/` the canonical Flora schema test lane, or should `schema/` be canonical? | NEEDS VERIFICATION |
| Which Flora schema files are canonical? | NEEDS VERIFICATION |
| Which validator owns Flora schema checks? | NEEDS VERIFICATION |
| Which fixture families already exist? | NEEDS VERIFICATION |
| Which CI job runs this lane? | NEEDS VERIFICATION |

## Definition of done

- [ ] Flora schema-family tests run locally.
- [ ] Valid and invalid fixture families are covered.
- [ ] Tests call canonical schemas and validators.
- [ ] Relationship to `tests/domains/flora/schema/` is resolved or documented.
- [ ] CI exposes the Flora schemas proof clearly enough for reviewers.
