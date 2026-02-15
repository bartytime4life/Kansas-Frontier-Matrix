# 🧪 Policy Test Fixtures

Deterministic, **synthetic** fixture data used by the KFM policy test suite (OPA/Rego)
and related governance gates.

> [!IMPORTANT]
> **Fixtures MUST be synthetic.** Do not include real sensitive locations, precise
> restricted geometry, private individual data, access tokens, or secrets in this folder.

---

## Table of contents

- [Why this directory exists](#why-this-directory-exists)
- [What belongs here](#what-belongs-here)
- [Directory layout](#directory-layout)
- [Fixture format](#fixture-format)
  - [Required files](#required-files)
  - [Common input shapes](#common-input-shapes)
  - [Expected assertions](#expected-assertions)
- [Examples](#examples)
  - [Focus Mode: cite-or-abstain](#focus-mode-cite-or-abstain)
  - [Data access: dataset sensitivity](#data-access-dataset-sensitivity)
  - [Provenance/run receipt: golden vectors](#provenancerun-receipt-golden-vectors)
- [Adding or updating fixtures](#adding-or-updating-fixtures)
- [Running tests locally](#running-tests-locally)
- [Governance and safety notes](#governance-and-safety-notes)
- [Troubleshooting](#troubleshooting)

---

## Why this directory exists

KFM relies on **policy-as-code** with a **default-deny** posture, and uses policy tests
to prevent regressions in critical governance behavior (data access controls, “cite or
abstain” rules, fail-closed behavior, etc.).:contentReference[oaicite:2]{index=2}:contentReference[oaicite:3]{index=3}

These fixtures exist to keep that test suite:

- **Fast** (small inputs)
- **Deterministic** (no network, no clock drift, no random IDs)
- **Reviewable** (human-readable, minimal, and documented)
- **Non-sensitive** (safe to store in git)

> [!NOTE]
> KFM “boss mode” non-negotiables include: trust membrane, fail-closed policy, dataset
> promotion gates, and Focus Mode cite-or-abstain + audit references.:contentReference[oaicite:4]{index=4}

---

## What belongs here

Fixtures in this directory SHOULD support (at minimum) the following test categories:

- **Policy allow/deny decisions**
  - Example: default-deny; allow only for authorized roles / public data.
- **Focus Mode output validation**
  - Example: **deny** if missing citations; **deny** if sensitivity is not OK.
- **Fail-closed inputs**
  - Missing required keys MUST result in deny (or equivalent safe fallback).
- **Governance regression (“golden”) cases**
  - If a bug allowed an unsafe behavior once, add a fixture so it never ships again.
- **Policy gate tests**
  - Example: “No Source, No Answer” style gates for required artifacts/metadata.
- **Provenance integrity vectors**
  - Example: hash reproducibility “golden vectors” and digest match checks.

These categories are explicitly called out as targets for automated tests and fixtures in
the KFM engineering guidance.:contentReference[oaicite:5]{index=5}

---

## Directory layout

This folder is intentionally simple. Prefer one folder per test case.

```text
policy/tests/fixtures/
├── ai/                         # Focus Mode & AI output governance fixtures
│   └── <case_name>/
│       ├── input.json
│       └── expected.json
├── data/                       # Data access / dataset sensitivity fixtures
│   └── <case_name>/
│       ├── input.json
│       └── expected.json
├── provenance/                 # Receipts, hashes, digests, and “golden vectors”
│   └── <case_name>/
│       ├── input.json
│       └── expected.json
└── README.md                   # This file
```

Naming guidance:

- Use `kebab-case` folder names (example: `deny-without-citations`).
- Make folder names describe the expected behavior (example: `allow-public-dataset`).
- Keep each case minimal: **only** the fields the policy needs.

---

## Fixture format

### Required files

Each fixture case folder MUST include:

- `input.json`  
  The policy input object (what the policy engine evaluates).

- `expected.json`  
  Assertions the test runner checks (the expected allow/deny result, and any required
  additional constraints).

Optional (only when it adds clarity):

- `README.md` inside the case folder  
  Short context + why the case exists (especially for regressions).

> [!TIP]
> Prefer small, synthetic fixtures to keep CI fast and deterministic.:contentReference[oaicite:6]{index=6}

---

### Common input shapes

KFM policies are written in OPA/Rego and commonly evaluate an `input` object.
A recommended (illustrative) policy input shape is:​:contentReference[oaicite:7]{index=7}

```json
{
  "actor": { "role": "public|reviewer|admin", "attributes": {} },
  "request": { "endpoint": "/api/v1/ai/query", "context": {} },
  "answer": {
    "text": "...",
    "has_citations": true,
    "citations": [],
    "sensitivity_ok": true
  }
}
```

Some policies (for data access) may instead center on `resource` + `actor`, e.g.:​:contentReference[oaicite:8]{index=8}

```json
{
  "actor": { "role": "public|reviewer|admin" },
  "resource": { "kind": "dataset", "sensitivity": "public|restricted|confidential" }
}
```

> [!IMPORTANT]
> If the policy contract evolves (new required keys), fixtures MUST be updated in the
> same PR so tests remain meaningful and fail-closed behavior is preserved.:contentReference[oaicite:9]{index=9}

---

### Expected assertions

At minimum, `expected.json` SHOULD assert the allow/deny decision:

```json
{ "allow": true }
```

or

```json
{ "allow": false }
```

Recommended optional assertions (use when your policies expose these signals):

- `deny_reason` (string enum)
- `required_fields_present` (array of required keys)
- `redactions` (array of required redaction operations)
- `audit_ref_required` (boolean)

> [!NOTE]
> Some KFM policies enforce “cite-or-abstain” patterns via a boolean `allow` rule that
> requires citations + sensitivity_ok.:contentReference[oaicite:10]{index=10}

---

## Examples

### Focus Mode: cite-or-abstain

This mirrors the documented pattern: allow only if citations exist and the sensitivity
check passes.:contentReference[oaicite:11]{index=11}

`policy/tests/fixtures/ai/deny-without-citations/input.json`

```json
{
  "actor": { "role": "public", "attributes": {} },
  "request": { "endpoint": "/api/v1/ai/query", "context": {} },
  "answer": {
    "text": "Uncited claim.",
    "has_citations": false,
    "citations": [],
    "sensitivity_ok": true
  }
}
```

`policy/tests/fixtures/ai/deny-without-citations/expected.json`

```json
{
  "allow": false,
  "deny_reason": "missing_citations"
}
```

> [!TIP]
> The KFM blueprint also includes example OPA unit tests that enforce this behavior.
> Use fixtures to keep the test inputs readable as they grow.:contentReference[oaicite:12]{index=12}

---

### Data access: dataset sensitivity

This matches the baseline idea: public data is accessible; non-public data requires
elevated roles (reviewer/admin).:contentReference[oaicite:13]{index=13}

`policy/tests/fixtures/data/allow-public-dataset/input.json`

```json
{
  "actor": { "role": "public" },
  "resource": { "kind": "dataset", "sensitivity": "public" }
}
```

`policy/tests/fixtures/data/allow-public-dataset/expected.json`

```json
{ "allow": true }
```

---

### Provenance/run receipt: golden vectors

KFM guidance recommends keeping fixtures small and synthetic, including “run receipt”
shapes for provenance integrity and policy-gate testing.:contentReference[oaicite:14]{index=14}

`policy/tests/fixtures/provenance/run-receipt-minimal/input.json`

```json
{
  "example": "kfm.run_receipt.v1",
  "fetched_at": "2026-02-13T00:00:00Z",
  "accessURL": "https://example.org/source",
  "etag": "W/\"abc123\"",
  "last_modified": "Wed, 12 Feb 2026 00:00:00 GMT",
  "spec_hash": "sha256:<spec>",
  "artifact_digest": "sha256:<artifact>",
  "tool_versions": { "pipeline": "1.0.0" },
  "policy_gate": {
    "status": "pass",
    "checks": ["license_present", "stac_present"]
  }
}
```

`policy/tests/fixtures/provenance/run-receipt-minimal/expected.json`

```json
{
  "allow": true,
  "required_fields_present": [
    "example",
    "fetched_at",
    "accessURL",
    "spec_hash",
    "artifact_digest",
    "policy_gate.status"
  ]
}
```

---

## Adding or updating fixtures

Use this checklist to keep fixtures consistent and CI-friendly:

- [ ] Fixture uses **synthetic** data only (no secrets, no PII, no restricted precision).
- [ ] Fixture is **minimal**: only fields required for the policy under test.
- [ ] Folder name describes the behavior (ex: `deny-without-citations`).
- [ ] `input.json` and `expected.json` are valid JSON.
- [ ] A **negative** case exists for each critical allow rule (deny should be tested too).
- [ ] For regressions: add a short per-case `README.md` explaining the bug and the fix.
- [ ] Tests pass locally and in CI.

---

## Running tests locally

Exact commands depend on the repo’s test runner (OPA native tests, Conftest, or a
wrapper script). The KFM guidance emphasizes keeping policy tests compatible with
Rego defaults and avoiding silent drift.:contentReference[oaicite:15]{index=15}

Typical commands you may see in this repo:

```bash
# Option A: OPA’s native unit test runner
opa test ./policy -v

# Option B: Conftest (often used to run OPA policies against inputs)
conftest test <target> --policy ./policy
```

> [!TIP]
> If you’re unsure which command is canonical, check CI workflow definitions and mirror
> those locally.

---

## Governance and safety notes

- Treat fixtures as governed artifacts: they should encode the “hard requirements” that
  protect communities and prevent misuse.
- If you need representative geometry, use **generalized or synthetic** shapes.
- If the fixture simulates a restricted dataset, represent it via a **classification field**
  rather than committing real coordinates or real site identifiers.
- If you are testing redaction rules, store **both**:
  - a “public/generalized” representation, and
  - a placeholder for “restricted/precise” (never the real data).

---

## Troubleshooting

<details>
<summary><strong>My fixture isn’t being picked up by tests</strong></summary>

Common causes:

- The test harness is only scanning certain subfolders (example: only `ai/`).
- Folder names don’t match what the harness expects.
- JSON is invalid (missing comma, trailing comments).

Try validating quickly:

```bash
jq . policy/tests/fixtures/<path>/input.json >/dev/null
jq . policy/tests/fixtures/<path>/expected.json >/dev/null
```

</details>

<details>
<summary><strong>Policy tests fail after upgrading OPA/Conftest</strong></summary>

KFM guidance calls out the risk of silent policy failures from syntax/default changes.
Pin versions in CI and add compatibility tests to catch drift early.:contentReference[oaicite:16]{index=16}

</details>
