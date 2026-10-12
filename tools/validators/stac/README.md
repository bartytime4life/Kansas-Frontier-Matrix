<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-stac-readme
title: STAC Validator Family
type: readme
version: v0.1.0
status: draft; fixture-first; no-network; non-authoritative
owners:
  - OWNER_TBD - Validation steward
  - OWNER_TBD - Catalog steward
created: 2026-08-08
updated: 2026-08-08
policy_label: public; tooling; validation; stac; non-release
owning_root: tools/
responsibility: Document the bounded executable validators for KFM STAC projections without creating catalog, evidence, policy, review, release, or publication authority.
truth_posture: CONFIRMED validator and fixture paths in this packet; PROPOSED profile semantics; NEEDS VERIFICATION external STAC conformance and steward review
related:
  - ../../../docs/standards/STAC_KFM_TRUST_EXTENSION.md
  - ../../../schemas/contracts/v1/stac/kfm-profile-v1.schema.json
  - ../../../fixtures/contracts/v1/stac/kfm-profile-v1/
  - ../../../tests/validators/test_validate_kfm_stac_profile.py
tags: [kfm, tools, validators, stac, catalog, fixture-first]
[/KFM_META_BLOCK_V2] -->

# STAC validators

`tools/validators/stac/` owns repository-wide executable checks for KFM STAC projections. It does not own semantic contracts, schemas, policy decisions, catalog records, evidence, proofs, releases, or published artifacts.

## `validate_kfm_profile_v1.py`

The validator provides deterministic, no-network checks for the proposed KFM STAC trust extension:

```bash
python tools/validators/stac/validate_kfm_profile_v1.py --fixtures
python tools/validators/stac/validate_kfm_profile_v1.py path/to/item.json
```

Finite outcomes are:

| Outcome | Meaning |
|---|---|
| `PASS` | The candidate satisfies the draft schema and bounded semantic checks. |
| `FAIL` | The candidate is readable but violates schema or semantic rules. |
| `ERROR` | The candidate, schema, or hashing dependency could not be evaluated safely. |

Diagnostics contain only stable reason codes and JSON pointers. They do not echo candidate values. A `PASS` grants no source admission, evidence closure, policy approval, review, promotion, release, publication, or public-use authority.

## Validation surface

- Draft 2020-12 schema validation;
- exact RFC 8785 JCS plus SHA-256 `kfm:spec_hash`;
- trust-class dependency closure;
- receipt/proof/release role separation;
- catalog/release/publication state consistency;
- canonical reason codes, extension identifiers, and KFM links;
- matching link relations for non-null KFM references; and
- fixture-manifest replay with exact findings.

The validator intentionally does not perform network resolution or authenticate referenced receipts, proofs, evidence bundles, reviews, or releases.
