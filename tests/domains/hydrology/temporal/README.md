<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-hydrology-temporal-readme
title: Hydrology Temporal Test README
type: test-readme
version: v0.1
status: draft; placeholder-expanded; temporal-test-lane; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Hydrology domain steward
  - OWNER_TBD — Temporal steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — QA steward
created: NEEDS VERIFICATION — blank placeholder existed before v0.1 expansion
updated: 2026-07-05
policy_label: public-doc; tests; hydrology; temporal; no-network; source-vintage-aware; cadence-aware; stale-state-aware; evidence-bound; release-gated; rollback-aware
tags: [kfm, tests, hydrology, temporal, source-vintage, observed-time, valid-time, retrieval-time, release-time, correction-time, stale-state, cadence, EvidenceBundle, PolicyDecision, ReleaseManifest, CorrectionNotice, RollbackCard, ABSTAIN, DENY, ERROR]
related:
  - ../../../README.md
  - ../README.md
  - ../sources/README.md
  - ../identity/README.md
  - ../policy/README.md
  - ../schema/README.md
  - ../no_network/README.md
  - ../../../../docs/domains/hydrology/DATA_LIFECYCLE.md
  - ../../../../docs/domains/hydrology/PUBLICATION_POSTURE.md
  - ../../../../docs/domains/hydrology/SOURCE_REGISTRY.md
  - ../../../../docs/domains/hydrology/SOURCE_ROLE_MATRIX.md
  - ../../../../docs/domains/hydrology/IDENTITY_MODEL.md
  - ../../../../contracts/domains/hydrology/
  - ../../../../schemas/contracts/v1/domains/hydrology/
  - ../../../../fixtures/domains/hydrology/temporal/
  - ../../../../data/registry/sources/hydrology/
  - ../../../../policy/domains/hydrology/
  - ../../../../release/manifests/hydrology/
notes:
  - "This file replaces a blank placeholder at tests/domains/hydrology/temporal/README.md."
  - "This is a test-lane README only. It does not define Hydrology doctrine, temporal doctrine, contracts, schemas, fixtures, source descriptors, lifecycle records, EvidenceBundles, policy rules, release decisions, pipeline code, public API material, public map material, public tiles, or published artifacts."
  - "The tested invariant is that Hydrology temporal checks preserve separate time semantics: source vintage, observed time, valid time, retrieval time, release time, correction time, stale state, cadence, evidence relationship, policy posture, release relationship, correction, and rollback remain visible before public carriers."
  - "Default posture is deterministic and no-network. Live source checks, upstream fetches, real source exports, lifecycle data, and public tiles do not belong in this lane."
  - "Rollback target for this replacement is previous blank blob SHA 8b137891791fe96927ad78e64b0aad7bded08bdc."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hydrology temporal tests

> Deterministic, no-network test documentation for proving that Hydrology time fields, source vintages, cadence posture, stale-state markers, correction lineage, and rollback targets remain distinct and auditable.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Domain: hydrology" src="https://img.shields.io/badge/domain-hydrology-2aa1c6">
  <img alt="Lane: temporal" src="https://img.shields.io/badge/lane-temporal-blue">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Boundary: time fields distinct" src="https://img.shields.io/badge/boundary-time__fields__distinct-success">
</p>

**Path:** `tests/domains/hydrology/temporal/README.md`  
**Status:** draft / placeholder-expanded / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Domain segment:** `hydrology`  
**Test lane:** `temporal`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED target was a blank placeholder before this expansion · CONFIRMED `tests/` is the canonical root for enforceability proof · CONFIRMED Hydrology lifecycle doctrine carries source role, rights, sensitivity, citation, time, cadence, source vintage, evidence closure, release state, correction, and rollback posture · CONFIRMED Hydrology publication posture separates stale from wrong and requires visible markers and traceable lifecycles · NEEDS VERIFICATION for executable temporal tests, fixture payload inventory, schema enforcement, validator behavior, policy runtime, release integration, CI coverage, and pass rates.

