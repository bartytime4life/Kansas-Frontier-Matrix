<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-hydrology-redaction-readme
title: Hydrology Redaction Test README
type: test-readme
version: v0.1
status: draft; placeholder-expanded; redaction-test-lane; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Hydrology domain steward
  - OWNER_TBD — Redaction steward
  - OWNER_TBD — Sensitivity steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — QA steward
created: NEEDS VERIFICATION — blank placeholder existed before v0.1 expansion
updated: 2026-07-05
policy_label: public-doc; tests; hydrology; redaction; no-network; deterministic-transform; sensitivity-aware; public-safe-geometry; evidence-bound; release-gated; rollback-aware
tags: [kfm, tests, hydrology, redaction, generalization, RedactionReceipt, SensitivityAssessment, GeneralizationTransform, public-safe-geometry, EvidenceBundle, PolicyDecision, ReleaseManifest, CorrectionNotice, RollbackCard, ABSTAIN, DENY, ERROR]
related:
  - ../../../README.md
  - ../README.md
  - ../policy/README.md
  - ../no_network/README.md
  - ../identity/README.md
  - ../../../../docs/domains/hydrology/PUBLICATION_POSTURE.md
  - ../../../../docs/domains/hydrology/BOUNDARY.md
  - ../../../../docs/domains/hydrology/DATA_LIFECYCLE.md
  - ../../../../docs/doctrine/sensitivity.md
  - ../../../../docs/architecture/sensitivity-tiers.md
  - ../../../../docs/standards/SENSITIVITY_RUBRIC.md
  - ../../../../policy/domains/hydrology/
  - ../../../../policy/sensitivity/hydrology/
  - ../../../../policy/redaction/profiles.yaml
  - ../../../../contracts/policy/policy_decision.md
  - ../../../../contracts/evidence/evidence_bundle.md
  - ../../../../contracts/release/release_manifest.md
  - ../../../../contracts/domains/hydrology/
  - ../../../../schemas/contracts/v1/domains/hydrology/
  - ../../../../schemas/contracts/v1/redaction_receipt.schema.json
  - ../../../../schemas/contracts/v1/sensitivity_assessment.schema.json
  - ../../../../schemas/contracts/v1/generalization_transform.schema.json
  - ../../../../fixtures/domains/hydrology/redaction/
  - ../../../../release/manifests/hydrology/
notes:
  - "This file replaces a blank placeholder at tests/domains/hydrology/redaction/README.md."
  - "This is a test-lane README only. It does not define Hydrology doctrine, sensitivity doctrine, redaction policy, redaction profiles, contracts, schemas, fixtures, source descriptors, lifecycle records, EvidenceBundles, policy rules, release decisions, pipeline code, public API material, public map material, public tiles, or published artifacts."
  - "The tested invariant is that Hydrology redaction checks preserve deterministic, auditable public-safe transforms: sensitivity posture, transform profile, output digest, evidence state, policy state, release relationship, correction, and rollback remain visible before public carriers."
  - "Default posture is deterministic and no-network. Live source checks, real source exports, lifecycle data, public tiles, and restricted records do not belong in this lane."
  - "Rollback target for this replacement is previous blank blob SHA 8b137891791fe96927ad78e64b0aad7bded08bdc."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hydrology redaction tests

> Deterministic, no-network test documentation for proving that Hydrology public-safe transforms are named, reproducible, receipt-backed, policy-gated, correction-aware, and rollback-ready.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Domain: hydrology" src="https://img.shields.io/badge/domain-hydrology-2aa1c6">
  <img alt="Lane: redaction" src="https://img.shields.io/badge/lane-redaction-blue">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Boundary: deterministic transforms" src="https://img.shields.io/badge/boundary-deterministic__transforms-success">
</p>

