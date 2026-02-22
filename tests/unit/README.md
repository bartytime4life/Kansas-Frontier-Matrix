<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/0bf077d2-2097-4b9a-883c-1ec414b7757a
title: Unit tests
type: standard
version: v1
status: draft
owners: TBD
created: 2026-02-22
updated: 2026-02-22
policy_label: public
related: []
tags: [kfm, tests, unit]
notes:
  - Framework-agnostic guidance for unit tests under tests/unit.
  - Repo-specific runner commands must be filled in after confirming toolchain and CI.
[/KFM_META_BLOCK_V2] -->

# Unit tests

Fast, deterministic tests for KFM domain logic and governance-critical invariants.

![status](https://img.shields.io/badge/status-draft-yellow)
![scope](https://img.shields.io/badge/scope-unit%20tests-blue)
![principle](https://img.shields.io/badge/principle-fail%20closed-critical)
![determinism](https://img.shields.io/badge/tests-deterministic-success)
![policy](https://img.shields.io/badge/policy-public-lightgrey)

**Status:** draft • **Owners:** TBD • **Location:** `tests/unit/`

## Navigation

- [Scope](#scope)
- [Directory layout](#directory-layout)
- [Running unit tests](#running-unit-tests)
- [Unit test contract](#unit-test-contract)
- [What belongs here](#what-belongs-here)
- [Governance-critical unit tests](#governance-critical-unit-tests)
- [Fixtures](#fixtures)
- [Determinism checklist](#determinism-checklist)
- [Patterns](#patterns)
- [Anti-patterns](#anti-patterns)
- [Troubleshooting](#troubleshooting)
- [References](#references)

---

## Scope

This directory contains **unit tests**: tests that validate a **small unit of logic in isolation** (typically pure domain logic, canonicalization, validation, deterministic hashing utilities).

Unit tests are part of the project’s **merge-blocking quality gates**: they must be fast, deterministic, and fail-closed.

---

## Directory layout

This is the intended shape. Keep it close to the repo’s chosen runner conventions.

```text
tests/
├─ unit/
│  ├─ README.md
│  ├─ fixtures/
│  │  ├─ specs/                  # golden spec JSONs used for spec_hash stability
│  │  ├─ vocabs/                 # controlled vocab fixtures (valid + invalid)
│  │  └─ redaction/              # synthetic examples for redaction/generalization helpers
│  ├─ spec_hash.test.<ext>       # golden hash tests (example name from KFM docs)
│  ├─ vocab_validation.test.<ext>
│  └─ ...                        # more unit tests
└─ ...                           # integration / e2e / policy / schema tests live elsewhere
```

> NOTE: `<ext>` is whatever your repo uses (e.g., `ts`, `js`, `py`, `go`). Do not introduce a second test runner from inside `tests/unit/`.

---

## Running unit tests

**Repo-specific commands are intentionally not hard-coded here.** Fill these in once the repo toolchain is confirmed (package manager, language, runner, CI job name).

Suggested “fill-in” section:

- Local:
  - `TODO: <command to run unit tests only>`
  - `TODO: <command to run unit tests in watch mode>`
- CI:
  - `TODO: <CI workflow/job name that runs unit tests>`

If you need a quick starting point to discover the right command:

- Search the repo for:
  - `package.json` scripts like `test`, `test:unit`
  - `pyproject.toml` / `pytest.ini`
  - `go test` usage in CI
  - `.github/workflows/*` test steps

---

## Unit test contract

Unit tests in this directory MUST:

- **Be deterministic**
  - No reliance on wall clock time, system timezone, random seeds, network availability, machine order, or parallel scheduling.
- **Be hermetic**
  - No external network calls.
  - No dependence on external services (DBs, object stores, OPA servers, tile servers, etc.).
- **Fail closed**
  - If an invariant is violated, tests must fail loudly and specifically.
- **Use synthetic or cleared data only**
  - Do not commit restricted datasets or sensitive coordinates into unit test fixtures.

Unit tests SHOULD:

- Run quickly (seconds, not minutes).
- Keep fixtures small and reviewable.
- Prefer pure functions and dependency injection over extensive mocking.

---

## What belongs here

Examples:

- Canonicalization and deterministic hashing helpers
- Controlled vocabulary validation
- DTO/shape validation helpers that do not require I/O
- Redaction/generalization helper functions (with synthetic inputs)
- Pure domain logic and state reducers
- Error mapping and failure-mode helpers (“default deny” behaviors at the function level)

---

## Governance-critical unit tests

The KFM design explicitly calls out unit tests as the place to encode governance-critical invariants, including:

- **Deterministic `spec_hash`**
  - Stability across OS and runtime
  - Golden fixtures with known expected hashes
  - Regression detection for “hash drift”
- **Controlled vocabulary validation**
  - Accept valid vocabulary terms
  - Reject unknown/unsafe values
- **Safety helpers**
  - Generalization/redaction helpers must not leak precision (use synthetic examples and assertions)

A helpful way to drive coverage is to maintain a small “invariants matrix”:

| Invariant | Why it matters | Unit test target | Fixture type |
|---|---|---|---|
| spec hashing is stable | prevents drift and broken provenance | `spec_hash.*` | golden spec JSON |
| vocab rejects unknown values | prevents silent schema/policy bypass | `vocab_validation.*` | valid + invalid vocab lists |
| redaction removes precision | prevents sensitive leakage | redaction utilities | synthetic coordinates |

---

## Fixtures

Keep unit fixtures:

- **Small**: minimal data that demonstrates the invariant.
- **Synthetic** unless explicitly cleared for inclusion.
- **Stable**: avoid non-deterministic fields like timestamps.

Recommended fixture rules:

- JSON fixtures should be formatted consistently (so diffs are readable).
- If your hashing depends on canonical JSON:
  - Store the “pre-canonical” fixture (human authored)
  - In test, canonicalize → hash → compare to known expected digest

Example fixture naming:

```text
tests/unit/fixtures/specs/
├─ spec_minimal.valid.json
├─ spec_ordering_noise.valid.json   # same semantic content, different ordering
└─ spec_invalid.missing_field.json
```

---

## Determinism checklist

Before merging, verify:

- [ ] No test reads the system clock without an injected/faked clock
- [ ] No test depends on local timezone/locale
- [ ] No test makes a network request
- [ ] No test writes outside a per-test temp directory
- [ ] Randomness is either removed or seeded deterministically
- [ ] Golden fixtures are pinned and reviewed
- [ ] Tests pass locally and in CI without retries

---

## Patterns

**Golden tests for deterministic hashing**

- Use a small set of representative inputs
- Store expected outputs explicitly
- Make drift detection obvious and reviewable

Pseudo-example:

```text
given spec fixture A
when compute spec_hash(spec A)
then equals "sha256:<expected>"
```

**Property-style invariants**

Where appropriate:

- “Canonicalize(A) == Canonicalize(A with reordered keys)”
- “Validate(vocab) fails for unknown term”
- “Generalize(precise geometry) never outputs original precision”

**One failure, one message**

Prefer targeted assertions over broad snapshot comparisons when testing governance-critical invariants.

---

## Anti-patterns

Avoid:

- Using real partner datasets, sensitive locations, or restricted artifacts as fixtures
- Hitting real external services “just for the test”
- Reliance on sleeps/timeouts for correctness
- Broad snapshots that hide which invariant broke
- Flaky tests masked by retries

---

## Troubleshooting

- **Flaky test**
  - First assumption: non-determinism (time, ordering, random, parallel interference).
  - Remove wall-clock and use controlled inputs.
- **Hash drift**
  - Confirm canonicalization step is stable (ordering, whitespace, numeric formats).
  - Confirm fixture didn’t change unintentionally.
  - Update expected hashes only with a clear, reviewed rationale.

---

## References

- KFM design requires governance invariants to be encoded as tests and enforced as merge gates.
- Work package guidance calls out `tests/unit/spec_hash.test` and golden fixtures for deterministic `spec_hash`.

(Repo maintainers: add links here once the repo’s authoritative docs are in place.)
