<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests/domains/atmosphere/readme
title: Atmosphere Domain Test Lane README
type: domain-test-readme
version: v0.1
status: draft
owners:
  - <PLACEHOLDER — Atmosphere steward>
  - <PLACEHOLDER — Test steward>
  - <PLACEHOLDER — Policy steward>
  - <PLACEHOLDER — Schema steward>
  - <PLACEHOLDER — Evidence/governance reviewer>
created: 2026-07-05
updated: 2026-07-05
policy_label: public
implementation_status: scaffold
verification_status: current-session path verified; child lanes listed in plan; executable tests, fixtures, validators, and CI not verified
related:
  - tests/README.md
  - docs/doctrine/directory-rules.md
  - docs/domains/atmosphere/README.md
  - docs/domains/atmosphere/FILE_SYSTEM_PLAN.md
  - docs/domains/atmosphere/POLICY.md
  - contracts/domains/atmosphere/
  - schemas/contracts/v1/domains/atmosphere/
  - policy/domains/atmosphere/
  - fixtures/domains/atmosphere/
  - tools/validators/
  - pipelines/domains/atmosphere/
  - data/receipts/
  - data/proofs/
  - release/
tags:
  - kfm
  - tests
  - domains
  - atmosphere
  - air
  - schema
  - policy-deny
  - source-role
  - knowledge-character
  - unit-normalization
  - no-network
  - evidence
  - fail-closed
] -->

<a id="top"></a>

# Atmosphere Domain Tests

> Parent test-lane contract for Atmosphere / Air domain tests. This directory verifies that Atmosphere records, claims, fixtures, schemas, policies, validators, and public-facing envelopes preserve evidence, object meaning, source role, knowledge character, units, time facets, caveats, and finite outcomes without becoming a second authority root.

