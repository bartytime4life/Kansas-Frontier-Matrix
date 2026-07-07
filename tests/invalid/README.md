<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-invalid-readme
title: Invalid Tests README
type: test-readme
version: v0.1
status: draft; placeholder-replaced; invalid-test-lane; PROPOSED / NEEDS VERIFICATION
owners:
  - OWNER_TBD - Test steward
  - OWNER_TBD - QA steward
  - OWNER_TBD - Policy steward
  - OWNER_TBD - Evidence steward
  - OWNER_TBD - Release steward
created: 2026-07-06
updated: 2026-07-06
policy_label: public-doc; tests; invalid; fail-closed; no-network; synthetic-only; evidence-aware; policy-aware; release-gated; rollback-aware
tags: [kfm, tests, invalid, fail-closed, negative-tests, validation-failure, ABSTAIN, DENY, ERROR, rollback, correction, trust-spine]
related:
  - ../README.md
  - ../fixtures/README.md
  - ../../fixtures/invalid/README.md
  - ../../contracts/
  - ../../schemas/
  - ../../policy/
  - ../../release/
  - ../../data/
notes:
  - "This README replaces placeholder content at tests/invalid/README.md."
  - "This lane documents invalid/fail-closed test intent. It is not a fixture home, schema home, policy home, contract home, evidence store, release store, or lifecycle data root."
  - "Invalid tests should prove that unsupported, unsafe, stale, conflicted, malformed, or forbidden paths fail closed with finite outcomes."
  - "Executable test files, runner wiring, fixtures consumed, schema bindings, policy/runtime wiring, CI jobs, and pass rates remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Invalid tests

> Test-lane README for invalid and fail-closed tests under `tests/invalid/`. This directory is for executable or test-owned negative checks that prove KFM rejects unsupported, unsafe, malformed, stale, conflicted, or forbidden paths without turning tests into schemas, policies, fixtures, evidence, releases, or source truth.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Lane: invalid tests" src="https://img.shields.io/badge/lane-invalid__tests-critical">
  <img alt="Posture: fail closed" src="https://img.shields.io/badge/posture-fail__closed-critical">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
</p>

**Path:** `tests/invalid/README.md`  
**Status:** draft / placeholder replaced / invalid test lane / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Lane family:** `invalid`  
**Default posture:** deterministic, synthetic, no-network, fail-closed tests only  
**Truth posture:** CONFIRMED target file existed as placeholder content before replacement; CONFIRMED `tests/` is the canonical enforceability root for KFM trust-spine checks; CONFIRMED `fixtures/invalid/` exists as a cross-cutting invalid fixture lane; NEEDS VERIFICATION for executable test inventory, fixture consumption, schema bindings, policy/runtime wiring, CI coverage, and pass rates.

---

## Scope

Use `tests/invalid/` for tests whose primary purpose is to verify that invalid inputs, invalid states, invalid paths, or invalid trust transitions fail closed.

In scope:

- tests for malformed payloads, missing required refs, and schema-validation failures;
- tests for missing evidence, unresolved citation support, and EvidenceRef resolution failures;
- tests for unknown rights, unresolved sensitivity, missing review, stale source, and absent release state;
- tests that prove forbidden direct access to RAW, WORK, QUARANTINE, candidate, canonical, or internal stores fails;
- tests for direct model-client calls, unlisted tile/style/sprite/glyph loads, and public path bypasses;
- tests that expect finite outcomes such as `ABSTAIN`, `DENY`, `ERROR`, validation failure, policy failure, correction-required, or rollback-required.

Out of scope:

- fixture payload storage;
- schema, contract, policy, release, evidence, or lifecycle authority;
- generated CI artifacts;
- production source material;
- app, package, renderer, connector, or model implementation.

