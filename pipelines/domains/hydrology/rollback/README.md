<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-hydrology-rollback-readme
title: Hydrology Rollback Pipeline README
type: readme
version: v0.1
status: draft
owners:
  - <hydrology-pipeline-owner>
  - <hydrology-domain-steward>
  - <release-steward>
  - <catalog-steward>
  - <map-layer-steward>
  - <evidence-steward>
  - <policy-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: pipelines/domains/hydrology/rollback/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipelines/domains/README.md
  - pipelines/domains/hydrology/README.md
  - pipelines/domains/hydrology/publish/README.md
  - pipelines/domains/hydrology/publish_layers/README.md
  - pipelines/domains/hydrology/catalog_close/README.md
  - docs/domains/hydrology/README.md
  - docs/domains/hydrology/PUBLICATION_POSTURE.md
  - docs/domains/hydrology/DATA_LIFECYCLE.md
  - pipeline_specs/hydrology/rollback.yaml
  - contracts/domains/hydrology/
  - schemas/contracts/v1/domains/hydrology/
  - policy/domains/hydrology/
  - policy/sensitivity/hydrology/
  - data/catalog/domain/hydrology/
  - data/triplets/hydrology/
  - data/published/layers/hydrology/
  - data/receipts/pipeline/
  - data/proofs/evidence_bundle/
  - release/candidates/hydrology/
  - release/manifests/hydrology/
  - release/promotion_decisions/hydrology/
  - release/corrections/hydrology/
tags:
  - kfm
  - pipelines
  - domains
  - hydrology
  - rollback
  - release-controlled
  - rollback-card
  - correction
  - tombstone
  - supersession
  - integrity
  - evidence-bundle
  - source-role
  - nfhl
  - governed-api
  - governance
notes:
  - "This README fills the blank pipelines/domains/hydrology/rollback path as a nested executable rollback-materialization sublane."
  - "Rollback logic here is executable rollback support only; it does not own rollback approval, release decisions, release manifests, policy, EvidenceBundle truth, catalog truth, lifecycle data, source descriptors, schemas, or public API authority."
  - "Rollback remains a governed release/correction state transition under release responsibility roots; this sublane may only materialize rollback actions from approved RollbackCard or release-correction inputs."
  - "Hydrology rollback must preserve source-role, time/freshness, evidence, public-safe transform, correction, supersession, tombstone, integrity, and rollback state."
  - "NFHL remains regulatory context only and must never roll back into observed flooding, current condition, or KFM-issued guidance."
  - "Concrete executable behavior, schedules, CI coverage, schema paths, release wiring, cache invalidation, and public API/map behavior remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hydrology Rollback Pipeline

