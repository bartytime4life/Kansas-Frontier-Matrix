<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-soil-readme
title: Soil Domain Pipeline README
type: readme
version: v0.1
status: draft
owners:
  - <soil-pipeline-owner>
  - <soil-domain-steward>
  - <source-steward>
  - <evidence-steward>
  - <policy-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: pipelines/domains/soil/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipelines/domains/README.md
  - docs/domains/soil/README.md
  - docs/domains/soil/ARCHITECTURE.md
  - docs/domains/soil/DATA_LIFECYCLE.md
  - docs/domains/soil/CANONICAL_PATHS.md
  - docs/runbooks/soil/PROMOTION_RUNBOOK.md
  - docs/sources/catalog/nrcs/ssurgo.md
  - docs/sources/catalog/nrcs/gssurgo.md
  - docs/sources/catalog/nrcs/soil-data-access.md
  - docs/sources/catalog/nrcs/scan-soil-climate.md
  - docs/sources/catalog/isric/README.md
  - pipeline_specs/soil/
  - contracts/domains/soil/
  - schemas/contracts/v1/domains/soil/
  - policy/domains/soil/
  - policy/sensitivity/soil/
  - data/raw/soil/
  - data/work/soil/
  - data/quarantine/soil/
  - data/processed/soil/
  - data/catalog/domain/soil/
  - data/triplets/soil/
  - data/published/layers/soil/
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
  - ssurgo
  - gssurgo
  - gnatsgo
  - soil-data-access
  - soil-moisture
  - pedon
  - horizon
  - hydrologic-soil-group
  - support-type-separation
  - evidence
  - policy
  - governance
notes:
  - "This README replaces the greenfield scaffold for pipelines/domains/soil."
  - "Soil pipeline logic is executable implementation support only; it does not own object meaning, schemas, source descriptors, policy, lifecycle data, catalog truth, interpretation authority, or release decisions."
  - "Support-type separation is mandatory: static survey, gridded derivative, station reading, satellite grid, pedon evidence, and interpretation cannot masquerade as one surface."
  - "Field-specific, owner-specific, unpublished, proprietary, private-network, cross-lane, or insufficiently evidenced soil products fail closed by default."
  - "Concrete executable behavior, source activation, schedules, CI coverage, schema paths, release wiring, and public API/map behavior remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Soil Domain Pipeline