[Back to top](#top)

---

## Repo fit

| Responsibility | Correct home | Relationship |
|---|---|---|
| Invalid/fail-closed tests | `tests/invalid/` | This lane. |
| Unit-test-scoped invalid fixtures | `tests/fixtures/` or a specific child lane | Inputs consumed by tests; not owned here. |
| Cross-cutting invalid fixtures | `fixtures/invalid/` | Shared fail-closed examples; not executable tests. |
| Domain invalid tests | `tests/domains/<domain>/` when ownership is domain-specific | Prefer the domain lane when a domain owns the failure. |
| Schema definitions | `schemas/` | Shape authority; tests reference, not define. |
| Contract meaning | `contracts/` | Semantic authority; tests verify, not define. |
| Policy rules | `policy/` | Admissibility authority; tests assert behavior. |
| Release decisions | `release/` | Publication authority; tests can block promotion but do not approve release. |
| Lifecycle data | `data/` roots | Tests must not become lifecycle stores. |

> [!IMPORTANT]
> `tests/invalid/` is a proof lane for failure behavior. It must not become a dumping ground for invalid fixtures, raw data, real sensitive material, schema variants, policy drafts, release records, or generated artifacts.

---

## Invalid-test rule

Invalid tests should make the failure condition visible, deterministic, and reviewable. A passing invalid test should prove that the system refused the unsafe or unsupported path; it should not prove that a claim is true, a source is authoritative, a release is approved, or an output is publishable.

Core expectations:

| Expectation | Required posture |
|---|---|
| Deterministic input | Use synthetic fixtures or toy refs only. |
| No-network default | No live source, API, tile, style, model, vendor, or public-service calls. |
| Fail-closed outcome | Missing support produces `ABSTAIN`, `DENY`, `ERROR`, or validation failure, not silent success. |
| Trust-spine coverage | Tests preserve evidence, policy, review, release, correction, and rollback gates where material. |
| Boundary assertions | Direct internal-store reads, direct frontend model calls, unmanifested tile/style loads, and public admin paths fail. |
| Sensitive safeguards | Sensitive cases use public-safe transformed fixtures and never include real exact sensitive material. |
| Specific ownership | Domain-owned invalid tests should live under `tests/domains/<domain>/` unless intentionally cross-cutting. |

---

## Expected invalid test families

| Family | What it proves | Expected outcome |
|---|---|---|
| `schema_shape_invalid` | Required field, version, enum, or type violation is rejected. | validation failure / `ERROR`. |
| `contract_semantics_invalid` | Payload shape may parse but meaning violates contract semantics. | validation failure / `ABSTAIN`. |
| `evidence_missing` | EvidenceRef fails to resolve to an admissible EvidenceBundle. | `ABSTAIN`. |
| `citation_invalid` | Citation support is missing, stale, or mismatched. | `ABSTAIN` / validation failure. |
| `policy_denied` | Policy refuses unknown rights, unresolved sensitivity, missing review, or restricted detail. | `DENY`. |
| `release_missing` | Public-facing path lacks release, correction, or rollback posture. | `DENY` / validation failure. |
| `direct_store_access` | UI/API/test path attempts RAW, WORK, QUARANTINE, candidate, or internal read. | validation failure / `DENY`. |
| `direct_model_client` | Frontend or public path calls model runtime directly. | validation failure / `DENY`. |
| `unmanifested_map_asset` | Tile/style/sprite/glyph load is not listed in a MapReleaseManifest. | validation failure / `DENY`. |
| `rollback_missing` | Consequential public state lacks rollback target. | validation failure / `ERROR`. |

---

## Accepted inputs

Accepted material is limited to test files and small local test notes, such as:

- `README.md` and lane-local documentation;
- executable test files once runner and naming convention are confirmed;
- small helper notes that point to fixtures in `tests/fixtures/`, `fixtures/invalid/`, or domain-specific fixture lanes;
- expected finite-outcome notes for `ABSTAIN`, `DENY`, `ERROR`, validation failure, correction-required, or rollback-required cases.

Use fixtures by reference. Keep payloads in fixture lanes unless a local inline test value is minimal, synthetic, and clearly test-only.

---

## Exclusions

Do not place these materials in this lane:

| Excluded material | Correct destination |
|---|---|
| invalid fixture payload collections | `tests/fixtures/` or `fixtures/invalid/` |
| cross-domain shared fixture examples | `fixtures/invalid/` or another root fixture lane |
| domain-specific invalid fixture examples | `fixtures/domains/<domain>/invalid/` or `tests/fixtures/<domain>/` if test-local |
| schema definitions | `schemas/` |
| contract definitions | `contracts/` |
| policy rules | `policy/` |
| release records, correction notices, rollback cards | `release/` roots |
| source records or lifecycle data | `data/` lifecycle roots |
| production logs, generated artifacts, screenshots, public exports | governed artifact/CI/output roots only |
| secrets, private endpoints, real sensitive material, direct model output | not allowed in repository tests |

---

## Suggested layout

```text
tests/invalid/
|-- README.md
|-- schema_shape_invalid.test.PROPOSED
|-- contract_semantics_invalid.test.PROPOSED
|-- evidence_missing.test.PROPOSED
|-- citation_invalid.test.PROPOSED
|-- policy_denied.test.PROPOSED
|-- release_missing.test.PROPOSED
|-- direct_store_access.test.PROPOSED
|-- direct_model_client.test.PROPOSED
|-- unmanifested_map_asset.test.PROPOSED
`-- rollback_missing.test.PROPOSED
```

The layout is intentionally schematic. Actual test filenames, extensions, package manager, runner, and framework remain NEEDS VERIFICATION.

---

## Run posture

No executable runner was verified while authoring this README.

```bash
: "PROPOSED / NEEDS VERIFICATION"
pytest tests/invalid
```

Default runs should be deterministic, local, no-network, public-safe, and finite-outcome only. Replace the command once the repo's actual test runner and naming convention are verified.

---

## Maintenance checklist

- [ ] Keep tests focused on invalid/fail-closed behavior.
- [ ] Prefer the most specific domain test lane when domain ownership is clear.
- [ ] Keep fixture payloads in fixture lanes and reference them from tests.
- [ ] Assert finite outcomes: `ABSTAIN`, `DENY`, `ERROR`, validation failure, correction-required, or rollback-required.
- [ ] Do not store real source data, sensitive detail, production logs, public artifacts, schemas, contracts, policy rules, release records, or implementation code here.
- [ ] Link each invalid test to the fixture, contract, schema, policy, release gate, or trust-spine rule it verifies once those links are verified.

---

## Verification status

| Item | Status |
|---|---|
| Target README path | CONFIRMED; placeholder replaced. |
| `tests/` authority | CONFIRMED as canonical enforceability root. |
| Forbidden-boundary assertions | CONFIRMED in `tests/README.md`. |
| Root invalid fixture lane | CONFIRMED at `fixtures/invalid/README.md`. |
| Executable test inventory | NEEDS VERIFICATION. |
| Actual runner/framework | NEEDS VERIFICATION. |
| Fixture consumption | NEEDS VERIFICATION. |
| Schema bindings | NEEDS VERIFICATION. |
| Policy/runtime wiring | NEEDS VERIFICATION. |
| CI wiring and pass rates | NEEDS VERIFICATION. |
| Tests and validators | NOT RUN. |
