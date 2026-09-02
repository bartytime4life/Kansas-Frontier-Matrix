# `schemas/contracts/v1/settlement/receipts/` — Settlement Receipt Schema Guardrail

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-settlement-receipts-readme
title: schemas/contracts/v1/settlement/receipts/ — Settlement Receipt Schema Guardrail
type: readme; schema-family-child-index; receipt-schema-boundary; settlement-compatibility-guardrail
authority_class: schema-family-guardrail
version: v0.1
status: draft; empty-schema-child-lane; singular-settlement-compatibility-path; settlements-infrastructure-overlap; no-current-settlement-receipt-schema-files-found; emitted-receipts-exist-elsewhere; do-not-promote-without-ADR; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Settlement sublane steward
  - OWNER_TBD — Settlements/Infrastructure domain steward
  - OWNER_TBD — Receipt steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Review steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Docs steward
created: NEEDS VERIFICATION — empty README existed before v0.1 expansion
updated: 2026-07-04
policy_label: public; schemas; contracts-v1; settlement; settlements-infrastructure; receipts; receipt-shape; compatibility-path; evidence-bound; policy-aware; review-aware; release-gated; rollback-aware; no-parallel-authority
tags: [kfm, schemas, contracts, v1, settlement, settlements-infrastructure, receipts, receipt-schema, process-memory, place-identity, validation-report, redaction-receipt, review-record, policy-decision, correction, rollback, no-parallel-authority]
related:
  - ../../README.md
  - ../README.md
  - ../../domains/settlement/README.md
  - ../../domains/settlements-infrastructure/README.md
  - ../../receipts/README.md
  - ../../receipts/redaction/README.md
  - ../../review/README.md
  - ../../release/README.md
  - ../../evidence/README.md
  - ../../policy/README.md
  - ../../governance/README.md
  - ../../../../data/receipts/settlement/README.md
  - ../../../../data/receipts/settlements-infrastructure/README.md
  - ../../../../data/receipts/settlements-infrastructure/condition_redaction/README.md
  - ../../../../data/proofs/settlement/README.md
  - ../../../../data/proofs/settlements-infrastructure/README.md
  - ../../../../contracts/domains/settlement/
  - ../../../../contracts/domains/settlements-infrastructure/
  - ../../../../docs/domains/settlements-infrastructure/
  - ../../../../fixtures/
  - ../../../../tests/
  - ../../../../release/
