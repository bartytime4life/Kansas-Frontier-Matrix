# `tests/api/deny/` — Governed API Deny-Test Lane

Negative API tests for KFM governed API behavior. This lane proves that deny, restrict, abstain, and fail-closed API outcomes are enforceable; it does not define policy rules, API implementation, fixtures, schemas, contracts, lifecycle data, or release decisions.

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-api-deny-readme
title: tests/api/deny/README.md — Governed API Deny-Test Lane
type: readme; directory-readme; negative-test-guardrail; api-deny-test-index
version: v0.1
status: draft; placeholder-expanded; no-direct-deny-tests-confirmed; NEEDS VERIFICATION
owners: OWNER_TBD — QA steward · API steward · Policy steward · Runtime steward · Security steward · Docs steward
created: NEEDS VERIFICATION — placeholder content existed before v0.1 expansion
updated: 2026-07-05
policy_label: public; tests; api; deny; fail-closed; no-policy-authority
tags: [kfm, tests, api, deny, restrict, abstain, fail-closed, runtime-envelope, policy, trust-spine]
related:
  - ../../README.md
  - ../README.md
  - ../../../policy/README.md
  - ../../../runtime/README.md
  - ../../../runtime/envelopes/README.md
  - ../../../contracts/
  - ../../../schemas/
  - ../../../fixtures/
  - ../../../tools/validators/
  - ../../../apps/
  - ../../../data/
  - ../../../release/
notes:
  - "Expanded from placeholder content in tests/api/deny/README.md."
  - "Current-session search found no direct files under tests/api/deny beyond this README."
  - "tests/ is confirmed as the canonical enforceability-proof root; it includes governed API envelope tests and negative policy/API behavior."
  - "policy/ is confirmed as the canonical policy root for allow / deny / restrict / abstain / redaction / public release / promotion / sensitivity."
  - "runtime/ is confirmed as subordinate to evidence, policy, release, and finite outcomes."
  - "This README does not prove actual API routes, deny-test files, fixtures, CI coverage, policy bundles, runtime envelope schemas, or implementation behavior."
[/KFM_META_BLOCK_V2] -->

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Lane: api deny" src="https://img.shields.io/badge/lane-api__deny-purple">
  <img alt="Posture: fail closed" src="https://img.shields.io/badge/posture-fail__closed-red">
  <img alt="Boundary: no policy authority" src="https://img.shields.io/badge/boundary-no__policy__authority-critical">
</p>

**Status:** draft / negative API test guardrail
**Path:** `tests/api/deny/`
**Current role:** README-only deny-test lane until test files are added and verified
**Truth posture:** CONFIRMED placeholder file existed before this update; CONFIRMED no direct test files found in current search; CONFIRMED `tests/`, `policy/`, and `runtime/` root boundaries; NEEDS VERIFICATION for actual API routes, deny fixtures, policy fixtures, schemas, validators, CI, and pass/fail behavior.

## Purpose

`tests/api/deny/` is the lane for negative governed API tests that prove API callers cannot bypass KFM policy, evidence, release, privacy, sensitivity, lifecycle, or runtime-envelope boundaries.

These tests should exercise cases where the API must return a finite non-answer outcome, especially:

- `DENY` when policy or governance state forbids response;
- `ABSTAIN` when evidence, citation support, source authority, freshness, or scope is insufficient;
- `ERROR` when validation, adapter, envelope, dependency, or configuration failure prevents completion;
- restricted/redacted responses where policy allows only limited output.

## Authority boundary

| Responsibility | Correct home | This lane's role |
|---|---|---|
| Negative API tests | `tests/api/deny/` | Proves deny/fail-closed behavior through tests. |
| Policy rules and policy decisions | `policy/` | Referenced by tests; not defined here. |
| API route implementation | accepted app/API root | Tested here; not implemented here. |
| Runtime outcomes and envelopes | `runtime/`, `runtime/envelopes/`, contracts/schemas | Expected by tests; not authored here unless test-only assertions. |
| Fixtures and golden examples | `fixtures/` or accepted test fixture home | Referenced by tests; not duplicated here unless test-scoped fixture rule is documented. |
| Contracts and schemas | `contracts/`, `schemas/` | Referenced by tests; not redefined here. |
| Lifecycle data, receipts, proofs, catalog, published artifacts | `data/` and accepted trust-object roots | May be referenced by safe synthetic pointers; not stored here. |
| Release decisions, correction, rollback | `release/` | May be tested; not decided here. |

