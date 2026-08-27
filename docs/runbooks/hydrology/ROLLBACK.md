<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbook-hydrology-rollback-readiness
title: Hydrology Rollback Readiness and Handoff
type: operational-boundary-runbook
version: v2.0.0
status: DRAFT_REPOSITORY_GROUNDED; GENERIC_SYNTHETIC_REHEARSAL_AVAILABLE; HYDROLOGY_SPECIFIC_REHEARSAL_ABSENT; OPERATIONAL_ROLLBACK_HELD; NOT_FOR_LIFE_SAFETY; NON_RELEASE; NON_PUBLICATION
owners: "@bartytime4life — verified CODEOWNERS route; accountable Hydrology, source, evidence, policy, correction, rollback, release, operations, and public-surface stewardship NEEDS VERIFICATION"
created: 2026-05-12
updated: 2026-08-27
supersedes: "unversioned PROPOSED scaffold at this path"
policy_label: repository-facing; hydrology; rollback-readiness; correction-aware; synthetic-proof-bounded; fail-closed; not-for-life-safety; non-publisher
owning_root: docs/
current_path: docs/runbooks/hydrology/ROLLBACK.md
path_authority: same-path modernization under accepted ADR-0029 and Directory Rules v2
responsibility: "Describe current Hydrology rollback readiness, finite candidate dispositions, mandatory preconditions, bounded validation, and accountable handoff without authorizing or executing a release-state or public-state mutation."
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
  target_path: docs/runbooks/hydrology/ROLLBACK.md
  target_prior_blob: 4ec794c5bad3b13368de88b8b258c10b9972cb1b
  rollback_card_contract: contracts/release/rollback_card.md
  rollback_card_schema: schemas/contracts/v1/release/rollback_card.schema.json
  rollback_card_validator: tools/validators/release/validate_rollback_card.py
  generic_synthetic_helper: tools/release/rollback_apply.py
  generic_synthetic_tests: tests/release/test_synthetic_rollback_rehearsal.py
  readiness_workflow: .github/workflows/rollback-drill.yml
  hydrology_workflow: .github/workflows/domain-hydrology.yml
  tracked_hydrology_candidate_payloads: 0
  tracked_hydrology_published_payloads: 0
  hydrology_specific_rollback_rehearsal: ABSENT
  production_rollback_pipeline: PLACEHOLDER
  published_alias_auditor: PLACEHOLDER
  open_pull_requests_at_inspection: 0
source_lineage:
  - title: KFM_Hydrology_Extended_Pro_PDF_Only_Reference_Report_2026-04-21.pdf
    source_class: PLANNING_LINEAGE
    use: Hydrology-first, HUC12, source-role, temporal, evidence, correction, and rollback framing only; its no-repository assumptions do not describe current implementation
  - title: KFM Alignment Register — 2026-08-23
    source_class: NOTION_COORDINATION_ONLY
    use: preserve validation, review, merge, rollback authorization, execution, release, deployment, promotion, and publication as separate states
  - title: KFM Markdown Update & Modernization Agent v1.0
    source_class: CURRENT_TASK_GUIDANCE
    use: same-path repository-grounded Markdown modernization and focused draft-pull-request delivery
related:
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../doctrine/directory-rules.md
  - ../../architecture/publication/ROLLBACK.md
  - ../ROLLBACK_RUNBOOK.md
  - ROLLBACK_RUNBOOK.md
  - PROMOTION_RUNBOOK.md
  - NO_NETWORK_TEST_RUNBOOK.md
  - VALIDATION.md
  - ../../domains/hydrology/README.md
  - ../../../contracts/release/rollback_card.md
  - ../../../schemas/contracts/v1/release/rollback_card.schema.json
  - ../../../fixtures/release/rollback_card/
  - ../../../tools/validators/release/validate_rollback_card.py
  - ../../../tools/release/rollback_apply.py
  - ../../../tests/validators/test_validate_rollback_card.py
  - ../../../tests/release/test_synthetic_rollback_rehearsal.py
  - ../../../.github/workflows/rollback-drill.yml
  - ../../../.github/workflows/domain-hydrology.yml
  - ../../../release/candidates/hydrology/README.md
  - ../../../data/published/hydrology/README.md
  - ../../../policy/domains/hydrology/README.md
notes:
  - The current shared RollbackCard profile proves candidate shape and bounded local consistency only; it requires authority, policy, review, execution, public mutation, and release flags to remain false or null.
  - The current executable rollback helper is marker-protected and synthetic-only. The hosted readiness workflow runs generic and Hazards rehearsal tests, not a Hydrology-specific rollback rehearsal.
  - The tracked Hydrology candidate and published-data lanes contain guidance only; production deployment and public runtime state remain UNKNOWN without runtime evidence.
  - The sibling ROLLBACK_RUNBOOK.md is retained as proposal-era planning lineage and contains unverified commands and paths. It is not current command authority.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hydrology Rollback Readiness and Handoff

> **One-line purpose.** Assess a suspected Hydrology release defect, choose a finite rollback-candidate, withdrawal-candidate, hold, error, or forward-correction posture, run only the repository's bounded checks, and prepare an accountable handoff without mutating public state or treating synthetic rehearsal as production rollback.

