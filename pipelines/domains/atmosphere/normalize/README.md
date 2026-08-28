<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-atmosphere-normalize-readme
title: Atmosphere Normalize Pipeline README
type: readme
version: v0.1
status: draft
owners:
  - <atmosphere-pipeline-owner>
  - <atmosphere-domain-steward>
  - <source-steward>
  - <normalization-steward>
  - <evidence-steward>
  - <policy-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public-with-atmosphere-normalization-gates
path: pipelines/domains/atmosphere/normalize/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipelines/domains/README.md
  - pipelines/domains/atmosphere/README.md
  - pipelines/domains/atmosphere/validate/README.md
  - pipelines/domains/atmosphere/publish/README.md
  - docs/domains/atmosphere/README.md
  - docs/domains/atmosphere/DATA_LIFECYCLE.md
  - docs/domains/atmosphere/SOURCE_REGISTRY.md
  - docs/runbooks/atmosphere/PROMOTION_RUNBOOK.md
  - pipeline_specs/atmosphere/normalize.yaml
  - contracts/domains/atmosphere/
  - schemas/contracts/v1/domains/atmosphere/
  - policy/domains/atmosphere/
  - data/raw/atmosphere/
  - data/work/atmosphere/
  - data/quarantine/atmosphere/
  - data/processed/atmosphere/
  - data/catalog/domain/atmosphere/
  - data/receipts/pipeline/
  - data/proofs/evidence_bundle/
  - release/candidates/atmosphere/
  - release/manifests/atmosphere/
tags:
  - kfm
  - pipelines
  - domains
  - atmosphere
  - normalize
  - transform-receipt
  - air-quality
  - weather
  - smoke
  - aod
  - climate
  - model-context
  - units
  - time
  - freshness
  - caveats
  - evidence-bundle
  - policy
  - governance
notes:
  - "This README fills the blank pipelines/domains/atmosphere/normalize path as a nested executable Atmosphere normalization sublane."
  - "Normalization converts admitted RAW/WORK/fixture inputs into structured WORK candidates and validation-ready records; it does not make public Atmosphere truth by itself."
  - "Unit conversions, station/network harmonization, temporal normalization, model-run normalization, correction context, caveats, and freshness fields must emit or preserve receipts."
  - "AQI, concentration, AOD, PM2.5, model field, observation, public report, and agency-context records remain separate knowledge characters."
  - "Concrete executable behavior, CI coverage, schema paths, release wiring, and public API/map behavior remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Atmosphere Normalize Pipeline

