# `schemas/contracts/v1/policy/` — Policy Schema Family Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-policy-readme
title: schemas/contracts/v1/policy/ — Policy Schema Family Index
type: readme; schema-family-index; policy-schema-boundary; policy-decision-guardrail
authority_class: schema-family-index
version: v0.2
status: draft; policy-family-present; mixed-maturity-schemas-present; promotion-governance-overlap; redaction-receipt-naming-drift; PROPOSED; no-parallel-authority; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Governance steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Sensitivity steward
  - OWNER_TBD — Redaction steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Docs steward
created: NEEDS VERIFICATION — short stub existed before v0.2 expansion
updated: 2026-07-04
policy_label: public; schemas; contracts-v1; policy; policy-decision; sensitivity-label; policy-input-bundle; promotion-decision; redaction-receipt; governance-adjacent; release-adjacent; sensitivity-aware; no-parallel-authority
tags: [kfm, schemas, contracts, v1, policy, PolicyDecision, SensitivityLabel, PolicyInputBundle, PromotionDecision, RedactionReceipt, access, render, capability, consent, sensitivity, governance, release, redaction, validation, rollback]
related:
  - ../README.md
  - ./policy_decision.schema.json
  - ./sensitivity_label.schema.json
  - ./policy_input_bundle.schema.json
  - ./promotion_decision.schema.json
  - ./redaction-receipt.json
  - ../governance/README.md
  - ../governance/promotion_decision.schema.json
  - ../governance/redaction_receipt.schema.json
  - ../release/
  - ../evidence/
  - ../exposure/README.md
  - ../../../../contracts/policy/policy_decision.md
  - ../../../../contracts/policy/sensitivity_label.md
  - ../../../../contracts/policy/policy_input_bundle.md
  - ../../../../policy/decision/README.md
  - ../../../../fixtures/contracts/v1/policy/README.md
  - ../../../../tests/
  - ../../../../release/
