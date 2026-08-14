<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/adr-0024-steward-separation-of-duties-for-release
title: ADR-0024 — Steward Separation of Duties for Release
type: adr
adr_id: ADR-0024
version: v1.3
status: draft
effective_decision_status: proposed
owners:
  - "OWNER_TBD — architecture decision owner"
  - "OWNER_TBD — release and publication steward"
  - "OWNER_TBD — governance and review steward"
  - "OWNER_TBD — evidence, policy, sensitivity, rights, correction, rollback, validation, and security stewards"
owner_status: "CODEOWNERS routes affected roots to @bartytime4life, but no accepted StewardshipAssignment, independent release approver, reviewer quorum, or operational actor-identity authority was verified"
reviewers_required:
  - Architecture steward
  - Docs steward
  - Release and publication steward
  - Governance and review steward
  - At least one affected domain or data steward
  - Evidence steward
  - Policy and sensitivity steward
  - Rights or sovereignty reviewer when applicable
  - Correction and rollback steward
  - Contracts and schemas stewards
  - Validation and CI steward
  - Security reviewer for actor identity, signatures, trust roots, or repository-control changes
created: 2026-05-15
updated: 2026-08-14
policy_label: public
truth_posture: cite-or-abstain
responsibility_root: docs/
owning_root: docs/
responsibility: "Records the proposed release separation-of-duties decision, actor/authority/subject-binding requirements, control-maturity model, current bounded proof surfaces, and remaining operational holds without creating approval or release authority."
current_path: docs/adr/ADR-0024-steward-separation-of-duties-for-release.md
supersedes: []
superseded_by: []
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: c9ccb11ded141edbd79763982056a1e6f90b8866
  target_prior_blob: 69b4a7228eb4abcc62a35dbbbeeeeddb04ab30d2
  adr_index_blob: 938c5894c36b99e14810918e2c550ab0e92d53b1
  adr_0029_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  repository_ruleset_id: 15484585
  repository_ruleset_name: Protect
  repository_ruleset_updated_at: 2026-07-29T13:00:55.368-05:00
  review_record_contract_blob: 9641345d1e5d939dc59687a900e60a563d92c4f0
  review_record_schema_blob: fe2f2223af46481e7fb19b0baa94f62ce9c6c855
  stewardship_assignment_contract_blob: 80c6fd4149deeb4172e2401dfaf741226380f085
  stewardship_assignment_schema_blob: bd12f7e5e8eea966306c250d992f2826693815c9
  review_authority_binding_contract_blob: f156e100660e9fd97ca95e90092143a3cd6d62ee
  review_authority_binding_schema_blob: 9407b357120537230aa4ef80a844ecf5149acc70
  review_authority_binding_fixtures_blob: 17ce1922ee6dee366a18de8d13d735dfd6b9680b
  review_authority_binding_validator_blob: a5e7c62dc4049b07a7ef8a3dec266f0b44ac58a6
  review_authority_binding_tests_blob: b70f696b984532fd304ff188f2c3ef2346d3f33d
  review_authority_binding_workflow_blob: d0dd3ea0900bf5a664bbf3e092735f8889ed6e41
  review_authority_binding_latest_main_run: 31654972756
  sensitive_release_review_contract_blob: 235ca86dd807c6842ca8c861f995371fe7758f64
  sensitive_release_review_schema_blob: 26321c9794dd5bf054a2aa6230a8b65724ef1c8f
  sensitive_release_review_fixtures_blob: 1c2b7fb06d2f604c5dfcdb0430422fb4bdf8ac24
  sensitive_release_review_validator_blob: d2209b353950bee801befc8c76e981869af1da03
  sensitive_release_review_tests_blob: 13b172e538ab1e99d124ad8ad8a12296908f935f
  sensitive_release_review_workflow_blob: cc47e292f20a3a27c97430800f1a0a1c5a8c6a95
  sensitive_release_review_latest_main_run: 31654972404
  release_policy_readme_blob: 8a6a91e18f29f6f961eac88270b385a95b86281e
inspection_boundary: >
  Current-session GitHub reads of the ADR inventory, accepted Directory Rules decision and bytes,
  target ADR, CODEOWNERS, active default-branch ruleset, ReviewRecord and StewardshipAssignment
  semantic/schema surfaces, ReviewAuthorityBinding and SensitiveReleaseReviewClosure contracts,
  schemas, fixtures, validators, tests, workflows, latest main workflow jobs/logs, and release-policy
  documentation. Supplied Atlas and Encyclopedia material remains design lineage. No actor was
  authenticated, no alias or conflict registry was resolved, no accepted stewardship assignment or
  SoD policy was evaluated, no governed release ReviewRecord was issued, and no promotion, release,
  correction, rollback, deployment, publication, or public-state mutation was exercised.
source_lineage:
  - KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas.pdf — Chapter 24 reviewer/SoD matrix and ADR-S-09 backlog
  - kfm_encyclopedia.pdf — Master Action Matrix separating steward, reviewer, policy admin, release manager, developer, and AI duties
related:
  - docs/adr/README.md
  - docs/adr/INDEX.md
  - docs/adr/ADR-0010-deny-by-default-for-dna-rare-species-archaeology-infrastructure.md
  - docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - docs/adr/ADR-0015-data-published-_domain_-current-alias-is-governed-by-rollback_card.md
  - docs/adr/ADR-0018-promotion-gate-sequence.md
  - docs/adr/ADR-0020-abstain-is-a-first-class-decision.md
  - docs/adr/ADR-0023-geo-manifest-signs-every-pmtiles-cog-release.md
  - docs/adr/ADR-0025-public-client-never-reads-canonical-internal-stores.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/doctrine/directory-rules.md
  - docs/governance/SEPARATION_OF_DUTIES.md
  - contracts/governance/ReviewRecord.md
  - contracts/governance/steward_assignment.md
  - contracts/governance/review_authority_binding.md
  - contracts/governance/sensitive_release_review_closure.md
  - schemas/contracts/v1/governance/review_record.schema.json
  - schemas/contracts/v1/governance/steward_assignment.schema.json
  - schemas/contracts/v1/governance/review_authority_binding.schema.json
  - schemas/contracts/v1/governance/sensitive_release_review_closure.schema.json
  - fixtures/contracts/v1/governance/review_authority_binding/cases.json
  - fixtures/contracts/v1/governance/sensitive_release_review_closure/cases.json
  - tools/validators/governance/validate_review_authority_binding.py
  - tools/validators/governance/validate_sensitive_release_review_closure.py
  - tests/validators/governance/test_review_authority_binding.py
  - tests/validators/governance/test_sensitive_release_review_closure.py
  - policy/release/README.md
  - .github/CODEOWNERS
  - .github/workflows/review-authority-binding.yml
  - .github/workflows/sensitive-release-review-closure.yml
  - .github/workflows/promotion-gate.yml
tags: [kfm, adr, governance, release, separation-of-duties, two-person-rule, review, actor-identity, authority-binding, sensitive-release, rights, correction, rollback]
notes:
  - "v1.3 is a same-path documentation-only repository reconciliation; it does not accept ADR-0024 or create release authority."
  - "ADR-0024 remains source status draft and effective decision status proposed in the canonical ADR index."
  - "ReviewAuthorityBinding and SensitiveReleaseReviewClosure are substantive deterministic no-network fixture profiles, but both declare authority NONE and all mutation/release/publication permissions false."
  - "The latest main runs for both dedicated profiles completed their focused tests successfully and then failed generated-authoring-receipt integrity because recorded artifact digests were stale."
  - "The active default-branch ruleset requires pull-request mediation and resolved review threads but requires zero approving reviews, no code-owner review, no named reviewers, and no last-push approval."
  - "Operational actor authentication, alias collapse, accepted assignment authority, executable SoD policy, independent human capacity, governed release records, and release integration remain unverified or absent."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ADR-0024 — Steward Separation of Duties for Release

