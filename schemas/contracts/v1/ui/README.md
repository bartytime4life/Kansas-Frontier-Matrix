# `schemas/contracts/v1/ui/` — UI Schema Family Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-ui-readme
title: schemas/contracts/v1/ui/ — UI Schema Family Index
type: readme; schema-family-index; ui-schema-boundary; governed-ui-guardrail
authority_class: schema-family-index
version: v0.2
status: draft; ui-family-present; mixed-maturity-schemas-present; runtime-map-exposure-overlap; PROPOSED; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — UI steward
  - OWNER_TBD — Map/UI steward
  - OWNER_TBD — Runtime steward
  - OWNER_TBD — Exposure steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Docs steward
created: NEEDS VERIFICATION — short stub existed before v0.2 expansion
updated: 2026-07-04
policy_label: public; schemas; contracts-v1; ui; governed-ui; map-context; evidence-drawer; citation-validation; focus; story; trust-badge; evidence-bound; policy-aware; release-gated; no-parallel-authority
tags: [kfm, schemas, contracts, v1, ui, governed-ui, focus-request, focus-response, ui-event, story-node, story-manifest, trust-badge, map-context, evidence-drawer, citation-validation, no-parallel-authority]
related:
  - ../README.md
  - ./ui_event.schema.json
  - ./story_node.schema.json
  - ./focus_request.schema.json
  - ./focus_response.schema.json
  - ./story_manifest.schema.json
  - ./trust_badge_state.schema.json
  - ./map_context_envelope.schema.json
  - ./evidence_drawer_payload.schema.json
  - ./citation_validation_report.schema.json
  - ../runtime/README.md
  - ../exposure/README.md
  - ../map/README.md
  - ../layers/README.md
  - ../evidence/README.md
  - ../policy/README.md
  - ../review/README.md
  - ../release/README.md
  - ../../../../contracts/ui/
  - ../../../../policy/ui/
  - ../../../../fixtures/ui/
  - ../../../../tools/validators/ui/
  - ../../../../tests/
notes:
  - "Expanded from a short stub at schemas/contracts/v1/ui/README.md."
  - "Current GitHub search surfaced nine schema files directly under schemas/contracts/v1/ui/."
  - "Opened UI schemas show mixed maturity: several PROPOSED stubs with id/spec_hash/version fields and one empty map-context scaffold."
  - "Runtime, exposure, and map schema README boundaries were inspected as adjacent lanes."
  - "This folder defines UI object shapes only; it is not UI implementation code, runtime execution authority, map rendering, exposure authority, emitted record storage, or release authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![family](https://img.shields.io/badge/family-ui-blueviolet)