---

## Purpose

`tests/domains/hydrology/temporal/` is the intended home for Hydrology temporal and freshness tests.

This lane should prove that Hydrology records and release-like carriers keep time semantics separate. Source vintage, observed time, valid time, retrieval time, release time, correction time, stale-state time, and rollback target time must not collapse into one generic timestamp.

A passing test here should **not** mean that a source is current, a refresh ran, a public layer is safe, or a release is approved. It should mean only that temporal guardrails behaved as expected against bounded fixtures and local files.

---

## Placement basis

`tests/` is the canonical root for enforceability proof. Hydrology is a domain segment inside that root. `temporal/` is a test lane, not a connector, lifecycle store, source registry, policy home, release home, proof store, public API surface, or public map surface.

| Responsibility | Correct home | This lane's relationship |
|---|---|---|
| Hydrology temporal tests | `tests/domains/hydrology/temporal/` | This directory. |
| Hydrology lifecycle doctrine | `docs/domains/hydrology/DATA_LIFECYCLE.md` | Temporal and lifecycle doctrine under test. |
| Publication/stale posture | `docs/domains/hydrology/PUBLICATION_POSTURE.md` | Stale, correction, and rollback posture under test. |
| Source descriptors | `data/registry/sources/hydrology/` | Source cadence and vintage context; not duplicated here. |
| Machine schemas | `schemas/contracts/v1/domains/hydrology/` | Shape checks where accepted. |
| Synthetic fixtures | `fixtures/domains/hydrology/temporal/` | Preferred toy inputs and expected outcomes if populated. |
| Policy homes | `policy/domains/hydrology/` | Referenced by tests, not bypassed here. |
| Release decisions | `release/` and `release/manifests/hydrology/` | Publication, correction, and rollback authority; tests cannot replace it. |

---

## Invariant under test

> **Hydrology time is multi-kind and release-significant.** Temporal fields must preserve what time means. Observation, source vintage, retrieval, validity, release, stale-state, correction, and rollback time cannot be substituted for one another.

Core checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Time-kind separation | Distinct time fields remain distinct where material. | validation failure / `ABSTAIN`. |
| Source vintage | Source-vintage posture is explicit where material. | validation failure. |
| Observation time | Observed readings carry observed/provider time and do not become release time. | validation failure. |
| Retrieval time | Retrieval timestamp is fetch context only, not claim truth. | validation failure / `ABSTAIN`. |
| Stale state | Cadence-aged fixtures produce stale/hold/abstain posture, not silent currency. | `ABSTAIN` / `DENY` / validation failure. |
| Correction time | Correction lineage records detected error or new evidence without silent edit. | validation failure. |
| Release boundary | Release time does not prove source freshness, evidence closure, policy approval, or source truth. | promotion-blocking failure. |
| No network | Default temporal tests use local files only. | validation failure / `ERROR`. |

---

## Expected scope

Tests in this lane may validate:

- distinct source-vintage, observed, valid, retrieval, release, correction, stale-state, and rollback fields;
- stable identity when release timestamp changes but source/vintage/content do not;
- stale-state when cadence tolerance is exceeded in a synthetic fixture;
- correction lineage when new evidence or error state supersedes a prior carrier;
- rejection of fixtures that present retrieval freshness as claim truth;
- no network behavior in the default suite.

Live checks, upstream endpoint calls, real source exports, production credentials, public tile generation, and real hydrology payloads are out of scope for the default suite.

---

## Fixture posture

Use synthetic, public-safe fixtures only.

Fixture requirements:

- deterministic and no-network;
- compact enough for review in a PR;
- explicit expected outcome;
- explicit source, source role, cadence, source vintage, observed/valid/retrieval/release/correction/stale time, evidence posture, policy state, release relationship, correction, and rollback posture where material;
- no real source exports, lifecycle data, public tiles, credentials, or published artifacts.

