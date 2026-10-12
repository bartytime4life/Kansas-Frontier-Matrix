<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-hydrology-ingest-3dep-terrain-readme
title: Hydrology 3DEP Terrain Ingest Pipeline README
type: readme
version: v0.1
status: draft
owners:
  - <hydrology-pipeline-owner>
  - <hydrology-domain-steward>
  - <usgs-source-steward>
  - <spatial-foundation-steward>
  - <evidence-steward>
  - <policy-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: pipelines/domains/hydrology/ingest_3dep_terrain/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipelines/domains/README.md
  - pipelines/domains/hydrology/README.md
  - pipelines/domains/hydrology/ingest/README.md
  - docs/domains/hydrology/README.md
  - docs/domains/hydrology/DATA_LIFECYCLE.md
  - docs/domains/hydrology/PUBLICATION_POSTURE.md
  - docs/sources/catalog/usgs/3dep-elevation.md
  - docs/sources/catalog/usgs/README.md
  - pipeline_specs/hydrology/ingest_3dep_terrain.yaml
  - contracts/domains/hydrology/
  - schemas/contracts/v1/domains/hydrology/
  - policy/domains/hydrology/
  - policy/sensitivity/hydrology/
  - data/raw/hydrology/
  - data/work/hydrology/
  - data/quarantine/hydrology/
  - data/processed/hydrology/
  - data/catalog/domain/hydrology/
  - data/triplets/hydrology/
  - data/registry/sources/hydrology/
  - data/receipts/pipeline/
  - data/proofs/evidence_bundle/
  - release/candidates/hydrology/
  - release/manifests/hydrology/
tags:
  - kfm
  - pipelines
  - domains
  - hydrology
  - ingest
  - 3dep
  - usgs
  - terrain
  - dem
  - lidar
  - elevation
  - watershed
  - flow-derivative
  - vertical-datum
  - crs
  - evidence
  - policy
  - governance
notes:
  - "This README fills the blank pipelines/domains/hydrology/ingest_3dep_terrain path as a nested executable terrain-ingest sublane."
  - "3DEP terrain ingest logic is executable implementation support only; it does not own USGS source descriptors, source catalog profiles, connector/fetch logic, schemas, policy, lifecycle data, catalog truth, hydrologic truth, or release decisions."
  - "The subdirectory name uses the requested underscore form ingest_3dep_terrain; if repo slug rules prefer hyphenated names, record the path decision with ADR/path-map/rollback notes before moving."
  - "3DEP source hierarchy must be preserved: LAZ point clouds, EPT/COPC delivery, DEMs, and derivative surfaces are separate evidence/support classes."
  - "Vertical datum, horizontal CRS, units, resolution, nodata, derivative method, and source vintage are gate-critical."
  - "Terrain derivatives may support hydrologic context, but they do not become observed hydrology, NFHL, forecast, regulatory decision, or public safety guidance."
  - "Concrete executable behavior, source linkage, schedules, CI coverage, schema paths, release wiring, and public API/map behavior remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hydrology 3DEP Terrain Ingest Pipeline

