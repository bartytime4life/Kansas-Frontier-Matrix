<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-release-readme
title: contracts/release — Release Contract Semantics README
type: readme
version: v0.2
status: draft; semantic-contract-lane; release-governance-aware; mixed-maturity
owners: OWNER_TBD — Release steward · Contracts steward · Schema steward · Policy steward · Evidence steward · Correction steward · Rollback steward · Docs steward · Directory Rules reviewer
created: NEEDS VERIFICATION — file existed before v0.2 expansion
updated: 2026-06-24
policy_label: public; contracts; release; semantic-contracts; promotion; release-manifest; rollback; correction-aware; withdrawal-aware; release-gated; no-artifact-store; no-runtime-authority
related:
  - ../README.md
  - ./release_manifest.md
  - ./promotion_decision.md
  - ./rollback_card.md
  - ./withdrawal_notice.md
  - ../correction/correction_notice.md
  - ../../schemas/contracts/v1/release/
  - ../../schemas/contracts/v1/correction/correction_notice.schema.json
  - ../../policy/release/
  - ../../policy/promotion/
  - ../../policy/sensitivity/
  - ../../release/
  - ../../docs/architecture/release-discipline.md
  - ../../docs/architecture/contract-schema-policy-split.md
  - ../../docs/standards/RELEASE_MANIFEST.md
  - ../../data/proofs/
  - ../../data/receipts/
tags: [kfm, contracts, release, promotion-decision, release-manifest, rollback-card, correction-notice, withdrawal-notice, release-gate, rollback, correction, supersession, auditability, no-file-move, release-gated]
notes:
  - "Expanded from existing `contracts/release/README.md`."
  - "This README is for human-readable semantic release object contracts only."
  - "Release object contracts are not the release artifact store, release process runner, policy engine, proof store, receipt store, public API, UI, map, or AI answer authority."
  - "Mixed maturity observed: `release_manifest.md` and `promotion_decision.md` contain object semantics; `rollback_card.md` and `withdrawal_notice.md` are scaffold-level; `correction_notice.md` is currently under `contracts/correction/`, creating a correction-vs-release placement seam."
  - "Rollback target for this expansion is previous blob SHA `fdbbf64f631b20d68f3984c200c1c1c5bd2cb3cb`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# contracts/release

> Semantic-contract lane for release governance object families. This folder explains the meaning of release objects such as `ReleaseManifest`, `PromotionDecision`, `RollbackCard`, and `WithdrawalNotice`. It does **not** store releases, publish artifacts, run promotion gates, replace policy, replace schemas, write proofs/receipts, or serve public API/UI/AI surfaces.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts-blue">
  <img alt="Family: release" src="https://img.shields.io/badge/family-release-0a7ea4">
  <img alt="Authority: semantic meaning" src="https://img.shields.io/badge/authority-semantic__meaning-blueviolet">
  <img alt="Invariant: not a file move" src="https://img.shields.io/badge/promotion-not__a__file__move-critical">
  <img alt="Posture: reversible" src="https://img.shields.io/badge/posture-reversible-green">
</p>

**Status:** draft / semantic-contract lane / mixed maturity  
**Path:** `contracts/release/README.md`  
**Owning root:** `contracts/` — human-readable semantic meaning for release object families  
**Schema authority:** `schemas/contracts/v1/release/`, not this folder  
**Policy authority:** `policy/release/`, `policy/promotion/`, and related policy roots, not this folder  
**Release artifact/process authority:** `release/`, not this folder  
**Truth posture:** CONFIRMED release README existed · CONFIRMED release object contracts and scaffolds observed · CONFIRMED release discipline doctrine says promotion is a governed state transition · NEEDS VERIFICATION for schemas, validators, fixtures, policy rules, CI, and release-runtime integration

## Quick jumps

