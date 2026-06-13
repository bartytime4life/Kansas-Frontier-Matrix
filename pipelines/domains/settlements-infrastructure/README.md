<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-settlements-infrastructure-readme
title: Settlements Infrastructure Domain Pipeline README
type: readme
version: v0.1
status: draft
owners:
  - <settlements-infrastructure-pipeline-owner>
  - <settlements-infrastructure-domain-steward>
  - <source-steward>
  - <evidence-steward>
  - <policy-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: pipelines/domains/settlements-infrastructure/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipelines/domains/README.md
  - pipelines/domains/settlement/README.md
  - docs/domains/settlements-infrastructure/README.md
  - docs/domains/settlements-infrastructure/DATA_LIFECYCLE.md
  - docs/domains/settlements-infrastructure/CANONICAL_PATHS.md
  - contracts/domains/settlements-infrastructure/
  - schemas/contracts/v1/domains/settlements-infrastructure/
  - policy/domains/settlements-infrastructure/
  - pipeline_specs/settlements-infrastructure/
  - data/raw/settlements-infrastructure/
  - data/work/settlements-infrastructure/
  - data/quarantine/settlements-infrastructure/
  - data/processed/settlements-infrastructure/
  - data/catalog/domain/settlements-infrastructure/
  - data/triplets/settlements-infrastructure/
  - data/published/layers/settlements-infrastructure/
  - data/registry/sources/settlements-infrastructure/
  - data/receipts/pipeline/
  - data/proofs/evidence_bundle/
  - release/candidates/settlements-infrastructure/
  - release/manifests/settlements-infrastructure/
tags:
  - kfm
  - pipelines
  - domains
  - settlements-infrastructure
  - settlements
  - infrastructure
  - municipalities
  - census-places
  - townsites
  - facilities
  - service-areas
  - operators
  - dependencies
  - evidence
  - policy
  - governance
notes:
  - "This README replaces the greenfield scaffold for pipelines/domains/settlements-infrastructure."
  - "Settlements/Infrastructure pipeline logic is executable implementation support only; it does not own object meaning, schemas, source descriptors, policy, lifecycle data, catalog truth, legal status, operational status, or release decisions."
  - "The shorter settlement path exists only as an alias/compatibility lane unless an ADR resolves the segment differently."
  - "Restricted or sensitive facility, operator, condition, dependency, private-property, living-person, and cultural context fail closed by default."
  - "Concrete executable behavior, source activation, schedules, CI coverage, schema paths, release wiring, and public API/map behavior remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Settlements / Infrastructure Domain Pipeline

