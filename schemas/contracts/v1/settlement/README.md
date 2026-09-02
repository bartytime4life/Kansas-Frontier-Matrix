# `schemas/contracts/v1/settlement/` — Settlement Schema Compatibility Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-settlement-readme
title: schemas/contracts/v1/settlement/ — Settlement Schema Compatibility Index
type: readme; schema-family-index; compatibility-index; settlement-schema-boundary; naming-drift-guardrail
authority_class: schema-family-guardrail
version: v0.1
status: draft; singular-settlement-compatibility-path; settlements-infrastructure-overlap; schema-scaffolds-present; receipts-child-lane-present; PROPOSED; CONFLICTED; no-parallel-authority; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Settlement sublane steward
  - OWNER_TBD — Settlements/Infrastructure domain steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Docs steward
created: NEEDS VERIFICATION — empty README existed before v0.1 expansion
updated: 2026-07-04
policy_label: public; schemas; contracts-v1; settlement; settlements-infrastructure; compatibility-path; fort-event; dependency; service-area; receipts; evidence-bound; policy-aware; release-gated; rollback-aware; no-parallel-authority
tags: [kfm, schemas, contracts, v1, settlement, settlements-infrastructure, compatibility, fort-event, dependency, service-area, receipts, process-memory, place-identity, infrastructure, no-parallel-authority]
related:
  - ../README.md
  - ./fort_event.schema.json
  - ./dependency.schema.json
  - ./service_area.schema.json
  - ./receipts/README.md
  - ../domains/settlement/README.md
  - ../domains/settlements-infrastructure/README.md
  - ../receipts/README.md
  - ../evidence/README.md
  - ../policy/README.md
  - ../review/README.md
  - ../release/README.md
  - ../../../../data/receipts/settlement/README.md
  - ../../../../data/receipts/settlements-infrastructure/README.md
  - ../../../../data/proofs/settlement/README.md
  - ../../../../data/proofs/settlements-infrastructure/README.md
  - ../../../../contracts/domains/settlement/
  - ../../../../contracts/domains/settlements-infrastructure/
  - ../../../../docs/domains/settlements-infrastructure/
  - ../../../../fixtures/
  - ../../../../tests/
  - ../../../../release/