> **Proposed decision.** KFM will require independently attributable review for every release-significant transition, with stricter multi-role review for sensitive, rights-constrained, corrective, rollback, public-access, policy-significant, and trust-root changes. Independence is established through resolved actor identity, current scoped authority, exact subject binding, and governed review evidence—not through role labels, account names, comments, CODEOWNERS routing, automation, or file count.

[![Decision: proposed](https://img.shields.io/badge/decision-proposed-d4a72c?style=flat-square)](#status)
[![ADR ID: confirmed](https://img.shields.io/badge/ADR--0024-confirmed-0969da?style=flat-square)](#current-repository-evidence)
[![Review binding: executable candidate](https://img.shields.io/badge/review%20binding-executable%20candidate-f59e0b?style=flat-square)](#bounded-executable-profiles)
[![T3/T4 closure: executable candidate](https://img.shields.io/badge/T3%2FT4%20closure-executable%20candidate-f59e0b?style=flat-square)](#bounded-executable-profiles)
[![Platform approvals: zero required](https://img.shields.io/badge/platform%20approvals-zero%20required-b42318?style=flat-square)](#repository-control-evidence)
[![Operational enforcement: hold](https://img.shields.io/badge/operational%20enforcement-HOLD-b42318?style=flat-square)](#current-enforcement-maturity)
[![Publication effect: none](https://img.shields.io/badge/publication-none-6e7781?style=flat-square)](#authority-and-publication-boundary)

> [!IMPORTANT]
> **The record is identified; the decision is not accepted.** The canonical [`INDEX.md`](./INDEX.md) uniquely assigns `ADR-0024` to this file and normalizes source metadata `draft` to effective status `proposed`. This revision, its pull request, a green documentation check, or any later merge cannot independently promote the decision to `accepted`.

> [!CAUTION]
> **Bounded structural checks are not operational release control.** The repository now contains deterministic fixture-only `ReviewAuthorityBinding` and T3/T4 `SensitiveReleaseReviewClosure` profiles. They check declared subject, actor, role, interval, author/reviewer separation, role-chain separation, policy projection, evidence references, correction path, and rollback reference. Both profiles explicitly set `authority: NONE`, prohibit every write/release/publication permission, and stop before actor authentication, live policy evaluation, promotion, or release.

> [!WARNING]
> **GitHub mediation is not independent approval.** The active default-branch ruleset blocks deletion and non-fast-forward updates, requires a pull request, and requires review-thread resolution. It currently requires `0` approving reviews, no code-owner review, no named required reviewer, and no last-push approval. CODEOWNERS routes all relevant roots to the same verified account. Neither surface proves KFM release separation of duties.

> [!NOTE]
> **Hosted profile failures are bounded and current.** In the latest main runs inspected, both dedicated profiles completed their focused deterministic tests successfully. Each workflow then failed only its generated-authoring-receipt integrity step because stored artifact digests no longer matched current bytes. That is real receipt drift and keeps hosted closure red; it is not evidence that the underlying fixture semantics failed, and it is not evidence of operational SoD.

**Quick navigation:** [Status](#status) · [Evidence](#evidence-boundary) · [Context](#context) · [Decision](#proposed-decision) · [Roles](#proposed-role-and-identity-model) · [Matrix](#proposed-separation-matrix) · [Maturity](#proposed-control-maturity) · [Authority](#authority-and-publication-boundary) · [Packet](#proposed-review-and-release-evidence-packet) · [Outcomes](#proposed-validation-and-finite-outcomes) · [Profiles](#bounded-executable-profiles) · [Controls](#repository-control-evidence) · [Current state](#current-repository-evidence) · [Enforcement](#current-enforcement-maturity) · [Plan](#implementation-and-convergence-plan) · [Acceptance](#acceptance-gates) · [Risks](#risk-and-open-question-ledger) · [Emergency](#emergency-containment-exception) · [Rollback](#rollback-and-supersession) · [Checklist](#verification-checklist) · [References](#references) · [History](#revision-history) · [Ledger](#appendix-a--no-loss-modernization-ledger)

---

<a id="status"></a>

## Status

| Field | Current value |
|---|---|
| **ADR ID** | `ADR-0024` — unique and confirmed in [`INDEX.md`](./INDEX.md) |
| **Tracked path** | `docs/adr/ADR-0024-steward-separation-of-duties-for-release.md` |
| **Owning root** | `docs/` — human decision record under accepted Directory Rules v2 |
| **Source metadata** | `draft` |
| **Effective decision status** | `proposed` |
| **Decision class** | Release review, actor identity, authority assignment, sensitive release, correction, rollback, public access, and trust-bearing repository controls |
| **Current implementation posture** | Substantive fixture-only structural profiles exist; operational identity, policy, independent-human, and release integration remain held |
| **Current platform posture** | Pull-request mediation exists; independent approving review is not required by the inspected ruleset |
| **Release/publication effect** | None |
| **Supersedes / superseded by** | None / none |
| **Atlas backlog relationship** | Addresses ADR-S-09; does not close it until this decision is accepted and its implementation is separately graduated |

### Acceptance and implementation are separate transitions

1. **ADR acceptance** would approve the role, identity, separation matrix, evidence packet, and control-maturity model.
2. **Implementation graduation** would require accepted actor and assignment contracts, closed machine schemas, executable policy, independent reviewer capacity, authenticated and subject-bound review records, repository-control parity, promotion/release integration, negative-path evidence, correction and rollback drills, and observed fail-closed behavior.

An accepted ADR without enforcement is doctrine. An executable fixture without accepted authority is a candidate proof surface. A platform approval without a governed release packet is platform evidence only.

[Back to top](#top)

---

<a id="evidence-boundary"></a>

## Evidence boundary

This edition is grounded at `main@c9ccb11ded141edbd79763982056a1e6f90b8866`. The target file remained blob `69b4a7228eb4abcc62a35dbbbeeeeddb04ab30d2` at that checkpoint. Repository evidence controls current maturity; the supplied Atlas and Encyclopedia preserve design lineage.

### Maturity ladder

| Layer | Meaning | Current state |
|---|---|---|
| **L0 — Doctrine/design** | Roles, matrices, duties, and release expectations are described | **CONFIRMED present; decision still proposed** |
| **L1 — Shape/fixture proof** | Closed schemas, deterministic fixtures, validators, and negative cases exercise declared structure | **PARTIAL / substantive** for two bounded profiles |
| **L2 — Governed identity and policy** | Actor aliases, authority assignments, policy decisions, recusal, current-head resolution, and accountable review records are resolved | **HELD / not established** |
| **L3 — Repository and release enforcement** | Platform controls and promotion/release workflows require the governed review packet | **HELD** |
| **L4 — Observed operation** | A real release, correction, rollback, and recovery drill demonstrate failure-closed SoD | **UNKNOWN / no proof asserted** |

### Evidence ledger

| Evidence surface | CONFIRMED current state | Does not prove |
|---|---|---|
| ADR inventory | ADR-0024 is unique; source `draft`; effective `proposed` | Acceptance or enforcement |
| Accepted Directory Rules | ADR-0029 adopts exact Directory Rules v2 bytes; `docs/` owns human ADRs | Acceptance of ADR-0024 or release authority |
| Atlas/Encyclopedia | Reviewer/SoD matrix and distinct action roles are design lineage | Repository assignments, policy, or enforcement |
| ReviewRecord contract/schema | Draft semantic contract exists; schema remains narrower and points to lowercase path | Accepted contract/schema convergence or actor authority |
| StewardshipAssignment contract/schema | Detailed semantic contract exists; schema is still permissive, requires only `id`, and allows extra fields | Governed assignment validity or release authority |
| ReviewAuthorityBinding | Closed fixture-only structural profile with deterministic identity and BOUND/HOLD/DENY | Actor/platform authentication, policy, apply, promotion, or release |
| SensitiveReleaseReviewClosure | Closed fixture-only T3/T4 profile over ReviewAuthorityBinding | Real sensitive review, policy approval, release, or publication |
| Dedicated tests | Self-review, role-chain collapse, stale assignment, mismatch, tamper, and no-network boundaries are exercised | Operational identities, human approval, or release mutation |
| Dedicated workflows | Read-only, no-network workflows exist; latest main runs failed stale authoring-receipt digests after focused tests passed | Exact-head green closure or operational SoD |
| CODEOWNERS | One verified account routes all affected paths; comments disclaim SoD authority | Independent review or completed approval |
| Active ruleset | PR mediation and resolved review threads; deletion/non-fast-forward blocked | Any required approving review or code-owner approval |
| Release policy lane | Substantive boundary documentation; current modules remain inactive scaffolds | Accepted executable SoD policy or governed consumer |
| Promotion/release surfaces | Candidate/readiness lanes and explicit holds exist | Governed promotion, release, correction, rollback, or publication |

### Truth labels

- **CONFIRMED** — verified from current repository bytes, platform evidence, or supplied doctrine lineage.
- **PROPOSED** — decision, role, profile, field, policy, or future enforcement target not accepted as current authority.
- **CONFLICTED** — admissible sources assign incompatible vocabulary, shape, path, or authority.
- **NEEDS VERIFICATION** — a concrete check remains before relying on the claim.
- **UNKNOWN** — available evidence cannot resolve the question.
- **HOLD** — fail-closed current result; graduation is intentionally blocked.

[Back to top](#top)

---

<a id="context"></a>

## Context

KFM publication may expose evidence-backed claims, APIs, map layers, PMTiles/COGs, exports, stories, AI-facing surfaces, and sensitive spatial relationships. The actor who authors, assembles, transforms, or submits a candidate may be mistaken, rushed, conflicted, or overconfident when evaluating the candidate's evidence, rights, precision, policy, correction, rollback, or release posture.

The lifecycle remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Promotion is a governed state transition—not a merge, file move, schema pass, workflow result, signature packet, administrator action, or generated explanation.

### Failures this decision is intended to prevent

- self-approval of a public or sensitive release candidate;
- one human counted twice through multiple roles, accounts, credentials, or aliases;
- a bot, AI, signer, workflow, or generated record treated as accountable human review;
- review bound to the wrong subject, digest, version, domain, time, or release scope;
- expired, revoked, provisional, out-of-scope, or unverified authority treated as current;
- sensitivity or rights review performed solely by the release author;
- correction or rollback approved solely by the detector, requestor, operator, or original publisher;
- public aliases, policies, schemas, validators, trust roots, or release controls changed without independent impact review;
- emergency containment becoming permanent, restored, or re-released without independent review;
- CODEOWNERS, a GitHub approval, or a green CI job mistaken for a governed release ReviewRecord;
- stale authoring receipts hidden behind otherwise green focused tests.

[Back to top](#top)

---

<a id="proposed-decision"></a>

## Proposed decision

Upon acceptance and implementation graduation:

1. **Every release-significant action must produce independently attributable review evidence.**
2. **Actor identity is primary.** Authors, reviewers, operators, and approvers must resolve to stable governed actor identities. Usernames, email strings, display names, role labels, certificates, or bot names alone are insufficient.
3. **Role authority must be current and scoped.** The actor must have a valid assignment for the action, subject, domain, sensitivity class, and review time.
4. **Subject binding is mandatory.** Review evidence must bind to the exact candidate reference, digest or `spec_hash`, release scope, policy context, and version reviewed.
5. **No self-approval for public release.** An actor who authored, assembled, materially transformed, or submitted a release candidate must not be the sole actor authorizing its transition to `PUBLISHED` or a public alias.
6. **Sensitive and rights-constrained release requires additional independent roles.** Sensitivity and rights/sovereignty review must be distinct from the author and release authority where applicable.
7. **Correction and rollback remain independently reviewed.** The detector/requestor, operator, and original publisher cannot be the sole correction, rollback, restoration, or re-release authority.
8. **Automation is evidence, not accountable approval.** CI, policy engines, validators, signers, AI, and bots may produce checks, receipts, finite projections, or recommendations; they do not satisfy a required human approval.
9. **Missing independence fails closed.** When a qualified independent reviewer, current assignment, policy decision, or complete packet is unavailable, the result is `HOLD`, `DENY`, `ABSTAIN`, or `ERROR` as appropriate—not self-approval.
10. **The review graph, not one object, proves SoD.** ReviewRecord, StewardshipAssignment, review-binding result, policy decision, PromotionDecision, ReleaseManifest, signature packet, correction/rollback objects, and execution receipts must resolve one governed subject without collapsing their meanings.
11. **High-risk containment may reduce exposure immediately, but restoration and re-release always require independent review.**
12. **Platform controls must complement governed records.** Required platform approvals, CODEOWNERS, branch rules, and workflow checks must not be represented as sufficient when the governed review packet is incomplete.
13. **Receipt integrity is part of review evidence.** A stale, missing, or mismatched receipt keeps the affected workflow or packet held until regenerated through the legitimate producer or explicitly superseded.

### Normative language boundary

`MUST`, `MUST NOT`, `SHOULD`, and `MAY` describe the proposed accepted state. They do not describe current operational enforcement.

[Back to top](#top)

---

<a id="proposed-role-and-identity-model"></a>

## Proposed role and identity model

### Candidate role vocabulary

| Role | Responsibility | Independence trigger |
|---|---|---|
| **Source steward** | Source admission, role, terms, provenance, activation, and retirement | Unresolved rights, authority, source role, or sovereignty |
| **Domain/data steward** | Candidate meaning, transformations, domain validation, and release-assembly input | Cannot solely approve own public release candidate |
| **Evidence reviewer** | EvidenceRef resolution, EvidenceBundle sufficiency, citation and claim support | Material public claim or evidence conflict |
| **Sensitivity reviewer** | Redaction, generalization, precision, access tier, harmful inference | Sensitive spatial, living-person, ecology, archaeology, infrastructure, or DNA data |
| **Rights/sovereignty representative** | Consent, sovereignty, cultural authority, redistribution constraints | Sovereign, cultural, consent-based, or unclear-rights release |
| **Policy steward/reviewer** | Policy meaning, deny/restrict rules, policy-bundle review | Release-enabling policy or exception |
| **Release authority** | Accountable final release decision and public-state transition | Every `PUBLISHED` or public-alias transition |
| **Correction reviewer** | Correction, withdrawal, supersession, and public notice | Steward-significant correction or disputed release |
| **Rollback authority/reviewer** | Rollback target, execution authorization, verification, restoration | Rollback or restoration of public state |
| **AI surface steward** | Public AI templates, evidence binding, finite outcomes, policy integration | Public or policy-significant AI surface change |
| **Docs/architecture steward** | ADR/doctrine integrity and control-plane documentation | Decision status, doctrine publication, or cross-root governance |
| **Validation/security reviewer** | Validator semantics, negative paths, trust roots, signatures, platform controls | Release-enabling validation, security, or repository-control change |
| **Automation actor** | CI, validator, policy, signer, deployment execution | Never satisfies required accountable human approval by itself |

A human may hold multiple roles, but that human counts once for independence. Multiple accounts, credentials, service identities, or signatures belonging to the same human also count once after alias resolution.

### Required identity and authority evidence

A conforming implementation needs accepted semantic and machine profiles for:

- stable `actor_ref` plus alias and account resolution;
- human, service, bot, and external-representative actor classes;
- assignment scope, issuer, effective interval, expiry, revocation, and authority basis;
- conflict-of-interest and recusal state where material;
- required independent roles per action class and sensitivity tier;
- exact review subject, version, digest, and policy-context binding;
- accountable signature or integrity binding over the review record;
- current-head, supersession, withdrawal, and correction handling;
- privacy-minimized retention and exposure of actor evidence.

A role name or fixture actor reference does not grant authority. This ADR does not create a new identity, assignment, policy, or release root.

[Back to top](#top)

---

<a id="proposed-separation-matrix"></a>

## Proposed separation matrix

| Action | Minimum independent evidence | Missing evidence result |
|---|---|---|
| Routine source admission with clear public rights | Source-steward review; author may be steward at low verified maturity | `HOLD` on unresolved authority or rights |
| Source admission with sovereignty, consent, or unclear rights | Source steward plus independent rights/sovereignty representative | `DENY` or `HOLD` |
| Routine non-sensitive normalization/validation | Deterministic checks plus periodic independent audit | `ERROR` or `HOLD` if checks unavailable |
| Sensitivity-relevant transform | Author/domain steward plus independent sensitivity reviewer | `DENY` or `HOLD` |
| Sensitive promotion to PROCESSED or CATALOG | Domain/data steward plus independent sensitivity/policy review | `HOLD` |
| Public release or public-alias transition | Candidate author/assembler distinct from release authority; evidence and policy reviews resolve | `DENY` or `HOLD` |
| T3/T4 or rights-constrained public release | Author plus independent sensitivity reviewer and release authority; rights/sovereignty representative when applicable | `DENY` or `HOLD` |
| Release-enabling policy/schema/validator/trust-root change | Implementer distinct from policy/security approver; release impact reviewed | `HOLD` |
| Correction, withdrawal, or supersession | Detector/requestor plus independent correction reviewer; release authority when public state changes | `HOLD` |
| Rollback execution | Requestor/operator distinct from rollback/release authority; target independently validated | `HOLD` |
| Restore or re-release after incident/withdrawal | New independent review and release decision; emergency operator cannot self-restore | `DENY` or `HOLD` |
| Public AI surface or policy-binding change | AI surface steward plus independent policy/docs review; sensitivity reviewer where affected | `HOLD` |
| ADR acceptance or doctrine publication affecting release | Docs/architecture steward plus affected subsystem and release reviewer | Remains `proposed` or unpublished |
| SoD-control weakening or removal | Implementer distinct from governance/security/release reviewers; migration and rollback evidence | `HOLD` |

### Independence constraints

A review set passes only when every required predicate is supported:

```text
resolved(author.actor_ref) != resolved(required_approver.actor_ref)
required_approver.assignment is active and scoped to subject + action + time
review.subject_ref + subject_digest match the evaluated candidate
review is issued against or after the exact reviewed version
review is not revoked, superseded, expired, recused, or conditional when unconditional approval is required
required human roles are not replaced by automation
policy, evidence, correction, and rollback dependencies resolve
```

String inequality between unverified account names is not enough.

[Back to top](#top)

---

<a id="proposed-control-maturity"></a>

## Proposed control maturity

Maturity describes verified control capability; it never grants permission to bypass high-risk review.

| Level | Control posture | Permitted scope | Public-release consequence |
|---|---|---|---|
| **M0 — Candidate-only bootstrap** | Documentation, contracts, schemas, fixtures, local checks, and no-authority projections | Non-public development and review preparation | No governed public release; `HOLD` |
| **M1 — Recorded manual independence** | Independent human review is subject-bound; identity and authority checked manually; complete packet retained | Low-risk non-sensitive pilot only | Conditional, accountable manual release decision; no sensitive release |
| **M2 — Machine-enforced high-risk SoD** | Actor/alias and assignment resolution, executable policy, negative fixtures, platform requirements, and release gate enforce independence | Sensitive, rights-constrained, corrective, rollback, public-alias, and trust-root classes | Minimum for these classes |
| **M3 — Comprehensive machine-enforced SoD** | All matrix rows, recusal, revocation, organizational controls, audit, recovery, and correction propagation are enforced | Repository-wide governed release | Goal state; accountable humans remain required |

### Graduation rules

- Maturity is declared per release/control profile and evidence packet, never inferred from a README, badge, fixture, or green check.
- Advancement requires independent review and may not be self-approved by the implementation author.
- A profile that cannot prove its level falls back to the lower verified level.
- Sensitive or rights-constrained public release requires M2; before M2 it remains held.
- A local result named `BOUND` or `CLOSED_FOR_SEPARATE_RELEASE_GATE` does not raise operational maturity by itself.
- A profile with stale receipt integrity is not exact-head green, even when focused semantic tests pass.
- Maturity may not be downgraded to make a blocked release pass.

**Current overall operational maturity: `M0 / HOLD`.** The repository has stronger L1 fixture evidence than v1.2 recorded, but no current evidence supports M1, M2, or M3 release operation.

[Back to top](#top)

---

<a id="authority-and-publication-boundary"></a>

## Authority and publication boundary

Separation of duties is necessary but not sufficient. Independent approval does not replace:

- EvidenceRef-to-EvidenceBundle closure;
- source, rights, consent, sovereignty, and sensitivity decisions;
- semantic, schema, geometry, temporal, and citation validation;
- policy evaluation and obligations;
- artifact integrity, receipts, signatures, and attestations;
- PromotionDecision and ReleaseManifest;
- correction, withdrawal, supersession, rollback, and cache invalidation;
- public-client trust-membrane controls.

Likewise, CODEOWNERS, branch rules, GitHub approval, a signature packet, a policy result, or a fixture closure cannot independently create release authority. Each is one evidence surface in a larger governed packet.

No direct RAW, WORK, QUARANTINE, internal catalog/proof/receipt, candidate, or model-output path is authorized by this ADR.

[Back to top](#top)

---

<a id="proposed-review-and-release-evidence-packet"></a>

## Proposed review and release evidence packet

A release-significant packet should resolve these distinct objects without collapsing them:

1. candidate/artifact identity and immutable digest or `spec_hash`;
2. authoring/submitting actor and producer receipts;
3. SourceDescriptor, EvidenceBundle, rights, consent, sovereignty, sensitivity, and policy records;
4. ReviewRecord(s) bound to the exact subject, version, digest, action, and time;
5. reviewer actor identity, alias resolution, active assignment, scope, and authority basis;
6. recusal or conflict statements where policy requires them;
7. review-authority binding result and stable reason codes;
8. sensitive-release closure result where T3/T4 or equivalent review applies;
9. PromotionDecision referencing the required review and support graph;
10. ReleaseManifest referencing exact artifacts, decision, reviews, evidence, and public scope;
11. human signoff packet and machine signature/attestation where separately required;
12. correction, withdrawal, supersession, rollback, and public-alias targets;
13. execution receipt proving the approved transition was the transition performed;
14. platform evidence proving the required repository reviews and checks applied to the exact head;
15. current receipt-integrity verification for every generated authoring or operational receipt in the packet.

### Object-family ownership guidance

- `ReviewRecord` owns an individual review action, reviewer, role, subject, basis, disposition, and time.
- `StewardshipAssignment` owns bounded responsibility and authority-assignment semantics.
- `ReviewAuthorityBinding` may project structural agreement among declared subject, review, and assignment; it is not authentication or authority.
- `SensitiveReleaseReviewClosure` may project fixture-only T3/T4 packet closure for a separate release gate; it is not release approval.
- `PolicyDecision` owns admissibility outcome and obligations.
- `PromotionDecision` owns the accountable lifecycle outcome and references required reviews.
- `ReleaseManifest` owns released artifact scope and references decisions, reviews, evidence, and rollback.
- `CorrectionNotice` and `RollbackCard` reference independent review and decisions.
- `AIReceipt` remains runtime process memory; it cannot become human approval.
- GitHub approvals and CODEOWNERS remain platform evidence, not substitutes for governed objects.

The current case conflict between `contracts/governance/ReviewRecord.md` and schema metadata naming lowercase `review_record.md` remains a governed migration question, not permission to create a second contract.

[Back to top](#top)

---

<a id="proposed-validation-and-finite-outcomes"></a>

## Proposed validation and finite outcomes

SoD validation is a prerequisite report, not a PromotionDecision.

| Outcome | Meaning |
|---|---|
| `PASS` | The validator itself completed and the record coherently represents its finite projection; interpret the profile-specific outcome separately |
| `BOUND` | A fixture-only ReviewAuthorityBinding structurally agrees; no actor authentication or release authority follows |
| `CLOSED_FOR_SEPARATE_RELEASE_GATE` | A fixture-only T3/T4 packet is structurally closed for a later, independent gate; no release authority follows |
| `HOLD` | Required reviewer, authority, policy, evidence, receipt, or complete packet is unresolved or conditional |
| `DENY` | Known actor collapse, unauthorized role, mismatch, prohibited self-review, invalid packet, or policy denial |
| `ABSTAIN` | The accountable decision cannot be made from available evidence or authority |
| `ERROR` | Identity resolver, policy engine, schema, storage, signature, receipt, validator, or orchestration failed |

`ERROR`, `ABSTAIN`, and `HOLD` never become approval by timeout, comment, mergeability, or administrator preference without a governed replacement decision.

### Minimum reason-code families

- `actor_identity_unresolved`
- `actor_alias_collapse`
- `author_approver_collapse`
- `reviewer_in_author_role_chain`
- `required_role_missing`
- `authority_assignment_missing`
- `authority_assignment_expired_or_revoked`
- `review_subject_mismatch`
- `review_version_or_digest_mismatch`
- `review_precedes_subject_version`
- `review_revoked_or_superseded`
- `automation_cannot_approve`
- `sensitivity_review_missing`
- `rights_or_sovereignty_review_missing`
- `correction_reviewer_collapse`
- `rollback_authority_collapse`
- `release_authority_missing`
- `control_maturity_unverified`
- `platform_required_approval_missing`
- `receipt_digest_mismatch`
- `emergency_containment_review_due`

### Required negative coverage

- same actor under two role labels;
- same human through two accounts or aliases;
- reviewer inside the author's declared role chain;
- bot or AI listed as release approver;
- assignment missing, provisional without expiry, expired, revoked, or out of scope;
- review bound to an old candidate version or digest;
- review copied across domains or releases;
- author also sole release authority;
- T3/T4 release missing sensitivity review or release-review responsibility;
- archaeology, sovereign, cultural, or consent-based release missing rights representative;
- detector self-approves correction;
- rollback requestor/operator self-approves rollback;
- emergency operator restores release without independent review;
- CODEOWNERS or GitHub thread resolution present but governed review absent;
- required reviewer unavailable in a single-maintainer repository;
- stale generated receipt after otherwise passing semantic tests;
- complete green path with distinct verified actors, current assignments, exact subject binding, policy, evidence, release, and rollback support.

[Back to top](#top)

---

<a id="bounded-executable-profiles"></a>

## Bounded executable profiles

### ReviewAuthorityBinding

**CONFIRMED current scope:** a strict no-network fixture profile checks a declared subject, review projection, assignment projection, actor/role match, assignment interval/status, review disposition, author/reviewer separation, deterministic identity, sorted/unique collections, and no-write permissions.

**Finite local outcomes:** `BOUND`, `HOLD`, `DENY`.

**Current proof:** twelve focused tests and eleven fixture cases exercise active/provisional/expired assignments, conditional review, actor and role mismatches, self-review, order drift, identity/outcome tampering, symlink rejection, deterministic CLI output, and absence of network/write surfaces.

**Non-effects:** the profile does not authenticate an actor or platform account, resolve aliases, evaluate policy, emit a write request, mutate lifecycle state, merge, promote, release, deploy, publish, or authorize public use.

### SensitiveReleaseReviewClosure

**CONFIRMED current scope:** a strict no-network T3/T4 fixture profile embeds and revalidates ReviewAuthorityBinding; binds the exact subject and author; requires the author in a declared role chain; rejects a reviewer in that chain; requires `RELEASE_REVIEW`; binds promotion, policy, release-manifest candidate, evidence, correction, and rollback references; and fixes every permission to `false`.

**Finite local outcomes:** `CLOSED_FOR_SEPARATE_RELEASE_GATE`, `HOLD`, `DENY`.

**Current proof:** focused tests cover T3/T4 closure, conditional review, policy HOLD/ABSTAIN/DENY, embedded binding reuse, self-review, role-chain collapse, missing release-review responsibility, subject mismatch, authority overclaim, identity tamper, symlink rejection, deterministic CLI output, and no network/write surface.

**Non-effects:** the profile does not authenticate an actor or signature, evaluate a real policy bundle, resolve evidence, approve a review, create PromotionDecision or ReleaseManifest, write state, expose sensitive data, release, deploy, or publish.

### Hosted workflow status

| Profile | Latest inspected main run | Focused semantics | Receipt integrity | Hosted conclusion |
|---|---:|---|---|---|
| ReviewAuthorityBinding | `31654972756` | Tests and fixture replay passed | Generated receipt had three artifact-digest mismatches | `failure` |
| SensitiveReleaseReviewClosure | `31654972404` | Focused deterministic validation passed | Generated receipt verification failed | `failure` |

These failures are actionable authoring-receipt drift. They do not justify weakening or skipping receipt validation, and they do not belong to this documentation-only ADR change unless a separate dependency-closed repair is requested.

[Back to top](#top)

---

<a id="repository-control-evidence"></a>

## Repository-control evidence

### CODEOWNERS

All inspected trust-bearing roots route to `@bartytime4life`. The file explicitly states that routing is not StewardshipAssignment, ReviewRecord, PolicyDecision, release approval, publication authority, or proof that review occurred. No second verified owner or team is declared for the relevant paths.

### Active default-branch ruleset

The inspected active ruleset `Protect` (`15484585`) applies to the default branch and currently:

- denies branch deletion;
- denies non-fast-forward updates;
- requires a pull request;
- requires review-thread resolution;
- allows merge, squash, and rebase methods;
- requires `0` approving reviews;
- requires no named reviewer;
- does not require code-owner review;
- does not require last-push approval;
- declares no bypass actors; the current user cannot bypass.

This is useful baseline repository mediation. It is not independent release approval and does not satisfy the proposed SoD matrix.

### Platform-to-governance rule

Platform evidence should be joined to the exact governed review packet. KFM must not infer that a GitHub approval proves actor authority, nor that a ReviewRecord proves the platform actually enforced the required review.

[Back to top](#top)

---

<a id="current-repository-evidence"></a>

## Current repository evidence

| Surface | Current verified state | Safe conclusion |
|---|---|---|
| ADR-0024 | Exact file; source `draft`; effective `proposed` | Decision not accepted |
| ADR-0029 / Directory Rules | Accepted placement decision and pinned v2 bytes | Same-path `docs/adr/` update is valid; no other ADR accepted by implication |
| ReviewRecord contract | Detailed draft at case-sensitive `ReviewRecord.md` | Semantic intent present; acceptance and path convergence unresolved |
| ReviewRecord schema | Closed narrow proposed shape; no actor identity or subject digest | Cannot prove full SoD |
| StewardshipAssignment contract | Detailed draft semantics | Responsibility model exists as proposal |
| StewardshipAssignment schema | Permissive stub requiring only `id` | Cannot validate current assignments or authority |
| ReviewAuthorityBinding family | Closed contract/schema/fixtures/validator/tests/workflow | Substantive structural candidate only; `authority: NONE` |
| SensitiveReleaseReviewClosure family | Closed T3/T4 contract/schema/fixtures/validator/tests/workflow | Substantive structural candidate only; separate release gate still required |
| Generated authoring receipts | Both latest dedicated main runs report stale digests | Hosted exact-head closure remains red |
| CODEOWNERS | One account and explicit non-authority disclaimer | Independent route absent |
| Default-branch ruleset | PR and thread-resolution mediation; zero approvals required | No platform-enforced independent approval |
| Release policy | Substantive README; modules explicitly inactive scaffolds | No accepted executable SoD policy or consumer |
| Release/correction/rollback shapes | Proposed and mixed maturity | No operational independent review proof |
| Governed release ReviewRecords | None confirmed in the inspected evidence | No accountable operational release review |
| Promotion/release integration | Readiness/candidate surfaces and holds | No governed release or publication authority |
| Production release/publication evidence | None inspected or asserted | Operational state remains unknown/held |

[Back to top](#top)

---

<a id="current-enforcement-maturity"></a>

## Current enforcement maturity

| Capability | Current state |
|---|---|
| ADR identity/status | `CONFIRMED / proposed` |
| Role and SoD doctrine | Present as draft/design lineage |
| ReviewAuthorityBinding structure | `SUBSTANTIVE FIXTURE-ONLY CANDIDATE` |
| T3/T4 sensitive closure structure | `SUBSTANTIVE FIXTURE-ONLY CANDIDATE` |
| Dedicated hosted receipt integrity | `FAIL / STALE DIGESTS` |
| Operational actor identity/alias resolution | `UNKNOWN / not established` |
| Accepted StewardshipAssignment schema | `ABSENT`; current schema is permissive scaffold |
| Governed current assignment registry | `UNKNOWN / not established` |
| Accepted ReviewRecord contract/schema convergence | `HELD / CONFLICTED` |
| Executable SoD policy | `NOT ESTABLISHED` |
| Independent CODEOWNERS route | `NOT ESTABLISHED` |
| Required platform approving review | `0` at inspected ruleset |
| Governed release ReviewRecords | `NONE CONFIRMED` |
| Promotion/release integration | `HOLD` |
| Sensitive-release operational enforcement | `HOLD` |
| Correction/rollback operational SoD | `HOLD` |
| Production release/publication proof | `NONE ASSERTED` |

**Overall operational maturity remains `M0 / HOLD`.** The fixture evidence is materially stronger than the previous ADR snapshot, but it does not cross the authority, policy, human-capacity, platform, release, or operation boundaries required for M1 or M2.

[Back to top](#top)

---

<a id="implementation-and-convergence-plan"></a>

## Implementation and convergence plan

Proceed through small, dependency-ordered, reversible slices:

1. **Review and accept, revise, or reject ADR-0024.** No implementation artifact may accept it by implication.
2. **Resolve actor identity and alias authority.** Define actor classes, canonical refs, account aliases, privacy, revocation, and conflict handling.
3. **Close StewardshipAssignment machine shape.** Align the detailed semantic contract with a strict versioned schema, fixtures, validator, and policy boundaries.
4. **Reconcile ReviewRecord path and shape.** Resolve the case conflict, align semantic and schema vocabularies, bind actor/subject/version/basis, and preserve migration history.
5. **Graduate ReviewAuthorityBinding beyond fixture declarations.** Add governed actor/assignment/current-head resolution while retaining no-write/no-release boundaries.
6. **Graduate T3/T4 closure deliberately.** Replace fixture-only policy projections with accepted policy and authenticated review dependencies; keep release as a separate gate.
7. **Repair stale generated receipts in a separate focused slice.** Regenerate through the legitimate receipt producer, verify exact artifact closure, and avoid hand-edited digests.
8. **Define and enforce release-review policy.** Start observe-only when reports are auditable; move to deny mode through reviewed change.
9. **Reconcile release objects.** PromotionDecision, ReleaseManifest, correction, rollback, AI-surface review, and signature packets reference one review graph without duplicating authority.
10. **Establish independent human capacity.** At least two qualified, separately attributable humans for every required action class; otherwise public release remains held.
11. **Strengthen platform controls.** Require appropriate approvals, code-owner or named-reviewer routes, stale-review dismissal/last-push approval where material, and exact-head parity—without treating these as replacements for governed records.
12. **Declare control maturity through an accepted registry/profile.** Do not infer it from README state.
13. **Wire promotion and release.** Validate exact subject digests, actors, assignments, policy, evidence, receipts, correction, rollback, and platform controls before mutation.
14. **Exercise negative paths and drills.** Sensitive release, policy change, correction, rollback, emergency containment, restoration, alias switch, signer compromise, and stale receipt.
15. **Graduate only on observed evidence.** Replace current holds only with real governed records, deterministic tests, hosted exact-head success, and reversible operation evidence.

### Documentation obligations

Material behavior changes must update this ADR or an accepted successor, the ADR index when status/supersession changes, semantic contracts, schemas, policy docs, release/review READMEs, runbooks, registers, fixtures/tests, platform-control documentation, and rollback guidance together.

[Back to top](#top)

---

<a id="acceptance-gates"></a>

## Acceptance gates

### ADR acceptance

- [ ] Architecture, release, governance/review, affected domain, evidence, policy/sensitivity, rights, correction/rollback, validation, security, and docs reviewers approve the proposed model.
- [ ] Role names and mappings are agreed without claiming current assignments.
- [ ] Release-significant action classes and required independent roles are explicit.
- [ ] Actor identity, alias resolution, assignment authority, and recusal dependencies are accepted or explicitly bounded.
- [ ] Automation and AI non-approval rule is explicit.
- [ ] Subject/version/digest and receipt-integrity binding are mandatory.
- [ ] M0–M3 is accepted as control maturity, not permission to bypass sensitive review.
- [ ] Sensitive and rights-constrained public release requires at least M2.
- [ ] Emergency containment cannot authorize restoration or re-release.
- [ ] Platform controls are complementary evidence, not governing release authority.
- [ ] Current single-account routing and zero-required-approval ruleset posture are recorded accurately.
- [ ] Bounded executable profiles are distinguished from actor authentication, policy, human approval, promotion, and release.
- [ ] No statement claims current governed release, rollback, or publication capability.

### Implementation graduation

- [ ] Accepted actor/alias and StewardshipAssignment contracts, schemas, fixtures, and validators exist.
- [ ] ReviewRecord contract path and machine shape converge through a governed migration.
- [ ] Real SoD policy and stable reason codes are active under the accepted policy home.
- [ ] Independent qualified human capacity and tested review routing exist.
- [ ] Required platform approvals apply to the exact head and match the governed review burden.
- [ ] Subject-bound review evidence is referenced from promotion and release records.
- [ ] Generated and operational receipts validate against current bytes.
- [ ] Sensitive release, correction, rollback, restoration, and emergency drills pass.
- [ ] No unauthorized public mutation occurs on missing, stale, conflicted, or failed dependencies.
- [ ] At least one representative release dry run demonstrates complete review, evidence, policy, release, correction, and rollback closure without publication.

[Back to top](#top)

---

<a id="consequences"></a>

## Consequences

### Positive

- Makes self-approval, alias collapse, role-chain collapse, and stale authority detectable.
- Preserves Atlas and Encyclopedia lineage without turning planning tables into implementation fact.
- Separates actor identity, assignment, review action, policy, promotion decision, manifest, execution, receipt, proof, and publication.
- Prevents bots, AI, CODEOWNERS, signatures, or string inequality from masquerading as accountable human review.
- Provides a staged path from fixture-only structural checks to machine-enforced sensitive release.
- Makes correction, rollback, public-alias, policy, platform-control, and emergency actions auditable.
- Treats receipt drift as a visible failure rather than hiding it behind focused test success.

### Costs

- Requires governed actor/alias and assignment infrastructure.
- Requires more than one qualified human for release-significant actions.
- Adds contract, schema, fixture, validator, policy, platform, release, and operational complexity.
- May hold releases in a single-maintainer project.
- Requires review records and approvals to be reissued after material subject changes.
- Creates administrative work for assignment expiry, revocation, recusal, backup coverage, and receipt regeneration.

### Preserved invariants

- No canonical root or lifecycle phase changes.
- Promotion remains a governed state transition.
- Evidence, policy, review, decision, receipt, proof, manifest, release, and publication remain distinct.
- Public clients remain behind governed and released interfaces.
- Sensitive and unclear-rights data remains deny-by-default.
- Documentation and platform state do not substitute for operation evidence.

[Back to top](#top)

---

<a id="alternatives-considered"></a>

## Alternatives considered

| Alternative | Disposition |
|---|---|
| Informal convention only | Rejected: non-auditable under deadline, staffing, or account changes |
| CODEOWNERS or GitHub approvals only | Rejected: platform routing/approval does not bind KFM evidence, policy, assignment, release action, or execution |
| `author_id != approver_id` strings only | Rejected: aliases, multiple accounts, bots, stale identities, and role labels defeat the test |
| One combined release-manager role | Rejected: collapses author, policy, sensitivity, rights, correction, and release authority |
| Automation or AI as second approver | Rejected: automation supplies evidence and checks, not accountable human judgment |
| Fixture closure treated as release approval | Rejected: both current profiles explicitly declare no authority and all permissions false |
| Ignore stale receipts because semantic tests pass | Rejected: receipt integrity is part of the evidence packet |
| Tooling required for every low-risk draft from day one | Rejected: M0 permits non-public candidate work but never public release |
| Manual review forever | Rejected: high-risk release must graduate to machine-enforced checks |
| Per-domain unrelated SoD policies | Rejected as default: creates vocabulary and enforcement drift; domain rules should extend one governed profile |
| Self-approval when no second maintainer exists | Rejected: unavailable independent review yields `HOLD`, not weaker governance |
| Change repository settings in this ADR PR | Rejected: documentation reconciliation and platform-control changes need separate review/rollback boundaries |

[Back to top](#top)

---

<a id="risk-and-open-question-ledger"></a>

## Risk and open-question ledger

| Item | Current status | Required resolution |
|---|---|---|
| Actor identity and alias contract | `OPEN` | Canonical identity, aliases, privacy, actor class, revocation, evidence |
| StewardshipAssignment schema | `PERMISSIVE STUB` | Strict versioned schema, fixtures, validator, policy, migration |
| ReviewRecord contract path/casing | `CONFLICTED` | Reconcile case-sensitive contract path and schema metadata |
| ReviewRecord actor/subject fields | `PROPOSED / INCOMPLETE` | Bind actor, role, exact subject, digest, basis, assignment, recusal, signature |
| ReviewAuthorityBinding authority | `NONE` | Preserve structural boundary while adding governed resolvers later |
| Sensitive T3/T4 closure authority | `NONE` | Separate accepted policy and release gate |
| Dedicated generated receipts | `STALE / FAIL` | Regenerate through legitimate producer and verify exact bytes |
| Release SoD policy | `NOT ESTABLISHED` | Accepted policy composition and governed consumer |
| Release manifest and promotion joins | `PARTIAL / MIXED` | Cross-object review graph and exact-subject validation |
| CODEOWNERS single account | `CONFIRMED LIMIT` | Verify and assign independent qualified humans/teams |
| Default-branch required approvals | `0` | Review materiality and adopt appropriate required approvals separately |
| External rights representative identity | `OPEN` | Authority attestation, privacy, retention, revocation |
| Recusal/conflict-of-interest | `OPEN` | Policy plus review/assignment fields |
| Reviewer signature integrity | `OPEN` | Signature profile distinct from human authority |
| Emergency withdrawal SLA | `OPEN` | Timebox, scope, follow-up, incident, correction, and restoration rules |
| Single-maintainer operating model | `HOLD RISK` | Add qualified reviewers or keep public release held |
| Maturity registry | `OPEN` | Accepted schema/register and reviewed profile declarations |
| Historical release audit | `UNKNOWN` | Inventory prior decisions, reviews, releases, and gaps |
| Platform-to-governance parity | `OPEN` | Exact-head joins between ruleset approvals and governed ReviewRecords |
| Operational drills | `UNKNOWN` | Release dry run, correction, rollback, restoration, and signer-compromise exercises |

[Back to top](#top)

---

<a id="emergency-containment-exception"></a>

## Emergency containment exception

A narrowly scoped exception may permit one authorized operator to **reduce exposure** immediately when delay creates credible harm, for example:

- disable a public alias;
- withdraw or quarantine a release;
- restrict access;
- revoke a compromised signer, credential, token, or serving path;
- stop a deployment or public endpoint;
- apply a temporary deny rule.

The exception:

1. never permits new publication or broader access;
2. never permits the operator to approve restoration or re-release;
3. requires an immutable incident/containment record with exact subject, actor, reason, time, and action;
4. requires independent review within a policy-defined timebox;
5. requires correction, withdrawal, rollback, cache invalidation, and public notice where applicable;
6. expires fail-closed if follow-up review is not completed;
7. cannot bypass routine release review;
8. cannot repair a stale receipt by suppressing receipt validation.

The current repository evidence does not prove an operationally authorized containment exception. This section remains part of the proposed decision.

[Back to top](#top)

---

<a id="rollback-and-supersession"></a>

## Rollback and supersession

### Documentation-only rollback

Restore the prior target blob:

```text
69b4a7228eb4abcc62a35dbbbeeeeddb04ab30d2
```

A transparent revert restores v1.2 proposed documentation. It does not change rulesets, actor assignments, receipts, review records, policy, release state, or public artifacts.

### If this ADR is later accepted

Accepted ADRs are governance history. Do not flip an accepted decision back to `proposed` or silently weaken it. A material change requires:

- a successor ADR;
- reciprocal supersession links;
- synchronized ADR index update;
- migration and compatibility plan for contracts, schemas, fixtures, policies, validators, assignments, review records, release objects, platform controls, and runbooks;
- correction and rollback analysis for releases relying on the prior decision.

### Control rollback

Weakening or disabling implemented SoD requires independent review at least as strong as the control being changed. Removing required reviewers, deleting review evidence, bypassing receipt checks, moving policy into an invented disabled path, or lowering maturity to unblock a release is not an acceptable rollback strategy without an accepted migration decision.

[Back to top](#top)

---

<a id="verification-checklist"></a>

## Verification checklist

### Current v1.3 reconciliation

- [x] Current main and target blob recorded.
- [x] ADR identity, filename, H1, source status, and index row preserved.
- [x] Accepted ADR-0029 and Directory Rules v2 placement authority verified.
- [x] ReviewRecord and StewardshipAssignment contract/schema drift inspected.
- [x] ReviewAuthorityBinding contract, schema, fixtures, validator, tests, workflow, and latest main run inspected.
- [x] SensitiveReleaseReviewClosure contract, schema, fixtures, validator, tests, workflow, and latest main run inspected.
- [x] Focused semantic success separated from stale generated-receipt workflow failure.
- [x] Active default-branch ruleset and CODEOWNERS posture inspected.
- [x] Bounded fixture outcomes separated from actor authentication, accountable approval, and release authority.
- [x] Emergency containment remains distinct from restoration and re-release.
- [x] Documentation rollback points to the immediately prior blob.
- [x] Source `draft` and effective `proposed` status remain unchanged.
- [x] No implementation, platform-setting, release, deployment, or publication claim introduced.
- [ ] Human review completed.
- [ ] ADR accepted, rejected, or revised through governed review.
- [ ] Implementation graduated.
- [ ] Governed release and rollback drill observed.

### Future implementation

- [ ] Actor/alias and authority-assignment profiles accepted.
- [ ] StewardshipAssignment schema is strict and aligns with semantic contract.
- [ ] ReviewRecord contract and schema path/fields converge.
- [ ] Review and assignment records are subject-bound, versioned, signed or integrity-bound, correctable, and revocable.
- [ ] SoD validator and policy use stable public-safe reason codes.
- [ ] Valid/invalid fixtures cover aliases, bots, stale roles, subject mismatch, T3/T4, rights, correction, rollback, emergency, platform, and receipt-drift paths.
- [ ] Independent qualified reviewer capacity exists.
- [ ] Platform required approvals complement governed records.
- [ ] PromotionDecision and ReleaseManifest resolve required review evidence.
- [ ] Generated receipts validate against current bytes.
- [ ] Audit and recovery drills pass without hidden overrides.

[Back to top](#top)

---

<a id="references"></a>

## References

| Reference | Current relationship and boundary |
|---|---|
| [`docs/adr/README.md`](./README.md) | ADR operating contract; merge does not accept a decision |
| [`docs/adr/INDEX.md`](./INDEX.md) | Confirms ADR-0024 identity, source `draft`, effective `proposed` |
| [ADR-0010](./ADR-0010-deny-by-default-for-dna-rare-species-archaeology-infrastructure.md) | Sensitive-domain fail-closed proposal |
| [ADR-0011](./ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md) | Keeps review, receipt, proof, manifest, and publication distinct |
| [ADR-0015](./ADR-0015-data-published-_domain_-current-alias-is-governed-by-rollback_card.md) | Public alias and rollback dependencies |
| [ADR-0018](./ADR-0018-promotion-gate-sequence.md) | Promotion sequence and readiness boundary |
| [ADR-0020](./ADR-0020-abstain-is-a-first-class-decision.md) | Missing evidence or authority may abstain/hold rather than fabricate |
| [ADR-0023](./ADR-0023-geo-manifest-signs-every-pmtiles-cog-release.md) | Artifact cryptography remains distinct from human approval |
| [ADR-0025](./ADR-0025-public-client-never-reads-canonical-internal-stores.md) | Public trust-membrane boundary |
| [ADR-0029](./ADR-0029-adopt-directory-governance-standard-v2.md) | Accepted placement authority; does not accept ADR-0024 |
| [Directory Rules](../doctrine/directory-rules.md) | Responsibility roots, authority, migration, and no-parallel-home law |
| [Separation of Duties standard](../governance/SEPARATION_OF_DUTIES.md) | Draft doctrine operationalization; not enforcement |
| [ReviewRecord contract](../../contracts/governance/ReviewRecord.md) | Detailed semantic draft at case-conflicted path |
| [ReviewRecord schema](../../schemas/contracts/v1/governance/review_record.schema.json) | Narrow proposed shape without full actor/subject authority |
| [StewardshipAssignment contract](../../contracts/governance/steward_assignment.md) | Detailed proposed responsibility semantics |
| [StewardshipAssignment schema](../../schemas/contracts/v1/governance/steward_assignment.schema.json) | Current permissive scaffold |
| [ReviewAuthorityBinding contract](../../contracts/governance/review_authority_binding.md) | Fixture-only structural binding; no authority |
| [ReviewAuthorityBinding schema](../../schemas/contracts/v1/governance/review_authority_binding.schema.json) | Closed no-authority shape |
| [ReviewAuthorityBinding fixtures](../../fixtures/contracts/v1/governance/review_authority_binding/cases.json) | Eleven deterministic cases |
| [ReviewAuthorityBinding validator](../../tools/validators/governance/validate_review_authority_binding.py) | Deterministic structural projection; no authentication/write/release |
| [ReviewAuthorityBinding tests](../../tests/validators/governance/test_review_authority_binding.py) | Focused negative and deterministic coverage |
| [ReviewAuthorityBinding workflow](../../.github/workflows/review-authority-binding.yml) | Read-only hosted check; latest run red on stale generated receipt |
| [SensitiveReleaseReviewClosure contract](../../contracts/governance/sensitive_release_review_closure.md) | Fixture-only T3/T4 closure for a separate gate; no authority |
| [SensitiveReleaseReviewClosure schema](../../schemas/contracts/v1/governance/sensitive_release_review_closure.schema.json) | Closed no-authority T3/T4 profile |
| [SensitiveReleaseReviewClosure fixtures](../../fixtures/contracts/v1/governance/sensitive_release_review_closure/cases.json) | Twelve deterministic cases |
| [SensitiveReleaseReviewClosure validator](../../tools/validators/governance/validate_sensitive_release_review_closure.py) | Reuses ReviewAuthorityBinding and preserves separate release gate |
| [SensitiveReleaseReviewClosure tests](../../tests/validators/governance/test_sensitive_release_review_closure.py) | Focused policy/role-chain/subject/tamper coverage |
| [SensitiveReleaseReviewClosure workflow](../../.github/workflows/sensitive-release-review-closure.yml) | Read-only hosted check; latest run red on generated receipt |
| [Release policy](../../policy/release/README.md) | Boundary documentation; modules remain inactive scaffolds |
| [CODEOWNERS](../../.github/CODEOWNERS) | One-account review routing only; explicit non-authority boundary |
| [Promotion workflow](../../.github/workflows/promotion-gate.yml) | Readiness and promotion-boundary evidence; not release authority |
| Repository ruleset `Protect` (`15484585`) | Active PR mediation with zero approving reviews required at inspected checkpoint |
| KFM Domains v1.1 + Pass 23/32 Consolidated Atlas | Design lineage for reviewer/SoD matrix and ADR-S-09 |
| KFM Encyclopedia | Design lineage separating steward, reviewer, policy, release, developer, and AI duties |

[Back to top](#top)

---

<a id="revision-history"></a>

## Revision history

| Version | Date | Summary |
|---|---|---|
| `v1.3` | 2026-08-14 | Same-path repository reconciliation against `main@c9ccb11d...`: records accepted Directory Rules placement authority; recognizes substantive fixture-only ReviewAuthorityBinding and T3/T4 SensitiveReleaseReviewClosure profiles; records their no-authority boundaries and latest stale-receipt workflow failures; verifies the active default-branch ruleset requires PR mediation but zero approvals; refreshes evidence, maturity, convergence, acceptance, risks, rollback, references, and no-loss ledger; preserves source `draft` and effective `proposed`. |
| `v1.2` | 2026-08-03 | Added the bounded fixture-only ReviewRecord/SoD candidate evidence while preserving overall M0/HOLD and live identity, policy, governed-record, and release dependencies. |
| `v1.1` | 2026-07-24 | Re-grounded the ADR in repository evidence; separated design lineage from implementation; replaced string-only identity checks with actor, authority, and subject binding; corrected M0; added emergency containment, convergence, acceptance, finite outcomes, risks, and successor-ADR rollback discipline. |
| `v1` | 2026-05-15 | Initial draft proposing role vocabulary, separation matrix, M0–M3 maturity, policy/platform enforcement, validation, rollback, and Atlas ADR-S-09 closure. |

---

<a id="appendix-a--no-loss-modernization-ledger"></a>

## Appendix A — No-loss modernization ledger

| Prior v1.2 material | v1.3 treatment |
|---|---|
| Proposed decision and source/effective status | **Preserved**; status remains `draft` / `proposed` |
| Acceptance versus implementation separation | **Preserved and sharpened** |
| Actor identity, authority, exact-subject, and no-string-only rules | **Preserved** |
| Candidate role vocabulary | **Preserved and expanded** with validation/security role |
| Separation matrix | **Preserved and extended** for control weakening and T3/T4 terminology |
| M0–M3 maturity model | **Preserved**; linked to a separate L0–L4 evidence ladder |
| Review/release evidence packet | **Preserved and expanded** with bounded-profile, platform, and receipt-integrity joins |
| Finite outcomes and reason-code families | **Preserved and clarified** so validator `PASS` does not equal release approval |
| Current evidence and M0/HOLD | **Refreshed** for two executable candidates, platform ruleset, and stale receipts |
| Implementation/convergence plan | **Preserved and reordered** around current dependency closure |
| Acceptance gates | **Preserved and split** into ADR acceptance and implementation graduation |
| Consequences and alternatives | **Preserved and updated** for current profile/receipt/platform evidence |
| Risk ledger | **Preserved and expanded** with receipt and platform parity risks |
| Emergency containment | **Preserved**; receipt bypass explicitly prohibited |
| Successor/supersession and rollback | **Preserved**; immediate prior blob corrected to v1.2 |
| Verification checklist and references | **Refreshed** with current files, workflows, runs, and platform evidence |
| Decision authority, release, deployment, publication | **Unchanged:** none created by this revision |

---

<sub>**Last updated:** 2026-08-14 · **Source metadata:** `draft` · **Effective decision status:** `proposed` · **Fixture evidence:** `PARTIAL / substantive` · **Operational enforcement:** `M0 / HOLD` · **Publication:** none · **Path:** `docs/adr/ADR-0024-steward-separation-of-duties-for-release.md`</sub>