**Path:** `tests/domains/hydrology/redaction/README.md`  
**Status:** draft / placeholder-expanded / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Domain segment:** `hydrology`  
**Test lane:** `redaction`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED target was a blank placeholder before this expansion · CONFIRMED `tests/` is the canonical root for enforceability proof · CONFIRMED Hydrology publication posture says public-safe geometry is conditional on source, time, and regulatory-vs-observational distinction · CONFIRMED Hydrology blocks public promotion for unclear rights, unresolved source role, missing EvidenceBundle closure, absent ReleaseManifest, and unresolved review/generalization cases · CONFIRMED sensitivity doctrine requires deterministic, reproducible, named transforms and receipt-style auditability · NEEDS VERIFICATION for executable redaction tests, fixture payload inventory, transform implementation, receipt schemas, policy runtime, release integration, CI coverage, and pass rates.

---

## Purpose

`tests/domains/hydrology/redaction/` is the intended home for Hydrology redaction and generalization tests.

This lane should prove that public-safe Hydrology carriers keep their sensitivity posture, transform profile, output digest, evidence support, policy state, release relationship, correction path, and rollback target visible.

A passing test here should **not** mean that real hydrology data is safe to publish, a transform is approved for production, a release is approved, or a public layer exists. It should mean only that redaction guardrails behaved as expected against bounded fixtures.

---

## Placement basis

`tests/` is the canonical root for enforceability proof. Hydrology is a domain segment inside that root. `redaction/` is a test lane, not the redaction policy home, profile registry, sensitivity doctrine home, schema authority, lifecycle store, proof store, release home, public API surface, or public map surface.

| Responsibility | Correct home | This lane's relationship |
|---|---|---|
| Hydrology redaction tests | `tests/domains/hydrology/redaction/` | This directory. |
| Sensitivity doctrine | `docs/doctrine/sensitivity.md` and standards docs | Doctrine under test; not redefined here. |
| Hydrology publication posture | `docs/domains/hydrology/PUBLICATION_POSTURE.md` | Domain publication boundary under test. |
| Redaction profiles | `policy/redaction/profiles.yaml`, `policy/sensitivity/hydrology/` | Expected policy homes if populated; tests do not replace them. |
| Hydrology policy | `policy/domains/hydrology/` | Referenced by tests, not bypassed here. |
| Machine schemas | `schemas/contracts/v1/` and `schemas/contracts/v1/domains/hydrology/` | Shape checks where accepted. |
| Synthetic fixtures | `fixtures/domains/hydrology/redaction/` | Preferred toy inputs and expected outcomes if populated. |
| Release decisions | `release/` and `release/manifests/hydrology/` | Publication, correction, and rollback authority; tests cannot replace it. |

---

## Invariant under test

> **Redaction is deterministic governance, not presentation polish.** Hydrology redaction/generalization must be named, reproducible, evidence-bound, policy-gated, receipt-backed, release-gated, correction-aware, and rollback-ready. It must not be improvised in the UI, AI response, map style, export script, or release note.

Core checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Sensitivity posture | Fixture records carry a public-safe or sensitivity posture where material. | validation failure / `ABSTAIN`. |
| Transform identity | Transform is named, versioned, deterministic, and parameterized. | validation failure. |
| Receipt posture | Receipt expectation records input ref, profile, parameters, output digest, decision state, and timestamp where material. | validation failure. |
| Source/time/role | Public-safe geometry preserves source, time, and regulatory-vs-observational distinction. | validation failure / `ABSTAIN`. |
| Evidence and policy | EvidenceBundle and PolicyDecision state remain visible before release. | `ABSTAIN` / `DENY`. |
| Release boundary | ReleaseManifest, correction path, and rollback target are required before public carriers. | promotion-blocking failure. |
| No edge improvisation | UI, map style, export, or AI wording cannot invent or silently alter redaction. | validation failure. |

---

## Expected scope

Tests in this lane may validate:

- deterministic public-safe transform fixtures;
- hold/deny behavior when review or generalization is unresolved;
- preservation of source, time, source-role, and regulatory-vs-observational distinctions;
- receipt fields before release-like carriers;
- stable output digests for identical transform inputs and parameters;
- correction behavior when transform inputs, profile, or parameters change;
- rejection of UI-only, AI-only, or release-note-only redaction.

Live source checks, real source exports, production credentials, public tile generation, and real hydrology payloads are out of scope for the default suite.

---

## Fixture posture

Use synthetic, public-safe fixtures only.

Fixture requirements:

- deterministic and no-network;
- compact enough for review in a PR;
- explicit expected outcome;
- explicit sensitivity posture, transform profile, evidence posture, policy state, release relationship, correction, and rollback posture where material;
- no real source exports, lifecycle data, public tiles, credentials, restricted records, or published artifacts.

---

## Finite outcomes

| Condition | Expected outcome |
|---|---|
| Public-safe fixture has source/time/role distinction and complete release context | accepted redaction support only. |
| Review or generalization is unresolved | `DENY` / `HOLD` / `ABSTAIN`. |
| Transform is unnamed, non-deterministic, or missing parameters | validation failure. |
| Receipt or output digest is missing where material | promotion-blocking failure. |
| UI, AI, map style, or export script performs unrecorded redaction | validation failure. |
| Evidence, policy, release, correction, or rollback context is unresolved | `ABSTAIN` / `DENY` / promotion block. |
| Redaction runtime unavailable | `ERROR` or `ABSTAIN`, never public exposure. |

---

## Suggested layout

```text
tests/domains/hydrology/redaction/
├── README.md
├── test_sensitivity_posture_required.py
├── test_transform_is_named_and_deterministic.py
├── test_receipt_required.py
├── test_review_or_generalization_holds.py
├── test_source_time_role_preserved.py
├── test_no_ui_or_ai_only_redaction.py
└── test_release_correction_rollback_required.py
```

---

## Run posture

```bash
pytest tests/domains/hydrology/redaction
```

Status of the command above: **PROPOSED / NEEDS VERIFICATION**. It assumes `pytest` is the accepted test runner and that executable test modules exist. This README does not claim the command currently passes.

---

## Evidence ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | `tests/domains/hydrology/redaction/README.md` existed as a blank placeholder before this replacement. | Did not define the lane. |
| `tests/README.md` | CONFIRMED | `tests/` is enforceability proof and failure should block promotion where trust-spine checks fail. | Does not prove this lane's modules or pass rate. |
| `tests/domains/hydrology/README.md` | CONFIRMED | Hydrology test parent currently exists as a greenfield stub. | Parent lane still needs expansion. |
| `docs/domains/hydrology/PUBLICATION_POSTURE.md` | CONFIRMED doctrine / PROPOSED realization | Defines public-safe geometry posture, deny-by-default rows, release artifacts, correction, stale-state, and rollback. | It is documentation evidence, not redaction runtime proof. |
| `docs/doctrine/sensitivity.md` | CONFIRMED doctrine / PROPOSED implementation paths | Defines sensitivity as first-class, deterministic transforms, redaction profiles, generalization transforms, and RedactionReceipt-style auditability. | Concrete profiles, schemas, CI, and pass rates remain NEEDS VERIFICATION. |
| Repo search | CONFIRMED | Found Hydrology publication posture and sensitivity/redaction doctrine references. | Search is not proof of executable tests or full redaction coverage. |

---

## Validation checklist

- [ ] Executable test modules exist under this lane.
- [ ] Test runner and import paths match the repo's accepted convention.
- [ ] Synthetic redaction fixtures exist for public-safe geometry, unresolved review/generalization, missing transform profile, missing receipt, output digest drift, and UI/AI-only redaction cases.
- [ ] Redaction profile and sensitivity assessment schemas are accepted or safely stubbed.
- [ ] EvidenceRef / EvidenceBundle behavior is available to tests or safely stubbed.
- [ ] PolicyDecision, ReleaseManifest, CorrectionNotice, RedactionReceipt, GeneralizationTransform, and RollbackCard expectations are defined before enforcing them.
- [ ] CI runs the no-network Hydrology redaction suite or marks it as an expected gap.
- [ ] Failures block public carrier promotion or release candidate approval where material.

---

## Rollback

Rollback is required if this lane becomes a live source-fetcher, lifecycle data store, redaction profile authority, sensitivity doctrine authority, source registry, contract root, schema authority, policy authority, proof store, release-decision root, public map/API/tile surface, AI surface, renderer implementation, pipeline implementation, or publication shortcut.

Rollback target for this replacement: previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`.

<p align="right"><a href="#top">Back to top</a></p>
