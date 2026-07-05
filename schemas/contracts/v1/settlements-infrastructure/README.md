# `schemas/contracts/v1/settlements-infrastructure/` — Schema Compatibility Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-settlements-infrastructure-readme
title: schemas/contracts/v1/settlements-infrastructure/ — Schema Compatibility Index
type: readme; compatibility-index; schema-boundary
authority_class: schema-family-guardrail
version: v0.1
status: draft; flat-compatibility-path; canonical-domain-lane-present; no-current-flat-schema-files-found; PROPOSED; NEEDS VERIFICATION before promotion
owners:
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
policy_label: public; schemas; contracts-v1; settlements-infrastructure; compatibility-path; evidence-bound; policy-aware; release-gated; no-parallel-authority
tags: [kfm, schemas, contracts, v1, settlements-infrastructure, compatibility, canonical-domain-lane, no-parallel-authority]
related:
  - ../README.md
  - ../domains/settlements-infrastructure/README.md
  - ../domains/settlement/README.md
  - ../settlement/README.md
  - ../settlement/receipts/README.md
  - ../receipts/README.md
  - ../evidence/README.md
  - ../policy/README.md
  - ../review/README.md
  - ../release/README.md
notes:
  - "Expanded from an empty file at schemas/contracts/v1/settlements-infrastructure/README.md."
  - "Current GitHub search did not surface schema files directly under this flat path beyond this README."
  - "schemas/contracts/v1/domains/settlements-infrastructure/README.md identifies itself as the schemas/contracts/v1 home for the domain lane and marks authority level canonical, while still PROPOSED greenfield scaffold."
  - "schemas/contracts/v1/settlement/README.md documents the flat singular settlement lane as compatibility posture with PROPOSED empty scaffolds."
  - "This README is a compatibility guardrail only and must not become parallel canonical schema authority without ADR or migration review."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![posture](https://img.shields.io/badge/posture-compatibility-orange)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **Purpose.** `schemas/contracts/v1/settlements-infrastructure/` is a flat compatibility index for Settlements/Infrastructure schema placement.
>
> **One-line boundary.** This path defines schema-placement guidance only. It does not replace `schemas/contracts/v1/domains/settlements-infrastructure/`, store emitted records, publish artifacts, or prove domain claims.

---

## Status

| Question | Answer | Truth label |
|---|---|---|
| Does this README path exist? | Yes. It was empty before this expansion. | **CONFIRMED** |
| Are schema files present directly under this flat path? | Not found in the current GitHub search beyond this README. | **NEEDS VERIFICATION / search-limited** |
| Is there a current canonical domain-lane signal? | Yes. `schemas/contracts/v1/domains/settlements-infrastructure/README.md` identifies itself as the schemas/contracts/v1 home for the domain lane and marks authority level `canonical`. | **CONFIRMED path evidence** |
| Is that canonical lane complete? | Not proven. Its status is `PROPOSED (greenfield scaffold)`. | **CONFIRMED scaffold / NEEDS VERIFICATION** |
| Is there related flat singular drift? | Yes. `schemas/contracts/v1/settlement/README.md` documents a compatibility lane with PROPOSED empty scaffolds. | **CONFIRMED** |

---

## Authority and placement

Current placement posture:

```text
schemas/contracts/v1/settlements-infrastructure/          # this flat compatibility guardrail
schemas/contracts/v1/domains/settlements-infrastructure/  # current canonical domain-lane signal
schemas/contracts/v1/domains/settlement/                  # singular compatibility index
schemas/contracts/v1/settlement/                          # flat singular compatibility index
schemas/contracts/v1/settlement/receipts/                 # receipt-schema guardrail
```

This README does not amend ADR-0001, Directory Rules, schema-home decisions, domain ownership, policy, validators, or release gates.

---

## Repo fit

```text
schemas/
└── contracts/
    └── v1/
        ├── settlements-infrastructure/
        │   └── README.md                         # this file; flat compatibility guardrail
        ├── domains/
        │   ├── settlements-infrastructure/
        │   │   └── README.md                     # current canonical domain-lane signal
        │   └── settlement/
        │       └── README.md                     # singular compatibility index
        ├── settlement/
        │   ├── README.md                         # flat singular compatibility index
        │   ├── fort_event.schema.json            # PROPOSED empty scaffold
        │   ├── dependency.schema.json            # PROPOSED empty scaffold
        │   ├── service_area.schema.json          # PROPOSED empty scaffold
        │   └── receipts/
        │       └── README.md                     # README-only receipt guardrail
        ├── receipts/
        ├── evidence/
        ├── review/
        ├── release/
        └── policy/
```

---

## Current inventory

| Path | Current posture | Notes |
|---|---|---|
| `schemas/contracts/v1/settlements-infrastructure/README.md` | **CONFIRMED present** | Empty file expanded by this README. |
| `schemas/contracts/v1/settlements-infrastructure/*.schema.json` | **Not found in current search** | Do not create here without placement review. |
| `schemas/contracts/v1/domains/settlements-infrastructure/README.md` | **Canonical domain-lane signal / PROPOSED scaffold** | Current domain schema home signal; still scaffold maturity. |
| `schemas/contracts/v1/settlement/README.md` | **Compatibility index** | Flat singular lane with three PROPOSED empty scaffolds. |
| `schemas/contracts/v1/settlement/receipts/README.md` | **README-only guardrail** | Receipt shape guardrail; not emitted receipt storage. |

---

## What belongs here

- This README.
- Compatibility notes for this flat path.
- Migration notes if this path is retained, retired, or made a profile lane.
- Pointers to canonical and compatibility schema surfaces.
- Future schema files only after accepted ADR or migration review.

---

## What does not belong here

- New canonical schema families while the domain lane remains the canonical signal.
- Emitted records, lifecycle data, proof outputs, catalog records, release records, policy decisions, EvidenceBundles, public artifacts, or generated summaries.
- Contract prose beyond README boundary notes.
- Validator code, packages, pipelines, runtime code, UI/API implementation, or map artifacts.
- Claims that an object is true, reviewed, policy-safe, release-approved, or public-ready merely because it validates against a schema in this folder.

---

## Compatibility rules

| Rule | Requirement |
|---|---|
| Keep canonical signal visible | Prefer `domains/settlements-infrastructure/` unless an ADR or migration note changes placement. |
| Shape is not truth | Schema validation constrains shape; it does not prove claims. |
| Roots remain separate | Schemas, contracts, policy, evidence, review, release, data, fixtures, tests, and pipelines keep separate authority. |
| No parallel authority | Equivalent shapes must not drift across flat, domain, singular, and receipt lanes without migration notes. |

---

## Promotion checklist

This flat path should not advance beyond compatibility posture unless:

- [ ] Placement is resolved.
- [ ] Naming relationship to `settlement` is documented.
- [ ] Paired semantic contracts exist or approved profiles are documented.
- [ ] Required fields are defined for any schema added here.
- [ ] Valid and invalid fixtures exist.
- [ ] Validators and CI coverage exist.
- [ ] Migration notes exist for overlapping surfaces.

---

## Validation

```bash
find schemas/contracts/v1/settlements-infrastructure -maxdepth 4 -type f | sort

find schemas/contracts/v1 -maxdepth 6 -type f \
  | grep -Ei 'settlement|settlements-infrastructure|receipt|review|release|policy|evidence' \
  | sort

find schemas/contracts/v1/settlements-infrastructure -name '*.json' -print0 \
  | xargs -0 -r -I{} python -m json.tool {} >/dev/null

python tools/validate_all.py || true
pytest tests/schemas tests/contract tests/policy tests/release || true
```

Replace `|| true` with fail-closed CI behavior once validator and test paths are confirmed.

---

## Rollback

Rollback for this README is ordinary Git rollback: revert the commit that changed `schemas/contracts/v1/settlements-infrastructure/README.md`.

Future schema rollback must restore `$id`, `$ref`, contracts, fixtures, validators, registry records, CI paths, and downstream consumers.

---

## Open questions

| Question | Status | Owner |
|---|---|---|
| Should this flat path remain empty, become a redirect/index, host shared profiles, or be retired? | **NEEDS VERIFICATION / ADR-sensitive** | Schema steward + Directory steward |
| Should canonical schemas live only under `schemas/contracts/v1/domains/settlements-infrastructure/`? | **NEEDS VERIFICATION** | Domain steward + Schema steward |
| How should flat singular `settlement/` scaffolds be reconciled? | **NEEDS VERIFICATION** | Settlement steward + Schema steward |

---

## Maintainer notes

- Keep this folder in compatibility posture until schema-home placement is resolved.
- Do not add canonical schemas here while `domains/settlements-infrastructure/` remains the canonical signal unless ADR or migration notes explicitly allow it.
- Keep emitted records and release records outside `schemas/`.
