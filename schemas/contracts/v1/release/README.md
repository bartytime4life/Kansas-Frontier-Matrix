# `schemas/contracts/v1/release/` — Release Schema Family Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-release-readme
title: schemas/contracts/v1/release/ — Release Schema Family Index
type: readme; schema-family-index; release-schema-boundary; publication-guardrail
authority_class: schema-family-index
version: v0.2
status: draft; release-family-present; mixed-maturity-schemas-present; promotion-policy-governance-overlap; receipt-overlap-present; namespace-drift-visible; PROPOSED; no-parallel-authority; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Release steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Governance steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Receipt steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Docs steward
created: NEEDS VERIFICATION — short stub existed before v0.2 expansion
updated: 2026-07-04
policy_label: public; schemas; contracts-v1; release; release-manifest; release-state; promotion-decision; rollback-card; correction-notice; withdrawal-notice; publication-transform-receipt; redaction-receipt; evidence-bound; policy-aware; governance-aware; rollback-aware; no-parallel-authority
tags: [kfm, schemas, contracts, v1, release, ReleaseManifest, ReleaseState, PromotionDecision, RollbackCard, CorrectionNotice, WithdrawalNotice, PublicationTransformReceipt, RedactionReceipt, publication, correction, rollback, withdrawal, promotion, no-parallel-authority]
related:
  - ../README.md
  - ./release_manifest.schema.json
  - ./release_state.schema.json
  - ./promotion_decision.schema.json
  - ./rollback_card.schema.json
  - ./correction_notice.schema.json
  - ./withdrawal_notice.schema.json
  - ./publication_transform_receipt.schema.json
  - ./redaction_receipt.schema.json
  - ../policy/README.md
  - ../governance/README.md
  - ../receipts/README.md
  - ../evidence/README.md
  - ../map/README.md
  - ../../../../contracts/release/
  - ../../../../policy/release/
  - ../../../../fixtures/release/
  - ../../../../tests/
  - ../../../../release/
