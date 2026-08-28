# `schemas/contracts/v1/review/` — Review Schema Family Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-review-readme
title: schemas/contracts/v1/review/ — Review Schema Family Index
type: readme; schema-family-index; review-schema-boundary; governance-release-overlap-guardrail
authority_class: schema-family-index
version: v0.1
status: draft; review-family-present; schema-scaffolds-present; correction-release-overlap; governance-adjacent; PROPOSED; no-parallel-authority; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Review steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Governance steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Docs steward
created: NEEDS VERIFICATION — empty README existed before v0.1 expansion
updated: 2026-07-04
policy_label: public; schemas; contracts-v1; review; review-record; correction-notice; governance-adjacent; release-adjacent; evidence-bound; policy-aware; rollback-aware; no-parallel-authority
tags: [kfm, schemas, contracts, v1, review, ReviewRecord, CorrectionNotice, governance, release, correction, validation, evidence, policy, auditability, rollback, no-parallel-authority]
related:
  - ../README.md
  - ./review_record.schema.json
  - ./correction_notice.schema.json
  - ../governance/README.md
  - ../governance/review_record.schema.json
  - ../release/README.md
  - ../release/correction_notice.schema.json
  - ../policy/README.md
  - ../evidence/README.md
  - ../../../../contracts/governance/ReviewRecord.md
  - ../../../../contracts/governance/README.md
  - ../../../../docs/governance/REVIEW_DUTIES.md
  - ../../../../docs/governance/STEWARD_CHARTERS.md
  - ../../../../docs/architecture/contract-schema-policy-split.md
  - ../../../../docs/architecture/publication/CORRECTION.md
  - ../../../../policy/governance/
  - ../../../../policy/release/
  - ../../../../fixtures/
  - ../../../../tests/
  - ../../../../release/