---

## Finite outcomes

| Condition | Expected outcome |
|---|---|
| Fixture preserves required time kinds and cadence posture | accepted temporal support only. |
| Observation time is replaced by release time | validation failure. |
| Source vintage is missing where material | `ABSTAIN` / validation failure. |
| Retrieval freshness is treated as claim truth | validation failure / `ABSTAIN`. |
| Cadence tolerance is exceeded | stale / `ABSTAIN` / `HOLD`. |
| Correction changes public meaning without correction lineage | validation failure. |
| Release timestamp is treated as source freshness proof | promotion-blocking failure. |
| Network check runs in default lane | validation failure / `ERROR`. |

---

## Suggested layout

```text
tests/domains/hydrology/temporal/
├── README.md
├── test_time_kinds_are_distinct.py
├── test_source_vintage_required.py
├── test_observed_time_not_release_time.py
├── test_retrieval_time_not_claim_truth.py
├── test_cadence_stale_state.py
├── test_correction_time_and_supersession.py
└── test_release_correction_rollback_required.py
```

---

## Run posture

```bash
pytest tests/domains/hydrology/temporal
```

Status of the command above: **PROPOSED / NEEDS VERIFICATION**. It assumes `pytest` is the accepted test runner and that executable test modules exist. This README does not claim the command currently passes.

---

## Evidence ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | `tests/domains/hydrology/temporal/README.md` existed as a blank placeholder before this replacement. | Did not define the lane. |
| `tests/README.md` | CONFIRMED | `tests/` is enforceability proof and failure should block promotion where trust-spine checks fail. | Does not prove this lane's modules or pass rate. |
| `tests/domains/hydrology/README.md` | CONFIRMED | Hydrology test parent currently exists as a greenfield stub. | Parent lane still needs expansion. |
| `docs/domains/hydrology/DATA_LIFECYCLE.md` | CONFIRMED doctrine / PROPOSED implementation | Defines Hydrology lifecycle, source time/cadence/vintage posture, evidence, release, correction, and rollback expectations. | Concrete validators, fixtures, CI, and pass rates remain NEEDS VERIFICATION. |
| `docs/domains/hydrology/PUBLICATION_POSTURE.md` | CONFIRMED doctrine / PROPOSED realization | Separates stale from wrong and requires visible stale/correction/rollback lifecycle markers. | Documentation evidence only; temporal runtime remains NEEDS VERIFICATION. |
| Repo search | CONFIRMED | Did not find a dedicated Hydrology temporal README before this replacement. | Search is not proof of absence or executable coverage. |

---

## Validation checklist

- [ ] Executable test modules exist under this lane.
- [ ] Test runner and import paths match the repo's accepted convention.
- [ ] Synthetic temporal fixtures exist for valid time-kind separation, missing source vintage, stale cadence, retrieval-time misuse, correction supersession, release timestamp misuse, and missing rollback cases.
- [ ] Temporal field names are accepted by paired contracts/schemas or safely stubbed.
- [ ] SourceDescriptor cadence behavior is available to tests or safely stubbed.
- [ ] EvidenceRef / EvidenceBundle behavior is available to tests or safely stubbed.
- [ ] PolicyDecision, ReleaseManifest, CorrectionNotice, RedactionReceipt, and RollbackCard expectations are defined before enforcing them.
- [ ] CI runs the no-network Hydrology temporal suite or marks it as an expected gap.
- [ ] Failures block public carrier promotion or release candidate approval where material.

---

## Rollback

Rollback is required if this lane becomes a live source-fetcher, lifecycle data store, source registry authority, contract root, schema authority, policy authority, proof store, release-decision root, public map/API/tile surface, AI surface, renderer implementation, pipeline implementation, or publication shortcut.

Rollback target for this replacement: previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`.

<p align="right"><a href="#top">Back to top</a></p>
