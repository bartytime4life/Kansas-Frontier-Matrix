<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/c07d6347-22d6-4e48-b19f-be2bcc0592b4
title: configs/contracts
type: standard
version: v1
status: draft
owners: TBD
created: 2026-02-24
updated: 2026-02-24
policy_label: public
related:
  - ../../schemas/
  - ../../policy/
  - ../../docs/governance/
tags: [kfm, contracts, schemas, policy-as-code]
notes:
  - This README defines how contract artifacts are organized and validated.
  - If your repo uses a different canonical contract home (e.g., /schemas), keep this README but update the “Directory layout” section to match reality.
[/KFM_META_BLOCK_V2] -->

# Contracts

Contract artifacts that define what the system is allowed to ingest, promote, serve, and render.

**Status:** draft  
**Owners:** TBD (assign a steward + policy engineer)  

![status](https://img.shields.io/badge/status-draft-orange)
![contracts](https://img.shields.io/badge/contracts-contract--first-blue)
![gates](https://img.shields.io/badge/gates-fail--closed-critical)
![policy](https://img.shields.io/badge/policy-OPA%20%2F%20Rego-informational)
![schemas](https://img.shields.io/badge/schemas-JSON%20Schema%202020--12-informational)

---

## Navigation

- [Why this directory exists](#why-this-directory-exists)
- [What belongs here](#what-belongs-here)
- [What must not go here](#what-must-not-go-here)
- [Directory layout](#directory-layout)
- [Contract rules](#contract-rules)
- [Validation and CI gates](#validation-and-ci-gates)
- [Versioning and compatibility](#versioning-and-compatibility)
- [Change workflow](#change-workflow)
- [Definition of done](#definition-of-done)
- [Appendix: templates](#appendix-templates)

---

## Why this directory exists

KFM treats **contracts** (schemas + policy rules + interface definitions) as the foundation of *fail-closed* governance.

If an artifact does not conform to its contract, it is **not trusted** and should not be:
- signed/attested,
- promoted to “Published,”
- served through governed APIs,
- rendered with “green/trusted” UI affordances.

> **NOTE**
> In KFM, contracts are part of the “trust membrane.” They must be reviewable, versioned, and enforceable in both **CI** and **runtime**.

[Back to top](#contracts)

---

## What belongs here

This directory is the canonical home for **machine-verifiable** contract artifacts and their fixtures.

| Contract surface | What it governs | Typical artifact types | Typical gate(s) |
|---|---|---|---|
| Pipeline receipts | What a run must emit (inputs/outputs/checks/digests) | JSON Schema + example fixtures | Schema validate + policy test |
| Promotion manifests | What “publish intent” must include (rights, digests, attest refs) | JSON Schema + example fixtures | Schema validate + policy test |
| Watchers / fetchers allow-list | Which automations are allowed to run | JSON Schema + signed registry entries | Schema validate + signature verify |
| Catalog profiles | Required keys and invariants for DCAT/STAC/PROV | JSON Schema / profiles / validators | Schema validate + policy test |
| API contract | Stable request/response shapes and error model | OpenAPI / GraphQL schema / DTO schema | Contract tests + version checks |
| Policy packs | Allow/deny rules for promotion + serving + UI safety | Rego policies + unit tests | Conftest/OPA tests (deny-by-default) |

[Back to top](#contracts)

---

## What must not go here

**Do not** store these in `configs/contracts/`:

- Raw or processed datasets (those belong in data zones, not contracts)
- Secrets, tokens, private keys, or credentials
- Personally identifying information (PII) or sensitive location coordinates
- “Example” fixtures that are not safe to publish (fixtures must be policy-safe)
- One-off scripts or ad-hoc notes (place in `tools/` or `docs/` as appropriate)

> **WARNING**
> Contracts are high-leverage. A “small” change here can silently widen what the system allows.
> Treat every contract change like production code.

[Back to top](#contracts)

---

## Directory layout

> This is the **recommended** structure. If your repo differs, update this tree to match reality.

```text
configs/
└─ contracts/                                       # Contract surfaces (schemas + policy + smoke tests)
   ├─ README.md                                     # What contracts exist, versioning, and CI enforcement (fail-closed)
   │
   ├─ schemas/                                      # Machine-validated schemas (inputs/outputs/registries/catalogs/api)
   │  ├─ run_receipt/                               # Run receipt schema family (promotion evidence)
   │  │  ├─ v1.schema.json                          # Run receipt v1 JSON Schema
   │  │  └─ examples/
   │  │     ├─ run_receipt.valid.json               # Minimal valid example (must pass)
   │  │     └─ run_receipt.invalid.missing_spec_hash.json # Invalid example (must fail)
   │  │
   │  ├─ run_manifest/                              # Run manifest schema family (run envelope / promotion receipt)
   │  │  ├─ v1.schema.json
   │  │  └─ examples/
   │  │     └─ …                                    # Valid/invalid examples (must pass/fail accordingly)
   │  │
   │  ├─ watcher_registry/                          # Watcher registry schema family (signed registry objects)
   │  │  ├─ v1.schema.json
   │  │  ├─ examples/
   │  │  └─ signatures/
   │  │     └─ README.md                            # Signature format + verification expectations (keys not stored here)
   │  │
   │  ├─ catalogs/                                  # Catalog schemas/profiles (minimums + constraints)
   │  │  ├─ dcat/                                   # DCAT constraints/schemas (as used by KFM)
   │  │  ├─ stac/                                   # STAC constraints/schemas (as used by KFM)
   │  │  └─ prov/                                   # PROV constraints/schemas (as used by KFM)
   │  │
   │  └─ api/                                       # API boundary contracts
   │     ├─ openapi/
   │     │  └─ v1.openapi.yaml                      # REST contract snapshot (OpenAPI 3.1)
   │     └─ graphql/
   │        └─ schema.graphql                       # Optional GraphQL SDL snapshot
   │
   ├─ policy/                                       # Contract-gate policy used by CI (OPA/Rego)
   │  ├─ opa/
   │  │  ├─ receipt.rego                            # Receipt policy checks (required fields, invariants)
   │  │  ├─ catalogs.rego                           # Catalog minimums checks (STAC/DCAT/PROV cross-links)
   │  │  ├─ api.rego                                # API contract policy checks (required headers/error envelopes, etc.)
   │  │  └─ _test.rego                              # OPA unit tests for these policies (opa test …)
   │  └─ fixtures/
   │     ├─ allow/                                  # Inputs expected to pass (allow=true)
   │     └─ deny/                                   # Inputs expected to fail (deny=true)
   │
   └─ tests/                                        # Smoke/contract harnesses (CI-friendly, fail-closed)
      └─ contract_smoke/
         └─ README.md                               # How smoke tests run + what constitutes a blocking failure
```

[Back to top](#contracts)

---

## Contract rules

### 1) Fail closed by default

- Schemas should be strict:
  - `additionalProperties: false` (unless there is a deliberate extension mechanism)
  - explicit `required` keys for anything governance depends on
- Policies should be strict:
  - default deny (`allow = false`) and only allow when all invariants pass

### 2) Contracts must be enforceable in CI and runtime

CI guarantees are meaningless if runtime evaluates different rules.
- Keep policy semantics aligned between CI gates and runtime policy decisions.
- Store test fixtures beside the contracts so regressions are caught early.

### 3) No “ghost metadata” leaks

Contracted error models and policy behavior must avoid leaking restricted existence:
- use policy-safe messages,
- avoid “403 vs 404 tells you it exists” behavior unless explicitly allowed by policy.

### 4) Deterministic IDs and hashes where required

Where a contract includes identifiers/hashes (e.g., `spec_hash`, digests, attestation URIs):
- the hashing inputs must be documented and canonicalized,
- fixtures must include both pass and fail cases.

[Back to top](#contracts)

---

## Validation and CI gates

### Local validation

You should be able to validate contracts locally before pushing.

```bash
# Example: policy checks (deny-by-default)
conftest test configs/contracts/schemas/run_receipt/examples/run_receipt.valid.json \
  --policy configs/contracts/policy/opa

# Example: validate JSON Schema (choose one tool; keep it consistent repo-wide)
# python -m jsonschema -i <instance.json> <schema.json>
# ajv validate -s <schema.json> -d <instance.json>
```

### CI expectations

At minimum, CI should:

- Validate every example fixture against its schema
- Run Conftest/OPA tests against fixtures (both allow and deny)
- Verify signatures for any signed registry inputs (e.g., watcher allow-list)
- Block merge if a “kill switch” is active (fail-closed emergency stop)

> **TIP**
> Add a small “contract smoke” job that runs fast and is required on every PR touching this directory.

[Back to top](#contracts)

---

## Versioning and compatibility

### Contract versioning

- Treat each contract as versioned: `v1`, `v2`, etc.
- Breaking changes require a **new version** and a migration plan.
- Keep old versions readable as long as there are producers/consumers that still emit/expect them.

### API versioning

- Freeze `/api/v1` semantics and only add backwards-compatible fields.
- Introduce `/api/v2` only for breaking changes.
- The OpenAPI/GraphQL spec is the contract; breaking it requires a version bump.

[Back to top](#contracts)

---

## Change workflow

When you change any contract artifact:

1. **Explain intent**  
   - What are we allowing/denying now that we didn’t before?

2. **Update schema/policy**  
   - Make the smallest possible change that achieves the intent.

3. **Add fixtures**  
   - At least one **valid** and one **invalid** fixture covering the change.

4. **Update tests**  
   - Add or adjust `_test.rego` or contract smoke tests to lock behavior.

5. **Version decision**  
   - If breaking: create a new `vN` contract and document migration.

6. **Review as governance**  
   - Treat as high-risk: require steward review.

[Back to top](#contracts)

---

## Definition of done

- [ ] A schema exists for every governed artifact type we emit/serve
- [ ] Each schema has:
  - [ ] at least one valid fixture
  - [ ] at least one invalid fixture
  - [ ] strictness documented (e.g., extension points)
- [ ] Policies are deny-by-default and have:
  - [ ] unit tests (`_test.rego`)
  - [ ] allow/deny fixtures
- [ ] CI fails if fixtures do not validate or policies deny
- [ ] Signature verification is enforced where registries are signed
- [ ] Versioning rules are followed and migrations documented

[Back to top](#contracts)

---

## Appendix: templates

<details>
<summary><strong>JSON Schema skeleton</strong></summary>

```json
{
  "$id": "https://kfm.example/schemas/<name>.v1.json",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "<Title>",
  "type": "object",
  "additionalProperties": false,
  "required": ["..."],
  "properties": {
    "...": { "type": "string" }
  }
}
```

</details>

<details>
<summary><strong>Rego policy skeleton</strong></summary>

```rego
package kfm.contracts.example

default allow = false

deny[msg] {
  # add conditions
  msg := "explain why (policy-safe)"
}

allow {
  count(deny) == 0
}
```

</details>

<details>
<summary><strong>Stable error model fields</strong></summary>

Use a stable error shape across governed APIs:

- `error_code`
- `message` (policy-safe)
- `audit_ref`
- optional remediation hints (safe suggestions)

</details>