notes:
  - "Expanded from an empty file at schemas/contracts/v1/settlement/receipts/README.md."
  - "Current GitHub search did not surface schema files directly under schemas/contracts/v1/settlement/receipts/ beyond this README."
  - "Current repository evidence treats singular settlement as a compatibility or sublane path while broader domain authority is settlements-infrastructure."
  - "Data receipt lanes exist at data/receipts/settlement/ and data/receipts/settlements-infrastructure/, but those are emitted/process-memory data roots, not schema shape roots."
  - "The shared receipt schema family already states receipt schemas define shape only and do not store emitted receipt instances."
  - "This folder may define settlement receipt object shapes in the future, but it must not become emitted receipt storage, proof authority, release authority, or a new standalone settlement truth root."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![family](https://img.shields.io/badge/family-receipts-purple)
![domain](https://img.shields.io/badge/domain-settlement%20compatibility-2da44e)
![posture](https://img.shields.io/badge/posture-guardrail-orange)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **Purpose.** `schemas/contracts/v1/settlement/receipts/` is a README-only guardrail for possible machine-checkable settlement receipt object shapes.
>
> **One-line boundary.** Settlement receipt schemas define shape only. They do not store emitted receipts, prove place identity, certify settlement status, approve release, replace evidence, or create a new standalone settlement authority.

---

## Quick jumps

[Status](#status) · [Authority and placement](#authority-and-placement) · [Naming posture](#naming-posture) · [Repo fit](#repo-fit) · [Current inventory](#current-inventory) · [Related receipt lanes](#related-receipt-lanes) · [Candidate receipt shapes](#candidate-receipt-shapes) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Receipt-schema rules](#receipt-schema-rules) · [Promotion checklist](#promotion-checklist) · [Validation](#validation) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

| Question | Answer | Truth label |
|---|---|---|
| Does this README path exist? | Yes: `schemas/contracts/v1/settlement/receipts/README.md`. It was empty before this expansion. | **CONFIRMED** |
| Are schema files currently present directly under this path? | Not found in the current GitHub search beyond this README. | **NEEDS VERIFICATION / search-limited** |
| Is singular `settlement` confirmed as the canonical domain schema slug? | No. Existing schema-domain documentation treats singular `settlement` as a compatibility path and points to `settlements-infrastructure` as the broader working schema lane. | **CONFIRMED compatibility posture** |
| Are emitted receipt data lanes present elsewhere? | Yes. `data/receipts/settlement/` and `data/receipts/settlements-infrastructure/` are documented data receipt lanes. | **CONFIRMED path evidence** |
| Is this folder emitted receipt storage? | No. This folder is under `schemas/` and may only define machine-checkable shapes. | **CONFIRMED boundary** |
| Can this folder prove settlement identity, review, policy, release, correction, rollback, or public readiness? | No. Receipt schemas shape records only; proof, policy, review, release, correction, and rollback remain separate. | **CONFIRMED boundary** |

> [!IMPORTANT]
> A settlement receipt schema is not a settlement receipt instance. A schema-valid receipt is not proof of a place, status, process, review, policy decision, correction, rollback, or release.

---

## Authority and placement

This folder is under the schema responsibility root:

```text
schemas/contracts/v1/settlement/receipts/
```

It may define settlement receipt object shapes only after placement is resolved. Adjacent authority remains separate:

- `schemas/contracts/v1/receipts/` owns shared receipt object shapes where accepted.
- `schemas/contracts/v1/domains/settlement/` is a compatibility schema-domain lane in current documentation.
- `schemas/contracts/v1/domains/settlements-infrastructure/` is the broader working Settlements/Infrastructure schema lane.
- `contracts/` owns semantic meaning.
- `data/receipts/` owns emitted receipt instances and receipt-local process memory.
- `data/proofs/` owns proof artifacts where present.
- `data/catalog/` owns catalog/discovery records where present.
- `policy/` owns policy posture where implemented.
- `schemas/contracts/v1/evidence/` owns evidence-support shapes.
- `schemas/contracts/v1/review/` owns review-support shapes where accepted.
- `schemas/contracts/v1/release/` owns release/correction/rollback support shapes where accepted.
- `release/` owns actual release, correction, withdrawal, and rollback records where present.
- `fixtures/` and `tests/` prove valid/invalid examples and validator behavior.

This README does not amend ADR-0001, Directory Rules, receipt doctrine, settlement naming governance, policy docs, validators, review duties, or release gates.

---

## Naming posture

Current repository evidence shows a naming split:

```text
schemas/contracts/v1/settlement/receipts/          # this requested child schema lane
schemas/contracts/v1/domains/settlement/           # singular compatibility index
schemas/contracts/v1/domains/settlements-infrastructure/  # broader working domain schema lane

data/receipts/settlement/                          # settlement-sublane emitted receipt/process-memory lane
data/receipts/settlements-infrastructure/          # broader domain emitted receipt/process-memory lane
```

This README treats `schemas/contracts/v1/settlement/receipts/` as a compatibility or sublane schema guardrail until accepted directory governance decides whether receipt schemas should live here, under `schemas/contracts/v1/receipts/`, under `schemas/contracts/v1/domains/settlements-infrastructure/`, or under another approved profile lane.

---

## Repo fit

```text
schemas/
└── contracts/
    └── v1/
        ├── README.md
        ├── settlement/
        │   └── receipts/
        │       └── README.md                     # this file; README-only guardrail
        ├── domains/
        │   ├── settlement/
        │   │   └── README.md                     # singular compatibility index
        │   └── settlements-infrastructure/
        │       └── README.md                     # broader working domain lane
        ├── receipts/
        │   └── README.md                         # shared receipt schema family
        ├── evidence/
        ├── review/
        ├── release/
        ├── policy/
        └── governance/

data/
└── receipts/
    ├── settlement/                                # emitted/process-memory records; not schema shape
    └── settlements-infrastructure/                # emitted/process-memory records; not schema shape

contracts/
policy/
fixtures/
tests/
release/
```

---

## Current inventory

| Path | Kind | Current posture | Notes |
|---|---|---|---|
| `schemas/contracts/v1/settlement/receipts/README.md` | README | **CONFIRMED present** | Empty file expanded by this README. |
| `schemas/contracts/v1/settlement/receipts/*.schema.json` | JSON Schema files | **Not found in current search** | Do not create here without ADR, paired contracts, fixtures, validators, and naming-placement review. |
| `schemas/contracts/v1/domains/settlement/README.md` | Schema-domain README | **CONFIRMED compatibility index** | Treats singular `settlement` as not confirmed canonical and points to `settlements-infrastructure`. |
| `data/receipts/settlement/README.md` | Data receipt README | **CONFIRMED emitted/process-memory lane** | Data root; not schema authority. |
| `data/receipts/settlements-infrastructure/README.md` | Data receipt README | **CONFIRMED emitted/process-memory lane** | Domain parent receipt lane; not schema authority. |
| `schemas/contracts/v1/receipts/README.md` | Shared receipt schema README | **CONFIRMED shared receipt family** | Defines receipt-schema vs emitted-receipt boundary. |

---

## Related receipt lanes

| Lane | Role signal | Boundary to preserve |
|---|---|---|
| `schemas/contracts/v1/receipts/` | Shared receipt schema family. | Defines receipt shapes only; emitted receipts belong under data roots. |
| `schemas/contracts/v1/settlement/receipts/` | Requested settlement receipt schema child lane. | README-only guardrail until placement is resolved. |
| `data/receipts/settlement/` | Settlement-sublane process-memory lane. | Data root, not schema shape, proof, catalog, release, or public API/UI material. |
| `data/receipts/settlements-infrastructure/` | Broader Settlements/Infrastructure process-memory lane. | Data root, not schema authority or release authority. |
| `data/receipts/settlements-infrastructure/condition_redaction/` | Confirmed child process-memory lane. | Receipt-local process memory, not condition truth or release approval. |

---

## Candidate receipt shapes

Candidate schemas below are proposals only and should not be created without steward review.

| Candidate schema | Purpose | Default posture |
|---|---|---|
| `settlement_validation_receipt.schema.json` | Shape for process records documenting settlement validation steps and references. | **PROPOSED / not created** |
| `settlement_identity_normalization_receipt.schema.json` | Shape for records describing identity-normalization process outputs. | **PROPOSED / identity-sensitive** |
| `settlement_redaction_receipt.schema.json` | Shape for protective transform records tied to settlement surfaces. | **PROPOSED / receipt-overlap-sensitive** |
| `settlement_review_receipt.schema.json` | Shape for process records that hand off to review, not review authority itself. | **PROPOSED / review-overlap-sensitive** |
| `settlement_release_candidate_receipt.schema.json` | Shape for process records supporting release-candidate handoff, not release approval. | **PROPOSED / release-gated** |

> [!CAUTION]
> Candidate names are proposals only. Do not treat them as repo files, accepted contracts, emitted records, proof, review, policy, correction, rollback, release authority, or public-safe outputs until created, paired, fixture-tested, and reviewed.

---

## What belongs here

- This README.
- Future machine-checkable JSON Schema files for settlement receipt object shapes if accepted.
- Schema index notes for settlement receipt object families.
- Migration notes for singular `settlement` vs broader `settlements-infrastructure` naming.
- Migration notes for shared receipt family vs domain-specific receipt profiles.
- Links to paired contracts, fixtures, validators, schema registry records, evidence references, policy references, review references, release references, correction references, rollback references, and tests.

---

## What does not belong here

- Emitted receipt instances, lifecycle data, source records, registry records, catalog records, triplets, proof outputs, release records, correction records, rollback cards, review decisions, policy decisions, EvidenceBundles, public map/API artifacts, dashboards, screenshots, or generated summaries.
- Settlement payloads, municipal-status data, census-place payloads, historic-townsite payloads, ghost-town records, infrastructure records, condition records, dependency records, source payloads, or domain payloads.
- Policy rules, review procedures, release implementation code, validator code, packages, pipelines, runtime code, UI/API implementation, map tiles, or public display behavior.
- Claims that a settlement, status, identity, receipt, review, correction, rollback, release, or public projection is true, complete, reviewed, policy-safe, release-approved, or publication-ready merely because it validates against a settlement receipt schema.

---

## Receipt-schema rules

| Rule | Requirement |
|---|---|
| Shape is not process proof | Schema validation constrains shape; it does not prove the process occurred. |
| Receipt is process memory | Receipt objects document process context and references; they do not replace evidence, review, policy, proof, or release records. |
| Naming stays visible | Singular `settlement` remains compatibility/sublane posture until naming governance resolves it. |
| Evidence remains separate | Receipt objects may cite EvidenceRefs or EvidenceBundles, but do not replace them. |
| Review remains separate | Review handoff fields do not prove review or approval. |
| Policy remains separate | Receipt objects may reference policy state, but do not decide admissibility. |
| Release remains separate | Release-candidate receipts do not publish or approve artifacts. |
| Shared receipts stay aligned | Domain-specific receipt schemas must not drift from shared receipt-family semantics without profile/migration notes. |
| Fixtures prove behavior | Accepted schemas need valid and invalid fixtures plus validator coverage. |
| No parallel authority | Equivalent receipt shapes must not drift across settlement, settlements-infrastructure, receipts, review, release, policy, and evidence roots without migration notes. |

---

## Promotion checklist

A settlement receipt schema should not advance beyond `PROPOSED` unless:

- [ ] Accepted placement is resolved: this lane, shared receipts lane, domain lane, or explicit profile.
- [ ] Singular `settlement` vs `settlements-infrastructure` naming is documented.
- [ ] Paired semantic contract exists or an approved profile is documented.
- [ ] `$id` namespace convention is settled.
- [ ] Required fields are defined.
- [ ] Emitted-record storage path is documented separately from schema shape.
- [ ] Evidence reference requirements are defined where receipt use depends on claims.
- [ ] Policy and review references are defined where receipt use depends on admissibility or review state.
- [ ] Correction and rollback requirements are defined where public use depends on the receipt chain.
- [ ] Valid fixtures exist.
- [ ] Invalid fixtures exist.
- [ ] Validators exist and paths are correct.
- [ ] CI/schema-test coverage exists.
- [ ] Migration notes exist for duplicate or overlapping receipt surfaces.

---

## Validation

Recommended local validation sequence:

```bash
# Confirm this requested schema child lane remains README-only unless authorized.
find schemas/contracts/v1/settlement/receipts -maxdepth 3 -type f | sort

# Inspect shared receipt schemas and settlement naming surfaces.
find schemas/contracts/v1 -maxdepth 6 -type f \
  | grep -Ei 'settlement|settlements-infrastructure|receipt|review|release|policy|evidence' \
  | sort

# Inspect emitted receipt lanes separately from schema shapes.
find data/receipts -maxdepth 5 -type f 2>/dev/null \
  | grep -Ei 'settlement|settlements-infrastructure|README|receipt' \
  | sort

# Validate JSON syntax for settlement receipt schemas if any are added later.
find schemas/contracts/v1/settlement/receipts -name '*.json' -print0 \
  | xargs -0 -r -I{} python -m json.tool {} >/dev/null

# Run project validators when available.
python tools/validate_all.py || true
pytest tests/schemas tests/contract tests/policy tests/governance tests/release || true
```

Replace `|| true` with fail-closed CI behavior once validator and test paths are confirmed.

---

## Rollback

Rollback for this README is ordinary Git rollback: revert the commit that changed `schemas/contracts/v1/settlement/receipts/README.md`.

Rollback for future settlement receipt schema changes requires checking every downstream reference:

1. Revert or migrate schema files.
2. Restore canonical `$id` and `$ref` targets.
3. Restore paired contract links.
4. Restore fixtures, validators, schema registry records, and CI paths.
5. Restore data receipt, proof, catalog, evidence, review, policy, release, correction, and rollback references.
6. Restore API/UI/MapLibre/Evidence Drawer consumers where applicable.
7. Preserve correction and rollback records if any public or semi-public settlement surface was affected.

---

## Open questions

| Question | Status | Owner |
|---|---|---|
| Should settlement receipt schemas live under `schemas/contracts/v1/settlement/receipts/`, shared `receipts/`, or `domains/settlements-infrastructure/` profiles? | **NEEDS VERIFICATION / ADR-sensitive** | Schema steward + Receipt steward |
| Is singular `settlement` an accepted sublane slug, compatibility path, or path to retire? | **NEEDS VERIFICATION / naming-sensitive** | Settlement steward + Directory steward |
| Which semantic contract owns settlement receipt meaning? | **NEEDS VERIFICATION** | Contract steward + Receipt steward |
| Which fixtures prove receipt shapes do not replace evidence, proof, review, policy, or release authority? | **NEEDS VERIFICATION** | Validation steward |
| Which settlement receipt projections, if any, are safe for public API/MapLibre/Focus Mode use? | **NEEDS VERIFICATION / release-gated** | Release steward + Policy steward |

---

## Maintainer notes

- Keep this folder README-only until settlement receipt schema-home placement is resolved.
- Prefer shared receipt-family profiles over duplicated domain-specific receipt semantics.
- Keep emitted receipt instances under `data/receipts/`, not under `schemas/`.
- Preserve evidence, review, policy, release, correction, rollback, and naming-governance boundaries for every settlement receipt surface.
