# `tests/api/` — Governed API Test Lane

Governed API envelope, route, trust-boundary, and negative-behavior tests for KFM. This lane proves that API surfaces respect evidence, policy, release, lifecycle, runtime-envelope, privacy, correction, and rollback boundaries; it does not implement API routes, define policy, store fixtures, or own public-client authority.

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-api-readme
title: tests/api/README.md — Governed API Test Lane
type: readme; directory-readme; api-test-guardrail; trust-spine-test-index
version: v0.1
status: draft; greenfield-stub-expanded; child-deny-lane-confirmed; implementation-depth-NEEDS-VERIFICATION
owners: OWNER_TBD — QA steward · API steward · Runtime steward · Policy steward · Evidence steward · Security steward · Docs steward
created: NEEDS VERIFICATION — greenfield stub existed before v0.1 expansion
updated: 2026-07-05
policy_label: public; tests; api; governed-api; finite-outcomes; no-api-authority
tags: [kfm, tests, api, governed-api, runtime-envelope, answer, abstain, deny, error, policy, evidence, release]
related:
  - ../README.md
  - ./deny/README.md
  - ../../runtime/README.md
  - ../../runtime/envelopes/README.md
  - ../../policy/README.md
  - ../../contracts/
  - ../../schemas/
  - ../../fixtures/
  - ../../tools/validators/
  - ../../apps/
  - ../../data/
  - ../../release/
notes:
  - "Expanded from a greenfield stub containing only '# tests/api' and 'Greenfield stub.'."
  - "Current-session search did not surface API test modules under tests/api; direct fetch confirms tests/api/deny/README.md exists."
  - "tests/ is confirmed as the canonical enforceability-proof root and includes governed API envelope tests."
  - "tests/api/deny/ is confirmed as the deny/fail-closed child lane."
  - "This README does not prove actual API route implementation, test modules, fixtures, CI coverage, schemas, policy bundles, runtime envelope implementation, or public-client behavior."
[/KFM_META_BLOCK_V2] -->

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Lane: API tests" src="https://img.shields.io/badge/lane-api__tests-purple">
  <img alt="Posture: finite outcomes" src="https://img.shields.io/badge/posture-finite__outcomes-green">
  <img alt="Boundary: no API authority" src="https://img.shields.io/badge/boundary-no__api__authority-critical">
</p>

**Status:** draft / governed API test index
**Path:** `tests/api/`
**Current role:** parent lane for governed API route, envelope, trust-boundary, and negative behavior tests
**Truth posture:** CONFIRMED greenfield stub before this update; CONFIRMED `tests/api/deny/README.md`; NEEDS VERIFICATION for actual test files, route inventory, fixtures, schemas, validators, CI, and pass/fail behavior.

## Purpose

`tests/api/` is the KFM test lane for governed API behavior.

API tests should prove that public or semi-public API surfaces use governed interfaces and released/supportable objects rather than reading from RAW, WORK, QUARANTINE, unpublished candidates, canonical/internal stores, direct model runtime output, or unsupported generated text.

A useful API test should verify at least one trust-spine boundary:

```text
request
  -> access/scope check
  -> evidence support check
  -> policy / sensitivity / rights check
  -> lifecycle / release / correction state check
  -> finite runtime or API outcome
  -> safe response body
```

## Authority boundary

| Responsibility | Correct home | This lane's role |
|---|---|---|
| Governed API tests | `tests/api/` | Proves route/envelope/trust-boundary behavior. |
| Deny and fail-closed API tests | `tests/api/deny/` | Proves negative and blocked outcomes. |
| API implementation | accepted app/API root | Tested here; not implemented here. |
| Runtime outcomes and envelopes | `runtime/`, `runtime/envelopes/`, contracts/schemas | Expected by tests; not authored here as authority. |
| Policy rules and decisions | `policy/` | Referenced by tests; not defined here. |
| Object meaning and shape | `contracts/`, `schemas/` | Referenced by tests; not redefined here. |
| Fixtures and snapshots | `fixtures/` or accepted test fixture home | Referenced by tests; not duplicated without a declared fixture rule. |
| Lifecycle records, receipts, proofs, catalog, published artifacts | `data/` and accepted trust-object roots | Referenced by safe pointers only. |
| Release decisions, corrections, rollback | `release/` | Tested by posture; not decided here. |

