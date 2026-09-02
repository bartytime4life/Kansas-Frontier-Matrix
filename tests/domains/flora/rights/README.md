<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests/domains/flora/rights/readme
title: Flora Rights Test Lane README
type: test-lane-readme
version: v0.1
status: draft
owners:
  - <PLACEHOLDER — Flora steward>
  - <PLACEHOLDER — Rights steward>
  - <PLACEHOLDER — Source steward>
  - <PLACEHOLDER — Policy steward>
  - <PLACEHOLDER — Test steward>
created: 2026-07-05
updated: 2026-07-05
policy_label: public
implementation_status: scaffold
verification_status: current-session path verified; executable tests, fixtures, rights policy, source descriptors, validators, release manifests, and CI not verified
related:
  - tests/README.md
  - tests/domains/flora/README.md
  - tests/domains/flora/policy/README.md
  - tests/domains/flora/policy_deny/README.md
  - tests/domains/flora/citation/README.md
  - tests/domains/flora/evidence_closure/README.md
  - docs/doctrine/directory-rules.md
  - docs/domains/flora/README.md
  - policy/domains/flora/
  - policy/sensitivity/flora/
  - data/registry/sources/flora/
  - fixtures/domains/flora/
  - data/receipts/
  - data/proofs/flora/
  - release/
tags:
  - kfm
  - tests
  - flora
  - rights
  - attribution
  - redistribution
  - source-role
  - policy
  - finite-outcome
  - no-network
  - fail-closed
] -->

<a id="top"></a>

# Flora Rights Tests

> Test-lane contract for proving Flora rights, attribution, redistribution, source-role, and public-use gates fail closed when rights posture is unknown, incompatible, expired, or outside the requested use.

