<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests/domains/atmosphere/policy-deny/readme
title: Atmosphere Policy-Deny Test Lane README
type: test-lane-readme
version: v0.1
status: draft
owners:
  - <PLACEHOLDER — Atmosphere steward>
  - <PLACEHOLDER — Policy steward>
  - <PLACEHOLDER — Test steward>
  - <PLACEHOLDER — Evidence/governance reviewer>
created: 2026-07-05
updated: 2026-07-05
policy_label: public
implementation_status: scaffold
verification_status: current-session path verified; child lane implementation, fixtures, validators, policy bundles, and CI not verified
related:
  - tests/README.md
  - tests/domains/atmosphere/README.md
  - docs/doctrine/directory-rules.md
  - docs/domains/atmosphere/FILE_SYSTEM_PLAN.md
  - docs/domains/atmosphere/POLICY.md
  - docs/domains/atmosphere/KNOWLEDGE_CHARACTERS.md
  - docs/domains/atmosphere/KNOWLEDGE_CHARACTER_REGISTRY.md
  - policy/domains/atmosphere/
  - contracts/domains/atmosphere/
  - schemas/contracts/v1/domains/atmosphere/
  - fixtures/domains/atmosphere/
  - tools/validators/
  - release/
  - data/receipts/
  - data/proofs/
tags:
  - kfm
  - tests
  - atmosphere
  - policy-deny
  - negative-tests
  - fail-closed
  - evidence
  - governance
  - no-network
  - cite-or-abstain
] -->

<a id="top"></a>

# Atmosphere Policy-Deny Tests

> Parent test-lane contract for Atmosphere / Air negative policy tests. This directory proves that policy-significant Atmosphere claims fail closed when object meaning, source role, knowledge character, evidence, caveat, review, freshness, sensitivity, rights, or release requirements are missing or collapsed.