> [!IMPORTANT]
> An API test can prove an API boundary is enforceable. It does not create the API route, define the policy, approve release, or make generated/model output authoritative.

## Current inventory

| Path | Status | Notes |
|---|---|---|
| `tests/api/README.md` | present | Greenfield stub expanded by this README. |
| `tests/api/deny/README.md` | present | Governed API deny-test child lane. |
| `tests/api/*` | no direct modules confirmed in current search | No API test modules, snapshots, fixtures, or route inventories confirmed in this pass. |
| `tests/README.md` | present | Canonical enforceability-proof root. |
| `runtime/README.md` | present | Runtime root with finite `ANSWER` / `ABSTAIN` / `DENY` / `ERROR` outcomes. |
| `policy/README.md` | present | Canonical policy root for allow / deny / restrict / abstain and public-release posture. |

## Repo fit

```text
tests/
├── README.md                         # canonical enforceability-proof root
└── api/
    ├── README.md                     # this file; governed API test parent lane
    └── deny/
        └── README.md                 # deny/fail-closed child lane

apps/                                 # governed API implementation roots, if present
runtime/                              # finite runtime outcomes and envelopes
policy/                               # allow / deny / restrict / abstain posture
contracts/                            # semantic meaning
schemas/                              # machine-checkable shape
fixtures/                             # deterministic examples
tools/validators/                     # validator implementation
data/                                 # lifecycle records, receipts, proofs, catalogs, emitted data
release/                              # release, correction, rollback authority
```

## API test responsibilities

| Responsibility | Requirement |
|---|---|
| Verify finite outcomes | API responses should resolve to `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`, or a documented restricted/redacted response class. |
| Verify trust membrane | API tests must prove public paths do not read RAW, WORK, QUARANTINE, unpublished candidates, or internal stores directly. |
| Verify evidence posture | Answer-like responses must have support pointers or must abstain. |
| Verify policy posture | Policy, rights, sensitivity, access, release, and correction states must be respected. |
| Verify release posture | Unreleased, held, withdrawn, corrected, superseded, or stale-sensitive material must not be exposed as published truth. |
| Verify shape and contract posture | Response bodies should conform to accepted schemas/contracts once those are confirmed. |
| Verify no leakage | Responses must not leak private identifiers, sensitive exact locations, private config, direct model internals, or unsupported source data. |
| Verify receipts/envelopes | Response tests should assert receipt/envelope pointers when the route is expected to emit or link them. |

## Recommended API test families

| Family | Purpose | Suggested home |
|---|---|---|
| Envelope shape tests | Prove response uses finite envelope fields and reason-code posture. | `tests/api/` or a future `tests/api/envelopes/` |
| Deny tests | Prove blocked requests return safe `DENY` or restricted/redacted responses. | `tests/api/deny/` |
| Abstain tests | Prove unsupported evidence/citation cases return `ABSTAIN`. | `tests/api/` or future `tests/api/abstain/` |
| Error tests | Prove validation/config/dependency failures return safe `ERROR`. | `tests/api/` or future `tests/api/error/` |
| Release-state tests | Prove held, withdrawn, corrected, stale, or unreleased records are not exposed as published truth. | `tests/api/` or future `tests/api/release/` |
| Leakage tests | Prove denied/abstained/error responses do not leak protected fields or internal paths. | `tests/api/deny/` or future `tests/api/leakage/` |
| Public-client contract tests | Prove public clients receive only governed API payloads. | `tests/api/` with UI/e2e companion tests |

## What belongs here

