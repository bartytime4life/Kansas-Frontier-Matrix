<!--
File: policy/tests/unit/README.md
Purpose: Explain + standardize OPA/Rego unit tests for KFM policy-as-code.
-->

# Policy Unit Tests (OPA/Rego)

![OPA/Rego](https://img.shields.io/badge/policy-OPA%2FRego-blue)
![Fail-closed](https://img.shields.io/badge/governance-fail--closed-critical)

This folder contains **OPA/Rego unit tests** for the Kansas Frontier Matrix (KFM) **policy-as-code** layer.

KFM policies are part of the **trust membrane**: they must be **deny-by-default** and enforce governance consistently across data, stories, and Focus Mode outputs.

> [!IMPORTANT]
> **Policy changes are governance changes.** If you change a policy rule, you must update/add unit tests in this suite.

---

## What counts as a “unit test” here

A **unit test** in this directory:

- Executes Rego rules directly with the OPA test runner
- Uses **small, deterministic inputs** (inline JSON objects or tiny fixtures)
- Verifies both:
  - ✅ explicit **allow** behavior
  - ❌ deny-by-default (**fail-closed**) behavior

Unit tests here are intentionally **not**:
- Conftest “policy checks” against repository files (those are *policy integration checks*)
- Runtime gateway / OPA wiring tests (those are *service/integration tests*)

---

## Directory layout

```text
policy/
├─ …                      # Rego policy modules live under policy/ (exact subfolders may vary)
└─ tests/
   └─ unit/
      ├─ README.md        # you are here
      └─ *_test.rego      # OPA unit tests (Rego packages ending with _test)
```

> [!NOTE]
> This README documents how unit tests work and how they’re expected to run in CI.  
> The only “required” path assumption is that policy unit tests live under `policy/`.

---

## Running the unit tests

### CI-equivalent (from repo root)

```bash
opa test policy -v
```

### From inside this folder

```bash
# from policy/tests/unit
opa test ../.. -v
```

> [!TIP]
> If tests fail with missing imports (e.g., `import data.kfm.ai` not found), it usually means you ran `opa test` only on the tests directory instead of the **policy/** root that contains both policies and tests.

---

## Related: running repository policy checks (Conftest)

OPA unit tests validate *policy logic*. Conftest typically validates *repo artifacts* (metadata, docs, catalogs, etc.) against policies.

From the repo root:

```bash
conftest test .
```

---

## Conventions for KFM policy tests

### 1) Package naming

- Policy module: `package kfm.<area>`
- Matching unit tests: `package kfm.<area>_test`

Examples:
- `package kfm.data` → `package kfm.data_test`
- `package kfm.ai` → `package kfm.ai_test`

### 2) Deny-by-default (fail-closed)

Policies should default to deny, then explicitly allow known-safe cases:

```rego
package kfm.example
default allow := false

allow if { input.actor.role == "admin" }
```

Unit tests must confirm:
- At least one allow case works
- At least one deny case works
- Missing/invalid inputs do **not** accidentally allow

### 3) Test naming

OPA discovers tests by rule names starting with `test_`:

```rego
test_something if { … }
```

---

## Example: Focus Mode “cite-or-abstain” tests

The KFM blueprint pattern for Focus Mode output validation is:  
**allow only if citations exist and sensitivity is OK**.

A unit test module typically looks like:

```rego
package kfm.ai_test

import data.kfm.ai

test_allow_with_citations if {
  ai.allow with input as {
    "answer": {"has_citations": true, "sensitivity_ok": true, "citations": [{"id":"c1"}]}
  }
}

test_deny_without_citations if {
  not ai.allow with input as {
    "answer": {"has_citations": false, "sensitivity_ok": true, "citations": []}
  }
}

test_deny_if_sensitivity_not_ok if {
  not ai.allow with input as {
    "answer": {"has_citations": true, "sensitivity_ok": false, "citations": [{"id":"c1"}]}
  }
}
```

---

## What we expect every policy change to include

### Minimum test coverage checklist

- [ ] **At least 1 allow test** for the new/changed behavior
- [ ] **At least 1 deny test** for the corresponding unsafe/missing/unauthorized case
- [ ] **Deny-by-default** remains true (no accidental allows)
- [ ] Tests are deterministic (no network, no time-dependent logic)
- [ ] Inputs/fixtures do **not** include sensitive real-world data (especially precise locations)

> [!CAUTION]
> Do not add real sensitive locations or culturally restricted details to test fixtures.  
> If you need location-like data, use synthetic coordinates or generalized bounding boxes.

---

## Troubleshooting

### “undefined ref” / import errors

**Symptom**
- `rego_type_error: undefined ref: data.kfm.ai`

**Fix**
- Ensure you run tests from the **policy/** root so both policy modules and tests are loaded:
  - `opa test policy -v`

### Tests pass locally but fail in CI

Common causes:
- You ran a narrower command locally (e.g., tested only one file)
- A policy dependency was added but not committed
- Policy syntax changed and your local tool versions differ from CI

**Fix**
- Re-run the CI-equivalent command locally:
  - `opa test policy -v`

---

## Why this matters (KFM governance)

KFM’s trust membrane relies on policy evaluation for:
- Data/story access decisions
- Sensitive-data handling (generalized vs restricted outputs)
- Focus Mode “cite-or-abstain” enforcement

Failing policy tests should be treated as **merge-blocking** until resolved.

---

## Next steps (when unit tests aren’t enough)

- Add **Conftest** checks for real repository artifacts (`conftest test .`)
- Add integration tests that validate:
  - Gateway → OPA decision request/response contracts
  - Audit/provenance recording includes policy decision context

