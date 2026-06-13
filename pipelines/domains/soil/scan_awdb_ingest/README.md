<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-soil-scan-awdb-ingest-readme
title: Soil SCAN AWDB Ingest Pipeline README
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
path: pipelines/domains/soil/scan_awdb_ingest/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipelines/domains/README.md
  - pipelines/domains/soil/README.md
  - docs/domains/soil/ARCHITECTURE.md
  - docs/domains/soil/DATA_LIFECYCLE.md
  - docs/domains/soil/CANONICAL_PATHS.md
  - docs/sources/catalog/nrcs/scan-soil-climate.md
  - docs/sources/catalog/nrcs/ssurgo.md
  - docs/sources/catalog/nrcs/gssurgo.md
  - pipeline_specs/soil/scan_awdb_ingest.yaml
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
  - nrcs
  - scan
  - awdb
  - ingest
  - station-observation
  - soil-moisture
  - soil-temperature
  - sensor-depth
  - heartbeat-freshness
  - support-type-separation
  - evidence
  - policy
  - governance
notes:
  - "This README fills the blank pipelines/domains/soil/scan_awdb_ingest path as a Soil-domain executable sublane."
  - "SCAN/AWDB ingest logic is executable implementation support only; it does not own NRCS source descriptors, source catalog profiles, source fetching, schemas, policy, lifecycle data, catalog truth, or release decisions."
  - "The subdirectory name uses the requested underscore form scan_awdb_ingest; if repo slug rules prefer hyphenated names, record the path decision with ADR/path-map/rollback notes before moving."
  - "SCAN station observations must preserve station id, variable, sensor depth, cadence, quality flag, timezone behavior, source role, heartbeat freshness, support type, and receipt lineage."
  - "Watcher signals are candidate evidence only; admitted station readings are observed records; modeled or aggregated derivatives require separate receipts."
  - "Concrete executable behavior, source linkage, schedules, CI coverage, schema paths, release wiring, and public API/map behavior remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# NRCS SCAN / AWDB Soil Ingest Pipeline