[![Operational rollback: held](https://img.shields.io/badge/operational%20rollback-HOLD-b42318?style=flat-square)](#current-disposition)
[![Generic rehearsal: synthetic only](https://img.shields.io/badge/generic%20rehearsal-synthetic%20only-8250df?style=flat-square)](#bounded-current-validation)
[![Hydrology-specific drill: absent](https://img.shields.io/badge/Hydrology%20drill-ABSENT-6e7781?style=flat-square)](#current-repository-evidence)
[![Public effect: none](https://img.shields.io/badge/public%20effect-none-6e7781?style=flat-square)](#authority-and-document-relationship)

<a id="not-for-life-safety"></a>

> [!CAUTION]
> **KFM Hydrology is not an emergency-alerting, flood-warning, navigation, engineering, insurance, permitting, dam-safety, or regulatory-determination system.** This runbook does not retrieve or validate current water conditions and cannot issue, replace, delay, retract, or interpret official warnings or protective instructions. Direct urgent or authoritative decisions to the responsible official source.

<a id="current-disposition"></a>

> [!IMPORTANT]
> **Current disposition: `GENERIC_SYNTHETIC_REHEARSAL_AVAILABLE / HYDROLOGY_SPECIFIC_REHEARSAL_ABSENT / OPERATIONAL_ROLLBACK_HOLD`.** The repository has a closed fixture-first `RollbackCard` candidate profile, a deterministic marker-protected synthetic rollback and withdrawal helper, eight generic rehearsal tests, and a read-only workflow that also runs four Hazards-specific tests. It does not have a Hydrology-specific rollback fixture or test, a populated Hydrology release candidate, a tracked Hydrology published payload, an accepted production rollback operator, a live published-alias auditor, authenticated rollback authority, active release policy, external invalidation execution, or an executed rollback receipt.

The highest result this document and the current executable surfaces can support is:

```text
BOUNDED_HYDROLOGY_ROLLBACK_READINESS_ASSESSMENT
```

That result is not `ROLLBACK_AUTHORIZED`, `ROLLBACK_EXECUTED`, `RECOVERED`, `RELEASED`, `DEPLOYED`, `PROMOTED`, or `PUBLISHED`.

**Quick navigation:** [Goal](#goal-and-scope) · [Authority](#authority-and-document-relationship) · [Evidence](#current-repository-evidence) · [Safety](#hydrology-safety-and-source-role-boundary) · [Decision](#rollback-decision-model) · [Defects](#hydrology-defect-classification) · [Containment](#immediate-containment-and-scope-freeze) · [Preconditions](#operational-preconditions) · [Validation](#bounded-current-validation) · [Interpretation](#interpret-the-results) · [Handoff](#accountable-handoff-packet) · [Recovery](#hydrology-recovery-requirements) · [Graduation](#operational-graduation-gate) · [Failures](#failure-handling-and-stop-conditions) · [Maintenance](#maintenance-and-document-rollback) · [Related](#related-repository-surfaces)

---

<a id="goal-and-scope"></a>

## Goal and scope

Use this document when a released, release-facing, or allegedly public Hydrology carrier may be wrong, stale, unsafe, unsupported, role-collapsed, or inconsistent with its declared release state.

The bounded current workflow is:

```text
defect signal
  -> freeze exact repository and alleged release scope
  -> classify the defect and affected carriers
  -> select a finite candidate disposition
  -> validate RollbackCard candidate shape and current Hydrology fixture boundaries
  -> optionally rehearse generic synthetic mechanics in a protected temporary root
  -> prepare accountable review and operations handoff
  -> stop before public-state mutation
```

### In scope

- identify the exact affected release reference, artifact set, domain scope, time scope, and public surfaces;
- distinguish a tracked repository artifact from an external or deployed state that remains `UNKNOWN`;
- classify Hydrology-specific evidence, identity, source-role, temporal, unit, rights, sensitivity, validation, and cross-lane defects;
- recommend `ROLLBACK_CANDIDATE`, `WITHDRAWAL_CANDIDATE`, `HOLD`, or `ERROR` using the shared `RollbackCard` vocabulary;
- recommend forward correction when rollback is unnecessary or no longer the soundest recovery path;
- require a distinct, digest-pinned prior release before recommending rollback;
- run the current candidate validator, generic synthetic rehearsal, Hydrology bounded checks, and documentation link check;
- preserve evidence, manifests, receipts, review history, correction lineage, and invalidation scope in the handoff; and
- state the exact blockers that prevent operational rollback.

### Out of scope

This document does not:

- mutate `data/published/`, a deployed API, a mutable alias, a tile archive, cache, CDN, catalog, search index, vector index, AI cache, or downstream derivative;
- activate or deactivate a live Hydrology source;
- create an accepted `RollbackCard`, `CorrectionNotice`, `ReleaseManifest`, review record, policy decision, signature, proof, or execution receipt;
- authenticate a reviewer or assign release/rollback authority;
- execute the proposal-era `kfm release ...` examples in [`ROLLBACK_RUNBOOK.md`](ROLLBACK_RUNBOOK.md);
- run database recovery, infrastructure failover, secret rotation, Git rollback, or schema-migration rollback;
- alter an official warning, regulatory record, upstream source, or emergency message; or
- release, deploy, promote, publish, or imply public recovery.

[Back to top](#top)

---

<a id="authority-and-document-relationship"></a>

## Authority and document relationship

Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) and [Directory Rules v2](../../doctrine/directory-rules.md) place human operating procedures under `docs/runbooks/`, semantic meaning under `contracts/`, machine shape under `schemas/`, policy under `policy/`, executable mechanics under `tools/` and `pipelines/`, behavioral evidence under `tests/`, release decisions under `release/`, process receipts under governed `data/receipts/` lanes, and public-safe carriers under governed published-data lanes.

This is a same-path replacement of an established scaffold. It creates no new responsibility root or parallel contract, schema, policy, receipt, proof, release, or publication home.

| Surface | Current role | Authority boundary |
|---|---|---|
| This file, `docs/runbooks/hydrology/ROLLBACK.md` | Repository-grounded readiness assessment and handoff procedure for the requested path | Documentation only; no transition authority |
| [`ROLLBACK_RUNBOOK.md`](ROLLBACK_RUNBOOK.md) | Proposal-era Hydrology rollback plan retained for lineage | Contains unverified commands, paths, cadence, thresholds, and implementation assumptions; not current command authority |
| [Cross-domain publication rollback architecture](../../architecture/publication/ROLLBACK.md) | Repository-grounded responsibility map and maturity boundary | Architecture explanation; does not execute rollback |
| [General rollback runbook](../ROLLBACK_RUNBOOK.md) | Cross-domain proposal-era operating guidance | Useful doctrine lineage; not proof of current production operation |
| [`RollbackCard` contract](../../../contracts/release/rollback_card.md) | Candidate semantic meaning | Proposed, candidate-only, non-executing |
| Paired schema and validator | Closed `1.0.0` shape and local consistency | Cannot prove reference resolution, review, policy, authority, execution, or public mutation |
| Synthetic helper | Deterministic plan/apply against marker-protected synthetic roots | Never a production operator |
| `rollback-drill` workflow | Read-only readiness inspection and bounded test execution | Green means the bounded profile and holds behaved as declared |
| Release and public-data roots | Decisions, receipts, and carriers in their accepted homes | Remain separate from this document |

The canonical lifecycle remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Rollback changes governed release state and downstream carriers. It does not move evidence backward through lifecycle directories or rewrite RAW source material.

[Back to top](#top)

---

<a id="current-repository-evidence"></a>

## Current repository evidence

The observations below are pinned to `main@8e7c862f5bf91fb27038ef264549b565b4827711`. Re-read the exact surfaces whenever the rollback contract, schema, fixtures, validator, helper, tests, workflows, Hydrology candidate lane, policy, proof/receipt lanes, published lane, operator, or alias mechanism changes.

| Surface | CONFIRMED repository evidence | Bounded conclusion |
|---|---|---|
| Requested path | The prior file was a 758-byte `PROPOSED scaffold` sourced from the Hydrology expansion backlog | A same-path substantive update is warranted; the scaffold was not operational guidance |
| Shared RollbackCard profile | A draft contract, closed `1.0.0` schema, three valid fixtures, six invalid fixtures, expected-findings manifest, no-network validator, focused tests, and path-scoped workflow exist | Candidate shape and local consistency are implemented; rollback authority and execution are not |
| Candidate governance boundary | Schema-valid candidates require authority, policy evaluation, completed review, rollback execution, public mutation, and release linkage to remain false or null | A valid card deliberately cannot represent an authorized or executed rollback |
| Generic synthetic helper | `tools/release/rollback_apply.py` requires the exact synthetic marker, `synthetic: true`, safe relative paths, current-alias identity, manifest and artifact digests, a distinct target for rollback, and the complete invalidation set | Deterministic `PLAN` and synthetic-root `APPLY` mechanics exist; public state is never touched |
| Generic rehearsal tests | Eight tests cover deterministic no-write planning, synthetic rollback, synthetic withdrawal, history preservation, and fail-closed marker, target, digest, invalidation, and non-synthetic cases | Generic synthetic mechanics are executable |
| Readiness workflow | `.github/workflows/rollback-drill.yml` runs RollbackCard fixture validation and the generic plus Hazards synthetic suites, requiring twelve non-vacuous tests | Current hosted scope is generic plus Hazards; it is not a Hydrology rollback proof |
| Hydrology rollback rehearsal | No Hydrology-specific synthetic rollback fixture or test is wired into the readiness workflow | Hydrology carrier, source-role, time, identity, cross-lane, and public-recovery behavior are unproved |
| Hydrology domain validation | `.github/workflows/domain-hydrology.yml` runs bounded no-network shape, polarity, type-separation, identity, ambiguity, and context-routing checks | Useful changed-area evidence; not rollback, evidence closure, active policy, proof, release, or publication evidence |
| Hydrology candidate lane | `release/candidates/hydrology/` contains its README only | No tracked Hydrology candidate dossier exists to roll forward or back |
| Hydrology published lane | `data/published/hydrology/` contains `.gitkeep` and its README, with no tracked public payload | No repository-tracked Hydrology artifact can currently be selected as an affected or prior release payload |
| Production rollback pipeline | `pipelines/rollback/main.py` remains an exact one-line greenfield placeholder | No accepted production rollback engine exists |
| Published-alias auditor | `scripts/maintenance/audit_published_aliases.py` remains a comment-only placeholder; the readiness workflow finds no tracked current alias | No accepted live alias inventory, audit, or mutation path exists |
| Executed rollback receipts | The accepted `data/receipts/rollback/` responsibility is not populated or established as an operational lane at this snapshot | No executed rollback or external invalidation receipt is available |
| Hydrology policy | The Hydrology policy lane remains mixed-maturity and evaluator-unbound | Operational rights, sensitivity, source-role, freshness, and release-policy evaluation remain held |
| Accountable authority | CODEOWNERS routes review to `@bartytime4life`; functional and independent release/rollback stewardship is not established | Review routing is not approval, separation of duties, or transition authority |
| Deployment/public runtime | No deployment target, runtime log, external storage inventory, public alias, or public read-back was inspected | Actual deployed Hydrology state is `UNKNOWN`; repository absence must not be generalized into a deployment claim |

### Evidence summary

```yaml
candidate_shape: BOUNDED_IMPLEMENTED
hydrology_domain_checks: BOUNDED_IMPLEMENTED
synthetic_rollback_mechanics: GENERIC_IMPLEMENTED
hydrology_specific_rehearsal: ABSENT
tracked_hydrology_candidate: ABSENT
tracked_hydrology_published_payload: ABSENT
active_release_policy: NOT_ESTABLISHED
production_operator: PLACEHOLDER
live_alias_audit_or_mutation: PLACEHOLDER
executed_rollback_receipt: ABSENT
operational_rollback: HOLD
```

[Back to top](#top)

---

<a id="hydrology-safety-and-source-role-boundary"></a>

## Hydrology safety and source-role boundary

A rollback candidate is unsafe when it restores the same semantic collapse that caused the defect.

| Hydrology family | Required role boundary | Rollback consequence |
|---|---|---|
| USGS Water Data or comparable gauge observations | Observation with parameter, unit, qualifier, provisional/final state, observed time, and retrieval time preserved | Do not restore a target that hides provisional status, changes units, or presents stale readings as current |
| FEMA NFHL or comparable regulatory flood context | Regulatory context only | Never restore a target that presents NFHL as observed inundation, forecast, live warning, or hydraulic-model truth |
| WBD/HUC boundaries | Versioned boundary/aggregate context with geometry identity | A metadata timestamp alone does not prove material change or safety; require the accepted material-change evidence |
| NHDPlus HR and legacy COMID bridges | Source-native identifiers and relation cardinality remain distinct | Exact one-to-one support may answer; split, merge, retired, unresolved, or ambiguous mappings abstain |
| Modeled or derived hydrography | Modeled or derived, with input/run identity and uncertainty | Never upgrade a model or derivative to observation during rollback |
| Public-safe flow profile | Synthetic fixture semantics, generalized support, bounded location, time, unit, and no-alert limitations | Passing the fixture does not prove a real gauge observation or public-release suitability |
| Cross-lane Hydrology context | Hydrology remains one bounded context; Soil, Hazards, Agriculture, Geology, Infrastructure, and other lanes retain their own claims | A Hydrology recovery cannot silently restore or approve another lane's carrier |

> [!WARNING]
> A prior release is not safe merely because it is older, green in CI, or still stored. It must satisfy current identity, source-role, rights, sensitivity, evidence, policy, review, correction, and rollback requirements. When no such target exists, recommend withdrawal or hold rather than inventing a rollback target.

[Back to top](#top)

---

<a id="rollback-decision-model"></a>

## Rollback decision model

Keep four vocabularies separate:

| Vocabulary | Values used here | Question answered |
|---|---|---|
| Truth label | `CONFIRMED`, `PROPOSED`, `UNKNOWN`, `NEEDS VERIFICATION` | How strongly is a statement supported? |
| RollbackCard candidate disposition | `ROLLBACK_CANDIDATE`, `WITHDRAWAL_CANDIDATE`, `HOLD`, `ERROR` | What recovery candidate is being proposed? |
| Public/runtime outcome | `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` | What may a governed consumer return? |
| Work state | `HOLD`, `REPAIR_REQUIRED`, `READY_FOR_ACCOUNTABLE_REVIEW` where applicable | What should maintainers do next? |

### Candidate selection

| Condition | Candidate posture | Required note |
|---|---|---|
| A distinct prior Hydrology release is immutable, digest-verifiable, currently admissible, evidence-supported, policy-safe, reviewable, and compatible with current public obligations | `ROLLBACK_CANDIDATE` | Name affected and target release refs; do not execute |
| The current carrier must leave public use and no safe prior release exists | `WITHDRAWAL_CANDIDATE` | Name the correction/withdrawal path and expected public finite outcome |
| Evidence, target identity, rights, sensitivity, policy, review, operator, alias, or invalidation support is unresolved | `HOLD` | List exact blockers; preserve prior state unless separately authorized containment applies |
| Input is malformed, internally contradictory, non-synthetic for the synthetic helper, or cannot be safely evaluated | `ERROR` | Record a public-safe reason code and no state change |
| A corrected successor can be reviewed through the normal promotion path without restoring an older release | Forward correction | This is a work recommendation, not a RollbackCard disposition; use the promotion/correction path and retain rollback readiness |

### Default at the current repository checkpoint

Because the tracked Hydrology candidate and published lanes contain no payloads, no Hydrology-specific rehearsal exists, policy is not operationally bound, and the production operator and alias auditor are placeholders, the default operational state is:

```text
HOLD — PREPARE ASSESSMENT AND REVIEW HANDOFF ONLY
```

[Back to top](#top)

---

<a id="hydrology-defect-classification"></a>

## Hydrology defect classification

Classify every material defect before selecting a candidate disposition. Multi-class defects inherit the strictest applicable response.

| Defect class | Hydrology example | Bounded response | Candidate tendency |
|---|---|---|---|
| Evidence contradiction or missing support | A public claim no longer resolves to its declared evidence | Consumer should `ABSTAIN`; preserve contradiction and correction lineage | Hold, withdrawal, or rollback only to a currently supported target |
| Source-role collapse | NFHL described as observed flooding; model output described as a measurement | Fail closed; do not restore the same collapse | Withdrawal or rollback to a role-correct target |
| Identity ambiguity | Permanent Identifier/COMID split, merge, retired, or unresolved relation collapsed to one answer | `ABSTAIN`; preserve all candidates and relation type | Hold until identity is resolved; never guess a target |
| Temporal or freshness defect | Provisional data treated as final; observed, retrieval, effective, release, or correction time collapsed | Mark stale or abstain; preserve time kinds | Forward correction, withdrawal, or role-safe rollback |
| Parameter, unit, or datum defect | Flow parameter or unit changed; datum omitted; no-data represented as a measurement | Deny affected claim until corrected | Rollback only to a target with explicit compatible semantics |
| WBD/HUC material-change defect | Geometry or area materially changed while metadata-only churn was mistaken for proof | Run the dedicated fixture-only material-change profile; require exact geometry/version basis | Hold or corrected successor; rollback is not automatic |
| USGS API cutover defect | Required endpoint family, rewrite map, dual-run reconciliation, or legacy dependency is inconsistent | Run the dedicated fixture-only cutover assessment | Hold or forward correction unless a safe prior interface remains supported |
| Rights or terms change | Redistribution or public-use basis is no longer supported | `DENY` public use; quarantine future intake as separately governed | Withdrawal unless a distinct admissible target exists |
| Sensitivity or harmful precision | A join exposes private-property, infrastructure, well-owner, or another lane's restricted detail | Contain through separately authorized incident/public controls; preserve audit evidence | Withdrawal or generalized corrected successor |
| Cross-lane contamination | Hazards, Soil, Agriculture, Geology, or Infrastructure derivative inherits defective Hydrology context | Notify each owning lane; mark dependent artifacts held or stale for separate review | Hydrology action does not authorize sibling-lane recovery |
| UI/AI persistence defect | Search, Evidence Drawer, map, export, or Focus answer continues to expose withdrawn support | Include every carrier in invalidation scope; consumer returns finite non-answer | Hold execution until external invalidation and read-back are accepted |
| Integrity or tamper defect | Manifest or artifact digest differs from the declared value | `ERROR` and stop; do not select or restore the artifact | No rollback to an unverifiable target |

[Back to top](#top)

---

<a id="immediate-containment-and-scope-freeze"></a>

## Immediate containment and scope freeze

This section prepares an accountable response. It does not grant authority to change a deployed surface.

1. **Record the exact repository SHA and detection time.** Do not describe `latest`, `current`, or `main` without an immutable revision.
2. **Identify the alleged release.** Record the affected `release_ref`, artifact digests, evidence refs, audience, geography, time window, and source roles. If the release cannot be identified, select `HOLD` or `ERROR`.
3. **Separate repository state from deployment state.** Record whether the carrier is tracked in this repository. Treat external object storage, CDN state, API state, caches, and deployed aliases as `UNKNOWN` until inspected by an authorized operator.
4. **Inventory every affected surface.** Include API caches, CDN, tiles, catalog, triplets, search index, vector index, AI cache, and downstream derivatives where applicable.
5. **Classify safety and source role.** For current or urgent water conditions, refer users to the official authority. Do not convert KFM containment into an official warning action.
6. **Freeze target selection.** Do not identify a prior release as safe before its current evidence, policy, role, time, rights, sensitivity, manifest, and artifact digests are verified.
7. **Choose a finite candidate disposition.** Record rollback candidate, withdrawal candidate, hold, error, or forward-correction recommendation without mutating state.
8. **Open accountable handoff.** Name the missing authority, policy, review, operator, invalidation, read-back, or receipt evidence that blocks execution.

### Never do during the assessment

- Do not edit a public alias or copy prior bytes into a published path.
- Do not delete the defective manifest, artifacts, EvidenceBundle, review record, or receipts.
- Do not disable validation to make a target pass.
- Do not use `tools/release/rollback_apply.py` outside an exact marker-protected synthetic workspace.
- Do not treat `KFM_NO_NETWORK=1` as proof of host-level egress denial.
- Do not infer release or rollback authority from CODEOWNERS, a pull request, CI, a schema pass, a signature, or generated prose.

[Back to top](#top)

---

<a id="operational-preconditions"></a>

## Operational preconditions

Operational rollback remains held until every applicable precondition is confirmed at one exact revision and for one exact affected release.

| Precondition | Evidence required | Failure posture |
|---|---|---|
| Affected release identity | Immutable `ReleaseManifest`, artifact digests, audience, release time, and public-surface inventory | `HOLD` or `ERROR` |
| Distinct target identity | Immutable prior manifest and target artifacts; target differs from affected release | Withdrawal candidate or `HOLD` |
| Current target admissibility | Resolved evidence, source role, rights, sensitivity, time/freshness, validation, policy, and review | `DENY`, `ABSTAIN`, or `HOLD` |
| Correction/withdrawal relationship | Accepted correction or withdrawal record profile and public-notice requirement | `HOLD` |
| Accountable actors | Authenticated detector, domain steward, correction reviewer, release authority, and required independent/specialist reviewers | `HOLD` |
| Active policy binding | Exact accepted policy bundle, evaluator, input, decision, obligations, and consumer enforcement | `HOLD` or `DENY` |
| Accepted operator | Production rollback interface with target, digest, review/signature, policy, no-write plan, apply, idempotency, and negative tests | `HOLD` |
| Published-state mechanism | Accepted alias or release-state projection plus read-only audit and mutation semantics | `HOLD` |
| Invalidation execution | Authenticated adapters and receipts for every applicable invalidation class | `HOLD` |
| History preservation | Append-only correction, affected release retention, and immutable evidence/review lineage | `ERROR` if history would be erased |
| Execution receipt | Accepted `data/receipts/rollback/` profile recording before/after identity, operations, invalidations, actor, policy, review, and result | `HOLD` |
| Public read-back | Independent verification that governed API, map, drawer, search, exports, and AI surfaces expose the intended corrected state | `HOLD` |
| Cross-lane closure | Each affected sibling lane records its own decision and recovery status | Hydrology may close only its own scope |

> [!IMPORTANT]
> A deadline, high feature value, green test, or prior publication cannot compensate for a missing release identity, evidence closure, rights/sensitivity decision, accountable review, safe target, accepted operator, correction path, invalidation proof, or rollback receipt.

[Back to top](#top)

---

<a id="bounded-current-validation"></a>

## Bounded current validation

Run from the repository root at a recorded commit. These commands validate the current bounded surfaces only. They do not authorize or execute rollback.

### 1. Dependency bootstrap

```bash
python tools/ci/install_python_ci.py project-test
```

Dependency installation is a separate bootstrap step and may require an approved package cache or network. It is not part of a no-live-source or hermetic claim.

### 2. RollbackCard candidate profile

```bash
python tools/validators/release/validate_rollback_card.py --fixtures

python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_rollback_card.py' \
  --verbose
```

A pass proves the declared shared candidate shape, exact fixture polarity, and bounded local consistency. It does not resolve references, authenticate actors, run policy, approve a target, execute invalidation, or mutate public state.

### 3. Generic plus Hazards synthetic rehearsal

```bash
python -m unittest -q \
  tests.release.test_synthetic_rollback_rehearsal \
  tests.domains.hazards.test_synthetic_rollback_rehearsal
```

The current readiness workflow requires a non-vacuous result of twelve tests with `OK`. This command proves generic synthetic mechanics and the exact Hazards fixture profile. **It is not a Hydrology-specific rollback rehearsal.**

### 4. Bounded Hydrology domain checks

```bash
export KFM_NO_NETWORK=1
export PYTHONDONTWRITEBYTECODE=1
export PYTHONHASHSEED=0
export PYTHONUNBUFFERED=1
export TZ=UTC

python -m pytest -q -p no:cacheprovider \
  tests/domains/hydrology/test_hydrology_smoke.py \
  tests/domains/hydrology/test_aquifer_observation.py \
  tests/domains/hydrology/test_aquifer_context_link.py \
  tests/domains/hydrology/test_nhdplus_hr_ambiguity.py \
  tests/domains/hydrology/test_adaptive_threshold_proposal.py \
  tests/domains/hydrology/test_hydro_identity_bridge.py \
  tests/domains/hydrology/test_streamflow_qc_context_assessment.py

python tests/domains/hydrology/test_public_safe_flow_fixture.py --verbose
python tests/cross_domain/test_environmental_observation_boundaries.py --verbose

python tools/validators/domains/hydrology/validate_evidence_bundle.py \
  fixtures/domains/hydrology/evidence_bundle/valid/valid_1.json

if python tools/validators/domains/hydrology/validate_evidence_bundle.py \
  fixtures/domains/hydrology/evidence_bundle/invalid/invalid_1.json; then
  echo "ERROR: known-invalid Hydrology EvidenceBundle fixture was accepted"
  exit 1
fi

python tools/validators/domains/hydrology/validate_aquifer_observation.py \
  --fixtures
python tools/validators/domains/hydrology/validate_aquifer_context_link.py \
  --fixtures
python tools/validators/domains/hydrology/validate_public_safe_flow_fixture.py \
  fixtures/domains/hydrology/public_safe_flow/valid/public_safe_flow.json
python tools/validators/domains/hydrology/validate_nhdplus_waterbody_crosswalk.py \
  --fixtures
```

These checks prove only their committed synthetic profiles. They do not establish source admission, real Hydrology truth, complete EvidenceBundle resolution, active policy, proof, release, rollback, or publication.

### 5. Documentation link validation

```bash
python tools/validators/docs/link-check/check_links.py \
  --repo-root . \
  --format text \
  docs/runbooks/hydrology/ROLLBACK.md
```

The link checker makes no external requests. External source currentness, deployment state, and public runtime behavior remain separate verification tasks.

[Back to top](#top)

---

<a id="interpret-the-results"></a>

## Interpret the results

| Result | What it establishes | What it does not establish |
|---|---|---|
| RollbackCard fixture validator passes | Candidate shape and local cross-field consistency | Safe target, resolved evidence, policy approval, review, authority, execution, or public recovery |
| Generic/Hazards rehearsal passes | Deterministic synthetic plan/apply mechanics, fail-closed guards, and history preservation for the exact tested profiles | Hydrology-specific behavior or production rollback |
| Hydrology bounded checks pass | The committed Hydrology synthetic profiles retain their declared shape, polarity, identity, role, and context boundaries | A real release, real source accuracy, EvidenceBundle closure, policy, proof, or rollback readiness |
| `rollback-drill` is green | The workflow's read-only checks and explicit holds behaved as expected at that SHA | Production operator, alias mutation, invalidation, executed receipt, or public recovery |
| A documentation PR merges | Repository documentation changed | Review authority, adoption, rollback authorization, release, deployment, promotion, or publication |
| No tracked Hydrology public payload exists | The inspected repository tree contains no such payload | No deployed or external Hydrology state exists |
| APIsec or another job is skipped | The job did not run | A pass or a failure |
| A check is pending | No settled exact-head result yet | Success or failure |

### Required classification for failures

- **Introduced:** caused by this change or its direct dependency closure.
- **Inherited:** reproduced at the exact base or otherwise supported as pre-existing.
- **Unrelated:** outside the changed path and not causally supported by the diff.
- **Skipped:** workflow explicitly did not run.
- **Not run:** no execution evidence exists.
- **Needs verification:** causation or significance cannot yet be established.

Do not call a failure inherited merely because the changed file is Markdown. Establish causation from exact-head evidence where possible.

[Back to top](#top)

---

<a id="accountable-handoff-packet"></a>

## Accountable handoff packet

Use this worksheet to prepare review. It is illustrative Markdown, not a machine contract or accepted release record.

```yaml
assessment_type: hydrology_rollback_readiness
assessment_version: 1
repository_sha: <40-character-commit>
detected_at: <timezone-aware-timestamp>

scope:
  affected_release_ref: <required-or-UNKNOWN>
  affected_artifact_refs: []
  alleged_public_surface_refs: []
  geography: <declared-scope>
  time_scope: <declared-scope>
  source_roles: []

state_separation:
  tracked_repository_payload_found: false
  deployed_public_state: UNKNOWN
  official_source_state: OUTSIDE_KFM_AUTHORITY

classification:
  defect_classes: []
  safety_or_official_referral_required: false
  cross_lane_dependencies: []

candidate:
  disposition: HOLD
  target_release_ref: null
  correction_notice_ref: null
  evidence_bundle_refs: []
  policy_decision_refs: []
  review_record_refs: []
  invalidations: []

validation:
  rollback_card_profile: NOT_RUN
  generic_synthetic_rehearsal: NOT_RUN
  hydrology_domain_profile: NOT_RUN
  hydrology_specific_rehearsal: ABSENT
  documentation_links: NOT_RUN

blockers:
  - HYDROLOGY_ROLLBACK_REHEARSAL_ABSENT
  - PRODUCTION_ROLLBACK_OPERATOR_ABSENT
  - PUBLISHED_ALIAS_MECHANISM_UNESTABLISHED
  - ACTIVE_RELEASE_POLICY_UNESTABLISHED
  - ACCOUNTABLE_ROLLBACK_AUTHORITY_UNVERIFIED
  - EXECUTION_RECEIPT_PROFILE_ABSENT

non_effects:
  source_activation: none
  lifecycle_mutation: none
  public_state_mutation: none
  release: none
  deployment: none
  promotion: none
  publication: none

recommended_next_state: HOLD_FOR_ACCOUNTABLE_REVIEW_AND_IMPLEMENTATION
```

### Minimum reviewer questions

1. Is the affected release a real governed release, an unreleased candidate, a synthetic fixture, a repository document, or an external/deployed state?
2. Can every affected and target artifact be identified and digest-verified?
3. Does the target satisfy current evidence, source-role, rights, sensitivity, time, unit, policy, review, correction, and rollback requirements?
4. Is rollback preferable to withdrawal or forward correction?
5. Who has authenticated authority to approve and execute the transition, and is required separation of duties met?
6. Which invalidation classes and external consumers must be handled, and how will completion be receipted?
7. How will public read-back prove that no stale API, map, drawer, search, export, or AI carrier remains?
8. Which sibling lanes require their own independent recovery decisions?

[Back to top](#top)

---

<a id="hydrology-recovery-requirements"></a>

## Hydrology recovery requirements

A future authorized operator must preserve all of the following. These are graduation requirements, not claims about current behavior.

### Identity and target integrity

- Bind affected and target releases to immutable manifests and artifact digests.
- Reject target-equals-affected and missing-target rollback requests.
- Preserve NHDPlus HR Permanent Identifiers and legacy COMIDs as distinct source-native families.
- Preserve exact, split, merge, complex, retired, and unresolved relation semantics; do not normalize ambiguity by assumption.
- Bind WBD/HUC geometry and material-change evidence to explicit versions and deterministic fingerprints.

### Time and scientific context

Keep material time kinds distinct, including observed, valid/effective, source, retrieval, release, correction, and transaction time. Preserve provisional/final status, parameter identity, units, datum, qualifiers, no-data semantics, model-run identity, uncertainty, and aggregation scope where applicable.

### Evidence, policy, and review

- Resolve every consequential EvidenceRef to admissible support.
- Re-evaluate current policy; do not reuse an old allow decision without current applicability evidence.
- Authenticate reviewers and release authority.
- Preserve source-role, rights, sensitivity, public-precision, cross-lane, and audience obligations.
- Require a CorrectionNotice or WithdrawalNotice whenever the public state changes materially.

### History and invalidation

- Retain affected manifests, artifacts, evidence, reviews, decisions, and receipts for audit unless a separate lawful deletion process applies.
- Record every applicable invalidation class: API cache, CDN, tiles, catalog, triplets, search index, vector index, AI cache, and downstream derivatives.
- Emit an execution receipt that records before/after identity, actor, policy, review, plan digest, operations, invalidations, read-back, and finite result.
- Verify public recovery independently after mutation; a successful operator exit code is not sufficient.

### Cross-lane consequences

| Lane | Typical Hydrology dependency | Required handoff |
|---|---|---|
| Hazards | Flood or drought context, exposure, stale-state interpretation | Name affected refs; Hazards decides its own correction or withdrawal |
| Soil | Hydrologic group, soil-moisture, drainage, or wetness context | Revalidate joined carriers and public precision |
| Agriculture | Irrigation, drought-stress, crop-water, or seasonal context | Preserve aggregation and model/observation distinctions |
| Geology | Aquifer and hydrostratigraphic context links | Keep measurements in Hydrology and geometry/units in Geology-owned context |
| Settlements/Infrastructure | Floodplain, bridge, dam, utility, or service exposure | Apply sensitivity and harmful-precision review before public recovery |
| Habitat, Fauna, and Flora | Riparian, wetland, aquatic habitat, occurrence, or suitability context | Owning biological lanes retain evidence and sensitivity authority |

Hydrology may notify and provide evidence. It must not approve another lane's release transition.

[Back to top](#top)

---

<a id="operational-graduation-gate"></a>

## Operational graduation gate

Remove the operational hold only through a separately reviewed, dependency-closed implementation that proves all applicable gates together.

- [ ] A Hydrology-specific, public-safe, non-locating synthetic rollback and withdrawal fixture exists.
- [ ] Hydrology-specific tests cover source-role, time, unit/datum, identity ambiguity, cross-lane notification, invalidation completeness, history preservation, tamper denial, and non-synthetic denial.
- [ ] The Hydrology profile is integrated into `rollback-drill` without replacing generic or Hazards coverage.
- [ ] A populated synthetic Hydrology affected release and distinct prior target are bound to immutable manifests and digests.
- [ ] The accepted RollbackCard operational profile resolves evidence, policy, review, correction, target, and release references.
- [ ] An exact active release-policy bundle, evaluator, obligations, and consumer enforcement path are accepted.
- [ ] Accountable actor identity and required separation of duties are authenticated and tested.
- [ ] A production operator has deterministic plan/apply, no-write plan, idempotency, concurrency, failure recovery, safe-path, signature/review, target, policy, and negative tests.
- [ ] The published-state/alias profile and read-only auditor are accepted and tested before mutation is enabled.
- [ ] External invalidation adapters are least-privilege, fail closed, observable, and receipt-backed.
- [ ] An append-only rollback execution receipt profile and validator exist in the accepted receipt home.
- [ ] Public API, map, Evidence Drawer, search, export, cache, and AI read-back checks prove parity after the synthetic drill.
- [ ] Correction, withdrawal, supersession, recompile, and rollback lineage remain inspectable.
- [ ] Accountable human review of the exact implementation and exact-head hosted evidence is complete.

Graduation of a synthetic Hydrology drill still does not authorize production rollback. Production authorization, release, deployment, promotion, and publication remain separate governed transitions.

[Back to top](#top)

---

<a id="failure-handling-and-stop-conditions"></a>

## Failure handling and stop conditions

| Condition | Finite response | Required action |
|---|---|---|
| Affected release cannot be identified | `ERROR` or `HOLD` | Narrow scope; do not mutate public state |
| No distinct safe target exists | Withdrawal candidate or `HOLD` | Preserve history and prepare correction/withdrawal review |
| Evidence is insufficient but no policy prohibition is established | `ABSTAIN` | Do not generate a Hydrology claim from plausibility |
| Rights, sensitivity, or source-role policy forbids exposure | `DENY` | Prepare separately authorized containment/withdrawal handoff |
| Target or artifact digest mismatches | `ERROR` | Stop; investigate integrity and storage lineage |
| Synthetic marker is absent or scenario is non-synthetic | `ERROR` / helper exit `2` | Do not bypass the guard or point the helper at real paths |
| Invalidation list is incomplete | `HOLD` or `ERROR` | Enumerate every applicable consumer before execution review |
| Accountable authority or policy binding is absent | `HOLD` | Do not treat CODEOWNERS, CI, or a PR as authorization |
| Hydrology-specific drill is absent | `HOLD` for Hydrology rollback readiness | Implement the bounded synthetic profile before claiming domain proof |
| A bounded check fails because of this documentation or direct dependency | Introduced failure | Repair before review handoff |
| Hosted failure is outside the changed path | `NEEDS VERIFICATION` | Establish causation before calling it inherited or unrelated |
| Official warning or urgent current-condition risk is involved | Official referral plus separately authorized KFM incident containment | Do not use this runbook as emergency authority |
| Public read-back cannot prove recovery | `HOLD` | Keep incident open; do not claim recovery |

### Anti-patterns

- **Hidden file copy:** restoring old bytes without governed target, policy, review, correction, execution, and receipts.
- **Old means safe:** selecting a prior release without current admissibility checks.
- **Schema pass means authority:** treating a candidate validator result as approval.
- **Synthetic means production:** applying the helper to a real or unmarked root.
- **Green hold means ready:** reading a workflow's explicit hold as operational capability.
- **Erase the defect:** deleting the affected release or evidence instead of preserving correction lineage.
- **Smoothed non-answer:** replacing `ABSTAIN` or `DENY` with vague confident prose.
- **Role collapse:** restoring NFHL as observed flooding or a model as a measurement.
- **Time collapse:** using retrieval, release, or correction time as observed/effective time.
- **Cross-lane auto-approval:** assuming a Hydrology recovery approves Hazards, Soil, Agriculture, Geology, Infrastructure, or biological derivatives.
- **Repository absence equals deployment absence:** claiming no public state exists because no tracked payload is present.
- **Documentation drift as command authority:** copying proposal-era CLI examples into operations without implemented tooling evidence.

[Back to top](#top)

---

<a id="maintenance-and-document-rollback"></a>

## Maintenance and document rollback

Reconcile this document whenever any of these surfaces changes:

- `contracts/release/rollback_card.md` or its schema, fixtures, validator, tests, or workflow;
- `tools/release/rollback_apply.py` or the generic/Hazards rehearsal profiles;
- `.github/workflows/rollback-drill.yml`;
- `.github/workflows/domain-hydrology.yml` or the accepted Hydrology validator/test inventory;
- the Hydrology candidate, proof, receipt, policy, or published-data lanes;
- the production rollback pipeline, published-state profile, alias auditor, invalidation adapters, or execution receipts;
- accepted correction, withdrawal, release, or separation-of-duties decisions;
- Hydrology source-role, identity, time, unit, rights, sensitivity, or public-use doctrine; or
- deployment/runtime evidence that changes the `UNKNOWN` public-state boundary.

### Known documentation follow-up

[`ROLLBACK_RUNBOOK.md`](ROLLBACK_RUNBOOK.md) remains a proposal-era planning document with unverified commands, paths, cadence, thresholds, and pre-mounted-repository assumptions. Preserve it as lineage until a separate compatibility/migration review either modernizes it, converts it to a redirect, or retires it with consumer and anchor closure. Do not silently maintain two independent operational authorities.

The one-byte [`README.md`](README.md) and other stale Hydrology runbook summaries are separate documentation drift. This update does not expand into their reconciliation.

### Roll back this documentation change

Revert the single commit that replaces this file if the document:

- misstates current repository evidence;
- breaks local links or stable document identity;
- overstates rollback, review, release, deployment, promotion, or publication authority;
- conflicts with accepted Directory Rules or a later accepted rollback decision; or
- causes focused documentation checks to fail.

Reverting this Markdown file does not modify a source, lifecycle object, RollbackCard, manifest, alias, cache, receipt, release, deployment, public carrier, or published state.

[Back to top](#top)

---

<a id="related-repository-surfaces"></a>

## Related repository surfaces

| Surface | Current role |
|---|---|
| [Publication Rollback Discipline](../../architecture/publication/ROLLBACK.md) | Cross-domain repository-grounded architecture and maturity boundary |
| [General Rollback Runbook](../ROLLBACK_RUNBOOK.md) | Proposal-era cross-domain operating lineage |
| [Hydrology proposal-era Rollback Runbook](ROLLBACK_RUNBOOK.md) | Detailed historical plan; not current command authority |
| [Hydrology Promotion Runbook](PROMOTION_RUNBOOK.md) | Repository-grounded promotion readiness and operational hold |
| [Hydrology No-Network Test Runbook](NO_NETWORK_TEST_RUNBOOK.md) | Offline Hydrology validation boundary; verify its current revision before use |
| [Hydrology Validation](VALIDATION.md) | Adjacent validation guidance; current workflows and tests outrank stale prose |
| [Hydrology domain README](../../domains/hydrology/README.md) | Domain meaning, source-role, time, identity, and public-use boundaries |
| [RollbackCard contract](../../../contracts/release/rollback_card.md) | Candidate semantics and explicit non-authority boundary |
| [RollbackCard schema](../../../schemas/contracts/v1/release/rollback_card.schema.json) | Closed candidate machine shape |
| [RollbackCard fixtures](../../../fixtures/release/rollback_card/) | Deterministic valid/invalid candidate examples |
| [RollbackCard validator](../../../tools/validators/release/validate_rollback_card.py) | Candidate shape and local-consistency validation |
| [Synthetic rollback helper](../../../tools/release/rollback_apply.py) | Marker-protected synthetic plan/apply only |
| [Generic synthetic tests](../../../tests/release/test_synthetic_rollback_rehearsal.py) | Eight deterministic rehearsal tests |
| [`rollback-drill` workflow](../../../.github/workflows/rollback-drill.yml) | Read-only generic/Hazards readiness checks and production holds |
| [Hydrology workflow](../../../.github/workflows/domain-hydrology.yml) | Bounded Hydrology fixture validation and explicit proof/release holds |
| [Hydrology candidate lane](../../../release/candidates/hydrology/README.md) | Pre-publication review guidance; no tracked candidate dossier at the evidence snapshot |
| [Hydrology published-data lane](../../../data/published/hydrology/README.md) | Released-carrier responsibility; no tracked payload at the evidence snapshot |
| [Hydrology policy boundary](../../../policy/domains/hydrology/README.md) | Mixed-maturity policy inventory and evaluator hold |

[Back to top](#top)
