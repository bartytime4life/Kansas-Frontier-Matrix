<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-hydrology-ingest-usgs-water-readme
title: Hydrology USGS Water Ingest Pipeline README
type: readme
version: v0.1
status: draft
owners:
  - <hydrology-pipeline-owner>
  - <hydrology-domain-steward>
  - <usgs-source-steward>
  - <hazards-domain-steward>
  - <evidence-steward>
  - <policy-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: pipelines/domains/hydrology/ingest_usgs_water/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipelines/domains/README.md
  - pipelines/domains/hydrology/README.md
  - pipelines/domains/hydrology/ingest/README.md
  - pipelines/domains/hydrology/catalog/README.md
  - pipelines/domains/hydrology/catalog_close/README.md
  - docs/domains/hydrology/README.md
  - docs/domains/hydrology/DATA_LIFECYCLE.md
  - docs/domains/hydrology/PUBLICATION_POSTURE.md
  - docs/sources/catalog/usgs/nwis-water.md
  - docs/sources/catalog/usgs/README.md
  - pipeline_specs/hydrology/ingest_usgs_water.yaml
  - contracts/domains/hydrology/
  - schemas/contracts/v1/domains/hydrology/
  - policy/domains/hydrology/
  - policy/sensitivity/hydrology/
  - policy/sensitivity/infrastructure/
  - data/raw/hydrology/
  - data/work/hydrology/
  - data/quarantine/hydrology/
  - data/processed/hydrology/
  - data/catalog/domain/hydrology/
  - data/triplets/hydrology/
  - data/registry/sources/hydrology/
  - data/registry/sources/usgs/
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
  - usgs
  - water-data
  - nwis
  - api-waterdata
  - instantaneous-values
  - daily-values
  - peak-flows
  - water-quality
  - groundwater
  - provisional-approved
  - source-role
  - evidence
  - policy
  - governance
notes:
  - "This README fills the blank pipelines/domains/hydrology/ingest_usgs_water path as a nested executable USGS Water ingest sublane."
  - "USGS Water ingest logic is executable implementation support only; it does not own USGS source descriptors, source catalog profiles, connector/fetch logic, schemas, policy, lifecycle data, catalog truth, hydrologic truth, operational decisions, or release decisions."
  - "The subdirectory name uses the requested underscore form ingest_usgs_water; if repo slug rules prefer hyphenated names, record the path decision with ADR/path-map/rollback notes before moving."
  - "USGS Water source-role split must be preserved: instantaneous values and peak flows are observed, daily values and annual statistics are aggregates, and site metadata is administrative."
  - "Provisional and approved values are distinct lifecycle states and must not be silently substituted."
  - "Modern api.waterdata.usgs.gov and legacy waterservices.usgs.gov / NWIS endpoints must be handled with cutover discipline until the source descriptor closes migration posture."
  - "Concrete executable behavior, source linkage, schedules, CI coverage, schema paths, release wiring, and public API/map behavior remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# USGS Water Hydrology Ingest Pipeline

