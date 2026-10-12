# `schemas/contracts/v1/joins/hydrology_hazards/` — Hydrology–Hazards Join Schema Guardrail

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-joins-hydrology-hazards-readme
title: schemas/contracts/v1/joins/hydrology_hazards/ — Hydrology–Hazards Join Schema Guardrail
type: readme; join-schema-index; cross-domain-guardrail; hydrology-hazards-boundary
authority_class: join-schema-guardrail
version: v0.1
status: draft; empty-join-lane; hydrology-domain-present; hazards-domain-present; no-current-join-schema-files-found; do-not-promote-without-ADR; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Hydrology domain steward
  - OWNER_TBD — Hazards domain steward
  - OWNER_TBD — Join steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Freshness steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Docs steward
created: NEEDS VERIFICATION — empty README existed before v0.1 expansion
updated: 2026-07-04
policy_label: public; schemas; contracts-v1; joins; hydrology-hazards; cross-domain; freshness-aware; evidence-bound; release-gated; rollback-aware; no-parallel-authority
tags: [kfm, schemas, contracts, v1, joins, hydrology, hazards, hydrology-hazards, watershed, huc, gauge, hydrograph, flow-observation, nfhl-zone, hazard-context, cross-domain, join-lane, no-parallel-authority]
related:
  - ../../README.md
  - ../README.md
  - ../../domains/README.md
  - ../../domains/hydrology/README.md
  - ../../domains/hydrology/huc_unit.schema.json
  - ../../domains/hydrology/watershed.schema.json
  - ../../domains/hydrology/nfhl_zone.schema.json
  - ../../domains/hydrology/gauge_site.schema.json
  - ../../domains/hydrology/hydrograph.schema.json
  - ../../domains/hydrology/flow_observation.schema.json
  - ../../domains/hazards/README.md
  - ../../domains/hazards/source_descriptor.schema.json
  - ../../domains/hazards/decision_envelope.schema.json
  - ../../domains/hazards/hazards_decision_envelope.schema.json
  - ../../../../contracts/domains/hydrology/
  - ../../../../contracts/domains/hazards/
  - ../../../../docs/domains/hydrology/
  - ../../../../docs/domains/hazards/
  - ../../../../policy/domains/hydrology/
  - ../../../../policy/domains/hazards/
  - ../../../../fixtures/domains/hydrology/
  - ../../../../fixtures/domains/hazards/
  - ../../../../tests/domains/hydrology/
  - ../../../../tests/domains/hazards/
