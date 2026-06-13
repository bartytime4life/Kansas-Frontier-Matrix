<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-soil-uscrn-ingest-readme
title: Soil USCRN Ingest Pipeline README
type: readme
version: v0.1
status: draft
owners:
  - <soil-pipeline-owner>
  - <soil-domain-steward>
  - <noaa-source-steward>
  - <source-steward>
  - <evidence-steward>
  - <policy-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: pipelines/domains/soil/uscrn_ingest/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipelines/domains/README.md
  - pipelines/domains/soil/README.md
  - docs/domains/soil/ARCHITECTURE.md
  - docs/domains/soil/DATA_LIFECYCLE.md
  - docs/domains/soil/CANONICAL_PATHS.md
  - docs/sources/catalog/noaa/noaa-uscrn.md
  - docs/sources/catalog/noaa/README.md
  - docs/sources/catalog/noaa/RIGHTS-AND-SENSITIVITY-MAP.md
  - pipeline_specs/soil/uscrn_ingest.yaml
  - contracts/domains/soil/
  - schemas/contracts/v1/domains/soil/
  - policy/domains/soil/
  - data/raw/soil/
  - data/work/soil/
  - data/quarantine/soil/
  - data/processed/soil/
  - data/catalog/domain/soil/
  - data/receipts/pipeline/
  - data/proofs/evidence_bundle/
  - release/candidates/soil/
tags:
  - kfm
  - pipelines
  - domains
  - soil
  - noaa
  - uscrn
  - ingest
  - station-observation
  - soil-moisture
  - soil-temperature
  - depth-aware
  - support-type-separation
  - evidence
  - policy
  - governance
notes:
  - "This README fills the blank pipelines/domains/soil/uscrn_ingest path as a Soil-domain executable sublane."
  - "USCRN ingest logic is executable implementation support only; it does not own NOAA source descriptors, source catalog profiles, connector/fetch logic, schemas, policy, lifecycle data, catalog truth, or release decisions."
  - "The subdirectory name uses the requested underscore form uscrn_ingest; if repo slug rules prefer hyphenated names, record the path decision with ADR/path-map/rollback notes before moving."
  - "USCRN station observations must preserve station, variable, depth, cadence, quality flag, source role, time basis, support type, and receipt lineage."
  - "Station-as-area, depth-collapse, cadence-collapse, reference-as-regulatory, and current-guidance collapses fail closed by default."
  - "Concrete executable behavior, connector linkage, schedules, CI coverage, schema paths, release wiring, and public API/map behavior remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# NOAA USCRN Soil Ingest Pipeline

