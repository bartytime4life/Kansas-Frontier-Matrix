# `schemas/contracts/v1/people/` — People Schema Alias Guardrail

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-people-readme
title: schemas/contracts/v1/people/ — People Schema Alias Guardrail
type: readme; schema-alias-index; placement-guardrail; people-identity-boundary
authority_class: alias-guardrail
version: v0.1
status: draft; empty-alias-index; top-level-home-unsettled; people-domain-bridge-present; people-dna-land-domain-present; restricted-review; no-current-root-schema-files-found; do-not-promote-without-ADR; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — People domain steward
  - OWNER_TBD — People/DNA/Land domain steward
  - OWNER_TBD — Identity-resolution steward
  - OWNER_TBD — Privacy steward
  - OWNER_TBD — Consent steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Docs steward
created: NEEDS VERIFICATION — empty README existed before v0.1 expansion
updated: 2026-07-04
policy_label: restricted-review; schemas; contracts-v1; people; alias-guardrail; people-dna-land; identity; consent; privacy; evidence-bound; release-gated; no-parallel-authority
tags: [kfm, schemas, contracts, v1, people, people-dna-land, identity, consent, privacy, restricted-review, alias, placement-guardrail, no-parallel-authority]
related:
  - ../README.md
  - ../domains/README.md
  - ../domains/people/README.md
  - ../domains/people/dna/README.md
  - ../domains/people-dna-land/README.md
  - ../domains/people-dna-land/people/README.md
  - ../domains/people-dna-land/genealogy/README.md
  - ../domains/people-dna-land/land-ownership/README.md
  - ../../../../contracts/domains/people/
  - ../../../../contracts/domains/people-dna-land/
  - ../../../../docs/domains/people-dna-land/
  - ../../../../policy/
  - ../../../../fixtures/domains/people-dna-land/
  - ../../../../tests/domains/people-dna-land/
  - ../../../../release/candidates/people-dna-land/
