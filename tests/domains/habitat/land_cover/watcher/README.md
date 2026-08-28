<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-habitat-land-cover-watcher-readme
title: Habitat Land-Cover Watcher Test README
type: test-readme
version: v0.1
status: draft; placeholder-expanded; test-lane; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Habitat domain steward
  - OWNER_TBD — Land-cover steward
  - OWNER_TBD — Watcher steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — QA steward
created: NEEDS VERIFICATION — blank placeholder existed before v0.1 expansion
updated: 2026-07-05
policy_label: public-doc; tests; habitat; land-cover; watcher; no-network; source-drift-aware; checkpoint-aware; materiality-aware; review-gated; watcher-not-publisher
tags: [kfm, tests, habitat, land_cover, watcher, source-drift, checkpoint, materiality-threshold, proposed-work, no-op, source-role, source-activation, review-gate, release-blocker, CorrectionNotice, RollbackCard, ABSTAIN, DENY]
related:
  - ../../../../README.md
  - ../../../../../fixtures/domains/habitat/land_cover/watcher/README.md
  - ../../../../../docs/domains/habitat/sublanes/land_cover.md
  - ../../../../../contracts/domains/habitat/land_cover/observation.md
  - ../../../../../contracts/domains/habitat/land_cover/change_summary.md
  - ../../../../../contracts/domains/habitat/land_cover/model_run_receipt.md
  - ../../../../../contracts/domains/habitat/land_cover/uncertainty.md
  - ../../../../../pipelines/domains/habitat/land_cover/
  - ../../../../../pipeline_specs/habitat/land_cover/
  - ../../../../../data/registry/sources/habitat/
  - ../../../../../policy/domains/habitat/land_cover/
  - ../../../../../policy/sensitivity/habitat/
  - ../../../../../release/manifests/habitat/
notes:
  - "This file replaces a blank placeholder at tests/domains/habitat/land_cover/watcher/README.md."
  - "This is a test-lane README only. It does not define Habitat land-cover doctrine, watcher implementation, source descriptors, fixtures, lifecycle records, evidence bundles, policy rules, release decisions, pipeline code, public API material, public map material, public tiles, or published artifacts."
  - "The tested invariant is that land-cover watchers observe source state, compare checkpoints, evaluate materiality, emit no-op or proposed-work records, and preserve review gates without becoming source activation, source authority, evidence closure, policy approval, release authority, public UI material, or publication."
  - "Default posture is deterministic and no-network. Live source checks, real source exports, lifecycle data, public tiles, and sensitive joined records do not belong in this lane."
  - "Rollback target for this replacement is previous blank blob SHA 8b137891791fe96927ad78e64b0aad7bded08bdc."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Habitat land-cover watcher tests

> Deterministic, no-network test documentation for proving that Habitat land-cover watchers observe and record source drift without publishing, activating sources, bypassing review, feeding public UI directly, or becoming source truth.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Domain: habitat" src="https://img.shields.io/badge/domain-habitat-2e7d32">
  <img alt="Sublane: land cover" src="https://img.shields.io/badge/sublane-land__cover-6a5acd">
  <img alt="Lane: watcher" src="https://img.shields.io/badge/lane-watcher-blue">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Boundary: watcher not publisher" src="https://img.shields.io/badge/boundary-watcher__not__publisher-success">
</p>

**Path:** `tests/domains/habitat/land_cover/watcher/README.md`  
**Status:** draft / placeholder-expanded / PROPOSED until paired test files are verified  
**Owning root:** `tests/`  
**Domain segment:** `habitat`  
**Test lane:** `land_cover/watcher`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED target was a blank placeholder before this expansion · CONFIRMED `tests/` is the canonical root for enforceability proof · CONFIRMED the paired fixture README defines watcher fixtures as toy source-head checks, source-drift detections, class-histogram changes, materiality thresholds, checkpoint records, proposed-work records, and no-op outcomes · CONFIRMED land-cover doctrine states materiality thresholds and the proposed-work/checkpoint watcher pattern as confirmed corpus ideas while implementation paths remain proposed · NEEDS VERIFICATION for executable test modules, fixture payload inventory, watcher implementation, source activation records, validator behavior, policy runtime, review queue behavior, CI coverage, and release-gate integration.