notes:
  - "Expanded from a short stub at schemas/contracts/v1/policy/README.md."
  - "Current GitHub search surfaced policy_decision.schema.json, sensitivity_label.schema.json, policy_input_bundle.schema.json, promotion_decision.schema.json, and redaction-receipt.json under this folder."
  - "policy_decision.schema.json and sensitivity_label.schema.json have concrete required fields and additionalProperties false, but remain x-kfm.status PROPOSED."
  - "policy_input_bundle.schema.json is a permissive PROPOSED stub requiring only id."
  - "promotion_decision.schema.json is a permissive PROPOSED scaffold with empty properties and additionalProperties true; PromotionDecision also appears under governance schemas."
  - "redaction-receipt.json is a placeholder JSON file with a hyphenated non-.schema name; redaction receipt meaning also overlaps governance and domain receipt lanes."
  - "This folder defines policy object shapes only; it must not become the policy authority root, release authority root, evidence authority root, or emitted decision store."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![family](https://img.shields.io/badge/family-policy-indigo)
![shape](https://img.shields.io/badge/authority-machine--shape-informational)
![maturity](https://img.shields.io/badge/maturity-PROPOSED-orange)
![overlap](https://img.shields.io/badge/overlap-governance%2Frelease-yellow)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **Purpose.** `schemas/contracts/v1/policy/` is the machine-checkable schema family for policy-support objects such as policy decisions, sensitivity labels, and policy input bundles.
>
> **One-line boundary.** This folder defines policy object **shape**. It does not implement policy, grant access, authorize release, downgrade sensitivity, redact data, or prove that a policy check actually happened.

---

## Quick jumps

[Status](#status) · [Authority and placement](#authority-and-placement) · [Repo fit](#repo-fit) · [Current schema inventory](#current-schema-inventory) · [Known overlap and drift risks](#known-overlap-and-drift-risks) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Schema-family rules](#schema-family-rules) · [Policy trust guardrails](#policy-trust-guardrails) · [Promotion checklist](#promotion-checklist) · [Validation](#validation) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

| Question | Answer | Truth label |
|---|---|---|
| Does this README path exist? | Yes: `schemas/contracts/v1/policy/README.md`. It was a short stub before this expansion. | **CONFIRMED** |
| Are policy schema files present in this folder? | Yes. Search surfaced policy decision, sensitivity label, policy input bundle, promotion decision, and redaction receipt placeholder files. | **CONFIRMED path presence** |
| Are all policy schemas mature/field-complete? | No. Some schemas have concrete required fields; others are permissive scaffolds or placeholders. | **CONFIRMED mixed maturity** |
| Is this folder policy authority? | No. This folder defines schema shapes only. Policy rules, policy operation, and policy decisions remain separate from schema definitions. | **CONFIRMED boundary** |
| Is this folder release authority? | No. Promotion and release decisions are release/governance-adjacent, but release authority belongs to release-governed lanes. | **CONFIRMED boundary** |
| Can these schemas alone prove policy was evaluated? | No. Schema validation shapes records; proof requires actual records, inputs, policy engine or review evidence, timestamps, and audit trail. | **CONFIRMED boundary** |

> [!IMPORTANT]
> A schema-valid `PolicyDecision` is not proof that the right policy ran, that the inputs were complete, that sensitivity was correctly assigned, or that release is allowed. Evidence, policy implementation, review state, and release state still matter.

---

## Authority and placement

This folder is under the schema responsibility root:

```text
schemas/contracts/v1/policy/
```

It may define machine-checkable policy-support shapes, but adjacent authority is split:

- `contracts/policy/` owns semantic meaning for policy object families.
- `policy/` owns policy posture, rules, decisions, or policy-operation documentation where implemented.
- `schemas/contracts/v1/governance/` owns governance/review/stewardship shapes and has overlapping promotion/redaction receipt surfaces.
- `schemas/contracts/v1/release/` owns release object shapes where present.
- `schemas/contracts/v1/evidence/` owns evidence-support shapes.
- `schemas/contracts/v1/exposure/` owns exposure response/envelope shape where present.
- `fixtures/` and `tests/` prove valid/invalid policy-shape behavior.
- `release/` owns promotion, release, correction, withdrawal, and rollback records.

This README does not amend ADR-0001, Directory Rules, policy docs, governance docs, release gates, validators, or release doctrine.

---

## Repo fit

```text
schemas/
└── contracts/
    └── v1/
        ├── README.md
        ├── policy/
        │   ├── README.md                         # this file
        │   ├── policy_decision.schema.json       # PROPOSED concrete schema
        │   ├── sensitivity_label.schema.json     # PROPOSED concrete schema
        │   ├── policy_input_bundle.schema.json   # PROPOSED permissive stub
        │   ├── promotion_decision.schema.json    # PROPOSED empty scaffold; governance/release-adjacent
        │   └── redaction-receipt.json            # PROPOSED placeholder; naming/schema drift
        ├── governance/                           # review/stewardship/governance shapes; separate authority
        ├── release/                              # release object shapes; separate authority
        ├── evidence/                             # evidence object shapes; separate authority
        └── exposure/                             # exposure object shapes; separate authority

contracts/
└── policy/                                       # semantic meaning; not machine shape

policy/                                           # policy rules/operation; not schema shape
fixtures/
tests/
release/
```

---

## Current schema inventory

| File | Current posture | Shape maturity | Notes |
|---|---|---|---|
| `policy_decision.schema.json` | **PROPOSED** | Concrete required fields | Requires `decision_id`, `outcome`, `policy_family`, `reasons`, `obligations`, and `evaluated_at`; `additionalProperties: false`. |
| `sensitivity_label.schema.json` | **PROPOSED** | Concrete required fields | Requires `level`, `reason`, and `applied_at`; allowed levels are `public`, `generalized`, `restricted`, and `quarantine`; `additionalProperties: false`. |
| `policy_input_bundle.schema.json` | **PROPOSED** | Permissive stub | Requires only `id`; includes `spec_hash`, `id`, and `version`; `additionalProperties: true`. |
| `promotion_decision.schema.json` | **PROPOSED** | Empty scaffold | Empty `properties`, `additionalProperties: true`, and `contract_doc: null`; overlaps governance/release meaning. |
| `redaction-receipt.json` | **PROPOSED placeholder** | Non-schema placeholder | Placeholder JSON with `status`, `path`, `source_docs`, and `notes`; filename is hyphenated and lacks `.schema.json`. |

---

## Known overlap and drift risks

| Risk | Evidence signal | Required posture |
|---|---|---|
| Policy vs governance overlap | `promotion_decision.schema.json` appears in policy, while governance also documents promotion/redaction receipt schema surfaces. | **NEEDS ADR / migration note before promotion** |
| Policy vs release overlap | Promotion decisions are release-adjacent and should not become release authority merely by schema placement. | **Release-gated** |
| Redaction receipt naming drift | `redaction-receipt.json` is a placeholder, not a `.schema.json`; governance has `redaction_receipt.schema.json`. | **NEEDS normalization** |
| Namespace drift | Some policy schemas use `https://schemas.kfm.local/contracts/v1/policy/...`, while newer schema families often use `kfm://schemas/contracts/v1/...`. | **NEEDS VERIFICATION** |
| Fixture path drift | `policy_decision` and `sensitivity_label` point to `fixtures/contracts/v1/policy/...`, while `policy_input_bundle` points to `fixtures/policy/...`. | **NEEDS VERIFICATION** |
| Policy root ambiguity | Schema `x-kfm.policy` values point to `policy/policy/`; actual policy operation paths need verification. | **NEEDS VERIFICATION** |

---

## What belongs here

- This README.
- Machine-checkable JSON Schema files for policy-support objects.
- Schema index notes for policy object families.
- Migration notes for policy/governance/release/sensitivity/redaction overlap.
- Links to paired contracts, fixtures, validators, schema registry records, policy references, release references, correction references, rollback references, and tests.

---

## What does not belong here

- Policy rule text or policy implementation code.
- Access-control configuration, capability gates, or runtime enforcement logic.
- Actual policy decision records, emitted sensitivity decisions, consent decisions, redaction decisions, promotion decisions, release records, correction records, rollback cards, receipts, proofs, catalog records, or public artifacts.
- Domain data, lifecycle data, source registry records, generated answers, dashboards, screenshots, or map/UI/API outputs.
- Claims that a policy decision is correct, complete, enforceable, release-approved, or public-safe merely because it validates against a schema.

---

## Schema-family rules

| Rule | Requirement |
|---|---|
| Shape is not enforcement | A policy schema constrains record shape; it does not run or enforce policy. |
| Decision is not truth by itself | A policy decision record must be backed by inputs, reasons, obligations, timestamp, policy version, and audit trail where required. |
| Sensitivity fails closed | Missing, ambiguous, or unsupported sensitivity posture should not be treated as public-safe. |
| Promotion is release-adjacent | Promotion-related shapes must not bypass release gates or governance review. |
| Redaction is receipt/evidence-adjacent | Redaction receipt shapes must not replace emitted receipts, proof records, or evidence bundles. |
| Contracts explain meaning | Each accepted schema needs a paired semantic contract or approved contract profile. |
| Fixtures prove behavior | Policy schemas need valid and invalid fixtures, including deny/restrict/abstain cases where applicable. |
| No parallel authority | Equivalent policy, governance, release, redaction, sensitivity, or exposure schemas must not drift across roots without a mirror/migration rule. |

---

## Policy trust guardrails

| Boundary | Requirement |
|---|---|
| Access posture | Access decisions must not be inferred from schema presence alone. |
| Sensitivity posture | Public, generalized, restricted, and quarantine labels require clear reasons and timestamps. |
| Consent posture | Consent-dependent decisions need explicit consent/policy support before public or semi-public use. |
| Evidence posture | Claims governed by policy still need EvidenceBundle or equivalent support where applicable. |
| Release posture | Public surfaces need release state, correction path, and rollback target support. |
| Audit posture | Policy-support objects should be inspectable and traceable to policy inputs, versions, reasons, and obligations. |

---

## Promotion checklist

A policy schema should not advance beyond `PROPOSED` unless:

- [ ] Paired semantic contract exists.
- [ ] `$id` namespace convention is settled.
- [ ] Required fields are defined.
- [ ] Outcome enum or label enum is reviewed by policy steward.
- [ ] Policy family or sensitivity family vocabulary is reviewed.
- [ ] Policy input bundle requirements are defined.
- [ ] Reasons and obligations are typed sufficiently for audit/review.
- [ ] Timestamps and policy-version fields are defined where needed.
- [ ] Valid fixtures exist.
- [ ] Invalid fixtures exist.
- [ ] Deny/restrict/abstain fixtures exist where applicable.
- [ ] Validators exist and paths are correct.
- [ ] CI/schema-test coverage exists.
- [ ] Governance/release/evidence overlap is resolved or documented.
- [ ] Redaction receipt naming and placement are normalized.
- [ ] Migration notes exist for duplicate or overlapping schema surfaces.

---

## Validation

Recommended local validation sequence:

```bash
# Inspect the policy schema family.
find schemas/contracts/v1/policy -maxdepth 3 -type f | sort

# Detect policy/governance/release overlap.
find schemas/contracts/v1 -maxdepth 5 -type f \
  | grep -Ei 'policy_decision|sensitivity_label|policy_input_bundle|promotion_decision|redaction[-_]receipt|release|governance|exposure' \
  | sort

# Validate JSON syntax for policy schemas and placeholders.
find schemas/contracts/v1/policy -name '*.json' -print0 \
  | xargs -0 -r -I{} python -m json.tool {} >/dev/null

# Inspect paired contracts and fixtures when present.
find contracts/policy fixtures/contracts/v1/policy fixtures/policy -maxdepth 4 -type f 2>/dev/null | sort

# Run project validators when available.
python tools/validate_all.py || true
pytest tests/schemas tests/contract tests/policy tests/release tests/governance || true
```

Replace `|| true` with fail-closed CI behavior once validator and test paths are confirmed.

---

## Rollback

Rollback for this README is ordinary Git rollback: revert the commit that changed `schemas/contracts/v1/policy/README.md`.

Rollback for future policy schema changes requires checking every downstream reference:

1. Revert or migrate schema files.
2. Restore canonical `$id` and `$ref` targets.
3. Restore paired contract links.
4. Restore fixtures, validators, schema registry records, and CI paths.
5. Restore policy, governance, release, evidence, exposure, correction, and receipt references.
6. Restore API/UI/MapLibre/Evidence Drawer consumers.
7. Preserve correction and rollback records if any public or semi-public policy surface was affected.

---

## Open questions

| Question | Status | Owner |
|---|---|---|
| Should `promotion_decision.schema.json` live under `policy/`, `governance/`, `release/`, or use explicit profiles? | **NEEDS VERIFICATION / ADR-sensitive** | Policy steward + Governance steward + Release steward |
| Should `redaction-receipt.json` be renamed to `redaction_receipt.schema.json`, moved, or retired in favor of governance/domain receipt schemas? | **NEEDS VERIFICATION / migration-sensitive** | Redaction steward + Schema steward |
| Should policy schema `$id`s use `https://schemas.kfm.local/contracts/...` or `kfm://schemas/contracts/...`? | **NEEDS VERIFICATION / namespace-sensitive** | Schema steward |
| Which policy fixtures are authoritative: `fixtures/contracts/v1/policy/...` or `fixtures/policy/...`? | **NEEDS VERIFICATION** | Validation steward |
| Which policy object fields are mandatory for public API, MapLibre, Focus Mode, and Evidence Drawer use? | **NEEDS VERIFICATION / release-sensitive** | Policy steward + Release steward |
| Which policy engine or review flow emits `PolicyDecision` records? | **UNKNOWN / NEEDS IMPLEMENTATION EVIDENCE** | Policy steward |

---

## Maintainer notes

- Keep this folder focused on machine-checkable policy-support shapes, not policy enforcement.
- Treat current schemas as PROPOSED until contracts, fixtures, validators, CI, and overlap decisions are verified.
- Prevent drift between policy, governance, release, exposure, evidence, sensitivity, redaction, and receipt schema families.
- Preserve policy, evidence, sensitivity, consent, governance, release, correction, and rollback boundaries for every policy surface.
