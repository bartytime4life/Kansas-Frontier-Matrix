<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests/domains/flora/no-network/readme
title: Flora No-Network Test Lane README
type: test-lane-readme
version: v0.1
status: draft
owners:
  - <PLACEHOLDER — Flora steward>
  - <PLACEHOLDER — Source steward>
  - <PLACEHOLDER — Test steward>
created: 2026-07-05
updated: 2026-07-05
policy_label: public
implementation_status: scaffold
verification_status: current-session path verified; executable tests, fixtures, network guards, replay packs, validators, and CI not verified
related:
  - tests/README.md
  - tests/domains/flora/README.md
  - tests/domains/flora/citation/README.md
  - tests/domains/flora/evidence_closure/README.md
  - docs/doctrine/directory-rules.md
  - docs/domains/flora/README.md
  - fixtures/domains/flora/
  - data/registry/sources/flora/
  - contracts/domains/flora/
  - schemas/contracts/v1/domains/flora/
  - policy/domains/flora/
  - policy/sensitivity/flora/
  - data/receipts/
  - data/proofs/flora/
  - release/
tags:
  - kfm
  - tests
  - flora
  - no-network
  - deterministic-fixtures
  - replay
  - source-boundary
  - evidence
  - policy
  - fail-closed
] -->

<a id="top"></a>

# Flora No-Network Tests

> Test-lane contract for proving the default Flora test suite is deterministic, fixture-backed, public-safe, and unable to depend on live source systems, credentials, or runtime network access.

