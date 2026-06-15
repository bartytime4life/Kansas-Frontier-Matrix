# Temporal Module

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://package/temporal/src/temporal
title: Temporal module README
type: package-readme
version: v0.2
status: draft
owners: <PLACEHOLDER — Temporal steward · Schema steward · Validation steward>
created: 2026-06-15
updated: 2026-06-15
policy_label: internal
related:
  - packages/temporal/README.md
  - schemas/contracts/v1/
  - contracts/
  - docs/doctrine/lifecycle-law.md
  - docs/doctrine/truth-posture.md
  - docs/doctrine/directory-rules.md
  - docs/architecture/contract-schema-policy-split.md
tags: [kfm, temporal, bitemporal, valid-time, transaction-time, correction, release, evidence]
notes:
  - "v0.2 polish pass: tightened navigation, added maintainer guidance, clarified public-boundary language, and improved GitHub readability."
  - "Implementation depth is UNKNOWN until this module is inspected in a mounted repository."
  - "This README defines the intended package boundary; it is not proof that all named helpers exist."
] -->

> Shared temporal primitives for KFM evidence, observations, releases, corrections, rollback, and historical state.

| Status | Package role | Public path |
|---|---|---|
| `DRAFT / NEEDS VERIFICATION` | Shared implementation support for time semantics | Governed API / released artifact payloads, not direct public imports |

## At a glance

`packages/temporal/src/temporal/` is the importable module home for shared KFM time semantics.

KFM is map-first, but it is also time-aware. A claim, source record, observation, release, correction, and user view can all have different timestamps. This module exists so those distinctions stay explicit instead of collapsing into a generic `date` field.

This README is a boundary contract and maintainer guide. It does not prove that every illustrative helper, export, or downstream consumer already exists.

## Quick navigation

