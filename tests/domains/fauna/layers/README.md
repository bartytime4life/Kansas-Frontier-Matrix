<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests/domains/fauna/layers/readme
title: Fauna Layers Test Lane README
type: test-lane-readme
version: v0.1
status: draft
owners:
  - <PLACEHOLDER — Fauna steward>
  - <PLACEHOLDER — Map/UI steward>
  - <PLACEHOLDER — Test steward>
created: 2026-07-05
updated: 2026-07-05
policy_label: public
implementation_status: scaffold
verification_status: current-session path verified; executable tests, fixtures, layer manifests, validators, and CI not verified
related:
  - tests/README.md
  - tests/domains/fauna/README.md
  - docs/doctrine/directory-rules.md
  - docs/domains/fauna/MAP_UI_CONTRACTS.md
  - docs/domains/fauna/SENSITIVITY.md
  - policy/domains/fauna/
  - policy/sensitivity/fauna/
  - fixtures/domains/fauna/
  - data/published/layers/fauna/
  - data/receipts/
  - data/proofs/fauna/
  - schemas/contracts/v1/map/
  - schemas/contracts/v1/ui/
  - apps/governed-api/
  - apps/explorer-web/
  - packages/maplibre/
tags:
  - kfm
  - tests
  - fauna
  - layers
  - map-ui
  - layer-manifest
  - release-manifest
  - trust-state
  - evidence
  - no-network
  - fail-closed
] -->

<a id="top"></a>

# Fauna Layer Tests

> Test-lane contract for proving Fauna map layers are governed, public-safe, release-bound, evidence-linked, trust-visible, and downstream of policy and publication controls.

