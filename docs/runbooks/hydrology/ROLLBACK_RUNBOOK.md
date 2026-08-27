<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbook-hydrology-rollback
title: Hydrology Rollback Runbook
type: operational-runbook
version: v2.0.0
status: DRAFT_REPOSITORY_GROUNDED; DECISION_AND_REVIEW_HANDOFF_ONLY; GENERIC_SYNTHETIC_REHEARSAL_AVAILABLE; HYDROLOGY_SPECIFIC_REHEARSAL_ABSENT; OPERATIONAL_ROLLBACK_HELD; NOT_FOR_LIFE_SAFETY; NON_RELEASE; NON_PUBLICATION
owners: "@bartytime4life — verified CODEOWNERS route; accountable Hydrology, evidence, policy, rights, sensitivity, review, correction, rollback, release, operations, and public-recovery stewardship NEEDS VERIFICATION"
created: 2026-05-12
updated: 2026-08-27
policy_label: repository-facing; hydrology; rollback; withdrawal; correction-aware; synthetic-proof-bounded; fail-closed; not-for-life-safety; non-publisher
owning_root: docs/
path_authority: same-path modernization under accepted ADR-0029 and Directory Rules v2
authority_effect: none
source_activation_effect: none
lifecycle_effect: none
release_effect: none
deployment_effect: none
promotion_effect: none
publication_effect: none
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 8e7c862f5bf91fb27038ef264549b565b4827711
  target_path: docs/runbooks/hydrology/ROLLBACK_RUNBOOK.md
  target_prior_blob: 6c6f06f87de2b2b0e528e670ef43ae46bbc17d06
  adjacent_scaffold_path: docs/runbooks/hydrology/ROLLBACK.md
  adjacent_scaffold_blob: 4ec794c5bad3b13368de88b8b258c10b9972cb1b
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adoption_adr_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  generic_rehearsal_runbook_blob: c65b2790a2796572498ff07d4d12c4f028eb50c6
  generic_rehearsal_helper_blob: a8f6bff350e79b453f425ebce9a9ded6801f8944
  generic_rehearsal_test_blob: b644ca6c4185b3f81bc339c077eae85299833261
  rollback_workflow_blob: 2d0c39fc6ff8e44bd9cf753ce546475079e8ffd5
  rollback_card_contract_blob: c6d3c35c56b064e04c3a2532f4709d938d7b0c1a
  rollback_card_schema_blob: e0a9edf02dd5d6997eda60a054a5bf19636c3dd4
  rollback_card_validator_blob: 9e9ed5a92851935b41a36698e4bead13ef4edf57
  hydrology_promotion_runbook_blob: ee57bfecd96fd05dae8a49e001850d3752596742
  hydrology_validation_runbook_blob: c6c6ee9c89ad394847ef9e5ac053b7a136595678
  production_rollback_pipeline_blob: 2afd3a3d859318e05dcb3e1b2763e4e375b790b6
  published_alias_auditor_blob: f3749474a32761b6671952e815180b4764d0df83
  hydrology_specific_rehearsal_fixture: absent
  hydrology_specific_rehearsal_test: absent
  hydrology_candidate_payloads: 0
  hydrology_proof_payloads: 0
  hydrology_receipt_payloads: 0
  hydrology_published_payloads: 0
  hydrology_rollback_card_instances: 0
  hydrology_release_review_records: 0
  open_pull_requests_touching_target_before_branch: 0
source_lineage:
  - title: KFM_Hydrology_Extended_Pro_PDF_Only_Reference_Report_2026-04-21.pdf
    source_class: PLANNING_LINEAGE
    use: hydrology-first, source-role, temporal, evidence, correction, and rollback framing only
  - title: Track Hazards synthetic rollback CI binding
    source_class: NOTION_COORDINATION_ONLY
    use: distinguish the implemented generic-plus-Hazards synthetic proof from absent Hydrology-specific and operational rollback evidence
  - title: KFM Markdown Update & Modernization Agent v1.0
    source_class: CURRENT_TASK_GUIDANCE
    use: same-path repository-grounded Markdown modernization and focused draft-pull-request delivery
related:
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../doctrine/directory-rules.md
  - ../README.md
  - ../../domains/hydrology/README.md
  - PROMOTION_RUNBOOK.md
  - VALIDATION.md
  - NO_NETWORK_TEST_RUNBOOK.md
  - SOURCE_REFRESH_RUNBOOK.md
  - ROLLBACK.md
  - ../rollback-rehearsal.md
  - ../../../contracts/release/rollback_card.md
  - ../../../schemas/contracts/v1/release/rollback_card.schema.json
  - ../../../fixtures/release/rollback_card/
  - ../../../tools/validators/release/validate_rollback_card.py
  - ../../../tools/release/rollback_apply.py
  - ../../../tests/release/test_synthetic_rollback_rehearsal.py
  - ../../../.github/workflows/rollback-drill.yml
  - ../../../release/rollback_cards/README.md
  - ../../../release/candidates/hydrology/README.md
  - ../../../release/reviews/README.md
  - ../../../data/proofs/hydrology/README.md
  - ../../../data/receipts/hydrology/README.md
  - ../../../data/published/hydrology/README.md
  - ../../../pipelines/rollback/main.py
  - ../../../scripts/maintenance/audit_published_aliases.py
notes:
  - The repository implements a deterministic, marker-protected synthetic rollback and withdrawal rehearsal over isolated temporary roots. It is not Hydrology-specific and is not a production rollback executor.
  - The rollback-drill workflow currently combines eight generic rehearsal tests with four Hazards-specific tests; it does not establish a Hydrology rollback rehearsal.
  - The RollbackCard contract, closed schema, fixtures, validator, and tests establish candidate shape and local consistency only. Every authority and public-mutation flag remains false.
  - The Hydrology candidate, proof, receipt, published-data, rollback-card, and accountable-review lanes contain no Hydrology payload or governed recovery record at the pinned base.
  - The production rollback pipeline and published-alias auditor remain one-line greenfield placeholders.
  - This runbook supports classification, fail-closed planning, bounded synthetic-mechanics validation, and accountable-review handoff. It never executes containment, rollback, withdrawal, correction, invalidation, alias mutation, release, deployment, promotion, or publication.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hydrology Rollback Runbook

> **One-line purpose.** Classify a defective Hydrology release-facing surface, prepare a rollback, withdrawal, hold, error, or forward-correction handoff, and stop before any lifecycle, alias, consumer, release, deployment, promotion, or publication mutation.