notes:
  - "Expanded from a short stub at schemas/contracts/v1/release/README.md."
  - "Current GitHub search surfaced release_manifest.schema.json, release_state.schema.json, promotion_decision.schema.json, rollback_card.schema.json, correction_notice.schema.json, withdrawal_notice.schema.json, publication_transform_receipt.schema.json, and redaction_receipt.schema.json under this folder."
  - "promotion_decision.schema.json is the most concrete inspected schema, with required fields and additionalProperties false."
  - "release_manifest.schema.json, rollback_card.schema.json, and withdrawal_notice.schema.json are permissive PROPOSED stubs requiring only id."
  - "release_state.schema.json, correction_notice.schema.json, redaction_receipt.schema.json, and publication_transform_receipt.schema.json are PROPOSED empty scaffolds with additionalProperties true."
  - "This folder defines release object shapes only; it does not perform release, publish artifacts, approve promotion, or store release records."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![family](https://img.shields.io/badge/family-release-purple)
![shape](https://img.shields.io/badge/authority-machine--shape-informational)
![maturity](https://img.shields.io/badge/maturity-mixed-orange)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **Purpose.** `schemas/contracts/v1/release/` is the machine-checkable schema family for release-support objects such as release manifests, release states, promotion decisions, rollback cards, correction notices, withdrawal notices, and publication transform receipts.
>
> **One-line boundary.** Release schemas define object shape only. They do not publish artifacts, approve promotion, bypass policy, replace evidence, emit receipts, perform correction, or create rollback authority.

---

## Quick jumps

[Status](#status) · [Authority and placement](#authority-and-placement) · [Repo fit](#repo-fit) · [Current schema inventory](#current-schema-inventory) · [Known overlap and drift risks](#known-overlap-and-drift-risks) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Release-family rules](#release-family-rules) · [Promotion checklist](#promotion-checklist) · [Validation](#validation) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

| Question | Answer | Truth label |
|---|---|---|
| Does this README path exist? | Yes: `schemas/contracts/v1/release/README.md`. It was a short stub before this expansion. | **CONFIRMED** |
| Are release schema files present in this folder? | Yes. Search surfaced eight release-family schema files under this folder. | **CONFIRMED path presence** |
| Are all release schemas mature/field-complete? | No. The inspected files are mixed: one detailed promotion decision schema, several permissive stubs, and several empty scaffolds. | **CONFIRMED mixed maturity** |
| Is this folder release authority? | No. This folder defines schema shapes only. Actual release records, release decisions, publication state, correction records, and rollback records belong in governed release/data roots. | **CONFIRMED boundary** |
| Can schema validation alone approve publication? | No. Publication requires evidence, policy, review, release state, correction path, and rollback support appropriate to the artifact. | **CONFIRMED boundary** |

> [!IMPORTANT]
> A schema-valid release object is not release approval. It is only a shaped record candidate unless backed by the governed inputs, review state, policy state, evidence support, release records, and rollback/correction posture required by KFM.

---

## Authority and placement

This folder is under the schema responsibility root:

```text
schemas/contracts/v1/release/
```

It may define release-support object shapes, but adjacent authority is separate:

- `contracts/release/` owns release object meaning.
- `policy/release/` and related policy roots own release policy posture where implemented.
- `release/` owns actual release, correction, withdrawal, and rollback records where present.
- `schemas/contracts/v1/policy/` owns policy-support shapes.
- `schemas/contracts/v1/governance/` owns governance/review/stewardship shapes.
- `schemas/contracts/v1/evidence/` owns evidence-support shapes.
- `schemas/contracts/v1/receipts/` owns receipt object shapes.
- `fixtures/` and `tests/` prove valid/invalid examples and validator behavior.

This README does not amend ADR-0001, Directory Rules, release doctrine, policy docs, validators, or release gates.

---

## Repo fit

```text
schemas/
└── contracts/
    └── v1/
        ├── README.md
        ├── release/
        │   ├── README.md                         # this file
        │   ├── release_manifest.schema.json      # PROPOSED permissive stub
        │   ├── release_state.schema.json         # PROPOSED empty scaffold
        │   ├── promotion_decision.schema.json    # PROPOSED concrete schema
        │   ├── rollback_card.schema.json         # PROPOSED permissive stub
        │   ├── correction_notice.schema.json     # PROPOSED empty scaffold
        │   ├── withdrawal_notice.schema.json     # PROPOSED permissive stub
        │   ├── publication_transform_receipt.schema.json
        │   └── redaction_receipt.schema.json
        ├── policy/
        ├── governance/
        ├── evidence/
        └── receipts/

contracts/
└── release/                                      # semantic meaning; not schema shape

policy/
release/                                          # actual release records/state where present; not schema shape
fixtures/
tests/
```

---

## Current schema inventory

| File | Current posture | Shape maturity | Notes |
|---|---|---|---|
| `promotion_decision.schema.json` | **PROPOSED** | Concrete schema | Requires `id`, `version`, `domain`, `run_id`, `decision`, evidence refs, rollback card URI, policy bundle, decision time, and review object; `additionalProperties: false`. |
| `release_manifest.schema.json` | **PROPOSED** | Permissive stub | Requires only `id`; includes `spec_hash`, `id`, and `version`; points to `contracts/release/release_manifest.md`, fixtures, validator, and `policy/release/`. |
| `rollback_card.schema.json` | **PROPOSED** | Permissive stub | Requires only `id`; points to `contracts/release/rollback_card.md`, fixtures, validator, and `policy/release/`. |
| `withdrawal_notice.schema.json` | **PROPOSED** | Permissive stub | Requires only `id`; points to `contracts/release/withdrawal_notice.md`, fixtures, validator, and `policy/release/`. |
| `release_state.schema.json` | **PROPOSED** | Empty scaffold | Empty `properties`, `additionalProperties: true`, `contract_doc: null`; source doc points to Roads/Rail/Trade release index. |
| `correction_notice.schema.json` | **PROPOSED** | Empty scaffold | Empty `properties`, `additionalProperties: true`, `contract_doc: null`; source doc points to Archaeology release index. |
| `redaction_receipt.schema.json` | **PROPOSED** | Empty scaffold / receipt overlap | Empty `properties`, `additionalProperties: true`, `contract_doc: null`; overlaps receipt/redaction schema families. |
| `publication_transform_receipt.schema.json` | **PROPOSED** | Empty scaffold / receipt overlap | Empty `properties`, `additionalProperties: true`, `contract_doc: null`; source doc points to Archaeology canonical paths. |

---

## Known overlap and drift risks

| Risk | Evidence signal | Required posture |
|---|---|---|
| Release vs policy overlap | `promotion_decision.schema.json` references `policy/promotion/`, while policy schema family also has policy and promotion surfaces. | **Keep policy and release authority separate** |
| Release vs governance overlap | Promotion/review fields are governance-adjacent. | **No bypass of review records** |
| Release vs receipts overlap | `redaction_receipt.schema.json` and `publication_transform_receipt.schema.json` live under release but are receipt-like objects. | **Needs receipt/profile placement decision** |
| Namespace drift | Some files use `https://schemas.kfm.local/contracts/...`; others use `kfm://schemas/contracts/...`; one uses `https://schemas.kfm.local/schemas/...`. | **NEEDS VERIFICATION** |
| Mixed maturity | Some files are detailed, others permissive or empty scaffolds. | **Do not imply completed release contract family** |
| Actual release record separation | Schema files live under `schemas/`; release records and publication state must live under governed release/data roots. | **Keep roots separate** |

---

## What belongs here

- This README.
- Machine-checkable JSON Schema files for release-support object shapes.
- Schema index notes for release object families.
- Migration notes for release/policy/governance/receipt overlap.
- Links to paired contracts, fixtures, validators, schema registry records, policy references, evidence references, receipt references, release records, correction references, rollback references, and tests.

---

## What does not belong here

- Actual release records, release manifests as emitted instances, publication records, correction records, withdrawal records, rollback records, promotion decisions as emitted records, policy decisions, review records, receipt instances, proof outputs, EvidenceBundles, catalog records, triplets, public map/API artifacts, dashboards, screenshots, or generated summaries.
- Policy rules, governance procedures, release implementation code, validator code, packages, pipelines, runtime code, UI/API implementation, or map tiles.
- Domain payloads or source payloads.
- Claims that an artifact is released, corrected, withdrawn, rollback-ready, public-safe, or publication-approved merely because it validates against a release schema.

---

## Release-family rules

| Rule | Requirement |
|---|---|
| Shape is not release | Schema validation constrains object shape; it does not publish. |
| Promotion is governed | Promotion must remain a governed decision with evidence, policy, review, rollback, and timestamp support. |
| Release is not policy | Release records may reference policy posture but do not replace policy evaluation. |
| Release is not evidence | Release records may cite EvidenceBundles but do not replace them. |
| Correction remains visible | Correction, withdrawal, and rollback paths must be auditable where public artifacts depend on them. |
| Receipts remain separate | Receipt-shaped release support must not drift from receipt-family semantics without a profile or migration rule. |
| Contracts explain meaning | Accepted release schemas need paired semantic contracts or approved contract profiles. |
| Fixtures prove behavior | Accepted schemas need valid and invalid fixtures plus validator coverage. |
| No parallel authority | Equivalent release, promotion, correction, rollback, receipt, policy, and governance shapes must not drift across roots without migration notes. |

---

## Promotion checklist

A release schema should not advance beyond `PROPOSED` unless:

- [ ] Paired semantic contract exists.
- [ ] `$id` namespace convention is settled.
- [ ] Required fields are defined.
- [ ] Object role is separated from policy, governance, evidence, receipt, and emitted release records.
- [ ] Evidence reference requirements are defined where release depends on claims.
- [ ] Policy reference requirements are defined where release depends on policy.
- [ ] Review/stewardship fields are defined where release depends on review.
- [ ] Correction and rollback requirements are defined.
- [ ] Valid fixtures exist.
- [ ] Invalid fixtures exist.
- [ ] Validators exist and paths are correct.
- [ ] CI/schema-test coverage exists.
- [ ] Migration notes exist for duplicate or overlapping schema surfaces.
- [ ] Public API, MapLibre, Focus Mode, or catalog consumers are release-gated if they use the object.

---

## Validation

Recommended local validation sequence:

```bash
# Inspect the release schema family.
find schemas/contracts/v1/release -maxdepth 3 -type f | sort

# Detect release/policy/governance/receipt overlap.
find schemas/contracts/v1 -maxdepth 5 -type f \
  | grep -Ei 'release|promotion|rollback|correction|withdrawal|publication_transform|redaction_receipt|policy|governance|receipt' \
  | sort

# Validate JSON syntax for release schemas.
find schemas/contracts/v1/release -name '*.json' -print0 \
  | xargs -0 -r -I{} python -m json.tool {} >/dev/null

# Inspect paired contracts and fixtures when present.
find contracts/release fixtures/release -maxdepth 4 -type f 2>/dev/null | sort

# Run project validators when available.
python tools/validate_all.py || true
pytest tests/schemas tests/contract tests/policy tests/governance tests/release || true
```

Replace `|| true` with fail-closed CI behavior once validator and test paths are confirmed.

---

## Rollback

Rollback for this README is ordinary Git rollback: revert the commit that changed `schemas/contracts/v1/release/README.md`.

Rollback for future release schema changes requires checking every downstream reference:

1. Revert or migrate schema files.
2. Restore canonical `$id` and `$ref` targets.
3. Restore paired contract links.
4. Restore fixtures, validators, schema registry records, and CI paths.
5. Restore policy, governance, evidence, receipt, release, correction, withdrawal, and rollback references.
6. Restore API/UI/MapLibre/Evidence Drawer consumers where applicable.
7. Preserve correction and rollback records if any public or semi-public release surface was affected.

---

## Open questions

| Question | Status | Owner |
|---|---|---|
| Which release schemas are intended to be field-complete in v1 and which are temporary scaffolds? | **NEEDS VERIFICATION** | Release steward + Schema steward |
| Should receipt-like release schemas remain under `release/`, move under `receipts/`, or become explicit profiles? | **NEEDS VERIFICATION / migration-sensitive** | Release steward + Receipt steward |
| Should all release `$id`s use `kfm://schemas/contracts/...` or `https://schemas.kfm.local/contracts/...`? | **NEEDS VERIFICATION / namespace-sensitive** | Schema steward |
| Which promotion decision shape is canonical across release, policy, and governance surfaces? | **NEEDS VERIFICATION / ADR-sensitive** | Release steward + Policy steward + Governance steward |
| Which release projections are safe for public API/MapLibre/Focus Mode use? | **NEEDS VERIFICATION / release-gated** | Release steward + Policy steward |

---

## Maintainer notes

- Keep this folder focused on release-support schema shape, not release execution.
- Treat current schemas as PROPOSED until contracts, fixtures, validators, CI, and overlap decisions are verified.
- Prevent drift between release, policy, governance, evidence, receipt, correction, withdrawal, rollback, and publication surfaces.
- Preserve evidence, policy, governance, release, correction, and rollback boundaries for every public or semi-public release surface.
