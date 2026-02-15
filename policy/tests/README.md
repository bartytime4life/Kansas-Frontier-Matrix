# KFM Policy Test Suite

**Path:** `/policy/tests`

[![Policy tests](https://img.shields.io/github/actions/workflow/status/<ORG>/<REPO>/policy-tests.yml?branch=main&label=policy%20tests&style=flat-square)](https://github.com/<ORG>/<REPO>/actions/workflows/policy-tests.yml)
[![OPA](https://img.shields.io/badge/OPA-OPA_VERSION-blue?style=flat-square)](#tooling)
[![Conftest](https://img.shields.io/badge/Conftest-CONFTEST_VERSION-informational?style=flat-square)](#tooling)
[![Governance](https://img.shields.io/badge/governance-fail--closed-critical?style=flat-square)](#non-negotiables-these-tests-enforce)
[![Focus Mode](https://img.shields.io/badge/focus-cite--or--abstain-ff69b4?style=flat-square)](#non-negotiables-these-tests-enforce)
[![Trust membrane](https://img.shields.io/badge/trust--membrane-enforced-success?style=flat-square)](#non-negotiables-these-tests-enforce)

> [!IMPORTANT]
> This directory exists to make KFM governance **enforceable**, **reviewable**, and **non-regressing**.  
> Policy changes are *production changes*.
>
> **Fail-closed by default** is required: if inputs/metadata/provenance are missing or invalid, the system must deny (or abstain) rather than guess.

---

## Table of Contents

- [Why this exists](#why-this-exists)
- [What “policy” means in KFM](#what-policy-means-in-kfm)
- [Non-negotiables these tests enforce](#non-negotiables-these-tests-enforce)
- [Directory layout](#directory-layout)
- [Tooling](#tooling)
- [Running tests locally](#running-tests-locally)
- [Test categories and required coverage](#test-categories-and-required-coverage)
  - [OPA unit tests](#opa-unit-tests)
  - [Conftest fixture tests](#conftest-fixture-tests)
  - [CI policy regression suite](#ci-policy-regression-suite)
  - [Schema and input-contract tests](#schema-and-input-contract-tests)
  - [Optional API contract and smoke tests](#optional-api-contract-and-smoke-tests)
- [How to add a new policy rule safely](#how-to-add-a-new-policy-rule-safely)
- [How to add a new regression test](#how-to-add-a-new-regression-test)
- [CI integration](#ci-integration)
- [Debugging and troubleshooting](#debugging-and-troubleshooting)
- [Security and privacy rules for test data](#security-and-privacy-rules-for-test-data)
- [Governance checklist](#governance-checklist)
- [Appendix: Canonical fixture shapes](#appendix-canonical-fixture-shapes)
- [Appendix: Badge configuration](#appendix-badge-configuration)

---

## Why this exists

KFM is an evidence-first platform where credibility and safety depend on:

- policy enforcement that cannot be bypassed, and
- policy behavior that does not drift over time.

Policy tests are designed to:

- Prevent regressions that re-introduce sensitive-data leakage.
- Enforce **cite-or-abstain** behavior for Focus Mode outputs.
- Ensure dataset publishing/promotion and access control are consistently gated.
- Guarantee auditability (every decision can be traced to policy + inputs + evidence).

---

## What “policy” means in KFM

KFM uses policy-as-code to enforce governance at two levels:

1. **Runtime access decisions**  
   Examples: “May this actor access this dataset/field/precision level?” “May this AI answer be returned (citations + sensitivity OK)?”

2. **CI/CD merge gates**  
   Examples: “Is this dataset allowed to be promoted/published?” “Do the required catalogs/receipts/attestations exist?” “Are Story Nodes and citations valid?”  
   These are *merge-blocking* to prevent shipping non-compliant artifacts.

> [!NOTE]
> The same Rego policies (or closely related policy packs) may be evaluated:
>
> - in CI (static fixtures / file scanning), and/or
> - at runtime (OPA sidecar / embedded evaluation).

---

## Non-negotiables these tests enforce

These are “must remain true” invariants for KFM:

- **Trust membrane**: external clients/UI never access databases directly; access is only through the governed API boundary.
- **Fail-closed policy**: missing keys/metadata/claims must deny by default.
- **Dataset promotion gates**: promotion/publishing requires the required governance artifacts (catalogs + provenance).
- **Focus Mode**: answers must **cite evidence or abstain**.
- **Sensitivity handling**: restricted and sensitive-location data must be redacted/generalized unless explicitly authorized.
- **Audit integrity**: responses/decisions must carry audit references and evidence identifiers so they are inspectable later.

---

## Directory layout

This README assumes the repository follows a standard KFM policy layout.

```text
policy/
├─ README.md                               # (Optional) Policy overview: principles, “default deny”, and how policy is used
├─ bundles/                                # Optional built OPA bundles (CI-generated; deployable artifacts)
│
├─ kfm/                                    # Rego packages (runtime + CI source of truth)
│  ├─ ai.rego                              # Focus Mode gate (cite-or-abstain + output contract checks)
│  ├─ data_access.rego                     # Data access allow/deny (roles/scopes/sensitivity)
│  ├─ promotion.rego                       # Promotion/publish gates (STAC/DCAT/PROV + digests/receipts)
│  ├─ redaction.rego                       # Redaction rules (precision/field stripping; deny if cannot comply)
│  ├─ audit.rego                           # Audit invariants (required fields + decision metadata)
│  └─ …                                    # Additional modules (licensing, story enforcement, thresholds, etc.)
│
└─ tests/                                  # Policy test harness (OPA + Conftest)
   ├─ README.md                            # ← YOU ARE HERE: how to run tests, fixture rules, and update workflow
   │
   ├─ unit/                                # OPA unit tests (.rego) — fast, hermetic, diff-friendly failures
   │  ├─ ai_test.rego                      # Unit tests for Focus Mode policy
   │  ├─ data_access_test.rego             # Unit tests for data access policy
   │  └─ …                                 # Unit tests for other policy modules
   │
   ├─ fixtures/                            # File-based inputs for conftest/opa eval (synthetic + deterministic)
   │  ├─ allow/                            # Inputs expected to pass (allow=true; with required reasons/metadata)
   │  ├─ deny/                             # Inputs expected to fail (deny=true; fail-closed behavior)
   │  ├─ regression/                       # Multi-issue repro fixtures (ensure specific past bugs never return)
   │  └─ schema/                           # Schema-validated fixture inputs (shape/required fields coverage)
   │
   ├─ golden/                              # “Never regress” cases from prior incidents (highest review bar)
   │  └─ leak_cases/                       # Leakage scenarios (token/PII/sensitive fields) that must always block/redact
   │
   └─ expected/                            # Optional expected outputs (snapshots/redacted payloads/decision envelopes)
```

> [!TIP]
> If your repo structure differs, keep the **intent** constant:
>
> - tests are separated into **unit**, **fixtures**, and **golden non-regression** sets, and
> - CI runs all of them on every PR.

---

## Tooling

Minimum tools to run this suite:

- **OPA** (Open Policy Agent) for evaluating and unit-testing Rego.
- **Conftest** for asserting policy compliance against files/fixtures in CI.

Recommended additional tooling (depends on how your CI is wired):

- JSON Schema validator (for policy input contracts and governed artifacts).
- A “receipt/citation validator” and link checker (for evidence resolution).
- Supply-chain verification tools (if acceptance harness includes them).

> [!IMPORTANT]
> Pin tool versions in CI and in local dev instructions.  
> Policy and tooling are part of the security boundary—silent behavior changes are unacceptable.

---

## Running tests locally

From the repo root:

### 1) Run OPA unit tests

```bash
opa test ./policy -v
```

### 2) Run Conftest tests against fixtures

```bash
conftest test ./policy/tests/fixtures -p ./policy
```

### 3) Run “golden” non-regression tests (must always pass)

```bash
conftest test ./policy/tests/golden -p ./policy
```

### Optional: run everything (recommended)

If your repo has a `Makefile`, add a standard target (recommended):

```makefile
policy-test:
	opa test ./policy -v
	conftest test ./policy/tests/fixtures -p ./policy
	conftest test ./policy/tests/golden -p ./policy
```

Then:

```bash
make policy-test
```

---

## Test categories and required coverage

### OPA unit tests

OPA unit tests are **logic-level** tests for policy modules.

Required characteristics:

- Cover both **allow** and **deny** paths.
- Assert **default deny** behavior (i.e., no missing-key “implicit allow”).
- Use minimal fixtures and explicit inputs.

**Example pattern** (illustrative):

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
```

> [!NOTE]
> If your policies are Conftest-style `deny[msg]`, keep unit tests focused on the decision surface your API/CI uses.  
> You can also unit-test `deny` length (`count(deny) == 0` / `> 0`) if that’s your chosen contract.

---

### Conftest fixture tests

Conftest is best for **file-based governance gates**, like:

- dataset metadata files
- DCAT/STAC/PROV artifacts
- run receipts / manifests
- Story Nodes / governed Markdown front matter
- API response envelopes (as JSON fixtures)

Required characteristics:

- Fixtures must be clearly organized into **allow** and **deny** cases.
- Every deny case should include an expected violation message (or stable reason).
- Prefer small, readable fixtures over huge real-world files.

---

### CI policy regression suite

This is the “never again” suite.

At minimum, keep these as permanent test classes:

1. **Golden non-regression leak tests**
   - If a prior incident/bug leaked restricted fields, the exact case becomes a golden fixture and must fail forever.

2. **Negative tests for sensitive-location precision**
   - Ensure sensitive-location layers cannot be returned at high precision to unauthorized roles.
   - Include cases where the UI attempts to request “precise geometry” without a grant.

3. **Field-level redaction tests**
   - Verify restricted fields (owner names, small-count health, precise archaeology coordinates, etc.) are redacted or generalized as required.

4. **Audit integrity tests**
   - Assert that policy-governed outputs include:
     - `audit_ref`
     - an evidence identifier (e.g., evidence bundle digest/hash)
   - If absent, deny / fail.

> [!IMPORTANT]
> Treat this regression suite as part of the *security boundary*.  
> Deleting or weakening golden tests requires governance review + explicit approval.

---

### Schema and input-contract tests

Policies should not accept “whatever JSON happens to arrive.”

Required:

- Validate that policy inputs match the expected shape.
- Missing keys must cause deny, not “null-tolerant allow.”

Recommended approach:

- Keep canonical input-shape fixtures in `policy/tests/fixtures/schema/`.
- Add policy rules that explicitly check required keys/types.
- Unit test these checks.

---

### Optional API contract and smoke tests

If the repo includes integration tests that hit a running API:

- Assert that representative endpoints:
  - respect access control decisions
  - enforce redaction/generalization
  - include audit references and evidence IDs
  - support evidence resolution for citations (if applicable)

> [!NOTE]
> If API contract tests live elsewhere (e.g., `/api/tests`), keep **policy-owned fixtures** here and link to them.

---

## How to add a new policy rule safely

1. **Decide the policy contract**
   - What is the input?
   - What is the decision surface? (`allow`, `deny[msg]`, structured decision object, etc.)
   - What data classifications apply?

2. **Add unit tests first**
   - At least one allow case + one deny case.
   - Add “missing key” tests to ensure fail-closed.

3. **Add fixture tests**
   - Put minimal JSON/YAML fixtures under `fixtures/allow` and `fixtures/deny`.

4. **Add or extend regression coverage if the change fixes an incident**
   - Add a golden test that would have caught the issue.

5. **Run locally**
   - `opa test ./policy -v`
   - `conftest test ./policy/tests -p ./policy`

6. **Document the change**
   - Short explanation in PR description and/or policy module header comment.

---

## How to add a new regression test

Use this template:

- `policy/tests/golden/<incident_id_or_short_name>/input.json`
- `policy/tests/golden/<incident_id_or_short_name>/README.md` *(optional but recommended)*

The golden fixture should:

- reproduce the leak/bypass/unsafe output in a minimal way
- assert the correct **deny** behavior (or abstain behavior)
- include a short “why this exists” note

---

## CI integration

Policy tests are merge-blocking.

Minimum recommended CI steps:

1. Install pinned versions of:
   - `opa`
   - `conftest`

2. Run:
   - `opa test ./policy -v`
   - `conftest test ./policy/tests/fixtures -p ./policy`
   - `conftest test ./policy/tests/golden -p ./policy`

Example GitHub Actions step (illustrative):

```yaml
- name: Policy tests
  run: |
    opa test ./policy -v
    conftest test ./policy/tests/fixtures -p ./policy
    conftest test ./policy/tests/golden -p ./policy
```

> [!IMPORTANT]
> CI should be configured to fail on policy violations.  
> If an emergency “deny switch” (kill-switch) exists, include tests that verify it works and is default-deny safe.

---

## Debugging and troubleshooting

### Print decisions for a single fixture

```bash
opa eval -d ./policy -i ./policy/tests/fixtures/deny/example.json "data.kfm.ai"
```

### Common failure modes

- **Unexpected allow**: you forgot `default allow := false`, or a rule isn’t scoped/guarded.
- **Missing key tolerated**: you need explicit input validation checks (or a schema gate).
- **Conftest finds nothing**: wrong policy path (`-p`) or packages don’t expose the expected rule names.
- **Regression fixture stopped failing**: you weakened a deny rule, or a “sanitize” path returned partial data unexpectedly.

---

## Security and privacy rules for test data

- **Never commit real secrets** (API keys, tokens, cookies).
- **Never commit real PII** (names, addresses, personal identifiers), even in “test-only” fixtures.
- Use synthesized or obviously fake values:
  - `"owner_name": "REDACTED_TEST_VALUE"`
  - `"lat": 0.0, "lon": 0.0` (or a safe dummy area)
- For sensitive-location tests, encode the *precision policy intent*, not the real site.

---

## Governance checklist

Use this checklist in PRs that touch `policy/`:

- [ ] Added/updated OPA unit tests (allow + deny paths)
- [ ] Added/updated fixture tests (Conftest and/or OPA eval fixtures)
- [ ] Added a golden regression test if fixing a leak/bypass/unsafe output
- [ ] Verified fail-closed behavior for missing keys/unknown roles
- [ ] Verified sensitive-location and restricted-field redaction/generalization
- [ ] Verified audit integrity expectations (audit ref + evidence id/hash)
- [ ] Verified CI runs the policy suite and is merge-blocking
- [ ] Governance reviewer sign-off for policy surface changes

---

## Appendix: Canonical fixture shapes

> [!NOTE]
> These are *recommended* shapes. Align them to the repo’s actual schemas if they differ.

### A) Dataset access decision input (illustrative)

```json
{
  "actor": { "role": "public|reviewer|admin", "scopes": ["..."] },
  "resource": {
    "kind": "dataset",
    "dataset_id": "ds_...",
    "sensitivity": "public|restricted|sensitive-location|aggregate-only"
  },
  "request": { "endpoint": "/api/v1/datasets/query" }
}
```

### B) Focus Mode output decision input (illustrative)

```json
{
  "answer": {
    "text": "…",
    "has_citations": true,
    "citations": [{ "id": "c1", "ref": "…" }],
    "sensitivity_ok": true
  }
}
```

### C) API response envelope fixture (audit integrity)

```json
{
  "data": { "…": "…" },
  "audit_ref": "audit_2026_...",
  "evidence_bundle": {
    "digest": "sha256:..."
  }
}
```

---

## Appendix: Badge configuration

> [!TIP]
> The badges at the top of this README are intentionally **safe placeholders**.
> Replace `<ORG>`, `<REPO>`, and workflow/tool versions with your repo’s real values.

### 1) GitHub Actions badge (policy tests)

- Update: `policy-tests.yml` → your workflow filename.
- Update: `main` → your default branch.

```text
https://img.shields.io/github/actions/workflow/status/<ORG>/<REPO>/policy-tests.yml?branch=main&label=policy%20tests&style=flat-square
```

### 2) Tool version badges (OPA / Conftest)

These are “informational” badges until you wire them to a real version source.

- Option A (static): replace `OPA_VERSION` and `CONFTEST_VERSION`.
- Option B (dynamic): point Shields to a raw JSON file in your repo (recommended once you have one).

Static examples:

```text
https://img.shields.io/badge/OPA-OPA_VERSION-blue?style=flat-square
https://img.shields.io/badge/Conftest-CONFTEST_VERSION-informational?style=flat-square
```

Dynamic JSON example (requires you to publish a `policy/tool-versions.json` or similar):

```text
https://img.shields.io/badge/dynamic/json?url=https://raw.githubusercontent.com/<ORG>/<REPO>/main/policy/tool-versions.json&query=$.opa&label=OPA&color=blue
```

> [!NOTE]
> If you add a `tool-versions.json`, treat it as a governed artifact:
> pin values, review changes, and run policy tests on every PR.
