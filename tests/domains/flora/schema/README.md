# Flora Schema Tests

> Test-lane README for `tests/domains/flora/schema/`.

This directory is for Flora schema tests under the `tests/` responsibility root. It should verify required fields, versions, and machine-shape conformance for Flora records by calling the canonical schema and validator code from their owning roots.

## Authority boundary

This directory is a test lane only. It is not a schema home, contract home, fixture inventory, evidence store, receipt, proof, release decision, or public artifact home.

## Directory fit

```text
tests/domains/flora/schema/
```

Directory Rules place domain-specific tests under `tests/domains/<domain>/`, with the domain as a segment inside the responsibility root.

## Expected proof

- Valid Flora fixtures pass the canonical schema.
- Invalid Flora fixtures fail for missing required fields, invalid values, invalid versions, or invalid reference shape.
- Schema shape remains separate from contract meaning.
- Schema validation does not equal evidence approval, policy approval, or release approval.
- Tests use deterministic local fixtures and do not require live network access by default.

## Suggested commands

```bash
pytest tests/domains/flora/schema
pytest tests/domains/flora
python tools/validate_all.py
```

Command names and validators are **NEEDS VERIFICATION** until checked against repository configuration.

## Open questions

| Question | Status |
|---|---|
| Which Flora schema files are canonical? | NEEDS VERIFICATION |
| Which validator owns Flora schema checks? | NEEDS VERIFICATION |
| Which fixture families already exist? | NEEDS VERIFICATION |
| Which CI job runs this lane? | NEEDS VERIFICATION |

## Definition of done

- [ ] Flora schema tests run locally.
- [ ] Valid and invalid fixture families are covered.
- [ ] Tests call canonical schemas and validators.
- [ ] CI exposes the Flora schema proof clearly enough for reviewers.