notes:
  - "Expanded from an empty file at schemas/contracts/v1/settlement/README.md."
  - "Current GitHub search surfaced fort_event.schema.json, dependency.schema.json, and service_area.schema.json directly under this folder."
  - "All three inspected schemas are PROPOSED empty scaffolds with empty properties, additionalProperties true, source_docs pointing to docs/domains/settlements-infrastructure/EXPANSION_BACKLOG.md, and contract_doc null."
  - "Current domain schema documentation treats singular settlement as a compatibility or conflicted path while broader domain authority points to settlements-infrastructure."
  - "The child receipts lane at schemas/contracts/v1/settlement/receipts/ is README-only and similarly treats singular settlement as compatibility/sublane posture."
  - "This folder may hold compatibility schema scaffolds, but it must not become a parallel canonical Settlements/Infrastructure schema home without ADR or migration notes."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![family](https://img.shields.io/badge/family-settlement-green)
![posture](https://img.shields.io/badge/posture-compatibility-orange)
![maturity](https://img.shields.io/badge/maturity-scaffold-orange)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **Purpose.** `schemas/contracts/v1/settlement/` is a compatibility schema lane for singular settlement-related shapes currently overlapping the broader `settlements-infrastructure` domain.
>
> **One-line boundary.** This path defines machine-checkable shape only. It does not prove settlement identity, certify infrastructure or service-area truth, store data or receipts, publish artifacts, or replace the broader Settlements/Infrastructure domain lane.

---

## Quick jumps

[Status](#status) · [Authority and placement](#authority-and-placement) · [Naming posture](#naming-posture) · [Repo fit](#repo-fit) · [Current schema inventory](#current-schema-inventory) · [Known overlap and drift risks](#known-overlap-and-drift-risks) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Settlement-family rules](#settlement-family-rules) · [Promotion checklist](#promotion-checklist) · [Validation](#validation) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

| Question | Answer | Truth label |
|---|---|---|
| Does this README path exist? | Yes: `schemas/contracts/v1/settlement/README.md`. It was empty before this expansion. | **CONFIRMED** |
| Are schema files present directly under this path? | Yes. Search surfaced `fort_event.schema.json`, `dependency.schema.json`, and `service_area.schema.json`. | **CONFIRMED path presence** |
| Are these schemas mature/field-complete? | No. All three inspected schemas are PROPOSED empty scaffolds with empty `properties`, `additionalProperties: true`, and `contract_doc: null`. | **CONFIRMED scaffold / NEEDS VERIFICATION** |
| Is singular `settlement` confirmed as the canonical domain schema slug? | No. Existing domain schema documentation treats singular `settlement` as a compatibility path and points to `settlements-infrastructure` as the broader working schema lane. | **CONFIRMED compatibility posture** |
| Is there a child receipt schema lane? | Yes. `schemas/contracts/v1/settlement/receipts/README.md` exists as a README-only guardrail. | **CONFIRMED** |
| Can this folder store lifecycle data, emitted receipts, proofs, catalog records, release records, public API behavior, or map artifacts? | No. This is a schema folder and may only define machine-checkable shape. | **CONFIRMED boundary** |

> [!IMPORTANT]
> A settlement schema scaffold is not settlement truth. A schema-valid settlement, fort event, dependency, or service-area object is not evidence-backed, reviewed, policy-safe, released, or public-ready by schema validation alone.

---

## Authority and placement

This folder is under the schema responsibility root:

```text
schemas/contracts/v1/settlement/
```

It may define settlement-related machine-checkable shapes only after placement is resolved. Adjacent authority remains separate:

- `schemas/contracts/v1/domains/settlement/` is a compatibility domain schema lane in current documentation.
- `schemas/contracts/v1/domains/settlements-infrastructure/` is the broader working Settlements/Infrastructure schema lane.
- `schemas/contracts/v1/settlement/receipts/` is a README-only settlement receipt schema guardrail.
- `schemas/contracts/v1/receipts/` owns shared receipt object shapes where accepted.
- `contracts/` owns semantic meaning.
- `data/` owns lifecycle data, emitted receipts, proof artifacts, catalog records, and published data products according to each data root.
- `policy/` owns policy posture where implemented.
- `schemas/contracts/v1/evidence/` owns evidence-support shapes.
- `schemas/contracts/v1/review/` owns review-support shapes where accepted.
- `schemas/contracts/v1/release/` owns release/correction/rollback support shapes where accepted.
- `release/` owns actual release, correction, withdrawal, and rollback records where present.
- `fixtures/` and `tests/` prove valid/invalid examples and validator behavior.

This README does not amend ADR-0001, Directory Rules, settlement naming governance, Settlements/Infrastructure doctrine, policy docs, validators, or release gates.

---

## Naming posture

Current repository evidence shows a naming split:

```text
schemas/contracts/v1/settlement/                    # this requested flat schema lane
schemas/contracts/v1/settlement/receipts/           # child receipt schema guardrail
schemas/contracts/v1/domains/settlement/            # singular compatibility domain index
schemas/contracts/v1/domains/settlements-infrastructure/  # broader working domain schema lane

data/receipts/settlement/                           # settlement-sublane emitted receipt/process-memory lane
data/receipts/settlements-infrastructure/           # broader domain emitted receipt/process-memory lane
```

This README treats `schemas/contracts/v1/settlement/` as a compatibility or sublane schema surface until accepted directory governance decides whether these schema files should stay here, move under `schemas/contracts/v1/domains/settlements-infrastructure/`, become shared profiles, or be retired.

---

## Repo fit

```text
schemas/
└── contracts/
    └── v1/
        ├── README.md
        ├── settlement/
        │   ├── README.md                         # this file; compatibility index
        │   ├── fort_event.schema.json            # PROPOSED empty scaffold
        │   ├── dependency.schema.json            # PROPOSED empty scaffold
        │   ├── service_area.schema.json          # PROPOSED empty scaffold
        │   └── receipts/
        │       └── README.md                     # README-only receipt guardrail
        ├── domains/
        │   ├── settlement/
        │   │   └── README.md                     # singular compatibility index
        │   └── settlements-infrastructure/
        │       └── README.md                     # broader working domain lane
        ├── receipts/
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

## Current schema inventory

| File | Current posture | Shape maturity | Notes |
|---|---|---|---|
| `fort_event.schema.json` | **PROPOSED** | Empty scaffold | Draft 2020-12 object; `$id` is `kfm://schemas/contracts/v1/settlement/fort_event.schema.json`; `properties` is empty; `additionalProperties: true`; source docs point to `docs/domains/settlements-infrastructure/EXPANSION_BACKLOG.md`; `contract_doc: null`. |
| `dependency.schema.json` | **PROPOSED** | Empty scaffold | Draft 2020-12 object; `$id` is `kfm://schemas/contracts/v1/settlement/dependency.schema.json`; `properties` is empty; `additionalProperties: true`; source docs point to `docs/domains/settlements-infrastructure/EXPANSION_BACKLOG.md`; `contract_doc: null`. |
| `service_area.schema.json` | **PROPOSED** | Empty scaffold | Draft 2020-12 object; `$id` is `kfm://schemas/contracts/v1/settlement/service_area.schema.json`; `properties` is empty; `additionalProperties: true`; source docs point to `docs/domains/settlements-infrastructure/EXPANSION_BACKLOG.md`; `contract_doc: null`. |
| `receipts/README.md` | **README-only guardrail** | Placement note | Child receipt schema lane; not a schema and not emitted receipt storage. |

---

## Known overlap and drift risks

| Risk | Evidence signal | Required posture |
|---|---|---|
| Singular vs broader slug drift | `schemas/contracts/v1/domains/settlement/README.md` says singular `settlement` is not confirmed canonical and points to `settlements-infrastructure`. | **Keep compatibility posture visible** |
| Flat schema vs domain schema placement | Current scaffolds live in flat `schemas/contracts/v1/settlement/`, not under `domains/settlements-infrastructure/`. | **Needs ADR/migration decision** |
| Receipt child lane overlap | `settlement/receipts/` exists as a README-only receipt schema guardrail. | **Keep receipt shape separate from emitted receipts** |
| Empty scaffold maturity | All inspected flat schemas have empty `properties` and `additionalProperties: true`. | **Do not imply field-complete validation** |
| Contract doc gap | All inspected flat schemas have `contract_doc: null`. | **Needs paired contract or approved profile** |
| Data/proof/release separation | Settlement/Infrastructure has data receipt and proof lanes elsewhere. | **Keep roots separate** |

---

## What belongs here

- This README.
- Existing compatibility schema scaffolds until placement is resolved.
- Future machine-checkable JSON Schema files for settlement-related object shapes only if accepted here by ADR or migration note.
- Compatibility notes for singular `settlement` versus broader `settlements-infrastructure` naming.
- Migration notes after accepted schema home is decided.
- Links to paired contracts, fixtures, validators, schema registry records, evidence references, policy references, receipt references, review references, release references, correction references, rollback references, and tests.

---

## What does not belong here

- New canonical schema families until placement is resolved.
- Contract prose beyond README boundary notes.
- Lifecycle data, emitted receipts, proof outputs, catalog records, source registry records, release records, correction records, rollback cards, review decisions, policy decisions, EvidenceBundles, public map/API artifacts, dashboards, screenshots, or generated summaries.
- Settlement payloads, municipal-status data, census-place payloads, historic-townsite payloads, ghost-town records, fort records, infrastructure records, condition records, dependency records, service-area payloads, source payloads, or domain payloads.
- Policy rules, review procedures, release implementation code, validator code, packages, pipelines, runtime code, UI/API implementation, map tiles, or public display behavior.
- Claims that a settlement object, fort event, dependency, service area, receipt, review, correction, rollback, release, or public projection is true, complete, reviewed, policy-safe, release-approved, or publication-ready merely because it validates against a schema in this folder.

---

## Settlement-family rules

| Rule | Requirement |
|---|---|
| Shape is not truth | Schema validation constrains shape; it does not prove settlement, fort, dependency, or service-area claims. |
| Compatibility stays visible | Singular `settlement` remains compatibility/sublane posture until naming governance resolves it. |
| Broader domain remains visible | `settlements-infrastructure` remains the broader working domain lane unless an ADR says otherwise. |
| Evidence remains separate | Objects may cite EvidenceRefs or EvidenceBundles, but do not replace them. |
| Review remains separate | Review fields or receipt handoff do not prove review or approval. |
| Policy remains separate | Objects may reference policy state, but do not decide admissibility. |
| Release remains separate | Release-candidate objects do not publish or approve artifacts. |
| Receipts stay separate | Receipt schemas and emitted receipts must not collapse into this parent lane. |
| Fixtures prove behavior | Accepted schemas need valid and invalid fixtures plus validator coverage. |
| No parallel authority | Equivalent settlement, infrastructure, receipt, review, release, policy, and evidence shapes must not drift across roots without migration notes. |

---

## Promotion checklist

A settlement schema should not advance beyond `PROPOSED` unless:

- [ ] Accepted placement is resolved: this lane, `domains/settlements-infrastructure/`, shared profile, or another approved lane.
- [ ] Singular `settlement` vs `settlements-infrastructure` naming is documented.
- [ ] Paired semantic contract exists or an approved profile is documented.
- [ ] `$id` namespace convention is settled.
- [ ] Required fields are defined.
- [ ] Source-role, identity, time, evidence, policy, review, release, correction, and rollback references are defined where material.
- [ ] Emitted-record storage paths are documented separately from schema shape.
- [ ] Valid fixtures exist.
- [ ] Invalid fixtures exist.
- [ ] Validators exist and paths are correct.
- [ ] CI/schema-test coverage exists.
- [ ] Migration notes exist for duplicate or overlapping schema surfaces.

---

## Validation

Recommended local validation sequence:

```bash
# Inspect the flat settlement compatibility schema lane.
find schemas/contracts/v1/settlement -maxdepth 4 -type f | sort

# Inspect broader settlement naming and schema surfaces.
find schemas/contracts/v1 -maxdepth 6 -type f \
  | grep -Ei 'settlement|settlements-infrastructure|fort_event|dependency|service_area|receipt|review|release|policy|evidence' \
  | sort

# Validate JSON syntax for flat settlement schemas.
find schemas/contracts/v1/settlement -name '*.json' -print0 \
  | xargs -0 -r -I{} python -m json.tool {} >/dev/null

# Inspect emitted receipt/proof lanes separately from schema shapes.
find data/receipts data/proofs -maxdepth 5 -type f 2>/dev/null \
  | grep -Ei 'settlement|settlements-infrastructure|README|receipt|proof' \
  | sort

# Run project validators when available.
python tools/validate_all.py || true
pytest tests/schemas tests/contract tests/policy tests/governance tests/release || true
```

Replace `|| true` with fail-closed CI behavior once validator and test paths are confirmed.

---

## Rollback

Rollback for this README is ordinary Git rollback: revert the commit that changed `schemas/contracts/v1/settlement/README.md`.

Rollback for future settlement schema changes requires checking every downstream reference:

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
| Should flat settlement schemas remain under `schemas/contracts/v1/settlement/`, move under `domains/settlements-infrastructure/`, or become explicit compatibility profiles? | **NEEDS VERIFICATION / ADR-sensitive** | Schema steward + Settlements/Infrastructure steward |
| Is singular `settlement` an accepted sublane slug, compatibility path, or path to retire? | **NEEDS VERIFICATION / naming-sensitive** | Settlement steward + Directory steward |
| Which semantic contracts own FortEvent, Dependency, and ServiceArea meanings? | **NEEDS VERIFICATION** | Contract steward |
| Which fixtures prove these scaffolds do not replace evidence, proof, review, policy, release, or emitted receipt authority? | **NEEDS VERIFICATION** | Validation steward |
| Which settlement projections are safe for public API/MapLibre/Focus Mode use? | **NEEDS VERIFICATION / release-gated** | Release steward + Policy steward |

---

## Maintainer notes

- Keep this folder in compatibility posture until schema-home placement is resolved.
- Do not add new canonical schemas here unless ADR or migration notes resolve the singular-vs-broader domain split.
- Prefer references to governed evidence, receipt, review, policy, and release objects over copied fields.
- Keep emitted receipts under `data/receipts/`, proofs under `data/proofs/`, and release records under `release/`.
- Preserve evidence, review, policy, release, correction, rollback, and naming-governance boundaries for every settlement schema surface.
