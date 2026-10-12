<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-soil-smap-ingest-readme
title: Soil SMAP Ingest Pipeline README
type: readme
version: v0.1
status: draft
owners:
  - <soil-pipeline-owner>
  - <soil-domain-steward>
  - <nasa-source-steward>
  - <source-steward>
  - <evidence-steward>
  - <policy-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: pipelines/domains/soil/smap_ingest/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipelines/domains/README.md
  - pipelines/domains/soil/README.md
  - docs/domains/soil/ARCHITECTURE.md
  - docs/domains/soil/DATA_LIFECYCLE.md
  - docs/domains/soil/CANONICAL_PATHS.md
  - docs/sources/catalog/nasa/nasa-smap.md
  - docs/sources/catalog/nasa/nasa-earthdata.md
  - pipeline_specs/soil/smap_ingest.yaml
  - contracts/domains/soil/
  - schemas/contracts/v1/domains/soil/
  - policy/domains/soil/
  - data/raw/soil/
  - data/work/soil/
  - data/quarantine/soil/
  - data/processed/soil/
  - data/catalog/domain/soil/
  - data/triplets/soil/
  - data/registry/sources/soil/
  - data/receipts/pipeline/
  - data/proofs/evidence_bundle/
  - release/candidates/soil/
  - release/manifests/soil/
tags:
  - kfm
  - pipelines
  - domains
  - soil
  - nasa
  - smap
  - ingest
  - soil-moisture
  - satellite-grid
  - model-assimilated
  - ldas
  - enkf
  - ease-grid
  - surface-root-zone-separation
  - support-type-separation
  - evidence
  - policy
  - governance
notes:
  - "This README fills the blank pipelines/domains/soil/smap_ingest path as a Soil-domain executable sublane."
  - "SMAP ingest logic is executable implementation support only; it does not own NASA source descriptors, source catalog profiles, source fetching, schemas, policy, lifecycle data, catalog truth, or release decisions."
  - "The subdirectory name uses the requested underscore form smap_ingest; if repo slug rules prefer hyphenated names, record the path decision with ADR/path-map/rollback notes before moving."
  - "SMAP L4 must be treated as model-assimilated LDAS/EnKF reference moisture, not raw observation truth."
  - "Surface and root-zone semantics, NRT and reprocessed products, EASE-Grid handling, QA flags, product version, source role, support type, and receipt lineage must be preserved."
  - "Concrete executable behavior, source linkage, schedules, CI coverage, schema paths, release wiring, and public API/map behavior remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# NASA SMAP Soil Ingest Pipeline

