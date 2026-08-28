# `schemas/contracts/v1/registries/` — Registry Schema Family Guardrail

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-registries-readme
title: schemas/contracts/v1/registries/ — Registry Schema Family Guardrail
type: readme; schema-family-index; registry-schema-boundary; placement-guardrail
authority_class: schema-family-guardrail
version: v0.1
status: draft; empty-schema-family; data-registry-lanes-present; no-current-registry-schema-files-found; do-not-promote-without-ADR; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Registry steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Data steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Docs steward
created: NEEDS VERIFICATION — empty README existed before v0.1 expansion
updated: 2026-07-04
policy_label: public; schemas; contracts-v1; registries; registry-shape; data-registry-separation; evidence-bound; policy-aware; release-gated; rollback-aware; no-parallel-authority
tags: [kfm, schemas, contracts, v1, registries, registry, source-registry, dataset-registry, layer-registry, sensitivity-registry, rights-registry, schema-guardrail, no-parallel-authority]
related:
  - ../README.md
  - ../layers/README.md
  - ../policy/README.md
  - ../evidence/README.md
  - ../receipts/README.md
  - ../../../../data/registry/
  - ../../../../data/registry/layers/README.md
  - ../../../../data/registry/sensitivity/README.md
  - ../../../../data/registry/rights/README.md
  - ../../../../data/registry/datasets/flora/README.md
  - ../../../../contracts/
  - ../../../../policy/
  - ../../../../fixtures/
  - ../../../../tests/
  - ../../../../release/