![status: draft](https://img.shields.io/badge/status-draft-orange)
![lane: tests%2Fdomains%2Ffauna%2Flayers-informational](https://img.shields.io/badge/lane-tests%2Fdomains%2Ffauna%2Flayers-informational)
![authority: tests--only](https://img.shields.io/badge/authority-tests--only-lightgrey)
![implementation: scaffold](https://img.shields.io/badge/implementation-scaffold-yellow)

**Status:** `draft`  
**Authority:** test-lane README; not a layer registry, tile artifact, release manifest, style, schema, policy bundle, fixture inventory, receipt, proof, or public artifact  
**Owning root:** `tests/`  
**Domain segment:** `domains/fauna/`  
**Lane:** `layers/`  
**Default posture:** public-safe fixtures; no-network by default; finite outcomes  
**Last reviewed:** 2026-07-05

---

## 1. Purpose

This directory is the Fauna domain test lane for **map layer behavior**.

It exists to prove that Fauna layers do not render or behave as stand-alone truth. A layer is a downstream carrier that should be backed by governed release state, evidence references, source-role separation, policy labels, sensitivity labels, transform references when required, artifact integrity hooks, rollback targets, and finite negative outcomes.

A mature lane should prove:

1. Public Fauna layers load only from governed layer and release manifests.
2. Public layer catalogs exclude unpublished, withdrawn, candidate, or internal records.
3. Layer metadata keeps policy, sensitivity, source role, evidence, time, rights, freshness, artifact, and rollback hooks visible.
4. Feature clicks route to governed claim/evidence resolution rather than treating feature fields as root truth.
5. Trust states such as released, stale, denied, redacted, unverified, degraded, correction-pending, and superseded remain visible and testable.
6. Tests verify layer behavior without creating registries, manifests, tiles, policies, schemas, receipts, proofs, releases, or production UI code.

---

## 2. Directory fit and authority

Directory Rules place domain-specific tests under the `tests/` responsibility root with the domain as a segment:

```text
tests/domains/fauna/layers/
```

| Placement question | Answer |
|---|---|
| Primary responsibility | Prove Fauna layer behavior. |
| Owning root | `tests/` |
| Domain segment | `domains/fauna/` |
| Test lane | `layers/` |
| Public layer artifact home | `data/published/layers/fauna/` when present. |
| Policy homes | `policy/domains/fauna/` and `policy/sensitivity/fauna/`. |
| Schema homes | `schemas/contracts/v1/map/` and `schemas/contracts/v1/ui/` when present. |
| Fixture home | `fixtures/domains/fauna/` unless tiny test-local examples are documented. |
| Receipt/proof homes | `data/receipts/` and `data/proofs/`. |
| Release home | `release/`. |
| UI/API homes | `apps/explorer-web/`, `apps/governed-api/`, and `packages/maplibre/` as applicable. |

> [!WARNING]
> This directory must not become a second layer registry, tile store, release home, policy home, schema home, fixture home, receipt/proof home, or UI implementation home.

[↑ Back to top](#top)

---

## 3. Status and evidence boundary

| Item | Status |
|---|---|
| Target README path exists in repo | CONFIRMED in this session before this README update. |
| Directory Rules basis for `tests/domains/<domain>/` | CONFIRMED from current repo doctrine. |
| `tests/README.md` allows policy, evidence-resolution, release-manifest, governed API envelope, UI trust-state, e2e, runtime-proof, and domain-specific tests | CONFIRMED from current repo docs. |
| Fauna Map UI contract says renderer is downstream of trust | CONFIRMED from current repo docs. |
| Fauna Map UI contract lists Fauna layer manifest obligations | CONFIRMED from current repo docs. |
| Fauna Map UI contract lists trust-visible layer states and badge accessibility obligations | CONFIRMED from current repo docs. |
| Actual executable tests in this directory | UNKNOWN in this README. |
| Actual layer manifests, tile manifests, release manifests, and validators | NEEDS VERIFICATION. |
| Actual fixture inventory | NEEDS VERIFICATION. |
| Actual CI job names / pytest markers | NEEDS VERIFICATION. |

This README defines the test-lane contract. It does not claim that layer manifests, tiles, fixtures, validators, UI routes, or CI jobs already exist.

---

## 4. Layer proof matrix

| Test concern | Required proof | Preferred lane behavior |
|---|---|---|
| Manifest required fields | Layer metadata carries required release, policy, sensitivity, source, evidence, time, rights, freshness, artifact, and rollback hooks. | Schema/validator assertion. |
| Release state | Public catalog only exposes released layer state. | Release-manifest assertion. |
| Policy/sensitivity state | Missing or blocking policy state prevents public rendering. | `DENY`, `ABSTAIN`, or validation failure. |
| Evidence reference | Feature carries an evidence reference hook for governed resolution. | Layer/feature assertion. |
| Click boundary | Click does not treat feature fields as root claims. | UI/API boundary assertion. |
| Source role | Source roles are not collapsed. | Contract/policy assertion. |
| Time facets | Material time fields remain distinct. | Time-aware assertion. |
| Trust-visible states | Released, stale, denied, redacted, degraded, unverified, correction, and superseded states are visible and accessible. | UI trust-state assertion. |
| Integrity hook | Artifact digest or comparable integrity field is present when required. | Manifest/integrity assertion. |
| No-network default | Tests use local public-safe fixtures and no live tiles/source calls. | Harness guard. |

---

## 5. What belongs here

This directory may contain:

- README and lane contract material for Fauna layer tests.
- Tests that validate Fauna LayerManifest or layer descriptor requirements against canonical schemas or validators.
- Tests that verify public layer catalogs exclude non-public entries.
- Tests that verify feature clicks route through governed claim/evidence resolution.
- Tests that verify trust-visible layer states and badges are present, accessible, and not proof substitutes.
- Tests that verify transform references are required for public-safe derivatives when policy requires them.
- Tests that verify time-aware fields remain distinct and stale/superseded states are visible.
- Tests that call canonical schema, release, policy, fixture, UI, and API code from their owning roots.
- Public-safe fixtures for positive and negative layer cases.

## 6. What does not belong here

This directory must not contain production layer manifests, tile artifacts, style manifests, release manifests, public map outputs, production UI/API/renderer code, policy definitions, schema definitions, source registry records, receipts, proofs, release decisions, reusable fixture inventories, or default tests that require live network access.

---

## 7. Fixture posture

Reusable fixtures should normally live under:

```text
fixtures/domains/fauna/
```

Expected fixture families include valid public layer metadata, missing release state, missing policy/sensitivity label, unresolved rights, missing evidence reference, missing transform reference, stale layer, superseded layer, and source-role boundary examples.

Fixture records should be deterministic, public-safe, no-network, and clearly test-only.

---

## 8. Expected outcomes

Fauna layer tests should prefer finite, inspectable outcomes:

```text
ANSWER | ABSTAIN | DENY | ERROR
```

Workflow-facing checks may also use:

```text
ALLOW | RESTRICT | DENY | HOLD | ERROR | NEEDS_REVIEW | QUARANTINE
```

A passing Fauna layer test proves behavior for the checked scenario. It is not evidence creation, policy approval, release approval, proof, tile publication, or public-layer publication.

---

## 9. Suggested local commands

> [!NOTE]
> Command names, layer validator names, UI route names, markers, and CI jobs are **NEEDS VERIFICATION** until checked against actual repository configuration.

```bash
pytest tests/domains/fauna/layers
pytest tests/domains/fauna
npx playwright test --grep fauna
python tools/validate_all.py
```

---

## 10. Open questions

| Question | Status | Notes |
|---|---|---|
| What is the canonical LayerManifest schema path? | NEEDS VERIFICATION | Fauna UI doc marks `schemas/contracts/v1/map/layer_manifest.schema.json` as PROPOSED. |
| Which layer validator command is canonical? | NEEDS VERIFICATION | Must inspect validator roots. |
| Which layer manifest fixture families already exist? | NEEDS VERIFICATION | Must inspect `fixtures/domains/fauna/`. |
| Which public layer artifact paths exist on `main`? | NEEDS VERIFICATION | Must inspect `data/published/layers/fauna/`. |
| Which CI job runs this lane? | NEEDS VERIFICATION | Must inspect `.github/workflows/`. |
| Should shared layer-manifest tests live here or in cross-domain map/UI test roots? | OPEN | This lane should own Fauna-specific expectations only. |

---

## 11. Definition of done

This lane is mature when:

- [ ] Fauna layer tests run locally.
- [ ] Positive public-safe layer fixtures prove allowed layer behavior.
- [ ] Missing release, policy, sensitivity, source-role, evidence, time, rights, freshness, artifact, and rollback paths are tested.
- [ ] Denied, restricted, redacted, stale, degraded, superseded, and invalid layer states are tested.
- [ ] Click-to-evidence behavior is tested where implementation exists.
- [ ] Badge/trust-state visibility and accessibility are tested where UI exists.
- [ ] Public-safe fixtures are used and verified no-network.
- [ ] Tests call canonical validators, policies, schemas, UI/API code, and release tooling rather than redefining behavior locally.
- [ ] CI exposes the Fauna layer proof clearly enough for reviewers.
- [ ] Open questions are resolved or tracked in a verification backlog.

---

## 12. Changelog

| Date | Version | Change |
|---|---:|---|
| 2026-07-05 | v0.1 | Initial governed README for the Fauna layers test lane. |

---

## 13. Last reviewed

**2026-07-05** — Initial README scaffold. Target path was present but empty before update. Current evidence confirms the tests root, Directory Rules domain-segment rule, root test allowance for policy/evidence/release/API/UI/e2e/runtime/domain tests, and Fauna Map UI layer obligations; executable tests, fixtures, layer manifests, tile artifacts, validators, route names, and CI enforcement remain **NEEDS VERIFICATION**.

[↑ Back to top](#top)
