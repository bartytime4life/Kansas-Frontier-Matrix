<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-habitat-land-cover-readme
title: Habitat Land Cover Pipeline README
type: readme
version: v0.1
status: draft
owners:
  - <habitat-pipeline-owner>
  - <habitat-domain-steward>
  - <land-cover-steward>
  - <source-steward>
  - <evidence-steward>
  - <policy-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: pipelines/domains/habitat/land_cover/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipelines/domains/README.md
  - pipelines/domains/habitat/README.md
  - docs/domains/habitat/README.md
  - docs/domains/habitat/sublanes/land_cover/README.md
  - docs/sources/catalog/usgs/nlcd.md
  - docs/sources/catalog/landfire/landfire.md
  - pipeline_specs/habitat/land_cover.yaml
  - contracts/domains/habitat/
  - schemas/contracts/v1/domains/habitat/
  - policy/domains/habitat/
  - policy/sensitivity/habitat/
  - data/raw/habitat/
  - data/work/habitat/
  - data/quarantine/habitat/
  - data/processed/habitat/
  - data/catalog/domain/habitat/
  - data/triplets/habitat/
  - data/published/layers/habitat/
  - data/registry/sources/habitat/
  - data/receipts/pipeline/
  - data/proofs/evidence_bundle/
  - release/candidates/habitat/
  - release/manifests/habitat/
tags:
  - kfm
  - pipelines
  - domains
  - habitat
  - land-cover
  - land-cover-observation
  - native-classification
  - advisory-crosswalk
  - nlcd
  - cdl
  - landfire
  - gap
  - nwi
  - source-role
  - evidence
  - policy
  - governance
notes:
  - "This README fills the blank pipelines/domains/habitat/land_cover path as a nested executable Habitat land-cover sublane."
  - "Land-cover pipeline logic is executable implementation support only; it does not own source descriptors, source catalog profiles, connectors, schemas, policy, lifecycle data, catalog truth, species or plant truth, or release decisions."
  - "LandCoverObservation is a Habitat-owned object family, but native source classification must be preserved and crosswalks remain advisory, lossy, and non-authoritative."
  - "NLCD is modeled thematic land-cover; it must not be treated as a direct measurement."
  - "Land-cover context may inform HabitatPatch, suitability, condition, and connectivity workflows, but it does not become occurrence truth, regulatory designation, crop truth, soil truth, hydrology truth, hazard truth, or release approval."
  - "Concrete executable behavior, source activation, schedules, CI coverage, schema paths, release wiring, and public API/map behavior remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Habitat Land Cover Pipeline

