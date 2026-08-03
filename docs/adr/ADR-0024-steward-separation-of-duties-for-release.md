<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/adr-0024-steward-separation-of-duties-for-release
title: ADR-0024 — Steward Separation of Duties for Release
type: adr
adr_id: ADR-0024
version: v1.2
status: draft
effective_decision_status: proposed
owners:
  - "NEEDS VERIFICATION — architecture decision owner"
  - "NEEDS VERIFICATION — release and publication steward"
  - "NEEDS VERIFICATION — governance and review steward"
  - "NEEDS VERIFICATION — evidence, policy, sensitivity, rights, correction, rollback, validation, and security stewards"
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
  - Security reviewer for actor identity, signatures, or trust-root changes
created: 2026-05-15
updated: 2026-08-03
policy_label: public
truth_posture: cite-or-abstain
responsibility_root: docs/
current_path: docs/adr/ADR-0024-steward-separation-of-duties-for-release.md
supersedes: []
superseded_by: null
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 68069dce9e292649697f63f96fa57edd07181a27
  target_prior_blob: 517493105f8464457782dee1ada5bf1e6db43c79
  adr_index_blob: cf08fae322ac53426f7394d97897fdb942253049
  directory_rules_blob: 2affb080e6f0043867c64c7f06c1ca52030fbd55
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  promotion_decision_schema_blob: a2d087a46772cf60e4b9dfb394892690e8a88b31
  release_manifest_schema_blob: 727db0a781900aa3816dcdce723fe355fec2e786
  review_record_schema_blob: fe2f2223af46481e7fb19b0baa94f62ce9c6c855
  review_record_fixture_readme_blob: fccac522a0c178bb87fdaf3c7d932861a40786da
  review_record_validator_blob: e1aa5fcc4b2da4055eb61276a031512512bcb4ca
  correction_notice_schema_blob: d3fe47b9005cd52cf26f349c892386e8ce6d4c5a
  rollback_card_schema_blob: 779ffcf282201ba4dba9689e622f92723db55b4e
  ai_receipt_schema_blob: 2e0bebdb3a38acbc3c58a919db46970c6e829b4a
  release_reviews_readme_blob: d927536c39a2102b1f012007fc8de4facb7abd90
  release_promotion_decisions_readme_blob: 18c6342f93212992f98d0e354390a36a79749858
  release_signatures_readme_blob: e25a62e73762af96d15fbb6c32c8d03fbac66e30
  release_state_register_blob: f576239f447045b04d7b30c540234d8641ceb7dc
  release_policy_readme_blob: 72fa13bfa2bd63ba0bd29201e282b45db0164d2c
  promotion_workflow_blob: c22941d5e1fad3317f46591705091ef2b6e7d265
inspection_boundary: >
  Current-session GitHub reads of the ADR index, Directory Rules, this ADR, CODEOWNERS,
  PromotionDecision, ReleaseManifest, ReviewRecord, CorrectionNotice, RollbackCard, and
  AIReceipt schemas, ReviewRecord fixtures and validator, release review, promotion-decision,
  and signature lane documentation, release-state register, release policy root, and promotion
  workflow source. Supplied Atlas and Encyclopedia materials were used as doctrine/design
  lineage for the reviewer-role and two-person-rule proposal. No branch ruleset, required-review
  configuration, StewardshipAssignment, actor-identity registry, real release ReviewRecord,
  policy evaluation, signer, promotion, release, correction, rollback, deployment, or production
  publication was exercised.
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
  - docs/doctrine/directory-rules.md
  - schemas/contracts/v1/governance/review_record.schema.json
  - schemas/contracts/v1/release/promotion_decision.schema.json
  - schemas/contracts/v1/release/release_manifest.schema.json
  - schemas/contracts/v1/release/correction_notice.schema.json
  - schemas/contracts/v1/release/rollback_card.schema.json
  - schemas/contracts/v1/runtime/ai_receipt.schema.json
  - fixtures/contracts/v1/governance/review_record/README.md
  - tools/validators/validate_review_record.py
  - release/reviews/README.md
  - release/promotion_decisions/README.md
  - release/signatures/README.md
  - control_plane/release_state_register.yaml
  - policy/release/README.md
  - .github/CODEOWNERS
  - .github/workflows/promotion-gate.yml
tags: [kfm, adr, governance, release, separation-of-duties, two-person-rule, review, actor-identity, sensitivity, rights, correction, rollback]
notes:
  - "v1.2 reconciles current evidence with a bounded fixture-only ReviewRecord candidate validator; it preserves effective decision status proposed, overall M0/HOLD, and every live identity, policy, governed-record, and release dependency."
  - "v1.1 is a same-path repository-grounded modernization. It preserves source metadata draft and effective decision status proposed; it does not accept ADR-0024 or implement separation of duties."
  - "The canonical ADR index uniquely assigns ADR-0024 to this exact path."
  - "The supplied Atlas and Encyclopedia support a proposed reviewer-role/SoD design and ADR backlog item; they do not prove accepted repository policy or current enforcement."
  - "Current CODEOWNERS routes all relevant paths to one verified GitHub account and explicitly disclaims stewardship, required review, independent approval, or separation-of-duties proof."
  - "The current promotion workflow runs bounded synthetic promotion and ReviewRecord candidates while confirming release/reviews remains guidance-only and creates no governed ReviewRecord or release authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ADR-0024 — Steward Separation of Duties for Release

> **Proposed decision.** KFM will require independently attributable review for every release-significant transition, with stricter multi-role review for sensitive, rights-constrained, corrective, rollback, public-access, and policy-significant changes. Independence is evaluated by resolved actor identity and current authority assignment—not by role labels, usernames, comments, CODEOWNERS routing, automation, or the mere presence of multiple files.

