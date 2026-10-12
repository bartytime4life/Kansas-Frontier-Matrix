<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-hydrology-catalog-readme
title: Hydrology Catalog Pipeline README
type: readme
version: v0.1
status: draft
owners:
  - <hydrology-pipeline-owner>
  - <hydrology-domain-steward>
  - <catalog-steward>
  - <source-steward>
  - <evidence-steward>
  - <policy-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: pipelines/domains/hydrology/catalog/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipelines/catalog/README.md
  - pipelines/domains/README.md
  - pipelines/domains/hydrology/README.md
  - docs/domains/hydrology/README.md
  - docs/domains/hydrology/PUBLICATION_POSTURE.md
  - docs/domains/hydrology/DATA_LIFECYCLE.md
  - pipeline_specs/hydrology/catalog.yaml
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
  - data/published/layers/hydrology/
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
  - catalog
  - stac
  - dcat
  - evidence-bundle
  - source-role
  - nfhl
  - gauge
  - watershed
  - huc
  - reach
  - public-safe
  - evidence
  - policy
  - governance
notes:
  - "This README fills the blank pipelines/domains/hydrology/catalog path as a nested executable catalog-handoff sublane."
  - "Hydrology catalog logic is executable implementation support only; it does not own source descriptors, object meaning, schemas, policy, lifecycle data, catalog truth, public release, or regulatory determinations."
  - "Catalog candidates are downstream projections from processed Hydrology records; they do not replace EvidenceBundle, SourceDescriptor, validation, review state, policy, or release state."
  - "Observed readings, modeled hydrographs, regulatory flood context, official-source context, and generated summaries must remain separate catalog classes."
  - "NFHL is regulatory context only and must never be cataloged as observed flooding."
  - "Concrete executable behavior, schedules, CI coverage, schema paths, release wiring, and public API/map behavior remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hydrology Catalog Pipeline