> Executable Hydrology sublane for normalizing admitted USGS Water Data / NWIS source captures into governed work candidates, quarantine records, validation handoffs, receipts, and downstream catalog/release-review packages — without collapsing provisional values into approved values, instantaneous observations into daily aggregates, site metadata into observations, or observed readings into official current guidance.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-USGS%20Water%20hydrology%20ingest-2e7d32)
![authority](https://img.shields.io/badge/authority-executable%20logic-0a7ea4)
![source-role](https://img.shields.io/badge/observed%20%E2%89%A0%20aggregate-d62728)
![approval](https://img.shields.io/badge/provisional%20%E2%89%A0%20approved-d62728)
![publication](https://img.shields.io/badge/publication-release%20gated-d62728)
![ci](https://img.shields.io/badge/CI-TODO-lightgrey)

**Status:** Draft  
**Path:** `pipelines/domains/hydrology/ingest_usgs_water/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Domain lane:** Hydrology  
**Sublane:** USGS Water ingest / station time-series normalization  
**Placement posture:** nested executable sublane under `pipelines/domains/hydrology/`; concrete executable behavior remains `PROPOSED / NEEDS VERIFICATION` unless backed by tests and repo evidence  
**Public posture:** no direct publication; USGS Water-derived output is work/quarantine/validation input only and requires downstream evidence, policy, catalog, release, correction, and rollback closure

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. USGS Water anti-collapse rules](#3-usgs-water-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Ingest scope](#6-ingest-scope)
- [7. Lifecycle contract](#7-lifecycle-contract)
- [8. Required gates](#8-required-gates)
- [9. Directory contract](#9-directory-contract)
- [10. Inputs and outputs](#10-inputs-and-outputs)
- [11. Minimal USGS Water ingest candidate record](#11-minimal-usgs-water-ingest-candidate-record)
- [12. Tests, fixtures, receipts, and proofs](#12-tests-fixtures-receipts-and-proofs)
- [13. Promotion, publication, correction, and rollback](#13-promotion-publication-correction-and-rollback)
- [14. Definition of done](#14-definition-of-done)
- [15. Open questions](#15-open-questions)

---

## 1. Purpose

`pipelines/domains/hydrology/ingest_usgs_water/` is the executable sublane for USGS Water Data / NWIS normalization inside the Hydrology domain.

It supports candidate processing for:

- USGS site metadata, station identity, site location, datum, and monitoring-program context;
- instantaneous values (IV) such as discharge, gage height, water temperature, precipitation, and groundwater level where admitted;
- daily values (DV) as aggregate products, not point-in-time observations;
- annual statistics as aggregate products;
- peak-flow records with uncertainty or qualification metadata where present;
- water-quality records with method metadata where admitted;
- parameter-code, unit, qualifier, approval-status, time-zone, and cadence preservation;
- modern API and legacy NWIS endpoint lineage during migration/cutover windows;
- quarantine records for missing site identity, missing parameter code, missing approval status, provisional/approved collapse, observed/aggregate collapse, cadence/time ambiguity, unit ambiguity, schema drift, or validation failure;
- validation, catalog, triplet, EvidenceBundle, release-review, correction, and rollback handoff packages.

This directory implements or will implement the **how** of USGS Water ingest normalization. It does not fetch USGS data directly, define USGS source identity, define Hydrology object meaning, define schemas, encode policy, store lifecycle data, decide release, issue current operational guidance, enforce water rights, or certify engineering use.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable pipeline logic: the **how**. | CONFIRMED root responsibility |
| Why `domains/hydrology/`? | Hydrology is the domain lane used by Hydrology docs and the Hydrology pipeline README. | CONFIRMED documentation pattern; behavior NEEDS VERIFICATION |
| Why `ingest_usgs_water/`? | This is a narrow executable sublane for USGS Water / NWIS station time-series input normalization. | PROPOSED / NEEDS VERIFICATION |
| Is this a connector? | No. Source fetching belongs in `connectors/usgs/` or an accepted source-edge home. This sublane reads admitted lifecycle inputs or fixtures. | CONFIRMED separation |
| Does this own the USGS Water source profile? | No. Source profile content lives under `docs/sources/catalog/usgs/nwis-water.md` and source descriptors live in registry homes. | CONFIRMED source-doc separation |
| Where do declarative run specs live? | `pipeline_specs/hydrology/ingest_usgs_water.yaml` or accepted spec home. | PROPOSED / NEEDS VERIFICATION |
| Can this sublane publish? | No. It may emit work candidates, quarantine records, validation handoffs, and receipts only through governed workflow. | CONFIRMED doctrine posture |

> [!IMPORTANT]
> USGS Water ingest is not publication, not a safety bulletin, not a water-rights determination, not engineering certification, and not release approval. It prepares evidence-bound site/time-series candidates for downstream validation and review.

[⬆ Back to top](#top)

---

## 3. USGS Water anti-collapse rules

USGS Water ingest must preserve source-role, approval status, site identity, parameter semantics, and time basis.

Disallowed collapses:

```text
provisional IV -> approved IV
IV observation -> DV aggregate
DV aggregate -> point-in-time observation
annual statistic -> daily value
site metadata -> observed reading
parameter code -> plain-language value without code lineage
stage / gage height -> discharge without rating/method support
gauge reading -> official warning or operational decision
legacy endpoint response -> modern endpoint response without cutover receipt
generated summary -> evidence
ingest receipt -> release approval
```

Required distinctions:

- site metadata is administrative;
- instantaneous and peak readings are observed records;
- daily values, annual statistics, and summaries are aggregates;
- provisional and approved values remain distinct approval states;
- parameter codes, units, qualifiers, time zones, observed time, retrieval time, and processing time are explicit;
- modern and legacy endpoint lineage is recorded during API migration;
- derived products such as ratings, conversions, comparisons, anomalies, and aggregates require separate method or aggregation receipts.

[⬆ Back to top](#top)

---

## 4. What belongs here

Files belong here when their primary responsibility is executable USGS Water ingest normalization.

Appropriate contents include:

- fixture-only USGS Water ingest entrypoints;
- site metadata normalizers;
- instantaneous-value normalizers;
- daily-value and annual-statistic aggregate normalizers;
- peak-flow and water-quality candidate normalizers;
- parameter-code, unit, qualifier, timezone, cadence, and approval-status helpers;
- provisional-vs-approved lifecycle validators;
- observed-vs-aggregate source-role validators;
- legacy-vs-modern endpoint lineage validators;
- site/time-series identity validators;
- quarantine routing helpers for missing site id, missing parameter code, approval-state gaps, unit ambiguity, time ambiguity, source-role collapse, evidence gaps, or schema failures;
- receipt emitters, if not shared;
- handoff helpers for Hydrology validation, catalog, and triplet stages;
- thin adapters that read governed lifecycle inputs, not live USGS endpoints.

A good placement test:

> If the code transforms admitted USGS Water lifecycle inputs into Hydrology site/time-series candidates, quarantine records, validation handoffs, receipts, or downstream handoff packages, it may belong here. If it fetches source data, defines schemas, stores lifecycle data, writes catalog records, issues guidance, or approves release, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| USGS source fetchers / connectors | `connectors/usgs/` or accepted connector home |
| USGS Water source catalog profile | `docs/sources/catalog/usgs/nwis-water.md` |
| Source descriptors / source registry entries | `data/registry/sources/usgs/`, `data/registry/sources/hydrology/`, or approved registry home |
| Hydrology architecture and doctrine | `docs/domains/hydrology/...` |
| Hazards operational context doctrine | `docs/domains/hazards/...` or accepted hazards docs home |
| Object meaning contracts | `contracts/domains/hydrology/` or accepted contract home |
| JSON Schemas | `schemas/contracts/v1/domains/hydrology/` or accepted schema home |
| Policy, rights, sensitivity, release rules | `policy/...` responsibility roots |
| Declarative run specs | `pipeline_specs/hydrology/...` |
| Fixtures | `fixtures/domains/hydrology/ingest_usgs_water/` or accepted fixture home |
| Tests | `tests/pipelines/domains/hydrology/ingest_usgs_water/` or accepted test home |
| Raw, work, quarantine, processed, catalog, triplet, or published outputs | `data/...` lifecycle homes |
| Catalog/triplet builders | `pipelines/domains/hydrology/catalog/`, `pipelines/catalog/`, or accepted graph/catalog adapter home |
| Catalog close / release preflight | `pipelines/domains/hydrology/catalog_close/` or release workflow homes |
| Receipts and proofs | `data/receipts/...`, `data/proofs/...` |
| Release decisions and manifests | `release/...` responsibility roots |
| Public API, map code, or public layers | `apps/governed-api/`, `apps/explorer-web/`, `data/published/...`, or release-controlled artifact homes |

[⬆ Back to top](#top)

---

## 6. Ingest scope

| Scope area | Ingest responsibility | Failure behavior |
|---|---|---|
| Site metadata | Preserve site id, location, datum, active/inactive status, and program context. | Quarantine if identity is missing. |
| Instantaneous values | Normalize observed readings with site id, parameter code, value, unit, qualifiers, time, and approval status. | Quarantine on missing parameter/time/unit/approval state. |
| Daily values | Normalize aggregate daily records with aggregation semantics. | Deny if cited as point observation. |
| Annual statistics | Normalize aggregate annual records with statistic semantics. | Deny if cited as daily/instantaneous value. |
| Peak flows | Preserve observed peak and uncertainty/qualification fields where present. | Restrict or quarantine on uncertainty gaps. |
| Water quality | Preserve method, unit, sample time, and parameter metadata. | Quarantine on method/parameter ambiguity. |
| API migration | Preserve modern/legacy endpoint source lineage. | Quarantine on untracked cutover ambiguity. |
| Hydrology/Hazards handoff | Prepare context candidates with caveats. | No direct warning, enforcement, or operational decision. |

[⬆ Back to top](#top)

---

## 7. Lifecycle contract

Every USGS Water ingest run must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal stance:

1. **Read** approved fixtures, immutable raw captures, work inputs, quarantine inputs in remediation mode, or prior processed USGS Water baselines.
2. **Normalize** into Hydrology work candidates with source role, site id, parameter code, approval status, time basis, unit, qualifier, endpoint lineage, evidence refs, policy refs, and receipt refs.
3. **Quarantine** missing source descriptor, missing site id, missing parameter code, unsupported source role, provisional/approved collapse, observed/aggregate collapse, unit ambiguity, time ambiguity, rights failure, schema drift, or validation failure.
4. **Emit receipts** with input refs, source refs, endpoint refs, parameter refs, approval-state refs, validation refs, output refs, and outcomes.
5. **Support promotion** only by feeding downstream Hydrology validation and review workflows.
6. **Never publish directly.**

USGS Water ingest is an early lifecycle transformation. It is not processed-state promotion, catalog closure, release approval, or public artifact creation by itself.

[⬆ Back to top](#top)

---

## 8. Required gates

Every USGS Water ingest run must check or explicitly fail closed on:

1. **Input lifecycle gate** — input is fixture, raw capture, work input, quarantine-remediation input, or accepted baseline.
2. **Source descriptor gate** — USGS Water source identity, API surface, role, cadence, rights, and sensitivity posture are known.
3. **Endpoint migration gate** — modern and legacy endpoint lineage is explicit during any dual-endpoint window.
4. **Site identity gate** — USGS site id, site metadata, location, and datum are present where required.
5. **Source-role gate** — site metadata, observed readings, peak readings, daily values, annual statistics, and generated summaries remain distinct.
6. **Approval-status gate** — provisional and approved values are never silently substituted.
7. **Parameter-code gate** — parameter code, variable meaning, units, and qualifiers are preserved.
8. **Time/cadence gate** — observation time, valid time, retrieval time, processing time, cadence, and stale-state are distinct.
9. **Aggregate gate** — daily values and annual statistics carry aggregation semantics and receipts where used downstream.
10. **Water-quality method gate** — sample/method metadata is present for claim-bearing water-quality use.
11. **Evidence gate** — claim-bearing downstream candidates can resolve evidence refs or abstain.
12. **Rights and sensitivity gate** — unresolved rights or restricted context cannot proceed to public-safe handoff.
13. **Schema/contract gate** — candidates match accepted schema and Hydrology semantics.
14. **No-direct-publish gate** — no writes to public UI, public API, catalog store, published layers, or release manifests as an ingest side effect.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended shape:

```text
pipelines/domains/hydrology/ingest_usgs_water/
├── README.md                         # this file
├── INGEST_CONTRACT.md                # PROPOSED: USGS Water ingest execution contract
├── run_dry_fixture.py                # PROPOSED synthetic/redacted fixture only
├── normalize_site_metadata.py        # PROPOSED
├── normalize_instantaneous_values.py # PROPOSED
├── normalize_daily_values.py         # PROPOSED
├── normalize_annual_statistics.py    # PROPOSED
├── normalize_peak_flows.py           # PROPOSED
├── normalize_water_quality.py        # PROPOSED
├── validate_source_role_split.py     # PROPOSED
├── validate_provisional_approved.py  # PROPOSED
├── validate_parameter_codes.py       # PROPOSED
├── validate_endpoint_lineage.py      # PROPOSED
├── route_quarantine.py               # PROPOSED
├── emit_receipt.py                   # PROPOSED only if not shared
└── adapters/                         # PROPOSED thin lifecycle adapters, no source fetching
```

Declarative specs should live outside this directory:

```text
pipeline_specs/hydrology/ingest_usgs_water.yaml # PROPOSED / NEEDS VERIFICATION
```

Generated outputs must not be written beside the ingest code. Use accepted lifecycle homes under `data/work/hydrology/`, `data/quarantine/hydrology/`, `data/processed/hydrology/`, proof homes under `data/proofs/`, receipt homes under `data/receipts/`, and release homes under `release/`.

[⬆ Back to top](#top)

---

## 10. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Fixture input | `fixtures/domains/hydrology/ingest_usgs_water/` or accepted fixture home | Synthetic, generalized, or redacted. |
| Raw USGS Water capture | `data/raw/hydrology/<source_id>/<run_id>/` or accepted USGS raw home | Immutable source-edge capture with descriptor and receipt. |
| Work candidate | `data/work/hydrology/<run_id>/` | Candidate only. |
| Quarantine record | `data/quarantine/hydrology/<reason>/<run_id>/` | Failed, restricted, unresolved, or unsafe material. |
| Processed observation handoff | `data/processed/hydrology/<dataset_id>/<version>/` | Only after downstream validation and promotion gates. |
| Receipt | `data/receipts/pipeline/hydrology/ingest_usgs_water/<run_id>.yml` or accepted receipt home | Records input refs, site ids, parameter codes, approval states, and outputs. |
| Evidence proof | `data/proofs/evidence_bundle/` or accepted proof home | Required for claim-bearing downstream records. |
| Catalog handoff | `pipelines/domains/hydrology/catalog/` via lifecycle data homes | No direct catalog writes from ingest unless approved by spec. |

[⬆ Back to top](#top)

---

## 11. Minimal USGS Water ingest candidate record

The final schema is not defined here. This example shows the minimum information a USGS Water ingest candidate should preserve.

```yaml
schema_version: kfm.hydrology_usgs_water_ingest_candidate.v1
candidate_id: hydrology_usgs_water_<site_id>_<parameter_code>_<timestamp_or_period>_<run_id>
pipeline_id: domains.hydrology.ingest_usgs_water
run_id: run_YYYYMMDDThhmmssZ
status: WORK_CANDIDATE
object_family: <site_metadata|instantaneous_value|daily_value|annual_statistic|peak_flow|water_quality_record|groundwater_level>
source:
  source_id: usgs_water_data
  source_role: <administrative|observed|aggregate|generated_context|synthetic>
  api_surface: <modern_api_waterdata|legacy_waterservices_nwis|fixture>
  lifecycle_ref: data/raw/hydrology/usgs_water_data/<run_id>/
  input_hash: sha256:<hash>
  rights_state: needs_review
site:
  site_id: null
  site_ref: null
  datum_ref: null
observation:
  parameter_code: null
  variable_name: null
  value: null
  unit: null
  qualifiers: []
  approval_status: <provisional|approved|unknown|not_applicable>
  observed_at: null
  valid_start: null
  valid_end: null
  cadence: null
anti_collapse:
  provisional_is_approved: false
  daily_value_is_instantaneous_observation: false
  site_metadata_is_observed_reading: false
  generated_summary_is_evidence: false
policy:
  outcome: ABSTAIN
  reason_code: SOURCE_DESCRIPTOR_SITE_PARAMETER_APPROVAL_OR_EVIDENCE_NOT_RESOLVED
evidence:
  evidence_bundle_ref: null
  citation_state: ABSTAIN
outputs:
  candidate_record: data/work/hydrology/run_YYYYMMDDThhmmssZ/usgs_water_candidate.yml
  receipt: data/receipts/pipeline/hydrology/ingest_usgs_water/run_YYYYMMDDThhmmssZ.yml
rollback:
  required_before_publication: true
```

[⬆ Back to top](#top)

---

## 12. Tests, fixtures, receipts, and proofs

Default execution is **fixture-only, synthetic/generalized/redacted, and no-network** until source activation, USGS Water ingest spec, evidence, policy, sensitivity, and CI coverage are approved.

Recommended tests:

```text
tests/pipelines/domains/hydrology/ingest_usgs_water/
├── test_no_network_dry_run.py              # PROPOSED
├── test_source_descriptor_required.py      # PROPOSED
├── test_endpoint_lineage_required.py       # PROPOSED
├── test_site_id_required.py                # PROPOSED
├── test_parameter_code_required.py         # PROPOSED
├── test_provisional_not_approved.py        # PROPOSED
├── test_iv_not_daily_value.py              # PROPOSED
├── test_daily_value_is_aggregate.py        # PROPOSED
├── test_site_metadata_not_observation.py   # PROPOSED
├── test_water_quality_method_required.py   # PROPOSED
├── test_evidence_gap_abstains.py           # PROPOSED
├── test_quarantine_on_schema_failure.py    # PROPOSED
├── test_receipt_hashes.py                  # PROPOSED
└── test_no_direct_publish.py               # PROPOSED
```

A dry run should prove fixtures load without network access, source descriptors and endpoint lineage are required, site ids and parameter codes are preserved, provisional and approved values remain distinct, instantaneous and aggregate products remain distinct, EvidenceBundle gaps produce abstention, receipts are deterministic, and no run writes directly to public UI, public API, catalog store, published layers, or release manifests.

[⬆ Back to top](#top)

---

## 13. Promotion, publication, correction, and rollback

USGS Water ingest may prepare work candidates and quarantine records. It does not publish.

Required chain:

```text
admitted USGS Water source capture
  -> site/time-series ingest candidate
  -> validation report
  -> policy decision
  -> EvidenceBundle closure
  -> processed Hydrology observation record
  -> catalog / triplet candidate
  -> release candidate
  -> ReleaseManifest
  -> RollbackCard
  -> public-safe artifact
```

Correction and rollback posture:

- denied, abstained, errored, restricted, stale, conflicted, and quarantined USGS Water ingest runs remain auditable;
- ingest receipts preserve source refs, endpoint refs, site refs, parameter refs, approval-status refs, rule ids, and outcomes;
- processed versions are produced by governed promotion, not hidden overwrite;
- downstream artifacts are invalidated if source refs, endpoint refs, site refs, parameter refs, approval-state refs, evidence refs, source-role refs, or policy refs drift;
- public artifact rollback is owned by `release/`, not by this directory.

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- fills the blank `pipelines/domains/hydrology/ingest_usgs_water/README.md` file;
- identifies this directory as a nested executable Hydrology USGS Water ingest sublane;
- prevents connector, source-profile, schema, contract, policy, fixture, test, data, proof, catalog, and release authority from being placed here;
- preserves USGS source-role split, site identity, parameter codes, provisional/approved status, IV/DV/annual/peak/water-quality distinctions, endpoint migration lineage, evidence, policy, lifecycle, catalog/triplet, release, correction, and rollback boundaries;
- blocks provisional-as-approved, aggregate-as-observation, site-metadata-as-observation, generated-summary-as-evidence, and direct catalog/release writes;
- gives maintainers a fixture-first, fail-closed expansion pattern.

Future executable work in this sublane is done only when it has source-descriptor coverage, synthetic/generalized/redacted no-network fixtures, schema-backed candidates, contract conformance, source-role/site/parameter/approval/evidence/policy/no-direct-publish tests, deterministic receipts, CI coverage, steward-review handoff, and release/correction/rollback documentation.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `HYDRO-USGS-WATER-001` | Should this sublane remain generic, or split into IV, DV, peaks, annual statistics, site metadata, groundwater, and water-quality sublanes? | NEEDS VERIFICATION / ADR |
| `HYDRO-USGS-WATER-002` | Which source-edge job owns USGS Water retrieval before this sublane reads lifecycle inputs? | NEEDS VERIFICATION |
| `HYDRO-USGS-WATER-003` | Which first-wave product families are approved for fixture-only dry runs: sites, IV, DV, peaks, annual statistics, groundwater, or water-quality? | NEEDS VERIFICATION |
| `HYDRO-USGS-WATER-004` | Which schema owns USGS Water ingest candidates and quarantine reasons? | NEEDS VERIFICATION |
| `HYDRO-USGS-WATER-005` | Which CI job owns USGS Water ingest invariant tests? | UNKNOWN |
| `HYDRO-USGS-WATER-006` | How should modern API and legacy NWIS cutover receipts be represented during the migration window? | NEEDS VERIFICATION / ADR |
| `HYDRO-USGS-WATER-007` | Should catalog handoff be forbidden as an ingest side effect, or allowed only through an explicit chained spec? | NEEDS VERIFICATION |
| `HYDRO-USGS-WATER-008` | Which receipt type owns provisional-to-approved replacement, aggregate derivation, and parameter-code normalization? | PROPOSED / NEEDS ADR |

---

## Maintainer note

Start with synthetic/generalized fixture-only dry runs and negative tests. Do not add live USGS fetching, direct catalog writes, public layer writes, release-manifest writes, current operational guidance, engineering-use language, or direct API payload generation until source roles, endpoint lineage, provisional/approved discipline, parameter-code preservation, evidence closure, public-safe transforms, release review, and rollback are proven.
