# 🧪 KFM Policy Golden Regression Suite (policy/tests/golden)

![Governed Artifact](https://img.shields.io/badge/governed-artifact-critical)
![Policy Regression](https://img.shields.io/badge/policy-regression-suite-important)
![Default Deny](https://img.shields.io/badge/default%20deny-required-black)
![Fail Closed](https://img.shields.io/badge/fail--closed-required-red)
![Security-Critical](https://img.shields.io/badge/security-critical-red)
![Cite-or-Abstain](https://img.shields.io/badge/focus%20mode-cite%20or%20abstain-blue)

> **Why this directory exists**
>
> This folder holds KFM’s **golden policy regression tests**: the set of cases we *never allow to regress*.
> If something ever leaked (restricted fields, sensitive location precision, missing audit refs, uncited Focus Mode claims), it gets a golden case here so it **stays fixed forever**.

---

## Governance Header

| Field | Value |
|---|---|
| Document | `policy/tests/golden/README.md` |
| Status | **Governed** (security-critical) |
| Effective date | **2026-02-15** |
| Owners | `CODEOWNERS` for `/policy/**` (required) |
| Review triggers | Any change touching `policy/tests/golden/**`, policy reason codes, redaction obligations, or the CI test harness wiring |
| Non‑negotiable | If this suite is missing or not executed in CI → **fail closed** (block merge/release) |

> [!IMPORTANT]
> Treat edits in this directory like production security changes.  
> **Do not “update expected outputs” to make a failing golden test pass** unless the change is explicitly approved as a policy behavior change.

---

## What is a “golden” policy test?

A golden test is a **regression lock** for a previously observed or high-risk failure mode.

Golden cases typically fall into one of these buckets:

| Bucket | What it prevents | Typical expected result |
|---|---|---|
| **Leak deny‑forever** | Previously leaked restricted fields/data | `allow == false` (deny) |
| **Sensitive‑location precision** | High-precision coordinates exposed to unauthorized roles | `allow == false` OR `allow == true` with **obligation** to generalize |
| **Redaction obligation** | Restricted fields returned unredacted | `allow == true` + `obligations` contain `redact_fields` |
| **Aggregate-only thresholds** | Small counts that enable re-identification | deny OR require aggregation obligation |
| **Focus Mode: cite-or-abstain** | Answers returned without evidence | deny/abstain path enforced by policy |
| **Audit integrity** | Missing `audit_ref` / missing evidence hash metadata | deny OR require obligation that output wrapper must satisfy |

> [!NOTE]
> “Golden” does **not** mean “happy path.”
> Golden suites are primarily **negative** and **security posture** tests.

---

## Non‑negotiables

1. **Default deny posture stays intact**
   - If policy cannot prove a request is allowed → **deny**.
2. **Golden leak tests are forever**
   - Once a leak is fixed, the regression case must remain in `golden/` permanently.
3. **No sensitive/real data in fixtures**
   - Fixtures must be **synthetic**. Never commit:
     - real addresses
     - precise archaeological site coordinates
     - names, phone numbers, emails, landowner identifiers
     - culturally restricted specifics
4. **Deterministic and reviewable**
   - Golden tests must be stable across machines.
   - No time-based randomness unless time is an explicit input field.
5. **If CI doesn’t run golden tests, governance is broken**
   - Missing gate ⇒ **fail closed**.

---

## Directory layout

This directory is intentionally simple and review-friendly.

```text
policy/tests/golden/
├─ README.md                 # this file
├─ cases/                    # (recommended) one folder per golden case
│  ├─ GOLDEN-0001-<slug>/
│  │  ├─ meta.yml            # what happened + why it must never regress
│  │  ├─ input.json          # sanitized policy input envelope
│  │  ├─ expected.json       # expected decision (allow/deny + reason_codes + obligations)
│  │  └─ case_test.rego      # (optional) test that binds input → decision assertions
│  └─ ...
└─ README_TEMPLATES/         # (optional) scaffolds for new cases
```

> [!TIP]
> If your repo prefers “Rego-only tests,” you can keep `cases/` empty and place `*_golden_test.rego` directly under `golden/`.
> The *contract* is the same: prior-leak scenarios must stay covered.

---

## Case metadata contract (`meta.yml`)

Each case must explain **why it exists** and how it maps to governance risk.

```yaml
case_id: GOLDEN-0001-sensitive-location-precision-leak
status: active
severity: high
category: sensitive-location
introduced_by: incident|bug|audit-finding
references:
  - issue: "GH-123"        # optional
  - incident: "INC-2026-02-14" # optional
policy_surface:
  - runtime_api
  - focus_mode
expected_behavior:
  decision: deny|allow-with-obligations
  invariants:
    - "unauthorized roles never receive high-precision geometry"
    - "reason_codes include SENSITIVE_LOCATION"
notes: >
  Sanitized fixture; coordinates are synthetic.
  This case must never be deleted.
```

---

## Running the golden suite

### How it runs in CI
Golden tests are intended to run as part of the repo’s **policy regression gate** and/or **acceptance harness**.

> [!IMPORTANT]
> If golden tests are not executed in CI, merges/releases must be blocked (fail closed).

### Typical local commands (OPA)
OPA’s `test` command supports filtering test cases by regex (useful for golden-only runs).  

```bash
# Run all policy tests (including golden)
opa test -v ./policy

# Run only tests that match "golden" (in package name or test name)
opa test -v -r 'golden' ./policy
```

> [!NOTE]
> The `-r/--run` flag is the standard OPA test filter; use it to keep local runs fast when iterating on golden cases.  
> Keep your test naming consistent so filtering works.

### Typical local commands (Conftest)
If your repo uses Conftest for policy-as-code checks against repo artifacts:

```bash
# Example pattern: run conftest against repo state using policy pack
conftest test . -p ./policy
```

> [!TIP]
> Golden tests are usually **OPA unit tests**; Conftest is often used for **repo artifact** enforcement (catalogs, manifests, receipts).
> Either way, CI must run the golden gate.

---

## Writing a golden test

Golden tests should assert *exactly what must never regress*.

### Minimum assertions (recommended)
A golden test should validate at least one of:

- `allow == false` (deny)
- decision includes required `reason_codes`
- decision includes required `obligations` (e.g., redaction/generalization)
- Focus Mode constraints (cite-or-abstain) are enforced by policy
- audit requirements are present/validated at boundary

### Example: deny-forever leak case (Rego test sketch)

```rego
package kfm.golden.leak_denies_test

# Illustrative only: adapt to your actual policy package/rules.
# Goal: a previously leaking request must always be denied.

test_prior_leak_is_denied {
  not data.kfm.data.allow with input as {
    "actor": {"role": "public"},
    "request": {"endpoint": "/api/v1/datasets/query", "method": "POST"},
    "resource": {"kind": "dataset", "id": "dataset_synthetic", "sensitivity": "restricted"}
  }
}
```

> [!WARNING]
> If you change policy packages/rule entrypoints, you must update golden tests accordingly.
> Deleting or weakening golden coverage is a governance breach.

---

## When a golden test fails

A golden failure means one of:

1. **A real regression** (highest likelihood, treat as security bug)
2. **A legitimate policy change** (must be explicitly approved and documented)
3. **A broken test harness** (CI not loading policy or tests correctly — still fail closed)

### Required response
- ✅ Fix policy or boundary enforcement so the test passes again.
- ✅ If behavior is intentionally changing:  
  - update `meta.yml` with rationale,
  - link approval (issue/ADR),
  - ensure replacement golden coverage exists for the new invariant.
- ❌ Do **not** “bless” a regression by editing `expected.json` or weakening assertions without governance review.

---

## Adding a new golden case (Definition of Done)

- [ ] Case has a stable `case_id` and a short slug
- [ ] Fixture is **sanitized** (no real sensitive info)
- [ ] Test reproduces the prior failure mode
- [ ] Test fails before the fix and passes after the fix
- [ ] `meta.yml` explains the risk and why this is permanent
- [ ] CI executes the golden suite as a required check (merge-blocking)

---

## Quick links

- Policy library overview: `../../README.md`
- Repo governance + CI gates: `../../../.github/README.md`
- Project root invariants: `../../../README.md`

---

