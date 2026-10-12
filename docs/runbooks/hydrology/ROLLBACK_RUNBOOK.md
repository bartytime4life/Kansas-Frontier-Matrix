<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbook-hydrology-rollback
title: Hydrology Rollback Runbook
type: operational-runbook
version: v2.0.2
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
  target_original_blob: 6c6f06f87de2b2b0e528e670ef43ae46bbc17d06
  immediate_prior_blob: e778fd09e352d5510b5a80a332c670a73f2fa401
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
review_corrections:
  - finding: synthetic correction and invalidation records were incorrectly described as append-only
    disposition: replacement-on-collision behavior is explicit; collision-safe persistence remains a graduation requirement
  - finding: the optional report path was omitted from the helper write boundary
    disposition: plan/apply and report writes are separated; caller-controlled report paths are explicit and held
  - finding: fixture validation did not validate a newly prepared candidate card
    disposition: the procedure now requires both fixture-matrix validation and validation of the actual candidate file
  - finding: unmerged abandonment guidance was phrased as a prerequisite to merge
    disposition: abandonment and authorized merge/revert paths are now distinct
source_lineage:
  - title: KFM_Hydrology_Extended_Pro_PDF_Only_Reference_Report_2026-04-21.pdf
    source_class: PLANNING_LINEAGE
    use: hydrology-first, source-role, temporal, evidence, correction, and rollback framing only
  - title: Track Hazards synthetic rollback CI binding
    source_class: NOTION_COORDINATION_ONLY
    use: distinguish generic-plus-Hazards synthetic proof from absent Hydrology-specific and operational rollback evidence
  - title: KFM Markdown Update & Modernization Agent v1.0
    source_class: CURRENT_TASK_GUIDANCE
    use: same-path repository-grounded Markdown modernization and focused draft-pull-request delivery
related:
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/doctrine/directory-rules.md
  - docs/runbooks/README.md
  - docs/domains/hydrology/README.md
  - docs/runbooks/hydrology/PROMOTION_RUNBOOK.md
  - docs/runbooks/hydrology/VALIDATION.md
  - docs/runbooks/hydrology/NO_NETWORK_TEST_RUNBOOK.md
  - docs/runbooks/hydrology/SOURCE_REFRESH_RUNBOOK.md
  - docs/runbooks/hydrology/ROLLBACK.md
  - docs/runbooks/rollback-rehearsal.md
  - contracts/release/rollback_card.md
  - schemas/contracts/v1/release/rollback_card.schema.json
  - fixtures/release/rollback_card/
  - tools/validators/release/validate_rollback_card.py
  - tools/release/rollback_apply.py
  - tests/release/test_synthetic_rollback_rehearsal.py
  - .github/workflows/rollback-drill.yml
  - release/rollback_cards/README.md
  - release/candidates/hydrology/README.md
  - release/reviews/README.md
  - data/proofs/hydrology/README.md
  - data/receipts/hydrology/README.md
  - data/published/hydrology/README.md
  - pipelines/rollback/main.py
  - scripts/maintenance/audit_published_aliases.py
notes:
  - The repository implements a deterministic, marker-protected synthetic rollback and withdrawal rehearsal. The scenario workspace is guarded; an optional report path remains caller-controlled and can write outside that workspace.
  - The rollback-drill workflow combines eight generic rehearsal tests with four Hazards-specific tests; it does not establish a Hydrology rollback rehearsal.
  - The RollbackCard contract, closed schema, fixtures, validator, and tests establish candidate shape and local consistency only. Every authority and public-mutation flag remains false.
  - The current synthetic helper can replace an existing correction or invalidation record when a scenario-derived ID collides. Current evidence does not prove append-only rehearsal history.
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
> **Current disposition: `GENERIC_SYNTHETIC_ROLLBACK_REHEARSAL_AVAILABLE / HYDROLOGY_SPECIFIC_ROLLBACK_PROOF_ABSENT / OPERATIONAL_HYDROLOGY_ROLLBACK_HOLD`.** The repository has a deterministic no-network helper for marker-protected synthetic scenario workspaces and a fixture-first `RollbackCard` validator. The helper's optional report path is not confined to the scenario workspace. The hosted rollback workflow extends the generic profile with a Hazards fixture, not a Hydrology fixture. No Hydrology candidate release, prior safe target, proof, receipt, published payload, rollback card, accountable review record, operational executor, alias auditor, invalidation adapter, or public recovery read-back is established.

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
  - SYNTHETIC_RECORD_COLLISION_GUARD_ABSENT
  - SYNTHETIC_REPORT_PATH_CONFINEMENT_ABSENT
