<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-hydrology-ingest-readme
title: Hydrology Ingest Pipeline README
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
path: pipelines/domains/hydrology/ingest/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipelines/domains/README.md
  - pipelines/domains/hydrology/README.md
  - docs/domains/hydrology/README.md
  - docs/domains/hydrology/PUBLICATION_POSTURE.md
  - docs/domains/hydrology/DATA_LIFECYCLE.md
  - pipeline_specs/hydrology/ingest.yaml
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
  - ingest
  - source-role
  - gauge
  - water-quality
  - groundwater
  - watershed
  - huc
  - nfhl
  - regulatory-context
  - evidence-bundle
  - public-safe
  - evidence
  - policy
  - governance
notes:
  - "This README fills the blank pipelines/domains/hydrology/ingest path as a nested executable Hydrology ingest sublane."
  - "Hydrology ingest logic is executable implementation support only; it does not own source descriptors, connectors, schemas, policy, lifecycle data, catalog truth, official forecasts, regulatory determinations, or release decisions."
  - "This sublane reads admitted lifecycle inputs or fixtures. Source fetching remains in connectors or accepted source-edge homes."
  - "Observed gauge readings, water-quality observations, groundwater observations, modeled outputs, regulatory context, official-source context, and generated summaries must remain separate truth classes."
  - "NFHL is regulatory context only and must never ingest as observed inundation."
  - "Concrete executable behavior, source linkage, schedules, CI coverage, schema paths, release wiring, and public API/map behavior remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hydrology Ingest Pipeline

