# `schemas/contracts/v1/receipts/` — Receipt Schema Family Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-receipts-readme
title: schemas/contracts/v1/receipts/ — Receipt Schema Family Index
type: readme; schema-family-index; receipt-schema-boundary
authority_class: schema-family-index
version: v0.1
status: draft; receipt-family-present; mixed-maturity-schemas-present; placeholder-drift-visible; child-lane-guardrail-present; PROPOSED; no-parallel-authority; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Receipt steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Docs steward
created: NEEDS VERIFICATION — empty README existed before v0.1 expansion
updated: 2026-07-04
policy_label: public; schemas; contracts-v1; receipts; generated-receipt; redaction-receipt; source-activation-decision; evidence-bound; policy-aware; release-gated; rollback-aware; no-parallel-authority
tags: [kfm, schemas, contracts, v1, receipts, GeneratedReceipt, RedactionReceipt, source-activation-decision, provenance, process-memory, validation, policy, release, rollback, no-parallel-authority]
related:
  - ../README.md
  - ./generated_receipt.schema.json
  - ./redaction_receipt.schema.json
  - ./source-activation-decision.json
  - ./redaction/README.md
  - ../governance/README.md
  - ../policy/README.md
  - ../evidence/README.md
  - ../release/
  - ../../../../contracts/shared/redaction_receipt.md
  - ../../../../data/receipts/
  - ../../../../fixtures/contracts/v1/
  - ../../../../tests/
  - ../../../../release/