[![Operational rollback: held](https://img.shields.io/badge/operational%20rollback-HOLD-b42318?style=flat-square)](#current-disposition)
[![Generic synthetic rehearsal: available](https://img.shields.io/badge/generic%20synthetic%20rehearsal-available-8250df?style=flat-square)](#generic-synthetic-rehearsal)
[![Hydrology rollback proof: absent](https://img.shields.io/badge/Hydrology%20rollback%20proof-absent-b42318?style=flat-square)](#hydrology-specific-rehearsal-gap)
[![Public effect: none](https://img.shields.io/badge/public%20effect-none-6e7781?style=flat-square)](#authority-and-terminal-boundary)

> [!WARNING]
> **KFM Hydrology is not an emergency-alerting, flood-warning, navigation, engineering, insurance, regulatory, or incident-command authority.** Do not use this procedure to issue, replace, delay, retract, summarize as actionable, or interpret a current warning, evacuation instruction, dam-safety direction, regulatory determination, or protective-action message. FEMA NFHL material is regulatory context, not observed inundation. Direct urgent and authoritative decisions to the responsible official source.

<a id="current-disposition"></a>

> [!IMPORTANT]
> **Current disposition: `GENERIC_SYNTHETIC_ROLLBACK_REHEARSAL_AVAILABLE / HYDROLOGY_SPECIFIC_ROLLBACK_PROOF_ABSENT / OPERATIONAL_HYDROLOGY_ROLLBACK_HOLD`.** The repository has a deterministic no-network helper for marker-protected synthetic workspaces and a fixture-first `RollbackCard` validator. The hosted rollback workflow extends that generic profile with a Hazards fixture, not a Hydrology fixture. No Hydrology candidate release, prior safe target, proof, receipt, published payload, rollback card, accountable review record, operational executor, alias auditor, invalidation adapter, or public recovery read-back is established.

```yaml
work_state: HOLD
available_evidence:
  - GENERIC_SYNTHETIC_PLAN_AND_APPLY_REHEARSAL
  - GENERIC_ROLLBACK_AND_WITHDRAWAL_UNIT_TESTS
  - ROLLBACKCARD_CANDIDATE_FIXTURE_VALIDATION
  - BOUNDED_HYDROLOGY_SHAPE_AND_POLARITY_VALIDATION
missing_evidence:
  - HYD_ROLLBACK_CANDIDATE_ABSENT
  - HYD_PRIOR_SAFE_RELEASE_TARGET_ABSENT
  - HYD_ROLLBACKCARD_INSTANCE_ABSENT
  - HYD_REVIEW_RECORD_ABSENT
  - HYD_POLICY_EXECUTION_UNBOUND
  - HYD_SPECIFIC_REHEARSAL_ABSENT
  - HYD_PRODUCTION_EXECUTOR_PLACEHOLDER
  - HYD_ALIAS_AUDITOR_PLACEHOLDER
  - HYD_INVALIDATION_ADAPTERS_ABSENT
  - HYD_PUBLIC_READBACK_ABSENT
lifecycle_effect: none
release_effect: none
deployment_effect: none
promotion_effect: none
publication_effect: none
```

**Quick navigation:** [Goal](#goal-and-scope) · [Authority](#authority-and-terminal-boundary) · [Evidence](#current-repository-evidence) · [Vocabulary](#state-and-vocabulary-separation) · [Safety](#hydrology-safety-and-source-role-boundary) · [Decision](#rollback-decision-model) · [Preconditions](#preconditions) · [Procedure](#rollback-preflight-and-handoff-procedure) · [Defects](#hydrology-defect-and-recovery-matrix) · [Target](#prior-target-safety) · [Invalidation](#invalidation-and-cross-lane-impact) · [Synthetic proof](#generic-synthetic-rehearsal) · [Interpretation](#interpret-the-results) · [Handoff](#accountable-review-handoff-packet) · [Gap](#hydrology-specific-rehearsal-gap) · [Graduation](#operational-graduation-gate) · [Validation](#documentation-validation) · [Related](#related-repository-surfaces) · [Maintenance](#maintenance-and-document-rollback)

---

<a id="goal-and-scope"></a>

## Goal and scope

Use this runbook when a released or release-facing Hydrology carrier may be defective and maintainers need a bounded, inspectable answer to this question:

> Is there enough exact support to prepare a rollback candidate, withdrawal candidate, hold, error record, or forward-correction handoff—and what must remain unchanged until accountable review and operational authority exist?

The intended operational circle is:

```text
defect signal
  -> fail-closed containment request and official-source referral where needed
  -> exact affected-release, artifact, claim, and consumer freeze
  -> rollback / withdrawal / hold / error / forward-correction classification
  -> evidence, source-role, identity, time, rights, sensitivity, policy, and target review
  -> RollbackCard candidate validation where applicable
  -> generic synthetic-mechanics rehearsal
  -> accountable review handoff
  -> separately authorized operational execution
  -> invalidation and public read-back
  -> append-only correction, receipts, proofs, and closure
```

Current repository evidence supports the classification, candidate-validation, generic-rehearsal, and review-handoff parts only. It does not support operational containment, target mutation, invalidation, alias change, or public recovery.

### In scope

- freeze the exact repository revision, affected release reference, artifact digests, public claims, source roles, spatial and temporal scope, and known consumers;
- distinguish rollback, withdrawal, hold, error, and forward correction without translating between them silently;
- preserve Hydrology source-role boundaries, especially observations, regulatory context, hydrographic identity, modeled products, derived context, candidates, and synthetic fixtures;
- require evidence, rights, sensitivity, policy, review, correction, target, invalidation, and public-recovery support appropriate to consequence;
- validate the current fixture-first `RollbackCard` profile;
- run the repository's generic marker-protected synthetic rehearsal as a mechanics check;
- interpret exact-revision results without converting a green check into review, execution, release, deployment, promotion, or publication authority;
- enumerate cross-lane and public-consumer effects for accountable review; and
- preserve the affected and prior release history rather than deleting or rewriting it.

### Out of scope

This runbook does not:

- issue or interpret a current flood warning, watch, evacuation instruction, dam-safety direction, or regulatory determination;
- activate, admit, fetch, alter, or withdraw a live source;
- create a Hydrology release, prior safe target, evidence bundle, proof, receipt, policy decision, review record, rollback card, correction notice, or public carrier;
- authorize direct edits to `data/published/`, a public alias, API route, cache, CDN, tile store, catalog, triplet store, search index, vector index, AI cache, deployment, or downstream derivative;
- execute the one-line production rollback pipeline placeholder;
- treat the generic synthetic helper or the Hazards-specific workflow extension as Hydrology rollback proof;
- treat `docs/runbooks/hydrology/ROLLBACK.md`, which remains a proposal scaffold, as an operational procedure or alternate release authority;
- perform repository revert, database recovery, infrastructure failover, source deactivation, secret rotation, or incident-response command; or
- claim operational recovery, release, deployment, promotion, publication, or public readiness.

[Back to top](#top)

---

<a id="authority-and-terminal-boundary"></a>

## Authority and terminal boundary

Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) and the adopted [Directory Rules v2](../../doctrine/directory-rules.md) place human runbooks under `docs/runbooks/`, semantic meaning under `contracts/`, machine shape under `schemas/`, policy under `policy/`, executable helpers under `tools/`, behavior evidence under `tests/`, lifecycle and trust artifacts under `data/`, and release decisions under `release/`.

This is a same-path modernization of an established file. It creates no new responsibility root, rollback record family, contract home, schema home, policy home, proof home, receipt home, release home, or public path.

| Responsibility | Owning surface | Current bounded role |
|---|---|---|
| Human Hydrology rollback procedure | `docs/runbooks/hydrology/ROLLBACK_RUNBOOK.md` | Explain classification, prerequisites, current capability, stop conditions, and handoff |
| Adjacent Hydrology rollback scaffold | [`ROLLBACK.md`](ROLLBACK.md) | Proposal-era placeholder only; no execution or authority effect |
| Generic synthetic procedure | [`docs/runbooks/rollback-rehearsal.md`](../rollback-rehearsal.md) | Explain the isolated marker-protected rehearsal |
| Generic synthetic mechanics | [`tools/release/rollback_apply.py`](../../../tools/release/rollback_apply.py) | Plan or mutate only a marker-protected synthetic workspace |
| Generic behavior proof | [`tests/release/test_synthetic_rollback_rehearsal.py`](../../../tests/release/test_synthetic_rollback_rehearsal.py) | Exercise eight generic rollback, withdrawal, integrity, and fail-closed cases |
| `RollbackCard` meaning | [`contracts/release/rollback_card.md`](../../../contracts/release/rollback_card.md) | Define a candidate plan and explicit non-authority boundary |
| `RollbackCard` machine shape | [`schemas/contracts/v1/release/rollback_card.schema.json`](../../../schemas/contracts/v1/release/rollback_card.schema.json) | Validate a closed `1.0.0` fixture-first candidate |
| Candidate local consistency | [`tools/validators/release/validate_rollback_card.py`](../../../tools/validators/release/validate_rollback_card.py) | Validate shape and bounded cross-field rules without executing rollback |
| Read-only CI inspection | [`.github/workflows/rollback-drill.yml`](../../../.github/workflows/rollback-drill.yml) | Run the candidate profile plus generic and Hazards synthetic checks while retaining production holds |
| Hydrology release and review inputs | [`release/candidates/hydrology/`](../../../release/candidates/hydrology/README.md) and [`release/reviews/`](../../../release/reviews/README.md) | Guidance only at the pinned base; no Hydrology candidate or review record |
| Hydrology proof, receipt, and published lanes | [`data/proofs/hydrology/`](../../../data/proofs/hydrology/README.md), [`data/receipts/hydrology/`](../../../data/receipts/hydrology/README.md), [`data/published/hydrology/`](../../../data/published/hydrology/README.md) | README and placeholder lanes only; no Hydrology payload |
| Production rollback pipeline | [`pipelines/rollback/main.py`](../../../pipelines/rollback/main.py) | One-line greenfield placeholder |
| Published-alias audit | [`scripts/maintenance/audit_published_aliases.py`](../../../scripts/maintenance/audit_published_aliases.py) | One-line greenfield placeholder |
| Release decisions and records | [`release/`](../../../release/README.md) | Remain separate append-only governed records |
| Public carriers and runtime state | Governed public delivery surfaces | Must not be mutated by this Markdown file or the synthetic helper |

The highest result this procedure can establish is:

```text
READY_FOR_ACCOUNTABLE_ROLLBACK_REVIEW
```

That result is not `APPROVED`, `ROLLBACK_AUTHORIZED`, `ROLLBACK_EXECUTED`, `RECOVERED`, `RELEASED`, `DEPLOYED`, `PROMOTED`, or `PUBLISHED`.

[Back to top](#top)

---

<a id="current-repository-evidence"></a>

## Current repository evidence

The observations below are pinned to `main@8e7c862f5bf91fb27038ef264549b565b4827711`. Re-read the exact surfaces when the helper, tests, workflow, contract, schema, validator, Hydrology lanes, executor, alias tooling, or public consumers change.

| Surface | CONFIRMED repository evidence | Bounded conclusion |
|---|---|---|
| Requested file | The prior v0.1 runbook still claimed the repository was unmounted and named unverified operational commands and paths | Proposal-era operational claims required replacement, not cosmetic editing |
| Generic helper | `rollback_apply.py` requires `.kfm-synthetic-rollback-rehearsal`, exact marker text, `synthetic: true`, safe relative paths, a current synthetic alias, matching manifest and artifact digests, a distinct target for rollback, and the complete invalidation vocabulary | Deterministic no-write `PLAN` and marker-protected synthetic `APPLY` exist; no real public state is touched |
| Generic tests | Eight tests cover deterministic no-write plan, rollback apply, withdrawal apply, non-synthetic denial, incomplete invalidation denial, missing target, digest mismatch, and missing marker | Generic synthetic behavior is executable and fail-closed within the tested profile |
| Rollback workflow | `rollback-drill` is read-only, receives no release or signing secret, and is configured to run the RollbackCard fixture profile plus eight generic and four Hazards tests, asserting twelve non-vacuous tests | A green workflow proves the configured candidate and synthetic profiles only; Hydrology-specific proof is absent |
| RollbackCard profile | The v1.0 contract, closed `1.0.0` schema, three valid fixtures, six invalid fixtures, expected-findings manifest, validator, tests, and workflow integration exist | A passing candidate proves shape and local consistency only |
| RollbackCard authority flags | Candidate validation requires authority creation, policy evaluation, completed review, rollback execution, and public mutation to remain false, with `release_ref` null | The candidate profile deliberately cannot represent an authorized or executed rollback |
| Hydrology-specific rehearsal | No `fixtures/domains/hydrology/synthetic_rollback_rehearsal/` or `tests/domains/hydrology/test_synthetic_rollback_rehearsal.py` is established in the inspected tree | Generic or Hazards proof must not be relabeled as Hydrology proof |
| Hydrology candidate lane | `release/candidates/hydrology/` contains its README only | No affected or target Hydrology candidate dossier is established |
| Hydrology release reviews | `release/reviews/` contains guidance and an Atmosphere lane, but no Hydrology review record | Accountable Hydrology rollback review is absent |
| Hydrology proof lane | `data/proofs/hydrology/` contains `.gitkeep` and README only | No Hydrology rollback or release proof instance is established |
| Hydrology receipt lane | `data/receipts/hydrology/` contains `.gitkeep` and README only | No Hydrology rollback or release receipt instance is established |
| Hydrology published lane | `data/published/hydrology/` contains `.gitkeep` and README only | No repository-carried Hydrology public payload or alias target is established |
| Rollback-card records | `release/rollback_cards/` has guidance, two non-Hydrology placeholder JSON files, and other domain directories; no Hydrology card instance is present | No Hydrology recovery candidate or accepted record exists |
| Production pipeline | `pipelines/rollback/main.py` is exactly a one-line greenfield placeholder | No accepted production rollback engine exists |
| Alias auditor | `scripts/maintenance/audit_published_aliases.py` is exactly a one-line greenfield placeholder | No accepted live alias inventory, audit, or mutation exists |
| GitHub review route | CODEOWNERS routes the repository to `@bartytime4life` and explicitly denies that routing is stewardship, approval, release authority, or proof of review | Accountable functional roles and separation of duties remain `NEEDS VERIFICATION` |
| Open overlap | No open pull request touching the target path was returned before the task branch was created | This same-path documentation slice had no detected PR overlap at the authority freeze |

### Evidence interpretation

The current repository has more than a proposal: generic synthetic mechanics and candidate validation are implemented. It has less than operational rollback: Hydrology-specific evidence, accountable review, policy execution, target selection, public mutation, invalidation, and read-back are absent or held.

Do not collapse these statements:

```text
GENERIC SYNTHETIC MECHANICS: IMPLEMENTED
ROLLBACKCARD CANDIDATE VALIDATION: IMPLEMENTED / NON-EXECUTING
HAZARDS SYNTHETIC EXTENSION: IMPLEMENTED
HYDROLOGY-SPECIFIC REHEARSAL: ABSENT
OPERATIONAL HYDROLOGY ROLLBACK: HOLD
PUBLIC RECOVERY: NOT ESTABLISHED
```

[Back to top](#top)

---

<a id="state-and-vocabulary-separation"></a>

## State and vocabulary separation

Rollback decisions become unsafe when different state machines are translated by assumption.

| Vocabulary | Examples | Question answered | Must not imply |
|---|---|---|---|
| Defect signal | evidence contradiction, rights change, validation failure, source withdrawal, policy failure | Why was recovery evaluation opened? | That rollback is the correct remedy |
| `RollbackCard.disposition` | `ROLLBACK_CANDIDATE`, `WITHDRAWAL_CANDIDATE`, `HOLD`, `ERROR` | What candidate recovery posture is being proposed? | Review, execution, or public mutation |
| Runtime or policy outcome | `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`; `HOLD` where the owning policy uses it | What may a consumer return or do? | A release-recovery disposition |
| Review state | unreviewed, review-ready, reviewed within an accepted profile | Has accountable review occurred? | Execution authority unless the governing profile says so |
| Synthetic execution state | `PLAN`, marker-protected synthetic `APPLY` | What happened inside an isolated rehearsal root? | A real alias or public carrier changed |
| Operational execution state | planned, authorized, applying, verified, failed, held | What happened in an accepted recovery executor? | Anything today; this executor is not established |
| Public recovery state | active, stale, withdrawn, superseded, corrected, recovered | What can governed public consumers observe? | That repository state alone proves public parity |

### Forward correction is separate

`FORWARD_CORRECTION` is not a current `RollbackCard.disposition`. A corrected artifact should travel through the accepted candidate, validation, policy, review, promotion, release, correction, and publication path. This runbook may recommend that route, but it must not encode it as a schema value the current contract does not define.

[Back to top](#top)

---

<a id="hydrology-safety-and-source-role-boundary"></a>

## Hydrology safety and source-role boundary

Rollback must preserve what each source can support. A prior release is unsafe when it restores a collapsed source role even if every byte digest matches.

| Source or product family | Hydrology role | Prohibited upgrade during recovery |
|---|---|---|
| WBD / HUC units | Watershed and hydrologic-unit identity and boundary context | Flood prediction, observed inundation, or emergency status |
| NHDPlus HR and related hydrography | Hydrographic identity, network, and crosswalk context | Regulatory flood determination or current flow observation |
| USGS Water observations | Time-bounded gauge or water observations with unit, qualifier, provisional/final, and retrieval context | Forecast, warning, or timeless condition |
| FEMA NFHL | Regulatory flood-hazard context | Observed inundation, current flood, forecast, warning, engineering conclusion, or insurance determination by KFM |
| 3DEP or terrain-derived products | Terrain source or derived hydrologic context | Gauge observation, regulatory source, or hydraulic-model result |
| Modeled hydrograph or derivative | Model or derived result with model/run support | Observation or official operational guidance |
| Synthetic fixture | Test input for bounded validation | Real-world condition, admitted source, released artifact, or public evidence |

> [!CAUTION]
> A target that predates current source-role controls is not automatically safe. If its role, time, evidence, rights, sensitivity, or representation posture cannot be revalidated, choose `WITHDRAWAL_CANDIDATE` or `HOLD` rather than restoring it.

[Back to top](#top)

---

<a id="rollback-decision-model"></a>

## Rollback decision model

Classify the recovery posture before preparing a candidate. Do not start from a desired target and reverse-engineer support.

| Condition | Candidate posture | Required reason |
|---|---|---|
| A distinct prior release is identified and revalidates as safer for the exact affected scope | `ROLLBACK_CANDIDATE` | Restore a verified predecessor through separately authorized execution |
| No distinct safe predecessor exists, including a defective first release | `WITHDRAWAL_CANDIDATE` | Remove current public use without inventing a target |
| Evidence, rights, sensitivity, policy, identity, review, target, invalidation, or public-readback support is incomplete | `HOLD` | Preserve current fail-closed containment and obtain missing support |
| The recovery input or evaluation is malformed or cannot be completed safely | `ERROR` | Record the failure without public mutation |
| The defect should be repaired in a new release rather than restoring old state | Forward-correction handoff | Use the normal governed correction and release path; not a RollbackCard disposition |

### Trigger reason codes

Use the finite `RollbackCard` trigger vocabulary when a card is prepared:

`RELEASE_DEFECT`, `EVIDENCE_CONTRADICTION`, `RIGHTS_CHANGE`, `SENSITIVITY_DISCOVERY`, `VALIDATION_FAILURE`, `SOURCE_WITHDRAWAL`, `POLICY_FAILURE`, `SECURITY_ISSUE`, `OPERATIONAL_FAILURE`, `EMERGENCY_HOLD`, `INSUFFICIENT_EVIDENCE`, or `INPUT_INVALID`.

The reason code is public-safe classification. Do not put secrets, private review text, protected locations, exploit detail, or sensitive infrastructure information into it.

[Back to top](#top)

---

<a id="preconditions"></a>

## Preconditions

### Planning and review-handoff preconditions

All items below are required before describing a packet as `READY_FOR_ACCOUNTABLE_ROLLBACK_REVIEW`:

- [ ] The exact 40-character repository SHA and affected-release reference are recorded.
- [ ] The affected artifact set, digests, claims, EvidenceRefs, source roles, geography, time interval, audience, and public consumers are bounded.
- [ ] The defect and trigger reason are classified without exposing sensitive values.
- [ ] The candidate disposition matches the current RollbackCard vocabulary or is explicitly a separate forward-correction recommendation.
- [ ] A rollback candidate names a distinct target; a withdrawal candidate has no target.
- [ ] Every consequential claim has resolvable evidence support or is marked unsupported.
- [ ] Rights, sensitivity, precision, source terms, and cross-lane reconstruction risks are reviewed.
- [ ] A target release is revalidated rather than assumed safe because it is older.
- [ ] Required invalidation classes and known consumer instances are enumerated.
- [ ] A correction or notice reference is supplied when public notice is required.
- [ ] The RollbackCard candidate passes its current fixture-first shape and local-consistency profile.
- [ ] Generic synthetic rehearsal evidence is labeled generic and synthetic, not Hydrology-specific or operational.
- [ ] Accountable reviewer roles, authority, separation, obligations, validity, and supersession state are named as established or missing.
- [ ] All missing support remains an explicit `HOLD`, `ERROR`, withdrawal posture, or open obligation.

### Operational preconditions

Current repository evidence does not satisfy these conditions. They are non-compensable before any real mutation:

- an accepted operational rollback plan/apply executor;
- authenticated authorization and separation of duties;
- accepted policy evaluation bound to the exact affected and target releases;
- evidence, proof, receipt, correction, and release-record resolution;
- an accepted public alias or equivalent target model;
- safe, idempotent consumer invalidation adapters;
- partial-failure detection and resumable or compensating behavior;
- deployment/environment identity and least-privilege credentials;
- exact public read-back and stale-leak detection; and
- a rehearsed Hydrology-specific synthetic profile before any non-public operational exercise.

Missing an operational precondition is a stop. Do not substitute repository file edits, manual cache clearing, or a green generic test.

[Back to top](#top)

---

<a id="rollback-preflight-and-handoff-procedure"></a>

## Rollback preflight and handoff procedure

### 1. Freeze identity and active work

Record:

- current `main` and task or incident SHA;
- affected release and artifact references;
- current public carrier or alias identity, when one exists;
- exact source, evidence, policy, review, correction, and release references;
- active pull requests, incidents, migrations, and recovery work touching the same surface;
- known public and internal consumers; and
- the person or system that detected the defect without treating detection as approval.

Stop on unresolved overlap, unknown affected identity, or an inability to bound the exposed surface.

### 2. Classify the Hydrology defect

Use the [Hydrology defect and recovery matrix](#hydrology-defect-and-recovery-matrix). A defect may have several classes. Preserve all material classes and apply the strictest rights, sensitivity, evidence, source-role, and public-safety posture.

### 3. Select a candidate disposition

Apply the [rollback decision model](#rollback-decision-model). Record why rollback is safer than withdrawal or forward correction. When the evidence does not support that comparison, use `HOLD`.

### 4. Revalidate a proposed prior target

Use [prior target safety](#prior-target-safety). A digest-valid predecessor can still be unsafe because its evidence, policy, source role, rights, sensitivity, time, schema, consumer compatibility, or correction state is stale.

### 5. Build a review packet—not a public mutation

Prepare stable references to:

- the affected release and exact artifact set;
- the target release or withdrawal posture;
- defect evidence and limitations;
- source descriptors and source roles;
- evidence, policy, review, correction, proof, receipt, manifest, and lineage records;
- invalidation classes and known consumer instances;
- target validation and public-readback plan;
- cross-lane impacts; and
- every unresolved blocker.

Do not copy governed payloads into this runbook or a pull-request body.

### 6. Validate the RollbackCard candidate profile

Repository-native candidate checks are:

```bash
python tools/validators/release/validate_rollback_card.py --fixtures

python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_rollback_card.py' \
  --verbose
```

A pass establishes the fixture matrix and bounded candidate semantics at the tested SHA. It does not resolve a Hydrology release, authenticate review, execute policy, select a target, mutate an alias, invalidate a consumer, issue a correction, or recover public state.

### 7. Run the generic synthetic rehearsal

Use the [generic synthetic rehearsal](#generic-synthetic-rehearsal) to check common mechanics. Keep the Hydrology-specific gap visible.

### 8. Interpret finite results

Use [interpret the results](#interpret-the-results). Record skipped, unavailable, inherited, introduced, non-comparable, and pending evidence separately.

### 9. Prepare accountable-review handoff

Use the [handoff packet](#accountable-review-handoff-packet). The handoff must ask for a decision; it must not say a decision already occurred.

### 10. Stop before mutation

Do not invoke `pipelines/rollback/main.py`; it is a placeholder. Do not invoke `audit_published_aliases.py`; it is a placeholder. Do not edit a real published lane, alias, cache, catalog, API route, search index, vector index, AI cache, deployment, or downstream derivative under this procedure.

[Back to top](#top)

---

<a id="hydrology-defect-and-recovery-matrix"></a>

## Hydrology defect and recovery matrix

| Defect class | Hydrology example | Candidate posture | Mandatory stop condition |
|---|---|---|---|
| Evidence contradiction or gap | Gauge, HUC, reach, or regulatory claim no longer resolves to admissible evidence | `HOLD`, withdrawal, or rollback to a revalidated target | No resolvable EvidenceBundle for the public claim |
| Source-role collapse | NFHL represented as observed inundation; modeled hydrograph represented as observation | Withdrawal or rollback only to a target that preserves the correct role | Proposed target repeats or obscures the collapse |
| Identity ambiguity | COMID, permanent identifier, HUC, gauge, or waterbody relation is split, merged, retired, or unresolved | `HOLD`, `ABSTAIN`, or rollback to an unambiguous target | Identity was inferred from name or geometry proximity alone |
| Temporal defect | Provisional reading shown as final; observed, valid, source, retrieval, release, or correction times collapsed | Mark affected claims stale; choose withdrawal, rollback, or forward correction | Target cannot preserve distinct material time kinds |
| Unit, datum, qualifier, or no-data defect | Flow, stage, water quality, or groundwater value changed meaning through normalization | Withdrawal, rollback, or forward correction after validation | Conversion or datum support cannot be reproduced |
| Geometry or topology defect | HUC hierarchy mismatch, invalid geometry, network break, or version-crosswalk error | Rollback to a digest-pinned, revalidated target or withdraw | Target geometry, CRS, topology, or source vintage is unverified |
| Rights or source withdrawal | Redistribution, attribution, access, or source terms no longer permit the released carrier | `WITHDRAWAL_CANDIDATE` or policy-directed `HOLD` | Rights remain unknown or inherited by assumption |
| Sensitivity or harmful precision | Hydrology join exposes private-property, infrastructure, archaeology, cultural, or other restricted detail | Immediate fail-closed escalation plus withdrawal/generalization handoff | Exact sensitive values would remain reconstructable |
| Policy failure | Accepted policy would deny current use or obligations cannot be enforced | `HOLD`, withdrawal, or rollback to a target that passes current policy | Policy result is a fixture declaration rather than accepted evaluation |
| Catalog or citation defect | Public carrier cannot resolve catalog, provenance, EvidenceRef, or correction lineage | `ABSTAIN`, withdrawal, rollback, or forward correction | Public claim would remain uncitable or misleading |
| Consumer drift | API, map, Evidence Drawer, export, search, graph, or AI surface retains the affected claim after release state changes | `HOLD` until invalidation and read-back are complete | Any known consumer cannot be enumerated or verified |
| Security or operational failure | Integrity, tenant, credential, storage, or delivery failure affects release trust | Security/operations escalation; RollbackCard candidate only when appropriate | This runbook would expose secrets or replace incident response |

[Back to top](#top)

---

<a id="prior-target-safety"></a>

## Prior target safety

A prior release is not safe merely because it existed before the defect.

For `ROLLBACK_CANDIDATE`, reviewers must establish all of the following for the exact affected scope:

| Target check | Required evidence | Failure posture |
|---|---|---|
| Distinct identity | Target release differs from the affected release and uses stable immutable identity | `ERROR` or `HOLD` |
| Manifest and artifact integrity | Target manifest and every referenced artifact digest match | `HOLD`; investigate integrity drift |
| Evidence resolution | Consequential target claims resolve to admissible EvidenceBundles | Choose an earlier target, withdraw, or hold |
| Source-role safety | Observation, regulatory, modeled, derived, contextual, and synthetic roles remain separate | Withdrawal or hold |
| Spatial and temporal validity | CRS, geometry, identity, source vintage, observed/valid/retrieval/release time, freshness, and qualifiers remain valid | Withdrawal, earlier target, or forward correction |
| Rights and sensitivity | Current rights, attribution, access, precision, and sensitivity policy permit the target use | `DENY` or `HOLD` through the owning policy |
| Review and policy | Accepted review and policy records apply to the target and intended audience | `HOLD` |
| Consumer compatibility | Governed APIs, maps, Evidence Drawer, exports, search, graph, AI, and downstream derivatives can consume the target safely | `HOLD` |
| Correction lineage | Target restoration does not erase the affected release, defect, correction, withdrawal, or supersession record | `HOLD` |
| Public read-back | A plan exists to prove every exposed consumer reflects the intended recovered state | `HOLD` |

A first Hydrology release has no predecessor by definition. Its recovery posture is withdrawal, hold, or forward correction—not an invented rollback target.

[Back to top](#top)

---

<a id="invalidation-and-cross-lane-impact"></a>

## Invalidation and cross-lane impact

The generic synthetic helper requires this complete invalidation vocabulary:

| Invalidation class | Hydrology-facing examples | Current operational status |
|---|---|---|
| `API_CACHE` | Governed Hydrology response cache | Adapter and public mutation not established |
| `CDN` | Public tile, raster, document, or static-carrier edge cache | Adapter and credentials not established |
| `TILES` | PMTiles, MVT, raster, or terrain carriers | No Hydrology published payload established |
| `CATALOG` | STAC, DCAT, PROV, citation, or release catalog projections | Operational invalidation not established |
| `TRIPLETS` | Hydrology graph/triplet projections | Operational invalidation not established |
| `SEARCH_INDEX` | Feature, source, evidence, or catalog search | Operational invalidation not established |
| `VECTOR_INDEX` | Retrieval or similarity derivatives | Operational invalidation not established |
| `AI_CACHE` | Focus Mode or explanation cache | Operational invalidation not established |
| `DOWNSTREAM_DERIVATIVES` | Joined maps, exports, dashboards, analyses, screenshots, or reports | Consumer inventory and fanout not established |

The vocabulary proves that a rehearsal scenario names every class. It does not prove that any live adapter was called.

### Cross-lane review inventory

A Hydrology defect can affect other responsibility lanes without transferring recovery authority to Hydrology:

| Lane | Typical dependency | Hydrology handoff obligation |
|---|---|---|
| Hazards | Flood, drought, exposure, warning, or resilience context | Name affected claims and references; Hazards owns its recovery decision |
| Soil | Soil-moisture, drainage, hydrologic group, wetness, or erosion context | Name joined carriers and stale-state risk |
| Agriculture | Irrigation, crop-water, drought-stress, reservoir, or groundwater context | Name affected observations, models, and public summaries |
| Settlements / Infrastructure | Floodplain, bridge, dam, utility, water-supply, or service-area context | Escalate sensitivity and harmful-precision review |
| Habitat / Fauna / Flora | Aquatic habitat, wetland, riparian, occurrence, or restoration context | Preserve source ownership and sensitivity obligations |
| Geology | Aquifer and hydrostratigraphic context | Preserve Geology-owned context and Hydrology-owned observation boundaries |

Do not auto-mutate a sibling lane. Record the dependency, evidence intersection, requested action, owner, and unresolved state for its accountable steward.

[Back to top](#top)

---

<a id="generic-synthetic-rehearsal"></a>

## Generic synthetic rehearsal

The repository's current executable rollback proof is deliberately generic and synthetic.

### What it proves

The generic helper and eight tests demonstrate, inside isolated temporary roots, that the current profile can:

- produce deterministic no-write plans;
- switch a synthetic current alias to a distinct prior synthetic release;
- withdraw a synthetic current alias without selecting a target;
- preserve the affected synthetic manifest and artifact bytes;
- write append-only synthetic correction and invalidation records;
- require every declared invalidation class;
- deny non-synthetic scenarios;
- deny missing markers, missing targets, unsafe paths, and digest mismatches; and
- keep every authority and public-mutation flag false.

### Repository-native command

```bash
python -m unittest -q tests.release.test_synthetic_rollback_rehearsal
```

### CLI boundary

The CLI defaults to a no-write plan and requires a caller-created marker-protected synthetic root:

```bash
python tools/release/rollback_apply.py \
  --workspace /tmp/kfm-rehearsal \
  --scenario /tmp/kfm-rehearsal/scenario.json
```

`--apply` still changes only that synthetic workspace. Never point the helper at a repository lifecycle lane, deployment mount, production store, public alias, cache, or real release directory.

### Workflow boundary

The current `rollback-drill` workflow is configured to run:

- the release RollbackCard candidate fixture profile;
- eight generic synthetic rehearsal tests; and
- four Hazards-specific synthetic rehearsal tests.

Its expected twelve-test result is **generic plus Hazards**, not generic plus Hydrology. A passing workflow must not be cited as Hydrology-specific rollback proof.

[Back to top](#top)

---

<a id="interpret-the-results"></a>

## Interpret the results

| Observed result | Truthful interpretation | Prohibited interpretation |
|---|---|---|
| RollbackCard fixture validator passes | Current valid/invalid candidate matrix and bounded local consistency passed at the tested SHA | A Hydrology card exists, references resolve, or rollback is approved |
| Generic eight-test suite passes | Marker-protected synthetic rollback and withdrawal mechanics passed | Hydrology behavior or production recovery passed |
| `rollback-drill` passes | Candidate validation plus generic and Hazards synthetic checks passed; production holds remained visible | Hydrology rollback, target mutation, or public recovery passed |
| Hydrology bounded validation passes | Named Hydrology fixture shape and polarity checks passed | The affected or target release is scientifically, legally, or operationally safe |
| Candidate support is missing but not contradictory | `HOLD` or withdrawal posture, depending on consequence | Infer a prior safe target |
| Policy denies the intended target or audience | Preserve policy `DENY`; candidate cannot advance | Translate `DENY` into a softer rollback recommendation |
| Input is malformed or evaluation cannot finish safely | `ERROR`; no mutation | Retry through manual file edits that bypass validation |
| Exact base and head cannot be compared | `NEEDS VERIFICATION` or `UNRESOLVED / NON-COMPARABLE` | Label the result inherited or introduced without proof |
| Hosted check is skipped | `SKIPPED`, with reason when known | `PASS` |
| Check did not run | `NOT RUN` | `PASS`, `FAIL`, or proof of absence |

Every validation result is revision-bound. Record the exact SHA, command or workflow, fixture inventory, result, and skipped or unavailable checks.

[Back to top](#top)

---

<a id="accountable-review-handoff-packet"></a>

## Accountable review handoff packet

The following YAML is an **illustrative documentation handoff**, not a `RollbackCard`, `ReviewRecord`, `PolicyDecision`, `CorrectionNotice`, release record, or execution instruction.

```yaml
handoff_type: HYDROLOGY_ROLLBACK_REVIEW
repository:
  base_sha: <40-character SHA>
  evaluated_sha: <40-character SHA>
  active_overlaps: []
affected:
  release_ref: <stable release ref or ABSENT>
  artifact_refs: []
  artifact_digests: []
  public_claim_refs: []
  current_public_state: <known state or UNKNOWN>
defect:
  trigger_reason_code: <RollbackCard reason code>
  classes: []
  detected_at: <timezone-aware time>
  evidence_refs: []
  sensitive_details_withheld: true
scope:
  geography: <bounded extent>
  object_families: []
  source_roles: []
  time_interval: <explicit interval>
  audience: <declared audience>
  consumers: []
recovery_candidate:
  disposition: ROLLBACK_CANDIDATE | WITHDRAWAL_CANDIDATE | HOLD | ERROR | FORWARD_CORRECTION_HANDOFF
  target_release_ref: <distinct ref or null>
  correction_notice_ref: <ref or null>
  reason: <public-safe explanation>
target_revalidation:
  manifest_integrity: <result>
  artifact_integrity: <result>
  evidence_resolution: <result>
  source_role: <result>
  spatial_temporal: <result>
  rights_sensitivity: <result>
  policy_review: <result>
  consumer_compatibility: <result>
invalidations:
  classes:
    - API_CACHE
    - CDN
    - TILES
    - CATALOG
    - TRIPLETS
    - SEARCH_INDEX
    - VECTOR_INDEX
    - AI_CACHE
    - DOWNSTREAM_DERIVATIVES
  concrete_consumers: []
  unowned_consumers: []
validation:
  rollback_card_candidate: <PASS | FAIL | ERROR | NOT RUN>
  generic_synthetic_rehearsal: <PASS | FAIL | NOT RUN>
  hydrology_specific_rehearsal: ABSENT
  hydrology_domain_checks: []
  tested_sha: <40-character SHA>
  skipped_or_unavailable: []
review:
  required_roles: []
  authenticated_records: []
  separation_of_duties: <confirmed | not confirmed>
  open_obligations: []
public_recovery:
  containment_authority: <ref or NEEDS VERIFICATION>
  execution_authority: <ref or NEEDS VERIFICATION>
  invalidation_plan: <ref or NEEDS VERIFICATION>
  readback_plan: <ref or NEEDS VERIFICATION>
result:
  review_readiness: READY_FOR_ACCOUNTABLE_ROLLBACK_REVIEW | BLOCKED
  reason_codes: []
non_effects:
  source_activated: false
  lifecycle_mutated: false
  rollback_card_accepted: false
  rollback_executed: false
  public_state_mutated: false
  release_executed: false
  deployment_executed: false
  promotion_executed: false
  publication_executed: false
```

### Minimum reviewer questions

1. Does the affected release exist, and are its artifacts, claims, and consumers bounded exactly?
2. Is the defect supported by evidence rather than inference, generated prose, or map appearance?
3. Are source roles, identity, spatial scope, time, units, datum, qualifiers, uncertainty, rights, sensitivity, and representation limits explicit?
4. Is rollback safer than withdrawal and forward correction for the exact exposed scope?
5. Does a distinct target revalidate under current evidence, policy, rights, sensitivity, schema, and consumer requirements?
6. Does the candidate card use the current contract vocabulary without claiming authority or execution?
7. Are reviewer identity, authority, scope, separation, obligations, validity, and supersession state authenticated?
8. Can every required consumer be invalidated idempotently, and can public read-back detect stale leaks?
9. Are sibling-lane dependencies named without mutating their state or assuming their decisions?
10. Is the requested result still only review, with operational authorization and execution separate?

[Back to top](#top)

---

<a id="hydrology-specific-rehearsal-gap"></a>

## Hydrology-specific rehearsal gap

No checked-in Hydrology synthetic rollback workspace, scenario, or domain test extends the generic helper at the pinned base. This is a material gap, not a reason to weaken the generic guard.

### Smallest dependency-closed follow-up

A future implementation slice should add one non-locating, unreleased, unpublished, no-network Hydrology rehearsal that reuses the generic helper rather than creating a second rollback engine. It should remain under the existing fixture and test responsibility roots and should not create a Hydrology release record.

Minimum negative and positive behavior should include:

1. deterministic no-write planning over a synthetic Hydrology release pair;
2. marker-protected synthetic alias restoration with affected history retained;
3. withdrawal when no distinct safe predecessor is declared;
4. denial when NFHL regulatory context is relabeled as observed inundation or warning support;
5. denial when provisional/final, observation/model, or source-role state is collapsed;
6. denial when HUC, reach, gauge, or crosswalk identity is ambiguous or the target equals the affected release;
7. denial on artifact or manifest tampering;
8. complete invalidation vocabulary and public-mutation flags remaining false; and
9. workflow recognition that cannot pass with zero tests.

The follow-up would prove a bounded Hydrology synthetic profile only. Production target selection, policy, review, signing, invalidation, alias mutation, deployment, and public recovery would remain separate.

[Back to top](#top)

---

<a id="operational-graduation-gate"></a>

## Operational graduation gate

Operational Hydrology rollback remains `HOLD` until current evidence demonstrates all of the following together:

1. one exact affected Hydrology release and immutable artifact/claim inventory;
2. one distinct target that revalidates as safe, or an accepted withdrawal posture when no target exists;
3. EvidenceRef-to-EvidenceBundle, proof, receipt, manifest, catalog, and correction closure;
4. accepted source-role, identity, spatial, temporal, unit, datum, qualifier, uncertainty, and representation controls;
5. current rights, sensitivity, precision, attribution, and source-term clearance;
6. an accepted active policy bundle/evaluator with enforceable obligations;
7. authenticated accountable review, authority intervals, separation of duties, and revocation/supersession handling;
8. accepted RollbackCard, CorrectionNotice, ReviewRecord, release-record, and execution-receipt profiles;
9. an accepted plan/apply executor with least privilege, idempotency, concurrency control, resumability, partial-failure handling, and no-history-erasure tests;
10. an accepted public alias or equivalent release-state model plus audit tooling;
11. real API, CDN, tile, catalog, triplet, search, vector, AI, and downstream invalidation adapters;
12. a Hydrology-specific no-network rehearsal and approved non-public operational exercise;
13. deployment/environment identity, secrets custody, monitoring, logs, alerting, and rollback-of-rollback posture;
14. exact public read-back proving every governed consumer reflects the intended state and correction lineage; and
15. a documented reversal or forward-recovery path that preserves affected history.

No weighted score, deadline, green generic test, schema pass, pull request, merge, signature alone, or operator confidence may compensate for a failed trust or safety gate.

[Back to top](#top)

---

<a id="documentation-validation"></a>

## Documentation validation

### Focused repository checks

```bash
python tools/validators/docs/link-check/check_links.py \
  --repo-root . \
  --format text \
  docs/runbooks/hydrology/ROLLBACK_RUNBOOK.md

python tools/validators/release/validate_rollback_card.py --fixtures

python -m unittest -q tests.release.test_synthetic_rollback_rehearsal
```

Run the repository's hosted Markdown, documentation graph, metadata, rollback-drill, Hydrology, contract, schema, policy, security, and topology checks when this file changes. Classify each result at the exact tested SHA.

### Documentation acceptance criteria

This runbook is ready for accountable documentation review only when:

- the proposal-era unmounted-repository posture and invented operational commands are removed;
- current generic synthetic mechanics, RollbackCard profile, workflow composition, and production holds are stated accurately;
- absence of a Hydrology-specific rehearsal, candidate, target, proof, receipt, card, review, published payload, executor, auditor, invalidation path, and read-back is explicit;
- RollbackCard, policy/runtime, review, synthetic execution, operational execution, and public recovery vocabularies remain separate;
- NFHL, observation, model, hydrography, terrain-derived, and synthetic roles cannot be collapsed by the procedure;
- rollback, withdrawal, hold, error, and forward correction have distinct meanings;
- no command can touch a real public or lifecycle surface;
- all relative links and stable anchors resolve;
- no sensitive locations, secrets, private review text, or rights-unclear payloads are included; and
- rollback of this Markdown is documented without implying reversal of operational state.

[Back to top](#top)

---

<a id="related-repository-surfaces"></a>

## Related repository surfaces

### Hydrology procedures and boundaries

- [Parent runbook index](../README.md)
- [Hydrology domain boundary](../../domains/hydrology/README.md)
- [Hydrology promotion preflight](PROMOTION_RUNBOOK.md)
- [Hydrology bounded validation](VALIDATION.md)
- [Hydrology no-network procedure](NO_NETWORK_TEST_RUNBOOK.md)
- [Hydrology source-refresh procedure](SOURCE_REFRESH_RUNBOOK.md)
- [Adjacent Hydrology rollback scaffold](ROLLBACK.md)

### Generic rollback contracts, mechanics, and checks

- [Generic synthetic rollback rehearsal](../rollback-rehearsal.md)
- [RollbackCard contract](../../../contracts/release/rollback_card.md)
- [RollbackCard schema](../../../schemas/contracts/v1/release/rollback_card.schema.json)
- [RollbackCard fixtures](../../../fixtures/release/rollback_card/)
- [RollbackCard validator](../../../tools/validators/release/validate_rollback_card.py)
- [Synthetic rollback helper](../../../tools/release/rollback_apply.py)
- [Generic synthetic rehearsal tests](../../../tests/release/test_synthetic_rollback_rehearsal.py)
- [Rollback-drill workflow](../../../.github/workflows/rollback-drill.yml)

### Release and Hydrology trust-artifact lanes

- [Release governance root](../../../release/README.md)
- [Rollback-card lane](../../../release/rollback_cards/README.md)
- [Hydrology candidate lane](../../../release/candidates/hydrology/README.md)
- [Release review lane](../../../release/reviews/README.md)
- [Hydrology proof lane](../../../data/proofs/hydrology/README.md)
- [Hydrology receipt lane](../../../data/receipts/hydrology/README.md)
- [Hydrology published lane](../../../data/published/hydrology/README.md)

### Explicit held surfaces

- [Production rollback pipeline placeholder](../../../pipelines/rollback/main.py)
- [Published-alias auditor placeholder](../../../scripts/maintenance/audit_published_aliases.py)

### Placement authority

- [Directory Rules v2](../../doctrine/directory-rules.md)
- [ADR-0029 — adopt Directory Governance Standard v2](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)

[Back to top](#top)

---

<a id="maintenance-and-document-rollback"></a>

## Maintenance and document rollback

Update this runbook when:

- a Hydrology rollback rehearsal fixture or domain test is added, removed, or changed;
- the generic helper, marker, scenario contract, invalidation vocabulary, test inventory, or workflow composition changes;
- the RollbackCard contract, schema, fixture matrix, validator, or finite vocabulary changes;
- a Hydrology candidate, prior target, proof, receipt, rollback card, correction notice, review record, release record, published carrier, or public alias appears;
- accepted policy, reviewer authority, separation of duties, execution, invalidation, deployment, monitoring, or public-readback evidence changes;
- the production pipeline or alias auditor stops being a placeholder;
- a real correction, withdrawal, rollback, incident, or rehearsal exposes a procedural gap;
- the adjacent `ROLLBACK.md` scaffold is retired, redirected, or assigned a distinct responsibility; or
- Directory Rules, accepted ADRs, contracts, or release architecture change this file's responsibility.

This is a documentation-only change. Before merge, close the draft pull request and discard only its task branch. After an authorized merge, revert the focused documentation commit or submit a smaller reviewed forward correction. The prior blob `6c6f06f87de2b2b0e528e670ef43ae46bbc17d06` restores the proposal-era document, but reverting this Markdown never reverses a source admission, lifecycle transition, release, correction, withdrawal, rollback, deployment, promotion, publication, alias, cache, public carrier, or operational state.

[Back to top](#top)