[![Decision: proposed](https://img.shields.io/badge/decision-proposed-d4a72c?style=flat-square)](#status)
[![ADR ID: confirmed](https://img.shields.io/badge/ADR--0024-confirmed-0969da?style=flat-square)](#current-repository-evidence)
[![Review records: none](https://img.shields.io/badge/governed%20ReviewRecords-none-b42318?style=flat-square)](#current-enforcement-maturity)
[![Validator: bounded candidate](https://img.shields.io/badge/review%20validator-bounded%20candidate-f59e0b?style=flat-square)](#current-enforcement-maturity)
[![CODEOWNERS: single route](https://img.shields.io/badge/CODEOWNERS-single%20route-f59e0b?style=flat-square)](#current-repository-evidence)
[![Enforcement: hold](https://img.shields.io/badge/enforcement-WORKFLOW__HOLD-b42318?style=flat-square)](#current-enforcement-maturity)
[![Publication effect: none](https://img.shields.io/badge/publication-none-6e7781?style=flat-square)](#authority-and-publication-boundary)

> [!IMPORTANT]
> **Identity is confirmed; acceptance is not.** [`docs/adr/INDEX.md`](./INDEX.md) uniquely assigns `ADR-0024` to this exact file. Its source metadata is `draft`, which the index normalizes conservatively to effective status `proposed`. Editing, merging, or validating this Markdown does not accept the decision.

> [!CAUTION]
> **The repository does not currently enforce governed release separation of duties.** `PromotionDecision` records a reviewer string and ticket but no proposer/approver identity split. The proposed `ReviewRecord` schema has no actor identity; a bounded validator composes only synthetic identity and authority declarations. `ReleaseManifest`, `CorrectionNotice`, and `RollbackCard` remain thin proposed schemas, the release policy root is a stub, and the SoD policy file is absent.

> [!WARNING]
> **Different labels do not prove different people.** A person may hold multiple roles, use multiple accounts, or trigger automation. SoD cannot be proven by `author_id != approver_id` string comparison alone. The validator must resolve aliases to a governed actor identity, verify current role/authority assignments, bind each review to the exact subject and version, and reject bots or generated text as accountable approvers.

> [!NOTE]
> The current fixture-only candidate compares canonical synthetic actor IDs and packet-supplied intervals. It does not resolve aliases, query a current-review head, authenticate authority, or determine which proposed schema role is qualified as release authority. Those omissions keep this ADR at `proposed` and enforcement at `M0 / HOLD`.

**Quick navigation:** [Status](#status) · [Evidence](#evidence-boundary) · [Context](#context) · [Decision](#proposed-decision) · [Terms](#proposed-role-and-identity-model) · [Matrix](#proposed-separation-matrix) · [Maturity](#proposed-control-maturity) · [Authority](#authority-and-publication-boundary) · [Evidence packet](#proposed-review-and-release-evidence-packet) · [Outcomes](#proposed-validation-and-finite-outcomes) · [Current evidence](#current-repository-evidence) · [Enforcement](#current-enforcement-maturity) · [Convergence](#implementation-and-convergence-plan) · [Acceptance](#acceptance-gates) · [Consequences](#consequences) · [Alternatives](#alternatives-considered) · [Risks](#risk-and-open-question-ledger) · [Emergency](#emergency-containment-exception) · [Rollback](#rollback-and-supersession) · [Checklist](#verification-checklist) · [References](#references) · [History](#revision-history)

---

<a id="status"></a>

## Status

| Field | Current value |
|---|---|
| **ADR ID** | `ADR-0024` — unique and confirmed in [`INDEX.md`](./INDEX.md) |
| **Tracked path** | `docs/adr/ADR-0024-steward-separation-of-duties-for-release.md` |
| **Source metadata** | `draft` |
| **Effective decision status** | `proposed` |
| **Decision class** | Release review, actor identity, authority assignment, sensitive release, correction, rollback, and public-access control |
| **Current repository posture** | Bounded fixture-only ReviewRecord/SoD candidate checks plus explicit workflow holds; no governed release ReviewRecord, live identity/authority resolution, or accepted SoD policy |
| **Implementation effect of this revision** | Reconciles this proposed ADR with a companion candidate hardening slice; does not accept or implement the full decision |
| **Release/publication effect** | None |
| **Supersedes / superseded by** | None / none |
| **Atlas backlog relationship** | Addresses ADR-S-09; does not close it until accepted and tracked accordingly |

### Acceptance versus implementation graduation

Two independent states must remain visible:

1. **ADR acceptance** would approve the role, identity, review, and control-maturity model.
2. **Implementation graduation** would require accepted actor/role contracts, closed schemas, fixtures, real validators, policy, independent reviewer availability, repository rules, release integration, signed or otherwise integrity-bound review records, and observed failure-closed behavior.

An accepted ADR without enforcement is doctrine. Multiple comments, labels, GitHub accounts, bots, or files without verified actor/authority resolution are not independent review.

[Back to top](#top)

---

<a id="evidence-boundary"></a>

## Evidence boundary

This revision uses repository bytes at `main@68069dce9e292649697f63f96fa57edd07181a27` plus the scoped bounded-candidate hardening diff and the supplied KFM Atlas and Encyclopedia as design lineage.

| Evidence surface | CONFIRMED current state | What remains unproved |
|---|---|---|
| ADR inventory | Exact ADR ID/path; source `draft`; effective `proposed` | Acceptance |
| Atlas/Encyclopedia | Reviewer/SoD matrix and distinct action roles are proposed design lineage | Repository policy, actor assignments, or enforcement |
| CODEOWNERS | All affected roots route to `@bartytime4life`; file disclaims stewardship and SoD proof | Required review, branch rules, independent approver, quorum |
| `PromotionDecision` | Closed schema with reviewer string/ticket and `APPROVE|DENY|ABSTAIN` | Proposer identity, role assignment, independent approval |
| `ReviewRecord` | Closed proposed schema, semantic draft at case-conflicted path, minimal schema fixtures, and a separate synthetic Gate G profile | Accepted contract path, governed actor identity, subject-version authority, current-head resolution, SoD policy |
| Release/correction/rollback schemas | ReleaseManifest and RollbackCard are thin stubs; CorrectionNotice is empty/open scaffold | Operational release, correction, or rollback review |
| AIReceipt | Closed runtime shape with no release-review actor fields | AI-surface change approval or human SoD |
| Release review lanes | README guidance exists; promotion workflow asserts no governed review record exists | Accountable review instances or release authority |
| Release signatures | Reviewer-signoff packet lane exists | Cryptographic artifact-signature profile or artifact binding |
| Release-state register | Empty proposed register describing reviewers and rollback targets | Lane maturity declarations or accepted state machine |
| Release policy | `policy/release/README.md` is a greenfield stub; `policy/release/sod.rego` absent | Executable SoD policy |
| Promotion workflow | Read-only bounded synthetic checks and authority holds exist | Promotion, signing, governed review, release, rollback, publication |

### Truth labels

- **CONFIRMED** — verified from current repository bytes or supplied doctrine lineage.
- **PROPOSED** — candidate decision, role, profile, field, policy, path role, or enforcement target.
- **CONFLICTED** — current sources assign incompatible vocabulary, shape, state, or authority.
- **NEEDS VERIFICATION** — a concrete check remains open.
- **UNKNOWN** — available evidence is insufficient.
- **HOLD** — current readiness evidence intentionally blocks graduation.

[Back to top](#top)

---

<a id="context"></a>

## Context

KFM publication can expose evidence-backed claims, maps, PMTiles/COGs, APIs, exports, stories, AI-facing surfaces, and sensitive spatial relationships. The same actor who creates a candidate may be motivated, rushed, mistaken, or conflicted when evaluating its evidence, rights, sensitivity, policy, release, correction, or rollback posture.

The supplied Atlas identifies reviewer separation as an ADR threshold question, and the Encyclopedia separates steward, domain editor, reviewer, policy admin, release manager, developer, and AI duties. Those sources support the design direction, while the live repository determines current maturity.

The lifecycle remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Promotion is a governed state transition, not a merge, file move, upload, schema pass, signature packet, generated summary, or administrator action.

### Failures this ADR addresses

- self-approval of a release candidate;
- one person acting under two labels and being counted twice;
- a bot or AI being treated as an accountable reviewer;
- review attached to the wrong subject, version, digest, or release scope;
- stale, revoked, or unverified role assignments;
- sensitivity or rights review performed by the release author;
- correction/rollback approved solely by the detector or original publisher;
- public aliases, policies, or trust roots changed without independent review;
- emergency containment becoming permanent unreviewed release state;
- CODEOWNERS routing being mistaken for completed review.

[Back to top](#top)

---

<a id="proposed-decision"></a>

## Proposed decision

Upon acceptance and implementation graduation:

1. **Every release-significant action must produce independently attributable review evidence.**
2. **Actor identity is primary.** Reviewers, authors, operators, and approvers must resolve to stable governed actor identities. Usernames, email strings, display names, role labels, certificates, or bot names alone are insufficient.
3. **Role authority must be current and scoped.** A reviewer must have a valid authority assignment for the action, domain, sensitivity class, and time of review.
4. **Subject binding is mandatory.** Review evidence must bind to the exact candidate, digest/spec hash, release scope, policy set, and version reviewed.
5. **No self-approval for public release.** The actor who authored, assembled, materially transformed, or submitted a release candidate must not be the sole actor authorizing its transition to `PUBLISHED` or a public alias.
6. **Sensitive and rights-constrained release requires additional independent roles.** Sensitivity and rights/sovereignty review must be separate from the author and release approver when applicable.
7. **Correction and rollback remain independently reviewed.** The detector/requestor and original publisher cannot be the sole correction/rollback approver.
8. **Automation is evidence, not authority.** CI, policy engines, validators, signers, AI, and bots may produce checks, receipts, or recommendations; they cannot substitute for an accountable human approval where this ADR requires one.
9. **Missing independence fails closed.** When qualified independent reviewers or verifiable assignments are unavailable, the result is `HOLD`, not self-approval.
10. **The review graph, not one object, proves SoD.** PromotionDecision, ReviewRecord, ReleaseManifest, signature packets, correction/rollback records, and receipts must cross-reference one governed subject and be evaluated together.
11. **High-risk withdrawals may use the emergency containment exception below, but restoration or re-release always requires independent review.**

### Normative language boundary

`MUST`, `MUST NOT`, `SHOULD`, and `MAY` describe the proposed accepted state. They do not describe current repository enforcement.

[Back to top](#top)

---

<a id="proposed-role-and-identity-model"></a>

## Proposed role and identity model

### Candidate role vocabulary

The names below preserve Atlas lineage while aligning with current repository terms. Acceptance would make the meanings authoritative for this decision; it would not by itself assign a person to a role.

| Role | Responsibility | Independence trigger |
|---|---|---|
| **Source steward** | Source admission, source role, terms, provenance, activation/retirement | Unresolved rights, authority, source-role, or sovereignty |
| **Domain/data steward** | Candidate meaning, transformations, domain validation, release assembly input | Cannot solely approve own public release candidate |
| **Evidence reviewer** | EvidenceRef resolution, EvidenceBundle sufficiency, citation/claim support | Material public claims or evidence conflict |
| **Sensitivity reviewer** | Redaction, generalization, precision, access tier, harmful inference | Sensitive spatial, living-person, ecology, archaeology, infrastructure, DNA |
| **Rights/sovereignty representative** | Consent, sovereignty, cultural authority, redistribution constraints | Sovereign, cultural, consent-based, or unclear-rights release |
| **Policy reviewer/admin** | Policy meaning, deny/restrict rules, policy bundle review | Release-enabling policy or policy exception |
| **Release authority** | Accountable final release decision and public-state transition | Every `PUBLISHED` or public-alias transition |
| **Correction reviewer** | Correction, withdrawal, supersession, public notice | Steward-significant correction or disputed release |
| **Rollback authority/reviewer** | Rollback target, execution authorization, verification | Rollback or restoration of public state |
| **AI surface steward** | Public AI templates, evidence binding, policy integration | Public/policy-significant AI surface change |
| **Docs/architecture steward** | ADR/doctrine integrity and control-plane documentation | Decision status, doctrine publication, cross-root governance |
| **Automation actor** | CI, validator, policy, signer, deployment execution | Never satisfies required accountable human approval by itself |

A person may hold multiple roles, but one actor still counts once for independence. The same human using multiple accounts or credentials also counts once after identity resolution.

### Actor and authority evidence

A conforming implementation needs accepted semantic/machine profiles for:

- stable `actor_ref` and alias resolution;
- human, service, bot, and external-representative actor classes;
- role/authority assignment with scope, issuer, effective time, expiry/revocation, and evidence;
- conflict-of-interest or recusal status where required;
- reviewer independence requirements for an action class;
- review subject identity and version/digest binding;
- accountable signature or integrity binding over the review record;
- correction and supersession of actor/role records.

This ADR does not assign exact file paths until Directory Rules and adjacent contract decisions are reviewed. It must not create a parallel identity, governance, or release home by convenience.

[Back to top](#top)

---

<a id="proposed-separation-matrix"></a>

## Proposed separation matrix

| Action | Minimum independent evidence | Required result when missing |
|---|---|---|
| Routine source admission with clear public rights | Source steward review; author may be steward at low control maturity | `HOLD` on unresolved authority/rights |
| Source admission with sovereignty, consent, or unclear rights | Source steward + independent rights/sovereignty representative | `DENY` or `HOLD` |
| Routine non-sensitive normalization/validation | Deterministic checks; periodic independent audit | `ERROR`/`HOLD` if checks unavailable |
| Sensitivity-relevant transform | Author/domain steward + independent sensitivity reviewer | `DENY` or `HOLD` |
| Promotion to PROCESSED/CATALOG for sensitive material | Domain/data steward + independent sensitivity/policy review | `HOLD` |
| Public release or public alias transition | Candidate author/assembler distinct from release authority; evidence/policy reviews resolve | `DENY` or `HOLD` |
| Sensitive-lane public release | Author + independent sensitivity reviewer + release authority + rights/sovereignty representative where applicable | `DENY` or `HOLD` |
| Release-enabling policy/schema/validator/trust-root change | Implementer distinct from policy/security approver; release impact reviewed | `HOLD` |
| Correction, withdrawal, or supersession | Detector/requestor + independent correction reviewer + release authority when public state changes | `HOLD` |
| Rollback execution | Requestor/operator distinct from rollback/release authority; target independently validated | `HOLD` |
| Restore or re-release after incident/withdrawal | New independent review and release decision; emergency operator cannot self-restore | `DENY` or `HOLD` |
| Public AI surface or policy-binding change | AI surface steward + independent policy/docs review; sensitivity reviewer where affected | `HOLD` |
| ADR acceptance or doctrine publication affecting release | Docs/architecture steward + affected subsystem/release reviewer | Remains `proposed`/unpublished |

### Independence constraints

A review set passes only when all required constraints hold:

```text
resolved(author.actor_ref) != resolved(required_approver.actor_ref)
required_approver.authority is active and scoped to subject/action
review.subject_ref + subject_digest match the evaluated candidate
review occurs after or against the exact reviewed version
review is not revoked, superseded, expired, or recused
required human roles are not replaced by automation
```

A simple comparison of unverified strings is not sufficient.

[Back to top](#top)

---

<a id="proposed-control-maturity"></a>

## Proposed control maturity

The old ADR's M0–M3 idea is retained but corrected: maturity describes **control capability**, not permission to bypass high-risk review.

| Level | Control posture | Permitted scope | Public-release consequence |
|---|---|---|---|
| **M0 — Candidate-only bootstrap** | Documentation, schemas, fixtures, candidates, local checks; no independent release evidence | Non-public development and review preparation | No governed public release; result `HOLD` |
| **M1 — Recorded manual independence** | Independent human review recorded and subject-bound; identity/authority checked manually | Low-risk non-sensitive release pilots | Conditional release only with complete manual packet and accountable decision |
| **M2 — Machine-enforced high-risk SoD** | Actor/role resolution, policy, negative fixtures, required-review rules, and release gate enforce independence | Sensitive, rights-constrained, corrective, rollback, public-alias, trust-root changes | Minimum required level for these release classes |
| **M3 — Machine-enforced comprehensive SoD** | All release-significant matrix rows, recusal, revocation, audit, and organizational controls enforced | Repository-wide governed release | Goal state; still requires accountable humans |

### Graduation rules

- Maturity is declared per release/control profile, not inferred from a README or green check.
- Advancement requires a reviewed evidence packet and cannot be self-approved by the implementation author.
- A profile that cannot prove its level falls back to the lower verified level.
- Sensitive or rights-constrained public release requires M2; before M2 it remains held.
- Maturity may not be downgraded merely to make a blocked release pass.
- `control_plane/release_state_register.yaml` currently has no entries or maturity shape; this ADR does not claim it is the accepted maturity registry.

[Back to top](#top)

---

<a id="authority-and-publication-boundary"></a>

## Authority and publication boundary

Separation of duties is necessary but not sufficient. Independent approval does not replace:

- EvidenceBundle closure;
- source/rights/sensitivity decisions;
- schema and semantic validation;
- policy evaluation;
- artifact integrity and signatures;
- PromotionDecision and ReleaseManifest;
- correction, withdrawal, supersession, and rollback targets;
- public-client trust membrane controls.

Likewise, CODEOWNERS, branch protection, GitHub approval, a signature packet, or a policy result cannot independently create release authority. Each is one control surface whose evidence must join the governed release packet.

A public release may proceed only from approved released artifacts and interfaces. No direct RAW, WORK, QUARANTINE, internal catalog/proof/receipt, candidate, or model-output path is authorized by this ADR.

[Back to top](#top)

---

<a id="proposed-review-and-release-evidence-packet"></a>

## Proposed review and release evidence packet

A future release packet should resolve, without collapsing their meanings:

1. candidate/artifact identity and immutable digest/spec hash;
2. submitting/authoring actor and relevant producer receipts;
3. source, evidence, rights, sensitivity, and policy records;
4. independent ReviewRecord(s) bound to the exact subject/version;
5. reviewer actor identity and current role/authority assignment;
6. recusal/conflict statements where policy requires them;
7. PromotionDecision referencing review and support records;
8. ReleaseManifest referencing the exact artifacts and decision;
9. reviewer signature packet or machine signature where separately required;
10. correction, withdrawal, supersession, rollback, and public-alias targets;
11. SoD validation result and reason codes;
12. execution receipt proving the approved transition was the transition performed.

### Schema responsibility guidance

Do not duplicate every actor field into every object. Prefer explicit references and join validation:

- `ReviewRecord` owns individual review action, actor, role, subject binding, decision, and time.
- `PromotionDecision` owns the accountable promotion outcome and references required reviews.
- `ReleaseManifest` owns release scope and references the decision/reviews/artifacts.
- `CorrectionNotice` and `RollbackCard` reference independent review/decision records.
- `AIReceipt` remains runtime process memory; public AI-surface governance needs a separate review/decision reference rather than turning an AI receipt into approval.

Exact field names and homes remain contract/schema decisions. A semantic draft is tracked at case-sensitive `contracts/governance/ReviewRecord.md`, while schema metadata names lowercase `review_record.md`; that path conflict must be resolved before schema expansion.

[Back to top](#top)

---

<a id="proposed-validation-and-finite-outcomes"></a>

## Proposed validation and finite outcomes

SoD validation is a prerequisite report, not a PromotionDecision.

| Outcome | Meaning |
|---|---|
| `PASS` | Required independent actors, authority, subject binding, and review evidence resolve |
| `DENY` | Known actor collapse, unauthorized approver, bot substitution, revoked assignment, or prohibited self-approval |
| `HOLD` | Required reviewer, authority assignment, rights/sensitivity decision, or complete evidence packet is unavailable |
| `ERROR` | Identity resolver, policy engine, schema, signature, storage, or validator failed |

`ERROR` and `HOLD` never become `PASS` by timeout, comment, or administrator override without a governed replacement decision.

### Minimum reason-code families

- `actor_identity_unresolved`
- `actor_alias_collapse`
- `author_approver_collapse`
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
- `emergency_containment_review_due`

### Required negative fixtures

At minimum:

- same actor under two role labels;
- same human through two accounts/aliases;
- bot/AI listed as release approver;
- actor assignment missing, expired, revoked, or out of scope;
- review bound to old candidate version/digest;
- review copied across domains or releases;
- author also sole release authority;
- sensitive release missing sensitivity review;
- archaeology/sovereign/consent release missing rights representative;
- detector self-approves correction;
- rollback requestor self-approves rollback;
- emergency operator restores release without independent review;
- CODEOWNERS approval present but governed review record absent;
- required reviewer unavailable in a single-maintainer repository;
- complete green path with distinct verified actors and subject binding.

[Back to top](#top)

---

<a id="current-repository-evidence"></a>

## Current repository evidence

| Surface | Current verified state | Safe conclusion |
|---|---|---|
| ADR-0024 | Exact file, source `draft`, effective `proposed` | Decision not accepted |
| CODEOWNERS | One account owns all relevant roots; comments explicitly disclaim SoD proof | No independent reviewer route established |
| PromotionDecision schema | Has reviewer string/ticket; no proposer/approver actor model | Shape cannot prove SoD |
| ReviewRecord schema | Requires review ID, subject ref, coarse role, decision, reasons, obligations, time | No actor identity, authority assignment, version/digest binding, recusal, or signature |
| ReviewRecord fixtures | One minimal schema pair plus a separate synthetic promotion Gate G subset | Broader governed SoD, alias, role-policy, current-head, recusal, signature, and release-record coverage remains absent |
| ReviewRecord contract | Authored draft exists as `contracts/governance/ReviewRecord.md`; schema declares lowercase `review_record.md` | Case/path relationship and acceptance remain conflicted |
| ReviewRecord validator | Bounded fixture-only candidate with finite outcomes, canonical syntax, review-time issuance, declared authority interval, explicit supersession marker, separation, and binding checks | No live alias/registry resolution, accepted role policy, current review-head lookup, governed record, or release authority |
| ReleaseManifest schema | Requires only `id`; extra properties allowed | No release-grade review fields |
| CorrectionNotice schema | Empty open scaffold | No correction-review enforcement |
| RollbackCard schema | Requires only `id`; extra properties allowed | No rollback-review enforcement |
| AIReceipt schema | Runtime receipt with no governance actor fields | Cannot prove AI-surface change SoD |
| release/reviews | Guidance plus atmosphere README/marker only | Promotion workflow confirms no governed ReviewRecord |
| release/promotion_decisions | Draft guidance and hydrology smoke sublane | No accountable release decision maturity |
| release/signatures | Reviewer signoff guidance and one draft packet | Not final approval or independent actor proof |
| release-state register | `entries: []`; no maturity field | No declared lane maturity |
| policy/release | README stub; SoD policy absent | No executable release SoD policy |
| promotion workflow | Read-only bounded candidate checks, unresolved smoke refs, and explicit authority hold | No governed review, promotion, release, or publication authority |

[Back to top](#top)

---

<a id="current-enforcement-maturity"></a>

## Current enforcement maturity

| Capability | Current state |
|---|---|
| ADR identity/status | `CONFIRMED / proposed` |
| Role vocabulary | Doctrine/design lineage; not accepted repository contract |
| Actor identity/alias resolution | `UNKNOWN` |
| Stewardship/authority assignment | `UNKNOWN` |
| ReviewRecord semantic contract | Draft exists at case-conflicted path; not accepted |
| ReviewRecord schema | Proposed shape only |
| ReviewRecord fixtures | Minimal schema cases plus bounded synthetic Gate G cases |
| ReviewRecord validator | Fixture-only candidate; no live identity/authority or governed-record resolution |
| SoD policy | Absent at checked path |
| Lane maturity registry | Empty proposed register; no accepted profile |
| Independent CODEOWNERS route | Not established |
| Required branch review/rulesets | `NEEDS VERIFICATION` |
| Governed release ReviewRecords | None confirmed by workflow |
| Promotion/release integration | `WORKFLOW_HOLD` |
| Sensitive-release two-person enforcement | Not established |
| Correction/rollback SoD | Not established |
| Production release/publication proof | None |

**Overall maturity: `M0 / HOLD`.** Candidate and documentation work may proceed, but no current evidence supports a claim of governed independent release approval.

[Back to top](#top)

---

<a id="implementation-and-convergence-plan"></a>

## Implementation and convergence plan

Implement in small, dependency-ordered, reversible slices:

1. **Review/accept or revise ADR-0024.** Do not let implementation artifacts accept it by implication.
2. **Define actor identity and authority assignment.** Include aliases, actor class, scope, effective time, revocation, and issuer.
3. **Create/fix the ReviewRecord semantic contract.** Align the declared contract path or migrate through an ADR-backed path decision.
4. **Version the ReviewRecord schema and fixtures.** Add actor/role/subject/version/authority references and negative cases.
5. **Graduate beyond the fixture-only ReviewRecord candidate.** Accept the actor/role/current-review profile, add registry and policy resolution, governed fixtures/records, stable outcomes/reason codes, and retain no release side effects.
6. **Define release-review policy.** Select the accepted policy home; begin observe-only only when reports are auditable, then deny mode through reviewed change.
7. **Reconcile release objects.** PromotionDecision, ReleaseManifest, correction, rollback, AI-surface review, and signature packets reference the governed review graph without duplicating authority.
8. **Establish independent reviewer capacity.** At least two qualified human actors for each required action class; otherwise release remains held.
9. **Wire repository controls.** CODEOWNERS/rulesets/required reviews supplement, but do not replace, governed records.
10. **Declare and validate control maturity.** Use an accepted registry/profile, not inferred README state.
11. **Wire promotion and release.** Validate exact subject digests, actor independence, policy, evidence, release, correction, and rollback before mutation.
12. **Exercise negative paths and drills.** Sensitive release, policy change, correction, rollback, emergency containment, alias restoration.
13. **Graduate only on observed evidence.** Current workflow hold is replaced only by real governed records and deterministic tests.

### Documentation obligations

When behavior changes, update this ADR or an accepted successor, the ADR index if status/supersession changes, contracts, schemas, policy docs, release/review READMEs, runbooks, registers, and test/fixture documentation together.

[Back to top](#top)

---

<a id="acceptance-gates"></a>

## Acceptance gates

- [ ] Architecture, release, governance/review, affected domain, evidence, policy/sensitivity, rights, correction/rollback, validation, security, and docs reviewers approve the proposed model.
- [ ] Role names and their mapping to current repository terms are agreed without claiming current assignments.
- [ ] Release-significant action classes and required independent roles are explicit.
- [ ] Actor identity and alias-resolution dependency is accepted or explicitly bounded.
- [ ] Automation/AI non-approval rule is explicit.
- [ ] Subject/version/digest binding is mandatory.
- [ ] M0–M3 is accepted as control maturity, not permission to bypass sensitive review.
- [ ] Sensitive and rights-constrained public release requires at least M2.
- [ ] Emergency containment cannot authorize restoration/re-release.
- [ ] Current single-account CODEOWNERS posture is recorded as insufficient for independent approval.
- [x] The fixture-only validator is distinguished from governed identity, authority, policy, review-record, and release enforcement.
- [ ] No statement claims current release, review, SoD, rollback, or publication capability.

Implementation graduation additionally requires:

- [ ] accepted actor/authority and ReviewRecord contracts/schemas;
- [ ] non-empty SoD valid/invalid fixtures;
- [ ] real validator and policy with stable reason codes;
- [ ] independent qualified human actors and tested review routing;
- [ ] subject-bound review evidence referenced from promotion/release records;
- [ ] branch/ruleset and governance-record parity tests;
- [ ] sensitive-release, correction, rollback, and emergency drills;
- [ ] observed fail-closed behavior and no unauthorized public mutation.

[Back to top](#top)

---

<a id="consequences"></a>

## Consequences

### Positive

- Makes self-approval and role collapse detectable.
- Preserves Atlas/Encyclopedia design lineage without turning planning tables into implementation fact.
- Separates actor identity, role authority, review action, decision, manifest, execution, and receipt.
- Prevents bots, AI, CODEOWNERS, or string inequality from masquerading as independent review.
- Provides a staged path from documentation-only bootstrap to machine-enforced sensitive release.
- Makes correction, rollback, policy, public-alias, and emergency actions auditable.

### Costs

- Requires actor/authority governance and alias resolution.
- Requires more than one qualified human for release-significant actions.
- Adds schema, fixture, validator, policy, repository-rule, and operational complexity.
- May hold releases in a single-maintainer project.
- Requires review records to be reissued when subject versions or digests change.
- Creates administrative work for assignment expiry, revocation, recusal, and backup coverage.

### Preserved invariants

- No canonical root or lifecycle phase changes.
- Promotion remains a governed state transition.
- Evidence, policy, review, decision, receipt, proof, release, and publication remain distinct.
- Public clients remain behind governed/released interfaces.
- Sensitive data remains deny-by-default.

[Back to top](#top)

---

<a id="alternatives-considered"></a>

## Alternatives considered

| Alternative | Disposition |
|---|---|
| Informal convention only | Rejected: deadline pressure and staff changes make it non-auditable |
| CODEOWNERS or PR approvals only | Rejected: routing/approval does not bind evidence, subject digest, role authority, release action, or execution |
| `author_id != approver_id` strings only | Rejected: aliases, multiple accounts, bots, stale identities, and role labels defeat the check |
| One combined release manager role | Rejected: collapses author, policy, sensitivity, rights, correction, and release authority |
| Automation/AI as second approver | Rejected: automation supplies evidence/checks, not accountable human judgment |
| Tooling required for all work from day one | Rejected: blocks candidate/bootstrap work; M0 permits non-public work but not release |
| Manual review forever | Rejected: high-risk release must graduate to machine-enforced checks |
| Per-domain unrelated SoD policies | Rejected as default: causes vocabulary and enforcement drift; domain additions should extend one governed profile |
| Self-approval when no second maintainer exists | Rejected: unavailable independent review yields `HOLD`, not weaker governance |

[Back to top](#top)

---

<a id="risk-and-open-question-ledger"></a>

## Risk and open-question ledger

| Item | Status | Required resolution |
|---|---|---|
| Actor identity contract/home | `OPEN` | Directory Rules review, semantic contract, schema, alias resolution |
| Role/authority assignment contract | `OPEN` | Scope, issuer, effective time, expiry/revocation, evidence |
| Atlas role names vs repository terms | `NEEDS VERIFICATION` | Accepted vocabulary/crosswalk |
| ReviewRecord contract path/casing | `CONFLICTED` | Reconcile schema-declared lowercase path with tracked `ReviewRecord.md` through governed migration |
| ReviewRecord actor/subject fields | `PROPOSED` | Versioned schema/fixtures/migration |
| SoD policy home | `OPEN` | `policy/release/`, `policy/governance/`, or accepted composition |
| Release manifest singular/plural paths | `CONFLICTED` | Separate ADR/accepted path decision |
| PromotionDecision vs prose lane outcomes | `CONFLICTED` | Contract and release-lane convergence |
| CODEOWNERS single account | `CONFIRMED LIMIT` | Independent qualified actor/team assignments |
| Branch protection/rulesets | `UNKNOWN` | Current GitHub ruleset evidence |
| External rights representative identity | `OPEN` | Attestation, authority, privacy, retention profile |
| Recusal/conflict-of-interest rules | `OPEN` | Policy and review-record fields |
| Reviewer signature integrity | `OPEN` | Signing profile separate from human authority |
| Emergency withdrawal SLA | `OPEN` | Timebox, scope, follow-up, incident/correction records |
| Single-maintainer operating model | `HOLD RISK` | Add qualified reviewers or keep release non-public |
| Maturity registry | `OPEN` | Accepted schema/register; current register empty |
| Historical release audit | `UNKNOWN` | Inventory prior decisions/reviews and classify gaps |
| Separation-of-duties monitoring | `OPEN` | Audit/reporting without treating dashboards as proof |

[Back to top](#top)

---

<a id="emergency-containment-exception"></a>

## Emergency containment exception

A narrowly scoped exception may permit one authorized operator to **reduce exposure** immediately when delay creates credible harm—for example:

- disable a public alias;
- withdraw or quarantine a release;
- restrict access;
- revoke a compromised signer or credential;
- stop a serving path;
- apply a temporary deny rule.

This exception:

1. never permits new publication or broader access;
2. never permits the operator to approve restoration or re-release;
3. requires an immutable incident/containment record, exact subject, reason, actor, time, and action;
4. requires independent review within a policy-defined timebox;
5. requires correction/withdrawal/rollback records and cache invalidation where applicable;
6. expires fail-closed if follow-up review is not completed;
7. cannot be used to bypass routine release review.

The current repository does not implement or authorize this exception; it is part of the proposed decision.

[Back to top](#top)

---

<a id="rollback-and-supersession"></a>

## Rollback and supersession

### Documentation-only rollback

Restore prior ADR blob:

```text
517493105f8464457782dee1ada5bf1e6db43c79
```

A transparent revert restores the prior proposed documentation. It does not change repository controls, actor assignments, review records, release state, or public artifacts.

### If this ADR is later accepted

Accepted ADRs are governance history. Do **not** flip an accepted decision back to `proposed` or silently weaken it. A material change requires:

- a successor ADR;
- reciprocal supersession links;
- updated ADR index;
- migration/compatibility plan for contracts, schemas, fixtures, policies, validators, review records, release objects, repository controls, and runbooks;
- correction/rollback analysis for releases that relied on the prior rule.

### Control rollback

Disabling or weakening an implemented SoD control requires independent review at least as strong as the control being changed. Moving policy into an invented `_disabled` folder, deleting review evidence, removing required reviewers, or downgrading maturity to unblock a release is not an acceptable rollback strategy without an accepted migration decision.

[Back to top](#top)

---

<a id="verification-checklist"></a>

## Verification checklist

### Current revision

- [x] ADR ID, filename, H1, and index row verified.
- [x] Source `draft` and effective `proposed` status preserved.
- [x] Directory Rules and supplied Atlas/Encyclopedia lineage reviewed.
- [x] Current schemas, fixtures, bounded candidate validator, release lanes, policy root, register, CODEOWNERS, and promotion workflow inspected.
- [x] Current gaps and workflow holds made explicit.
- [x] String inequality replaced by actor identity, authority, and subject-binding requirements.
- [x] M0 corrected to candidate-only; no maturity level authorizes unreviewed sensitive release.
- [x] Emergency containment separated from restoration/re-release.
- [x] Accepted-ADR rollback corrected to successor/supersession discipline.
- [x] No implementation, review, release, rollback, or publication claim introduced.
- [ ] Human review completed.
- [ ] ADR accepted.
- [ ] Implementation graduated.
- [ ] Governed release observed.

### Future implementation

- [ ] Actor/alias and authority-assignment profiles accepted.
- [ ] ReviewRecord semantic contract exists and matches schema.
- [ ] SoD fields/references are subject-bound and versioned.
- [ ] Validator and policy produce stable finite outcomes/reason codes.
- [ ] Valid/invalid fixtures cover aliases, bots, stale roles, subject mismatches, sensitive release, correction, rollback, and emergency paths.
- [ ] Independent qualified reviewer capacity exists.
- [ ] CODEOWNERS/rulesets complement governed review records.
- [ ] PromotionDecision and ReleaseManifest resolve review evidence.
- [ ] Corrections, withdrawals, rollback, and public aliases enforce separation.
- [ ] Audit and recovery drills pass without hidden overrides.

[Back to top](#top)

---

<a id="references"></a>

## References

| Reference | Relationship and current boundary |
|---|---|
| [`docs/adr/README.md`](./README.md) | ADR operating contract; merge does not accept a decision |
| [`docs/adr/INDEX.md`](./INDEX.md) | Confirms ADR-0024 identity, source `draft`, effective `proposed` |
| [ADR-0010](./ADR-0010-deny-by-default-for-dna-rare-species-archaeology-infrastructure.md) | Sensitive-domain fail-closed posture |
| [ADR-0011](./ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md) | Keeps review, receipt, proof, manifest, and publication distinct |
| [ADR-0015](./ADR-0015-data-published-_domain_-current-alias-is-governed-by-rollback_card.md) | Public alias/rollback decision dependencies |
| [ADR-0018](./ADR-0018-promotion-gate-sequence.md) | Promotion sequence and current readiness hold |
| [ADR-0020](./ADR-0020-abstain-is-a-first-class-decision.md) | Missing evidence/authority may abstain/hold rather than fabricate |
| [ADR-0023](./ADR-0023-geo-manifest-signs-every-pmtiles-cog-release.md) | Artifact cryptography is distinct from human approval |
| [ADR-0025](./ADR-0025-public-client-never-reads-canonical-internal-stores.md) | Public trust-membrane boundary |
| [Directory Rules](../doctrine/directory-rules.md) | Responsibility roots, authority, ADR/migration discipline |
| [PromotionDecision schema](../../schemas/contracts/v1/release/promotion_decision.schema.json) | Current reviewer string/ticket shape |
| [ReviewRecord schema](../../schemas/contracts/v1/governance/review_record.schema.json) | Proposed closed shape without actor identity |
| [ReviewRecord fixtures](../../fixtures/contracts/v1/governance/review_record/README.md) | Minimal shape fixtures; no SoD coverage |
| [ReviewRecord validator](../../tools/validators/validate_review_record.py) | Bounded fixture-only candidate; no live identity/authority, current-head, governed-record, or release authority |
| [ReleaseManifest schema](../../schemas/contracts/v1/release/release_manifest.schema.json) | Confirmed thin stub |
| [CorrectionNotice schema](../../schemas/contracts/v1/release/correction_notice.schema.json) | Confirmed empty/open scaffold |
| [RollbackCard schema](../../schemas/contracts/v1/release/rollback_card.schema.json) | Confirmed thin stub |
| [AIReceipt schema](../../schemas/contracts/v1/runtime/ai_receipt.schema.json) | Runtime receipt; no release-review actor fields |
| [Release reviews](../../release/reviews/README.md) | Review guidance; no governed records confirmed |
| [Promotion decisions](../../release/promotion_decisions/README.md) | Decision-lane guidance; not release proof |
| [Release signatures](../../release/signatures/README.md) | Human signoff packets; not final release authority |
| [Release-state register](../../control_plane/release_state_register.yaml) | Empty proposed register; no maturity model |
| [Release policy root](../../policy/release/README.md) | Greenfield stub |
| [CODEOWNERS](../../.github/CODEOWNERS) | Review routing only; no SoD proof |
| [Promotion workflow](../../.github/workflows/promotion-gate.yml) | Read-only readiness/hold evidence |
| KFM Domains v1.1 + Pass 23/32 Consolidated Atlas | Design lineage for reviewer/SoD matrix and ADR-S-09 |
| KFM Encyclopedia | Master Action Matrix separating steward/reviewer/policy/release duties |

[Back to top](#top)

---

<a id="revision-history"></a>

## Revision history

| Version | Date | Summary |
|---|---|---|
| v1 | 2026-05-15 | Initial draft proposing role vocabulary, separation matrix, M0–M3 maturity ladder, schema/policy/CODEOWNERS enforcement, validation, rollback, and Atlas ADR-S-09 closure. |
| v1.1 | 2026-07-24 | Re-grounded the ADR in current repository evidence; preserved effective proposed status; changed ADR-S-09 from claimed closed to addressed pending acceptance; separated design lineage from implementation; replaced string-only author/approver checks with actor identity, authority, and subject binding; corrected M0 to candidate-only; surfaced schema, policy, reviewer-capacity, and workflow holds; added emergency containment, convergence, acceptance, finite outcomes, risk, and successor-ADR rollback discipline. |

---

<sub>This ADR is governed by KFM doctrine: release is a governed state transition; review is evidence, not prose; automation is not accountable approval; sensitive and rights-constrained releases fail closed.</sub>