> Executable Hydrology sublane for normalizing admitted USGS 3DEP terrain inputs and terrain-derived hydrologic support layers into governed work candidates, quarantine records, validation handoffs, receipts, and downstream catalog/release-review packages — without collapsing terrain evidence into observed hydrology, regulatory flood context, modeled hydrograph truth, public safety guidance, or release approval.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-3DEP%20terrain%20hydrology%20ingest-2e7d32)
![authority](https://img.shields.io/badge/authority-executable%20logic-0a7ea4)
![datum](https://img.shields.io/badge/vertical%20datum-gate%20critical-d62728)
![anti-collapse](https://img.shields.io/badge/terrain%20%E2%89%A0%20observed%20hydrology-d62728)
![publication](https://img.shields.io/badge/publication-release%20gated-d62728)
![ci](https://img.shields.io/badge/CI-TODO-lightgrey)

**Status:** Draft  
**Path:** `pipelines/domains/hydrology/ingest_3dep_terrain/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Domain lane:** Hydrology  
**Sublane:** 3DEP terrain ingest / terrain-support normalization  
**Placement posture:** nested executable sublane under `pipelines/domains/hydrology/`; concrete executable behavior remains `PROPOSED / NEEDS VERIFICATION` unless backed by tests and repo evidence  
**Public posture:** no direct publication; terrain-derived output is work/quarantine/validation input only and requires downstream evidence, policy, catalog, release, correction, and rollback closure

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. 3DEP terrain anti-collapse rules](#3-3dep-terrain-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Ingest scope](#6-ingest-scope)
- [7. Lifecycle contract](#7-lifecycle-contract)
- [8. Required gates](#8-required-gates)
- [9. Directory contract](#9-directory-contract)
- [10. Inputs and outputs](#10-inputs-and-outputs)
- [11. Minimal 3DEP terrain ingest candidate record](#11-minimal-3dep-terrain-ingest-candidate-record)
- [12. Tests, fixtures, receipts, and proofs](#12-tests-fixtures-receipts-and-proofs)
- [13. Promotion, publication, correction, and rollback](#13-promotion-publication-correction-and-rollback)
- [14. Definition of done](#14-definition-of-done)
- [15. Open questions](#15-open-questions)

---

## 1. Purpose

`pipelines/domains/hydrology/ingest_3dep_terrain/` is the executable sublane for 3DEP terrain-support normalization inside the Hydrology domain.

It supports candidate processing for:

- admitted USGS 3DEP DEM, elevation, and terrain asset references;
- terrain source hierarchy refs such as LAZ, EPT/COPC, DEM, hillshade, slope, aspect, and uncertainty layers;
- hydrology-support derivatives such as slope, flow direction, flow accumulation, drainage conditioning, terrain masks, watershed-support rasters, and upstream/downstream terrain context;
- terrain artifact manifests with horizontal CRS, vertical datum, geoid model, units, resolution, nodata, and source vintage;
- derivative method receipts and parameter hashes;
- quarantine records for datum mismatch, CRS mismatch, unit ambiguity, nodata drift, derivative-method gaps, unsupported resampling, source-role collapse, or validation failure;
- validation, catalog, triplet, EvidenceBundle, release-review, correction, and rollback handoff packages.

This directory implements or will implement the **how** of terrain-support ingest. It does not fetch USGS data directly, define 3DEP source identity, define Hydrology object meaning, define schemas, encode policy, store lifecycle data, decide release, issue current safety guidance, decide NFHL meaning, or certify hydrologic model results.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable pipeline logic: the **how**. | CONFIRMED root responsibility |
| Why `domains/hydrology/`? | Hydrology is the domain lane used by Hydrology docs and the Hydrology pipeline README. | CONFIRMED documentation pattern; behavior NEEDS VERIFICATION |
| Why `ingest_3dep_terrain/`? | This is a narrow executable sublane for terrain inputs used as hydrology support evidence. | PROPOSED / NEEDS VERIFICATION |
| Is this a connector? | No. Source fetching belongs in `connectors/usgs/` or an accepted source-edge home. This sublane reads admitted lifecycle inputs or fixtures. | CONFIRMED separation |
| Does this own 3DEP source profile? | No. Source profile content lives under `docs/sources/catalog/usgs/3dep-elevation.md` and source descriptors live in registry homes. | CONFIRMED source-doc separation |
| Where do declarative run specs live? | `pipeline_specs/hydrology/ingest_3dep_terrain.yaml` or accepted spec home. | PROPOSED / NEEDS VERIFICATION |
| Can this sublane publish? | No. It may emit work candidates, quarantine records, validation handoffs, and receipts only through governed workflow. | CONFIRMED doctrine posture |

> [!IMPORTANT]
> Terrain ingest is not hydrologic truth, not NFHL, not observed water, not a forecast, not public guidance, and not release approval. It prepares evidence-bound terrain-support candidates for downstream validation and review.

[⬆ Back to top](#top)

---

## 3. 3DEP terrain anti-collapse rules

3DEP terrain ingest must preserve source hierarchy, datum, units, and derivative method.

Disallowed collapses:

```text
LAZ point cloud -> DEM without derivation receipt
EPT/COPC delivery -> immutable source truth
1 m DEM -> coarser DEM without aggregation receipt
hillshade / slope / aspect -> observed terrain measurement
terrain derivative -> observed streamflow
elevation support -> NFHL or regulatory determination
flow accumulation -> mapped stream truth
terrain conditioning -> watershed truth without review
vertical datum A -> vertical datum B without transform receipt
meters -> feet without unit receipt
generated summary -> evidence
ingest receipt -> release approval
```

Required distinctions:

- LAZ, EPT/COPC, DEM, coarser DEM, and derivative products remain separate support classes;
- horizontal CRS, vertical datum, geoid model, units, resolution, nodata, and source vintage are explicit;
- analysis CRS and web-delivery CRS remain separate;
- hydrologic derivatives carry method and parameter receipts;
- terrain-support outputs remain derived context until Hydrology validation, evidence, policy, and release review close;
- downstream catalog/triplet products preserve the terrain-source lineage and do not replace canonical Hydrology records.

[⬆ Back to top](#top)

---

## 4. What belongs here

Files belong here when their primary responsibility is executable Hydrology terrain-support ingest.

Appropriate contents include:

- fixture-only terrain ingest entrypoints;
- admitted 3DEP asset manifest readers;
- DEM, COG, raster, point-cloud, and terrain metadata normalizers;
- vertical datum, geoid model, horizontal CRS, unit, resolution, nodata, and source-vintage validators;
- terrain derivative candidate builders for hydrology support;
- flow direction, flow accumulation, slope, terrain mask, and drainage-support candidate builders;
- derivative method and parameter receipt builders;
- source-role and support-class anti-collapse validators;
- quarantine routing helpers for datum, CRS, unit, nodata, lineage, method, evidence, or schema failures;
- receipt emitters, if not shared;
- handoff helpers for hydrology validation, catalog, and triplet stages;
- thin adapters that read governed lifecycle inputs, not live USGS endpoints.

A good placement test:

> If the code transforms admitted 3DEP terrain lifecycle inputs into Hydrology terrain-support candidates, quarantine records, validation handoffs, receipts, or downstream handoff packages, it may belong here. If it fetches source data, defines schemas, stores lifecycle data, decides public release, or claims hydrologic truth, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| USGS source fetchers / connectors | `connectors/usgs/` or accepted connector home |
| 3DEP source catalog profile | `docs/sources/catalog/usgs/3dep-elevation.md` |
| Source descriptors / source registry entries | `data/registry/sources/usgs/`, `data/registry/sources/hydrology/`, or approved registry home |
| Hydrology architecture and doctrine | `docs/domains/hydrology/...` |
| Spatial Foundation terrain doctrine | `docs/domains/spatial-foundation/...` or accepted spatial docs home |
| Object meaning contracts | `contracts/domains/hydrology/` or accepted contract home |
| JSON Schemas | `schemas/contracts/v1/domains/hydrology/` or accepted schema home |
| Policy, rights, sensitivity, release rules | `policy/...` responsibility roots |
| Declarative run specs | `pipeline_specs/hydrology/...` |
| Fixtures | `fixtures/domains/hydrology/ingest_3dep_terrain/` or accepted fixture home |
| Tests | `tests/pipelines/domains/hydrology/ingest_3dep_terrain/` or accepted test home |
| Raw, work, quarantine, processed, catalog, triplet, or published outputs | `data/...` lifecycle homes |
| Catalog/triplet builders | `pipelines/domains/hydrology/catalog/`, `pipelines/catalog/`, or accepted graph/catalog adapter home |
| Catalog close / release preflight | `pipelines/domains/hydrology/catalog_close/` or release workflow homes |
| Receipts and proofs | `data/receipts/...`, `data/proofs/...` |
| Release decisions and manifests | `release/...` responsibility roots |
| Public API, map code, or terrain tiles | `apps/governed-api/`, `apps/explorer-web/`, `data/published/...`, or release-controlled artifact homes |

[⬆ Back to top](#top)

---

## 6. Ingest scope

| Scope area | Ingest responsibility | Failure behavior |
|---|---|---|
| 3DEP asset identity | Preserve source id, product class, source role, source vintage, and asset refs. | Quarantine if missing. |
| CRS / datum / units | Validate horizontal CRS, vertical datum, geoid, units, and transform refs. | Quarantine on ambiguity or mismatch. |
| Resolution / nodata | Preserve resolution, grid alignment, nodata, overviews, and resampling method. | Quarantine on drift. |
| DEM support | Normalize DEM candidates as modeled derivatives. | Never raw observation truth. |
| Point-cloud support | Preserve LAZ/EPT/COPC source hierarchy. | Quarantine on class collapse. |
| Terrain derivatives | Build derived candidates only with method receipts. | Abstain or quarantine if method support missing. |
| Hydrology use | Prepare support inputs for watershed/reach/topology workflows. | No direct streamflow or NFHL claims. |
| Cross-lane context | Preserve Spatial Foundation and Hydrology ownership boundaries. | Restrict or quarantine if ownership collapses. |

[⬆ Back to top](#top)

---

## 7. Lifecycle contract

Every 3DEP terrain ingest run must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal stance:

1. **Read** approved fixtures, immutable raw captures, work inputs, quarantine inputs in remediation mode, or prior processed terrain-support baselines.
2. **Normalize** into Hydrology terrain-support work candidates with source role, product class, source vintage, CRS, vertical datum, units, resolution, nodata, method refs, evidence refs, policy refs, and receipt refs.
3. **Quarantine** missing source descriptor, unsupported source role, datum mismatch, CRS mismatch, unit ambiguity, nodata drift, unsupported resampling, missing derivative method, evidence gap, schema drift, or validation failure.
4. **Emit receipts** with input refs, source refs, method refs, validation refs, transform refs, output refs, and outcomes.
5. **Support promotion** only by feeding downstream Hydrology validation and review workflows.
6. **Never publish directly.**

Terrain ingest is an early lifecycle transformation. It is not processed-state promotion, catalog closure, release approval, or public artifact creation by itself.

[⬆ Back to top](#top)

---

## 8. Required gates

Every 3DEP terrain ingest run must check or explicitly fail closed on:

1. **Input lifecycle gate** — input is fixture, raw capture, work input, quarantine-remediation input, or accepted baseline.
2. **Source descriptor gate** — source identity, role, cadence/vintage, rights, and sensitivity posture are known.
3. **Source hierarchy gate** — LAZ, EPT/COPC, DEM, coarser DEM, and derivatives remain distinct.
4. **CRS gate** — horizontal CRS is explicit and transformation state is recorded.
5. **Vertical datum gate** — vertical datum, geoid model, and vertical units are explicit.
6. **Unit gate** — meters/feet and derivative units are explicit and never silently mixed.
7. **Resolution/nodata gate** — grid resolution, nodata, overviews, and resampling methods are preserved.
8. **Derivative method gate** — hydrologic terrain derivatives carry method and parameter receipt refs.
9. **Hydrology anti-collapse gate** — terrain outputs do not become observed water, NFHL, forecast, or official guidance.
10. **Evidence gate** — claim-bearing downstream candidates can resolve evidence refs or abstain.
11. **Rights and sensitivity gate** — unresolved rights or restricted context cannot proceed to public-safe handoff.
12. **Schema/contract gate** — candidates match accepted schema and Hydrology semantics.
13. **No-direct-publish gate** — no writes to public UI, public API, catalog store, terrain tiles, published layers, or release manifests as an ingest side effect.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended shape:

```text
pipelines/domains/hydrology/ingest_3dep_terrain/
├── README.md                         # this file
├── INGEST_CONTRACT.md                # PROPOSED: 3DEP terrain ingest contract
├── run_dry_fixture.py                # PROPOSED synthetic/redacted fixture only
├── normalize_3dep_asset.py           # PROPOSED
├── normalize_dem_metadata.py         # PROPOSED
├── normalize_pointcloud_metadata.py  # PROPOSED
├── normalize_terrain_derivative.py   # PROPOSED
├── validate_crs_datum_units.py       # PROPOSED
├── validate_resolution_nodata.py     # PROPOSED
├── validate_source_hierarchy.py      # PROPOSED
├── build_hydrology_support_candidate.py # PROPOSED
├── route_quarantine.py               # PROPOSED
├── emit_receipt.py                   # PROPOSED only if not shared
└── adapters/                         # PROPOSED thin lifecycle adapters, no source fetching
```

Declarative specs should live outside this directory:

```text
pipeline_specs/hydrology/ingest_3dep_terrain.yaml # PROPOSED / NEEDS VERIFICATION
```

Generated outputs must not be written beside the ingest code. Use accepted lifecycle homes under `data/work/hydrology/`, `data/quarantine/hydrology/`, `data/processed/hydrology/`, proof homes under `data/proofs/`, receipt homes under `data/receipts/`, and release homes under `release/`.

[⬆ Back to top](#top)

---

## 10. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Fixture input | `fixtures/domains/hydrology/ingest_3dep_terrain/` or accepted fixture home | Synthetic, generalized, or redacted. |
| Raw 3DEP capture | `data/raw/hydrology/<source_id>/<run_id>/` or accepted USGS raw home | Immutable source-edge capture with descriptor and receipt. |
| Work candidate | `data/work/hydrology/<run_id>/` | Candidate only. |
| Quarantine record | `data/quarantine/hydrology/<reason>/<run_id>/` | Failed, restricted, unresolved, or unsafe material. |
| Terrain-support processed handoff | `data/processed/hydrology/<dataset_id>/<version>/` | Only after downstream validation and promotion gates. |
| Receipt | `data/receipts/pipeline/hydrology/ingest_3dep_terrain/<run_id>.yml` or accepted receipt home | Records input refs, methods, checks, transforms, and outputs. |
| Evidence proof | `data/proofs/evidence_bundle/` or accepted proof home | Required for claim-bearing downstream records. |
| Catalog handoff | `pipelines/domains/hydrology/catalog/` via lifecycle data homes | No direct catalog writes from terrain ingest unless approved by spec. |

[⬆ Back to top](#top)

---

## 11. Minimal 3DEP terrain ingest candidate record

The final schema is not defined here. This example shows the minimum information a 3DEP terrain ingest candidate should preserve.

```yaml
schema_version: kfm.hydrology_3dep_terrain_ingest_candidate.v1
candidate_id: hydrology_3dep_<asset_or_derivative>_<run_id>_<hash>
pipeline_id: domains.hydrology.ingest_3dep_terrain
run_id: run_YYYYMMDDThhmmssZ
status: WORK_CANDIDATE
object_family: <dem_asset|pointcloud_asset|terrain_derivative|flow_direction|flow_accumulation|slope|drainage_support|watershed_support>
source:
  source_id: usgs_3dep
  source_role: <observed_pointcloud|analytic_delivery|modeled_derivative|second_order_derivative|synthetic>
  lifecycle_ref: data/raw/hydrology/usgs_3dep/<run_id>/
  input_hash: sha256:<hash>
  rights_state: needs_review
terrain:
  product_class: <laz|ept|copc|dem_1m|dem_coarser|hillshade|slope|aspect|uncertainty|derived_hydrology_support>
  source_vintage: null
  horizontal_crs: null
  vertical_datum: null
  geoid_model: null
  units_xy: null
  units_z: null
  resolution: null
  nodata: null
method:
  derivative_method: null
  parameter_hash: null
  transform_receipt_ref: null
anti_collapse:
  terrain_is_observed_hydrology: false
  dem_is_pointcloud_truth: false
  nfhl_or_regulatory_claim_created: false
  generated_summary_is_evidence: false
policy:
  outcome: ABSTAIN
  reason_code: DATUM_CRS_SOURCE_ROLE_OR_EVIDENCE_NOT_RESOLVED
evidence:
  evidence_bundle_ref: null
  citation_state: ABSTAIN
outputs:
  candidate_record: data/work/hydrology/run_YYYYMMDDThhmmssZ/3dep_terrain_candidate.yml
  receipt: data/receipts/pipeline/hydrology/ingest_3dep_terrain/run_YYYYMMDDThhmmssZ.yml
rollback:
  required_before_publication: true
```

[⬆ Back to top](#top)

---

## 12. Tests, fixtures, receipts, and proofs

Default execution is **fixture-only, synthetic/generalized/redacted, and no-network** until source activation, terrain spec, evidence, policy, sensitivity, and CI coverage are approved.

Recommended tests:

```text
tests/pipelines/domains/hydrology/ingest_3dep_terrain/
├── test_no_network_dry_run.py             # PROPOSED
├── test_source_descriptor_required.py     # PROPOSED
├── test_source_hierarchy_required.py      # PROPOSED
├── test_laz_not_dem_without_receipt.py    # PROPOSED
├── test_crs_required.py                   # PROPOSED
├── test_vertical_datum_required.py        # PROPOSED
├── test_units_not_silently_mixed.py       # PROPOSED
├── test_resolution_nodata_preserved.py    # PROPOSED
├── test_derivative_method_required.py     # PROPOSED
├── test_terrain_not_observed_hydrology.py # PROPOSED
├── test_nfhl_not_created_from_terrain.py  # PROPOSED
├── test_evidence_gap_abstains.py          # PROPOSED
├── test_receipt_hashes.py                 # PROPOSED
└── test_no_direct_publish.py              # PROPOSED
```

A dry run should prove fixtures load without network access, source hierarchy is explicit, CRS/datum/units/resolution/nodata checks run, terrain derivatives require method receipts, terrain does not become observed hydrology or NFHL, EvidenceBundle gaps produce abstention, receipts are deterministic, and no run writes directly to public UI, public API, catalog store, terrain tiles, published layers, or release manifests.

[⬆ Back to top](#top)

---

## 13. Promotion, publication, correction, and rollback

3DEP terrain ingest may prepare work candidates and quarantine records. It does not publish.

Required chain:

```text
admitted 3DEP source capture
  -> terrain-support ingest candidate
  -> validation report
  -> policy decision
  -> EvidenceBundle closure
  -> processed Hydrology terrain-support record
  -> catalog / triplet candidate
  -> release candidate
  -> ReleaseManifest
  -> RollbackCard
  -> public-safe artifact
```

Correction and rollback posture:

- denied, abstained, errored, restricted, stale, conflicted, and quarantined terrain ingest runs remain auditable;
- ingest receipts preserve source refs, source hierarchy, CRS/datum/unit refs, method refs, rule ids, and outcomes;
- processed versions are produced by governed promotion, not hidden overwrite;
- downstream artifacts are invalidated if source refs, terrain refs, datum refs, method refs, evidence refs, source-role refs, or policy refs drift;
- public artifact rollback is owned by `release/`, not by this directory.

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- fills the blank `pipelines/domains/hydrology/ingest_3dep_terrain/README.md` file;
- identifies this directory as a nested executable Hydrology terrain-ingest sublane;
- prevents connector, source-profile, schema, contract, policy, fixture, test, data, proof, catalog, and release authority from being placed here;
- preserves 3DEP source hierarchy, CRS, vertical datum, units, resolution, nodata, method receipts, evidence, policy, lifecycle, catalog/triplet, release, correction, and rollback boundaries;
- blocks terrain-as-observed-hydrology, terrain-as-NFHL, DEM-as-point-cloud-truth, datum/unit mixing, generated-summary-as-evidence, and direct catalog/release writes;
- gives maintainers a fixture-first, fail-closed expansion pattern.

Future executable work in this sublane is done only when it has source-descriptor coverage, synthetic/generalized/redacted no-network fixtures, schema-backed candidates, contract conformance, source-hierarchy/datum/CRS/evidence/policy/no-direct-publish tests, deterministic receipts, CI coverage, steward-review handoff, and release/correction/rollback documentation.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `HYDRO-3DEP-001` | Should this sublane remain Hydrology-specific or move to Spatial Foundation with Hydrology adapters? | NEEDS VERIFICATION / ADR |
| `HYDRO-3DEP-002` | Which source-edge job owns USGS 3DEP retrieval before this sublane reads lifecycle inputs? | NEEDS VERIFICATION |
| `HYDRO-3DEP-003` | Which first-wave products are approved for fixture-only dry runs: DEM, LAZ metadata, COG, slope, flow direction, flow accumulation, or terrain masks? | NEEDS VERIFICATION |
| `HYDRO-3DEP-004` | Which schema owns terrain-support candidates and terrain artifact manifests? | NEEDS VERIFICATION |
| `HYDRO-3DEP-005` | Which CI job owns 3DEP terrain ingest invariant tests? | UNKNOWN |
| `HYDRO-3DEP-006` | Should catalog handoff be forbidden as an ingest side effect, or allowed only through an explicit chained spec? | NEEDS VERIFICATION |
| `HYDRO-3DEP-007` | Which receipt type owns terrain derivative methods, datum transforms, and hydrologic terrain-support transforms? | PROPOSED / NEEDS ADR |

---

## Maintainer note

Start with synthetic/generalized fixture-only dry runs and negative tests. Do not add live USGS fetching, direct catalog writes, public terrain-tile writes, public map layer writes, release-manifest writes, current safety guidance, or direct API payload generation until source roles, CRS/datum/units, method receipts, evidence closure, public-safe transforms, release review, and rollback are proven.
