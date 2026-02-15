<!--
File: policy/bundles/_shared/README.md
Purpose: Shared Rego libraries + contracts for all KFM policy bundles.
-->

# Shared Policy Bundle: `_shared`

![policy](https://img.shields.io/badge/policy-OPA%2FRego-blue)
![bundle](https://img.shields.io/badge/bundle-_shared-informational)
![mode](https://img.shields.io/badge/default-deny--by--default-critical)
![governance](https://img.shields.io/badge/governance-evidence--first-success)

This directory contains **shared** Rego modules, helper rules, and lightweight contracts used across policy bundles under `policy/bundles/`.

> [!IMPORTANT]
> `_shared` is **library code**. Avoid putting **product-facing** `allow/deny` “final decisions” here unless the decision is explicitly defined as a *shared primitive* and is documented below.

---

## Why `_shared` exists

Across KFM, multiple policy bundles enforce consistent governance and security rules (e.g., *deny-by-default*, *fail-closed*, *cite-or-abstain*, and *sensitive-data handling*). `_shared` exists to:

- Centralize **reusable helpers** (string/array/object helpers, evidence guards, classification helpers, normalization).
- Provide **stable input-shape checks** (so policies fail closed instead of silently passing).
- Reduce drift: one canonical implementation, many consumers.

---

## Non-negotiable policy contract

These rules keep KFM policies predictable, auditable, and safe.

### ✅ Deny-by-default

Policies must be written so that **missing inputs** or **unknown states** do **not** accidentally produce an “allow”.

- Prefer `default allow := false`
- Prefer explicit positive checks to earn an allow.

### ✅ Fail-closed on missing/invalid required fields

If a policy depends on input fields (e.g., actor role, dataset sensitivity, evidence refs), then **missing fields must not allow access**.

> [!NOTE]
> Fail-closed can be implemented via explicit guards (recommended) and/or schema validation performed by the calling system or CI harness.

### ✅ Evidence-first (“No Source, No Answer”)

When evaluating **narrative outputs** (Focus Mode, Story Node claims, summaries, etc.), policies should enforce that claims have **traceable evidence references** or the system must abstain/deny publication.

### ✅ Sensitive data must be handled intentionally

Policies must support deny/redact/aggregate patterns for sensitive materials (e.g., precise locations, protected records). If a caller is not entitled, policies should **deny** or instruct the caller to **return a generalized/sanitized response** (depending on the bundle’s intent).

---

## How other bundles should consume `_shared`

OPA/Conftest resolve `import data...` references based on the policy load paths.

### Recommended usage pattern

- Treat `_shared` as an additional policy root included whenever evaluating a bundle.
- Keep bundle-specific decisions in their own bundle directory.
- Import shared helpers by namespace (example below).

> [!TIP]
> If your tooling supports multiple policy paths, include both:
> - the bundle you’re testing/evaluating, and
> - `policy/bundles/_shared`

---

## Rego conventions (required)

### Rego version compatibility

- Write policies to be compatible with **Rego v1 semantics**.
- Prefer explicitly declaring Rego v1 mode at the top of modules:

```rego
import rego.v1
```

> [!WARNING]
> Tooling defaults can change. CI should include a compatibility test that ensures policies behave under the repo’s pinned OPA/Conftest configuration.

### Namespaces

Shared code must live under a stable namespace:

- ✅ `package kfm.shared.<area>`
- ✅ `package kfm.shared.util.<topic>`
- ❌ `package main` (avoid)
- ❌ `package kfm.<bundle_name>` (bundle-specific belongs in that bundle)

### Rule naming

- Use **verbs** for predicates (`is_valid_*`, `has_*`, `can_*`, `deny_*`).
- Prefer booleans/predicates + small pure helpers over “giant rules”.

### Inputs are untrusted

Assume `input` is untrusted and can be malformed. Always guard field access.

---

## Minimal expected directory layout

This README does not require these folders to exist yet, but this structure is the intended baseline:

```text
policy/
└─ bundles/
   └─ _shared/                                  # Shared bundle components reused across policy packs
      ├─ README.md                               # What belongs here, reuse rules, and versioning expectations
      │
      ├─ lib/                                    # Shared Rego modules (recommended)
      │   └─ *.rego                               # Pure helpers + common decision utilities (no product-specific wiring)
      │
      ├─ data/                                   # Optional shared static policy data (OPA data documents)
      │   └─ *.json                               # Controlled vocabularies, role maps, thresholds, flags (if shared)
      │
      └─ tests/                                  # Shared unit tests (run with: opa test …)
          └─ *.rego                               # Regression + smoke tests for shared lib/data behavior
```

**Notes**
- `*.rego` in `_shared` should typically be **imported** by other bundles, not executed as top-level decisions.
- `*.json` in `_shared/data` should be **small**, **reviewable**, and **non-sensitive**.

---

## Example: importing shared helpers

> [!NOTE]
> This is an illustrative example showing the intended import style and default-deny pattern.

```rego
package kfm.ai

import rego.v1
import data.kfm.shared.evidence as evidence

default allow := false

allow if {
  evidence.has_min_citations(input.answer, 1)
  input.answer.sensitivity_ok
}
```

---

## Testing

### OPA unit tests (preferred for Rego correctness)

Use OPA’s built-in test runner for `*_test.rego` modules.

```bash
opa test policy/bundles/_shared -v
```

### Conftest (preferred for “policy gates” on files/artifacts)

Conftest evaluates policies against real files (JSON/YAML/etc.). When testing a bundle that depends on `_shared`, include both paths.

```bash
conftest test <TARGETS...> \
  --policy policy/bundles/_shared \
  --policy policy/bundles/<BUNDLE_NAME>
```

> [!TIP]
> Keep `_shared` tests focused on:
> - helper behavior (pure functions/predicates),
> - input guards (missing field behavior),
> - regression tests for edge cases (nulls, empty arrays, unexpected types).

---

## Change control

Because `_shared` is a dependency for many bundles, changes must be treated as “high blast radius”.

### Required checklist for edits

- [ ] Add/update **OPA unit tests** for any changed helper logic.
- [ ] Confirm **fail-closed** behavior for missing/invalid inputs.
- [ ] Avoid breaking namespace changes unless absolutely necessary.
- [ ] If breaking changes are required, add a temporary **compat shim** (old API delegating to new API) and document deprecation.

> [!WARNING]
> Never add secrets, private keys, tokens, or sensitive record contents to `_shared` (including `data/`).

---

## What belongs here vs. what does not

| Category | Belongs in `_shared` | Belongs in another bundle |
|---|---|---|
| Pure helper predicates/utilities | ✅ Yes | ❌ No |
| Common evidence/citation guards | ✅ Yes | ❌ No |
| Shared normalization (IDs, strings, time parsing) | ✅ Yes | ❌ No |
| Top-level “product decision” policies (e.g., `kfm.data.allow`) | ❌ No | ✅ Yes |
| Dataset-specific rules (SSURGO, GTFS, KHRI, etc.) | ❌ No | ✅ Yes |
| Anything containing sensitive ground-truth (restricted coords, protected site identifiers) | ❌ No | ✅ Governed storage only |

---

## Governance note

Policies in this repository are part of the KFM trust boundary. Treat changes here as **production-impacting**:

- Prefer small, reviewable diffs.
- Add tests for any behavior change.
- Default to deny when uncertain.

---

