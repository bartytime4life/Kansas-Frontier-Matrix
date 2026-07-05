<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests/domains/fauna/readme
title: Fauna Domain Test Lane README
type: test-lane-readme
version: v0.1
status: draft
owners:
  - <PLACEHOLDER — Fauna steward>
  - <PLACEHOLDER — Test steward>
  - <PLACEHOLDER — Policy steward>
  - <PLACEHOLDER — Release steward>
  - <PLACEHOLDER — UI steward>
created: 2026-07-05
updated: 2026-07-05
policy_label: public
implementation_status: scaffold
verification_status: current-session path verified; executable tests, fixtures, validators, schemas, policies, releases, and CI not verified
related:
  - tests/README.md
  - docs/doctrine/directory-rules.md
  - docs/domains/fauna/README.md
  - docs/domains/fauna/SENSITIVITY.md
  - docs/domains/fauna/MAP_UI_CONTRACTS.md
  - docs/domains/fauna/SOURCE_REGISTRY.md
  - docs/domains/fauna/RELEASE_INDEX.md
  - fixtures/domains/fauna/
  - contracts/domains/fauna/
  - schemas/contracts/v1/domains/fauna/
  - policy/domains/fauna/
  - policy/sensitivity/fauna/
  - data/registry/sources/fauna/
  - data/receipts/
  - data/proofs/fauna/
  - release/
tags:
  - kfm
  - tests
  - fauna
  - domain-tests
  - evidence
  - policy
  - sensitivity
  - release
  - map-ui
  - finite-outcome
  - no-network
  - fail-closed
] -->

<a id="top"></a>

# Fauna Domain Tests

> Parent test-lane contract for proving Fauna behavior across source governance, evidence, policy, release, map UI, tiles, visual state, accessibility, and lifecycle boundaries.

