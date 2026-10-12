<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbook-people-dna-land-revocation
title: People/DNA/Land Revocation Propagation Review and Closure Handoff
type: runbook
version: v1.0.0
prior_state: explicit scaffold with no review, propagation, validation, or closure-handoff procedure
status: DRAFT_REPOSITORY_GROUNDED; ONE_EXISTING_BOUNDED_SYNTHETIC_PROPAGATION_PROFILE_EXECUTABLE; REAL_REVOCATION_STATUS_RESOLUTION_EXECUTION_CLEANUP_AND_CLOSURE_HELD; NON_RELEASE; NON_PUBLICATION
owners:
  - "@bartytime4life — verified GitHub review route"
  - "NEEDS VERIFICATION — accountable People/DNA/Land, privacy, consent, legal, Indigenous/Tribal, policy, evidence, source, data-custody, security, operations, release, and independent-review assignments"
created: 2026-08-28
updated: 2026-08-28
policy_label: repository-facing; sensitive-domain; consent-revocation; synthetic-fixture-only; fail-closed; no-cleanup-execution; non-release; non-publication
current_path: docs/runbooks/people-dna-land/revocation.md
owning_root: docs/
responsibility: Human procedure for reviewing the repository's bounded synthetic consent-revocation propagation assessment and preparing a minimized closure handoff without resolving real consent status, executing revocation or cleanup, changing lifecycle or release state, or claiming operational closure.
truth_posture: cite-or-abstain
authority_class: explanatory operational documentation
authority_rank: subordinate to accepted doctrine and ADRs, semantic contracts, schemas, policy, consent and rights authority, evidence, accountable review, lifecycle, correction, withdrawal, release, rollback, deployment, and publication authorities
canonical_relationship: same-path replacement of an explicit scaffold; no sibling policy, contract, receipt, cleanup, release, or proof authority created
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: f68fe0ff504562bb8d2b4aedacb3d46eb66f17f3
  target_prior_blob: 4f8d5957114e3e8c5c90e5f226e7df0fdc5c837d
  lane_index_prior_blob: 30c4bf4c16ff46e118e439bf0ee4498a8c274737
  consent_runbook_blob: e1670ce137abfef004682ff63e0449f091c95b17
  propagation_contract_blob: dbf1fdff6585f3db4213c17d8f18bfc81ecec04d
  propagation_schema_blob: e976211d1bf536b2aae7901842474dbcb1c3a484
  propagation_fixture_blob: bb3b15effa7e73762f57035339d2e106be47178c
  propagation_validator_blob: 76c7805428f253a7a711c7bc68a27e9cbcce40e7
  propagation_test_blob: bceeef36e5c4e456e6f8a3fc192cd1c349d34fb5
  tests_readme_blob: 77bb1bfd3d3e576bc975c91bbe46dd3e6d8fee52
  domain_workflow_blob: bcf64c3e3b6653b9543489fc5a6031805ae3ef48
  verified_real_revocation_status_resolver: NONE_AT_PINNED_REVISION
  verified_cleanup_executor: NONE_AT_PINNED_REVISION
  verified_action_receipt_resolver: NONE_AT_PINNED_REVISION
  verified_operational_closure_proof: NONE_AT_PINNED_REVISION
related:
  - ./README.md
  - ./CONSENT_RUNBOOK.md
  - ./LIVING_PERSON_REVIEW.md
  - ./NO_NETWORK_TEST_RUNBOOK.md
  - ./ROLLBACK_RUNBOOK.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../domains/people-dna-land/CONSENT_MODEL.md
  - ../../domains/people-dna-land/DNA_HANDLING.md
  - ../../../contracts/domains/people-dna-land/consent_revocation_propagation_assessment.md
  - ../../../schemas/contracts/v1/domains/people-dna-land/consent_revocation_propagation_assessment.schema.json
  - ../../../fixtures/domains/people-dna-land/consent_revocation_propagation/README.md
  - ../../../fixtures/domains/people-dna-land/consent_revocation_propagation/cases.json
  - ../../../tests/domains/people-dna-land/consent/revocation/test_consent_revocation_propagation_assessment.py
  - ../../../tools/validators/domains/people-dna-land/validate_consent_revocation_propagation_assessment.py
  - ../../../policy/consent/people-dna-land/README.md
  - ../../../.github/workflows/domain-people-dna-land.yml