**Quick jumps:** [Purpose](#purpose) · [Placement basis](#placement-basis) · [Invariant under test](#invariant-under-test) · [Expected test scope](#expected-test-scope) · [Fixture posture](#fixture-posture) · [Assertions](#assertions) · [Finite outcomes](#finite-outcomes) · [Forbidden shortcuts](#forbidden-shortcuts) · [Suggested test layout](#suggested-test-layout) · [Run posture](#run-posture) · [Evidence ledger](#evidence-ledger) · [Validation checklist](#validation-checklist) · [Rollback](#rollback)

---

## Purpose

`tests/domains/habitat/land_cover/watcher/` is the intended home for tests that prove Habitat land-cover watcher behavior stays inside its governed role.

A watcher may detect that a source head, version, digest, source vintage, class histogram, materiality threshold, checkpoint, or freshness state changed. It may create a bounded proposed-work record for review. It must not silently create source authority, lifecycle data, observations, change summaries, model receipts, uncertainty surfaces, layer manifests, release artifacts, or public UI material.

A passing test here should **not** mean that a real source is activated, a real source changed, a proposed work item is reviewed, or a public derivative is released. It should mean only that watcher guardrails behaved as expected against bounded fixtures.

---

## Placement basis

`tests/` is the canonical root for enforceability proof. Habitat appears as a lane segment inside the tests root, not as a repo-root domain folder.

| Responsibility | Correct home | This lane's relationship |
|---|---|---|
| Habitat land-cover watcher tests | `tests/domains/habitat/land_cover/watcher/` | This directory. |
| Synthetic watcher fixtures | `fixtures/domains/habitat/land_cover/watcher/` | Preferred toy inputs and expected outcomes. |
| Watcher doctrine | `docs/domains/habitat/sublanes/land_cover.md` | Referenced doctrine; tests do not redefine it. |
| Source registry | `data/registry/sources/habitat/` | Source activation, source role, rights, cadence, and caveats. |
| Observation/change/model/uncertainty consumers | `contracts/domains/habitat/land_cover/` | Watcher proposals may point toward these lanes; they do not create their records. |
| Pipeline logic and specs | `pipelines/domains/habitat/land_cover/`, `pipeline_specs/habitat/land_cover/` | Systems under test where accepted; not duplicated here. |
| Policy and sensitivity homes | `policy/domains/habitat/land_cover/`, `policy/sensitivity/habitat/` | Referenced by tests, not bypassed here. |
| Release decisions | `release/` and `release/manifests/habitat/` | Publication, correction, and rollback authority; tests and watchers cannot replace it. |

---

## Invariant under test

> **Watcher observes and records; watcher does not publish.** A Habitat land-cover watcher may compare source state against a checkpoint, evaluate materiality, and emit no-op, hold, deny, or proposed-work outcomes. It must preserve source activation, source role, rights, evidence, validation, policy, review, correction, and rollback boundaries without creating public truth or release authority.

For this test lane, the invariant decomposes into ten checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Source activation | Watcher does not act as authority when source activation, role, rights, or cadence is missing. | hold / validation failure. |
| Source-head comparison | Source head, version, digest, timestamp, or checkpoint comparison is explicit and deterministic. | validation failure / `ERROR`. |
| Checkpoint discipline | Checkpoint writes are explicit, reversible, and not publication. | validation failure. |
| Materiality threshold | Threshold profile and below/above threshold decision are explicit. | review required / validation failure. |
| Proposed work | Proposed-work records are review inputs, not lifecycle data, release artifacts, or public outputs. | `DENY` / validation failure. |
| No-op path | Unchanged or below-threshold inputs produce no-op or review-optional outcome without side effects. | validation failure. |
| Evidence and validation | Watcher output links to evidence/validation context where consequential, but does not close proof. | `ABSTAIN`. |
| Policy and sensitivity | Policy and sensitivity gates are preserved before downstream work or exposure. | `DENY` / hold. |
| Review and release | Review and release remain separate governed transitions. | promotion-blocking failure. |
| No authority upgrade | Watcher output cannot become observation truth, model proof, layer truth, public UI truth, or AI truth. | test failure. |

---

## Expected test scope

Tests in this lane should be small, synthetic, and deterministic. They may validate:

- source unchanged with matching checkpoint -> no-op;
- source changed and threshold exceeded -> proposed-work record for review;
- source changed but below threshold -> no-op or review-optional finite outcome;
- missing source activation, source role, rights posture, or cadence -> hold or validation failure;
- stale source or failed validation -> hold/review-required outcome;
- checkpoint creation/update rules without publication side effects;
- failure when watcher output is treated as source truth, lifecycle data, EvidenceBundle proof, release approval, public UI material, or published artifact;
- denial when public UI, map, API, Evidence Drawer, Focus Mode, or AI tries to consume proposed work directly.

Live source checks, live source downloads, real source exports, public tile generation, and provider-backed model calls are out of scope for the default suite.

---

## Fixture posture

Use `fixtures/domains/habitat/land_cover/watcher/` when possible.

Fixture requirements:

- synthetic and public-safe;
- deterministic and no-network;
- compact enough for review in a PR;
- explicit expected outcome;
- explicit source ID, source head, source role, source activation state, rights state, watcher cadence, checkpoint state, threshold profile, evidence state, validation state, policy state, review state, release-blocker state, correction state, and rollback state where material;
- no real source exports, lifecycle data, real public tiles, sensitive joined records, or published artifacts.

Preferred fixture families:

| Fixture kind | Preferred lane | Example expected outcome |
|---|---|---|
| Source unchanged | `fixtures/domains/habitat/land_cover/watcher/` | no-op output. |
| Source changed above threshold | same | proposed-work output / review required. |
| Source changed below threshold | same or invalid lane | no-op or review-optional output. |
| Missing source activation | same or invalid lane | hold output. |
| Missing source role or rights posture | same or invalid lane | hold / validation failure. |
| Watcher output treated as publication | same or invalid lane | validation failure. |
| Public UI consumes proposed work | same or invalid lane | `DENY` / validation failure. |

---

## Assertions

A useful watcher test should make the watcher-not-publisher boundary obvious.

### Positive path

- source activation and source role are explicit before watcher activity;
- source-head and checkpoint comparison is deterministic;
- materiality threshold and outcome are visible;
- no-op outcomes have no publication side effects;
- proposed-work records are review inputs only;
- evidence, validation, policy, review, correction, and rollback references are linkable where material;
- downstream observation, change-summary, model-run, uncertainty, layer-manifest, API, renderer, Evidence Drawer, Focus Mode, or AI examples remain carriers or consumers, not watcher authority.

### Negative path

- missing activation, role, rights posture, or cadence fails closed;
- watcher cannot activate a source;
- watcher cannot write lifecycle, processed, catalog, published, proof, release, public API, public map, or public tile authority;
- proposed-work cannot bypass review;
- watcher output cannot replace EvidenceBundle proof, PolicyDecision, ReviewRecord, ReleaseManifest, catalog closure, or source activation;
- public UI, map, popup, tile, graph edge, Focus Mode answer, or AI text cannot consume proposed work as truth.

---

## Finite outcomes

This lane should prefer explicit finite outcomes over loose pass/fail text.

| Condition | Expected outcome |
|---|---|
| Source unchanged with matching checkpoint | no-op. |
| Source changed and materiality threshold exceeded | proposed-work / review required. |
| Source changed but below threshold | no-op or review-optional finite outcome. |
| Source activation, source role, or rights posture missing | hold / validation failure. |
| Watcher validation fails | hold / validation failure. |
| Watcher output treated as publication, proof, policy, review, or release approval | validation failure. |
| Public UI requests proposed work directly | `DENY` / validation failure. |
| Policy engine unavailable | `ERROR` or `ABSTAIN`, never public exposure. |

---

## Forbidden shortcuts

Do not use this test lane to:

- fetch live upstream source systems;
- store real source exports, real lifecycle data, real source records, or real public tiles;
- store proof packs, release manifests, or generated public layers;
- store sensitive joined records or exact protected-resource geometry;
- redefine watcher doctrine, source descriptors, fixtures, policy rules, receipts, proofs, release decisions, renderer code, or production code;
- bypass source activation, source role, rights, materiality, evidence, validation, policy, review, correction, or rollback checks with a fixture flag;
- infer release state from file existence, checkpoint existence, proposed-work existence, layer name, map rendering, tile availability, or AI wording;
- publish, promote, or release anything.

Any test that needs live source checking belongs in a gated integration tier with source admission, lifecycle state, policy, receipts, release controls, and rollback targets.

---

## Suggested test layout

The exact Python module names remain NEEDS VERIFICATION until the runner and existing test conventions are inspected. A minimal future layout could be:

```text
tests/domains/habitat/land_cover/watcher/
├── README.md
├── test_source_activation_required.py
├── test_source_head_checkpoint.py
├── test_materiality_threshold.py
├── test_no_op_behavior.py
├── test_proposed_work_review_gate.py
├── test_watcher_not_publication.py
└── test_public_ui_denies_proposed_work.py
```

---

## Run posture

```bash
pytest tests/domains/habitat/land_cover/watcher
```

Status of the command above: **PROPOSED / NEEDS VERIFICATION**. It assumes `pytest` is the accepted test runner and that executable test modules exist. This README does not claim the command currently passes.

---

## Evidence ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | `tests/domains/habitat/land_cover/watcher/README.md` existed as a blank placeholder before this replacement. | Did not define the lane. |
| `tests/README.md` | CONFIRMED | `tests/` is enforceability proof; domain-specific tests belong under `tests/domains/<domain>/`; failures should block promotion. | Does not prove habitat/land_cover/watcher modules or pass rate. |
| `fixtures/domains/habitat/land_cover/watcher/README.md` | CONFIRMED | Fixture lane defines toy source-head checks, source-drift detections, histogram changes, materiality thresholds, checkpoint records, proposed-work records, and no-op outcomes; fixtures are not lifecycle data, EvidenceBundles, policy decisions, review approvals, release state, public map material, public tiles, Habitat truth, or published artifacts. | Does not prove payload inventory or consumer tests. |
| `docs/domains/habitat/sublanes/land_cover.md` | CONFIRMED doctrine / PROPOSED implementation | Land-cover doctrine says materiality thresholds and proposed-work/checkpoint watcher pattern are confirmed corpus ideas, while implementation paths remain proposed. | Concrete watcher implementation, validators, source activation, and CI behavior remain NEEDS VERIFICATION. |

---

## Validation checklist

Before treating this README as implemented behavior, verify:

- [ ] Executable test modules exist under this lane.
- [ ] Test runner and import paths match the repo's accepted convention.
- [ ] Synthetic fixtures exist for source unchanged, source changed above threshold, source changed below threshold, missing source activation, missing source role, failed validation, proposed work, and public UI denial.
- [ ] SourceDescriptor/source-role behavior is available to tests or safely stubbed.
- [ ] Watcher checkpoint and materiality-threshold behavior are accepted before enforcing them.
- [ ] EvidenceRef / EvidenceBundle behavior is available to tests or safely stubbed.
- [ ] PolicyDecision, ReviewRecord, ReleaseManifest, CorrectionNotice, and RollbackCard expectations are defined before enforcing them.
- [ ] CI runs the no-network Habitat land-cover watcher suite.
- [ ] Failures block public carrier promotion or release candidate approval.

---

## Rollback

Rollback is required if this lane becomes a live source-fetcher, source export store, lifecycle data store, fixture root, source registry, policy authority, proof store, release-decision root, public map/API/tile surface, AI surface, renderer implementation, pipeline implementation, or publication shortcut.

Rollback target for this replacement: previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`.

<p align="right"><a href="#top">Back to top</a></p>
