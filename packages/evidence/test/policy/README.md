<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/d63030da-a06e-4ad3-8d20-7e6495e245f8
title: Policy Tests — Evidence Package
type: standard
version: v1
status: draft
owners: TBD
created: 2026-02-25
updated: 2026-02-25
policy_label: restricted
related:
  - TODO: link-to-kfm-governance-guide
  - TODO: link-to-packages/evidence/README.md
tags: [kfm, evidence, tests, policy]
notes:
  - This directory README is intentionally "fail-closed": it avoids assuming the repo’s runner/tooling until verified.
  - Replace TODOs once the package manager + test runner are confirmed.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Policy Tests — Evidence Package

Executable assertions that **Evidence artifacts obey policy labels, allow/deny outcomes, and obligations** (e.g., redaction/generalization notices) — and that the same policy semantics hold in **CI and runtime**.

![Status](https://img.shields.io/badge/status-draft-lightgrey)
![Area](https://img.shields.io/badge/area-evidence_policy_tests-blue)
![Gate](https://img.shields.io/badge/promotion_gate-Gate_F_TODO-lightgrey)
![CI](https://img.shields.io/badge/ci-required_TODO-lightgrey)

**Status:** draft • **Owners:** TBD • **Scope:** Evidence policy tests

---

## Quick nav

- [Purpose](#purpose)
- [Where this fits in KFM](#where-this-fits-in-kfm)
- [Directory layout](#directory-layout)
- [What belongs here](#what-belongs-here)
- [What must not go here](#what-must-not-go-here)
- [Test categories](#test-categories)
- [How to run](#how-to-run)
- [Adding a policy test](#adding-a-policy-test)
- [Fixtures and golden files](#fixtures-and-golden-files)
- [Traceability to policy decisions](#traceability-to-policy-decisions)
- [Definition of Done](#definition-of-done)

---

## Purpose

This folder contains **policy-focused tests** for the `evidence` package.

These tests exist to ensure:

1. **Same policy semantics in CI and runtime.** If CI tests and runtime enforcement diverge, CI guarantees are meaningless.
2. **Default-deny posture** is preserved unless explicitly allowed by policy.
3. **Obligations** (e.g., “show_notice: geometry generalized”) are emitted consistently and are available to downstream surfaces (API/UI/Focus).
4. **No sensitive leakage** through “helpful” errors, metadata, receipts, exports, or public tiles.

> **NOTE:** This README does not assume a specific engine (OPA/Rego, in-house DSL, etc.). KFM defaults to policy-as-code with fixtures. If your implementation differs, keep the test *intent* and adapt the wiring.

[↑ Back to top](#top)

---

## Where this fits in KFM

Policy enforcement must be consistent across multiple “enforcement points”:

- **CI** (blocks merges)
- **Runtime API** (blocks serving protected resources)
- **Evidence resolver** (blocks resolving/rendering evidence bundles)
- **UI** (shows badges/notices but does not decide policy)

These tests are the **Evidence-side** guardrail ensuring the evidence resolver and its outputs honor policy decisions and obligations.

[↑ Back to top](#top)

---

## Directory layout

> **Directory Documentation Standard**: this section is required for README-like docs.

```
packages/evidence/test/policy/
  README.md                # this document
  cases/                   # (recommended) policy-focused tests
  fixtures/                # (recommended) fixture inputs + expected decisions/obligations
  golden/                  # (optional) stable “expected bundle” snapshots for regression tests
  helpers/                 # (recommended) shared helpers (policy eval wrapper, assertions)
```

> **TODO:** Update this tree to match the repo’s actual structure once confirmed.

[↑ Back to top](#top)

---

## What belongs here

✅ **Acceptable inputs**

- Fixture-driven allow/deny tests (including obligations)
- “No leakage” tests (public responses must not expose restricted details)
- Redaction/generalization behavior tests (public vs restricted versions)
- License/rights enforcement tests (export, display, attribution requirements)
- Evidence bundle output tests validating:
  - policy label propagation
  - required fields for downstream attribution/notice surfaces
  - deterministic output shape for stable UI rendering

[↑ Back to top](#top)

---

## What must not go here

❌ **Exclusions**

- Performance benchmarks (put in a perf suite)
- End-to-end UI tests (put in UI test harness)
- Network-dependent integration tests (keep policy tests deterministic)
- Tests that require privileged secrets or access tokens
- Real sensitive coordinates, PII, or restricted partner data embedded in fixtures

> **WARNING:** Fixtures must be safe-to-share within the repo. Use synthetic or heavily generalized examples.

[↑ Back to top](#top)

---

## Test categories

| Category | What it protects | Example assertion |
|---|---|---|
| **AuthZ allow/deny** | Prevents unauthorized reads/exports | public user cannot read `restricted` |
| **Obligations** | Ensures required notices/actions are attached | `public_generalized` → emits `show_notice` obligation |
| **Sensitivity leakage** | Prevents “metadata side-channels” | public responses do not contain restricted bbox/coords |
| **Generalization correctness** | Prevents reverse engineering sensitive locations | public tiles/exports contain no precise coordinate fields |
| **Licensing/rights** | Prevents accidental reuse violations | exports require license + rights metadata present |
| **Evidence bundle shape** | Ensures downstream clients can render safely | bundle includes policy decision + obligations consistently |

[↑ Back to top](#top)

---

## How to run

Because the repo’s package manager and test runner are **not confirmed in this README**, use the discovery workflow below and then fill in the TODOs.

### 1) Discover the test command

```bash
# From repo root (adjust as needed)
cat packages/evidence/package.json
```

Look for scripts like `test`, `test:policy`, `vitest`, `jest`, etc.

### 2) Run policy tests (fill in once confirmed)

```bash
# TODO: replace <pkgmgr> and <runner-args> once confirmed
cd packages/evidence
<pkgmgr> test <runner-args> policy
```

> **TIP:** If your runner supports test name/path filtering, keep policy tests runnable in isolation.

[↑ Back to top](#top)

---

## Adding a policy test

### Checklist

1. Add/extend **fixtures** (input + expected allow/deny + obligations).
2. Write a test in `cases/` that:
   - evaluates policy via the same adapter used by runtime (or via a shared harness),
   - asserts **decision** (allow/deny),
   - asserts **obligations** (if any),
   - asserts **no sensitive leakage** in public outputs.
3. Ensure it runs in CI and is stable/deterministic.

### Fixture shape (recommended)

Keep fixtures simple and explicit:

- user context (role/groups)
- action (read/export/resolve)
- resource (policy_label + identifiers)
- expected decision + obligations

Example (illustrative):

```json
{
  "name": "public_cannot_read_restricted",
  "input": {
    "user": { "role": "public" },
    "action": "read",
    "resource": { "policy_label": "restricted" }
  },
  "expect": {
    "decision": "deny",
    "obligations": []
  }
}
```

### Test skeleton (pseudocode)

```ts
// PSEUDOCODE — adapt to the package’s actual test runner and policy adapter.

import { evaluatePolicy } from "../helpers/evaluatePolicy";
import { loadFixture } from "../helpers/loadFixture";

test("public cannot read restricted", async () => {
  const fx = loadFixture("public_cannot_read_restricted.json");
  const result = await evaluatePolicy(fx.input);

  expect(result.decision).toBe("deny");
  expect(result.obligations ?? []).toEqual([]);
});
```

> **NOTE:** Keep the adapter boundary thin. The goal is to prove that the **policy contract** holds, not to duplicate policy logic in the tests.

[↑ Back to top](#top)

---

## Fixtures and golden files

### Fixture rules

- Prefer **synthetic** or **anonymized** data.
- If demonstrating sensitive-location behavior:
  - use fake geometries,
  - or pre-generalized geometries,
  - and include a test that the public output contains **no coordinate fields**.

### Golden files (optional)

If you snapshot entire evidence bundles:

- store “golden” expected outputs in `golden/`
- keep them **small**
- regenerate via a deterministic harness
- treat changes as **breaking** until reviewed (policy changes are governance changes)

[↑ Back to top](#top)

---

## Traceability to policy decisions

Every policy test should trace back to a policy basis:

- a policy decision id (preferred) like `kfm://policy_decision/...`
- or a governance rule reference
- or an explicit “why” comment in the test

Example pattern (recommended):

```ts
/**
 * Policy basis: kfm://policy_decision/TODO
 * Why: Restricted datasets must be denied to public users; no metadata leakage in deny responses.
 */
```

[↑ Back to top](#top)

---

## Definition of Done

A change in this folder is “done” when:

- [ ] New or updated fixtures exist for the scenario (allow/deny + obligations)
- [ ] A policy test asserts decision + obligations
- [ ] A “no leakage” assertion is present when relevant
- [ ] Tests run deterministically (no network, no time dependencies unless mocked)
- [ ] CI is configured so policy tests **block merges**
- [ ] Any policy label vocabulary changes are coordinated with governance owners

[↑ Back to top](#top)

---

<details>
  <summary><strong>Appendix: Common policy labels (starter)</strong></summary>

These labels are commonly used in KFM governance:

- `public`
- `public_generalized`
- `restricted`
- `restricted_sensitive_location`
- `internal`
- `embargoed`
- `quarantine`

> **TODO:** Confirm the authoritative vocabulary source in this repo and link it here.

</details>