notes:
  - "Expanded from an empty file at schemas/contracts/v1/receipts/README.md."
  - "Current search surfaced generated_receipt.schema.json, redaction_receipt.schema.json, and source-activation-decision.json under this folder."
  - "generated_receipt.schema.json has concrete required fields and additionalProperties false."
  - "redaction_receipt.schema.json is a permissive PROPOSED scaffold with empty properties and contract_doc null."
  - "source-activation-decision.json is a placeholder JSON file, not a .schema.json file."
  - "A redaction/ child README exists as a placement guardrail and does not replace the flat redaction_receipt.schema.json surface."
  - "This folder defines receipt object shapes only; emitted receipt instances belong under data/receipts or another governed data root."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![family](https://img.shields.io/badge/family-receipts-purple)
![shape](https://img.shields.io/badge/authority-machine--shape-informational)
![maturity](https://img.shields.io/badge/maturity-mixed-orange)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **Purpose.** `schemas/contracts/v1/receipts/` is the machine-checkable schema family for receipt-shaped process-memory and provenance objects.
>
> **One-line boundary.** Receipt schemas define object shape only. They do not prove the recorded event happened, store emitted receipt instances, approve release, replace EvidenceBundles, or make generated material authoritative.

---

## Quick jumps

[Status](#status) · [Authority and placement](#authority-and-placement) · [Repo fit](#repo-fit) · [Current schema inventory](#current-schema-inventory) · [Known overlap and drift risks](#known-overlap-and-drift-risks) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Receipt-family rules](#receipt-family-rules) · [Promotion checklist](#promotion-checklist) · [Validation](#validation) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

| Question | Answer | Truth label |
|---|---|---|
| Does this README path exist? | Yes: `schemas/contracts/v1/receipts/README.md`. It was empty before this expansion. | **CONFIRMED** |
| Are receipt schema files present in this folder? | Yes. Search surfaced `generated_receipt.schema.json` and `redaction_receipt.schema.json`. | **CONFIRMED path presence** |
| Are placeholder files present? | Yes. Search surfaced `source-activation-decision.json`, which is not a `.schema.json` file. | **CONFIRMED path presence** |
| Are all receipt schemas mature/field-complete? | No. `generated_receipt.schema.json` has concrete required fields, while `redaction_receipt.schema.json` is an empty permissive scaffold. | **CONFIRMED mixed maturity** |
| Is the `redaction/` child lane canonical? | Not proven. It is a README-only placement guardrail in the current session. | **NEEDS VERIFICATION / ADR-sensitive** |
| Can this folder store emitted receipt instances? | No. This is schema documentation and schema shape only; emitted receipts belong under governed data roots such as `data/receipts/`. | **CONFIRMED boundary** |

> [!IMPORTANT]
> A receipt schema is not a receipt instance. A schema-valid receipt is not proof by itself; it needs actual records, inputs, timestamps, references, validation, and review context appropriate to its use.

---

## Authority and placement

This folder is under the schema responsibility root:

```text
schemas/contracts/v1/receipts/
```

It may define machine-checkable receipt shapes, but adjacent authority is separate:

- `contracts/` owns semantic meaning for receipt object families.
- `data/receipts/` or another governed data root owns emitted receipt instances.
- `schemas/contracts/v1/evidence/` owns evidence-support shapes.
- `schemas/contracts/v1/policy/` owns policy-support shapes.
- `schemas/contracts/v1/governance/` owns governance/review/stewardship shapes.
- `schemas/contracts/v1/release/` owns release object shapes where present.
- `fixtures/` and `tests/` prove examples and validator behavior.
- `release/` owns release, correction, withdrawal, and rollback records.

This README does not amend ADR-0001, Directory Rules, receipt doctrine, governance docs, policy docs, validators, or release gates.

---

## Repo fit

```text
schemas/
└── contracts/
    └── v1/
        ├── README.md
        ├── receipts/
        │   ├── README.md                         # this file
        │   ├── generated_receipt.schema.json     # concrete PROPOSED schema
        │   ├── redaction_receipt.schema.json     # permissive PROPOSED scaffold
        │   ├── source-activation-decision.json   # placeholder / naming drift
        │   └── redaction/
        │       └── README.md                     # child placement guardrail
        ├── evidence/
        ├── governance/
        ├── policy/
        └── release/

contracts/
data/
└── receipts/                                     # emitted receipt instances; not schema shape
fixtures/
tests/
release/
```

---

## Current schema inventory

| File | Current posture | Shape maturity | Notes |
|---|---|---|---|
| `generated_receipt.schema.json` | **PROPOSED** | Concrete schema | Requires receipt identity, contract version, artifact paths/hashes, model identity, prompt/contract hash, parameters, inputs, truth labels, validation gates, policy decisions, citations, human review, created time, and emitter. |
| `redaction_receipt.schema.json` | **PROPOSED** | Empty scaffold | Empty `properties`, `additionalProperties: true`, `contract_doc: null`; source docs point to Fauna API/data lifecycle docs. |
| `source-activation-decision.json` | **PROPOSED placeholder** | Non-schema placeholder | Placeholder JSON with `status`, `path`, `source_docs`, and `notes`; filename is hyphenated and lacks `.schema.json`. |
| `redaction/README.md` | **README-only guardrail** | Placement note | Child-lane README; not a schema and not canonical authority. |

---

## Known overlap and drift risks

| Risk | Evidence signal | Required posture |
|---|---|---|
| Schema vs emitted record | Receipt schema files live under `schemas/`; emitted records live under governed data roots. | **Keep roots separate** |
| Flat vs child receipt path | `redaction_receipt.schema.json` is flat while `redaction/README.md` exists as a child guardrail. | **Needs placement decision before movement** |
| Receipt vs governance overlap | Governance schema family has receipt-adjacent surfaces. | **No parallel authority without profile/migration rule** |
| Receipt vs policy overlap | Policy schema family has placeholder/decision surfaces. | **Keep policy decision and receipt record roles separate** |
| Placeholder naming drift | `source-activation-decision.json` is not `.schema.json`. | **Needs normalization before promotion** |
| Namespace drift | Receipt schemas use different `$id` conventions across current files. | **NEEDS VERIFICATION** |

---

## What belongs here

- This README.
- Machine-checkable JSON Schema files for receipt object shapes.
- README-only guardrails for candidate receipt child lanes.
- Migration notes for flat-vs-child schema layout decisions.
- Links to paired contracts, fixtures, validators, schema registry records, evidence references, policy references, release references, correction references, rollback references, and tests.

---

## What does not belong here

- Emitted receipt instances.
- Lifecycle data, source records, catalog records, triplets, proof outputs, release records, correction records, rollback cards, public artifacts, dashboards, screenshots, or generated summaries.
- Policy rules, governance decisions, release decisions, or runtime code.
- Domain data or source payloads.
- Claims that a receipt is true, complete, reviewed, policy-safe, release-approved, or publication-ready merely because it validates against a schema.

---

## Receipt-family rules

| Rule | Requirement |
|---|---|
| Shape is not event proof | Schema validation constrains shape; it does not prove the recorded event occurred. |
| Receipt is process memory | Receipt objects document process context and references; they do not replace evidence, governance, or release records. |
| Contracts explain meaning | Accepted schemas need paired semantic contracts or approved contract profiles. |
| Fixtures prove behavior | Accepted schemas need valid and invalid fixtures plus validator coverage. |
| Policy and release remain separate | Receipt objects may reference policy/release records but do not make those decisions. |
| Generated output remains downstream | A generated receipt can support AI artifact provenance; it does not make generated language sovereign truth. |
| No parallel authority | Equivalent receipt shapes must not drift across receipts, governance, policy, domain lanes, and data roots without migration notes. |

---

## Promotion checklist

A receipt schema should not advance beyond `PROPOSED` unless:

- [ ] Paired semantic contract exists.
- [ ] `$id` namespace convention is settled.
- [ ] Required fields are defined.
- [ ] Object role is separated from evidence, policy, governance, and release records.
- [ ] Valid fixtures exist.
- [ ] Invalid fixtures exist.
- [ ] Validators exist and paths are correct.
- [ ] CI/schema-test coverage exists.
- [ ] Emitted-record storage path is documented separately from schema shape.
- [ ] Migration notes exist for duplicate or overlapping schema surfaces.
- [ ] Release/correction/rollback references are defined where public use depends on the receipt.

---

## Validation

Recommended local validation sequence:

```bash
# Inspect the receipt schema family.
find schemas/contracts/v1/receipts -maxdepth 4 -type f | sort

# Detect receipt-related shape overlap across schema families.
find schemas/contracts/v1 -maxdepth 6 -type f \
  | grep -Ei 'receipt|source[-_]activation|generated' \
  | sort

# Validate JSON syntax for receipt schemas and placeholders.
find schemas/contracts/v1/receipts -name '*.json' -print0 \
  | xargs -0 -r -I{} python -m json.tool {} >/dev/null

# Inspect emitted receipt README lanes separately from schemas.
find data/receipts -maxdepth 5 -name 'README.md' -type f 2>/dev/null | sort

# Run project validators when available.
python tools/validate_all.py || true
pytest tests/schemas tests/contract tests/policy tests/governance tests/release || true
```

Replace `|| true` with fail-closed CI behavior once validator and test paths are confirmed.

---

## Rollback

Rollback for this README is ordinary Git rollback: revert the commit that changed `schemas/contracts/v1/receipts/README.md`.

Rollback for future receipt schema changes requires checking every downstream reference:

1. Revert or migrate schema files.
2. Restore canonical `$id` and `$ref` targets.
3. Restore paired contract links.
4. Restore fixtures, validators, schema registry records, and CI paths.
5. Restore evidence, policy, governance, release, correction, and emitted receipt references.
6. Restore API/UI/MapLibre/Evidence Drawer consumers where applicable.
7. Preserve correction and rollback records if any public or semi-public receipt surface was affected.

---

## Open questions

| Question | Status | Owner |
|---|---|---|
| Should receipt schemas stay flat under `receipts/` or move into per-receipt child folders? | **NEEDS VERIFICATION / ADR-sensitive** | Receipt steward + Schema steward |
| Should `source-activation-decision.json` become a `.schema.json`, move elsewhere, or remain a placeholder? | **NEEDS VERIFICATION / naming-sensitive** | Receipt steward + Source steward |
| Which contract owns `GeneratedReceipt` meaning? | **NEEDS VERIFICATION** | Contract steward + AI/build steward |
| Which emitted receipt roots are authoritative for generated, redaction, source activation, and domain-specific receipts? | **NEEDS VERIFICATION** | Receipt steward + Data steward |
| Which receipt projections are safe for public API/MapLibre/Focus Mode use? | **NEEDS VERIFICATION / release-gated** | Release steward + Policy steward |

---

## Maintainer notes

- Keep this folder focused on receipt schema shape, not emitted receipt storage.
- Prefer one canonical schema home per receipt family with explicit profile or migration notes.
- Keep schemas, contracts, policy, evidence, governance, emitted records, proof, and release authority separate.
