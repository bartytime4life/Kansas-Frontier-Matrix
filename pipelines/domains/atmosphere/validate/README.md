<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-atmosphere-validate-readme
title: Atmosphere Validate Pipeline README
type: readme
version: v0.1
status: draft
owners:
  - <atmosphere-pipeline-owner>
  - <atmosphere-domain-steward>
  - <validation-steward>
  - <source-steward>
  - <evidence-steward>
  - <policy-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public-with-atmosphere-validation-freshness-and-caveat-gates
path: pipelines/domains/atmosphere/validate/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipelines/domains/README.md
  - pipelines/domains/atmosphere/README.md
  - pipelines/domains/air/README.md
  - docs/domains/atmosphere/README.md
  - docs/domains/atmosphere/DATA_LIFECYCLE.md
  - docs/domains/atmosphere/SOURCE_REGISTRY.md
  - docs/domains/atmosphere/CANONICAL_PATHS.md
  - docs/runbooks/atmosphere/PROMOTION_RUNBOOK.md
  - pipeline_specs/atmosphere/validate.yaml
  - contracts/domains/atmosphere/
  - schemas/contracts/v1/domains/atmosphere/
  - policy/domains/atmosphere/
  - policy/sensitivity/atmosphere/
  - data/work/atmosphere/
  - data/quarantine/atmosphere/
  - data/processed/atmosphere/
  - data/catalog/domain/atmosphere/
  - data/triplets/atmosphere/
  - data/receipts/pipeline/
  - data/proofs/evidence_bundle/
  - release/candidates/atmosphere/
  - release/manifests/atmosphere/
tags:
  - kfm
  - pipelines
  - domains
  - atmosphere
  - air
  - validate
  - validation-report
  - air-quality
  - weather
  - smoke
  - aod
  - climate
  - model-context
  - advisory-context
  - freshness
  - evidence-bundle
  - policy
  - governance
notes:
  - "This README fills the blank pipelines/domains/atmosphere/validate path as a nested executable Atmosphere validation sublane."
  - "Atmosphere validation logic is executable implementation support only; it does not own source descriptors, connectors, schemas, contracts, policy, lifecycle data, catalog truth, official notices, or release decisions."
  - "Validation converts normalized WORK candidates into ValidationReport outcomes, processed-candidate handoffs, or quarantine records; it does not publish or replace official issuing authorities."
  - "AQI, concentration, AOD, smoke context, model fields, observations, notice context, climate normals/anomalies, and low-cost sensor records must remain distinct."
  - "Concrete executable behavior, source activation, schedules, CI coverage, schema paths, release wiring, and public API/map behavior remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Atmosphere Validate Pipeline

