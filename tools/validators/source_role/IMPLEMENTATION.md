# Source-role anti-collapse validator implementation

**Status:** `PROPOSED_INACTIVE` · fixture-first · no-network · non-authoritative

The executable implementation for this validator lane is now:

```text
tools/validators/source_role/source_role_core.py
tools/validators/source_role/source_role_rules.py
tools/validators/source_role/validate_source_role.py
```

The former plural placeholder remains only as a compatibility shim:

```text
tools/validators/sources/validate_source_role.py
```

It imports and runs the canonical entrypoint. It does not define a second schema, vocabulary, or outcome grammar.

## Bound schema inputs

- `schemas/contracts/v1/source/source_descriptor.schema.json` — admitted source posture and active source-role, authority-rank, and claim-role vocabularies;
- `schemas/contracts/v1/source/source_role_use_request.schema.json` — bounded downstream-use request.

## Outcomes

`PASS=0`, `ERROR=2`, `HOLD=3`, `RESTRICT=4`, `ABSTAIN=5`, `DENY=6`.

Outcome precedence is `ERROR > DENY > HOLD > RESTRICT > ABSTAIN > PASS`.

A `PASS` proves only that the supplied descriptor snapshot and downstream-use request are internally compatible under this profile. It creates no source role, evidence, policy decision, review approval, source activation, release, publication, or public permission.

## Commands

```bash
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python -m pytest -q tests/validators/test_validate_source_role.py

PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tools/validators/source_role/validate_source_role.py --fixtures

PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tools/validators/sources/validate_source_role.py --fixtures
```

## Non-effects

The implementation does not read live endpoints, mutate source descriptors or registries, activate connectors, create EvidenceBundles, decide rights or sensitivity, approve review, promote, release, publish, or expose source data.
