<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-data-readme
title: contracts/data/ — Data Semantic Contracts
type: readme
version: v0.3
status: draft
owners: OWNER_TBD — Contract steward · Data steward · Source steward · Evidence steward · Schema steward · Policy steward · Validation steward · Release steward · Docs steward
created: 2026-06-20
updated: 2026-09-08
policy_label: public; contracts; data; semantic-contracts; lifecycle-aware; evidence-aware
tags: [kfm, contracts, data, semantic-contracts, lifecycle, raw, work, quarantine, processed, catalog, triplet, published, evidence, governance]
related:
  - ../README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../docs/architecture/contract-schema-policy-split.md
  - ../../docs/architecture/domain-placement-law.md
  - ../../schemas/contracts/v1/data/
  - ../../policy/
  - ../../fixtures/
  - ../../tests/
  - ../../tools/validators/
  - ../../.github/workflows/
  - ../../data/
  - ../../release/
notes:
  - "Reconciled the direct contract inventory and declared implementation companions against main@d58c91b5ca5efb915bb21bf8d6945c46faa41e47."
  - "This directory defines semantic meanings for data-related contract objects only; it is not the actual data lifecycle root."
  - "Presence of a schema, validator, fixture, test, or workflow is implementation evidence, not proof of execution, policy approval, release, or public-use authority."
  - "Three contract documents declare validator paths that are absent from the observed tree; those gaps are recorded below."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Data Semantic Contracts

> Semantic contracts for governed data objects and lifecycle references. This folder defines meaning; it does not store datasets, schemas, policy rules, validator code, fixtures, proofs, or releases.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Owner: OWNER_TBD" src="https://img.shields.io/badge/owner-OWNER__TBD-lightgrey">
  <img alt="Inventory: 34 contracts" src="https://img.shields.io/badge/contracts-34-blue">
  <img alt="Schemas: 34 present" src="https://img.shields.io/badge/schemas-34%2F34-green">
  <img alt="Validator references: 3 unresolved" src="https://img.shields.io/badge/validator__refs-3__unresolved-orange">
  <img alt="Authority: semantic" src="https://img.shields.io/badge/authority-semantic__contracts-purple">
</p>

`contracts/data/`

## Quick jumps

