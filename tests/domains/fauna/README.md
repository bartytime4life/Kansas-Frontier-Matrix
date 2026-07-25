<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests/domains/fauna/readme
title: Fauna Domain Test Lane README
type: test-lane-readme
version: v0.2
status: draft
owners:
  - <PLACEHOLDER — Fauna steward>
  - <PLACEHOLDER — Test steward>
  - <PLACEHOLDER — Policy steward>
  - <PLACEHOLDER — Release steward>
  - <PLACEHOLDER — UI steward>
created: 2026-07-05
updated: 2026-07-25
policy_label: public
implementation_status: bounded-public-safe-fixture-validation-slice
verification_status: five deterministic standard-library tests over five fixtures verified locally; production schemas, source admission, policy runtime, proof, release, promotion, and publication remain unverified and held
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
![implementation: bounded slice](https://img.shields.io/badge/implementation-bounded__slice-yellow)

**Status:** `draft`  
**Authority:** parent domain test README; not a source registry, schema, contract, policy bundle, fixture inventory, receipt, proof, release decision, UI implementation, or public artifact  
**Owning root:** `tests/`  
**Domain segment:** `domains/fauna/`  
**Default posture:** public-safe fixtures; no-network by default; finite outcomes; fail closed for unresolved source, evidence, rights, sensitivity, review, release, or correction state  
**Last reviewed:** 2026-07-25

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
| Accepted executable test slice | CONFIRMED: `test_fauna_smoke.py` contains five standard-library tests for the synthetic public-safe fixture profile. |
| Accepted fixture inventory | CONFIRMED only for one positive and four fail-closed JSON fixtures named in §3.1; all other fixture maturity remains unchanged. |
| Accepted validator | CONFIRMED: `tools/validators/domains/fauna/validate_public_safe_fixture.py`; standard-library, deterministic, and fixture-only. |
| Current occurrence schemas | CONFIRMED as permissive `PROPOSED` scaffolds; this slice does not promote or treat them as production validation authority. |
| Current source descriptors | CONFIRMED as `PROPOSED` templates with unresolved `TBD` role, authority, rights, sensitivity, cadence, and access fields; this slice accepts only `fixture:` refs and synthetic source role. |
| Current policy runtime, release manifests, receipts, proofs, UI routes, and public artifacts | NEEDS VERIFICATION and outside this slice. |

This README defines the parent test-lane contract. Acceptance of the bounded slice below does not claim that other child lanes, tests, fixtures, validators, schemas, policies, releases, or workflows are implemented.

### 3.1 Accepted bounded validation slice

| Surface | Accepted scope |
|---|---|
| Validator | Synthetic fixture safety only; it does not validate `OccurrencePublic`, source admission, policy execution, evidence closure, geoprivacy transforms, release, or publication. |
| Positive fixture | `fixtures/domains/fauna/valid/non_sensitive_occurrence.json` passes only because it is synthetic, fixture-only, location-withheld, no-network, and explicitly not released or promotion-eligible. |
| Negative fixtures | Missing source reference; unresolved taxonomy; unresolved evidence, rights, policy, geoprivacy, review, correction, and rollback; and unresolved sensitivity plus precision-shaped keys return stable fail-closed findings. |
| Network posture | The validator uses only the Python standard library; every accepted test blocks socket and URL-opening calls. |
| CI | Only `validate-fauna` in `.github/workflows/domain-fauna.yml` runs this exact test module. Proof and release-dry-run jobs remain held. |

No pass from this slice is a PolicyDecision, ReviewRecord, ValidationReport, EvidenceBundle, RedactionReceipt, ReleaseManifest, correction approval, rollback proof, promotion decision, publication approval, or claim about real fauna.

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
The accepted bounded command is:

```bash
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python -m unittest discover \
  --start-directory tests/domains/fauna \
  --pattern 'test_fauna_smoke.py' \
  --verbose
```

Other Fauna test, policy, release, UI, tile, Playwright, or validator commands remain NEEDS VERIFICATION until separately accepted.

---

## 11. Open questions

| Question | Status | Notes |
|---|---|---|
| Which Fauna child lanes already contain executable tests? | PARTIALLY RESOLVED | Only the bounded root `test_fauna_smoke.py` slice is accepted; child-lane executable maturity remains NEEDS VERIFICATION. |
| Which fixture families already exist? | PARTIALLY RESOLVED | One positive and four negative JSON fixtures are accepted for the bounded slice; other fixture families remain NEEDS VERIFICATION. |
| Which validators are canonical for Fauna domain tests? | PARTIALLY RESOLVED | `validate_public_safe_fixture.py` is accepted only for synthetic fixture safety; broader validator ownership remains open. |
| Which schema and contract files are canonical for Fauna tests? | NEEDS VERIFICATION | Must inspect `schemas/` and `contracts/`. |
| Which policy bundles govern Fauna sensitivity and admissibility? | NEEDS VERIFICATION | Must inspect policy roots. |
| Which release manifests, rollback cards, and public artifacts exist? | NEEDS VERIFICATION | Must inspect release/publication roots. |
| Which CI job runs the Fauna domain test lane? | PARTIALLY RESOLVED | `validate-fauna` runs only the accepted bounded module; proof and release-dry-run jobs remain explicit holds. |
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
| 2026-07-25 | v0.2 | Accepted one deterministic, no-network, synthetic fixture-safety slice and kept all production policy, schema, source, proof, release, promotion, and publication claims held. |
| 2026-07-05 | v0.1 | Replaced greenfield stub with governed parent README for the Fauna domain test lane. |

---

## 14. Last reviewed

**2026-07-25** — Verified the Directory Rules lane placement, current fail-closed Fauna policy scaffolds, permissive occurrence-schema scaffolds, placeholder fixture inventory, and unresolved source descriptors. Accepted only the five-test synthetic fixture-safety slice. All production validation, source admission, evidence, policy, review, geoprivacy, proof, release, correction, rollback, promotion, and publication behavior remains outside scope or NEEDS VERIFICATION.

[↑ Back to top](#top)