> Executable Soil-domain sublane for normalizing admitted NASA SMAP soil-moisture products into KFM work candidates, quarantine records, processed candidates, catalog/triplet handoffs, receipts, and release-review packages — without collapsing model-assimilated products into raw observations, surface moisture into root-zone moisture, NRT into reprocessed Standard Quality, or gridded products into station truth.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-SMAP%20soil%20ingest-2e7d32)
![authority](https://img.shields.io/badge/authority-executable%20logic-0a7ea4)
![support](https://img.shields.io/badge/support--type-satellite__soil__moisture-d62728)
![surface-root](https://img.shields.io/badge/surface%20%E2%89%A0%20root--zone-d62728)
![publication](https://img.shields.io/badge/publication-release%20gated-d62728)
![ci](https://img.shields.io/badge/CI-TODO-lightgrey)

**Status:** Draft  
**Path:** `pipelines/domains/soil/smap_ingest/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Domain lane:** Soil  
**Sublane:** NASA SMAP ingest  
**Placement posture:** nested executable sublane under `pipelines/domains/soil/`; concrete executable behavior remains `PROPOSED / NEEDS VERIFICATION` unless backed by tests and repo evidence  
**Public posture:** no direct publication; public output requires lifecycle, EvidenceBundle, source-role, support-type tag, product/version/cadence separation, surface/root-zone separation, rights, sensitivity, policy, catalog/triplet, release, correction, and rollback closure

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. SMAP anti-collapse rules](#3-smap-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Ingest scope](#6-ingest-scope)
- [7. Lifecycle contract](#7-lifecycle-contract)
- [8. Required gates](#8-required-gates)
- [9. Directory contract](#9-directory-contract)
- [10. Inputs and outputs](#10-inputs-and-outputs)
- [11. Minimal SMAP ingest candidate record](#11-minimal-smap-ingest-candidate-record)
- [12. Tests, receipts, and proofs](#12-tests-receipts-and-proofs)
- [13. Promotion, publication, correction, and rollback](#13-promotion-publication-correction-and-rollback)
- [14. Definition of done](#14-definition-of-done)
- [15. Open questions](#15-open-questions)

---

## 1. Purpose

`pipelines/domains/soil/smap_ingest/` is the executable sublane for NASA SMAP normalization inside the Soil domain.

It supports candidate processing for:

- SMAP product metadata, product version, collection, granule, and processing-level references;
- SMAP L3 or selected observation-class gridded products where admitted;
- SMAP L4 model-assimilated surface soil-moisture products;
- SMAP L4 model-assimilated root-zone soil-moisture products;
- NRT/LANCE products and Standard Quality or reprocessed products as distinct cadence/trust classes;
- EASE-Grid native references and governed conversion candidates such as COG or GeoParquet;
- QA flag, uncertainty, retrieval/assimilation method, temporal, and spatial-resolution metadata;
- quarantine records for missing product identity, unresolved rights, missing QA, missing layer semantics, NRT supersession gaps, schema drift, support-type failure, or validation failure;
- catalog/triplet handoff packages after evidence, validation, and policy close.

This directory implements or will implement the **how** of SMAP Soil ingest. It does not fetch from NASA directly, define NASA source identity, define Soil object meaning, define schemas, encode policy, store lifecycle data, decide public release, or turn SMAP-derived products into station truth, ground truth, crop/yield truth, or management advice.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable pipeline logic: the **how**. | CONFIRMED root responsibility |
| Why `domains/soil/`? | Soil is the domain lane; Soil docs place executable logic under `pipelines/domains/soil/`. | CONFIRMED documentation pattern; behavior NEEDS VERIFICATION |
| Why `smap_ingest/`? | This is a narrow executable sublane for SMAP soil-moisture normalization under Soil. | PROPOSED / NEEDS VERIFICATION |
| Is this a source fetcher? | No. Source fetching belongs in `connectors/<source>` or an accepted source-edge home. This sublane reads admitted lifecycle inputs or fixtures. | CONFIRMED separation |
| Where does the source profile live? | `docs/sources/catalog/nasa/nasa-smap.md`. | CONFIRMED source-doc path |
| Where does a declarative run spec live? | `pipeline_specs/soil/smap_ingest.yaml` or accepted spec home. | PROPOSED / NEEDS VERIFICATION |
| Where do schemas and contracts live? | `schemas/contracts/v1/domains/soil/` and `contracts/domains/soil/` or accepted homes. | PROPOSED / NEEDS VERIFICATION |
| Can this sublane publish? | No. It may prepare candidates and release handoffs only through governed workflow. | CONFIRMED doctrine posture |

> [!IMPORTANT]
> SMAP ingest code is subordinate to SourceDescriptor, source role, product version, product level, QA flags, surface/root-zone separation, NRT/reprocessed supersession handling, support-type tagging, EvidenceBundle closure, policy decisions, release manifests, correction notices, and rollback cards. A successful ingest is not public release.

[⬆ Back to top](#top)

---

## 3. SMAP anti-collapse rules

SMAP must remain a gridded satellite/model-assimilated soil-moisture product with explicit product semantics.

Disallowed collapses:

```text
SMAP L4 -> raw observation truth
SMAP surface -> root-zone value
SMAP root-zone -> surface value
SMAP NRT -> reprocessed truth
SMAP grid cell -> station reading
SMAP grid cell -> field-specific fact
SMAP grid cell -> countywide truth without aggregation receipt
SMAP / Mesonet comparison -> silent merged product
generated summary -> evidence
```

Required distinctions:

- product level and product id are explicit;
- NRT, Standard Quality, and reprocessed products remain distinct;
- surface and root-zone layers remain separate catalog assets or Items;
- EASE-Grid/native grid metadata, resolution, CRS, and transform lineage are preserved;
- QA flags and uncertainty fields are retained or quarantine reason is recorded;
- source role and support type are explicit;
- interpolation, aggregation, comparison, or derived indicator products require their own receipts.

[⬆ Back to top](#top)

---

## 4. What belongs here

Files belong here when their primary responsibility is executable SMAP Soil ingest processing.

Appropriate contents include:

- fixture-only dry-run entrypoints for SMAP ingest;
- product/granule metadata normalization helpers;
- EASE-Grid, CRS, resolution, and transform metadata helpers;
- surface/root-zone layer separation helpers;
- NRT vs Standard Quality/reprocessed supersession helpers;
- QA flag and uncertainty normalization helpers;
- time, cadence, overpass, valid-window, retrieval, and processing timestamp helpers;
- source-role and support-type validators;
- resolution-mismatch, no-silent-merge, and station/grid anti-collapse validators;
- quarantine routing helpers for missing metadata, missing QA, missing layer semantics, unresolved rights, supersession drift, or validation failure;
- receipt emitters, if not shared;
- catalog/triplet handoff helpers, if not centralized in `pipelines/catalog/`;
- thin adapters that read governed lifecycle inputs, not live NASA endpoints.

A good placement test:

> If the code transforms admitted SMAP lifecycle inputs into Soil moisture candidates, quarantine records, processed records, receipts, or catalog handoffs, it may belong here. If it fetches NASA data, defines source identity, defines schemas, encodes policy, creates public artifacts, or approves release, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| NASA source fetcher | `connectors/nasa/`, `connectors/nasa-smap/`, or accepted connector home |
| SMAP source profile | `docs/sources/catalog/nasa/nasa-smap.md` |
| NASA Earthdata access profile | `docs/sources/catalog/nasa/nasa-earthdata.md` |
| Source descriptors / source registry entries | `data/registry/sources/soil/`, `data/registry/sources/nasa/`, or accepted registry home |
| Soil architecture and doctrine | `docs/domains/soil/...` |
| Object meaning contracts | `contracts/domains/soil/...` |
| JSON Schemas | `schemas/contracts/v1/domains/soil/...` |
| Policy bundles and release rules | `policy/domains/soil/`, rights, sensitivity, and release policy roots |
| Declarative run specs | `pipeline_specs/soil/...` |
| Fixtures | `fixtures/domains/soil/smap_ingest/` or accepted fixture home |
| Tests | `tests/pipelines/domains/soil/smap_ingest/` or accepted test home |
| Raw, work, quarantine, processed, catalog, triplet, or published outputs | `data/...` lifecycle homes |
| Receipts and proofs | `data/receipts/...`, `data/proofs/...` |
| Release decisions | `release/candidates/soil/`, `release/manifests/soil/`, rollback/correction release homes |
| Public API or map code | `apps/governed-api/`, `apps/explorer-web/`, packages |
| Mesonet, USCRN, SCAN, SSURGO, gSSURGO, crop, drought, or vegetation-stress products | Owning source/domain lanes or reviewed downstream products only |

[⬆ Back to top](#top)

---

## 6. Ingest scope

| Scope area | Pipeline responsibility | Publication posture |
|---|---|---|
| Product metadata | Normalize product id, product level, collection/version, granule id, and source refs. | Candidate until descriptor, rights, and validation close. |
| Surface moisture | Normalize surface soil-moisture layer with method and caveats. | Surface is not root-zone. |
| Root-zone moisture | Normalize root-zone soil-moisture layer with method and caveats. | Root-zone is not surface. |
| NRT products | Normalize NRT class, latency, QA, and supersession expectation. | Preliminary; must be superseded or tombstoned as applicable. |
| Reprocessed products | Normalize Standard Quality or reprocessed products as canonical analytical lane. | Supersedes NRT for same window where source supports it. |
| Native grid | Preserve EASE-Grid, resolution, CRS, cell geometry, and transform lineage. | Grid cell is not station truth. |
| QA / uncertainty | Preserve quality flags and uncertainty fields. | Missing QA quarantines or restricts. |
| Catalog/triplet handoff | Prepare restricted or public-safe catalog/graph candidates after evidence closure. | Projection does not replace canonical review state. |

[⬆ Back to top](#top)

---

## 7. Lifecycle contract

Every SMAP ingest run must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal stance:

1. **Read** approved fixtures, immutable raw captures, work candidates, quarantine inputs in remediation mode, or prior processed baselines.
2. **Normalize** into gridded soil-moisture candidates with source role, support type, product level, product version, grid metadata, surface/root-zone layer, cadence class, QA, uncertainty, temporal scope, evidence refs, and receipt refs.
3. **Quarantine** unresolved rights, missing descriptor, missing product identity, missing layer semantics, missing QA, grid metadata failure, NRT supersession drift, support-type failure, schema drift, or validation failure.
4. **Promote to processed** only after validation, policy, evidence, support-type, grid, QA, cadence/supersession, and review gates close.
5. **Prepare catalog/triplet handoffs** only after processed-state and evidence closure, and only with product-level, surface/root-zone, cadence, uncertainty, and model-assimilation caveats.
6. **Publish** only through release decisions, public-safe artifacts, rollback targets, and correction paths.

Promotion is a governed state transition with receipts and review evidence, not a file move.

[⬆ Back to top](#top)

---

## 8. Required gates

Every SMAP ingest run must check or explicitly fail closed on:

1. **Source descriptor gate** — NASA SMAP source identity, role, cadence, rights, access posture, and sensitivity posture are known.
2. **Product identity gate** — product id, product level, collection, version, granule id, and source refs are recorded.
3. **Source-role gate** — L4 remains model-assimilated reference product; selected L3 observation-class products remain distinct.
4. **Support-type gate** — candidates carry the accepted satellite/gridded/model-assimilated soil support label.
5. **Surface/root-zone gate** — surface and root-zone products remain separate and are never averaged into unlabeled soil moisture.
6. **NRT/reprocessed gate** — preliminary products remain marked as NRT and are superseded or tombstoned when Standard Quality/reprocessed products close.
7. **Grid gate** — native EASE-Grid, resolution, CRS, transform, and cell geometry are preserved.
8. **QA/uncertainty gate** — QA flags, retrieval/assimilation caveats, and uncertainty fields are preserved or quarantined.
9. **Resolution mismatch gate** — SMAP grid cells, station observations, field parcels, county units, and derived rasters remain distinct.
10. **No-silent-merge gate** — SMAP is never silently merged with Mesonet, USCRN, SCAN, SSURGO, HLS, FIRMS, drought, crop, or vegetation-stress products.
11. **Rights gate** — unknown or restrictive license, permission, attribution, privacy, or redistribution terms block public release.
12. **Sensitivity gate** — field-specific, owner-specific, cross-lane, or insufficiently reviewed derivatives fail closed until reviewed.
13. **Derived-artifact gate** — aggregation, resampling, interpolation, comparison, anomaly, or downstream indicator derivation requires its own receipt.
14. **Schema, contract, evidence, policy, validation, receipt, catalog/triplet, and release gates** — all must close or the run abstains, denies, or quarantines.
15. **No-direct-publish gate** — no writes to public UI, public API, or `data/published/` without release workflow authority.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended shape:

```text
pipelines/domains/soil/smap_ingest/
├── README.md                         # this file
├── PIPELINE_CONTRACT.md              # PROPOSED: sublane execution contract
├── run_dry_fixture.py                # PROPOSED synthetic/redacted fixture only
├── normalize_product_metadata.py     # PROPOSED
├── normalize_surface_moisture.py     # PROPOSED
├── normalize_root_zone_moisture.py   # PROPOSED
├── normalize_grid_metadata.py        # PROPOSED
├── normalize_qa_uncertainty.py       # PROPOSED
├── normalize_time_cadence.py         # PROPOSED
├── validate_surface_root_zone.py     # PROPOSED
├── validate_nrt_supersession.py      # PROPOSED
├── validate_grid_resolution.py       # PROPOSED
├── validate_support_type.py          # PROPOSED
├── build_catalog_handoff.py          # PROPOSED if not centralized in pipelines/catalog/
├── emit_receipt.py                   # PROPOSED only if not shared
└── adapters/                         # PROPOSED thin lifecycle adapters, no NASA fetching
```

Declarative specs should live outside this directory:

```text
pipeline_specs/soil/smap_ingest.yaml # PROPOSED / NEEDS VERIFICATION
```

Generated outputs must not be written beside the code that generated them. Use accepted lifecycle homes under `data/`, proof homes under `data/proofs/`, receipt homes under `data/receipts/`, and release homes under `release/`.

[⬆ Back to top](#top)

---

## 10. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Fixture input | `fixtures/domains/soil/smap_ingest/` or accepted fixture home | Synthetic, generalized, or redacted. |
| Raw SMAP capture | `data/raw/soil/<source_id>/<run_id>/` or accepted NASA raw home | Immutable source-edge capture with source descriptor and receipt. |
| Work candidate | `data/work/soil/<run_id>/` | Candidate only. |
| Quarantine record | `data/quarantine/soil/<reason>/<run_id>/` | Failed, restricted, unresolved, or unsafe material. |
| Processed SMAP dataset | `data/processed/soil/<dataset_id>/<version>/` | Validated/restricted; not automatically public. |
| Catalog candidate | `data/catalog/domain/soil/...` or approved catalog home | After processed-state, transform, and evidence gates. |
| Triplet / graph delta | `data/triplets/soil/...` or approved graph-delta home | Projection only. |
| Receipts / proofs | `data/receipts/...`, `data/proofs/...` | Required for auditable promotion and release review. |
| Release handoff | `release/candidates/soil/...` | Only through release workflow. |

[⬆ Back to top](#top)

---

## 11. Minimal SMAP ingest candidate record

The final schema is not defined here. This example shows the minimum information a SMAP ingest candidate should preserve.

```yaml
schema_version: kfm.soil_smap_ingest_candidate.v1
candidate_id: soil_smap_<product_id>_<layer>_<cell_or_granule_digest>_<run_id>
pipeline_id: domains.soil.smap_ingest
run_id: run_YYYYMMDDThhmmssZ
status: WORK_CANDIDATE
source:
  source_id: nasa_smap
  source_role: <model_assimilated_reference|observation|candidate>
  support_type: <satellite_soil_moisture|model_assimilated_soil_moisture>
  lifecycle_ref: data/raw/soil/nasa_smap/<run_id>/
  input_hash: sha256:<hash>
  rights_state: needs_review
product:
  product_id: <smap_product_id>
  product_level: <L3|L4|NRT|other>
  collection_version: <version_or_null>
  cadence_class: <nrt|standard_quality|reprocessed|other>
  granule_id: <granule_id>
layer:
  moisture_layer: <surface|root_zone>
  model_assimilated: true
  raw_observation_truth: false
grid:
  native_grid: EASE-Grid
  crs: <crs_or_null>
  resolution_m: <resolution_or_null>
  cell_ref: <cell_or_asset_ref>
qa:
  qa_flags: []
  uncertainty_ref: null
  preliminary: true
  superseded_by: null
anti_collapse:
  surface_is_root_zone: false
  nrt_is_reprocessed_truth: false
  grid_cell_is_station_observation: false
  smap_is_ground_truth: false
  generated_summary_is_evidence: false
policy:
  outcome: ABSTAIN
  reason_code: SOURCE_DESCRIPTOR_QA_SURFACE_ROOT_OR_EVIDENCE_NOT_RESOLVED
evidence:
  evidence_bundle_ref: null
  citation_state: ABSTAIN
outputs:
  candidate_record: data/work/soil/run_YYYYMMDDThhmmssZ/smap_candidate.yml
  receipt: data/receipts/pipeline/soil/smap_ingest/run_YYYYMMDDThhmmssZ.yml
rollback:
  required_before_publication: true
```

[⬆ Back to top](#top)

---

## 12. Tests, receipts, and proofs

Default execution is **fixture-only, synthetic/generalized/redacted, and no-network** until source activation, rights review, support-type review, QA review, product-version review, and CI coverage are approved.

Recommended tests:

```text
tests/pipelines/domains/soil/smap_ingest/
├── test_no_network_dry_run.py                 # PROPOSED
├── test_l4_model_assimilated_not_raw_truth.py # PROPOSED
├── test_surface_root_zone_separate.py         # PROPOSED
├── test_nrt_reprocessed_supersession.py       # PROPOSED
├── test_ease_grid_metadata_required.py        # PROPOSED
├── test_quality_flags_preserved.py            # PROPOSED
├── test_support_type_required.py              # PROPOSED
├── test_grid_not_station_truth.py             # PROPOSED
├── test_no_silent_mesonet_merge.py            # PROPOSED
├── test_derived_indicator_requires_receipt.py # PROPOSED
├── test_missing_evidence_abstains.py          # PROPOSED
├── test_receipt_hashes.py                     # PROPOSED
└── test_no_direct_publish.py                  # PROPOSED
```

A dry run should prove fixtures load without network access, L4 remains model-assimilated reference moisture, surface/root-zone layers are separated, NRT/reprocessed cadence is preserved, EASE-Grid metadata is present, QA flags are retained, EvidenceBundle gaps produce abstention, receipts are deterministic, and no run writes directly to public UI, public API, `data/published/`, or release manifests.

[⬆ Back to top](#top)

---

## 13. Promotion, publication, correction, and rollback

SMAP ingest may prepare candidates. It does not publish.

Required promotion chain:

```text
SMAP raw/work input
  -> gridded/model-assimilated soil-moisture candidate
  -> validation report
  -> policy decision
  -> support-type / QA / grid / cadence receipt where required
  -> EvidenceBundle closure
  -> processed Soil SMAP dataset version
  -> catalog / triplet candidate
  -> release candidate
  -> ReleaseManifest
  -> RollbackCard
  -> public-safe artifact
```

Correction and rollback posture:

- denied, abstained, errored, restricted, preliminary, superseded, and quarantined runs remain auditable;
- candidate rollback preserves receipts and proof state;
- NRT products are superseded or tombstoned rather than silently deleted where applicable;
- processed versions are superseded by governed state transition, not hidden overwrite;
- derived products are invalidated if product refs, layer refs, grid refs, QA refs, cadence refs, method refs, or policy refs drift;
- public artifact rollback is owned by `release/`, not by this directory.

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- fills the blank `pipelines/domains/soil/smap_ingest/README.md` file;
- identifies this directory as a nested executable Soil sublane;
- prevents connector, source-profile, schema, contract, policy, fixture, test, data, receipt, proof, catalog, and release authority from being placed here;
- preserves SMAP source role, support type, product identity, EASE-Grid metadata, surface/root-zone distinction, NRT/reprocessed cadence, QA/uncertainty, evidence, policy, lifecycle, catalog/triplet, release, correction, and rollback boundaries;
- blocks modeled/raw, surface/root-zone, NRT/reprocessed, grid/station, and public/private lifecycle collapse;
- gives maintainers a fixture-first, fail-closed expansion pattern.

Future executable work in this sublane is done only when it has source-descriptor coverage, synthetic/generalized/redacted no-network fixtures, schema-backed candidates, contract conformance, source-role/support-type/product/layer/grid/QA/evidence tests, deterministic receipts, no-direct-publish tests, CI coverage, steward-review handoff, and release/correction/rollback documentation.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `SOIL-SMAP-001` | Should the subdirectory remain `smap_ingest` or be renamed to a hyphenated slug after path convention review? | NEEDS VERIFICATION / ADR |
| `SOIL-SMAP-002` | Which source-edge job owns NASA SMAP retrieval before this ingest sublane reads lifecycle inputs? | NEEDS VERIFICATION |
| `SOIL-SMAP-003` | Which SMAP product identifiers, layers, cadence classes, and fields are first-wave approved for fixture-only dry runs? | NEEDS VERIFICATION |
| `SOIL-SMAP-004` | Which CI job owns SMAP ingest invariant tests? | UNKNOWN |
| `SOIL-SMAP-005` | Should catalog handoff logic live here or in centralized `pipelines/catalog/` with a SMAP adapter? | NEEDS VERIFICATION |
| `SOIL-SMAP-006` | Which public-safe map/API products are allowed after review and release, and at what product/layer/cadence/resolution caveat level? | NEEDS VERIFICATION |
| `SOIL-SMAP-007` | Which receipt type owns SMAP-to-Mesonet comparison, anomaly, or cross-lane indicator products? | PROPOSED / NEEDS ADR |

---

## Maintainer note

Start with synthetic/generalized fixture-only dry runs and negative tests. Do not add live NASA fetching, supportless values, unlabeled SMAP moisture, silent station merges, unreceipted resampling, public map layers, release handoff automation, or direct API payload generation until source roles, rights, support-type separation, product/layer/cadence handling, QA validation, evidence closure, and rollback are proven.
