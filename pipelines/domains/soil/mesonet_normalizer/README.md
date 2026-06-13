<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-soil-mesonet-normalizer-readme
title: Soil Mesonet Normalizer Pipeline README
type: readme
version: v0.1
status: draft
owners:
  - <soil-pipeline-owner>
  - <soil-domain-steward>
  - <kansas-source-steward>
  - <source-steward>
  - <evidence-steward>
  - <policy-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: pipelines/domains/soil/mesonet_normalizer/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipelines/domains/README.md
  - pipelines/domains/soil/README.md
  - pipelines/domains/soil/moisture_validator/README.md
  - docs/domains/soil/ARCHITECTURE.md
  - docs/domains/soil/DATA_LIFECYCLE.md
  - docs/domains/soil/CANONICAL_PATHS.md
  - docs/sources/catalog/kansas/kansas-mesonet.md
  - pipeline_specs/soil/mesonet_normalizer.yaml
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
  - kansas
  - kansas-mesonet
  - mesonet-normalizer
  - station-observation
  - soil-moisture
  - soil-temperature
  - station-health
  - operator-consent
  - support-type-separation
  - source-role
  - evidence
  - policy
  - governance
notes:
  - "This README fills the blank pipelines/domains/soil/mesonet_normalizer path as a Soil-domain executable normalization sublane."
  - "Mesonet normalizer logic is executable implementation support only; it does not own Kansas Mesonet source descriptors, source catalog profiles, source fetching, schemas, policy, lifecycle data, catalog truth, station-health truth, or release decisions."
  - "The subdirectory name uses the requested underscore form mesonet_normalizer; if repo slug rules prefer hyphenated names, record the path decision with ADR/path-map/rollback notes before moving."
  - "Kansas Mesonet station readings must preserve station id, native temporal cadence, soil depth, variable, station-health metadata, operator-consent/rights posture, source role, support type, and receipt lineage."
  - "Station observations are not gridded surfaces, SMAP products, SSURGO survey evidence, SoilGrids modeled surfaces, regulatory determinations, or management advice."
  - "Concrete executable behavior, source linkage, schedules, CI coverage, schema paths, release wiring, and public API/map behavior remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Kansas Mesonet Soil Normalizer Pipeline