notes:
  - "Expanded from an empty file at schemas/contracts/v1/review/README.md."
  - "Current GitHub search surfaced review_record.schema.json and correction_notice.schema.json under this folder."
  - "Both inspected review schemas are PROPOSED empty scaffolds with empty properties, additionalProperties true, and contract_doc null."
  - "ReviewRecord also appears as a governance family concern, and CorrectionNotice also appears under release schemas."
  - "This folder defines review object shapes only; it does not perform review, approve release, decide correction, enforce governance, or store review records."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![family](https://img.shields.io/badge/family-review-purple)
![shape](https://img.shields.io/badge/authority-machine--shape-informational)
![maturity](https://img.shields.io/badge/maturity-scaffold-orange)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **Purpose.** `schemas/contracts/v1/review/` is the machine-checkable schema family for review-support object shapes such as review records and correction notices.
>
> **One-line boundary.** Review schemas define object shape only. They do not perform review, approve promotion, publish artifacts, decide correction, replace EvidenceBundles, replace policy, or prove that review happened.

---

## Quick jumps

[Status](#status) · [Authority and placement](#authority-and-placement) · [Repo fit](#repo-fit) · [Current schema inventory](#current-schema-inventory) · [Known overlap and drift risks](#known-overlap-and-drift-risks) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Review-family rules](#review-family-rules) · [Promotion checklist](#promotion-checklist) · [Validation](#validation) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

| Question | Answer | Truth label |
|---|---|---|
| Does this README path exist? | Yes: `schemas/contracts/v1/review/README.md`. It was empty before this expansion. | **CONFIRMED** |
| Are review schema files present in this folder? | Yes. Search surfaced `review_record.schema.json` and `correction_notice.schema.json`. | **CONFIRMED path presence** |
| Are the review schemas mature/field-complete? | Not proven. Both inspected schemas are PROPOSED empty scaffolds with empty `properties`, `additionalProperties: true`, and `contract_doc: null`. | **CONFIRMED scaffold / NEEDS VERIFICATION** |
| Is this folder governance authority? | No. This folder defines review schema shape only; governance standards and review duty posture remain separate. | **CONFIRMED boundary** |
| Is this folder release or correction authority? | No. Correction and release authority remain with governed release/correction roots and release review state. | **CONFIRMED boundary** |
| Can schema validation prove review happened? | No. Schema validation can shape a record, but proof requires actual records, reviewers, policy/release context, evidence, and audit trail. | **CONFIRMED boundary** |

> [!IMPORTANT]
> A schema-valid `ReviewRecord` or `CorrectionNotice` is not approval, correction, release, or proof. It is a shaped object candidate unless backed by governed records and review context.

---

## Authority and placement

This folder is under the schema responsibility root:

```text
schemas/contracts/v1/review/
```

It may define machine-checkable review-support shapes, but adjacent authority is separate:

- `contracts/` owns semantic meaning for review object families.
- `docs/governance/` owns human-facing review duties, stewardship, escalation, and separation-of-duties guidance where present.
- `schemas/contracts/v1/governance/` owns governance/review/stewardship shapes where accepted.
- `schemas/contracts/v1/release/` owns release and correction object shapes where accepted.
- `schemas/contracts/v1/policy/` owns policy-support shapes.
- `schemas/contracts/v1/evidence/` owns evidence-support shapes.
- `policy/` owns admissibility posture where implemented.
- `release/` owns actual release, correction, withdrawal, and rollback records where present.
- `fixtures/` and `tests/` prove valid/invalid examples and validator behavior.

This README does not amend ADR-0001, Directory Rules, governance docs, review duties, policy docs, validators, or release gates.

---

## Repo fit

```text
schemas/
└── contracts/
    └── v1/
        ├── README.md
        ├── review/
        │   ├── README.md                         # this file
        │   ├── review_record.schema.json         # PROPOSED empty scaffold
        │   └── correction_notice.schema.json     # PROPOSED empty scaffold; release overlap
        ├── governance/
        │   └── review_record.schema.json         # related governance surface
        ├── release/
        │   └── correction_notice.schema.json     # related release surface
        ├── policy/
        └── evidence/

contracts/
└── governance/                                   # confirmed review-related semantic surfaces exist

docs/
└── governance/                                   # review duties/stewardship docs; not schema shape

policy/
release/
fixtures/
tests/
```

---

## Current schema inventory

| File | Current posture | Shape maturity | Notes |
|---|---|---|---|
| `review_record.schema.json` | **PROPOSED** | Empty scaffold | Empty `properties`, `additionalProperties: true`, `contract_doc: null`; source docs point to Agriculture and Archaeology API contracts. |
| `correction_notice.schema.json` | **PROPOSED** | Empty scaffold / release overlap | Empty `properties`, `additionalProperties: true`, `contract_doc: null`; source doc points to Archaeology API contracts. |

---

## Known overlap and drift risks

| Risk | Evidence signal | Required posture |
|---|---|---|
| Review vs governance overlap | Governance README treats ReviewRecord as a governance-family concern, while this folder also has `review_record.schema.json`. | **Needs canonical/profile decision** |
| Review vs release overlap | Release README inventories `correction_notice.schema.json`; this folder also has a CorrectionNotice scaffold. | **Needs correction-profile decision** |
| Empty scaffold maturity | Both review schemas currently have empty `properties` and `additionalProperties: true`. | **Do not imply field-complete review validation** |
| Contract doc gap | Both inspected review schemas have `contract_doc: null`. | **Needs paired contract or approved profile** |
| Actual review record separation | Schema files live under `schemas/`; review records and review decisions must live under governed review/governance/release/data roots. | **Keep roots separate** |

---

## What belongs here

- This README.
- Machine-checkable JSON Schema files for review-support object shapes if accepted.
- Schema index notes for review object families.
- Migration notes for review/governance/release correction overlap.
- Links to paired contracts, fixtures, validators, schema registry records, policy references, evidence references, release references, correction references, rollback references, and tests.

---

## What does not belong here

- Actual review records, emitted correction notices, review decisions, governance decisions, policy decisions, release decisions, correction records, rollback records, EvidenceBundles, proof outputs, receipt instances, catalog records, triplets, public map/API artifacts, dashboards, screenshots, or generated summaries.
- Review procedures, governance policy, release implementation code, validator code, packages, pipelines, runtime code, UI/API implementation, or map tiles.
- Domain payloads or source payloads.
- Claims that an artifact is reviewed, corrected, approved, release-ready, public-safe, or publication-approved merely because it validates against a review schema.

---

## Review-family rules

| Rule | Requirement |
|---|---|
| Shape is not review | Schema validation constrains object shape; it does not prove review occurred. |
| Review is not release | Review records may support release, but they do not publish artifacts. |
| Correction is release-adjacent | Correction notices need release/correction/rollback alignment before public use. |
| Review is not evidence | Review records may cite evidence, but do not replace EvidenceBundles. |
| Review is not policy | Review records may reference policy posture, but do not replace policy evaluation. |
| Contracts explain meaning | Accepted review schemas need paired semantic contracts or approved profiles. |
| Fixtures prove behavior | Accepted schemas need valid and invalid fixtures plus validator coverage. |
| No parallel authority | Equivalent review and correction shapes must not drift across review, governance, release, policy, and evidence roots without migration notes. |

---

## Promotion checklist

A review schema should not advance beyond `PROPOSED` unless:

- [ ] Paired semantic contract exists or an approved governance/release profile is documented.
- [ ] `$id` namespace convention is settled.
- [ ] Required fields are defined.
- [ ] Object role is separated from governance, policy, evidence, correction, release, and emitted review records.
- [ ] Reviewer/steward identity requirements are defined where review depends on responsible parties.
- [ ] Evidence reference requirements are defined where review depends on claims.
- [ ] Policy and release references are defined where review depends on admissibility or publication state.
- [ ] Correction and rollback requirements are defined where correction/public use depends on review.
- [ ] Valid fixtures exist.
- [ ] Invalid fixtures exist.
- [ ] Validators exist and paths are correct.
- [ ] CI/schema-test coverage exists.
- [ ] Migration notes exist for duplicate or overlapping schema surfaces.

---

## Validation

Recommended local validation sequence:

```bash
# Inspect the review schema family.
find schemas/contracts/v1/review -maxdepth 3 -type f | sort

# Detect review/governance/release correction overlap.
find schemas/contracts/v1 -maxdepth 5 -type f \
  | grep -Ei 'review_record|correction_notice|review|governance|release|policy|evidence' \
  | sort

# Validate JSON syntax for review schemas.
find schemas/contracts/v1/review -name '*.json' -print0 \
  | xargs -0 -r -I{} python -m json.tool {} >/dev/null

# Inspect paired contracts and fixtures when present.
find contracts fixtures -maxdepth 5 -type f 2>/dev/null \
  | grep -Ei 'review_record|correction_notice|review|correction' \
  | sort

# Run project validators when available.
python tools/validate_all.py || true
pytest tests/schemas tests/contract tests/policy tests/governance tests/release || true
```

Replace `|| true` with fail-closed CI behavior once validator and test paths are confirmed.

---

## Rollback

Rollback for this README is ordinary Git rollback: revert the commit that changed `schemas/contracts/v1/review/README.md`.

Rollback for future review schema changes requires checking every downstream reference:

1. Revert or migrate schema files.
2. Restore canonical `$id` and `$ref` targets.
3. Restore paired contract links.
4. Restore fixtures, validators, schema registry records, and CI paths.
5. Restore governance, policy, evidence, correction, release, and rollback references.
6. Restore API/UI/MapLibre/Evidence Drawer consumers where applicable.
7. Preserve correction and rollback records if any public or semi-public review surface was affected.

---

## Open questions

| Question | Status | Owner |
|---|---|---|
| Should ReviewRecord schema authority live under `review/`, `governance/`, or a shared profile? | **NEEDS VERIFICATION / ADR-sensitive** | Review steward + Governance steward + Schema steward |
| Should CorrectionNotice schema authority live under `review/`, `release/`, or a shared correction profile? | **NEEDS VERIFICATION / migration-sensitive** | Review steward + Release steward |
| Which semantic contract owns review object meaning? | **NEEDS VERIFICATION** | Contract steward |
| Which fixtures prove review/correction records do not replace evidence, policy, or release authority? | **NEEDS VERIFICATION** | Validation steward |
| Which review projections are safe for public API/MapLibre/Focus Mode use? | **NEEDS VERIFICATION / release-gated** | Release steward + Policy steward |

---

## Maintainer notes

- Keep this folder focused on review-support schema shape, not review execution.
- Treat current schemas as PROPOSED scaffolds until contracts, fixtures, validators, CI, and overlap decisions are verified.
- Prevent drift between review, governance, policy, evidence, correction, release, and rollback surfaces.
- Preserve evidence, policy, governance, release, correction, and rollback boundaries for every review surface.
