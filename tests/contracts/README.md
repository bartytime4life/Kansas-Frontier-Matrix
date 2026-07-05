# `tests/contracts/` — Contract Enforceability Test Lane

Contract tests for KFM semantic object meaning. This lane proves that contract Markdown under `contracts/` remains enforceable, aligned with schemas where applicable, supported by fixtures/validators/policy, and safe for governed API/UI/runtime/release use; it does not define contract authority, schemas, policy, validators, fixtures, lifecycle records, or release decisions.

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-contracts-readme
title: tests/contracts/README.md — Contract Enforceability Test Lane
type: readme; directory-readme; contract-test-guardrail; semantic-enforcement-index
version: v0.1
status: draft; greenfield-stub-expanded; no-direct-contract-tests-confirmed; NEEDS VERIFICATION
owners: OWNER_TBD — QA steward · Contracts steward · Schema steward · Policy steward · Evidence steward · Release steward · Docs steward
created: NEEDS VERIFICATION — greenfield stub existed before v0.1 expansion
updated: 2026-07-05
policy_label: public; tests; contracts; semantic-contracts; no-contract-authority
tags: [kfm, tests, contracts, semantic-contracts, schemas, fixtures, validators, policy, release, evidence]
related:
  - ../README.md
  - ../../contracts/README.md
  - ../../contracts/OBJECT_MAP.md
  - ../../schemas/contracts/v1/
  - ../../policy/
  - ../../fixtures/
  - ../../tools/validators/
  - ../../data/
  - ../../release/
notes:
  - "Expanded from a greenfield stub containing only '# tests/contracts' and 'Greenfield stub.'."
  - "Current-session search did not surface contract test modules under tests/contracts."
  - "tests/ is confirmed as the canonical enforceability-proof root and includes contract tests as an accepted test class."
  - "contracts/ is confirmed as the canonical semantic-contract root; schemas define shape, policy defines admissibility, and tests/validators prove enforcement."
  - "This README does not prove actual contract test modules, schema alignment coverage, fixture coverage, validator coverage, policy behavior, CI wiring, release readiness, or public-client behavior."
[/KFM_META_BLOCK_V2] -->

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Lane: contract tests" src="https://img.shields.io/badge/lane-contract__tests-purple">
  <img alt="Authority: enforceability proof" src="https://img.shields.io/badge/authority-enforceability__proof-green">
  <img alt="Boundary: no contract authority" src="https://img.shields.io/badge/boundary-no__contract__authority-critical">
</p>

**Status:** draft / contract test index
**Path:** `tests/contracts/`
**Current role:** parent lane for tests that prove semantic contracts are enforceable
**Truth posture:** CONFIRMED greenfield stub before this update; CONFIRMED no direct contract test modules found in current search; CONFIRMED `tests/` and `contracts/` root boundaries; NEEDS VERIFICATION for test files, schema coverage, fixtures, validators, CI, and pass/fail behavior.

## Purpose

`tests/contracts/` is the KFM test lane for semantic contract enforceability.

Contract tests should prove that Markdown contracts under `contracts/` match the object meaning they claim, preserve authority boundaries, point to expected companion schemas/fixtures/policy/validators, and do not drift into schema, policy, source-registry, proof, data, release, runtime, API, or UI authority.

A useful contract test should verify at least one contract boundary:

```text
contract document
  -> declares semantic meaning
  -> names companion schema posture
  -> names policy/evidence/release posture where material
  -> has fixture or validator support where implementation is claimed
  -> preserves lifecycle and public-client boundaries
```

## Authority boundary

| Responsibility | Correct home | This lane's role |
|---|---|---|
| Contract tests | `tests/contracts/` | Proves semantic contract claims and boundaries are enforceable. |
| Semantic contract authority | `contracts/` | Tested here; not defined here. |
| Machine-checkable shape | `schemas/` | Referenced by tests; not authored here. |
| Policy/admissibility | `policy/` | Referenced by tests; not defined here. |
| Fixtures and golden examples | `fixtures/` or accepted test fixture home | Referenced by tests; not duplicated without a declared fixture rule. |
| Validator implementation | `tools/validators/` | Tested here; not implemented here. |
| Evidence, proofs, receipts, lifecycle records | `data/` and accepted trust-object roots | Referenced by safe pointers only. |
| Release, correction, rollback | `release/` | Tested by posture; not decided here. |
| Runtime/API/UI implementation | accepted runtime/app/UI roots | May consume contract behavior; not implemented here. |

> [!IMPORTANT]
> A contract test can prove that semantic meaning is enforceable. It does not create or change the contract, schema, policy, fixture, validator, data record, or release state.

## Current inventory

| Path | Status | Notes |
|---|---|---|
| `tests/contracts/README.md` | present | Greenfield stub expanded by this README. |
| `tests/contracts/*` | no files found in current search | No contract test modules, snapshots, fixtures, or configs confirmed in this pass. |
| `tests/README.md` | present | Canonical enforceability-proof root. |
| `contracts/README.md` | present | Canonical semantic-contract root. |
| `schemas/contracts/v1/` | referenced | Machine-checkable companion schema root; full coverage not verified here. |

## Repo fit

```text
tests/
├── README.md                         # canonical enforceability-proof root
└── contracts/
    └── README.md                     # this file; contract enforceability tests

contracts/                            # semantic meaning
schemas/contracts/v1/                 # machine-checkable shape
policy/                               # allow / deny / restrict / abstain posture
fixtures/                             # deterministic examples
tools/validators/                     # validator implementation
data/                                 # lifecycle records, receipts, proofs, catalogs, emitted data
release/                              # release, correction, rollback authority
runtime/                              # runtime envelopes and adapter behavior
apps/                                 # governed API/UI implementation roots
```

