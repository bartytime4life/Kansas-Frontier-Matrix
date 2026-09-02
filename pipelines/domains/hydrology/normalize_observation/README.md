<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-hydrology-normalize-observation-readme
title: Hydrology Observation Normalize Pipeline README
type: readme
version: v0.1
status: draft
owners:
  - <hydrology-pipeline-owner>
  - <hydrology-domain-steward>
  - <source-steward>
  - <evidence-steward>
  - <policy-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: pipelines/domains/hydrology/normalize_observation/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipelines/domains/README.md
  - pipelines/domains/hydrology/README.md
  - pipelines/domains/hydrology/ingest/README.md
  - pipelines/domains/hydrology/normalize/README.md
  - pipelines/domains/hydrology/ingest_usgs_water/README.md
  - pipelines/domains/hydrology/catalog/README.md
  - pipelines/domains/hydrology/catalog_close/README.md
  - docs/domains/hydrology/README.md
  - docs/domains/hydrology/DATA_LIFECYCLE.md
  - docs/domains/hydrology/PUBLICATION_POSTURE.md
  - docs/sources/catalog/usgs/nwis-water.md
  - pipeline_specs/hydrology/normalize_observation.yaml
  - contracts/domains/hydrology/
  - schemas/contracts/v1/domains/hydrology/
  - policy/domains/hydrology/
  - policy/sensitivity/hydrology/
  - data/work/hydrology/
  - data/quarantine/hydrology/
  - data/processed/hydrology/
  - data/catalog/domain/hydrology/
  - data/triplets/hydrology/
  - data/receipts/pipeline/
  - data/proofs/evidence_bundle/
  - release/candidates/hydrology/
  - release/manifests/hydrology/
tags:
  - kfm
  - pipelines
  - domains
  - hydrology
  - normalize-observation
  - observation
  - station
  - gauge
  - well
  - instantaneous-values
  - peak-flows
  - water-quality
  - groundwater
  - parameter-code
  - qa
  - approval-status
  - evidence
  - policy
  - governance
notes:
  - "This README fills the blank pipelines/domains/hydrology/normalize_observation path as a nested executable Hydrology observation-normalization sublane."
  - "Observation normalization is executable implementation support only; it does not own source descriptors, connectors, schemas, policy, lifecycle data, catalog truth, operational decisions, or release decisions."
  - "The subdirectory name uses the requested underscore form normalize_observation; if repo slug rules prefer hyphenated names, record the path decision with ADR/path-map/rollback notes before moving."
  - "Observation normalization preserves observed source-role records such as instantaneous values, peak readings, site-linked water-quality samples, and groundwater readings; it does not convert aggregates, models, regulatory context, site metadata, or generated summaries into observations."
  - "Provisional and approved values, parameter codes, units, qualifiers, QA flags, site identity, time basis, datum, and receipt lineage must travel with every normalized observation candidate."
  - "Concrete executable behavior, source linkage, schedules, CI coverage, schema paths, release wiring, and public API/map behavior remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hydrology Observation Normalize Pipeline