notes:
  - "Expanded from an empty file at schemas/contracts/v1/registries/README.md."
  - "Current GitHub search did not surface schema files directly under schemas/contracts/v1/registries/ beyond this README."
  - "Current search surfaced data registry lanes under data/registry/, including layers, sensitivity, rights, and datasets."
  - "Representative data registry READMEs state that registry/control records do not store payloads, publish artifacts, define schema authority, or replace policy/release gates."
  - "This folder may define registry object shapes in the future, but it must not become the emitted registry data root."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![family](https://img.shields.io/badge/family-registries-blueviolet)
![posture](https://img.shields.io/badge/posture-guardrail-orange)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **Purpose.** `schemas/contracts/v1/registries/` is a README-only guardrail for possible machine-checkable registry record shapes.
>
> **One-line boundary.** Registry schemas define object shape only. Actual registry/control records belong under governed data registry roots such as `data/registry/...`, not under this schema folder.

---

## Quick jumps

[Status](#status) · [Authority and placement](#authority-and-placement) · [Repo fit](#repo-fit) · [Current inventory](#current-inventory) · [Related registry lanes](#related-registry-lanes) · [Candidate registry shapes](#candidate-registry-shapes) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Registry-family rules](#registry-family-rules) · [Promotion checklist](#promotion-checklist) · [Validation](#validation) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

| Question | Answer | Truth label |
|---|---|---|
| Does this README path exist? | Yes: `schemas/contracts/v1/registries/README.md`. It was empty before this expansion. | **CONFIRMED** |
| Are schema files currently present directly under `schemas/contracts/v1/registries/`? | Not found in the current GitHub search beyond this README. | **NEEDS VERIFICATION / search-limited** |
| Are registry data lanes present elsewhere? | Yes. Search surfaced multiple `data/registry/...` README lanes. | **CONFIRMED path evidence** |
| Is this schema folder a registry data root? | No. It is under `schemas/` and may only define machine-checkable shapes. | **CONFIRMED boundary** |
| Can registry schemas publish data or close release gates? | No. Registry schemas can constrain shape; they cannot publish artifacts or replace evidence, policy, review, release, correction, or rollback records. | **CONFIRMED boundary** |

> [!IMPORTANT]
> A registry schema is not a registry record. A registry record is not, by itself, source truth, domain truth, proof, policy approval, release approval, or publication.

---

## Authority and placement

This folder is under the schema responsibility root:

```text
schemas/contracts/v1/registries/
```

It may define shared registry record shapes only after placement and contract review. Adjacent authority remains separate:

- `data/registry/` owns emitted registry/control records.
- `contracts/` owns semantic meaning for registry object families.
- `schemas/contracts/v1/layers/` owns shared layer object shapes.
- `schemas/contracts/v1/policy/` owns policy-support shapes.
- `schemas/contracts/v1/evidence/` owns evidence-support shapes.
- `schemas/contracts/v1/receipts/` owns receipt object shapes.
- `policy/` owns policy posture where implemented.
- `release/` owns release, correction, withdrawal, and rollback records.
- `fixtures/` and `tests/` prove valid/invalid examples and validator behavior.

This README does not amend ADR-0001, Directory Rules, registry docs, policy docs, validators, or release gates.

---

## Repo fit

```text
schemas/
└── contracts/
    └── v1/
        ├── README.md
        ├── registries/
        │   └── README.md                         # this file; guardrail only
        ├── layers/
        ├── policy/
        ├── evidence/
        └── receipts/

data/
└── registry/                                     # emitted registry/control records; not schema shape
    ├── layers/
    ├── sensitivity/
    ├── rights/
    └── datasets/

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
| `schemas/contracts/v1/registries/README.md` | README | **CONFIRMED present** | Empty file expanded by this README. |
| `schemas/contracts/v1/registries/*.schema.json` | Schema files | **Not found in current search** | Do not create here without contract pairing, fixtures, validators, and placement review. |
| `data/registry/layers/README.md` | Data registry README | **CONFIRMED inspected** | Layer registry/control lane; not layer bytes, schema authority, policy, release authority, or public material. |
| `data/registry/sensitivity/README.md` | Data registry README | **CONFIRMED inspected** | Sensitivity registry/control lane; not source storage, proof storage, receipt storage, schema authority, policy, release authority, or public material. |
| `data/registry/rights/README.md` | Data registry README | **CONFIRMED surfaced** | Rights registry lane surfaced by search; not inspected in this edit. |
| `data/registry/datasets/flora/README.md` | Data registry README | **CONFIRMED surfaced** | Dataset registry lane surfaced by search; not inspected in this edit. |

---

## Related registry lanes

Current search surfaced the following `data/registry/...` surfaces. This list is search-derived and not a complete registry inventory.

| Path | Role signal | Posture |
|---|---|---|
| `data/registry/layers/` | Layer registry/control records. | **DRAFT / data root** |
| `data/registry/sensitivity/` | Sensitivity registry/control records. | **DRAFT / restricted-review** |
| `data/registry/rights/` | Rights registry/control records. | **NEEDS VERIFICATION** |
| `data/registry/datasets/flora/` | Flora dataset registry records. | **NEEDS VERIFICATION** |
| `data/registry/layers/<domain>/` | Domain-specific layer registry lanes. | **NEEDS VERIFICATION** |
| `data/registry/sensitivity/<domain>/` | Domain-specific sensitivity registry lanes. | **NEEDS VERIFICATION** |

---

## Candidate registry shapes

Candidate schemas below are proposals only and should not be created without steward review.

| Candidate schema | Purpose | Default posture |
|---|---|---|
| `registry_record.schema.json` | Generic registry record envelope. | **PROPOSED / not created** |
| `layer_registry_record.schema.json` | Shape for layer registry/control records. | **PROPOSED / layer-profile-sensitive** |
| `dataset_registry_record.schema.json` | Shape for dataset registry records. | **PROPOSED / source-role-sensitive** |
| `source_registry_record.schema.json` | Shape for source registry records or descriptors. | **PROPOSED / source-steward review required** |
| `sensitivity_registry_record.schema.json` | Shape for sensitivity registry/control records. | **PROPOSED / restricted-review** |
| `rights_registry_record.schema.json` | Shape for rights registry records. | **PROPOSED / rights-review required** |
| `registry_validation_report.schema.json` | Shape for registry validation output. | **PROPOSED / proof-adjacent** |

> [!CAUTION]
> Candidate names are proposals only. Do not treat them as repo files, accepted contracts, data records, validator proof, or release authority until created, paired, fixture-tested, and reviewed.

---

## What belongs here

- This README.
- Future machine-checkable JSON Schema files for shared registry record shapes if accepted.
- Schema index notes for registry object families.
- Migration notes for registry schema placement.
- Links to paired contracts, data registry roots, fixtures, validators, schema registry records, policy references, evidence references, release references, correction references, rollback references, and tests.

---

## What does not belong here

- Emitted registry records.
- Source data, lifecycle data, catalog records, triplets, proof outputs, receipt instances, release records, correction notices, rollback cards, published artifacts, public map artifacts, dashboards, screenshots, or generated summaries.
- Policy rules, release decisions, rights decisions, source identity decisions, or runtime code.
- Domain payloads or source payloads.
- Claims that a registry record is true, complete, policy-safe, release-approved, or publication-ready merely because it validates against a schema.

---

## Registry-family rules

| Rule | Requirement |
|---|---|
| Shape is not record | Schema validation constrains shape; it does not create or authorize registry records. |
| Registry is not publication | Registry records may support readiness, routing, or control state; they do not publish artifacts. |
| Registry is not proof | Registry records may point to evidence/proof/receipts, but do not replace them. |
| Registry is not policy | Registry records may point to policy posture, but do not decide policy. |
| Contracts explain meaning | Accepted registry schemas need paired semantic contracts or approved contract profiles. |
| Fixtures prove behavior | Accepted schemas need valid and invalid fixtures plus validator coverage. |
| No parallel authority | Equivalent registry shapes must not drift across `schemas/`, `data/registry/`, domain lanes, policy lanes, and release lanes without migration notes. |

---

## Promotion checklist

A registry schema should not advance beyond `PROPOSED` unless:

- [ ] Paired semantic contract exists.
- [ ] `$id` namespace convention is settled.
- [ ] Required fields are defined.
- [ ] Emitted-record storage path is documented separately from schema shape.
- [ ] Relationship to source, dataset, layer, rights, sensitivity, evidence, policy, receipt, and release references is defined.
- [ ] Valid fixtures exist.
- [ ] Invalid fixtures exist.
- [ ] Validators exist and paths are correct.
- [ ] CI/schema-test coverage exists.
- [ ] Migration notes exist for duplicate or overlapping schema surfaces.
- [ ] Release/correction/rollback references are defined where public use depends on registry state.

---

## Validation

Recommended local validation sequence:

```bash
# Inspect this registry schema family.
find schemas/contracts/v1/registries -maxdepth 4 -type f | sort

# Inspect data registry README lanes separately from schemas.
find data/registry -maxdepth 5 -name 'README.md' -type f 2>/dev/null | sort

# Detect registry-related schemas and placeholders elsewhere.
find schemas/contracts/v1 -maxdepth 6 -type f \
  | grep -Ei 'registry|source_descriptor|layer_manifest|sensitivity_label|rights' \
  | sort

# Validate JSON syntax for registry-related schema files when present.
find schemas/contracts/v1 -maxdepth 6 -type f \
  | grep -Ei 'registry|source_descriptor|layer_manifest|sensitivity_label|rights' \
  | xargs -r -I{} python -m json.tool {} >/dev/null

# Run project validators when available.
python tools/validate_all.py || true
pytest tests/schemas tests/contract tests/policy tests/release || true
```

Replace `|| true` with fail-closed CI behavior once validator and test paths are confirmed.

---

## Rollback

Rollback for this README is ordinary Git rollback: revert the commit that changed `schemas/contracts/v1/registries/README.md`.

Rollback for future registry schema changes requires checking every downstream reference:

1. Revert or migrate schema files.
2. Restore canonical `$id` and `$ref` targets.
3. Restore paired contract links.
4. Restore fixtures, validators, schema registry records, and CI paths.
5. Restore data registry, evidence, policy, governance, receipt, release, correction, and rollback references.
6. Restore API/UI/MapLibre/Evidence Drawer consumers where applicable.
7. Preserve correction and rollback records if any public or semi-public registry surface was affected.

---

## Open questions

| Question | Status | Owner |
|---|---|---|
| Should shared registry schemas live under `schemas/contracts/v1/registries/`, or should each registry type be owned by its domain/family schema lane? | **NEEDS VERIFICATION / ADR-sensitive** | Registry steward + Schema steward |
| Which contract lane owns generic registry record semantics? | **NEEDS VERIFICATION** | Contract steward + Registry steward |
| Which emitted registry roots are authoritative for source, dataset, layer, rights, sensitivity, and crosswalk records? | **NEEDS VERIFICATION** | Registry steward + Data steward |
| Should `layer_manifest` and `layer_registry_record` remain separate object families? | **NEEDS VERIFICATION / map-layer-sensitive** | Layer steward + Registry steward |
| Which registry projections are safe for public API/MapLibre/Focus Mode use? | **NEEDS VERIFICATION / release-gated** | Release steward + Policy steward |

---

## Maintainer notes

- Keep this folder README-only until registry schema-home placement is resolved.
- Prefer one canonical schema home per registry object family with explicit profile or migration notes.
- Keep schemas, contracts, data registry records, policy, evidence, receipts, proof, and release authority separate.
