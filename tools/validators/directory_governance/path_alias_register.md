# Path Alias Register Validator

`validate_path_alias_register.py` deterministically validates `control_plane/path_alias_register.yaml` against:

- the Draft 2020-12 Path Alias Register schema;
- the adopted Directory Rules v2 SHA-256 and `ADR-0029`;
- the exact Root Registry digest and registry base;
- compatibility-class, dual-read/single-write, root, identity, exposure, mutation, expiry, parity, and rollback invariants;
- repository path, legacy Git blob, and canonical-content parity when repository checks are enabled.

## Commands

```bash
python tools/validators/directory_governance/validate_path_alias_register.py --fixtures
python tools/validators/directory_governance/validate_path_alias_register.py
python -m unittest discover \
  --start-directory tests/validators/directory_governance \
  --pattern 'test_validate_path_alias_register.py' \
  --verbose
```

For bounded synthetic/local testing, repository and exact Root Registry byte checks may be disabled explicitly:

```bash
python tools/validators/directory_governance/validate_path_alias_register.py \
  --skip-repository \
  --skip-projection-binding
```

Those flags are test aids. The hosted workflow validates the current register without either bypass.

## Outcomes

- `PASS` — no applicable inconsistency.
- `FAIL_NEW_DRIFT` — an alias expired or a required old/canonical path or registered root is absent.
- `FAIL_INVARIANT` — shape-compatible input violates alias, identity, root, class, permission, parity, or rollback invariants.
- `HOLD_UNRESOLVED` — accepted-decision or consumer evidence is unresolved.
- `ERROR_VALIDATOR` — input, parser, schema, Root Registry, or repository-root evaluation failed safely.

## Boundary

A green result is bounded conformance evidence. It does not accept an ADR, authorize an alias or legacy write, close consumers, create a tombstone, perform a migration, retire or delete a path, or release/deploy/promote/publish anything.
