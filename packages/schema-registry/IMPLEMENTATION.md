# Schema registry implementation slice

**Status:** PARTIAL implementation, fixture-first and no-network.
**Authority:** helper mechanics only; canonical machine shape remains under `schemas/contracts/v1/`.

This slice replaces the `core.py` placeholder with a read-only local registry builder. It:

- requires an explicit local schema root;
- indexes `*.schema.json` in deterministic order;
- preserves current validator compatibility by visibly skipping schemas without `$id`;
- rejects duplicate `$id`, duplicate JSON keys, non-finite numbers, malformed roots, symlinks, path escape, and bounded resource-limit violations;
- records exact file SHA-256 values and a deterministic registry snapshot digest;
- exposes typed lookup outcomes and a conversion to `referencing.Registry`;
- performs no network access and writes no schemas, receipts, proofs, policy, release, or lifecycle state.

The package does **not** yet replace `tools/validators/_common/local_resolver.py`. A separate parity PR must prove equal identifier and document resolution over the current canonical schema tree before any consumer migration.

## Focused validation

```bash
python -m pip install -e "./packages/schema-registry[test]"
python -m pytest -q tests/packages/schema_registry
kfm-schema-registry fixtures/packages/schema-registry/valid --pretty
```

## Rollback

Revert the package implementation commit. No canonical schema, source activation, lifecycle data, public route, release object, or published artifact is changed by this slice.
