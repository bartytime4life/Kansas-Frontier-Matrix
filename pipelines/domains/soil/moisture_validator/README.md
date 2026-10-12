<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-soil-moisture-validator-readme
title: Soil Moisture Validator Pipeline README
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
path: pipelines/domains/soil/moisture_validator/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipelines/domains/README.md
  - pipelines/domains/soil/README.md
  - pipelines/domains/soil/uscrn_ingest/README.md
  - pipelines/domains/soil/scan_awdb_ingest/README.md
  - pipelines/domains/soil/smap_ingest/README.md
  - docs/domains/soil/ARCHITECTURE.md
  - docs/domains/soil/DATA_LIFECYCLE.md
  - docs/domains/soil/CANONICAL_PATHS.md
  - docs/sources/catalog/nrcs/scan-soil-climate.md
  - docs/sources/catalog/noaa/noaa-uscrn.md
  - docs/sources/catalog/nasa/nasa-smap.md
  - pipeline_specs/soil/moisture_validator.yaml
  - contracts/domains/soil/
  - schemas/contracts/v1/domains/soil/
  - policy/domains/soil/
  - data/raw/soil/
  - data/work/soil/
  - data/quarantine/soil/
  - data/processed/soil/
  - data/catalog/domain/soil/
  - data/triplets/soil/
  - data/receipts/pipeline/
  - data/proofs/evidence_bundle/
  - release/candidates/soil/
  - release/manifests/soil/
tags:
  - kfm
  - pipelines
  - domains
  - soil
  - moisture-validator
  - validation
  - station-observation
  - satellite-grid
  - model-assimilated
  - support-type-separation
  - source-role
  - evidence
  - policy
  - governance
notes:
  - "This README fills the blank pipelines/domains/soil/moisture_validator path as a Soil-domain executable validation sublane."
  - "The moisture validator is executable implementation support only; it does not own source descriptors, source catalog profiles, source fetching, schemas, policy, lifecycle data, catalog truth, release decisions, or scientific truth."
  - "The subdirectory name uses the requested underscore form moisture_validator; if repo slug rules prefer hyphenated names, record the path decision with ADR/path-map/rollback notes before moving."
  - "The validator must preserve support-type separation across station observations, satellite/model products, static survey evidence, gridded derivatives, pedon evidence, and interpretations."
  - "Validation is not promotion. Passing validation may create a validation receipt; it does not publish, merge, or canonize soil-moisture truth."
  - "Concrete executable behavior, source linkage, schedules, CI coverage, schema paths, release wiring, and public API/map behavior remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Soil Moisture Validator Pipeline