> Executable Hydrology sublane for canonicalizing admitted observed station/site readings into schema-ready observation candidates, quarantine records, validation handoffs, receipts, and downstream processed/catalog/release-review packages — without converting aggregates, models, regulatory context, site metadata, or generated summaries into observations.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-hydrology%20observation%20normalize-2e7d32)
![authority](https://img.shields.io/badge/authority-executable%20logic-0a7ea4)
![source-role](https://img.shields.io/badge/source--role-observed%20only-d62728)
![approval](https://img.shields.io/badge/provisional%20%E2%89%A0%20approved-d62728)
![publication](https://img.shields.io/badge/publication-release%20gated-d62728)
![ci](https://img.shields.io/badge/CI-TODO-lightgrey)

**Status:** Draft  
**Path:** `pipelines/domains/hydrology/normalize_observation/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Domain lane:** Hydrology  
**Sublane:** Observation normalization  
**Placement posture:** nested executable sublane under `pipelines/domains/hydrology/`; concrete executable behavior remains `PROPOSED / NEEDS VERIFICATION` unless backed by tests and repo evidence  
**Publication posture:** no direct publication; normalized observation output is validation/processed-state input only and requires downstream evidence, policy, catalog, release, correction, and rollback closure

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Observation anti-collapse rules](#3-observation-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Normalization scope](#6-normalization-scope)
- [7. Lifecycle contract](#7-lifecycle-contract)
- [8. Required gates](#8-required-gates)
- [9. Directory contract](#9-directory-contract)
- [10. Inputs and outputs](#10-inputs-and-outputs)
- [11. Minimal normalized observation candidate](#11-minimal-normalized-observation-candidate)
- [12. Tests, fixtures, receipts, and proofs](#12-tests-fixtures-receipts-and-proofs)
- [13. Promotion, publication, correction, and rollback](#13-promotion-publication-correction-and-rollback)
- [14. Definition of done](#14-definition-of-done)
- [15. Open questions](#15-open-questions)

---

## 1. Purpose

`pipelines/domains/hydrology/normalize_observation/` is the executable sublane for canonicalizing Hydrology observations after source-specific ingest has created admitted work candidates.

It supports normalization for:

- gauge, well, observation-site, and sample-site linked observations;
- instantaneous values such as flow, stage, gage height, precipitation, groundwater level, water temperature, and other admitted observed variables;
- peak-flow observations and peak-event records with qualification metadata;
- water-quality sample observations with parameter, method, and unit metadata;
- groundwater observations with site, datum, depth, and time metadata;
- parameter codes, units, qualifiers, missing values, QA flags, approval status, and provisional/approved state;
- observation time, valid time, source time, retrieval time, processing time, and normalization time;
- quarantine records for missing site identity, parameter code, unit, QA, approval status, time basis, datum, source role, evidence, or schema conformance;
- validation, processed-state, catalog, triplet, EvidenceBundle, release-review, correction, and rollback handoff packages.

This directory implements or will implement the **how** of Hydrology observation normalization. It does not fetch source data, perform source-specific ingest, define Hydrology object meaning, define schemas, encode policy, store lifecycle data, decide release, issue current advisories, or certify engineering use.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable pipeline logic: the **how**. | CONFIRMED root responsibility |
| Why `domains/hydrology/`? | Hydrology is the domain lane used by Hydrology docs and pipeline READMEs. | CONFIRMED documentation pattern; behavior NEEDS VERIFICATION |
| Why `normalize_observation/`? | This is a narrow executable sublane for canonicalizing observed Hydrology readings after ingest. | PROPOSED / NEEDS VERIFICATION |
| Is this an ingest lane? | No. Ingest lanes create source-specific work candidates; this lane normalizes observed candidates. | PROPOSED |
| Can it normalize aggregates or models? | Not as observations. Aggregates and models must stay in their own source-role lanes. | CONFIRMED governance posture |
| Where do declarative run specs live? | `pipeline_specs/hydrology/normalize_observation.yaml` or accepted spec home. | PROPOSED / NEEDS VERIFICATION |
| Can this sublane publish? | No. It may emit normalized candidates, quarantine records, validation handoffs, and receipts only through governed workflow. | CONFIRMED doctrine posture |

> [!IMPORTANT]
> Observation normalization is not source fetch, not source-specific ingest, not aggregate derivation, not model output generation, not release approval, and not public artifact creation. It standardizes admitted observed candidates while preserving source role, site identity, time basis, units, QA, approval state, evidence, and lifecycle state.

[⬆ Back to top](#top)

---

## 3. Observation anti-collapse rules

Hydrology observation normalization must preserve observed-record semantics.

Disallowed collapses:

```text
daily value -> instantaneous observation
annual statistic -> observation
modeled hydrograph -> observation
NFHL regulatory context -> observation
site metadata -> observation
provisional value -> approved value
stage / gage height -> discharge without rating/method support
parameter code -> unlabeled plain-language value
unit conversion -> silent overwrite
missing qualifier -> clean observation
generated summary -> evidence
normalize receipt -> release approval
```

Required distinctions:

- `source_role: observed` is required for observation outputs;
- aggregates, modeled records, regulatory context, administrative site metadata, and generated summaries are denied or rerouted;
- site/station/sample identity is explicit;
- parameter codes, variable names, units, qualifiers, QA flags, missing-value markers, approval status, and method refs are preserved;
- time basis fields remain distinct;
- any conversion, rating, interpolation, aggregation, or gap fill requires a method or derivation receipt and cannot silently overwrite the original observation.

[⬆ Back to top](#top)

---

## 4. What belongs here

Files belong here when their primary responsibility is executable observed-reading normalization.

Appropriate contents include:

- fixture-only observation-normalization entrypoints;
- observation candidate canonicalizers;
- site/station/sample identity validators;
- parameter-code, unit, qualifier, QA, and missing-value normalizers;
- provisional/approved and approval-status validators;
- time-basis and cadence normalizers for observed records;
- datum, elevation, depth, and site-reference normalizers where applicable;
- no-aggregate-as-observation validators;
- no-model-as-observation and no-regulatory-context-as-observation validators;
- quarantine routing helpers for missing identity, parameter, unit, time, QA, approval, datum, evidence, or schema issues;
- normalization receipt builders, if not shared;
- handoff helpers for validation and processed-state review;
- thin adapters that read governed lifecycle inputs, not live source endpoints.

A good placement test:

> If the code canonicalizes admitted Hydrology observed candidates into schema-ready normalized observations, quarantine records, validation handoffs, receipts, or downstream handoff packages, it may belong here. If it fetches source data, handles source-specific ingest, normalizes aggregates/models/regulatory records as their own classes, defines schemas, stores lifecycle data, writes catalog records, approves release, or creates public API/map payloads, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Source fetchers / connectors | `connectors/<source>` or accepted connector home |
| Source-specific ingest code | `pipelines/domains/hydrology/ingest_*` or accepted ingest sublane |
| Generic normalization shared with other classes | `pipelines/domains/hydrology/normalize/` or shared package |
| Aggregate/model/regulatory normalizers | Separate accepted sublane or generic normalize with class-specific validators |
| Source catalog profiles | `docs/sources/catalog/...` |
| Source descriptors / source registry entries | `data/registry/sources/hydrology/` or approved registry home |
| Hydrology architecture and doctrine | `docs/domains/hydrology/...` |
| Object meaning contracts | `contracts/domains/hydrology/` or accepted contract home |
| JSON Schemas | `schemas/contracts/v1/domains/hydrology/` or accepted schema home |
| Policy, rights, sensitivity, release rules | `policy/...` responsibility roots |
| Declarative run specs | `pipeline_specs/hydrology/...` |
| Fixtures | `fixtures/domains/hydrology/normalize_observation/` or accepted fixture home |
| Tests | `tests/pipelines/domains/hydrology/normalize_observation/` or accepted test home |
| Raw, work, quarantine, processed, catalog, triplet, or published outputs | `data/...` lifecycle homes |
| Catalog/triplet builders or close checks | `pipelines/domains/hydrology/catalog/`, `pipelines/catalog/`, `pipelines/domains/hydrology/catalog_close/` |
| Receipts and proofs | `data/receipts/...`, `data/proofs/...` |
| Release decisions and manifests | `release/...` responsibility roots |
| Public API or map code | `apps/governed-api/`, `apps/explorer-web/`, packages |

[⬆ Back to top](#top)

---

## 6. Normalization scope

| Scope area | Normalization responsibility | Failure behavior |
|---|---|---|
| Source role | Confirm candidate is observed before producing observation output. | Reroute, deny, or quarantine. |
| Site identity | Preserve site id, station/sample refs, datum refs, and monitoring context. | Quarantine if missing. |
| Parameter | Preserve parameter code, variable name, unit, and method refs. | Quarantine on ambiguity. |
| Value | Preserve value, missing markers, qualifiers, and QA flags. | Restrict or quarantine if incomplete. |
| Approval state | Preserve provisional, approved, revised, or unknown state. | Quarantine or restrict if collapsed. |
| Time basis | Preserve observed time, valid time, source time, retrieval time, processing time, and normalization time. | Quarantine on collapse. |
| Conversion | Record conversion/rating/interpolation method refs if applied. | Deny silent conversion. |
| Evidence | Carry evidence refs forward; do not invent support. | Abstain if unresolved. |

[⬆ Back to top](#top)

---

## 7. Lifecycle contract

Every Hydrology observation-normalize run must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal stance:

1. **Read** approved fixtures, observed work candidates, quarantine inputs in remediation mode, or prior normalized observed baselines.
2. **Normalize** into canonicalized observation candidates with source role, site refs, parameter refs, time basis, units, QA, approval state, evidence refs, policy refs, and receipt refs.
3. **Quarantine** unresolved source role, non-observation class, missing site identity, parameter ambiguity, unit ambiguity, time ambiguity, QA gaps, approval-state collapse, evidence gaps, schema drift, or validation failure.
4. **Emit receipts** with input refs, normalization version, method refs, transform refs, output refs, and outcomes.
5. **Support validation** only by providing schema-ready observed candidates and auditable receipts.
6. **Never publish directly.**

Observation normalization is an intermediate lifecycle transformation. It is not processed-state promotion, catalog closure, release approval, or public artifact creation by itself.

[⬆ Back to top](#top)

---

## 8. Required gates

Every observation-normalize run must check or explicitly fail closed on:

1. **Input lifecycle gate** — input is fixture, work candidate, quarantine-remediation input, or accepted baseline.
2. **Ingest receipt gate** — source-derived candidates have ingest receipt refs unless explicitly fixture-only.
3. **Source descriptor gate** — source identity, role, cadence/vintage, rights, and policy posture are known.
4. **Observed-role gate** — output observations require observed source role.
5. **Non-observation reroute gate** — aggregates, models, regulatory context, administrative metadata, and generated records do not normalize as observations.
6. **Site identity gate** — site id, station/sample id, datum refs, and monitoring context are explicit where applicable.
7. **Parameter/unit gate** — parameter code, unit, qualifier, method, missing-value, and conversion posture are explicit.
8. **QA/approval gate** — QA flags, provisional/approved/revised state, and qualifiers are preserved.
9. **Time/cadence gate** — observation time, valid time, source time, retrieval time, processing time, and normalization time remain distinct.
10. **Evidence gate** — claim-bearing downstream candidates can resolve evidence refs or abstain.
11. **Schema/contract gate** — normalized observation candidates match accepted schema and Hydrology semantics.
12. **No-direct-publish gate** — no writes to public UI, public API, catalog store, published layers, or release manifests as a normalization side effect.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended shape:

```text
pipelines/domains/hydrology/normalize_observation/
├── README.md                         # this file
├── NORMALIZE_OBSERVATION_CONTRACT.md # PROPOSED: observation normalization contract
├── run_dry_fixture.py                # PROPOSED synthetic/redacted fixture only
├── normalize_observation_identity.py # PROPOSED
├── normalize_site_refs.py            # PROPOSED
├── normalize_parameter_units.py      # PROPOSED
├── normalize_qa_approval.py          # PROPOSED
├── normalize_observation_time.py     # PROPOSED
├── validate_observed_role.py         # PROPOSED
├── validate_not_aggregate.py         # PROPOSED
├── validate_not_modeled.py           # PROPOSED
├── validate_not_regulatory_context.py # PROPOSED
├── route_quarantine.py               # PROPOSED
├── emit_receipt.py                   # PROPOSED only if not shared
└── adapters/                         # PROPOSED thin lifecycle adapters, no source fetching
```

Declarative specs should live outside this directory:

```text
pipeline_specs/hydrology/normalize_observation.yaml # PROPOSED / NEEDS VERIFICATION
```

Generated outputs must not be written beside the normalization code. Use accepted lifecycle homes under `data/work/hydrology/`, `data/quarantine/hydrology/`, `data/processed/hydrology/`, proof homes under `data/proofs/`, receipt homes under `data/receipts/`, and release homes under `release/`.

[⬆ Back to top](#top)

---

## 10. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Fixture input | `fixtures/domains/hydrology/normalize_observation/` or accepted fixture home | Synthetic, generalized, or redacted. |
| Observed work candidate input | `data/work/hydrology/<run_id>/` | Main normalization input. |
| Quarantine remediation input | `data/quarantine/hydrology/<reason>/<run_id>/` | Remediation mode only. |
| Normalized observation candidate | `data/work/hydrology/<run_id>/` or accepted work home | Candidate only. |
| Quarantine output | `data/quarantine/hydrology/<reason>/<run_id>/` | Failed or unresolved material. |
| Processed handoff candidate | `data/processed/hydrology/<dataset_id>/<version>/` | Only after downstream validation and promotion gates. |
| Receipt | `data/receipts/pipeline/hydrology/normalize_observation/<run_id>.yml` or accepted receipt home | Records input refs, methods, transforms, checks, and outputs. |
| Evidence proof | `data/proofs/evidence_bundle/` or accepted proof home | Required for claim-bearing downstream records. |

[⬆ Back to top](#top)

---

## 11. Minimal normalized observation candidate

The final schema is not defined here. This example shows the minimum information a Hydrology normalized observation candidate should preserve.

```yaml
schema_version: kfm.hydrology_normalized_observation_candidate.v1
candidate_id: hydrology_obs_<source_id>_<site_id>_<parameter_code>_<observed_at_or_period>_<run_id>
pipeline_id: domains.hydrology.normalize_observation
run_id: run_YYYYMMDDThhmmssZ
status: WORK_CANDIDATE
object_family: <flow_observation|stage_observation|water_level_observation|groundwater_observation|water_quality_observation|peak_flow_observation|precipitation_observation>
source:
  source_id: <source_id>
  source_role: observed
  ingest_receipt_ref: data/receipts/pipeline/hydrology/<ingest_lane>/<run_id>.yml
  input_hash: sha256:<hash>
  rights_state: needs_review
site:
  site_id: null
  station_ref: null
  sample_ref: null
  datum_ref: null
observation:
  parameter_code: null
  variable_name: null
  value: null
  unit: null
  qualifiers: []
  qa_flags: []
  approval_status: <provisional|approved|revised|unknown|not_applicable>
  observed_at: null
  valid_start: null
  valid_end: null
  retrieved_at: null
  normalized_at: YYYY-MM-DDThh:mm:ssZ
method:
  conversion_applied: false
  conversion_receipt_ref: null
anti_collapse:
  aggregate_is_observation: false
  model_is_observation: false
  regulatory_context_is_observation: false
  site_metadata_is_observation: false
  provisional_is_approved: false
  generated_summary_is_evidence: false
policy:
  outcome: ABSTAIN
  reason_code: OBSERVATION_IDENTITY_TIME_UNIT_QA_OR_EVIDENCE_NOT_RESOLVED
evidence:
  evidence_bundle_ref: null
  citation_state: ABSTAIN
outputs:
  candidate_record: data/work/hydrology/run_YYYYMMDDThhmmssZ/normalized_observation.yml
  receipt: data/receipts/pipeline/hydrology/normalize_observation/run_YYYYMMDDThhmmssZ.yml
rollback:
  required_before_publication: true
```

[⬆ Back to top](#top)

---

## 12. Tests, fixtures, receipts, and proofs

Default execution is **fixture-only, synthetic/generalized/redacted, and no-network** until normalization spec, evidence, policy, and CI coverage are approved.

Recommended tests:

```text
tests/pipelines/domains/hydrology/normalize_observation/
├── test_no_network_dry_run.py              # PROPOSED
├── test_ingest_receipt_required.py         # PROPOSED
├── test_observed_role_required.py          # PROPOSED
├── test_aggregate_not_observation.py       # PROPOSED
├── test_model_not_observation.py           # PROPOSED
├── test_regulatory_context_not_observation.py # PROPOSED
├── test_site_metadata_not_observation.py   # PROPOSED
├── test_site_parameter_units_required.py   # PROPOSED
├── test_qa_approval_state_preserved.py     # PROPOSED
├── test_provisional_not_approved.py        # PROPOSED
├── test_time_fields_not_collapsed.py       # PROPOSED
├── test_evidence_gap_abstains.py           # PROPOSED
├── test_receipt_hashes.py                  # PROPOSED
└── test_no_direct_publish.py               # PROPOSED
```

A dry run should prove fixtures load without network access, ingest receipts are required for non-fixture inputs, observed role is required, aggregates/models/regulatory/site metadata are rejected or rerouted, parameter/unit/time/QA checks run, EvidenceBundle gaps produce abstention, receipts are deterministic, and no run writes directly to public UI, public API, catalog store, published layers, or release manifests.

[⬆ Back to top](#top)

---

## 13. Promotion, publication, correction, and rollback

Hydrology observation normalization may prepare canonicalized observations and quarantine records. It does not publish.

Required chain:

```text
ingested observed Hydrology candidate
  -> normalized observation candidate
  -> validation report
  -> policy decision
  -> EvidenceBundle closure
  -> processed Hydrology observation record
  -> catalog / triplet candidate
  -> release candidate
  -> ReleaseManifest
  -> RollbackCard
  -> released artifact
```

Correction and rollback posture:

- denied, abstained, errored, restricted, stale, conflicted, and quarantined observation-normalization runs remain auditable;
- normalization receipts preserve input hashes, ingest refs, method refs, rule ids, transforms, QA/approval state, and outcomes;
- processed versions are produced by governed promotion, not hidden overwrite;
- downstream artifacts are invalidated if source refs, site refs, parameter refs, time refs, unit refs, QA refs, approval refs, evidence refs, source-role refs, or policy refs drift;
- release rollback is owned by `release/`, not by this directory.

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- fills the blank `pipelines/domains/hydrology/normalize_observation/README.md` file;
- identifies this directory as a nested executable Hydrology observation-normalization sublane;
- prevents connector, source-profile, ingest, schema, contract, policy, fixture, test, data, proof, catalog, aggregate/model normalization, and release authority from being placed here;
- preserves observed source role, site identity, parameter codes, units, qualifiers, QA flags, approval state, time basis, evidence, policy, lifecycle, catalog/triplet, release, correction, and rollback boundaries;
- blocks aggregate-as-observation, model-as-observation, regulatory-context-as-observation, site-metadata-as-observation, provisional-as-approved, generated-summary-as-evidence, and direct catalog/release writes;
- gives maintainers a fixture-first, fail-closed expansion pattern.

Future executable work in this sublane is done only when it has fixture coverage, schema-backed candidates, contract conformance, observed-role/site/parameter/unit/QA/approval/time/evidence/no-direct-publish tests, deterministic receipts, CI coverage, steward-review handoff, and release/correction/rollback documentation.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `HYDRO-NORM-OBS-001` | Should observation normalization remain a dedicated sublane or be implemented as validators inside generic `pipelines/domains/hydrology/normalize/`? | NEEDS VERIFICATION / ADR |
| `HYDRO-NORM-OBS-002` | Which schema owns normalized Hydrology observation candidates and quarantine reasons? | NEEDS VERIFICATION |
| `HYDRO-NORM-OBS-003` | Which first-wave observed inputs should normalize first: USGS Water IV, peaks, groundwater, water quality, or all observed candidates? | NEEDS VERIFICATION |
| `HYDRO-NORM-OBS-004` | Which CI job owns observation-normalization invariant tests? | UNKNOWN |
| `HYDRO-NORM-OBS-005` | How should rating conversions such as stage-to-discharge be represented without rewriting original observations? | NEEDS VERIFICATION / ADR |
| `HYDRO-NORM-OBS-006` | Which receipt type owns unit conversion, parameter-code normalization, QA normalization, and provisional-to-approved replacement? | PROPOSED / NEEDS ADR |
| `HYDRO-NORM-OBS-007` | Should catalog handoff be forbidden as an observation-normalize side effect, or allowed only through an explicit chained spec? | NEEDS VERIFICATION |

---

## Maintainer note

Start with synthetic/generalized fixture-only dry runs and negative tests. Do not add live source fetching, source-specific ingest logic, aggregate/model/regulatory normalization, direct catalog writes, public layer writes, release-manifest writes, advisory language, or direct API payload generation until observed-role preservation, site/parameter/unit/time/QA normalization, evidence closure, release review, and rollback are proven.