> Executable Hydrology sublane for materializing release-approved rollback actions against previously published Hydrology artifacts — without making rollback decisions, rewriting canonical evidence, hiding superseded artifacts, or exposing internal lifecycle stores.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-hydrology%20rollback-2e7d32)
![authority](https://img.shields.io/badge/authority-rollback%20materialization%20only-0a7ea4)
![release](https://img.shields.io/badge/rollback%20approval-not%20owned%20here-d62728)
![anti-collapse](https://img.shields.io/badge/rollback%20%E2%89%A0%20hidden%20overwrite-d62728)
![ci](https://img.shields.io/badge/CI-TODO-lightgrey)

**Status:** Draft  
**Path:** `pipelines/domains/hydrology/rollback/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Domain lane:** Hydrology  
**Sublane:** Rollback materialization / correction support  
**Placement posture:** nested executable sublane under `pipelines/domains/hydrology/`; concrete executable behavior remains `PROPOSED / NEEDS VERIFICATION` unless backed by tests and repo evidence  
**Publication posture:** release-controlled rollback support only; no rollback approval, no release decision, no direct public API authority, and no hidden overwrite

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Rollback anti-collapse rules](#3-rollback-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Rollback scope](#6-rollback-scope)
- [7. Lifecycle contract](#7-lifecycle-contract)
- [8. Required gates](#8-required-gates)
- [9. Directory contract](#9-directory-contract)
- [10. Inputs and outputs](#10-inputs-and-outputs)
- [11. Minimal rollback receipt](#11-minimal-rollback-receipt)
- [12. Tests, fixtures, receipts, and proofs](#12-tests-fixtures-receipts-and-proofs)
- [13. Correction, supersession, and rollback](#13-correction-supersession-and-rollback)
- [14. Definition of done](#14-definition-of-done)
- [15. Open questions](#15-open-questions)

---

## 1. Purpose

`pipelines/domains/hydrology/rollback/` is the executable sublane for materializing approved Hydrology rollback actions.

It supports rollback execution for:

- published Hydrology layer artifacts;
- published catalog exports;
- published graph/triplet projection exports;
- released metadata bundles for watersheds, HUCs, reaches, gauges, wells, waterbodies, observation datasets, hydrographs, terrain-support context, and regulatory-context products;
- tombstone markers, supersession markers, withdrawal markers, and correction notices;
- rollback integrity manifests and receipts proving every action was derived from a specific RollbackCard, ReleaseManifest, correction decision, and previously published artifact digest;
- governed API/cache invalidation handoff metadata where approved by release/API owners;
- audit packages that preserve the difference between withdrawn/superseded artifacts and canonical records.

This directory implements or will implement the **how** of rollback materialization. It does not decide rollback, define policy, approve corrections, define source identity, alter EvidenceBundles, mutate canonical records, fetch source data, issue current guidance, decide regulatory meaning, or certify engineering use.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable pipeline logic: the **how** of rollback materialization. | CONFIRMED root responsibility |
| Why `domains/hydrology/`? | Hydrology is the domain lane used by Hydrology docs and pipeline READMEs. | CONFIRMED documentation pattern; behavior NEEDS VERIFICATION |
| Why `rollback/`? | This is a narrow executable lane for materializing approved rollback/correction actions. | PROPOSED / NEEDS VERIFICATION |
| Does this own rollback decisions? | No. Rollback decisions, ReleaseManifests, correction decisions, and rollback cards remain under release responsibility roots. | CONFIRMED governance posture |
| Does this replace `publish/` or `publish_layers/`? | No. Publish lanes materialize approved artifacts; this lane materializes approved rollback or correction actions for those artifacts. | PROPOSED |
| Can it read RAW/WORK/QUARANTINE? | No for normal rollback. It reads release, published-artifact, integrity, correction, and rollback refs only. | CONFIRMED doctrine posture |
| Can it edit public API or UI code? | No. It may emit approved rollback artifacts/metadata; governed API and UI code live in app/package roots. | CONFIRMED root separation |

> [!IMPORTANT]
> A rollback pipeline is not a rollback authority. It is an executor that consumes approved rollback/correction inputs and produces auditable, reversible, public-safe rollback artifacts, receipts, tombstones, supersession markers, and cache/API handoff metadata where allowed.

[⬆ Back to top](#top)

---

## 3. Rollback anti-collapse rules

Rollback must not hide evidence history or mutate canonical truth.

Disallowed collapses:

```text
rollback job -> rollback approval
rollback receipt -> ReleaseManifest
withdrawn artifact -> deleted history
superseded artifact -> hidden overwrite
rollback marker -> EvidenceBundle change
rollback action -> source descriptor change
catalog tombstone -> canonical record deletion
triplet rollback -> erased provenance
NFHL regulatory context -> observed flooding
cache invalidation -> release decision
generated rollback summary -> evidence
missing rollback card -> rollback action
```

Required distinctions:

- RollbackCard, ReleaseManifest, correction decision, EvidenceBundle, SourceDescriptor, catalog item, graph delta, published artifact, tombstone, and rollback receipt remain distinct;
- rollback actions are append-only/auditable unless release policy explicitly authorizes physical removal;
- source role and knowledge character remain explicit in rollback metadata;
- correction time, rollback time, release time, tile-build time, observation time, and valid time remain distinct;
- withdrawn artifacts remain traceable through receipts and integrity manifests;
- public clients must be redirected to governed APIs or released rollback/correction artifacts, not internal stores.

[⬆ Back to top](#top)

---

## 4. What belongs here

Files belong here when their primary responsibility is executable Hydrology rollback materialization.

Appropriate contents include:

- fixture-only rollback dry-run entrypoints;
- RollbackCard readers;
- release/correction input validators;
- published artifact digest and integrity validators;
- tombstone, supersession, withdrawal, and correction marker builders;
- rollback receipt builders;
- rollback target materializers for layers, catalog exports, graph exports, and metadata packages;
- cache/API invalidation handoff emitters, if approved and not owned by API code;
- no-canonical-mutation validators;
- no-history-erasure validators;
- no-NFHL-as-observed validators for rollback metadata;
- thin adapters that read approved rollback inputs, not source systems or unapproved lifecycle stores.

A good placement test:

> If the code takes an approved Hydrology RollbackCard/correction input and materializes auditable rollback artifacts, tombstones, supersession markers, receipts, or cache handoff metadata, it may belong here. If it decides rollback, alters release approval, fetches source data, mutates canonical records, edits public API/UI code, or erases provenance, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Rollback approvals, release decisions, ReleaseManifests, correction approvals, rollback cards | `release/...` responsibility roots |
| Source fetchers / connectors | `connectors/<source>` or accepted connector home |
| Source catalog profiles | `docs/sources/catalog/...` |
| Source descriptors / source registry entries | `data/registry/sources/hydrology/` or approved registry home |
| Hydrology architecture and doctrine | `docs/domains/hydrology/...` |
| Object meaning contracts | `contracts/domains/hydrology/` or accepted contract home |
| JSON Schemas | `schemas/contracts/v1/domains/hydrology/` or accepted schema home |
| Policy, rights, sensitivity, release rules | `policy/...` responsibility roots |
| Ingest, normalize, validate, catalog, catalog-close, or publish logic | Owning `pipelines/domains/hydrology/*` lane |
| Declarative run specs | `pipeline_specs/hydrology/...` |
| Fixtures | `fixtures/domains/hydrology/rollback/` or accepted fixture home |
| Tests | `tests/pipelines/domains/hydrology/rollback/` or accepted test home |
| Raw, work, quarantine, processed, catalog, triplet, or published source stores | `data/...` lifecycle homes |
| Public API or UI code | `apps/governed-api/`, `apps/explorer-web/`, packages |
| Current guidance, operational decisions, regulatory determinations, or engineering certification | Outside this rollback materialization lane |

[⬆ Back to top](#top)

---

## 6. Rollback scope

| Scope area | Rollback responsibility | Failure behavior |
|---|---|---|
| Rollback input | Confirm approved RollbackCard/correction decision and ReleaseManifest refs. | Deny rollback materialization. |
| Published artifact refs | Verify artifact ids, paths, hashes, formats, and release ids. | Deny or quarantine on mismatch. |
| Tombstone/supersession | Materialize approved markers and notices. | Deny if release/correction refs are missing. |
| Evidence refs | Preserve EvidenceBundle refs and citation state. | Deny if claim-bearing rollback lacks support. |
| Source-role metadata | Preserve observed, modeled, regulatory, aggregate, derived, generated context. | Deny if collapsed. |
| NFHL context | Preserve regulatory-context caveat. | Deny if treated as observed flooding or current condition. |
| Integrity | Emit hashes, manifests, and rollback receipts. | Deny if digest mismatch. |
| Cache/API handoff | Emit approved invalidation metadata only. | Deny if it would alter app code or release state. |

[⬆ Back to top](#top)

---

## 7. Lifecycle contract

Every Hydrology rollback run must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal stance:

1. **Read** approved rollback inputs only: RollbackCard, correction decision, ReleaseManifest refs, published artifact refs, prior publish receipts, catalog/triplet refs, EvidenceBundle refs, policy outcomes, and integrity manifests.
2. **Validate** rollback approval, artifact identity, artifact hashes, public-safe state, source-role metadata, correction path, and target rollback posture.
3. **Materialize** approved tombstone, supersession, withdrawal, replacement-pointer, or cache/API handoff artifacts into accepted release/published homes only.
4. **Emit receipts** with rollback refs, input refs, release refs, artifact hashes, output refs, correction refs, and verification refs.
5. **Never mutate** canonical stores, source descriptors, policy, schemas, EvidenceBundles, or release decisions.
6. **Never run rollback without approved rollback input.**

Rollback is a governed release/correction state transition controlled by release authority. This pipeline only performs the approved materialization step.

[⬆ Back to top](#top)

---

## 8. Required gates

Every Hydrology rollback run must check or explicitly fail closed on:

1. **RollbackCard gate** — approved RollbackCard or accepted rollback decision exists and names Hydrology targets.
2. **ReleaseManifest gate** — original ReleaseManifest and release id are known.
3. **Published-artifact gate** — artifact ids, paths, hashes, formats, and release ids match prior publish receipts.
4. **Correction decision gate** — correction, withdrawal, supersession, or tombstone reason is explicit.
5. **Evidence gate** — rollback/correction notices preserve EvidenceBundle refs for claim-bearing material.
6. **Policy gate** — finite policy outcome authorizes rollback action scope.
7. **Source-role gate** — observed, modeled, regulatory, official-source, aggregate, derived, and generated classes remain distinct.
8. **NFHL gate** — NFHL remains regulatory context and never appears as observed flooding or current guidance in rollback metadata.
9. **Integrity gate** — output paths, hashes, manifests, and rollback receipts pass validation.
10. **No-history-erasure gate** — artifacts are tombstoned/superseded/withdrawn per release policy, not silently erased.
11. **No-canonical-mutation gate** — rollback job does not alter source, processed, catalog, graph, policy, schema, EvidenceBundle, or release authority records.
12. **Governed API boundary gate** — API/cache invalidation is handoff metadata only unless app/API owners approve and implement it in their roots.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended shape:

```text
pipelines/domains/hydrology/rollback/
├── README.md                         # this file
├── ROLLBACK_CONTRACT.md              # PROPOSED: hydrology rollback materialization contract
├── run_dry_fixture.py                # PROPOSED synthetic/redacted fixture only
├── read_rollback_card.py             # PROPOSED
├── validate_rollback_inputs.py       # PROPOSED
├── validate_published_artifacts.py   # PROPOSED
├── validate_integrity_manifest.py    # PROPOSED
├── validate_no_history_erasure.py    # PROPOSED
├── build_tombstone_marker.py         # PROPOSED
├── build_supersession_marker.py      # PROPOSED
├── build_correction_notice.py        # PROPOSED
├── build_rollback_receipt.py         # PROPOSED
├── emit_cache_invalidation_handoff.py # PROPOSED only if approved
└── adapters/                         # PROPOSED thin release-input adapters, no source fetching
```

Declarative specs should live outside this directory:

```text
pipeline_specs/hydrology/rollback.yaml # PROPOSED / NEEDS VERIFICATION
```

Generated outputs must not be written beside this code. Use accepted release-controlled homes such as `release/corrections/hydrology/`, `release/manifests/hydrology/`, `data/published/layers/hydrology/` for approved tombstones/supersession pointers if policy allows, and `data/receipts/pipeline/hydrology/rollback/`.

[⬆ Back to top](#top)

---

## 10. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Fixture input | `fixtures/domains/hydrology/rollback/` or accepted fixture home | Synthetic, generalized, or redacted. |
| RollbackCard input | `release/manifests/hydrology/` or approved rollback-card home | Required before real rollback run. |
| Original ReleaseManifest | `release/manifests/hydrology/` | Required to bind rollback to a release. |
| Published artifact refs | `data/published/layers/hydrology/` or approved published homes | Verified by prior publish receipts. |
| Publish receipts | `data/receipts/pipeline/hydrology/publish/` and `data/receipts/pipeline/hydrology/publish_layers/` | Provide artifact hashes and refs. |
| Evidence input | `data/proofs/evidence_bundle/` | Preserved for correction/rollback notices. |
| Rollback output | `release/corrections/hydrology/` or approved release-controlled home | Tombstone, supersession, withdrawal, correction, or handoff metadata. |
| Rollback receipt | `data/receipts/pipeline/hydrology/rollback/<run_id>.yml` or accepted receipt home | Records rollback card, inputs, hashes, outputs, verification. |

[⬆ Back to top](#top)

---

## 11. Minimal rollback receipt

The final schema is not defined here. This example shows the minimum information a Hydrology rollback receipt should preserve.

```yaml
schema_version: kfm.hydrology_rollback_receipt.v1
receipt_id: hydrology_rollback_<release_id>_<run_id>_<hash>
pipeline_id: domains.hydrology.rollback
run_id: run_YYYYMMDDThhmmssZ
status: ROLLBACK_RECEIPT
rollback:
  rollback_id: <rollback_id>
  rollback_card_ref: release/manifests/hydrology/<release_id>.rollback.yml
  correction_decision_ref: release/corrections/hydrology/<rollback_id>/decision.yml
  original_release_manifest_ref: release/manifests/hydrology/<release_id>.yml
input_refs:
  published_artifact_refs: []
  publish_receipt_refs: []
  evidence_bundle_refs: []
  policy_decision_refs: []
  public_safe_transform_refs: []
action:
  action_type: <tombstone|supersede|withdraw|replace_pointer|cache_invalidation_handoff>
  reason_code: <reason>
  approved_by_ref: <release_decision_ref>
anti_collapse:
  rollback_job_is_rollback_approval: false
  rollback_receipt_is_release_manifest: false
  supersession_is_hidden_overwrite: false
  tombstone_is_canonical_deletion: false
  nfhl_is_observed_flooding: false
outputs:
  artifacts:
    - artifact_ref: release/corrections/hydrology/<rollback_id>/<artifact>.yml
      artifact_hash: sha256:<hash>
      artifact_kind: <tombstone|supersession|withdrawal|correction|handoff>
  integrity_manifest_ref: release/corrections/hydrology/<rollback_id>/manifest.yml
outcome:
  decision: MATERIALIZED
  rollback_handoff: complete
verification:
  published_artifacts_matched_prior_hashes: true
  no_canonical_mutation: true
  no_history_erasure: true
```

[⬆ Back to top](#top)

---

## 12. Tests, fixtures, receipts, and proofs

Default execution is **fixture-only, synthetic/generalized/redacted, and no-network** until rollback-input schema, published-artifact refs, evidence, policy, rollback, and CI coverage are approved.

Recommended tests:

```text
tests/pipelines/domains/hydrology/rollback/
├── test_no_network_dry_run.py              # PROPOSED
├── test_rollback_card_required.py          # PROPOSED
├── test_original_release_manifest_required.py # PROPOSED
├── test_published_artifact_hash_required.py # PROPOSED
├── test_publish_receipt_required.py        # PROPOSED
├── test_no_raw_work_quarantine_inputs.py   # PROPOSED
├── test_no_canonical_mutation.py           # PROPOSED
├── test_no_history_erasure.py              # PROPOSED
├── test_nfhl_not_observed_flooding.py      # PROPOSED
├── test_tombstone_not_canonical_delete.py  # PROPOSED
├── test_rollback_not_approval.py           # PROPOSED
├── test_integrity_hashes.py                # PROPOSED
├── test_correction_notice_required.py      # PROPOSED
└── test_governed_api_boundary.py           # PROPOSED
```

A dry run should prove fixtures load without network access, rollback cards and original release manifests are required, published artifact hashes match prior receipts, raw/work/quarantine inputs are denied, rollback does not mutate canonical stores, tombstones do not erase history, receipts are deterministic, and API/cache invalidation remains a governed handoff unless app/API owners implement it.

[⬆ Back to top](#top)

---

## 13. Correction, supersession, and rollback

Hydrology rollback must make correction, supersession, and withdrawal visible.

Required chain:

```text
approved Hydrology RollbackCard
  -> rollback input validation
  -> published artifact hash verification
  -> tombstone / supersession / withdrawal / correction materialization
  -> rollback integrity manifest
  -> rollback receipt
  -> cache/API handoff metadata where approved
  -> governed API / released artifact availability update by owning app or release workflow
```

Correction and rollback posture:

- published artifacts are superseded or withdrawn by governed release/correction workflow, not hidden overwrite;
- rollback receipts preserve release refs, rollback refs, input refs, artifact hashes, evidence refs, source-role refs, policy outcomes, correction refs, and verification refs;
- public artifacts are invalidated if RollbackCard, ReleaseManifest, EvidenceBundle, policy, source-role, public-safe transform, catalog, graph, correction, or artifact-hash refs drift;
- rollback action is owned by `release/`, but this pipeline may materialize approved rollback artifacts and prove no canonical mutation occurred.

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- fills the blank `pipelines/domains/hydrology/rollback/README.md` file;
- identifies this directory as a nested executable Hydrology rollback materialization sublane;
- prevents rollback-decision, source, schema, contract, policy, fixture, test, data, proof, catalog, graph, app, UI, and source-of-truth authority from being placed here;
- preserves RollbackCard, ReleaseManifest, correction decision, EvidenceBundle, source-role, time/freshness, policy, public-safe transform, artifact integrity, tombstone, supersession, correction, and rollback boundaries;
- blocks rollback-as-approval, rollback-as-hidden-overwrite, tombstone-as-canonical-delete, artifact-withdrawal-as-erased-history, NFHL-as-observed, and direct internal-store exposure;
- gives maintainers a fixture-first, fail-closed expansion pattern.

Future executable work in this sublane is done only when it has rollback-input fixtures, schema-backed rollback receipts, contract conformance, rollback-card/release-manifest/evidence/public-safe/source-role/no-canonical-mutation/no-history-erasure tests, deterministic integrity manifests, CI coverage, steward-review handoff, and correction/rollback documentation.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `HYDRO-ROLLBACK-001` | Should Hydrology rollback remain domain-specific, or should shared rollback materialization live in a release pipeline with Hydrology adapters? | NEEDS VERIFICATION / ADR |
| `HYDRO-ROLLBACK-002` | Which release schema owns RollbackCard, rollback receipts, correction manifests, and integrity manifests? | NEEDS VERIFICATION |
| `HYDRO-ROLLBACK-003` | Which action types are first-wave: tombstone, supersede, withdraw, replace pointer, cache-invalidation handoff, or all by adapter? | NEEDS VERIFICATION |
| `HYDRO-ROLLBACK-004` | Which CI job owns Hydrology rollback invariant tests? | UNKNOWN |
| `HYDRO-ROLLBACK-005` | Which published artifact classes are first-wave rollback targets: layers, catalog exports, graph exports, metadata packages, or all by release manifest? | NEEDS VERIFICATION |
| `HYDRO-ROLLBACK-006` | How should governed API cache invalidation be linked to rollback receipts without letting the rollback pipeline own API behavior? | NEEDS VERIFICATION / ADR |
| `HYDRO-ROLLBACK-007` | Which rollback verification format is required before artifact availability is changed? | NEEDS VERIFICATION |

---

## Maintainer note

Start with synthetic/generalized fixture-only dry runs and negative tests. Do not add live source fetching, rollback-decision logic, direct public API code, direct UI code, hidden deletion, unreviewed generated correction summaries, or writes to rollback/published homes until RollbackCard, ReleaseManifest, EvidenceBundle, public-safe transform, artifact integrity, correction, and no-canonical-mutation gates are proven.
