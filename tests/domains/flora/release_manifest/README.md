<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests/domains/flora/release-manifest/readme
title: Flora Release Manifest Test Lane README
type: test-lane-readme
version: v0.1
status: draft
owners:
  - <PLACEHOLDER — Flora steward>
  - <PLACEHOLDER — Release steward>
  - <PLACEHOLDER — Evidence steward>
  - <PLACEHOLDER — Test steward>
created: 2026-07-05
updated: 2026-07-05
policy_label: public
implementation_status: scaffold
verification_status: current-session path verified; executable tests, fixtures, release manifests, schemas, validators, rollback cards, correction notices, and CI not verified
related:
  - tests/README.md
  - tests/domains/flora/README.md
  - tests/domains/flora/evidence_closure/README.md
  - tests/domains/flora/policy/README.md
  - tests/domains/flora/policy_deny/README.md
  - docs/doctrine/directory-rules.md
  - docs/domains/flora/README.md
  - docs/domains/flora/PUBLICATION_AND_ROLLBACK.md
  - fixtures/domains/flora/
  - schemas/contracts/v1/domains/flora/
  - contracts/domains/flora/
  - policy/domains/flora/
  - policy/sensitivity/flora/
  - data/receipts/
  - data/proofs/flora/
  - release/
tags:
  - kfm
  - tests
  - flora
  - release-manifest
  - publication-gate
  - rollback
  - correction
  - evidence
  - lifecycle
  - no-network
  - fail-closed
] -->

<a id="top"></a>

# Flora Release Manifest Tests

> Test-lane contract for proving Flora `ReleaseManifest` records are complete, resolvable, policy-aware, rollback-capable, and separate from both evidence closure and publication authority.

