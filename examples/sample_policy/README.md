# Sample Policy Pack (OPA/Rego)
Example **default-deny** policy-as-code pack for Kansas Frontier Matrix (KFM): role-based allow rules + policy labels + obligations, designed to be enforced consistently in **CI** and **runtime**.

**Status:** example / draft  
**Owners:** `<governance-owner>` (set in repo)  
**Scope:** sample policy logic + fixtures + tests (no infrastructure assumptions)

![policy](https://img.shields.io/badge/policy-OPA%2FRego-informational)
![posture](https://img.shields.io/badge/posture-default--deny-critical)
![tests](https://img.shields.io/badge/tests-OPA%20unit%20tests-success)

---

## Jump to
- [What this example is](#what-this-example-is)
- [Directory layout](#directory-layout)
- [Policy model](#policy-model)
- [Starter controlled vocabulary](#starter-controlled-vocabulary)
- [How to run tests](#how-to-run-tests)
- [How to wire into CI](#how-to-wire-into-ci)
- [Extending the sample](#extending-the-sample)
- [Sensitive location release pattern](#sensitive-location-release-pattern)
- [Definition of Done](#definition-of-done)
- [Notes and limitations](#notes-and-limitations)

---

## What this example is
This folder is a **sample** policy pack demonstrating:

1. **Default deny** posture (explicit allows only).
2. A simple authorization input shape:
   - `input.user.role`
   - `input.action`
   - `input.resource.policy_label`
3. A policy output concept that can include **obligations** (e.g., show UI notice, generalize geometry, remove attributes).
4. **Fixtures + unit tests** that must be runnable in CI and treated as merge-blocking.

> **Non-negotiable posture reminder:** CI and runtime must share the same policy semantics (or at minimum the same fixtures and outcomes). If they differ, CI “green” does not mean policy correctness.

---

## Directory layout
This layout mirrors the KFM “minimal starting policy pack structure” template.

```text
examples/sample_policy/
  README.md
  policy/
    rego/
      kfm.rego
    fixtures/
      public_user.json
      steward_user.json
      dataset_public.json
      dataset_restricted.json
    tests/
      kfm_test.rego
```

If your repository already has a `policy/` directory at the root, you can:
- keep this example as-is under `examples/`, or
- copy the `policy/` subtree to your canonical policy location.

---

## Policy model

### Input shape (authorization request)
```json
{
  "user": { "role": "public" },
  "action": "read",
  "resource": { "policy_label": "public" }
}
```

### Output shape (policy decision concept)
KFM treats a policy decision as: **allow/deny + obligations + reason codes** (for auditing and UX).

```json
{
  "decision_id": "kfm://policy_decision/xyz",
  "policy_label": "restricted",
  "decision": "deny",
  "reason_codes": ["SENSITIVE_SITE", "RIGHTS_UNCLEAR"],
  "obligations": [
    { "type": "generalize_geometry", "min_cell_size_m": 5000 },
    { "type": "remove_attributes", "fields": ["exact_location", "owner_name"] }
  ],
  "evaluated_at": "2026-02-20T12:00:00Z",
  "rule_id": "deny.restricted_dataset.default"
}
```

### Example policy (illustrative)
A minimal example rule set:

- **steward** can do anything
- **public** can `read` only when `policy_label == "public"`
- an **obligation** is emitted for `public_generalized` to tell the UI to show a notice

```rego
# policy/rego/kfm.rego
package kfm.authz

default allow = false

# Input shape:
# input.user.role
# input.resource.policy_label
# input.action

allow {
  input.user.role == "steward"
}

allow {
  input.user.role == "public"
  input.action == "read"
  input.resource.policy_label == "public"
}

# Obligations: if dataset is public_generalized, record obligation for UI notice
obligations[o] {
  input.resource.policy_label == "public_generalized"
  o := {"type": "show_notice", "message": "Geometry generalized due to policy."}
}
```

---

## Starter controlled vocabulary
KFM expects policy labels to be **controlled**, versioned, and validated (don’t let arbitrary strings drift into catalogs, APIs, or UI).

Starter `policy_label` list:
- `public`
- `public_generalized`
- `restricted`
- `restricted_sensitive_location`
- `internal`
- `embargoed`
- `quarantine`

> Tip: if you add a new label, treat it as a governed change:
> update the vocabulary, add fixtures, and add tests that cover both “allow” and “deny” behavior.

---

## How to run tests
From the repo root:

```bash
opa test ./examples/sample_policy/policy -v
```

If you want “only this pack” while developing:

```bash
cd examples/sample_policy
opa test ./policy -v
```

### Example tests (illustrative)
```rego
# policy/tests/kfm_test.rego
package kfm.authz_test

import data.kfm.authz

test_public_can_read_public {
  authz.allow with input as {
    "user": {"role": "public"},
    "action": "read",
    "resource": {"policy_label": "public"}
  }
}

test_public_cannot_read_restricted {
  not authz.allow with input as {
    "user": {"role": "public"},
    "action": "read",
    "resource": {"policy_label": "restricted"}
  }
}
```

---

## How to wire into CI
This sample assumes only one hard requirement:

- **Policy tests must run in CI and block merges.**

### GitHub Actions example (drop-in snippet)
```yaml
name: policy
on:
  pull_request:

jobs:
  opa-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      # Option A: install OPA yourself (pin versions in real repos)
      # - run: curl -L -o opa https://openpolicyagent.org/downloads/latest/opa_linux_amd64
      # - run: chmod +x ./opa && sudo mv ./opa /usr/local/bin/opa

      # Option B: use a setup action (pin a version)
      - uses: open-policy-agent/setup-opa@v2
        with:
          version: 0.63.0

      - run: opa test ./examples/sample_policy/policy -v
```

Then enforce:
- the `policy / opa-test` check is **required**
- merges are blocked if it fails

---

## Extending the sample

### Add a new role
1. Add fixture for the role (e.g., `policy/fixtures/reviewer_user.json`)
2. Add allow/deny rules in `kfm.rego`
3. Add unit tests demonstrating:
   - at least one allowed scenario
   - at least one denied scenario

### Add a new policy label
1. Add the label to the controlled vocabulary (wherever your repo keeps vocab)
2. Add fixtures for datasets under that label
3. Add tests that prove:
   - policy denies by default
   - policy only allows under explicit conditions
   - obligations are returned when required

### Add an obligation
Common obligation patterns KFM expects to show up in decisions:
- `show_notice` (UX disclosure)
- `generalize_geometry` (sensitive location mitigation)
- `remove_attributes` (PII / sensitive field stripping)

> IMPORTANT: obligations are not “documentation.” They are enforcement instructions and must be reflected in downstream transforms and UI behavior.

---

## Sensitive location release pattern
For datasets like archaeology or sensitive species, KFM’s recommended pattern is:

1. **Classification:** `restricted_sensitive_location`
2. **Dual outputs:**
   - restricted precise dataset version
   - public_generalized dataset version (only if any public representation is allowed)
3. **Generalization method:** choose and document (grid aggregation, dissolve, etc.)
4. **Testing:** confirm no precise coordinates leak
5. **UX notice:** UI indicates generalization and reason
6. **Governance review:** designated authority approves release criteria

This sample pack only demonstrates the *policy label + obligation concept*; you still need:
- data transforms that actually generalize/redact
- leakage tests that validate outputs

---

## Definition of Done
Use this as a minimal merge gate for policy-as-code.

### Policy pack DoD
- [ ] Default deny posture is in place (`default allow = false`)
- [ ] All `policy_label` values come from a controlled vocabulary
- [ ] Fixtures exist for each label that the runtime intends to support
- [ ] Unit tests cover:
  - [ ] public allow case (public dataset)
  - [ ] public deny case (restricted dataset)
  - [ ] steward allow case
  - [ ] obligations case (public_generalized)
- [ ] CI runs `opa test` and blocks merges on failures
- [ ] Policy change PRs require governance review (CODEOWNERS or equivalent)

### Promotion gate alignment
When used as part of promotion, ensure promotion is blocked unless:
- policy label is assigned,
- obligations are applied where required,
- default-deny tests pass.

---

## Notes and limitations
- This is an **illustrative** policy: it does not encode rights metadata or licensing constraints.
- It does not implement “policy-safe errors” (avoid leaking existence of restricted datasets via error text/timing).
- It does not implement runtime PEP logic (enforcement in API, evidence resolver, or UI).

If you adopt this pattern in production:
- pin tool versions (OPA, test runners),
- treat policy changes as behavior changes,
- require review and regression tests on every policy update.
