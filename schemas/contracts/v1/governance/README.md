# `schemas/contracts/v1/governance/` — Governance Schema Family Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-governance-readme
title: schemas/contracts/v1/governance/ — Governance Schema Family Index
type: readme; schema-family-index; governance-boundary; review-stewardship-shape
authority_class: schema-family-index
version: v0.2
status: draft; schema-stubs-present; PROPOSED; overlap-sensitive; release-adjacent; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Governance steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Docs steward
created: NEEDS VERIFICATION — short stub existed before v0.2 expansion
updated: 2026-07-04
policy_label: public; schemas; contracts-v1; governance; review-record; stewardship-assignment; promotion-decision; redaction-receipt; separation-of-duties; auditability; release-adjacent; no-parallel-authority
tags: [kfm, schemas, contracts, v1, governance, ReviewRecord, StewardshipAssignment, PromotionDecision, RedactionReceipt, review, stewardship, separation-of-duties, drift, verification, release-gates, auditability, rollback]
related:
  - ../README.md
  - ./review_record.schema.json
  - ./steward_assignment.schema.json
  - ./promotion_decision.schema.json
  - ./redaction_receipt.schema.json
  - ../../../../contracts/governance/README.md
  - ../../../../contracts/governance/ReviewRecord.md
  - ../../../../contracts/governance/steward_assignment.md
  - ../../../../contracts/release/README.md
  - ../../../../schemas/contracts/v1/release/
  - ../../../../schemas/contracts/v1/policy/
  - ../../../../schemas/contracts/v1/evidence/
  - ../../../../policy/governance/
  - ../../../../policy/release/
  - ../../../../docs/governance/SEPARATION_OF_DUTIES.md
  - ../../../../docs/governance/ESCALATION.md
  - ../../../../docs/architecture/contract-schema-policy-split.md
  - ../../../../docs/architecture/publication/RELEASE_GATES.md
  - ../../../../docs/registers/DRIFT_REGISTER.md
  - ../../../../docs/registers/VERIFICATION_BACKLOG.md
