<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-catalog-trust-extension-readme
title: Catalog Trust Extension Validator
type: validator-readme
version: v0.1.0
status: draft; deterministic; no-network; non-authoritative
owners: OWNER_TBD — Validation steward · Catalog steward · Evidence steward
created: 2026-08-08
updated: 2026-08-08
policy_label: repository-facing; catalog; validator; fixture-first; no-publication-authority
owning_root: tools/
responsibility: Document the deterministic no-network validator for the bounded catalog trust-extension payload.
truth_posture: CONFIRMED validator bytes and synthetic test evidence; PROPOSED operational adoption; cite-or-abstain
related:
  - ../../../contracts/data/catalog_trust_extension.md
  - ../../../schemas/contracts/v1/data/catalog_trust_extension.schema.json
  - ../../../fixtures/data/catalog_trust_extension/
  - ../../../tests/validators/test_validate_catalog_trust_extension.py
tags: [kfm, validator, catalog, stac, dcat, prov, source-role, proof, receipt]
[/KFM_META_BLOCK_V2] -->

# Catalog Trust Extension validator

`validate_catalog_trust_extension.py` validates only the shared KFM trust payload described by `CatalogTrustExtension`.

## Accepted scope

The validator checks:

- closed Draft 2020-12 schema conformance;
- RFC 8785 JCS plus SHA-256 `spec_hash`;
- proof-reference requirements for `proof` and `publication` trust classes;
- denial of `candidate` + `publication` collapse;
- explicit false authority flags;
- duplicate-key, non-finite-number, size, depth, node, symlink, and unreadable-input failures; and
- exact fixture-manifest polarity.

It performs no network access and never dereferences a host, receipt, or proof reference.

## Commands

```bash
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_catalog_trust_extension.py' \
  --verbose

python tools/validators/catalog_trust_extension/validate_catalog_trust_extension.py \
  --fixtures
```

## Outcome boundary

`PASS` proves only bounded shape and internal semantic consistency for the supplied payload. It does not validate the complete STAC/DCAT/PROV host, resolve evidence, close proof, apply policy, approve review, create catalog closure, promote, release, publish, or authorize public use.

## Stable findings

| Code | Meaning |
|---|---|
| `SCHEMA_INVALID` | Closed schema constraint failed. |
| `SPEC_HASH_MISMATCH` | Stored hash does not match the canonical extension payload. |
| `PROOF_REF_REQUIRED` | A proof/publication class lacks `kfm:proof_ref`. |
| `CANDIDATE_PUBLICATION_FORBIDDEN` | Candidate source role claims publication class. |
| `GOVERNANCE_BOUNDARY_VIOLATION` | One or more authority flags are not false. |
| `JSON_*`, `FILE_*`, `INPUT_*` | Input could not be inspected safely. |

Diagnostics contain codes and paths, not untrusted values.

## Rollback

Revert the additive validator lane with its paired contract, schema, fixtures, tests, workflow, and generated receipt. No external system or catalog state is mutated.
