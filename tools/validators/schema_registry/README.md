# Schema registry parity validator

**Status:** implementation validator; read-only, deterministic, and no-network.
**Owning root:** `tools/validators/` — repository validation mechanics.
**Package under test:** `packages/schema-registry/`.
**Current comparison target:** `tools/validators/_common/local_resolver.py`.

The validator builds both registry implementations over `schemas/contracts/v1/` and compares:

- the complete sorted `$id` set;
- decoded schema content for every shared `$id` using deterministic SHA-256 digests;
- the number of schema files intentionally skipped because they have no `$id`.

A passing report proves local identifier/content parity only. It does not accept schemas, migrate consumers, establish contract meaning, decide policy, resolve evidence, approve release, or publish anything.

```bash
python tools/validators/schema_registry/validate_schema_registry_parity.py --pretty
python -m pytest -q tests/validators/schema_registry
```

## Finite outcomes

| Outcome | Meaning |
| --- | --- |
| `PASS` | Both implementations expose the same `$id` set and decoded content. |
| `ERROR` | A registry failed to build, an id exists on only one side, or decoded content differs. |

Schemas without `$id` remain visible as `skipped_missing_id_count` and do not fail parity because the existing resolver intentionally skips them. Admission policy for those files remains a separate governance concern.

## Rollback

Revert this validator, its focused tests, workflow, and receipt. The package and the existing resolver remain unchanged; no schema or consumer migration is performed by this slice.
