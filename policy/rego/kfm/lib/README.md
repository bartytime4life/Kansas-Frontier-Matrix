# KFM Policy Library (Rego Utilities)
![Governed](https://img.shields.io/badge/governed-yes-6f42c1)
![Policy posture](https://img.shields.io/badge/posture-default--deny-critical)
![Engine](https://img.shields.io/badge/engine-OPA%2FRego-0052cc)
![Tests](https://img.shields.io/badge/tests-opa%20test%20%2B%20conftest-brightgreen)

**Path:** `policy/rego/kfm/lib/`

This folder contains **shared, reusable Rego modules** (helper functions, shared predicates, normalization utilities, and common policy contracts) used across KFM policy bundles.

The **goal** of `kfm/lib` is to make KFM’s governance rules:
- **consistent** across subsystems (API, ingestion/promotion, Story Nodes, Focus Mode),
- **auditable** (deterministic decisions; explainable reason codes),
- **fail-closed** (missing/invalid inputs never “accidentally allow”),
- and **maintainable** (small, composable helpers with unit tests).

---

## Table of Contents
- [Non-Negotiables (KFM Invariants)](#non-negotiables-kfm-invariants)
- [What Belongs in `lib`](#what-belongs-in-lib)
- [What Does Not Belong in `lib`](#what-does-not-belong-in-lib)
- [Repo Context and Expected Layout](#repo-context-and-expected-layout)
- [Library Design Rules](#library-design-rules)
- [Package & Naming Conventions](#package--naming-conventions)
- [Shared Policy Contracts](#shared-policy-contracts)
  - [Canonical Input Shape](#canonical-input-shape)
  - [Standard Decisions & Outputs](#standard-decisions--outputs)
  - [Sensitivity & Redaction Helpers](#sensitivity--redaction-helpers)
  - [Citations / “Cite-or-Abstain” Helpers](#citations--cite-or-abstain-helpers)
- [Testing](#testing)
  - [Unit Tests](#unit-tests)
  - [Regression Suite (Non-Regression Against Leaks)](#regression-suite-non-regression-against-leaks)
- [Local Development](#local-development)
- [CI Integration Expectations](#ci-integration-expectations)
- [How to Add or Change a Library Module](#how-to-add-or-change-a-library-module)
- [Governance & Change Control](#governance--change-control)
- [Troubleshooting](#troubleshooting)

---

## Non-Negotiables (KFM Invariants)

These are the “always true” constraints that all helper modules in `lib/` must support.

- **Default deny / fail-closed**  
  Policies must deny by default. Missing keys, malformed inputs, or unknown classifications must *not* fall through to allow.

- **Trust membrane**  
  Policy evaluation is part of KFM’s “governed boundary.” External clients and the UI must not bypass enforcement (e.g., UI→DB shortcuts).

- **Evidence-first**  
  Where the system claims facts (especially AI answers), the rules must support **“cite or abstain.”**

- **Sensitivity-aware**  
  Policies must support sensitivity classes (e.g., public vs restricted vs sensitive-location) and enforce safe outputs (including redacted derivatives).

> **Note:** Some of the above invariants are stated in KFM’s internal design artifacts; exact module boundaries and filenames in this repository should be treated as **(not confirmed in repo)** unless defined elsewhere.

---

## What Belongs in `lib`

`lib/` is for **shared building blocks** that multiple policy packs import.

Typical content:
- input normalization (`normalize_*` helpers)
- shared constants / enums (roles, sensitivity classes, action types)
- common predicates (e.g., `is_admin(actor)`, `has_role(actor, "reviewer")`)
- reason-code builders (standardized denial reasons)
- schema-ish checks (presence/shape checks; lightweight validation)
- shared logic for:
  - sensitivity & redaction
  - citation requirements
  - dataset promotion readiness checks (catalog presence, receipt presence, etc.) *(the contract comes from higher-level policies; helpers live here)*

---

## What Does Not Belong in `lib`

Avoid putting these in `lib/`:
- system-specific business rules (“Kansas Mesonet policy thresholds”, “Provider X quirks”)  
  → those should live in a **policy pack** (bundle) for the owning subsystem.
- policies that are intended to be queried directly as final decisions (`data.kfm.ai.allow`, `data.kfm.data.allow`, etc.)  
  → those should live in **bundle entrypoints**, not in shared library code.
- anything that depends on runtime infrastructure assumptions (network calls, filesystem reads, DB shape, etc.)  
  → Rego should remain deterministic and hermetic.

---

## Repo Context and Expected Layout

This README is for `policy/rego/kfm/lib`, but contributors need orientation in the broader policy tree.

**Recommended (not confirmed in repo) directory context:**

```text
policy/
  rego/
    kfm/
      lib/                 # ← YOU ARE HERE (shared helpers)
        README.md
        *.rego
      bundles/             # deployable / queryable policy packs (entrypoints)
        *.rego
      tests/               # golden + regression tests (or colocated *_test.rego)
        *.rego
      schemas/             # JSON Schemas used by CI and/or policy input validation
        *.json
      data/                # data.json / role maps / controlled vocabularies (OPA data documents)
        *.json
      examples/            # example inputs used in docs/tests
        *.json
```

If your repo differs, keep this README accurate and update the tree.

---

## Library Design Rules

1. **Deterministic & side-effect free**
   - No time-based logic, randomness, or external IO assumptions.
   - “Same input → same decision” must always hold.

2. **Fail-closed on unknowns**
   - Unknown roles, unknown sensitivity labels, missing keys → return “deny” or “invalid input” reasons.

3. **Reason codes are first-class**
   - Helpers should make it easy for policy entrypoints to return consistent denial reasons.
   - Prefer structured objects: `{code, message, details}`.

4. **Prefer small, composable helpers**
   - One helper should do one thing.
   - Avoid monolithic “mega modules.”

5. **No duplicate policy logic**
   - If multiple bundles need the same behavior, move it into `lib/`.

---

## Package & Naming Conventions

### Package naming
Use a consistent namespace to avoid collisions:

- Library modules: `package kfm.lib.<area>`
  - Example: `package kfm.lib.sensitivity`
  - Example: `package kfm.lib.citations`
  - Example: `package kfm.lib.roles`

- Bundle entrypoints (outside this folder): `package kfm.<domain>`
  - Example: `package kfm.data`
  - Example: `package kfm.ai`

> Keep package names stable. Renaming packages is a breaking change for all importing bundles.

### Function naming
- Predicates: `is_*`, `has_*`, `can_*`
- Normalizers: `normalize_*`
- Parsers / coercion: `parse_*`, `to_*`
- Reason builders: `deny_*`, `reason_*`

### Formatting
- Run `opa fmt` on all `.rego` files.
- Keep helpers documented with short comments.

---

## Shared Policy Contracts

### Canonical input shape

KFM documents recommend an input shape that captures:
- **actor context** (role/attributes),
- **request context** (endpoint),
- plus **domain-specific objects** (resource, answer, etc.). *(Exact schema may be enforced elsewhere.)*

**Illustrative input (not confirmed in repo):**
```json
{
  "actor": {
    "id": "user:123",
    "role": "public|reviewer|admin",
    "attributes": { "org": "kfm", "scopes": ["read:public"] }
  },
  "request": {
    "endpoint": "/api/v1/ai/query",
    "method": "POST",
    "context": {
      "trace_id": "00-...-...",
      "view_state": {
        "timeRange": ["1860-01-01", "1870-01-01"],
        "bbox": [-102.0, 36.9, -94.6, 40.0],
        "activeLayers": ["kfm.layer.population_1870"]
      }
    }
  },

  "resource": {
    "kind": "dataset|layer|story|evidence_bundle",
    "id": "dataset:ks-population-1870",
    "sensitivity": "public|restricted|sensitive-location|aggregate-only"
  },

  "answer": {
    "text": "...",
    "has_citations": true,
    "citations": [{"ref":"..."}],
    "sensitivity_ok": true
  }
}
```

**Library responsibility:** `lib/` should provide helpers that make it easy for entrypoint policies to:
- detect missing keys safely,
- normalize known enums,
- and produce consistent denial reasons.

### Standard decisions & outputs

Entry points should generally evaluate to **a small, stable decision surface**, such as:

- `allow: boolean`
- `deny: [{code, message, details}]` (optional but strongly recommended)
- `obligations: [...]` (optional; used for redaction or “return sanitized version” behaviors)
- `audit: {...}` (optional; e.g., policy bundle hash / decision id) *(not confirmed in repo)*

**Example decision object (pattern):**
```json
{
  "allow": false,
  "deny": [
    {
      "code": "KFM_DENY_MISSING_CITATIONS",
      "message": "Focus Mode answers must include citations.",
      "details": {"min_citations": 1}
    }
  ],
  "obligations": []
}
```

---

### Sensitivity & redaction helpers

KFM must support sensitivity-aware handling, including “sensitive-location” and “aggregate-only” patterns.

**Recommended helper responsibilities:**
- parse/normalize sensitivity labels
- determine if a role can access “precise” data
- compute obligations such as:
  - “generalize coordinates”
  - “suppress field”
  - “aggregate above threshold”
- guarantee: if sensitivity is unknown → deny

> Redaction is considered a first-class transformation in KFM and should be traceable via provenance artifacts. (Exact PROV wiring is enforced outside of `lib/`.)

---

### Citations / “cite-or-abstain” helpers

A core KFM enforcement pattern is: **AI answers must cite evidence or abstain.**

**Recommended helper responsibilities:**
- `has_min_citations(answer, n)`
- `citations_present(answer)`
- `sensitivity_ok(answer)` *(note: how this is computed may be upstream; helpers should not guess)*

**Example snippet (helper usage):**
```rego
# bundle entrypoint (NOT in lib/)
package kfm.ai
default allow := false

import data.kfm.lib.citations
import data.kfm.lib.reasons

min_citations := 1

allow if {
  citations.citations_present(input.answer)
  citations.has_min_citations(input.answer, min_citations)
  input.answer.sensitivity_ok == true
}
```

---

## Testing

### Unit tests

Every helper module should have tests. Two acceptable patterns:

- colocate: `foo.rego` + `foo_test.rego` (preferred)
- centralized: `tests/*.rego` importing `lib/*`

Write tests for:
- happy paths
- missing keys
- unknown enums
- boundary values (e.g., `min_citations = 1`)

### Regression suite (non-regression against leaks)

In addition to unit tests, maintain **golden “leak prevention” tests** for:
- sensitive-location precision leakage
- restricted field leakage (e.g., ownership/personally identifying fields)
- aggregate-only small-count leakage
- “audit integrity” expectations (e.g., a response must include an audit reference) *(actual auditing enforced elsewhere; tests can assert decision outputs)*

> Keep regression tests forever: once a leak is fixed, it must never reappear.

---

## Local Development

**Prereqs (not confirmed in repo):**
- `opa`
- `conftest` (if used in your CI)
- `make` (optional)

Common commands:
```bash
# Format
opa fmt -w policy/rego/kfm

# Unit tests
opa test -v policy/rego/kfm

# (Optional) conftest-style tests if your repo uses conftest
conftest test policy/rego/kfm
```

---

## CI Integration Expectations

KFM’s governance model expects that policy changes are *merge-blocking* when invalid.

Recommended CI behavior (some of this may be implemented elsewhere in the repo):
- run `opa test` for Rego policies
- validate governed artifacts (Story Nodes, catalogs, etc.)
- run “acceptance harness” checks that combine metadata validation + policy tests + supply-chain verification *(not confirmed in repo)*

If your repo uses a single `make verify` (or similar), this README should point to it.

---

## How to Add or Change a Library Module

Checklist:
- [ ] Create `lib/<name>.rego` with `package kfm.lib.<area>`
- [ ] Add/update `lib/<name>_test.rego`
- [ ] Run `opa fmt` and `opa test`
- [ ] If changing a shared contract (input shape, enums, reason codes):
  - [ ] update relevant JSON Schema *(not confirmed in repo)*
  - [ ] update any bundle entrypoints that import the helper
  - [ ] add regression tests for fail-closed behavior
- [ ] Update this README if the module registry or conventions change

---

## Governance & Change Control

Treat policy as a governed artifact:
- Changes must be reviewed with the same seriousness as code that controls data access.
- Prefer **small, reversible** changes.
- Keep a stable public surface for helper modules (avoid breaking imports without a migration plan).

---

## Troubleshooting

### “Why is my policy denying everything?”
- Ensure `default allow := false` exists only at entrypoints (bundles), not in helpers.
- Confirm your input shape matches what your helpers expect.
- Use tracing:
```bash
opa eval -d policy/rego/kfm -i input.json "data.kfm.ai.allow" --explain=full
```

### “Tests pass locally but fail in CI”
- Check tool versions (OPA/Conftest) are pinned in CI.
- Ensure you ran `opa fmt` and committed formatted output.

---

## Appendix: Suggested Library Module Registry (Template)

Maintain a small registry table here to help humans:

| Module (package) | File | Purpose | Stable API? |
|---|---|---|---|
| `kfm.lib.roles` | `roles.rego` | Role predicates (`is_admin`, `has_role`) | ✅ |
| `kfm.lib.sensitivity` | `sensitivity.rego` | Sensitivity parsing + access rules | ✅ |
| `kfm.lib.citations` | `citations.rego` | Citation presence + min-citation checks | ✅ |
| `kfm.lib.reasons` | `reasons.rego` | Standard deny reason builders | ✅ |

> Replace this template with the actual modules present in this folder. (not confirmed in repo)

