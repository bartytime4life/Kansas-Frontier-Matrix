<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/9a4c2d6e-2d1c-4f47-84e0-6f8d5f2c6f9f
title: packages/domain/test — Domain package test suite
type: standard
version: v1
status: draft
owners: TBD (see CODEOWNERS)
created: 2026-02-25
updated: 2026-02-25
policy_label: public
related:
  - packages/domain
tags:
  - kfm
  - domain
  - tests
notes:
  - If this repo is private, change policy_label to restricted.
  - doc_id must stay stable; do not regenerate on edits.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# 🧪 packages/domain/test — Domain package test suite

Fast, deterministic tests for the **domain layer**: pure models + rules, no infrastructure.

[![Status](https://img.shields.io/badge/status-draft-orange)](#)
[![Layer](https://img.shields.io/badge/layer-domain-blue)](#)
[![Tests](https://img.shields.io/badge/tests-runner%20TODO-lightgrey)](#)
[![Determinism](https://img.shields.io/badge/deterministic-required-success)](#)
[![Policy](https://img.shields.io/badge/trust%20membrane-enforced-important)](#)

**Quick nav:**  
[Purpose](#purpose) · [Scope](#scope) · [Suggested layout](#suggested-layout) · [Quickstart](#quickstart) · [Test taxonomy](#test-taxonomy) · [Fixture rules](#fixture-rules) · [Conventions](#conventions) · [Definition of done](#definition-of-done) · [Troubleshooting](#troubleshooting)

---

## Purpose

This directory holds tests that protect the **domain contract**:

- Domain models stay **pure** and **portable**.
- Domain rules remain **deterministic** and **reproducible**.
- Domain logic never “reaches around” interfaces to touch infrastructure concerns.
- Domain behavior is stable under refactors, platform differences, and dependency upgrades.

> **WARNING**
> Domain tests must not require a database, object storage, network calls, Kubernetes, or external services.
> If a test needs infrastructure, it belongs in an integration or system test suite elsewhere.

[Back to top](#top)

---

## Scope

### In scope

- Domain entities, value objects, invariants, and pure decision logic
- Canonical serialization and deterministic identity
- Validation rules (schema-level rules at the domain boundary)
- “Contract expectations” for interfaces (without calling real adapters)

### Out of scope

- API endpoint tests
- Database query correctness
- Neo4j/PostGIS indexing behavior
- Policy engine integration using real OPA deployments
- UI behavior

[Back to top](#top)

---

## Suggested layout

This is a recommended structure for keeping tests discoverable and consistent. Adjust to match the repo’s established conventions.

```text
packages/domain/test/
  README.md

  unit/
    *.test.(ts|js)

  property/
    *.property.test.(ts|js)

  contract/
    *.contract.test.(ts|js)

  golden/
    *.golden.test.(ts|js)
    fixtures/

  fixtures/
    synthetic/
    minimal/
    README.md

  helpers/
    builders/
    assertions/
```

[Back to top](#top)

---

## Quickstart

> **NOTE**
> This repo may use `pnpm`, `npm workspaces`, `yarn`, or another runner. Use whichever is standard here.

From the repo root, try one of these patterns:

```sh
# pnpm (workspace filter)
pnpm --filter "<domain-package-name>" test

# npm workspaces
npm --workspace packages/domain test

# yarn workspaces
yarn workspace "<domain-package-name>" test
```

Common “targeted run” patterns:

```sh
# run a single file
<test-runner> packages/domain/test/unit/some_rule.test.ts

# run only domain tests by path
<test-runner> packages/domain/test
```

If you don’t know the runner yet, look for:

- `packages/domain/package.json` scripts (`test`, `test:unit`, `test:watch`)
- A root-level `package.json` workspace runner config
- A repo-wide test config file (`jest.config.*`, `vitest.config.*`, etc.)

[Back to top](#top)

---

## Test taxonomy

| Test type | Goal | Typical folder | Must be deterministic | Must avoid infra |
|---|---|---:|:---:|:---:|
| Unit tests | Verify a single rule or invariant | `unit/` | ✅ | ✅ |
| Property tests | Prove invariants hold across many inputs | `property/` | ✅ | ✅ |
| Golden tests | Lock down canonical serialization, hashing, stable outputs | `golden/` | ✅ | ✅ |
| Contract tests | Ensure domain ↔ interface expectations stay stable | `contract/` | ✅ | ✅ |

### High-value tests to prioritize

- **Deterministic identity and hashing**
  - Same input spec → same hash across OS/Node versions
  - Stable canonical JSON handling
- **Domain invariants**
  - Constructing invalid entities fails fast
  - Boundary validation rejects ambiguous states
- **Edge-case rules**
  - Time handling, normalization rules, or “empty-but-valid” cases
- **No side effects**
  - Rules should be pure; time and randomness must be injected

[Back to top](#top)

---

## Fixture rules

Fixtures in this directory are treated like shipped code.

- Use **synthetic**, **minimal**, **non-sensitive** data.
- Never add secrets, API keys, tokens, or production credentials.
- Do not include personally identifying information unless it is explicitly sanctioned for test use.
- For any vulnerable or sensitive locations, never include precise coordinates—use coarse or randomized geometry.

Recommended fixture patterns:

- `fixtures/minimal/`: smallest valid examples
- `fixtures/synthetic/`: generated data with clear provenance in comments

[Back to top](#top)

---

## Conventions

### Naming

Pick the convention that matches the existing runner:

- `*.test.ts` / `*.test.js`, or
- `*.spec.ts` / `*.spec.js`

Within this directory, prefer one naming style consistently.

### Structure

Recommended test shape:

- Arrange: build a valid domain object / input
- Act: call a pure function or method
- Assert: check outputs and invariants

Example skeleton:

```ts
// packages/domain/test/unit/example_rule.test.ts
import { describe, it, expect } from "<test-runner>";

describe("ExampleRule", () => {
  it("rejects invalid state", () => {
    // arrange
    const input = /* ... */;

    // act
    const result = /* ... */;

    // assert
    expect(result).toEqual(/* ... */);
  });
});
```

### Boundaries

Domain tests should:

- depend on **domain exports** (typically `packages/domain/src/...`)
- avoid importing from:
  - infrastructure implementations
  - runtime adapters
  - network clients
  - database drivers

If you need to validate boundaries, add a dedicated “dependency boundary” test (or lint rule) that fails when domain imports infra.

[Back to top](#top)

---

## Definition of done

For a change that touches domain logic, the PR is not done unless:

- [ ] Added or updated tests in `packages/domain/test/`
- [ ] Tests are deterministic and pass locally and in CI
- [ ] Fixtures are synthetic, minimal, and non-sensitive
- [ ] No domain code introduces direct infrastructure dependencies
- [ ] Golden outputs updated intentionally and reviewed when applicable
- [ ] Any change to domain contracts is reflected in contract tests

[Back to top](#top)

---

## Troubleshooting

### Tests fail only on CI

Common causes:

- Hidden time dependency (`Date.now()`, timezone variance)
- Randomness without a fixed seed
- File path differences between OS
- Locale-dependent formatting

Fix approach:

- Inject time and randomness
- Force canonical serialization
- Avoid relying on iteration order unless explicitly defined

### Golden tests changed unexpectedly

- Confirm whether behavior changed intentionally.
- If intentional: update fixtures with a clear commit message and ensure the change is reviewed.
- If unintentional: treat as regression and revert.

[Back to top](#top)

---

## Appendix

<details>
<summary><strong>Dependency boundary enforcement ideas</strong></summary>

- Add a lint rule or dependency graph rule:
  - “packages/domain/src must not import from packages/infra”
- Add a small test that parses compiled output or import graph and fails on forbidden imports.
- Keep allow-lists short and explicit.

</details>