- This README.
- Governed API route tests.
- API response envelope tests.
- API trust-boundary tests.
- API leakage tests using synthetic or redacted inputs.
- API deny/abstain/error tests or child-lane indexes.
- Test-only pointers to policy fixtures, evidence fixtures, route fixtures, runtime envelope fixtures, schema/contract checks, release-state fixtures, and validators.

## What does not belong here

| Do not put this in `tests/api/` | Correct home |
|---|---|
| API route implementation | accepted app/API root |
| Runtime adapter implementation | `runtime/` or accepted runtime/package root |
| Policy rules or policy decisions | `policy/` |
| Canonical contracts | `contracts/` |
| JSON Schema definitions | `schemas/` |
| Validator implementation | `tools/validators/` |
| General fixture libraries or golden source data | `fixtures/` or accepted test fixture home |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | `data/` lifecycle roots |
| EvidenceBundles, SourceDescriptors, receipts, proofs, catalogs, release manifests | accepted `data/`, registry, proof, receipt, catalog, or release roots |
| Release decisions, correction notices, rollback records, publication approvals | `release/` |
| Real exact sensitive geometry, living-person identifiers, DNA/genomic data, private addresses, private landowner details, or infrastructure details | never in default API tests; use synthetic/redacted/generalized fixtures |
| Live network calls, live credentials, private provider config, or model internals | never in default deterministic API tests |
| Generated text treated as evidence, policy, review, release, correction, rollback, legal/title conclusion, or publication authority | nowhere |

## Minimal API test card

```markdown
# <api-test-id>

## Status
DRAFT / READY_FOR_REVIEW / ACTIVE_TEST / VALIDATION_REQUIRED / HELD / SUPERSEDED / RETIRED

## Route or surface
<api route, handler, envelope family, or N/A>

## Test family
envelope / answer / abstain / deny / error / release-state / leakage / public-client / other

## Expected outcome
ANSWER / ABSTAIN / DENY / ERROR / RESTRICTED / REDACTED

## Governed support pointers
- Policy: <path or N/A>
- Contract: <path or N/A>
- Schema: <path or N/A>
- Fixture: <path or N/A>
- Validator: <path or N/A>
- Runtime envelope: <path or N/A>
- Release/correction/rollback: <path or N/A>

## Assertion summary
<what the route must prove>

## Boundary checks
<stores, paths, fields, identifiers, or source states that must not be exposed>

## Reviewer
<steward or maintainer>
```

## Validation

```bash
find tests/api -maxdepth 5 -type f | sort
find tests policy runtime contracts schemas fixtures tools/validators apps data release -maxdepth 5 -type f 2>/dev/null | sort
pytest tests/api tests/policy tests/runtime || true
```

Replace `|| true` with fail-closed CI behavior once accepted API test commands are confirmed.

## Review checklist

- [ ] Test proves a governed API route, envelope, or public trust boundary.
- [ ] Expected outcome is finite or explicitly restricted/redacted.
- [ ] Policy, evidence, lifecycle, release, and correction assumptions are explicit where material.
- [ ] Test does not read directly from RAW, WORK, QUARANTINE, unpublished candidates, internal stores, or direct model runtime output as the normal public path.
- [ ] Test uses synthetic, redacted, or generalized fixtures only.
- [ ] Test does not define policy, schema, contract, lifecycle state, release state, fixture authority, or API implementation.
- [ ] Failure should block promotion when the route is release/public-surface significant.

## Open questions

| Question | Status |
|---|---|
| Which governed API routes currently exist and need API test coverage? | NEEDS VERIFICATION |
| Which RuntimeResponseEnvelope or API envelope schema is canonical for tests? | NEEDS VERIFICATION |
| Should `tests/api/` grow child lanes for `envelopes/`, `abstain/`, `error/`, `release/`, and `leakage/`? | NEEDS VERIFICATION |
| Which fixtures are canonical for API tests, and should snapshots live here or under `fixtures/`? | NEEDS VERIFICATION |
| Which CI workflow blocks release or promotion when API tests fail? | NEEDS VERIFICATION |
