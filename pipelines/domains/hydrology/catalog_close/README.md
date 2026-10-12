<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-hydrology-catalog-close-readme
title: Hydrology Catalog Close Pipeline README
type: readme
version: v0.1
status: draft
owners:
  - <hydrology-pipeline-owner>
  - <hydrology-domain-steward>
  - <catalog-steward>
  - <release-steward>
  - <evidence-steward>
  - <policy-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: pipelines/domains/hydrology/catalog_close/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipelines/catalog/README.md
  - pipelines/domains/README.md
  - pipelines/domains/hydrology/README.md
  - pipelines/domains/hydrology/catalog/README.md
  - docs/domains/hydrology/README.md
  - docs/domains/hydrology/PUBLICATION_POSTURE.md
  - docs/domains/hydrology/DATA_LIFECYCLE.md
  - pipeline_specs/hydrology/catalog_close.yaml
  - contracts/domains/hydrology/
  - schemas/contracts/v1/domains/hydrology/
  - policy/domains/hydrology/
  - policy/sensitivity/hydrology/
  - data/processed/hydrology/
  - data/catalog/domain/hydrology/
  - data/triplets/hydrology/
  - data/quarantine/hydrology/
  - data/receipts/pipeline/
  - data/proofs/evidence_bundle/
  - release/candidates/hydrology/
  - release/manifests/hydrology/
  - release/promotion_decisions/hydrology/
tags:
  - kfm
  - pipelines
  - domains
  - hydrology
  - catalog-close
  - closure-gate
  - release-preflight
  - evidence-bundle
  - rollback
  - correction
  - nfhl
  - source-role
  - public-safe
  - evidence
  - policy
  - governance
notes:
  - "This README fills the blank pipelines/domains/hydrology/catalog_close path as a nested executable catalog-closure sublane."
  - "Catalog close is executable preflight/closure support only; it does not own catalog truth, release decisions, source descriptors, schemas, policy, lifecycle data, or public publication."
  - "Closure verifies that a Hydrology catalog/triplet candidate has evidence, source-role, time/freshness, sensitivity, public-safe, correction, and rollback closure before release handoff."
  - "NFHL remains regulatory context only and must not close as observed flooding."
  - "Observed readings, modeled hydrographs, regulatory flood context, official-source context, and generated summaries must remain separate through closure."
  - "Concrete executable behavior, schedules, CI coverage, schema paths, release wiring, and public API/map behavior remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hydrology Catalog Close Pipeline

