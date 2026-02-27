<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/ed1cc6bc-7df0-4675-ad33-29b423c572ca
title: Policy Fixtures
type: standard
version: v1
status: draft
owners: TODO
created: 2026-02-27
updated: 2026-02-27
policy_label: internal
related:
  - apps/api/src/policy/
  - apps/api/src/policy/fixtures/
tags: [kfm, policy, fixtures]
notes:
  - Deterministic allow/deny + obligation fixtures used to keep CI and runtime policy semantics aligned.
  - Keep this README synced with the directory contents and the policy adapter contract.
[/KFM_META_BLOCK_V2] -->

# Policy fixtures

Deterministic **allow/deny + obligations** test cases for the API policy boundary.

![Status](https://img.shields.io/badge/status-draft-yellow)
![Scope](https://img.shields.io/badge/scope-api%2Fpolicy%2Ffixtures-blue)
![Merge%20Gate](https://img.shields.io/badge/merge%20gate-fail--closed-critical)
![Determinism](https://img.shields.io/badge/tests-deterministic-important)

---

## Navigation

- [Purpose](#purpose)
- [Where this fits](#where-this-fits)
- [Directory contract](#directory-contract)
- [Suggested layout](#suggested-layout)
- [Fixture format](#fixture-format)
- [Policy labels](#policy-labels)
- [Obligations](#obligations)
- [Running the fixture suite](#running-the-fixture-suite)
- [Adding or changing fixtures](#adding-or-changing-fixtures)
- [Definition of done for a fixture PR](#definition-of-done-for-a-fixture-pr)
- [Appendix: examples](#appendix-examples)

---

## Purpose

This directory exists to make policy behavior:

1. **Testable** — every important decision has a reproducible input → output case.
2. **Stable** — changes to policy are reviewed via diffs to fixture outcomes.
3. **Aligned across environments** — the same semantics are enforced in **CI** and in the **runtime API**.
4. **Auditable** — fixtures document why a decision is allow/deny and what obligations must be surfaced.

> **Key idea:** CI policy checks are only meaningful if runtime policy behavior matches them. Fixtures are
> the smallest shared artifact that enforces that parity.

---

## Where this fits

```mermaid
flowchart LR
  subgraph CI["CI (merge gate)"]
    F["Fixtures (this directory)"]
    P["Policy bundle (OPA/Rego or equivalent)"]
    T["Policy test runner"]
    F --> T
    P --> T
    T -->|pass| M["Merge allowed"]
    T -->|deny (fail closed)| B["Merge blocked"]
  end

  subgraph RT["Runtime (governed API)"]
    API["API endpoints"]
    PDP["Policy Decision Point (PDP)"]
    PEP["Policy Enforcement Point (PEP)"]
    API --> PEP --> PDP --> PEP --> API
  end

  subgraph UI["UI surfaces"]
    U["Map / Story / Focus"]
  end

  P -. "same policy bundle" .-> PDP
  F -. "same fixture semantics" .-> PDP
  PDP -->|"decision + obligations"| U
  U -->|"requests"| API
```

**Rule of thumb**

- **PDP** answers “is this allowed?” and “what obligations apply?”
- **PEP** enforces the answer (CI gate, API gate, evidence resolver gate, etc.)
- The **UI never decides policy**; it only renders the decision and obligations.

---

## Directory contract

### Acceptable inputs

This directory may contain:

- Machine-readable fixture files describing:
  - **input** to the policy engine
  - **expected** decision (`allow` / `deny`)
  - **expected** obligations (array)
- Fixture registries / indexes that make the suite easy to enumerate and review
- README / docs explaining fixture semantics and how to run them

### Exclusions

Do **not** commit any of the following:

- **Secrets** (tokens, passwords, API keys), even for “test” environments
- **Real PII** or “close-to-real” PII (use synthetic test identities)
- **Precise sensitive locations** (use synthetic geometries or coarse placeholders)
- External network dependencies (fixtures must run offline and deterministically)
- Vendor- or environment-specific runtime config (belongs in deployment/config docs)

> ⚠️ **Fail closed:** if a fixture can’t run without extra hidden state, it is not a fixture.

---

## Suggested layout

> This is a *recommended* structure. Keep it in sync with the actual files in this folder.

```text
apps/api/src/policy/fixtures/
├── README.md
├── fixtures.registry.json           # (optional) inventory of fixture ids + purpose
├── authz/                          # allow/deny authorization fixtures
│   ├── *.fixture.json
│   └── *.fixture.yaml
├── obligations/                    # obligations-only cases (UI notices, attribution, etc.)
│   └── *.fixture.json
├── redaction/                      # sensitive-location / PII-related obligations & denials
│   └── *.fixture.json
└── _shared/                        # shared inputs (roles, example resources, helpers)
    └── *.json
```

---

## Fixture format

### Minimal shape (recommended)

A single file per case is easiest to review:

```json
{
  "id": "authz_public_read_public",
  "title": "Public user can read a public resource",
  "input": {
    "user": { "role": "public" },
    "action": "read",
    "resource": { "policy_label": "public" }
  },
  "expect": {
    "decision": "allow",
    "obligations": []
  },
  "notes": [
    "Baseline allow path for unauthenticated/public UI usage."
  ]
}
```

### Input contract (baseline)

Fixtures should keep the *minimum* contract consistent across the suite:

- `input.user.role` — e.g., `public`, `contributor`, `steward`, `operator`
- `input.action` — e.g., `read`, `resolve_evidence`, `download`, `export`
- `input.resource.policy_label` — the classification label used for enforcement

You may extend `input` when needed (e.g., tenant/partner attrs, dataset ids, request context), but keep
extensions **additive** and **documented**.

### Expected output contract (baseline)

- `expect.decision`: `allow` | `deny`
- `expect.obligations`: `Array<object>` — obligations are **machine-readable** instructions for downstream surfaces

---

## Policy labels

> Treat these as a controlled vocabulary. If you introduce a new label, add fixtures for it and ensure
> all enforcement points handle it explicitly.

Starter set:

- `public`
- `public_generalized`
- `restricted`
- `restricted_sensitive_location`
- `internal`
- `embargoed`
- `quarantine`

---

## Obligations

Obligations are how policy communicates “allowed, but…” (and “denied, and explain safely”).

### Common obligation patterns

| Obligation type | When to use | Typical consumer |
|---|---|---|
| `show_notice` | UI must display a notice (e.g., generalization applied) | UI (badge/banner) |
| `require_attribution` | downloads/exports must include attribution/license text | API export/download |
| `generalize_geometry` | return generalized geometry or coarser geography | tiler / API |
| `redact_fields` | suppress specific fields in responses | API serializer |
| `min_count_threshold` | publish only aggregates above a threshold | pipeline / API |
| `no_leakage_in_errors` | ensure 403/404 do not reveal restricted metadata | API error model |

### Obligation shape (recommended)

Keep obligations explicit and enumerable:

```json
{
  "type": "show_notice",
  "code": "GEOMETRY_GENERALIZED",
  "message": "Geometry was generalized due to policy.",
  "audience": "public"
}
```

> ✅ Prefer a stable `code` over parsing `message`.

---

## Running the fixture suite

Because this repo’s toolchain may vary, **treat commands below as examples** and wire them to your
actual scripts (e.g., `apps/api/package.json`).

```bash
# Example: run policy tests from the repo root (adjust for your workspace tool)
# pnpm -C apps/api test:policy
# npm --workspace apps/api run test:policy
# yarn workspace api test:policy
```

Minimum expectation:

- Policy fixtures are executed in CI.
- Failures **block merges** (“fail closed”).
- Output clearly identifies the failing `fixture.id` and the diff between expected and actual results.

---

## Adding or changing fixtures

1. **Name the scenario**: create a stable `id` (treat it as an API contract).
2. **Create the input**: keep it minimal; avoid time-dependent fields.
3. **Define the expected result**:
   - decision (`allow`/`deny`)
   - obligations (if any)
4. **Run the fixture suite locally**.
5. **Add coverage for edge cases** (especially around restricted/sensitive labels).
6. **Update the registry** (if you maintain one).
7. **Review the diff** as a *policy change* (fixtures are governance artifacts).

### Determinism checklist (per fixture)

- [ ] No calls to external services
- [ ] No reliance on `now()` / system time
- [ ] Stable ordering (sort arrays before comparing)
- [ ] Synthetic identifiers only
- [ ] No precise sensitive geometry unless explicitly allowed (prefer synthetic placeholders)

---

## Definition of done for a fixture PR

- [ ] New/changed fixtures run in CI and pass
- [ ] For any new `policy_label`, there is at least:
  - [ ] 1 **allow** case (if it can ever be allowed)
  - [ ] 1 **deny** case
  - [ ] 1 **obligation** case (if applicable)
- [ ] Error cases do not leak restricted metadata (test 403/404 behavior)
- [ ] Fixtures cover the “default deny” baseline (unknown labels/actions deny)
- [ ] README updated if fixture format / contract changes

---

## Appendix: examples

<details>
<summary><strong>Example: deny restricted to public</strong></summary>

```json
{
  "id": "authz_public_read_restricted",
  "title": "Public user cannot read restricted resources",
  "input": {
    "user": { "role": "public" },
    "action": "read",
    "resource": { "policy_label": "restricted" }
  },
  "expect": {
    "decision": "deny",
    "obligations": [
      {
        "type": "no_leakage_in_errors",
        "code": "NO_RESTRICTED_METADATA",
        "message": "Do not reveal whether the resource exists or any restricted metadata."
      }
    ]
  }
}
```

</details>

<details>
<summary><strong>Example: allow public_generalized with notice obligation</strong></summary>

```json
{
  "id": "authz_public_read_public_generalized",
  "title": "Public can read generalized outputs but must see a notice",
  "input": {
    "user": { "role": "public" },
    "action": "read",
    "resource": { "policy_label": "public_generalized" }
  },
  "expect": {
    "decision": "allow",
    "obligations": [
      {
        "type": "show_notice",
        "code": "GEOMETRY_GENERALIZED",
        "message": "Geometry was generalized due to policy."
      }
    ]
  }
}
```

</details>

---

<a id="back-to-top"></a>

[Back to top](#policy-fixtures)