## Contract test responsibilities

| Responsibility | Requirement |
|---|---|
| Verify semantic boundary | Contracts define meaning only; they must not become schema, policy, data, proof, release, runtime, API, or UI implementation. |
| Verify schema posture | Contracts that claim schema support should point to an accepted schema or be marked schema-missing / needs verification. |
| Verify policy posture | Contracts that affect access, sensitivity, rights, release, or public exposure should reference policy posture. |
| Verify evidence posture | Contracts involving claims, citations, proof, or source support should preserve EvidenceRef / EvidenceBundle requirements. |
| Verify release posture | Contracts that describe public-facing objects should preserve release, correction, rollback, and withdrawal boundaries. |
| Verify negative states | Contract tests should cover missing schema, mismatched schema, missing policy, unsupported evidence, and overclaimed release states. |
| Verify no duplicate authority | Tests should catch parallel contract homes, mirrored schemas in contract space, and compatibility guards that become authority by accident. |

## Recommended contract test families

| Family | Purpose | Suggested home |
|---|---|---|
| Metadata tests | Confirm contract docs carry expected metadata, status, owners, and truth labels. | `tests/contracts/` |
| Boundary tests | Confirm contract docs do not define schemas, policy rules, data instances, or release decisions. | `tests/contracts/` |
| Schema-alignment tests | Confirm contract fields align with companion schemas where schemas exist. | `tests/contracts/` or `tests/schemas/` companion tests |
| Object-map tests | Confirm contract object families are indexed without overclaiming completeness. | `tests/contracts/` |
| Maturity-label tests | Confirm labels such as `schema-missing`, `validated`, or `released` are supported by evidence. | `tests/contracts/` |
| Public-surface tests | Confirm public-facing contracts require evidence, policy, release, correction, and rollback posture. | `tests/contracts/` with API/UI companions |
| Drift tests | Catch duplicate object authority, compatibility guards hardening into authority, or topic-as-root drift. | `tests/contracts/` |

## What belongs here

- This README.
- Contract metadata tests.
- Contract boundary tests.
- Contract-to-schema alignment tests.
- Contract object-map tests.
- Contract maturity-label tests.
- Contract public-surface readiness tests.
- Test-only pointers to schemas, policy fixtures, contract fixtures, validators, evidence fixtures, release fixtures, and companion API/UI/runtime tests.

## What does not belong here

| Do not put this in `tests/contracts/` | Correct home |
|---|---|
| Semantic contract documents | `contracts/` |
| JSON Schema definitions | `schemas/` |
| Policy rules or policy decisions | `policy/` |
| Validator implementation | `tools/validators/` |
| General fixture libraries or golden source data | `fixtures/` or accepted test fixture home |
| Source descriptors, evidence bundles, receipts, proofs, catalogs, lifecycle records, or published artifacts | accepted `data/`, registry, proof, receipt, catalog, or published roots |
| Release manifests, promotion decisions, correction notices, rollback records, publication approvals | `release/` |
| Runtime adapter, API route, or UI implementation | accepted runtime/app/UI/package roots |
| Real sensitive data or private identifiers | never in default contract tests; use synthetic/redacted/generalized fixtures |
| Generated text treated as semantic authority, evidence, policy, review, release, correction, rollback, or publication authority | nowhere |

## Minimal contract test card

```markdown
# <contract-test-id>

## Status
DRAFT / READY_FOR_REVIEW / ACTIVE_TEST / VALIDATION_REQUIRED / HELD / SUPERSEDED / RETIRED

## Contract under test
<contracts/... path or N/A>

## Test family
metadata / boundary / schema-alignment / object-map / maturity / public-surface / drift / other

## Expected result
PASS / FAIL_CLOSED / NEEDS_FIXTURE / NEEDS_SCHEMA / NEEDS_POLICY / NEEDS_RELEASE_REVIEW

## Governed support pointers
- Contract: <path or N/A>
- Schema: <path or N/A>
- Policy: <path or N/A>
- Fixture: <path or N/A>
- Validator: <path or N/A>
- Evidence/proof: <path or N/A>
- Release/correction/rollback: <path or N/A>

## Assertion summary
<what semantic boundary or alignment must be proven>

## Drift checks
<duplicate authority, schema-policy-data-release leakage, or compatibility-path risks>

## Reviewer
<steward or maintainer>
```

## Validation

```bash
find tests/contracts -maxdepth 5 -type f | sort
find contracts schemas/contracts policy fixtures tools/validators data release runtime apps -maxdepth 5 -type f 2>/dev/null | sort
pytest tests/contracts tests/schemas tests/policy || true
```

Replace `|| true` with fail-closed CI behavior once accepted contract test commands are confirmed.

## Review checklist

- [ ] Test proves a semantic contract boundary or alignment rule.
- [ ] Contract path under test is explicit.
- [ ] Companion schema posture is explicit where material.
- [ ] Policy, evidence, release, correction, and rollback assumptions are explicit where material.
- [ ] Test does not define contracts, schemas, policies, fixtures, validators, lifecycle records, or release state.
- [ ] Test uses synthetic, redacted, or generalized fixtures only.
- [ ] Failure should block promotion when the contract is release/public-surface significant.

## Open questions

| Question | Status |
|---|---|
| Which contracts currently have companion schemas and should be covered first? | NEEDS VERIFICATION |
| Which object-map checks are accepted for contract inventory coverage? | NEEDS VERIFICATION |
| Should contract tests live only here, or should some be paired with `tests/schemas/` and `tools/validators/`? | NEEDS VERIFICATION |
| Which fixtures are canonical for semantic contract tests? | NEEDS VERIFICATION |
| Which CI workflow blocks release or promotion when contract tests fail? | NEEDS VERIFICATION |