![status: draft](https://img.shields.io/badge/status-draft-orange)
![lane: tests%2Fdomains%2Fflora%2Fno__network-informational](https://img.shields.io/badge/lane-tests%2Fdomains%2Fflora%2Fno__network-informational)
![authority: tests--only](https://img.shields.io/badge/authority-tests--only-lightgrey)
![posture: no--network-blue](https://img.shields.io/badge/posture-no--network-blue)
![implementation: scaffold](https://img.shields.io/badge/implementation-scaffold-yellow)

**Status:** `draft`  
**Authority:** no-network test-lane README; not a source connector, source registry, fixture inventory, credential store, evidence store, receipt, proof, release decision, or public artifact  
**Owning root:** `tests/`  
**Domain segment:** `domains/flora/`  
**Lane:** `no_network/`  
**Default posture:** deterministic public-safe fixtures; no live network by default; finite outcomes; fail closed when a test needs unmocked source access  
**Last reviewed:** 2026-07-05

---

## 1. Purpose

This directory is the Flora domain test lane for **no-network behavior**.

It exists to prove that the default Flora test suite does not depend on live source systems, live credentials, mutable remote APIs, or unrecorded external state. Flora tests may verify source-admission, evidence, geometry, citation, policy, release, and UI behavior only through deterministic fixtures, replay packets, mocks, or adapter seams that preserve the source/evidence boundary.

A mature lane should prove:

1. Default Flora tests cannot open live network connections.
2. Source connectors are mocked, replayed, or isolated behind explicit adapter seams.
3. Fixtures are deterministic, public-safe, and clearly test-only.
4. Replay records do not become evidence, source descriptors, receipts, proofs, or release decisions.
5. Tests fail closed when required fixture data is missing.
6. Network-enabled integration tests, if ever added, are explicitly opt-in and excluded from the default suite.
7. CI enforces the default no-network posture.

---

## 2. Directory fit and authority

Directory Rules place domain-specific tests under the `tests/` responsibility root with the domain as a segment:

```text
tests/domains/flora/no_network/
```

| Placement question | Answer |
|---|---|
| Primary responsibility | Prove Flora no-network test behavior. |
| Owning root | `tests/` |
| Domain segment | `domains/flora/` |
| Test lane | `no_network/` |
| Fixture home | `fixtures/domains/flora/` unless tiny test-local examples are documented. |
| Source registry home | `data/registry/sources/flora/` when present. |
| Contract/schema homes | `contracts/domains/flora/` and `schemas/contracts/v1/domains/flora/` when present. |
| Policy homes | `policy/domains/flora/` and `policy/sensitivity/flora/`. |
| Receipt/proof homes | `data/receipts/` and `data/proofs/flora/`. |
| Release home | `release/`. |

> [!WARNING]
> This directory must not become a second source registry, connector implementation home, fixture inventory, credential store, evidence store, schema home, policy home, receipt home, proof home, release home, or source-data home.

[↑ Back to top](#top)

---

## 3. Status and evidence boundary

| Item | Status |
|---|---|
| Target README path exists in repo | CONFIRMED in this session before this README update. |
| Directory Rules basis for `tests/domains/<domain>/` | CONFIRMED from current repo doctrine. |
| `tests/README.md` allows validator, policy, evidence-resolution, lifecycle, receipt/proof, release-manifest, governed API, UI trust-state, runtime-proof, and domain-specific tests | CONFIRMED from current repo docs. |
| `tests/README.md` excludes live network calls and live credentials in the default suite | CONFIRMED from current repo docs. |
| `tests/README.md` excludes duplicate authority homes and trust-bearing records from `tests/` | CONFIRMED from current repo docs. |
| Flora docs anchor Flora to the trust spine and public-safe botanical outputs | CONFIRMED from current repo docs. |
| Actual executable no-network tests in this directory | UNKNOWN in this README. |
| Actual network guard, fixture inventory, replay packs, connector mocks, markers, and CI jobs | NEEDS VERIFICATION. |

This README defines the test-lane contract. It does not claim that no-network guards, mocks, replay packs, fixtures, validators, markers, or CI checks already exist.

---

## 4. No-network rule

**Rule:** A default Flora test may pass only when it executes without live network access, live source credentials, or mutable external service state.

Tests should fail or require a finite negative outcome when:

- a test attempts DNS, HTTP, database, object-store, package-download, or external API access without an explicit opt-in marker;
- a source connector is invoked directly instead of through a mocked or replayed adapter seam;
- a fixture depends on current remote state;
- credentials, tokens, cookies, private URLs, or live source secrets are required;
- missing replay data silently falls back to a live call;
- replay data is treated as an evidence bundle, source descriptor, receipt, proof, or release decision;
- generated output fills gaps caused by missing fixture data; or
- network-enabled checks run in the default suite.

Tests may allow connector-facing behavior only when the source interaction is mocked, replayed, deterministic, public-safe, and clearly marked as test-only.

---

## 5. Proof matrix

| Test concern | Required proof | Expected behavior |
|---|---|---|
| Network blocked | Default suite denies outbound network calls. | Harness assertion. |
| Connector seam | Source connector calls are mocked or replayed. | Adapter assertion. |
| No credentials | Tests run without live secrets or private tokens. | Environment assertion. |
| Replay determinism | Replay inputs are pinned and local. | Fixture assertion. |
| Missing fixture | Missing replay/fixture data does not trigger live fallback. | `ERROR`, `ABSTAIN`, or validation failure. |
| Evidence boundary | Replay data is not treated as EvidenceBundle truth. | Boundary assertion. |
| Source boundary | Replay data is not a source descriptor or admission decision. | Boundary assertion. |
| Policy boundary | No-network fixture still runs rights/sensitivity/review gates. | Policy assertion. |
| CI default | CI default job excludes network-enabled checks. | Workflow assertion. |
| Opt-in integration | Any live integration test is explicit, isolated, and excluded by default. | Marker assertion. |

---

## 6. What belongs here

This directory may contain:

- README and lane contract material for Flora no-network tests.
- Tests that assert network guards, mocked adapters, replay isolation, missing-fixture failure, and credential-free execution.
- Negative tests proving live fallback is blocked.
- Positive tests proving public-safe fixture/replay behavior.
- Tiny test-local examples when documented and not reusable fixture inventory.

## 7. What does not belong here

This directory must not contain connector implementation, source descriptors, production source data, reusable fixture inventories, credentials, private URLs, evidence bundles, receipts, proofs, release decisions, schemas, contracts, policy definitions, published artifacts, generated model output, or default tests that require live network access.

---

## 8. Fixture and replay posture

Reusable Flora fixtures should normally live under:

```text
fixtures/domains/flora/
```

Fixture and replay records should be deterministic, public-safe, no-network, and clearly test-only. They should model source/evidence/policy states rather than become source descriptors, evidence bundles, receipts, proofs, or release decisions.

Expected fixture families include valid local replay, missing replay, connector blocked, credential missing, live fallback blocked, stale replay, policy denial replay, evidence-boundary replay, source-boundary replay, and opt-in integration marker case.

---

## 9. Suggested local commands

> [!NOTE]
> Command names, markers, network guard names, validator names, workflow names, and exact package commands are **NEEDS VERIFICATION** until checked against actual repository configuration.

```bash
pytest tests/domains/flora/no_network
pytest tests/domains/flora
python tools/validate_all.py
```

---

## 10. Open questions

| Question | Status | Notes |
|---|---|---|
| Which test harness blocks network calls? | NEEDS VERIFICATION | Must inspect test configuration. |
| Which marker names distinguish default no-network and opt-in integration tests? | NEEDS VERIFICATION | Must inspect pytest/playwright/workflow configuration. |
| Which Flora connectors need replay seams? | NEEDS VERIFICATION | Must inspect source/connector roots. |
| Which fixture or replay families already exist? | NEEDS VERIFICATION | Must inspect `fixtures/domains/flora/`. |
| Which CI job enforces no-network by default? | NEEDS VERIFICATION | Must inspect `.github/workflows/`. |
| Should shared no-network tests live here or under a cross-domain no-network test root? | OPEN | This lane should own Flora-specific expectations only. |

---

## 11. Definition of done

This lane is mature when:

- [ ] Flora no-network tests run locally.
- [ ] Network blocked, connector seam, no credentials, replay determinism, missing fixture, live fallback blocked, stale replay, policy-denial replay, evidence-boundary replay, and source-boundary replay cases are tested.
- [ ] Positive public-safe fixtures prove deterministic behavior without becoming source or evidence authority.
- [ ] Negative fixtures prove fail-closed behavior for missing replay or accidental live access.
- [ ] Tests call canonical adapters/validators rather than redefining behavior locally.
- [ ] Public-safe fixtures are used and verified no-network.
- [ ] CI exposes the Flora no-network proof clearly enough for reviewers.
- [ ] Open questions are resolved or tracked in a verification backlog.

---

## 12. Changelog

| Date | Version | Change |
|---|---:|---|
| 2026-07-05 | v0.1 | Initial governed README for the Flora no-network test lane. |

---

## 13. Last reviewed

**2026-07-05** — Initial README scaffold. Target path was present but empty before update. Current evidence confirms the tests root, Directory Rules domain-segment rule, root test allowance for validator/policy/evidence/lifecycle/receipt/release/API/UI/runtime/domain tests, and default no-network doctrine; executable tests, fixtures, network guards, replay packs, connector mocks, markers, validators, and CI enforcement remain **NEEDS VERIFICATION**.

[↑ Back to top](#top)
