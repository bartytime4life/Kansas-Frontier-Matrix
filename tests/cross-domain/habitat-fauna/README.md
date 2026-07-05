# `tests/cross-domain/habitat-fauna/` — Habitat × Fauna Cross-Domain Test Lane

Cross-domain tests for Habitat × Fauna joins, habitat assignments, sensitivity inheritance, geoprivacy gates, and ownership preservation. This lane proves cross-domain behavior is enforceable; it does not own Habitat truth, Fauna truth, policy rules, contracts, schemas, fixtures, validators, lifecycle data, release decisions, or public-client authority.

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-cross-domain-habitat-fauna-readme
title: tests/cross-domain/habitat-fauna/README.md — Habitat × Fauna Cross-Domain Test Lane
type: readme; directory-readme; cross-domain-test-guardrail; habitat-fauna-test-index
version: v0.1
status: draft; empty-path-expanded; path-naming-NEEDS-VERIFICATION; no-direct-test-modules-confirmed
owners: OWNER_TBD — QA steward · Habitat steward · Fauna steward · Policy steward · Evidence steward · Sensitivity reviewer · Docs steward
created: NEEDS VERIFICATION — empty file existed before v0.1 expansion
updated: 2026-07-05
policy_label: restricted-review; tests; cross-domain; habitat; fauna; sensitivity; geoprivacy
tags: [kfm, tests, cross-domain, habitat, fauna, geoprivacy, sensitivity, fail-closed, evidence-bundle, redaction-receipt]
related:
  - ../../README.md
  - ../../../docs/domains/habitat/HABITAT_SENSITIVITY_PROFILE.md
  - ../../../docs/domains/fauna/SENSITIVITY.md
  - ../../../docs/domains/fauna/CROSS_LANE_RELATIONS.md
  - ../../../contracts/domains/habitat/
  - ../../../contracts/domains/fauna/
  - ../../../policy/
  - ../../../fixtures/
  - ../../../tools/validators/
  - ../../../data/
  - ../../../release/
notes:
  - "Expanded from an empty tests/cross-domain/habitat-fauna/README.md."
  - "Current-session search found no direct test modules under tests/cross-domain/habitat-fauna beyond this README."
  - "tests/ is confirmed as the canonical enforceability-proof root."
  - "Habitat sensitivity profile confirms Habitat's dominant risk is join-induced sensitivity; sensitivity is a property of the resulting product, not just the input."
  - "Fauna sensitivity profile confirms deny-by-default, fail-closed, generalize-before-release, receipt-bearing posture for sensitive fauna records."
  - "Fauna cross-lane relations confirm Habitat owns patches and suitability, Fauna owns occurrences, and the habitat assignment is a relation, not ownership transfer."
  - "Naming convention conflict: this existing path uses tests/cross-domain/, while fauna cross-lane docs mention tests/cross_domain/. Treat placement as NEEDS VERIFICATION until ADR or maintainer decision resolves it."
  - "This README does not prove actual test modules, fixtures, validator coverage, policy bundles, schema coverage, CI behavior, release readiness, or public-client behavior."
[/KFM_META_BLOCK_V2] -->

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Lane: habitat fauna" src="https://img.shields.io/badge/lane-habitat__fauna-purple">
  <img alt="Posture: fail closed" src="https://img.shields.io/badge/posture-fail__closed-red">
  <img alt="Boundary: no domain authority" src="https://img.shields.io/badge/boundary-no__domain__authority-critical">
</p>

**Status:** draft / cross-domain test guardrail
**Path:** `tests/cross-domain/habitat-fauna/`
**Current role:** README-only test lane for Habitat × Fauna join behavior
**Truth posture:** CONFIRMED target file existed and was empty; CONFIRMED no direct test modules found in current search; CONFIRMED root test, Habitat sensitivity, Fauna sensitivity, and Fauna cross-lane relation boundaries; NEEDS VERIFICATION for path naming, test files, fixtures, validators, policies, schemas, CI, and release-gate integration.

## Purpose

`tests/cross-domain/habitat-fauna/` is for tests that prove Habitat × Fauna cross-domain behavior is safe, evidence-backed, policy-aware, and fail-closed.

These tests should focus on the high-risk edge where useful habitat context can accidentally expose sensitive fauna information. They should prove that:

- Habitat owns habitat patches, suitability, corridors, and related habitat surfaces;
- Fauna owns occurrences, taxa, sensitive sites, seasonal ranges, and fauna-side observations;
- a habitat assignment is a relation, not an ownership transfer;
- the resulting product inherits the most restrictive sensitivity of any input;
- unresolved sensitivity, evidence, policy, review, release, or transform state fails closed;
- public-facing outputs use only governed, public-safe derivatives.

## Placement note

