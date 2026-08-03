<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/contracts/v1/common/readme
title: fixtures/contracts/v1/common/ — Common Contract Fixture Family Index
type: readme; fixture-index; non-authoritative
version: v0.3.0
status: draft; repository-grounded; partial-coverage
owners: OWNER_TBD — Schema steward · Common-contract steward · Fixture steward · Validator steward · Test/QA steward · Docs steward
updated: 2026-08-03
policy_label: public-review; fixtures; common-contracts; synthetic-only
owning_root: fixtures/
notes:
  - "v0.3.0 adds the bounded TemporalWindow fixture and validator profile."
  - "IdentityToken and SpatialGeometry coverage remain unresolved."
  - "Fixture success proves tested shape or bounded semantics only, never evidence, policy, review, release, or publication."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

<!-- Legacy v0.2 fragment anchors retained for inbound compatibility. -->
<a id="status-and-evidence-boundary"></a>
<a id="scope-and-audience"></a>
<a id="placement-and-authority"></a>
<a id="current-coverage-matrix"></a>
<a id="executable-harness-and-coverage-boundary"></a>
<a id="fixture-family-layout"></a>
<a id="fixture-outcome-language"></a>
<a id="no-network-rights-and-sensitivity-posture"></a>
<a id="validation"></a>
<a id="maintenance-and-change-discipline"></a>
<a id="open-verification-register"></a>
<a id="evidence-ledger"></a>
<a id="correction-and-rollback"></a>

# Common Contract Fixture Family Index

`fixtures/contracts/v1/common/`

> Synthetic, deterministic positive and negative cases for shared KFM contract schemas. Fixtures prove only the reviewed validation boundary; they do not create semantic, evidence, policy, review, lifecycle, release, or publication authority.

## Placement

| Responsibility | Home |
|---|---|
| Shared semantic meaning | `contracts/common/` |
| Shared machine shape | `schemas/contracts/v1/common/` |
| Synthetic validation candidates | `fixtures/contracts/v1/common/` |
| Executable validators | `tools/validators/` |
| Tests | `tests/schemas/` and `tests/validators/` |
| Admissibility and exposure | `policy/`, evidence, review, and release roots |

The family path follows the existing `fixtures/` responsibility root. It does not create a new root or a parallel schema home.

## Current coverage

| Object | Contract/schema | Fixture posture | Validator posture |
|---|---|---|---|
| `spec_hash` | Present, proposed profile | Populated positive/negative family | Placeholder remains outside this slice |
| `identity_token` | Present, proposed profile | NEEDS VERIFICATION | Declared implementation not verified |
| `temporal_window` | Present, proposed profile | **Implemented:** 2 valid, 3 schema-invalid, 2 semantic-invalid | **Implemented bounded no-network validator** |
| `spatial_geometry` | Present, proposed profile | NEEDS VERIFICATION | Placeholder remains outside this slice |

See [`temporal_window/README.md`](temporal_window/README.md) for exact cases and boundaries.

## Discovery boundary

`tests/schemas/test_common_contracts.py` discovers a common schema only when a matching fixture directory exists. The generic test:

- checks `valid/valid_*.json`;
- checks `invalid/invalid_*.json`;
- optionally matches expected-error sidecars;
- does not exercise `semantic_invalid/`;
- does not use a format checker in the shared runner;
- does not establish complete schema-tree coverage.

The dedicated TemporalWindow validator closes the reviewed format and ordering gaps without changing the generic harness for unrelated families.

## Family layout

```text
<schema_name>/
├── README.md
├── valid/
│   ├── README.md
│   └── valid_<n>.json
├── invalid/
│   ├── README.md
│   ├── invalid_<n>.json
│   └── invalid_<n>.expected_error.txt
└── semantic_invalid/          # only when a dedicated validator owns extra checks
    ├── README.md
    ├── invalid_<n>.json
    └── invalid_<n>.expected_error.txt
```

## Outcome language

| Outcome | Meaning |
|---|---|
| `PASS` | A valid fixture passed the declared bounded checks. |
| `EXPECTED_REJECTION` | An invalid fixture failed and matched reviewed sidecar evidence. |
| `FIXTURE_POLARITY_ERROR` | A reviewed invalid fixture passed. |
| `EXPECTED_REJECTION_MISMATCH` | Failure occurred for an unreviewed or different reason. |
| `HARNESS_ERROR` | Schema, parser, dependency, or fixture setup failed. |

Missing files, placeholder crashes, or arbitrary nonzero exits are never accepted as expected rejection.

## Safety

Fixtures must be compact, synthetic, deterministic, public-safe, and no-network. Do not place production payloads, credentials, living-person data, DNA, private land records, exact sensitive geometry, source-system secrets, EvidenceBundles, release records, or published artifacts here.

## Commands

```bash
python -m pytest -q tests/schemas/test_common_contracts.py

python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_temporal_window.py' \
  --verbose

python tools/validators/validate_temporal_window.py --fixtures
```

## Remaining gaps

- IdentityToken fixture and validator closure.
- SpatialGeometry fixture and validator closure.
- Dedicated SpecHash validator implementation.
- Full common-schema presence/non-vacuity enforcement.
- Dedicated workflow coverage is added for TemporalWindow; production-consumer and policy integration remain unresolved.
- Steward and CODEOWNERS verification.

## Correction and rollback

Update this index whenever a common schema, contract, fixture family, validator, or discovery rule changes. Rollback of the TemporalWindow slice removes its child family and restores this index to prior blob `9ec92d1daa7521d9b0adf1e529a61f5146471164`.

<p align="right"><a href="#top">Back to top</a></p>