> Executable Settlements / Infrastructure pipeline lane for transforming admitted settlement, municipality, census-place, townsite, facility, network, service-area, operator, condition-observation, and dependency source material into governed candidates, quarantine records, processed records, catalog/triplet handoffs, receipts, and release-review packages.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-settlements%20infrastructure%20pipeline-2e7d32)
![authority](https://img.shields.io/badge/authority-executable%20logic-0a7ea4)
![publication](https://img.shields.io/badge/publication-release%20gated-d62728)
![ci](https://img.shields.io/badge/CI-TODO-lightgrey)

**Status:** Draft  
**Path:** `pipelines/domains/settlements-infrastructure/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Domain lane:** Settlements / Infrastructure  
**Placement posture:** canonical executable lane for the Settlements / Infrastructure bounded context; `pipelines/domains/settlement/` is only an alias/compatibility lane unless ADR resolves otherwise  
**Public posture:** no direct publication; public output requires lifecycle, EvidenceBundle, source-role, rights, sensitivity, policy, catalog/triplet, release, correction, and rollback closure

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Settlement alias posture](#3-settlement-alias-posture)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Pipeline scope](#6-pipeline-scope)
- [7. Source-family posture](#7-source-family-posture)
- [8. Lifecycle contract](#8-lifecycle-contract)
- [9. Required gates](#9-required-gates)
- [10. Directory contract](#10-directory-contract)
- [11. Inputs and outputs](#11-inputs-and-outputs)
- [12. Minimal pipeline candidate record](#12-minimal-pipeline-candidate-record)
- [13. Dry-run, tests, fixtures, receipts, and proofs](#13-dry-run-tests-fixtures-receipts-and-proofs)
- [14. Promotion, publication, correction, and rollback](#14-promotion-publication-correction-and-rollback)
- [15. Definition of done](#15-definition-of-done)
- [16. Open questions](#16-open-questions)

---

## 1. Purpose

`pipelines/domains/settlements-infrastructure/` is the executable pipeline lane for Settlements / Infrastructure-domain transformations.

It supports candidate processing for:

- settlements, municipalities, census places, townsites, and ghost towns;
- forts, missions, reservation communities, and historically sensitive place context;
- infrastructure assets, network nodes, network segments, facilities, service areas, operators, condition observations, and dependencies;
- source-vintage-aware settlement and facility identity candidates;
- public-safe settlement and infrastructure map products after evidence, policy, and release review;
- catalog, graph, Evidence Drawer, Focus Mode, and correction/rollback handoff packages.

This directory implements or will implement the **how** of processing. It does not define object meaning, schemas, policy, source descriptors, legal status, operational status, lifecycle storage, catalog truth, or release approval.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable pipeline logic: the **how**. | CONFIRMED root responsibility |
| Why `domains/settlements-infrastructure/`? | Domain docs identify this segment as the proposed pipeline-logic home for the full bounded context. | CONFIRMED documentation pattern; executable behavior NEEDS VERIFICATION |
| What about `pipelines/domains/settlement/`? | It is an alias/compatibility lane and must not create parallel authority. | CONFIRMED current README posture; ADR still needed |
| Where do declarative specs live? | `pipeline_specs/settlements-infrastructure/` or accepted spec home. | PROPOSED / NEEDS VERIFICATION |
| Where do source fetchers live? | `connectors/<source>`, not here. | CONFIRMED separation |
| Where do schemas live? | `schemas/contracts/v1/domains/settlements-infrastructure/` or accepted schema home. | PROPOSED / NEEDS VERIFICATION |
| Where do contracts live? | `contracts/domains/settlements-infrastructure/` or accepted contract home. | PROPOSED / NEEDS VERIFICATION |
| Where does policy live? | `policy/domains/settlements-infrastructure/` and related sensitivity, rights, and release policy roots as applicable. | PROPOSED / NEEDS VERIFICATION |
| Where do outputs live? | Lifecycle homes under `data/`, not beside pipeline code. | CONFIRMED lifecycle posture |
| Can this lane publish? | No. It may prepare candidates and release handoffs only through governed workflow. | CONFIRMED doctrine posture |

> [!IMPORTANT]
> Pipeline code is subordinate to source descriptors, source roles, rights, EvidenceBundle closure, sensitivity transforms, review state, policy decisions, release manifests, correction notices, and rollback cards. A successful run is not public release.

[⬆ Back to top](#top)

---

## 3. Settlement alias posture

`pipelines/domains/settlement/` exists as a shorter compatibility path. It must remain subordinate to this whole-domain lane unless an ADR says otherwise.

Rules:

- keep whole-domain executable logic here;
- do not create duplicate schemas, contracts, policies, source registries, data lanes, release lanes, or public surfaces under both `settlement` and `settlements-infrastructure`;
- if a narrow settlement-only helper is placed under the alias lane, record alias status in receipts and tests;
- migration requires an ADR, path map, compatibility note, tests, and rollback note;
- a shorter path must not weaken evidence, source-role, sensitivity, or release controls.

[⬆ Back to top](#top)

---

## 4. What belongs here

Files belong here when their primary responsibility is executable Settlements / Infrastructure-domain processing.

Appropriate contents include:

- fixture-only dry-run entrypoints;
- settlement, municipality, census-place, townsite, ghost-town, fort, mission, and community candidate builders;
- infrastructure asset, network node, network segment, facility, service-area, operator, condition-observation, and dependency normalizers;
- settlement identity and temporal-status helpers;
- source-role validators for authority records, observations, administrative records, model/context records, and generated summaries;
- public-safe transform helpers, if not centralized elsewhere;
- quarantine routing helpers for rights, sensitivity, identity, temporal, source-role, or geometry failures;
- catalog/triplet handoff helpers, if not centralized in `pipelines/catalog/`;
- receipt emitters, if not shared;
- thin adapters that read governed lifecycle inputs, not live source systems.

A good placement test:

> If the code transforms Settlements / Infrastructure lifecycle inputs into candidates, processed records, restricted catalog/triplet handoffs, receipts, or review handoffs, it may belong here. If it fetches source data, defines meaning, defines schema, encodes policy, stores lifecycle data, approves release, or makes legal/operational determinations, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Source fetchers / connectors | `connectors/<source>` |
| Source catalog profiles | `docs/sources/catalog/...` |
| Source descriptors / source registry entries | `data/registry/sources/settlements-infrastructure/` or approved registry home |
| Settlements / Infrastructure architecture and doctrine | `docs/domains/settlements-infrastructure/...` |
| Object meaning contracts | `contracts/domains/settlements-infrastructure/...` |
| JSON Schemas | `schemas/contracts/v1/domains/settlements-infrastructure/...` |
| Policy bundles and release rules | `policy/domains/settlements-infrastructure/`, rights, sensitivity, and release policy roots |
| Declarative run specs | `pipeline_specs/settlements-infrastructure/...` |
| Fixtures | `fixtures/domains/settlements-infrastructure/` or accepted fixture home |
| Tests | `tests/pipelines/domains/settlements-infrastructure/` or accepted test home |
| Raw, work, quarantine, processed, catalog, triplet, or published outputs | `data/...` lifecycle homes |
| Receipts and proofs | `data/receipts/...`, `data/proofs/...` |
| Release decisions | `release/candidates/settlements-infrastructure/`, `release/manifests/settlements-infrastructure/`, rollback/correction release homes |
| Public API or map code | `apps/governed-api/`, `apps/explorer-web/`, packages |
| Roads, rail, water, hazards, parcels, archaeology, or living-person truth | Owning domain lanes only |

> [!WARNING]
> The previous scaffold wording allowed docs, contracts, schemas, policies, fixtures, tests, packages, pipelines, registries, or data lifecycle artifacts here. This README narrows the boundary: **only executable pipeline logic belongs here.** The other responsibility roots remain separate authority surfaces.

[⬆ Back to top](#top)

---

## 6. Pipeline scope

| Scope area | Pipeline responsibility | Publication posture |
|---|---|---|
| Settlements | Normalize settlement identity, names, roles, evidence, and time scope. | Candidate until evidence and review close. |
| Municipalities | Normalize municipal authority/source records and temporal status. | Source-bound; not inferred from census or map context alone. |
| Census places | Normalize census geography and source vintage. | Census place is not municipal truth. |
| Townsites / ghost towns | Normalize historical place evidence and uncertainty. | Sensitive or culturally reviewed where needed. |
| Forts / missions / communities | Normalize historical and community context with review state. | Sensitive context fails closed until reviewed. |
| Assets / facilities / service areas | Normalize source-bound candidates and limitations. | Not service guarantee or operational truth. |
| Operators / condition observations / dependencies | Preserve source-bound, time-bound context. | Public output requires review and release. |
| Catalog/triplet handoff | Prepare restricted or public-safe catalog/graph candidates after evidence closure. | Projection does not replace canonical review state. |

[⬆ Back to top](#top)

---

## 7. Source-family posture

Pipeline code may consume only admitted or fixture-bound source material.

Candidate source families may include, subject to source descriptors, rights, and steward review:

- Census TIGER / census place geography;
- GNIS and gazetteers;
- state and local GIS sources;
- municipal and local legal records;
- historical gazetteers and maps;
- operator and provider sources;
- bridge, facility, and local infrastructure sources;
- FEMA / hazards / resilience context;
- roads/rail, hydrology, hazards, people/land, archaeology, agriculture, and spatial foundation context through governed joins;
- local upload or steward-curated material only through source-descriptor, rights, sensitivity, and review gates.

This README does not activate any source. Each source family requires SourceDescriptor coverage, source role, rights posture, sensitivity classification, attribution, fixtures, validation, and review routing before use.

[⬆ Back to top](#top)

---

## 8. Lifecycle contract

Every pipeline must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal pipeline stance:

1. **Read** approved synthetic/generalized/redacted fixtures, immutable raw captures, work candidates, quarantine inputs in remediation mode, or prior processed baselines.
2. **Normalize** into work candidates with source role, rights, temporal scope, spatial/place scope, identity posture, sensitivity posture, evidence references, and public-safe transform posture.
3. **Quarantine** unresolved rights, source-role mismatch, identity ambiguity, temporal ambiguity, restricted detail, cultural sensitivity, private-property joins, geometry risk, schema drift, or validation failure.
4. **Promote to processed** only after validation, policy, evidence, sensitivity/public-safe transform, review, and reviewer gates appropriate to significance.
5. **Prepare catalog/triplet handoffs** only after processed-state and evidence closure, and only with sensitivity-safe payloads.
6. **Publish** only through release decisions, public-safe artifacts, rollback targets, and correction paths.

Promotion is a governed state transition with receipts and review evidence, not a file move.

[⬆ Back to top](#top)

---

## 9. Required gates

Every run must check or explicitly fail closed on:

1. **Source descriptor gate** — every input has stable source identity, role, cadence, rights, and sensitivity posture.
2. **Source-role gate** — authority, observation, administrative, historical, modeled, aggregate, candidate, synthetic, context, and generated records are not silently collapsed.
3. **Identity gate** — name reuse, relocation, abandonment, incorporation, disincorporation, annexation, boundary changes, and source-vintage differences remain temporally scoped.
4. **Settlement/municipality/census gate** — settlement candidate, municipality, census place, historic townsite, and community context remain distinct.
5. **Sensitivity gate** — restricted facility, operator, condition, dependency, private-property, living-person, and cultural contexts fail closed unless public-safe handling is proven.
6. **Rights gate** — unknown or restrictive license, permission, attribution, privacy, or redistribution terms block public release.
7. **Public-safe transform gate** — public products require approved redaction, aggregation, generalization, delay, restriction, or denial decisions with receipts.
8. **Temporal gate** — source time, event time, valid time, observed time, retrieval time, processing time, catalog time, and release time remain distinct.
9. **Spatial/place gate** — place point, boundary, facility geometry, service area, network node/segment, and public-safe spatial transforms remain distinct.
10. **Cross-lane ownership gate** — roads/rail, hydrology, hazards, archaeology, people/land, and other domains keep their own truth and sensitivity rules.
11. **Schema, contract, evidence, policy, validation, receipt, catalog/triplet, and release gates** — all must close or the run abstains, denies, or quarantines.
12. **No-direct-publish gate** — no writes to public UI, public API, or `data/published/` without release workflow authority.

[⬆ Back to top](#top)

---

## 10. Directory contract

Recommended shape:

```text
pipelines/domains/settlements-infrastructure/
├── README.md                         # this file
├── PIPELINE_CONTRACT.md              # PROPOSED: execution contract
├── run_dry_fixture.py                # PROPOSED synthetic/generalized/redacted fixtures only
├── normalize_settlement.py           # PROPOSED
├── normalize_municipality.py         # PROPOSED
├── normalize_census_place.py         # PROPOSED
├── normalize_townsite.py             # PROPOSED
├── normalize_facility.py             # PROPOSED
├── normalize_service_area.py         # PROPOSED
├── normalize_operator.py             # PROPOSED
├── normalize_condition_observation.py # PROPOSED
├── normalize_dependency.py           # PROPOSED
├── validate_source_role_anticollapse.py # PROPOSED
├── apply_public_safe_transform.py    # PROPOSED; may belong in shared tools if reused
├── build_catalog_handoff.py          # PROPOSED if not centralized in pipelines/catalog/
├── validate_settlements_infrastructure_candidate.py # PROPOSED wrapper if not centralized in tools/
├── emit_receipt.py                   # PROPOSED only if not shared
└── adapters/                         # PROPOSED thin lifecycle adapters, no source fetching
```

Declarative specs should live outside this directory:

```text
pipeline_specs/settlements-infrastructure/
├── README.md                         # PROPOSED / NEEDS VERIFICATION
├── settlement_dry_run.yaml           # PROPOSED
├── infrastructure_asset_dry_run.yaml # PROPOSED
├── source_role_anticollapse.yaml     # PROPOSED
├── public_safe_transform.yaml        # PROPOSED
└── catalog_handoff.yaml              # PROPOSED
```

Generated outputs must not be written beside the code that generated them. Use accepted lifecycle homes under `data/`, proof homes under `data/proofs/`, receipt homes under `data/receipts/`, and release homes under `release/`.

[⬆ Back to top](#top)

---

## 11. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Fixture input | `fixtures/domains/settlements-infrastructure/` or accepted fixture home | Synthetic, generalized, or redacted where needed. |
| Raw capture | `data/raw/settlements-infrastructure/<source_id>/<run_id>/` | Immutable source-edge capture with source descriptor and receipt. |
| Work candidate | `data/work/settlements-infrastructure/<run_id>/` | Candidate only. |
| Quarantine record | `data/quarantine/settlements-infrastructure/<reason>/<run_id>/` | Failed, restricted, unresolved, or unsafe material. |
| Processed dataset | `data/processed/settlements-infrastructure/<dataset_id>/<version>/` | Validated/restricted; not automatically public. |
| Catalog candidate | `data/catalog/domain/settlements-infrastructure/...` or approved catalog home | After processed-state, transform, and evidence gates. |
| Triplet / graph delta | `data/triplets/settlements-infrastructure/...` or approved graph-delta home | Projection only. |
| Receipts / proofs | `data/receipts/...`, `data/proofs/...` | Required for auditable promotion and release review. |
| Release handoff | `release/candidates/settlements-infrastructure/...` | Only through release workflow. |

[⬆ Back to top](#top)

---

## 12. Minimal pipeline candidate record

The final schema is not defined here. This example shows the minimum information a pipeline candidate should preserve.

```yaml
schema_version: kfm.settlements_infrastructure_pipeline_candidate.v1
candidate_id: si_<object_family>_<run_id>_<hash>
pipeline_id: domains.settlements-infrastructure
run_id: run_YYYYMMDDThhmmssZ
status: WORK_CANDIDATE
object_family: <settlement|municipality|census_place|townsite|ghost_town|fort|mission|community|infrastructure_asset|network_node|network_segment|facility|service_area|operator|condition_observation|dependency>
source_inputs:
  - source_id: src_settlements_infrastructure_example
    source_role: <authority|observation|administrative|historical|modeled|aggregate|candidate|synthetic|context|restricted>
    lifecycle_ref: data/raw/settlements-infrastructure/<source_id>/<run_id>/
    input_hash: sha256:<hash>
    rights_state: needs_review
anti_collapse:
  settlement_candidate_is_municipal_authority: false
  census_place_is_municipality: false
  condition_observation_is_current_operational_status: false
  service_area_is_service_guarantee: false
  generated_summary_is_evidence: false
sensitivity:
  restricted_detail_risk: needs_review
  public_release_default: DENY_UNTIL_REVIEW
policy:
  outcome: ABSTAIN
  reason_code: RIGHTS_SENSITIVITY_OR_EVIDENCE_NOT_RESOLVED
evidence:
  evidence_bundle_ref: null
  citation_state: ABSTAIN
outputs:
  candidate_record: data/work/settlements-infrastructure/run_YYYYMMDDThhmmssZ/candidate.yml
  receipt: data/receipts/pipeline/settlements-infrastructure/run_YYYYMMDDThhmmssZ.yml
rollback:
  required_before_publication: true
```

[⬆ Back to top](#top)

---

## 13. Dry-run, tests, fixtures, receipts, and proofs

Default execution is **fixture-only, synthetic/generalized/redacted, and no-network** until source activation, rights review, sensitivity review, source-role review, and CI coverage are approved.

Recommended tests:

```text
tests/pipelines/domains/settlements-infrastructure/
├── test_no_network_dry_run.py                     # PROPOSED
├── test_source_role_required.py                   # PROPOSED
├── test_rights_unknown_denied.py                  # PROPOSED
├── test_census_place_not_municipality.py          # PROPOSED
├── test_settlement_candidate_not_authority.py     # PROPOSED
├── test_condition_not_current_status.py           # PROPOSED
├── test_service_area_not_service_guarantee.py     # PROPOSED
├── test_restricted_detail_denied.py               # PROPOSED
├── test_settlement_alias_no_parallel_authority.py # PROPOSED
├── test_missing_evidence_abstains.py              # PROPOSED
├── test_receipt_hashes.py                         # PROPOSED
└── test_no_direct_publish.py                      # PROPOSED
```

A dry run should prove fixtures load without network access, source roles are present, ambiguous or restricted material is denied or quarantined, EvidenceBundle gaps produce abstention, receipts are deterministic, and no run writes directly to public UI, public API, `data/published/`, or release manifests.

[⬆ Back to top](#top)

---

## 14. Promotion, publication, correction, and rollback

Pipelines may prepare candidates. They do not publish.

Required promotion chain:

```text
settlements / infrastructure source or work input
  -> candidate
  -> validation report
  -> policy decision
  -> public-safe transform receipt where required
  -> EvidenceBundle closure
  -> processed restricted dataset version
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
- alias-path migration must preserve receipts, evidence, review state, and rollback targets;
- public artifact rollback is owned by `release/`, not by this directory;
- correction notices must point back to source, evidence, public-safe transforms, validation, catalog, release, and rollback state.

[⬆ Back to top](#top)

---

## 15. Definition of done

This README is done when it:

- replaces the greenfield scaffold with a usable Settlements / Infrastructure pipeline contract;
- identifies this directory as executable pipeline logic only;
- marks `settlement` as an alias/compatibility path, not a parallel authority root;
- corrects the boundary so docs, schemas, contracts, policy, fixtures, tests, data, registries, receipts, proofs, and release decisions do not live here;
- preserves source-role, identity, sensitivity, evidence, policy, lifecycle, catalog/triplet, release, correction, and rollback boundaries;
- blocks direct publication and restricted detail exposure;
- gives maintainers a fixture-first, fail-closed expansion pattern.

Future executable work in this lane is done only when it has source-descriptor coverage, synthetic/generalized/redacted no-network fixtures, schema-backed candidates, contract conformance, rights/sensitivity/source-role/evidence tests, deterministic receipts, no-parallel-authority tests, no-direct-publish tests, CI coverage, steward-review handoff, and release/correction/rollback documentation.

[⬆ Back to top](#top)

---

## 16. Open questions

| ID | Question | Status |
|---|---|---|
| `SI-PIPE-001` | Which child modules should be implemented first: settlements, municipalities, facilities, service areas, operators, condition observations, dependencies, or catalog handoff? | NEEDS VERIFICATION |
| `SI-PIPE-002` | Should `pipelines/domains/settlement/` remain as compatibility alias, become a Settlement-only sublane, or be removed after ADR resolution? | NEEDS VERIFICATION / ADR |
| `SI-PIPE-003` | Which source descriptors are first-wave approved for fixture-only dry runs? | NEEDS VERIFICATION |
| `SI-PIPE-004` | Which CI job owns Settlements / Infrastructure pipeline invariant tests? | UNKNOWN |
| `SI-PIPE-005` | Should catalog handoff logic live here or in centralized `pipelines/catalog/` with Settlements / Infrastructure adapters? | NEEDS VERIFICATION |
| `SI-PIPE-006` | Which public-safe map/API products are allowed after review and release, and at what redaction/generalization level? | NEEDS VERIFICATION |
| `SI-PIPE-007` | How should cross-lane joins with Roads/Rail, Hydrology, Hazards, People/Land, Archaeology, Agriculture, or Spatial Foundation be denied, restricted, or generalized? | NEEDS VERIFICATION |

---

## Maintainer note

Start with synthetic/generalized/redacted fixture-only dry runs and negative tests. Do not add live source fetching, restricted detail examples, private-property joins, public operational-condition claims, public map layers, release handoff automation, or direct API payload generation until source roles, rights, sensitivity review, public-safe transforms, evidence closure, alias-path governance, and rollback are proven.