The requested path exists as `tests/cross-domain/habitat-fauna/`.

Current repo evidence also shows a fauna cross-lane doc mentioning `tests/cross_domain/` with an underscore form for relation tests. Until a maintainer or ADR resolves the naming convention, this README treats the requested path as an existing compatibility/test lane and marks naming as **NEEDS VERIFICATION**.

Do not create parallel cross-domain test homes without a migration note.

## Authority boundary

| Responsibility | Correct home | This lane's role |
|---|---|---|
| Habitat × Fauna tests | `tests/cross-domain/habitat-fauna/` or accepted cross-domain test lane | Proves cross-domain behavior and fail-closed joins. |
| Habitat object meaning | `contracts/domains/habitat/`, Habitat docs | Referenced by tests; not defined here. |
| Fauna object meaning | `contracts/domains/fauna/`, Fauna docs | Referenced by tests; not defined here. |
| Policy and sensitivity decisions | `policy/` and governed review/release roots | Referenced by tests; not decided here. |
| Fixtures and synthetic examples | `fixtures/` or accepted test fixture home | Referenced by tests; not duplicated without a fixture rule. |
| Validator implementation | `tools/validators/` | Tested here; not implemented here. |
| Evidence, receipts, lifecycle records | `data/` and accepted trust-object roots | Referenced by safe pointers only. |
| Release, correction, rollback | `release/` | Tested by posture; not decided here. |

> [!IMPORTANT]
> Cross-domain tests prove boundary discipline. They do not publish habitat products, reveal fauna locations, approve redaction transforms, or decide release state.

## Current inventory

| Path | Status | Notes |
|---|---|---|
| `tests/cross-domain/habitat-fauna/README.md` | present | Empty file expanded by this README. |
| `tests/cross-domain/habitat-fauna/*` | no files found in current search | No test modules, fixtures, snapshots, or configs confirmed in this pass. |
| `tests/cross-domain/README.md` | not found in direct fetch | Parent README should be created or path convention resolved. |
| `tests/README.md` | present | Canonical enforceability-proof root. |
| `docs/domains/habitat/HABITAT_SENSITIVITY_PROFILE.md` | present | Habitat sensitivity and join-induced risk profile. |
| `docs/domains/fauna/SENSITIVITY.md` | present | Fauna sensitivity and geoprivacy posture. |
| `docs/domains/fauna/CROSS_LANE_RELATIONS.md` | present | Fauna cross-lane relation and ownership lattice. |

## Repo fit

```text
tests/
├── README.md                         # canonical enforceability-proof root
└── cross-domain/                     # path exists through this child; parent README not confirmed
    └── habitat-fauna/
        └── README.md                 # this file

contracts/domains/habitat/             # Habitat semantic meaning
contracts/domains/fauna/               # Fauna semantic meaning
policy/                                # sensitivity, rights, release, allow/deny/restrict/abstain posture
fixtures/                              # deterministic synthetic/redacted examples
tools/validators/                      # validator implementation
data/                                  # lifecycle records, receipts, proofs, catalogs, emitted data
release/                               # release, correction, rollback authority
```

## Test responsibilities

| Responsibility | Requirement |
|---|---|
| Preserve ownership | Habitat objects stay Habitat-owned; Fauna objects stay Fauna-owned; relations cite, never copy or overwrite. |
| Preserve source role | Tests must distinguish authority, observation, context, model, and derived relations. |
| Preserve sensitivity | The joined product inherits the most restrictive sensitivity of either side. |
| Preserve evidence posture | Relation claims require EvidenceRef / EvidenceBundle support or must abstain. |
| Preserve policy posture | Sensitive joins must reference policy state before public-safe output is allowed. |
| Preserve geoprivacy posture | Public derivatives require documented redaction, aggregation, generalization, or suppression posture and receipt pointers. |
| Preserve finite outcomes | Unsupported joins should produce `ABSTAIN`, `DENY`, or fail-closed test failure, not guessed assignments. |
| Preserve release posture | Unreleased, held, corrected, superseded, or review-pending join products must not be treated as public truth. |

## Required negative cases

| Case | Expected posture |
|---|---|
| Habitat patch joined to sensitive Fauna occurrence without reviewed transform | `DENY` / fail closed |
| Habitat assignment lacks EvidenceBundle support | `ABSTAIN` |
| Habitat suitability is copied into Fauna-owned truth rather than cited | test failure |
| Fauna occurrence geometry leaks through habitat surface, summary, tile, API payload, or UI payload | test failure |
| Cross-domain relation lowers sensitivity instead of inheriting the most restrictive input | test failure |
| Redaction/generalization receipt is missing for public derivative | `DENY` / fail closed |
| Policy state is missing for sensitive join | `DENY` |
| Ambiguous many-to-many habitat/fauna join is flattened without disambiguation | `ABSTAIN` / test failure |
| Release state is missing, held, withdrawn, corrected, superseded, or stale-sensitive | `DENY` / `ABSTAIN` |