lifecycle_effect: none
release_effect: none
deployment_effect: none
promotion_effect: none
publication_effect: none
```

**Quick navigation:** [Goal](#goal-and-scope) · [Authority](#authority-and-terminal-boundary) · [Evidence](#current-repository-evidence) · [Vocabulary](#state-and-vocabulary-separation) · [Safety](#hydrology-safety-and-source-role-boundary) · [Decision](#rollback-decision-model) · [Preconditions](#preconditions) · [Procedure](#rollback-preflight-and-handoff-procedure) · [Target](#prior-target-safety) · [Invalidation](#invalidation-and-cross-lane-impact) · [Synthetic proof](#generic-synthetic-rehearsal) · [Results](#interpret-the-results) · [Handoff](#accountable-review-handoff-packet) · [Gap](#hydrology-specific-rehearsal-gap) · [Graduation](#operational-graduation-gate) · [Validation](#documentation-validation) · [Related](#related-repository-surfaces) · [Maintenance](#maintenance-and-document-rollback)

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
  -> governed correction, receipts, proofs, and closure
```

Current repository evidence supports the classification, candidate-validation, generic-rehearsal, and review-handoff parts only. It does not support operational containment, target mutation, invalidation, alias change, or public recovery.

### In scope

- freeze the exact repository revision, affected release reference, artifact digests, public claims, source roles, spatial and temporal scope, and known consumers;
- distinguish rollback, withdrawal, hold, error, and forward correction without translating between them silently;
- preserve Hydrology source-role boundaries, especially observations, regulatory context, hydrographic identity, modeled products, derived context, candidates, and synthetic fixtures;
- require evidence, rights, sensitivity, policy, review, correction, target, invalidation, and public-recovery support appropriate to consequence;
- validate the current fixture-first `RollbackCard` profile and the actual candidate file prepared for review;
- run the repository's generic marker-protected synthetic rehearsal as a mechanics check;
- interpret exact-revision results without converting a green check into review, execution, release, deployment, promotion, or publication authority;
- enumerate cross-lane and public-consumer effects for accountable review; and
- preserve affected and prior release history in the future operational design.

### Out of scope

This runbook does not:

