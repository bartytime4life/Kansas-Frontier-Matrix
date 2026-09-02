<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/fixtures-data-catalog-trust-extension
title: Catalog Trust Extension Fixtures
type: fixture-readme
version: v0.1.0
status: synthetic; no-network; non-release
owners: OWNER_TBD — Fixture steward · Catalog steward · Validation steward
created: 2026-08-08
updated: 2026-08-08
policy_label: public-safe-synthetic; catalog; stac; dcat; prov
owning_root: fixtures/
responsibility: Document the synthetic positive and negative fixture corpus for CatalogTrustExtension validation.
truth_posture: CONFIRMED synthetic fixture inventory; PROPOSED adoption; no live-source evidence
related:
  - ../../../contracts/data/catalog_trust_extension.md
  - ../../../schemas/contracts/v1/data/catalog_trust_extension.schema.json
  - ../../../tools/validators/catalog_trust_extension/validate_catalog_trust_extension.py
  - ../../../tests/validators/test_validate_catalog_trust_extension.py
tags: [kfm, fixtures, catalog, trust-extension, negative-tests]
[/KFM_META_BLOCK_V2] -->

# Catalog Trust Extension fixtures

This lane contains synthetic fixtures for the bounded `CatalogTrustExtension` payload.

## Inventory

Valid fixtures cover:

- a STAC Item carrying receipt-class synthetic source context;
- a DCAT Distribution carrying catalog-class aggregate context;
- a PROV Activity carrying proof-class modeled context; and
- a publication-class STAC descriptor whose authority flags remain false.

Invalid fixtures prove fail-closed behavior for:

- proof/publication class without a proof reference;
- candidate source role claiming publication class;
- any self-authorizing governance flag;
- mismatched `spec_hash`;
- noncanonical source role;
- missing run-receipt reference; and
- unknown fields in the closed schema.

`expected_findings_manifest.json` is the canonical fixture inventory and exact outcome/finding oracle.

## Safety boundary

All identifiers are synthetic `fixture:` or `catalog-trust-extension:` values. The fixtures contain no live endpoint, real source payload, place, person, precise coordinate, release record, credential, or public artifact.

A valid fixture proves only the declared contract/schema/validator relationship. It does not validate a host catalog record, create evidence or proof, apply policy, approve review, release, or publish.