## What belongs here

- This README.
- Habitat × Fauna cross-domain test modules.
- Tests for habitat assignment relation behavior.
- Tests for ownership preservation and owner-publishes / consumer-cites discipline.
- Tests for sensitivity inheritance and fail-closed joins.
- Tests for geoprivacy receipt requirements using synthetic or redacted fixtures.
- Test-only pointers to Habitat/Fauna contracts, policy fixtures, evidence fixtures, release-state fixtures, and validators.

## What does not belong here

| Do not put this in `tests/cross-domain/habitat-fauna/` | Correct home |
|---|---|
| Habitat or Fauna implementation code | accepted domain package or app root |
| Habitat or Fauna semantic contracts | `contracts/domains/habitat/`, `contracts/domains/fauna/` |
| Policy rules or sensitivity decisions | `policy/` and governed review/release roots |
| JSON Schema definitions | `schemas/` |
| Validator implementation | `tools/validators/` |
| General fixture libraries or golden source data | `fixtures/` or accepted test fixture home |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | `data/` lifecycle roots |
| EvidenceBundles, SourceDescriptors, receipts, proofs, catalogs, release manifests | accepted `data/`, registry, proof, receipt, catalog, or release roots |
| Release decisions, correction notices, rollback records, publication approvals | `release/` |
| Exact sensitive occurrence locations, nests, dens, roosts, hibernacula, spawning sites, private parcel detail, or rare-species exposure aids | never in default tests; use synthetic/redacted/generalized fixtures |
| Generated text treated as evidence, policy, review, release, correction, rollback, or publication authority | nowhere |

## Minimal test card

```markdown
# <habitat-fauna-test-id>

## Status
DRAFT / READY_FOR_REVIEW / ACTIVE_TEST / VALIDATION_REQUIRED / HELD / SUPERSEDED / RETIRED

## Test family
ownership / sensitivity-inheritance / geoprivacy / evidence / policy / release / ambiguity / leakage / other

## Join under test
<Habitat object family> × <Fauna object family>

## Expected outcome
PASS / ABSTAIN / DENY / FAIL_CLOSED / NEEDS_REDACTION_RECEIPT / NEEDS_REVIEW

## Governed support pointers
- Habitat contract: <path or N/A>
- Fauna contract: <path or N/A>
- Policy: <path or N/A>
- Fixture: <path or N/A>
- Validator: <path or N/A>
- Evidence/proof: <path or N/A>
- Redaction/Aggregation receipt: <path or N/A>
- Release/correction/rollback: <path or N/A>

## Assertion summary
<what cross-domain boundary must be proven>

## Leakage checks
<fields, geometry, summaries, stores, or route outputs that must not expose sensitive detail>

## Reviewer
<Habitat steward, Fauna steward, sensitivity reviewer, or maintainer>
```

## Validation

```bash
find tests/cross-domain/habitat-fauna -maxdepth 5 -type f | sort
find tests contracts/domains/habitat contracts/domains/fauna policy fixtures tools/validators data release -maxdepth 5 -type f 2>/dev/null | sort
pytest tests/cross-domain/habitat-fauna tests/policy || true
```

Replace `|| true` with fail-closed CI behavior once accepted cross-domain test commands are confirmed.

## Review checklist

- [ ] Test proves a Habitat × Fauna boundary, not only local function behavior.
- [ ] Habitat and Fauna object ownership remain separate and explicit.
- [ ] Join sensitivity inherits the most restrictive input.
- [ ] Evidence, policy, review, release, and receipt assumptions are explicit where material.
- [ ] Test uses synthetic, redacted, or generalized fixtures only.
- [ ] Test does not define contracts, schemas, policies, fixtures, validators, lifecycle records, release state, or domain implementation.
- [ ] Failure should block promotion when the join affects public API/UI/map/tile output.

## Open questions

| Question | Status |
|---|---|
| Should the canonical cross-domain test parent be `tests/cross-domain/` or `tests/cross_domain/`? | NEEDS VERIFICATION |
| Should a parent `tests/cross-domain/README.md` be created to govern all cross-domain test lanes? | NEEDS VERIFICATION |
| Which Habitat × Fauna contracts and schemas should be tested first? | NEEDS VERIFICATION |
| Which fixtures are canonical for habitat-fauna sensitivity inheritance tests? | NEEDS VERIFICATION |
| Which validator path owns Habitat × Fauna join checks? | NEEDS VERIFICATION |
| Which CI workflow blocks release or promotion when habitat-fauna cross-domain tests fail? | NEEDS VERIFICATION |