> Executable Soil-domain validation sublane for checking admitted soil-moisture candidates from station, satellite, model-assimilated, survey-derived, gridded, and interpreted sources before processed/catalog/release handoff — without merging source roles, support types, depths, cadences, grids, stations, QA states, or evidence status.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-soil%20moisture%20validation-2e7d32)
![authority](https://img.shields.io/badge/authority-executable%20logic-0a7ea4)
![support](https://img.shields.io/badge/support--type-required-d62728)
![publication](https://img.shields.io/badge/publication-release%20gated-d62728)
![ci](https://img.shields.io/badge/CI-TODO-lightgrey)

**Status:** Draft  
**Path:** `pipelines/domains/soil/moisture_validator/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Domain lane:** Soil  
**Sublane:** Soil moisture validation  
**Placement posture:** nested executable validation sublane under `pipelines/domains/soil/`; concrete executable behavior remains `PROPOSED / NEEDS VERIFICATION` unless backed by tests and repo evidence  
**Public posture:** no direct publication; public output requires lifecycle, EvidenceBundle, source-role, support-type, depth/cadence/grid/station preservation, rights, sensitivity, policy, catalog/triplet, release, correction, and rollback closure

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Validation anti-collapse rules](#3-validation-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Validation scope](#6-validation-scope)
- [7. Lifecycle contract](#7-lifecycle-contract)
- [8. Required validation gates](#8-required-validation-gates)
- [9. Directory contract](#9-directory-contract)
- [10. Inputs and outputs](#10-inputs-and-outputs)
- [11. Minimal validation receipt record](#11-minimal-validation-receipt-record)
- [12. Tests, fixtures, receipts, and proofs](#12-tests-fixtures-receipts-and-proofs)
- [13. Promotion, publication, correction, and rollback](#13-promotion-publication-correction-and-rollback)
- [14. Definition of done](#14-definition-of-done)
- [15. Open questions](#15-open-questions)

---

## 1. Purpose

`pipelines/domains/soil/moisture_validator/` is the executable sublane for validating soil-moisture candidates inside the Soil domain.

It supports validation for:

- station soil-moisture candidates from SCAN/AWDB, USCRN, Mesonet, or other admitted station sources;
- satellite or model-assimilated soil-moisture candidates such as SMAP;
- surface/root-zone, depth-aware, and cadence-aware moisture records;
- QA flag, missing-value, freshness, preliminary/reprocessed, and uncertainty checks;
- station-vs-grid-vs-area anti-collapse checks;
- support-type and source-role conformance checks;
- comparison or consistency checks across sources only when a comparison receipt records method, limitations, and source roles;
- validation receipts that downstream promotion, catalog, graph, and release workflows can inspect.

This directory implements or will implement the **how** of validating soil-moisture candidates. It does not fetch source data, define source identity, define Soil object meaning, define schemas, encode policy, store lifecycle data, decide public release, or turn validation pass/fail into scientific truth.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable pipeline logic: the **how**. | CONFIRMED root responsibility |
| Why `domains/soil/`? | Soil is the domain lane; Soil docs place executable logic under `pipelines/domains/soil/`. | CONFIRMED documentation pattern; behavior NEEDS VERIFICATION |
| Why `moisture_validator/`? | This is a narrow executable validation sublane for soil-moisture candidates. | PROPOSED / NEEDS VERIFICATION |
| Is this an ingest pipeline? | No. It validates candidates emitted by ingest sublanes or lifecycle inputs. | PROPOSED |
| Is this a source fetcher? | No. Fetching belongs in connectors or accepted source-edge homes. | CONFIRMED separation |
| Where does a declarative validation spec live? | `pipeline_specs/soil/moisture_validator.yaml` or accepted spec home. | PROPOSED / NEEDS VERIFICATION |
| Where do schemas and contracts live? | `schemas/contracts/v1/domains/soil/` and `contracts/domains/soil/` or accepted homes. | PROPOSED / NEEDS VERIFICATION |
| Can this sublane publish? | No. It may emit validation results and receipts only through governed workflow. | CONFIRMED doctrine posture |

> [!IMPORTANT]
> Validation code is subordinate to source descriptors, source roles, support-type tags, depth/cadence semantics, QA flags, freshness state, EvidenceBundle closure, policy decisions, release manifests, correction notices, and rollback cards. A validation pass is not public release.

[⬆ Back to top](#top)

---

## 3. Validation anti-collapse rules

Soil-moisture validation must preserve source meaning.

Disallowed collapses:

```text
validation pass -> publication approval
validation pass -> scientific truth
station reading -> area-wide surface
satellite grid -> station observation
SMAP L4 -> raw observation truth
surface moisture -> root-zone moisture
sensor depth A -> sensor depth B
NRT record -> reprocessed record
watcher signal -> observed reading
comparison check -> silent merged product
generated summary -> evidence
```

Required distinctions:

- source role is explicit and never rewritten in place;
- support type is explicit and required;
- station, grid, map unit, county, and area scopes remain distinct;
- sensor depth, layer, and cadence remain distinct;
- QA and uncertainty are preserved;
- freshness and stale-state are recorded where applicable;
- cross-source comparison, fusion, aggregation, interpolation, or anomaly products require separate receipts.

[⬆ Back to top](#top)

---

## 4. What belongs here

Files belong here when their primary responsibility is executable soil-moisture validation.

Appropriate contents include:

- fixture-only validation entrypoints;
- support-type validators;
- source-role validators;
- station-vs-grid-vs-area scope validators;
- depth, layer, cadence, and unit validators;
- QA flag, uncertainty, missing-value, and range validators;
- freshness and stale-source validators;
- NRT/reprocessed supersession validators;
- no-silent-merge and comparison-receipt validators;
- validation receipt emitters, if not shared;
- catalog/release preflight validators, if not centralized elsewhere;
- thin adapters that read governed lifecycle inputs, not live source systems.

A good placement test:

> If the code validates admitted Soil moisture candidates and emits validation results, quarantine decisions, or receipts, it may belong here. If it fetches data, normalizes source-specific files, defines schemas, encodes policy, builds derived surfaces, or approves release, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Source fetchers | `connectors/<source>` or accepted connector home |
| Source-specific ingest code | `pipelines/domains/soil/<source>_ingest/` |
| Source catalog profiles | `docs/sources/catalog/...` |
| Source descriptors / source registry entries | `data/registry/sources/soil/` or accepted registry home |
| Soil architecture and doctrine | `docs/domains/soil/...` |
| Object meaning contracts | `contracts/domains/soil/...` |
| JSON Schemas | `schemas/contracts/v1/domains/soil/...` |
| Policy bundles and release rules | `policy/domains/soil/`, rights, sensitivity, and release policy roots |
| Declarative run specs | `pipeline_specs/soil/...` |
| Fixtures | `fixtures/domains/soil/moisture_validator/` or accepted fixture home |
| Tests | `tests/pipelines/domains/soil/moisture_validator/` or accepted test home |
| Raw, work, quarantine, processed, catalog, triplet, or published outputs | `data/...` lifecycle homes |
| Receipts and proofs | `data/receipts/...`, `data/proofs/...` |
| Release decisions | `release/candidates/soil/`, `release/manifests/soil/`, rollback/correction release homes |
| Public API or map code | `apps/governed-api/`, `apps/explorer-web/`, packages |
| Crop/yield, drought, vegetation-stress, hazard, hydrology, or management decisions | Owning domain or reviewed downstream products only |

[⬆ Back to top](#top)

---

## 6. Validation scope

| Scope area | Validation responsibility | Failure behavior |
|---|---|---|
| Source role | Confirm observed, model-assimilated, aggregate, candidate, or derived role is explicit. | Abstain or quarantine. |
| Support type | Confirm station, satellite/model, gridded derivative, survey, pedon, or interpretation support class. | Deny, abstain, or quarantine. |
| Station scope | Confirm station readings remain station-scoped. | Quarantine if emitted as area truth. |
| Grid scope | Confirm SMAP/grid candidates preserve grid metadata and are not station truth. | Quarantine or deny. |
| Depth / layer | Confirm sensor depth or surface/root-zone layer is explicit. | Quarantine if ambiguous. |
| Cadence / time | Confirm source cadence, observed time, retrieved time, processed time, and release time are distinct. | Quarantine if collapsed. |
| QA / uncertainty | Confirm QA flags, uncertainty, and missing values are preserved. | Quarantine or restrict. |
| Freshness | Confirm stale heartbeat/preliminary state is recorded where applicable. | Restrict or quarantine current-context uses. |
| Comparison | Confirm cross-source comparison has receipt and does not merge source roles. | Deny or quarantine. |
| Evidence | Confirm EvidenceBundle references exist for claim-bearing outputs. | Abstain. |
| Release preflight | Confirm validator result does not bypass release workflow. | Deny direct publication. |

[⬆ Back to top](#top)

---

## 7. Lifecycle contract

Every moisture-validation run must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal stance:

1. **Read** approved fixtures, work candidates, quarantine inputs in remediation mode, or processed candidates that need validation.
2. **Validate** source role, support type, station/grid scope, depth/layer, cadence, units, QA, freshness, uncertainty, evidence refs, and policy refs.
3. **Route** failures to quarantine, abstention, denial, restriction, or remediation depending on severity and policy outcome.
4. **Emit receipts** with input refs, validation version, rule ids, method refs, outcomes, and output refs.
5. **Support promotion** only by providing evidence to a governed promotion workflow.
6. **Never publish** directly.

Validation is a gate input. It is not a governed promotion by itself.

[⬆ Back to top](#top)

---

## 8. Required validation gates

Every moisture-validator run must check or explicitly fail closed on:

1. **Input lifecycle gate** — input is fixture, work, quarantine-remediation, or approved processed candidate.
2. **Source descriptor gate** — source identity, role, cadence, rights, and sensitivity posture are known.
3. **Source-role gate** — observed, candidate, model-assimilated, aggregate, and derived records remain distinct.
4. **Support-type gate** — every candidate has a soil support type.
5. **Station/grid/area gate** — station, grid, field, county, map unit, and area scopes remain distinct.
6. **Depth/layer gate** — sensor depth, surface layer, root-zone layer, and horizon/soil profile depth are not substituted.
7. **Cadence/time gate** — native cadence, observed time, valid time, retrieved time, processed time, and release time remain distinct.
8. **QA/uncertainty gate** — quality flags, missing values, confidence, and uncertainty are recorded or quarantine reason is recorded.
9. **Freshness gate** — stale station heartbeat, preliminary NRT, superseded records, and reprocessed replacements are marked where applicable.
10. **No-silent-merge gate** — SCAN, USCRN, Mesonet, SMAP, SSURGO, gSSURGO, and derived products are not silently merged.
11. **Comparison receipt gate** — any comparison, interpolation, aggregation, anomaly, or derived indicator has its own receipt.
12. **Rights and sensitivity gate** — unresolved or restricted inputs cannot proceed to public release preflight.
13. **Evidence gate** — claim-bearing validator conclusions have EvidenceBundle refs or abstain.
14. **Schema and contract gate** — candidate records match accepted schema and contract semantics.
15. **No-direct-publish gate** — validator cannot write to public UI, public API, published layers, or release manifests as a side effect.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended shape:

```text
pipelines/domains/soil/moisture_validator/
├── README.md                         # this file
├── VALIDATOR_CONTRACT.md             # PROPOSED: validator execution contract
├── run_dry_fixture.py                # PROPOSED synthetic/redacted fixture only
├── validate_support_type.py          # PROPOSED
├── validate_source_role.py           # PROPOSED
├── validate_station_grid_scope.py    # PROPOSED
├── validate_depth_layer.py           # PROPOSED
├── validate_cadence_time.py          # PROPOSED
├── validate_units_ranges.py          # PROPOSED
├── validate_qa_uncertainty.py        # PROPOSED
├── validate_freshness.py             # PROPOSED
├── validate_no_silent_merge.py       # PROPOSED
├── validate_comparison_receipt.py    # PROPOSED
├── build_validation_receipt.py       # PROPOSED if not shared
└── adapters/                         # PROPOSED thin lifecycle adapters, no source fetching
```

Declarative specs should live outside this directory:

```text
pipeline_specs/soil/moisture_validator.yaml # PROPOSED / NEEDS VERIFICATION
```

Generated outputs must not be written beside the validator. Use accepted lifecycle homes under `data/`, proof homes under `data/proofs/`, receipt homes under `data/receipts/`, and release homes under `release/`.

[⬆ Back to top](#top)

---

## 10. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Fixture input | `fixtures/domains/soil/moisture_validator/` or accepted fixture home | Synthetic, generalized, or redacted. |
| Work candidate | `data/work/soil/<run_id>/` | Main validation input. |
| Quarantine input | `data/quarantine/soil/<reason>/<run_id>/` | Remediation mode only. |
| Processed candidate | `data/processed/soil/<dataset_id>/<version>/` | Pre-catalog or revalidation input. |
| Validation receipt | `data/receipts/pipeline/soil/moisture_validator/<run_id>.yml` or accepted receipt home | Records rule outcomes, inputs, methods, and refs. |
| Quarantine output | `data/quarantine/soil/<reason>/<run_id>/` | For failed or unsafe candidates. |
| Proof output | `data/proofs/evidence_bundle/` or accepted proof home | Evidence and validation proof refs. |
| Release handoff | `release/candidates/soil/...` | Only if upstream release workflow consumes validator output. |

[⬆ Back to top](#top)

---

## 11. Minimal validation receipt record

The final schema is not defined here. This example shows the minimum information a moisture validation receipt should preserve.

```yaml
schema_version: kfm.soil_moisture_validation_receipt.v1
receipt_id: soil_moisture_validator_<run_id>_<hash>
pipeline_id: domains.soil.moisture_validator
run_id: run_YYYYMMDDThhmmssZ
status: VALIDATION_RECEIPT
input:
  candidate_ref: data/work/soil/<run_id>/<candidate>.yml
  input_hash: sha256:<hash>
  source_id: <source_id>
  source_role: <observed|candidate|model_assimilated_reference|aggregate|derived>
  support_type: <station_soil_moisture|satellite_soil_moisture|model_assimilated_soil_moisture|gridded_derivative_soil|authoritative_static_soil|interpretation>
validator:
  validator_version: v0.1
  spec_ref: pipeline_specs/soil/moisture_validator.yaml
  ruleset_hash: sha256:<hash>
checks:
  support_type: PASS
  source_role: PASS
  station_grid_scope: PASS
  depth_layer: PASS
  cadence_time: PASS
  qa_uncertainty: PASS
  freshness: PASS
  no_silent_merge: PASS
  comparison_receipt: NOT_APPLICABLE
  evidence: ABSTAIN
outcome:
  decision: ABSTAIN
  reason_code: EVIDENCE_BUNDLE_NOT_RESOLVED
  quarantine_ref: null
  promotion_eligible: false
anti_collapse:
  validation_pass_is_publication: false
  station_reading_is_area_truth: false
  satellite_grid_is_station_observation: false
  comparison_is_merge: false
evidence:
  evidence_bundle_ref: null
  citation_state: ABSTAIN
outputs:
  receipt_ref: data/receipts/pipeline/soil/moisture_validator/run_YYYYMMDDThhmmssZ.yml
rollback:
  required_before_publication: true
```

[⬆ Back to top](#top)

---

## 12. Tests, fixtures, receipts, and proofs

Default execution is **fixture-only, synthetic/generalized/redacted, and no-network** until source activation, rule review, support-type review, QA review, and CI coverage are approved.

Recommended tests:

```text
tests/pipelines/domains/soil/moisture_validator/
├── test_no_network_dry_run.py              # PROPOSED
├── test_support_type_required.py           # PROPOSED
├── test_source_role_required.py            # PROPOSED
├── test_station_not_area.py                # PROPOSED
├── test_grid_not_station_truth.py          # PROPOSED
├── test_surface_root_zone_separate.py      # PROPOSED
├── test_depth_not_substituted.py           # PROPOSED
├── test_cadence_not_collapsed.py           # PROPOSED
├── test_quality_flags_required.py          # PROPOSED
├── test_stale_context_restricts.py         # PROPOSED
├── test_no_silent_merge.py                 # PROPOSED
├── test_comparison_requires_receipt.py     # PROPOSED
├── test_missing_evidence_abstains.py       # PROPOSED
├── test_receipt_hashes.py                  # PROPOSED
└── test_no_direct_publish.py               # PROPOSED
```

A dry run should prove fixtures load without network access, support type is required, source roles remain distinct, station/grid/depth/cadence checks run, QA and freshness are preserved, comparison products require receipts, EvidenceBundle gaps produce abstention, receipts are deterministic, and the validator does not write directly to public UI, public API, `data/published/`, or release manifests.

[⬆ Back to top](#top)

---

## 13. Promotion, publication, correction, and rollback

The moisture validator may emit validation receipts. It does not publish.

Required promotion chain:

```text
soil moisture candidate
  -> moisture validation receipt
  -> policy decision
  -> EvidenceBundle closure
  -> processed Soil dataset version or quarantine record
  -> catalog / triplet candidate
  -> release candidate
  -> ReleaseManifest
  -> RollbackCard
  -> public-safe artifact
```

Correction and rollback posture:

- denied, abstained, errored, restricted, stale, superseded, and quarantined validation results remain auditable;
- validator receipts preserve input hashes, rule ids, method refs, and outcomes;
- processed versions are superseded by governed state transition, not hidden overwrite;
- derived products are invalidated if source refs, support-type refs, depth/layer refs, QA refs, freshness refs, method refs, or policy refs drift;
- public artifact rollback is owned by `release/`, not by this directory.

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- fills the blank `pipelines/domains/soil/moisture_validator/README.md` file;
- identifies this directory as a nested executable Soil validation sublane;
- prevents source fetcher, ingest, schema, contract, policy, fixture, test, data, proof, catalog, and release authority from being placed here;
- preserves source role, support type, station/grid/area scope, depth/layer, cadence/time, QA/uncertainty, freshness, evidence, policy, lifecycle, catalog/triplet, release, correction, and rollback boundaries;
- blocks validation-as-publication, station-as-area, grid-as-station, depth/layer substitution, cadence collapse, silent merge, and supportless-value promotion;
- gives maintainers a fixture-first, fail-closed expansion pattern.

Future executable work in this sublane is done only when it has source-descriptor coverage, synthetic/generalized/redacted no-network fixtures, schema-backed validation receipts, contract conformance, source-role/support-type/depth/cadence/QA/freshness/evidence tests, deterministic receipts, no-direct-publish tests, CI coverage, steward-review handoff, and release/correction/rollback documentation.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `SOIL-MOIST-VAL-001` | Should the subdirectory remain `moisture_validator` or be renamed to a hyphenated slug after path convention review? | NEEDS VERIFICATION / ADR |
| `SOIL-MOIST-VAL-002` | Which first-wave inputs should the validator support: SCAN, USCRN, SMAP, Mesonet, or all admitted soil-moisture candidates? | NEEDS VERIFICATION |
| `SOIL-MOIST-VAL-003` | Which validation result schema owns rule ids, failure modes, and quarantine routing? | NEEDS VERIFICATION |
| `SOIL-MOIST-VAL-004` | Which CI job owns moisture-validator invariant tests? | UNKNOWN |
| `SOIL-MOIST-VAL-005` | Should catalog/release preflight checks live here or in a centralized validation package with Soil adapters? | NEEDS VERIFICATION |
| `SOIL-MOIST-VAL-006` | Which receipt type owns cross-source comparison, anomaly, aggregation, or model-fusion validation? | PROPOSED / NEEDS ADR |
| `SOIL-MOIST-VAL-007` | Which public-safe map/API products are allowed after validation, review, and release, and at what support-type/cadence/freshness caveat level? | NEEDS VERIFICATION |

---

## Maintainer note

Start with synthetic/generalized fixture-only dry runs and negative tests. Do not add live source fetching, ingestion logic, silent source merging, supportless values, unreceipted comparisons, public map layers, release handoff automation, or direct API payload generation until source roles, support-type separation, QA/freshness handling, evidence closure, and rollback are proven.