> Executable Hydrology sublane for closing catalog and graph handoff candidates before release workflow review. It verifies evidence, policy, source-role separation, time/freshness caveats, sensitivity decisions, public-safe transforms, correction paths, and rollback targets without publishing anything or converting catalog projections into canonical truth.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-hydrology%20catalog%20close-2e7d32)
![authority](https://img.shields.io/badge/authority-executable%20preflight-0a7ea4)
![anti-collapse](https://img.shields.io/badge/NFHL%20%E2%89%A0%20observed%20flooding-d62728)
![release](https://img.shields.io/badge/release-preflight%20only-d62728)
![ci](https://img.shields.io/badge/CI-TODO-lightgrey)

**Status:** Draft  
**Path:** `pipelines/domains/hydrology/catalog_close/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Domain lane:** Hydrology  
**Sublane:** Catalog close / release preflight  
**Placement posture:** nested executable sublane under `pipelines/domains/hydrology/`; concrete executable behavior remains `PROPOSED / NEEDS VERIFICATION` unless backed by tests and repo evidence  
**Public posture:** no direct publication; closure output is a reviewable handoff to release workflow only

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Closure anti-collapse rules](#3-closure-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Closure scope](#6-closure-scope)
- [7. Lifecycle contract](#7-lifecycle-contract)
- [8. Required gates](#8-required-gates)
- [9. Directory contract](#9-directory-contract)
- [10. Inputs and outputs](#10-inputs-and-outputs)
- [11. Minimal closure receipt](#11-minimal-closure-receipt)
- [12. Tests, fixtures, receipts, and proofs](#12-tests-fixtures-receipts-and-proofs)
- [13. Promotion, publication, correction, and rollback](#13-promotion-publication-correction-and-rollback)
- [14. Definition of done](#14-definition-of-done)
- [15. Open questions](#15-open-questions)

---

## 1. Purpose

`pipelines/domains/hydrology/catalog_close/` is the executable sublane for closing Hydrology catalog/triplet candidates before release workflow review.

It supports closure checks for:

- catalog candidates for watersheds, HUC units, streams, reaches, gauges, wells, waterbodies, observations, hydrographs, and regulatory-context products;
- graph/triplet deltas derived from processed Hydrology records;
- public-safe layer candidates prepared by the Hydrology catalog sublane;
- EvidenceBundle references and evidence-resolution status;
- source-role and knowledge-character separation;
- time/freshness, observation, valid, retrieval, processing, catalog, release, and correction timestamps;
- NFHL/regulatory-context separation;
- model/method receipts for modeled hydrographs and derived outputs;
- public-safe transform receipts;
- correction paths and rollback targets required before release handoff.

This directory implements or will implement the **how** of catalog closure. It does not build the canonical source record, fetch source data, define schemas, encode policy, store catalog truth, write public API payloads, issue current safety guidance, or approve release.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable pipeline logic: the **how**. | CONFIRMED root responsibility |
| Why `domains/hydrology/`? | Hydrology is the domain lane used by Hydrology docs and pipeline README. | CONFIRMED documentation pattern; behavior NEEDS VERIFICATION |
| Why `catalog_close/`? | This is a narrow pre-release closure sublane for hydrology-specific catalog and graph handoff candidates. | PROPOSED / NEEDS VERIFICATION |
| Does this replace `pipelines/domains/hydrology/catalog/`? | No. `catalog/` builds handoff candidates; `catalog_close/` verifies closure before release workflow handoff. | PROPOSED |
| Does this replace `release/`? | No. It emits closure receipts; release decisions remain under release responsibility roots. | CONFIRMED governance posture |
| Where do catalog records live? | `data/catalog/domain/hydrology/` or approved catalog home. | CONFIRMED lifecycle posture; implementation NEEDS VERIFICATION |
| Where do closure receipts live? | `data/receipts/pipeline/hydrology/catalog_close/` or accepted receipt home. | PROPOSED / NEEDS VERIFICATION |
| Can this sublane publish? | No. It may prepare closure receipts and release handoffs only through governed workflow. | CONFIRMED doctrine posture |

> [!IMPORTANT]
> A closed catalog candidate is not automatically published. Closure means the candidate is eligible for release review because evidence, policy, source-role, time/freshness, sensitivity, correction, and rollback checks have explicit outcomes.

[⬆ Back to top](#top)

---

## 3. Closure anti-collapse rules

Catalog close must not convert projected metadata into truth or release authority.

Disallowed collapses:

```text
closure receipt -> release approval
catalog candidate -> public artifact
catalog candidate -> EvidenceBundle
triplet delta -> canonical review state
NFHL regulatory context -> observed inundation
observed gauge reading -> modeled hydrograph
modeled hydrograph -> observed gauge reading
official-source context -> KFM-issued current guidance
generated summary -> evidence
missing rollback target -> closed release handoff
```

Required distinctions:

- source role and knowledge character are explicit;
- observed, modeled, regulatory, official-source, derived, and generated classes stay separate;
- catalog candidate, triplet delta, release candidate, ReleaseManifest, and published artifact remain distinct;
- EvidenceBundle references resolve or closure abstains;
- public-safe transform state is explicit;
- correction and rollback refs exist before release handoff;
- finite policy outcome is recorded for every closure decision.

[⬆ Back to top](#top)

---

## 4. What belongs here

Files belong here when their primary responsibility is executable Hydrology catalog-closure processing.

Appropriate contents include:

- fixture-only closure preflight entrypoints;
- closure receipt builders;
- EvidenceBundle reference validators;
- source-role and knowledge-character closure validators;
- NFHL/regulatory-context closure validators;
- time/freshness closure validators;
- model/method receipt validators;
- public-safe transform reference validators;
- triplet/provenance closure validators;
- correction-path and rollback-target validators;
- release-candidate handoff builders that do not approve release;
- thin adapters that read governed lifecycle inputs, not live source systems.

A good placement test:

> If the code verifies that a Hydrology catalog/triplet candidate is complete enough for release workflow review and emits a closure receipt, it may belong here. If it fetches data, builds raw/processed Hydrology records, stores catalog truth, writes public layers, or approves release, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Source fetchers / connectors | `connectors/<source>` |
| Source descriptors / source registry entries | `data/registry/sources/hydrology/` or approved registry home |
| Hydrology architecture and doctrine | `docs/domains/hydrology/...` |
| Object meaning contracts | `contracts/domains/hydrology/` or accepted contract home |
| JSON Schemas | `schemas/contracts/v1/domains/hydrology/` or accepted schema home |
| Policy, rights, sensitivity, release rules | `policy/...` responsibility roots |
| Catalog candidate builders | `pipelines/domains/hydrology/catalog/` or centralized catalog adapters |
| Shared catalog framework logic | `pipelines/catalog/` or shared packages |
| Declarative run specs | `pipeline_specs/hydrology/...` |
| Fixtures | `fixtures/domains/hydrology/catalog_close/` or accepted fixture home |
| Tests | `tests/pipelines/domains/hydrology/catalog_close/` or accepted test home |
| Raw, work, quarantine, processed, catalog, triplet, or published outputs | `data/...` lifecycle homes |
| Receipts and proofs | `data/receipts/...`, `data/proofs/...` |
| Release decisions and manifests | `release/candidates/hydrology/`, `release/manifests/hydrology/`, rollback/correction release homes |
| Public API or map code | `apps/governed-api/`, `apps/explorer-web/`, packages |
| Current safety instructions, official forecast decisions, or regulatory determinations | Outside this executable closure lane |

[⬆ Back to top](#top)

---

## 6. Closure scope

| Scope area | Closure responsibility | Failure behavior |
|---|---|---|
| Processed input | Confirm catalog candidate points to processed Hydrology input. | Quarantine or deny release handoff. |
| Evidence | Confirm EvidenceBundle refs resolve. | Abstain or quarantine. |
| Source role | Confirm observed, modeled, regulatory, official-source, derived, and generated classes are labeled. | Deny closure if collapsed. |
| NFHL context | Confirm regulatory-context label and caveat. | Deny closure if treated as observed event. |
| Time/freshness | Confirm observation/valid/retrieval/processing/catalog/release/correction times. | Quarantine or restrict. |
| Model outputs | Confirm method/model receipt refs. | Abstain or quarantine. |
| Triplet deltas | Confirm provenance and review-state refs. | Deny closure if projection replaces canonical state. |
| Public-safe transform | Confirm redaction/generalization/restriction/denial state. | Deny release handoff if missing. |
| Correction/rollback | Confirm correction path and rollback target. | Deny release handoff if missing. |

[⬆ Back to top](#top)

---

## 7. Lifecycle contract

Every Hydrology catalog-close run must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal stance:

1. **Read** catalog/triplet candidates, processed input refs, validation reports, public-safe transform receipts, EvidenceBundle refs, policy outcomes, correction refs, and rollback refs.
2. **Validate** closure state without mutating canonical records.
3. **Emit** a closure receipt only when every required gate has a finite outcome.
4. **Route** failed closure to quarantine, abstention, denial, restriction, or remediation depending on severity.
5. **Support release workflow** by providing reviewable closure packages.
6. **Never publish directly.**

Catalog close is a release-preflight gate. It is not release approval.

[⬆ Back to top](#top)

---

## 8. Required gates

Every Hydrology catalog-close run must check or explicitly fail closed on:

1. **Input lifecycle gate** — input is catalog/triplet candidate derived from processed Hydrology records.
2. **Processed-ref gate** — every catalog candidate points to an immutable processed input ref.
3. **Source descriptor gate** — source identity, role, rights, cadence/freshness, and sensitivity posture are known.
4. **Source-role gate** — observed, modeled, regulatory, official-source context, derived, and generated classes remain distinct.
5. **NFHL gate** — NFHL records remain regulatory context, not observed inundation.
6. **Time/freshness gate** — all material time fields and freshness/stale states are explicit.
7. **Model receipt gate** — model or reconstruction products carry method receipt refs.
8. **Evidence gate** — claim-bearing catalog records resolve EvidenceBundle support or abstain.
9. **Policy gate** — finite policy outcome exists; no silent allow.
10. **Sensitivity/public-safe gate** — public-facing handoff candidates carry redaction/generalization/restriction/denial state.
11. **Triplet/projection gate** — graph deltas preserve provenance and do not replace canonical records or review state.
12. **Schema/contract gate** — closure records match approved catalog and hydrology semantics.
13. **Correction/rollback gate** — correction path and rollback target are present before release handoff.
14. **No-direct-publish gate** — no writes to public UI, public API, published layers, or release manifests without release workflow authority.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended shape:

```text
pipelines/domains/hydrology/catalog_close/
├── README.md                         # this file
├── CLOSURE_CONTRACT.md               # PROPOSED: hydrology catalog-close contract
├── run_dry_fixture.py                # PROPOSED synthetic/redacted fixture only
├── close_catalog_candidate.py        # PROPOSED
├── close_triplet_delta.py            # PROPOSED
├── build_closure_receipt.py          # PROPOSED
├── validate_processed_refs.py        # PROPOSED
├── validate_source_roles.py          # PROPOSED
├── validate_nfhl_context.py          # PROPOSED
├── validate_time_freshness.py        # PROPOSED
├── validate_evidence_refs.py         # PROPOSED
├── validate_public_safe_state.py     # PROPOSED
├── validate_correction_rollback.py   # PROPOSED
└── adapters/                         # PROPOSED thin lifecycle adapters, no source fetching
```

Declarative specs should live outside this directory:

```text
pipeline_specs/hydrology/catalog_close.yaml # PROPOSED / NEEDS VERIFICATION
```

Generated outputs must not be written beside this code. Use accepted lifecycle homes under `data/catalog/domain/hydrology/`, graph homes under `data/triplets/hydrology/`, quarantine homes under `data/quarantine/hydrology/`, proof homes under `data/proofs/`, receipt homes under `data/receipts/`, and release homes under `release/`.

[⬆ Back to top](#top)

---

## 10. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Fixture input | `fixtures/domains/hydrology/catalog_close/` or accepted fixture home | Synthetic, generalized, or redacted. |
| Catalog candidate input | `data/catalog/domain/hydrology/...` or approved catalog home | Projection only; not release. |
| Triplet candidate input | `data/triplets/hydrology/...` or approved graph-delta home | Projection only. |
| Processed input ref | `data/processed/hydrology/<dataset_id>/<version>/` | Required immutable input. |
| Evidence input | `data/proofs/evidence_bundle/` or accepted proof home | Required for claim-bearing records. |
| Closure receipt | `data/receipts/pipeline/hydrology/catalog_close/<run_id>.yml` or accepted receipt home | Records gate outcomes and refs. |
| Quarantine record | `data/quarantine/hydrology/<reason>/<run_id>/` | Failed, restricted, unresolved, or unsafe material. |
| Release handoff | `release/candidates/hydrology/...` | Only through release workflow. |

[⬆ Back to top](#top)

---

## 11. Minimal closure receipt

The final schema is not defined here. This example shows the minimum information a Hydrology catalog-close receipt should preserve.

```yaml
schema_version: kfm.hydrology_catalog_close_receipt.v1
receipt_id: hydrology_catalog_close_<dataset_id>_<run_id>_<hash>
pipeline_id: domains.hydrology.catalog_close
run_id: run_YYYYMMDDThhmmssZ
status: CLOSURE_RECEIPT
input:
  catalog_candidate_ref: data/catalog/domain/hydrology/<dataset_id>/<version>/catalog.json
  triplet_delta_ref: data/triplets/hydrology/<dataset_id>/<version>/delta.jsonl
  processed_ref: data/processed/hydrology/<dataset_id>/<version>/
  input_hash: sha256:<hash>
knowledge_character: <observed|modeled|regulatory_context|official_source_context|derived|generated_context>
gates:
  processed_ref: PASS
  source_role: PASS
  nfhl_context: PASS
  time_freshness: PASS
  model_receipt: NOT_APPLICABLE
  evidence_bundle: PASS
  policy: ABSTAIN
  public_safe_state: PASS
  correction_path: PASS
  rollback_target: PASS
anti_collapse:
  closure_is_release_approval: false
  nfhl_is_observed_flooding: false
  modeled_hydrograph_is_observation: false
  catalog_item_is_evidence_bundle: false
  triplet_projection_is_canonical_truth: false
outcome:
  decision: ABSTAIN
  reason_code: POLICY_OR_RELEASE_REVIEW_NOT_CLOSED
  release_handoff_eligible: false
outputs:
  closure_receipt_ref: data/receipts/pipeline/hydrology/catalog_close/run_YYYYMMDDThhmmssZ.yml
rollback:
  required_before_publication: true
```

[⬆ Back to top](#top)

---

## 12. Tests, fixtures, receipts, and proofs

Default execution is **fixture-only, synthetic/generalized/redacted, and no-network** until catalog profile, closure spec, evidence, policy, sensitivity, and CI coverage are approved.

Recommended tests:

```text
tests/pipelines/domains/hydrology/catalog_close/
├── test_no_network_dry_run.py             # PROPOSED
├── test_catalog_candidate_input_required.py # PROPOSED
├── test_processed_ref_required.py         # PROPOSED
├── test_nfhl_not_observed_flooding.py     # PROPOSED
├── test_model_receipt_required.py         # PROPOSED
├── test_time_freshness_required.py        # PROPOSED
├── test_evidence_bundle_required.py       # PROPOSED
├── test_closure_not_release.py            # PROPOSED
├── test_catalog_not_evidence_bundle.py    # PROPOSED
├── test_triplet_not_canonical_truth.py    # PROPOSED
├── test_public_safe_transform_required.py # PROPOSED
├── test_rollback_target_required.py       # PROPOSED
├── test_receipt_hashes.py                 # PROPOSED
└── test_no_direct_publish.py              # PROPOSED
```

A dry run should prove fixtures load without network access, processed refs are required, NFHL stays regulatory context, observations and model products remain distinct, EvidenceBundle gaps produce abstention, closure cannot approve release, receipts are deterministic, and no run writes directly to public UI, public API, `data/published/`, or release manifests.

[⬆ Back to top](#top)

---

## 13. Promotion, publication, correction, and rollback

Hydrology catalog-close may emit closure receipts and release handoff candidates. It does not publish.

Required chain:

```text
catalog / triplet candidate
  -> closure checks
  -> closure receipt
  -> release candidate handoff
  -> ReleaseManifest review
  -> RollbackCard
  -> public-safe artifact
```

Correction and rollback posture:

- denied, abstained, errored, restricted, stale, conflicted, and quarantined closure runs remain auditable;
- closure receipts preserve input hashes, evidence refs, source-role refs, policy outcomes, correction refs, and rollback refs;
- release handoff eligibility is recomputed when processed refs, EvidenceBundle refs, policy refs, transform refs, catalog refs, graph refs, or rollback refs drift;
- public artifact rollback is owned by `release/`, not by this directory.

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- fills the blank `pipelines/domains/hydrology/catalog_close/README.md` file;
- identifies this directory as a nested executable Hydrology catalog-close sublane;
- prevents source fetcher, schema, contract, policy, data, proof, catalog-store, graph-store, and release authority from being placed here;
- preserves processed refs, source role, NFHL/regulatory-context separation, observed/model distinction, time/freshness, EvidenceBundle refs, policy, public-safe state, correction path, rollback target, and release boundary;
- blocks closure-as-release, catalog-as-evidence, NFHL-as-observed, model-as-observation, and triplet-as-canonical-truth collapse;
- gives maintainers a fixture-first, fail-closed expansion pattern.

Future executable work in this sublane is done only when it has closure-profile review, processed-input fixtures, schema-backed closure receipts, contract conformance, source-role/NFHL/evidence/policy/release/rollback tests, deterministic receipts, no-direct-publish tests, CI coverage, steward-review handoff, and release/correction/rollback documentation.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `HYDRO-CATALOG-CLOSE-001` | Should catalog close remain Hydrology-specific, or move into centralized `pipelines/catalog/` with Hydrology adapters? | NEEDS VERIFICATION / ADR |
| `HYDRO-CATALOG-CLOSE-002` | Which closure schema owns gate outcomes, release handoff eligibility, and rollback refs? | NEEDS VERIFICATION |
| `HYDRO-CATALOG-CLOSE-003` | Which first-wave object families should closure support: HUCs, reaches, gauges, water-quality series, NFHL context, or model outputs? | NEEDS VERIFICATION |
| `HYDRO-CATALOG-CLOSE-004` | Which CI job owns Hydrology catalog-close invariant tests? | UNKNOWN |
| `HYDRO-CATALOG-CLOSE-005` | Which policy outcome values are allowed to proceed from closure receipt to release-candidate review? | NEEDS VERIFICATION |
| `HYDRO-CATALOG-CLOSE-006` | Which rollback target format is required before release handoff? | NEEDS VERIFICATION |
| `HYDRO-CATALOG-CLOSE-007` | How should closure respond when catalog candidate, triplet delta, processed input, and EvidenceBundle refs drift at different times? | NEEDS VERIFICATION |

---

## Maintainer note

Start with synthetic/generalized fixture-only dry runs and negative tests. Do not add live source fetching, catalog-store writes, graph-store writes, public map layer writes, release-manifest writes, current safety guidance, or direct API payload generation until source roles, evidence closure, public-safe transforms, catalog profiles, release review, and rollback are proven.