![status: draft](https://img.shields.io/badge/status-draft-orange)
![lane: tests%2Fdomains%2Fatmosphere-informational](https://img.shields.io/badge/lane-tests%2Fdomains%2Fatmosphere-informational)
![authority: tests--only](https://img.shields.io/badge/authority-tests--only-lightgrey)
![posture: no--network](https://img.shields.io/badge/posture-no--network-blue)
![implementation: scaffold](https://img.shields.io/badge/implementation-scaffold-yellow)

**Status:** `draft`  
**Authority:** parent domain-test README; not a schema, contract, policy implementation, validator, fixture inventory, source registry, receipt, proof, release decision, or published artifact  
**Owning root:** `tests/`  
**Domain segment:** `domains/atmosphere/`  
**Default posture:** deterministic, public-safe fixtures; finite outcomes; cite-or-abstain  
**Last reviewed:** 2026-07-05

---

## Contents

1. [Purpose](#1-purpose)
2. [Directory fit and authority](#2-directory-fit-and-authority)
3. [Status and evidence boundary](#3-status-and-evidence-boundary)
4. [Domain test lanes](#4-domain-test-lanes)
5. [What belongs here](#5-what-belongs-here)
6. [What does not belong here](#6-what-does-not-belong-here)
7. [Shared proof matrix](#7-shared-proof-matrix)
8. [Fixture posture](#8-fixture-posture)
9. [Expected outcomes](#9-expected-outcomes)
10. [Lifecycle boundaries](#10-lifecycle-boundaries)
11. [No-network default](#11-no-network-default)
12. [Suggested local commands](#12-suggested-local-commands)
13. [Review burden](#13-review-burden)
14. [Related folders and files](#14-related-folders-and-files)
15. [Open questions](#15-open-questions)
16. [Definition of done](#16-definition-of-done)
17. [Changelog](#17-changelog)
18. [Last reviewed](#18-last-reviewed)

---

## 1. Purpose

This directory is the parent test lane for the Atmosphere / Air domain.

It exists to prove that Atmosphere behavior is governed and inspectable across schema validation, object meaning, policy denials, source-role boundaries, knowledge-character boundaries, unit normalization, no-network test discipline, evidence resolution, lifecycle state, and public-facing response envelopes.

A mature Atmosphere test lane should support these claims:

1. **Domain-specific tests live under the test root.** Atmosphere is a segment inside `tests/`, not a competing root.
2. **Tests verify behavior; they do not implement it.** Schemas, contracts, policy, validators, fixtures, receipts, proofs, releases, and production code remain in their own roots.
3. **Evidence-dependent claims resolve or abstain.** If an Atmosphere claim needs evidence, the test should require a resolvable evidence path or a finite abstention/denial outcome.
4. **Object meaning does not collapse.** Air stations, observations, AQI/report context, PM2.5, ozone, AOD, smoke, model context, weather, climate, advisory context, proofs, receipts, and release objects remain distinct.
5. **Units and time facets remain explicit.** Unit normalization, averaging period, observed time, valid time, issue time, retrieval time, and processing time must not be silently flattened.
6. **Default tests are deterministic.** Tests should use local public-safe fixtures and avoid live network calls unless explicitly marked outside the default suite.
7. **Publication remains governed.** A passing test can support review, but it is not release approval.

---

## 2. Directory fit and authority

Directory Rules place domain-specific tests under the `tests/` responsibility root with the domain as a segment:

```text
tests/domains/atmosphere/
```

This path is correct because:

| Placement question | Answer |
|---|---|
| Primary responsibility | Prove Atmosphere domain behavior. |
| Owning root | `tests/` |
| Domain segment | `domains/atmosphere/` |
| Schema home | `schemas/contracts/v1/domains/atmosphere/` |
| Contract home | `contracts/domains/atmosphere/` |
| Policy home | `policy/domains/atmosphere/` |
| Validator home | `tools/validators/` |
| Fixture home | `fixtures/domains/atmosphere/` unless tiny test-local fixtures are documented. |
| Pipeline home | `pipelines/domains/atmosphere/` |
| Receipt/proof homes | `data/receipts/` and `data/proofs/` |
| Release home | `release/` |

> [!WARNING]
> This directory must not become a second schema, contract, policy, validator, fixture, source-registry, receipt, proof, release, or data home. It verifies behavior against those authorities.

[↑ Back to top](#top)

---

## 3. Status and evidence boundary

| Item | Status |
|---|---|
| Target README path exists in repo | CONFIRMED in this session; previous content was a greenfield stub. |
| Directory Rules basis for `tests/domains/<domain>/` | CONFIRMED from current repo doctrine. |
| `tests/README.md` allows domain-specific tests under `tests/domains/<domain>/` | CONFIRMED from current repo docs. |
| `tests/README.md` allows schema, contract, validator, policy, evidence, lifecycle, receipt/proof, release-manifest, API, UI, e2e, runtime-proof, and domain-specific tests | CONFIRMED from current repo docs. |
| Atmosphere file-system plan lists `tests/domains/atmosphere/` child lanes | CONFIRMED from current repo docs. |
| Atmosphere policy spine lists key deny/restrict rules | CONFIRMED from current repo docs. |
| Executable tests under each child lane | UNKNOWN in this README. |
| Fixture inventory | NEEDS VERIFICATION. |
| Validator modules and commands | NEEDS VERIFICATION. |
| CI job names / pytest markers | NEEDS VERIFICATION. |
| Runtime/API/UI behavior | NEEDS VERIFICATION unless supported by executable tests. |

This README defines the parent domain-test lane contract. It does not claim that every child lane, fixture set, validator, policy bundle, or CI gate is complete.

---

## 4. Domain test lanes

The Atmosphere file-system plan names these child lanes under `tests/domains/atmosphere/`:

| Child lane | Responsibility | Status boundary |
|---|---|---|
| `schema/` | Schema shape, metadata, and schema-to-contract alignment tests. | Parent/child README work may exist in open PRs; executable tests NEED VERIFICATION. |
| `source-role/` | Source-role anti-collapse tests. | NEEDS VERIFICATION beyond existing docs. |
| `knowledge-character/` | Knowledge-character boundary tests. | README work may exist in open PRs; executable tests NEED VERIFICATION. |
| `unit-normalization/` | Unit conversion and normalization behavior tests. | README work may exist in an open PR; executable tests NEED VERIFICATION. |
| `policy-deny/` | Negative policy tests that fail closed for unsupported or collapsed claims. | Parent/child README work may exist in open PRs; executable tests NEED VERIFICATION. |
| `no-network-fixtures/` | Public-safe deterministic fixture discipline for no-network tests. | README work may exist in open PRs; fixture inventory NEEDS VERIFICATION. |
| `no-network/` | Default offline/no-network behavior for Atmosphere tests. | README work may exist in open PRs; enforcement NEEDS VERIFICATION. |

Additional sublanes may be added when they have a clear test responsibility and do not duplicate an existing authority root.

---

## 5. What belongs here

This directory may contain:

- README files that define Atmosphere test-lane contracts.
- Domain-specific tests that verify schema, contract, validator, policy, evidence, lifecycle, API, UI, runtime, and fixture behavior for Atmosphere objects.
- Tests that call canonical schema, policy, validator, fixture, and pipeline code from the owning roots.
- Tests that prove Atmosphere outputs use finite outcomes such as `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` where applicable.
- Tests that prove child lanes do not leak source data, internal stores, or unpublished candidates into public-facing surfaces.
- Small test-local examples when they are not reusable fixtures and the reason is documented.

---

## 6. What does not belong here

This directory must not contain:

- Production code or pipeline implementation.
- Schema, contract, policy, or registry definitions.
- Raw source payloads, normalized data products, catalog records, triplets, published layers, reports, or downloads.
- Trust-bearing receipts, proofs, release decisions, rollback decisions, or public artifacts.
- Reusable fixture inventories that belong under `fixtures/domains/atmosphere/`.
- Live source credentials, private endpoints, or developer-local cache material.
- Default tests that require live network access.

[↑ Back to top](#top)

---

## 7. Shared proof matrix

| Test concern | Required proof | Owning or likely child lane |
|---|---|---|
| Schema path resolves | Atmosphere schemas load from canonical schema root. | `schema/` |
| Contract meaning preserved | Object family cannot be changed by field naming alone. | `schema/`, `knowledge-character/`, `policy-deny/` |
| Source role present | Records that need source role carry it or fail closed. | `source-role/`, `policy-deny/` |
| Knowledge character present | Records carry valid character or fail closed. | `knowledge-character/`, `policy-deny/` |
| Unit normalization is auditable | Source unit, target unit, method, and receipt expectations are explicit. | `unit-normalization/` |
| AQI/report boundary preserved | AQI/report context is not treated as concentration by label change. | `policy-deny/` |
| AOD/PM2.5 boundary preserved | AOD/raster context is not treated as PM2.5 measurement by label change. | `policy-deny/` |
| Model/observed boundary preserved | Model/forecast context is not treated as observed measurement by label change. | `policy-deny/` |
| Low-cost sensor caveats travel | Caveat, correction, confidence, and limitation fields remain visible where required. | `policy-deny/`, `knowledge-character/` |
| No-network default | Default tests avoid live services and mutable upstream state. | `no-network/`, `no-network-fixtures/` |
| Fixture boundary | Reusable fixtures live under fixture roots and are public-safe. | `no-network-fixtures/`, child lanes |
| Evidence behavior | Evidence-dependent claims resolve evidence or return finite abstention/denial. | domain tests, runtime/API lanes |
| Lifecycle boundary | Test outputs are not catalog truth, proof, or release approval. | parent lane plus child lanes |

---

## 8. Fixture posture

Reusable Atmosphere fixtures should normally live under:

```text
fixtures/domains/atmosphere/
```

This test root may contain tiny local examples only when:

- they are not reusable fixture records;
- they are small enough to inspect in a test file;
- they do not duplicate fixture-root responsibilities;
- they are deterministic and public-safe; and
- the test explains why they are local.

Expected fixture families include valid and invalid examples for stations, observations, pollutant-specific records, AQI/report context, AOD context, model context, unit-normalization cases, missing source role, missing knowledge character, stale-source examples, and no-network behavior.

---

## 9. Expected outcomes

Atmosphere tests should prefer finite, inspectable outcomes:

```text
ANSWER | ABSTAIN | DENY | ERROR
```

Review or pipeline tests may also use workflow outcomes such as:

```text
ALLOW | RESTRICT | DENY | HOLD | ERROR | NEEDS_REVIEW | QUARANTINE
```

| Condition | Preferred outcome |
|---|---|
| EvidenceRef missing for evidence-dependent claim | `ABSTAIN`, `DENY`, or validation failure. |
| Source role or knowledge character missing | `DENY` or validation failure. |
| Object-family collapse | `DENY` or validation failure. |
| Unit ambiguity | `HOLD`, `DENY`, `ERROR`, or validation failure. |
| Fixture attempts live access in default suite | Test failure or `DENY`. |
| Policy module missing or ambiguous | `ERROR` in test setup, not silent pass. |
| Valid governed case | Allowed only for the checked scope; not release approval. |

---

## 10. Lifecycle boundaries

Atmosphere tests support the KFM lifecycle but do not move records through it:

```text
RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED
```

| Boundary | Rule |
|---|---|
| RAW | Do not store raw source payloads in this test tree. |
| WORK / QUARANTINE | Tests may verify behavior but do not become work storage. |
| PROCESSED | Do not store processed Atmosphere products here. |
| CATALOG / TRIPLET | Do not treat test output as catalog or graph truth. |
| PUBLISHED | Tests do not publish. |
| RECEIPTS / PROOFS | Tests may assert references; trust-bearing records stay in their roots. |
| RELEASE | Release decisions remain under `release/`. |

---

## 11. No-network default

Default Atmosphere tests should avoid:

- live source services,
- internet access,
- remote schema or unit-registry fetching,
- local credential files,
- developer machine caches,
- mutable upstream API responses, and
- direct source-system side effects.

Live or integration checks, if needed, should be explicitly marked outside the default suite.

---

## 12. Suggested local commands

> [!NOTE]
> Command names, validator names, marker names, and CI job names are **NEEDS VERIFICATION** until checked against actual repo configuration.

Likely domain lane check:

```bash
pytest tests/domains/atmosphere
```

Likely child lane checks:

```bash
pytest tests/domains/atmosphere/schema
pytest tests/domains/atmosphere/policy-deny
pytest tests/domains/atmosphere/unit-normalization
```

Possible repo-wide validation command if implemented:

```bash
python tools/validate_all.py
```

---

## 13. Review burden

Reviewers should be able to answer:

- Does this tree verify Atmosphere behavior rather than define production authority?
- Do child lanes call canonical schemas, contracts, policies, validators, fixtures, and pipelines instead of redefining them?
- Are source roles, knowledge characters, object families, units, caveats, time facets, and evidence requirements preserved?
- Do unsupported claims fail closed or abstain?
- Are fixtures deterministic, public-safe, and no-network by default?
- Are receipts, proofs, releases, source registries, schemas, contracts, and policy definitions kept in their canonical roots?
- Are implementation gaps marked **UNKNOWN** or **NEEDS VERIFICATION** instead of hidden?

---

## 14. Related folders and files

| Path | Relationship |
|---|---|
| `tests/README.md` | Root test contract and allowed test content. |
| `docs/domains/atmosphere/README.md` | Human-facing Atmosphere domain lane doctrine. |
| `docs/domains/atmosphere/FILE_SYSTEM_PLAN.md` | Planning document listing this test root and child lanes. |
| `docs/domains/atmosphere/POLICY.md` | Human-facing policy spine that policy tests should verify against implementation. |
| `contracts/domains/atmosphere/` | Object-meaning contracts. |
| `schemas/contracts/v1/domains/atmosphere/` | Machine-readable schema home. |
| `policy/domains/atmosphere/` | Policy implementation home. |
| `fixtures/domains/atmosphere/` | Reusable fixture home. |
| `tools/validators/` | Validator implementation home. |
| `pipelines/domains/atmosphere/` | Pipeline implementation home. |
| `data/receipts/` | Trust-bearing process-memory records. |
| `data/proofs/` | Evidence/proof artifacts. |
| `release/` | Release decisions, candidates, and rollback/correction surfaces. |

---

## 15. Open questions

| Question | Status | Notes |
|---|---|---|
| Which child lanes already have executable tests on `main`? | NEEDS VERIFICATION | README branches are not implementation proof. |
| Which pytest markers are canonical for Atmosphere lanes? | NEEDS VERIFICATION | Must be checked against test config. |
| Which CI jobs run Atmosphere tests? | NEEDS VERIFICATION | Must be checked against `.github/workflows/`. |
| Which validators are canonical for schema, policy, unit, and evidence checks? | NEEDS VERIFICATION | Do not invent validator behavior. |
| Which fixture families are present and reviewed? | NEEDS VERIFICATION | Prefer root fixture lane with documented public-safe posture. |
| Should API/UI trust-state tests for Atmosphere live here or in surface-specific test roots? | OPEN | Parent lane may document linkage; surface roots may own rendering/envelope tests. |

---

## 16. Definition of done

This parent lane is mature when:

- [ ] Parent Atmosphere tests run locally.
- [ ] Each planned child lane has a README contract and at least one executable proof where implementation exists.
- [ ] Schema, source-role, knowledge-character, unit-normalization, policy-deny, and no-network expectations are covered or explicitly deferred.
- [ ] Reusable fixtures are deterministic, public-safe, and stored in the governed fixture root unless test-local.
- [ ] Tests call canonical validators/policies/schemas/contracts rather than redefining them locally.
- [ ] Evidence-dependent claims resolve evidence or produce finite abstention/denial.
- [ ] Tests run no-network by default.
- [ ] CI exposes the Atmosphere test proof clearly enough for reviewers.
- [ ] Open questions are resolved or tracked in a verification backlog.

---

## 17. Changelog

| Date | Version | Change |
|---|---:|---|
| 2026-07-05 | v0.1 | Replaced greenfield stub with governed Atmosphere domain-test README. |

---

## 18. Last reviewed

**2026-07-05** — Replaced greenfield stub. Current evidence confirms the tests root, Directory Rules domain-segment rule, Atmosphere file-system test lanes, Atmosphere domain README, and policy spine; executable tests, fixtures, validator behavior, child-lane merge state, and CI enforcement remain **NEEDS VERIFICATION**.

[↑ Back to top](#top)
