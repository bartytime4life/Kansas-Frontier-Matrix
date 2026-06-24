<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-review-readme
title: contracts/review — Review Contract Semantics README
type: readme
version: v0.2
status: draft; compatibility-lane; semantic-boundary; no-parallel-authority
owners: OWNER_TBD — Review steward · Governance steward · Contracts steward · Schema steward · Policy steward · Release steward · Evidence steward · Docs steward · Directory Rules reviewer
created: NEEDS VERIFICATION — file existed before v0.2 expansion
updated: 2026-06-24
policy_label: public; contracts; review; governance-adjacent; semantic-contracts; review-record; separation-of-duties; no-parallel-authority; release-gated
tags: [kfm, contracts, review, review-record, governance, separation-of-duties, semantic-boundary, compatibility, evidence, policy, release, auditability, no-parallel-authority]
related:
  - ../README.md
  - ../governance/README.md
  - ../governance/ReviewRecord.md
  - ../release/README.md
  - ../release/promotion_decision.md
  - ../release/release_manifest.md
  - ../policy/policy_decision.md
  - ../evidence/evidence_bundle.md
  - ../../schemas/contracts/v1/governance/review_record.schema.json
  - ../../schemas/contracts/v1/review/
  - ../../policy/governance/
  - ../../policy/release/
  - ../../docs/governance/SEPARATION_OF_DUTIES.md
  - ../../docs/governance/ESCALATION.md
  - ../../docs/architecture/contract-schema-policy-split.md
  - ../../docs/architecture/release-discipline.md
  - ../../docs/focus-mode/state/review-state.md
notes:
  - "Expanded from existing `contracts/review/README.md` stub."
  - "Current inspected ReviewRecord contract authority is `contracts/governance/ReviewRecord.md`; this README must not duplicate or supersede it."
  - "No `schemas/contracts/v1/review/README.md` or review-family schema home was verified in this session; review schema placement remains NEEDS VERIFICATION."
  - "This README defines a review semantic boundary/pointer only. It does not create review approval, release approval, policy behavior, CODEOWNERS, branch protection, CI, review workflow enforcement, proof, receipt, public API/UI behavior, or AI truth claims."
  - "Rollback target for this expansion is previous blob SHA `22348e243d918d530f4ab0a429524c8f1abbf6bb`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# contracts/review

> Review-family semantic boundary for KFM. This folder is a compatibility/orientation lane for review concepts and review object pointers. The inspected canonical `ReviewRecord` semantic contract currently lives at [`../governance/ReviewRecord.md`](../governance/ReviewRecord.md), so this README must not become a competing review-record authority.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts-blue">
  <img alt="Family: review" src="https://img.shields.io/badge/family-review-0a7ea4">
  <img alt="Authority: semantic pointer" src="https://img.shields.io/badge/authority-semantic__pointer-lightgrey">
  <img alt="Canonical: governance" src="https://img.shields.io/badge/canonical-governance-purple">
  <img alt="Posture: no parallel authority" src="https://img.shields.io/badge/posture-no__parallel__authority-critical">
</p>

**Status:** draft / compatibility lane / semantic boundary  
**Path:** `contracts/review/README.md`  
**Owning root:** `contracts/` — semantic contract meaning only  
**Inspected canonical ReviewRecord contract:** [`../governance/ReviewRecord.md`](../governance/ReviewRecord.md)  
**Adjacent governance lane:** [`../governance/README.md`](../governance/README.md)  
**Schema posture:** `schemas/contracts/v1/governance/review_record.schema.json` is referenced by the governance contract; `schemas/contracts/v1/review/` was not verified  
**Policy authority:** `policy/governance/`, `policy/release/`, and related policy roots, not this README  
**Truth posture:** CONFIRMED target stub replaced · CONFIRMED `ReviewRecord` currently lives under `contracts/governance/` · CONFIRMED governance README says governance owns semantic review/review-record meaning · NEEDS VERIFICATION for any independent `contracts/review/` object roster, schemas, validators, fixtures, tests, CI, branch protection, CODEOWNERS, and runtime enforcement

## Quick jumps