- issue or interpret a current flood warning, watch, evacuation instruction, dam-safety direction, or regulatory determination;
- activate, admit, fetch, alter, or withdraw a live source;
- create a Hydrology release, prior safe target, EvidenceBundle, proof, receipt, policy decision, review record, rollback card, correction notice, or public carrier;
- authorize direct edits to `data/published/`, a public alias, API route, cache, CDN, tile store, catalog, triplet store, search index, vector index, AI cache, deployment, or downstream derivative;
- execute the one-line production rollback pipeline placeholder;
- treat the generic synthetic helper or Hazards-specific workflow extension as Hydrology rollback proof;
- treat the current [`ROLLBACK.md`](ROLLBACK.md) readiness companion as an operational procedure or alternate release authority;
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
| Human Hydrology rollback procedure | This file | Explain classification, prerequisites, capability, stop conditions, and handoff |
| Adjacent Hydrology rollback scaffold | [`ROLLBACK.md`](ROLLBACK.md) | Proposal-era placeholder only |
| Generic synthetic procedure | [`../rollback-rehearsal.md`](../rollback-rehearsal.md) | Explain the isolated marker-protected rehearsal |
| Generic synthetic mechanics | [`tools/release/rollback_apply.py`](../../../tools/release/rollback_apply.py) | Plan or mutate a marker-protected scenario workspace; optionally write a caller-selected report path |
| Generic behavior proof | [`tests/release/test_synthetic_rollback_rehearsal.py`](../../../tests/release/test_synthetic_rollback_rehearsal.py) | Exercise eight generic rollback, withdrawal, integrity, and fail-closed cases |
| `RollbackCard` meaning | [`contracts/release/rollback_card.md`](../../../contracts/release/rollback_card.md) | Define a candidate plan and explicit non-authority boundary |
| `RollbackCard` machine shape | [`schemas/contracts/v1/release/rollback_card.schema.json`](../../../schemas/contracts/v1/release/rollback_card.schema.json) | Validate a closed fixture-first candidate |
| Candidate local consistency | [`tools/validators/release/validate_rollback_card.py`](../../../tools/validators/release/validate_rollback_card.py) | Validate fixtures or explicit candidate files without executing rollback |
| Read-only CI inspection | [`.github/workflows/rollback-drill.yml`](../../../.github/workflows/rollback-drill.yml) | Run candidate, generic, and Hazards synthetic checks while retaining production holds |
| Hydrology release and review inputs | [`release/candidates/hydrology/`](../../../release/candidates/hydrology/README.md) and [`release/reviews/`](../../../release/reviews/README.md) | Guidance only at the pinned base |
| Hydrology proof, receipt, and published lanes | [`data/proofs/hydrology/`](../../../data/proofs/hydrology/README.md), [`data/receipts/hydrology/`](../../../data/receipts/hydrology/README.md), and [`data/published/hydrology/`](../../../data/published/hydrology/README.md) | README and placeholder lanes only |
| Production rollback pipeline | [`pipelines/rollback/main.py`](../../../pipelines/rollback/main.py) | One-line greenfield placeholder |
| Published-alias audit | [`scripts/maintenance/audit_published_aliases.py`](../../../scripts/maintenance/audit_published_aliases.py) | One-line greenfield placeholder |
| Release decisions and records | [`release/`](../../../release/README.md) | Separate governed responsibility; current synthetic helper is not its persistence implementation |

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
| Prior runbook | The v0.1 file claimed the repository was unmounted and named unverified operational commands and paths | Proposal-era claims required replacement, not cosmetic editing |
| Generic helper | Requires a synthetic-workspace marker, `synthetic: true`, safe relative scenario paths, matching manifest/artifact digests, a distinct rollback target, and complete invalidation vocabulary | Scenario mutation is marker-protected; optional report output is separately caller-controlled |
| Generic tests | Eight tests cover deterministic plan, rollback apply, withdrawal apply, non-synthetic denial, incomplete invalidation denial, missing target, digest mismatch, and missing marker | Generic synthetic behavior is executable within the tested profile |
| Plan/report writes | Plan mode is no-write only when `--report` is omitted; with `--report`, plan and apply may create or replace the caller-selected path | Report-path confinement is not proved and must be treated as a hold |
| Synthetic record persistence | Correction and invalidation records use deterministic scenario-derived paths and replacement writes; existing same-ID records are not rejected | Reusing an ID can replace prior synthetic records; append-only or collision-safe history is **not proved** |
| Rollback workflow | Read-only workflow runs the RollbackCard profile plus eight generic and four Hazards tests | A green workflow proves those bounded profiles only; Hydrology-specific proof is absent |
| RollbackCard profile | Contract, closed schema, fixtures, expected findings, validator, tests, and workflow integration exist | A passing fixture matrix does not validate a newly prepared candidate file |
| RollbackCard authority flags | Candidate validation keeps authority creation, policy evaluation, completed review, execution, public mutation, and release binding false or null | The candidate cannot represent authorized or executed rollback |
| Hydrology-specific rehearsal | No checked-in Hydrology rollback fixture or domain rehearsal test was found | Generic or Hazards proof must not be relabeled as Hydrology proof |
| Hydrology candidate lane | README only | No affected or target Hydrology dossier is established |
| Hydrology release reviews | No Hydrology review record | Accountable Hydrology rollback review is absent |
| Hydrology proof lane | `.gitkeep` and README only | No Hydrology rollback or release proof instance is established |
| Hydrology receipt lane | `.gitkeep` and README only | No Hydrology rollback or release receipt instance is established |
| Hydrology published lane | `.gitkeep` and README only | No repository-carried Hydrology public payload or alias target is established |
| Rollback-card records | No Hydrology card instance | No Hydrology recovery candidate or accepted record exists |
| Production pipeline | One-line placeholder | No accepted production rollback engine exists |
| Alias auditor | One-line placeholder | No accepted live alias inventory, audit, or mutation exists |
| GitHub review route | CODEOWNERS routes the repository to `@bartytime4life` while denying that routing proves stewardship or approval | Functional owners and separation of duties remain `NEEDS VERIFICATION` |

### Evidence interpretation

```text
GENERIC SYNTHETIC MECHANICS: IMPLEMENTED
ROLLBACKCARD CANDIDATE VALIDATION: IMPLEMENTED / NON-EXECUTING
HAZARDS SYNTHETIC EXTENSION: IMPLEMENTED
SYNTHETIC SAME-ID COLLISION SAFETY: ABSENT
SYNTHETIC REPORT-PATH CONFINEMENT: ABSENT
HYDROLOGY-SPECIFIC REHEARSAL: ABSENT
OPERATIONAL HYDROLOGY ROLLBACK: HOLD
PUBLIC RECOVERY: NOT ESTABLISHED
```