![maturity](https://img.shields.io/badge/maturity-mixed-orange)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **Purpose.** `schemas/contracts/v1/ui/` is the machine-checkable schema family for governed UI object shapes such as UI events, focus request/response objects, story surfaces, trust badges, map context envelopes, evidence drawer payloads, and citation validation reports.
>
> **One-line boundary.** UI schemas define object shape only. They do not implement UI, render MapLibre, execute runtime behavior, decide exposure, replace evidence, or approve release.

---

## Quick jumps

[Status](#status) · [Authority and placement](#authority-and-placement) · [Repo fit](#repo-fit) · [Current inventory](#current-inventory) · [Known overlap and drift risks](#known-overlap-and-drift-risks) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [UI-family rules](#ui-family-rules) · [Promotion checklist](#promotion-checklist) · [Validation](#validation) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

| Question | Answer | Truth label |
|---|---|---|
| Does this README path exist? | Yes. It was a short stub before this expansion. | **CONFIRMED** |
| Are UI schema files present in this folder? | Yes. Search surfaced nine schema files directly under `schemas/contracts/v1/ui/`. | **CONFIRMED path presence** |
| Are all UI schemas field-complete? | Not proven. Opened examples are PROPOSED stubs: several contain only `spec_hash`, `id`, and `version`, while `map_context_envelope.schema.json` has empty `properties`. | **CONFIRMED mixed maturity / NEEDS VERIFICATION** |
| Is this folder UI implementation authority? | No. This folder is under `schemas/` and may only define machine-checkable shape. | **CONFIRMED boundary** |
| Can UI schema validation approve public display or exposure? | No. Display/exposure depends on evidence, policy, runtime, review, release, and governed UI/API behavior outside this folder. | **CONFIRMED boundary** |

> [!IMPORTANT]
> A schema-valid UI object is not a rendered UI, a safe public surface, or a released artifact. It is only a shaped payload candidate until governed evidence, policy, runtime, release, and implementation boundaries are satisfied where applicable.

---

## Authority and placement

This folder is under the schema responsibility root:

```text
schemas/contracts/v1/ui/
```

Adjacent authority remains separate:

- `contracts/ui/` owns semantic meaning where paired contract docs exist.
- `policy/ui/` owns UI policy posture where implemented.
- `schemas/contracts/v1/runtime/` owns runtime-support object shapes.
- `schemas/contracts/v1/exposure/` owns exposure/cross-boundary object shapes where accepted.
- `schemas/contracts/v1/map/` and `schemas/contracts/v1/layers/` own map/layer object shapes where accepted.
- `schemas/contracts/v1/evidence/` owns evidence object shapes.
- `schemas/contracts/v1/policy/` owns policy-decision and sensitivity machine shapes.
- `schemas/contracts/v1/review/` and `schemas/contracts/v1/release/` own review/release support shapes where accepted.
- `fixtures/` and `tests/` prove examples and behavior where present.
- UI application code, API handlers, MapLibre runtime, and emitted UI/runtime records live outside this folder.

This README does not amend ADR-0001, Directory Rules, UI contracts, runtime contracts, exposure rules, policy docs, validators, public API behavior, or release gates.

---

## Repo fit

```text
schemas/
└── contracts/
    └── v1/
        ├── ui/
        │   ├── README.md
        │   ├── ui_event.schema.json
        │   ├── story_node.schema.json
        │   ├── focus_request.schema.json
        │   ├── focus_response.schema.json
        │   ├── story_manifest.schema.json
        │   ├── trust_badge_state.schema.json
        │   ├── map_context_envelope.schema.json
        │   ├── evidence_drawer_payload.schema.json
        │   └── citation_validation_report.schema.json
        ├── runtime/
        ├── exposure/
        ├── map/
        ├── layers/
        ├── evidence/
        ├── policy/
        ├── review/
        └── release/

contracts/ui/
policy/ui/
fixtures/ui/
tools/validators/ui/
tests/
```

---

## Current inventory

| File | Current posture | Shape maturity | Notes |
|---|---|---|---|
| `ui_event.schema.json` | **PROPOSED** | Minimal stub | Has `$id`, `x-kfm` links to contract, fixtures, validator, and policy; properties include `spec_hash`, `id`, and `version`; only `id` is required; `additionalProperties: true`. |
| `story_node.schema.json` | **PROPOSED** | NEEDS VERIFICATION | Present by search; not opened in this pass. |
| `focus_request.schema.json` | **PROPOSED** | Minimal stub | Has `$id`, `x-kfm` links to contract, fixtures, validator, and policy; properties include `spec_hash`, `id`, and `version`; only `id` is required; `additionalProperties: true`. |
| `focus_response.schema.json` | **PROPOSED** | NEEDS VERIFICATION | Present by search; not opened in this pass. |
| `story_manifest.schema.json` | **PROPOSED** | NEEDS VERIFICATION | Present by search; not opened in this pass. |
| `trust_badge_state.schema.json` | **PROPOSED** | NEEDS VERIFICATION | Present by search; not opened in this pass. |
| `map_context_envelope.schema.json` | **PROPOSED** | Empty scaffold | Empty `properties`; `additionalProperties: true`; source docs include several domain map/API contracts; `contract_doc: null`. |
| `evidence_drawer_payload.schema.json` | **PROPOSED** | Minimal stub | Has `$id`, `x-kfm` links to contract, fixtures, validator, and policy; properties include `spec_hash`, `id`, and `version`; only `id` is required; `additionalProperties: true`. |
| `citation_validation_report.schema.json` | **PROPOSED** | Minimal stub | Has `$id`, `x-kfm` links to contract, fixtures, validator, and policy; properties include `spec_hash`, `id`, and `version`; only `id` is required; `additionalProperties: true`. |

---

## Known overlap and drift risks

| Risk | Evidence signal | Required posture |
|---|---|---|
| UI vs runtime overlap | UI has `evidence_drawer_payload`, while runtime also has an evidence-drawer payload schema surface. | **Needs placement/profile clarity** |
| UI vs map overlap | UI has `map_context_envelope`, while map/layer families govern map-facing objects. | **Keep map rendering and layer publication separate** |
| UI vs exposure overlap | UI surfaces can become public-facing, while exposure decisions belong to policy/exposure/release-governed lanes. | **Do not treat UI shape as exposure approval** |
| Mixed maturity | Some UI files are minimal stubs and one opened file is empty. | **Do not imply completed UI contract family** |
| Contract/validator links need verification | Several opened schemas point to `contracts/ui/`, `fixtures/ui/`, `tools/validators/ui/`, and `policy/ui/`. | **Verify before promotion** |
| Namespace drift | UI schemas use both `https://schemas.kfm.local/contracts/...` and `kfm://schemas/contracts/...` `$id` patterns. | **NEEDS VERIFICATION** |

---

## What belongs here

- This README.
- Machine-checkable JSON Schema files for UI object shapes when accepted.
- UI schema index notes and drift notes.
- Migration notes for UI/runtime/exposure/map overlap.
- Links to paired UI contracts, fixtures, validators, policy references, evidence references, release references, correction references, rollback references, and tests.

---

## What does not belong here

- UI implementation code, frontend components, API handlers, runtime code, MapLibre code, map tiles, style files, dashboards, screenshots, generated UI outputs, or public artifacts.
- Lifecycle data, emitted UI events, runtime records, source records, catalog records, proof outputs, receipt instances, EvidenceBundles, policy decisions, release records, correction records, or rollback records.
- Contract prose beyond README boundary notes.
- Claims that a UI surface is rendered, safe for public display, evidence-supported, policy-approved, release-approved, or complete merely because a payload validates against a UI schema.

---

## UI-family rules

| Rule | Requirement |
|---|---|
| Shape is not implementation | Schema validation constrains object shape; it does not implement UI behavior. |
| UI is not exposure approval | A UI-shaped payload must still pass policy, evidence, review, release, and exposure checks where public or semi-public display is involved. |
| Evidence remains separate | Evidence drawer payloads may reference evidence, but do not replace EvidenceBundles. |
| Runtime remains separate | UI events and focus objects may interact with runtime envelopes, but do not execute runtime behavior. |
| Map remains separate | Map context objects do not render MapLibre, publish tiles, or replace map/layer schemas. |
| Contracts explain meaning | Accepted UI schemas need paired semantic contracts or approved profiles. |
| Fixtures prove behavior | Accepted schemas need valid and invalid fixtures plus validator coverage. |
| No parallel authority | Equivalent UI, runtime, exposure, map, evidence, policy, and release shapes must not drift across roots without migration notes. |

---

## Promotion checklist

A UI schema should not advance beyond `PROPOSED` unless:

- [ ] Paired semantic contract exists or approved profile is documented.
- [ ] `$id` namespace convention is settled.
- [ ] Required fields are defined beyond placeholder fields where needed.
- [ ] UI/runtime/exposure/map overlap is resolved.
- [ ] Evidence and citation reference requirements are defined where display depends on evidence.
- [ ] Policy/exposure requirements are defined where UI output can cross a public or semi-public boundary.
- [ ] Valid fixtures exist.
- [ ] Invalid fixtures exist.
- [ ] Validators exist and paths are correct.
- [ ] CI/schema-test coverage exists.
- [ ] Migration notes exist for duplicate or overlapping schema surfaces.

---

## Validation

```bash
find schemas/contracts/v1/ui -maxdepth 3 -type f | sort

find schemas/contracts/v1/ui -name '*.json' -print0 \
  | xargs -0 -r -I{} python -m json.tool {} >/dev/null

find schemas/contracts/v1/ui schemas/contracts/v1/runtime schemas/contracts/v1/exposure schemas/contracts/v1/map schemas/contracts/v1/layers -maxdepth 4 -type f 2>/dev/null \
  | grep -Ei 'ui|focus|story|evidence_drawer|citation|map_context|runtime|exposure|layer|map' \
  | sort

python tools/validate_all.py || true
pytest tests/schemas tests/contract || true
```

Replace `|| true` with fail-closed CI behavior once validator and test paths are confirmed.

---

## Rollback

Rollback for this README is ordinary Git rollback: revert the commit that changed `schemas/contracts/v1/ui/README.md`.

Future schema rollback must restore `$id`, `$ref`, paired contracts, fixtures, validators, registry records, CI paths, and downstream consumers.

---

## Open questions

| Question | Status | Owner |
|---|---|---|
| Which UI schemas are real contract surfaces versus placeholders? | **NEEDS VERIFICATION** | UI steward + Schema steward |
| Should evidence drawer payload live under UI, runtime, or a shared profile? | **NEEDS VERIFICATION / placement-sensitive** | UI steward + Runtime steward + Evidence steward |
| Should map context envelope live under UI, map, runtime, or exposure? | **NEEDS VERIFICATION / placement-sensitive** | UI steward + Map/UI steward + Runtime steward |
| Which fixtures prove focus request/response and story surfaces without implying public release? | **NEEDS VERIFICATION** | Validation steward |
| Which UI schemas need exposure/release policy gates before public display? | **NEEDS VERIFICATION** | UI steward + Policy steward + Release steward |

---

## Maintainer notes

- Keep this folder focused on UI schema shape, not UI implementation.
- Resolve UI/runtime/exposure/map overlaps before promoting duplicated or adjacent shapes.
- Keep emitted records, public artifacts, validators, runtime code, and release records outside this folder.