![status: draft](https://img.shields.io/badge/status-draft-orange)
![lane: tests%2Fdomains%2Fatmosphere%2Fpolicy--deny-informational](https://img.shields.io/badge/lane-tests%2Fdomains%2Fatmosphere%2Fpolicy--deny-informational)
![policy: fail--closed](https://img.shields.io/badge/policy-fail--closed-blue)
![authority: tests--only](https://img.shields.io/badge/authority-tests--only-lightgrey)
![implementation: scaffold](https://img.shields.io/badge/implementation-scaffold-yellow)

**Status:** `draft`  
**Authority:** parent test-lane README; not a schema, policy implementation, validator, source registry, release decision, receipt, proof, or fixture inventory  
**Owning root:** `tests/`  
**Domain segment:** `domains/atmosphere/`  
**Lane:** `policy-deny/`  
**Default posture:** fail closed; cite-or-abstain; preserve policy-significant distinctions  
**Last reviewed:** 2026-07-05

> [!IMPORTANT]
> KFM Atmosphere is **not** an emergency alerting or life-safety system. This lane can test advisory-context boundaries, but it must not make KFM the issuing authority for official alerts, protective action, or emergency instructions.

---

## Contents

1. [Purpose](#1-purpose)
2. [Directory fit and authority](#2-directory-fit-and-authority)
3. [Status and evidence boundary](#3-status-and-evidence-boundary)
4. [What belongs here](#4-what-belongs-here)
5. [What does not belong here](#5-what-does-not-belong-here)
6. [Policy-deny spine](#6-policy-deny-spine)
7. [Child lane map](#7-child-lane-map)
8. [Expected finite outcomes](#8-expected-finite-outcomes)
9. [Fixture contract](#9-fixture-contract)
10. [Lifecycle and publication boundaries](#10-lifecycle-and-publication-boundaries)
11. [No-network default](#11-no-network-default)
12. [Suggested local commands](#12-suggested-local-commands)
13. [Review burden](#13-review-burden)
14. [Related folders](#14-related-folders)
15. [Open questions](#15-open-questions)
16. [Definition of done](#16-definition-of-done)
17. [Changelog](#17-changelog)
18. [Last reviewed](#18-last-reviewed)

---

## 1. Purpose

This directory is the Atmosphere / Air parent lane for **policy-deny tests**.

Its job is to prove that Atmosphere records, layers, API responses, AI answers, catalog candidates, graph projections, UI labels, and release candidates do not pass when they collapse policy-significant distinctions.

A mature policy-deny lane should support these claims:

1. **Negative cases fail closed.** Unsupported or mischaracterized Atmosphere claims produce `DENY`, `ABSTAIN`, `RESTRICT`, `HOLD`, `ERROR`, or validation failure as appropriate.
2. **Evidence outranks labels.** Renaming a field, layer, tooltip, record, or generated answer cannot convert one knowledge character or object family into another.
3. **Policy definitions remain external.** Tests call policy and validator logic from canonical homes; tests do not become policy implementations.
4. **Fixtures are controlled.** Invalid fixtures are deterministic, public-safe, no-network, and kept in the governed fixture lane unless deliberately test-local.
5. **Publication remains governed.** A passing test can support a release review, but it is never a release decision by itself.
6. **AI surfaces are downstream carriers.** Generated language must abstain or qualify when evidence and policy do not support a claim.

---

## 2. Directory fit and authority

Directory Rules place enforceability proof under `tests/`. Domain-specific test material uses the domain as a segment inside the responsibility root:

```text
tests/domains/atmosphere/policy-deny/
```

This path is correct because:

| Placement question | Answer |
|---|---|
| Primary responsibility | Prove Atmosphere policy negative cases and fail-closed behavior. |
| Owning root | `tests/` |
| Domain segment | `domains/atmosphere/` |
| Parent lane | `policy-deny/` |
| Policy home | `policy/domains/atmosphere/` |
| Validator home | `tools/validators/` |
| Object meaning home | `contracts/domains/atmosphere/` |
| Machine shape home | `schemas/contracts/v1/domains/atmosphere/` when schemas exist. |
| Fixture home | `fixtures/domains/atmosphere/` unless tiny local test-only samples are documented. |
| Source registry home | `data/registry/sources/atmosphere/` when present. |
| Release home | `release/` |
| Receipts/proofs home | `data/receipts/` and `data/proofs/` |

> [!WARNING]
> This directory must not become a second policy, schema, contract, fixture, receipt, proof, registry, or release home. It proves behavior against those authorities.

[↑ Back to top](#top)

---

## 3. Status and evidence boundary

| Item | Status |
|---|---|
| Target README path exists in repo | CONFIRMED in this session before this README update. |
| Directory Rules basis for `tests/domains/<domain>/` | CONFIRMED from current repo doctrine. |
| `tests/README.md` allows policy tests and negative cases that fail closed | CONFIRMED from current repo docs. |
| Atmosphere file-system plan names `tests/domains/atmosphere/policy-deny/` | CONFIRMED; plan language includes PROPOSED lane details. |
| Atmosphere policy docs name the policy-deny spine | CONFIRMED from current repo docs. |
| Actual child test implementations | UNKNOWN in this README. |
| Actual reusable invalid fixture inventory | NEEDS VERIFICATION. |
| Canonical policy module names and package names | NEEDS VERIFICATION. |
| Canonical pytest markers and CI job names | NEEDS VERIFICATION. |
| Runtime/API/UI behavior | NEEDS VERIFICATION unless proven by tests outside this README. |

This README defines the parent lane contract. It does not claim that all child tests, validators, Rego bundles, fixtures, CI jobs, or runtime integrations are already complete.

---

## 4. What belongs here

This directory may contain:

- README and lane contract material for Atmosphere policy negative tests.
- Parent-level tests that check shared policy-deny behavior across multiple child lanes.
- Tests that assert required source role and knowledge-character fields are present before a claim is allowed.
- Tests that assert finite outcomes for policy failure cases.
- Tests that call canonical policy and validator logic from their owning roots.
- Tests that assert policy-deny fixtures are local, deterministic, public-safe, and no-network.
- Tests that ensure UI/API/AI/catalog surfaces preserve denial, restriction, abstention, caveat, and trust-state information.
- Tiny local test-only examples when they are not reusable fixtures and the reason is documented.

---

## 5. What does not belong here

This directory must not contain:

- Policy implementation files.
- Production validators, pipelines, connectors, adapters, or transformation code.
- Raw source payloads, live source pulls, downloaded caches, processed datasets, catalog records, triplets, or published layers.
- Real credentials, API keys, service accounts, cookies, signed URLs, or private endpoints.
- Schema, contract, source registry, release, receipt, or proof definitions.
- Reusable fixture inventories that belong under `fixtures/domains/atmosphere/`.
- Tests that run live network calls by default.
- Emergency or life-safety instructions that present KFM as the issuing authority.

> [!CAUTION]
> A test that redefines policy locally can pass while the system still violates policy. Tests should import or invoke policy/validator behavior from the canonical implementation when that implementation exists.

[↑ Back to top](#top)

---

## 6. Policy-deny spine

The Atmosphere policy spine names these negative or restrictive cases:

| Policy intent | Guarded distinction | Parent-lane expectation |
|---|---|---|
| AQI is not concentration | Public AQI report vs pollutant concentration observation | Deny or abstain when AQI/report/index objects are presented as concentration observations. |
| AOD is not PM2.5 | Remote-sensing/AOD context vs PM2.5 measurement | Deny or abstain when AOD/mask/raster context is presented as PM2.5 measurement without governed transformation. |
| Model is not observation | Model/forecast/reanalysis context vs observed sensor measurement | Deny or abstain when model output is presented as observed data without governed observed object identity. |
| Source role required | Missing or collapsed source role / knowledge character | Deny when source role or knowledge character is absent or unsupported. |
| Low-cost sensor caveats | Low-cost sensor context vs uncaveated/high-authority claim | Restrict, deny, hold, or abstain when required caveats/confidence/limitations are absent. |
| Advisory is not issuing authority | Advisory context vs official emergency instruction | Deny or redirect when KFM output would replace the official authority. |
| Freshness gate | Current/fresh vs stale source cadence | Restrict, deny, hold, or mark stale when source cadence is exceeded. |
| Dryrun no live fetch | Deterministic test/dryrun vs live network/source access | Deny live HTTP/network access in default tests and dryrun paths. |

This table is a README summary of the lane spine. The governing policy files and tests remain authoritative only when implemented and verified.

---

## 7. Child lane map

Expected or active child lanes include:

| Child lane | Purpose | Status boundary |
|---|---|---|
| `aqi-vs-concentration/` | AQI/report/index objects must not be treated as concentration observations. | README work may exist in an open PR; implementation depth NEEDS VERIFICATION. |
| `aod-vs-pm25/` | AOD/raster/remote-sensing context must not be treated as PM2.5 measurement without governed transformation. | README work may exist in an open PR; implementation depth NEEDS VERIFICATION. |
| `low-cost-sensor-caveat/` | Low-cost sensor records require caveat/confidence/limitation controls for strong claims or public promotion. | README work may exist in an open PR; implementation depth NEEDS VERIFICATION. |
| `model-vs-observed/` | Model/forecast/reanalysis context must not be treated as observed sensor measurement. | README work may exist in an open PR; implementation depth NEEDS VERIFICATION. |
| `advisory-not-alert/` | Advisory context must not replace official alerting or emergency authority. | PROPOSED / NEEDS VERIFICATION unless implemented. |
| `source-role-required/` | Source role and knowledge character must be present and valid. | PROPOSED / NEEDS VERIFICATION unless implemented. |
| `freshness-gate/` | Stale source values must not be surfaced as fresh. | PROPOSED / NEEDS VERIFICATION unless implemented. |
| `dryrun-no-live-fetch/` | Default test/dryrun paths must not perform live source fetches. | PROPOSED / NEEDS VERIFICATION unless implemented. |

Child README files document sublane intent. They do not prove tests exist unless actual test files and CI/runtime evidence are verified.

---

## 8. Expected finite outcomes

Policy-deny tests should prefer finite, inspectable outcomes:

```text
ANSWER | ABSTAIN | DENY | ERROR
```

Policy/review pipelines may also use review or promotion outcomes such as:

```text
ALLOW | RESTRICT | DENY | HOLD | ERROR
```

| Condition | Preferred outcome |
|---|---|
| Missing source role or knowledge character | `DENY` or validation failure. |
| Missing EvidenceRef / EvidenceBundle for an evidence-dependent claim | `ABSTAIN` or validation failure. |
| Unsupported object-family conversion | `DENY` or validation failure. |
| Missing caveat/confidence/limitation field | `RESTRICT`, `DENY`, `HOLD`, or validation failure. |
| Stale source cadence | `RESTRICT`, `HOLD`, stale marker, `DENY`, or validation failure. |
| Unresolved rights or review state | `DENY`, `HOLD`, or validation failure. |
| Policy module missing or ambiguous | `ERROR` in test setup, not silent pass. |
| Fixture missing | Test failure with clear path. |
| Generated response lacks cited support | `ABSTAIN` or corrected answer with caveat. |
| Valid governed product with evidence, policy, review, and release posture | Allowed only under correct governed identity. |

---

## 9. Fixture contract

Reusable policy-deny fixtures should normally live under:

```text
fixtures/domains/atmosphere/
```

Expected invalid fixture families include:

| Fixture family | Example use |
|---|---|
| `aqi-as-concentration/` | AQI/report object mislabeled as concentration. |
| `aod-as-pm25/` | AOD/raster object mislabeled as PM2.5 measurement. |
| `model-as-observed/` | Model/forecast object mislabeled as observation. |
| `low-cost-sensor-missing-caveat/` | Low-cost sensor record missing required caveat/confidence/limitation controls. |
| `advisory-as-alert/` | Advisory context overstepping issuing-authority boundary. |
| `missing-source-role/` | Atmosphere object without source role or knowledge character. |
| `stale-source/` | Source record beyond cadence/freshness window. |
| `live-fetch-in-dryrun/` | Operational fixture proving live fetch attempts fail in dryrun/default tests. |

Fixture records should be deterministic, public-safe, no-network, and visibly test-only or governed fixture data. They must not be raw source payloads or release artifacts.

---

## 10. Lifecycle and publication boundaries

This lane supports the KFM lifecycle but does not move records through it:

```text
RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED
```

| Boundary | Rule |
|---|---|
| RAW | Do not place raw source payloads in this directory. |
| WORK / QUARANTINE | Do not use this directory as scratch processing storage. |
| PROCESSED | Do not store processed Atmosphere products here. |
| CATALOG / TRIPLET | Do not treat test outputs as catalog or graph truth. |
| PUBLISHED | Tests never publish. |
| RECEIPTS / PROOFS | Do not store trust-bearing receipts or proofs here. |
| RELEASE | Release decisions remain under `release/`. |

A policy-deny pass means the code path behaved as expected for a negative case. It is not a release approval.

---

## 11. No-network default

Default Atmosphere policy-deny tests must avoid:

- live source services,
- internet access,
- live tile or geocode requests,
- local credential files,
- developer machine caches,
- private endpoints,
- mutable upstream API responses, and
- direct source-system side effects.

Live-source checks, if ever needed, should be integration/manual only and excluded from default CI.

---

## 12. Suggested local commands

> [!NOTE]
> Command names, policy test runners, marker names, and CI job names are **NEEDS VERIFICATION** until checked against the actual repository configuration.

Likely parent lane check:

```bash
pytest tests/domains/atmosphere/policy-deny
```

Likely full Atmosphere test check:

```bash
pytest tests/domains/atmosphere
```

Possible policy engine check if configured:

```bash
opa test policy/domains/atmosphere tests/domains/atmosphere/policy-deny
```

Possible repo-wide validation command if implemented:

```bash
python tools/validate_all.py
```

---

## 13. Review burden

Reviewers should be able to answer:

- Does this lane test negative policy behavior rather than implement policy?
- Do tests call canonical validators and policy modules when available?
- Do unsupported claims fail closed?
- Are object-family, source-role, knowledge-character, time-kind, caveat, evidence, rights, review, and freshness distinctions preserved?
- Are generated answers and UI/API/catalog surfaces prevented from overclaiming?
- Are fixtures local, deterministic, public-safe, and no-network?
- Are reusable fixtures kept under the fixture root rather than duplicated here?
- Are receipts, proofs, release decisions, and source data kept out of this directory?
- Are policy scaffold gaps and filename/package drift marked NEEDS VERIFICATION instead of hidden?

---

## 14. Related folders

| Path | Relationship |
|---|---|
| `tests/domains/atmosphere/` | Parent Atmosphere test lane. |
| `tests/domains/atmosphere/source-role/` | Source-role anti-collapse tests. |
| `tests/domains/atmosphere/knowledge-character/` | Knowledge-character anti-collapse tests. |
| `tests/domains/atmosphere/no-network/` | Broad no-network/default-offline behavior. |
| `tests/domains/atmosphere/no-network-fixtures/` | Fixture-specific no-network/public-safe fixture discipline. |
| `policy/domains/atmosphere/` | Canonical Atmosphere policy home. |
| `contracts/domains/atmosphere/` | Object-meaning contracts. |
| `schemas/contracts/v1/domains/atmosphere/` | Machine-readable contract schemas when present. |
| `fixtures/domains/atmosphere/` | Reusable valid/invalid fixture home. |
| `tools/validators/` | Validator implementation home. |
| `docs/domains/atmosphere/` | Human-facing Atmosphere domain doctrine. |
| `release/` | Release decisions and candidates. |
| `data/receipts/` | Trust-bearing receipts. |
| `data/proofs/` | Proof artifacts. |

---

## 15. Open questions

| Question | Status | Notes |
|---|---|---|
| Which child policy-deny sublanes are present on `main` versus open PR branches? | NEEDS VERIFICATION | This README does not assume prior child README PRs are merged. |
| Which policy filenames are canonical? | NEEDS VERIFICATION | Planning names and scaffold filenames may differ. |
| What is the canonical OPA/Rego package naming convention? | NEEDS VERIFICATION | Must align with final policy tooling. |
| Which pytest markers are canonical for policy-deny, no-network, and integration tests? | NEEDS VERIFICATION | Candidate names are not authoritative. |
| Which CI job proves Atmosphere policy-deny behavior? | NEEDS VERIFICATION | Must be checked against `.github/workflows/`. |
| Should UI/API/AI trust-state negative tests live here or in their surface-specific test lanes? | OPEN | Parent lane may own policy units; surface lanes may own rendering/envelope tests. |
| Which invalid fixtures are synthetic, transformed public samples, or source-derived fixture records? | NEEDS VERIFICATION | Prefer public-safe transformed or synthetic fixtures. |

---

## 16. Definition of done

This lane is mature when:

- [ ] Parent policy-deny tests run locally.
- [ ] Child denial/restriction lanes have README contracts and at least one executable negative test each.
- [ ] Tests call canonical policy/validator code rather than redefining policy locally.
- [ ] Invalid fixtures are deterministic, public-safe, no-network, and stored in the governed fixture lane unless test-local.
- [ ] Unsupported claims produce finite outcomes rather than silent pass-through.
- [ ] UI/API/AI/catalog overclaim paths are covered here or delegated with links.
- [ ] Receipts, proofs, release decisions, source registries, schemas, contracts, and policy definitions remain in their canonical roots.
- [ ] CI exposes the policy-deny proof clearly enough for reviewers.
- [ ] Open questions are resolved or tracked in a verification backlog.

---

## 17. Changelog

| Date | Version | Change |
|---|---:|---|
| 2026-07-05 | v0.1 | Initial governed README for the Atmosphere policy-deny parent test lane. |

---

## 18. Last reviewed

**2026-07-05** — Initial README scaffold. Target path was present but empty before update. Current evidence confirms the tests root, Directory Rules domain segment rule, Atmosphere file-system plan, and Atmosphere policy spine; child test implementation, fixture inventory, canonical module names, validator behavior, and CI enforcement remain **NEEDS VERIFICATION**.

[↑ Back to top](#top)
