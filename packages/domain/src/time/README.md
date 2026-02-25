<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/3e66a4e2-2b2f-4c3d-a5a4-9fb9f0ab1a5d
title: Domain Time Primitives
type: standard
version: v1
status: draft
owners: kfm-core (TODO: confirm CODEOWNERS)
created: 2026-02-25
updated: 2026-02-25
policy_label: public
related:
  - kfm://doc/TODO-domain-readme
  - kfm://doc/TODO-architecture-time
tags: [kfm, domain, time]
notes:
  - Canonical time types + conventions (event/valid/transaction time) for KFM domain modeling.
[/KFM_META_BLOCK_V2] -->

# Time (domain)
> Canonical time primitives + conventions for KFM, including multi-axis time (event, valid, transaction) and safe time-range operations.

**Status:** draft • **Owners:** `kfm-core` (TODO) • **Layer:** Domain • **Policy:** public

![status](https://img.shields.io/badge/status-draft-orange)
![layer](https://img.shields.io/badge/layer-domain-blue)
![scope](https://img.shields.io/badge/scope-time-9cf)
![policy](https://img.shields.io/badge/policy-public-brightgreen)
<!-- TODO: Replace with real CI/path badges once repo URLs are confirmed. -->

**Quick nav:**  
[Purpose](#purpose) • [Time axes](#time-axes) • [Core types](#core-types-proposed) • [Serialization](#serialization-proposed) • [Directory contract](#directory-contract) • [Examples](#examples) • [Testing](#testing--invariants) • [Change checklist](#change-checklist-definition-of-done)

---

## Purpose

This directory contains *domain-layer* time modeling primitives used across KFM:
- pipelines (run receipts / audit)
- catalogs (STAC/DCAT temporal extents)
- runtime APIs (query filters)
- map + story UI (time windows and animations)

This is where we centralize **terminology** and **invariants** so contributors don’t re-invent time semantics in every feature.

> NOTE: This is intentionally **policy-aware** (time can be generalized/bucketed as a redaction obligation), but it is **not** a policy engine.

[Back to top](#time-domain)

---

## Time axes

KFM needs more than a single “timestamp” in many domains. We model up to three axes:

| Axis | Meaning | Typical examples | When to use |
|---|---|---|---|
| **Event time** | When something happened | “flood peak time”, “sensor reading time”, “incident occurrence time” | Most observational facts and events |
| **Valid time** | When a statement is considered true | “county boundary existed from X to Y” | Administrative history, boundaries, regulatory/legal truth windows |
| **Transaction time** | When KFM recorded or published the data | “ingested_at”, “published_at”, “promoted_at” | Audits, reproducibility, freshness, conflict resolution |

### Guidance
- Start with **event time + transaction time**.
- Add **valid time** when the domain includes *boundary changes* or other administrative history where “true when” differs from “recorded when”.

[Back to top](#time-domain)

---

## Design goals

- **Explicitness over guessing**
  - No “implicit local timezone” assumptions.
  - No silent conversion between time axes.
- **Determinism**
  - Parsing/formatting must be stable to support hashing, caching, and reproducible runs.
- **Safe range math**
  - One canonical interval convention throughout the codebase.
- **Minimal dependencies**
  - Keep domain primitives portable and testable.

---

## Core types (PROPOSED)

> Everything below is an intended API surface. Confirm actual filenames/exports before wiring imports.

| Type / function | Responsibility | Notes |
|---|---|---|
| `Instant` | A single point in time | Stores the moment + precision (optional) |
| `TimeRange` | A half-open range `[start, end)` | Avoids off-by-one overlap bugs; supports intersection/contains |
| `TimeAxis` | `event` \| `valid` \| `transaction` | Prevents mixing axes in filters/logic |
| `TimeWindow` | UI/query-friendly window | Often pairs `axis + range` |
| `Clock` interface | Deterministic time source | Domain code should not call system clock directly |

### Canonical invariants (recommended)
- `TimeRange.start < TimeRange.end` (strict)
- `TimeRange` is **half-open**: includes `start`, excludes `end`
- Axis must be carried with ranges used for filtering
  - e.g., filtering by “event time window” vs “valid time window” yields different semantics

---

## Serialization (PROPOSED)

### Instants
- Prefer **ISO 8601** timestamps with an explicit offset (UTC recommended).
- Keep precision explicit when the source is day-level/month-level, etc.
  - Example: a county boundary valid “in 1887” should not be coerced to an arbitrary midnight without tagging precision.

### Ranges
- Serialize ranges as `{ "start": "...", "end": "..." }` with the same instant encoding.
- Treat open-ended ranges explicitly (e.g. `end = null`) only if your downstream consumers support it.

> WARNING: If you stringify dates differently in different places, you will break reproducibility (hash drift) and cache keys.

---

## Policy and generalization hooks (PROPOSED)

Some policy decisions may require **redaction/generalization** that affects time, not just geometry or attributes. Examples:
- bucket an event timestamp to day/month
- clamp to a broader window
- remove time entirely for sensitive records

This package can provide small, pure helpers such as:
- `floorToDay(instant)`
- `bucketToMonth(instant)`
- `generalizeRange(range, granularity)`

> NOTE: This module does *not* decide *when* to generalize — it only provides safe mechanics once an obligation is computed elsewhere.

---

## Directory contract

### Where it fits in the repo
`packages/domain/src/time/` is **domain-layer** code:
- ✅ Pure types + operations
- ✅ Safe parsing/formatting utilities
- ✅ Domain invariants + validations
- ✅ Test fixtures for time semantics

### Acceptable inputs (what belongs here)
- time primitives (`Instant`, `TimeRange`, `TimeAxis`)
- range operations (`intersect`, `contains`, `overlaps`, `union` where safe)
- conversion helpers with explicit axes/precision
- deterministic serialization for hashing and signatures

### Exclusions (what must not go here)
- ❌ database adapters / SQL query builders
- ❌ API controllers/handlers
- ❌ UI components (sliders, timeline widgets)
- ❌ anything that fetches current time directly (use a `Clock` injected from infrastructure)
- ❌ policy rule evaluation logic (OPA/Rego adapters, etc.)

---

## Proposed directory layout

> Replace with the actual tree once the module stabilizes.

```text
packages/domain/src/time/
  README.md
  index.(ts|js)                 # public exports (if applicable)
  axis.(ts|js)                  # TimeAxis
  instant.(ts|js)               # Instant + precision
  range.(ts|js)                 # TimeRange + ops
  window.(ts|js)                # TimeWindow helper for filters
  clock.(ts|js)                 # Clock interface + test clock
  __tests__/
    range.test.(ts|js)
    parse_roundtrip.test.(ts|js)
```

---

## Examples

### Example 1 — Attaching axis + window to a filter (pseudo)

```ts
// pseudo-code (TypeScript-style)
const window: TimeWindow = {
  axis: "event",
  range: TimeRange.closedOpen(
    Instant.parse("2019-05-01T00:00:00Z"),
    Instant.parse("2019-06-01T00:00:00Z")
  )
};

query = query.withTimeWindow(window);
```

### Example 2 — Valid time vs transaction time (conceptual)
- Valid time answers: “When was this boundary considered true?”
- Transaction time answers: “When did KFM learn/publish this boundary record?”

Keep them separate — “true when” is not always “recorded when”.

---

## Testing & invariants

Minimum expectations for this module:

- [ ] Round-trip parse/serialize stability (`parse(serialize(x)) == x`)
- [ ] Range properties: intersection symmetry, containment correctness
- [ ] Axis safety: compile-time/runtime guardrails against mixing axes
- [ ] Clock determinism: tests do not depend on wall-clock time

---

## Change checklist (Definition of Done)

When modifying anything in `packages/domain/src/time/`:

- [ ] Update this README if you change meaning/semantics (axis definitions, range rules)
- [ ] Add tests for edge cases (DST boundaries, precision loss, open-ended windows)
- [ ] Ensure serialization remains stable (no accidental formatting drift)
- [ ] If changing exported types: add a migration note and check downstream compile/tests
- [ ] If introducing valid-time usage: document why event+transaction is insufficient

---

<details>
<summary>Appendix: Known tricky edge cases</summary>

- **Day-level sources**: “YYYY-MM-DD” is not the same as midnight UTC — it’s a *date* with implicit timezone context.
- **Boundary changes**: almost always require valid time if you’re building historical map narratives.
- **Reproducibility**: stable time string formatting matters for hashing, caching, and signatures.

</details>

[Back to top](#time-domain)
