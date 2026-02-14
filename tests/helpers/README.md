<!--
File: tests/helpers/README.md
Purpose: Shared helper utilities for KFM test suites (backend, UI, policy, pipelines).
-->

# 🧪 KFM Test Helpers (`tests/helpers`)

Shared, **governed** helper utilities used across KFM test suites to keep tests:

- **Deterministic** (no flaky time/random behavior)
- **Hermetic** (no accidental network / external dependencies)
- **Evidence-first** (where facts are asserted, we also assert citations / provenance)
- **Aligned with KFM invariants** (trust membrane, fail-closed policy gates)

> ✅ If you are writing tests that touch **governed behavior** (policy decisions, citations, promotion gates, evidence resolver), prefer reusing helpers from this directory rather than re-rolling ad-hoc fixtures.

---

## Table of contents

- [What belongs here](#what-belongs-here)
- [What does *not* belong here](#what-does-not-belong-here)
- [Design goals and invariants](#design-goals-and-invariants)
- [Suggested directory layout](#suggested-directory-layout)
- [How helpers map to KFM’s clean layers](#how-helpers-map-to-kfms-clean-layers)
- [Helper categories](#helper-categories)
- [Golden sets and snapshots](#golden-sets-and-snapshots)
- [Adding or changing a helper](#adding-or-changing-a-helper)
- [Governance and sensitive data rules](#governance-and-sensitive-data-rules)
- [Troubleshooting](#troubleshooting)

---

## What belongs here

This folder is for **test-only** code that is intentionally reusable.

Typical contents include:

- **Fixtures**: small, synthetic data samples (e.g., minimal STAC/DCAT/PROV fragments, Story Node skeletons, policy inputs).
- **Builders / factories**: functions that generate valid domain objects with defaults (and allow overrides).
- **Fakes / stubs** for ports/adapters:
  - repository fakes (in-memory implementations)
  - object store fakes
  - graph/search fakes
  - OPA/PDP response fakes (when you are not running real OPA in tests)
- **Assertions / matchers**:
  - “has citations”
  - “audit_ref present”
  - “policy denied”
  - “no UI direct DB access” safety checks (when applicable)
- **Harnesses** for recurring test patterns:
  - OpenAPI contract test runner / snapshot checks
  - Focus Mode “gold-set” regression runner
  - pipeline promotion gate checks (metadata present, checksums present, etc.)
- **Determinism utilities**:
  - time freeze helpers
  - seeded randomness
  - stable temp dir creators
  - stable JSON canonicalization helpers (for reproducible diffs)

---

## What does *not* belong here

Avoid putting these in `tests/helpers`:

- ❌ **Production code** (belongs under `src/`, `web/`, `policy/`, etc.)
- ❌ **Live calls** to upstream providers or external services  
  - If you need HTTP, use mocks, stubs, or **record/replay** fixtures.
- ❌ **Secrets** (API keys, tokens, `.env` contents)
- ❌ **Sensitive or restricted records** (real site coordinates, embargoed datasets, private individuals)
- ❌ **Large binaries** checked into git (keep fixtures minimal; store references/digests elsewhere if needed)
- ❌ “Magic” global monkeypatching that hides policy or governance failures

> ⚠️ Principle: if a helper makes tests *pass* by hiding or bypassing governance, it’s the wrong helper.

---

## Design goals and invariants

### Non‑negotiables

- **Deterministic**: tests must produce the same result across machines.
  - Freeze time, pin seeds, avoid dependency on ordering.
- **Hermetic**: tests should not require internet access.
- **Fail‑closed friendly**: helper defaults must not “auto‑allow” policies.
  - When a helper generates policy inputs, its default posture should be “deny unless explicitly allowed”.
- **Trust membrane aligned**:
  - UI/E2E helpers must route through the **API boundary** and must not directly query databases or internal stores.
- **Evidence-first**:
  - If a test asserts a factual answer/result, it should also assert the presence and resolvability of citations/provenance.

### Helper API style rules

- Prefer **pure functions** over stateful helpers.
- Prefer **explicit naming**:
  - `make_*` / `build_*` for factories
  - `fake_*` for fakes
  - `assert_*` for assertions
  - `with_*` for context managers / scopes
- Avoid hidden globals:
  - No implicit global random seed changes.
  - No implicit time monkeypatch unless the name clearly says so.

---

## Suggested directory layout

> This repository may not use every folder below. Create subfolders as needed, but keep names consistent.

```text
tests/
  helpers/
    README.md                # ← you are here

    assertions/              # custom matchers, reusable asserts
    builders/                # factories/builders for domain objects/DTOs
    fixtures/                # small synthetic fixtures (JSON, GeoJSON, YAML, etc.)
    fakes/                   # in-memory fakes / stubs for ports & adapters
    harness/                 # reusable harness runners (contract, gold-set, etc.)
    http/                    # test clients, request builders, auth stubs
    policy/                  # helpers for OPA inputs/outputs + policy test utilities
    snapshots/               # stable snapshots / golden files (small)
    time/                    # freeze time, deterministic clocks
    tmp/                     # temp dirs, file helpers, cleanup utilities
```

> ✅ Rule of thumb: if it can be used by more than one test suite (backend + UI + policy), it belongs in `tests/helpers/`.

---

## How helpers map to KFM’s clean layers

KFM’s clean architecture expects tests at every layer. Helpers should help you write the *right* kind of tests at the *right* boundary.

| Layer | What gets tested | What helpers should provide |
|---|---|---|
| **Domain** | Entities/value objects + invariants | Small builders, property generators, pure assertions |
| **Use cases** | Workflows + business rules | Fakes for ports, scenario builders, deterministic clocks |
| **Integration** | Contracts/DTOs/schemas | Contract test harness, schema validators, stable canonicalization |
| **Infrastructure** | DB clients, API handlers, OPA adapters | Test containers (if used), HTTP clients, smoke-test harness |

> The “clean layers + trust membrane” approach also implies **frontend never talks to databases directly**, so UI testing helpers must enforce API-only interactions.

---

## Helper categories

### 1) Assertions (`assertions/`)

Use assertions to keep tests readable and to standardize governance checks.

Recommended assertions:

- `assert_has_citations(result)`  
- `assert_citations_resolve(result.citations)`  
- `assert_has_audit_ref(result.audit_ref)`  
- `assert_policy_denied(response)` / `assert_policy_allowed(response)`  
- `assert_no_direct_db_access(build_artifacts | bundle | telemetry)` *(static analysis hooks may live elsewhere; helpers can wrap them)*

### 2) Builders / factories (`builders/`)

Builders generate minimal valid objects with safe defaults.

Recommended patterns:

- **Default minimal valid**
- **Override fields explicitly**
- **Stable IDs** when needed for snapshot tests

Example (pseudocode):

```python
# builders/dataset.py
def make_dataset(*, dataset_id="ds_test", sensitivity="public", **overrides):
    base = {"dataset_id": dataset_id, "sensitivity_level": sensitivity, "title": "Test Dataset"}
    base.update(overrides)
    return base
```

### 3) Fixtures (`fixtures/`)

Fixtures should be:

- **Small** (ideally <10–50KB per file)
- **Synthetic** (never restricted, never private)
- **Versioned** (include a fixture version comment/header when practical)

Examples of fixture types:

- minimal STAC collection/item examples
- minimal DCAT dataset/distribution examples
- minimal PROV activity/entity/agent examples
- Story Node v3 skeleton examples
- policy input JSON examples (allow/deny scenarios)

### 4) Fakes / stubs (`fakes/`)

Fakes are preferred over mocks for most workflow tests.

Guidance:

- Fakes should implement **the same port/interface** your use-case depends on.
- Keep fakes in-memory and deterministic.
- Provide inspection points:
  - “what was called?”
  - “what was stored?”

### 5) Harness (`harness/`)

Harnesses are reusable test runners for recurring governed behaviors.

Common harnesses in KFM-style repos:

- **OpenAPI contract harness**  
  - validate schema compatibility for `/api/v1`
  - detect breaking changes
- **Policy test harness**  
  - run OPA tests
  - validate policy inputs are schema-complete
- **Promotion gate harness**  
  - validate catalog artifacts exist and cross-link correctly
  - validate checksums exist
  - fail closed if required artifacts missing
- **Focus Mode evaluation harness**  
  - run curated “gold-set” prompts/expected outcomes
  - assert cite-or-abstain behavior
  - assert citations resolve and sensitivity rules respected

---

## Golden sets and snapshots

### What is a “gold-set”?

A **gold-set** is a curated set of test cases (inputs + expected outcomes) used to prevent regressions in governed behavior.

Use gold-sets for:

- Focus Mode cite-or-abstain regressions
- evidence resolver formatting
- policy decision stability on critical scenarios
- story node rendering semantics (where deterministic)

### Rules for gold-sets

- Gold-sets must be **reviewable** and small.
- Gold-set updates must be intentional:
  - include a changelog note in the PR description
  - justify why the expected output changed
- Prefer asserting **invariants** over exact wording where possible:
  - presence of citations
  - resolvability of citations
  - correct denial for restricted content
  - stable audit_ref behavior

> 🧠 Tip: When output text is inherently variable, store expectations as structured constraints (e.g., “must include ≥1 citation”, “must abstain when no evidence”) rather than exact strings.

---

## Adding or changing a helper

### Definition of Done (DoD)

When adding/changing a helper, your PR should satisfy:

- [ ] Helper is **test-only** and does not leak into production builds
- [ ] Helper has **its own unit tests** (yes, helpers need tests too)
- [ ] Helper does not introduce non-determinism (time/random/network)
- [ ] Helper defaults do not bypass governance (fail-closed friendly)
- [ ] Helper has **clear naming** and minimal surface area
- [ ] Helper is documented here (or in a nearby README if scoped)
- [ ] If helper affects gold-sets/snapshots: update is justified and reviewed

### Backwards compatibility

Treat widely-used helpers as internal APIs:

- Avoid breaking changes.
- If a change is necessary:
  - provide a migration path
  - update dependent tests in the same PR

---

## Governance and sensitive data rules

### Don’t commit sensitive data

KFM deals with potentially sensitive content (e.g., restricted heritage/biodiversity location data). Test fixtures must not increase risk.

**Hard rules:**

- No real restricted coordinates, site IDs, or identifying attributes.
- No PII (names/emails/phone numbers) unless clearly synthetic.
- No licensed datasets copied into fixtures unless you have explicit rights and the repo is authorized.

### Generalize when in doubt

If you need “realistic” data:

- generalize geometry (coarsen coordinates)
- reduce precision
- use fake IDs and synthetic attribute tables
- document any assumptions in the fixture header

> 🚨 If you believe a test requires restricted material to be meaningful, stop and route it through governance review (do not embed it here).

---

## Troubleshooting

### My test is flaky

Common causes:

- Time dependence → use a deterministic clock / freeze time helper
- Randomness → seed your RNG and make ordering explicit
- Parallelism → avoid shared global state; isolate temp dirs

### My integration test fails locally but passes in CI

Checklist:

- Ensure you didn’t accidentally depend on local services
- Ensure environment variables are not required (use defaults/fakes)
- If using containers, ensure ports are not hard-coded and collisions are handled

### My policy tests are confusing

Policy tests should be:

- explicit about inputs
- explicit about expected allow/deny
- default-deny friendly (missing keys should not “pass”)

If you are writing Focus Mode output validation tests, ensure your input clearly sets:
- whether citations exist
- whether sensitivity checks pass
- the citation list shape

---

## Final note

If you’re unsure whether a helper belongs here, ask:

> “Will this reduce duplication across multiple suites **without** bypassing governance?”

If yes, it probably belongs in `tests/helpers`.