[Scope](#scope) · [Repo fit](#repo-fit) · [Observed contract index](#observed-contract-index) · [Accepted contents](#accepted-contents) · [Exclusions](#exclusions) · [Release lifecycle semantics](#release-lifecycle-semantics) · [Object-family boundaries](#object-family-boundaries) · [Trust rules](#trust-rules) · [Validation checklist](#validation-checklist) · [Open questions](#open-questions) · [Rollback](#rollback)

---

## Scope

`contracts/release/` defines semantic meaning for release governance objects.

In scope:

- Markdown contracts that explain release object meaning;
- release-manifest semantics;
- promotion-decision semantics;
- rollback-card semantics;
- withdrawal-notice semantics;
- release object naming and boundary rules;
- release/correction/rollback relationship notes;
- cross-references to schemas, policy, fixtures, tests, release artifacts, proofs, receipts, and doctrine.

Out of scope:

- release artifact storage;
- release manifest JSON instances;
- promotion decision JSON instances;
- signed attestations, receipts, proof packs, or content-addressed artifacts;
- executable policy gates;
- schema definitions;
- release pipelines or runners;
- public API, UI, map, or AI output.

> [!IMPORTANT]
> Promotion is a governed state transition, not a file move. A release contract can define what a release object means; it cannot publish an artifact by itself.

---

## Repo fit

| Responsibility | Correct home | This README's boundary |
|---|---|---|
| Release object meaning | `contracts/release/` | This folder. Human-readable semantic contracts only. |
| Correction object meaning | `contracts/correction/` and/or release/correction seam | Current inspected `CorrectionNotice` contract is under `contracts/correction/`; placement seam remains NEEDS VERIFICATION. |
| Machine schemas | `schemas/contracts/v1/release/` and `schemas/contracts/v1/correction/` | Shape authority. |
| Release policy | `policy/release/`, `policy/promotion/`, sensitivity/rights/access policy roots | Admissibility and gate decisions. |
| Release artifact records | `release/` | Release candidates, manifests, correction/rollback records, and publication process outputs. |
| Receipts and proofs | `data/receipts/`, `data/proofs/` or accepted roots | Auditable evidence of gate execution. |
| Lifecycle data | `data/raw/`, `data/work/`, `data/quarantine/`, `data/processed/`, `data/catalog/`, `data/published/` | Evidence-bearing artifacts by phase. |
| Runtime/API/UI | `apps/`, `ui/`, `web/`, packages, or governed API roots | Downstream consumers only. |
| Release doctrine | `docs/architecture/release-discipline.md`, `docs/standards/RELEASE_MANIFEST.md` | Explains process and standards, not object instance storage. |

---

## Observed contract index

| Contract path | Object family | Observed maturity | Notes |
|---|---|---|---|
| `README.md` | Release contract-lane README | Expanded in this change. | Semantic lane only. |
| `release_manifest.md` | `ReleaseManifest` | PROPOSED; object semantics present. | Current contract says schema is thin/permissive and follow-up hardening is needed. |
| `promotion_decision.md` | `PromotionDecision` | PROPOSED; object semantics present. | States promotion is a state transition decision, not a file move. |
| `rollback_card.md` | `RollbackCard` | PROPOSED greenfield scaffold. | Needs expansion and schema/validator/fixture verification. |
| `withdrawal_notice.md` | `WithdrawalNotice` | PROPOSED greenfield scaffold. | Needs expansion and schema/validator/fixture verification. |
| `../correction/correction_notice.md` | `CorrectionNotice` | Draft semantic contract under correction family. | Placement seam between correction and release remains NEEDS VERIFICATION. |

---

## Accepted contents

Release contracts may describe:

| Accepted item | Purpose | Required posture |
|---|---|---|
| `README.md` | Release contract-family orientation. | Accepted. |
| `release_manifest.md` | Meaning of release manifest object family. | Must not be release artifact storage. |
| `promotion_decision.md` | Meaning of promotion decision object family. | Must preserve promotion as governed transition. |
| `rollback_card.md` | Meaning of rollback target and rollback instruction object family. | Must preserve reversibility/auditability. |
| `withdrawal_notice.md` | Meaning of withdrawal notice object family. | Must prevent silent disappearance. |
| Release/correction seam notes | Notes linking release objects to correction/rollback/withdrawal objects. | Must not duplicate canonical correction contracts. |

---

## Exclusions

| Do not put this here | Correct owner / home | Reason |
|---|---|---|
| JSON Schema files | `schemas/contracts/v1/release/` or accepted schema home | Schemas own machine-checkable shape. |
| Release JSON instances or manifest artifacts | `release/` or accepted release artifact roots | Contracts define meaning; they do not store releases. |
| Rego/OPA/equivalent policy rules | `policy/release/`, `policy/promotion/`, related policy roots | Policy owns admissibility. |
| Proof packs, receipt records, signing artifacts | `data/proofs/`, `data/receipts/`, release/signing roots | Trust artifacts remain separately auditable. |
| RAW/WORK/QUARANTINE/PROCESSED/CATALOG/TRIPLET/PUBLISHED data | `data/<phase>/` | Lifecycle state must remain phase-visible. |
| Runtime runners, release CLIs, pipelines | `packages/`, `pipelines/`, `tools/`, or repo-confirmed implementation roots | Execution is implementation, not semantic contract. |
| Public API routes, UI, map layers, AI answers | `apps/`, `ui/`, `web/`, governed runtime roots | Public surfaces are downstream of release gates. |
| Silent edits to published artifacts | Nowhere | Corrections, withdrawals, and rollbacks must be explicit artifacts. |

---

## Release lifecycle semantics

Release contracts apply at and after the transition into `PUBLISHED`:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Key release-adjacent transitions:

| Transition | Required semantic objects | Failure-closed posture |
|---|---|---|
| CATALOG/TRIPLET → PUBLISHED | `ReleaseManifest`, release policy decision, review where required, rollback target. | HOLD at CATALOG/TRIPLET; no public surface change. |
| PUBLISHED → PUBLISHED′ correction | `CorrectionNotice`, review, invalidation/supersession path, updated release manifest where needed. | No silent edit; stale-state or hold if incomplete. |
| PUBLISHED → prior release rollback | `RollbackCard`, correction/rollback notice, targeted prior release, invalidation list. | Hold until rollback target validates. |
| PUBLISHED → withdrawn | `WithdrawalNotice`, reason, affected artifacts, public-safe notice, successor/rollback if any. | Do not delete without audit trail. |

---

## Object-family boundaries

| Object | Means | Does not mean |
|---|---|---|
| `ReleaseManifest` | Governed manifest binding a release identity/version/spec lineage and release artifact set. | Not proof closure by itself; not release approval without gates; not raw artifact storage. |
| `PromotionDecision` | Reviewed decision to approve, deny, or abstain on a transition. | Not a file move; not a runtime response; not release manifest. |
| `RollbackCard` | Named rollback target/instructions for reversing or restoring a prior public state. | Not deletion; not silent mutation; not proof that rollback has run. |
| `WithdrawalNotice` | Named notice that a published artifact/claim/release is withdrawn or no longer public-safe. | Not erasure; not destruction of audit history. |
| `CorrectionNotice` | Named post-release repair/supersession/stale/wrong/redaction/dispute artifact. | Not currently canonical in this folder; inspected path is `contracts/correction/correction_notice.md`. |

---

## Trust rules

1. **Semantic only.** `contracts/release/` explains object meaning. It does not execute releases.
2. **Promotion is not movement.** Copying, renaming, deploying, or merging a file does not make it published.
3. **Release requires closure.** Required artifacts must exist, required references must resolve, and policy decisions must be recorded.
4. **Public clients are downstream.** Public API/UI/map/AI surfaces consume released artifacts through governed interfaces only.
5. **Rollback is first-class.** Every material release must have a rollback target or an explicit reason why rollback is impossible and what mitigation applies.
6. **Corrections are visible.** Published records are corrected, superseded, withdrawn, or rolled back with notices, not silently edited.
7. **Receipts/proofs stay separate.** Release contracts may require proof and receipts; they do not store those artifacts.
8. **Sensitivity and rights fail closed.** Unknown rights, unresolved evidence, missing review, sensitive exact location, living-person data, DNA/genomics, archaeology, infrastructure, or cultural sensitivity blocks or restricts release until governed.

---

## Validation checklist

- [ ] Every release contract has a paired schema or explicitly marked schema gap.
- [ ] Every schema path exists or is labeled NEEDS VERIFICATION.
- [ ] Validators are identified and wired, or labeled NEEDS VERIFICATION.
- [ ] Fixtures include valid, invalid, denied/abstained/held, correction, withdrawal, and rollback cases.
- [ ] Release policy decisions are modeled separately from release manifests.
- [ ] Release manifests do not replace EvidenceBundle, ReviewRecord, PolicyDecision, proof, or receipt artifacts.
- [ ] Public surfaces cannot read RAW, WORK, QUARANTINE, canonical/internal stores, or direct model output.
- [ ] Correction and rollback paths are auditable.

---

## Open questions

- Should `CorrectionNotice` remain under `contracts/correction/`, or should release README list it only as an adjacent family?
- Should `contracts/release/correction_notice.md` be recreated as a compatibility pointer, or avoided to prevent duplicate authority?
- When should `release_manifest` schema move from permissive placeholder to closed, explicit signed-release shape?
- Which fixtures prove rollback and withdrawal negative states?
- Which release gate owns final separation-of-duties enforcement?

---

## Rollback

Rollback is required if this README is used to store release artifacts, publish content, bypass policy/review/schema/test gates, host executable release logic, silently correct public records, or treat generated AI output as release authority.

Rollback target for this expansion: previous blob SHA `fdbbf64f631b20d68f3984c200c1c1c5bd2cb3cb`.

<p align="right"><a href="#top">Back to top</a></p>
