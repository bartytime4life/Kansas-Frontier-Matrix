<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-habitat-land-cover-model-run-readme
title: Habitat Land-Cover Model-Run Test README
type: test-readme
version: v0.1
status: draft; placeholder-expanded; test-lane; PROPOSED / NEEDS VERIFICATION
owners:
  - OWNER_TBD — Habitat domain steward
  - OWNER_TBD — Land-cover steward
  - OWNER_TBD — Model-run steward
  - OWNER_TBD — QA steward
created: NEEDS VERIFICATION — blank placeholder existed before v0.1 expansion
updated: 2026-07-05
policy_label: public-doc; tests; habitat; land-cover; model-run; no-network; receipt-not-proof; release-gated
tags: [kfm, tests, habitat, land_cover, model_run, ModelRunReceipt, input-digest, config-digest, output-digest, release-gated]
related:
  - ../../../../README.md
  - ../../../../../fixtures/domains/habitat/land_cover/model_run/README.md
  - ../../../../../contracts/domains/habitat/land_cover/model_run_receipt.md
  - ../../../../../docs/domains/habitat/sublanes/land_cover.md
notes:
  - "This file replaces a blank placeholder at tests/domains/habitat/land_cover/model_run/README.md."
  - "This README documents a test lane only. It does not define contracts, schemas, fixtures, receipts, policy, release decisions, pipeline code, public API material, map material, tiles, or published artifacts."
  - "Rollback target for this replacement is previous blank blob SHA 8b137891791fe96927ad78e64b0aad7bded08bdc."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Habitat land-cover model-run tests

> Deterministic, no-network test documentation for Habitat land-cover model-run and receipt checks.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Domain: habitat" src="https://img.shields.io/badge/domain-habitat-2e7d32">
  <img alt="Lane: model run" src="https://img.shields.io/badge/lane-model__run-blue">
</p>

**Path:** `tests/domains/habitat/land_cover/model_run/README.md`  
**Status:** draft / placeholder-expanded / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Default execution posture:** deterministic, synthetic, no-network fixtures only  
**Truth posture:** CONFIRMED target was a blank placeholder before this expansion · CONFIRMED the paired fixture README describes toy model-run metadata, input digests, config digests, output inventory, validation posture, uncertainty notes, and receipt pointers · CONFIRMED the land-cover `ModelRunReceipt` contract says a receipt is process memory and not publication authority · NEEDS VERIFICATION for executable test modules, fixtures, schema, validators, pipeline integration, receipt storage, release integration, CI coverage, and pass rates.

---

## Purpose

`tests/domains/habitat/land_cover/model_run/` is the intended home for bounded checks over Habitat land-cover model-run records and receipt-style outputs.

The lane should verify that model-run records preserve:

- run identity;
- model or transform identity;
- input closure;
- config closure;
- output inventory;
- validation posture;
- evidence references;
- correction and rollback references;
- release relationship where public use is material.

---

## Placement basis

| Responsibility | Correct home |
|---|---|
| Model-run tests | `tests/domains/habitat/land_cover/model_run/` |
| Synthetic examples | `fixtures/domains/habitat/land_cover/model_run/` |
| Receipt meaning | `contracts/domains/habitat/land_cover/model_run_receipt.md` |
| Land-cover doctrine | `docs/domains/habitat/sublanes/land_cover.md` |
| Pipelines | `pipelines/domains/habitat/land_cover/` |
| Pipeline specs | `pipeline_specs/habitat/land_cover/` |
| Receipts | `data/receipts/habitat/land_cover/` |
| Release | `release/manifests/habitat/` |

---

## Expected checks

Future tests should cover:

- required run ID and model or transform ID;
- input digest presence;
- config digest presence;
- output reference and digest presence;
- receipt completeness;
- model-vs-observation labeling;
- correction and rollback posture;
- finite outcome behavior when evidence, validation, policy, or release context is not available.

---

## Suggested layout

```text
tests/domains/habitat/land_cover/model_run/
├── README.md
├── test_run_identity_required.py
├── test_input_config_closure.py
├── test_output_inventory.py
├── test_model_vs_observation.py
└── test_release_correction_rollback.py
```

---

## Run posture

```bash
pytest tests/domains/habitat/land_cover/model_run
```

Status: **PROPOSED / NEEDS VERIFICATION**. This README does not claim that the command currently passes.

---

## Rollback

Rollback is required if this lane becomes a source-export store, model-output store, lifecycle data store, fixture root, contract root, schema authority, receipt authority, policy authority, proof store, release-decision root, public map/API/tile surface, renderer implementation, pipeline implementation, or publication shortcut.

<p align="right"><a href="#top">Back to top</a></p>
