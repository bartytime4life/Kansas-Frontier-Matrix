<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/common/elapsed-time-unit-disclosure
title: ElapsedTimeUnitDisclosureCandidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; no-network; non-authoritative
owners: OWNER_TBD — Common contract steward · Analytics steward · Query steward · Validation steward
created: 2026-08-11
updated: 2026-08-11
owning_root: contracts/
policy_label: internal; common; temporal; metric; units; disclosure
responsibility: Define fixture-only timestamp-difference unit, conversion, timezone, boundary, rounding, null, and sign declarations without executing a query or creating metric, evidence, policy, review, release, or publication authority.
truth_posture: "CONFIRMED supplied-card traceability and bounded repository gap; PROPOSED inactive disclosure; UNKNOWN runtime adoption; NEEDS VERIFICATION engine and timezone behavior, human review, and hosted exact-head CI"
related:
  - ./rolling_metric_window_disclosure.md
  - ./temporal_window.md
  - ../governance/query_run_record.md
  - ../../schemas/contracts/v1/common/elapsed_time_unit_disclosure.schema.json
  - ../../fixtures/contracts/v1/common/elapsed_time_unit_disclosure/cases.json
  - ../../tools/validators/validate_elapsed_time_unit_disclosure.py
  - ../../tests/validators/test_validate_elapsed_time_unit_disclosure.py
  - ../../docs/intake/exploratory/pass-18-elapsed-time-unit-disclosure-source-map.md
tags: [kfm, common, temporal, elapsed-time, units, timezone, rounding, fixture-only, no-network]
notes:
  - "Implements the smallest dependency-closed portion of supplied Pass 18 card KFM-P18-INV-312."
  - "A PASS proves disclosure coherence only; it does not prove query execution, metric correctness, review, release, or publication."
[/KFM_META_BLOCK_V2] -->

# ElapsedTimeUnitDisclosureCandidate

`ElapsedTimeUnitDisclosureCandidate` is an additive, fixture-only profile for making timestamp-difference metric semantics explicit. It binds query and method definitions by digest, names the start and end fields, records subtraction order, timezone and boundary assumptions, declares extraction and displayed units, and checks the exact rational conversion between fixed-duration units.

It implements the narrow requirement in supplied Pass 18 card `KFM-P18-INV-312`: SQL metrics that compare timestamps should record the extraction unit and conversion rule used to compute elapsed time, rather than hiding conversions such as epoch seconds divided by `3600` to produce hours.

## Boundary

A validator `PASS` proves only that:

- the closed candidate shape and deterministic profile hash agree;
- query, method, engine, timezone, boundary, parity, evidence, review, and limitation declarations satisfy local rules;
- start and end field identities remain distinct and subtraction direction is explicit;
- fixed-duration conversion is an exact reduced rational ratio;
- calendar units are not silently treated as fixed durations;
- negative and null handling cannot silently discard meaning; and
- public-support candidates disclose unit, conversion, timezone, boundary, and rounding semantics and carry review and release-manifest references.

The validator does not parse or execute SQL, connect to a database, inspect timestamps or rows, compute an elapsed value, validate an IANA timezone, resolve references or evidence, assess metric fitness, decide policy or review, promote, release, deploy, publish, or authorize public use.

## Conversion semantics

For fixed-duration units, the declared relationship is:

`displayed_value = extracted_value × conversion_numerator ÷ conversion_denominator`

The fraction must be reduced and exactly match the declared units. Examples include seconds to hours as `1/3600` and hours to minutes as `60/1`.

`CALENDAR_MONTH` and `CALENDAR_YEAR` require `CALENDAR_BOUNDARY_COUNT` plus a digest-bound boundary profile. They may be disclosed only as identity conversions in this first profile; cross-calendar and calendar-to-fixed conversions deny because a universal fixed ratio would hide calendar semantics. Business-time semantics likewise require a boundary profile.

## Sign, null, timezone, and parity semantics

- `ABSOLUTE_VALUE` denies because it hides subtraction direction.
- `DROP` denies because it silently changes the metric population.
- `UNRESOLVED` timezone assumptions and engine parity abstain.
- `MISMATCH` engine parity denies.
- a synthetic parity claim requires an explicit fixture reference.

The profile carries no timestamp values, elapsed values, source rows, SQL text, credentials, connection details, or arbitrary generated prose.

## Finite validator outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | Unit, conversion, timezone, boundary, rounding, parity, disclosure, reference, and non-authority declarations are locally coherent. |
| `ABSTAIN` | Assessment, timezone, parity, or a required reference remains incomplete or unresolved. |
| `DENY` | Conversion, calendar, sign, null, field, disclosure, parity, timestamp, reference-array, limitation, or deterministic-identity declarations are incoherent. |
| `ERROR` | The candidate cannot be parsed or evaluated safely, or declares assessment error. |

These are validation results only, not metric truth, evidence, policy, review, release, or publication decisions.

## Directory Rules basis

Reusable elapsed-time meaning is adjacent to temporal-window and rolling-metric declarations under `contracts/common/`. Machine shape, synthetic replay, executable validation, conformance proof, orchestration, source reconciliation, and generated authoring provenance remain in their established responsibility roots.

No query runner, database adapter, metric store, evidence store, policy lane, release path, public panel, or new root is created.

## Validation

```bash
python -m unittest tests.validators.test_validate_elapsed_time_unit_disclosure -v
python tools/validators/validate_elapsed_time_unit_disclosure.py --fixtures
```

## Rollback

Revert the additive packet. It has no runtime consumer and changes no query, database, metric, evidence, policy, lifecycle, review, release, deployment, or public artifact.