> Executable Atmosphere / Air / Climate sublane for validating normalized atmospheric WORK candidates into `ValidationReport` outcomes, processed-candidate handoffs, quarantine records, receipts, and downstream catalog/release readiness checks — while preserving source identity, source role, units, temporal facets, caveats, freshness, EvidenceBundle readiness, policy outcomes, correction paths, and rollback boundaries.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-atmosphere%20validate-2e7d32)
![authority](https://img.shields.io/badge/authority-validation%20logic%20only-0a7ea4)
![boundary](https://img.shields.io/badge/not-official%20notice%20authority-d62728)
![publication](https://img.shields.io/badge/publication-no%20direct%20publish-d62728)
![ci](https://img.shields.io/badge/CI-TODO-lightgrey)

**Status:** Draft  
**Path:** `pipelines/domains/atmosphere/validate/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Domain lane:** Atmosphere / Air / Climate  
**Sublane:** Validate / WORK-to-PROCESSED readiness  
**Placement posture:** nested executable sublane under `pipelines/domains/atmosphere/`; concrete executable behavior remains `PROPOSED / NEEDS VERIFICATION` unless backed by tests and repo evidence  
**Public posture:** no direct publication and no official notice authority; validation outputs remain reports, processed-candidate handoffs, quarantine records, and receipts until catalog, release, correction, and rollback closure.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Validation anti-collapse rules](#3-validation-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Validation scope](#6-validation-scope)
- [7. Lifecycle contract](#7-lifecycle-contract)
- [8. Required gates](#8-required-gates)
- [9. Directory contract](#9-directory-contract)
- [10. Inputs and outputs](#10-inputs-and-outputs)
- [11. Minimal validation report candidate](#11-minimal-validation-report-candidate)
- [12. Tests, fixtures, receipts, and proofs](#12-tests-fixtures-receipts-and-proofs)
- [13. Promotion, publication, correction, and rollback](#13-promotion-publication-correction-and-rollback)
- [14. Definition of done](#14-definition-of-done)
- [15. Open questions](#15-open-questions)

---

## 1. Purpose

`pipelines/domains/atmosphere/validate/` is the executable sublane for Atmosphere validation.

It supports validation for:

- `AirStation`, `AirObservation`, `PM25Observation`, `OzoneObservation`, and other air-quality candidates;
- `SmokeContext`, `AODRaster`, remote-sensing masks, and smoke/aerosol context candidates;
- `WeatherStation`, `WeatherObservation`, `WindField`, `PrecipitationObservation`, and `TemperatureObservation` candidates;
- `ClimateNormal`, `ClimateAnomaly`, forecast/model field, and notice-context candidates;
- source descriptor, source role, rights, citation, source-vintage, content-hash, unit, sensor channel, station/network, temporal, and freshness closure;
- caveat and confidence requirements for low-cost sensor, model, notice-context, and derived-fusion products;
- `ValidationReport` outputs, processed-candidate handoffs, quarantine records, receipts, catalog-readiness signals, and release-readiness blockers.

This directory implements or will implement the **how** of Atmosphere validation. It does not fetch source data, admit sources, normalize records, define schemas, decide policy, issue official notices, own EvidenceBundle truth, own catalog truth, decide release, or publish public API/map payloads.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable pipeline logic: the **how**. | CONFIRMED root responsibility |
| Why `domains/atmosphere/`? | Visible domain docs use `atmosphere` as the lane and treat `air` as slug drift / alias pending ADR. | CONFIRMED documentation pattern; implementation NEEDS VERIFICATION |
| Why `validate/`? | This is a narrow executable sublane for validating normalized WORK candidates before processed/catalog handoff. | PROPOSED / NEEDS VERIFICATION |
| Does this own schemas or policy? | No. It consumes accepted contracts, schemas, policy outcomes, and source descriptors. | CONFIRMED authority separation |
| Does this replace official notices? | No. Notice context must redirect to the official issuing source and remain context only. | CONFIRMED domain boundary |
| Can this sublane publish? | No. It may prepare validation reports and handoffs only through governed workflow. | CONFIRMED doctrine posture |

> [!IMPORTANT]
> Validation pass is not publication. A passing `ValidationReport` means a candidate met the validation contract for the checked scope; it still requires EvidenceBundle closure, catalog closure, release review, correction path, and rollback target before any public surface changes.

[⬆ Back to top](#top)

---

## 3. Validation anti-collapse rules

Atmosphere validation must preserve observations, reports, model fields, remote-sensing context, notice context, processed records, catalog records, EvidenceBundles, policy decisions, and release artifacts as separate objects.

Disallowed collapses:

```text
validation pass -> public release
validation pass -> official notice
AQI -> concentration
AOD -> PM2.5
model field -> observation
low-cost sensor reading -> regulatory-grade observation without caveat/correction
smoke plume context -> official notice
notice context -> issuing authority text
schema-valid object -> policy-approved object
ValidationReport -> EvidenceBundle
EvidenceRef -> EvidenceBundle
generated validation summary -> evidence
pipeline run -> ReleaseManifest
```

Required distinctions:

- normalized WORK candidate, `ValidationReport`, processed candidate, quarantine record, EvidenceBundle, catalog record, release candidate, ReleaseManifest, CorrectionNotice, and RollbackCard remain separate;
- observed time, valid time, issue time, expiry time, model run time, retrieval time, processing time, release time, and correction time remain distinct;
- units, conversion receipts, station/network identity, sensor channels, model metadata, and caveats remain auditable;
- stale or rights-unclear material fails closed;
- every public claim resolves evidence or abstains.

[⬆ Back to top](#top)

---

## 4. What belongs here

Files belong here when their primary responsibility is executable Atmosphere validation.

Appropriate contents include:

- fixture-only validation dry-run entrypoints;
- schema/contract conformance checks that reference accepted schema homes;
- source descriptor, source-role, rights, station/network, sensor-channel, and citation validators;
- unit, conversion, temporal, CRS, spatial-grid, and extent validators;
- freshness/stale-state validators;
- AQI-vs-concentration, AOD-vs-PM2.5, model-field-vs-observation, and notice-context boundary checks;
- caveat/confidence/limitation validators for low-cost sensors, models, derived-fusion, and notice context;
- EvidenceRef and EvidenceBundle readiness checks;
- quarantine reason-code routing helpers;
- `ValidationReport` builders and receipt emitters;
- handoff helpers for processed, catalog, triplet, and release workflows without owning those decisions.

A good placement test:

> If the code checks normalized Atmosphere candidates and emits validation reports, processed-candidate handoffs, quarantine records, or receipts, it may belong here. If it fetches sources, admits sources, normalizes records, defines schemas, decides policy, writes catalog truth, approves release, issues official notices, or serves public API/map output, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Source fetchers and API clients | `connectors/<source>` or accepted connector home |
| Ingest/source admission | `pipelines/domains/atmosphere/ingest/` or accepted ingest lane |
| Normalization mappers | `pipelines/domains/atmosphere/normalize/` or accepted normalize lane |
| Catalog and triplet builders | catalog sublanes and lifecycle catalog/triplet homes |
| Atmosphere doctrine and object meaning | `docs/domains/atmosphere/`, `contracts/domains/atmosphere/` |
| JSON Schemas | `schemas/contracts/v1/domains/atmosphere/` or accepted schema home |
| Policy, rights, sensitivity, release rules | `policy/...` responsibility roots |
| Official notice wording or operational source text | Official issuing sources and governed context only |
| Declarative run specs | `pipeline_specs/atmosphere/...` |
| Fixtures | `fixtures/domains/atmosphere/validate/` or accepted fixture home |
| Tests | `tests/pipelines/domains/atmosphere/validate/` or accepted test home |
| Raw, work, quarantine, processed, catalog, triplet, or published outputs | `data/...` lifecycle homes |
| Public API or map code | `apps/governed-api/`, `apps/explorer-web/`, packages |
| Release decisions and manifests | `release/...` responsibility roots |

[⬆ Back to top](#top)

---

## 6. Validation scope

| Scope area | Validate responsibility | Failure behavior |
|---|---|---|
| Source identity | Confirm source id, descriptor ref, role, citation, rights, vintage, and input hashes are present. | Fail/hold or quarantine. |
| Schema/contract | Confirm candidate shape and object role match accepted contract. | Fail validation. |
| Units/time | Confirm units, conversion receipts, observed/valid/issue/expiry/model/retrieval times, and cadence. | Hold or quarantine on ambiguity. |
| Knowledge-character boundaries | Confirm AQI, concentrations, AOD, model fields, observations, climate context, and notice context are distinct. | Fail on collapse. |
| Freshness | Confirm source cadence and stale-state thresholds are explicit. | Hold or quarantine stale candidates. |
| Caveats | Confirm correction, confidence, limitations, and official-source redirection where required. | Fail closed if missing. |
| Evidence | Confirm claim-bearing candidates can resolve EvidenceRef/EvidenceBundle requirements or abstain. | Hold if unresolved. |
| Handoff | Emit validation report and processed-candidate handoff only when gates close. | No direct catalog or publish. |

[⬆ Back to top](#top)

---

## 7. Lifecycle contract

Every Atmosphere validation run must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal stance:

1. **Read** approved fixtures, normalized WORK candidates, or approved QUARANTINE remediation records.
2. **Validate** source descriptor refs, source roles, rights, units, temporal facets, station/network identity, sensor metadata, model metadata, freshness, caveats, evidence readiness, policy/review refs, and receipt refs.
3. **Emit** `ValidationReport` records with pass/fail/hold outcomes and deterministic reason codes.
4. **Route** failures or unresolved material to QUARANTINE with structured reasons.
5. **Prepare** processed-candidate handoffs only when validation closes; processed promotion remains governed and auditable.
6. **Never catalog, publish, or issue official notices directly.**

Validation is the WORK-to-PROCESSED readiness gate. It is not catalog closure, release approval, official notice issuance, or public serving.

[⬆ Back to top](#top)

---

## 8. Required gates

Every Atmosphere validation run must check or explicitly fail closed on:

1. **Input lifecycle gate** — input is normalized WORK, approved QUARANTINE remediation, or fixture-only material.
2. **SourceDescriptor gate** — source identity, source family, source role, rights, citation, cadence, and source vintage are present.
3. **Schema/contract gate** — candidate validates against the accepted Atmosphere contract shape.
4. **Source-role gate** — observation, regulatory archive, public report, model field, remote-sensing context, aggregate, synthetic, and notice context remain distinct.
5. **Unit/conversion gate** — units, conversion factors, conversion receipts, sensor channels, and parameter semantics are explicit.
6. **Temporal gate** — observed, valid, issue, expiry, model run, retrieval, processing, release, and correction times remain distinct.
7. **Freshness gate** — source cadence, stale-state threshold, and freshness outcome are explicit.
8. **Caveat gate** — low-cost sensor, model, derived-fusion, and notice-context records carry required caveats, confidence, limitations, or official-source redirection.
9. **Evidence gate** — claim-bearing candidates resolve EvidenceRef/EvidenceBundle preconditions or abstain.
10. **Policy/review gate** — finite policy outcome and review state exist where materiality or sensitivity requires it.
11. **Receipt gate** — validation output includes deterministic input/output digests and reason codes.
12. **No-direct-catalog gate** — validation does not write catalog/triplet records as a side effect.
13. **No-direct-publish gate** — validation does not write public UI, public API, published layers, release manifests, or official notice text.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended shape:

```text
pipelines/domains/atmosphere/validate/
├── README.md                         # this file
├── VALIDATE_CONTRACT.md              # PROPOSED: Atmosphere validation execution contract
├── run_dry_fixture.py                # PROPOSED synthetic fixture only
├── validate_schema_contract.py       # PROPOSED
├── validate_source_descriptor.py     # PROPOSED
├── validate_source_role.py           # PROPOSED
├── validate_units_temporal.py        # PROPOSED
├── validate_station_network.py       # PROPOSED
├── validate_freshness.py             # PROPOSED
├── validate_caveats.py               # PROPOSED
├── validate_evidence_refs.py         # PROPOSED
├── build_validation_report.py        # PROPOSED
├── route_quarantine.py               # PROPOSED
├── emit_validation_receipt.py        # PROPOSED only if not shared
└── adapters/                         # PROPOSED thin lifecycle adapters, no source fetching
```

Declarative specs should live outside this directory:

```text
pipeline_specs/atmosphere/validate.yaml # PROPOSED / NEEDS VERIFICATION
```

Generated outputs must not be written beside this code. Use accepted lifecycle homes under `data/work/atmosphere/`, `data/quarantine/atmosphere/`, `data/processed/atmosphere/`, and `data/receipts/` before downstream catalog, release, and published-layer roots.

[⬆ Back to top](#top)

---

## 10. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Fixture input | `fixtures/domains/atmosphere/validate/` or accepted fixture home | Synthetic or redacted atmospheric fixture. |
| Normalized WORK input | `data/work/atmosphere/<run_id>/` | Candidate from normalization; read by stable refs. |
| QUARANTINE remediation input | `data/quarantine/atmosphere/<reason>/<run_id>/` | Only in explicit remediation mode. |
| ValidationReport | `data/processed/atmosphere/<dataset_id>/<version>/` or accepted validation-report home | Report/handoff only; not public. |
| Processed candidate | `data/processed/atmosphere/<dataset_id>/<version>/` | Only after governed validation and promotion. |
| QUARANTINE output | `data/quarantine/atmosphere/<reason>/<run_id>/` | Failed, restricted, malformed, stale, or unresolved material. |
| Receipt | `data/receipts/pipeline/atmosphere/validate/<run_id>.yml` or accepted receipt home | Records inputs, checks, reason codes, and output refs. |
| Downstream handoff | catalog/release sublanes | Handoff only; no publication by file move. |

[⬆ Back to top](#top)

---

## 11. Minimal validation report candidate

The final schema is not defined here. This example shows the minimum information an Atmosphere validation report should preserve.

```yaml
schema_version: kfm.atmosphere_validation_report.v1
validation_report_id: atmosphere_validate_<source_id>_<object_role>_<hash>
pipeline_id: domains.atmosphere.validate
run_id: run_YYYYMMDDThhmmssZ
status: HOLD
source:
  source_id: <source_id>
  source_descriptor_ref: data/registry/sources/atmosphere/<source_id>.yml
  source_role: <observation|regulatory_archive|public_report|model_field|remote_sensing|aggregate|notice_context|synthetic>
  source_vintage: null
  rights_state: needs_review
candidate:
  work_ref: data/work/atmosphere/<run_id>/normalized_candidate.yml
  object_role: <AirObservation|PM25Observation|OzoneObservation|SmokeContext|AODRaster|WeatherObservation|WindField|PrecipitationObservation|TemperatureObservation|ClimateNormal|ClimateAnomaly|ForecastContext|AdvisoryContext>
checks:
  schema_contract_passed: false
  source_descriptor_resolved: false
  source_role_preserved: false
  units_temporal_valid: false
  freshness_valid: false
  caveats_ready: false
  evidence_ready: false
  receipt_ready: false
failure:
  outcome: HOLD
  reason_codes: []
evidence:
  evidence_ref_candidates: []
  evidence_bundle_ready: false
policy:
  policy_decision_ref: null
  review_record_ref: null
anti_collapse:
  validation_pass_is_publication: false
  validation_report_is_evidence_bundle: false
  aqi_is_concentration: false
  aod_is_pm25: false
  model_field_is_observation: false
  notice_context_is_official_notice_text: false
outputs:
  validation_report_ref: data/processed/atmosphere/<dataset_id>/<version>/validation_report.yml
  quarantine_ref: null
  receipt_ref: data/receipts/pipeline/atmosphere/validate/run_YYYYMMDDThhmmssZ.yml
rollback:
  required_before_publication: true
```

[⬆ Back to top](#top)

---

## 12. Tests, fixtures, receipts, and proofs

Default execution is **fixture-only, synthetic, and no-network** until validation specs, source descriptors, evidence, policy, sensitivity, and CI coverage are approved.

Recommended tests:

```text
tests/pipelines/domains/atmosphere/validate/
├── test_no_network_dry_run.py              # PROPOSED
├── test_normalized_work_input_required.py  # PROPOSED
├── test_source_descriptor_required.py      # PROPOSED
├── test_schema_contract_required.py        # PROPOSED
├── test_source_role_preserved.py           # PROPOSED
├── test_aqi_not_concentration.py           # PROPOSED
├── test_aod_not_pm25.py                    # PROPOSED
├── test_model_field_not_observation.py     # PROPOSED
├── test_notice_context_not_official_text.py # PROPOSED
├── test_units_temporal_facets.py           # PROPOSED
├── test_freshness_required.py              # PROPOSED
├── test_caveats_required.py                # PROPOSED
├── test_evidence_ref_resolution_required.py # PROPOSED
├── test_no_catalog_side_effect.py          # PROPOSED
├── test_receipt_hashes.py                  # PROPOSED
└── test_no_direct_publish.py               # PROPOSED
```

A dry run should prove fixtures load without network access, normalized WORK inputs are required, source descriptors and source roles are preserved, schema/contract checks run deterministically, unit and temporal facets remain distinct, freshness and caveats are enforced, EvidenceRef readiness is explicit, receipts are deterministic, and no run writes directly to catalog, triplet, public UI, public API, published layers, release manifests, or official notice text.

[⬆ Back to top](#top)

---

## 13. Promotion, publication, correction, and rollback

Atmosphere validation pipelines may prepare reports, processed-candidate handoffs, quarantine records, and receipts. They do not publish.

Required chain:

```text
normalized WORK candidate
  -> validation checks
  -> ValidationReport pass / hold / fail
  -> processed candidate or QUARANTINE hold
  -> EvidenceBundle closure
  -> catalog / triplet handoff
  -> release candidate
  -> ReleaseManifest
  -> RollbackCard
  -> public artifact
```

Correction and rollback posture:

- denied, held, failed, restricted, stale, conflicted, and quarantined validation runs remain auditable;
- receipts preserve source refs, source-role refs, units, temporal facets, station/network refs, caveat refs, evidence refs, policy refs, check versions, and failure reasons;
- validation reports are superseded through governed state transitions, not hidden overwrite;
- downstream artifacts are invalidated if source refs, source-role refs, validation versions, EvidenceBundle refs, freshness refs, caveat refs, policy refs, correction refs, or rollback refs drift;
- release rollback is owned by `release/`, not by this directory.

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- fills the blank `pipelines/domains/atmosphere/validate/README.md` file;
- identifies this directory as a nested executable Atmosphere validation sublane;
- prevents connector, source-admission, normalization, source-profile, schema, contract, policy, fixture, test, data, proof, public API, UI, official-notice, catalog, and release authority from being placed here;
- preserves source descriptor, source family, source role, source vintage, units, temporal facets, freshness, caveats, EvidenceRef/EvidenceBundle readiness, policy/review state, lifecycle, quarantine, correction, and rollback boundaries;
- blocks validation-pass-as-publication, validation-report-as-EvidenceBundle, AQI-as-concentration, AOD-as-PM2.5, model-field-as-observation, notice-context-as-official-text, generated-summary-as-evidence, catalog side effects, and direct publication writes;
- gives maintainers a fixture-first, fail-closed expansion pattern.

Future executable work in this sublane is done only when it has source-descriptor fixtures, no-network tests, schema-backed validation reports, contract conformance, source-role/unit/time/freshness/caveat/evidence/no-catalog/no-direct-publish tests, deterministic receipts, CI coverage, steward-review handoff, and release/correction/rollback documentation.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `ATM-VAL-001` | Should Atmosphere validation remain one sublane, or split into air-quality, weather, smoke/AOD, climate, model, and notice-context validators? | NEEDS VERIFICATION / ADR |
| `ATM-VAL-002` | Which schema owns `ValidationReport`, validation reason codes, validation receipts, and processed-candidate handoff fields? | NEEDS VERIFICATION |
| `ATM-VAL-003` | Which validator bundle is first-wave: source-role, units/time, freshness, caveats, evidence, or all through a composed fixture? | NEEDS VERIFICATION |
| `ATM-VAL-004` | Which CI job owns Atmosphere validation invariant tests? | UNKNOWN |
| `ATM-VAL-005` | Should EvidenceBundle construction begin during validation or wait for catalog closure? | NEEDS VERIFICATION / ADR |
| `ATM-VAL-006` | Which slug is authoritative for schema and contract homes: `atmosphere`, `air`, or both through an ADR-managed compatibility bridge? | NEEDS VERIFICATION / ADR |
| `ATM-VAL-007` | What is the authoritative reason-code mapping between validation failure and Atmosphere quarantine records? | NEEDS VERIFICATION |

---

## Maintainer note

Start with synthetic fixture-only dry runs and negative tests. Do not add live source fetching, ingest authority, normalization authority, source-profile editing, schema authority, policy authority, official-notice authority, direct catalog writes, direct public API code, direct UI code, release-manifest writes, public layer writes, or generated atmosphere summaries until source roles, source descriptors, schema/contract checks, unit/time handling, freshness/caveat handling, EvidenceRef handling, policy review, deterministic receipts, and rollback expectations are proven.
