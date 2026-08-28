<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests/domains/flora/policy-deny/readme
title: Flora Policy Deny Test Lane README
type: test-lane-readme
version: v0.1
status: draft
owners:
  - <PLACEHOLDER — Flora steward>
  - <PLACEHOLDER — Policy steward>
  - <PLACEHOLDER — Test steward>
created: 2026-07-05
updated: 2026-07-05
policy_label: public
implementation_status: scaffold
verification_status: current-session path verified; executable tests, fixtures, policy bundles, validators, review records, release manifests, and CI not verified
related:
  - tests/README.md
  - tests/domains/flora/README.md
  - tests/domains/flora/policy/README.md
  - tests/domains/flora/citation/README.md
  - tests/domains/flora/evidence_closure/README.md
  - tests/domains/flora/geometry/README.md
  - docs/doctrine/directory-rules.md
  - docs/domains/flora/README.md
  - policy/domains/flora/
  - policy/sensitivity/flora/
  - fixtures/domains/flora/
  - data/registry/sources/flora/
  - data/receipts/
  - data/proofs/flora/
  - release/
tags:
  - kfm
  - tests
  - flora
  - policy-deny
  - negative-tests
  - rights
  - sensitivity
  - review
  - release
  - finite-outcome
  - no-network
  - fail-closed
] -->

<a id="top"></a>

# Flora Policy Deny Tests

> Test-lane contract for proving Flora policy negative cases fail closed with finite, inspectable outcomes rather than silently rendering public claims, geometry, citations, layers, drawer payloads, Focus answers, or releases.