notes:
  - "Expanded from an empty file at schemas/contracts/v1/joins/hydrology_hazards/README.md."
  - "Current GitHub search did not surface schema files directly under this join lane beyond this README in the current check."
  - "Hydrology domain schema files were surfaced under schemas/contracts/v1/domains/hydrology/."
  - "Hazards domain schema files were surfaced under schemas/contracts/v1/domains/hazards/."
  - "This README is a join-placement guardrail only; do not create canonical join schemas here without ADR, paired contracts, fixtures, validators, and steward review."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![family](https://img.shields.io/badge/family-joins-purple)
![join](https://img.shields.io/badge/join-hydrology--hazards-blue)
![posture](https://img.shields.io/badge/posture-guardrail-orange)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **Purpose.** `schemas/contracts/v1/joins/hydrology_hazards/` is an empty guardrail README for a possible Hydrology–Hazards join schema lane.
>
> **One-line boundary.** This path may only define join-shape contracts if placement is accepted; it must not replace `schemas/contracts/v1/domains/hydrology/` or `schemas/contracts/v1/domains/hazards/`.

---

## Quick jumps

[Status](#status) · [Placement decision](#placement-decision) · [Repo fit](#repo-fit) · [Current inventory](#current-inventory) · [Related surfaced lanes](#related-surfaced-lanes) · [Candidate join shapes](#candidate-join-shapes) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Join guardrails](#join-guardrails) · [Migration rules](#migration-rules) · [Validation](#validation) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

| Question | Answer | Truth label |
|---|---|---|
| Does this README path exist? | Yes: `schemas/contracts/v1/joins/hydrology_hazards/README.md`. It was empty before this expansion. | **CONFIRMED** |
| Are schema files currently present under this join lane? | Not found in the current GitHub search beyond this README. | **NEEDS VERIFICATION / search-limited** |
| Are Hydrology and Hazards domain schema lanes present? | Yes. Both domain schema lanes were surfaced by search. | **CONFIRMED path evidence** |
| Is this join lane canonical? | Not proven. Treat as guardrail/index only until ADR or steward decision. | **NEEDS VERIFICATION / ADR-sensitive** |
| Can this lane store joined data, lifecycle records, alerts, or released outputs? | No. This path is schema documentation only, not lifecycle data, emitted records, release records, public artifacts, or operational guidance. | **CONFIRMED boundary** |

> [!IMPORTANT]
> A Hydrology–Hazards join schema should describe relationship shape. It must not collapse Hydrology-owned water, watershed, gauge, hydrograph, or flow meaning into Hazards-owned event/context/decision meaning, and it must not become an operational alert or public-safety authority.

---

## Placement decision

Current placement posture:

```text
Requested join guardrail:
  schemas/contracts/v1/joins/hydrology_hazards/

Hydrology domain schema lane:
  schemas/contracts/v1/domains/hydrology/

Hazards domain schema lane:
  schemas/contracts/v1/domains/hazards/
```

Rationale:

- Domain schemas normally belong under `schemas/contracts/v1/domains/<domain>/...`.
- Hydrology schema search surfaced domain-owned shapes such as `huc_unit`, `watershed`, `nfhl_zone`, `gauge_site`, `hydrograph`, `flow_observation`, and support schemas.
- Hazards schema search surfaced domain-owned shapes such as `source_descriptor`, `decision_envelope`, `hazards_decision_envelope`, release/rollback/correction support schemas, and receipt/support schemas.
- This join lane may be useful for neutral relationship shapes, but it is not confirmed as accepted in this session.
- Any future schema here must be paired with contracts, fixtures, validators, registry entries, and review across both domains.

---

## Repo fit

```text
schemas/
└── contracts/
    └── v1/
        ├── README.md
        ├── joins/
        │   └── hydrology_hazards/
        │       └── README.md                     # this file; join guardrail only
        └── domains/
            ├── hydrology/
            │   ├── README.md
            │   ├── huc_unit.schema.json
            │   ├── watershed.schema.json
            │   ├── nfhl_zone.schema.json
            │   ├── gauge_site.schema.json
            │   └── hydrograph.schema.json
            └── hazards/
                ├── README.md
                ├── receipts/
                │   └── README.md
                ├── source_descriptor.schema.json
                ├── decision_envelope.schema.json
                └── hazards_decision_envelope.schema.json

contracts/
├── domains/hydrology/                             # semantic meaning; not machine shape
└── domains/hazards/                               # semantic meaning; not machine shape

policy/
fixtures/
tests/
release/
```

---

## Current inventory

| Path | Status | Note |
|---|---|---|
| `schemas/contracts/v1/joins/hydrology_hazards/README.md` | **CONFIRMED present** | Empty file expanded by this README. |
| `schemas/contracts/v1/joins/hydrology_hazards/*.schema.json` | **Not found in current search** | Do not create here without ADR, paired contracts, and validation plan. |
| `schemas/contracts/v1/domains/hydrology/README.md` | **CONFIRMED surfaced by search** | Hydrology domain schema lane. |
| `schemas/contracts/v1/domains/hazards/README.md` | **CONFIRMED surfaced by search** | Hazards domain schema lane. |
| Hydrology schema files | **CONFIRMED surfaced by search** | Includes watershed/HUC/gauge/hydrograph/flow/support schemas. |
| Hazards schema files | **CONFIRMED surfaced by search** | Includes source, decision, receipt, release, rollback, correction, and support schemas. |

---

## Related surfaced lanes

| Path | Role signal | Posture |
|---|---|---|
| `schemas/contracts/v1/domains/hydrology/` | Hydrology-owned machine shape lane. | **PROPOSED / active domain lane** |
| `schemas/contracts/v1/domains/hazards/` | Hazards-owned machine shape lane. | **PROPOSED / active domain lane** |
| `schemas/contracts/v1/domains/hazards/receipts/` | Hazards receipt schema child index. | **DRAFT index / not emitted receipt storage** |
| `schemas/contracts/v1/joins/hydrology_hazards/` | Possible neutral join schema lane. | **README-only guardrail** |

---

## Candidate join shapes

Candidate join schemas below require steward review, paired contracts, fixtures, validators, registry records, and release/policy review before promotion.

| Candidate schema | Purpose | Default posture |
|---|---|---|
| `hydrology_hazards_join.schema.json` | Generic relationship between Hydrology feature refs and Hazards context refs. | **PROPOSED / not created** |
| `watershed_hazard_context.schema.json` | Relationship shape between watershed/HUC refs and hazard context refs. | **PROPOSED / evidence-bound** |
| `gauge_hazard_context.schema.json` | Relationship shape between gauge/hydrograph refs and hazard context refs. | **PROPOSED / freshness-aware** |
| `nfhl_hazard_context.schema.json` | Relationship shape for Hydrology flood-context schemas and Hazards context schemas. | **PROPOSED / placement-sensitive** |
| `hydrology_hazards_release_projection.schema.json` | Public/release projection for already-governed join outputs. | **PROPOSED / release-gated** |

> [!CAUTION]
> Candidate names are proposals only. Do not treat them as repo files, accepted contracts, or implementation proof until created, paired, fixture-tested, and reviewed.

---

## What belongs here

- This README.
- Join schema placement notes for Hydrology–Hazards relationships.
- Future neutral join schema files if an accepted ADR or migration plan authorizes this lane.
- Links to paired contracts, fixtures, validators, schema registry records, policy references, release references, and tests.
- Drift notes preventing duplicate Hydrology or Hazards schema authority.

---

## What does not belong here

- Hydrology-owned canonical schemas.
- Hazards-owned canonical schemas.
- Semantic contract prose.
- Policy rules, exposure decisions, release decisions, or operational guidance.
- Lifecycle data, joined datasets, source records, catalog records, triplets, receipt instances, proof outputs, release records, correction notices, rollback cards, or public artifacts.
- Validator code, packages, pipelines, runtime code, UI/API implementation, map tiles, dashboards, screenshots, or generated summaries.
- Claims that a join is valid, complete, true, current, safe, or public-ready merely because it validates against a schema.

---

## Join guardrails

| Boundary | Requirement |
|---|---|
| Domain ownership | Hydrology and Hazards keep their own canonical shapes and semantic contracts. |
| Join neutrality | A join schema records relationship shape, not source truth for either side. |
| Reference discipline | Use stable references to domain-owned objects rather than duplicating domain fields. |
| Time/freshness discipline | Join outputs should preserve source time, observation time, issue time, retrieval time, release time, and expiry where applicable. |
| Evidence dependency | Join outputs need EvidenceBundle or equivalent support where claims depend on evidence. |
| Policy dependency | Joins that affect release, access, or public display must carry policy posture. |
| Release dependency | Public join projections must be release-gated and rollback-aware. |
| No parallel authority | Do not maintain identical join schema definitions under `joins/` and either domain lane without a mirror/migration rule. |

---

## Migration rules

Do not move or duplicate join schemas into this path unless a reviewed migration plan defines:

- source path;
- target path;
- owning root;
- reason for migration;
- schema `$id` changes;
- `$ref` and consumer updates;
- fixture and validator updates;
- schema registry updates;
- Hydrology and Hazards steward review;
- freshness and policy review;
- release and rollback impact;
- deprecation/mirror window;
- tests proving no parallel authority remains.

---

## Validation

Recommended local validation sequence:

```bash
# Confirm this join lane remains README-only unless authorized.
find schemas/contracts/v1/joins/hydrology_hazards -maxdepth 2 -type f | sort

# Inspect Hydrology/Hazards related schema lanes.
find schemas/contracts/v1/domains/hydrology schemas/contracts/v1/domains/hazards -maxdepth 4 -type f \
  | grep -Ei 'huc|watershed|nfhl|gauge|hydrograph|flow|hazard|decision|receipt|README' \
  | sort

# Detect duplicate hydrology-hazards join authority.
find schemas/contracts/v1 -maxdepth 6 -type f \
  | grep -Ei 'hydrology.*hazards|hazards.*hydrology|watershed.*hazard|gauge.*hazard|nfhl.*hazard' \
  | sort

# Validate JSON syntax for related domain schemas.
find schemas/contracts/v1/domains/hydrology schemas/contracts/v1/domains/hazards -name '*.schema.json' -print0 \
  | xargs -0 -r -I{} python -m json.tool {} >/dev/null

# Run project validators when available.
python tools/validate_all.py || true
pytest tests/schemas tests/contract tests/domains/hydrology tests/domains/hazards tests/policy || true
```

Replace `|| true` with fail-closed CI behavior once validator and test paths are confirmed.

---

## Rollback

Rollback for this README is ordinary Git rollback: revert the commit that changed `schemas/contracts/v1/joins/hydrology_hazards/README.md`.

Rollback for future join schema changes requires checking every downstream reference:

1. Revert or migrate schema files.
2. Restore canonical `$id` and `$ref` targets.
3. Restore paired contract links.
4. Restore fixtures, validators, schema registry records, and CI paths.
5. Restore Hydrology, Hazards, policy, evidence, release, and receipt references.
6. Restore API/UI/MapLibre/Evidence Drawer consumers.
7. Preserve correction and rollback records if any public join surface was affected.

---

## Open questions

| Question | Status | Owner |
|---|---|---|
| Should Hydrology–Hazards relationships live under `joins/`, a Hydrology extension, a Hazards extension, or another cross-domain lane? | **NEEDS VERIFICATION / ADR-sensitive** | Schema steward + Hydrology steward + Hazards steward |
| Should the slug be `hydrology_hazards`, `hydrology-hazards`, `hazards-hydrology`, or another convention? | **NEEDS VERIFICATION / ADR-sensitive** | Schema steward + Join steward |
| Which contract lane should own neutral join semantics? | **NEEDS VERIFICATION** | Contract steward |
| Which fixtures prove that joins do not duplicate domain-owned fields? | **NEEDS VERIFICATION** | Validation steward |
| Which join projections are safe for public API/MapLibre/Focus Mode use? | **NEEDS VERIFICATION / release-gated** | Release steward + Policy steward |

---

## Maintainer notes

- Keep this path README-only until the join-home decision is resolved.
- Prefer references to Hydrology and Hazards domain objects over copied fields.
- Do not let this join lane duplicate Hydrology or Hazards schema authority.
- Preserve evidence, time/freshness, ownership, policy, release, correction, and rollback boundaries for all Hydrology–Hazards join surfaces.
