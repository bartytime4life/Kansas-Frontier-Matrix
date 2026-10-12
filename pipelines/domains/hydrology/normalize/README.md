<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-hydrology-normalize-readme
title: Hydrology Normalize Pipeline README
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
path: pipelines/domains/hydrology/normalize/README.md
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
  - pipeline_specs/hydrology/normalize.yaml
  - contracts/domains/hydrology/
  - schemas/contracts/v1/domains/hydrology/
  - policy/domains/hydrology/
  - policy/sensitivity/hydrology/
  - data/raw/hydrology/
  - data/work/hydrology/
  - data/quarantine/hydrology/
  - data/processed/hydrology/
  - data/catalog/domain/hydrology/
  - data/triplets/hydrology/
  - data/registry/sources/hydrology/
  - data/receipts/pipeline/
  - data/proofs/evidence_bundle/
  - release/candidates/hydrology/
  - release/manifests/hydrology/
tags:
  - kfm
  - pipelines
  - domains
  - hydrology
  - normalize
  - canonicalization
  - source-role
  - time-normalization
  - geometry-normalization
  - unit-normalization
  - qa-normalization
  - evidence-bundle
  - nfhl
  - gauge
  - watershed
  - huc
  - public-safe
  - evidence
  - policy
  - governance
notes:
  - "This README fills the blank pipelines/domains/hydrology/normalize path as a nested executable Hydrology normalization sublane."
  - "Hydrology normalize logic is executable implementation support only; it does not own source descriptors, connectors, schemas, policy, lifecycle data, catalog truth, operational decisions, regulatory determinations, or release decisions."
  - "Normalization is not ingest, validation, processed-state promotion, catalog closure, or publication. It transforms admitted work candidates into canonicalized work/processed candidates only under governed gates."
  - "Observed readings, modeled hydrographs, regulatory context, official-source context, terrain/topology derivatives, aggregates, and generated summaries must remain separate truth classes."
  - "NFHL remains regulatory context only and must never normalize into observed flooding."
  - "Concrete executable behavior, source linkage, schedules, CI coverage, schema paths, release wiring, and public API/map behavior remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hydrology Normalize Pipeline