[Scope](#scope) · [Repo fit](#repo-fit) · [Review vs governance](#review-vs-governance) · [Accepted contents](#accepted-contents) · [Exclusions](#exclusions) · [Review concepts](#review-concepts) · [Trust rules](#trust-rules) · [Validation checklist](#validation-checklist) · [Open questions](#open-questions) · [Rollback](#rollback)

---

## Scope

`contracts/review/` is a review-family boundary and compatibility lane.

It may define or point to semantic concepts such as:

- review scope;
- reviewer role;
- reviewer identity boundary;
- review basis refs;
- review disposition;
- review conditions;
- review expiration;
- review supersession;
- separation-of-duties context;
- review-to-release relationships.

It must not duplicate the inspected `ReviewRecord` contract currently under `contracts/governance/`.

> [!IMPORTANT]
> A review record supports trust. It does not itself publish data, approve release, execute policy, resolve evidence as truth, or prove platform enforcement.

---

## Repo fit

| Responsibility | Correct home | Relationship to this README |
|---|---|---|
| Review semantic boundary | `contracts/review/README.md` | This file; compatibility/orientation lane. |
| Canonical inspected ReviewRecord object | `contracts/governance/ReviewRecord.md` | Current object-level review contract authority. |
| Governance contract lane | `contracts/governance/README.md` | Adjacent/canonical governance lane for review, stewardship, escalation, and separation-of-duties objects. |
| Release decisions and release objects | `contracts/release/` | Review records may support release, but release objects remain separate. |
| Policy decision meaning | `contracts/policy/policy_decision.md` | Policy gate outcome object, distinct from review. |
| Evidence support | `contracts/evidence/evidence_bundle.md` | Evidence authority; review may cite it. |
| Machine schemas | `schemas/contracts/v1/governance/` and/or future accepted `schemas/contracts/v1/review/` | Shape authority; current review schema placement is unresolved. |
| Governance/release policy | `policy/governance/`, `policy/release/` | Admissibility/enforcement rules. |
| Platform enforcement | `.github/`, CODEOWNERS, branch protection, CI | Implementation evidence; not contract authority. |
| Tests and fixtures | `tests/`, `fixtures/` | Enforceability and examples. |
| Docs/runbooks | `docs/governance/`, `docs/runbooks/`, `docs/architecture/` | Human process and doctrine; not object instance storage. |

---

## Review vs governance

The repository currently treats review as part of the governance contract family.

| Concern | Review boundary | Governance lane |
|---|---|---|
| Review vocabulary | May define shared review terms and compatibility notes. | Owns inspected `ReviewRecord` object contract. |
| Review event object | Do not duplicate here unless ADR/migration accepts a move. | `contracts/governance/ReviewRecord.md`. |
| Separation of duties | May point to required concepts. | Governance owns semantic stewardship/review responsibility. |
| Release support | Review may support promotion/release/correction/rollback. | Governance records review posture; release objects record release state. |
| Enforcement | Not implemented by contracts. | Still not implemented by governance contracts; enforcement is policy/platform/tests. |

---

## Accepted contents

Until an ADR or migration note accepts `contracts/review/` as a canonical object family, only conservative content belongs here.

| Accepted item | Purpose | Required posture |
|---|---|---|
| `README.md` | Boundary pointer and review-family orientation. | Accepted. |
| `GLOSSARY.md` | Optional shared review vocabulary. | Must point to canonical ReviewRecord contract. |
| `MIGRATION.md` | Temporary notes if review contracts move from governance to review. | Must include rollback and compatibility plan. |
| `BACKLINKS.md` | Optional backlink audit for references to review vs governance. | Pointer only. |
| `VALIDATION_NOTES.md` | Optional notes about schema/validator/test gaps. | Must not define machine schema or policy behavior. |

Object-level contracts under this folder remain PROPOSED until reviewed placement is accepted.

---

## Exclusions

| Do not put this here | Correct home | Reason |
|---|---|---|
| Duplicate `ReviewRecord` contract | `contracts/governance/ReviewRecord.md` unless ADR moves it | Avoids parallel authority. |
| JSON Schema | `schemas/contracts/v1/governance/` or accepted schema home | Schemas own shape. |
| Policy rules | `policy/governance/`, `policy/release/`, related policy roots | Policy owns admissibility/enforcement. |
| Review instances / approval records | governed data/release/governance artifact homes once accepted | Contracts define meaning; they do not store review events. |
| CODEOWNERS, branch protection, workflow config | `.github/` or platform settings | Platform enforcement is outside contract prose. |
| Receipts/proofs | `data/receipts/`, `data/proofs/` or accepted roots | Audit artifacts remain separate. |
| Release manifests or promotion decisions | `contracts/release/` and `release/` | Release state is not review state. |
| Public API/UI/map/AI behavior | governed runtime/API/UI roots | Review is upstream trust support only. |

---

## Review concepts

Review concepts are semantic building blocks used by `ReviewRecord` and related governance/release objects.

| Concept | Meaning | Boundary |
|---|---|---|
| `reviewed_object_ref` | The artifact, claim, source, policy, release candidate, map layer, AI output, or document being reviewed. | Must resolve where review affects trust-bearing output. |
| `review_scope` | Bounded review area such as source, evidence, schema, policy, sensitivity, release, AI, UI, map, docs, or cross-cutting. | Closed vocabulary recommended. |
| `reviewer_role` | Role used for the review: domain steward, source steward, contract steward, schema steward, policy steward, sensitivity reviewer, release authority, AI-surface steward, etc. | Must support separation of duties. |
| `basis_refs` | EvidenceBundle, SourceDescriptor, PolicyDecision, schema, fixture, ADR, release artifact, validation report, or document references used as review basis. | Reference is not enough; critical refs must resolve. |
| `disposition` | Outcome such as APPROVE, APPROVE_WITH_CONDITIONS, REQUEST_CHANGES, ABSTAIN, DENY, ESCALATE, NEEDS_VERIFICATION. | Vocabulary NEEDS VERIFICATION. |
| `conditions` | Conditions before merge, promotion, publication, display, export, or AI answer use. | Required for conditional approval. |
| `expires_at` | Time when review must be refreshed due to source cadence, sensitivity, evidence age, or release cycle. | Required for time-sensitive reviews. |
| `related_release_refs` | PromotionDecision, ReleaseManifest, RollbackCard, CorrectionNotice, WithdrawalNotice refs. | Required when review supports release/correction/rollback. |

---

## Trust rules

1. **Review is support, not sovereignty.** Review records support trust, but evidence, policy, release, and schema objects keep their own authority.
2. **Do not collapse review into approval.** A review can recommend/approve within a scope, but promotion/release still needs policy, manifests, and gates.
3. **References must resolve.** A review basis that cannot be resolved is not proof.
4. **Separation of duties matters.** Author, reviewer, sensitivity reviewer, and release authority should be separated where risk/materiality requires.
5. **Review is scoped.** Approval in one scope does not imply approval across all scopes.
6. **Sensitive reviews fail closed.** Rights, sovereignty, cultural sensitivity, living-person, DNA/genomics, rare species, archaeology, infrastructure, and exact-location exposure require conservative review posture.
7. **Generated language is not review evidence by itself.** AI summaries may help a reviewer, but ReviewRecord/EvidenceBundle/policy/release artifacts outrank generated language.

---

## Validation checklist

- [ ] Decide whether `contracts/review/` remains a compatibility lane or becomes canonical by ADR/migration.
- [ ] If canonical, create/move object contracts with rollback/backlink migration plan.
- [ ] Resolve schema home: `schemas/contracts/v1/governance/review_record.schema.json` vs `schemas/contracts/v1/review/`.
- [ ] Verify validators and fixtures for review records.
- [ ] Verify policy behavior for governance/review release gates.
- [ ] Verify separation-of-duties enforcement in policy/platform/CI where applicable.
- [ ] Verify public/released surfaces require review where doctrine/policy says they must.
- [ ] Verify review records do not leak sensitive facts in public-safe summaries.

---

## Open questions

- Should review stay under `contracts/governance/`, or should `contracts/review/` become the canonical review object family?
- Should `ReviewRecord.md` be renamed/moved to snake_case if schemas use `review_record.schema.json`?
- What is the accepted review disposition vocabulary?
- Which reviews require full `ReviewRecord` versus lightweight reviewer/ticket binding inside objects such as `PromotionDecision`?
- Which platform evidence proves separation-of-duties enforcement?

---

## Rollback

Rollback is required if this folder is used to create duplicate `ReviewRecord` authority, store review instances, bypass governance/release/policy/evidence gates, claim CI/CODEOWNERS/platform enforcement without verification, or authorize public API/UI/map/AI behavior directly.

Rollback target for this expansion: previous blob SHA `22348e243d918d530f4ab0a429524c8f1abbf6bb`.

<p align="right"><a href="#top">Back to top</a></p>