> [!IMPORTANT]
> A deny test proves that a boundary is enforceable. It does not create the policy, approve a release, define a public API route, or authorize exposure.

## Current inventory

| Path | Status | Notes |
|---|---|---|
| `tests/api/deny/README.md` | present | Placeholder content replaced by this README. |
| `tests/api/deny/*` | no files found in current search | No deny-test modules, fixtures, snapshots, or configs confirmed under this path. |
| `tests/README.md` | present | Canonical tests root; tests prove enforceability of the KFM trust spine. |
| `policy/README.md` | present | Canonical policy root for allow / deny / restrict / abstain / redaction / release / promotion / sensitivity. |
| `runtime/README.md` | present | Runtime root; finite outcomes and policy/evidence/release subordination. |

## Repo fit

```text
tests/
├── README.md                         # canonical enforceability-proof root
└── api/
    └── deny/
        └── README.md                 # this file; deny/fail-closed API test lane

policy/                               # allow / deny / restrict / abstain rules
runtime/                              # finite runtime outcomes and envelopes
contracts/                            # semantic meaning
schemas/                              # machine-checkable shape
fixtures/                             # deterministic examples
tools/validators/                     # validator implementation
data/                                 # lifecycle records, receipts, proofs, catalogs, emitted data
release/                              # release, correction, rollback authority
apps/                                 # governed API and UI implementation roots
```

## Deny-test responsibilities

| Responsibility | Requirement |
|---|---|
| Verify fail-closed behavior | Missing policy, evidence, release, consent, rights, or sensitivity state must not fall through to `ANSWER`. |
| Verify finite outcomes | API response must resolve to `DENY`, `ABSTAIN`, `ERROR`, or allowed restricted output. |
| Verify no leakage | Denied responses must not expose RAW, WORK, QUARANTINE, internal store paths, private IDs, sensitive geometry, private runtime output, or model internals. |
| Verify policy linkage | Test cases should point to the policy rule, policy fixture, or policy decision family they exercise. |
| Verify evidence posture | Unsupported EvidenceRef or missing EvidenceBundle must produce `ABSTAIN` or `DENY`, not invented support. |
| Verify release posture | Unreleased, withdrawn, corrected, held, stale, or review-pending material must not be exposed as published truth. |
| Verify receipts/envelopes | Response shape should preserve reason codes, support pointers, and receipt/envelope posture where applicable. |

## Required negative cases

| Case | Expected posture |
|---|---|
| Missing authentication or access role, where route requires it | `DENY` |
| Policy decision missing for sensitive request | `DENY` |
| Policy decision explicitly denies request | `DENY` |
| Rights or license state missing for public output | `DENY` or `ABSTAIN` |
| Sensitivity state unknown for people, DNA, rare species, archaeology, infrastructure, or exact private-location material | `DENY` or restricted/generalized output |
| EvidenceRef cannot resolve to EvidenceBundle | `ABSTAIN` |
| Citation-required output has no valid citation support | `ABSTAIN` |
| Release state is missing, held, withdrawn, corrected, superseded, or stale-sensitive | `DENY` or `ABSTAIN` |
| API tries to read RAW, WORK, QUARANTINE, unpublished candidates, or internal stores directly | test failure |
| Runtime/model output appears without governed envelope and support state | `ERROR` or test failure |
| Route returns unbounded free text instead of finite envelope posture | test failure |

## What belongs here