![status: draft](https://img.shields.io/badge/status-draft-orange)
![lane: tests%2Fdomains%2Fflora%2Frights-informational](https://img.shields.io/badge/lane-tests%2Fdomains%2Fflora%2Frights-informational)
![authority: tests--only](https://img.shields.io/badge/authority-tests--only-lightgrey)
![posture: fail--closed](https://img.shields.io/badge/posture-fail--closed-blue)
![implementation: scaffold](https://img.shields.io/badge/implementation-scaffold-yellow)

**Status:** `draft`  
**Authority:** rights test-lane README; not a rights policy, rights registry, source registry, source descriptor, license record, fixture inventory, evidence store, receipt, proof, release decision, or public artifact  
**Owning root:** `tests/`  
**Domain segment:** `domains/flora/`  
**Lane:** `rights/`  
**Default posture:** public-safe fixtures; no-network by default; finite outcomes; fail closed when rights, attribution, redistribution, source role, evidence, review, or release state is unresolved  
**Last reviewed:** 2026-07-05

---

## 1. Purpose

This directory is the Flora domain test lane for **rights and public-use behavior**.

It exists to prove that Flora data, claims, citations, geometry, layers, drawer payloads, Focus answers, exports, and release candidates cannot become public-facing KFM output unless rights and attribution requirements are valid for the requested use. Rights tests verify behavior; they do not define rights policy, admit sources, create source descriptors, issue licenses, or approve releases.

A mature lane should prove:

1. Unknown, missing, incompatible, expired, or out-of-scope rights fail closed.
2. Required attribution and redistribution terms are preserved into public outputs where policy allows use.
3. Source role and rights posture are checked together before a source supports a claim or surface.
4. Rights decisions remain distinct from evidence closure, sensitivity review, and release approval.
5. UI, API, map, export, drawer, and Focus surfaces preserve rights state and finite outcomes.
6. Fixtures and replay records do not become license records, source descriptors, evidence bundles, or release decisions.
7. Default tests use deterministic public-safe fixtures only.

---

## 2. Directory fit and authority

Directory Rules place domain-specific tests under the `tests/` responsibility root with the domain as a segment:

```text
tests/domains/flora/rights/
```

| Placement question | Answer |
|---|---|
| Primary responsibility | Prove Flora rights and public-use behavior. |
| Owning root | `tests/` |
| Domain segment | `domains/flora/` |
| Test lane | `rights/` |
| Parent policy lane | `tests/domains/flora/policy/` |
| Policy homes | `policy/domains/flora/` and `policy/sensitivity/flora/`. |
| Source registry home | `data/registry/sources/flora/` when present. |
| Fixture home | `fixtures/domains/flora/` unless tiny test-local examples are documented. |
| Receipt/proof homes | `data/receipts/` and `data/proofs/flora/`. |
| Release home | `release/`. |

> [!WARNING]
> This directory must not become a second rights policy home, rights registry, source registry, license store, fixture inventory, evidence store, receipt home, proof home, release home, public artifact home, or source-data home.

[↑ Back to top](#top)

---

## 3. Status and evidence boundary

| Item | Status |
|---|---|
| Target README path exists in repo | CONFIRMED in this session before this README update. |
| Directory Rules basis for `tests/domains/<domain>/` | CONFIRMED from current repo doctrine. |
| `tests/README.md` allows policy tests, including unknown-rights negative cases that must fail closed | CONFIRMED from current repo docs. |
| `tests/README.md` allows evidence-resolution, lifecycle, receipt/proof, release-manifest, governed API, UI trust-state, runtime-proof, and domain-specific tests | CONFIRMED from current repo docs. |
| `tests/README.md` excludes live network calls, live source credentials, duplicate authority homes, trust-bearing records, and release decisions from `tests/` | CONFIRMED from current repo docs. |
| Flora docs identify policy roots as `policy/domains/flora/` and `policy/sensitivity/flora/` | CONFIRMED from current repo docs. |
| Flora docs state cite-or-abstain, deterministic identity, governed promotion, auditable provenance, receipts, and rollback targets | CONFIRMED from current repo docs. |
| Actual executable tests in this directory | UNKNOWN in this README. |
| Actual rights policy fields, source descriptors, fixtures, validators, review records, release manifests, and CI jobs | NEEDS VERIFICATION. |

This README defines the test-lane contract. It does not claim that rights tests, fixtures, validators, rights policy fields, source descriptors, review records, release manifests, or CI checks already exist.

---

## 4. Rights rule

**Rule:** A Flora object or output may pass rights tests only when rights, attribution, redistribution, source role, evidence, policy, review, and release conditions are valid for the requested use and surface.

Tests should fail or require a finite negative outcome when:

- rights state is missing, unknown, expired, incompatible, or outside the requested use;
- required attribution text or source credit is missing from a public surface where required;
- redistribution terms do not permit the requested export, tile, API, drawer, Focus, or publication behavior;
- source role is incompatible with rights posture or claim use;
- source descriptor, license reference, or rights field does not resolve where required;
- evidence support exists but rights do not permit public use;
- release state is present but rights were not evaluated;
- rights state is hidden by UI, map, export, drawer, Focus, or generated text;
- cached or derived material bypasses rights re-check; or
- rights policy, source descriptors, license records, receipts, proofs, or release decisions are stored under `tests/`.

Tests may allow public-facing behavior only when the fixture is public-safe, rights permit the requested use, attribution requirements are preserved, evidence and policy requirements resolve where required, and the test remains inside its validation scope.

---

## 5. Proof matrix

| Test concern | Required proof | Expected behavior |
|---|---|---|
| Unknown rights | Rights posture is absent or unresolved. | `DENY`, `ABSTAIN`, or validation failure. |
| Incompatible rights | Rights do not allow requested use. | `DENY` or validation failure. |
| Attribution required | Required credit is preserved in public output. | Attribution assertion. |
| Redistribution limit | Export/tile/API/publication use is blocked when not permitted. | `DENY`, non-export, or validation failure. |
| Source-role fit | Source role and rights posture support the claim/surface. | Source-rights assertion. |
| Rights reference resolution | License/rights/source reference resolves where required. | Resolution assertion. |
| Evidence boundary | Evidence support does not override rights limits. | Boundary assertion. |
| Release boundary | Release state does not replace rights evaluation. | Boundary assertion. |
| UI/API visibility | Rights outcome is surfaced as finite state. | Envelope/UI assertion. |
| No-network default | Tests use deterministic local public-safe fixtures only. | Harness guard. |

---

## 6. What belongs here

This directory may contain:

- README and lane contract material for Flora rights tests.
- Tests that call canonical rights, policy, source, evidence, release, UI/API, and validator code from owning roots.
- Negative tests for unknown rights, incompatible rights, missing attribution, blocked redistribution, unresolved source/rights reference, source-role mismatch, evidence-overrides-rights anti-pattern, release-overrides-rights anti-pattern, hidden rights state, and cached bypass.
- Positive tests for public-safe fixtures where rights permit the requested use and attribution is preserved.
- Tiny test-local examples when documented and not reusable fixture inventory.

## 7. What does not belong here

This directory must not contain rights policy definitions, license records, source descriptors, source records, production evidence, reusable fixture inventories, schemas, contracts, trust-bearing receipts, proofs, release decisions, published artifacts, credentials, generated model output, or default tests that require live network access.

---

## 8. Fixture posture

Reusable Flora fixtures should normally live under:

```text
fixtures/domains/flora/
```

Fixture records should be deterministic, public-safe, no-network, and clearly test-only. They should model rights states rather than become source descriptors, license records, policy definitions, evidence bundles, receipts, proofs, or release decisions.

Expected fixture families include rights allow, unknown rights, incompatible rights, missing attribution, redistribution blocked, unresolved rights reference, source-role mismatch, evidence-overrides-rights anti-pattern, release-overrides-rights anti-pattern, hidden rights state, cached bypass, and valid attribution control.

---

## 9. Suggested local commands

> [!NOTE]
> Command names, validators, test runners, markers, workflow names, and exact package commands are **NEEDS VERIFICATION** until checked against actual repository configuration.

```bash
pytest tests/domains/flora/rights
pytest tests/domains/flora/policy
pytest tests/domains/flora/policy_deny
pytest tests/domains/flora
python tools/validate_all.py
```

---

## 10. Open questions

| Question | Status | Notes |
|---|---|---|
| Which Flora rights fields are canonical? | NEEDS VERIFICATION | Must inspect source descriptor and policy schemas. |
| Which validator owns rights and attribution checks? | NEEDS VERIFICATION | Must inspect validator/tool roots. |
| Which source descriptor paths are canonical for Flora rights tests? | NEEDS VERIFICATION | Must inspect `data/registry/sources/flora/`. |
| Which public surfaces must display attribution? | NEEDS VERIFICATION | Must inspect UI/API/export contracts. |
| Which fixture families already exist? | NEEDS VERIFICATION | Must inspect `fixtures/domains/flora/`. |
| Which CI job runs this lane? | NEEDS VERIFICATION | Must inspect `.github/workflows/`. |
| Should shared rights tests live here or under a cross-domain rights test root? | OPEN | This lane should own Flora-specific expectations only. |

---

## 11. Definition of done

This lane is mature when:

- [ ] Flora rights tests run locally.
- [ ] Rights allow, unknown rights, incompatible rights, missing attribution, redistribution blocked, unresolved rights reference, source-role mismatch, evidence-overrides-rights, release-overrides-rights, hidden rights state, and cached bypass cases are tested.
- [ ] Positive public-safe fixtures prove allowed rights behavior without becoming source admission or release approval.
- [ ] Negative fixtures prove fail-closed behavior for unresolved or incompatible rights states.
- [ ] Tests call canonical rights/policy/source/evidence/release/API validators rather than redefining behavior locally.
- [ ] Public-safe fixtures are used and verified no-network.
- [ ] CI exposes the Flora rights proof clearly enough for reviewers.
- [ ] Open questions are resolved or tracked in a verification backlog.

---

## 12. Changelog

| Date | Version | Change |
|---|---:|---|
| 2026-07-05 | v0.1 | Initial governed README for the Flora rights test lane. |

---

## 13. Last reviewed

**2026-07-05** — Initial README scaffold. Target path was present but empty before update. Current evidence confirms the tests root, Directory Rules domain-segment rule, root test allowance for policy negative cases and domain tests, and Flora policy/public-safe doctrine; executable tests, fixtures, rights policy fields, source descriptors, validators, review records, release manifests, and CI enforcement remain **NEEDS VERIFICATION**.

[↑ Back to top](#top)
