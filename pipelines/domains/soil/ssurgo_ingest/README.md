<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-soil-ssurgo-ingest-readme
title: Soil SSURGO Ingest Pipeline README
type: readme
version: v0.1
status: draft
owners:
  - <soil-pipeline-owner>
  - <soil-domain-steward>
  - <nrcs-source-steward>
  - <source-steward>
  - <evidence-steward>
  - <policy-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: pipelines/domains/soil/ssurgo_ingest/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipelines/domains/README.md
  - pipelines/domains/soil/README.md
  - docs/domains/soil/ARCHITECTURE.md
  - docs/domains/soil/DATA_LIFECYCLE.md
  - docs/domains/soil/CANONICAL_PATHS.md
  - docs/sources/catalog/nrcs/ssurgo.md
  - docs/sources/catalog/nrcs/soil-data-access.md
  - docs/sources/catalog/nrcs/gssurgo.md
  - pipeline_specs/soil/ssurgo_ingest.yaml
  - contracts/domains/soil/
  - schemas/contracts/v1/domains/soil/
  - policy/domains/soil/
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
  - nrcs
  - ssurgo
  - ingest
  - soil-survey
  - mukey
  - cokey
  - chkey
  - authoritative-static-soil
  - support-type-separation
  - evidence
  - policy
  - governance
notes:
  - "This README fills the blank pipelines/domains/soil/ssurgo_ingest path as a Soil-domain executable sublane."
  - "SSURGO ingest logic is executable implementation support only; it does not own NRCS source descriptors, source catalog profiles, connector/fetch logic, schemas, policy, lifecycle data, catalog truth, or release decisions."
  - "The subdirectory name uses the requested underscore form ssurgo_ingest; if repo slug rules prefer hyphenated names, record the path decision with ADR/path-map/rollback notes before moving."
  - "SSURGO ingest must preserve MUKEY/COKEY/CHKEY lineage, map-unit/component/horizon hierarchy, source vintage, support type, geometry scope, attribute provenance, and receipt lineage."
  - "SSURGO is authoritative static soil survey evidence, not SDA live-query behavior, gSSURGO gridded derivative truth, crop/yield truth, hydrology truth, real-time soil moisture, or management advice."
  - "Concrete executable behavior, connector linkage, schedules, CI coverage, schema paths, release wiring, and public API/map behavior remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# SSURGO Soil Ingest Pipeline