[Status](#status) · [Authority boundary](#authority-boundary) · [Observed snapshot](#observed-snapshot) · [Contract inventory](#contract-inventory) · [Implementation companions](#implementation-companions) · [Known gaps](#known-gaps) · [Lifecycle boundary](#lifecycle-boundary) · [Authoring rules](#authoring-rules) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Definition of done](#definition-of-done)

---

## Status

> [!IMPORTANT]
> **Document status:** `draft`  
> **Owner:** `OWNER_TBD`  
> **Observed repository state:** `CONFIRMED` at `main@d58c91b5ca5efb915bb21bf8d6945c46faa41e47` with tree `8a9b36a3f35d71450c67be291f7e77f981058ddb`.  
> **Currentness rule:** re-pin the branch, target blob, inventory, and companion paths before operational use.

The observed directory contains 35 direct files: this README and 34 object-level semantic contract documents. The inventory and companion counts below are a repository-presence snapshot. They do not change any contract's declared status or prove that a validator or workflow ran successfully.

---

## Authority boundary

The adopted split is:

| Root | Decision class |
|---|---|
| `contracts/` | What an object or interface means. |
| `schemas/` | What machine shape is valid. |
| `policy/` | When an object is allowed, denied, held, restricted, or requires abstention. |
| `fixtures/` and `tests/` | Executable examples and enforceability evidence. |
| `tools/validators/` | Validator implementation. |
| `data/` | Governed data instances and lifecycle state. |
| `release/` | Release, correction, supersession, and rollback records. |

This README may report repository evidence, but it cannot create schema, policy, source-admission, review, release, publication, or public-use authority.

The path is governed by [Directory Rules](../../docs/doctrine/directory-rules.md), [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md), the [contract/schema/policy split](../../docs/architecture/contract-schema-policy-split.md), and the [domain placement law](../../docs/architecture/domain-placement-law.md). No path change is proposed here.

---

## Observed snapshot

| Observation | Result | Interpretation |
|---|---:|---|
| Direct files under `contracts/data/` | 35 | One README plus 34 semantic contract documents; no direct subdirectories. |
| Contract documents containing a draft posture | 9 | Status remains owned by each contract. |
| Contract documents with no draft marker and a proposed posture | 25 | Proposed, inactive, fixture-only, experimental, and review-required qualifiers remain binding. |
| Same-stem schemas under `schemas/contracts/v1/data/` | 34 / 34 | Machine-shape companions are present for every listed contract. |
| Contracts declaring at least one validator path that resolves | 29 / 34 | Presence only; execution and coverage are separate checks. |
| Contracts declaring a validator path that does not resolve | 3 / 34 | Stale references are listed in [Known gaps](#known-gaps). |
| Contracts without a declared validator path | 2 / 34 | Absence of a declaration is not proof that no related tool exists. |
| Contracts declaring at least one fixture JSON path that resolves | 17 / 34 | Not an exhaustive fixture inventory. |
| Contracts declaring at least one test module path that resolves | 23 / 34 | Not proof that the test ran on this snapshot. |
| Same-stem workflow files present under `.github/workflows/` | 24 / 34 | Naming correlation only; triggers, path filters, and successful execution require separate verification. |

---

## Contract inventory

The statuses below are copied from each contract's metadata. A file's presence here does not promote it to active, accepted, authoritative, or released.

| Contract | Declared status |
|---|---|
| [`analytical_view_manifest.md`](analytical_view_manifest.md) | `proposed-inactive; fixture-only; no-network; non-authoritative` |
| [`baseline_cohort_assessment.md`](baseline_cohort_assessment.md) | `proposed; fixture-first; local-only; non-authoritative` |
| [`cartographic_omission_disclosure.md`](cartographic_omission_disclosure.md) | `proposed-inactive; fixture-only; no-network; non-authoritative` |
| [`catalog_closure_packet.md`](catalog_closure_packet.md) | `draft; PROPOSED; fixture-first` |
| [`catalog_distribution_mapping_profile.md`](catalog_distribution_mapping_profile.md) | `proposed` |
| [`catalog_health_report.md`](catalog_health_report.md) | `draft; PROPOSED; fixture-first` |
| [`catalog_matrix.md`](catalog_matrix.md) | `draft` |
| [`catalog_matrix_claim_closure_profile.md`](catalog_matrix_claim_closure_profile.md) | `proposed` |
| [`catalog_matrix_closure_profile.md`](catalog_matrix_closure_profile.md) | `proposed` |
| [`catalog_trust_extension.md`](catalog_trust_extension.md) | `draft; DRAFT_SCHEMA; fixture-first; non-authoritative` |
| [`county_environmental_recency_spine.md`](county_environmental_recency_spine.md) | `proposed-inactive; fixture-only; non-authoritative` |
| [`county_year_panel.md`](county_year_panel.md) | `proposed; inactive; fixture-only; review-required` |
| [`dataset_version.md`](dataset_version.md) | `draft` |
| [`friday_natural_systems_pulse.md`](friday_natural_systems_pulse.md) | `proposed; inactive; no-network; no-automation` |
| [`layer_catalog_item.md`](layer_catalog_item.md) | `draft` |
| [`layer_descriptor.md`](layer_descriptor.md) | `draft` |
| [`layer_legend_disclosure.md`](layer_legend_disclosure.md) | `proposed-inactive; fixture-only; no-network; non-authoritative` |
| [`layer_manifest.md`](layer_manifest.md) | `draft; proposed-inactive; dual-profile; fixture-only-strict-profile` |
| [`lidar_lineage_manifest_candidate.md`](lidar_lineage_manifest_candidate.md) | `proposed; experimental; fixture-only; non-authoritative` |
| [`map_scale_generalization_disclosure.md`](map_scale_generalization_disclosure.md) | `proposed-inactive; fixture-only; no-network; non-authoritative` |
| [`material_change_assessment.md`](material_change_assessment.md) | `proposed; fixture-first; no-network; non-authoritative` |
| [`output_lane_split_manifest.md`](output_lane_split_manifest.md) | `proposed-inactive` |
| [`public_map_misuse_review.md`](public_map_misuse_review.md) | `proposed; inactive; fixture-only; NEEDS STEWARD REVIEW` |
| [`spatial_table_normalization_assessment.md`](spatial_table_normalization_assessment.md) | `proposed-inactive; fixture-only; no-network; non-authoritative` |
| [`stac_attestation_hook.md`](stac_attestation_hook.md) | `proposed-inactive; fixture-only; non-authoritative` |
| [`stac_geoparquet_mirror_assessment.md`](stac_geoparquet_mirror_assessment.md) | `proposed; experimental-profile; fixture-only; non-authoritative` |
| [`stac_link_closure_assessment.md`](stac_link_closure_assessment.md) | `proposed; fixture-only; no-network; non-authoritative` |
| [`stac_search_behavior_fixture_profile.md`](stac_search_behavior_fixture_profile.md) | `proposed-inactive; fixture-only; non-authoritative` |
| [`stac_zarr_asset_metadata_profile.md`](stac_zarr_asset_metadata_profile.md) | `proposed-inactive; fixture-only; non-authoritative` |
| [`synthetic_release_catalog_closure_profile.md`](synthetic_release_catalog_closure_profile.md) | `proposed` |
| [`temporal_slice.md`](temporal_slice.md) | `proposed; fixture-first; no-network; non-authoritative` |
| [`time_series_promotion_candidate_manifest.md`](time_series_promotion_candidate_manifest.md) | `proposed-inactive` |
| [`typed_receipt_aggregation.md`](typed_receipt_aggregation.md) | `proposed-inactive; fixture-only; non-authoritative` |
| [`validation_report.md`](validation_report.md) | `draft` |

---

## Implementation companions

Every inventory item has a same-stem schema at:

```text
schemas/contracts/v1/data/<contract_stem>.schema.json
```

The contract documents also declare validators across `tools/validators/data/`, `tools/validators/catalog/`, `tools/validators/catalog_closure/`, `tools/validators/catalog_trust_extension/`, `tools/validators/receipts/`, `tools/validators/stac/`, and the validator root. Fixtures are primarily declared under `fixtures/contracts/v1/data/`, with the STAC attestation hook declaring `fixtures/data/stac_attestation_hook/`. Tests are declared under `tests/data/`, `tests/generators/`, and `tests/validators/`.

Companion presence establishes only that a path resolved in the observed tree. It does not establish:

- that a schema is adopted rather than draft;
- that declared valid, invalid, denied, held, stale, superseded, and rollback cases are complete;
- that a validator is registered or exercised by a required workflow;
- that a same-stem workflow watches the contract, schema, validator, fixture, and test paths;
- that a hosted run succeeded at the observed commit;
- that policy, evidence, review, source admission, release, or public-use gates passed.

---

## Known gaps

Three contract documents declare validator paths that were absent from the observed tree:

| Contract | Declared unresolved path |
|---|---|
| [`catalog_matrix.md`](catalog_matrix.md) | `tools/validators/data/validate_catalog_matrix.py` |
| [`layer_catalog_item.md`](layer_catalog_item.md) | `tools/validators/data/validate_layer_catalog_item.py` |
| [`layer_descriptor.md`](layer_descriptor.md) | `tools/validators/data/validate_layer_descriptor.py` |

Two contract documents do not declare a validator path:

- [`output_lane_split_manifest.md`](output_lane_split_manifest.md) declares a generator, fixture, and generator test instead;
- [`public_map_misuse_review.md`](public_map_misuse_review.md) retains its proposed, inactive, fixture-only, and steward-review-required posture.

These observations are documentation findings, not authorization to add tools, change statuses, activate workflows, or weaken validation.

---

## Lifecycle boundary

Actual KFM data belongs under the `data/` responsibility root. The lifecycle is:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

| Stage | Contract posture | Public posture |
|---|---|---|
| `RAW` | Source-admitted material before normalization. | Not public by default. |
| `WORK` | Intermediate working material. | Not public. |
| `QUARANTINE` | Held for rights, sensitivity, validation, source-role, or evidence problems. | Denied or restricted until resolved. |
| `PROCESSED` | Derived or normalized material. | Not public by itself. |
| `CATALOG` | Catalog, index, or metadata representation. | Public only when separately released and policy-safe. |
| `TRIPLET` | Graph or triplet representation. | Derived view, not sovereign truth. |
| `PUBLISHED` | Released artifact or public-safe product. | Requires evidence, rights, sensitivity, validation, review, policy, and release gates. |

> [!CAUTION]
> A contract that describes data is not the data. A schema-valid object is not automatically evidence-backed, policy-admissible, reviewed, released, or safe for public use.

---

## Authoring rules

Every data contract under this folder must state:

- the object family and semantic identity it defines;
- its declared maturity and activity posture;
- the lifecycle stages it can reference;
- source-role, provenance, rights, sensitivity, and geoprivacy requirements;
- evidence and temporal requirements;
- schema, validator, fixture, test, and workflow companions, with unresolved paths labeled;
- policy, review, release, correction, supersession, and rollback behavior;
- valid and invalid usage examples;
- what belongs under schemas, policy, fixtures, tests, data, and release instead of the contract.

Shared object families must be referenced or extended rather than copied. A locator is not authority, validator presence is not execution, and documentation cannot promote an object.

---

## Validation

Before relying on this directory:

1. Re-pin the repository commit and target README blob.
2. Re-enumerate direct files under `contracts/data/`.
3. Resolve each contract's schema, validator, fixture, test, and workflow declarations against the same tree.
4. Inspect workflow path filters and validator registration; do not infer coverage from filenames.
5. Run the applicable exact-head checks and preserve their run identifiers and conclusions.
6. Verify source-role, rights, sensitivity, evidence, review, policy, correction, and release gates for any operational consumer.
7. Confirm that public API, UI, and AI surfaces cannot read RAW, WORK, QUARANTINE, unpublished candidates, or internal stores as public truth.

---

## Evidence basis

| Source | Status | Supports | Limit |
|---|---|---|---|
| GitHub `main@d58c91b5ca5efb915bb21bf8d6945c46faa41e47` / tree `8a9b36a3f35d71450c67be291f7e77f981058ddb` | `CONFIRMED` repository snapshot | Direct inventory and companion-path presence. | Point-in-time evidence; requires re-pin. |
| [`contracts/README.md`](../README.md) | `CONFIRMED` repository doctrine | Contracts own semantic meaning. | Does not prove data-family execution. |
| [Directory Rules](../../docs/doctrine/directory-rules.md) and [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | `CONFIRMED` adopted placement law | Authority split, inheritance, machine projection, and migration controls. | Does not activate a contract or authorize release. |
| [Contract/schema/policy split](../../docs/architecture/contract-schema-policy-split.md) and [domain placement law](../../docs/architecture/domain-placement-law.md) | `CONFIRMED` repository guidance | Meaning, shape, admissibility, enforceability, and lifecycle separation. | Concrete execution requires validators, tests, workflows, and run evidence. |
| Connected Drive Directory Rules and KFM Unified Doctrine Synthesis | `CONFIRMED` read-only supporting context | Consistent contracts/schemas/policy/data separation. | Supporting context only; GitHub remains implementation authority. |
| KFM Knowledge Workspace in Notion | `CONFIRMED` coordination surface | Bounded handoff and review context. | Does not implement, approve, merge, release, or publish repository changes. |

---

## Rollback

The pre-change README content is preserved by blob `1f413dba0129ef892e9a5b49e5b89b8e828a3e20`.

Before merge, abandon this documentation-only change by closing its PR and deleting only its task branch. After an authorized merge, restore the prior content through a separately reviewed revert. Do not use rollback to erase evidence, bypass review, or claim that companion implementation was removed.

---

## Definition of done

- [x] The direct `contracts/data/` inventory is enumerated at a pinned repository tree.
- [x] Every listed contract's same-stem canonical data schema is present at the pinned tree.
- [x] Declared validator, fixture, and test paths are reconciled for repository presence.
- [x] Unresolved validator declarations are explicit.
- [x] Presence, execution, policy approval, review, release, and public-use authority are kept separate.
- [ ] Contract and directory owners are confirmed and `OWNER_TBD` is replaced.
- [ ] The three unresolved validator declarations are corrected or implemented by separately reviewed work.
- [ ] Validator registration, workflow path coverage, and exact-head execution evidence are verified per contract.
- [ ] Contract maturity and activity postures receive steward review.
- [ ] Policy, evidence, source-admission, release, correction, supersession, and rollback gates are verified for operational use.

---

## Status summary

`contracts/data/` contains 34 semantic contract documents with 34 same-stem machine schemas at the observed repository tree. That is meaningful implementation presence, but it is not blanket proof of validator execution, policy admissibility, review, release, publication, or public-use authority. Three declared validator paths remain unresolved, two contracts declare no validator path, and every contract retains its own draft or proposed posture until separately reviewed.

<p align="right"><a href="#top">Back to top</a></p>
