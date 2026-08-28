<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbook-hydrology-rollback-readiness
title: Hydrology Rollback Readiness and Handoff
type: operational-boundary-runbook
version: v2.0.1
status: DRAFT_REPOSITORY_GROUNDED; GENERIC_SYNTHETIC_REHEARSAL_AVAILABLE; HYDROLOGY_SPECIFIC_REHEARSAL_ABSENT; OPERATIONAL_ROLLBACK_HELD; NOT_FOR_LIFE_SAFETY; NON_RELEASE; NON_PUBLICATION
owners: "@bartytime4life — verified CODEOWNERS route; accountable Hydrology, source, evidence, policy, correction, rollback, release, operations, and public-surface stewardship NEEDS VERIFICATION"
created: 2026-05-12
updated: 2026-08-27
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
  - This edition replaces the prior unversioned proposal scaffold at the same path; that predecessor exposed no durable document identifier for a relation edge.
  - The shared RollbackCard profile proves candidate shape and bounded local consistency only; it requires authority, policy, review, execution, public mutation, and release flags to remain false or null.
  - The executable rollback helper is marker-protected and synthetic-only. The hosted readiness workflow runs generic and Hazards rehearsal tests, not a Hydrology-specific rollback rehearsal.
  - The tracked Hydrology candidate and published-data lanes contain guidance only; production deployment and public runtime state remain UNKNOWN without runtime evidence.
  - The sibling ROLLBACK_RUNBOOK.md is proposal-era planning lineage with unverified commands and paths, not current command authority.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hydrology Rollback Readiness and Handoff

> **One-line purpose.** Assess a suspected Hydrology release defect, choose a finite rollback-candidate, withdrawal-candidate, hold, error, or forward-correction posture, run only repository-owned bounded checks, and prepare an accountable handoff without mutating public state or treating synthetic rehearsal as production rollback.