> Executable Soil-domain sublane for normalizing admitted USDA NRCS SSURGO static soil-survey material into KFM work candidates, quarantine records, processed candidates, catalog/triplet handoffs, receipts, and release-review packages — without collapsing survey polygons, component tables, horizon tables, derived interpretations, gridded derivatives, SDA query behavior, or public release state.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-SSURGO%20soil%20ingest-2e7d32)
![authority](https://img.shields.io/badge/authority-executable%20logic-0a7ea4)
![support](https://img.shields.io/badge/support--type-authoritative__static__soil-d62728)
![publication](https://img.shields.io/badge/publication-release%20gated-d62728)
![ci](https://img.shields.io/badge/CI-TODO-lightgrey)

**Status:** Draft  
**Path:** `pipelines/domains/soil/ssurgo_ingest/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Domain lane:** Soil  
**Sublane:** SSURGO ingest  
**Placement posture:** nested executable sublane under `pipelines/domains/soil/`; concrete executable behavior remains `PROPOSED / NEEDS VERIFICATION` unless backed by tests and repo evidence  
**Public posture:** no direct publication; public output requires lifecycle, EvidenceBundle, source-role, support-type tag, MUKEY/COKEY/CHKEY lineage, source vintage, rights, sensitivity, policy, catalog/triplet, release, correction, and rollback closure

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. SSURGO anti-collapse rules](#3-ssurgo-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Ingest scope](#6-ingest-scope)
- [7. Source-family posture](#7-source-family-posture)
- [8. Lifecycle contract](#8-lifecycle-contract)
- [9. Required gates](#9-required-gates)
- [10. Directory contract](#10-directory-contract)
- [11. Inputs and outputs](#11-inputs-and-outputs)
- [12. Minimal SSURGO ingest candidate record](#12-minimal-ssurgo-ingest-candidate-record)
- [13. Dry-run, tests, fixtures, receipts, and proofs](#13-dry-run-tests-fixtures-receipts-and-proofs)
- [14. Promotion, publication, correction, and rollback](#14-promotion-publication-correction-and-rollback)
- [15. Definition of done](#15-definition-of-done)
- [16. Open questions](#16-open-questions)

---

## 1. Purpose

`pipelines/domains/soil/ssurgo_ingest/` is the executable sublane for SSURGO normalization inside the Soil domain.

It supports candidate processing for:

- SSURGO survey area packages and source-vintage metadata;
- map-unit polygon references and MUKEY identity;
- component records and COKEY joins;
- horizon records and CHKEY joins;
- component-horizon lineage and weighted rollups;
- soil properties, hydrologic soil group, and survey-derived interpretation candidates;
- geometry, tabular, and relation integrity checks;
- source-vintage and SoilTimeCaveat handling;
- quarantine records for missing lineage, missing geometry, missing source descriptor, unresolved rights, schema drift, support-type failure, or validation failure;
- catalog/triplet handoff packages after evidence, validation, and policy close.

This directory implements or will implement the **how** of SSURGO ingest. It does not fetch from NRCS directly, define NRCS source identity, define Soil object meaning, define schemas, encode policy, store lifecycle data, decide public release, or turn SSURGO-derived interpretations into crop, water, habitat, geology, or management truth.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable pipeline logic: the **how**. | CONFIRMED root responsibility |
| Why `domains/soil/`? | Soil is the domain lane; Soil docs place executable logic under `pipelines/domains/soil/`. | CONFIRMED documentation pattern; behavior NEEDS VERIFICATION |
| Why `ssurgo_ingest/`? | This is a narrow executable sublane for SSURGO static soil-survey normalization under Soil. | PROPOSED / NEEDS VERIFICATION |
| Is this a connector? | No. Source fetching belongs in `connectors/<source>` or an accepted source-edge home. This sublane reads admitted lifecycle inputs or fixtures. | CONFIRMED separation |
| Where does the source profile live? | `docs/sources/catalog/nrcs/ssurgo.md`. | CONFIRMED source-doc path |
| Where does a declarative run spec live? | `pipeline_specs/soil/ssurgo_ingest.yaml` or accepted spec home. | PROPOSED / NEEDS VERIFICATION |
| Where do schemas and contracts live? | `schemas/contracts/v1/domains/soil/` and `contracts/domains/soil/` or accepted homes. | PROPOSED / NEEDS VERIFICATION |
| Can this sublane publish? | No. It may prepare candidates and release handoffs only through governed workflow. | CONFIRMED doctrine posture |

> [!IMPORTANT]
> SSURGO ingest code is subordinate to SourceDescriptor, source role, rights, support-type tagging, MUKEY/COKEY/CHKEY lineage, geometry/table validation, EvidenceBundle closure, policy decisions, release manifests, correction notices, and rollback cards. A successful ingest is not public release.

[⬆ Back to top](#top)

---

## 3. SSURGO anti-collapse rules

SSURGO must remain authoritative static soil-survey evidence.

Disallowed collapses:

```text
SSURGO survey polygon -> real-time condition
SSURGO map unit -> component fact without component weighting
component row -> horizon row
horizon property -> map-unit property without derivation receipt
SSURGO vector survey -> gSSURGO raster derivative truth
SSURGO snapshot -> SDA live-query result
SSURGO suitability interpretation -> crop/yield truth
hydrologic soil group -> flood determination
soil property -> geology/lithology truth
generated summary -> evidence
```

Required distinctions:

- map-unit identity, component identity, and horizon identity remain separate;
- MUKEY, COKEY, and CHKEY lineage is preserved where applicable;
- geometry source, table source, survey area, and source vintage are recorded;
- support type is `authoritative_static_soil` or the accepted static survey support label;
- SDA query outputs and gSSURGO gridded derivatives are separate product families;
- KFM-derived rollups, interpretations, joins, and public-safe layers require receipts.

[⬆ Back to top](#top)

---

## 4. What belongs here

Files belong here when their primary responsibility is executable SSURGO Soil ingest processing.

Appropriate contents include:

- fixture-only dry-run entrypoints for SSURGO ingest;
- survey-area metadata normalization helpers;
- map-unit geometry and MUKEY normalizers;
- component and COKEY normalizers;
- horizon and CHKEY normalizers;
- component-horizon join and lineage validators;
- soil property, hydrologic soil group, erosion context, and suitability candidate builders;
- source-vintage and SoilTimeCaveat helpers;
- geometry CRS/projection and topology sanity checks;
- support-type validators for `authoritative_static_soil`;
- quarantine routing helpers for missing lineage, missing geometry, unsupported source vintage, unresolved rights, schema drift, or validation failure;
- receipt emitters, if not shared;
- catalog/triplet handoff helpers, if not centralized in `pipelines/catalog/`;
- thin adapters that read governed lifecycle inputs, not live NRCS endpoints.

A good placement test:

> If the code transforms admitted SSURGO lifecycle inputs into Soil survey candidates, quarantine records, processed records, receipts, or catalog handoffs, it may belong here. If it fetches NRCS data, defines source identity, defines schemas, encodes policy, creates public maps, or approves release, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| NRCS fetcher / source-edge connector | `connectors/nrcs/` or accepted connector home |
| SSURGO source profile | `docs/sources/catalog/nrcs/ssurgo.md` |
| SDA API profile | `docs/sources/catalog/nrcs/soil-data-access.md` |
| gSSURGO derivative profile | `docs/sources/catalog/nrcs/gssurgo.md` |
| Source descriptors / source registry entries | `data/registry/sources/soil/`, `data/registry/sources/nrcs/`, or accepted registry home |
| Soil architecture and doctrine | `docs/domains/soil/...` |
| Object meaning contracts | `contracts/domains/soil/...` |
| JSON Schemas | `schemas/contracts/v1/domains/soil/...` |
| Policy bundles and release rules | `policy/domains/soil/`, rights, sensitivity, and release policy roots |
| Declarative run specs | `pipeline_specs/soil/...` |
| Fixtures | `fixtures/domains/soil/ssurgo_ingest/` or accepted fixture home |
| Tests | `tests/pipelines/domains/soil/ssurgo_ingest/` or accepted test home |
| Raw, work, quarantine, processed, catalog, triplet, or published outputs | `data/...` lifecycle homes |
| Receipts and proofs | `data/receipts/...`, `data/proofs/...` |
| Release decisions | `release/candidates/soil/`, `release/manifests/soil/`, rollback/correction release homes |
| Public API or map code | `apps/governed-api/`, `apps/explorer-web/`, packages |
| Crop/yield, flood, groundwater, lithology, habitat, or land-management claims | Owning domain lanes or reviewed downstream products only |

[⬆ Back to top](#top)

---

## 6. Ingest scope

| Scope area | Pipeline responsibility | Publication posture |
|---|---|---|
| Survey area | Normalize survey package identity, source vintage, and retrieval context. | Candidate until descriptor, rights, and validation close. |
| Map units | Normalize MUKEY, map-unit symbol/name, geometry refs, and survey area relation. | Geometry is source-vintage bound. |
| Components | Normalize component rows, percentages, COKEY, and map-unit joins. | Component weighting required for rollups. |
| Horizons | Normalize horizon rows, depths, CHKEY, and component joins. | Depth sanity and lineage required. |
| Soil properties | Normalize property values, units, nulls, ranges, and provenance. | No unitless/supportless values. |
| Hydrologic soil group | Normalize classification and caveats. | Context for hydrology, not flood truth. |
| Interpretations | Build erosion/suitability candidates with caveats. | Interpretation, not management advice. |
| Catalog/triplet handoff | Prepare restricted or public-safe catalog/graph candidates after evidence closure. | Projection does not replace canonical review state. |

[⬆ Back to top](#top)

---

## 7. Source-family posture

This sublane is for NRCS SSURGO static soil-survey products only.

It may consume:

- no-network synthetic or redacted SSURGO-like fixtures;
- admitted immutable SSURGO raw captures under `data/raw/soil/` or an accepted NRCS raw home;
- work candidates from a governed source-edge ingest;
- approved source registry metadata and source descriptors;
- policy, schema, and contract refs used by validators.

It must not activate a source by itself. Source activation requires source descriptor coverage, rights posture, sensitivity classification, retrieval method, source head/cadence, fixtures, validation, and review routing.

[⬆ Back to top](#top)

---

## 8. Lifecycle contract

Every SSURGO ingest run must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal stance:

1. **Read** approved fixtures, immutable raw captures, work candidates, quarantine inputs in remediation mode, or prior processed baselines.
2. **Normalize** into static-soil survey candidates with source role, support type, survey area, MUKEY/COKEY/CHKEY lineage, geometry refs, units, depths, source vintage, evidence refs, and receipt refs.
3. **Quarantine** unresolved rights, missing descriptor, missing survey area, missing MUKEY, missing COKEY/CHKEY where required, geometry/table mismatch, unit ambiguity, horizon-depth failure, support-type failure, schema drift, or validation failure.
4. **Promote to processed** only after validation, policy, evidence, support-type, lineage, geometry/table, source-vintage, and review gates close.
5. **Prepare catalog/triplet handoffs** only after processed-state and evidence closure, and only with support-type, scale, and time caveats.
6. **Publish** only through release decisions, public-safe artifacts, rollback targets, and correction paths.

Promotion is a governed state transition with receipts and review evidence, not a file move.

[⬆ Back to top](#top)

---

## 9. Required gates

Every SSURGO ingest run must check or explicitly fail closed on:

1. **Source descriptor gate** — NRCS SSURGO source identity, role, cadence/vintage, rights, and sensitivity posture are known.
2. **Source-role gate** — SSURGO survey records remain authoritative static soil-survey records, not live measurements or management decisions.
3. **Support-type gate** — SSURGO candidates carry the accepted `authoritative_static_soil` support label.
4. **Survey-area gate** — survey area/source vintage is recorded and not treated as timeless truth.
5. **MUKEY gate** — map-unit identity is present where map-unit records are emitted.
6. **COKEY gate** — component identity and map-unit relation are present where component records are emitted.
7. **CHKEY gate** — horizon identity and component relation are present where horizon records are emitted.
8. **Lineage gate** — component/horizon/property joins preserve MUKEY/COKEY/CHKEY lineage.
9. **Geometry gate** — geometry CRS, scale, topology, and source-vintage caveats are recorded.
10. **Unit and depth gate** — property units, nulls, ranges, horizon depths, and aggregation rules are explicit.
11. **Interpretation gate** — erosion and suitability products remain interpretations with caveats.
12. **Rights gate** — unknown or restrictive license, permission, attribution, privacy, or redistribution terms block public release.
13. **Sensitivity gate** — field-specific, owner-specific, unpublished, proprietary, cross-lane, or insufficiently reviewed records fail closed until reviewed.
14. **Derived-artifact gate** — gridding, component-weighted rollup, property aggregation, public map derivation, or cross-lane join requires a receipt.
15. **Schema, contract, evidence, policy, validation, receipt, catalog/triplet, and release gates** — all must close or the run abstains, denies, or quarantines.
16. **No-direct-publish gate** — no writes to public UI, public API, or `data/published/` without release workflow authority.

[⬆ Back to top](#top)

---

## 10. Directory contract

Recommended shape:

```text
pipelines/domains/soil/ssurgo_ingest/
├── README.md                         # this file
├── PIPELINE_CONTRACT.md              # PROPOSED: sublane execution contract
├── run_dry_fixture.py                # PROPOSED synthetic/redacted fixture only
├── normalize_survey_area.py          # PROPOSED
├── normalize_map_unit.py             # PROPOSED
├── normalize_component.py            # PROPOSED
├── normalize_horizon.py              # PROPOSED
├── normalize_soil_property.py        # PROPOSED
├── normalize_hydrologic_soil_group.py # PROPOSED
├── build_interpretation_candidate.py # PROPOSED
├── validate_mukey_cokey_chkey.py     # PROPOSED
├── validate_geometry_tables.py       # PROPOSED
├── validate_units_depths.py          # PROPOSED
├── validate_support_type.py          # PROPOSED
├── build_catalog_handoff.py          # PROPOSED if not centralized in pipelines/catalog/
├── emit_receipt.py                   # PROPOSED only if not shared
└── adapters/                         # PROPOSED thin lifecycle adapters, no NRCS fetching
```

Declarative specs should live outside this directory:

```text
pipeline_specs/soil/ssurgo_ingest.yaml # PROPOSED / NEEDS VERIFICATION
```

Generated outputs must not be written beside the code that generated them. Use accepted lifecycle homes under `data/`, proof homes under `data/proofs/`, receipt homes under `data/receipts/`, and release homes under `release/`.

[⬆ Back to top](#top)

---

## 11. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Fixture input | `fixtures/domains/soil/ssurgo_ingest/` or accepted fixture home | Synthetic, generalized, or redacted. |
| Raw SSURGO capture | `data/raw/soil/<source_id>/<run_id>/` or accepted NRCS raw home | Immutable source-edge capture with source descriptor and receipt. |
| Work candidate | `data/work/soil/<run_id>/` | Candidate only. |
| Quarantine record | `data/quarantine/soil/<reason>/<run_id>/` | Failed, restricted, unresolved, or unsafe material. |
| Processed survey dataset | `data/processed/soil/<dataset_id>/<version>/` | Validated/restricted; not automatically public. |
| Catalog candidate | `data/catalog/domain/soil/...` or approved catalog home | After processed-state, transform, and evidence gates. |
| Triplet / graph delta | `data/triplets/soil/...` or approved graph-delta home | Projection only. |
| Receipts / proofs | `data/receipts/...`, `data/proofs/...` | Required for auditable promotion and release review. |
| Release handoff | `release/candidates/soil/...` | Only through release workflow. |

[⬆ Back to top](#top)

---

## 12. Minimal SSURGO ingest candidate record

The final schema is not defined here. This example shows the minimum information a SSURGO ingest candidate should preserve.

```yaml
schema_version: kfm.soil_ssurgo_ingest_candidate.v1
candidate_id: soil_ssurgo_<object_family>_<mukey_or_digest>_<run_id>
pipeline_id: domains.soil.ssurgo_ingest
run_id: run_YYYYMMDDThhmmssZ
status: WORK_CANDIDATE
source:
  source_id: nrcs_ssurgo
  source_role: authority
  support_type: authoritative_static_soil
  lifecycle_ref: data/raw/soil/nrcs_ssurgo/<run_id>/
  input_hash: sha256:<hash>
  rights_state: needs_review
survey:
  survey_area_id: <survey_area_id>
  source_vintage: <vintage_or_null>
object:
  object_family: <soil_map_unit|soil_component|horizon|soil_property|hydrologic_soil_group|erosion_risk|suitability_rating|component_horizon_join>
  mukey: <mukey_or_null>
  cokey: <cokey_or_null>
  chkey: <chkey_or_null>
geometry:
  geometry_ref: restricted_or_public_safe_ref
  crs: <crs_or_null>
lineage:
  mukey_present: true
  cokey_required: false
  chkey_required: false
  join_path: []
anti_collapse:
  ssurgo_is_realtime_condition: false
  ssurgo_is_gssurgo_grid: false
  ssurgo_is_sda_live_query: false
  interpretation_is_measurement: false
  generated_summary_is_evidence: false
policy:
  outcome: ABSTAIN
  reason_code: SOURCE_DESCRIPTOR_LINEAGE_OR_EVIDENCE_NOT_RESOLVED
evidence:
  evidence_bundle_ref: null
  citation_state: ABSTAIN
outputs:
  candidate_record: data/work/soil/run_YYYYMMDDThhmmssZ/ssurgo_candidate.yml
  receipt: data/receipts/pipeline/soil/ssurgo_ingest/run_YYYYMMDDThhmmssZ.yml
rollback:
  required_before_publication: true
```

[⬆ Back to top](#top)

---

## 13. Dry-run, tests, fixtures, receipts, and proofs

Default execution is **fixture-only, synthetic/generalized/redacted, and no-network** until source activation, rights review, support-type review, lineage review, and CI coverage are approved.

Recommended tests:

```text
tests/pipelines/domains/soil/ssurgo_ingest/
├── test_no_network_dry_run.py             # PROPOSED
├── test_source_role_authority.py          # PROPOSED
├── test_support_type_authoritative_static.py # PROPOSED
├── test_mukey_required_for_map_units.py   # PROPOSED
├── test_cokey_join_for_components.py      # PROPOSED
├── test_chkey_join_for_horizons.py        # PROPOSED
├── test_component_horizon_lineage.py      # PROPOSED
├── test_geometry_table_integrity.py       # PROPOSED
├── test_horizon_depth_sanity.py           # PROPOSED
├── test_interpretation_not_measurement.py # PROPOSED
├── test_gssurgo_not_ssurgo.py             # PROPOSED
├── test_missing_evidence_abstains.py      # PROPOSED
├── test_receipt_hashes.py                 # PROPOSED
└── test_no_direct_publish.py              # PROPOSED
```

A dry run should prove fixtures load without network access, SSURGO records remain authoritative static soil records, MUKEY/COKEY/CHKEY lineage is preserved, geometry/table integrity checks run, missing support type is denied or quarantined, EvidenceBundle gaps produce abstention, receipts are deterministic, and no run writes directly to public UI, public API, `data/published/`, or release manifests.

[⬆ Back to top](#top)

---

## 14. Promotion, publication, correction, and rollback

SSURGO ingest may prepare candidates. It does not publish.

Required promotion chain:

```text
SSURGO raw/work input
  -> static soil survey candidate
  -> validation report
  -> policy decision
  -> support-type / lineage / geometry-table receipt where required
  -> EvidenceBundle closure
  -> processed Soil survey dataset version
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
- derived products are invalidated if source refs, MUKEY/COKEY/CHKEY refs, support-type refs, method refs, or policy refs drift;
- public artifact rollback is owned by `release/`, not by this directory.

[⬆ Back to top](#top)

---

## 15. Definition of done

This README is done when it:

- fills the blank `pipelines/domains/soil/ssurgo_ingest/README.md` file;
- identifies this directory as a nested executable Soil sublane;
- prevents connector, source-profile, schema, contract, policy, fixture, test, data, receipt, proof, catalog, and release authority from being placed here;
- preserves SSURGO source role, support type, survey area, source vintage, MUKEY/COKEY/CHKEY lineage, geometry/table integrity, evidence, policy, lifecycle, catalog/triplet, release, correction, and rollback boundaries;
- blocks SSURGO/SDA/gSSURGO, map-unit/component/horizon, interpretation/measurement, and public/private lifecycle collapse;
- gives maintainers a fixture-first, fail-closed expansion pattern.

Future executable work in this sublane is done only when it has source-descriptor coverage, synthetic/generalized/redacted no-network fixtures, schema-backed candidates, contract conformance, source-role/support-type/lineage/geometry/evidence tests, deterministic receipts, no-direct-publish tests, CI coverage, steward-review handoff, and release/correction/rollback documentation.

[⬆ Back to top](#top)

---

## 16. Open questions

| ID | Question | Status |
|---|---|---|
| `SOIL-SSURGO-001` | Should the subdirectory remain `ssurgo_ingest` or be renamed to a hyphenated slug after path convention review? | NEEDS VERIFICATION / ADR |
| `SOIL-SSURGO-002` | Which connector or source-edge job owns NRCS SSURGO retrieval before this ingest sublane reads lifecycle inputs? | NEEDS VERIFICATION |
| `SOIL-SSURGO-003` | Which SSURGO tables, fields, joins, and survey-area packages are first-wave approved for fixture-only dry runs? | NEEDS VERIFICATION |
| `SOIL-SSURGO-004` | Which CI job owns SSURGO ingest invariant tests? | UNKNOWN |
| `SOIL-SSURGO-005` | Should catalog handoff logic live here or in centralized `pipelines/catalog/` with a SSURGO adapter? | NEEDS VERIFICATION |
| `SOIL-SSURGO-006` | Which public-safe map/API products are allowed after review and release, and at what scale/source-vintage caveat level? | NEEDS VERIFICATION |
| `SOIL-SSURGO-007` | Which receipt type owns component-weighted rollups, public map derivations, and cross-lane suitability products? | PROPOSED / NEEDS ADR |

---

## Maintainer note

Start with synthetic/generalized fixture-only dry runs and negative tests. Do not add live NRCS fetching, supportless values, lineage-free joins, unreceipted rollups, public map layers, release handoff automation, or direct API payload generation until source roles, rights, support-type separation, MUKEY/COKEY/CHKEY lineage, evidence closure, and rollback are proven.