> Executable Hydrology sublane for building governed catalog and graph handoff candidates from processed Hydrology records — preserving EvidenceBundle references, source roles, time/freshness state, NFHL regulatory-context separation, sensitivity decisions, release posture, correction path, and rollback targets.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-hydrology%20catalog%20handoff-2e7d32)
![authority](https://img.shields.io/badge/authority-executable%20logic-0a7ea4)
![anti-collapse](https://img.shields.io/badge/NFHL%20%E2%89%A0%20observed%20flooding-d62728)
![publication](https://img.shields.io/badge/publication-release%20gated-d62728)
![ci](https://img.shields.io/badge/CI-TODO-lightgrey)

**Status:** Draft  
**Path:** `pipelines/domains/hydrology/catalog/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Domain lane:** Hydrology  
**Sublane:** Catalog handoff  
**Placement posture:** nested executable sublane under `pipelines/domains/hydrology/`; concrete executable behavior remains `PROPOSED / NEEDS VERIFICATION` unless backed by tests and repo evidence  
**Public posture:** no direct publication; catalog outputs require processed-state input, EvidenceBundle closure, source-role separation, temporal/freshness caveats, sensitivity decision, policy outcome, release handoff, correction path, and rollback closure

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Catalog anti-collapse rules](#3-catalog-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Catalog scope](#6-catalog-scope)
- [7. Lifecycle contract](#7-lifecycle-contract)
- [8. Required gates](#8-required-gates)
- [9. Directory contract](#9-directory-contract)
- [10. Inputs and outputs](#10-inputs-and-outputs)
- [11. Minimal catalog handoff record](#11-minimal-catalog-handoff-record)
- [12. Tests, fixtures, receipts, and proofs](#12-tests-fixtures-receipts-and-proofs)
- [13. Promotion, publication, correction, and rollback](#13-promotion-publication-correction-and-rollback)
- [14. Definition of done](#14-definition-of-done)
- [15. Open questions](#15-open-questions)

---

## 1. Purpose

`pipelines/domains/hydrology/catalog/` is the executable sublane for Hydrology catalog-handoff processing.

It supports candidate processing for:

- catalog records for watersheds, HUC units, stream/reach identities, waterbodies, gauges, wells, and observation datasets;
- catalog records for flow, stage, water-level, water-quality, aquifer, groundwater, and hydrograph datasets;
- regulatory flood-context catalog candidates such as NFHL-zone products with explicit regulatory-context labels;
- modeled hydrograph and topology outputs with model/method receipt links;
- public-safe layer candidates after processed-state, policy, and release gates close;
- STAC/DCAT-style metadata candidates, where the approved catalog profile permits;
- graph/triplet handoff candidates that preserve provenance and do not replace canonical records;
- Evidence Drawer, Focus Mode, correction, and rollback handoff packages.

This directory implements or will implement the **how** of catalog handoff. It does not fetch source data, define Hydrology object meaning, define schemas, encode policy, store lifecycle data, decide release, issue current safety guidance, or decide regulatory meaning.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable pipeline logic: the **how**. | CONFIRMED root responsibility |
| Why `domains/hydrology/`? | Hydrology is the domain lane used by the Hydrology pipeline README and domain docs. | CONFIRMED documentation pattern; behavior NEEDS VERIFICATION |
| Why `catalog/` here? | This is a narrow executable sublane for hydrology-specific catalog/triplet handoff. | PROPOSED / NEEDS VERIFICATION |
| Does this replace `pipelines/catalog/`? | No. Shared catalog pipeline logic should remain centralized; this lane holds Hydrology-specific adapters only. | PROPOSED |
| Where do catalog records live? | `data/catalog/domain/hydrology/` or approved catalog home. | CONFIRMED lifecycle posture; implementation NEEDS VERIFICATION |
| Where do graph deltas live? | `data/triplets/hydrology/` or accepted graph-delta home. | PROPOSED / NEEDS VERIFICATION |
| Can this sublane publish? | No. It may prepare catalog and release handoffs only through governed workflow. | CONFIRMED doctrine posture |

> [!IMPORTANT]
> Catalog candidates are projections. They are not the canonical source record, not the EvidenceBundle, not the ReleaseManifest, and not an approval to publish. A catalog handoff that lacks evidence, policy, sensitivity, time/freshness, source-role, and rollback closure must abstain, deny, or quarantine.

[⬆ Back to top](#top)

---

## 3. Catalog anti-collapse rules

Hydrology catalog work must preserve truth class and lifecycle state.

Disallowed collapses:

```text
processed candidate -> published catalog item without release
catalog item -> EvidenceBundle
catalog item -> canonical source record
NFHL regulatory context -> observed inundation
observed gauge reading -> modeled hydrograph
modeled hydrograph -> observed gauge reading
official-source context -> KFM-issued guidance
generated summary -> evidence
triplet projection -> canonical review state
```

Required distinctions:

- source role is explicit;
- knowledge character is explicit where material;
- observed, modeled, regulatory, forecast-like, operational-context, and generated artifacts remain distinct;
- observation time, valid time, retrieval time, processing time, catalog time, release time, and correction time remain distinct;
- EvidenceBundle references resolve or the catalog handoff abstains;
- public-safe transform and release state are explicit;
- rollback target and correction path are recorded before public release handoff.

[⬆ Back to top](#top)

---

## 4. What belongs here

Files belong here when their primary responsibility is executable Hydrology catalog-handoff processing.

Appropriate contents include:

- fixture-only catalog handoff entrypoints;
- Hydrology-to-catalog record mappers;
- Hydrology-to-STAC or Hydrology-to-DCAT candidate mappers, where approved;
- Hydrology-to-triplet/graph handoff adapters, if not centralized elsewhere;
- source-role and knowledge-character validators for catalog records;
- NFHL/regulatory-context anti-collapse validators;
- gauge/time-series catalog validators;
- model/hydrograph receipt-reference validators;
- public-safe transform reference validators;
- release-preflight validators that do not approve release;
- receipt emitters, if not shared;
- thin adapters that read governed lifecycle inputs, not live source systems.

A good placement test:

> If the code transforms processed Hydrology lifecycle inputs into catalog, graph, or release-review handoff candidates, it may belong here. If it fetches source data, normalizes raw hydrology observations, defines schemas, encodes policy, stores catalog records, or approves public release, it belongs somewhere else.

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
| Shared catalog framework logic | `pipelines/catalog/` or shared packages |
| Declarative run specs | `pipeline_specs/hydrology/...` |
| Fixtures | `fixtures/domains/hydrology/catalog/` or accepted fixture home |
| Tests | `tests/pipelines/domains/hydrology/catalog/` or accepted test home |
| Raw, work, quarantine, processed, catalog, triplet, or published outputs | `data/...` lifecycle homes |
| Receipts and proofs | `data/receipts/...`, `data/proofs/...` |
| Release decisions | `release/candidates/hydrology/`, `release/manifests/hydrology/`, rollback/correction release homes |
| Public API or map code | `apps/governed-api/`, `apps/explorer-web/`, packages |
| Current safety instructions, official forecast decisions, or regulatory determinations | Outside this executable catalog handoff lane |

[⬆ Back to top](#top)

---

## 6. Catalog scope

| Scope area | Catalog responsibility | Failure behavior |
|---|---|---|
| Watersheds / HUCs | Emit source-bound catalog candidates with identity and time caveats. | Quarantine or abstain on missing evidence. |
| Stream / reach identity | Preserve source and geometry lineage. | No silent geometry authority. |
| Gauge / well sites | Preserve station/site identity, source, and observation family. | No current-state implication without freshness state. |
| Time-series datasets | Preserve variables, units, cadence, time basis, source role, and QA refs. | Quarantine if time/cadence is collapsed. |
| NFHL context | Label as regulatory context only. | Deny catalog handoff if treated as observed event. |
| Modeled hydrographs | Require ModelRunReceipt or equivalent method receipt. | Abstain or quarantine if method support is missing. |
| Public-safe layers | Reference approved public-safe transform and release candidate. | No direct publication. |
| Triplet/graph delta | Emit graph projection with provenance and review-state refs. | Projection cannot replace canonical review state. |

[⬆ Back to top](#top)

---

## 7. Lifecycle contract

Every Hydrology catalog run must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal stance:

1. **Read** approved fixtures, processed hydrology records, validation reports, public-safe transform receipts, EvidenceBundle refs, and release-candidate inputs.
2. **Validate** source role, evidence refs, schema refs, public-safe transform refs, time/freshness state, sensitivity outcome, policy decision, correction path, and rollback target.
3. **Emit** catalog or graph handoff candidates only into accepted lifecycle homes.
4. **Quarantine** missing EvidenceBundle, missing source role, NFHL/observed collapse, model/observation collapse, missing public-safe transform, missing rollback target, schema drift, policy failure, or validation failure.
5. **Support release** only by providing reviewable handoff packages to release workflow.
6. **Never publish directly.**

Catalog creation is a projection step. It is not public release by itself.

[⬆ Back to top](#top)

---

## 8. Required gates

Every Hydrology catalog run must check or explicitly fail closed on:

1. **Input lifecycle gate** — input is processed, fixture-only, or explicitly release-candidate material.
2. **Source descriptor gate** — source identity, role, rights, cadence/freshness, and sensitivity posture are known.
3. **Source-role gate** — observed, modeled, regulatory, official-source context, derived, and generated records remain distinct.
4. **NFHL gate** — NFHL records remain regulatory context, not observed inundation.
5. **Gauge/time-series gate** — variable, unit, cadence, observed time, valid time, retrieval time, and processing time are preserved.
6. **Model receipt gate** — model or reconstruction products carry model/method receipt refs.
7. **Evidence gate** — claim-bearing catalog records resolve EvidenceBundle support or abstain.
8. **Policy gate** — finite policy outcome exists; no silent allow.
9. **Sensitivity/public-safe gate** — public-facing catalog candidates carry redaction/generalization/restriction/denial state.
10. **Triplet/projection gate** — graph deltas preserve provenance and do not replace canonical records or review state.
11. **Schema/contract gate** — catalog candidates match approved catalog and hydrology semantics.
12. **Correction/rollback gate** — correction path and rollback target are present before release handoff.
13. **No-direct-publish gate** — no writes to public UI, public API, published layers, or release manifests without release workflow authority.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended shape:

```text
pipelines/domains/hydrology/catalog/
├── README.md                         # this file
├── PIPELINE_CONTRACT.md              # PROPOSED: hydrology catalog handoff contract
├── run_dry_fixture.py                # PROPOSED synthetic/redacted fixture only
├── build_catalog_candidate.py        # PROPOSED
├── build_stac_item_candidate.py      # PROPOSED if approved profile exists
├── build_dcat_record_candidate.py    # PROPOSED if approved profile exists
├── build_triplet_handoff.py          # PROPOSED if not centralized in pipelines/catalog/
├── validate_source_role.py           # PROPOSED
├── validate_nfhl_context.py          # PROPOSED
├── validate_time_freshness.py        # PROPOSED
├── validate_evidence_refs.py         # PROPOSED
├── validate_public_safe_release.py   # PROPOSED release preflight only
├── emit_receipt.py                   # PROPOSED only if not shared
└── adapters/                         # PROPOSED thin lifecycle adapters, no source fetching
```

Declarative specs should live outside this directory:

```text
pipeline_specs/hydrology/catalog.yaml # PROPOSED / NEEDS VERIFICATION
```

Generated catalog outputs must not be written beside this code. Use accepted lifecycle homes under `data/catalog/domain/hydrology/`, graph homes under `data/triplets/hydrology/`, proof homes under `data/proofs/`, receipt homes under `data/receipts/`, and release homes under `release/`.

[⬆ Back to top](#top)

---

## 10. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Fixture input | `fixtures/domains/hydrology/catalog/` or accepted fixture home | Synthetic, generalized, or redacted. |
| Processed hydrology input | `data/processed/hydrology/<dataset_id>/<version>/` | Validated/restricted; not automatically public. |
| Evidence input | `data/proofs/evidence_bundle/` or accepted proof home | Required for claim-bearing records. |
| Transform receipt input | `data/receipts/...` | Public-safe and model/method receipts where applicable. |
| Catalog candidate | `data/catalog/domain/hydrology/...` or approved catalog home | Projection only. |
| Triplet / graph delta | `data/triplets/hydrology/...` or approved graph-delta home | Projection only. |
| Quarantine record | `data/quarantine/hydrology/<reason>/<run_id>/` | Failed, restricted, unresolved, or unsafe material. |
| Run receipt | `data/receipts/pipeline/hydrology/catalog/<run_id>.yml` or accepted receipt home | Records input refs, methods, checks, and outputs. |
| Release handoff | `release/candidates/hydrology/...` | Only through release workflow. |

[⬆ Back to top](#top)

---

## 11. Minimal catalog handoff record

The final schema is not defined here. This example shows the minimum information a Hydrology catalog handoff should preserve.

```yaml
schema_version: kfm.hydrology_catalog_handoff.v1
handoff_id: hydrology_catalog_<dataset_id>_<run_id>_<hash>
pipeline_id: domains.hydrology.catalog
run_id: run_YYYYMMDDThhmmssZ
status: CATALOG_CANDIDATE
input:
  processed_ref: data/processed/hydrology/<dataset_id>/<version>/
  input_hash: sha256:<hash>
  source_ids: []
  source_roles: []
knowledge_character: <observed|modeled|regulatory_context|derived|generated_context>
anti_collapse:
  nfhl_is_observed_flooding: false
  modeled_hydrograph_is_observation: false
  catalog_item_is_evidence_bundle: false
  triplet_projection_is_canonical_truth: false
validation:
  evidence_bundle_ref: data/proofs/evidence_bundle/<bundle_id>.json
  policy_outcome: ABSTAIN
  public_safe_transform_ref: null
  rollback_target_ref: null
outputs:
  catalog_candidate_ref: data/catalog/domain/hydrology/<dataset_id>/<version>/catalog.json
  triplet_delta_ref: data/triplets/hydrology/<dataset_id>/<version>/delta.jsonl
  receipt_ref: data/receipts/pipeline/hydrology/catalog/run_YYYYMMDDThhmmssZ.yml
rollback:
  required_before_publication: true
```

[⬆ Back to top](#top)

---

## 12. Tests, fixtures, receipts, and proofs

Default execution is **fixture-only, synthetic/generalized/redacted, and no-network** until catalog profile, evidence, policy, sensitivity, and CI coverage are approved.

Recommended tests:

```text
tests/pipelines/domains/hydrology/catalog/
├── test_no_network_dry_run.py                 # PROPOSED
├── test_processed_input_required.py           # PROPOSED
├── test_source_role_required.py               # PROPOSED
├── test_nfhl_not_observed_flooding.py         # PROPOSED
├── test_model_receipt_required.py             # PROPOSED
├── test_gauge_time_freshness_preserved.py     # PROPOSED
├── test_evidence_bundle_required.py           # PROPOSED
├── test_catalog_not_release.py                # PROPOSED
├── test_triplet_not_canonical_truth.py        # PROPOSED
├── test_public_safe_transform_required.py     # PROPOSED
├── test_rollback_target_required.py           # PROPOSED
├── test_receipt_hashes.py                     # PROPOSED
└── test_no_direct_publish.py                  # PROPOSED
```

A dry run should prove fixtures load without network access, processed-state inputs are required, NFHL stays regulatory context, observations and model products remain distinct, EvidenceBundle gaps produce abstention, catalog/triplet candidates retain provenance, receipts are deterministic, and no run writes directly to public UI, public API, `data/published/`, or release manifests.

[⬆ Back to top](#top)

---

## 13. Promotion, publication, correction, and rollback

Hydrology catalog pipelines may prepare catalog and graph candidates. They do not publish.

Required promotion chain:

```text
processed Hydrology record
  -> evidence / policy / public-safe validation
  -> catalog candidate
  -> triplet / graph candidate
  -> release candidate
  -> ReleaseManifest
  -> RollbackCard
  -> public-safe artifact
```

Correction and rollback posture:

- denied, abstained, errored, restricted, stale, conflicted, and quarantined catalog runs remain auditable;
- catalog candidates preserve input hashes, evidence refs, source-role refs, and policy outcomes;
- graph deltas are superseded by governed state transition, not hidden overwrite;
- catalog candidates are invalidated if processed refs, EvidenceBundle refs, policy refs, source-role refs, transform refs, or rollback refs drift;
- public artifact rollback is owned by `release/`, not by this directory.

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- fills the blank `pipelines/domains/hydrology/catalog/README.md` file;
- identifies this directory as a nested executable Hydrology catalog-handoff sublane;
- prevents source fetcher, source-profile, schema, contract, policy, fixture, test, data, proof, catalog-store, graph-store, and release authority from being placed here;
- preserves source role, NFHL/regulatory-context separation, observed/model distinction, time/freshness, EvidenceBundle refs, policy, lifecycle, catalog/triplet, release, correction, and rollback boundaries;
- blocks catalog-as-release, catalog-as-evidence, NFHL-as-observed, model-as-observation, and triplet-as-canonical-truth collapse;
- gives maintainers a fixture-first, fail-closed expansion pattern.

Future executable work in this sublane is done only when it has processed-input fixtures, catalog-profile review, schema-backed handoff candidates, contract conformance, source-role/NFHL/evidence/policy/release tests, deterministic receipts, no-direct-publish tests, CI coverage, steward-review handoff, and release/correction/rollback documentation.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `HYDRO-CATALOG-001` | Should Hydrology-specific catalog code live here, or should all catalog logic live in centralized `pipelines/catalog/` with Hydrology adapters? | NEEDS VERIFICATION / ADR |
| `HYDRO-CATALOG-002` | Which approved catalog profile governs first-wave Hydrology candidates: STAC, DCAT, KFM internal catalog, or all three through adapters? | NEEDS VERIFICATION |
| `HYDRO-CATALOG-003` | Which Hydrology object families are first-wave catalog candidates: HUCs, reaches, gauges, water-quality series, NFHL context, or model outputs? | NEEDS VERIFICATION |
| `HYDRO-CATALOG-004` | Which schema owns catalog handoff and triplet delta fields? | NEEDS VERIFICATION |
| `HYDRO-CATALOG-005` | Which CI job owns Hydrology catalog invariant tests? | UNKNOWN |
| `HYDRO-CATALOG-006` | Which public-safe map/API products are allowed after review and release, and at what precision/time/freshness caveat level? | NEEDS VERIFICATION |
| `HYDRO-CATALOG-007` | Which receipt type owns model, public-safe transform, and graph-projection derivations used by catalog handoff? | PROPOSED / NEEDS ADR |

---

## Maintainer note

Start with synthetic/generalized fixture-only dry runs and negative tests. Do not add live source fetching, direct catalog-store writes, public map layer writes, release-manifest writes, current safety guidance, or direct API payload generation until source roles, evidence closure, public-safe transforms, catalog profiles, release review, and rollback are proven.