notes:
  - "Expanded from a short stub at schemas/contracts/v1/governance/README.md."
  - "Current GitHub search surfaced review_record.schema.json, steward_assignment.schema.json, promotion_decision.schema.json, and redaction_receipt.schema.json under this folder."
  - "review_record.schema.json has concrete required fields and additionalProperties false, but remains x-kfm.status PROPOSED."
  - "steward_assignment.schema.json is a permissive PROPOSED stub requiring only id."
  - "promotion_decision.schema.json and redaction_receipt.schema.json are permissive PROPOSED scaffolds with empty properties and additionalProperties true."
  - "PromotionDecision and RedactionReceipt are release/policy/evidence-adjacent; this folder must not become a parallel release, policy, evidence, or receipt authority without ADR/migration notes."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![family](https://img.shields.io/badge/family-governance-purple)
![shape](https://img.shields.io/badge/authority-machine--shape-informational)
![maturity](https://img.shields.io/badge/maturity-PROPOSED-orange)
![release](https://img.shields.io/badge/release-adjacent-critical)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **Purpose.** `schemas/contracts/v1/governance/` is the machine-checkable schema family for governance objects that make review, stewardship, escalation, responsibility, drift, verification, and governance-support decisions inspectable.
>
> **One-line boundary.** This folder defines governance object **shape**. It does not implement governance, grant approval, enforce policy, publish artifacts, replace release gates, replace EvidenceBundles, or prove that review/separation-of-duties actually happened.

---

## Quick jumps

[Status](#status) · [Authority and placement](#authority-and-placement) · [Repo fit](#repo-fit) · [Current schema inventory](#current-schema-inventory) · [Known overlap and drift risks](#known-overlap-and-drift-risks) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Schema-family rules](#schema-family-rules) · [Governance trust guardrails](#governance-trust-guardrails) · [Promotion checklist](#promotion-checklist) · [Validation](#validation) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

| Question | Answer | Truth label |
|---|---|---|
| Does this README path exist? | Yes: `schemas/contracts/v1/governance/README.md`. It was a short stub before this expansion. | **CONFIRMED** |
| Are governance schema files present in this folder? | Yes. Search surfaced four schema files under `schemas/contracts/v1/governance/`. | **CONFIRMED path presence** |
| Are all governance schemas mature/field-complete? | No. `review_record.schema.json` has concrete fields, while the other opened schemas are permissive or empty scaffolds. | **CONFIRMED mixed maturity** |
| Is there paired governance contract prose? | Yes. `contracts/governance/README.md`, `ReviewRecord.md`, and `steward_assignment.md` were surfaced and inspected. | **CONFIRMED** |
| Is this folder release authority? | No. Release decisions, manifests, corrections, withdrawals, and rollback belong to release lanes; governance schemas may reference them. | **CONFIRMED boundary** |
| Can these schemas alone prove governance happened? | No. They shape records; proof requires actual records, reviewers, policy, release state, and audit trail. | **CONFIRMED governance boundary** |

> [!IMPORTANT]
> Governance records are trust-supporting objects, not trust by themselves. A schema-valid `ReviewRecord` or `StewardshipAssignment` is not proof that review occurred, that separation of duties was satisfied, that policy passed, or that a release is approved.

---

## Authority and placement

This folder is under the schema responsibility root:

```text
schemas/contracts/v1/governance/
```

It may define machine-checkable governance shapes, but adjacent authority is split:

- `contracts/governance/` owns semantic meaning for governance object families.
- `docs/governance/` owns human-facing governance standards such as separation of duties and escalation.
- `policy/governance/` owns admissibility posture where implemented.
- `contracts/release/` and `schemas/contracts/v1/release/` own release object meaning and shape.
- `schemas/contracts/v1/policy/` owns policy-decision and sensitivity machine shapes.
- `schemas/contracts/v1/evidence/` owns EvidenceBundle/EvidenceRef and evidence-support shapes.
- `fixtures/` and `tests/` prove valid/invalid governance behavior.

This README does not amend ADR-0001, Directory Rules, governance docs, release gates, policy, validators, or release doctrine.

---

## Repo fit

```text
schemas/
└── contracts/
    └── v1/
        ├── README.md
        ├── governance/
        │   ├── README.md                         # this file
        │   ├── review_record.schema.json         # PROPOSED concrete schema
        │   ├── steward_assignment.schema.json    # PROPOSED permissive stub
        │   ├── promotion_decision.schema.json    # PROPOSED empty scaffold; release-adjacent
        │   └── redaction_receipt.schema.json     # PROPOSED empty scaffold; receipt/policy/evidence-adjacent
        ├── release/                              # release object shapes; separate authority
        ├── policy/                               # policy object shapes; separate authority
        └── evidence/                             # evidence object shapes; separate authority

contracts/
├── governance/
│   ├── README.md
│   ├── ReviewRecord.md
│   └── steward_assignment.md
└── release/                                      # release semantic contracts; separate authority

docs/
├── governance/
├── architecture/
└── registers/

policy/
├── governance/
└── release/

fixtures/
tests/
release/
```

---

## Current schema inventory

Current GitHub search surfaced the following files under `schemas/contracts/v1/governance/`. This is a search-derived index, not a complete mounted-checkout manifest.

| File | Current opened signal | Paired contract signal | Status |
|---|---|---|---|
| `review_record.schema.json` | Draft 2020-12 object; concrete fields; required `review_id`, `subject_ref`, `reviewer_role`, `decision`, `reasons`, `obligations`, `reviewed_at`; `additionalProperties: false`; `x-kfm.status: PROPOSED`. | `contracts/governance/ReviewRecord.md` exists and defines review-event meaning. | **PROPOSED / partially shaped** |
| `steward_assignment.schema.json` | Draft 2020-12 object; permissive stub with `id`, `version`, `spec_hash`; requires only `id`; `additionalProperties: true`; `x-kfm.status: PROPOSED`. | `contracts/governance/steward_assignment.md` exists and defines stewardship-assignment meaning. | **PROPOSED scaffold** |
| `promotion_decision.schema.json` | Draft 2020-12 object; empty `properties`; `additionalProperties: true`; `x-kfm.status: PROPOSED`; `contract_doc: null`. | Release-adjacent; paired governance contract not confirmed. | **PROPOSED scaffold / placement-sensitive** |
| `redaction_receipt.schema.json` | Draft 2020-12 object; empty `properties`; `additionalProperties: true`; `x-kfm.status: PROPOSED`; `contract_doc: null`. | Receipt/policy/evidence-adjacent; paired governance contract not confirmed. | **PROPOSED scaffold / placement-sensitive** |

> [!NOTE]
> These files confirm path presence and scaffold intent. They do not confirm final field shape, validator behavior, fixture coverage, policy enforcement, release readiness, or public-safe behavior.

---

## Known overlap and drift risks

| Risk | Evidence | Required posture |
|---|---|---|
| Casing mismatch for ReviewRecord | Schema uses `review_record.schema.json`; contract path surfaced as `contracts/governance/ReviewRecord.md`, while schema `x-kfm.contract_doc` points to lowercase `contracts/governance/review_record.md`. | Resolve with casing/mirror/deprecation note before promotion. |
| PromotionDecision overlap | Promotion decisions are release-governance objects and may belong with `release/` schemas or governance depending on accepted model. | Do not let governance and release schemas become parallel authorities. |
| RedactionReceipt overlap | Redaction receipts may belong with evidence, policy, domain, receipt, or governance lanes depending on accepted receipt-home ADR. | Keep placement **NEEDS VERIFICATION** until receipt-home decision is resolved. |
| Permissive scaffold risk | Several governance schemas allow additional properties or have empty properties. | Do not rely on permissive schemas for governance proof or release approval. |

---

## What belongs here

- This README.
- Governance-family JSON Schema files after schema/contract review.
- Machine-readable shapes for review records, stewardship assignments, escalation records, governance decisions, drift records, verification backlog items, separation-of-duties records, and governance-support decision records where accepted.
- Migration notes, mirror notes, deprecation notes, and drift notes for governance schema placement.
- Links to paired semantic contracts, fixtures, validators, policy references, release references, evidence references, correction references, rollback references, and tests.

---

## What does not belong here

- Semantic contract prose.
- Policy rules or policy modules.
- Release approvals, release manifests, promotion decisions as emitted records, correction notices, withdrawal notices, or rollback cards as data.
- EvidenceBundle instances, source payloads, catalog records, proof outputs, receipt instances, review records as emitted data, or lifecycle payloads.
- Validator code, packages, runtime code, UI/API implementation, dashboards, screenshots, or generated summaries.
- Claims that review, approval, separation-of-duties, release, redaction, or policy compliance occurred merely because an object validates against a schema.

---

## Schema-family rules

| Rule | Requirement |
|---|---|
| Meaning/shape split | Contracts explain governance object meaning; schemas define machine shape only. |
| Governance/release split | Governance may support release, but release manifests, correction, withdrawal, and rollback remain release authority. |
| Governance/policy split | Governance records who reviewed or took responsibility; policy decides allow/deny/restrict/abstain. |
| Governance/evidence split | Review can inspect evidence, but EvidenceBundle remains evidence authority. |
| Review is not approval | A review record must state its scope and decision boundary; it must not silently become release approval. |
| Stewardship is not enforcement | Stewardship assignment records responsibility; it does not prove that the responsible party acted. |
| Deterministic identity | Governance records should use stable IDs and spec hashes where practical. |
| Auditability | Governance records must be inspectable, scoped, timestamped, and tied to reviewed object refs. |
| No parallel authority | Do not duplicate release, evidence, policy, receipt, or domain schema authority under `governance/` without ADR or migration notes. |

---

## Governance trust guardrails

A mature governance flow should preserve this boundary:

```text
artifact / claim / schema / policy / release candidate / AI output
  -> evidence and context refs
  -> reviewer / steward assignment / separation-of-duties check
  -> ReviewRecord / GovernanceDecision / EscalationRecord as applicable
  -> policy and release gates remain separate
  -> release-lane objects when release lane permits
  -> audit trail remains inspectable
```

Required fail-safe posture:

| Condition | Expected posture |
|---|---|
| Reviewer identity missing | Mark record invalid or **NEEDS VERIFICATION**; do not infer approval. |
| Reviewed object missing | Reject or mark invalid; review scope must be explicit. |
| Evidence/support refs missing | Record may exist, but trust-bearing action must abstain/deny or mark evidence gap. |
| Policy context missing | Review cannot imply policy pass. |
| Release context missing | Review cannot imply publication approval. |
| Stewardship unclear | Escalate or mark **NEEDS VERIFICATION**. |
| Separation-of-duties required but not proven | Block promotion or mark release gate unmet. |
| Schema is permissive | Do not treat validation as governance proof. |

---

## Promotion checklist

A governance schema should not advance beyond `PROPOSED` unless:

- [ ] Schema placement is settled against release, policy, evidence, receipts, and domain schema homes.
- [ ] Paired semantic contract exists and matches schema path/casing.
- [ ] `$id` and filename are stable.
- [ ] JSON Schema dialect is pinned.
- [ ] Required fields are defined.
- [ ] Valid fixtures exist.
- [ ] Invalid fixtures exist.
- [ ] Validator implementation exists.
- [ ] CI/schema-test support exists.
- [ ] Review scope, reviewer role, decision vocabulary, reason/obligation fields, timestamps, and subject refs are fixture-tested where applicable.
- [ ] Separation-of-duties and stewardship examples are represented where required.
- [ ] Release-adjacent objects do not duplicate release authority.
- [ ] Policy/evidence dependencies are explicit.
- [ ] Correction and rollback references are clear for public/release-affecting decisions.

---

## Validation

Recommended local validation sequence:

```bash
find schemas/contracts/v1/governance -maxdepth 2 -type f | sort
find schemas/contracts/v1/governance -name '*.schema.json' -print0 \
  | xargs -0 -r -I{} python -m json.tool {} >/dev/null
python tools/validate_all.py || true
pytest tests/schemas tests/contract tests/governance tests/policy tests/release || true
```

Replace `|| true` with fail-closed CI behavior once validator and test paths are confirmed.

---

## Rollback

Rollback for this README is ordinary Git rollback: revert the commit that changed `schemas/contracts/v1/governance/README.md`.

Rollback for future governance schema changes requires checking every downstream reference:

1. Revert or migrate schema files.
2. Restore canonical `$id` and `$ref` targets.
3. Restore paired contract links and path casing.
4. Restore fixtures, validators, schema registry records, and CI paths.
5. Restore policy, evidence, release, and receipt references.
6. Restore governance docs, registers, review-console payloads, governed API payloads, and release-gate consumers.
7. Preserve correction/rollback records if any public or release-affecting governance object was affected.

---

## Open questions

| Question | Status | Owner |
|---|---|---|
| Should `ReviewRecord.md` casing be mirrored by schema metadata, or should the contract be normalized to lowercase path? | **NEEDS VERIFICATION / migration-sensitive** | Governance steward + schema steward |
| Should `promotion_decision.schema.json` live under governance, release, or both with explicit profile/mirror rules? | **NEEDS VERIFICATION / ADR-sensitive** | Release steward + governance steward + schema steward |
| Should `redaction_receipt.schema.json` live under governance, evidence, policy, receipts, or domain lanes? | **NEEDS VERIFICATION / ADR-sensitive** | Governance steward + evidence steward + policy steward |
| Which governance schemas are field-complete and fixture-tested? | **NEEDS VERIFICATION** | Validation steward |
| Which governance records are required for publication gates? | **NEEDS VERIFICATION / release-gated** | Release steward + governance steward |

---

## Maintainer notes

- Treat current governance schemas as `PROPOSED` until contracts, fixtures, validators, CI, policy, and release references are verified.
- Do not let governance schemas become parallel release, policy, evidence, or receipt authority.
- Preserve inspectability, separation-of-duties, evidence linkage, release gates, correction path, and rollback support.
- Never treat schema validity as proof of review, approval, policy compliance, or publication readiness.
