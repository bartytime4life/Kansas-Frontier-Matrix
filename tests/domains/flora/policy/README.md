<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests/domains/flora/policy/readme
title: Flora Policy Test Lane README
type: test-lane-readme
version: v0.1
status: draft
owners:
  - <PLACEHOLDER — Flora steward>
  - <PLACEHOLDER — Policy steward>
  - <PLACEHOLDER — Evidence steward>
  - <PLACEHOLDER — Test steward>
created: 2026-07-05
updated: 2026-07-05
policy_label: public
implementation_status: scaffold
verification_status: current-session path verified; executable tests, fixtures, policy bundles, validators, review records, release manifests, and CI not verified
related:
  - tests/README.md
  - tests/domains/flora/README.md
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
  - policy
  - admissibility
  - rights
  - sensitivity
  - review
  - release
  - finite-outcome
  - no-network
  - fail-closed
] -->

<a id="top"></a>

# Flora Policy Tests

> Parent test-lane contract for proving Flora admissibility gates return finite, reviewable outcomes before public claims, geometry, layers, citations, drawer payloads, Focus answers, or releases are allowed.

![status: draft](https://img.shields.io/badge/status-draft-orange)
![lane: tests%2Fdomains%2Fflora%2Fpolicy-informational](https://img.shields.io/badge/lane-tests%2Fdomains%2Fflora%2Fpolicy-informational)
![authority: tests--only](https://img.shields.io/badge/authority-tests--only-lightgrey)
![posture: fail--closed](https://img.shields.io/badge/posture-fail--closed-blue)
![implementation: scaffold](https://img.shields.io/badge/implementation-scaffold-yellow)

**Status:** `draft`  
**Authority:** policy test-lane README; not a policy bundle, policy registry, review record, source registry, evidence store, fixture inventory, receipt, proof, release decision, or public artifact  
**Owning root:** `tests/`  
**Domain segment:** `domains/flora/`  
**Lane:** `policy/`  
**Default posture:** public-safe fixtures; no-network by default; finite outcomes; fail closed when rights, sensitivity, review, source, evidence, or release state is unresolved  
**Last reviewed:** 2026-07-05

---

## 1. Purpose

This directory is the Flora domain test lane for **policy and admissibility behavior**.

It exists to prove that Flora records, claims, geometry, citations, map layers, drawer payloads, Focus answers, and release candidates are evaluated by the governing policy roots before they can become public-facing KFM output. Tests verify policy behavior; they do not define policy, approve exceptions, create review records, or publish data.

A mature lane should prove:

1. Flora policy decisions return finite outcomes such as `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`.
2. Unknown rights, unresolved sensitivity, missing review, stale source, missing evidence, or absent release state fail closed.
3. Public-safe outputs are allowed only when policy, evidence, source role, review, and release conditions are satisfied for the tested scope.
4. Policy decisions are distinct from evidence closure and release approval.
5. Review, correction, rollback, and receipt/proof references remain auditable where required.
6. UI and map surfaces preserve policy state instead of hiding it.
7. Default tests use deterministic public-safe fixtures only.

---

## 2. Directory fit and authority

Directory Rules place domain-specific tests under the `tests/` responsibility root with the domain as a segment:

```text
tests/domains/flora/policy/
```

| Placement question | Answer |
|---|---|
| Primary responsibility | Prove Flora policy and admissibility behavior. |
| Owning root | `tests/` |
| Domain segment | `domains/flora/` |
| Test lane | `policy/` |
| Policy homes | `policy/domains/flora/` and `policy/sensitivity/flora/`. |
| Fixture home | `fixtures/domains/flora/` unless tiny test-local examples are documented. |
| Source registry home | `data/registry/sources/flora/` when present. |
| Receipt/proof homes | `data/receipts/` and `data/proofs/flora/`. |
| Release home | `release/`. |

> [!WARNING]
> This directory must not become a second policy home, policy registry, review-record home, source registry, evidence store, fixture inventory, receipt home, proof home, release home, public artifact home, or source-data home.

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
| Actual policy bundles, fixtures, validators, review records, release manifests, and CI jobs | NEEDS VERIFICATION. |

This README defines the test-lane contract. It does not claim that policy tests, policy bundles, fixtures, validators, review records, release manifests, or CI checks already exist.

---

## 4. Policy rule

**Rule:** A Flora object or output may pass policy tests only when rights, sensitivity, source role, evidence, review, release, correction, rollback, and public-safe transformation conditions are valid for the tested use.

Tests should fail or require a finite negative outcome when:

- rights or attribution state is unknown;
- sensitivity state is unresolved;
- required review state is missing;
- source role is incompatible with the requested use;
- evidence support is missing, stale, conflicted, or outside claim scope;
- public-safe transformation is required but lacks governance reference;
- release state, correction path, or rollback target is required but missing;
- policy state is hidden by UI, tile, layer, Focus, drawer, or generated text;
- policy approval is treated as evidence closure or release approval; or
- policy definitions, review records, receipts, proofs, or release decisions are stored under `tests/`.

Tests may allow public-facing behavior only when the fixture is public-safe, policy permits it, evidence support resolves where required, review/release state is valid for the tested scope, and the test remains inside its validation boundary.

---

## 5. Proof matrix

| Test concern | Required proof | Expected behavior |
|---|---|---|
| Rights gate | Unknown or incompatible rights fail closed. | `DENY`, `ABSTAIN`, or validation failure. |
| Sensitivity gate | Unresolved policy-controlled detail fails closed. | `DENY`, `ABSTAIN`, or non-render. |
| Review gate | Required review state is present before allow. | Review assertion. |
| Source-role gate | Source role is compatible with use. | Source/policy assertion. |
| Evidence gate | Required evidence support resolves before allow. | Evidence assertion or `ABSTAIN`. |
| Freshness gate | Stale source/evidence is visible and bounded. | Trust-state assertion. |
| Transformation gate | Public-safe derivative carries governance reference where required. | Transform/reference assertion. |
| Release boundary | Policy allow does not replace release approval. | Boundary assertion. |
| UI/API boundary | Runtime returns finite outcome and does not leak internal stores. | Envelope assertion. |
| No-network default | Tests use deterministic local public-safe fixtures only. | Harness guard. |

---

## 6. Child lanes

| Child lane | Responsibility | Status boundary |
|---|---|---|
| `rights/` | Prove rights/attribution/redistribution gates. | PROPOSED / NEEDS VERIFICATION unless implemented. |
| `sensitivity/` | Prove sensitivity and public-safe transformation gates. | PROPOSED / NEEDS VERIFICATION unless implemented. |
| `review/` | Prove required reviewer state gates. | PROPOSED / NEEDS VERIFICATION unless implemented. |
| `freshness/` | Prove stale source/evidence states fail closed or surface trust state. | PROPOSED / NEEDS VERIFICATION unless implemented. |
| `release_boundary/` | Prove policy allow does not become release approval. | PROPOSED / NEEDS VERIFICATION unless implemented. |
| `ui_boundary/` | Prove UI/API surfaces preserve policy outcome. | PROPOSED / NEEDS VERIFICATION unless implemented. |

Additional child lanes may be added when they have a clear policy-test responsibility and do not duplicate another authority root.

---

## 7. What belongs here

This directory may contain:

- README and lane contract material for Flora policy tests.
- Tests that call canonical policy, sensitivity, evidence, source, review, release, UI/API, and validator code from owning roots.
- Negative tests for unknown rights, unresolved sensitivity, missing review, stale source, missing evidence, missing release boundary, and hidden policy state.
- Positive tests for public-safe fixtures where policy allow is justified by governance references.
- Tiny test-local examples when documented and not reusable fixture inventory.

## 8. What does not belong here

This directory must not contain policy definitions, policy registries, review records, source descriptors, source records, production evidence, reusable fixture inventories, schemas, contracts, trust-bearing receipts, proofs, release decisions, published artifacts, credentials, generated model output, or default tests that require live network access.

---

## 9. Fixture posture

Reusable Flora fixtures should normally live under:

```text
fixtures/domains/flora/
```

Fixture records should be deterministic, public-safe, no-network, and clearly test-only. They should model policy states rather than become policy definitions, review records, evidence bundles, receipts, proofs, or release decisions.

Expected fixture families include policy allow, unknown rights, unresolved sensitivity, missing review, stale source, missing evidence, denied source role, missing transformation reference, release-boundary case, UI-hidden-policy anti-pattern, and no-network policy fixture.

---

## 10. Suggested local commands

> [!NOTE]
> Command names, validators, test runners, markers, workflow names, and exact package commands are **NEEDS VERIFICATION** until checked against actual repository configuration.

```bash
pytest tests/domains/flora/policy
pytest tests/domains/flora/evidence_closure
pytest tests/domains/flora
python tools/validate_all.py
```

---

## 11. Open questions

| Question | Status | Notes |
|---|---|---|
| Which Flora policy bundles are canonical? | NEEDS VERIFICATION | Must inspect policy roots. |
| Which sensitivity policy fields are required for default Flora fixtures? | NEEDS VERIFICATION | Must inspect policy/sensitivity roots. |
| Which validator owns Flora policy checks? | NEEDS VERIFICATION | Must inspect validator/tool roots. |
| Which review records are required for each policy outcome? | NEEDS VERIFICATION | Must inspect review/release doctrine and implementation. |
| Which fixture families already exist? | NEEDS VERIFICATION | Must inspect `fixtures/domains/flora/`. |
| Which CI job runs this lane? | NEEDS VERIFICATION | Must inspect `.github/workflows/`. |
| Should shared policy tests live here or under a cross-domain policy test root? | OPEN | This lane should own Flora-specific expectations only. |

---

## 12. Definition of done

This lane is mature when:

- [ ] Flora policy tests run locally.
- [ ] Unknown rights, unresolved sensitivity, missing review, stale source, missing evidence, denied source role, missing transformation reference, release-boundary, and hidden-policy cases are tested.
- [ ] Positive public-safe fixtures prove allowed policy behavior without becoming release approval.
- [ ] Negative fixtures prove fail-closed behavior for unresolved or unsafe states.
- [ ] Tests call canonical policy/evidence/source/review/release validators rather than redefining behavior locally.
- [ ] Public-safe fixtures are used and verified no-network.
- [ ] CI exposes the Flora policy proof clearly enough for reviewers.
- [ ] Open questions are resolved or tracked in a verification backlog.

---

## 13. Changelog

| Date | Version | Change |
|---|---:|---|
| 2026-07-05 | v0.1 | Initial governed README for the Flora policy test lane. |

---

## 14. Last reviewed

**2026-07-05** — Initial README scaffold. Target path was present but empty before update. Current evidence confirms the tests root, Directory Rules domain-segment rule, root test allowance for policy/evidence/lifecycle/receipt/release/API/UI/runtime/domain tests, and Flora policy/public-safe doctrine; executable tests, fixtures, policy bundles, validators, review records, release manifests, and CI enforcement remain **NEEDS VERIFICATION**.

[↑ Back to top](#top)