- [Boundary](#boundary)
- [What belongs here](#what-belongs-here)
- [What does not belong here](#what-does-not-belong-here)
- [Temporal vocabulary](#temporal-vocabulary)
- [Temporal profiles](#temporal-profiles)
- [Golden rules](#golden-rules)
- [Expected helper surface](#expected-helper-surface)
- [Examples](#examples)
- [Validation expectations](#validation-expectations)
- [Testing checklist](#testing-checklist)
- [Maintenance checklist](#maintenance-checklist)
- [Open verification items](#open-verification-items)

## Boundary

| Field | Value |
|---|---|
| Path | `packages/temporal/src/temporal/README.md` |
| Responsibility root | `packages/` — shared reusable implementation package |
| Module scope | Temporal semantics, interval handling, bitemporal vocabulary, freshness helpers, and validation support |
| Public authority | None. This module supports contracts, validators, APIs, and release tools; it is not the authority for claims |
| Trust posture | Evidence-bound, time-aware, correction-aware, rollback-aware |
| Normal public path | Public clients consume governed API outputs and released artifacts, not this module directly |

## Purpose

The `temporal` module should provide reusable temporal vocabulary and helpers so domains do not invent incompatible time fields, interval conventions, freshness rules, or correction semantics.

KFM must be able to distinguish:

- when something was true in the world
- when a source observed or reported it
- when KFM retrieved it
- when KFM processed it
- when KFM released it
- when KFM corrected it
- when a prior public statement was superseded
- which temporal lens a user or API query is asking from

## What belongs here

| Area | Belongs here |
|---|---|
| Temporal vocabulary | Shared names and constants for KFM time dimensions |
| Interval helpers | Inclusive/exclusive interval checks, overlap checks, containment checks |
| Bitemporal helpers | Valid-time and transaction-time support primitives |
| Freshness checks | Source age, retrieval age, release age, stale-state classification |
| Correction support | Supersession and correction-time comparison helpers |
| Test fixtures | Small synthetic temporal examples used by validators and packages |
| Serialization support | Stable conversion to ISO 8601 / UTC-oriented forms |
| Validation helpers | Low-level helpers used by validators, not policy decisions themselves |

## What does not belong here

This module must not become a parallel authority for contracts, schemas, policies, releases, or public truth.

| Does not belong | Correct home |
|---|---|
| Contract meaning | `contracts/` |
| Machine-readable schema authority | `schemas/contracts/v1/` |
| Policy allow / deny / redact decisions | `policy/` |
| Release decisions | `release/` |
| Raw, processed, catalog, proof, receipt, or published data | `data/` |
| Domain-specific business rules | Owning domain package or contract |
| Public UI rendering | `packages/ui/`, `packages/maplibre/`, or deployable apps |
| Direct public claims | Governed API / release surfaces only |

## Repo fit

`packages/temporal` should be a reusable implementation package. The nested `src/temporal/` module should contain importable code, internal documentation, and module-level examples.

Broader package setup, packaging metadata, test commands, and cross-package dependency notes belong in `packages/temporal/README.md` once verified.

## Temporal vocabulary

KFM should keep materially different time dimensions separate.

| Time kind | Meaning | Example use |
|---|---|---|
| `valid_time` | When the claim, condition, observation, boundary, or relationship applies in the world | Historical county boundary validity; parcel ownership assertion period |
| `observed_time` | When a sensor, survey, person, agency, or source observed the condition | Stream gauge reading time; field survey date |
| `source_time` | When the source system says the record was created, updated, published, or effective | Agency feed updated timestamp |
| `retrieval_time` | When KFM fetched, received, or captured the source material | Connector run timestamp |
| `processing_time` | When KFM normalized, transformed, validated, or staged the record | Pipeline run timestamp |
| `transaction_time` | When KFM stored, changed, corrected, or superseded the internal record | Audit history / bitemporal transaction record |
| `release_time` | When KFM made a reviewed artifact or claim available through a release surface | ReleaseManifest timestamp |
| `correction_time` | When KFM corrected, withdrew, amended, or superseded a prior release or claim | Correction notice timestamp |
| `view_time` | The user-selected time lens used in a UI, API query, map layer, or report | “Show the county as of 1875” |
| `generated_time` | When an interpretive derivative was generated | AI summary envelope timestamp |

## Temporal profiles

Not every object family needs every time kind. Each contract or schema should declare a temporal profile.

| Profile | Use when | Typical required fields |
|---|---|---|
| `current_state` | Only current known state matters and history is not material | `source_time`, `retrieval_time` |
| `valid_time` | The real-world effective period matters | `valid_time.start`, `valid_time.end` |
| `transaction_time` | Audit history of KFM changes matters | `transaction_time.start`, `transaction_time.end` |
| `bitemporal` | Both real-world validity and KFM knowledge/correction history matter | `valid_time`, `transaction_time` |
| `event_time` | A discrete event is being represented | `observed_time` or `event_time` |
| `release_time` | Publication, rollback, or correction depends on release state | `release_time`, `correction_time` |
| `view_time` | A client or analysis asks from a particular temporal lens | `view_time` |

## Golden rules

1. Do not use a generic `date` field when the type of time matters.
2. Do not collapse valid time, transaction time, release time, correction time, and generated time into one timestamp.
3. Prefer explicit field names over overloaded labels.
4. Prefer half-open intervals for interval logic unless a contract says otherwise.
5. Keep open-ended, unknown-ended, and not-applicable intervals distinct.
6. Treat corrections and supersessions as first-class temporal facts.
7. Keep public display labels conservative when temporal support is missing or stale.

Preferred field names:

```text
valid_start
valid_end
observed_at
source_updated_at
retrieved_at
processed_at
transaction_start
transaction_end
released_at
corrected_at
superseded_at
generated_at
```

## Interval conventions

Until a stronger contract says otherwise, interval-oriented helpers should prefer half-open intervals:

```text
[start, end)
```

That means:

- `start` is included
- `end` is excluded
- adjacent intervals can meet without overlapping
- open-ended current intervals should be represented explicitly, not hidden behind magic dates

Example:

```text
1870-01-01 <= t < 1880-01-01
```

## Sentinel values

Avoid magic “forever” dates such as:

```text
9999-12-31
```

If a sentinel is unavoidable for compatibility, it must be documented in the contract, schema, validator, or adapter that uses it.

Preferred form:

```yaml
valid_time:
  start: "1870-01-01"
  end: null
  end_status: open
```

or:

```yaml
valid_time:
  start: "1870-01-01"
  end: null
  end_status: unknown
```

## Expected helper surface

The implementation may eventually expose helpers such as:

```python
from temporal import (
    TemporalInterval,
    TemporalProfile,
    coerce_utc,
    intervals_overlap,
    contains_instant,
    classify_staleness,
    validate_half_open_interval,
)
```

These names are illustrative until source inspection confirms actual exports.

## Examples

### Valid-time record

```yaml
claim_id: kfm-example-claim-001
temporal_profile: valid_time
valid_time:
  start: "1875-01-01"
  end: "1880-01-01"
  interval_semantics: half_open
source_time:
  source_updated_at: "2026-05-01T00:00:00Z"
retrieval_time:
  retrieved_at: "2026-05-02T14:18:00Z"
```

### Bitemporal correction

```yaml
claim_id: kfm-example-claim-002
temporal_profile: bitemporal
valid_time:
  start: "1875-01-01"
  end: "1880-01-01"
transaction_time:
  start: "2026-05-02T14:18:00Z"
  end: "2026-06-01T10:00:00Z"
correction:
  corrected_at: "2026-06-01T10:00:00Z"
  correction_reason: "source_revision"
  supersedes: kfm-example-claim-002-v1
```

### Stale public payload label

```yaml
status: NEEDS_VERIFICATION
reason: stale_source_time
message: "Source timestamp is older than the freshness window for this claim family."
```

## Validation expectations

Temporal helpers should support validators that can fail closed when:

- a required time field is missing
- a generic `date` field appears where a specific time kind is required
- `start` is after `end`
- closed intervals overlap where a claim family requires non-overlap
- a record claims release state without `released_at`
- a correction lacks a prior claim, correction reason, or correction timestamp
- source freshness cannot be evaluated
- open-ended intervals do not declare whether the end is `open`, `unknown`, or `not_applicable`
- local timezone values are used without normalization rules
- public payloads expose stale or corrected records without a stale/correction label

## Public-client boundary

This module should not be imported directly by normal public clients.

Public users should receive temporal information through governed API payloads, EvidenceBundle resolution, release manifests, layer metadata, Evidence Drawer payloads, and policy-safe UI labels.

## Testing checklist

Minimum useful tests for this module should cover:

- parse and serialize UTC timestamps
- reject invalid interval ordering
- detect interval overlap
- accept adjacent half-open intervals
- classify stale source records
- classify corrected and superseded records
- preserve unknown versus open-ended temporal semantics
- reject ambiguous generic dates in strict mode
- produce deterministic output for identical temporal inputs

## Maintenance checklist

Before changing this module, verify:

- downstream schemas still use the same temporal vocabulary
- validators still agree with helper semantics
- release and correction records still round-trip
- public payload examples still label time dimensions clearly
- old sentinel-date compatibility behavior remains documented
- rollback and correction tests still pass
- changes do not collapse valid time, transaction time, release time, and correction time into one field

## Safe change pattern

1. Add or update the contract language first.
2. Update schemas and fixtures.
3. Update temporal helpers.
4. Update validators.
5. Add regression tests.
6. Update API / UI examples if public labels change.
7. Record migration or rollback notes when existing data is affected.

## Reviewer checklist

A review is not complete until the reviewer can answer yes to these checks:

- Are all temporal field names specific enough to avoid ambiguity?
- Are interval semantics documented?
- Are correction and supersession cases represented?
- Are public-facing stale states labelable?
- Are contract, schema, validator, and package responsibilities still separated?
- Can the change be rolled back without losing temporal meaning?

## Open verification items

- Confirm actual package manager and test runner.
- Confirm actual module exports.
- Confirm whether this package already has a root README.
- Confirm whether temporal contracts already exist under `contracts/` or `schemas/contracts/v1/`.
- Confirm the accepted naming convention for valid-time and transaction-time fields.
- Confirm whether KFM uses UTC-only timestamps, local source timestamps plus timezone fields, or both.
- Confirm whether any existing data uses sentinel dates that must be preserved for compatibility.

## Status summary

This README defines the intended responsibility boundary for `packages/temporal/src/temporal/`.

It should be treated as a draft package contract until source files, tests, imports, schemas, validators, and downstream consumers are inspected.