> Executable Hydrology sublane for normalizing admitted hydrology source captures and fixture inputs into governed work candidates, quarantine records, validation handoffs, receipts, and later processed-state inputs — without collapsing observed, modeled, regulatory, official-source, derived, or generated truth classes.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-hydrology%20ingest-2e7d32)
![authority](https://img.shields.io/badge/authority-executable%20logic-0a7ea4)
![anti-collapse](https://img.shields.io/badge/NFHL%20%E2%89%A0%20observed%20flooding-d62728)
![publication](https://img.shields.io/badge/publication-release%20gated-d62728)
![ci](https://img.shields.io/badge/CI-TODO-lightgrey)

**Status:** Draft  
**Path:** `pipelines/domains/hydrology/ingest/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Domain lane:** Hydrology  
**Sublane:** Ingest / normalization  
**Placement posture:** nested executable sublane under `pipelines/domains/hydrology/`; concrete executable behavior remains `PROPOSED / NEEDS VERIFICATION` unless backed by tests and repo evidence  
**Public posture:** no direct publication; ingest output is work/quarantine/validation input only and requires downstream evidence, policy, catalog, release, correction, and rollback closure

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Ingest anti-collapse rules](#3-ingest-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Ingest scope](#6-ingest-scope)
- [7. Lifecycle contract](#7-lifecycle-contract)
- [8. Required gates](#8-required-gates)
- [9. Directory contract](#9-directory-contract)
- [10. Inputs and outputs](#10-inputs-and-outputs)
- [11. Minimal ingest candidate record](#11-minimal-ingest-candidate-record)
- [12. Tests, fixtures, receipts, and proofs](#12-tests-fixtures-receipts-and-proofs)
- [13. Promotion, publication, correction, and rollback](#13-promotion-publication-correction-and-rollback)
- [14. Definition of done](#14-definition-of-done)
- [15. Open questions](#15-open-questions)

---

## 1. Purpose

`pipelines/domains/hydrology/ingest/` is the executable sublane for Hydrology source-ingest normalization after source material has been admitted into the KFM lifecycle.

It supports candidate processing for:

- watershed and HUC source captures;
- stream, river, reach, and waterbody identity records;
- gauge, well, and observation-site metadata;
- flow, stage, water-level, water-quality, aquifer, groundwater, and hydrograph observation candidates;
- NFHL and other regulatory-context records with explicit source-role separation;
- terrain, topology, and upstream/downstream trace inputs where admitted;
- modeled or reconstructed hydrograph candidates only when method/model receipt references are present;
- quarantine records for missing source descriptor, source-role collapse, time ambiguity, geometry ambiguity, rights uncertainty, schema drift, or validation failure;
- validation, catalog, triplet, EvidenceBundle, release-review, correction, and rollback handoff packages.

This directory implements or will implement the **how** of Hydrology ingest normalization. It does not fetch source data, define Hydrology object meaning, define schemas, encode policy, store lifecycle data, decide release, issue current safety guidance, or decide regulatory meaning.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable pipeline logic: the **how**. | CONFIRMED root responsibility |
| Why `domains/hydrology/`? | Hydrology is the domain lane used by Hydrology docs and the Hydrology pipeline README. | CONFIRMED documentation pattern; behavior NEEDS VERIFICATION |
| Why `ingest/` here? | This is a narrow executable sublane for Hydrology lifecycle-input normalization. | PROPOSED / NEEDS VERIFICATION |
| Is this a connector? | No. Source fetching belongs in `connectors/<source>` or accepted source-edge homes. This sublane reads admitted lifecycle inputs or fixtures. | CONFIRMED separation |
| Where do raw captures live? | `data/raw/hydrology/<source_id>/<run_id>/` or accepted raw home. | CONFIRMED lifecycle posture; implementation NEEDS VERIFICATION |
| Where do declarative run specs live? | `pipeline_specs/hydrology/ingest.yaml` or accepted spec home. | PROPOSED / NEEDS VERIFICATION |
| Can this sublane publish? | No. It may emit work candidates, quarantine records, validation handoffs, and receipts only through governed workflow. | CONFIRMED doctrine posture |

> [!IMPORTANT]
> Ingest is not publication, not catalog closure, not regulatory determination, and not current safety guidance. Ingest prepares evidence-bound candidates for downstream validation and review.

[⬆ Back to top](#top)

---

## 3. Ingest anti-collapse rules

Hydrology ingest must preserve source-role and knowledge-character separation.

Disallowed collapses:

```text
raw source capture -> processed record without validation
observed gauge reading -> modeled hydrograph
modeled hydrograph -> observed gauge reading
NFHL regulatory context -> observed inundation
official-source context -> KFM-issued current guidance
water-quality observation -> general water-status claim
terrain/topology derivative -> source observation
generated summary -> evidence
ingest receipt -> release approval
```

Required distinctions:

- source identity and source role are explicit;
- observation site, observed variable, unit, time basis, and QA state are explicit where applicable;
- observed, modeled, regulatory, official-source, derived, and generated records remain distinct;
- observation time, valid time, retrieval time, processing time, catalog time, release time, and correction time remain distinct;
- NFHL and similar records stay regulatory context;
- model/reconstruction outputs carry method receipt references;
- outputs without EvidenceBundle-ready support abstain or quarantine rather than becoming authoritative claims.

[⬆ Back to top](#top)

---

## 4. What belongs here

Files belong here when their primary responsibility is executable Hydrology ingest normalization.

Appropriate contents include:

- fixture-only ingest entrypoints;
- source-capture-to-work-candidate normalizers;
- watershed and HUC normalizers;
- stream/reach/waterbody identity normalizers;
- gauge, well, and observation-site metadata normalizers;
- flow, stage, water-level, water-quality, aquifer, groundwater, and hydrograph observation normalizers;
- NFHL/regulatory-context anti-collapse validators;
- source-role, time/freshness, unit, QA, geometry, topology, and method-receipt validators;
- quarantine routing helpers for rights, source-role, temporal, geometry, unit, evidence, or schema failures;
- receipt emitters, if not shared;
- handoff helpers for validation, catalog, and triplet stages;
- thin adapters that read governed lifecycle inputs, not live source endpoints.

A good placement test:

> If the code transforms admitted Hydrology lifecycle inputs into work candidates, quarantine records, validation handoffs, receipts, or downstream handoff packages, it may belong here. If it fetches source data, defines schemas, encodes policy, stores lifecycle data, writes catalog records, or approves release, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Source fetchers / connectors | `connectors/<source>` |
| Source catalog profiles | `docs/sources/catalog/...` |
| Source descriptors / source registry entries | `data/registry/sources/hydrology/` or approved registry home |
| Hydrology architecture and doctrine | `docs/domains/hydrology/...` |
| Object meaning contracts | `contracts/domains/hydrology/` or accepted contract home |
| JSON Schemas | `schemas/contracts/v1/domains/hydrology/` or accepted schema home |
| Policy, rights, sensitivity, release rules | `policy/...` responsibility roots |
| Declarative run specs | `pipeline_specs/hydrology/...` |
| Fixtures | `fixtures/domains/hydrology/ingest/` or accepted fixture home |
| Tests | `tests/pipelines/domains/hydrology/ingest/` or accepted test home |
| Raw, work, quarantine, processed, catalog, triplet, or published outputs | `data/...` lifecycle homes |
| Catalog/triplet builders | `pipelines/domains/hydrology/catalog/`, `pipelines/catalog/`, or accepted graph/catalog adapter home |
| Catalog close / release preflight | `pipelines/domains/hydrology/catalog_close/` or release workflow homes |
| Receipts and proofs | `data/receipts/...`, `data/proofs/...` |
| Release decisions and manifests | `release/...` responsibility roots |
| Public API or map code | `apps/governed-api/`, `apps/explorer-web/`, packages |

[⬆ Back to top](#top)

---

## 6. Ingest scope

| Scope area | Ingest responsibility | Failure behavior |
|---|---|---|
| Source identity | Preserve source id, source role, rights, and retrieval refs. | Quarantine if missing. |
| Watersheds / HUCs | Normalize identity, geometry refs, version, and source vintage. | Quarantine on geometry/version ambiguity. |
| Streams / reaches | Normalize hydrographic identity and topology references. | Quarantine on identity/topology ambiguity. |
| Gauges / wells | Normalize site metadata and observation family. | Quarantine on missing site identity. |
| Time-series observations | Normalize variable, unit, cadence, QA, observed time, valid time, and retrieval time. | Quarantine or restrict on collapse. |
| NFHL context | Preserve regulatory-context role. | Deny or quarantine if treated as observed event. |
| Modeled hydrographs | Preserve method/model receipt refs. | Abstain or quarantine if method support missing. |
| Cross-lane context | Preserve owning domain and source-role boundaries. | Restrict or quarantine if ownership collapses. |

[⬆ Back to top](#top)

---

## 7. Lifecycle contract

Every Hydrology ingest run must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal stance:

1. **Read** approved fixtures, immutable raw captures, work inputs, quarantine inputs in remediation mode, or prior processed baselines.
2. **Normalize** into Hydrology work candidates with source role, rights, time/freshness state, geometry refs, units, QA, evidence refs, policy refs, and receipt refs.
3. **Quarantine** missing source descriptor, unsupported source role, NFHL/observed collapse, modeled/observed collapse, unit ambiguity, time ambiguity, geometry ambiguity, rights failure, schema drift, or validation failure.
4. **Emit receipts** with input refs, source refs, method refs, validation refs, output refs, and outcomes.
5. **Support promotion** only by feeding downstream validation and review workflows.
6. **Never publish directly.**

Ingest is an early lifecycle transformation. It is not processed-state promotion by itself.

[⬆ Back to top](#top)

---

## 8. Required gates

Every Hydrology ingest run must check or explicitly fail closed on:

1. **Input lifecycle gate** — input is fixture, raw capture, work input, quarantine-remediation input, or accepted baseline.
2. **Source descriptor gate** — source identity, role, cadence/freshness, rights, and sensitivity posture are known.
3. **Source-role gate** — observed, modeled, regulatory, official-source context, derived, and generated records remain distinct.
4. **NFHL gate** — NFHL and similar records remain regulatory context, not observed inundation.
5. **Observation gate** — variable, unit, observation site, QA, cadence, observed time, and valid time are explicit where applicable.
6. **Model receipt gate** — model or reconstruction products carry method/model receipt refs.
7. **Geometry/topology gate** — geometry refs, CRS, topology, and source vintage are explicit where applicable.
8. **Time/freshness gate** — source time, observed time, valid time, retrieval time, processing time, and stale-state are distinct.
9. **Evidence gate** — claim-bearing downstream candidates can resolve evidence refs or abstain.
10. **Rights and sensitivity gate** — unresolved rights or restricted context cannot proceed to public-safe handoff.
11. **Schema/contract gate** — candidates match accepted schema and Hydrology semantics.
12. **No-direct-publish gate** — no writes to public UI, public API, catalog store, published layers, or release manifests as an ingest side effect.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended shape:

```text
pipelines/domains/hydrology/ingest/
├── README.md                         # this file
├── INGEST_CONTRACT.md                # PROPOSED: hydrology ingest execution contract
├── run_dry_fixture.py                # PROPOSED synthetic/redacted fixture only
├── normalize_source_capture.py       # PROPOSED
├── normalize_watershed_huc.py        # PROPOSED
├── normalize_hydro_feature.py        # PROPOSED
├── normalize_observation_site.py     # PROPOSED
├── normalize_time_series.py          # PROPOSED
├── normalize_nfhl_context.py         # PROPOSED
├── normalize_model_output.py         # PROPOSED
├── validate_source_role.py           # PROPOSED
├── validate_time_freshness.py        # PROPOSED
├── validate_geometry_topology.py     # PROPOSED
├── route_quarantine.py               # PROPOSED
├── emit_receipt.py                   # PROPOSED only if not shared
└── adapters/                         # PROPOSED thin lifecycle adapters, no source fetching
```

Declarative specs should live outside this directory:

```text
pipeline_specs/hydrology/ingest.yaml # PROPOSED / NEEDS VERIFICATION
```

Generated outputs must not be written beside the ingest code. Use accepted lifecycle homes under `data/work/hydrology/`, `data/quarantine/hydrology/`, `data/processed/hydrology/`, proof homes under `data/proofs/`, receipt homes under `data/receipts/`, and release homes under `release/`.

[⬆ Back to top](#top)

---

## 10. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Fixture input | `fixtures/domains/hydrology/ingest/` or accepted fixture home | Synthetic, generalized, or redacted. |
| Raw capture | `data/raw/hydrology/<source_id>/<run_id>/` | Immutable source-edge capture with descriptor and receipt. |
| Work candidate | `data/work/hydrology/<run_id>/` | Candidate only. |
| Quarantine record | `data/quarantine/hydrology/<reason>/<run_id>/` | Failed, restricted, unresolved, or unsafe material. |
| Processed input handoff | `data/processed/hydrology/<dataset_id>/<version>/` | Only after downstream validation and promotion gates. |
| Receipt | `data/receipts/pipeline/hydrology/ingest/<run_id>.yml` or accepted receipt home | Records input refs, methods, checks, and outputs. |
| Evidence proof | `data/proofs/evidence_bundle/` or accepted proof home | Required for claim-bearing downstream records. |
| Catalog handoff | `pipelines/domains/hydrology/catalog/` via lifecycle data homes | No direct catalog writes from ingest unless approved by spec. |

[⬆ Back to top](#top)

---

## 11. Minimal ingest candidate record

The final schema is not defined here. This example shows the minimum information a Hydrology ingest candidate should preserve.

```yaml
schema_version: kfm.hydrology_ingest_candidate.v1
candidate_id: hydrology_ingest_<object_family>_<run_id>_<hash>
pipeline_id: domains.hydrology.ingest
run_id: run_YYYYMMDDThhmmssZ
status: WORK_CANDIDATE
object_family: <watershed|huc_unit|hydro_feature|reach_identity|gauge_site|groundwater_well|flow_observation|water_level_observation|water_quality_observation|aquifer_observation|nfhl_context|modeled_hydrograph>
source:
  source_id: <source_id>
  source_role: <observed|modeled|regulatory_context|official_source_context|derived|generated_context|synthetic>
  lifecycle_ref: data/raw/hydrology/<source_id>/<run_id>/
  input_hash: sha256:<hash>
  rights_state: needs_review
time:
  source_time: null
  observed_at: null
  valid_start: null
  valid_end: null
  retrieved_at: YYYY-MM-DDThh:mm:ssZ
  processed_at: YYYY-MM-DDThh:mm:ssZ
geometry:
  geometry_ref: null
  crs: null
  topology_ref: null
anti_collapse:
  nfhl_is_observed_flooding: false
  modeled_hydrograph_is_observation: false
  official_context_is_kfm_guidance: false
  generated_summary_is_evidence: false
policy:
  outcome: ABSTAIN
  reason_code: SOURCE_DESCRIPTOR_EVIDENCE_OR_POLICY_NOT_RESOLVED
evidence:
  evidence_bundle_ref: null
  citation_state: ABSTAIN
outputs:
  candidate_record: data/work/hydrology/run_YYYYMMDDThhmmssZ/ingest_candidate.yml
  receipt: data/receipts/pipeline/hydrology/ingest/run_YYYYMMDDThhmmssZ.yml
rollback:
  required_before_publication: true
```

[⬆ Back to top](#top)

---

## 12. Tests, fixtures, receipts, and proofs

Default execution is **fixture-only, synthetic/generalized/redacted, and no-network** until source activation, ingest spec, evidence, policy, sensitivity, and CI coverage are approved.

Recommended tests:

```text
tests/pipelines/domains/hydrology/ingest/
├── test_no_network_dry_run.py             # PROPOSED
├── test_source_descriptor_required.py     # PROPOSED
├── test_source_role_required.py           # PROPOSED
├── test_nfhl_not_observed_flooding.py     # PROPOSED
├── test_modeled_not_observed.py           # PROPOSED
├── test_observation_time_units_required.py # PROPOSED
├── test_geometry_topology_refs.py         # PROPOSED
├── test_evidence_gap_abstains.py          # PROPOSED
├── test_quarantine_on_schema_failure.py   # PROPOSED
├── test_receipt_hashes.py                 # PROPOSED
└── test_no_direct_publish.py              # PROPOSED
```

A dry run should prove fixtures load without network access, source descriptors and source roles are required, NFHL stays regulatory context, observations and model products remain distinct, time/unit/geometry checks run, EvidenceBundle gaps produce abstention, receipts are deterministic, and no run writes directly to public UI, public API, catalog store, published layers, or release manifests.

[⬆ Back to top](#top)

---

## 13. Promotion, publication, correction, and rollback

Hydrology ingest may prepare work candidates and quarantine records. It does not publish.

Required chain:

```text
admitted Hydrology source capture
  -> ingest candidate
  -> validation report
  -> policy decision
  -> EvidenceBundle closure
  -> processed Hydrology record
  -> catalog / triplet candidate
  -> release candidate
  -> ReleaseManifest
  -> RollbackCard
  -> public-safe artifact
```

Correction and rollback posture:

- denied, abstained, errored, restricted, stale, conflicted, and quarantined ingest runs remain auditable;
- ingest receipts preserve input hashes, source refs, method refs, rule ids, and outcomes;
- processed versions are produced by governed promotion, not hidden overwrite;
- downstream artifacts are invalidated if source refs, method refs, evidence refs, source-role refs, or policy refs drift;
- public artifact rollback is owned by `release/`, not by this directory.

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- fills the blank `pipelines/domains/hydrology/ingest/README.md` file;
- identifies this directory as a nested executable Hydrology ingest sublane;
- prevents connector, source-profile, schema, contract, policy, fixture, test, data, proof, catalog, and release authority from being placed here;
- preserves source role, observed/modeled/regulatory separation, NFHL context, time/freshness, units, QA, geometry/topology, evidence, policy, lifecycle, catalog/triplet, release, correction, and rollback boundaries;
- blocks ingest-as-publication, NFHL-as-observed, model-as-observation, generated-summary-as-evidence, and direct catalog/release writes;
- gives maintainers a fixture-first, fail-closed expansion pattern.

Future executable work in this sublane is done only when it has source-descriptor coverage, synthetic/generalized/redacted no-network fixtures, schema-backed candidates, contract conformance, source-role/NFHL/evidence/policy/no-direct-publish tests, deterministic receipts, CI coverage, steward-review handoff, and release/correction/rollback documentation.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `HYDRO-INGEST-001` | Should Hydrology ingest stay as a generic sublane, or split into source-specific sublanes such as USGS Water, WBD, NHD, NWIS, NFHL, and water-quality ingest? | NEEDS VERIFICATION / ADR |
| `HYDRO-INGEST-002` | Which connector or source-edge jobs own retrieval before this sublane reads lifecycle inputs? | NEEDS VERIFICATION |
| `HYDRO-INGEST-003` | Which first-wave object families are approved for fixture-only dry runs: HUCs, reaches, gauges, observations, NFHL context, or modeled outputs? | NEEDS VERIFICATION |
| `HYDRO-INGEST-004` | Which schema owns ingest candidates and quarantine reasons? | NEEDS VERIFICATION |
| `HYDRO-INGEST-005` | Which CI job owns Hydrology ingest invariant tests? | UNKNOWN |
| `HYDRO-INGEST-006` | Should catalog handoff be forbidden as an ingest side effect, or allowed only through an explicit chained spec? | NEEDS VERIFICATION |
| `HYDRO-INGEST-007` | Which receipt type owns model/method support for reconstructed hydrographs before ingest-to-validation handoff? | PROPOSED / NEEDS ADR |

---

## Maintainer note

Start with synthetic/generalized fixture-only dry runs and negative tests. Do not add live source fetching, direct catalog writes, public map layer writes, release-manifest writes, current safety guidance, or direct API payload generation until source roles, evidence closure, public-safe transforms, catalog profiles, release review, and rollback are proven.