non_effects:
  - does_not_issue_amend_suspend_or_revoke_real_consent
  - does_not_authenticate_a_subject_representative_rights_holder_or_community_authority
  - does_not_access_real_people_genealogy_dna_land_consent_or_culturally_restricted_payloads
  - does_not_activate_or_replace_policy
  - does_not_resolve_or_authenticate_receipts
  - does_not_execute_blocking_invalidation_purge_deletion_erasure_notification_or_withdrawal
  - does_not_mutate_raw_work_quarantine_processed_catalog_triplet_or_published_state
  - does_not_establish_evidence_rights_sensitivity_review_release_or_publication_closure
  - does_not_release_deploy_promote_or_publish
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# People/DNA/Land Revocation Propagation Review and Closure Handoff

Use this runbook to review the repository's **existing synthetic consent-revocation propagation assessment** at an exact revision and prepare a minimized, fail-closed handoff. It is a human review procedure. It is not a revocation endpoint, consent authority, policy runtime, cleanup executor, receipt verifier, incident-response service, release controller, or proof that revocation is complete.

> [!CAUTION]
> Do not place real names, family relationships, DNA or genomic values, raw kit or vendor identifiers, consent credentials, revocation records, private addresses, exact locations, person-parcel joins, disputed title details, protected cultural information, or proprietary source excerpts in this runbook, Git, pull requests, issues, CI logs, fixtures, screenshots, or public artifacts.

> [!IMPORTANT]
> **A declared revocation is not operational closure.** Keep these states separate: consent status observed; next use denied; propagation assessed; actions executed; action receipts resolved; derivatives verified absent or inaccessible; correction or withdrawal completed; release state changed. The current repository proves only a bounded synthetic assessment of declared states and receipt references.