> Executable Habitat sublane for transforming admitted land-cover source captures and fixture inputs into governed `LandCoverObservation` candidates, quarantine records, normalized records, catalog/triplet handoffs, receipts, and release-review packages — while preserving native classifications, source roles, evidence, rights, time, sensitivity posture, and public-safe release boundaries.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-habitat%20land%20cover-2e7d32)
![authority](https://img.shields.io/badge/authority-executable%20logic-0a7ea4)
![crosswalk](https://img.shields.io/badge/crosswalk-advisory%20only-d62728)
![publication](https://img.shields.io/badge/publication-release%20gated-d62728)
![ci](https://img.shields.io/badge/CI-TODO-lightgrey)

**Status:** Draft  
**Path:** `pipelines/domains/habitat/land_cover/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Domain lane:** Habitat  
**Sublane:** Land cover / `LandCoverObservation` processing  
**Placement posture:** nested executable sublane under `pipelines/domains/habitat/`; concrete executable behavior remains `PROPOSED / NEEDS VERIFICATION` unless backed by tests and repo evidence  
**Public posture:** no direct publication; public-safe land-cover outputs require lifecycle, EvidenceBundle, source-role, sensitivity, policy, catalog/triplet, release, correction, and rollback closure

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Land-cover anti-collapse rules](#3-land-cover-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Land-cover scope](#6-land-cover-scope)
- [7. Lifecycle contract](#7-lifecycle-contract)
- [8. Required gates](#8-required-gates)
- [9. Directory contract](#9-directory-contract)
- [10. Inputs and outputs](#10-inputs-and-outputs)
- [11. Minimal land-cover candidate record](#11-minimal-land-cover-candidate-record)
- [12. Tests, fixtures, receipts, and proofs](#12-tests-fixtures-receipts-and-proofs)
- [13. Promotion, publication, correction, and rollback](#13-promotion-publication-correction-and-rollback)
- [14. Definition of done](#14-definition-of-done)
- [15. Open questions](#15-open-questions)

---

## 1. Purpose

`pipelines/domains/habitat/land_cover/` is the executable sublane for Habitat land-cover processing.

It supports candidate processing for:

- `LandCoverObservation` records;
- NLCD, CDL, LANDFIRE, GAP, NWI, and other admitted land-cover source families;
- native class-code and class-label preservation;
- class-map version preservation per source epoch or release;
- advisory crosswalk attachment without replacing native source classes;
- raster, vector, tile-index, and summary metadata candidates where admitted;
- HabitatPatch, habitat quality, suitability, condition, connectivity, restoration, and stewardship-context handoffs;
- quarantine records for missing source descriptor, missing class map, source-role collapse, crosswalk overwrite, time ambiguity, geometry/CRS ambiguity, rights uncertainty, sensitivity failure, schema drift, or validation failure;
- validation, catalog, triplet, EvidenceBundle, release-review, correction, and rollback handoff packages.

This directory implements or will implement the **how** of Habitat land-cover processing. It does not fetch source data, define Habitat object meaning, define schemas, encode policy, store lifecycle data, decide release, own species or plant occurrence truth, own crop truth, own wetland regulatory truth, own soil/hydrology/hazards truth, or certify public map products.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable pipeline logic: the **how**. | CONFIRMED root responsibility |
| Why `domains/habitat/`? | Habitat is the domain lane under the domain-pipeline umbrella. | CONFIRMED path responsibility pattern; behavior NEEDS VERIFICATION |
| Why `land_cover/`? | This is a narrow executable sublane for Habitat-owned `LandCoverObservation` processing. | PROPOSED / NEEDS VERIFICATION |
| Is this a connector? | No. Source fetching belongs in `connectors/<source>` or an accepted source-edge home. | CONFIRMED separation |
| Does this own the land-cover doctrine? | No. Human-facing doctrine remains in `docs/domains/habitat/` and `docs/domains/habitat/sublanes/land_cover/`. | CONFIRMED doc separation |
| Does this own source profiles? | No. Source profiles such as NLCD and LANDFIRE remain under `docs/sources/catalog/...`; SourceDescriptors remain in registry homes. | CONFIRMED source separation |
| Can this sublane publish? | No. It may prepare candidates and release handoffs only through governed workflow. | CONFIRMED doctrine posture |

> [!IMPORTANT]
> Land-cover pipeline output is not public release, not a species occurrence, not a plant record, not a regulatory designation, and not a single unified authority class. Each source's native classification is preserved; crosswalks are advisory context.

[⬆ Back to top](#top)

---

## 3. Land-cover anti-collapse rules

Land-cover processing must preserve source role, native class semantics, time, and release state.

Disallowed collapses:

```text
native class -> common class without preserving native class
crosswalk class -> authoritative source class
NLCD modeled pixel -> direct field measurement
CDL crop context -> Agriculture crop truth
LANDFIRE fuel context -> current hazard decision
NWI wetland class -> hydrology root truth
land-cover context -> occurrence truth
HabitatPatch -> LandCoverObservation
modeled suitability -> observed land cover
source epoch A -> source epoch B without class-map reconciliation
generated summary -> evidence
pipeline run -> release approval
```

Required distinctions:

- source identity, source role, source epoch, class-map version, native class code, and native class label are explicit;
- crosswalks are lossy, advisory, and separately versioned;
- modeled, observed, regulatory, aggregate, administrative, candidate, and synthetic records remain distinct;
- land-cover context can support habitat reasoning but cannot overwrite Fauna, Flora, Agriculture, Hydrology, Soil, Hazards, or release authority;
- publication requires public-safe transforms, review, correction path, and rollback target.

[⬆ Back to top](#top)

---

## 4. What belongs here

Files belong here when their primary responsibility is executable Habitat land-cover processing.

Appropriate contents include:

- fixture-only dry-run entrypoints;
- land-cover source-candidate normalizers;
- native class-code and class-label preservation helpers;
- class-map version validators;
- advisory crosswalk attachment helpers;
- class-map reconciliation validators for cross-release comparisons;
- raster metadata, tiling/index, geometry, CRS, nodata, and resolution validators;
- HabitatPatch and suitability handoff candidate builders that preserve source role;
- policy/sensitivity preflight helpers for controlled ecology joins;
- quarantine routing helpers for missing source descriptor, rights uncertainty, class-map gaps, crosswalk misuse, source-role collapse, evidence gaps, or schema failures;
- receipt emitters, if not shared;
- handoff helpers for validation, catalog, triplet, and release workflow.

A good placement test:

> If the code transforms admitted land-cover lifecycle inputs into Habitat `LandCoverObservation` candidates, quarantine records, validation handoffs, receipts, or downstream handoff packages, it may belong here. If it fetches source data, defines schemas, stores lifecycle data, decides policy, owns source profiles, writes catalog records directly, or approves release, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Source fetchers / connectors | `connectors/<source>` or accepted connector home |
| Source catalog profiles | `docs/sources/catalog/...` |
| Source descriptors / source registry entries | `data/registry/sources/habitat/`, `data/registry/sources/usgs/`, `data/registry/sources/mrlc/`, or approved registry home |
| Habitat doctrine and object meaning | `docs/domains/habitat/...`, `contracts/domains/habitat/` |
| JSON Schemas | `schemas/contracts/v1/domains/habitat/` or accepted schema home |
| Policy, rights, sensitivity, release rules | `policy/...` responsibility roots |
| Declarative run specs | `pipeline_specs/habitat/...` |
| Fixtures | `fixtures/domains/habitat/land_cover/` or accepted fixture home |
| Tests | `tests/pipelines/domains/habitat/land_cover/` or accepted test home |
| Raw, work, quarantine, processed, catalog, triplet, or published outputs | `data/...` lifecycle homes |
| Fauna/Flora occurrence truth | `docs/domains/fauna/`, `docs/domains/flora/`, and their corresponding responsibility roots |
| Agriculture crop truth | `docs/domains/agriculture/` and Agriculture responsibility roots |
| Hydrology, soil, hazards, or stewardship truth | Owning domain roots |
| Release decisions and manifests | `release/...` responsibility roots |
| Public API or map code | `apps/governed-api/`, `apps/explorer-web/`, packages |

[⬆ Back to top](#top)

---

## 6. Land-cover scope

| Scope area | Pipeline responsibility | Failure behavior |
|---|---|---|
| Source identity | Preserve source id, descriptor refs, rights, source role, and source epoch. | Quarantine if missing. |
| Native class | Preserve native class code, label, class-map version, and source vocabulary. | Quarantine on loss. |
| Crosswalk | Attach advisory mappings without replacing source classes. | Deny or quarantine if authoritative overwrite is attempted. |
| Geometry/raster | Preserve CRS, resolution, nodata, grid/tile refs, and source vintage. | Quarantine on mismatch. |
| Time | Preserve source, observed/derived, valid, retrieval, processing, release, and correction times. | Quarantine on collapse. |
| Habitat handoff | Prepare evidence-bound context for HabitatPatch, suitability, condition, connectivity, and restoration workflows. | No direct truth transfer. |
| Controlled joins | Preserve policy and review outcomes before context joins. | Fail closed if unresolved. |
| Release handoff | Prepare public-safe candidates only after evidence and policy closure. | No direct publication. |

[⬆ Back to top](#top)

---

## 7. Lifecycle contract

Every Habitat land-cover run must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal stance:

1. **Read** approved fixtures, immutable raw captures, work inputs, quarantine inputs in remediation mode, or prior processed land-cover baselines.
2. **Normalize** into Habitat work candidates with source role, native class, class-map version, source epoch, geometry/raster refs, time refs, evidence refs, policy refs, and receipt refs.
3. **Quarantine** missing source descriptor, missing native class, missing class-map version, source-role collapse, crosswalk overwrite, rights failure, sensitivity failure, evidence gap, schema drift, or validation failure.
4. **Emit receipts** with input refs, source refs, class-map refs, crosswalk refs, transform refs, validation refs, output refs, and outcomes.
5. **Support promotion** only by feeding downstream validation and review workflows.
6. **Never publish directly.**

Land-cover processing is a lifecycle transformation. It is not catalog closure, release approval, or public artifact creation by itself.

[⬆ Back to top](#top)

---

## 8. Required gates

Every Habitat land-cover run must check or explicitly fail closed on:

1. **Input lifecycle gate** — input is fixture, raw capture, work input, quarantine-remediation input, or accepted baseline.
2. **Source descriptor gate** — source identity, role, rights, citation, cadence/vintage, and sensitivity posture are known.
3. **Native-class gate** — native class code, label, and class-map version are preserved.
4. **Crosswalk gate** — crosswalk is advisory, versioned, lossy, and never authoritative.
5. **Source-role gate** — modeled, observed, regulatory, aggregate, administrative, candidate, and synthetic records remain distinct.
6. **Raster/geometry gate** — CRS, resolution, nodata, grid/tile refs, geometry refs, and source vintage are explicit where applicable.
7. **Temporal gate** — source time, observed/derived time, valid time, retrieval time, processing time, release time, and correction time remain distinct.
8. **Evidence gate** — claim-bearing downstream candidates can resolve EvidenceBundle support or abstain.
9. **Policy/sensitivity gate** — unresolved rights, controlled joins, exact exposure risk, or public-safe transform gaps fail closed.
10. **Schema/contract gate** — candidates match accepted Habitat schema and `LandCoverObservation` semantics.
11. **Correction/rollback gate** — release-facing handoff includes correction path and rollback target expectations.
12. **No-direct-publish gate** — no writes to public UI, public API, published layers, or release manifests as a pipeline side effect.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended shape:

```text
pipelines/domains/habitat/land_cover/
├── README.md                         # this file
├── LAND_COVER_PIPELINE_CONTRACT.md   # PROPOSED: land-cover execution contract
├── run_dry_fixture.py                # PROPOSED synthetic/generalized fixture only
├── normalize_land_cover_candidate.py # PROPOSED
├── preserve_native_classification.py # PROPOSED
├── attach_advisory_crosswalk.py      # PROPOSED
├── validate_class_map_version.py     # PROPOSED
├── validate_source_role.py           # PROPOSED
├── validate_raster_geometry.py       # PROPOSED
├── validate_policy_public_safe.py    # PROPOSED
├── route_quarantine.py               # PROPOSED
├── emit_receipt.py                   # PROPOSED only if not shared
└── adapters/                         # PROPOSED thin lifecycle adapters, no source fetching
```

Declarative specs should live outside this directory:

```text
pipeline_specs/habitat/land_cover.yaml # PROPOSED / NEEDS VERIFICATION
```

Generated outputs must not be written beside this code. Use accepted lifecycle homes under `data/work/habitat/`, `data/quarantine/habitat/`, `data/processed/habitat/`, `data/catalog/domain/habitat/`, `data/triplets/habitat/`, `data/published/layers/habitat/`, proof homes under `data/proofs/`, receipt homes under `data/receipts/`, and release homes under `release/`.

[⬆ Back to top](#top)

---

## 10. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Fixture input | `fixtures/domains/habitat/land_cover/` or accepted fixture home | Synthetic, generalized, or redacted. |
| Raw source capture | `data/raw/habitat/<source_id>/<run_id>/` | Immutable source-edge capture with descriptor and receipt. |
| Work candidate | `data/work/habitat/<run_id>/` | Candidate only. |
| Quarantine record | `data/quarantine/habitat/<reason>/<run_id>/` | Failed, restricted, unresolved, or unsafe material. |
| Processed land-cover record | `data/processed/habitat/<dataset_id>/<version>/` | Only after validation and governed promotion. |
| Catalog/triplet handoff | `data/catalog/domain/habitat/`, `data/triplets/habitat/` | Projection only; not publication. |
| Receipt | `data/receipts/pipeline/habitat/land_cover/<run_id>.yml` or accepted receipt home | Records inputs, class maps, crosswalks, checks, outputs. |
| Evidence proof | `data/proofs/evidence_bundle/` or accepted proof home | Required for claim-bearing records. |
| Release handoff | `release/candidates/habitat/` | Reviewable, release-gated output only. |

[⬆ Back to top](#top)

---

## 11. Minimal land-cover candidate record

The final schema is not defined here. This example shows the minimum information a Habitat land-cover candidate should preserve.

```yaml
schema_version: kfm.habitat_land_cover_candidate.v1
candidate_id: habitat_land_cover_<source_id>_<epoch>_<tile_or_geom>_<hash>
pipeline_id: domains.habitat.land_cover
run_id: run_YYYYMMDDThhmmssZ
status: WORK_CANDIDATE
object_family: LandCoverObservation
source:
  source_id: <source_id>
  source_role: <observed|modeled|regulatory|aggregate|administrative|candidate|synthetic>
  lifecycle_ref: data/raw/habitat/<source_id>/<run_id>/
  input_hash: sha256:<hash>
  rights_state: needs_review
classification:
  native_class_code: null
  native_class_label: null
  native_class_map_version: null
  advisory_crosswalk_refs: []
  crosswalk_is_authoritative: false
spatial:
  raster_ref: null
  vector_ref: null
  crs: null
  resolution: null
  nodata: null
time:
  source_epoch: null
  valid_start: null
  valid_end: null
  retrieved_at: null
  processed_at: YYYY-MM-DDThh:mm:ssZ
policy:
  outcome: ABSTAIN
  reason_code: SOURCE_DESCRIPTOR_CLASS_MAP_POLICY_OR_EVIDENCE_NOT_RESOLVED
evidence:
  evidence_bundle_ref: null
  citation_state: ABSTAIN
anti_collapse:
  native_class_replaced_by_crosswalk: false
  land_cover_is_occurrence_truth: false
  modeled_product_is_observation: false
  generated_summary_is_evidence: false
outputs:
  candidate_record: data/work/habitat/run_YYYYMMDDThhmmssZ/land_cover_candidate.yml
  receipt: data/receipts/pipeline/habitat/land_cover/run_YYYYMMDDThhmmssZ.yml
rollback:
  required_before_publication: true
```

[⬆ Back to top](#top)

---

## 12. Tests, fixtures, receipts, and proofs

Default execution is **fixture-only, synthetic/generalized/redacted, and no-network** until source activation, land-cover spec, evidence, policy, sensitivity, and CI coverage are approved.

Recommended tests:

```text
tests/pipelines/domains/habitat/land_cover/
├── test_no_network_dry_run.py              # PROPOSED
├── test_source_descriptor_required.py      # PROPOSED
├── test_native_classification_preserved.py # PROPOSED
├── test_crosswalk_advisory_only.py         # PROPOSED
├── test_class_map_version_required.py      # PROPOSED
├── test_source_role_preserved.py           # PROPOSED
├── test_nlcd_not_field_measurement.py      # PROPOSED
├── test_no_occurrence_truth_claim.py       # PROPOSED
├── test_raster_geometry_required.py        # PROPOSED
├── test_policy_public_safe_required.py     # PROPOSED
├── test_evidence_gap_abstains.py           # PROPOSED
├── test_quarantine_on_schema_failure.py    # PROPOSED
├── test_receipt_hashes.py                  # PROPOSED
└── test_no_direct_publish.py               # PROPOSED
```

A dry run should prove fixtures load without network access, source descriptors are required, native classification is preserved, crosswalks remain advisory, class-map versions are tracked, controlled joins fail closed, receipts are deterministic, and no run writes directly to public UI, public API, catalog store, published layers, or release manifests.

[⬆ Back to top](#top)

---

## 13. Promotion, publication, correction, and rollback

Habitat land-cover pipelines may prepare candidates and handoff packages. They do not publish.

Required chain:

```text
admitted land-cover source capture
  -> land-cover work candidate
  -> validation report
  -> policy decision
  -> EvidenceBundle closure
  -> processed LandCoverObservation
  -> catalog / triplet candidate
  -> release candidate
  -> ReleaseManifest
  -> RollbackCard
  -> public-safe artifact
```

Correction and rollback posture:

- denied, abstained, errored, restricted, stale, conflicted, and quarantined land-cover runs remain auditable;
- receipts preserve source refs, native class refs, class-map refs, crosswalk refs, transform refs, evidence refs, source-role refs, policy outcomes, and failure reasons;
- processed versions are produced by governed promotion, not hidden overwrite;
- downstream artifacts are invalidated if source refs, class-map refs, crosswalk refs, EvidenceBundle refs, policy refs, source-role refs, correction refs, or rollback refs drift;
- release rollback is owned by `release/`, not by this directory.

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- fills the blank `pipelines/domains/habitat/land_cover/README.md` file;
- identifies this directory as a nested executable Habitat land-cover sublane;
- prevents connector, source-profile, schema, contract, policy, fixture, test, data, proof, catalog, graph, public API, UI, and release authority from being placed here;
- preserves `LandCoverObservation`, source roles, native classifications, class-map versions, advisory crosswalks, time, geometry/raster refs, evidence, policy, lifecycle, catalog/triplet, release, correction, and rollback boundaries;
- blocks crosswalk-as-authority, modeled-pixel-as-field-measurement, land-cover-as-occurrence-truth, generated-summary-as-evidence, and direct publication writes;
- gives maintainers a fixture-first, fail-closed expansion pattern.

Future executable work in this sublane is done only when it has source-descriptor coverage, synthetic/generalized/redacted no-network fixtures, schema-backed candidates, contract conformance, native-class/crosswalk/source-role/evidence/policy/no-direct-publish tests, deterministic receipts, CI coverage, steward-review handoff, and release/correction/rollback documentation.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `HAB-LC-001` | Should land-cover execution remain one sublane, or split into NLCD, CDL, LANDFIRE, GAP, and NWI source-specific sublanes? | NEEDS VERIFICATION / ADR |
| `HAB-LC-002` | Which source-edge job owns each land-cover retrieval before this sublane reads lifecycle inputs? | NEEDS VERIFICATION |
| `HAB-LC-003` | Which schema owns `LandCoverObservation`, class-map versions, advisory crosswalks, and quarantine reasons? | NEEDS VERIFICATION |
| `HAB-LC-004` | Which first-wave source is approved for fixture-only dry runs: NLCD, CDL, LANDFIRE, GAP, NWI, or a synthetic class map? | NEEDS VERIFICATION |
| `HAB-LC-005` | Which CI job owns Habitat land-cover invariant tests? | UNKNOWN |
| `HAB-LC-006` | Where should shared crosswalk tables live so this executable lane does not become classification authority? | NEEDS VERIFICATION / ADR |
| `HAB-LC-007` | What public-safe precision, class aggregation, and caveat levels are allowed for released habitat land-cover layers? | NEEDS VERIFICATION |

---

## Maintainer note

Start with synthetic/generalized fixture-only dry runs and negative tests. Do not add live source fetching, source-profile editing, schema authority, policy authority, direct catalog writes, public layer writes, release-manifest writes, or generated class summaries until source roles, native class preservation, advisory crosswalk handling, EvidenceBundle closure, public-safe transforms, release review, and rollback are proven.