> Executable Soil-domain sublane for normalizing admitted Kansas Mesonet soil-moisture and soil-temperature station readings into KFM work candidates, quarantine records, processed candidates, validation handoffs, catalog/triplet handoffs, receipts, and release-review packages — without collapsing point-station observations into gridded surfaces, native cadence into another cadence, one soil depth into another, or operator-consent requirements into assumed rights.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-Mesonet%20soil%20normalizer-2e7d32)
![authority](https://img.shields.io/badge/authority-executable%20logic-0a7ea4)
![support](https://img.shields.io/badge/support--type-station__soil__moisture-d62728)
![rights](https://img.shields.io/badge/operator%20consent-required-d62728)
![publication](https://img.shields.io/badge/publication-release%20gated-d62728)
![ci](https://img.shields.io/badge/CI-TODO-lightgrey)

**Status:** Draft  
**Path:** `pipelines/domains/soil/mesonet_normalizer/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Domain lane:** Soil  
**Sublane:** Kansas Mesonet normalizer  
**Placement posture:** nested executable normalization sublane under `pipelines/domains/soil/`; concrete executable behavior remains `PROPOSED / NEEDS VERIFICATION` unless backed by tests and repo evidence  
**Public posture:** no direct publication; public output requires lifecycle, EvidenceBundle, source-role, support-type tag, station-health metadata, operator-consent/rights closure, native cadence/depth preservation, policy, catalog/triplet, release, correction, and rollback closure

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Mesonet anti-collapse rules](#3-mesonet-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Normalization scope](#6-normalization-scope)
- [7. Lifecycle contract](#7-lifecycle-contract)
- [8. Required gates](#8-required-gates)
- [9. Directory contract](#9-directory-contract)
- [10. Inputs and outputs](#10-inputs-and-outputs)
- [11. Minimal Mesonet normalizer candidate record](#11-minimal-mesonet-normalizer-candidate-record)
- [12. Tests, receipts, and proofs](#12-tests-receipts-and-proofs)
- [13. Promotion, publication, correction, and rollback](#13-promotion-publication-correction-and-rollback)
- [14. Definition of done](#14-definition-of-done)
- [15. Open questions](#15-open-questions)

---

## 1. Purpose

`pipelines/domains/soil/mesonet_normalizer/` is the executable sublane for Kansas Mesonet soil-observation normalization inside the Soil domain.

It supports candidate processing for:

- Kansas Mesonet station metadata needed for soil-variable lineage;
- soil-moisture and soil-temperature observations at admitted sensor depths;
- native temporal cadences such as 5-minute, hourly, and daily records where admitted;
- station-health metadata required before downstream analytics use the feed;
- rights/operator-consent status checks before normalization or release handoff;
- station/depth/cadence-specific observation candidates;
- quality flag, missing-value, unit, timestamp, and timezone normalization;
- support-type tagging as `station_soil_moisture` or the accepted soil-station support label;
- quarantine records for missing station health, missing rights/consent, missing depth, cadence collapse, unknown quality state, schema drift, or support-type failure;
- moisture-validator, catalog/triplet, and release-review handoff packages after evidence, validation, and policy close.

This directory implements or will implement the **how** of Kansas Mesonet Soil normalization. It does not fetch from the Mesonet directly, define source identity, define Soil object meaning, define schemas, encode policy, store lifecycle data, decide public release, or turn station observations into gridded surfaces, station-health truth, crop/yield truth, drought determination, or management advice.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable pipeline logic: the **how**. | CONFIRMED root responsibility |
| Why `domains/soil/`? | Soil is the domain lane; Soil docs place executable logic under `pipelines/domains/soil/`. | CONFIRMED documentation pattern; behavior NEEDS VERIFICATION |
| Why `mesonet_normalizer/`? | This is a narrow executable sublane for Kansas Mesonet soil-observation normalization under Soil. | PROPOSED / NEEDS VERIFICATION |
| Is this a source fetcher? | No. Source fetching belongs in `connectors/kansas/kansas-mesonet/` or an accepted source-edge home. This sublane reads admitted lifecycle inputs or fixtures. | CONFIRMED separation |
| Where does the source profile live? | `docs/sources/catalog/kansas/kansas-mesonet.md`. | CONFIRMED source-doc path |
| Where does a declarative run spec live? | `pipeline_specs/soil/mesonet_normalizer.yaml` or accepted spec home. | PROPOSED / NEEDS VERIFICATION |
| Where do schemas and contracts live? | `schemas/contracts/v1/domains/soil/` and `contracts/domains/soil/` or accepted homes. | PROPOSED / NEEDS VERIFICATION |
| Can this sublane publish? | No. It may prepare candidates, validation handoffs, and receipts only through governed workflow. | CONFIRMED doctrine posture |

> [!IMPORTANT]
> Mesonet normalizer code is subordinate to SourceDescriptor, source role, operator-consent/rights records, station-health metadata, native cadence, soil depth, QA flags, support-type tagging, EvidenceBundle closure, policy decisions, release manifests, correction notices, and rollback cards. A successful normalization run is not public release.

[⬆ Back to top](#top)

---

## 3. Mesonet anti-collapse rules

Kansas Mesonet must remain in-situ, point-station observed evidence unless a downstream receipt proves a separate derivative.

Disallowed collapses:

```text
station reading -> gridded surface
station reading -> countywide value
station reading -> field-specific fact
5 cm value -> 10/20/50 cm value
5-minute record -> hourly/daily record without aggregation receipt
station-health missing -> analytics-ready feed
unknown operator consent -> release-ready rights
Mesonet observed value -> SMAP / SCAN / USCRN / SoilGrids value
comparison check -> silent merged product
generated summary -> evidence
```

Required distinctions:

- station id and station geometry remain station-scoped;
- native cadence is preserved;
- sensor depth is explicit;
- station-health metadata is present before analytics handoff;
- operator-consent/rights status is known before release handoff;
- source role remains observed for admitted in-situ station readings;
- modeled, aggregated, interpolated, fused, or anomaly products become separate artifacts with separate receipts.

[⬆ Back to top](#top)

---

## 4. What belongs here

Files belong here when their primary responsibility is executable Kansas Mesonet Soil normalization.

Appropriate contents include:

- fixture-only dry-run entrypoints for Mesonet normalization;
- station metadata normalization helpers scoped to Soil;
- station-health metadata checks and handoff helpers;
- variable/depth/cadence parsing helpers;
- timestamp, timezone, unit, quality flag, and missing-value normalization helpers;
- source-role, rights/consent, and support-type validators;
- station-as-area, depth-collapse, cadence-collapse, station-health, and no-silent-merge validators;
- quarantine routing helpers for missing rights/consent, missing station health, missing depth, unsupported cadence, quality-state uncertainty, or validation failure;
- receipt emitters, if not shared;
- handoff helpers for `pipelines/domains/soil/moisture_validator/`, if not centralized elsewhere;
- catalog/triplet handoff helpers, if not centralized in `pipelines/catalog/`;
- thin adapters that read governed lifecycle inputs, not live Mesonet endpoints.

A good placement test:

> If the code transforms admitted Kansas Mesonet lifecycle inputs into Soil observation candidates, quarantine records, validation handoffs, processed records, receipts, or catalog handoffs, it may belong here. If it fetches source data, defines source identity, defines schemas, encodes policy, creates public artifacts, or approves release, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Kansas Mesonet fetcher / source-edge connector | `connectors/kansas/kansas-mesonet/` or accepted connector home |
| Kansas Mesonet source profile | `docs/sources/catalog/kansas/kansas-mesonet.md` |
| Source descriptors / source registry entries | `data/registry/sources/soil/`, `data/registry/sources/kansas/`, or accepted registry home |
| Soil architecture and doctrine | `docs/domains/soil/...` |
| Object meaning contracts | `contracts/domains/soil/...` |
| JSON Schemas | `schemas/contracts/v1/domains/soil/...` |
| Policy bundles, consent/rights rules, release rules | `policy/domains/soil/`, rights, sensitivity, and release policy roots |
| Declarative run specs | `pipeline_specs/soil/...` |
| Fixtures | `fixtures/domains/soil/mesonet_normalizer/` or accepted fixture home |
| Tests | `tests/pipelines/domains/soil/mesonet_normalizer/` or accepted test home |
| Raw, work, quarantine, processed, catalog, triplet, or published outputs | `data/...` lifecycle homes |
| Receipts and proofs | `data/receipts/...`, `data/proofs/...` |
| Release decisions | `release/candidates/soil/`, `release/manifests/soil/`, rollback/correction release homes |
| Public API or map code | `apps/governed-api/`, `apps/explorer-web/`, packages |
| SMAP, SCAN, USCRN, SSURGO, gSSURGO, SoilGrids, crop/yield, drought, vegetation-stress, or hazard products | Owning source/domain lanes or reviewed downstream products only |

[⬆ Back to top](#top)

---

## 6. Normalization scope

| Scope area | Normalizer responsibility | Failure behavior |
|---|---|---|
| Station metadata | Normalize station id, location ref, and source metadata. | Quarantine if missing required identity. |
| Station health | Require station-health metadata before analytics handoff. | Deny analytics handoff or quarantine. |
| Soil moisture | Normalize station/depth/cadence observations with units and QA. | Requires depth and support type. |
| Soil temperature | Normalize station/depth/cadence observations with units and QA. | Requires depth and support type. |
| Native cadence | Preserve 5-minute, hourly, daily, or admitted cadence. | Aggregation requires receipt. |
| Operator consent / rights | Preserve rights and consent posture. | Unknown rights default to deny/restrict. |
| Source role | Preserve admitted station readings as observed. | Reject if silently modeled/aggregated. |
| Validator handoff | Emit records ready for moisture validation. | Validator pass does not publish. |
| Catalog/triplet handoff | Prepare restricted or public-safe candidates after evidence closure. | Projection does not replace canonical review state. |

[⬆ Back to top](#top)

---

## 7. Lifecycle contract

Every Mesonet normalizer run must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal stance:

1. **Read** approved fixtures, immutable raw captures, work candidates, quarantine inputs in remediation mode, or prior processed baselines.
2. **Normalize** into station-scoped Soil observation candidates with source role, support type, variable, depth, cadence, unit, quality flag, station health, rights/consent state, temporal scope, evidence refs, and receipt refs.
3. **Quarantine** unresolved rights/consent, missing station identity, missing station health, missing variable, missing depth, missing cadence, unit ambiguity, quality-state failure, support-type failure, schema drift, or validation failure.
4. **Handoff to validation** only after normalizer-level checks close; validation remains a separate gate.
5. **Prepare catalog/triplet handoffs** only after processed-state and evidence closure, and only with station/depth/cadence/rights caveats.
6. **Publish** only through release decisions, public-safe artifacts, rollback targets, and correction paths.

Promotion is a governed state transition with receipts and review evidence, not a file move.

[⬆ Back to top](#top)

---

## 8. Required gates

Every Mesonet normalizer run must check or explicitly fail closed on:

1. **Source descriptor gate** — Kansas Mesonet source identity, role, cadence, rights, operator-consent state, and sensitivity posture are known.
2. **Source-role gate** — native admitted station records remain observed records.
3. **Station-scope gate** — station reading is not gridded, countywide, or field truth.
4. **Station-health gate** — station-health metadata exists before downstream analytics handoff.
5. **Variable gate** — each candidate names the observed variable.
6. **Depth gate** — depth-aware soil variables preserve 5/10/20/50 cm or admitted source depths and do not substitute one depth for another.
7. **Cadence gate** — 5-minute, hourly, daily, or other admitted cadence products remain distinct unless an aggregation receipt exists.
8. **Unit and quality gate** — units, missing values, quality flags, and station-health fields are preserved or quarantined.
9. **Rights/consent gate** — unknown or unresolved operator consent/rights denies or restricts downstream use.
10. **Support-type gate** — Mesonet soil observations carry the accepted station soil support label.
11. **No-silent-merge gate** — Mesonet is never silently merged with SMAP, SCAN, USCRN, SSURGO, gSSURGO, SoilGrids, crop, drought, or vegetation-stress products.
12. **Derived-artifact gate** — aggregation, interpolation, gridding, comparison, anomaly, or fusion products require a separate receipt.
13. **Schema, contract, evidence, policy, validation, receipt, catalog/triplet, and release gates** — all must close or the run abstains, denies, or quarantines.
14. **No-direct-publish gate** — no writes to public UI, public API, or `data/published/` without release workflow authority.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended shape:

```text
pipelines/domains/soil/mesonet_normalizer/
├── README.md                         # this file
├── PIPELINE_CONTRACT.md              # PROPOSED: sublane execution contract
├── run_dry_fixture.py                # PROPOSED synthetic/redacted fixture only
├── normalize_station_metadata.py     # PROPOSED
├── normalize_station_health.py       # PROPOSED
├── normalize_soil_observation.py     # PROPOSED
├── parse_variable_depth_cadence.py   # PROPOSED
├── normalize_time_basis.py           # PROPOSED
├── normalize_units_quality.py        # PROPOSED
├── validate_operator_consent.py      # PROPOSED
├── validate_station_scope.py         # PROPOSED
├── validate_depth_cadence.py         # PROPOSED
├── validate_support_type.py          # PROPOSED
├── handoff_to_moisture_validator.py  # PROPOSED
├── build_catalog_handoff.py          # PROPOSED if not centralized in pipelines/catalog/
├── emit_receipt.py                   # PROPOSED only if not shared
└── adapters/                         # PROPOSED thin lifecycle adapters, no source fetching
```

Declarative specs should live outside this directory:

```text
pipeline_specs/soil/mesonet_normalizer.yaml # PROPOSED / NEEDS VERIFICATION
```

Generated outputs must not be written beside the normalizer. Use accepted lifecycle homes under `data/`, proof homes under `data/proofs/`, receipt homes under `data/receipts/`, and release homes under `release/`.

[⬆ Back to top](#top)

---

## 10. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Fixture input | `fixtures/domains/soil/mesonet_normalizer/` or accepted fixture home | Synthetic, generalized, or redacted. |
| Raw Mesonet capture | `data/raw/soil/<source_id>/<run_id>/` or accepted Kansas raw home | Immutable source-edge capture with source descriptor and receipt. |
| Work candidate | `data/work/soil/<run_id>/` | Candidate only. |
| Quarantine record | `data/quarantine/soil/<reason>/<run_id>/` | Failed, restricted, unresolved, or unsafe material. |
| Normalized candidate | `data/work/soil/<run_id>/` or accepted work home | Handoff to moisture validator. |
| Processed observations | `data/processed/soil/<dataset_id>/<version>/` | Validated/restricted; not automatically public. |
| Receipts / proofs | `data/receipts/...`, `data/proofs/...` | Required for auditable promotion and release review. |
| Release handoff | `release/candidates/soil/...` | Only through release workflow. |

[⬆ Back to top](#top)

---

## 11. Minimal Mesonet normalizer candidate record

The final schema is not defined here. This example shows the minimum information a Mesonet normalizer candidate should preserve.

```yaml
schema_version: kfm.soil_mesonet_normalizer_candidate.v1
candidate_id: soil_mesonet_<station_id>_<variable>_<depth>_<timestamp_hash>
pipeline_id: domains.soil.mesonet_normalizer
run_id: run_YYYYMMDDThhmmssZ
status: WORK_CANDIDATE
source:
  source_id: kansas_mesonet
  source_role: observed
  lifecycle_ref: data/raw/soil/kansas_mesonet/<run_id>/
  input_hash: sha256:<hash>
  rights_state: needs_review
  operator_consent_ref: null
station:
  station_id: <station_id>
  station_ref: <station_ref>
  geometry_scope: station_point
  station_health_ref: null
observation:
  variable: <soil_moisture|soil_temperature|other_soil_variable>
  support_type: station_soil_moisture
  depth_cm: <5|10|20|50|other_admitted_depth>
  cadence: <native|five_minute|hourly|daily|other>
  observed_at: YYYY-MM-DDThh:mm:ssZ
  value: <number_or_null>
  unit: <unit>
  quality_flags: []
anti_collapse:
  station_reading_is_area_truth: false
  depth_substitution_allowed: false
  cadence_substitution_allowed: false
  rights_assumed_without_operator_consent: false
  generated_summary_is_evidence: false
policy:
  outcome: ABSTAIN
  reason_code: SOURCE_DESCRIPTOR_RIGHTS_STATION_HEALTH_OR_EVIDENCE_NOT_RESOLVED
evidence:
  evidence_bundle_ref: null
  citation_state: ABSTAIN
outputs:
  candidate_record: data/work/soil/run_YYYYMMDDThhmmssZ/mesonet_candidate.yml
  receipt: data/receipts/pipeline/soil/mesonet_normalizer/run_YYYYMMDDThhmmssZ.yml
rollback:
  required_before_publication: true
```

[⬆ Back to top](#top)

---

## 12. Tests, receipts, and proofs

Default execution is **fixture-only, synthetic/generalized/redacted, and no-network** until source activation, operator-consent review, rights review, station-health review, support-type review, quality review, and CI coverage are approved.

Recommended tests:

```text
tests/pipelines/domains/soil/mesonet_normalizer/
├── test_no_network_dry_run.py              # PROPOSED
├── test_source_role_observed.py            # PROPOSED
├── test_operator_consent_required.py       # PROPOSED
├── test_station_health_required.py         # PROPOSED
├── test_station_not_area.py                # PROPOSED
├── test_depth_required_for_soil_variables.py # PROPOSED
├── test_depth_not_substituted.py           # PROPOSED
├── test_cadence_not_collapsed.py           # PROPOSED
├── test_quality_flags_preserved.py         # PROPOSED
├── test_support_type_required.py           # PROPOSED
├── test_no_silent_smap_merge.py            # PROPOSED
├── test_handoff_to_moisture_validator.py   # PROPOSED
├── test_missing_evidence_abstains.py       # PROPOSED
├── test_receipt_hashes.py                  # PROPOSED
└── test_no_direct_publish.py               # PROPOSED
```

A dry run should prove fixtures load without network access, admitted records remain observed station readings, operator-consent and station-health gates run, depth and cadence are preserved, missing support type is denied or quarantined, quality flags are retained, EvidenceBundle gaps produce abstention, receipts are deterministic, and no run writes directly to public UI, public API, `data/published/`, or release manifests.

[⬆ Back to top](#top)

---

## 13. Promotion, publication, correction, and rollback

Mesonet normalization may prepare candidates. It does not publish.

Required promotion chain:

```text
Kansas Mesonet raw/work input
  -> station/depth/cadence observation candidate
  -> normalizer receipt
  -> moisture validation receipt
  -> policy decision
  -> EvidenceBundle closure
  -> processed Soil observation dataset version
  -> catalog / triplet candidate
  -> release candidate
  -> ReleaseManifest
  -> RollbackCard
  -> public-safe artifact
```

Correction and rollback posture:

- denied, abstained, errored, rights-restricted, station-health-failed, and quarantined runs remain auditable;
- candidate rollback preserves receipts and proof state;
- processed versions are superseded by governed state transition, not hidden overwrite;
- derived products are invalidated if station refs, depth refs, cadence refs, quality refs, station-health refs, rights refs, support-type refs, method refs, or policy refs drift;
- public artifact rollback is owned by `release/`, not by this directory.

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- fills the blank `pipelines/domains/soil/mesonet_normalizer/README.md` file;
- identifies this directory as a nested executable Soil normalization sublane;
- prevents source fetcher, source-profile, schema, contract, policy, fixture, test, data, proof, catalog, and release authority from being placed here;
- preserves source role, operator-consent/rights, station-health, station scope, variable/depth/cadence, units/quality, support type, evidence, policy, lifecycle, validation handoff, catalog/triplet, release, correction, and rollback boundaries;
- blocks station-as-area, depth-collapse, cadence-collapse, no-consent release, no-station-health analytics, silent merge, and supportless-value promotion;
- gives maintainers a fixture-first, fail-closed expansion pattern.

Future executable work in this sublane is done only when it has source-descriptor coverage, synthetic/generalized/redacted no-network fixtures, schema-backed candidates, contract conformance, source-role/rights/station-health/support-type/depth/cadence/quality/evidence tests, deterministic receipts, no-direct-publish tests, CI coverage, steward-review handoff, and release/correction/rollback documentation.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `SOIL-MESONET-001` | Should the subdirectory remain `mesonet_normalizer` or be renamed to a hyphenated slug after path convention review? | NEEDS VERIFICATION / ADR |
| `SOIL-MESONET-002` | Which connector or source-edge job owns Kansas Mesonet retrieval before this normalizer reads lifecycle inputs? | NEEDS VERIFICATION |
| `SOIL-MESONET-003` | Which station variables, depths, cadence classes, station-health fields, and quality flags are first-wave approved for fixture-only dry runs? | NEEDS VERIFICATION |
| `SOIL-MESONET-004` | What exact operator-consent record is required before runtime use? | NEEDS VERIFICATION |
| `SOIL-MESONET-005` | Which CI job owns Mesonet normalizer invariant tests? | UNKNOWN |
| `SOIL-MESONET-006` | Should catalog handoff logic live here or in centralized `pipelines/catalog/` with a Mesonet adapter? | NEEDS VERIFICATION |
| `SOIL-MESONET-007` | Which public-safe map/API products are allowed after review and release, and at what station/depth/cadence/station-health caveat level? | NEEDS VERIFICATION |
| `SOIL-MESONET-008` | Which receipt type owns Mesonet-to-SMAP, Mesonet-to-SCAN, Mesonet-to-USCRN, or station-to-surface comparison products? | PROPOSED / NEEDS ADR |

---

## Maintainer note

Start with synthetic/generalized fixture-only dry runs and negative tests. Do not add live Mesonet fetching, station-as-area outputs, depth substitution, cadence substitution, no-consent release paths, analytics without station-health metadata, derived surfaces, public map layers, release handoff automation, or direct API payload generation until source roles, operator rights, support-type separation, quality validation, station health, evidence closure, and rollback are proven.