> Executable Atmosphere / Air / Climate sublane for transforming admitted atmospheric RAW/WORK/fixture material into normalized, validation-ready WORK candidates while preserving source identity, source role, units, conversion receipts, temporal facets, station/network identity, metadata, model metadata, caveats, freshness, evidence refs, policy posture, quarantine reasons, correction paths, and rollback boundaries.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-atmosphere%20normalize-2e7d32)
![authority](https://img.shields.io/badge/authority-normalization%20logic%20only-0a7ea4)
![knowledge](https://img.shields.io/badge/knowledge%20characters-preserved-455a64)
![publication](https://img.shields.io/badge/publication-no%20direct%20publish-d62728)
![ci](https://img.shields.io/badge/CI-TODO-lightgrey)

**Status:** Draft  
**Path:** `pipelines/domains/atmosphere/normalize/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Domain lane:** Atmosphere / Air / Climate  
**Sublane:** Normalize / WORK candidate shaping  
**Placement posture:** nested executable sublane under `pipelines/domains/atmosphere/`; concrete executable behavior remains `PROPOSED / NEEDS VERIFICATION` unless backed by tests and repo evidence  
**Public posture:** no direct publication; normalized outputs remain WORK candidates, quarantine records, validation inputs, and receipts until validation, catalog, release, correction, and rollback closure.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Normalize anti-collapse rules](#3-normalize-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Normalization scope](#6-normalization-scope)
- [7. Lifecycle contract](#7-lifecycle-contract)
- [8. Required gates](#8-required-gates)
- [9. Directory contract](#9-directory-contract)
- [10. Inputs and outputs](#10-inputs-and-outputs)
- [11. Minimal normalized candidate record](#11-minimal-normalized-candidate-record)
- [12. Tests, fixtures, receipts, and proofs](#12-tests-fixtures-receipts-and-proofs)
- [13. Promotion, publication, correction, and rollback](#13-promotion-publication-correction-and-rollback)
- [14. Definition of done](#14-definition-of-done)
- [15. Open questions](#15-open-questions)

---

## 1. Purpose

`pipelines/domains/atmosphere/normalize/` is the executable sublane for Atmosphere normalization.

It supports candidate processing for:

- station and network metadata harmonization;
- measured air-quality, weather, smoke/aerosol, climate, model, forecast, and agency-context records;
- unit normalization and conversion receipts, including explicit parameter semantics and source-unit retention;
- temporal normalization of observed, valid, issue, expiry, model-run, retrieval, processing, release, and correction times;
- spatial, CRS, grid, station, network, channel, height, exposure, and uncertainty normalization;
- correction context, caveat, confidence, limitation, and calibration-state preservation;
- freshness fields and source-cadence state for validation and release checks;
- quarantine records for rights uncertainty, source-role collapse, unit ambiguity, impossible values, missing time facets, stale sources, missing caveats, schema drift, or unsupported model/remote-sensing metadata.

This directory implements or will implement the **how** of Atmosphere normalization. It does not fetch source data, admit sources, define source descriptors, define schemas, decide policy, own EvidenceBundle truth, own catalog truth, decide release, or publish public API/map payloads.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable pipeline logic: the **how**. | CONFIRMED root responsibility |
| Why `domains/atmosphere/`? | Visible domain docs use `atmosphere` as the lane and treat `air` as slug drift / alias pending ADR. | CONFIRMED documentation pattern; implementation NEEDS VERIFICATION |
| Why `normalize/`? | This is a narrow executable sublane for transforming admitted Atmosphere inputs into normalized WORK candidates. | PROPOSED / NEEDS VERIFICATION |
| Is this ingest? | No. Ingest admits captures; normalization reshapes admitted material for validation. | CONFIRMED local separation |
| Does this own schemas or policy? | No. It consumes accepted contracts, schemas, policy outcomes, and source descriptors. | CONFIRMED authority separation |
| Can this sublane publish? | No. It may prepare validation-ready candidates only through governed workflow. | CONFIRMED doctrine posture |

> [!IMPORTANT]
> A normalized Atmosphere record is not validated truth, catalog truth, or public truth. Normalization makes records comparable, validatable, evidence-linkable, and digestable while preserving original source fields and caveats.

[⬆ Back to top](#top)

---

## 3. Normalize anti-collapse rules

Atmosphere normalization must preserve source roles, measured fields, public reports, model fields, remote-sensing context, agency context, units, time, evidence state, and lifecycle state.

Disallowed collapses:

```text
normalized record -> accepted public truth
AQI -> concentration
AOD -> PM2.5
model field -> observation
public report -> regulatory archive
uncorrected sensor reading -> direct truth without caveat/correction
unit conversion -> silent edit
station alias -> station identity without evidence
schema-shaped object -> validation pass
generated normalization summary -> evidence
pipeline run -> release approval
```

Required distinctions:

- source capture, normalized WORK candidate, quarantine record, ValidationReport, processed object, EvidenceBundle, catalog record, release candidate, ReleaseManifest, CorrectionNotice, and RollbackCard remain separate;
- original source units, normalized units, conversion factors, method refs, and TransformReceipts remain auditable;
- observed time, valid time, issue time, expiry time, model run time, retrieval time, processing time, release time, and correction time remain distinct;
- station/network identity, channels, model metadata, remote-sensing metadata, caveats, confidence, and limitations are not silently flattened;
- every downstream claim resolves evidence or abstains.

[⬆ Back to top](#top)

---

## 4. What belongs here

Files belong here when their primary responsibility is executable Atmosphere normalization.

Appropriate contents include:

- fixture-only normalization dry-run entrypoints;
- source-to-normalized-field mappers;
- unit conversion helpers that emit TransformReceipt inputs;
- station/network/site/channel harmonization helpers;
- temporal facet normalization helpers;
- CRS, grid, geometry, extent, and uncertainty normalization helpers;
- correction-context and caveat-preservation helpers;
- model-run, forecast, smoke, AOD, remote-sensing, climate-normal, and anomaly metadata shapers;
- freshness and cadence field builders;
- source-role and knowledge-character boundary preservation helpers;
- quarantine routing helpers for unresolved units, source roles, rights, caveats, impossible values, stale inputs, or schema drift;
- receipt emitters, if not shared;
- handoff helpers for validation and catalog workflows.

A good placement test:

> If the code transforms admitted Atmosphere RAW/WORK/fixture inputs into normalized WORK candidates, quarantine records, validation-ready handoffs, or receipts, it may belong here. If it fetches from an upstream, admits source captures, defines a SourceDescriptor, decides policy, writes catalog truth, approves release, or serves public API/map output, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Upstream fetchers and API clients | `connectors/<source>` or accepted connector home |
| Ingest/source admission | `pipelines/domains/atmosphere/ingest/` or accepted ingest lane |
| Validation logic | `pipelines/domains/atmosphere/validate/` |
| Catalog and triplet builders | catalog sublanes and lifecycle catalog/triplet homes |
| Atmosphere doctrine and object meaning | `docs/domains/atmosphere/`, `contracts/domains/atmosphere/` |
| Source descriptors / source registry entries | `data/registry/sources/atmosphere/` or approved registry home |
| JSON Schemas | `schemas/contracts/v1/domains/atmosphere/` or accepted schema home |
| Policy, rights, sensitivity, release rules | `policy/...` responsibility roots |
| Declarative run specs | `pipeline_specs/atmosphere/...` |
| Fixtures | `fixtures/domains/atmosphere/normalize/` or accepted fixture home |
| Tests | `tests/pipelines/domains/atmosphere/normalize/` or accepted test home |
| Raw, work, quarantine, processed, catalog, triplet, or published outputs | `data/...` lifecycle homes |
| Public API or map code | `apps/governed-api/`, `apps/explorer-web/`, packages |
| Release decisions and manifests | `release/...` responsibility roots |

[⬆ Back to top](#top)

---

## 6. Normalization scope

| Scope area | Normalize responsibility | Failure behavior |
|---|---|---|
| Source identity | Preserve source id, source role, source family, source vintage, citation refs, rights, and input hashes. | Quarantine if missing or conflicting. |
| Units and parameters | Normalize units and parameter semantics while preserving original fields and conversion receipt inputs. | Quarantine on ambiguity. |
| Time | Preserve observed, valid, issue, expiry, model-run, retrieval, processing, release, and correction times. | Quarantine on material collapse. |
| Station/network | Harmonize station, site, network, channel, height, and exposure fields without erasing source labels. | Hold if identity unresolved. |
| Knowledge character | Preserve observation, public report, regulatory archive, model field, remote-sensing mask, climate normal/anomaly, derived fusion, and agency context. | Fail on role collapse. |
| Caveats/freshness | Carry correction, confidence, limitations, source cadence, and stale-state inputs forward. | Hold or quarantine if missing. |
| Evidence | Carry source refs and candidate EvidenceRef inputs forward. | Abstain if unresolved. |
| Validation handoff | Emit validation-ready candidates with receipts. | No direct processed/catalog output. |

[⬆ Back to top](#top)

---

## 7. Lifecycle contract

Every Atmosphere normalization run must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal stance:

1. **Read** approved fixtures, admitted RAW captures, WORK candidates, or QUARANTINE remediation inputs with source identity and receipts.
2. **Normalize** fields into validation-ready Atmosphere candidates while preserving original source fields, source refs, source roles, units, conversion refs, temporal facets, station/network identity, rights, caveats, freshness, and evidence refs.
3. **Prepare** deterministic identity and digest inputs without claiming validation, catalog, or release truth.
4. **Quarantine** unresolved source roles, rights, unit ambiguity, impossible values, station identity conflicts, stale inputs, missing caveats, temporal collapse, schema drift, and unsupported model/remote-sensing metadata.
5. **Emit receipts** for every normalized, rejected, quarantined, or abstained normalization action.
6. **Never publish or catalog directly.**

Normalization is a WORK-stage shaping operation. It is not source admission, validation pass, catalog closure, or release.

[⬆ Back to top](#top)

---

## 8. Required gates

Every Atmosphere normalization run must check or explicitly fail closed on:

1. **Input lifecycle gate** — input is admitted RAW, WORK, approved QUARANTINE remediation, or fixture-only material.
2. **SourceDescriptor gate** — source identity, source family, source role, rights, citation, cadence, and source vintage are present.
3. **Original-field preservation gate** — original units, source labels, coordinates/grids, event times, issue/valid times, and metadata remain recoverable.
4. **Unit/conversion gate** — unit conversions and corrections record method, factor, source, and receipt-ready metadata.
5. **Temporal gate** — observed, valid, issue, expiry, model run, retrieval, processing, release, and correction times remain distinct.
6. **Knowledge-character gate** — AQI, concentration, AOD, model fields, observations, public reports, and agency context remain distinct.
7. **Station/network gate** — station aliases and network ids are harmonized without unsupported identity merges.
8. **Freshness/caveat gate** — model, derived-fusion, and agency-context records preserve caveats, confidence, limitations, source cadence, and stale-state inputs.
9. **Evidence gate** — candidate evidence refs are preserved and unresolved support abstains.
10. **Quarantine reason gate** — every denied/held record has a structured reason code and receipt.
11. **No-direct-catalog gate** — normalization does not write catalog/triplet records as a side effect.
12. **No-direct-publish gate** — normalization does not write public UI, public API, published layers, or release manifests.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended shape:

```text
pipelines/domains/atmosphere/normalize/
├── README.md                         # this file
├── NORMALIZE_CONTRACT.md             # PROPOSED: Atmosphere normalization execution contract
├── run_dry_fixture.py                # PROPOSED synthetic fixture only
├── normalize_units.py                # PROPOSED
├── normalize_temporal_facets.py      # PROPOSED
├── normalize_station_network.py      # PROPOSED
├── normalize_air_quality.py          # PROPOSED
├── normalize_weather.py              # PROPOSED
├── normalize_smoke_aod.py            # PROPOSED
├── normalize_model_context.py        # PROPOSED
├── normalize_climate_context.py      # PROPOSED
├── prepare_freshness_caveats.py      # PROPOSED
├── route_quarantine.py               # PROPOSED
├── emit_normalize_receipt.py         # PROPOSED only if not shared
└── adapters/                         # PROPOSED thin lifecycle adapters, no source fetching
```

Declarative specs should live outside this directory:

```text
pipeline_specs/atmosphere/normalize.yaml # PROPOSED / NEEDS VERIFICATION
```

Generated outputs must not be written beside this code. Use accepted lifecycle homes under `data/work/atmosphere/`, `data/quarantine/atmosphere/`, and `data/receipts/` before downstream validation, processed, catalog, release, and published-layer roots.

[⬆ Back to top](#top)

---

## 10. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Fixture input | `fixtures/domains/atmosphere/normalize/` or accepted fixture home | Synthetic atmospheric fixture. |
| RAW capture | `data/raw/atmosphere/<source_id>/<run_id>/` | Immutable input; read only. |
| WORK input | `data/work/atmosphere/<run_id>/` | Candidate from ingest or remediation. |
| Normalized WORK candidate | `data/work/atmosphere/<run_id>/` | Validation-ready candidate; not processed truth. |
| QUARANTINE record | `data/quarantine/atmosphere/<reason>/<run_id>/` | Failed, restricted, malformed, stale, or unresolved material. |
| Receipt | `data/receipts/pipeline/atmosphere/normalize/<run_id>.yml` or accepted receipt home | Records inputs, normalization choices, checks, hashes, and output refs. |
| Downstream handoff | validate/catalog sublanes | Handoff only; no promotion by file move. |

[⬆ Back to top](#top)

---

## 11. Minimal normalized candidate record

The final schema is not defined here. This example shows the minimum information an Atmosphere normalized candidate should preserve.

```yaml
schema_version: kfm.atmosphere_normalized_candidate.v1
normalized_candidate_id: atmosphere_normalized_<source_id>_<object_role>_<hash>
pipeline_id: domains.atmosphere.normalize
run_id: run_YYYYMMDDThhmmssZ
status: WORK_CANDIDATE
source:
  source_id: <source_id>
  source_family: <aqs|airnow|nws|mesonet|hrrr_smoke|hms|cams|goes|viirs|openaq|other>
  source_role: <observation|regulatory_archive|public_report|model_field|remote_sensing|aggregate|advisory_context|synthetic>
  source_descriptor_ref: data/registry/sources/atmosphere/<source_id>.yml
  source_vintage: null
  rights_state: needs_review
object:
  object_role: <AirObservation|PM25Observation|OzoneObservation|SmokeContext|AODRaster|WeatherObservation|WindField|PrecipitationObservation|TemperatureObservation|ClimateNormal|ClimateAnomaly|ForecastContext|AdvisoryContext>
  original_parameter_label: null
  normalized_parameter: null
  knowledge_character: needs_review
units:
  original_unit: null
  normalized_unit: null
  transform_receipt_candidate: null
time:
  observed_time: null
  valid_time: null
  issue_time: null
  expiry_time: null
  model_run_time: null
  retrieval_time: null
spatial:
  station_ref: null
  network_ref: null
  crs: null
  grid_ref: null
freshness_caveats:
  cadence_ref: null
  freshness_state: needs_review
  caveats_required: true
  limitations_ref: null
policy:
  outcome: ABSTAIN
  reason_code: SOURCE_UNITS_TIME_CAVEATS_OR_EVIDENCE_NOT_RESOLVED
evidence:
  evidence_ref_candidates: []
anti_collapse:
  normalized_is_validated_truth: false
  aqi_is_concentration: false
  aod_is_pm25: false
  model_field_is_observation: false
  unit_conversion_is_silent_edit: false
outputs:
  work_ref: data/work/atmosphere/run_YYYYMMDDThhmmssZ/normalized_candidate.yml
  quarantine_ref: null
  receipt_ref: data/receipts/pipeline/atmosphere/normalize/run_YYYYMMDDThhmmssZ.yml
rollback:
  required_before_publication: true
```

[⬆ Back to top](#top)

---

## 12. Tests, fixtures, receipts, and proofs

Default execution is **fixture-only, synthetic, and no-network** until normalization specs, source descriptors, evidence, policy, caveat, freshness, and CI coverage are approved.

Recommended tests:

```text
tests/pipelines/domains/atmosphere/normalize/
├── test_no_network_dry_run.py              # PROPOSED
├── test_source_descriptor_required.py      # PROPOSED
├── test_original_fields_preserved.py       # PROPOSED
├── test_unit_conversion_receipt_ready.py   # PROPOSED
├── test_temporal_facets_preserved.py       # PROPOSED
├── test_station_network_not_silently_merged.py # PROPOSED
├── test_aqi_not_concentration.py           # PROPOSED
├── test_aod_not_pm25.py                    # PROPOSED
├── test_model_field_not_observation.py     # PROPOSED
├── test_caveats_preserved.py               # PROPOSED
├── test_freshness_state_prepared.py        # PROPOSED
├── test_malformed_payload_quarantines.py   # PROPOSED
├── test_no_catalog_side_effect.py          # PROPOSED
├── test_receipt_hashes.py                  # PROPOSED
└── test_no_direct_publish.py               # PROPOSED
```

A dry run should prove fixtures load without network access, source descriptors and source roles are required, original fields are preserved, unit conversions are receipt-ready, temporal facets remain distinct, AQI/AOD/model boundaries hold, freshness/caveat fields are prepared, receipts are deterministic, and no run writes directly to catalog, triplet, public UI, public API, published layers, or release manifests.

[⬆ Back to top](#top)

---

## 13. Promotion, publication, correction, and rollback

Atmosphere normalization pipelines may prepare normalized work candidates, quarantine records, validation handoffs, and receipts. They do not publish.

Required chain:

```text
admitted RAW / WORK / fixture input
  -> normalization checks
  -> normalized WORK candidate or QUARANTINE hold
  -> validation report
  -> EvidenceBundle closure
  -> processed Atmosphere object
  -> catalog / triplet handoff
  -> release candidate
  -> ReleaseManifest
  -> RollbackCard
  -> public artifact
```

Correction and rollback posture:

- denied, abstained, malformed, restricted, stale, conflicted, and quarantined normalization runs remain auditable;
- receipts preserve source refs, source-role refs, original fields, normalized fields, units, conversion refs, station/network refs, temporal facets, caveats, freshness state, evidence refs, payload hashes, normalizer refs, and failure reasons;
- normalized candidates are superseded through governed state transitions, not hidden overwrite;
- downstream artifacts are invalidated if source refs, source-role refs, temporal scopes, unit conversion refs, station/network refs, freshness refs, caveat refs, EvidenceBundle refs, policy refs, review refs, correction refs, or rollback refs drift;
- release rollback is owned by `release/`, not by this directory.

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- fills the blank `pipelines/domains/atmosphere/normalize/README.md` file;
- identifies this directory as a nested executable Atmosphere normalization sublane;
- prevents connector, ingest/source-admission, source-profile, schema, contract, policy, fixture, test, data, proof, public API, UI, validation, catalog, and release authority from being placed here;
- preserves source descriptor, source family, source role, source vintage, original fields, normalized fields, unit conversions, temporal facets, station/network identity, knowledge-character labels, freshness, caveats, EvidenceRef readiness, lifecycle, quarantine, correction, and rollback boundaries;
- blocks normalized-record-as-truth, AQI-as-concentration, AOD-as-PM2.5, model-field-as-observation, unit-conversion-as-silent-edit, generated-summary-as-evidence, catalog side effects, and direct publication writes;
- gives maintainers a fixture-first, fail-closed expansion pattern.

Future executable work in this sublane is done only when it has source-descriptor fixtures, no-network tests, schema-backed normalized candidates, contract conformance, source-role/original-field/unit/time/freshness/caveat/evidence/no-catalog/no-direct-publish tests, deterministic receipts, CI coverage, steward-review handoff, and release/correction/rollback documentation.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `ATM-NORM-001` | Should Atmosphere normalization remain one sublane, or split into air-quality, weather, smoke/AOD, climate, model, and advisory-context normalizers? | NEEDS VERIFICATION / ADR |
| `ATM-NORM-002` | Which schema owns normalized candidates, unit-conversion receipt refs, freshness fields, and quarantine reason codes? | NEEDS VERIFICATION |
| `ATM-NORM-003` | Which validator bundle is first-wave for fixture-only dry runs: units/time, station/network, AQI/AOD/model boundaries, caveats/freshness, or all together? | NEEDS VERIFICATION |
| `ATM-NORM-004` | Which CI job owns Atmosphere normalization invariant tests? | UNKNOWN |
| `ATM-NORM-005` | Which slug is authoritative for schema and contract homes: `atmosphere`, `air`, or both through an ADR-managed compatibility bridge? | NEEDS VERIFICATION / ADR |
| `ATM-NORM-006` | Which unit vocabulary and conversion policy should be authoritative for atmospheric parameters? | NEEDS VERIFICATION / ADR |
| `ATM-NORM-007` | Should freshness state be computed during normalization, validation, or catalog closure? | NEEDS VERIFICATION |

---

## Maintainer note

Start with synthetic fixture-only dry runs and negative tests. Do not add live source fetching, ingest authority, source-profile editing, schema authority, policy authority, direct validation pass shortcuts, direct catalog writes, direct public API code, direct UI code, release-manifest writes, public layer writes, or generated atmosphere summaries until source roles, source descriptors, original-field preservation, unit/time handling, station/network handling, freshness/caveat handling, deterministic receipts, review state, and rollback are proven.