> Executable Soil-domain sublane for normalizing admitted NRCS SCAN / AWDB soil-climate station readings into KFM work candidates, quarantine records, processed candidates, catalog/triplet handoffs, receipts, and release-review packages — without collapsing station observations into area truth, watcher signals into published facts, one sensor depth into another depth, one cadence into another cadence, or modeled/aggregated derivatives into observed station readings.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-SCAN%20AWDB%20soil%20ingest-2e7d32)
![authority](https://img.shields.io/badge/authority-executable%20logic-0a7ea4)
![support](https://img.shields.io/badge/support--type-station__soil__moisture-d62728)
![publication](https://img.shields.io/badge/publication-release%20gated-d62728)
![ci](https://img.shields.io/badge/CI-TODO-lightgrey)

**Status:** Draft  
**Path:** `pipelines/domains/soil/scan_awdb_ingest/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Domain lane:** Soil  
**Sublane:** NRCS SCAN / AWDB ingest  
**Placement posture:** nested executable sublane under `pipelines/domains/soil/`; concrete executable behavior remains `PROPOSED / NEEDS VERIFICATION` unless backed by tests and repo evidence  
**Public posture:** no direct publication; public output requires lifecycle, EvidenceBundle, source-role, support-type tag, station/depth/cadence preservation, freshness, rights, sensitivity, policy, catalog/triplet, release, correction, and rollback closure

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. SCAN / AWDB anti-collapse rules](#3-scan--awdb-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Ingest scope](#6-ingest-scope)
- [7. Lifecycle contract](#7-lifecycle-contract)
- [8. Required gates](#8-required-gates)
- [9. Directory contract](#9-directory-contract)
- [10. Inputs and outputs](#10-inputs-and-outputs)
- [11. Minimal SCAN / AWDB ingest candidate record](#11-minimal-scan--awdb-ingest-candidate-record)
- [12. Tests, receipts, and proofs](#12-tests-receipts-and-proofs)
- [13. Promotion, publication, correction, and rollback](#13-promotion-publication-correction-and-rollback)
- [14. Definition of done](#14-definition-of-done)
- [15. Open questions](#15-open-questions)

---

## 1. Purpose

`pipelines/domains/soil/scan_awdb_ingest/` is the executable sublane for NRCS SCAN / AWDB station-reading normalization inside the Soil domain.

It supports candidate processing for:

- SCAN station metadata and AWDB source references;
- soil-moisture and soil-temperature observations where the admitted source provides them;
- ancillary station climate observations that must stay secondary to the Soil ingest purpose;
- station/depth/cadence-specific observation candidates;
- source timezone behavior, observation time, retrieval time, processing time, and heartbeat freshness;
- quality flag propagation, missing-value handling, and stale-source routing;
- support-type tagging as `station_soil_moisture` or the accepted soil-station support label;
- quarantine records for unresolved metadata, missing depth, missing cadence, stale heartbeat, missing quality flags, unknown rights, schema drift, or support-type failure;
- catalog/triplet handoff packages after evidence, validation, and policy close.

This directory implements or will implement the **how** of SCAN / AWDB Soil ingest. It does not fetch from NRCS directly, define NRCS source identity, define Soil object meaning, define schemas, encode policy, store lifecycle data, decide public release, or turn station observations into area-wide truth, static survey truth, gridded satellite truth, crop/yield truth, or management advice.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable pipeline logic: the **how**. | CONFIRMED root responsibility |
| Why `domains/soil/`? | Soil is the domain lane; Soil docs place executable logic under `pipelines/domains/soil/`. | CONFIRMED documentation pattern; behavior NEEDS VERIFICATION |
| Why `scan_awdb_ingest/`? | This is a narrow executable sublane for SCAN / AWDB station-reading normalization under Soil. | PROPOSED / NEEDS VERIFICATION |
| Is this a source fetcher? | No. Source fetching belongs in `connectors/<source>` or an accepted source-edge home. This sublane reads admitted lifecycle inputs or fixtures. | CONFIRMED separation |
| Where does the source profile live? | `docs/sources/catalog/nrcs/scan-soil-climate.md`. | CONFIRMED source-doc path |
| Where does a declarative run spec live? | `pipeline_specs/soil/scan_awdb_ingest.yaml` or accepted spec home. | PROPOSED / NEEDS VERIFICATION |
| Where do schemas and contracts live? | `schemas/contracts/v1/domains/soil/` and `contracts/domains/soil/` or accepted homes. | PROPOSED / NEEDS VERIFICATION |
| Can this sublane publish? | No. It may prepare candidates and release handoffs only through governed workflow. | CONFIRMED doctrine posture |

> [!IMPORTANT]
> SCAN / AWDB ingest code is subordinate to SourceDescriptor, source role, station metadata, sensor-depth schema, timezone behavior, QA flags, heartbeat freshness, support-type tagging, EvidenceBundle closure, policy decisions, release manifests, correction notices, and rollback cards. A successful ingest is not public release.

[⬆ Back to top](#top)

---

## 3. SCAN / AWDB anti-collapse rules

SCAN / AWDB must remain station-scoped observed time-series evidence unless a downstream receipt proves a separate derivative.

Disallowed collapses:

```text
watcher signal -> published truth
station reading -> area-wide surface
station reading -> static soil map unit property
sensor depth A -> sensor depth B
hourly value -> daily value without aggregation receipt
observed station reading -> modeled fusion product
modeled fusion product -> observed station reading
SCAN reading -> Mesonet / USCRN / SMAP value
stale station heartbeat -> current context
generated summary -> evidence
```

Required distinctions:

- watcher output is candidate evidence only;
- admitted station readings are observed records;
- station id and station geometry remain station-scoped;
- variable names are explicit;
- sensor depth is explicit where the source is depth-aware;
- cadence and timezone behavior are explicit;
- quality flags are retained or quarantine reason is recorded;
- heartbeat freshness is recorded for near-current context;
- modeled, aggregated, interpolated, or fused outputs become separate artifacts with separate receipts.

[⬆ Back to top](#top)

---

## 4. What belongs here

Files belong here when their primary responsibility is executable SCAN / AWDB Soil ingest processing.

Appropriate contents include:

- fixture-only dry-run entrypoints for SCAN / AWDB ingest;
- station metadata normalization helpers scoped to Soil ingest;
- variable/depth/cadence parsing helpers;
- timezone and timestamp normalization helpers;
- heartbeat freshness and stale-source classifiers;
- quality flag and missing-value normalization helpers;
- source-role and support-type validators;
- watcher-as-candidate, station-as-area, depth-collapse, cadence-collapse, and aggregation-denial validators;
- quarantine routing helpers for missing metadata, missing depth, unsupported cadence, stale heartbeat, rights uncertainty, or validation failure;
- receipt emitters, if not shared;
- catalog/triplet handoff helpers, if not centralized in `pipelines/catalog/`;
- thin adapters that read governed lifecycle inputs, not live NRCS endpoints.

A good placement test:

> If the code transforms admitted SCAN / AWDB lifecycle inputs into Soil observation candidates, quarantine records, processed records, receipts, or catalog handoffs, it may belong here. If it fetches NRCS data, defines source identity, defines schemas, encodes policy, creates public artifacts, or approves release, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| NRCS fetcher / source-edge connector | `connectors/nrcs/` or accepted connector home |
| SCAN source profile | `docs/sources/catalog/nrcs/scan-soil-climate.md` |
| Source descriptors / source registry entries | `data/registry/sources/soil/`, `data/registry/sources/nrcs/`, or accepted registry home |
| Soil architecture and doctrine | `docs/domains/soil/...` |
| Object meaning contracts | `contracts/domains/soil/...` |
| JSON Schemas | `schemas/contracts/v1/domains/soil/...` |
| Policy bundles and release rules | `policy/domains/soil/`, rights, sensitivity, and release policy roots |
| Declarative run specs | `pipeline_specs/soil/...` |
| Fixtures | `fixtures/domains/soil/scan_awdb_ingest/` or accepted fixture home |
| Tests | `tests/pipelines/domains/soil/scan_awdb_ingest/` or accepted test home |
| Raw, work, quarantine, processed, catalog, triplet, or published outputs | `data/...` lifecycle homes |
| Receipts and proofs | `data/receipts/...`, `data/proofs/...` |
| Release decisions | `release/candidates/soil/`, `release/manifests/soil/`, rollback/correction release homes |
| Public API or map code | `apps/governed-api/`, `apps/explorer-web/`, packages |
| Static soil mapping, satellite grids, state station networks, modeled fusion, crop/yield, drought, or management products | Owning source/domain lanes or reviewed downstream products only |

[⬆ Back to top](#top)

---

## 6. Ingest scope

| Scope area | Pipeline responsibility | Publication posture |
|---|---|---|
| Station metadata | Normalize station id, location reference, install/decommission status where available, and source metadata. | Station scoped; not area truth. |
| Soil moisture | Normalize station/depth/cadence observations with units and quality flags. | Requires support type and depth. |
| Soil temperature | Normalize station/depth/cadence observations with units and quality flags. | Requires support type and depth. |
| Ancillary climate | Preserve as secondary context with correct domain handoff where needed. | Does not replace Atmosphere domain truth. |
| Time basis | Normalize source timezone, observation time, cadence, retrieval time, and processing time. | No cadence collapse without receipt. |
| Heartbeat freshness | Classify stale source when expected updates are missing. | Stale records are not current context. |
| Quality flags | Preserve quality flags or record quarantine reason. | Public products need quality posture. |
| Source role | Preserve native station readings as observed; watcher signals as candidate. | Aggregates or models are separate artifacts. |
| Catalog/triplet handoff | Prepare restricted or public-safe catalog/graph candidates after evidence closure. | Projection does not replace canonical review state. |

[⬆ Back to top](#top)

---

## 7. Lifecycle contract

Every SCAN / AWDB ingest run must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal stance:

1. **Read** approved fixtures, immutable raw captures, work candidates, quarantine inputs in remediation mode, or prior processed baselines.
2. **Normalize** into station-scoped Soil observation candidates with source role, support type, variable, depth, cadence, unit, quality flag, timezone, heartbeat freshness, temporal scope, evidence references, and receipt refs.
3. **Quarantine** unresolved rights, missing station identity, missing variable, missing depth, missing cadence, unit ambiguity, quality-flag failure, stale heartbeat where current context is requested, support-type failure, schema drift, or validation failure.
4. **Promote to processed** only after validation, policy, evidence, support-type, quality, freshness, and review gates close.
5. **Prepare catalog/triplet handoffs** only after processed-state and evidence closure, and only with station/depth/cadence/freshness caveats.
6. **Publish** only through release decisions, public-safe artifacts, rollback targets, and correction paths.

Promotion is a governed state transition with receipts and review evidence, not a file move.

[⬆ Back to top](#top)

---

## 8. Required gates

Every SCAN / AWDB ingest run must check or explicitly fail closed on:

1. **Source descriptor gate** — NRCS SCAN source identity, role, cadence, rights, and sensitivity posture are known.
2. **Watcher gate** — watcher signals remain candidate evidence and cannot become published truth by themselves.
3. **Source-role gate** — native admitted station records remain observed records.
4. **Station-scope gate** — station reading is not area truth.
5. **Variable gate** — each candidate names the observed variable.
6. **Depth gate** — depth-aware soil variables preserve sensor depth and do not substitute one depth for another.
7. **Cadence gate** — hourly, daily, or other cadence products remain distinct unless an aggregation receipt exists.
8. **Timezone gate** — source timezone behavior, observation time, retrieval time, and processing time are recorded.
9. **Heartbeat freshness gate** — stale source state is recorded and cannot be presented as current context.
10. **Support-type gate** — SCAN soil observations carry the accepted station soil support label.
11. **Unit and quality gate** — units, missing values, and quality flags are preserved or quarantined.
12. **Derived-artifact gate** — interpolation, gap-fill, gridding, spatial averaging, comparison, or fusion products require a separate derivation/model/comparison receipt.
13. **Schema, contract, evidence, policy, validation, receipt, catalog/triplet, and release gates** — all must close or the run abstains, denies, or quarantines.
14. **No-direct-publish gate** — no writes to public UI, public API, or `data/published/` without release workflow authority.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended shape:

```text
pipelines/domains/soil/scan_awdb_ingest/
├── README.md                         # this file
├── PIPELINE_CONTRACT.md              # PROPOSED: sublane execution contract
├── run_dry_fixture.py                # PROPOSED synthetic/redacted fixture only
├── normalize_station_metadata.py     # PROPOSED
├── normalize_soil_observation.py     # PROPOSED
├── parse_variable_depth_cadence.py   # PROPOSED
├── normalize_time_basis.py           # PROPOSED
├── normalize_quality_flags.py        # PROPOSED
├── classify_heartbeat_freshness.py   # PROPOSED
├── validate_watcher_candidate.py     # PROPOSED
├── validate_station_scope.py         # PROPOSED
├── validate_depth_cadence.py         # PROPOSED
├── validate_support_type.py          # PROPOSED
├── build_catalog_handoff.py          # PROPOSED if not centralized in pipelines/catalog/
├── emit_receipt.py                   # PROPOSED only if not shared
└── adapters/                         # PROPOSED thin lifecycle adapters, no NRCS fetching
```

Declarative specs should live outside this directory:

```text
pipeline_specs/soil/scan_awdb_ingest.yaml # PROPOSED / NEEDS VERIFICATION
```

Generated outputs must not be written beside the code that generated them. Use accepted lifecycle homes under `data/`, proof homes under `data/proofs/`, receipt homes under `data/receipts/`, and release homes under `release/`.

[⬆ Back to top](#top)

---

## 10. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Fixture input | `fixtures/domains/soil/scan_awdb_ingest/` or accepted fixture home | Synthetic, generalized, or redacted. |
| Raw SCAN / AWDB capture | `data/raw/soil/<source_id>/<run_id>/` or accepted NRCS raw home | Immutable source-edge capture with source descriptor and receipt. |
| Work candidate | `data/work/soil/<run_id>/` | Candidate only. |
| Quarantine record | `data/quarantine/soil/<reason>/<run_id>/` | Failed, restricted, unresolved, stale, or unsafe material. |
| Processed observations | `data/processed/soil/<dataset_id>/<version>/` | Validated/restricted; not automatically public. |
| Catalog candidate | `data/catalog/domain/soil/...` or approved catalog home | After processed-state, transform, and evidence gates. |
| Triplet / graph delta | `data/triplets/soil/...` or approved graph-delta home | Projection only. |
| Receipts / proofs | `data/receipts/...`, `data/proofs/...` | Required for auditable promotion and release review. |
| Release handoff | `release/candidates/soil/...` | Only through release workflow. |

[⬆ Back to top](#top)

---

## 11. Minimal SCAN / AWDB ingest candidate record

The final schema is not defined here. This example shows the minimum information a SCAN / AWDB ingest candidate should preserve.

```yaml
schema_version: kfm.soil_scan_awdb_ingest_candidate.v1
candidate_id: soil_scan_<station_id>_<variable>_<depth>_<timestamp_hash>
pipeline_id: domains.soil.scan_awdb_ingest
run_id: run_YYYYMMDDThhmmssZ
status: WORK_CANDIDATE
source:
  source_id: nrcs_scan
  upstream_api_family: awdb
  source_role: observed
  lifecycle_ref: data/raw/soil/nrcs_scan/<run_id>/
  input_hash: sha256:<hash>
  rights_state: needs_review
station:
  station_id: <station_id>
  station_ref: <station_ref>
  geometry_scope: station_point
observation:
  variable: <soil_moisture|soil_temperature|ancillary_climate_variable>
  support_type: station_soil_moisture
  depth_cm: <number_or_null>
  cadence: <native|hourly|daily|other>
  source_timezone: <timezone_or_null>
  observed_at: YYYY-MM-DDThh:mm:ssZ
  value: <number_or_null>
  unit: <unit>
  quality_flags: []
freshness:
  heartbeat_expected: true
  heartbeat_state: needs_review
  stale_current_context_allowed: false
anti_collapse:
  watcher_signal_is_published_truth: false
  station_reading_is_area_truth: false
  depth_substitution_allowed: false
  cadence_substitution_allowed: false
  modeled_fusion_is_observed: false
  generated_summary_is_evidence: false
policy:
  outcome: ABSTAIN
  reason_code: SOURCE_DESCRIPTOR_SUPPORT_TYPE_FRESHNESS_OR_EVIDENCE_NOT_RESOLVED
evidence:
  evidence_bundle_ref: null
  citation_state: ABSTAIN
outputs:
  candidate_record: data/work/soil/run_YYYYMMDDThhmmssZ/scan_awdb_candidate.yml
  receipt: data/receipts/pipeline/soil/scan_awdb_ingest/run_YYYYMMDDThhmmssZ.yml
rollback:
  required_before_publication: true
```

[⬆ Back to top](#top)

---

## 12. Tests, receipts, and proofs

Default execution is **fixture-only, synthetic/generalized/redacted, and no-network** until source activation, rights review, support-type review, quality-flag review, heartbeat-freshness review, and CI coverage are approved.

Recommended tests:

```text
tests/pipelines/domains/soil/scan_awdb_ingest/
├── test_no_network_dry_run.py              # PROPOSED
├── test_watcher_signal_candidate_only.py   # PROPOSED
├── test_source_role_observed.py            # PROPOSED
├── test_station_not_area.py                # PROPOSED
├── test_depth_required_for_soil_variables.py # PROPOSED
├── test_depth_not_substituted.py           # PROPOSED
├── test_cadence_not_collapsed.py           # PROPOSED
├── test_timezone_recorded.py               # PROPOSED
├── test_heartbeat_stale_quarantines.py     # PROPOSED
├── test_quality_flags_preserved.py         # PROPOSED
├── test_support_type_required.py           # PROPOSED
├── test_derived_surface_requires_receipt.py # PROPOSED
├── test_missing_evidence_abstains.py       # PROPOSED
├── test_receipt_hashes.py                  # PROPOSED
└── test_no_direct_publish.py               # PROPOSED
```

A dry run should prove fixtures load without network access, watcher outputs remain candidate-only, admitted records remain station observations, depth and cadence are preserved, heartbeat freshness is recorded, missing support type is denied or quarantined, quality flags are retained, EvidenceBundle gaps produce abstention, receipts are deterministic, and no run writes directly to public UI, public API, `data/published/`, or release manifests.

[⬆ Back to top](#top)

---

## 13. Promotion, publication, correction, and rollback

SCAN / AWDB ingest may prepare candidates. It does not publish.

Required promotion chain:

```text
SCAN / AWDB raw/work input
  -> station/depth/cadence observation candidate
  -> validation report
  -> policy decision
  -> support-type / quality / time / freshness receipt where required
  -> EvidenceBundle closure
  -> processed Soil observation dataset version
  -> catalog / triplet candidate
  -> release candidate
  -> ReleaseManifest
  -> RollbackCard
  -> public-safe artifact
```

Correction and rollback posture:

- denied, abstained, errored, stale, restricted, and quarantined runs remain auditable;
- candidate rollback preserves receipts and proof state;
- processed versions are superseded by governed state transition, not hidden overwrite;
- derived products are invalidated if station refs, depth refs, cadence refs, quality refs, freshness refs, support-type refs, method refs, or policy refs drift;
- public artifact rollback is owned by `release/`, not by this directory.

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- fills the blank `pipelines/domains/soil/scan_awdb_ingest/README.md` file;
- identifies this directory as a nested executable Soil sublane;
- prevents connector, source-profile, schema, contract, policy, fixture, test, data, receipt, proof, catalog, and release authority from being placed here;
- preserves watcher-candidate status, station scope, variable/depth/cadence, source timezone, heartbeat freshness, support type, source role, quality, evidence, policy, lifecycle, catalog/triplet, release, correction, and rollback boundaries;
- blocks watcher-as-publisher, station-as-area, depth-collapse, cadence-collapse, stale-current-context, and supportless-value promotion;
- gives maintainers a fixture-first, fail-closed expansion pattern.

Future executable work in this sublane is done only when it has source-descriptor coverage, synthetic/generalized/redacted no-network fixtures, schema-backed candidates, contract conformance, source-role/support-type/depth/cadence/quality/freshness/evidence tests, deterministic receipts, no-direct-publish tests, CI coverage, steward-review handoff, and release/correction/rollback documentation.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `SOIL-SCAN-001` | Should the subdirectory remain `scan_awdb_ingest` or be renamed to a hyphenated slug after path convention review? | NEEDS VERIFICATION / ADR |
| `SOIL-SCAN-002` | Which connector or source-edge job owns NRCS SCAN / AWDB retrieval before this ingest sublane reads lifecycle inputs? | NEEDS VERIFICATION |
| `SOIL-SCAN-003` | Which station variables, depths, cadence classes, timezone rules, and quality flags are first-wave approved for fixture-only dry runs? | NEEDS VERIFICATION |
| `SOIL-SCAN-004` | Which CI job owns SCAN / AWDB ingest invariant tests? | UNKNOWN |
| `SOIL-SCAN-005` | Should catalog handoff logic live here or in centralized `pipelines/catalog/` with a SCAN adapter? | NEEDS VERIFICATION |
| `SOIL-SCAN-006` | Which public-safe map/API products are allowed after review and release, and at what station/depth/cadence/freshness caveat level? | NEEDS VERIFICATION |
| `SOIL-SCAN-007` | Which receipt type owns SCAN-to-SMAP, SCAN-to-Mesonet, SCAN-to-USCRN, or station-to-surface comparison products? | PROPOSED / NEEDS ADR |

---

## Maintainer note

Start with synthetic/generalized fixture-only dry runs and negative tests. Do not add live NRCS fetching, station-as-area outputs, depth substitution, cadence substitution, stale-current-context outputs, derived surfaces, public map layers, release handoff automation, or direct API payload generation until source roles, rights, support-type separation, quality validation, heartbeat freshness, evidence closure, and rollback are proven.