> Executable Soil-domain sublane for normalizing admitted NOAA U.S. Climate Reference Network soil variables into KFM work candidates, quarantine records, processed candidates, catalog/triplet handoffs, receipts, and release-review packages — without collapsing station observations into area truth, one depth into another depth, one cadence into another cadence, or reference-grade observations into regulatory or operational authority.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-USCRN%20soil%20ingest-2e7d32)
![authority](https://img.shields.io/badge/authority-executable%20logic-0a7ea4)
![support](https://img.shields.io/badge/support--type-station__soil__moisture-d62728)
![publication](https://img.shields.io/badge/publication-release%20gated-d62728)
![ci](https://img.shields.io/badge/CI-TODO-lightgrey)

**Status:** Draft  
**Path:** `pipelines/domains/soil/uscrn_ingest/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Domain lane:** Soil  
**Sublane:** NOAA USCRN ingest  
**Placement posture:** nested executable sublane under `pipelines/domains/soil/`; concrete executable behavior remains `PROPOSED / NEEDS VERIFICATION` unless backed by tests and repo evidence  
**Public posture:** no direct publication; public output requires lifecycle, EvidenceBundle, source-role, support-type tag, depth/cadence preservation, rights, sensitivity, policy, catalog/triplet, release, correction, and rollback closure

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. USCRN anti-collapse rules](#3-uscrn-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Ingest scope](#6-ingest-scope)
- [7. Source-family posture](#7-source-family-posture)
- [8. Lifecycle contract](#8-lifecycle-contract)
- [9. Required gates](#9-required-gates)
- [10. Directory contract](#10-directory-contract)
- [11. Inputs and outputs](#11-inputs-and-outputs)
- [12. Minimal USCRN ingest candidate record](#12-minimal-uscrn-ingest-candidate-record)
- [13. Dry-run, tests, fixtures, receipts, and proofs](#13-dry-run-tests-fixtures-receipts-and-proofs)
- [14. Promotion, publication, correction, and rollback](#14-promotion-publication-correction-and-rollback)
- [15. Definition of done](#15-definition-of-done)
- [16. Open questions](#16-open-questions)

---

## 1. Purpose

`pipelines/domains/soil/uscrn_ingest/` is the executable sublane for NOAA USCRN soil-variable normalization inside the Soil domain.

It supports candidate processing for:

- USCRN station metadata needed for soil-variable lineage;
- soil-moisture and soil-temperature observations where the USCRN product provides them;
- variable/depth/cadence-specific observation candidates;
- quality flag propagation and source-vintage/freshness posture;
- time normalization and timezone harmonization;
- support-type tagging as `station_soil_moisture` or the accepted soil-station support label;
- quarantine records for unresolved metadata, missing depth, missing cadence, missing quality flags, unknown rights, schema drift, or support-type failure;
- catalog/triplet handoff packages after evidence and validation close.

This directory implements or will implement the **how** of USCRN Soil ingest. It does not fetch from NOAA directly, define NOAA source identity, define Soil object meaning, define schemas, encode policy, store lifecycle data, decide public release, or turn USCRN observations into regional truth.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable pipeline logic: the **how**. | CONFIRMED root responsibility |
| Why `domains/soil/`? | Soil is the domain lane; Soil docs place executable logic under `pipelines/domains/soil/`. | CONFIRMED documentation pattern; behavior NEEDS VERIFICATION |
| Why `uscrn_ingest/`? | This is a narrow executable sublane for USCRN soil-variable normalization under Soil. | PROPOSED / NEEDS VERIFICATION |
| Is this a connector? | No. Source fetching belongs in `connectors/<source>` or an accepted source-edge home. This sublane reads admitted lifecycle inputs or fixtures. | CONFIRMED separation |
| Where does the source profile live? | `docs/sources/catalog/noaa/noaa-uscrn.md`. | CONFIRMED source-doc path |
| Where does a declarative run spec live? | `pipeline_specs/soil/uscrn_ingest.yaml` or accepted spec home. | PROPOSED / NEEDS VERIFICATION |
| Where do schemas and contracts live? | `schemas/contracts/v1/domains/soil/` and `contracts/domains/soil/` or accepted homes. | PROPOSED / NEEDS VERIFICATION |
| Can this sublane publish? | No. It may prepare candidates and release handoffs only through governed workflow. | CONFIRMED doctrine posture |

> [!IMPORTANT]
> USCRN ingest code is subordinate to SourceDescriptor, source-role, quality flags, depth/cadence preservation, support-type tagging, EvidenceBundle closure, policy decisions, release manifests, correction notices, and rollback cards. A successful ingest is not public release.

[⬆ Back to top](#top)

---

## 3. USCRN anti-collapse rules

USCRN must remain a station observation product.

Disallowed collapses:

```text
station reading -> county value
station reading -> regional surface
5 cm value -> 100 cm value
hourly value -> daily value without aggregation receipt
USCRN reference observation -> regulatory determination
USCRN observation -> current guidance
USCRN soil observation -> crop/yield truth
USCRN station comparison -> validation result without comparison receipt
```

Required distinctions:

- station id and station geometry remain station-scoped;
- variable names are explicit;
- depth is explicit where the soil variable is depth-aware;
- cadence is explicit;
- quality flags are retained or quarantine reason is recorded;
- source role remains `observation` for native station readings;
- KFM-derived aggregation, interpolation, gap-fill, or surface creation becomes a separate derived artifact with its own receipt.

[⬆ Back to top](#top)

---

## 4. What belongs here

Files belong here when their primary responsibility is executable USCRN Soil ingest processing.

Appropriate contents include:

- fixture-only dry-run entrypoints for USCRN soil ingest;
- station metadata normalization helpers scoped to Soil ingest;
- soil-variable column/field mapping helpers;
- variable/depth/cadence parsing helpers;
- quality flag and missing-value normalization helpers;
- timezone and timestamp normalization helpers;
- source-role and support-type validators;
- station-as-area, depth-collapse, cadence-collapse, and aggregation-denial validators;
- quarantine routing helpers for missing metadata, missing depth, unsupported cadence, rights uncertainty, or validation failure;
- receipt emitters, if not shared;
- catalog/triplet handoff helpers, if not centralized in `pipelines/catalog/`;
- thin adapters that read governed lifecycle inputs, not live NOAA endpoints.

A good placement test:

> If the code transforms admitted USCRN lifecycle inputs into Soil observation candidates, quarantine records, processed records, receipts, or catalog handoffs, it may belong here. If it fetches NOAA data, defines source identity, defines schemas, encodes policy, creates public maps, or approves release, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| NOAA fetcher / source-edge connector | `connectors/noaa/` or accepted connector home |
| NOAA USCRN source profile | `docs/sources/catalog/noaa/noaa-uscrn.md` |
| Source descriptors / source registry entries | `data/registry/sources/soil/`, `data/registry/sources/noaa/`, or accepted registry home |
| Soil architecture and doctrine | `docs/domains/soil/...` |
| Object meaning contracts | `contracts/domains/soil/...` |
| JSON Schemas | `schemas/contracts/v1/domains/soil/...` |
| Policy bundles and release rules | `policy/domains/soil/`, rights, sensitivity, and release policy roots |
| Declarative run specs | `pipeline_specs/soil/...` |
| Fixtures | `fixtures/domains/soil/uscrn_ingest/` or accepted fixture home |
| Tests | `tests/pipelines/domains/soil/uscrn_ingest/` or accepted test home |
| Raw, work, quarantine, processed, catalog, triplet, or published outputs | `data/...` lifecycle homes |
| Receipts and proofs | `data/receipts/...`, `data/proofs/...` |
| Release decisions | `release/candidates/soil/`, `release/manifests/soil/`, rollback/correction release homes |
| Public API or map code | `apps/governed-api/`, `apps/explorer-web/`, packages |
| Regional interpolation, gap-fill, or gridded products | Separate modeled/derived pipeline with separate receipt, not native USCRN ingest |

[⬆ Back to top](#top)

---

## 6. Ingest scope

| Scope area | Pipeline responsibility | Publication posture |
|---|---|---|
| Station metadata | Normalize station id, location reference, elevation where present, and source metadata. | Station scoped; not area truth. |
| Soil moisture | Normalize station/depth/cadence observations with units and quality flags. | Requires support type and depth. |
| Soil temperature | Normalize station/depth/cadence observations with units and quality flags. | Requires support type and depth. |
| Time basis | Normalize timestamp, timezone, cadence, valid time, and processing time. | No cadence collapse without receipt. |
| Quality flags | Preserve NOAA quality flags or record quarantine reason. | Public products need quality posture. |
| Source role | Preserve native station readings as observation. | Aggregates or models are separate artifacts. |
| Catalog/triplet handoff | Prepare restricted or public-safe catalog/graph candidates after evidence closure. | Projection does not replace canonical review state. |

[⬆ Back to top](#top)

---

## 7. Source-family posture

This sublane is for NOAA USCRN soil variables only.

It may consume:

- no-network synthetic or redacted USCRN-like fixtures;
- admitted immutable USCRN raw captures under `data/raw/soil/` or an accepted NOAA raw home;
- work candidates from a governed source-edge ingest;
- approved source registry metadata and source descriptors;
- policy, schema, and contract refs used by validators.

It must not activate a source by itself. Source activation requires source descriptor coverage, rights posture, sensitivity classification, retrieval method, source head/cadence, fixtures, validation, and review routing.

[⬆ Back to top](#top)

---

## 8. Lifecycle contract

Every USCRN ingest run must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal stance:

1. **Read** approved fixtures, immutable raw captures, work candidates, quarantine inputs in remediation mode, or prior processed baselines.
2. **Normalize** into station-scoped Soil observation candidates with source role, support type, variable, depth, cadence, unit, quality flag, temporal scope, evidence references, and receipt refs.
3. **Quarantine** unresolved rights, missing station identity, missing variable, missing depth, missing cadence, unit ambiguity, quality-flag failure, support-type failure, schema drift, or validation failure.
4. **Promote to processed** only after validation, policy, evidence, support-type, quality, and review gates close.
5. **Prepare catalog/triplet handoffs** only after processed-state and evidence closure, and only with station/depth/cadence caveats.
6. **Publish** only through release decisions, public-safe artifacts, rollback targets, and correction paths.

Promotion is a governed state transition with receipts and review evidence, not a file move.

[⬆ Back to top](#top)

---

## 9. Required gates

Every USCRN ingest run must check or explicitly fail closed on:

1. **Source descriptor gate** — NOAA USCRN source identity, role, cadence, rights, and sensitivity posture are known.
2. **Source-role gate** — native USCRN station records remain observation records.
3. **Station-scope gate** — station reading is not area truth.
4. **Variable gate** — each candidate names the observed variable.
5. **Depth gate** — depth-aware soil variables preserve depth and do not substitute one depth for another.
6. **Cadence gate** — hourly, daily, monthly, or other cadence products remain distinct unless an aggregation receipt exists.
7. **Support-type gate** — USCRN soil observations carry the accepted station soil support label.
8. **Unit and quality gate** — units, missing values, and quality flags are preserved or quarantined.
9. **Time gate** — observed time, valid time, retrieval time, processing time, catalog time, release time, and correction time remain distinct.
10. **Rights gate** — unknown or restrictive license, permission, attribution, privacy, or redistribution terms block public release.
11. **Sensitivity gate** — station metadata, cross-lane joins, private-network comparisons, or field-specific inferences fail closed until reviewed.
12. **Derived-artifact gate** — interpolation, gap-fill, gridding, spatial averaging, or comparison products require a separate derivation/model/comparison receipt.
13. **Schema, contract, evidence, policy, validation, receipt, catalog/triplet, and release gates** — all must close or the run abstains, denies, or quarantines.
14. **No-direct-publish gate** — no writes to public UI, public API, or `data/published/` without release workflow authority.

[⬆ Back to top](#top)

---

## 10. Directory contract

Recommended shape:

```text
pipelines/domains/soil/uscrn_ingest/
├── README.md                         # this file
├── PIPELINE_CONTRACT.md              # PROPOSED: sublane execution contract
├── run_dry_fixture.py                # PROPOSED synthetic/redacted fixture only
├── normalize_station_metadata.py     # PROPOSED
├── normalize_soil_observation.py     # PROPOSED
├── parse_variable_depth_cadence.py   # PROPOSED
├── normalize_quality_flags.py        # PROPOSED
├── normalize_time_basis.py           # PROPOSED
├── validate_station_scope.py         # PROPOSED
├── validate_depth_cadence.py         # PROPOSED
├── validate_support_type.py          # PROPOSED
├── build_catalog_handoff.py          # PROPOSED if not centralized in pipelines/catalog/
├── emit_receipt.py                   # PROPOSED only if not shared
└── adapters/                         # PROPOSED thin lifecycle adapters, no NOAA fetching
```

Declarative specs should live outside this directory:

```text
pipeline_specs/soil/uscrn_ingest.yaml # PROPOSED / NEEDS VERIFICATION
```

Generated outputs must not be written beside the code that generated them. Use accepted lifecycle homes under `data/`, proof homes under `data/proofs/`, receipt homes under `data/receipts/`, and release homes under `release/`.

[⬆ Back to top](#top)

---

## 11. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Fixture input | `fixtures/domains/soil/uscrn_ingest/` or accepted fixture home | Synthetic, generalized, or redacted. |
| Raw USCRN capture | `data/raw/soil/<source_id>/<run_id>/` or accepted NOAA raw home | Immutable source-edge capture with source descriptor and receipt. |
| Work candidate | `data/work/soil/<run_id>/` | Candidate only. |
| Quarantine record | `data/quarantine/soil/<reason>/<run_id>/` | Failed, restricted, unresolved, or unsafe material. |
| Processed observations | `data/processed/soil/<dataset_id>/<version>/` | Validated/restricted; not automatically public. |
| Catalog candidate | `data/catalog/domain/soil/...` or approved catalog home | After processed-state, transform, and evidence gates. |
| Receipts / proofs | `data/receipts/...`, `data/proofs/...` | Required for auditable promotion and release review. |
| Release handoff | `release/candidates/soil/...` | Only through release workflow. |

[⬆ Back to top](#top)

---

## 12. Minimal USCRN ingest candidate record

The final schema is not defined here. This example shows the minimum information a USCRN ingest candidate should preserve.

```yaml
schema_version: kfm.soil_uscrn_ingest_candidate.v1
candidate_id: soil_uscrn_<station_id>_<variable>_<depth>_<timestamp_hash>
pipeline_id: domains.soil.uscrn_ingest
run_id: run_YYYYMMDDThhmmssZ
status: WORK_CANDIDATE
source:
  source_id: noaa_uscrn
  source_role: observation
  lifecycle_ref: data/raw/soil/noaa_uscrn/<run_id>/
  input_hash: sha256:<hash>
  rights_state: needs_review
station:
  station_id: <station_id>
  station_ref: <station_ref>
  geometry_scope: station_point
observation:
  variable: <soil_moisture|soil_temperature|other_soil_variable>
  support_type: station_soil_moisture
  depth_cm: <number_or_null>
  cadence: <native|hourly|daily|monthly|other>
  observed_at: YYYY-MM-DDThh:mm:ssZ
  value: <number_or_null>
  unit: <unit>
  quality_flags: []
anti_collapse:
  station_reading_is_area_truth: false
  depth_substitution_allowed: false
  cadence_substitution_allowed: false
  reference_observation_is_regulatory: false
  generated_summary_is_evidence: false
policy:
  outcome: ABSTAIN
  reason_code: SOURCE_DESCRIPTOR_SUPPORT_TYPE_OR_EVIDENCE_NOT_RESOLVED
evidence:
  evidence_bundle_ref: null
  citation_state: ABSTAIN
outputs:
  candidate_record: data/work/soil/run_YYYYMMDDThhmmssZ/uscrn_candidate.yml
  receipt: data/receipts/pipeline/soil/uscrn_ingest/run_YYYYMMDDThhmmssZ.yml
rollback:
  required_before_publication: true
```

[⬆ Back to top](#top)

---

## 13. Dry-run, tests, fixtures, receipts, and proofs

Default execution is **fixture-only, synthetic/generalized/redacted, and no-network** until source activation, rights review, support-type review, quality-flag review, and CI coverage are approved.

Recommended tests:

```text
tests/pipelines/domains/soil/uscrn_ingest/
├── test_no_network_dry_run.py             # PROPOSED
├── test_source_role_observation.py        # PROPOSED
├── test_station_not_area.py               # PROPOSED
├── test_depth_required_for_soil_variables.py # PROPOSED
├── test_depth_not_substituted.py          # PROPOSED
├── test_cadence_not_collapsed.py          # PROPOSED
├── test_quality_flags_preserved.py        # PROPOSED
├── test_support_type_required.py          # PROPOSED
├── test_derived_surface_requires_receipt.py # PROPOSED
├── test_missing_evidence_abstains.py      # PROPOSED
├── test_receipt_hashes.py                 # PROPOSED
└── test_no_direct_publish.py              # PROPOSED
```

A dry run should prove fixtures load without network access, native records remain station observations, depth and cadence are preserved, missing support type is denied or quarantined, quality flags are retained, EvidenceBundle gaps produce abstention, receipts are deterministic, and no run writes directly to public UI, public API, `data/published/`, or release manifests.

[⬆ Back to top](#top)

---

## 14. Promotion, publication, correction, and rollback

USCRN ingest may prepare candidates. It does not publish.

Required promotion chain:

```text
USCRN raw/work input
  -> station/depth/cadence observation candidate
  -> validation report
  -> policy decision
  -> support-type / quality / time receipt where required
  -> EvidenceBundle closure
  -> processed Soil observation dataset version
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
- derived products are invalidated if station refs, depth refs, cadence refs, quality refs, support-type refs, method refs, or policy refs drift;
- public artifact rollback is owned by `release/`, not by this directory.

[⬆ Back to top](#top)

---

## 15. Definition of done

This README is done when it:

- fills the blank `pipelines/domains/soil/uscrn_ingest/README.md` file;
- identifies this directory as a nested executable Soil sublane;
- prevents connector, schema, contract, policy, fixture, test, data, receipt, proof, catalog, and release authority from being placed here;
- preserves station scope, variable/depth/cadence, support-type, source-role, quality, evidence, policy, lifecycle, catalog/triplet, release, correction, and rollback boundaries;
- blocks station-as-area, depth-collapse, cadence-collapse, and supportless-value promotion;
- gives maintainers a fixture-first, fail-closed expansion pattern.

Future executable work in this sublane is done only when it has source-descriptor coverage, synthetic/generalized/redacted no-network fixtures, schema-backed candidates, contract conformance, source-role/support-type/depth/cadence/quality/evidence tests, deterministic receipts, no-direct-publish tests, CI coverage, steward-review handoff, and release/correction/rollback documentation.

[⬆ Back to top](#top)

---

## 16. Open questions

| ID | Question | Status |
|---|---|---|
| `SOIL-USCRN-001` | Should the subdirectory remain `uscrn_ingest` or be renamed to a hyphenated slug after path convention review? | NEEDS VERIFICATION / ADR |
| `SOIL-USCRN-002` | Which connector or source-edge job owns NOAA USCRN retrieval before this ingest sublane reads lifecycle inputs? | NEEDS VERIFICATION |
| `SOIL-USCRN-003` | Which USCRN soil variables and depths are first-wave approved for fixture-only dry runs? | NEEDS VERIFICATION |
| `SOIL-USCRN-004` | Which CI job owns USCRN ingest invariant tests? | UNKNOWN |
| `SOIL-USCRN-005` | Should catalog handoff logic live here or in centralized `pipelines/catalog/` with a USCRN adapter? | NEEDS VERIFICATION |
| `SOIL-USCRN-006` | Which public-safe map/API products are allowed after review and release, and at what station/depth/cadence caveat level? | NEEDS VERIFICATION |
| `SOIL-USCRN-007` | Which receipt type owns USCRN-derived spatial interpolation, multi-station aggregation, or station-to-satellite comparison products? | PROPOSED / NEEDS ADR |

---

## Maintainer note

Start with synthetic/generalized fixture-only dry runs and negative tests. Do not add live NOAA fetching, station-as-area outputs, depth substitution, cadence substitution, derived surfaces, public map layers, release handoff automation, or direct API payload generation until source roles, rights, support-type separation, quality validation, evidence closure, and rollback are proven.