notes:
  - "Expanded from an empty file at schemas/contracts/v1/people/README.md."
  - "Current GitHub search did not surface schema files directly under schemas/contracts/v1/people/ beyond this README in the current check."
  - "schemas/contracts/v1/domains/people/README.md exists as a short-segment People schema bridge and is PROPOSED / CONFLICTED."
  - "schemas/contracts/v1/domains/people-dna-land/README.md exists as the broader People / DNA / Land schema index with restricted-review posture."
  - "schemas/contracts/v1/domains/people-dna-land/people/README.md exists as a CONFLICTED / transitional People sublane index and should not receive schema files merely because the folder exists."
  - "This top-level people path is an alias guardrail only; do not create canonical People schemas here without ADR, paired contracts, fixtures, validators, consent/policy review, and steward review."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![family](https://img.shields.io/badge/family-people-purple)
![posture](https://img.shields.io/badge/posture-alias__guardrail-orange)
![canonical](https://img.shields.io/badge/canonical-NEEDS__ADR-yellow)
![review](https://img.shields.io/badge/review-restricted--review-critical)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **Purpose.** `schemas/contracts/v1/people/` is an empty top-level alias guardrail for People-shaped schema work.
>
> **One-line boundary.** Current evidence places People schema discussion under conflicted domain bridge paths, especially `schemas/contracts/v1/domains/people/` and `schemas/contracts/v1/domains/people-dna-land/`; this top-level path must not become a parallel canonical People schema home without an accepted ADR or migration plan.

---

## Quick jumps

[Status](#status) · [Placement decision](#placement-decision) · [Repo fit](#repo-fit) · [Current inventory](#current-inventory) · [Related surfaced lanes](#related-surfaced-lanes) · [Candidate people shapes](#candidate-people-shapes) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [People guardrails](#people-guardrails) · [Migration rules](#migration-rules) · [Validation](#validation) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

| Question | Answer | Truth label |
|---|---|---|
| Does this README path exist? | Yes: `schemas/contracts/v1/people/README.md`. It was empty before this expansion. | **CONFIRMED** |
| Are schema files currently present directly under `schemas/contracts/v1/people/`? | Not found in the current GitHub search beyond this README. | **NEEDS VERIFICATION / search-limited** |
| Where is People schema discussion currently surfaced? | `schemas/contracts/v1/domains/people/`, `schemas/contracts/v1/domains/people-dna-land/`, and `schemas/contracts/v1/domains/people-dna-land/people/`. | **CONFIRMED path evidence** |
| Is the short `people` domain path canonical? | Not settled. It is marked a PROPOSED / CONFLICTED short-segment bridge. | **CONFIRMED conflict-visible** |
| Is the broader `people-dna-land` lane fully implemented? | Not proven. Its README says concrete schema inventory remains NEEDS VERIFICATION. | **CONFIRMED boundary** |
| Is this top-level path canonical? | Not proven. Treat this path as README-only until ADR or steward decision. | **NEEDS VERIFICATION / ADR-sensitive** |
| Can this path store personal payloads, consent records, identity stores, proofs, release records, public API artifacts, or generated answers? | No. This is schema documentation only, not a data, policy, consent, proof, release, runtime, or publication root. | **CONFIRMED boundary** |

> [!IMPORTANT]
> People-shaped schema work is restricted-review by default. Do not use this top-level folder to bypass the conflicted `people` / `people-dna-land` placement question, consent review, privacy review, source-role review, or release gates.

---

## Placement decision

Current placement posture:

```text
Empty top-level alias guardrail:
  schemas/contracts/v1/people/

Short People domain bridge:
  schemas/contracts/v1/domains/people/

Broader People / DNA / Land domain schema lane:
  schemas/contracts/v1/domains/people-dna-land/

Transitional People child lane under broader domain:
  schemas/contracts/v1/domains/people-dna-land/people/
```

Rationale:

- Domain schemas normally belong under `schemas/contracts/v1/domains/<domain>/...` unless an accepted exception says otherwise.
- The short `domains/people/` path is already marked a bridge and not confirmed canonical.
- The broader `domains/people-dna-land/` lane exists, but its child sublanes are transitional and its concrete schema inventory remains unverified.
- This top-level `people/` path would create a third possible People schema home if used for schemas now.
- Any future schema here must be justified by ADR, migration note, paired contracts, fixtures, validators, consent/policy review, and steward review.

---

## Repo fit

```text
schemas/
└── contracts/
    └── v1/
        ├── README.md
        ├── people/
        │   └── README.md                         # this file; top-level alias guardrail only
        └── domains/
            ├── people/
            │   ├── README.md                     # short-segment bridge; CONFLICTED
            │   └── dna/
            │       └── README.md                 # transitional bridge
            └── people-dna-land/
                ├── README.md                     # broader restricted-review schema index
                ├── people/
                │   └── README.md                 # transitional sublane index
                ├── genealogy/
                │   └── README.md                 # transitional sublane index
                └── land-ownership/
                    └── README.md                 # transitional sublane index

contracts/
├── domains/people/                                # short-segment semantic bridge; not schema shape
└── domains/people-dna-land/                       # broader semantic-contract lane

policy/
fixtures/
tests/
data/
release/
```

---

## Current inventory

| Path | Status | Note |
|---|---|---|
| `schemas/contracts/v1/people/README.md` | **CONFIRMED present** | Empty file expanded by this README. |
| `schemas/contracts/v1/people/*.schema.json` | **Not found in current search** | Do not create here without ADR, paired contracts, and validation plan. |
| `schemas/contracts/v1/domains/people/README.md` | **CONFIRMED inspected** | Short-segment People bridge; PROPOSED / CONFLICTED. |
| `schemas/contracts/v1/domains/people/dna/README.md` | **CONFIRMED surfaced** | DNA child bridge under short People path; transitional. |
| `schemas/contracts/v1/domains/people-dna-land/README.md` | **CONFIRMED inspected** | Broader People / DNA / Land schema index; restricted-review. |
| `schemas/contracts/v1/domains/people-dna-land/people/README.md` | **CONFIRMED inspected** | Transitional People sublane index; no schema files confirmed. |
| `schemas/contracts/v1/domains/people-dna-land/genealogy/README.md` | **CONFIRMED surfaced** | Transitional child index. |
| `schemas/contracts/v1/domains/people-dna-land/land-ownership/README.md` | **CONFIRMED surfaced** | Transitional child index. |

---

## Related surfaced lanes

| Path | Role signal | Posture |
|---|---|---|
| `schemas/contracts/v1/domains/people/` | Short People bridge for schema discussion. | **PROPOSED / CONFLICTED** |
| `schemas/contracts/v1/domains/people-dna-land/` | Broader People / DNA / Land schema lane. | **PROPOSED / restricted-review** |
| `schemas/contracts/v1/domains/people-dna-land/people/` | People sublane under broader domain. | **CONFLICTED / transitional** |
| `schemas/contracts/v1/people/` | Top-level alias guardrail. | **README-only** |

---

## Candidate people shapes

Candidate shapes below are placement-sensitive and require steward review, paired contracts, fixtures, validators, consent/policy review, and release review before promotion.

| Candidate schema | Purpose | Default posture |
|---|---|---|
| `person_assertion.schema.json` | Assertion-first person statement shape. | **PROPOSED / not created here** |
| `person_identity_candidate.schema.json` | Candidate identity record shape. | **PROPOSED / restricted-review** |
| `person_canonical.schema.json` | Canonical-person shape, if ever allowed by doctrine. | **NEEDS VERIFICATION / high-risk** |
| `name_assertion.schema.json` | Name assertion shape. | **PROPOSED / evidence-bound** |
| `life_event.schema.json` | Birth, death, marriage, residence, or other life-event assertion shape. | **PROPOSED / evidence-bound** |
| `identity_resolution_record.schema.json` | Evidence-bound identity resolution record. | **PROPOSED / consent-policy-sensitive** |
| `public_safe_person_summary.schema.json` | Public-safe summary descriptor. | **PROPOSED / release-gated** |

> [!CAUTION]
> Candidate names are proposals only. Do not treat them as repo files, accepted contracts, implementation proof, consent support, identity truth, or publication authority until created, paired, fixture-tested, and reviewed.

---

## What belongs here

- This README.
- Alias, deprecation, placement, and migration notes for the top-level `people/` path.
- Pointers to the accepted People schema home once settled.
- Drift notes explaining why schema files should not be added directly here without review.
- Links to paired contracts, policy references, consent references, fixtures, validators, schema registry records, release references, correction references, rollback references, and tests.

---

## What does not belong here

- Canonical People JSON Schema files unless an accepted ADR/migration authorizes this exact top-level path.
- Duplicate People schemas already proposed under `domains/people/` or `domains/people-dna-land/`.
- Sensitive or real-world personal payloads.
- Consent records, policy decisions, source registry records, lifecycle data, proof outputs, emitted receipts, catalog records, release records, public API/UI/map artifacts, generated-answer artifacts, person stores, identity-truth stores, relationship-truth stores, or public genealogy outputs.
- Semantic contract prose beyond README boundary notes.
- Validator code, packages, pipelines, runtime code, UI/API implementation, dashboards, screenshots, or generated summaries.
- Claims that a People schema is complete, consent-safe, identity-safe, release-approved, or public-ready merely because it validates against a schema.

---

## People guardrails

| Boundary | Requirement |
|---|---|
| Assertion-first | Treat person claims as evidence-bound assertions unless a reviewed contract says otherwise. |
| Identity is not truth by default | A candidate identity or resolved identity object is not sovereign identity truth by itself. |
| Consent matters | Consent-dependent surfaces must reference consent/policy posture before release or display. |
| Privacy fails closed | Living-person, DNA-derived, family-link, land-link, or identity-resolution outputs require restricted review by default. |
| Domain ownership remains unsettled | Do not silently choose `people/`, `domains/people/`, or `domains/people-dna-land/` as canonical without ADR/steward decision. |
| Evidence dependency | People claims need EvidenceBundle or equivalent support where claims depend on evidence. |
| Policy dependency | Public or semi-public People outputs need policy posture and release support. |
| Release dependency | Public People projections must be release-gated and rollback-aware. |
| No parallel authority | Do not maintain equivalent People schemas under top-level `people/` and domain lanes without a mirror/migration rule. |

---

## Migration rules

Do not move or duplicate People schemas into this top-level path unless a reviewed migration plan defines:

- source path;
- target path;
- owning root;
- reason for migration;
- chosen meaning of top-level `people`;
- schema `$id` changes;
- `$ref` and consumer updates;
- fixture and validator updates;
- schema registry updates;
- People and People/DNA/Land steward review;
- privacy, consent, and policy review;
- release and rollback impact;
- deprecation/mirror window;
- tests proving no parallel authority remains.

---

## Validation

Recommended local validation sequence:

```bash
# Confirm this top-level alias remains README-only unless authorized.
find schemas/contracts/v1/people -maxdepth 2 -type f | sort

# Inspect People-related schema lanes.
find schemas/contracts/v1/domains/people schemas/contracts/v1/domains/people-dna-land -maxdepth 4 -type f \
  | grep -Ei 'people|person|identity|dna|genealogy|land|ownership|README' \
  | sort

# Detect duplicate People schema authority.
find schemas/contracts/v1 -maxdepth 7 -type f \
  | grep -Ei 'person|people|identity|genealogy|dna|land_ownership|ownership' \
  | sort

# Validate JSON syntax for related schemas when present.
find schemas/contracts/v1/domains/people schemas/contracts/v1/domains/people-dna-land -name '*.schema.json' -print0 \
  | xargs -0 -r -I{} python -m json.tool {} >/dev/null

# Run project validators when available.
python tools/validate_all.py || true
pytest tests/schemas tests/contract tests/domains/people-dna-land tests/policy tests/release || true
```

Replace `|| true` with fail-closed CI behavior once validator and test paths are confirmed.

---

## Rollback

Rollback for this README is ordinary Git rollback: revert the commit that changed `schemas/contracts/v1/people/README.md`.

Rollback for future People schema changes requires checking every downstream reference:

1. Revert or migrate schema files.
2. Restore canonical `$id` and `$ref` targets.
3. Restore paired contract links.
4. Restore fixtures, validators, schema registry records, and CI paths.
5. Restore policy, consent, source-registry, evidence, release, correction, and receipt references.
6. Restore API/UI/MapLibre/Evidence Drawer consumers.
7. Preserve correction and rollback records if any public People surface was affected.

---

## Open questions

| Question | Status | Owner |
|---|---|---|
| Should `schemas/contracts/v1/people/` become an accepted top-level People schema family or remain README-only? | **NEEDS VERIFICATION / ADR-sensitive** | Schema steward + People steward + People/DNA/Land steward |
| Should accepted People schemas live under `domains/people/`, `domains/people-dna-land/`, a shared/common family, or another path? | **NEEDS VERIFICATION / migration-sensitive** | Schema steward + domain stewards |
| How should People, DNA, genealogy, land-link, and identity-resolution schema surfaces be separated? | **NEEDS VERIFICATION / policy-sensitive** | Privacy steward + Consent steward + Policy steward |
| Which contract lane owns neutral People schema semantics? | **NEEDS VERIFICATION** | Contract steward |
| Which fixtures prove assertion-first, consent-aware, restricted-review behavior? | **NEEDS VERIFICATION** | Validation steward |
| Which People-derived summaries are safe for public API/MapLibre/Focus Mode use? | **NEEDS VERIFICATION / release-gated** | Release steward + Policy steward |

---

## Maintainer notes

- Keep this path README-only until the People schema-home decision is resolved.
- Prefer references to domain-owned assertions, evidence bundles, consent posture, and policy records over copied personal fields.
- Do not let this top-level lane duplicate `domains/people/` or `domains/people-dna-land/` schema authority.
- Preserve restricted-review, assertion-first semantics, consent, privacy, evidence, policy, release, correction, and rollback boundaries for every People surface.