[![Operational rollback: held](https://img.shields.io/badge/operational%20rollback-HOLD-b42318?style=flat-square)](#current-disposition)
[![Generic rehearsal: synthetic only](https://img.shields.io/badge/generic%20rehearsal-synthetic%20only-8250df?style=flat-square)](#bounded-current-validation)
[![Hydrology-specific drill: absent](https://img.shields.io/badge/Hydrology%20drill-ABSENT-6e7781?style=flat-square)](#current-repository-evidence)
[![Public effect: none](https://img.shields.io/badge/public%20effect-none-6e7781?style=flat-square)](#authority-and-document-relationship)

> [!CAUTION]
> **KFM Hydrology is not an emergency-alerting, flood-warning, navigation, engineering, insurance, permitting, dam-safety, or regulatory-determination system.** This runbook does not retrieve or validate current water conditions and cannot issue, replace, delay, retract, or interpret official warnings or protective instructions. Direct urgent or authoritative decisions to the responsible official source.

<a id="current-disposition"></a>

> [!IMPORTANT]
> **Current disposition: `GENERIC_SYNTHETIC_REHEARSAL_AVAILABLE / HYDROLOGY_SPECIFIC_REHEARSAL_ABSENT / OPERATIONAL_ROLLBACK_HOLD`.** The repository has a closed fixture-first `RollbackCard` candidate profile, a deterministic marker-protected synthetic rollback and withdrawal helper, eight generic rehearsal tests, and a read-only workflow that also runs four Hazards-specific tests. It does not have a Hydrology-specific rollback fixture or test, a populated Hydrology release candidate, a tracked Hydrology published payload, an accepted production rollback operator, a live published-alias auditor, authenticated rollback authority, active release policy, external invalidation execution, or an executed rollback receipt.

The highest result supported here is:

```text
BOUNDED_HYDROLOGY_ROLLBACK_READINESS_ASSESSMENT
```

That result is not `ROLLBACK_AUTHORIZED`, `ROLLBACK_EXECUTED`, `RECOVERED`, `RELEASED`, `DEPLOYED`, `PROMOTED`, or `PUBLISHED`.

**Quick navigation:** [Goal](#goal-and-scope) · [Authority](#authority-and-document-relationship) · [Evidence](#current-repository-evidence) · [Safety](#hydrology-safety-and-source-role-boundary) · [Decision](#rollback-decision-model) · [Defects](#hydrology-defect-classification) · [Containment](#immediate-containment-and-scope-freeze) · [Preconditions](#operational-preconditions) · [Validation](#bounded-current-validation) · [Interpretation](#interpret-the-results) · [Handoff](#accountable-handoff-packet) · [Recovery](#hydrology-recovery-requirements) · [Graduation](#operational-graduation-gate) · [Failures](#failure-handling-and-stop-conditions) · [Maintenance](#maintenance-and-document-rollback) · [Related](#related-repository-surfaces)

---

<a id="goal-and-scope"></a>

## Goal and scope

Use this document when a released, release-facing, or allegedly public Hydrology carrier may be wrong, stale, unsafe, unsupported, role-collapsed, or inconsistent with its declared release state.

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
- separate tracked repository artifacts from external or deployed state that remains `UNKNOWN`;
- classify Hydrology evidence, identity, source-role, temporal, unit, rights, sensitivity, validation, and cross-lane defects;
- recommend `ROLLBACK_CANDIDATE`, `WITHDRAWAL_CANDIDATE`, `HOLD`, or `ERROR` using the shared `RollbackCard` vocabulary;
- recommend forward correction when rollback is unnecessary or no longer the soundest recovery path;
- require a distinct, digest-pinned prior release before recommending rollback;
- run candidate validation, synthetic rehearsal, bounded Hydrology checks, and documentation link validation;
- preserve evidence, manifests, receipts, reviews, correction lineage, and invalidation scope in the handoff; and
- state the exact blockers that prevent operational rollback.

### Out of scope

This document does not:

- mutate `data/published/`, a deployed API, alias, tile archive, cache, CDN, catalog, search index, vector index, AI cache, or derivative;
- activate or deactivate a live source;
- create or approve a `RollbackCard`, `CorrectionNotice`, `ReleaseManifest`, review record, policy decision, proof, signature, or execution receipt;
- authenticate a reviewer or assign rollback authority;
- execute proposal-era `kfm release ...` examples from [`ROLLBACK_RUNBOOK.md`](ROLLBACK_RUNBOOK.md);
- perform database recovery, infrastructure failover, secret rotation, Git rollback, or schema-migration rollback;
- alter an official warning, regulatory record, upstream source, or emergency message; or
- release, deploy, promote, publish, or imply public recovery.

[Back to top](#top)

---

<a id="authority-and-document-relationship"></a>

## Authority and document relationship

Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) and [Directory Rules v2](../../doctrine/directory-rules.md) place human procedures under `docs/runbooks/`, semantic meaning under `contracts/`, machine shape under `schemas/`, policy under `policy/`, mechanics under `tools/` and `pipelines/`, behavioral evidence under `tests/`, release decisions under `release/`, receipts under governed `data/receipts/` lanes, and public-safe carriers under governed published-data lanes.

This is a same-path replacement of an established scaffold. It creates no new responsibility root or parallel contract, schema, policy, receipt, proof, release, or publication home.

| Surface | Current role | Authority boundary |
|---|---|---|
| This file | Repository-grounded Hydrology rollback readiness and handoff | Documentation only; no transition authority |
| [`ROLLBACK_RUNBOOK.md`](ROLLBACK_RUNBOOK.md) | Proposal-era Hydrology rollback plan retained for lineage | Unverified commands and paths; not current command authority |
| [Publication rollback architecture](../../architecture/publication/ROLLBACK.md) | Cross-domain responsibility map and maturity boundary | Architecture explanation; no execution |
| [General rollback runbook](../ROLLBACK_RUNBOOK.md) | Cross-domain proposal-era operating guidance | Doctrine lineage; not production proof |
| [`RollbackCard` contract](../../../contracts/release/rollback_card.md) | Candidate semantic meaning | Proposed, candidate-only, non-executing |
| Paired schema and validator | Closed `1.0.0` shape and local consistency | Cannot prove resolution, review, policy, authority, or public mutation |
| Synthetic helper | Deterministic plan/apply against marker-protected synthetic roots | Never a production operator |
| `rollback-drill` workflow | Read-only readiness inspection and bounded test execution | Green means only the bounded profile and holds behaved as declared |

The lifecycle remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Rollback changes governed release state and downstream carriers. It does not rewrite RAW evidence or move objects backward through lifecycle directories.

[Back to top](#top)

---

<a id="current-repository-evidence"></a>

## Current repository evidence

The observations below are pinned to `main@8e7c862f5bf91fb27038ef264549b565b4827711`. Re-read the exact surfaces whenever the contract, schema, fixtures, validator, helper, tests, workflows, candidate lane, policy, proof/receipt lanes, published lane, operator, or alias mechanism changes.

| Surface | CONFIRMED repository evidence | Bounded conclusion |
|---|---|---|
| Requested path | Prior content was a 758-byte `PROPOSED scaffold` | Same-path modernization was warranted; the scaffold was not operational guidance |
| Shared RollbackCard profile | Draft contract, closed schema, three valid fixtures, six invalid fixtures, expected findings, no-network validator, tests, and workflow exist | Candidate shape and local consistency are implemented; authority and execution are not |
| Candidate boundary | Valid candidates require authority, policy, review, execution, public mutation, and release linkage to remain false or null | A valid candidate deliberately cannot represent an authorized rollback |
| Generic helper | Requires the exact synthetic marker, `synthetic: true`, safe paths, current-alias identity, manifest/artifact digests, distinct target, and complete invalidations | Deterministic synthetic `PLAN` and `APPLY` mechanics exist; public state is never touched |
| Generic tests | Eight tests cover planning, rollback, withdrawal, history preservation, and fail-closed marker, target, digest, invalidation, and non-synthetic cases | Generic synthetic mechanics are executable |
| Readiness workflow | Runs RollbackCard validation and generic plus Hazards synthetic suites, requiring twelve tests | Hosted scope is generic plus Hazards, not Hydrology rollback proof |
| Hydrology rehearsal | No Hydrology-specific rollback fixture or test is wired into the workflow | Hydrology carrier, role, time, identity, cross-lane, and public recovery remain unproved |
| Hydrology validation | Domain workflow runs bounded no-network shape, polarity, type-separation, identity, ambiguity, and context-routing checks | Useful changed-area evidence; not rollback, policy, proof, or release evidence |
| Candidate lane | `release/candidates/hydrology/` contains its README only | No tracked Hydrology candidate dossier exists |
| Published lane | `data/published/hydrology/` contains `.gitkeep` and its README only | No repository-tracked Hydrology release payload can be selected as affected or prior target |
| Production operator | `pipelines/rollback/main.py` is a one-line greenfield placeholder | No accepted production rollback engine exists |
| Alias auditor | `scripts/maintenance/audit_published_aliases.py` is comment-only; workflow finds no tracked current alias | No accepted live alias inventory, audit, or mutation path exists |
| Execution receipts | No operational rollback receipt lane or instance is established | No executed rollback or invalidation receipt is available |
| Hydrology policy | Mixed-maturity and evaluator-unbound | Operational rights, sensitivity, role, freshness, and release-policy evaluation remain held |
| Accountable authority | CODEOWNERS routes review to `@bartytime4life`; functional and independent stewardship is unestablished | Routing is not approval, separation of duties, or transition authority |
| Deployment/runtime | No deployment target, runtime log, external storage inventory, public alias, or public read-back was inspected | Deployed Hydrology state is `UNKNOWN`; repository absence is not deployment evidence |

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

A rollback candidate is unsafe when it restores the semantic collapse that caused the defect.

| Hydrology family | Required boundary | Rollback consequence |
|---|---|---|
| Gauge observations | Preserve parameter, unit, qualifier, provisional/final state, observed time, and retrieval time | Do not restore hidden provisional status, changed units, or stale-as-current readings |
| FEMA NFHL or comparable flood context | Regulatory context only | Never restore it as observed inundation, forecast, warning, or hydraulic-model truth |
| WBD/HUC boundaries | Versioned boundary/aggregate context with geometry identity | Metadata timestamps alone do not prove material change or safety |
| NHDPlus HR and legacy COMID bridges | Keep source-native IDs and relation cardinality distinct | Exact one-to-one may answer; split, merge, retired, unresolved, or ambiguous mappings abstain |
| Modeled or derived hydrography | Carry model/run identity and uncertainty | Never upgrade a model or derivative to observation |
| Public-safe flow fixture | Synthetic, generalized, bounded, no-alert semantics | A fixture pass does not prove a real observation or release suitability |
| Cross-lane context | Hydrology remains one bounded context; neighboring lanes retain their claims | Hydrology recovery cannot approve another lane's carrier |

> [!WARNING]
> A prior release is not safe merely because it is older, green in CI, or still stored. It must satisfy current identity, source-role, rights, sensitivity, evidence, policy, review, correction, and rollback requirements. With no safe target, recommend withdrawal or hold rather than inventing one.

[Back to top](#top)

---

<a id="rollback-decision-model"></a>

## Rollback decision model

| Vocabulary | Values | Question answered |
|---|---|---|
| Truth label | `CONFIRMED`, `PROPOSED`, `UNKNOWN`, `NEEDS VERIFICATION` | How strong is the support? |
| Candidate disposition | `ROLLBACK_CANDIDATE`, `WITHDRAWAL_CANDIDATE`, `HOLD`, `ERROR` | What recovery candidate is proposed? |
| Runtime outcome | `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` | What may a governed consumer return? |
| Work state | `HOLD`, `REPAIR_REQUIRED`, `READY_FOR_ACCOUNTABLE_REVIEW` | What should maintainers do next? |

| Condition | Candidate posture | Required note |
|---|---|---|
| A distinct prior release is immutable, digest-verifiable, admissible, supported, policy-safe, reviewable, and compatible | `ROLLBACK_CANDIDATE` | Name affected and target refs; do not execute |
| Current carrier must leave public use and no safe prior release exists | `WITHDRAWAL_CANDIDATE` | Name correction/withdrawal path and expected public outcome |
| Evidence, target, rights, sensitivity, policy, review, operator, alias, or invalidation support is unresolved | `HOLD` | List exact blockers |
| Input is malformed, contradictory, non-synthetic for the helper, or cannot be safely evaluated | `ERROR` | Record a public-safe reason code and no state change |
| A corrected successor can use the normal promotion path | Forward correction | Work recommendation, not a RollbackCard disposition |

At this repository checkpoint the default is:

```text
HOLD — PREPARE ASSESSMENT AND REVIEW HANDOFF ONLY
```

[Back to top](#top)

---

<a id="hydrology-defect-classification"></a>

## Hydrology defect classification

| Defect | Hydrology example | Bounded response | Candidate tendency |
|---|---|---|---|
| Missing or contradictory evidence | Public claim no longer resolves support | `ABSTAIN`; preserve contradiction and correction lineage | Hold, withdrawal, or supported target only |
| Source-role collapse | NFHL called observed flooding; model called measurement | Fail closed | Withdrawal or role-correct target |
| Identity ambiguity | Split, merge, retired, or unresolved relation collapsed to one answer | `ABSTAIN`; preserve all candidates | Hold; never guess |
| Temporal/freshness defect | Provisional treated as final; time kinds collapsed | Mark stale or abstain | Correction, withdrawal, or time-safe target |
| Parameter, unit, or datum defect | Wrong flow parameter/unit; datum omitted; no-data as measurement | Deny affected claim | Target must carry explicit compatible semantics |
| WBD/HUC change defect | Geometry change confused with metadata churn | Run dedicated fixture-only material-change profile | Hold or corrected successor |
| USGS API cutover defect | Endpoint family, rewrite map, dual-run, or legacy dependency inconsistent | Run dedicated fixture-only cutover profile | Hold or correction unless safe prior interface remains |
| Rights/terms change | Public redistribution basis no longer supported | `DENY` public use | Withdrawal unless a distinct admissible target exists |
| Harmful precision | Private-property, infrastructure, owner, or restricted detail exposed | Separately authorized containment; preserve audit evidence | Withdrawal or generalized successor |
| Cross-lane contamination | Hazards, Soil, Agriculture, Geology, or Infrastructure depends on defective context | Notify owning lanes; hold dependent carriers | No sibling-lane auto-approval |
| UI/AI persistence | Map, drawer, search, export, or Focus answer keeps withdrawn support | Include every carrier in invalidation scope | Hold until invalidation/read-back close |
| Integrity/tamper defect | Manifest or artifact digest differs | `ERROR`; stop | Never restore unverifiable target |

[Back to top](#top)

---

<a id="immediate-containment-and-scope-freeze"></a>

## Immediate containment and scope freeze

This prepares an accountable response; it does not grant authority to change a deployed surface.

1. Record the exact repository SHA and detection time.
2. Identify the alleged release, artifact digests, evidence refs, audience, geography, time window, and roles.
3. Separate repository state from deployment state; external storage, CDN, API, cache, and alias state remains `UNKNOWN` until inspected.
4. Inventory every affected carrier: API cache, CDN, tiles, catalog, triplets, search, vector index, AI cache, and derivatives.
5. Classify safety and source role; refer urgent/current-condition needs to the official authority.
6. Freeze target selection until current evidence, policy, role, time, rights, sensitivity, manifest, and digests are verified.
7. Choose a finite candidate disposition without mutating state.
8. Open an accountable handoff naming the missing authority, policy, review, operator, invalidation, read-back, or receipt evidence.

### Never do during assessment

- Do not edit a public alias or copy prior bytes into a published path.
- Do not delete the defective manifest, artifacts, EvidenceBundle, review, or receipts.
- Do not weaken validation to make a target pass.
- Do not use `tools/release/rollback_apply.py` outside an exact marker-protected synthetic workspace.
- Do not treat `KFM_NO_NETWORK=1` as host-level egress proof.
- Do not infer authority from CODEOWNERS, CI, a pull request, schema pass, signature, or generated prose.

[Back to top](#top)

---

<a id="operational-preconditions"></a>

## Operational preconditions

Operational rollback remains held until every applicable precondition is confirmed for one exact release and revision.

| Precondition | Evidence required | Failure posture |
|---|---|---|
| Affected release identity | Immutable manifest, artifact digests, audience, release time, public-surface inventory | `HOLD` or `ERROR` |
| Distinct target | Immutable prior manifest and artifacts; target differs from affected release | Withdrawal or `HOLD` |
| Target admissibility | Evidence, role, rights, sensitivity, time/freshness, validation, policy, review | `DENY`, `ABSTAIN`, or `HOLD` |
| Correction/withdrawal relationship | Accepted record profile and public-notice requirement | `HOLD` |
| Accountable actors | Authenticated detector, domain steward, correction reviewer, release authority, required specialists | `HOLD` |
| Active policy | Exact accepted bundle, evaluator, input, decision, obligations, consumer enforcement | `HOLD` or `DENY` |
| Accepted operator | Target/digest/review/policy/no-write/apply/idempotency/negative tests | `HOLD` |
| Published-state mechanism | Accepted alias or projection with audit and mutation semantics | `HOLD` |
| Invalidation execution | Authenticated adapters and receipts for every applicable class | `HOLD` |
| History preservation | Append-only correction and immutable evidence/review lineage | `ERROR` if history would be erased |
| Execution receipt | Accepted before/after, operations, invalidations, actor, policy, review, result profile | `HOLD` |
| Public read-back | Independent API, map, drawer, search, export, and AI verification | `HOLD` |
| Cross-lane closure | Each affected sibling lane records its own decision | Hydrology closes only its scope |

No deadline, feature value, green test, or prior publication compensates for a missing identity, safe target, evidence, rights/sensitivity decision, review, operator, correction path, invalidation proof, or receipt.

[Back to top](#top)

---

<a id="bounded-current-validation"></a>

## Bounded current validation

Run from the repository root at a recorded commit. These commands validate bounded surfaces only; they do not authorize or execute rollback.

### Dependency bootstrap

```bash
python tools/ci/install_python_ci.py project-test
```

Bootstrap may require an approved package cache or network and is separate from any no-live-source or hermetic claim.

### RollbackCard candidate profile

```bash
python tools/validators/release/validate_rollback_card.py --fixtures

python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_rollback_card.py' \
  --verbose
```

### Generic plus Hazards synthetic rehearsal

```bash
python -m unittest -q \
  tests.release.test_synthetic_rollback_rehearsal \
  tests.domains.hazards.test_synthetic_rollback_rehearsal
```

The current workflow requires twelve tests with `OK`. This is generic plus Hazards coverage, **not a Hydrology-specific rollback rehearsal**.

### Bounded Hydrology checks

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

python tools/validators/domains/hydrology/validate_aquifer_observation.py --fixtures
python tools/validators/domains/hydrology/validate_aquifer_context_link.py --fixtures
python tools/validators/domains/hydrology/validate_public_safe_flow_fixture.py \
  fixtures/domains/hydrology/public_safe_flow/valid/public_safe_flow.json
python tools/validators/domains/hydrology/validate_nhdplus_waterbody_crosswalk.py --fixtures
```

These checks prove only their committed synthetic profiles, not source admission, real Hydrology truth, complete evidence resolution, active policy, proof, release, rollback, or publication.

### Documentation links

```bash
python tools/validators/docs/link-check/check_links.py \
  --repo-root . \
  --format text \
  docs/runbooks/hydrology/ROLLBACK.md
```

The checker makes no external requests. External currentness, deployment state, and public behavior remain separate.

[Back to top](#top)

---

<a id="interpret-the-results"></a>

## Interpret the results

| Result | Establishes | Does not establish |
|---|---|---|
| Candidate validator passes | Candidate shape and local consistency | Safe target, evidence, policy, review, authority, execution, recovery |
| Generic/Hazards rehearsal passes | Deterministic synthetic mechanics and fail-closed guards for tested profiles | Hydrology-specific behavior or production rollback |
| Hydrology checks pass | Declared synthetic shape, polarity, identity, role, and context boundaries | Real release, source accuracy, evidence closure, policy, proof, rollback readiness |
| `rollback-drill` is green | Read-only checks and explicit holds behaved as declared | Operator, alias mutation, invalidation, receipt, recovery |
| Documentation merges | Repository documentation changed | Review authority, adoption, authorization, release, deployment, promotion, publication |
| No tracked public payload | Repository tree contains no such payload | No deployed or external Hydrology state exists |
| A job is skipped | It did not run | Pass or failure |
| A check is pending | No settled result exists | Success or failure |

Classify failures as **introduced**, **inherited**, **unrelated**, **skipped**, **not run**, or **needs verification**. Do not call a failure inherited merely because the changed file is Markdown.

[Back to top](#top)

---

<a id="accountable-handoff-packet"></a>

## Accountable handoff packet

Illustrative worksheet; this is not a machine contract or accepted release record.

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

Reviewers must confirm the affected release and digests, target admissibility, rollback versus withdrawal/correction choice, authenticated authority, invalidation classes, public read-back method, and every sibling lane requiring its own decision.

[Back to top](#top)

---

<a id="hydrology-recovery-requirements"></a>

## Hydrology recovery requirements

A future authorized operator must preserve these requirements; they are not current-behavior claims.

### Identity, time, and integrity

- Bind affected and target releases to immutable manifests and artifact digests.
- Reject target-equals-affected and missing-target requests.
- Preserve NHDPlus HR Permanent Identifiers and legacy COMIDs as distinct source-native families.
- Preserve exact, split, merge, complex, retired, and unresolved relation semantics.
- Bind WBD/HUC geometry and material-change evidence to explicit versions and deterministic fingerprints.
- Keep observed, valid/effective, source, retrieval, release, correction, and transaction time distinct.
- Preserve provisional/final state, parameter, units, datum, qualifiers, no-data semantics, model/run identity, uncertainty, and aggregation scope.

### Evidence, policy, review, and history

- Resolve every consequential EvidenceRef to admissible support.
- Re-evaluate current policy rather than replaying an old allow result without applicability evidence.
- Authenticate reviewers and release authority.
- Preserve role, rights, sensitivity, public precision, cross-lane, and audience obligations.
- Require a CorrectionNotice or WithdrawalNotice when public state changes materially.
- Retain affected manifests, artifacts, evidence, reviews, decisions, and receipts unless a separate lawful deletion process applies.
- Receipt every API, CDN, tile, catalog, triplet, search, vector-index, AI-cache, and derivative invalidation.
- Verify recovery independently after mutation; an operator exit code is insufficient.

### Cross-lane handoff

| Lane | Typical dependency | Required handoff |
|---|---|---|
| Hazards | Flood/drought context and stale-state interpretation | Hazards decides its own correction or withdrawal |
| Soil | Hydrologic group, moisture, drainage, wetness | Revalidate joined carriers and precision |
| Agriculture | Irrigation, drought stress, crop-water context | Preserve aggregate/model/observation distinctions |
| Geology | Aquifer and hydrostratigraphic context | Keep measurements in Hydrology and Geology-owned context separate |
| Settlements/Infrastructure | Floodplain, bridge, dam, utility, service exposure | Apply sensitivity and harmful-precision review |
| Habitat, Fauna, Flora | Riparian, wetland, aquatic habitat, occurrence, suitability | Biological lanes retain evidence and sensitivity authority |

Hydrology may notify and provide evidence. It cannot approve another lane's transition.

[Back to top](#top)

---

<a id="operational-graduation-gate"></a>

## Operational graduation gate

Remove the operational hold only through a separately reviewed, dependency-closed implementation proving all applicable gates.

- [ ] Public-safe, non-locating Hydrology rollback and withdrawal fixtures exist.
- [ ] Hydrology tests cover role, time, unit/datum, identity ambiguity, cross-lane notification, invalidation completeness, history, tamper denial, and non-synthetic denial.
- [ ] Hydrology coverage is added to `rollback-drill` without replacing generic or Hazards coverage.
- [ ] Synthetic affected and distinct prior releases are bound to immutable manifests and digests.
- [ ] The operational profile resolves evidence, policy, review, correction, target, and release references.
- [ ] An accepted release-policy bundle, evaluator, obligations, and consumer enforcement path exist.
- [ ] Actor identity and required separation of duties are authenticated and tested.
- [ ] A production operator supports deterministic plan/apply, no-write planning, idempotency, concurrency, recovery, safe paths, review/signature, target, policy, and negative tests.
- [ ] Published-state/alias profile and read-only auditor are accepted and tested before mutation.
- [ ] External invalidation adapters are least-privilege, fail closed, observable, and receipt-backed.
- [ ] An append-only execution receipt profile and validator exist in the accepted receipt home.
- [ ] API, map, Evidence Drawer, search, export, cache, and AI read-back checks prove parity.
- [ ] Correction, withdrawal, supersession, recompile, and rollback lineage remain inspectable.
- [ ] Accountable human review and exact-head hosted evidence are complete.

Synthetic drill graduation still does not authorize production rollback. Authorization, release, deployment, promotion, and publication remain separate transitions.

[Back to top](#top)

---

<a id="failure-handling-and-stop-conditions"></a>

## Failure handling and stop conditions

| Condition | Response | Required action |
|---|---|---|
| Affected release unidentified | `ERROR` or `HOLD` | Narrow scope; no mutation |
| No distinct safe target | Withdrawal or `HOLD` | Preserve history and prepare correction review |
| Evidence insufficient | `ABSTAIN` | Do not generate a claim from plausibility |
| Rights, sensitivity, or role forbids exposure | `DENY` | Prepare separately authorized containment/withdrawal handoff |
| Target/artifact digest mismatch | `ERROR` | Stop and investigate lineage |
| Synthetic marker absent or input non-synthetic | `ERROR` / helper exit `2` | Never bypass the guard |
| Invalidation list incomplete | `HOLD` or `ERROR` | Enumerate all consumers |
| Authority or policy binding absent | `HOLD` | CI, CODEOWNERS, and PRs are not authorization |
| Hydrology drill absent | Hydrology rollback `HOLD` | Implement bounded synthetic profile first |
| Changed-area failure introduced | Introduced failure | Repair before handoff |
| Hosted failure causation unclear | `NEEDS VERIFICATION` | Do not label inherited/unrelated without evidence |
| Official warning or urgent current-condition risk | Official referral | This runbook is not emergency authority |
| Public read-back cannot prove recovery | `HOLD` | Do not claim recovery |

Avoid hidden file copies, old-means-safe reasoning, schema-pass-as-authority, synthetic-as-production, green-hold-as-ready, erasing defect history, smoothing non-answers, role/time collapse, cross-lane auto-approval, repository-absence-as-deployment-evidence, and proposal prose as command authority.

[Back to top](#top)

---

<a id="maintenance-and-document-rollback"></a>

## Maintenance and document rollback

Reconcile this document when the RollbackCard profile, synthetic helper/tests, rollback workflow, Hydrology validation inventory, candidate/proof/receipt/policy/published lanes, production operator, alias/audit mechanism, invalidation adapters, correction/release decisions, source-role/time/rights/sensitivity doctrine, or deployment/runtime evidence changes.

### Known documentation follow-up

[`ROLLBACK_RUNBOOK.md`](ROLLBACK_RUNBOOK.md) remains a proposal-era document with unverified commands, paths, cadence, thresholds, and pre-mounted-repository assumptions. Preserve it as lineage until a separate compatibility review modernizes it, converts it to a redirect, or retires it with consumer and anchor closure. Do not silently maintain two operational authorities.

The one-byte [`README.md`](README.md) and stale adjacent Hydrology summaries are separate drift and remain outside this update.

### Roll back this documentation change

Revert the commit replacing this file if it misstates repository evidence, breaks local links or stable identity, overstates rollback/review/release/deployment/promotion/publication authority, conflicts with accepted Directory Rules or a later decision, or causes focused documentation checks to fail.

Reverting this Markdown does not modify a source, lifecycle object, RollbackCard, manifest, alias, cache, receipt, release, deployment, public carrier, or published state.

[Back to top](#top)

---

<a id="related-repository-surfaces"></a>

## Related repository surfaces

| Surface | Current role |
|---|---|
| [Publication Rollback Discipline](../../architecture/publication/ROLLBACK.md) | Cross-domain architecture and maturity boundary |
| [General Rollback Runbook](../ROLLBACK_RUNBOOK.md) | Proposal-era cross-domain operating lineage |
| [Hydrology proposal-era Rollback Runbook](ROLLBACK_RUNBOOK.md) | Historical plan; not current command authority |
| [Hydrology Promotion Runbook](PROMOTION_RUNBOOK.md) | Promotion readiness and operational hold |
| [Hydrology No-Network Test Runbook](NO_NETWORK_TEST_RUNBOOK.md) | Offline validation boundary |
| [Hydrology Validation](VALIDATION.md) | Adjacent guidance; current workflows/tests outrank stale prose |
| [Hydrology domain README](../../domains/hydrology/README.md) | Domain meaning, source-role, time, identity, public-use boundary |
| [RollbackCard contract](../../../contracts/release/rollback_card.md) | Candidate semantics and non-authority boundary |
| [RollbackCard schema](../../../schemas/contracts/v1/release/rollback_card.schema.json) | Closed candidate shape |
| [RollbackCard fixtures](../../../fixtures/release/rollback_card/) | Deterministic valid/invalid candidates |
| [RollbackCard validator](../../../tools/validators/release/validate_rollback_card.py) | Shape and local consistency |
| [Synthetic helper](../../../tools/release/rollback_apply.py) | Marker-protected synthetic plan/apply only |
| [Generic synthetic tests](../../../tests/release/test_synthetic_rollback_rehearsal.py) | Eight deterministic rehearsal tests |
| [`rollback-drill` workflow](../../../.github/workflows/rollback-drill.yml) | Read-only generic/Hazards readiness checks and production holds |
| [Hydrology workflow](../../../.github/workflows/domain-hydrology.yml) | Bounded fixture validation and proof/release holds |
| [Hydrology candidate lane](../../../release/candidates/hydrology/README.md) | Pre-publication review guidance; no tracked dossier at snapshot |
| [Hydrology published lane](../../../data/published/hydrology/README.md) | Released-carrier responsibility; no tracked payload at snapshot |
| [Hydrology policy boundary](../../../policy/domains/hydrology/README.md) | Mixed-maturity policy inventory and evaluator hold |

[Back to top](#top)