- This README.
- Deny/fail-closed API test modules.
- Negative API-envelope assertions.
- Snapshot expectations for safe `DENY`, `ABSTAIN`, and `ERROR` bodies, if snapshots are accepted by the repo.
- Test-only pointers to policy fixtures, evidence fixtures, runtime envelope fixtures, API route fixtures, and release-state fixtures.
- Notes explaining why a route must deny, abstain, restrict, redact, or fail closed.

## What does not belong here

| Do not put this in `tests/api/deny/` | Correct home |
|---|---|
| API implementation code | accepted app/API root |
| Policy rules or policy decisions | `policy/` |
| Canonical contracts | `contracts/` |
| JSON Schema definitions | `schemas/` |
| Validator implementation | `tools/validators/` |
| General fixture libraries or golden source data | `fixtures/` or accepted test fixture home |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | `data/` lifecycle roots |
| EvidenceBundles, SourceDescriptors, receipts, proofs, catalogs, release manifests | accepted `data/`, registry, proof, receipt, catalog, or release roots |
| Release decisions, correction notices, rollback records, publication approvals | `release/` |
| Real exact sensitive geometry, living-person identifiers, DNA/genomic data, private addresses, private landowner details, or infrastructure details | never in default test suite; use synthetic/redacted/generalized fixtures |
| Live network calls, live credentials, private provider config, or model internals | never in default deterministic tests |
| Generated text treated as evidence, policy, review, release, correction, rollback, legal/title conclusion, or publication authority | nowhere |

## Test note template

```markdown
# <api-deny-test-id>

## Status
DRAFT / READY_FOR_REVIEW / ACTIVE_TEST / VALIDATION_REQUIRED / HELD / SUPERSEDED / RETIRED

## Route or surface
<api route, handler, envelope family, or N/A>

## Deny reason family
policy / access / rights / sensitivity / evidence / citation / release / runtime / validation / other

## Expected outcome
DENY / ABSTAIN / ERROR / RESTRICTED / REDACTED

## Governed support pointers
- Policy: <path or N/A>
- Contract: <path or N/A>
- Schema: <path or N/A>
- Fixture: <path or N/A>
- Validator: <path or N/A>
- Runtime envelope: <path or N/A>
- Release/correction/rollback: <path or N/A>

## Assertion summary
<what must be denied, abstained, redacted, restricted, or failed closed>

## Leakage checks
<fields, stores, paths, identifiers, or details that must not appear>

## Reviewer
<steward or maintainer>
```

## Validation

```bash
find tests/api/deny -maxdepth 4 -type f | sort
find tests/api tests/policy tests/runtime fixtures policy runtime contracts schemas tools/validators -maxdepth 5 -type f 2>/dev/null | sort
pytest tests/api/deny tests/api tests/policy tests/runtime || true
```

Replace `|| true` with fail-closed CI behavior once accepted API deny-test commands are confirmed.

## Review checklist

- [ ] Test proves a governed API boundary, not only local function behavior.
- [ ] Expected outcome is finite: `DENY`, `ABSTAIN`, `ERROR`, restricted, or redacted.
- [ ] Policy reference is explicit when policy causes the denial.
- [ ] Evidence or citation gap is explicit when the expected outcome is `ABSTAIN`.
- [ ] Release/correction/rollback state is explicit when publication state causes denial.
- [ ] Test uses synthetic, redacted, or generalized fixtures only.
- [ ] Denied response does not leak internal stores, sensitive identifiers, private config, raw lifecycle paths, or direct model output.
- [ ] Test does not define policy, schema, contract, fixture authority, lifecycle data, release state, or API implementation.

## Open questions

| Question | Status |
|---|---|
| Which governed API routes currently exist and require deny tests? | NEEDS VERIFICATION |
| Which envelope schema defines the expected API denial body? | NEEDS VERIFICATION |
| Which policy fixtures are canonical for deny/restrict/abstain API tests? | NEEDS VERIFICATION |
| Should snapshots live under `tests/api/deny/` or a central fixture/snapshot lane? | NEEDS VERIFICATION |
| Which CI workflow blocks promotion when API deny tests fail? | NEEDS VERIFICATION |