![status: draft](https://img.shields.io/badge/status-draft-orange)
![lane: tests%2Fdomains%2Ffauna-informational](https://img.shields.io/badge/lane-tests%2Fdomains%2Ffauna-informational)
![authority: tests--only](https://img.shields.io/badge/authority-tests--only-lightgrey)
![posture: fail--closed](https://img.shields.io/badge/posture-fail--closed-blue)
![implementation: scaffold](https://img.shields.io/badge/implementation-scaffold-yellow)

**Status:** `draft`  
**Authority:** parent domain test README; not a source registry, schema, contract, policy bundle, fixture inventory, receipt, proof, release decision, UI implementation, or public artifact  
**Owning root:** `tests/`  
**Domain segment:** `domains/fauna/`  
**Default posture:** public-safe fixtures; no-network by default; finite outcomes; fail closed for unresolved source, evidence, rights, sensitivity, review, release, or correction state  
**Last reviewed:** 2026-07-05

---

## 1. Purpose

This directory is the parent test lane for the **Fauna** domain.

It exists to prove that Fauna behavior is governed before any animal-related source, record, claim, map feature, layer, tile, drawer payload, Focus answer, visual state, or release surface can become public-facing KFM output. Tests are proof and regression guards; they do not create truth, source authority, policy, release state, receipts, proofs, or publication artifacts.

A mature Fauna test lane should prove:

1. Source descriptors, source roles, rights, sensitivity, freshness, and activation state are checked before use.
2. Evidence-dependent claims resolve to released evidence support or produce a finite negative outcome.
3. Policy-withheld Fauna material fails closed unless governed public-safe transformation and review requirements are satisfied.
4. Public map/UI surfaces use governed APIs and released manifests only.
5. Tiles, screenshots, popups, badges, drawers, generated text, and map styles remain downstream carriers, never truth authority.
6. Release, correction, rollback, receipts, proofs, and audit boundaries are visible and not collapsed into a file move.
7. Default tests are deterministic, public-safe, and no-network.

---

## 2. Directory fit and authority

Directory Rules place domain-specific tests under the `tests/` responsibility root with the domain as a segment:

```text
tests/domains/fauna/
```

| Placement question | Answer |
|---|---|
| Primary responsibility | Prove Fauna domain behavior. |
| Owning root | `tests/` |
| Domain segment | `domains/fauna/` |
| Parent lane | `tests/domains/fauna/` |
| Fixture home | `fixtures/domains/fauna/` unless tiny test-local examples are documented. |
| Contract home | `contracts/domains/fauna/` when present. |
| Schema home | `schemas/contracts/v1/domains/fauna/` when present. |
| Policy homes | `policy/domains/fauna/` and `policy/sensitivity/fauna/`. |
| Source registry home | `data/registry/sources/fauna/`. |
| Receipt/proof homes | `data/receipts/` and `data/proofs/`. |
| Release home | `release/`. |
| Public artifact home | `data/published/layers/fauna/` when present. |

> [!WARNING]
> This directory must not become a second schema home, contract home, policy home, source registry, fixture inventory, receipt home, proof home, release home, published artifact home, UI implementation home, or source-data home.

[↑ Back to top](#top)

---

## 3. Status and evidence boundary

| Item | Status |
|---|---|
| Target README path existed as a greenfield stub before this update | CONFIRMED in this session. |
| Directory Rules basis for `tests/domains/<domain>/` | CONFIRMED from current repo doctrine. |
| `tests/README.md` allows policy, evidence-resolution, lifecycle, receipt/proof, release-manifest, governed API, UI trust-state, e2e, runtime-proof, and domain-specific tests | CONFIRMED from current repo docs. |
| `tests/README.md` excludes sensitive material, live network calls, duplicate authority homes, trust-bearing receipts/proofs, and release decisions from `tests/` | CONFIRMED from current repo docs. |
| Fauna domain docs define Fauna as sensitivity-aware and deny-by-default for policy-withheld material | CONFIRMED from current repo docs. |
| Actual executable tests under this directory | UNKNOWN in this README. |
| Actual fixture inventory | NEEDS VERIFICATION. |
| Actual validators, schemas, policy bundles, release manifests, receipts, proofs, UI routes, and CI jobs | NEEDS VERIFICATION. |

This README defines the parent test-lane contract. It does not claim that all child lanes, executable tests, fixtures, validators, schemas, policies, releases, or workflows already exist.

---

## 4. Parent domain rule

**Rule:** A Fauna output may pass test gates only when the relevant source, evidence, policy, sensitivity, rights, review, receipt, release, correction, rollback, UI, and public-safe fixture conditions are valid for the tested scope.

Tests should fail or require a finite negative outcome when:

- source identity, role, rights, activation, or freshness is unresolved;
- evidence references are missing, unresolved, stale, conflicted, unreleased, or withdrawn;
- sensitive-lane rules are bypassed or enforced only through presentation;
- public clients read lifecycle/internal stores or direct source data;
- UI surfaces treat feature properties, popups, screenshots, tiles, badges, or generated summaries as claims;
- release, review, correction, and rollback state are merged or hidden;
- receipts/proofs/release decisions are stored under `tests/`;
- reusable fixtures are duplicated under `tests/` without a declared boundary; or
- default tests require live network calls, credentials, or production services.

Tests may allow public-facing behavior only when the fixture is public-safe, policy permits it, evidence support resolves, required governance references are present, release state is current, and the test remains inside its validation scope.

---

## 5. Child lanes

| Child lane | Responsibility | Status boundary |
|---|---|---|
| `a11y/` | Prove accessibility of trust states and negative outcomes. | README work may exist; executable tests NEEDS VERIFICATION. |
| `focus/` | Prove citation, denial, bounded context, and abstention behavior. | README work may exist; executable tests NEEDS VERIFICATION. |
| `layers/` | Prove public layer manifest, release, trust-state, and clickability gates. | README work may exist; executable tests NEEDS VERIFICATION. |
| `policy/` | Prove policy gates, including redaction and fail-closed behavior. | README work may exist; executable tests NEEDS VERIFICATION. |
| `release/` | Prove ReleaseManifest, correction, rollback, and invalidation behavior. | README work may exist; executable tests NEEDS VERIFICATION. |
| `sources/` | Prove source descriptor, source role, rights, freshness, and watcher boundaries. | README work may exist; executable tests NEEDS VERIFICATION. |
| `tiles/` | Prove tile manifests, field allowlists, integrity, and release gates. | README work may exist; executable tests NEEDS VERIFICATION. |
| `ui/` | Prove map UI, drawer, Focus-adjacent UI, trust state, and governed API boundaries. | README work may exist; executable tests NEEDS VERIFICATION. |
| `visual/` | Prove visual regression, trust-state visibility, and screenshot boundary. | README work may exist; executable tests NEEDS VERIFICATION. |
| `schema/` | Prove Fauna schema conformance where domain schemas exist. | PROPOSED / NEEDS VERIFICATION unless implemented. |
| `contracts/` | Prove object meaning matches Fauna contracts. | PROPOSED / NEEDS VERIFICATION unless implemented. |
| `pipeline/` | Prove lifecycle and promotion gates for Fauna processing. | PROPOSED / NEEDS VERIFICATION unless implemented. |

Additional child lanes may be added when they have a clear test responsibility and do not duplicate another authority root.

---

## 6. Parent proof matrix

| Test concern | Required proof | Expected behavior |
|---|---|---|
| Source governance | Source identity, role, rights, activation, and freshness are checked. | Pass or finite negative outcome. |
| Evidence resolution | Evidence support resolves or answer abstains. | `ANSWER` or `ABSTAIN`. |
| Sensitivity gate | Policy-withheld material fails closed unless governed public-safe conditions are met. | `DENY`, `ABSTAIN`, or non-render. |
| Policy gate | Rights, sensitivity, review, source, and release policy are enforced. | Fail closed if unresolved. |
| Lifecycle boundary | Pre-public lifecycle material does not surface as public truth. | Boundary assertion. |
| Release gate | Public output has release, correction path, and rollback target where required. | Release assertion. |
| Receipt/proof boundary | Tests assert references but do not store trust-bearing records. | Placement assertion. |
| UI boundary | Public clients use governed APIs and released manifests only. | API/UI boundary assertion. |
| Tile/layer boundary | Tiles/layers are downstream public-safe carriers, not evidence or release authority. | Manifest/allowlist assertion. |
| Focus boundary | Focus answers cite released evidence or deny/abstain. | `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`. |
| A11y/trust state | Trust state is text-labelled, keyboard reachable, and not color-only. | Accessibility assertion. |
| No-network default | Tests use deterministic local public-safe fixtures only. | Harness guard. |

---

## 7. What belongs here

This directory may contain README material, child-lane READMEs, and tests that call canonical schema, contract, validator, source, policy, evidence, release, UI, tile, layer, and fixture code from owning roots.

It may include negative tests for missing source descriptors, unresolved rights, unresolved sensitivity, missing evidence, stale source, missing review, missing receipt, missing release state, direct-store access, presentation-only sensitivity handling, and hidden negative outcomes.

It may include positive tests for public-safe fixtures with required governance references and tiny test-local examples when they are documented and not reusable fixture inventory.

## 8. What does not belong here

This directory must not contain production code, source records, sensitive source detail, reusable fixture inventories, schemas, contracts, policy definitions, source descriptors, receipts, proofs, release decisions, published artifacts, UI implementation, generated model output, credentials, production screenshots, production tiles, or default tests that require live network access.

---

## 9. Fixture posture

Reusable Fauna fixtures should normally live under:

```text
fixtures/domains/fauna/
```

Fixture records should be deterministic, public-safe, no-network, and clearly test-only. They should model governance states rather than include production source material or trust-bearing decisions.

Expected fixture families include valid public-safe source, missing source role, unresolved rights, unresolved sensitivity, sensitive denial, public-safe derivative, missing evidence, stale evidence, conflicted support, missing receipt, missing release, withdrawn release, rollback target, public layer, public tile, drawer answer, drawer denial, Focus abstention, trust-badge state, and visual-regression state.

---

## 10. Suggested local commands

> [!NOTE]
> Command names, validators, test runners, markers, workflow names, and exact package commands are **NEEDS VERIFICATION** until checked against actual repository configuration.

```bash
pytest tests/domains/fauna
pytest tests/domains/fauna/policy
pytest tests/domains/fauna/release
pytest tests/domains/fauna/ui
pytest tests/domains/fauna/tiles
npx playwright test --grep fauna
python tools/validate_all.py
```

---

## 11. Open questions

| Question | Status | Notes |
|---|---|---|
| Which Fauna child lanes already contain executable tests? | NEEDS VERIFICATION | Must inspect `tests/domains/fauna/`. |
| Which fixture families already exist? | NEEDS VERIFICATION | Must inspect `fixtures/domains/fauna/`. |
| Which validators are canonical for Fauna domain tests? | NEEDS VERIFICATION | Must inspect validator/tool roots. |
| Which schema and contract files are canonical for Fauna tests? | NEEDS VERIFICATION | Must inspect `schemas/` and `contracts/`. |
| Which policy bundles govern Fauna sensitivity and admissibility? | NEEDS VERIFICATION | Must inspect policy roots. |
| Which release manifests, rollback cards, and public artifacts exist? | NEEDS VERIFICATION | Must inspect release/publication roots. |
| Which CI job runs the Fauna domain test lane? | NEEDS VERIFICATION | Must inspect `.github/workflows/`. |
| Which cross-domain test cases belong outside this domain segment? | OPEN | Shared inference-risk tests may require a cross-domain test root. |

---

## 12. Definition of done

This parent lane is mature when:

- [ ] Fauna domain tests run locally.
- [ ] Active child lanes have executable proof where implementation exists.
- [ ] Source, evidence, sensitivity, policy, release, UI, Focus, tile, visual, accessibility, and lifecycle boundary cases are tested.
- [ ] Positive public-safe fixtures prove allowed behavior without becoming source admission or release approval.
- [ ] Negative fixtures prove fail-closed behavior for unresolved or unsafe states.
- [ ] Tests call canonical code and validators rather than redefining behavior locally.
- [ ] Public-safe fixtures are used and verified no-network.
- [ ] CI exposes the Fauna test proof clearly enough for reviewers.
- [ ] Open questions are resolved or tracked in a verification backlog.

---

## 13. Changelog

| Date | Version | Change |
|---|---:|---|
| 2026-07-05 | v0.1 | Replaced greenfield stub with governed parent README for the Fauna domain test lane. |

---

## 14. Last reviewed

**2026-07-05** — Replaced greenfield stub. Current evidence confirms the tests root, Directory Rules domain-segment rule, root test allowance for policy/evidence/lifecycle/receipt/release/API/UI/e2e/runtime/domain tests, and Fauna sensitivity-aware domain doctrine; executable tests, fixtures, validators, schemas, policies, releases, and CI enforcement remain **NEEDS VERIFICATION**.

[↑ Back to top](#top)