[Back to top](#top)

---

<a id="state-and-vocabulary-separation"></a>

## State and vocabulary separation

| Vocabulary | Examples | Question answered | Must not imply |
|---|---|---|---|
| Defect signal | evidence contradiction, rights change, validation failure, source withdrawal | Why was recovery evaluation opened? | That rollback is the correct remedy |
| `RollbackCard.disposition` | `ROLLBACK_CANDIDATE`, `WITHDRAWAL_CANDIDATE`, `HOLD`, `ERROR` | What candidate posture is proposed? | Review, execution, or public mutation |
| Runtime or policy outcome | `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`; `HOLD` where owned | What may a consumer return or do? | A release-recovery disposition |
| Review state | unreviewed, review-ready, reviewed in an accepted profile | Has accountable review occurred? | Execution authority unless an accepted control says so |
| Synthetic execution | `PLAN`, marker-protected synthetic `APPLY` | What happened inside a rehearsal? | A real alias or public carrier changed |
| Operational execution | planned, authorized, applying, verified, failed, held | What happened in an accepted recovery executor? | Anything today; the executor is absent |
| Public recovery | stale, withdrawn, superseded, corrected, recovered | What can governed public consumers observe? | That repository state alone proves public parity |

`FORWARD_CORRECTION` is not a current `RollbackCard.disposition`. A corrected artifact must use the accepted candidate, validation, policy, review, promotion, release, correction, and publication path. This runbook may recommend that route without inventing a schema value.

[Back to top](#top)

---

<a id="hydrology-safety-and-source-role-boundary"></a>

## Hydrology safety and source-role boundary

A prior release is unsafe when it restores a collapsed source role even if its bytes match.

| Source or product family | Hydrology role | Prohibited upgrade during recovery |
|---|---|---|
| WBD / HUC | Watershed and hydrologic-unit identity and boundary context | Flood prediction, observed inundation, or emergency status |
| NHDPlus HR and related hydrography | Hydrographic identity, network, and crosswalk context | Regulatory determination or current observation |
| USGS Water observations | Time-bounded observations with unit, qualifier, status, and retrieval context | Forecast, warning, or timeless condition |
| FEMA NFHL | Regulatory flood-hazard context | Observed inundation, current flood, forecast, warning, engineering, or insurance determination by KFM |
| 3DEP or terrain derivatives | Terrain source or derived hydrologic context | Gauge observation, regulation, or hydraulic-model result |
| Modeled hydrograph or derivative | Model or derived result with run support | Observation or official operational guidance |
| Synthetic fixture | Test input | Real condition, admitted source, released artifact, or public evidence |

> [!CAUTION]
> A target that predates current source-role controls is not automatically safe. When its role, time, evidence, rights, sensitivity, or representation posture cannot be revalidated, choose `WITHDRAWAL_CANDIDATE` or `HOLD` rather than restoring it.

[Back to top](#top)

---

<a id="rollback-decision-model"></a>

## Rollback decision model

| Condition | Candidate posture | Required interpretation |
|---|---|---|
| A distinct prior release is identified and revalidates as safer for the exact scope | `ROLLBACK_CANDIDATE` | Restore a verified predecessor only through separately authorized execution |
| No distinct safe predecessor exists, including a defective first release | `WITHDRAWAL_CANDIDATE` | Remove current use without inventing a target |
| Evidence, rights, sensitivity, policy, identity, review, target, invalidation, or read-back support is incomplete | `HOLD` | Preserve fail-closed containment and obtain support |
| Input or evaluation is malformed or cannot finish safely | `ERROR` | Record failure without public mutation |
| A new corrected release is safer than restoring old state | Forward-correction handoff | Use the normal governed correction and release path |

Current `RollbackCard` trigger reasons include `RELEASE_DEFECT`, `EVIDENCE_CONTRADICTION`, `RIGHTS_CHANGE`, `SENSITIVITY_DISCOVERY`, `VALIDATION_FAILURE`, `SOURCE_WITHDRAWAL`, `POLICY_FAILURE`, `SECURITY_ISSUE`, `OPERATIONAL_FAILURE`, `EMERGENCY_HOLD`, `INSUFFICIENT_EVIDENCE`, and `INPUT_INVALID`.

Do not place secrets, protected locations, exploit details, or private review text in a public-safe reason code.

[Back to top](#top)

---

<a id="preconditions"></a>

## Preconditions

### Review-handoff preconditions

- [ ] Exact repository SHA and affected release reference are recorded.
- [ ] Affected artifacts, digests, claims, EvidenceRefs, source roles, geography, time, audience, and consumers are bounded.
- [ ] Defect and trigger reason are supported without exposing sensitive values.
- [ ] Candidate disposition matches the current contract or is explicitly a separate forward-correction recommendation.
- [ ] A rollback candidate names a distinct target; a withdrawal candidate has no target.
- [ ] Consequential claims resolve to evidence or remain unsupported.
- [ ] Rights, sensitivity, precision, source terms, and reconstruction risks are reviewed.
- [ ] A proposed target is revalidated rather than presumed safe because it is older.
- [ ] Required invalidation classes and concrete consumers are enumerated.
- [ ] Correction or notice reference is supplied when public notice is required.
- [ ] The repository fixture matrix passes at the exact tested SHA.
- [ ] The **actual candidate card file** passes the validator at that same SHA.
- [ ] Generic synthetic evidence is labeled generic and synthetic.
- [ ] Synthetic same-ID collision and caller-controlled report-path behavior are disclosed.
- [ ] Reviewer identity, authority, separation, obligations, validity, and supersession are established or marked missing.
- [ ] Missing support remains a `HOLD`, `ERROR`, withdrawal posture, or open obligation.

### Operational preconditions

Current repository evidence does not establish:

- an accepted production plan/apply executor;
- authenticated authorization and separation of duties;
- accepted policy evaluation bound to affected and target releases;
- resolved evidence, proof, receipt, correction, and release records;
- an accepted public alias or equivalent release-state model;
- collision-safe record persistence;
- confinement or policy enforcement for report outputs;
- safe idempotent invalidation adapters;
- partial-failure detection and resumable or compensating behavior;
- deployment identity and least-privilege credentials;
- exact public read-back and stale-leak detection; or
- a Hydrology-specific synthetic rehearsal.

Missing an operational precondition is a stop. Do not substitute manual file edits, cache clearing, or a green generic test.

[Back to top](#top)

---

<a id="rollback-preflight-and-handoff-procedure"></a>

## Rollback preflight and handoff procedure

### 1. Freeze identity and overlap

Record current `main`, evaluated SHA, affected release, artifact digests, public claims, source/evidence/policy/review/correction references, active PRs or incidents, known consumers, and the detector. Detection is not approval.

### 2. Classify the defect

Preserve every material defect class: evidence, source role, identity, time, unit/datum/qualifier, geometry/topology, rights, sensitivity, policy, catalog/citation, consumer drift, security, or operations.

### 3. Select a candidate posture

Apply the [decision model](#rollback-decision-model). Record why rollback is safer than withdrawal or forward correction. Use `HOLD` when the comparison is unsupported.

### 4. Revalidate the target

Use [prior target safety](#prior-target-safety). Digest validity alone is insufficient.

### 5. Prepare references, not payload copies

The packet should point to affected and target records, evidence, source roles, policy, review, correction, proof, receipts, manifests, invalidations, cross-lane impacts, and blockers. Do not copy governed payloads into this runbook or PR text.

### 6. Validate fixtures and the actual candidate

Set `CANDIDATE_CARD` to the exact file being handed to reviewers. The first command proves the repository's known fixture matrix; the second validates the candidate itself.

```bash
CANDIDATE_CARD="${CANDIDATE_CARD:?set CANDIDATE_CARD to the candidate JSON path}"

python tools/validators/release/validate_rollback_card.py --fixtures
python tools/validators/release/validate_rollback_card.py "$CANDIDATE_CARD"

python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_rollback_card.py' \
  --verbose
```

A fixture pass does not rescue a candidate-file failure. A candidate pass still proves local shape and cross-field consistency only; it does not resolve references, authenticate review, evaluate policy, select a target, or execute rollback.

### 7. Run the generic rehearsal

```bash
python -m unittest -q tests.release.test_synthetic_rollback_rehearsal
```

Keep the Hydrology-specific gap, same-ID collision limitation, and report-path boundary visible.

### 8. Prepare accountable-review handoff

Use the [handoff packet](#accountable-review-handoff-packet). Ask for a decision; do not imply one occurred.

### 9. Stop before mutation

Do not invoke [`pipelines/rollback/main.py`](../../../pipelines/rollback/main.py) or [`audit_published_aliases.py`](../../../scripts/maintenance/audit_published_aliases.py); both are placeholders. Do not edit a real published lane, alias, cache, catalog, API route, index, AI cache, deployment, or derivative under this procedure.

[Back to top](#top)

---

<a id="prior-target-safety"></a>

## Prior target safety

| Target check | Required evidence | Failure posture |
|---|---|---|
| Distinct identity | Target differs from the affected release and uses immutable identity | `ERROR` or `HOLD` |
| Manifest and artifact integrity | Manifest and referenced artifact digests match | `HOLD` |
| Evidence resolution | Consequential target claims resolve to admissible EvidenceBundles | Earlier target, withdrawal, or hold |
| Source-role safety | Observation, regulatory, modeled, derived, contextual, and synthetic roles remain separate | Withdrawal or hold |
| Spatial and temporal validity | CRS, geometry, identity, vintage, observed/valid/retrieval/release time, freshness, and qualifiers remain valid | Withdrawal, earlier target, or forward correction |
| Rights and sensitivity | Current terms, attribution, access, precision, and policy permit use | `DENY` or `HOLD` through owning policy |
| Review and policy | Accepted records apply to the target and audience | `HOLD` |
| Consumer compatibility | Governed API, map, Evidence Drawer, export, search, graph, AI, and derivatives can consume it safely | `HOLD` |
| Correction lineage | Restoration does not erase the affected release or defect record | `HOLD` |
| Public read-back | A plan can prove every exposed consumer reflects the intended state | `HOLD` |

A first Hydrology release has no predecessor. Its posture is withdrawal, hold, or forward correction—not an invented rollback target.

[Back to top](#top)

---

<a id="invalidation-and-cross-lane-impact"></a>

## Invalidation and cross-lane impact

The generic scenario requires these invalidation classes:

`API_CACHE`, `CDN`, `TILES`, `CATALOG`, `TRIPLETS`, `SEARCH_INDEX`, `VECTOR_INDEX`, `AI_CACHE`, and `DOWNSTREAM_DERIVATIVES`.

That vocabulary proves only that a rehearsal scenario names every class. It does not prove any live adapter was called.

| Lane | Typical dependency | Hydrology handoff obligation |
|---|---|---|
| Hazards | Flood, drought, exposure, warning, resilience | Name affected claims; Hazards owns its recovery decision |
| Soil | Soil moisture, drainage, wetness, erosion | Name joined carriers and stale-state risk |
| Agriculture | Irrigation, crop-water, drought, reservoirs, groundwater | Name affected observations, models, and summaries |
| Settlements / Infrastructure | Floodplain, bridge, dam, utility, supply, service area | Escalate sensitivity and harmful precision |
| Habitat / Fauna / Flora | Aquatic habitat, wetland, riparian, occurrence, restoration | Preserve owning-lane evidence and sensitivity obligations |
| Geology | Aquifer and hydrostratigraphic context | Preserve Geology context and Hydrology observation boundaries |

Do not auto-mutate a sibling lane. Record the dependency, evidence intersection, requested action, owner, and unresolved state.

[Back to top](#top)

---

<a id="generic-synthetic-rehearsal"></a>

## Generic synthetic rehearsal

### What current evidence proves

Inside a marker-protected synthetic scenario workspace, the helper and eight tests demonstrate:

- deterministic no-write planning **when `--report` is omitted**;
- synthetic rollback to a distinct prior release;
- synthetic withdrawal without a target;
- affected manifest and artifact bytes remain present;
- correction and invalidation records are written at deterministic scenario-derived paths;
- every declared invalidation class is required;
- non-synthetic, unmarked, unsafe scenario paths, missing targets, and digest mismatches fail closed; and
- authority and public-mutation flags remain false.

> [!CAUTION]
> **Current rehearsal history is not append-only.** The helper writes correction and invalidation JSON through replacement semantics and does not reject an existing record with the same scenario-derived ID. Reusing an ID can replace a prior synthetic record. The eight generic tests do not exercise that collision. Current evidence therefore proves neither reject-on-exist behavior nor versioned collision-safe history.

> [!CAUTION]
> **The optional report path is not confined to the synthetic workspace.** When `--report PATH` is supplied, both plan and apply modes may create or replace that caller-selected path wherever the process can write. Use no report path for a no-write plan, or place it inside a dedicated disposable synthetic directory. Never point it at a repository file, governed lifecycle lane, release record, deployment mount, public store, or shared operational path.

### CLI boundary

No-write plan without a report:

```bash
python tools/release/rollback_apply.py \
  --workspace /tmp/kfm-rehearsal \
  --scenario /tmp/kfm-rehearsal/scenario.json
```

Synthetic apply with a report confined by caller convention to the same disposable root:

```bash
python tools/release/rollback_apply.py \
  --workspace /tmp/kfm-rehearsal \
  --scenario /tmp/kfm-rehearsal/scenario.json \
  --report /tmp/kfm-rehearsal/report.json \
  --apply
```

The helper enforces the scenario workspace marker; it does not enforce report-path confinement. Current documentation therefore requires caller restraint and retains operational `HOLD`.

### Workflow boundary

The current `rollback-drill` workflow runs:

- the RollbackCard candidate fixture profile;
- eight generic synthetic tests; and
- four Hazards-specific synthetic tests.

Its expected twelve-test result is **generic plus Hazards**, not Hydrology. A green workflow does not prove Hydrology rollback, collision-safe recovery records, report-path confinement, target mutation, or public recovery.

[Back to top](#top)

---

<a id="interpret-the-results"></a>

## Interpret the results

| Observation | Required interpretation |
|---|---|
| RollbackCard fixtures pass | Current fixture matrix and local consistency passed at the tested SHA |
| Actual candidate file passes | That exact file passed local shape and cross-field validation only |
| Generic eight-test suite passes | Marker-protected synthetic mechanics passed; collision safety, report confinement, and Hydrology behavior remain unproved |
| `rollback-drill` passes | Candidate, generic, and Hazards synthetic checks passed while operational holds remained visible |
| Hydrology bounded validation passes | Named Hydrology fixture shape and polarity checks passed; release safety did not |
| Candidate support is missing | `HOLD` or withdrawal posture, depending on consequence |
| Accepted policy denies use | Preserve `DENY`; do not translate it into a softer recommendation |
| Evaluation cannot finish safely | `ERROR`; no mutation |
| Exact base/head comparison is unavailable | `NEEDS VERIFICATION` or `UNRESOLVED / NON-COMPARABLE` |
| A check is skipped | `SKIPPED`, never `PASS` |
| A check did not run | `NOT RUN`, never inferred success |

Record exact SHA, command or workflow, fixture inventory, candidate path and digest, result, and skipped or unavailable checks.

[Back to top](#top)

---

<a id="accountable-review-handoff-packet"></a>

## Accountable review handoff packet

The YAML below is an **illustrative documentation handoff**, not a `RollbackCard`, `ReviewRecord`, `PolicyDecision`, `CorrectionNotice`, release record, or execution instruction.

```yaml
handoff_type: HYDROLOGY_ROLLBACK_REVIEW
repository:
  base_sha: <40-character SHA>
  evaluated_sha: <40-character SHA>
  active_overlaps: []
affected:
  release_ref: <stable ref or ABSENT>
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
  card_path: <exact candidate path or null>
  card_digest: <sha256 or null>
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
  fixture_matrix: <PASS | FAIL | ERROR | NOT_RUN>
  actual_candidate_file: <PASS | FAIL | ERROR | NOT_RUN>
  generic_synthetic_rehearsal: <PASS | FAIL | NOT_RUN>
  synthetic_record_collision_safety: ABSENT
  synthetic_report_path_confinement: ABSENT
  hydrology_specific_rehearsal: ABSENT
  hydrology_domain_checks: []
  tested_sha: <40-character SHA>
  skipped_or_unavailable: []
review:
  required_roles: []
  authenticated_records: []
  separation_of_duties: <confirmed | not_confirmed>
  open_obligations: []
public_recovery:
  execution_authority: <ref or NEEDS_VERIFICATION>
  invalidation_plan: <ref or NEEDS_VERIFICATION>
  readback_plan: <ref or NEEDS_VERIFICATION>
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

[Back to top](#top)

---

<a id="hydrology-specific-rehearsal-gap"></a>

## Hydrology-specific rehearsal gap

No checked-in Hydrology synthetic rollback workspace, scenario, or domain test extends the generic helper at the pinned base.

A future dependency-closed slice should add one non-locating, unreleased, unpublished, no-network Hydrology profile that reuses the generic helper rather than creating a second engine. It should prove:

1. deterministic no-write planning over a synthetic Hydrology release pair;
2. marker-protected synthetic restoration with affected history retained;
3. withdrawal when no distinct safe predecessor is declared;
4. denial when NFHL is relabeled as observed inundation or warning support;
5. denial when provisional/final, observation/model, or source-role state is collapsed;
6. denial when HUC, reach, gauge, or crosswalk identity is ambiguous;
7. denial when target equals affected release or digests fail;
8. complete invalidation vocabulary with public-mutation flags false;
9. reject-on-exist or versioned preservation when correction or invalidation IDs collide;
10. report-path confinement beneath the synthetic root, or explicit denial of out-of-root report paths; and
11. workflow recognition that cannot pass with zero tests.

That follow-up would prove a bounded Hydrology synthetic profile only. Production target selection, policy, review, signing, invalidation, alias mutation, deployment, and public recovery would remain separate.

[Back to top](#top)

---

<a id="operational-graduation-gate"></a>

## Operational graduation gate

Operational Hydrology rollback remains `HOLD` until current evidence demonstrates all of the following together:

1. exact affected Hydrology release and immutable artifact/claim inventory;
2. distinct revalidated target, or accepted withdrawal posture when no target exists;
3. EvidenceRef-to-EvidenceBundle, proof, receipt, manifest, catalog, and correction closure;
4. accepted source-role, identity, spatial, temporal, unit, datum, qualifier, uncertainty, and representation controls;
5. current rights, sensitivity, precision, attribution, and source-term clearance;
6. accepted active policy evaluator with enforceable obligations;
7. authenticated accountable review, authority intervals, separation of duties, and revocation/supersession handling;
8. accepted RollbackCard, CorrectionNotice, ReviewRecord, release-record, and execution-receipt profiles;
9. accepted plan/apply executor with least privilege, idempotency, concurrency control, resumability, partial-failure handling, and no-history-erasure tests;
10. collision-safe recovery-record persistence using reject-on-exist or versioned immutable records, with positive and negative tests;
11. report-output confinement or an accepted policy that safely prohibits or governs out-of-workspace reports;
12. accepted public alias or equivalent release-state model plus audit tooling;
13. real API, CDN, tile, catalog, triplet, search, vector, AI, and downstream invalidation adapters;
14. Hydrology-specific no-network rehearsal and approved non-public operational exercise;
15. deployment identity, secrets custody, monitoring, logs, alerting, and rollback-of-rollback posture;
16. exact public read-back proving every governed consumer reflects intended state and correction lineage; and
17. documented reversal or forward-recovery path preserving affected history.

No weighted score, deadline, green generic test, schema pass, PR, merge, signature alone, or operator confidence may compensate for a failed trust or safety gate.

[Back to top](#top)

---

<a id="documentation-validation"></a>

## Documentation validation

```bash
python tools/validators/docs/link-check/check_links.py \
  --repo-root . \
  --format text \
  docs/runbooks/hydrology/ROLLBACK_RUNBOOK.md

python tools/validators/release/validate_rollback_card.py --fixtures
python tools/validators/release/validate_rollback_card.py "$CANDIDATE_CARD"
python -m unittest -q tests.release.test_synthetic_rollback_rehearsal
```

Run hosted Markdown, document-graph, metadata, rollback-drill, Hydrology, contract, schema, policy, security, and topology checks at the exact changed SHA.

This runbook is ready for accountable documentation review only when:

- proposal-era unmounted-repository posture and invented operational commands are removed;
- current generic mechanics, RollbackCard profile, workflow composition, and production holds are accurate;
- absent Hydrology candidate, target, proof, receipt, card, review, published payload, executor, auditor, invalidation path, and read-back are explicit;
- the actual candidate file, not only fixtures, must pass validation;
- rollback, withdrawal, hold, error, and forward correction remain distinct;
- NFHL, observations, models, hydrography, terrain derivatives, and fixtures cannot be collapsed;
- synthetic same-ID replacement and out-of-workspace report behavior are explicit;
- no command can touch a real public or lifecycle surface;
- relative links and stable anchors resolve;
- no sensitive values or rights-unclear payloads are included; and
- abandonment of an unmerged change is distinct from reverting an authorized merge.

[Back to top](#top)

---

<a id="related-repository-surfaces"></a>

## Related repository surfaces

### Hydrology procedures

- [Hydrology domain boundary](../../domains/hydrology/README.md)
- [Hydrology promotion preflight](PROMOTION_RUNBOOK.md)
- [Hydrology bounded validation](VALIDATION.md)
- [Hydrology no-network procedure](NO_NETWORK_TEST_RUNBOOK.md)
- [Hydrology source refresh](SOURCE_REFRESH_RUNBOOK.md)
- [Adjacent rollback scaffold](ROLLBACK.md)

### Generic rollback controls

- [Generic synthetic rehearsal](../rollback-rehearsal.md)
- [RollbackCard contract](../../../contracts/release/rollback_card.md)
- [RollbackCard schema](../../../schemas/contracts/v1/release/rollback_card.schema.json)
- [RollbackCard fixtures](../../../fixtures/release/rollback_card/)
- [RollbackCard validator](../../../tools/validators/release/validate_rollback_card.py)
- [Synthetic helper](../../../tools/release/rollback_apply.py)
- [Generic synthetic tests](../../../tests/release/test_synthetic_rollback_rehearsal.py)
- [Rollback-drill workflow](../../../.github/workflows/rollback-drill.yml)

### Release and Hydrology lanes

- [Release governance](../../../release/README.md)
- [Rollback-card lane](../../../release/rollback_cards/README.md)
- [Hydrology candidate lane](../../../release/candidates/hydrology/README.md)
- [Release review lane](../../../release/reviews/README.md)
- [Hydrology proof lane](../../../data/proofs/hydrology/README.md)
- [Hydrology receipt lane](../../../data/receipts/hydrology/README.md)
- [Hydrology published lane](../../../data/published/hydrology/README.md)

### Held surfaces

- [Production rollback pipeline placeholder](../../../pipelines/rollback/main.py)
- [Published-alias auditor placeholder](../../../scripts/maintenance/audit_published_aliases.py)

[Back to top](#top)

---

<a id="maintenance-and-document-rollback"></a>

## Maintenance and document rollback

Update this runbook when:

- a Hydrology rollback fixture or domain test changes;
- helper marker, scenario contract, record-write semantics, report-path behavior, invalidation vocabulary, test inventory, or workflow composition changes;
- RollbackCard contract, schema, fixtures, validator, or vocabulary changes;
- a Hydrology candidate, target, proof, receipt, card, correction notice, review record, release record, published carrier, or public alias appears;
- policy, reviewer authority, execution, invalidation, deployment, monitoring, or public-readback evidence changes;
- production pipeline or alias auditor stops being a placeholder;
- a real correction, withdrawal, rollback, incident, or rehearsal exposes a gap;
- the adjacent `ROLLBACK.md` scaffold is retired or assigned a distinct responsibility; or
- Directory Rules, accepted ADRs, contracts, or release architecture change this file's responsibility.

To **abandon an unmerged documentation change**, close its draft pull request and delete only its task branch after preserving any review history that must remain auditable. To **continue toward merge**, leave the pull request open until the repository's review and merge controls complete. After an authorized merge, revert the focused documentation commits or submit a smaller reviewed forward correction. Reverting this Markdown never reverses a source admission, lifecycle transition, release, correction, withdrawal, rollback, deployment, promotion, publication, alias, cache, public carrier, or operational state.

[Back to top](#top)