![status: draft](https://img.shields.io/badge/status-draft-orange)
![lane: tests%2Fdomains%2Fflora%2Fpolicy__deny-informational](https://img.shields.io/badge/lane-tests%2Fdomains%2Fflora%2Fpolicy__deny-informational)
![authority: tests--only](https://img.shields.io/badge/authority-tests--only-lightgrey)
![posture: fail--closed](https://img.shields.io/badge/posture-fail--closed-blue)
![implementation: scaffold](https://img.shields.io/badge/implementation-scaffold-yellow)

**Status:** `draft`  
**Authority:** negative policy test-lane README; not a policy bundle, review record, source registry, evidence store, fixture inventory, receipt, proof, release decision, or public artifact  
**Owning root:** `tests/`  
**Domain segment:** `domains/flora/`  
**Lane:** `policy_deny/`  
**Default posture:** public-safe fixtures; no-network by default; deny/abstain/error on unresolved governance state  
**Last reviewed:** 2026-07-05

---

## 1. Purpose

This directory is the Flora domain test lane for **policy-deny and fail-closed behavior**.

It exists to prove that Flora outputs are not allowed when governance support is incomplete, incompatible, unresolved, stale, restricted, or outside the requested scope. These tests focus on negative cases: the expected result is a finite outcome such as `DENY`, `ABSTAIN`, `ERROR`, or validation failure, not a public answer or hidden fallback.

A mature lane should prove:

1. Unknown rights, unresolved sensitivity, missing review, stale support, missing evidence, incompatible source role, and missing release boundary cases fail closed.
2. Negative policy outcomes remain visible to API, UI, drawer, Focus, layer, and export surfaces.
3. Deny and abstain states are not replaced by generated text, cached map state, styling, or empty panels.
4. Public-safe transformed fixtures are used where spatial or sensitive concepts are modeled.
5. Policy denial is distinct from evidence closure and release approval.
6. Default tests are deterministic and no-network.

---

## 2. Directory fit and authority

Directory Rules place domain-specific tests under the `tests/` responsibility root with the domain as a segment:

```text
tests/domains/flora/policy_deny/
```

| Placement question | Answer |
|---|---|
| Primary responsibility | Prove Flora policy negative and fail-closed behavior. |
| Owning root | `tests/` |
| Domain segment | `domains/flora/` |
| Test lane | `policy_deny/` |
| Parent policy lane | `tests/domains/flora/policy/` |
| Policy homes | `policy/domains/flora/` and `policy/sensitivity/flora/`. |
| Fixture home | `fixtures/domains/flora/` unless tiny test-local examples are documented. |
| Source registry home | `data/registry/sources/flora/` when present. |
| Receipt/proof homes | `data/receipts/` and `data/proofs/flora/`. |
| Release home | `release/`. |

> [!WARNING]
> This directory must not become a second policy home, deny-registry, review-record home, source registry, evidence store, fixture inventory, receipt home, proof home, release home, public artifact home, or source-data home.

[↑ Back to top](#top)

---

## 3. Status and evidence boundary

| Item | Status |
|---|---|
| Target README path exists in repo | CONFIRMED in this session before this README update. |
| Directory Rules basis for `tests/domains/<domain>/` | CONFIRMED from current repo doctrine. |
| `tests/README.md` allows policy tests, including negative cases that must fail closed | CONFIRMED from current repo docs. |
| `tests/README.md` allows evidence-resolution, lifecycle, receipt/proof, release-manifest, governed API, UI trust-state, runtime-proof, and domain-specific tests | CONFIRMED from current repo docs. |
| `tests/README.md` excludes sensitive material, live network calls, duplicate authority homes, trust-bearing records, and release decisions from `tests/` | CONFIRMED from current repo docs. |
| Flora docs identify policy roots as `policy/domains/flora/` and `policy/sensitivity/flora/` | CONFIRMED from current repo docs. |
| Flora docs state cite-or-abstain, deny-by-default protection for sensitive plant locations, and public-safe botanical outputs | CONFIRMED from current repo docs. |
| Actual executable tests in this directory | UNKNOWN in this README. |
| Actual deny fixtures, policy bundles, validators, review records, release manifests, and CI jobs | NEEDS VERIFICATION. |

This README defines the test-lane contract. It does not claim that policy-deny tests, fixtures, validators, policy bundles, review records, release manifests, or CI checks already exist.

---

## 4. Deny rule

**Rule:** A Flora request must fail closed when policy prerequisites for the requested public use are missing, incompatible, unresolved, or outside scope.

Tests should expect `DENY`, `ABSTAIN`, `ERROR`, or validation failure when:

- rights, attribution, or redistribution posture is unknown or incompatible;
- sensitivity state is unresolved or not public-safe for the requested use;
- required review state is missing;
- source role is incompatible with the claim or surface;
- evidence support is missing, stale, conflicted, or outside claim scope;
- public-safe transformation is required but lacks governance reference;
- release state, correction path, or rollback target is required but missing;
- browser, API, drawer, Focus, layer, tile, export, or generated text hides the negative policy state;
- cached or derived material bypasses policy re-check; or
- policy definitions, review records, receipts, proofs, or release decisions are stored under `tests/`.

Tests may assert an allowed result only when the negative condition has been removed by a governed fixture state and the test remains inside its validation scope.

---

## 5. Proof matrix

| Negative case | Required proof | Expected behavior |
|---|---|---|
| Unknown rights | Rights state is absent or incompatible. | `DENY`, `ABSTAIN`, or validation failure. |
| Unresolved sensitivity | Public-safe state is not established. | `DENY`, `ABSTAIN`, or non-render. |
| Missing review | Required review state is absent. | `DENY`, `ABSTAIN`, or validation failure. |
| Source-role mismatch | Source role does not support the claim. | `ABSTAIN`, `DENY`, or validation failure. |
| Missing evidence | Evidence reference is absent or unresolved. | `ABSTAIN` or validation failure. |
| Stale support | Freshness state blocks current presentation. | Trust-visible negative outcome. |
| Missing transformation reference | Public-safe derivative lacks required governance reference. | `DENY` or validation failure. |
| Missing release boundary | Release/correction/rollback requirement is absent. | `DENY`, `ERROR`, or validation failure. |
| Hidden negative state | UI/API/generated text suppresses denial or abstention. | Test failure. |
| No-network default | Negative tests run with local public-safe fixtures only. | Harness assertion. |

---

## 6. What belongs here

This directory may contain:

- README and lane contract material for Flora policy-deny tests.
- Tests that call canonical policy, sensitivity, evidence, source, review, release, API/UI, and validator code from owning roots.
- Negative fixtures for unknown rights, unresolved sensitivity, missing review, stale source, missing evidence, source-role mismatch, missing transformation reference, missing release boundary, cached bypass, and hidden negative state.
- Positive control fixtures only when needed to prove that the deny condition is the cause of failure.
- Tiny test-local examples when documented and not reusable fixture inventory.

## 7. What does not belong here

This directory must not contain policy definitions, deny registries, review records, source descriptors, source records, production evidence, reusable fixture inventories, schemas, contracts, trust-bearing receipts, proofs, release decisions, published artifacts, credentials, generated model output, or default tests that require live network access.

---

## 8. Fixture posture

Reusable Flora fixtures should normally live under:

```text
fixtures/domains/flora/
```

Fixture records should be deterministic, public-safe, no-network, and clearly test-only. They should model deny conditions rather than become policy definitions, review records, evidence bundles, receipts, proofs, or release decisions.

Expected fixture families include unknown rights, unresolved sensitivity, missing review, stale source, missing evidence, source-role mismatch, missing transformation reference, missing release boundary, hidden negative state, cached bypass, and valid allow-control.

---

## 9. Suggested local commands

> [!NOTE]
> Command names, validators, test runners, markers, workflow names, and exact package commands are **NEEDS VERIFICATION** until checked against actual repository configuration.

```bash
pytest tests/domains/flora/policy_deny
pytest tests/domains/flora/policy
pytest tests/domains/flora
python tools/validate_all.py
```

---

## 10. Open questions

| Question | Status | Notes |
|---|---|---|
| Which Flora deny-condition fixtures already exist? | NEEDS VERIFICATION | Must inspect `fixtures/domains/flora/`. |
| Which policy validator owns deny outcome checks? | NEEDS VERIFICATION | Must inspect validator/tool roots. |
| Which finite outcome envelope is canonical for Flora policy denial? | NEEDS VERIFICATION | Must inspect governed API contracts. |
| Which review or release references are required for each deny case? | NEEDS VERIFICATION | Must inspect policy/release roots. |
| Which CI job runs this lane? | NEEDS VERIFICATION | Must inspect `.github/workflows/`. |
| Should shared negative policy tests live here or under a cross-domain policy-deny test root? | OPEN | This lane should own Flora-specific expectations only. |

---

## 11. Definition of done

This lane is mature when:

- [ ] Flora policy-deny tests run locally.
- [ ] Unknown rights, unresolved sensitivity, missing review, stale source, missing evidence, source-role mismatch, missing transformation reference, missing release boundary, hidden negative state, and cached bypass cases are tested.
- [ ] Positive controls prove deny conditions are specific and not accidental harness failures.
- [ ] Tests call canonical policy/evidence/source/review/release/API validators rather than redefining behavior locally.
- [ ] Public-safe fixtures are used and verified no-network.
- [ ] CI exposes the Flora policy-deny proof clearly enough for reviewers.
- [ ] Open questions are resolved or tracked in a verification backlog.

---

## 12. Changelog

| Date | Version | Change |
|---|---:|---|
| 2026-07-05 | v0.1 | Initial governed README for the Flora policy-deny test lane. |

---

## 13. Last reviewed

**2026-07-05** — Initial README scaffold. Target path was present but empty before update. Current evidence confirms the tests root, Directory Rules domain-segment rule, root test allowance for policy negative cases and finite-outcome/domain tests, and Flora public-safe policy doctrine; executable tests, fixtures, policy bundles, validators, review records, release manifests, and CI enforcement remain **NEEDS VERIFICATION**.

[↑ Back to top](#top)
