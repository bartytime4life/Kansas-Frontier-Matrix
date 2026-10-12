<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/contracts/v1/common/temporal-window/readme
title: TemporalWindow Fixture Profile
type: fixture-readme
version: v0.1.0
status: draft; executable; no-network
updated: 2026-08-03
policy_label: public-review; synthetic-only; non-authoritative
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# TemporalWindow Fixture Profile

Synthetic positive, schema-negative, and semantic-negative candidates for the proposed common `TemporalWindow` contract.

**Schema:** `schemas/contracts/v1/common/temporal_window.schema.json`  
**Contract:** `contracts/common/temporal_window.md`  
**Validator:** `tools/validators/validate_temporal_window.py`  
**Tests:** `tests/validators/test_validate_temporal_window.py`

> [!IMPORTANT]
> These fixtures prove only bounded shape, aware date-time syntax, parser safety, and interval ordering. They are not source evidence, policy decisions, review records, release records, or public claims.

## Inventory

| Lane | File | Reviewed boundary |
|---|---|---|
| valid | `valid/valid_1.json` | UTC observed interval with `start < end`. |
| valid | `valid/valid_2.json` | Equal instants represented with different offsets. |
| invalid | `invalid/invalid_1_missing_time_kind.json` | Required `time_kind`. |
| invalid | `invalid/invalid_2_unknown_time_kind.json` | Closed enum. |
| invalid | `invalid/invalid_3_extra_property.json` | Closed top-level object. |
| semantic invalid | `semantic_invalid/invalid_1_reversed_interval.json` | `end` cannot precede `start`. |
| semantic invalid | `semantic_invalid/invalid_2_naive_datetime.json` | Date-times must carry timezone information. |

Every negative candidate has a sibling expected-error sidecar.

## Why semantic-invalid is separate

The shared schema harness does not use a format checker and cannot compare two timestamps. The dedicated validator therefore owns:

- timezone-aware date-time enforcement;
- normalized interval ordering;
- unsafe-file and bounded-parser behavior;
- duplicate-key and finite-JSON checks;
- deterministic sidecar-matched fixture mode.

This separation avoids weakening or changing unrelated common-schema behavior.

## Commands

```bash
python tools/validators/validate_temporal_window.py --fixtures

python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_temporal_window.py' \
  --verbose

python -m pytest -q tests/schemas/test_common_contracts.py
```

## Boundaries

- The current schema enum remains `PROPOSED`.
- Proposed ADR-0014 remains unresolved and is not accepted by these fixtures.
- A valid window does not prove that a source observed, published, corrected, superseded, or released anything.
- Freshness, embargo, evidence, policy, review, correction, and release remain with their owning families.

## Rollback

Remove this fixture family and restore the placeholder validator through a reviewed revert. No production data or public state is affected.

<p align="right"><a href="#top">Back to top</a></p>