> Executable Hydrology sublane for canonicalizing admitted Hydrology work candidates into schema-ready normalized records, quarantine records, validation handoffs, receipts, and downstream processed/catalog/release-review packages — without collapsing source roles, time bases, units, QA states, geometries, regulatory context, modeled products, observed records, or release state.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-hydrology%20normalize-2e7d32)
![authority](https://img.shields.io/badge/authority-executable%20logic-0a7ea4)
![source-role](https://img.shields.io/badge/source--role-preserved-d62728)
![anti-collapse](https://img.shields.io/badge/NFHL%20%E2%89%A0%20observed%20flooding-d62728)
![publication](https://img.shields.io/badge/publication-release%20gated-d62728)
![ci](https://img.shields.io/badge/CI-TODO-lightgrey)

**Status:** Draft  
**Path:** `pipelines/domains/hydrology/normalize/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Domain lane:** Hydrology  
**Sublane:** Normalize / canonicalization  
**Placement posture:** nested executable sublane under `pipelines/domains/hydrology/`; concrete executable behavior remains `PROPOSED / NEEDS VERIFICATION` unless backed by tests and repo evidence  
**Publication posture:** no direct publication; normalized output is validation/processed-state input only and requires downstream evidence, policy, catalog, release, correction, and rollback closure

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

`pipelines/domains/hydrology/normalize/` is the executable sublane for Hydrology canonicalization after source material has already entered the KFM lifecycle.

It supports normalization for:

- watershed and HUC candidates;
- stream, river, reach, waterbody, gauge, well, and observation-site candidates;
- flow, stage, water-level, water-quality, aquifer, groundwater, hydrograph, and related time-series candidates;
- regulatory-context candidates such as NFHL-derived records;
- terrain, topology, NHDPlus HR, WBD/HUC, and other admitted context candidates;
- source role, support class, knowledge character, time basis, unit, QA, geometry, CRS, datum, and method refs;
- quarantine records for role collapse, time ambiguity, unit ambiguity, geometry ambiguity, source-vintage gaps, missing QA, evidence gaps, schema drift, or validation failure;
- validation, processed-state, catalog, triplet, EvidenceBundle, release-review, correction, and rollback handoff packages.

This directory implements or will implement the **how** of Hydrology normalization. It does not fetch source data, define Hydrology object meaning, define schemas, encode policy, store lifecycle data, decide release, issue current advisories, or decide regulatory meaning.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable pipeline logic: the **how**. | CONFIRMED root responsibility |
| Why `domains/hydrology/`? | Hydrology is the domain lane used by Hydrology docs and the Hydrology pipeline README. | CONFIRMED documentation pattern; behavior NEEDS VERIFICATION |
| Why `normalize/` here? | This is a narrow executable sublane for canonicalizing Hydrology work candidates after ingest. | PROPOSED / NEEDS VERIFICATION |
| Is this an ingest lane? | No. Source-specific ingest sublanes create work candidates; this lane canonicalizes admitted candidates. | PROPOSED |
| Is this a connector? | No. Source fetching belongs in connectors or accepted source-edge homes. | CONFIRMED separation |
| Where do declarative run specs live? | `pipeline_specs/hydrology/normalize.yaml` or accepted spec home. | PROPOSED / NEEDS VERIFICATION |
| Can this sublane publish? | No. It may emit normalized candidates, quarantine records, validation handoffs, and receipts only through governed workflow. | CONFIRMED doctrine posture |

> [!IMPORTANT]
> Normalize is not source fetch, not ingest, not catalog closure, not release approval, and not public artifact creation. It standardizes admitted Hydrology candidates while preserving evidence, source role, lifecycle state, and policy posture.

[⬆ Back to top](#top)

---

## 3. Normalize anti-collapse rules

Hydrology normalization must preserve source meaning and lifecycle state.

Disallowed collapses:

```text
raw capture -> normalized record without ingest receipt
ingest candidate -> processed record without validation
observed gauge reading -> modeled hydrograph
modeled hydrograph -> observed gauge reading
NFHL regulatory context -> observed inundation
WBD/HUC administrative framework -> observed hydrology
NHDPlus VAA modeled attribute -> measured value
3DEP terrain derivative -> observed water record
provisional value -> approved value
unit conversion -> silent overwrite
generated summary -> evidence
normalize receipt -> release approval
```

Required distinctions:

- source identity, source role, and knowledge character are explicit;
- observed, modeled, regulatory, official-source context, administrative, derived, aggregate, and generated records remain distinct;
- observation time, valid time, source time, retrieval time, processing time, normalization time, catalog time, release time, and correction time remain distinct;
- units, parameter codes, QA flags, qualifier fields, CRS, vertical datum, source vintage, and geometry lineage are preserved or quarantined;
- canonicalized output remains lifecycle-bound and cannot bypass validation, catalog closure, release, correction, or rollback.

[⬆ Back to top](#top)

---

## 4. What belongs here

Files belong here when their primary responsibility is executable Hydrology normalization.

Appropriate contents include:

- fixture-only normalization entrypoints;
- candidate canonicalization helpers;
- source-role and knowledge-character normalizers that preserve, not rewrite, meaning;
- unit, parameter-code, qualifier, QA, and missing-value normalizers;
- time-basis and cadence normalizers;
- geometry, CRS, datum, topology, and source-vintage normalizers;
- canonical ID builders for Hydrology candidates;
- quarantine routing helpers for unresolved role, time, unit, QA, geometry, CRS, datum, evidence, policy, or schema issues;
- normalization receipt builders, if not shared;
- handoff helpers for validation, processed-state promotion review, catalog, and triplet stages;
- thin adapters that read governed lifecycle inputs, not live source endpoints.

A good placement test:

> If the code canonicalizes admitted Hydrology work candidates into schema-ready normalized candidates, quarantine records, validation handoffs, receipts, or downstream handoff packages, it may belong here. If it fetches source data, defines schemas, stores lifecycle data, writes catalog records, approves release, or creates public API/map payloads, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Source fetchers / connectors | `connectors/<source>` or accepted connector home |
| Source-specific ingest code | `pipelines/domains/hydrology/ingest_*` or accepted ingest sublane |
| Source catalog profiles | `docs/sources/catalog/...` |
| Source descriptors / source registry entries | `data/registry/sources/hydrology/` or approved registry home |
| Hydrology architecture and doctrine | `docs/domains/hydrology/...` |
| Object meaning contracts | `contracts/domains/hydrology/` or accepted contract home |
| JSON Schemas | `schemas/contracts/v1/domains/hydrology/` or accepted schema home |
| Policy, rights, sensitivity, release rules | `policy/...` responsibility roots |
| Declarative run specs | `pipeline_specs/hydrology/...` |
| Fixtures | `fixtures/domains/hydrology/normalize/` or accepted fixture home |
| Tests | `tests/pipelines/domains/hydrology/normalize/` or accepted test home |
| Raw, work, quarantine, processed, catalog, triplet, or published outputs | `data/...` lifecycle homes |
| Catalog/triplet builders | `pipelines/domains/hydrology/catalog/`, `pipelines/catalog/`, or accepted graph/catalog adapter home |
| Catalog close / release preflight | `pipelines/domains/hydrology/catalog_close/` or release workflow homes |
| Receipts and proofs | `data/receipts/...`, `data/proofs/...` |
| Release decisions and manifests | `release/...` responsibility roots |
| Public API or map code | `apps/governed-api/`, `apps/explorer-web/`, packages |

[⬆ Back to top](#top)

---

## 6. Normalization scope

| Scope area | Normalization responsibility | Failure behavior |
|---|---|---|
| Source role | Preserve observed, modeled, regulatory, administrative, aggregate, derived, and generated classes. | Quarantine or abstain on collapse. |
| Identity | Build stable candidate IDs from source refs, feature keys, version/vintage, time, and geometry refs. | Quarantine on unstable identity. |
| Time basis | Normalize time fields without mixing observation, valid, source, retrieval, processing, and release times. | Quarantine on ambiguity. |
| Units and parameters | Normalize units, parameter codes, qualifiers, and missing values with method refs. | Quarantine on silent conversion risk. |
| Geometry | Normalize geometry refs, CRS, topology, and source-vintage lineage. | Quarantine on drift or CRS ambiguity. |
| QA and approval state | Preserve QA, qualifier, approval, provisional, stale, and revision states. | Restrict or quarantine if missing. |
| Evidence refs | Carry evidence refs forward; do not invent support. | Abstain if unresolved. |
| Handoff | Prepare records for validation and later catalog/triplet stages. | No direct publication. |

[⬆ Back to top](#top)

---

## 7. Lifecycle contract

Every Hydrology normalize run must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal stance:

1. **Read** approved fixtures, work candidates, quarantine inputs in remediation mode, or prior normalized baselines.
2. **Normalize** into canonicalized Hydrology candidates with source role, knowledge character, identity refs, time basis, units, QA, geometry refs, source vintage, evidence refs, policy refs, and receipt refs.
3. **Quarantine** unresolved source role, unsupported knowledge class, unit ambiguity, time ambiguity, geometry/CRS ambiguity, QA gaps, approval-state collapse, evidence gaps, schema drift, or validation failure.
4. **Emit receipts** with input refs, normalization version, method refs, transform refs, output refs, and outcomes.
5. **Support validation** only by providing schema-ready candidates and auditable receipts.
6. **Never publish directly.**

Normalization is an intermediate lifecycle transformation. It is not processed-state promotion, catalog closure, release approval, or public artifact creation by itself.

[⬆ Back to top](#top)

---

## 8. Required gates

Every Hydrology normalize run must check or explicitly fail closed on:

1. **Input lifecycle gate** — input is fixture, work candidate, quarantine-remediation input, or accepted baseline.
2. **Ingest receipt gate** — source-derived candidates have ingest receipt refs unless explicitly fixture-only.
3. **Source descriptor gate** — source identity, role, cadence/vintage, rights, and policy posture are known.
4. **Source-role gate** — observed, modeled, regulatory, administrative, aggregate, derived, and generated records remain distinct.
5. **Identity gate** — candidate ID strategy is deterministic and preserves source keys, vintage/version, and scope.
6. **Time/cadence gate** — all material time fields and cadence fields remain distinct.
7. **Unit/parameter gate** — units, parameter codes, qualifiers, conversion method, and missing values are explicit.
8. **QA/approval gate** — QA flags, approval status, provisional status, stale status, and revision status are preserved.
9. **Geometry/CRS gate** — geometry refs, CRS, datum, topology, and source vintage are explicit where applicable.
10. **Evidence gate** — claim-bearing downstream candidates can resolve evidence refs or abstain.
11. **Rights gate** — unresolved rights cannot proceed to release handoff.
12. **Schema/contract gate** — normalized candidates match accepted schema and Hydrology semantics.
13. **No-direct-publish gate** — no writes to public UI, public API, catalog store, published layers, or release manifests as a normalization side effect.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended shape:

```text
pipelines/domains/hydrology/normalize/
├── README.md                         # this file
├── NORMALIZE_CONTRACT.md             # PROPOSED: hydrology normalize execution contract
├── run_dry_fixture.py                # PROPOSED synthetic/redacted fixture only
├── normalize_candidate_identity.py   # PROPOSED
├── normalize_source_role.py          # PROPOSED
├── normalize_time_basis.py           # PROPOSED
├── normalize_units_parameters.py     # PROPOSED
├── normalize_qa_approval.py          # PROPOSED
├── normalize_geometry_refs.py        # PROPOSED
├── validate_no_role_collapse.py      # PROPOSED
├── validate_no_time_collapse.py      # PROPOSED
├── validate_no_unit_silent_overwrite.py # PROPOSED
├── route_quarantine.py               # PROPOSED
├── emit_receipt.py                   # PROPOSED only if not shared
└── adapters/                         # PROPOSED thin lifecycle adapters, no source fetching
```

Declarative specs should live outside this directory:

```text
pipeline_specs/hydrology/normalize.yaml # PROPOSED / NEEDS VERIFICATION
```

Generated outputs must not be written beside the normalization code. Use accepted lifecycle homes under `data/work/hydrology/`, `data/quarantine/hydrology/`, `data/processed/hydrology/`, proof homes under `data/proofs/`, receipt homes under `data/receipts/`, and release homes under `release/`.

[⬆ Back to top](#top)

---

## 10. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Fixture input | `fixtures/domains/hydrology/normalize/` or accepted fixture home | Synthetic, generalized, or redacted. |
| Work candidate input | `data/work/hydrology/<run_id>/` | Main normalization input. |
| Quarantine remediation input | `data/quarantine/hydrology/<reason>/<run_id>/` | Remediation mode only. |
| Normalized work candidate | `data/work/hydrology/<run_id>/` or accepted work home | Candidate only. |
| Quarantine output | `data/quarantine/hydrology/<reason>/<run_id>/` | Failed or unresolved material. |
| Processed handoff candidate | `data/processed/hydrology/<dataset_id>/<version>/` | Only after downstream validation and promotion gates. |
| Receipt | `data/receipts/pipeline/hydrology/normalize/<run_id>.yml` or accepted receipt home | Records input refs, methods, transforms, checks, and outputs. |
| Evidence proof | `data/proofs/evidence_bundle/` or accepted proof home | Required for claim-bearing downstream records. |

[⬆ Back to top](#top)

---

## 11. Minimal normalized candidate record

The final schema is not defined here. This example shows the minimum information a Hydrology normalization candidate should preserve.

```yaml
schema_version: kfm.hydrology_normalized_candidate.v1
candidate_id: hydrology_normalized_<object_family>_<source_key>_<run_id>_<hash>
pipeline_id: domains.hydrology.normalize
run_id: run_YYYYMMDDThhmmssZ
status: WORK_CANDIDATE
object_family: <watershed|huc_unit|hydro_feature|reach_identity|gauge_site|groundwater_well|flow_observation|water_level_observation|water_quality_observation|nfhl_context|terrain_support|network_topology|modeled_hydrograph>
source:
  source_id: <source_id>
  source_role: <observed|modeled|regulatory_context|administrative|aggregate|derived|generated_context|synthetic>
  ingest_receipt_ref: data/receipts/pipeline/hydrology/<ingest_lane>/<run_id>.yml
  input_hash: sha256:<hash>
  rights_state: needs_review
identity:
  source_key: null
  normalized_key: null
  source_vintage: null
time:
  source_time: null
  observed_at: null
  valid_start: null
  valid_end: null
  retrieved_at: null
  normalized_at: YYYY-MM-DDThh:mm:ssZ
measure:
  parameter_code: null
  value: null
  unit: null
  qualifiers: []
  qa_flags: []
geometry:
  geometry_ref: null
  crs: null
  datum: null
anti_collapse:
  source_role_rewritten: false
  observed_is_modeled: false
  regulatory_context_is_observed: false
  unit_conversion_silent: false
  generated_summary_is_evidence: false
policy:
  outcome: ABSTAIN
  reason_code: SOURCE_ROLE_TIME_UNIT_GEOMETRY_OR_EVIDENCE_NOT_RESOLVED
evidence:
  evidence_bundle_ref: null
  citation_state: ABSTAIN
outputs:
  candidate_record: data/work/hydrology/run_YYYYMMDDThhmmssZ/normalized_candidate.yml
  receipt: data/receipts/pipeline/hydrology/normalize/run_YYYYMMDDThhmmssZ.yml
rollback:
  required_before_publication: true
```

[⬆ Back to top](#top)

---

## 12. Tests, fixtures, receipts, and proofs

Default execution is **fixture-only, synthetic/generalized/redacted, and no-network** until normalization spec, evidence, policy, and CI coverage are approved.

Recommended tests:

```text
tests/pipelines/domains/hydrology/normalize/
├── test_no_network_dry_run.py              # PROPOSED
├── test_ingest_receipt_required.py         # PROPOSED
├── test_source_role_preserved.py           # PROPOSED
├── test_nfhl_not_observed.py               # PROPOSED
├── test_observed_not_modeled.py            # PROPOSED
├── test_time_fields_not_collapsed.py       # PROPOSED
├── test_units_not_silently_overwritten.py  # PROPOSED
├── test_parameter_codes_preserved.py       # PROPOSED
├── test_qa_approval_state_preserved.py     # PROPOSED
├── test_geometry_crs_datum_preserved.py    # PROPOSED
├── test_evidence_gap_abstains.py           # PROPOSED
├── test_quarantine_on_schema_failure.py    # PROPOSED
├── test_receipt_hashes.py                  # PROPOSED
└── test_no_direct_publish.py               # PROPOSED
```

A dry run should prove fixtures load without network access, ingest receipts are required for non-fixture inputs, source roles are preserved, time/unit/geometry/QA checks run, EvidenceBundle gaps produce abstention, receipts are deterministic, and no run writes directly to public UI, public API, catalog store, published layers, or release manifests.

[⬆ Back to top](#top)

---

## 13. Promotion, publication, correction, and rollback

Hydrology normalization may prepare canonicalized candidates and quarantine records. It does not publish.

Required chain:

```text
ingested Hydrology work candidate
  -> normalized candidate
  -> validation report
  -> policy decision
  -> EvidenceBundle closure
  -> processed Hydrology record
  -> catalog / triplet candidate
  -> release candidate
  -> ReleaseManifest
  -> RollbackCard
  -> released artifact
```

Correction and rollback posture:

- denied, abstained, errored, restricted, stale, conflicted, and quarantined normalization runs remain auditable;
- normalization receipts preserve input hashes, ingest refs, method refs, rule ids, transforms, and outcomes;
- processed versions are produced by governed promotion, not hidden overwrite;
- downstream artifacts are invalidated if source refs, ingest refs, normalized IDs, time refs, unit refs, geometry refs, evidence refs, source-role refs, or policy refs drift;
- release rollback is owned by `release/`, not by this directory.

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- fills the blank `pipelines/domains/hydrology/normalize/README.md` file;
- identifies this directory as a nested executable Hydrology normalization sublane;
- prevents connector, source-profile, ingest, schema, contract, policy, fixture, test, data, proof, catalog, and release authority from being placed here;
- preserves source role, knowledge character, identity, source vintage, time basis, units, QA, geometry/CRS/datum, evidence, policy, lifecycle, catalog/triplet, release, correction, and rollback boundaries;
- blocks normalization-as-publication, observed-as-modeled, regulatory-context-as-observed, unit silent overwrite, generated-summary-as-evidence, and direct catalog/release writes;
- gives maintainers a fixture-first, fail-closed expansion pattern.

Future executable work in this sublane is done only when it has fixture coverage, schema-backed candidates, contract conformance, source-role/time/unit/QA/geometry/evidence/policy/no-direct-publish tests, deterministic receipts, CI coverage, steward-review handoff, and release/correction/rollback documentation.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `HYDRO-NORM-001` | Should normalization remain a generic Hydrology sublane or split into observation, geometry, regulatory-context, terrain, and topology normalizers? | NEEDS VERIFICATION / ADR |
| `HYDRO-NORM-002` | Which schema owns normalized Hydrology candidates and quarantine reasons? | NEEDS VERIFICATION |
| `HYDRO-NORM-003` | Which first-wave source families should normalize first: WBD/HUC, USGS Water, NHDPlus HR, NFHL, or 3DEP terrain? | NEEDS VERIFICATION |
| `HYDRO-NORM-004` | Which CI job owns Hydrology normalization invariant tests? | UNKNOWN |
| `HYDRO-NORM-005` | Should normalized output remain under `data/work/` until validation, or can it be staged under a separate normalized work subdirectory? | NEEDS VERIFICATION |
| `HYDRO-NORM-006` | Which receipt type owns unit conversion, time-basis canonicalization, geometry CRS normalization, and source-role preservation? | PROPOSED / NEEDS ADR |
| `HYDRO-NORM-007` | Should catalog handoff be forbidden as a normalize side effect, or allowed only through an explicit chained spec? | NEEDS VERIFICATION |

---

## Maintainer note

Start with synthetic/generalized fixture-only dry runs and negative tests. Do not add live source fetching, source-specific ingest logic, direct catalog writes, public layer writes, release-manifest writes, advisory language, or direct API payload generation until source roles, unit/time/geometry normalization, evidence closure, release review, and rollback are proven.