**Navigation:** [Authority](#1-purpose-and-authority-boundary) · [Evidence](#2-current-repository-evidence) · [States](#3-state-and-terminology-boundary) · [Stop](#4-mandatory-stop-conditions) · [Inputs](#5-trigger-and-required-inputs) · [Matrix](#6-declared-propagation-matrix) · [Procedure](#7-review-procedure) · [Validation](#8-bounded-synthetic-validation) · [Results](#9-result-interpretation-and-closure-claims) · [Record](#10-minimum-result-record) · [Gaps](#11-operational-graduation-gaps) · [Acceptance](#12-acceptance-criteria) · [Maintenance](#13-maintenance-correction-and-documentation-rollback)

## 1. Purpose and authority boundary

Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts the [Directory Rules](../../doctrine/directory-rules.md). The existing path is therefore retained under `docs/runbooks/` as the human-procedure home. Contracts, schemas, policy, fixtures, tests, validators, data, evidence, receipts, proofs, release decisions, and runtime operations retain their own responsibility roots.

This same-path replacement may:

- explain the current fixture-only propagation contract and its limitations;
- route reviewers to the exact schema, fixture manifest, validator, test, and workflow;
- require the closed seven-surface dependency inventory;
- distinguish declared state from execution and closure;
- define fail-closed stop conditions and review steps;
- record an exact-head validation result; and
- prepare a minimized handoff to accountable authorities.

It may not:

- determine that a real consent grant is authentic, current, legally sufficient, or held by an authorized person;
- recognize authority on behalf of an Indigenous Nation, Tribe, descendant community, family member, joint holder, or representative;
- issue, amend, suspend, expire, revoke, or restore consent;
- activate, replace, or bypass policy;
- establish identity, kinship, DNA support, residence, ownership, title, legal boundary, source rights, or EvidenceBundle closure;
- execute denial, invalidation, purge, deletion, erasure, notification, withdrawal, correction, release replacement, or rollback;
- authenticate a referenced status, revocation, or action receipt;
- declare operational closure from a passing fixture profile; or
- change lifecycle, release, deployment, promotion, or publication state.

The broader [consent review runbook](./CONSENT_RUNBOOK.md) owns review of a precisely scoped consent question. This file owns the **detailed human review of the existing synthetic propagation profile and its closure handoff**. Neither file executes revocation.

[Back to top](#top)

## 2. Current repository evidence

The following state was pinned at `main@f68fe0ff504562bb8d2b4aedacb3d46eb66f17f3`.

| Surface | Confirmed state | Safe conclusion |
|---|---|---|
| [Propagation semantic contract](../../../contracts/domains/people-dna-land/consent_revocation_propagation_assessment.md) | Proposed, inactive, synthetic-fixture-only contract over a closed seven-surface inventory | KFM can assess declared local consistency; the contract creates no consent, cleanup, policy, release, or publication authority |
| [Propagation schema](../../../schemas/contracts/v1/domains/people-dna-land/consent_revocation_propagation_assessment.schema.json) | Draft 2020-12 shape with fixed consent states, dependency order, outcomes, limitations, and false authority claims | Schema validity constrains the fixture object; it does not authenticate its references or prove execution |
| [Fixture manifest](../../../fixtures/domains/people-dna-land/consent_revocation_propagation/cases.json) | Seventeen synthetic positive and negative cases covering active, mismatched, revoked, expired, unknown, error, receipt, ordering, hash, and authority-overclaim paths | The repository has deterministic test material without real people, DNA, credentials, locations, or consent records |
| [Validator](../../../tools/validators/domains/people-dna-land/validate_consent_revocation_propagation_assessment.py) | Deterministic local validator for schema, hash, time, scope, dependency, outcome, and receipt-reference coherence | A `PASS` proves declared fixture consistency only; receipt resolution and action execution are outside the validator |
| [Test](../../../tests/domains/people-dna-land/consent/revocation/test_consent_revocation_propagation_assessment.py) | Repository-owned synthetic test profile | A green test is exact-revision behavior evidence, not real revocation or cleanup proof |
| [Domain workflow](../../../.github/workflows/domain-people-dna-land.yml) | Executes two bounded synthetic consent profiles and explicitly holds broader policy runtime, proof, revocation execution, cleanup, and release | This runbook routes one of the two existing profiles; it does not add a third profile |
| [Consent-policy boundary](../../../policy/consent/people-dna-land/README.md) | Documentation exists, but repository presence is not policy activation and runtime binding remains unproved | Do not present the synthetic assessment as active production policy |
| [Rollback runbook](./ROLLBACK_RUNBOOK.md) | Repository-grounded hold boundary; operational rollback is unavailable | Revocation, withdrawal, correction, deletion, and rollback remain distinct |
| Real status resolver, action executor, receipt resolver, dependency crawler, closure proof | No verified complete path was established at the pinned revision | Real or operational use remains `HOLD` and requires accountable escalation |

The April 2026 People/Genealogy/DNA/Land architecture blueprint remains useful proposal lineage for `ConsentGrant`, `RevocationReceipt`, affected artifacts, and cleanup-action concepts. It was prepared without a mounted repository, so it does not override the current contract, schema, validator, tests, workflow, or holds.

[Back to top](#top)

## 3. State and terminology boundary

Use the repository contract's terms exactly when describing the synthetic object.

### 3.1 Consent status and assessment outcome

| Consent status | Declared assessment outcome | Meaning in the current fixture profile |
|---|---|---|
| `ACTIVE` with every scope dimension matched | `SATISFIED` | The consent dimension is declared current and in scope; every other gate remains independent |
| `ACTIVE` with any scope mismatch | `DENY` | The requested use is outside the declared consent scope |
| `REVOKED` | `DENY` | Next consequential use is denied and materialized derivatives require declared invalidation or purge actions |
| `EXPIRED` | `DENY` | Next consequential use is denied and materialized derivatives require declared invalidation or purge actions |
| `UNKNOWN` | `ABSTAIN` | Current status cannot be established; surfaces remain blocked or pending review |
| `ERROR` | `ERROR` | Evaluation failed; surfaces remain blocked or pending review |

The seven scope dimensions are `purpose`, `operation`, `fields`, `relationships`, `audience`, `retention`, and `time`. A consent result cannot fill an evidence, rights, sensitivity, policy, review, lifecycle, release, correction, rollback, deployment, or publication gap.

### 3.2 Dependency state and action vocabulary

The dependency order is closed and exact:

`READ` → `ANSWER` → `EXPORT` → `TILE` → `GRAPH` → `INDEX` → `CACHE`

The fixture schema permits these declared states:

- `READY`
- `BLOCKED`
- `INVALIDATED`
- `PURGED`
- `PENDING`

The fixture schema permits these declared actions:

- `NONE`
- `DENY_NEXT_USE`
- `INVALIDATE`
- `PURGE`
- `REVIEW`

These values are **assessment declarations**. They do not prove a deployed action happened.

### 3.3 Revocation, withdrawal, correction, erasure, and rollback

Keep the following distinct:

| State or action | Meaning | This runbook's authority |
|---|---|---|
| Revocation | A consent grant is declared withdrawn or no longer usable | Review a synthetic declaration only |
| Expiry | A consent grant is outside its validity interval | Review a synthetic declaration only |
| Deny next use | Prevent another consequential read, answer, or export | Verify the fixture expectation; do not execute |
| Invalidate or purge derivative | Make a tile, graph, index, or cache unusable or absent | Verify the fixture declaration; do not execute |
| Withdrawal or correction | Change the governed availability or claims of released material | Route to owning authority |
| Tombstone | Preserve minimized supersession or audit lineage without restating protected content | Proposal/policy lineage; no executor established here |
| Erasure or deletion | Physically remove material under an applicable authority | Separate legal, policy, custody, and operations decision |
| Rollback | Restore a prior governed system or release state | Separate held procedure |

A tombstone is not erasure. Revocation is not automatically deletion. Rollback is not a substitute for revocation, withdrawal, correction, or incident containment.

[Back to top](#top)

## 4. Mandatory stop conditions

Stop without copying sensitive details into repository-visible surfaces when any of these conditions applies:

- the case involves a real person, real DNA or genomic material, a real consent credential, a real revocation record, or a real private person-land relationship;
- subject, holder, representative, joint-holder, family-member, community, Indigenous, Tribal, or rights-holder authority is unresolved;
- the status source, observation time, validity interval, or revocation evidence cannot be authenticated in the approved system;
- purpose, operation, fields, relationships, audience, retention, or time scope is missing or ambiguous;
- rights, source terms, sensitivity, living status, harmful precision, cultural protocol, sovereignty, legal hold, embargo, custody, or retention is unresolved;
- the affected dependency inventory is incomplete or does not include all known reads, answers, exports, tiles, graphs, indexes, caches, generated summaries, replicas, and public carriers;
- an action receipt is absent, unresolved, unauthenticated, stale, or inconsistent with the declared action;
- a command would call a live provider, use a credential, inspect a restricted payload, write lifecycle state, or mutate a deployed system;
- a repository-visible fixture, log, screenshot, issue, or pull request would expose protected values;
- deletion, erasure, notification, withdrawal, correction, release replacement, cache purge, graph cleanup, index cleanup, or rollback must actually occur;
- the current contract, schema, fixture, validator, test, or workflow no longer matches the pinned revision; or
- a passing test is being treated as legal, policy, review, release, or operational approval.

Use `HOLD` when required support or execution is unresolved. Use `ESCALATE` when an accountable authority or approved handling environment is required. Use the contract's `ABSTAIN`, `DENY`, or `ERROR` only for the assessment outcome it actually defines.

[Back to top](#top)

## 5. Trigger and required inputs

Run this procedure only for one bounded review trigger:

- synthetic `REVOKED`;
- synthetic `EXPIRED`;
- synthetic `UNKNOWN`;
- synthetic `ERROR`;
- synthetic active consent with a scope mismatch; or
- review of a proposed documentation change affecting the propagation profile.

Record only minimized, non-sensitive facts.

| Input | Requirement |
|---|---|
| Repository identity | Exact commit SHA, branch or pull-request head, and affected repository paths |
| Validation identity | `HEAD`, `MERGE_RESULT`, `STALE`, or `NOT_RUN` |
| Material posture | `synthetic_fixture_only`; stop for real or source-derived sensitive material |
| Trigger | One status or scope-mismatch condition |
| Status observation | Opaque status receipt reference plus observed and evaluation times; do not include credential bodies |
| Revocation reference | Required by the synthetic contract for `REVOKED`; treat it as an unresolved assertion unless separately verified |
| Scope review | Purpose, operation, fields, relationships, audience, retention, and time |
| Dependency inventory | The exact seven ordered surfaces required by the fixture profile |
| Declared action references | Opaque action receipt references where the fixture requires them |
| Independent gates | Evidence, rights, sensitivity, policy, accountable review, lifecycle, release, correction, withdrawal, rollback, deployment, and publication |
| Next authority | One named review class or owning system, not an invented individual |

Do not add real names, dates of birth, family links, kit IDs, genomic values, addresses, coordinates, parcel-owner relationships, tokens, signatures, protected cultural details, or proprietary excerpts.

[Back to top](#top)

## 6. Declared propagation matrix

The matrix below restates the current semantic contract and validator behavior. It does not create a runtime plan.

| Trigger | `READ`, `ANSWER`, `EXPORT` | `TILE`, `GRAPH`, `INDEX`, `CACHE` | Receipt expectation | Closure statement |
|---|---|---|---|---|
| `ACTIVE` and all scope dimensions match | `READY` / `NONE` | `READY` / `NONE` | No action receipt | Consent dimension only; continue to independent gates |
| `ACTIVE` with any scope mismatch | `BLOCKED` / `DENY_NEXT_USE` | `BLOCKED` / `DENY_NEXT_USE` | Action receipt reference on every surface | Requested use denied; execution and closure not proved |
| `REVOKED` | `BLOCKED` / `DENY_NEXT_USE` | `INVALIDATED` / `INVALIDATE` or `PURGED` / `PURGE` | Revocation receipt reference plus action receipt reference on every surface | Declared propagation is internally consistent only |
| `EXPIRED` | `BLOCKED` / `DENY_NEXT_USE` | `INVALIDATED` / `INVALIDATE` or `PURGED` / `PURGE` | Action receipt reference on every surface | Declared propagation is internally consistent only |
| `UNKNOWN` | `BLOCKED` / `DENY_NEXT_USE` or `PENDING` / `REVIEW` | `BLOCKED` / `DENY_NEXT_USE` or `PENDING` / `REVIEW` | A blocked surface requires an action receipt reference | Fail closed; status and closure unresolved |
| `ERROR` | `BLOCKED` / `DENY_NEXT_USE` or `PENDING` / `REVIEW` | `BLOCKED` / `DENY_NEXT_USE` or `PENDING` / `REVIEW` | A blocked surface requires an action receipt reference | Fail closed; evaluation and closure unresolved |

The validator checks declaration coherence and reference presence. It does not resolve the references, call the actions, inspect deployed surfaces, or prove protected material is absent.

[Back to top](#top)

## 7. Review procedure

### 7.1 Freeze the review boundary

1. Record the exact repository SHA and target paths.
2. Confirm the target is the existing synthetic contract, schema, fixture, validator, test, workflow, or its documentation.
3. Search for open overlapping work on those paths.
4. Confirm no real or source-derived sensitive payload is present.
5. Confirm the action is review-only and has no external or lifecycle effect.
6. Stop if any accountable authority, restricted environment, or operational executor is required.

### 7.2 Select and materialize one synthetic case

Use the repository fixture manifest and validator. Do not invent a new status, surface, action, outcome, reason code, authority claim, or cleanup behavior in prose.

For an existing fixture case:

1. identify the case name;
2. verify its inherited base and patch;
3. confirm its expected validator outcome and codes;
4. confirm the generated `profile_spec_hash` is deterministic; and
5. confirm no protected value has entered the fixture.

A new case belongs with the fixture, validator, and test owners—not in this documentation-only procedure.

### 7.3 Verify the consent and time declaration

Confirm:

- `observed_at` is not after `evaluated_at`;
- an active grant has `valid_until`;
- an active grant is not evaluated after `valid_until`;
- `REVOKED` carries a revocation receipt reference;
- the expected status reason code is present; and
- reason codes are canonical and sorted as required by the validator.

This validates fixture semantics only. It does not authenticate the status source or receipt.

### 7.4 Verify scope and dependency closure

Confirm all seven scope dimensions are present and the dependency list is exactly ordered:

1. `READ`
2. `ANSWER`
3. `EXPORT`
4. `TILE`
5. `GRAPH`
6. `INDEX`
7. `CACHE`

An omitted, reordered, duplicated, or additional surface fails the current closed profile. Do not normalize it by assumption.

### 7.5 Verify declared actions and receipt references

For every surface:

1. compare the declared state/action pair with [§6](#6-declared-propagation-matrix);
2. verify the fixture includes an action receipt reference where required;
3. record that the reference is **unresolved by this profile**;
4. do not infer that an executor ran; and
5. do not infer that a derivative is inaccessible merely because its fixture state says `INVALIDATED` or `PURGED`.

### 7.6 Preserve independent gates

Before handing off, record separate states for:

- identity and representative authority;
- evidence and provenance;
- rights and source terms;
- sensitivity, privacy, sovereignty, cultural protocol, and harmful precision;
- policy runtime and obligations;
- lifecycle state;
- correction, withdrawal, tombstone, retention, deletion, and erasure;
- release and rollback;
- deployment and publication; and
- accountable and independent review.

No consent or propagation result fills these fields automatically.

### 7.7 Run the bounded checks and interpret

Run [§8](#8-bounded-synthetic-validation), classify the exact revision, then prepare the minimized record in [§10](#10-minimum-result-record). Keep closure unasserted unless a separate operational authority provides verified evidence for every required action and affected surface.

[Back to top](#top)

## 8. Bounded synthetic validation

The [no-network runbook](./NO_NETWORK_TEST_RUNBOOK.md) owns the wider test-egress caveat. The current repository profile is deterministic and uses repository-owned synthetic fixtures. This is not proof of runner-wide firewalling, subprocess isolation, dependency-install isolation, or deployed-system behavior.

From a clean checkout at the exact SHA under review:

```bash
git rev-parse HEAD
git status --short

export KFM_NO_NETWORK=1
export PYTHONDONTWRITEBYTECODE=1
export PYTHONHASHSEED=0

python \
  tests/domains/people-dna-land/consent/revocation/test_consent_revocation_propagation_assessment.py \
  --verbose

python \
  tools/validators/domains/people-dna-land/validate_consent_revocation_propagation_assessment.py \
  --fixtures
```

### Validation identity

| Identity | Meaning |
|---|---|
| `HEAD` | The tested SHA is the exact branch head |
| `MERGE_RESULT` | The tested SHA is a synthetic pull-request merge result and is labeled as such |
| `STALE` | The branch head changed after testing |
| `NOT_RUN` | The command or environment was unavailable |

A green result proves only:

- schema-valid fixture materialization;
- deterministic profile hashing;
- exact finite outcome behavior;
- current local time, scope, dependency, state/action, limitation, and authority-claim checks;
- expected positive and negative case polarity; and
- the named no-network synthetic profile at the tested revision.

It does not prove:

- a production consent store or status resolver;
- authentic subject or representative authority;
- receipt authenticity;
- action execution;
- deployed derivative discovery or cleanup;
- policy activation;
- EvidenceBundle closure;
- rights or sensitivity clearance;
- correction, withdrawal, erasure, release, rollback, deployment, or publication safety.

[Back to top](#top)

## 9. Result interpretation and closure claims

Keep four axes distinct.

| Axis | Values | Meaning |
|---|---|---|
| Test execution | `PASS`, `FAIL`, `NOT_RUN` | Whether the named test and validator behaved as expected |
| Assessment outcome | `SATISFIED`, `DENY`, `ABSTAIN`, `ERROR` | The finite outcome declared by the synthetic contract |
| Work state | `PROCEED_TO_OTHER_GATES`, `HOLD`, `ESCALATE` | Human review routing only; not a machine policy decision |
| Closure claim | `NOT_ASSERTED` | This runbook never declares operational closure |

### Required interpretation

| Condition | Test result | Assessment | Work state | Required statement |
|---|---|---|---|---|
| Existing positive fixture validates | `PASS` | Fixture-declared outcome | `HOLD` or `PROCEED_TO_OTHER_GATES` as applicable | Declared synthetic consistency only |
| Expected negative fixture is rejected with exact codes | `PASS` for the test suite | Candidate denied or errored | `HOLD` | Negative behavior worked at the tested SHA |
| Positive fixture unexpectedly fails | `FAIL` | Do not reinterpret | `HOLD` | Profile regression or stale expectation |
| Negative fixture is accepted | `FAIL` | Unsafe | `HOLD` and escalate | Fail-open regression |
| Current status is unknown | Test may pass | `ABSTAIN` | `HOLD` or `ESCALATE` | Consequential surfaces remain blocked or pending |
| Evaluation fails | Test may pass | `ERROR` | `HOLD` | Preserve the error; do not convert it to denial or allow |
| Real material or real action is required | Not determined here | Not determined here | `ESCALATE` | Use an approved environment and accountable authority |
| Receipts are merely syntactically present | Test may pass | No additional authority | `HOLD` | Receipt resolution and action proof remain missing |

Never write “revocation completed,” “all derivatives removed,” “consent withdrawn everywhere,” or equivalent language from this profile alone.

[Back to top](#top)

## 10. Minimum result record

The following is an **illustrative repository-safe handoff**, not a canonical schema:

```yaml
handoff_ref: "opaque-review-reference"
repository_sha: "<exact-sha>"
affected_paths:
  - "<repository path only>"
material_posture: "synthetic_fixture_only"
fixture_case: "<existing-case-name>"
validation:
  identity: "HEAD | MERGE_RESULT | STALE | NOT_RUN"
  result: "PASS | FAIL | NOT_RUN"
  commands:
    - "test_consent_revocation_propagation_assessment.py --verbose"
    - "validate_consent_revocation_propagation_assessment.py --fixtures"
assessment:
  consent_status: "ACTIVE | REVOKED | EXPIRED | UNKNOWN | ERROR"
  declared_outcome: "SATISFIED | DENY | ABSTAIN | ERROR"
  reason_codes:
    - "<contract-compatible non-sensitive code>"
dependency_review:
  inventory: ["READ", "ANSWER", "EXPORT", "TILE", "GRAPH", "INDEX", "CACHE"]
  declarations_match_profile: true
  action_receipt_refs_present: true
  action_receipts_resolved: false
  actions_executed: false
independent_gates:
  identity_authority: "UNRESOLVED | HELD | SEPARATELY_VERIFIED"
  evidence: "UNRESOLVED | HELD | SEPARATELY_VERIFIED"
  rights: "UNRESOLVED | HELD | SEPARATELY_VERIFIED"
  sensitivity_and_sovereignty: "UNRESOLVED | HELD | SEPARATELY_VERIFIED"
  policy_runtime: "UNRESOLVED | HELD | SEPARATELY_VERIFIED"
  accountable_review: "UNRESOLVED | HELD | SEPARATELY_VERIFIED"
  correction_withdrawal_release: "HELD"
work_state: "PROCEED_TO_OTHER_GATES | HOLD | ESCALATE"
closure_claim: "NOT_ASSERTED"
limitations:
  - "CONSENT_DIMENSION_ONLY"
  - "NO_CLEANUP_EXECUTION"
  - "NO_EVIDENCE_OR_POLICY_AUTHORITY"
  - "NO_REAL_PERSON_OR_DNA_DATA"
  - "NO_RELEASE_OR_PUBLICATION_AUTHORITY"
next_action: "<one bounded review action or stop reason>"
```

The human-only fields in this example do not extend the semantic contract. Opaque references must not encode protected values.

[Back to top](#top)

## 11. Operational graduation gaps

This procedure must remain review-only until current implementation evidence establishes all of the following in their owning roots:

1. an authenticated consent-status source with subject, holder, representative, dispute, suspension, expiry, and revocation semantics;
2. approved handling for real living-person, DNA/genomic, land-linked, and culturally restricted material;
3. accepted consent-policy placement, machine inputs, runtime evaluation, reason codes, obligations, and fail-closed integration;
4. a complete runtime dependency inventory beyond the current seven-surface fixture profile, including replicas, generated products, exports, backups, and external consumers as applicable;
5. authorized action executors for blocking, invalidation, purge, withdrawal, correction, notification, retention, deletion, or erasure;
6. authenticated action receipts plus a resolver that verifies actor, target, time, effect, and result without exposing protected content;
7. post-action verification that every required derivative or carrier is absent, inaccessible, superseded, or correctly restricted;
8. EvidenceRef-to-EvidenceBundle closure and independent rights, sensitivity, sovereignty, source-role, and living-person review;
9. correction, withdrawal, release, rollback, and public-cache integration that preserves visible lineage;
10. an accepted tombstone-versus-erasure decision path and retention policy;
11. accountable privacy, consent, Indigenous/Tribal, legal, domain, evidence, policy, custody, security, operations, release, and independent-review roles with separation of duties; and
12. a no-production rehearsal that exercises the real dependency and receipt paths without being mistaken for operational completion.

Missing any item keeps operational revocation closure at `HOLD`.

[Back to top](#top)

## 12. Acceptance criteria

This documentation update is ready for accountable review when:

1. it replaces the explicit scaffold at the established path without creating a parallel authority;
2. it accurately describes the current contract, schema, fixture, validator, test, and workflow;
3. it preserves the exact seven-surface inventory and finite assessment outcomes;
4. it distinguishes status observation, declared propagation, action execution, receipt resolution, and closure;
5. it includes exact current synthetic commands and validation-identity rules;
6. it keeps real data, policy activation, cleanup execution, legal sufficiency, release, deployment, and publication outside its authority;
7. it fails closed on missing status, scope, dependency, receipt, evidence, rights, sensitivity, authority, or execution support;
8. its illustrative record contains no sensitive values and does not extend the machine contract;
9. directly related navigation classifies this as one human runbook over an existing profile, not a new executable capability; and
10. documentation rollback remains reversible and distinct from real revocation or operational rollback.

[Back to top](#top)

## 13. Maintenance, correction, and documentation rollback

Re-review this file when any of the following changes:

- the semantic contract or schema;
- consent-state, scope, dependency, state/action, outcome, reason-code, limitation, or authority-claim vocabulary;
- fixture case inventory or inheritance;
- validator hashing, parsing, time, receipt, or dependency behavior;
- test entry points or workflow wiring;
- no-network controls;
- policy placement, bundle activation, evaluator binding, or obligation enforcement;
- real status, receipt, action, dependency, cleanup, notification, correction, withdrawal, retention, deletion, erasure, release, or rollback implementation;
- accountable ownership or approved sensitive-data handling; or
- the local runbook index.

Before merge, close the draft pull request and delete only its task-owned branch. After an authorized merge, revert the focused documentation commit or submit a reviewed forward correction. Either action changes documentation only. It does not restore consent, undo a revocation, resurrect deleted material, reverse cleanup, re-enable a derivative, withdraw or restore a release, or change public state.

The prior scaffold remains in Git history. Restoring it would remove this review guidance without changing any contract, schema, fixture, validator, test, workflow, policy, data, receipt, release, deployment, or publication state.

[Back to top](#top)