> Executable Soil-domain pipeline lane for transforming admitted soil-survey, gridded-soil, horizon, component, pedon, hydrologic-soil-group, soil-moisture, erosion-context, and suitability source material into governed candidates, quarantine records, processed records, catalog/triplet handoffs, receipts, and release-review packages — without collapsing support types, evidence roles, source vintages, policy state, or release state.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-soil%20domain%20pipeline-2e7d32)
![authority](https://img.shields.io/badge/authority-executable%20logic-0a7ea4)
![support](https://img.shields.io/badge/support--type-required-d62728)
![publication](https://img.shields.io/badge/publication-release%20gated-d62728)
![ci](https://img.shields.io/badge/CI-TODO-lightgrey)

**Status:** Draft  
**Path:** `pipelines/domains/soil/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Domain lane:** Soil  
**Placement posture:** soil child lane under `pipelines/domains/`; concrete executable behavior remains `PROPOSED / NEEDS VERIFICATION` unless backed by tests and repo evidence  
**Public posture:** no direct publication; public output requires lifecycle, EvidenceBundle, source-role, support-type tag, rights, sensitivity, policy, catalog/triplet, release, correction, and rollback closure

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Support-type separation](#3-support-type-separation)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Pipeline scope](#6-pipeline-scope)
- [7. Source-family posture](#7-source-family-posture)
- [8. Lifecycle contract](#8-lifecycle-contract)
- [9. Required gates](#9-required-gates)
- [10. Sensitivity, support-type, and public-safe posture](#10-sensitivity-support-type-and-public-safe-posture)
- [11. Directory contract](#11-directory-contract)
- [12. Inputs and outputs](#12-inputs-and-outputs)
- [13. Minimal pipeline candidate record](#13-minimal-pipeline-candidate-record)
- [14. Dry-run, tests, fixtures, receipts, and proofs](#14-dry-run-tests-fixtures-receipts-and-proofs)
- [15. Promotion, publication, correction, and rollback](#15-promotion-publication-correction-and-rollback)
- [16. Definition of done](#16-definition-of-done)
- [17. Open questions](#17-open-questions)

---

## 1. Purpose

`pipelines/domains/soil/` is the executable pipeline lane for Soil-domain transformations.

It supports candidate processing for:

- soil map units, components, horizons, and component-horizon joins;
- soil properties, hydrologic soil group, and survey-derived interpretations;
- pedon and soil-profile evidence;
- station, satellite, and gridded soil-moisture observations;
- erosion context and suitability ratings;
- source-vintage and time-caveat records;
- public-safe soil map and API products after evidence, policy, and release review;
- catalog, graph, Evidence Drawer, Focus Mode, and correction/rollback handoff packages.

This directory implements or will implement the **how** of Soil processing. It does not define object meaning, schemas, policy, source descriptors, crop/yield truth, hydrology truth, geology truth, habitat truth, lifecycle storage, catalog truth, or release approval.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable pipeline logic: the **how**. | CONFIRMED root responsibility |
| Why `domains/soil/`? | Soil architecture identifies `pipelines/domains/soil/` as the executable pipeline segment. | CONFIRMED documentation pattern; executable behavior NEEDS VERIFICATION |
| Where do declarative specs live? | `pipeline_specs/soil/` or accepted spec home. | PROPOSED / NEEDS VERIFICATION |
| Where do source fetchers live? | `connectors/<soil-source>`, not here. | CONFIRMED separation |
| Where do schemas live? | `schemas/contracts/v1/domains/soil/` or accepted schema home. | PROPOSED / NEEDS VERIFICATION |
| Where do contracts live? | `contracts/domains/soil/` or accepted contract home. | PROPOSED / NEEDS VERIFICATION |
| Where does policy live? | `policy/domains/soil/`, sensitivity policy, rights policy, and release policy roots as applicable. | PROPOSED / NEEDS VERIFICATION |
| Where do outputs live? | Lifecycle homes under `data/`, not beside pipeline code. | CONFIRMED lifecycle posture |
| Can this lane publish? | No. It may prepare candidates and release handoffs only through governed workflow. | CONFIRMED doctrine posture |

> [!IMPORTANT]
> Soil pipeline code is subordinate to source descriptors, source roles, rights, support-type tags, EvidenceBundle closure, sensitivity transforms, policy decisions, release manifests, correction notices, and rollback cards. A successful run is not public release.

[⬆ Back to top](#top)

---

## 3. Support-type separation

Support-type separation is the soil-specific invariant.

The pipeline must keep these categories distinct:

- `authoritative_static_soil` — SSURGO / SDA-style survey evidence;
- `gridded_derivative_soil` — gSSURGO, gNATSGO, SoilGrids, and similar grids;
- `station_soil_moisture` — station observations such as Mesonet, SCAN, or USCRN where admitted;
- `satellite_soil_moisture` — satellite-grid observations such as SMAP where admitted;
- `pedon_evidence` — profile-level observations and descriptions;
- `interpretation` — erosion risk, suitability rating, hydrologic interpretation, and other derived products.

Disallowed collapses:

```text
survey polygon -> gridded derivative truth
station reading -> countywide surface
satellite grid -> station observation
interpretation -> measured property
SoilGrid context -> SSURGO authority
generated summary -> evidence
```

Any soil candidate without support-type classification must abstain, deny, or quarantine rather than silently proceeding.

[⬆ Back to top](#top)

---

## 4. What belongs here

Files belong here when their primary responsibility is executable Soil-domain processing.

Appropriate contents include:

- fixture-only dry-run entrypoints for Soil pipeline behavior;
- soil map unit, component, horizon, and component-horizon join normalizers;
- MUKEY / COKEY / CHKEY lineage helpers;
- soil property, hydrologic soil group, and interpretation candidate builders;
- pedon and soil profile normalizers;
- soil-moisture observation normalizers;
- support-type separation validators;
- unit, depth, horizon, time-caveat, and source-vintage validators;
- public-safe transform helpers, if not centralized elsewhere;
- quarantine routing helpers for rights, source-role, support-type, time, unit, lineage, sensitivity, or validation failures;
- catalog/triplet handoff helpers, if not centralized in `pipelines/catalog/`;
- receipt emitters, if not shared;
- thin adapters that read governed lifecycle inputs, not live source systems.

A good placement test:

> If the code transforms Soil lifecycle inputs into candidates, processed records, restricted catalog/triplet handoffs, receipts, or review handoffs, it may belong here. If it fetches source data, defines meaning, defines schema, encodes policy, stores lifecycle data, approves release, or makes crop, water, geology, or habitat truth claims, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Source fetchers / connectors | `connectors/<soil-source>` |
| Source catalog profiles | `docs/sources/catalog/...` |
| Source descriptors / source registry entries | `data/registry/sources/soil/` or approved registry home |
| Soil architecture and doctrine | `docs/domains/soil/...` |
| Object meaning contracts | `contracts/domains/soil/...` |
| JSON Schemas | `schemas/contracts/v1/domains/soil/...` |
| Policy bundles and release rules | `policy/domains/soil/`, sensitivity, rights, and release policy roots |
| Declarative run specs | `pipeline_specs/soil/...` |
| Fixtures | `fixtures/domains/soil/` or accepted fixture home |
| Tests | `tests/pipelines/domains/soil/` or accepted test home |
| Raw, work, quarantine, processed, catalog, triplet, or published outputs | `data/...` lifecycle homes |
| Receipts and proofs | `data/receipts/...`, `data/proofs/...` |
| Release decisions | `release/candidates/soil/`, `release/manifests/soil/`, rollback/correction release homes |
| Public API or map code | `apps/governed-api/`, `apps/explorer-web/`, packages |
| Crop/yield, streamflow, groundwater, lithology, habitat-patch, or species/plant occurrence truth | Owning domain lanes only |

> [!WARNING]
> The previous scaffold wording allowed docs, contracts, schemas, policies, fixtures, tests, packages, pipelines, registries, or data lifecycle artifacts here. This README narrows the boundary: **only executable Soil pipeline logic belongs here.** The other responsibility roots remain separate authority surfaces.

[⬆ Back to top](#top)

---

## 6. Pipeline scope

| Scope area | Pipeline responsibility | Publication posture |
|---|---|---|
| Soil map units | Normalize map-unit identity, geometry refs, source vintage, and MUKEY lineage. | Public only after evidence and release closure. |
| Components / horizons | Normalize component and horizon records, percentages, depths, and joins. | Requires lineage validation. |
| Soil properties | Normalize measured or derived properties with units and support type. | No unitless or supportless values. |
| Hydrologic soil group | Normalize classification and caveats. | Context for hydrology; not flood truth. |
| Soil moisture | Normalize station/satellite observations, depths, units, QC, and time basis. | Current-state displays need freshness and release controls. |
| Pedon / profile | Normalize profile evidence. | Evidence object, not generalized survey surface unless derived. |
| Erosion risk | Build interpretive candidates. | Interpretation, not Hazards authority. |
| Suitability rating | Build suitability candidates and caveats. | Not crop/yield truth or management advice. |
| Cross-lane joins | Prepare soil × agriculture/hydrology/habitat/geology/flora/fauna relations. | Other domains keep ownership; joins are derived. |
| Catalog/triplet handoff | Prepare restricted or public-safe catalog/graph candidates after evidence closure. | Projection does not replace canonical review state. |

[⬆ Back to top](#top)

---

## 7. Source-family posture

Soil pipeline code may consume only admitted or fixture-bound source material.

Candidate source families may include, subject to source descriptors, rights, and steward review:

- NRCS SSURGO;
- USDA NRCS Soil Data Access;
- NRCS gSSURGO;
- NRCS gNATSGO;
- Kansas Mesonet soil-moisture sources where admitted;
- NRCS SCAN;
- NOAA USCRN;
- NASA SMAP;
- ISRIC SoilGrids;
- agriculture, hydrology, habitat, geology, flora, fauna, and hazards context through governed joins;
- local upload or steward-curated material only through source-descriptor, rights, sensitivity, and review gates.

This README does not activate any source. Each source family requires SourceDescriptor coverage, source role, rights posture, sensitivity classification, attribution, fixtures, validation, and review routing before use.

[⬆ Back to top](#top)

---

## 8. Lifecycle contract

Every Soil pipeline must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal pipeline stance:

1. **Read** approved synthetic/generalized/redacted fixtures, immutable raw captures, work candidates, quarantine inputs in remediation mode, or prior processed baselines.
2. **Normalize** into work candidates with source role, rights, support type, temporal scope, spatial scope, lineage, units, depth basis, sensitivity posture, evidence references, and public-safe transform posture.
3. **Quarantine** unresolved rights, source-role mismatch, missing support type, unit ambiguity, lineage failure, horizon-depth failure, unsupported cross-support aggregation, sensitivity risk, schema drift, or validation failure.
4. **Promote to processed** only after validation, policy, evidence, support-type, sensitivity/public-safe transform, review, and reviewer gates appropriate to significance.
5. **Prepare catalog/triplet handoffs** only after processed-state and evidence closure, and only with sensitivity-safe payloads and support-type caveats.
6. **Publish** only through release decisions, public-safe artifacts, rollback targets, and correction paths.

Promotion is a governed state transition with receipts and review evidence, not a file move.

[⬆ Back to top](#top)

---

## 9. Required gates

Every Soil pipeline run must check or explicitly fail closed on:

1. **Source descriptor gate** — every input has stable source identity, role, cadence/vintage, rights, and sensitivity posture.
2. **Source-role gate** — authority, observation, context, model, derivative, aggregate, candidate, synthetic, and generated records are not silently collapsed.
3. **Support-type gate** — static survey, gridded derivative, station reading, satellite grid, pedon evidence, and interpretation remain distinct.
4. **Lineage gate** — MUKEY, COKEY, CHKEY, horizon, component, and map-unit relations remain traceable where applicable.
5. **Unit/depth gate** — units, depths, layer intervals, vertical basis, and QC flags are explicit where applicable.
6. **Time-caveat gate** — source vintage, observed time, valid time, retrieval time, processing time, catalog time, release time, and correction time remain distinct.
7. **Rights gate** — unknown or restrictive license, permission, attribution, privacy, or redistribution terms block public release.
8. **Sensitivity gate** — field-specific, owner-specific, unpublished, proprietary, private-network, cross-lane, or insufficiently reviewed records fail closed.
9. **Public-safe transform gate** — public products require approved redaction, aggregation, generalization, delay, restriction, or denial decisions with receipts where needed.
10. **Cross-lane ownership gate** — agriculture, hydrology, geology, habitat, flora, fauna, hazards, and people/land lanes keep their own truth and sensitivity rules.
11. **Schema, contract, evidence, policy, validation, receipt, catalog/triplet, and release gates** — all must close or the run abstains, denies, or quarantines.
12. **No-direct-publish gate** — no writes to public UI, public API, or `data/published/` without release workflow authority.

[⬆ Back to top](#top)

---

## 10. Sensitivity, support-type, and public-safe posture

Soil is often public-safe at appropriate scale, but KFM still fails closed where rights, source role, support type, or sensitivity is unresolved.

Default posture:

- supportless soil values are denied or quarantined;
- survey evidence, gridded derivatives, station observations, satellite grids, pedon evidence, and interpretations remain distinct;
- suitability and erosion context are interpretive and must carry caveats;
- farm-specific, owner-specific, unpublished, proprietary, or private-network material requires review before downstream public use;
- cross-lane joins must not leak restricted ecology, people/land, infrastructure, or site-specific context;
- generated summaries cannot replace source evidence, support type, time caveat, policy, validation, or release state.

[⬆ Back to top](#top)

---

## 11. Directory contract

Recommended shape:

```text
pipelines/domains/soil/
├── README.md                         # this file
├── PIPELINE_CONTRACT.md              # PROPOSED: Soil execution contract
├── run_dry_fixture.py                # PROPOSED synthetic/generalized/redacted fixtures only
├── normalize_map_unit.py             # PROPOSED
├── normalize_component.py            # PROPOSED
├── normalize_horizon.py              # PROPOSED
├── normalize_soil_property.py        # PROPOSED
├── normalize_hydrologic_soil_group.py # PROPOSED
├── normalize_soil_moisture.py        # PROPOSED
├── normalize_pedon.py                # PROPOSED
├── build_interpretation_candidate.py # PROPOSED
├── validate_support_type.py          # PROPOSED
├── validate_lineage.py               # PROPOSED
├── validate_units_depths.py          # PROPOSED
├── apply_public_safe_transform.py    # PROPOSED; may belong in shared tools if reused
├── build_catalog_handoff.py          # PROPOSED if not centralized in pipelines/catalog/
├── validate_soil_candidate.py        # PROPOSED wrapper if not centralized in tools/
├── emit_receipt.py                   # PROPOSED only if not shared
└── adapters/                         # PROPOSED thin lifecycle adapters, no source fetching
```

Declarative specs should live outside this directory:

```text
pipeline_specs/soil/
├── README.md                         # PROPOSED / NEEDS VERIFICATION
├── ssurgo_dry_run.yaml               # PROPOSED
├── soil_moisture_dry_run.yaml        # PROPOSED
├── support_type_checks.yaml          # PROPOSED
├── public_safe_transform.yaml        # PROPOSED
└── catalog_handoff.yaml              # PROPOSED
```

Generated outputs must not be written beside the code that generated them. Use accepted lifecycle homes under `data/`, proof homes under `data/proofs/`, receipt homes under `data/receipts/`, and release homes under `release/`.

[⬆ Back to top](#top)

---

## 12. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Fixture input | `fixtures/domains/soil/` or accepted fixture home | Synthetic, generalized, or redacted where needed. |
| Raw capture | `data/raw/soil/<source_id>/<run_id>/` | Immutable source-edge capture with source descriptor and receipt. |
| Work candidate | `data/work/soil/<run_id>/` | Candidate only. |
| Quarantine record | `data/quarantine/soil/<reason>/<run_id>/` | Failed, restricted, unresolved, or unsafe material. |
| Processed dataset | `data/processed/soil/<dataset_id>/<version>/` | Validated/restricted; not automatically public. |
| Catalog candidate | `data/catalog/domain/soil/...` or approved catalog home | After processed-state, transform, and evidence gates. |
| Triplet / graph delta | `data/triplets/soil/...` or approved graph-delta home | Projection only. |
| Receipts / proofs | `data/receipts/...`, `data/proofs/...` | Required for auditable promotion and release review. |
| Release handoff | `release/candidates/soil/...` | Only through release workflow. |

[⬆ Back to top](#top)

---

## 13. Minimal pipeline candidate record

The final schema is not defined here. This example shows the minimum information a Soil pipeline candidate should preserve.

```yaml
schema_version: kfm.soil_pipeline_candidate.v1
candidate_id: soil_<object_family>_<run_id>_<hash>
pipeline_id: domains.soil
run_id: run_YYYYMMDDThhmmssZ
status: WORK_CANDIDATE
object_family: <soil_map_unit|soil_component|horizon|soil_property|hydrologic_soil_group|soil_moisture_observation|pedon|erosion_risk|suitability_rating|component_horizon_join>
support_type: <authoritative_static_soil|gridded_derivative_soil|station_soil_moisture|satellite_soil_moisture|pedon_evidence|interpretation>
source_inputs:
  - source_id: src_soil_example
    source_role: <authority|observation|context|model|derivative|aggregate|candidate|synthetic|restricted>
    lifecycle_ref: data/raw/soil/<source_id>/<run_id>/
    input_hash: sha256:<hash>
    rights_state: needs_review
lineage:
  mukey: null
  cokey: null
  chkey: null
anti_collapse:
  gridded_derivative_is_survey_truth: false
  station_reading_is_surface: false
  interpretation_is_measurement: false
  generated_summary_is_evidence: false
temporal_scope:
  source_vintage: null
  observed_at: null
  valid_start: null
  valid_end: null
  retrieved_at: YYYY-MM-DDThh:mm:ssZ
  processed_at: YYYY-MM-DDThh:mm:ssZ
method:
  transform_family: soil_candidate_normalization
  algorithm_version: <version>
  parameter_hash: sha256:<hash>
sensitivity:
  field_specific_risk: needs_review
  owner_specific_risk: needs_review
  cross_lane_risk: needs_review
  public_release_default: DENY_UNTIL_REVIEW
policy:
  outcome: ABSTAIN
  reason_code: SUPPORT_TYPE_RIGHTS_OR_EVIDENCE_NOT_RESOLVED
evidence:
  evidence_bundle_ref: null
  citation_state: ABSTAIN
outputs:
  candidate_record: data/work/soil/run_YYYYMMDDThhmmssZ/candidate.yml
  receipt: data/receipts/pipeline/soil/run_YYYYMMDDThhmmssZ.yml
rollback:
  required_before_publication: true
```

[⬆ Back to top](#top)

---

## 14. Dry-run, tests, fixtures, receipts, and proofs

Default execution is **fixture-only, synthetic/generalized/redacted, and no-network** until source activation, rights review, support-type review, sensitivity review, source-role review, and CI coverage are approved.

Recommended tests:

```text
tests/pipelines/domains/soil/
├── test_no_network_dry_run.py             # PROPOSED
├── test_source_role_required.py           # PROPOSED
├── test_rights_unknown_denied.py          # PROPOSED
├── test_support_type_required.py          # PROPOSED
├── test_mukey_cokey_chkey_lineage.py      # PROPOSED
├── test_horizon_depth_sanity.py           # PROPOSED
├── test_soil_moisture_unit_depth_qc.py    # PROPOSED
├── test_cross_support_aggregation_denies.py # PROPOSED
├── test_interpretation_not_measurement.py # PROPOSED
├── test_missing_evidence_abstains.py      # PROPOSED
├── test_receipt_hashes.py                 # PROPOSED
└── test_no_direct_publish.py              # PROPOSED
```

A dry run should prove fixtures load without network access, source roles are present, missing support type is denied or quarantined, lineage and unit checks run, EvidenceBundle gaps produce abstention, receipts are deterministic, and no run writes directly to public UI, public API, `data/published/`, or release manifests.

[⬆ Back to top](#top)

---

## 15. Promotion, publication, correction, and rollback

Soil pipelines may prepare candidates. They do not publish.

Required promotion chain:

```text
soil source or work input
  -> soil candidate
  -> validation report
  -> policy decision
  -> support-type / lineage / public-safe transform receipt where required
  -> EvidenceBundle closure
  -> processed restricted dataset version
  -> catalog / triplet candidate
  -> release candidate
  -> ReleaseManifest
  -> RollbackCard
  -> public-safe artifact
```

Correction and rollback posture:

- denied, abstained, errored, restricted, and quarantined runs remain auditable;
- candidate rollback preserves receipts and proof state;
- processed versions are superseded by governed state transition, not hidden overwrite;
- cross-support derivatives are invalidated if source refs, support-type refs, method refs, or policy refs drift;
- public artifact rollback is owned by `release/`, not by this directory;
- correction notices must point back to source, evidence, support type, validation, catalog, release, and rollback state.

[⬆ Back to top](#top)

---

## 16. Definition of done

This README is done when it:

- replaces the greenfield scaffold with a usable Soil pipeline contract;
- identifies this directory as executable pipeline logic only;
- corrects the boundary so docs, schemas, contracts, policy, fixtures, tests, data, registries, receipts, proofs, and release decisions do not live here;
- preserves support-type separation, source-role, lineage, units, time caveats, evidence, policy, lifecycle, catalog/triplet, release, correction, and rollback boundaries;
- blocks direct publication and unresolved field-specific or owner-specific exposure;
- gives maintainers a fixture-first, fail-closed expansion pattern.

Future executable work in this lane is done only when it has source-descriptor coverage, synthetic/generalized/redacted no-network fixtures, schema-backed candidates, contract conformance, rights/support-type/sensitivity/source-role/evidence tests, deterministic receipts, no-direct-publish tests, CI coverage, steward-review handoff, and release/correction/rollback documentation.

[⬆ Back to top](#top)

---

## 17. Open questions

| ID | Question | Status |
|---|---|---|
| `SOIL-PIPE-001` | Which child modules should be implemented first: SSURGO map units, components/horizons, soil moisture, support-type validation, or catalog handoff? | NEEDS VERIFICATION |
| `SOIL-PIPE-002` | Which source descriptors are first-wave approved for fixture-only dry runs? | NEEDS VERIFICATION |
| `SOIL-PIPE-003` | Which CI job owns Soil pipeline invariant tests? | UNKNOWN |
| `SOIL-PIPE-004` | Should catalog handoff logic live here or in centralized `pipelines/catalog/` with Soil adapters? | NEEDS VERIFICATION |
| `SOIL-PIPE-005` | Which public-safe map/API products are allowed after review and release, and at what support-type, scale, and time-caveat level? | NEEDS VERIFICATION |
| `SOIL-PIPE-006` | How should cross-lane joins with Agriculture, Hydrology, Habitat, Geology, Flora, Fauna, Hazards, or People/Land be denied, restricted, or generalized? | NEEDS VERIFICATION |
| `SOIL-PIPE-007` | Which object family owns cross-support derivation receipts if they become reusable outside Soil? | PROPOSED / NEEDS ADR |

---

## Maintainer note

Start with synthetic/generalized/redacted fixture-only dry runs and negative tests. Do not add live source fetching, supportless values, cross-support aggregation, field-specific products, public map layers, release handoff automation, or direct API payload generation until source roles, rights, support-type separation, lineage validation, public-safe transforms, evidence closure, and rollback are proven.