![status: draft](https://img.shields.io/badge/status-draft-orange)
![lane: tests%2Fdomains%2Fflora%2Frelease__manifest-informational](https://img.shields.io/badge/lane-tests%2Fdomains%2Fflora%2Frelease__manifest-informational)
![authority: tests--only](https://img.shields.io/badge/authority-tests--only-lightgrey)
![posture: fail--closed](https://img.shields.io/badge/posture-fail--closed-blue)
![implementation: scaffold](https://img.shields.io/badge/implementation-scaffold-yellow)

**Status:** `draft`  
**Authority:** release-manifest test-lane README; not a release decision, release manifest store, rollback card, correction notice, evidence store, fixture inventory, receipt, proof, schema, policy bundle, or public artifact  
**Owning root:** `tests/`  
**Domain segment:** `domains/flora/`  
**Lane:** `release_manifest/`  
**Default posture:** public-safe fixtures; no-network by default; finite outcomes; fail closed when release identity, contents, digests, evidence references, policy decision, correction path, or rollback target is missing or unresolved  
**Last reviewed:** 2026-07-05

---

## 1. Purpose

This directory is the Flora domain test lane for **ReleaseManifest behavior**.

It exists to prove that Flora releases are not treated as public, current, or safe unless their release manifest is complete and every required dependency resolves. These tests verify release-manifest shape, dependency closure, digest coverage, evidence binding, policy-decision linkage, correction path, rollback target, and lifecycle boundary behavior. They do not issue release decisions or store production release artifacts.

A mature lane should prove:

1. A Flora release candidate cannot become public without a release manifest.
2. The manifest pins release identity, contents, digests, evidence references, release time, correction path, and rollback target where required.
3. Required dependencies resolve; references alone are not enough.
4. Policy, rights, sensitivity, review, and evidence gates have evaluated before public exposure.
5. Release approval is distinct from evidence closure, policy allow, UI rendering, or file placement.
6. Correction and rollback state is auditable and not silently edited away.
7. Default tests use deterministic public-safe fixtures only.

---

## 2. Directory fit and authority

Directory Rules place domain-specific tests under the `tests/` responsibility root with the domain as a segment:

```text
tests/domains/flora/release_manifest/
```

| Placement question | Answer |
|---|---|
| Primary responsibility | Prove Flora release-manifest behavior. |
| Owning root | `tests/` |
| Domain segment | `domains/flora/` |
| Test lane | `release_manifest/` |
| Release home | `release/`. |
| Fixture home | `fixtures/domains/flora/` unless tiny test-local examples are documented. |
| Schema/contract homes | `schemas/contracts/v1/domains/flora/` and `contracts/domains/flora/` when present. |
| Policy homes | `policy/domains/flora/` and `policy/sensitivity/flora/`. |
| Receipt/proof homes | `data/receipts/` and `data/proofs/flora/`. |
| Public artifact home | `data/published/layers/flora/` when present. |

> [!WARNING]
> This directory must not become a second release home, release-manifest registry, rollback-card store, correction-notice store, evidence store, fixture inventory, receipt home, proof home, schema home, policy home, public artifact home, or source-data home.

[↑ Back to top](#top)

---

## 3. Status and evidence boundary

| Item | Status |
|---|---|
| Target README path exists in repo | CONFIRMED in this session before this README update. |
| Directory Rules basis for `tests/domains/<domain>/` | CONFIRMED from current repo doctrine. |
| `tests/README.md` allows release-manifest tests and receipt/proof tests | CONFIRMED from current repo docs. |
| `tests/README.md` allows evidence-resolution, lifecycle, policy, governed API, UI trust-state, runtime-proof, and domain-specific tests | CONFIRMED from current repo docs. |
| `tests/README.md` excludes trust-bearing receipts, proofs, release decisions, live network calls, and duplicate authority homes from `tests/` | CONFIRMED from current repo docs. |
| Flora docs say the release gate is the only route from CATALOG to PUBLISHED | CONFIRMED from current repo docs. |
| Flora publication docs require `ReleaseManifest`, rollback target, correction path, and review record where required | CONFIRMED from current repo docs. |
| Flora publication docs say required artifacts must resolve their dependencies and policy must have evaluated | CONFIRMED from current repo docs. |
| Actual executable tests in this directory | UNKNOWN in this README. |
| Actual release manifest schemas, fixtures, validators, rollback cards, correction notices, release roots, and CI jobs | NEEDS VERIFICATION. |

This README defines the test-lane contract. It does not claim that release-manifest tests, fixtures, schemas, validators, release manifests, rollback cards, correction notices, or CI checks already exist.

---

## 4. Release-manifest rule

**Rule:** A Flora release-manifest fixture may pass only when the manifest is complete for the tested lifecycle state, all required dependencies resolve, policy/review/evidence gates have valid recorded outcomes, and rollback/correction targets are present where required.

Tests should fail or require a finite negative outcome when:

- a release candidate lacks a manifest;
- `release_id`, `contents[]`, `digests`, `evidence_refs[]`, `time`, correction path, or rollback target is missing where required;
- a listed artifact lacks digest coverage;
- an evidence reference, source reference, review reference, receipt/proof reference, correction target, or rollback target does not resolve;
- policy has not evaluated or recorded a decision;
- review state is required but absent;
- a release manifest is treated as evidence closure or policy approval;
- copying a file to a public path is treated as publication;
- UI or API surfaces read unreleased material directly; or
- release decisions, rollback cards, correction notices, receipts, or proofs are stored under `tests/`.

Tests may allow a manifest only when the fixture is public-safe, all required references resolve, release boundary semantics are preserved, and the test remains inside its validation scope.

---

## 5. Proof matrix

| Test concern | Required proof | Expected behavior |
|---|---|---|
| Manifest required | Release candidate has a manifest before public exposure. | Validation assertion. |
| Identity and time | `release_id` and release time are present. | Schema/contract assertion. |
| Contents listed | Every included dataset/bundle/layer/tile artifact is enumerated. | Contents assertion. |
| Digest coverage | Included artifacts have content digests where required. | Integrity assertion. |
| Evidence references | Evidence refs are present and resolve where required. | Evidence assertion or `ABSTAIN`. |
| Policy decision | Policy gate evaluated and recorded an outcome. | Policy assertion. |
| Review state | Required review record is present and resolves. | Review assertion. |
| Correction path | Correction path exists where required. | Correction assertion. |
| Rollback target | Rollback target exists and resolves where required. | Rollback assertion. |
| Lifecycle boundary | Release is a governed transition, not a file move. | Boundary assertion. |
| No-network default | Tests use deterministic local public-safe fixtures only. | Harness guard. |

---

## 6. What belongs here

This directory may contain:

- README and lane contract material for Flora release-manifest tests.
- Tests that call canonical release, schema, contract, evidence, policy, review, receipt/proof, rollback, correction, UI/API, and validator code from owning roots.
- Negative tests for missing manifest, missing digest, unresolved evidence reference, unresolved rollback target, missing correction path, missing policy decision, missing review state, file-move-as-publication, and UI/API direct-read bypass.
- Positive tests for public-safe release-manifest fixtures with complete dependency closure.
- Tiny test-local examples when documented and not reusable fixture inventory.

## 7. What does not belong here

This directory must not contain production release decisions, release manifests, rollback cards, correction notices, trust-bearing receipts, proofs, production evidence, source records, reusable fixture inventories, schemas, contracts, policy definitions, published artifacts, credentials, generated model output, or default tests that require live network access.

---

## 8. Fixture posture

Reusable Flora fixtures should normally live under:

```text
fixtures/domains/flora/
```

Fixture records should be deterministic, public-safe, no-network, and clearly test-only. They should model release-manifest states rather than become release decisions, rollback cards, correction notices, evidence bundles, receipts, or proofs.

Expected fixture families include valid release manifest, missing manifest, missing contents, missing digest, unresolved evidence reference, missing policy decision, missing review state, missing correction path, unresolved rollback target, stale/superseded release, file-move-as-publication anti-pattern, and UI/API direct-read bypass.

---

## 9. Suggested local commands

> [!NOTE]
> Command names, validators, test runners, markers, workflow names, and exact package commands are **NEEDS VERIFICATION** until checked against actual repository configuration.

```bash
pytest tests/domains/flora/release_manifest
pytest tests/domains/flora/evidence_closure
pytest tests/domains/flora/policy
pytest tests/domains/flora
python tools/validate_all.py
```

---

## 10. Open questions

| Question | Status | Notes |
|---|---|---|
| Which ReleaseManifest schema is canonical for Flora? | NEEDS VERIFICATION | Must inspect schema and release roots. |
| What is the relationship between Flora `ReleaseManifest` and `MapReleaseManifest`? | NEEDS VERIFICATION | Flora docs mark this relationship for verification. |
| Which validator owns release-manifest completeness checks? | NEEDS VERIFICATION | Must inspect validator/tool roots. |
| Which rollback and correction object paths are canonical? | NEEDS VERIFICATION | Must inspect release and rollback roots. |
| Which fixture families already exist? | NEEDS VERIFICATION | Must inspect `fixtures/domains/flora/`. |
| Which CI job runs this lane? | NEEDS VERIFICATION | Must inspect `.github/workflows/`. |
| Should shared release-manifest tests live here or under a cross-domain release test root? | OPEN | This lane should own Flora-specific expectations only. |

---

## 11. Definition of done

This lane is mature when:

- [ ] Flora release-manifest tests run locally.
- [ ] Valid manifest, missing manifest, missing contents, missing digest, unresolved evidence reference, missing policy decision, missing review state, missing correction path, unresolved rollback target, stale/superseded release, file-move-as-publication, and UI/API direct-read bypass cases are tested.
- [ ] Positive public-safe fixtures prove allowed manifest behavior without becoming release approval.
- [ ] Negative fixtures prove fail-closed behavior for incomplete publication gates.
- [ ] Tests call canonical release/evidence/policy/review/rollback/correction validators rather than redefining behavior locally.
- [ ] Public-safe fixtures are used and verified no-network.
- [ ] CI exposes the Flora release-manifest proof clearly enough for reviewers.
- [ ] Open questions are resolved or tracked in a verification backlog.

---

## 12. Changelog

| Date | Version | Change |
|---|---:|---|
| 2026-07-05 | v0.1 | Initial governed README for the Flora release-manifest test lane. |

---

## 13. Last reviewed

**2026-07-05** — Initial README scaffold. Target path was present but empty before update. Current evidence confirms the tests root, Directory Rules domain-segment rule, root test allowance for release-manifest/evidence/lifecycle/policy/API/UI/runtime/domain tests, and Flora publication-gate doctrine; executable tests, fixtures, schemas, validators, release manifests, rollback cards, correction notices, and CI enforcement remain **NEEDS VERIFICATION**.

[↑ Back to top](#top)
